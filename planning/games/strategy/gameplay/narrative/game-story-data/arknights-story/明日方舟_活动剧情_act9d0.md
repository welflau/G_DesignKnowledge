# 明日方舟 · 活动剧情 · act9d0（15段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act9d0」完整剧情脚本（15个文件，1902行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act9d0
- 脚本文件数：15

### level_act9d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[Blocker(fadetime=1,block=true)]
[Dialog(fadetime=2,block=true)]
是我。
已经抵达目标地点，肉眼确认到信号烟坐标。
......很久没有和同行打交道，稍微有点损失。
但是他们在地下发报站藏着的物资也很充裕，好歹能挽回一些。
嗯，是的，斥候可以先出发了。
我会尽快。
......对了，有个意料之外的损失。
W死了。
[PlaySound(key="$transmission", volume=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_battlefield",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Character(name="avg_npc_052",name2="avg_npc_047",fadetime=1.5,block=true)]
[delay(time=1.5)]
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......
[name="伊内丝"]  ......说的那么惨不忍睹，结果还不是四肢健全地回来了吗？
[name="伊内丝"]  还是说，你只不过是想用苦肉计邀功？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  那么你也大可不必离开营地来接应我们，你不需要这么担心。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  我不担心任何人，别自作多情。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  如果不是W殿后为我们创造机会，我们谁也逃不出来。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......
[name="伊内丝"]  ......什么时候的事？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  两小时前，通讯被隔断的时候，小队遭到了埋伏。
[name="赫德雷"]  W摧毁了废墟，然后我们逃了出来，他死战到了最后一刻。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  可惜。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......的确，如果他能活着回到营地，按人头来算，他会超过我成为这里最值钱的雇佣兵。
[name="赫德雷"]  算了，事到如今说这些也没意义，至少他不用再打仗了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  敌人已经撤退，要去回收吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  不可能，重新深入的风险太大，谁也承担不起。
[name="赫德雷"]  怎么？莫非你们关系很好？我怎么不知道？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  我只是可惜他身上的战利品。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  没什么特别的，有些人的藏品比他丰富得多。
[name="赫德雷"]  等这场战争结束，我们有的是机会重操旧业。
[name="赫德雷"]  ......如果会结束的话。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  哼......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  互相安慰的话之后再说。日落前我们要离开这里，再停留下去会成为众矢之的。
[name="赫德雷"]  回营地去，立刻整队出发。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  哼——？
[name="伊内丝"]  你这是在命令我？赫德雷“副”队长？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......其他小队都失去联系，现在总指挥权轮替在我手上。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  我们平起平坐。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  唉......
[name="赫德雷"]  ......伊内丝，我们赶紧离开这里，回到据点，然后联系雇主，重新商谈一下报酬。
[name="赫德雷"]  这只是建议，不是命令，好吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  哼......
[name="伊内丝"]  W的死，能给我们加上多少筹码？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  很多。
[name="赫德雷"]  他是一名优秀的雇佣兵，明码标价的优秀。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  那至少他......不算白白送死。
[name="伊内丝"]  他最后有没有留下什么——
[dialog]
[stopmusic(fadetime=1)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ——安静。
[name="伊内丝"]  有人靠近，三点钟方向，不是我们的人......
[Character(name="avg_npc_047")]
[name="赫德雷"]  ......
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.7)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ——只有一个人，滚出来。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1)]
[name="衣衫褴褛的萨卡兹女性"]  ......
[Character(name="avg_npc_052")]
[name="伊内丝"]  萨卡兹......？本地人吗？
[name="伊内丝"]  不，不对，你手里拿着的是W的刀和铳......
[name="伊内丝"]  你是什么人？
[Character]
[name="衣衫褴褛的萨卡兹女性"]  ......
[Character(name="avg_npc_052")]
[name="伊内丝"]  不说话？那么，死吧。
[Character(name="avg_npc_047")]
[name="赫德雷"]  等等。
[name="赫德雷"]  她是跟着我们来的。
[Character]
[name="衣衫褴褛的萨卡兹女性"]  ......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......你放任她跟踪你？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我们的行进速度不慢，她在取得了W的遗物之后徒步跟上了我们，以她的身手，徒步。
[name="赫德雷"]  她是个“有经验”的萨卡兹，我想在撤离的时候也许会需要一个本地向导。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ——你在发什么疯？那不是更应该在这里杀了她吗？
[name="伊内丝"]  你要是想害死我们所有人，大可直接动手。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我怎么敢。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  那如果她是个刺客呢？如果她把我们带进布好的陷阱里呢？
[name="伊内丝"]  你知道卡兹戴尔有多少人想要你的脑袋吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  喔，有多少？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......你面前就有一个。
[name="伊内丝"]  你的头非常值钱，只是暂且被我保存在你的脖子上而已，别太自以为是。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  非常感谢你的勤俭，但是我也没有开玩笑。
[name="赫德雷"]  她冒险捡起了W的刀，还有那把铳，然后正大光明地站在我们的面前。
[name="赫德雷"]  你的法术可以感觉到，她有敌意吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......脑子正常的人都不会突然接受一个来路不明的萨卡兹。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  嗯，这就是你我不一样的地方了。
[name="赫德雷"]  一路上，我给过她很多次破绽，而她......向我扔了三次石子。
[name="赫德雷"]  很有趣的示好方法，不是吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......哈？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  按老规矩，也许我们应该给她一个机会。
[name="赫德雷"]  这场战役造成了不少位置的空缺，比起用招募的手段招来一些同样来历不明的萨卡兹，我宁可，自己挑选。
[Character]
[name="衣衫褴褛的萨卡兹女性"]  ......
[Character(name="avg_npc_052")]
[name="伊内丝"]  可她只是个外人，那套规矩也不该——
[name="伊内丝"]  ——啊，算了。
[name="伊内丝"]  十分钟后出发，我不在乎出发的是几个人。
[name="伊内丝"]  但如果我还要额外处理一具尸体——不管是谁的，都建议你动作快点。
[Dialog]
[Character(name="avg_npc_052")]
[delay(time=0.7)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(fadetime=1,block=true)]
[delay(time=2)]
[Character(name="avg_npc_047")]
[name="赫德雷"]  呵呵，真是没耐心。
[name="赫德雷"]  ......好了，你，认真听我说。
[Character]
[name="衣衫褴褛的萨卡兹女性"]  ......
[Character(name="avg_npc_047")]
[name="赫德雷"]  你拿着的是我们战友的遗物。
[name="赫德雷"]  放下这些东西，你可以活着离开这里，然后死

... (全文7293字符)
```

### level_act9d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_battlefield",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
数个月后
4:28  P.M.    天气/多云
卡兹戴尔东西部战场，军事缓冲区边缘
[Dialog]
[Character]
[Blocker(fadetime=2,block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
小小的伏击。
看来和你说的一样，的确有不少人盯着我的脑袋，真是头疼。
敌军人数很少，是打算迅速斩首撤离吧。
毕竟我们只有半支负责扫荡的小队，这的确是个千载难逢的机会，干掉我的机会。
......但是很可惜，这个“机会”是我故意留给他们的。
好了，回头见，去卡兹戴尔的信使就快回来了。
[dialog]
[PlaySound(key="$transmission", volume=1)]
[delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  ——
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  ......你在找什么？
[name="W"]  这具尸体......是刚才的刺客？
[Character(name="avg_npc_047")]
[name="赫德雷"]  ——有了。
[name="赫德雷"]  我就知道他会带在身上。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  这是......纸条？
[name="W"]  不，比起这个，你认识这个刺客？
[Character(name="avg_npc_047")]
[name="赫德雷"]  刺客，当然。
[name="赫德雷"]  我们有过合作，出生入死，几个月前我们还在疤痕商场欢庆过共同的胜利。
[name="赫德雷"]  他当时甚至还说，他愿意把他的女儿嫁给我。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  听着真蠢，既然都是雇佣兵，迟早不都会——
[Character(name="avg_npc_046")]
[name="W"]  ————
[name="W"]  ——等等，你总不能？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  不，我当然拒绝了。
[name="赫德雷"]  ......用别的理由。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  那上面写着什么？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  值得关注的东西，行情，报价，总之你也应该了解一下。
[Character(name="avg_npc_046")]
[name="W"]  ......
[name="W"]  ......这是什么？
[name="W"]  都是人名......不，是化名和代号，后面还画着......糖果？什么意思？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  糖果数量代表悬赏额，只有他自己在用的黑话，谁能从他这儿拿到最多的糖果，谁就是最炙手可热的队伍。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  恶趣味的记号，真让人恶心。
[name="W"]  ......不过看上去金额不小，谁出钱？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  每当我们完成一桩合同，都会有人额外准备一笔钱，用来除掉我们，比如雇主自己。
[name="赫德雷"]  越强大的佣兵越昂贵，越昂贵的佣兵越危险，越危险的佣兵越该死，而没死成的佣兵......会更强大。
[name="赫德雷"]  这场战争把我们逼上死路，也给了我们活下去的余地。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  听上去还挺合理的。
[Character(name="avg_npc_047")]
[name="赫德雷"]  就当是行规吧。
[name="赫德雷"]  ......“佣兵，化名赫德雷，十颗。手下很强，十五颗。算上交情，二十颗。”
[name="赫德雷"]  倒是挺会要价的。
[name="赫德雷"]  ......
[name="赫德雷"]  “W，旧的那个，已经结算。新的这个，麻烦，十颗，视情况加价。”
[name="赫德雷"]  看来他们似乎对你评价很高。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  或许是因为上个月我把那群军火贩子活埋在了树林里。
[name="W"]  哈......所以，我该高兴吗？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  军火......我为什么不知道这件事？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  顺手为之罢了。
[name="W"]  当你们劫掠拉特兰人的时候，有谁想过要挨个汇报吗？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  不。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  对嘛，一个道理。
[name="W"]  既然这不算是任务的一部分，雇佣兵就没有必要时刻分享自己踢开了多少石子。
[name="W"]  嗯......话说回来，原来我比那个“W”要强吗。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  很难用“强弱”来准确描述单兵的作战能力，对我而言，服从命令要更加重要。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  行了，下次我会如实汇报的，这样总行了吧？
[name="W"]  我想知道，那个“W”是个什么样的人？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  ......他啊，是个怪人。
[name="赫德雷"]  他和我们共行了很长时间，一次比一次卖力，非常优秀。
[name="赫德雷"]  他曾想靠战功成为我们的领袖，为了让所有人都给他庆祝生日。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  ......生日？萨卡兹？过生日？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  当然不是真的生日......他还不至于那么怪胎。
[name="赫德雷"]  他杀了一个拉特兰人，拿到了他的铳，大概他们之间有点故事，然后他就把那天定做了自己的生日。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  嗯哼......猎杀拉特兰人为乐的佣兵，也许我们还挺合得来的。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  这只是漫长仇视的一部分。
[name="赫德雷"]  但是，“为乐”？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  至少我乐在其中。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  不错的回答。
[name="赫德雷"]  “W”的确是其中最积极的一份子。
[name="赫德雷"]  平时总是没心没肺地笑，话里有话，似乎永远藏着什么阴谋。
[name="赫德雷"]  但其实比谁都容易相信别人。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  为什么？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  因为他抱着一个“执念”，偏执的人总会落入他人引导的陷阱，无论善意恶意。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  ......听上去不就是蠢嘛，我明白了。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=1)]
[name="赫德雷"]  你当然明白。
[name="赫德雷"]  因为你们本来就是同一类人，精于伪装，随心所欲。
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  我？
[Character(name="avg_npc_046")]
[name="W"]  ......
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="avg_ac9_4",xScale=1.1, yScale=1.1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=false)]
[ImageTween(xFrom=0, yFrom=0, xTo=-30, yTo=0, xScale=1.1, yScale=1.1, duration=30, block=false)]
[name="W"]  ......呵。
[name="W"]  你为什么觉得自己能猜透我的想法？还是说你和伊内丝一样有什么古怪的源石技艺？
[name="赫德雷"]  你......
[name="W"]  不是因为当时你也清楚，我们可以做到同归于尽吗？
[name="赫德雷"]  唉......非要嘴硬逞强这点，你倒是和伊内丝也挺像的......
[name="赫德雷"]  走吧，回去见见我们的信使。
[name="赫德雷"]  要下雨了。
[Dialog]
[delay(time=1)]
[Blocker(a=0.4, r=0,g=0, b=0, fadetime=1, block=true)]
那是我第一次看见她笑。和W一样的笑。
给她一个伪装的借口，总好过她继续这样麻木的工作。
我需要的是一个能确实开辟道路的雇佣兵，不是单纯的傀儡，这里从来不缺傀儡。
从那一天起，W成为了W。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Image(fadetime=0)]
[Background]
......但伊内丝说的对。
是很荒唐。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_barracks",screenadapt="coverall")]
[Bloc

... (全文11225字符)
```

### level_act9d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_barracks",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$m_bat_epic_intro", key="$m_bat_epic_loop", volume=0.4)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[delay(time=0.7)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=2)]
[Character(name="avg_npc_053",fadetime=0.5,block=true)]
[PlaySound(key="$d_gen_soldiersrun", volume=0.9)]
[delay(time=0.7)]
[name="萨卡兹战士"]  嘁，这些家伙是上次的——他们怎么找到这里的！？
[Character(name="avg_npc_053",name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  赶紧撤退！别磨蹭了！
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_046",fadetime=1,block=true)]
[delay(time=1)]
[name="W"]  已经被包围了，敌人数量很多。
[Dialog]
[Character(name="avg_npc_053")]
[CameraShake(duration=0.4, xstrength=0, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="萨卡兹战士"]  那就赶紧找一个方向突破！！
[Character(name="avg_npc_046")]
[name="W"]  敌人的斥候已经解决了我们的所有岗哨，敌明我暗......
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  少废话！难道要站在这里等着被术师轰死吗！？
[name="萨卡兹战士"]  等等，你是、你是赫德雷那边的......你为什么在这里？
[Character(name="avg_npc_053",name2="avg_npc_046",focus=1)]
[name="萨卡兹战士"]  赫德雷呢？他的人呢？他才是负责——
[Dialog]
[stopmusic(fadetime=0.6)]
[Character(name="avg_npc_046")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$bottlebroken", volume=0.9)]
[delay(time=2)]
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  你、你毁了我的通讯设备！你想做什么——！
[Character(name="avg_npc_046")]
[name="W"]  ......真吵啊。
[name="W"]  负责巡逻的人的确是我喔，这样才方便在你们的营地周围设好源石炸药嘛。
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  ......你！赫德雷！你们出卖......！
[Character(name="avg_npc_046")]
[name="W"]  别说得这么难听。
[name="W"]  我们只是要出趟远门，正好这时候有客人上门，总得有人留下看家嘛。
[name="W"]  如果给客人留下些甜点，尽到待客之道，也就不至于再被穷追猛打了吧？
[name="W"]  于是，就只好辛苦你们啦。
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  你、你早就该发现敌情，你是故意把我们留在这里送死——！？
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_046")]
[name="W"]  ......哼嗯。
[name="W"]  你们就努力挣扎一下吧，拖得越久，我们就能走得越远。
[name="W"]  ——再一次，由衷感谢你们。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_barracks",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  命令是帮助其他没来得及逃走的小队，不过......
[name="赫德雷"]  ......为什么没有其他人逃出来？
[Character(name="avg_npc_047", name2="avg_npc_046", focus=2)]
[name="W"]  他们自愿留下来殿后了。
[name="W"]  放心吧，我给他们留下了一点小小的礼物......所以他们会帮我们拖住敌人的。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......我可不觉得这里会有谁舍己为人。
[name="伊内丝"]  牺牲他人，优先保全自己的队伍，无可指摘的判断，用不着用谎言粉饰。
[name="伊内丝"]  但对上司隐瞒实情就完全是另一回事了。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  ......
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  你骗不过我的眼睛，W，注意你自己的言行。
[name="伊内丝"]  你嫩得很。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  ......铭记在心，伊内丝队长。
[name="W"]  毕竟我们还要共处......很长时间。
[Character(name="avg_npc_052")]
[name="伊内丝"]  现在怎么办？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ——无妨，事情已经发生了，反正到最后都是殊途同归。
[name="赫德雷"]  也许W的决定是对的。
[Character(name="avg_npc_052", name2="avg_npc_047", focus=1)]
[name="伊内丝"]  ......你真的这么想？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我们和这处营地里的任何萨卡兹都没有一丁点关系。
[name="赫德雷"]  他们的身份，他们的过往，他们的生和死，都和我们无关。
[Character(name="avg_npc_046", name2="avg_npc_047", focus=1)]
[name="W"]  真坚决啊。
[Character(name="avg_npc_047")]
[name="赫德雷"]  先谈工作，伊内丝，你和W分头带人离开，随军信使保持无线电静默，然后去指定地点汇合。
[name="赫德雷"]  ......我之后会跟上的。
[Character(name="avg_npc_052")]
[name="伊内丝"]  ......
[Character(name="avg_npc_046")]
[name="W"]  ......
[Character(name="avg_npc_047")]
[name="赫德雷"]  ......还有。
[name="赫德雷"]  我不管你们怎么互相利用，不许直接向对方下手。
[Character(name="avg_npc_052")]
[name="伊内丝"]  不直接就行？
[Character(name="avg_npc_046")]
[name="W"]  这倒是挺宽松的。
[Character(name="avg_npc_047")]
[name="赫德雷"]  ......唉。
[name="赫德雷"]  我不希望这种情况出现，但说实话，我也管不着。
[name="赫德雷"]  但如果想好好活下去，至少现在，就先让每一个萨卡兹物尽其用吧。
[Dialog]
[Blocker(fadetime=1,block=true)]
赫德雷一直是这样。
该想的事情，想得很少，想了也没用的事情，想得很多。
......我不否认W是个优秀的战士，但是她欠缺了太多的东西。
如果她只不过是一个非常非常善于战斗的萨卡兹......
......哼。
[stopmusic(fadetime=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_coldforest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Character(name="avg_npc_052",name2="avg_npc_046",fadetime=1,block=true)]
[delay(time=2)]
[Character(name="avg_npc_046")]
[name="W"]  天还没黑，你就一定要自己生一簇篝火躲在这里吗？
[name="W"]  不，你好像很喜欢篝火。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......但是我并不喜欢被人打扰。
[name="伊内丝"]  你的队伍比预定的汇合时间慢了三个小时。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  那场袭击，是你和赫德雷规划好的吗？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  你去问赫德雷。
[Character(name=

... (全文12298字符)
```

### level_act9d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Character]
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="avg_ac9_1",xScale=1.1, yScale=1.1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1.2, yScaleTo=1.2,duration=15, block=false)]
卡兹戴尔北面，有一片桦树林。
那里属于生命的时间，从春天开始，到入冬结束。
而漫长的隆冬只有死亡，所有生命都不约而同地离开那里，只有裸露在地表上的源石结晶反射着月光。
......灰白色的树干，细长的影子在雪地上交叉重叠，了无生气。
那就是我看到的景色。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
......
......伊内丝！
......伊内丝！啧！
......该死！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_battlefield",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", crossfade=3,volume=0.4)]
[Character(name="avg_npc_046",fadetime=1,block=true)]
[delay(time=1)]
[name="W"]  你如果可以醒过来，就麻烦你早点醒过来。
[Character(name="avg_npc_052")]
[name="伊内丝"]  呃——
[name="伊内丝"]  （头......好痛......）
[name="伊内丝"]  现在是......什么情况？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  没什么情况，不过为了防止你刚才摔到失忆，我可以提醒你一下。
[name="W"]  一个小时前我们遭到伏击，敌人很迅速，术师来不及构筑法术工事，队伍被打散了，附近就我们两个。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......
[name="伊内丝"]  通讯呢？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  被干扰了，不知道什么手段，对方很专业，比以往任何一个猎物都要专业。
[name="W"]  不过好消息是，对方没有朝着护送目标去，看来他们只是捕风捉影地找到了一点小消息，其实一无所知呢。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  ......
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......继续行动，想办法和其他人汇合。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  哎呀？我还以为你至少会怀疑我两句呢。
[name="W"]  我会把你留下来做活饵哦。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  你觉得现在我和你打，谁会活下来？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  当然是——
[Character(name="avg_npc_046")]
[name="W"]  ......
[name="W"]  啧——你还真是，性格恶劣，你一眼就确认了我的伤势？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  喔......原来你这么疼啊。
[name="伊内丝"]  我还以为你连自己的情绪波动都能伪装得像模像样，一瞬间担心了一下，看来是多余的。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  ——你醒来第一件事就是用你的源石技艺观察队友吗？还真是充满信任啊，队长。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  习惯而已。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  啊，原来如此，睁眼的第一刻就要警惕周围，真是个胆小鬼啊。
[Dialog]
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="W"]  啧！疼......
[stopmusic(fadetime=1.5)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  你说过活饵，对吧？是个不错的提议。
[name="伊内丝"]  带着一个站都站不稳的佣兵行动才是犯蠢，你就留下吧，我会帮你通知周围的敌人的。
[name="伊内丝"]  你最好和他们愉快相处，不要死得太快。
[Character(name="avg_npc_052")]
[name="伊内丝"]  回头见，W。
[name="伊内丝"]  最后说一句，我根本没信任过你。
[Character(name="avg_npc_046")]
[name="W"]  嘁，你这——！
[name="W"]  ——
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_053",fadetime=1,block=true)]
[delay(time=1)]
[name="萨卡兹战士"]  ......发现佣兵，一人。
[name="萨卡兹战士"]  确认对方代号，W。
[Character(name="avg_npc_046")]
[name="W"]  ......这么快？
[name="W"]  不，其实你们一直都跟着我们......？
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  就凭你们这些人的身手，放走一两人根本不足为惧。
[name="萨卡兹战士"]  哼，本想跟着监视你们直到发现本队，没想到竟然抛下同伴。
[name="萨卡兹战士"]  把那支队伍的信息全部告诉我，你可以死得痛快点。
[Character(name="avg_npc_046")]
[name="W"]  这下可麻烦了呀......我其实是很乐意坦诚相待的，但我真的什么都不知道。
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  你受伤不轻，我们时间也不多，仓促的拷问可能致死，对我们都不好。
[Character(name="avg_npc_046")]
[name="W"]  那你去追那个女人啊，她知道的比我多。
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  ......她把你当诱饵，你就不恨她吗？
[name="萨卡兹战士"]  和我们合作，痛快得多。
[Character(name="avg_npc_046")]
[name="W"]  ......诱饵呢。
[name="W"]  你......用工业源石碎屑引诱过源石虫吗？
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  ......你在说什么？
[Character(name="avg_npc_046")]
[name="W"]  只是卡兹戴尔的一个偏方啦，经常会因为源石虫遇到很多麻烦不是吗。
[name="W"]  野生的源石虫智力很低，据说会对源石有反应——
[name="W"]  ——不过真假姑且不论，你知道那些被引诱过来的虫子，会是什么下场吗？
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  别故弄玄虚——
[stopmusic(fadetime=1)]
[dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=2)]
[Character(name="avg_npc_046")]
[name="W"]  就会像你埋伏在后方的同伴那样，被炸得稀烂。
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  什——什么时候！？
[Character(name="avg_npc_046")]
[name="W"]  唉，都说了是“活饵”了，会没有陷阱吗？
[name="W"]  你该早点下杀手，或者干脆逃跑。现在再给你一次机会，我们重新来一遍。
[name="W"]  咳咳——
[name="W"]  ——这么快！？原来你们一直在追踪我们？
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  你这疯子！！
[dialog]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[PlaySound(key="$knifegore", volume=0.9)]
[Character(name="avg_npc_053")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  呃——背后——谁——
[Character(name="avg_npc_052", name2="avg_npc_053", focus=1)]
[name="伊内丝"]  小点声，别乱动。
[name="伊内丝"]  虽然只是把外行人也挥得动的细剑，但我可不是什么剑术大师，一失手，你就会死。
[Character(name="avg_npc_052", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  你——你什么时候——
[Character(name="avg_npc_052", name2="avg_npc_053", focus=1)]
[name="伊内丝"]  我和阴影的亲和力可是很高的，你真的以为一个侦查员都不带就能抓到我？
[name="伊内丝"]  来，告诉我，你的主人是谁？
[Character(name="avg_npc_052", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  我——不会——
[Character(name="avg_npc_053")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[nam

... (全文20433字符)
```

### level_act9d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(fadetime=1,block=true)]
[Dialog(fadetime=2,block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac9_8",xFrom=-60, yFrom=50,xScale=1.2, yScale=1.2, fadetime=0)]
[ImageTween(xFrom=-60, yFrom=50, xTo=20, yTo=-20, xScaleFrom=1.2, yScaleFrom=1.2,xScaleTo=1.05, yScaleTo=1.05, duration=30, block=false)]
[Blocker(a=0, fadetime=2, block=true)]
那些萨卡兹都停下了。
燃烧着的废墟向中心挤压过来，那些怪物一样的敌人居高临下。
在这场包围中心的，是一个突兀出现的女性，一个......古怪的人。
她不是萨卡兹，但是就那么只身站在战场的正中心，面不改色。
伊内丝在颤抖，我可猜不出她是为了什么颤抖。
听力似乎因为爆炸稍有受损，我听不清他们在说什么。
但是我知道，他们在畏惧。
是因为面前这个人吗？
不是，所有人都看着另一个方向，都看着另一个人。
在我失去意识的最后一秒，我看到了——
一个......萨卡兹。
毫无敌意的......纤细的萨卡兹。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
......
[dialog]
[delay(time=0.6)]
他们......临时......
萨卡兹......必须......
[dialog]
[delay(time=0.6)]
......你要......什么？
[dialog]
[delay(time=0.6)]
她的伤很重......如果我们不在这里作应急处理......
......如果......他......会找到这里......我们没有时间......
......凯尔希，来搭把手。
[dialog]
[delay(time=0.6)]
......唉，好吧。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[Character(name="avg_npc_046")]
[CameraShake(duration=0.4, xstrength=0, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="W"]  ——！
[name="W"]  这里是——
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  船上。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  船......？
[name="W"]  ......我们怎么还活着？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  你想自嘲能不能不要带上我？
[name="伊内丝"]  唉......
[name="伊内丝"]  总的来说，被救下了。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  ......那这里是哪里？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  运输队本队，我们一直护送的就是这艘舰船，现在临时收纳了一些伤员。
[name="伊内丝"]  看样子都是些正在搭建中的设施，真是不明白这艘船是什么构造，闻所未闻。
[name="伊内丝"]  （但是那时候看见的影子，确实是......还是别深究了吧。）
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  ......赫德雷呢？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......他在和雇主......不，他在和......和这里的主人谈判。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  也对，既然你还愿意乖乖待在这里，那赫德雷肯定没事。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  啧。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  那么，这里的主人是怎么回事？
[name="W"]  你好像很紧张，我不需要你那种有害视力的源石技艺就能感觉到。
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  ......你不会以为，我待在这里真的是在关心你吧？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=2)]
[name="W"]  我想也不是，那是为了什么？
[Character(name="avg_npc_052", name2="avg_npc_046", focus=1)]
[name="伊内丝"]  唉。
[name="伊内丝"]  我现在，稍微有点可怜他了。
[name="伊内丝"]  那间屋子里的，都是些什么妖魔鬼怪......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_047")]
[name="赫德雷"]  ......
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  ......你不用这么紧张，会影响到会议的效率。
[name="凯尔希"]  你们尽力做到了最好，而泄露了情报是我们的失误。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  ......战场上无论对错，我很清楚我们在和谁作对。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  那就好。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  可我没想到那位指挥官......原来真的是殿下身边的人。
[name="赫德雷"]  您的......那种力量也让我深感意外，我还没有为您出手相助正式道谢，凯尔希医生。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  谢特蕾西娅吧，是她的意思。
[dialog]
[Character]
[name="？？？"]  我怎么了？
[Character(name="avg_npc_047")]
[CameraShake(duration=0.4, xstrength=0, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="赫德雷"]  ——！
[Character(name="avg_npc_047")]
[name="赫德雷"]  殿下——
[dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_056",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  这里不是卡兹戴尔，不必多礼，我们坐下谈吧，赫德雷。
[Character(name="avg_npc_047")]
[name="赫德雷"]  ......遵命。
[name="赫德雷"]  那您身边的这位就是......
[Character(name="avg_npc_048")]
[name="？？？"]  ......
[Character(name="avg_npc_056")]
[name="？？？"]  希望你不要介意，任何战略情报博士都必须了如指掌。
[Character(name="avg_npc_047")]
[name="赫德雷"]  感谢理解。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_046")]
[name="W"]  ......
[name="W"]  （真的是一艘舰船......这个规模不算小了吧......）
[name="W"]  （有些设施看上去是全新的，有些地方又破旧的让人无法靠近......）
[name="W"]  （我记得......这是从雷姆必拓......）
[Character(name="avg_npc_051")]
[name="娇小的卡特斯"]  啊！抱、抱歉，这前面的设施还在施工......
[name="娇小的卡特斯"]  凯尔希医生说过......不要随便去更深处的地方，会很危险......
[Character(name="avg_npc_046")]
[name="W"]  哼嗯——
[name="W"]  好吧，那我就换条路吧。
[Character(name="avg_npc_051")]
[name="娇小的卡特斯"]  谢谢。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Character(name="avg_npc_046")]
[name="W"]  ......真有礼貌啊，那双耳朵，果然不是萨卡兹吧。
[name="W"]  说起来，那个比伊内丝还讨人厌的女人，好像是个医生来着？也不是萨卡兹......
[name="W"]  这里到底是怎么回事，明明身在战场的中心，尽是些萨卡兹之外的——
[Dialog]
[Character]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
怎么又卡住了啊！！
[Character(name="avg_npc_046")]
[name="W"]  唔？
[Dialog]
[Character]
[Blocker(a=1, r=0,

... (全文13380字符)
```

### level_act9d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_npc_049")]
[name="凯尔希"]  你决定了。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  并不是疑问的语气呢，凯尔希医生......不，我最近才得知，我应该叫您凯尔希勋爵。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  现在谈论这些没有意义。
[name="凯尔希"]  我只是对你的决定感到惋惜，你们可以成为特蕾西娅得力的助手。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  殿下她......在上次任务结束的时候，曾单独找到过我。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  像是她的风格。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  殿下说过，她记得我的出身，我过去在卡兹戴尔停留过。
[name="赫德雷"]  ......那座巨大的工业区，和围绕在它周围延绵百里，充斥着犯罪与死亡的腐烂城市。
[name="赫德雷"]  因为难民的不断增加，腐臭的贫民窟已经快堆上天空了。
[name="赫德雷"]  你觉得卡兹戴尔有多少所谓的“贵族”？又有多少在战争中称王封侯，冠着可笑称谓的萨卡兹？
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  多如草芥。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  的确，不过草芥。
[name="赫德雷"]  ......但也许殿下她都记得。
[name="赫德雷"]  我很感谢殿下的仁慈，她记住了我们这些萨卡兹最后还能被称之为人的部分。
[name="赫德雷"]  也只有殿下她能做到。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  那你为什么还想要逃离这里？
[Character(name="avg_npc_052")]
[name="伊内丝"]  ......不要把话说得这么难听，医生。
[Character(name="avg_npc_052", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  伊内丝，凯尔希医生在这些日子帮我们不少，我们都清楚。
[Character(name="avg_npc_052")]
[name="伊内丝"]  哼......
[Character(name="avg_npc_049")]
[name="凯尔希"]  ......我也无意冒犯。
[name="凯尔希"]  你们决定离开，继续以自由佣兵的身份浪迹大地，我没有理由阻止。
[name="凯尔希"]  有很多事情，不用我说。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  是的。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  那么还有一个萨卡兹呢？
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  W有她自己的打算。
[name="赫德雷"]  况且我也不觉得我们还有约束力去让每一个佣兵遵守军规。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  不成规模的雇佣兵总是如此，比起那些扭成一股的庞大力量，想要保持独立的势力总是脆弱不堪的。
[name="凯尔希"]  但你们所追求的东西......也值得一些迷失了的萨卡兹战士学习。
[name="凯尔希"]  无论如何，你们是自己选的这条路。
[name="凯尔希"]  哪怕你们无处可逃。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  雇佣兵只会逃进战争正中，用废墟中升起的烟雾隐藏自己。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=1)]
[name="凯尔希"]  ......如果可能的话，我希望你们做得到。
[Character(name="avg_npc_049", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  谢谢。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_coldforest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ......还跟着我们的萨卡兹，只剩下这么点人了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  很多人也选择留在了那里。更多人，永远失去了选择归宿的权利。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  营地也没了，装备也只有巴别塔提供的最低限度武装。
[name="伊内丝"]  比起雇佣兵，更像是一群去郊游的登山客啊......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......回到了最早，我们在桦树林里相遇，然后决定自立门户的时候。
[name="赫德雷"]  幸好凯尔希医生为我们提供了一些特别合约，至少还有工作，日子还能过。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  如果要继续为她做事，我们离不离开巴别塔又有什么区别？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我们只是作为一支为利益而战的佣兵队伍，接受了一份价格不菲的合同。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  都是自欺欺人罢了。
[name="伊内丝"]  ......等等，我们的旗呢？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  留下了，都被留下了，反正都是自欺欺人，干脆彻底一点。
[name="赫德雷"]  还记得吗？最开始的时候，一个旗手倒下，会立刻有另一个旗手去接替。
[name="赫德雷"]  从西部到东部，成为雇佣兵，然后折返回这里，旗帜从未倒下。
[name="赫德雷"]  直到第七十个，还是第八十个旗手死在旗下，他把旗杆插进了自己的腹部，旗帜还是没倒。
[name="赫德雷"]  在我们护卫罗德岛本舰的时候，那些敌人......那些来自卡兹戴尔的强敌，轻易撕碎了我们的防线。
[name="赫德雷"]  那时候，握着旗的，是个孩子。
[name="赫德雷"]  我们在坡下，敌人在坡上，法术像是泥石流一样冲刷着地面。
[name="赫德雷"]  在凯尔希医生抵达之前，我们几乎没有还手之力。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  旗帜都毁了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  是的。
[name="赫德雷"]  但其实我可以去伸手接住旗杆的。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我一直不喜欢雇佣兵的旗帜。
[name="赫德雷"]  它明明应该倒下的。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  那时候开始的老兵还活着几个？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  你，和我。
[name="赫德雷"]  ......先赶路吧。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_battlefield",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ......
[name="伊内丝"]  喂，赫德雷。
[name="伊内丝"]  你是故意把W留在殿下身边的吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  你怎么看殿下？还有凯尔希，以及——“博士”。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  原来你也会在背后议论他人。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  只是闲聊。
[name="赫德雷"]  你在那里一次都没有使用过法术，这对你而言很不寻常，我担心——
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......不是没用，是不敢，凯尔希医生暗示过我。
[name="伊内丝"]  那里的秘密太多了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我们的确不该太过深究。光是凯尔希的身份，就足够......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  但我无意间试探过殿下，我的法术并不能直接窥探到人的内心，只是通过观察他们的“阴影”来进行感知......
[name="伊内丝"]  殿下很特殊。
[name="伊内丝"]  殿下她......太过悲伤了。却又无比伟岸，温和。
[name="伊内丝"]  凯尔希医生很古怪，她有着近乎机械的部分，但是这台机械意外地充满人情味。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......你说那个医生？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  你们是感觉不到的吧。
[name="伊内丝"]  她平等地注视着所有人。她没有称呼我们为“魔族”。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  也许只是因为那是在殿下的身边。
[name="赫德雷"]  那，博士呢？
[Character(name="avg_npc_052",name2

... (全文12157字符)
```

### level_act9d0_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(fadetime=1,block=true)]
[Dialog(fadetime=2,block=true)]
我自己明明说过，谁也不能置身事外。
结果我自己还是想要逃离这场战争，因此从巴别塔，从W和殿下那里......
逃走了。
......真是矛盾。
后悔吗？也许吧。
但我就算在那里，也做不成任何事情。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_barracks",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
5:58  A.M.    天气/小雨   
卡兹戴尔最北部边郊，战区边缘，佣兵营地
离开巴别塔数月后
[dialog]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  这份情报......
[name="赫德雷"]  ......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......
[name="伊内丝"]  说点什么吧，你比较擅长这个，能说会道。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......说点什么呢。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  干嘛把问题抛回来......？
[name="伊内丝"]  ......僵持了这么久的战局，会在一夜之间倾斜吗？
[name="伊内丝"]  这半年多发生了什么？这太快了......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我们都知道有哪里出了问题。
[name="赫德雷"]  但是，是哪里。没人知道。
[name="赫德雷"]  不，应该说是不敢知道。
[name="赫德雷"]  殿下......还有殿下身边的那些人，他们不该沦落到如此下场，我们都这么觉得。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  但是现在......我们的下场呢？也会是这样吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  太早了。这场战争结束的太早了。
[name="赫德雷"]  直到上个月我们都还在履行和巴别塔的战略合约，联络突然中断，了无音讯......
[name="赫德雷"]  所有人都知道我们是哪一边的，我们甚至还没准备好离开这里。
[name="赫德雷"]  ......如果真的就这么戛然而止，我们只会无处可逃。
[name="赫德雷"]  让信使再去联系一趟在各地的线人，打听所有能打听到的情报。
[name="赫德雷"]  也许我们必须......回到战场正中了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  虽然，我也预料到会有这么一天。
[name="伊内丝"]  我们其实都知道的，不是吗？
[name="伊内丝"]  如果我们真的想彻底撒手不管，当时就没必要答应他们的请求。
[name="伊内丝"]  靠我们自己逃离这里，翻过瓦兰登湖，在其他地方继续大展拳脚——
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  伊内丝，我——
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  打住。
[name="伊内丝"]  我们很难从那里脱身，那份温暖太容易令人茫然，我们都沉醉于此。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  也许我们就应该彻底抛下巴别塔，带着我们的人离开。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  还是老毛病，你又变得多愁善感起来了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  从什么时候开始，我似乎没有做过任何一个有利于我们的决定。
[name="赫德雷"]  也许我们已经不该继续待在战场上......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  够了，你是萨卡兹还是我是萨卡兹？
[name="伊内丝"]  这片大地还有任何其他哪怕一处避雨的木棚，容纳得下我们这些手染鲜血的萨卡兹吗？
[name="伊内丝"]  别总是这么自责，责任是我们共同承担的。
[name="伊内丝"]  还有，就目前来看，那时候你选择接纳W，还算是个不错的决定。
[name="伊内丝"]  她帮我们挣了不少钱，也干掉了不少人。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......但愿吧。
[name="赫德雷"]  W......她还活着吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  我觉得她没那么容易死掉。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  她在殿下身边的时日也不短了，说不定她会知道更多的事情。
[name="赫德雷"]  我们必须迅速把握住现在卡兹戴尔的一切导向，如果能重新找到她，也许事情会变得简单一点。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  我们真的要依靠她作为后盾？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  好吧。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......真遗憾。
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, fadetime=2, block=true)]
[Background(image="bg_battlefield",screenadapt="coverall")]
[Blocker(a=0, fadetime=3, block=true)]
[Character(name="avg_npc_046#2",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1)]
[name="W"]  ——找到了，哎，你还真是能跑啊。
[playMusic(intro="$nervous_intro", key="$nervous_loop",crossfade=2,volume=0.4)]
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  你看上去心如死灰，我听说过你最近在做什么，W。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=1)]
[name="W"]  那你也应该知道，你是最后一个了。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  没错，你都看见了，这场仗死了很多人。
[name="萨卡兹战士"]  你只是在近乎麻木地增加这个数字。
[name="萨卡兹战士"]  即使是从我的立场而言，还没死掉的任何一个人做的事情，都比你的所作所为更有意义。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=1)]
[name="W"]  闭嘴。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  要我提醒你一遍吗？
[name="萨卡兹战士"]  特蕾西娅已经死了。整个卡兹戴尔，整个泰拉大陆都会知道卡兹戴尔的新王当立。
[name="萨卡兹战士"]  那只是一次斩首行动，你们依旧保留了很多核心成员。
[name="萨卡兹战士"]  比如那个指挥官再也没有出现过，他们做出了正确的选择。
[name="萨卡兹战士"]  殿下没有彻底赶尽杀绝，是因为他希望尽快终结混乱的局面，卡兹戴尔需要殿下开辟下一段道路——
[name="萨卡兹战士"]  ——至于你呢？你是来谈论对错的吗？
[name="萨卡兹战士"]  你当然不会发问，但你心里就是这么想的，一边这么想，一边把当时出现在你视野里的面孔一个一个抹杀掉。
[name="萨卡兹战士"]  说到底你只是来宣泄个人情绪的，小佣兵，沉浸在自己不值一提的复仇里。
[name="萨卡兹战士"]  你赢不了任何人。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=1)]
[name="W"]  反正我赢得过你，而且会很轻松。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  杀得掉我，不能说明什么。
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=1)]
[name="W"]  你的话很多哎，到底是在猜我的心思，还是单纯在死之前，发泄你自己的想法？
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  都有，我没必要否认。
[name="萨卡兹战士"]  自从那个凯——自从我差点被同伴喷出的鲜血所窒息之后，我就握不住武器了。
[name="萨卡兹战士"]  我们都流了血，洒满巴别塔的殿堂，你眼里的景象，在我眼里只会更加真切。
[name="萨卡兹战士"]  既然你找到了我，那我必死无疑，呵。
[name="萨卡兹战士"]  我知道。
[dialog]
[Character(name="avg_npc_046#2")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$pistol")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_046#2")]
[name="W"]  别扯那么多，对于杀你这件事......我只是想这么做而已，就当是排解一下失业的压力吧。
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  呸......我真是低估你了，疯子。
[name="萨卡兹战士"]  你真能像这样一点愤怒都没有地扣下扳机？还是说，你真的疯到了连自己的情绪都感觉不到？
[name="萨卡兹战士"]  你只身一人......还想继续这样追杀多少同胞？
[name="萨卡兹战士"]  你以为......你的这种举动不是在为特雷西斯殿下考虑？你帮他灭口，你还......
[Character(name="avg_npc_046#2", name2="avg_npc_053", focus=1)]
[name="W"]  不要喋喋不休了，想死的难道不是你吗？
[name="W"]  如果你逃回你亲爱的摄政王身边

... (全文12599字符)
```

### level_act9d0_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(fadetime=1,block=true)]
巴别塔发生了什么——但凡当时和特蕾西娅殿下有所联系的萨卡兹，都会有这个疑问。
W无疑看清了真相，但在漫长的旅途中，她只字不谈。
我没有问，伊内丝也没有，但我觉得她会比我更接近真相。
不知不觉之间，我已经是走在最后的那个人了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  ......我明白了。
[name="赫德雷"]  是的，不会有问题，各支队之间保持联络。
[name="赫德雷"]  ......遵命。
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  ......呼。
[name="赫德雷"]  各位，看来我们要在这里驻扎一阵子了。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  怎么了？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  先遣队观察到了天灾云，没有天灾信使在这附近，以防万一，我们只能尽可能远离天灾。
[name="赫德雷"]  无论如何，不能冒这个风险。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......天灾吗。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  很少亲眼见识到在荒野肆虐的天灾。
[name="赫德雷"]  不过卡兹戴尔和源石打交道的历史也有很久了，倒是不至于那么慌乱。
[name="赫德雷"]  ......W呢？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  待在她自己的小队。
[name="伊内丝"]  ......你要去找她？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我......不确定。W变了很多。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  你以为W会因为失去特蕾西娅而性情大变。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  但她现在冷静得不像是W。
[name="赫德雷"]  不过先前在战场上找到她的时候，她确实还是那副玩世不恭的嘴脸。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  应该说比起过去有过之而无不及。
[name="伊内丝"]  真难得，你竟然能察觉到这种细微的违和感。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......别讽刺我。如果W安静下来，那根本不算“细微”的违和感。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  W她——啊。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_thundercloud",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="伊内丝"]  山的那一边，云在汇聚，气压的变化非常剧烈......那就是天灾云？
[name="赫德雷"]  ......这个规模，可能驻扎在这里也是不安全的，通知所有支队，按原路线后撤五十公里。
[name="赫德雷"]  去找W，动作快。
[name="伊内丝"]  ......别命令我。
[name="伊内丝"]  嗯......
[name="伊内丝"]  W给我的感觉，和那个很像喔，现在。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Character(name="avg_npc_046#2")]
[name="W"]  ——啊啊。
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=1)]
[name="伊内丝"]  W！你在干什么——！
[name="伊内丝"]  这里——风好大！
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=2)]
[name="W"]  还能干什么，欣赏天灾啊！
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=1)]
[name="伊内丝"]  你疯了吗——
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=2)]
[name="W"]  你说什么？听——不——清——
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=1)]
[name="伊内丝"]  啧，忘了你本来就是个疯子。
[name="伊内丝"]  别让你手下的萨卡兹陪你一起送命！
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=2)]
[name="W"]  我已经让他们跟着赫德雷撤离了啦，我又不蠢——啊。
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=1)]
[name="伊内丝"]  W！你给我小心点！嘁！
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=2)]
[name="W"]  你才是别过来喔，摔下去你可受不了——
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=1)]
[name="伊内丝"]  你就受得了吗？你要是不想死就给我回来——！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  ......你们两个搞什么。
[Character(name="avg_npc_052", name2="avg_npc_047",focus=1)]
[name="伊内丝"]  你问她。
[Character(name="avg_npc_046#2", name2="avg_npc_047",focus=1)]
[name="W"]  是她非要碍着我吧。
[Character(name="avg_npc_046#2", name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......唉。
[name="赫德雷"]  幸亏W的队伍没有损失，否则在与整合运动的领袖合流之前，我们就要先上一趟军事法庭。
[Character(name="avg_npc_052", name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......
[Character(name="avg_npc_052", name2="avg_npc_047",focus=2)]
[name="赫德雷"]  都先回去休息吧，等待通知。
[Character(name="avg_npc_046#2", name2="avg_npc_047",focus=1)]
[name="W"]  在天灾中作战又怎么样？你害怕矿石病吗？害怕风暴吗？
[Character(name="avg_npc_046#2", name2="avg_npc_052",focus=2)]
[name="伊内丝"]  我只是单纯的不想死于非命。
[Character(name="avg_npc_046#2")]
[name="W"]  我们都该提前适应一下。
[name="W"]  这会是种有趣的体验。
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_047")]
[name="赫德雷"]  伊内丝。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  别这样，我没生气，又不是小孩子吵架要你来回哄。
[name="伊内丝"]  W她......把队伍安置得很好。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  很难得。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  很难得......我都不知道她是更疯了，还是......她......哎。
[name="伊内丝"]  她是个屁的天灾云，她就是个天灾。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  （粗口......）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_046#2",fadetime=1,block=true)]
[delay(time=1)]
[name="W"]  哼哼哼~哼哼~
[Character]
[name="萨卡兹战士"]  ......你心情好像很不错。
[Character(name="avg_npc_046#2")]
[name=

... (全文7425字符)
```

### level_act9d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[Character(name="avg_npc_054",fadetime=1,block=true)]
[delay(time=1)]
[name="萨卡兹佣兵领袖"]  你......我对你有印象......同胞。我们在战场上见过面。
[name="萨卡兹佣兵领袖"]  ......唉，唉。你不该来切尔诺伯格，罗德岛的信息已经分发给了全队。你和你的部下都会死。
[name="萨卡兹佣兵领袖"]  不过，即使你们如此优秀，还是不应该如此轻易地穿过W负责的防线，除非......
[name="萨卡兹佣兵领袖"]  这么说来，她还是做出了这个选择。其实我们都有预料到。
[Decision(options="你们中有人曾和我们并肩作战。;这是我们还在战场上谈话的唯一理由。", values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_054")]
[name="萨卡兹佣兵领袖"]  ......特蕾西娅是个卓越的领袖，她改变了很多人对这片大地的看法。
[name="萨卡兹佣兵领袖"]  理想化的看法。
[name="萨卡兹佣兵领袖"]  不用急着反驳，我比你更清楚卡兹戴尔所面临的残酷，我并不想否定她，但比起一个伟大的过程，我只想要一个微不足道的结果。
[name="萨卡兹佣兵领袖"]  只有如今摄政王的手腕能为萨卡兹带来新的未来，绝不是泛滥的善意。
[Decision(options="我们本可以试着携手共进，至少不用同归于尽。", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_054")]
[name="萨卡兹佣兵领袖"]  愚蠢的想法，萨卡兹绵长的愤懑如何安放？长久以来的倾斜如何扶正？
[name="萨卡兹佣兵领袖"]  未感染者，乌萨斯。感染者，整合运动。萨卡兹，卡兹戴尔。
[name="萨卡兹佣兵领袖"]  都是一回事，与整合运动合作的日子里我更加确信了这件事。
[name="萨卡兹佣兵领袖"]  摄政王殿下能为我们开拓一个新的家园，我只是选择追随这个可能性。
[name="萨卡兹佣兵领袖"]  一如当年，你们天真地追随特蕾西娅。
[name="萨卡兹佣兵领袖"]  ......好了。
[name="萨卡兹佣兵领袖"]  既然W把你放了进来，你一定也付出了代价。
[name="萨卡兹佣兵领袖"]  你付出了什么呢？为了拖延时间掩护你而丧命的部下？甚至是......你自己？
[Decision(options="......", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_054")]
[name="萨卡兹佣兵领袖"]  告诉我你现在的名字吧。
[Decision(options="——Scout。;雇佣兵不也都是用假名的吗，加尔森。", values="1;2")]
[Predicate(references="1")]
[Character(name="avg_npc_054")]
[name="萨卡兹佣兵领袖"]  很耳熟的代号，为表尊重，我本来是想把你的本名刻在这把刀上。
[Predicate(references="2")]
[Character(name="avg_npc_054")]
[name="萨卡兹佣兵领袖"]  ......你说得也对。
[Predicate(references="1;2")]
[Dialog]
[Blocker(fadetime=1,block=true)]
[Character]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[PlaySound(key="$rungeneral")]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.4)]
[delay(time=2)]
[Character(name="avg_npc_052",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=1)]
[name="伊内丝"]  放弃抵抗吧。
[name="伊内丝"]  ......还有你的十二位队员，已经被确认全灭了。
[name="伊内丝"]  雷发，米米，图钉，死于整合运动术师的包围网正中，有一个是站着死的。
[name="伊内丝"]  小玛丽，长音，斯琳珂，长蝎占据了一处阵线，W亲自带队过去了。
[name="伊内丝"]  姆拉姆，酒莓软芯，淤兰，和我们的一支小队同归于尽，有人杀出了重围，然后被赫德雷的刀兵斩首。
[name="伊内丝"]  普特尔刚才死在那栋楼下，很意外，好像是为了救一个没来得及撤出的平民。
[name="伊内丝"]  索拉娜还留着一口气，被带回去了，想必她会想方设法自尽的吧。
[name="伊内丝"]  ......还不吭声吗。
[name="伊内丝"]  别躲了，你听得见，影子一清二楚，你的气息混乱不堪，伤得不轻。
[Dialog]
[Character]
[Character(name="avg_npc_026",fadetime=1,block=true)]
[delay(time=1)]
[name="Scout"]  ......你为什么知道他们的名字？
[Character(name="avg_npc_052",name2="avg_npc_026",focus=1)]
[name="伊内丝"]  W特意嘱咐过，你们会把兵牌一类的东西挂在身上。
[name="伊内丝"]  “至少杀了谁还是要弄明白的，这里毕竟不是卡兹戴尔，不留神杀错人可就不好办了”。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=2)]
[name="Scout"]  那不是兵牌，牺牲的那些干员们......也不全是士兵。
[name="Scout"]  我以为会是W来亲自动手。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=1)]
[name="伊内丝"]  她......哼，我要是说她不忍心亲手解决你，你会信吗？
[name="伊内丝"]  摄政王派来的领袖已经被你杀了，想要接管的可不止她一个，她现在比较忙。
[name="伊内丝"]  就像当时你和W说好的一样。
[name="伊内丝"]  一旦你完成任务，我们就会“后知后觉”地全力歼灭你们。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=2)]
[name="Scout"]  ......
[Character(name="avg_npc_052",name2="avg_npc_026",focus=1)]
[name="伊内丝"]  ......你在巷战的过程中还抽空救了个人。但现在，那不是我们的管辖范围。
[name="伊内丝"]  但是爱国者在那里，你不需要过问。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=2)]
[name="Scout"]  ......这样，就好。
[name="Scout"]  你们......变了，过去的W不是个会刻意记住死者名讳的人。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=1)]
[name="伊内丝"]  她确实变了，但更多时候是变得更像个疯子。
[name="伊内丝"]  你纯粹的战地经验就堪比浮士德的源石技艺，说不定只是为了让你动摇，好让我用法术捕捉你才故意记下名字的呢？
[Character(name="avg_npc_052",name2="avg_npc_026",focus=2)]
[name="Scout"]  ......老样子，总不放过任何取乐的机会。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=1)]
[name="伊内丝"]  彼此，你不是也接受了这种W才能想出来的疯狂交易。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=2)]
[name="Scout"]  用我的命换取一个机会，再让该把握住这个机会的人把握住它，这并不疯狂。
[name="Scout"]  还有我牺牲的队员们，也一样。他们为了自己的理念而死，没有他们，我无法成功。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=1)]
[name="伊内丝"]  ......看来时过境迁，大家都有一些变化。
[Character(name="avg_npc_052",name2="avg_npc_026",focus=2)]
[name="Scout"]  你也是，过去的你绝不会像现在这样，给敌人喘息的空间。
[name="Scout"]  赫德雷应该提醒过你。
[Dialog]
[Character(name="avg_npc_026")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$pistol")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[delay(time=0.5)]
[Character]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ——
[name="伊内丝"]  为什么还要抵抗？
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ......啧，不见了......
[name="伊内丝"]  ......
[name="伊内丝"]  但愿你能就这么逃掉......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_052")]
[name="伊内丝"]  （这个方向吗？）
[name="伊内丝"]  （......）
[name="伊内丝"]  （没错，这里。动作真快。）
[name="伊内丝"]  （麻烦的家伙，如果他没有受伤，恐怕我连他人都见不着......）
[name="伊内丝"]  （等等。）
[name="伊内丝"]  （他......他在向核心城转移？）
[name="伊内丝"]  （那里——啧！）
[Dial

... (全文10071字符)
```

### level_act9d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(fadetime=1,block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Dialog(fadetime=2,block=true)]
塔露拉变了。
第一次见到塔露拉的时候，她给我的感觉，和特蕾西娅殿下很像。
但殿下一直非常的悲伤，她背负着......也知晓着这片大地的更多秘密。
塔露拉不同，她很愤怒，足够冷静的，却又充满热情的愤怒。
虽然细小很多，却同样强盛。也许他们这样的人无论力量大小，都拥有着近似的部分。
这股愤怒催生了整合运动，让无数追随者趋之若鹜。
但很快......就改变了。
我们每天的工作，变成了煽动、加害和挑拨。
这不再是一场感染者的革命——
——而是我们在卡兹戴尔目睹过无数次的，被过度操纵的战争阴谋。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  她没有追上来。
[name="赫德雷"]  ......如果我们真的和她正面碰上，事情就麻烦了。
[name="赫德雷"]  你不该对塔露拉使用法术，这也不是第一次了，我们要时常小心自己看见的东西。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......塔露拉的身上一定发生了什么，这件事必须告诉W。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  多亏了W几次的小动作，我们已经遭到那些暴徒的猜忌了，这还不够吗？
[name="赫德雷"]  你到底看到了什么？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  过去的塔露拉只是个反抗者。她把反抗的机会带给那些被解放的感染者。
[name="伊内丝"]  现在呢？他们几乎毫不收敛自己的欲望，单纯的破坏，滥杀。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  这不足以说明什么，萨卡兹之外的种族对感染者素来如此。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......你不明白。
[name="伊内丝"]  我不是在说这种行为本身怎么了，我是在说这样的行为会招致什么后果......
[name="伊内丝"]  塔露拉她......在葬送整合运动，刻意的。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  ......为什么？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  你不觉得这个情况似曾相识吗？
[name="伊内丝"]  她是个优秀的领袖，能将这些普通的感染者卷入战争，甚至带给他们胜利。
[name="伊内丝"]  但她，也只有她才能用最神不知鬼不觉的方法，一步步毁掉自己一手搭建起来的高塔。
[name="伊内丝"]  甚至......
[name="伊内丝"]  甚至塔露拉她自己，都只是其中一块比较精美的砖瓦，随时可以被粉碎。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  你是在说......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  和三年前给我的感觉一样。
[name="伊内丝"]  但他......他或许素来如此，他可以毫不犹豫地做到这一切......只是藏的很好罢了。
[name="伊内丝"]  塔露拉不同，她的变化太突然了。
[name="伊内丝"]  她的影子......她甚至有两个影子，不像是法术的痕迹，倒像是......
[name="伊内丝"]  一座废墟，古老，强盛，满是那种力量的残留......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  你的法术性质很特殊，尽管如此，你这次的感觉也太模糊了，这还是不构成行动的理由。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  但这件事W必须知道！
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  小声点，我们已经被注意到了。
[name="赫德雷"]  任何动作都会成为别人的把柄，你明白的。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  那你觉得我们还能经受住第二次巴别塔那样的变故吗？
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  我不确定......
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  ......至少W不能。
[name="伊内丝"]  我去找她，既然加尔森已经死了，她就是新的领导人。
[Character(name="avg_npc_052",name2="avg_npc_047",focus=2)]
[name="赫德雷"]  等等！如果塔露拉真的已经注意到了，你这样会——
[Character(name="avg_npc_052",name2="avg_npc_047",focus=1)]
[name="伊内丝"]  等不了，别想命令我，现在我们还是平起平坐。
[name="伊内丝"]  ......哼。
[name="伊内丝"]  话是这么说，这好像是我第一次抗命。
[name="伊内丝"]  你不该总是想这么多的，赫德雷。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_cher_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", crossfade=5,volume=0.4)]
[PlaySound(key="$rungeneral")]
[Character(name="avg_npc_052")]
[name="伊内丝"]  ......
[name="伊内丝"]  （W，就在前面，穿过这条巷子就......）
[name="伊内丝"]  （那里不是营地？她在做什么？）
[name="伊内丝"]  （总之得快一点——）
[name="伊内丝"]  ——
[name="伊内丝"]  ——谁？
[Character(name="char_1002_nsabr_2")]
[name="整合运动士兵"]  ......
[Character(name="avg_npc_052")]
[name="伊内丝"]  感染者......？有什么事吗？
[Character(name="char_1002_nsabr_2")]
[name="整合运动士兵"]  注意你的语气，魔族。
[name="整合运动士兵"]  先是有几支佣兵队伍叛逃，接着又让敌人出现在了城内。
[name="整合运动士兵"]  你们犯下的错误太多，你该不会以为领袖没有看在眼里吧？
[Character(name="avg_npc_052")]
[name="伊内丝"]  让开，我没有义务听你抱怨。
[Character(name="char_1002_nsabr_2")]
[name="整合运动士兵"]  你有这个义务对塔露拉负责。
[Character(name="avg_npc_052")]
[name="伊内丝"]  ——我明白了，等我向W汇报完之后，我会去向塔露拉报到。
[Character(name="char_1002_nsabr_2")]
[name="整合运动士兵"]  不必了。
[name="整合运动士兵"]  我们需要的不是这种“负责”。
[Character(name="avg_npc_052")]
[name="伊内丝"]  什么......
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_052")]
[name="伊内丝"]  啧.....来真的？
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动士兵"]  刚才发生的袭击波及了这里，萨卡兹雇佣兵小队长之一的伊内丝，死亡。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="坚毅的整合运动术师"]  不去确认她的尸体？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="整合运动士兵"]  ......刚才的战斗动静太大，已经有人被吸引过来了，立刻炸毁这条街道。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="坚毅的整合运动术师"]  是。
[Character(name="char_1002_nsabr_2")]
[name="整合运动士兵"]  等等。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="整合运动士兵"]  整合运动也要有人......和她一并奋战到了最后。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="坚毅的整合运动

... (全文7071字符)
```

### level_act9d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Character]
[Blocker(fadetime=1,block=true)]
[Dialog(fadetime=2,block=true)]
数月前，与整合运动接洽后
10:14  P.M.    天气/晴
乌萨斯，无名城郊荒漠
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_wild_a",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_047")]
[name="赫德雷"]  ......你和整合运动的领袖们都见过了。
[name="赫德雷"]  感觉如何？
[Character(name="avg_npc_046#2")]
[name="W"]  你问我，还是问她？
[name="W"]  问我的话，我只能说不出所料。差不多就该是这些家伙，来做这些事。
[Character(name="avg_npc_052")]
[name="伊内丝"]  很奇特。有被刻意引导而推上那个位置而变得残暴的小孩，也有坚韧到超乎想象的战士。
[Character(name="avg_npc_046#2")]
[name="W"]  有很了不起的家伙，但也有很无趣的反派。
[name="W"]  总的来说呢，打了那么多年仗，我们见得也不少了吧。
[Character(name="avg_npc_052")]
[name="伊内丝"]  不过，有个人倒是让我很在意......
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=2)]
[name="W"]  啊啊，你说那个啊。一直和另一个小兔子待在一边的。
[Character(name="avg_npc_052", name2="avg_npc_046#2", focus=1)]
[name="伊内丝"]  他们的队伍给人的感觉和其他感染者完全不同。这种萨卡兹战士才算得上是战争的符号。
[Character(name="avg_npc_047")]
[name="赫德雷"]  萨卡兹？
[Character(name="avg_npc_046#2")]
[name="W"]  但也很少能见到那样的萨卡兹啊，而且他自称乌萨斯人，也早就和卡兹戴尔断了联系。
[name="W"]  真可怜啊，他本可以不用活得这么疲惫。
[Character(name="avg_npc_052")]
[name="伊内丝"]  也许我们都该见见他。
[name="伊内丝"]  他给人留下的感觉，超过了“战士”这个范畴。
[name="伊内丝"]  你啊，不是总喜欢想很多吗？比起干想，不如去找他那种人聊聊。
[name="伊内丝"]  我们也许都能从他身上学到不少。
[Character(name="avg_npc_047")]
[name="赫德雷"]  你们说的是......
[Character]
[Dialog]
[Delay(time=1)]
[name="？？？"]  打扰，我想，单独见见你们。
[Character(name="avg_npc_046#2")]
[name="W"]  ......真是说来就来，你赶好的吗？
[Character(name="avg_npc_047")]
[name="赫德雷"]  您是......
[Character]
[Dialog]
[Character(name="avg_npc_025_1",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1)]
[name="？？？"]  我，是谁，暂且，不重要。
[name="？？？"]  现在，我并非，以领袖的名义，来见你们，请放心。
[name="？？？"]  我只是想，来听一听......
[name="？？？"]  同胞，和家乡，发生的事情。
[name="？？？"]  我知道，在卡兹戴尔，发生了，许多事情。
[name="？？？"]  我，有所耳闻，却不知详情。
[Character(name="avg_npc_025_1", name2="avg_npc_046#2", focus=2)]
[name="W"]  你只是个乌萨斯人。
[Character(name="avg_npc_025_1")]
[name="？？？"]  这两者，并不冲突。
[name="？？？"]  血脉，从未改变。黑暗，根深蒂固。
[name="？？？"]  我虽从未在意，但也都，无法动摇。
[Character(name="avg_npc_025_1", name2="avg_npc_046#2", focus=2)]
[name="W"]  那么就算你知道了，又打算做什么？
[name="W"]  都已经是很久以前的事情了——
[Character(name="avg_npc_025_1")]
[name="？？？"]  不会，做什么，也不能，做什么。
[name="？？？"]  只是，在很久以前，我见过，特蕾西娅。
[Character(name="avg_npc_025_1", name2="avg_npc_046#2", focus=2)]
[name="W"]  ——嚯。
[Character(name="avg_npc_025_1")]
[name="？？？"]  你们的反应，我明白。她也在你们这，留下了痕迹。毕竟，你们也是，萨卡兹。
[name="？？？"]  泥泞的，也好，血腥的，也罢。
[name="？？？"]  她是英雄，至少，被如此推崇。她，伟大的战士，也是，难得的君主。
[name="？？？"]  我的血肉，忠于乌萨斯，我的族群，自我流放，但我，还是萨卡兹。
[name="？？？"]  我想知道，她的，卡兹戴尔，发生了什么。
[name="？？？"]  我只是，想要知道。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_wild_a",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
现在，切尔诺伯格转移途中
5:22  A.M.    天气/晴
切尔诺伯格，萨卡兹佣兵驻扎区
[Dialog]
[Character(name="avg_npc_046#2",fadetime=1,block=true)]
[delay(time=1)]
[name="W"]  ......
[name="W"]  ......你找我有事？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  我们希望萨卡兹雇佣兵队伍能给出一个解释。
[name="整合运动士兵"]  先是有你的队伍叛逃，而前去追击的人汇报说，你根本没有全力以赴。
[name="整合运动士兵"]  数个小时前，又有敌人潜伏进切尔诺伯格，同样是你们的失职。
[name="整合运动士兵"]  再加上最早攻占切尔诺伯格的时候，有人报告你放走了——
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  啊，好了好了，我明白客户的不满了，能少说两句吗？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  我们只是“合作”关系，现在我是领袖，如果我现在拍桌子翻脸，塔露拉会高兴吗？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  还是爱国者老爷子让你们产生了......整合运动真的精于战争的错觉？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  不要搞错到底是哪些人才能为你们带来胜利。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  ......
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  想明白了就赶紧滚回去，告诉那个龙女，她该知道的事情我会去找她的，不要这么着急。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  还有一件事。
[name="整合运动士兵"]  就在刚刚，城内发现了潜入的敌军残党。萨卡兹雇佣兵伊内丝，与对方交火后同归于尽。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  ......
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  整合运动也参与了这场阻击战，敌人很强，我们都遭到了损失。
[name="整合运动士兵"]  这都是你的失职所致。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  ......别这么急着咄咄逼人。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  刚才，似乎东边有些动静。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  没错。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  那......尸体呢？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  很遗憾。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  我问的是敌人的尸体，伊内丝可不会什么夸张的杀伤性法术。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  我们的术师也参加了战斗，整条街道都毁于一旦。 
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  ——你们这也太明目张胆了吧？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  我不知道你在说什么。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  ......那在你们看来，这件事应该怎么处理？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  ......我们的主要兵力正着眼于将要在龙门发生的战斗，无暇顾及。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  领袖暂时不会深究你的责任。你们应该自行处理。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  嗯......你的乌萨斯口音很重。
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=1)]
[name="整合运动士兵"]  ......所以呢？
[Character(name="char_1002_nsabr_2", name2="avg_npc_046#2", focus=2)]
[name="W"]  你们......
[Character(name="

... (全文17835字符)
```

### level_act9d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_victoria",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_055",fadetime=1,block=true)]
[delay(time=1)]
[name="赦罪师"]  报告，我看过了。
[name="赦罪师"]  你们在整合运动那里取得的成果，实在令人难以恭维。
[name="赦罪师"]  但，即使如此，你们也的确找到了一些预料之外的收获。
[Character(name="avg_npc_055", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  感谢——
[Character(name="avg_npc_055")]
[name="赦罪师"]  啊啊，不用道谢，至少这次还不用。
[name="赦罪师"]  你们也都是优秀的战士，在死前，你们任何的奖赏都是你们的血与火所夺来的。
[name="赦罪师"]  摄政王殿下熟知每一个微不足道的萨卡兹所践行的轨迹，即使你们太过微不足道。
[name="赦罪师"]  在这座殿堂里逐渐失去价值的，不光是那些感染者，你明白吗？
[Character(name="avg_npc_055", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  ......我明白。
[Character(name="avg_npc_055")]
[name="赦罪师"]  嗯。
[name="赦罪师"]  如果我所猜没错，罗德岛如今已经迎回了那个让人不快的人。
[name="赦罪师"]  至于你们......你们应该有所接触。
[Character(name="avg_npc_047")]
[name="赫德雷"]  ——！
[name="赫德雷"]  （摄政王比W还更快一步？在这么遥远的伦蒂尼姆——？）
[Character(name="avg_npc_055")]
[name="赦罪师"]  雇佣兵仅仅效忠于利益。这种出发点，未必是什么坏事。
[name="赦罪师"]  等到尘埃落定，回到殿下的座前——
[name="赦罪师"]  ——你就可以赢得你的奖赏。
[Character(name="avg_npc_055", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  ......那其他的战士们？
[Character(name="avg_npc_055")]
[name="赦罪师"]  那位感染者青年有她自己的手腕，你们还没有发觉吗？
[name="赦罪师"]  但殿下已无心深入这场闹剧，殿下与我自有判断，维多利亚将持续观望整合运动。
[name="赦罪师"]  我们缺乏从W手里夺回那支队伍控制权的......“高效手段”。
[name="赦罪师"]  况且，我们依旧需要以支持者的名义，去煽动在大地各处活动的感染者们。
[Character(name="avg_npc_055", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  我们仍旧要利用整合运动？我以为这样的发展会让殿下......
[Character(name="avg_npc_055")]
[name="赦罪师"]  放弃？不不不，年轻的雇佣兵。
[name="赦罪师"]  还不够混乱，远远不够。哪怕是远离了领袖的整合运动，也依旧能成为祸乱的根源——
[name="赦罪师"]  ——以及，刚才的言论，是否可以认作是对殿下的质询？
[Character(name="avg_npc_055", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  不，不敢。
[Character(name="avg_npc_055", name2="avg_npc_047", focus=1)]
[name="赦罪师"]  无妨，抬起头来......
[name="赦罪师"]  对了，对了。
[name="赦罪师"]  你暂时先不用回去了。漫长的路程会耽误太多时间，而那里发生的一切正在加速。
[name="赦罪师"]  就暂且留在这里，享受你为数不多的清闲时间吧。
[Character(name="avg_npc_055", name2="avg_npc_047", focus=2)]
[name="赫德雷"]  ......感激不尽。
[Character(name="avg_npc_055")]
[name="赦罪师"]  那么，殿下还在等我，原地解散吧。
[name="赦罪师"]  记住，先做好自己的事情，赫德雷。
[Character(name="avg_npc_047")]
[name="赫德雷"]  明白。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_055")]
[name="赦罪师"]  ......赫德雷，是吗。
[name="赦罪师"]  我很期待，你到底还能发现些什么。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_victoria",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_047",fadetime=1,block=true)]
[delay(time=1)]
[name="赫德雷"]  ......唉。
[Character]
[name="萨卡兹信使"]  这意思是......我们都被软禁了？
[Character(name="avg_npc_047")]
[name="赫德雷"]  我不是没有考虑过，已经比想象中好很多了......
[name="赫德雷"]  不过，我们还是太天真了。
[Character]
[name="萨卡兹信使"]  哪一边天真？是误以为自己会死，还是误以为摄政王一无所知？
[Character(name="avg_npc_047")]
[name="赫德雷"]  都有，他......始终都掌握一切。
[name="赫德雷"]  也难怪......他可是特雷西斯。那些故事里的他和特蕾西娅，是多么的所向披靡......
[name="赫德雷"]  只不过这场战争让我们都忘了，那些故事......都不只是故事。
[Character]
[name="萨卡兹信使"]  该怎么警告W？现在整合运动的事情又发展到哪一步了？
[name="萨卡兹信使"]  我们在路上花了很多时间，说不定现在她已经和塔露拉闹掰了。
[Character(name="avg_npc_047")]
[name="赫德雷"]  又或者，这场闹剧会在龙门被终结。
[Character]
[name="萨卡兹信使"]  ......会不会太快了点？
[Character(name="avg_npc_047")]
[name="赫德雷"]  这才符合W的规划。如果塔露拉真的打算毁掉这些感染者，那W一定会先毁掉塔露拉。
[name="赫德雷"]  用萨卡兹的方式，不择手段。
[name="赫德雷"]  毕竟因为某位佣兵的死，她很不高兴。
[Character]
[name="萨卡兹信使"]  她明明心里有数。
[Character(name="avg_npc_047")]
[name="赫德雷"]  时局至此，容不得她继续犹豫下去。她只是缺乏一个动手的好心情而已。
[Character]
[name="萨卡兹信使"]  但现在是我们落于被动。
[Character(name="avg_npc_047")]
[name="赫德雷"]  有办法。想骗过摄政王的眼睛，无论如何都非常冒险，但是......
[Character(name="avg_npc_047")]
[name="赫德雷"]  我依旧有权对我的直属小队下达“待命”的指令。
[Character]
[name="萨卡兹信使"]  维多利亚很混乱，暗号不容易被注意到。
[Character(name="avg_npc_047")]
[name="赫德雷"]  不光如此，消息将会绕过摄政王所掌控的那些最敏感的地区......发向卡兹戴尔。
[Character]
[name="萨卡兹信使"]  卡兹戴尔？
[Character(name="avg_npc_047")]
[name="赫德雷"]  那里的战场废墟早已经无人问津。
[name="赫德雷"]  但我们毕竟，在那里挣扎了很久。
[name="赫德雷"]  在某处废墟下有一个秘密发报站，信号塔被伪装成遭到破坏的样子，线路完好无损。
[Character]
[name="萨卡兹信使"]  等等，那时候......
[name="萨卡兹信使"]  ......你什么时候做好这些准备的？
[Character(name="avg_npc_047")]
[name="赫德雷"]  从一开始，花了很大一笔钱。
[Character]
[name="萨卡兹信使"]  ......呵呵。
[name="萨卡兹信使"]  你啊......让他们看到你现在的表情，应该都会很惊讶吧。
[name="萨卡兹信使"]  从什么时候开始，每次上战场，再归来，你永远是一副若有所思的样子，好像做错了事的孩子。
[name="萨卡兹信使"]  我还以为，你会更加丧失斗志。
[Character(name="avg_npc_047")]
[name="赫德雷"]  不，恰恰相反，我反而越来越明白我该做什么了。
[Character]
[name="萨卡兹信使"]  为什么？
[Character(name="avg_npc_047")]
[name="赫德雷"]  因为我没得选，这样反而解脱了，不是吗？
[Character]
[name="萨卡兹信使"]  W一定对你说了些什么，在你离开切尔诺伯格之前。
[Character(name="avg_npc_047")]
[name="赫德雷"]  你觉得她像是那种会和盘托出的人吗？
[Character]
[name="萨卡兹信使"]  不是。如果是，就没今天这么麻烦了。
[Character(name="avg_npc_047")]
[name="赫德雷"]  不过她的确在我离开核心城前找了我一次。那时候她已经察觉到我们的意思了。
[name="赫德雷"]  她——
[Dialog]
[stopmusic(fadetime=1)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_cher_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
[Character(name="avg_npc_047", name2="avg_npc_046#2", focus=2)]
[name="W"]  雇佣兵的性命可以用价格来衡量吗？
[Character(name="avg_npc_047", name2="avg_npc_046#2", focus=1)]
[name="赫德雷"]  当然。一直以来。为什么这么问？你可是最懂得这个道理的。
[Character(name="avg_npc_047", name2="avg_npc_046#2", focus=2)]
[name="W"]  可，谁来决定？
[Character(name="avg_npc_047", name2="avg_npc_046#2", focus=1)]
[name="赫德雷"]  战争本身。
[Character(name="avg_npc_047", name2="avg_npc_046#2", focus=2)]
[name="W"]  是啊......战功，战绩，在厮杀中夺取名利，抬高身价，作为道具被他人认可。
[

... (全文9110字符)
```

### level_act9d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Background]
[Delay(time=1)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_npc_046#2")]
[name="W"]  你们还要往前走吗？
[name="W"]  不进行治疗的话，你会感染的。
[Character]
[name="坚强的孩子"]  ——我凭什么相信一个魔族？
[Character(name="avg_npc_046#2")]
[name="W"]  魔族、魔族呢。
[name="W"]  身边尽是些魔族，我都快忘记这个称呼了。
[Character]
[name="坚强的孩子"]  嘁，你不要跟在我们后面！
[Character(name="avg_npc_046#2")]
[name="W"]  我已经离得很远了吧？
[Character]
[name="坚强的孩子"]  别这么假惺惺的，要是想动手的话，现在就动手啊！
[name="孱弱的孩子"]  卢、卢布廖夫，别刺激她比较好......
[name="坚强的孩子"]  ......行了，我们自己走就好。
[name="坚强的孩子"]  别管她。
[name="孱弱的孩子"]  对、对不起......
[name="坚强的孩子"]  感染就感染，我们不要魔族帮忙！
[name="孱弱的孩子"]  ......嗯。
[Character(name="avg_npc_046#2")]
[name="W"]  嗯哼......
[name="W"]  这附近有一家废弃的医院。切尔诺伯格区级医院。
[name="W"]  你们想知道在哪里吗？
[Character]
[name="坚强的孩子"]  ......
[name="孱弱的孩子"]  卢布廖夫......？
[name="坚强的孩子"]  别听她的，肯定都是骗我们的。
[name="坚强的孩子"]  咱们甩掉她......走快点。
[name="坚强的孩子"]  看到那边的巷子了吗？你从那个拐角跑进去，一分钟之内跑到！
[name="孱弱的孩子"]  ......好。
[name="坚强的孩子"]  ——跑！
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_9",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_046#2")]
[name="W"]  跑的还挺快。
[Character]
[name="坚强的孩子"]  她、她怎么这么快就跟上来了——唔！
[name="孱弱的孩子"]  卢布廖夫......你的腿！血、血变成黑色了......
[name="坚强的孩子"]  嘁，要不是刚才救了你，我怎么会跑不过她！
[name="孱弱的孩子"]  对不起、对不起......
[name="坚强的孩子"]  算了！小声点。
[name="坚强的孩子"]  别让她发现。
[Character(name="avg_npc_046#2")]
[name="W"]  ......
[name="W"]  前面的街道，左拐，能看到一处被毁掉的广场。
[name="W"]  广场西边，那座最大的白色建筑，是医院。
[name="W"]  废弃的医院。
[Character]
[name="孱弱的孩子"]  ......我们，好像已经被发现了......
[name="坚强的孩子"]  都是你不听话——算了。
[name="坚强的孩子"]  喂，魔族。
[name="坚强的孩子"]  ......你为什么要告诉我们？
[Character(name="avg_npc_046#2")]
[name="W"]  一时兴起啊。
[name="W"]  你们两个，什么关系？
[Character]
[name="孱弱的孩子"]  ......
[name="坚强的孩子"]  ......我只是出来找吃的，遇见了他。
[name="孱弱的孩子"]  是卢布廖夫救了我......
[Character(name="avg_npc_046#2")]
[name="W"]  嗯......所以你听他的？
[Character]
[name="孱弱的孩子"]  ......
[Character(name="avg_npc_046#2")]
[name="W"]  算了，随便吧，现在，轮到你帮帮你自己的救命恩人了。
[Character]
[name="坚强的孩子"]  你想让他做什么？
[name="孱弱的孩子"]  卢布廖夫......
[Character(name="avg_npc_046#2")]
[name="W"]  没什么。我说过，前面不远，就有一家医院。
[name="W"]  当然，整合运动也不傻，不会干放着那些医疗物资视作无物......所以，如果你想救这位卢布廖夫小朋友......就去偷。
[name="W"]  那里都是感染者暴徒，是杀了你们的家人、亲人、朋友的暴徒。
[name="W"]  也只有那里有抑制矿石病早期症状的药剂。
[name="W"]  去偷，去抢，怎么都好。
[name="W"]  但是不要指望那边的人会帮你。
[Character]
[name="坚强的孩子"]  别去！没必要听他的！
[name="孱弱的孩子"]  但、但是......
[Character(name="avg_npc_046#2")]
[name="W"]  别去？
[name="W"]  他知道你的名字，卢布廖夫，你知道他的吗？
[Character]
[name="坚强的孩子"]  这和现在有什么关系！？
[name="坚强的孩子"]  别去！你做不到的！那里都是——
[name="孱弱的孩子"]  我——
[name="孱弱的孩子"]  我......我想试试......
[name="孱弱的孩子"]  不光是卢布廖夫哥哥，好多人都在天灾发生的时候受了伤......
[name="孱弱的孩子"]  大家都很痛......我......
[name="坚强的孩子"]  你怎么能不听我的话！
[name="孱弱的孩子"]  我......
[Character(name="avg_npc_046#2")]
[name="W"]  他没有义务听你的话。
[name="W"]  想要救那些人，想法很好。
[name="W"]  记住我说的那家医院，医疗物资已经被集中在了地下仓库。
[name="W"]  你可以从停车场的通风管道潜进去，或者从排水沟里走，只要化学废料没那么多。
[name="W"]  说不定，你会死在那里。
[Character]
[name="孱弱的孩子"]  ......
[name="坚强的孩子"]  看吧，你的脚都在打颤，别想了！我们就不该听这个魔族的话！
[name="坚强的孩子"]  赶紧走吧！
[name="孱弱的孩子"]  我......
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[name="孱弱的孩子"]  噫——
[name="坚强的孩子"]  发、发生什么了？
[Character(name="avg_npc_046#2")]
[name="W"]  龙门发生了不少事......也让这里出现了一些缺口。
[name="W"]  在如今的切尔诺伯格，那可是难得的战地医院，怎么会没有别的人打它的主意呢？
[name="W"]  你们觉得为什么......身为魔族的我，会对那里有一家医院这么清楚？
[Character]
[name="坚强的孩子"]  你这个——唔，啊——
[name="孱弱的孩子"]  我......我......
[Character(name="avg_npc_046#2")]
[name="W"]  他很痛苦，而且照这个势头发展下去，他无药可救。
[name="W"]  如果你不做决定的话......
[name="W"]  你们就死在这里吧。
[Character]
[name="孱弱的孩子"]  啊......
[name="坚强的孩子"]  你、呜、你到底想做什么！别过来！
[Character(name="avg_npc_046#2")]
[name="W"]  去。
[name="W"]  还是不去？
[name="W"]  啊......不过你现在去说不定也晚了，既然已经发生暴乱，去偷东西就更难了吧——
[Character]
[name="孱弱的孩子"]  我，我去。
[Character(name="avg_npc_046#2")]
[name="W"]  ——嗯......会死哦。
[Character]
[name="坚强的孩子"]  为什么要听她的话，是我把你救出来的！
[name="孱弱的孩子"]  可我、我想试试......
[name="坚强的孩子"]  你哪能做到啊！我们继续去找药店和食物，这样就好！
[name="孱弱的孩子"]  ——
[name="孱弱的孩子"]  对不起！
[name="坚强的孩子"]  啊......等等！
[Character(name="avg_npc_046#2")]
[name="W"]  连他的名字都不知道，想出声阻止都没法子，真可怜。
[Character]
[name="坚强的孩子"]  你......你骗他！你这个魔鬼！
[Character(name="avg_npc_046#2")]
[name="W"]  骗？
[name="W"]  我可没有说一句谎话。
[name="W"]  当然，信不信我，由你。
[name="W"]  信不信他，也随便你。
[Character]
[name="坚强的孩子"]  ......我，我要去找他，呜......
[Character(name="avg_npc_046#2")]
[name="W"]  为什么？
[Character]
[name="坚强的孩子"]  他、他没有我什么都做不到......
[Character(name="avg_npc_046#2")]
[name="W"]  你在担心他会逃跑。
[name="W"]  你在想......他为什么要把你一个人留给我，留给一个魔族。
[Character]
[name="坚强的孩子"]  我没有！
[name="坚强的孩子"]  *乌萨斯粗口*！你这个怪物——
[Character(name="avg_npc_046#2")]
[name="W"]  闭嘴。
[name="W"]  ......就在这里等他。一步都不许动。
[name="W"]  否则，我现在就可以杀了你。
[Character]
[name="坚强的孩子"]  呜——
[Character(name="avg_npc_046#2")]
[name="W"]  你以为我是谁？
[name="W"]  我是凶手。
[name="W"]  是毁了这座城市，伤害你父母和朋友的凶手。
[name="W"]  ......啊，哈哈，对了。
[name="W"]  忘记你还有这把刀。那刀柄上的是萨卡兹的配饰，还染着血。
[name="W"]  你猜猜看是谁的血？
[Character]
[name="坚强的孩子"]  呜......呜呜，我，我不知道......你让他......
[Character(name="avg_npc_046#2")]
[name="W"]  哭吧，孩子是可以哭的。
[name="W"]  至于之后的死活......就要看你们的表现了。
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[name="坚强的孩子"]  他做不到的......
[Character(name="avg_npc_046#2")]
[name="W"]  是吗。
[Character]
[name="坚强的孩子"]  如果不是我把他从废墟地下挖出来，他早就......
[name="坚强的孩子"]  ......他不能没有我的。
[Character(name="avg_npc_046#2")]
[name="W"]  ......
[name="W"]  没有谁......是不能没有另一个人的。
[name="W"]  没有。
[Character]
[name="坚强的孩子"]  ......
[Character]
[Dialog]
[Blocker(a=1, r

... (全文10786字符)
```

### tutorial_act9d0_04

```
[HEADER(is_skippable=true, is_autoable=false)] 活动04关卡内剧情
[PopupDialog(dialogHead="$avatar_ines")] 等等，是敌人。
[PopupDialog(dialogHead="$avatar_hoederer")] 一处简陋的据点，一些零散的同行，他们没有注意到这里。
[PopupDialog(dialogHead="$avatar_ines")] 他们只是驻扎在这里，尚处在<@tu.kw>待命状态</>，我们应该先下手为强。
[PopupDialog(dialogHead="$avatar_hoederer")] 一旦意识到自己受到了攻击，他们就会立刻进入<@tu.kw>临战状态</>，这称不上什么空隙。
[PopupDialog(dialogHead="$avatar_ines")] 很简单，我们可以<@tu.kw>逐个逐个</>的......蚕食他们，他们不会有反抗的机会的。
[Blocker(fadetime=0.3, block=true, a=0)]
```

### tutorial_act9d0_05

```
[HEADER(is_skippable=true,is_autoable=false)] 活动05关卡内剧情
[PopupDialog(dialogHead="$avatar_hoederer")] 注意那个<@tu.kw>哨兵</>，很稀奇的配置，看来敌人队伍的规模比想象中大一些。
[PopupDialog(dialogHead="$avatar_hoederer")] 哨兵受到伤害就会立刻<@tu.kw>警告</>全队，很可惜，我们做不到无声地解决他们，他们不会轻易倒下。
[PopupDialog(dialogHead="$avatar_hoederer")] 团结在旗帜下的佣兵有着更强的作战能力自不必说，而且所有待命的敌人都会进入<@tu.kw>临战状态</>。
[PopupDialog(dialogHead="$avatar_ines")] 优先消灭尚在<@tu.kw>待命状态</>的主力军，等到旗下无人的时候，光杆司令只能任人宰割。
[Blocker(fadetime=0.3, block=true, a=0)] 
```


## 统计

- 总字符数：152633
- 对话行数：1902


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
