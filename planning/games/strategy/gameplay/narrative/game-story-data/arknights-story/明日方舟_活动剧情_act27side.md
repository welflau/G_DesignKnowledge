# 明日方舟 · 活动剧情 · act27side（33段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act27side」完整剧情脚本（33个文件，3246行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act27side
- 脚本文件数：33

### guide_act27side_after_settle

```
[HEADER(is_skippable=false, is_tutorial=true)] 商店街完成经营
[PopupDialog(dialogHead="$avatar_npc_1005")] 呼......今天的售卖过程全部完成啦。多、多亏有博士在，总体来说......非常顺利！
[PopupDialog(dialogHead="$avatar_npc_1005")] 博、博士！今天的营业圆满结束啦！明天也一起加油，努力赚钱，让汐斯塔风情街越来越繁荣吧！
```

### guide_act27side_order

```
[HEADER(is_skippable=false, is_tutorial=true)] 商店街进货引导
[Tutorial(waitForSignal="grocery_order_routed")]
[PopupDialog(dialogHead="$avatar_npc_1005")] 博、博士！您可算来啦......您问我为什么会开店？是因为诗怀雅小姐啦......
[PopupDialog(dialogHead="$avatar_npc_1005")] 她申请了一笔政府资金，用来实地考察汐斯塔风情街的商业价值，还让我来负责经营这个店铺......
[PopupDialog(dialogHead="$avatar_npc_1005")] 虽然我自学了一些店铺经营知识，但还是希望有人能来指导指导我呀......
[PopupDialog(dialogHead="$avatar_npc_1005")] 亲身实践经营一家店铺，应该会和书本上的描述有很多不一样的地方吧？比如——进货！
[PopupDialog(dialogHead="$avatar_npc_1005")] 即使现在的汐斯塔风情街有点萧条，我们还是要为可能会光临的顾客做好准备。
[Tutorial(target="grocery_order_customer", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 顾客根据喜好可以划分成饮品爱好者、餐点爱好者和纪念品爱好者。
[Tutorial(target="grocery_order_customer", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 赚的钱越多，店铺生意就越兴隆，来汐斯塔风情街观光购物的顾客也会慢慢变多的！
[Tutorial(target="grocery_order_good", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 为了迎接即将到来的顾客，营业前我们要依据不同爱好者的比例，准备好饮品、餐点、纪念品三种商品。
[Tutorial(target="grocery_order_good", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 不过......每天每种商品的总供应量是有限的，还会有三家对手店铺与我们竞争这些商品哦。
[Tutorial(target="grocery_order_price", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 进货时，依据不同的进货单价，可以采用三种竞价策略......唔，我记得分别是保守、稳健、激进！
[Tutorial(target="grocery_order_price", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 如果想要从供货商手中拿到更多的商品，就需要给出更高、更有诱惑力的进货单价哦。
[Tutorial(target="grocery_order_price", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 怎么办！对手店铺竟然和我们用了相同的策略......要不要用更高的价格进货呢？
[Tutorial(target="grocery_order_price", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 但也不要进太多货噢......每个顾客只会买一份商品，剩下的卖不掉可就糟糕啦！
[Tutorial(target="grocery_order_inquire", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 嗯？您问怎么得知对手店铺的竞价策略？诗怀雅小姐说，要在生意场上占据先机，掌握信息很重要！
[Tutorial(target="grocery_order_inquire", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 我们可以找埃尼斯先生帮忙“打探消息”，提早了解对手店铺的竞价策略哦。
[Tutorial(target="grocery_order_inquire", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 有了从对手店铺打探来的出价，我们可以判断自己店铺的竞争力，这样就能推算进多少货更合适了！
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 注意啦，“打探消息”的次数有限，每天只有四次机会。不仅在当前进货时，而且在后续售卖时，我们都需要“打探消息”，所以要谨慎做决定哦！
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 每天会刷新能“打探消息”的次数。如果当天的次数没有用完，可不会保留到下一天哦！要把握住每一个机会！
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 第一次尝试还不熟练，可以多“打探”几次，之后就是每天四次啦。
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 当然，随着赚取的消费券越来越多，我们每天“打探消息”的次数也会增加哦。
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 如果当天进货来的饮品和餐点没有卖完，剩下的都会在打烊后统一销毁。
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 不过，没卖完的纪念品可以继续售卖哦！嘿嘿......到时候可以把剩下的纪念品送给罗德岛的朋友们！
[Tutorial(target="grocery_order_inquire_detail", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 随着时间的推移，陆续会有新的饮品和餐点供货。博士，到时候我们可不能错过它们，也好给顾客们提供不同的体验呀。
```

### guide_act27side_sell

```
[HEADER(is_skippable=false, is_tutorial=true)] 商店街卖货引导
[Tutorial(waitForSignal="grocery_sell_routed")]
[Tutorial(target="grocery_sell_title", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 每天的售卖过程分成三轮，我们将依次出售饮品、餐点、纪念品。
[Tutorial(target="grocery_sell_customer", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 每一轮售卖，我们只会售卖一种商品，而且只有对应的爱好者会前来光顾哦。饮品......应该会吸引饮品爱好者前来购买吧？
[Tutorial(target="grocery_sell_slider", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 在开始售卖前，每家店铺都可以自由地对商品进行定价。如果我们的商品更便宜，就能吸引到更多的顾客来购买！
[Tutorial(target="grocery_sell_inquire", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 如果我们能知道对手店铺商品的定价，或许能帮助我们给出更具吸引力的价格哦！
[Tutorial(target="grocery_sell_inquire", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 别忘了还有埃尼斯先生帮我们“打探消息”！在售卖前，通过“打探消息”，我们能知道对手店铺中定价较高者的价格。
[Tutorial(target="grocery_sell_inquire", focusStyle="HighlightRect",           black="$f_tut_black", animStyle="Highlight", protectTime=0.5, dialogHead="$avatar_npc_1005")] 在“打探消息”的帮助下，斟酌商品定价，争取吸引足够多的顾客，把今天的库存商品全部售完吧！
```

### level_act27side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_desert_1",screenadapt="showall")]
[Delay(time=1)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15, fadetime=0.1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1.5)]
[name="广播声"]......自1097年起，受日渐活跃的火山活动影响，汐斯塔自由邦在赫尔曼·道尔科斯市长的规划之下，启动了“搬迁项目”。
[name="广播声"]预计到1099年初，超过九成的汐斯塔市民将告别火山与海滩，在移动城市上开启新生活......
[name="卡车司机"]先说好小姑娘，你给的钱只够送你到下个中转站的，后面的路你还得自己想办法。
[Dialog]
[charslot(slot="m",name="avg_npc_1015_1#1$1",duration=1)]
[delay(time=2)]
[name="低沉的少女"]嗯......我会的。
[charslot(slot="m",name="avg_npc_1015_1#1$1",focus="none")]
[name="卡车司机"]说得轻巧啊。像你这么大的孩子就敢一个人跑国外去，你知道荒地上有多危险吗？
[name="卡车司机"]为什么要去汐斯塔？瞒着家人去追喜欢的乐队？
[charslot(slot="m",name="avg_npc_1015_1#8$1",focus="m")]
[name="低沉的少女"]去找工作。
[charslot(slot="m",name="avg_npc_1015_1#8$1",focus="none")]
[name="卡车司机"]从哥伦比亚跑去汐斯塔工作，你简直像是与世隔绝了七十年。
[name="卡车司机"]早些时候那里确实算是个发财的好地方，听说在火山上随手抓一把土都能捡到黑曜石。
[name="卡车司机"]但现在要想找份工作过活，怎么都是哥伦比亚的机会多一点。
[charslot(slot="m",name="avg_npc_1015_1#1$1",focus="m")]
[name="低沉的少女"]大学毕业前，我签了一家建筑公司，实习期刚结束的时候，碰上了严重的工程事故。公司要找人顶罪，就把错误都推在我身上。
[charslot(slot="m",name="avg_npc_1015_1#2$1",focus="m")]
[name="低沉的少女"]履历上有了这个记录，我找不到别的工作，只能跟着一些小型拆迁队干活。他们使用源石炸药操作不当，我被误伤，感染了矿石病。
[name="低沉的少女"]本来想尽量留在移动城市里，可是交医疗保险的时候遇到了骗子，最后一点积蓄也没了。
[charslot(slot="m",name="avg_npc_1015_1#2$1",focus="none")]
[name="卡车司机"]......是够倒霉的。
[Dialog]
[charslot]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=0.5)]
[name="广播声"]深受矿石病的折磨？这无法阻挡你成为联邦的奠基人，边疆的开拓者！
[name="广播声"]拓荒队，为每一个属于哥伦比亚的孩子，提供追求繁荣富足未来的机会......
[charslot(slot="m",name="avg_npc_1015_1#1$1",focus="m")]
[name="低沉的少女"]我觉得自己是该换个地方生活了......爷爷说过，汐斯塔是个很美丽的地方。
[charslot(slot="m",name="avg_npc_1015_1#1$1",focus="none")]
[name="卡车司机"]好吧，小姑娘。祝你在新的地方运气会好点。
[charslot(slot="m",name="avg_npc_1015_1#9$1",focus="m")]
[stopmusic(fadetime=1.5)]
[name="低沉的少女"]我相信会的。
[Dialog]
[charslot]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=0.5)]
[name="广播声"]我迷失了我的方向♪
[name="广播声"]我迷失了我的路♪
[Dialog]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=0.5)]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=0.7)]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1)]
车载广播的声音变得怪异，音响的啸叫与雪花音代替了原本舒缓的歌谣。 
这辆货运卡车忽然脱了力，在荒野中缓缓停了下来。
[name="卡车司机"]见鬼了，怎么回事？
[Dialog]
[PlaySound(key="$sportscarstart", volume=1,channel="1")]
[Delay(time=0.65)]
[StopSound(channel="1")]
[Delay(time=1.5)]
[PlaySound(key="$sportscarstart", volume=1,channel="1")]
[Delay(time=0.65)]
[StopSound(channel="1")]
[Delay(time=1.5)]
[PlaySound(key="$sportscarstart", volume=1,channel="1")]
[Delay(time=0.8)]
[StopSound(channel="1")]
[PlaySound(key="$d_avg_engingivup",volume=1,channel="2")]
[CameraShake(duration=1, xstrength=40, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=false)]
[Delay(time=2.5)]
[name="卡车司机"]......
[charslot(slot="m",name="avg_npc_1015_1#3$1",focus="m")]
[name="低沉的少女"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1005_1#10$1")]
[charslot(slot="r",name="avg_npc_994_1#1$1")]
[Background(image="41_g9_purewhitevolcano_inside",screenadapt="showall")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1005_1#10$1",focus="l")]
[name="雪雉"]老板，这个特价甜点可以再来一份吗？
[charslot(slot="r",name="avg_npc_994_1#1$1",focus="r")]
[name="时髦的店主"]当然！或者你想不想尝尝别的口味？
[charslot(slot="l",name="avg_npc_1005_1#4$1",focus="l")]
[name="雪雉"]汐斯塔不愧是旅游胜地，物价和哥伦比亚完全不一样啊......
[charslot(slot="l",name="avg_npc_1005_1#11$1",focus="l")]
[name="雪雉"]这里的点心看起来都好精致，鸡尾酒看起来也好漂亮......
[charslot(slot="r",name="avg_npc_994_1#5$1",focus="r")]
[name="时髦的店主"]当然，这些可都是我原创的，别的地方可吃不到。
[name="时髦的店主"]而且我们这的每一款鸡尾酒都有一段故事哦，像这个“肉豆蔻沙滩”......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#10$1",focus="m")]
[name="埃尼斯"]喂喂——
[name="埃尼斯"]坐在那边的那两位，他们也是朋友？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4106_bryota_1#10$1",focus="r")]
[charslot(slot="r",name="avg_npc_1005_1#10$1",focus="r")]
[name="雪雉"]嗯，大家都是龙门人，也是一家公司的同事，关系很好的。
[charslot(slot="l",name="avg_4106_bryota_1#20$1",focus="l")]
[name="埃尼斯"]可是为什么，他们俩现在看起来像是随时会打起来一样......
[charslot(slot="r",name="avg_npc_1005_1#7$1",focus="r")]
[name="雪雉"]好朋友，也是会吵架的吧......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1033_swire2_1#8$1",focus="r")]
[charslot(slot="r",name="avg_npc_990_1#10$1",focus="r")]
[name="拜松"]没想到诗怀雅局长会亲自来到这里。
[charslot(slot="l",name="avg_1033_swire2_1#8$1",focus="l")]
[name="诗怀雅"]近卫局也是有年假的，合理地使用假期，这没什么问题吧？
[charslot(slot="r",name="avg_npc_990_1#10$1",focus="r")]
[name="拜松"]诗怀雅小姐，我很清楚您来到这里的目的。
[charslot(slot="r",name="avg_npc_990_1#3$1",focus="r")]
[name="拜松"]不得不说，在新地块建设和商业街改建工程的竞标名单上，见到您和您家族集团的名字，我很意外。
[charslot(slot="r",name="avg_npc_990_1#3$1",focus="none")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="埃尼斯"]咳咳咳咳咳——
[name="雪雉"]埃尼斯先生！您、您怎么了！
[name="埃尼斯"]不小心吓......不是，呛到了......
[charslot(slot="l",name="avg_1033_swire2_1#6$1",focus="l")]
[name="诗怀雅"]嗯哼，我倒是早就听说了峯驰物流和汐斯塔的合作，你们也是看中了这片地块的位置，想要建设物流中心吧。欧厄尔呢？
[charslot(slot="r",name="avg_npc_990_1#10$1",focus="r")]
[name="拜松"]现在是由我来全权负责这次的项目。
[name="拜松"]您可以理解为，我代表的“峯联贸易”是峯驰物流旗下的子公司，但完全不依赖峯驰物流的资源。
[charslot(slot="l",name="avg_1033_swire2_1#10$1",focus="l")]
[name="诗怀雅"]完全不依赖家里的资源，还真是典型的富家子弟会说的话。所以，你这次也是骑自行车来的？
[charslot(slot="r",name="avg_npc_990_1#3$1",focus="r")]
[name="拜松"]诗怀雅小姐，这样的场合，还请不要打趣......
[charslot(slot="l",name="avg_1033_swire2_1#8$1",focus="l")]
[name="诗怀雅"]好啊，既然是商业会谈，我们就开门见山地说吧。
[name="诗怀雅"]这一次的建设项目很有前景，许多双眼睛都在盯着。我当然也很感兴趣。
[name="诗怀雅"]峯驰物流既然还没有与汐斯塔签订正式的合同，那我们还是处于公平的竞标关系。

... (全文26401字符)
```

### level_act27side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g4_siestanewstreet_n",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$EyjafjallaDream_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_180_amgoat_1#3$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="m",name="avg_180_amgoat_1#3$1",focus="m")]
[name="阿黛尔"]是谁在说话......？
[Dialog]
[charslot]
[name="？？？"]我啊，是我。
[name="？？？"]唉，总觉得你应该已经习惯我在了，但想起来好像还从来没有这样对你说过话。不对，还是说过来着，唉，我已经忘了。
[Dialog]
[charslot]
[charslot(slot="r",name="avg_180_amgoat_1#5$1")]
[charslot(slot="l",name="avg_npc_1014_1#1$1",posfrom="0,650",posto="0,650",duration=0,isblock=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_dream", volume=1)]
[charslot(slot="l",posfrom="0,650",posto="0,0",duration=8,isblock=false)]
[Delay(time=6)]
[PlaySound(key="$d_avg_blcksheepborn", volume=1)]
[charslot(slot="l",action="jump",power=30,times=1,duration=3.5,isblock=true)]
像是一朵厚重的云从夜空里轻飘飘地落了下来——
浑身毛绒绒的生物，缓慢旋转着身体，现身在阿黛尔的眼前。
有一些轻巧，又有一些滑稽地落在了路边的信箱上。
[Dialog]
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="r")]
[charslot(slot="r",name="avg_180_amgoat_1#5$1",focus="r")]
[name="阿黛尔"]啊——
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="外形奇特的生物"]你好？晚上好？
[charslot(slot="r",name="avg_180_amgoat_1#9$1",focus="r")]
[name="阿黛尔"]......小黑羊？
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="外形奇特的生物"]你管我叫小黑羊？算了，也行吧。
[name="外形奇特的生物"]为什么这么惊讶？我们也算见过的，应该是见过的。
[charslot(slot="r",name="avg_180_amgoat_1#9$1",focus="r")]
[name="阿黛尔"]抱歉，我以为，你......您是不会说话的......
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="外形奇特的生物"]平时是不太会说话的。应该说，只有我会这样讲话，至于那些分身，他们大概是不太愿意和人交流吧。或者是还没有学会？
[name="外形奇特的生物"]算了，也不重要。现在我遇到了你，直接来找你说就好。
[charslot(slot="r",name="avg_180_amgoat_1#5$1",focus="r")]
[name="阿黛尔"]您......知道我？
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="外形奇特的生物"]该怎么说，我也算看着你长大的？
[name="外形奇特的生物"]不不不，我可没有偷窥别人的习惯。就是一种，简单且单纯的，陪伴。总之，我当然是对你有印象的。
[name="外形奇特的生物"]不知道在这里遇见你算不算巧合，但毕竟是个难得的机会。
[charslot(slot="r",name="avg_180_amgoat_1#9$1",focus="r")]
[name="阿黛尔"]对不起......我好像有点弄不清状况......
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="外形奇特的生物"]当然，我能理解，小小的人类总是有问不完的问题——不用着急，我都会回答的。
[name="外形奇特的生物"]来聊聊吧，现在有时间吗？我不太确定你这个年纪的孩子还用不用赶在某个时间点前回家。
[charslot(slot="r",name="avg_180_amgoat_1#10$1",focus="r")]
[name="阿黛尔"]我已经不是小孩子了......！
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="外形奇特的生物"]太好了，那就是说你有时间咯，想不想跟我去散散步？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_991_1#1$1")]
[charslot(slot="r",name="avg_npc_992_1#1$1")]
[Background(image="41_g9_purewhitevolcano_inside",screenadapt="showall")]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]大水坑、大温泉，还有白白的烟。
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[name="小男孩"]你画的不对！火山冒出来的是灰色的烟，汐斯塔可不是这个样子的。
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]可是，那边已经不再是汐斯塔了呀。
[name="小女孩"]我们现在待的地方才是汐斯塔，大高楼那边，可都是白色的烟！
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[name="小男孩"]这里是汐斯塔，可是以前的汐斯塔，也还是汐斯塔啊。
[name="小男孩"]唔，我知道了，就叫它老汐斯塔吧。
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]现在的汐斯塔，应该是老汐斯塔的孩子。
[name="小女孩"]老汐斯塔就像爸爸一样，虽然现在离我们有点远......但总有一天会回来，还会给我们带礼物！
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4106_bryota_1#1$1",duration=1.5)]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[Delay(time=2.5)]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=2)]
[charslot(slot="r",posfrom="0,0",posto="100,0",duration=2)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]你们要什么礼物？
[Dialog]
[charslot(slot="l",name="avg_npc_991_1#1$1",posfrom="-100,0",posto="-100,0",focus="l")]
[name="小男孩"]埃尼斯！
[charslot(slot="r",name="avg_npc_992_1#1$1",posfrom="100,0",posto="100,0",focus="r")]
[name="小女孩"]打工结束了吗？
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]嘘——小点声，哈莉已经睡着了。
[name="埃尼斯"]小家伙们，上次我和你们说什么来着？
[charslot(slot="l",name="avg_npc_991_1#1$1",posfrom="-100,0",posto="-100,0",focus="l")]
[name="小男孩"]不要晚上乱跑，不可以去移动城市外的箱子地块......
[charslot(slot="r",name="avg_npc_992_1#1$1",posfrom="100,0",posto="100,0",focus="r")]
[name="小女孩"]还有不可以在画纸之外的地方乱涂乱画......
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]那我在餐厅后墙上看到的大作《赫尔曼是贝壳脑袋》，是谁画上去的？
[charslot(slot="l",name="avg_npc_991_1#1$1",posfrom="-100,0",posto="-100,0",focus="l")]
[name="小男孩"]可是大人们都在这么说......
[charslot(slot="m",name="avg_4106_bryota_1#14$1",focus="m")]
[name="埃尼斯"]嗯......实际上，大人们也不总是对的。所以我们三人的探险队才是有意义的，我们能发现他们发现不了的宝物。
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]但是在那之前，明天把墙壁清理干净好不好？
[charslot(slot="l",name="avg_npc_991_1#1$1",posfrom="-100,0",posto="-100,0",focus="l")]
[name="小男孩"]好吧......
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]那看在你们承认错误的分上——
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="0,-30",duration=1.5,isblock=true)]
少年伸出手，三枚精致的小土偶静静躺在手心，小巧精致，脸上的表情栩栩如生，和桌子上摆着的全家福中洋溢着笑容的脸庞一模一样。
[charslot(slot="m",name="avg_4106_bryota_1#1$1",posfrom="0,-30",posto="0,-30",focus="m")]
[name="埃尼斯"]这就是我们探险小分队新的信物了，一人一个！
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]这是从哪来的？
[charslot(slot="m",name="avg_4106_bryota_1#5$1",posfrom="0,-30",posto="0,-30",focus="m")]
[name="埃尼斯"]是我自己做的哦，我说过，我会魔法。
[Dialog]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="all")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4106_bryota_1#6$1",posfrom="0,-30",posto="0,-30",focus="m")]
[name="埃尼斯"]唔......不喜欢？


... (全文21532字符)
```

### level_act27side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g9_purewhitevolcano_inside",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$transmission", volume=1)]
[name="广播声"]早上好亲爱的汐斯塔居民们，今天是1099年8月16日。
[name="广播声"]空气湿度75%，能见度18公里，风向南西南。
[name="广播声"]距离预计的火山爆发时间，还有十五天......
[name="广播声"]虽然是个难得的好天气，但还是需要再次提醒大家，不要随意靠近移动城市外的海岸戏水。
[name="广播声"]要时刻记得，看似平静的海面下还有看不见的暗礁和暗流，就和平静生活里数不清的麻烦一样不是吗？
[name="广播声"]好了，在这个阳光明媚的清晨，各位的心情怎么样呢？让我们用一首剩骨头乐队的《Life Always Goes On》迎来美好的新的一天吧！
[dialog]
[PlaySound(key="$d_avg_electricguitar",channel="2",volume=0.6)]
[Delay(time=1.5)]
[name="广播声"]早上七点，我被拽离梦乡，梦中我还在与追求的人拥吻♪
[name="广播声"]睁开眼看到的还是让人厌倦的景象，太阳和麻烦事一起找上我♪
[dialog]
[PlaySound(key="$d_avg_doorbell",channel="1",volume=1)]
[PlaySound(key="$dooropenquite",channel="2",volume=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_994_1#1$1",duration=1.5)]
[delay(time=2)]
[name="时髦的店主"]让我看看今天拜访这家小店的第一位客人......哦，真是不出意料。
[name="时髦的店主"]这么阳光明媚的早晨，就没有比那个火山快要爆发更好的消息吗？
[Dialog]
[charslot]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_997_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot]
[charslot(slot="l",name="avg_npc_994_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_997_1#2$1",focus="r")]
[name="疲惫的政府职员"]哈莉太太，如果您能适当放下一些执念的话，我带来的也是好消息。
[charslot(slot="l",name="avg_npc_994_1#5$1",focus="l")]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[name="哈莉"]不要这么叫我，我还没有老到被你当长辈的年纪。
[name="哈莉"]看在今天好天气的分上，科斯达，我可以给你几分钟的时间——你这次带来的又是什么说辞？
[charslot(slot="r",name="avg_npc_997_1#6$1",focus="r")]
[name="科斯达"]就业补贴和免税......？
[charslot(slot="l",name="avg_npc_994_1#2$1",focus="l")]
[name="哈莉"]得了吧。
[name="哈莉"]那能不能先说说，我们搬去市中心以后，能就什么业？
[charslot(slot="r",name="avg_npc_997_1#1$1",focus="r")]
[name="科斯达"]总不会比等在这条没有游客来的商业街更糟。
[charslot(slot="r",name="avg_npc_997_1#5$1",focus="r")]
[name="科斯达"]哈莉女士，我想我必须要提醒您的是，这条街上不止您一户居民......也不是每个人都不愿意在这份意向书上签字。
[charslot(slot="l",name="avg_npc_994_1#4$1",focus="l")]
[name="哈莉"]很好，那同样的，也就不会只有我来骂你了。
[name="哈莉"]给市政厅一个建议，你们最好还是弄清楚住在这里的人们最想要的是什么。
[name="哈莉"]当初赫尔曼告诉我们，这要命的火山马上就要爆发了，结果怎么样呢？两年了，火山还在那里，但汐斯塔的每个人都被折腾得够呛。
[name="哈莉"]哦，当然，像你这种在市政厅找到了体面工作的人除外。
[name="哈莉"]这家“纯白火山”不只是一间房子，还是我和三个孩子的家。
[name="哈莉"]我们已经因为火山搬过一次家了，赫尔曼休想让我们再搬一次。尤其是我不确定他在每一次要求我们搬家的时候是否清醒。
[charslot(slot="r",name="avg_npc_997_1#6$1",focus="r")]
[name="科斯达"]哈莉女士，这不是某个人的家——
[charslot(slot="r",name="avg_npc_997_1#6$1",focus="none")]
[name="广播声"]我要让你知道，这是我的地盘，我的生活♪
[name="广播声"]不要告诉我该怎么做，再说一句就干掉你，干掉你♪
[charslot(slot="l",name="avg_npc_994_1#1$1",focus="l")]
[name="哈莉"]多棒的音乐，我喜欢这个歌词。
[charslot(slot="r",name="avg_npc_997_1#1$1",focus="r")]
[name="科斯达"]......
[charslot(slot="l",name="avg_npc_994_1#5$1",focus="l")]
[name="哈莉"]好啦，科斯达。噢，应该叫“尊敬的市政厅老爷”，请回吧。
[Dialog]
[stopmusic(fadetime=1)]
[charslot(slot="r",name="avg_npc_997_1#1$1",focus="r")]
[delay(time=3)]
[charslot(slot="r",posfrom="0,0",posto="150,0",duration=2,focus="r")]
[charslot(slot="r",afrom=1,ato=0,duration=1.5,focus="r")]
[PlaySound(key="$dooropenquite",channel="2",volume=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_994_1#2$1",focus="l")]
[Delay(time=2)]
[PlaySound(key="$d_avg_doorbell",channel="1",volume=1)]
[PlaySound(key="$dooropenquite",channel="2",volume=1)]
[charslot(slot="l",name="avg_npc_994_1#3$1",focus="l")]
[Delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_993_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="伯德"]冒昧打扰，请问......你们这里还招驻店歌手吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g8_siestavolcanomuseum_inside",screenadapt="showall")]
[PlaySound(key="$d_avg_crwddiscuss_inside",loop=true,channel="1",volume=0.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_180_amgoat_1#8$1",focus="m")]
[name="阿黛尔"]大家现在看到的橱窗里的生物，就是“汐斯塔火山源石虫”。
[name="阿黛尔"]这种源石虫长时间生活在火山环境中，外形和习性都已与其他地区的源石虫有了显著差异，生物学家将它们当作特殊种类来研究。
[charslot(slot="m",name="avg_180_amgoat_1#12$1",focus="m")]
[name="阿黛尔"]很神奇的是，这些源石虫虽然离开了火山，生活在博物馆的恒温箱中，但它们休眠与活动的规律，还是符合汐斯塔火山能量的起落。
[charslot(slot="m",name="avg_180_amgoat_1#8$1",focus="m")]
[name="阿黛尔"]这正是生物与生态环境相互影响、相互依赖的表现......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot]
[StopSound(channel="1",fadetime=1.5)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_highheelfts",channel="2",volume=1)]
[charslot(slot="m",name="avg_1033_swire2_1#7$1",duration=1.5)]
[Delay(time=2.5)]
[name="诗怀雅"]不错嘛，艾雅法拉。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1033_swire2_1#7$1",focus="r")]
[charslot(slot="r",name="avg_180_amgoat_1#5$1",focus="r")]
[name="阿黛尔"]啊......诗怀雅小姐！你是来汐斯塔度假的吗？
[charslot(slot="l",name="avg_1033_swire2_1#7$1",focus="l")]
[name="诗怀雅"]算是吧。好不容易有了假期，当然要来尽情享受夏天啊。
[name="诗怀雅"]你呢？我好像还是头一回见到你作为研究员的一面。
[charslot(slot="r",name="avg_180_amgoat_1#8$1",focus="r")]
[name="阿黛尔"]我只是来协助整理博物馆的资料啦......
[charslot(slot="l",name="avg_1033_swire2_1#9$1",focus="l")]
[name="诗怀雅"]但游客们听得都很认真啊，还有人在记笔记呢。而且，我也有问题想问一下你。
[charslot(slot="l",name="avg_1033_swire2_1#7$1",focus="l")]
[name="诗怀雅"]艾雅法拉，你愿不愿意再给我也讲讲这些展品呢？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[charslot(slot="m",name="avg_180_amgoat_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_180_amgoat_1#1$1",focus="m")]
[name="阿黛尔"]好奇怪啊，比起这些地质展品，诗怀雅小姐好像更关心博物馆周边的地价呢......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_blcksheepborn",channel="1",volume=1)]
[charslot(slot="m",name="avg_npc_1014_1#1$1",posfrom="

... (全文22955字符)
```

### level_act27side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g1_siestacommercialstreet_d",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_991_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_992_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[name="小男孩"]今天去哪里玩呢？我们已经被禁止在温泉店里游泳了......多叫几个人去箱子地块捉迷藏怎么样？
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]埃尼斯说了不让我们去海边。我还想再去火山博物馆看看，上次还没找到爸爸呢。
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[name="小男孩"]别找了，找不到的......对了，埃尼斯今天在哪里打工？
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]今天是星期三，下午三点，应该在帮汤姆爷爷看店。
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="all")]
[name="小男孩&小女孩"]冷饮店！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="l")]
[name="小男孩"]我要巧克力味的。
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]我要草莓味的。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]好，好。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="l")]
[name="小男孩"]等一下，汤姆爷爷今天是不是做了新口味？蛋糕味的冰淇淋是什么味道？可以多给我们一个尝尝吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]汤姆爷爷说过，每个小孩子每天只有一个球的份额。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="l")]
[name="小男孩"]但你从来不吃冰淇淋的，可以把你的那一份让给我们吗？
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]不要这样，埃尼斯也很辛苦......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#11$1",focus="m")]
[name="埃尼斯"]不不，我可不算小孩子了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]但是今天天气很热，冰淇淋化得要更快一点，吃到嘴里就不满一个了，这不公平。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]是啊，怎么办呢？
[name="埃尼斯"]今天天气很热，蛋糕味的冰淇淋看起来也很好吃对不对？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="all")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="all")]
[name="小男孩&小女孩"]（眼巴巴）
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]嗯......如果你们保证在晚饭前回家并且帮哈莉摆好餐具的话，我就瞒着汤姆爷爷多给你们一个怎么样？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="all")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="all")]
[name="小男孩&小女孩"]好——
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4106_bryota_1#20$1",focus="m")]
[name="埃尼斯"]每次都这么说，希望你们吃晚饭的时候能藏好一点啊......
[Dialog]
[charslot]
一个蛋筒冰淇淋慢悠悠地在小女孩的眼前飘过。小女孩愣了神，勺子里好大一块冰淇淋，在烈日下融化了。
草莓味的冰淇淋滴落在地面上，留下一摊水迹。不见身形的生物踩了上去，显现了它的脚印。
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]......咦？
[name="小女孩"]刚才好像有一只冰淇淋跑走了。
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[name="小男孩"]冰淇淋跑了？
[charslot(slot="r",name="avg_npc_992_1#1$1",focus="r")]
[name="小女孩"]好像也是草莓味的。
[charslot(slot="l",name="avg_npc_991_1#1$1",focus="l")]
[name="小男孩"]如果抓到它的话是不是可以多吃一个球了？
[Dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_993_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="伯德"]我也可以要一份冰淇淋吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4106_bryota_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="l")]
[name="埃尼斯"]三金券。
[charslot(slot="r",name="avg_npc_993_1#4$1",focus="r")]
[name="伯德"]咦，我不能免费领吗？真可惜。
[charslot(slot="l",name="avg_4106_bryota_1#20$1",focus="l")]
[name="埃尼斯"]别开玩笑了女士，这里还是要做生意的。
[charslot(slot="r",name="avg_npc_993_1#8$1",focus="r")]
[name="伯德"]那请给我咖啡味的。
[Dialog]
[charslot(slot="l",name="avg_4106_bryota_1#1$1",focus="l")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="l",posfrom="0,0",posto="50,0",duration=0.8,isblock=true)]
[charslot(slot="l",posfrom="50,0",posto="0,0",duration=0.8,isblock=true)]
[charslot(slot="l",name="avg_4106_bryota_1#1$1",focus="l")]
[name="埃尼斯"]谢谢惠顾。
[name="埃尼斯"]这个时候还有外国游客来汐斯塔，真稀奇。
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]可能是你低估了这里的魅力。
[name="伯德"]你为什么没有在享受这个夏日呢？在我的家乡，像你这个年纪的孩子都应该在大街小巷疯跑。
[charslot(slot="r",name="avg_npc_993_1#8$1",focus="r")]
[name="伯德"]当一个受欢迎的好哥哥不容易吧。
[charslot(slot="l",name="avg_4106_bryota_1#1$1",focus="l")]
[name="埃尼斯"]生活所迫。
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]你会什么乐器吗？
[charslot(slot="l",name="avg_4106_bryota_1#6$1",focus="l")]
[name="埃尼斯"]乐器？我连歌唱课都没有上过......
[charslot(slot="l",name="avg_4106_bryota_1#1$1",focus="l")]
[name="埃尼斯"]拇指琴......算吗？
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]唔......我觉得你的气质，会很适合萨克斯。
[charslot(slot="l",name="avg_4106_bryota_1#11$1",focus="l")]
[name="埃尼斯"]哈哈，听起来不像是我的经济能力承担得起的乐器啊。
[charslot(slot="r",name="avg_npc_993_1#8$1",focus="r")]
[name="伯德"]我今天心情不错，因为找到了一份新工作。如果我请你一杯的话，可以再多和我聊聊吗？
[charslot(slot="l",name="avg_4106_bryota_1#1$1",focus="l")]
[name="埃尼斯"]抱歉，时间到了，我要去做下一份工作了。
[name="埃尼斯"]要是下次还想一起聊天的话，就来我家的店吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g1_siestacommercialstreet_d",screenadapt="showall")]
[charslot(slot="r",name="avg_npc_990_1#1$1")]
[charslot(slot="l",name="avg_npc_022")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_022",focus="l")]

... (全文22340字符)
```

### level_act27side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g3_siestanewstreet_d",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_1033_swire2_1#8$1",duration=1.5)]
[delay(time=2)]
[name="诗怀雅"]没认错的话，这里是罗德岛驻汐斯塔办事处？
[charslot(slot="m",name="avg_4106_bryota_1#8$1",focus="m")]
[name="埃尼斯"]你怎么知道——
[charslot(slot="m",name="avg_1033_swire2_1#8$1",focus="m")]
[name="诗怀雅"]很巧，我恰好认识一些罗德岛的朋友。
[name="诗怀雅"]你不是在做旅游向导吗？矿石病制药公司的驻地总该不是旅游地点吧？
[charslot(slot="m",name="avg_4106_bryota_1#11$1",focus="m")]
[name="埃尼斯"]我是送客人到这里......
[charslot(slot="m",name="avg_1033_swire2_1#5$1",focus="m")]
[name="诗怀雅"]这样的借口还是省省吧。
[name="诗怀雅"]不管是什么原因，作为一个矿石病人隐藏自己的身份都是很危险的事。就算在汐斯塔，这也是违法行为吧？
[charslot(slot="m",name="avg_4106_bryota_1#11$1",focus="m")]
[name="埃尼斯"]我当然知道！
[charslot(slot="m",name="avg_4106_bryota_1#20$1",focus="m")]
[name="埃尼斯"]可我有什么办法......
[charslot(slot="m",name="avg_1033_swire2_1#5$1",focus="m")]
[name="诗怀雅"]所以你打那么多份工，还有从我这赚的钱，都是为了治病？
[charslot(slot="m",name="avg_4106_bryota_1#20$1",focus="m")]
[name="埃尼斯"]......还有家人。
[name="埃尼斯"]我自己怎样都好，可我担心我走了，他们的生活会过不下去。
[charslot(slot="m",name="avg_4106_bryota_1#2$1",focus="m")]
[name="埃尼斯"]我只是需要一点时间，等家里的店搬迁完，能有新的出路......
[charslot(slot="m",name="avg_1033_swire2_1#4$1",focus="m")]
[name="诗怀雅"]唔......
[charslot(slot="m",name="avg_4106_bryota_1#2$1",focus="m")]
[name="埃尼斯"]别这么看着我，我可没有卖惨博同情的意思。
[charslot(slot="m",name="avg_1033_swire2_1#6$1",focus="m")]
[name="诗怀雅"]我只是想起来，之前我算了算，就算按这里出租车的价格，那天你也多收了我不少金券。
[charslot(slot="m",name="avg_4106_bryota_1#10$1",focus="m")]
[name="埃尼斯"]你不也骗我说你是普通游客来着......
[charslot(slot="m",name="avg_1033_swire2_1#7$1",focus="m")]
[name="诗怀雅"]之前还觉得你文文弱弱，没想到你还挺伶牙俐齿的？
[charslot(slot="m",name="avg_4106_bryota_1#10$1",focus="m")]
[name="埃尼斯"]你到底想怎么样？
[charslot(slot="m",name="avg_1033_swire2_1#7$1",focus="m")]
[name="诗怀雅"]我们来做个交易吧。
[name="诗怀雅"]你也见到了，那天在酒吧里和我谈生意的竞争对手，峯驰物流的家伙。
[name="诗怀雅"]我准备和他竞争那一片商业街区的改建权，但他是主场作战，我没有优势，所以需要一些本地人作为帮手。
[charslot(slot="m",name="avg_1033_swire2_1#9$1",focus="m")]
[name="诗怀雅"]只要你答应帮我做点事，我就当今天从来没有见过你，怎么样？
[charslot(slot="m",name="avg_4106_bryota_1#13$1",focus="m")]
[name="埃尼斯"]你威胁我——
[charslot(slot="m",name="avg_1033_swire2_1#9$1",focus="m")]
[name="诗怀雅"]别说这么难听嘛，就当互相帮助？老规矩，报酬不会少的。
[charslot(slot="m",name="avg_4106_bryota_1#14$1",focus="m")]
[name="埃尼斯"]我可不准备接受你的施舍......
[charslot(slot="m",name="avg_1033_swire2_1#7$1",focus="m")]
[name="诗怀雅"]我也不准备无缘无故地去施舍陌生人，这是伪善。我只想寻求公平的交易。
[charslot(slot="m",name="avg_4106_bryota_1#17$1",focus="m")]
[name="埃尼斯"]那你想要干什么......
[charslot(slot="m",name="avg_1033_swire2_1#7$1",focus="m")]
[name="诗怀雅"]我是合法的商人，强买强拆的事是绝对不会做的。除此之外，我的风格是尽可能寻求双赢。
[name="诗怀雅"]说起来简单，但改建这种事肯定少不了各种纠纷。不过我保证，会比峯驰物流的家伙做得更好。
[name="诗怀雅"]看在我们已经有缘合作过一次的分上，要不要考虑投票支持我一下？
[charslot(slot="m",name="avg_4106_bryota_1#14$1",focus="m")]
[name="埃尼斯"]我只想让我家的那间酒吧平平稳稳地拆掉就够了......
[charslot(slot="m",name="avg_1033_swire2_1#9$1",focus="m")]
[name="诗怀雅"]那我们就达成交易了。
[charslot(slot="m",name="avg_1033_swire2_1#8$1",focus="m")]
[name="诗怀雅"]对了，还是要叮嘱一句。
[name="诗怀雅"]就算有再要紧的事，矿石病的治疗还是拖延不得的，你还是早做打算为好。
[charslot(slot="m",name="avg_4106_bryota_1#20$1",focus="m")]
[name="埃尼斯"]你和我说了这么多......你就不介意和感染者这样打交道？
[charslot(slot="m",name="avg_1033_swire2_1#8$1",focus="m")]
[name="诗怀雅"]......
[charslot(slot="m",name="avg_1033_swire2_1#6$1",focus="m")]
[name="诗怀雅"]我有一个朋友，也是感染者。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g8_siestavolcanomuseum_inside",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$radio", volume=1)]
临近闭馆，博物馆里已经没有游客。讲解的录音还在循环播放，空旷的展厅里只剩巨大的山岩沉默。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="“瑙曼夫妇为我们留下了数以千计的照片、标本......”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“乌纳火山周边村落的重建......”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“他们走过百多座火山，足迹遍布各个国家与地区......”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_180_amgoat_1#1$1",focus="m")]
[name="阿黛尔"]......
[Dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot="r",name="avg_npc_991_1#1$1",duration=1.5)]
[charslot(slot="l",name="avg_npc_992_1#1$1",duration=1.5)]
[Delay(time=2)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[charslot(slot="r",name="avg_npc_991_1#1$1",focus="r")]
[name="小男孩"]你真的看到了吗？
[charslot(slot="l",name="avg_npc_992_1#1$1",focus="l")]
[name="小女孩"]是真的！我亲眼看见那个冰淇淋跑进来的......
[charslot(slot="r",name="avg_npc_991_1#1$1",focus="r")]
[name="小男孩"]我看你就是想来博物馆吧。
[name="小男孩"]都说了找不到的，我怀疑他在骗我们，他根本没去过那么多地方......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_996_1#10$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_996_1#10$1",focus="m")]
[name="卡恩"]现在已经停止入馆了，你们是怎么进来的？
[charslot(slot="m",name="avg_npc_991_1#1$1",focus="m")]
[name="胆怯的小男孩"]对不起......我们这就走。
[charslot(slot="m",name="avg_npc_992_1#1$1",focus="m")]
[name="天真的小女孩"]请问你们有见过我爸爸吗？
[charslot(slot="m",name="avg_npc_996_1#10$1",focus="m")]
[name="卡恩"]你们的爸爸？
[charslot(slot="m",name="avg_npc_992_1#1$1",focus="m")]
[name="天真的小女孩"]我们在找一个......找一个......好像是叫探险家？
[name="天真的小女孩"]爸爸去过很多地方！在他寄来的照片上，我们见过火山、雪山，还有移动城市里的山......
[name="天真的小女孩"]火山博物馆里可能会有他的照片！
[charslot(slot="m",name="avg_npc_996_1#1$1",focus="m")]
[name="卡恩"]你们的父亲叫什么名字？
[charslot(slot="m",name="avg_npc_992_1#1$1",focus="m")]
[name="天真的小女孩"]他叫查克！
[charslot(slot="m",name="avg_npc_996_1#10$1",focus="m")]
[name="卡恩"]我没有听说过叫这个名字的火山学家。你们应该是找错了地方。
[charslot(slot="m",name="avg_180_amgoat_1#8$1",focus="m")]
[name="阿黛尔"]我可能知道你的爸爸

... (全文28584字符)
```

### level_act27side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g4_siestanewstreet_n",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$EyjafjallaDream_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_1008_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1011_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_1008_1#1$1",focus="l")]
[name="着急的生物"]找到了吗？
[charslot(slot="r",name="avg_npc_1011_1#1$1",focus="r")]
[name="迷糊的生物"]找到了找到了。
[name="迷糊的生物"]是在羽兽唱歌的时候找到的。
[charslot(slot="l",name="avg_npc_1008_1#1$1",focus="l")]
[name="着急的生物"]今天的天气怎么样？
[charslot(slot="r",name="avg_npc_1011_1#1$1",focus="r")]
[name="迷糊的生物"]在坏事发生前都是好的。
[charslot(slot="l",name="avg_npc_1008_1#1$1",focus="l")]
[name="着急的生物"]时间很紧急，我们现在马上就要开始聚会。
[name="着急的生物"]嘿，你怎么才来？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_1016_agoat2_1#4$2",focus="m")]
[name="阿黛尔"]......我？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1008_1#1$1",focus="m")]
[name="着急的生物"]不用多说，我一眼就看得出，你和那些平庸的人不太一样。
[name="着急的生物"]我建议你加入我们的大计划。
[charslot(slot="m",name="avg_1016_agoat2_1#4$2",focus="m")]
[name="阿黛尔"]计划？是要做什么？
[charslot(slot="m",name="avg_1016_agoat2_1#2$2",focus="m")]
[name="阿黛尔"]这里是哪......我为什么穿着，妈妈的衣服？
[charslot(slot="m",name="avg_npc_1008_1#1$1",focus="m")]
[name="着急的生物"]我们要找到自己最喜欢的东西，把它背在身上，再也不拿下来。
[charslot(slot="m",name="avg_npc_1011_1#1$1",focus="m")]
[name="迷糊的生物"]沉甸甸的，直不起腰，但是很重要！
[charslot(slot="m",name="avg_npc_1008_1#1$1",focus="m")]
[name="着急的生物"]你的背上为什么什么都没有？
[charslot(slot="m",name="avg_npc_1011_1#1$1",focus="m")]
[name="迷糊的生物"]不对，不对，她的背上是有的！
[Dialog]
[charslot]
[charslot(slot="r",name="avg_npc_1007_1#1$1",posfrom="-150,0",posto="-150,0",afrom=0,ato=1,duration=1.5,focus="r")]
[charslot(slot="l",name="avg_1016_agoat2_1#9$2",posfrom="150,0",posto="150,0",focus="l")]
[Delay(time=2.5)]
[charslot(slot="l",posfrom="150,0",posto="0,0",duration=1.5,focus="all")]
[charslot(slot="r",posfrom="-150,0",posto="0,0",duration=1.5,focus="all")]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1007_1#1$1",focus="r")]
[name="温和的生物"]晚上好，孩子，你听到了铃声吗？
[charslot(slot="l",name="avg_1016_agoat2_1#2$2",focus="l")]
[name="阿黛尔"]铃声？没有......可能是因为我很多时候，听不太清......
[charslot(slot="r",name="avg_npc_1007_1#1$1",focus="r")]
[name="温和的生物"]那你也该来加入我们的聚会。
[charslot(slot="l",name="avg_1016_agoat2_1#4$2",focus="l")]
[name="阿黛尔"]在哪里的聚会？
[charslot(slot="r",name="avg_npc_1007_1#1$1",focus="r")]
[name="温和的生物"]下课铃响了之后，世界的尽头。
[name="温和的生物"]但在那之前，我有一些东西要给你看看。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g8_siestavolcanomuseum_inside",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1007_1#1$1",duration=1.5,focus="m")]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]唔，看来我没有记错。
[name="温和的生物"]这些石头、标本、红色的图片，应该是要带着你来看的。
[Dialog]
[charslot]
温和的生物迈开脚步，轻巧地走在前面。
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]你看，这些岩石已经活了数千年，数万年，我们还不在的时候，它们就深埋在地下了。
[name="温和的生物"]它们那么美，那么热烈，虽然在很深的地下，相隔着数百公里，可是最终还是汇聚到一起，迎来了辉煌的喷发。
[name="温和的生物"]你很喜欢它们，对不对？
[charslot(slot="m",name="avg_1016_agoat2_1#1$2",focus="m")]
[name="阿黛尔"]火山吗？是的......
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]火山，石头，它们都是很珍贵的宝物。
[name="温和的生物"]可是，我的阿黛尔......
[name="温和的生物"]要是有人用它们来做一些不好的事，该怎么办呢？
[charslot(slot="m",name="avg_1016_agoat2_1#2$2",focus="m")]
[name="阿黛尔"]不好的事......？是指什么？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1008_1#1$1",posfrom="900,0",posto="900,0",isblock=false)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_blcksheepborn", volume=1,channel="1")]
[charslot(slot="m",action="jump",posto="-1900,0",power=50,times=3,duration=4.5,isblock=false)]
[Delay(time=2.8)]
[name="着急的生物"]是个还不错的聚会♪
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1011_1#1$1",posfrom="-900,0",posto="-900,0",isblock=false)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_blcksheepborn", volume=1,channel="1")]
[charslot(slot="m",action="jump",posto="1900,0",power=50,times=3,duration=4.5,isblock=false)]
[Delay(time=2.8)]
[name="迷糊的生物"]聚会是个还不错的♪
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1008_1#1$1",posfrom="-900,0",posto="-900,0",isblock=false)]
[Delay(time=0.3)]
[charslot(slot="l",action="jump",posto="900,0",power=50,times=3,duration=3,isblock=false)]
[Delay(time=2.8)]
[name="着急的生物"]北风北风我们找到了♪
[Dialog]
[charslot(slot="r",name="avg_npc_1011_1#1$1",posfrom="900,0",posto="900,0",isblock=false)]
[Delay(time=0.3)]
[charslot(slot="r",action="jump",posto="-900,0",power=50,times=3,duration=3,isblock=false)]
[Delay(time=2.8)]
[charslot(slot="r",focus="r")]
[name="迷糊的生物"]种子种子又在哪里呢♪
[Dialog]
[charslot]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]啊，派对要开始了。
[name="温和的生物"]阿黛尔，你要不要带上一块岩石去参加？
[name="温和的生物"]我们快跟上吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g6_siestaunbuiltland_n",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_1016_agoat2_1#2$2",duration=1.5)]
[Delay(time=2)]
[name="阿黛尔"]......
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]怎么了，你在想什么呢？
[charslot(slot="m",name="avg_1016_agoat2_1#7$2")]
[name="阿黛尔"]呃......不好意思，我......
[charslot(slot="m",name="avg_1016_agoat2_1#2$2")]
[name="阿黛尔"]小黑羊......你是多利先生吗？
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]我是多利，我也不是多利。
[name="温和的生物"]我是谁，取决于我在你心中的样子。
[charslot(slot="m",name="avg_1016_agoat2_1#9$2")]
[name="阿黛尔"]你和多利先生，有些不一样。
[name="阿黛尔"]那这些......都是小黑羊吗？
[charslot(slot="m",name="avg_npc_1007_1#1$1")]
[name="温和的生物"]不不，不能说“都是”。他们每只都是独一无二的，与这世界的联系也是独一无二的。
[

... (全文10199字符)
```

### level_act27side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_village",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="r",name="avg_npc_071",duration=1.5)]
[charslot(slot="l",name="avg_npc_070",duration=1.5)]
[delay(time=2)]
[charslot(slot="r",name="avg_npc_071",focus="r")]
[name="阿达克利斯人A"]要我说啊，那个叫安麦尔的没尾巴也太奇怪了！
[name="阿达克利斯人A"]吃东西会吃出羽兽蛋壳，轮到她过桥的时候吊绳居然断了，搭房子被瀑布冲了，抓鳞反而被大鳞抓走！
[charslot(slot="l",name="avg_npc_070",focus="l")]
[name="阿达克利斯人B"]噢，我记得依娜姆大姐说过，这叫什么来着？美运体质？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_075",focus="m")]
[name="依娜姆"]是霉运体质。
[name="依娜姆"]你们两个，别忘了向安麦尔道谢。没有她，就像你们这样工作一天快活一天，这些新房子可不知道什么时候才能建好呢！
[Dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=1, g=1, b=1, fadetime=1, block=true)]
[delay(time=1)]
[charslot]
轰隆——
[Dialog]
[PlaySound(key="$d_avg_bodyfallvalley", volume=1,channel="2")]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1,channel="1")]
[charslot(slot="m",name="avg_npc_1015_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1015_1#6$1")]
[name="安麦尔"]咳咳、咳咳！
[charslot(slot="m",name="avg_npc_075",focus="m")]
[name="依娜姆"]怎、怎么回事？门怎么炸了？
[charslot(slot="m",name="avg_npc_1015_1#6$1")]
[name="安麦尔"]没事，我很快就能把它修好......我本来在烘干合页上的黏合剂，可能是我操作不当哈哈哈......
[Dialog]
[charslot]
[charslot(slot="r",name="avg_npc_071")]
[charslot(slot="l",name="avg_npc_070")]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_npc_071",focus="r")]
[name="阿达克利斯人A"]黏合剂？
[charslot(slot="l",name="avg_npc_070",focus="l")]
[name="阿达克利斯人B"]那是我的酒壶，我奶奶给我的。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_075",focus="l")]
[charslot(slot="r",name="avg_npc_1015_1#5$1",focus="l")]
[name="依娜姆"]......
[charslot(slot="r",name="avg_npc_1015_1#5$1",focus="r")]
[name="安麦尔"]......
[charslot(slot="l",name="avg_npc_075",focus="l")]
[name="依娜姆"]咳，东西应该都搬来了吧？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_071",focus="m")]
[name="阿达克利斯人A"]都在这边了，我们搬了一上午呢！今天晚上可得好好泡个澡了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_075",focus="r")]
[charslot(slot="r",name="avg_npc_1015_1#3$1",focus="r")]
[name="安麦尔"]一上午？都是什么货物......咖啡？
[charslot(slot="l",name="avg_npc_075",focus="l")]
[name="依娜姆"]对，都是汐斯塔的咖啡。我们开通了和汐斯塔的商路，这是送来的第一批货品。
[charslot(slot="r",name="avg_npc_1015_1#6$1",focus="r")]
[name="安麦尔"]我看看，包装上好像有说明文字......“把花的种子和咖啡豆一起烘焙”......汐斯塔人用这种配方来调和咖啡的苦味。
[name="安麦尔"]我小的时候，爷爷也是这么做咖啡喝的。
[charslot(slot="l",name="avg_npc_075",focus="l")]
[name="依娜姆"]安麦尔小姐的爷爷，好像是汐斯塔人吧？
[charslot(slot="r",name="avg_npc_1015_1#9$1",focus="r")]
[name="安麦尔"]嗯......不过我们一家人很早之前就搬到哥伦比亚了。等这个月的活干完，我攒的钱就够搭车回汐斯塔了！
[charslot(slot="l",name="avg_npc_075",focus="l")]
[name="依娜姆"]嗯？早知道我就让汐斯塔派来的商队带上你了，一个多小时前他们刚走。
[Dialog]
[charslot(slot="r",action="jump",power=5,times=2,duration=0.3,isblock=true)]
[charslot(slot="r",name="avg_npc_1015_1#3$1",focus="r")]
[name="安麦尔"]什么？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g8_siestavolcanomuseum_inside",screenadapt="showall")]
[playMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="考察日志：", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="1095年9月3日，莱塔尼亚北部，乌纳火山", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="考察目标：获得乌纳火山爆发的一手观测数据，计算火山爆发时周围环境中源石粉尘浓度梯度衰减数值，建立理论模型", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="预计观测时间：五个小时", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="考察队成员：卡提亚、玛格娜、凯勒", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
老旧的笔记本里，夹着一张照片。
三个穿着登山服的人站成一排，三张笑脸被山风吹得通红。
[Dialog]
[charslot(slot="m",name="avg_180_amgoat_1#11$1",focus="m")]
[name="阿黛尔"]凯勒老师......也在当时的考察队伍里。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[charslot(slot="l",name="avg_180_amgoat_1#1$1")]
[charslot(slot="r",name="avg_npc_996_1#2$1")]
[Background(image="41_g4_siestanewstreet_n",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_996_1#2$1",focus="r")]
[name="卡恩"]那次考察中，凯勒本该也是考察队的一员。
[charslot(slot="r",name="avg_npc_996_1#10$1",focus="r")]
[name="卡恩"]但是登山的前一天，凯勒突然离开队伍，返回了威廉大学。
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="阿黛尔"]突然离队？是有什么原因吗？
[charslot(slot="r",name="avg_npc_996_1#2$1",focus="r")]
[name="卡恩"]不知道，当年的考察笔记中完全没有提及。只知道紧跟那场事故之后，凯勒出现在了威廉大学和莱塔尼亚政府的会议上。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot="m",name="avg_180_amgoat_1#2$1",focus="m")]
[Background(image="41_g8_siestavolcanomuseum_inside",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="阿黛尔"]多利先生，那个时候你在吗......？
[Dialog]
[charslot]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_180_amgoat_1#4$1",focus="m")]
[name="阿黛尔"]唉......还是要帮你找到东西才肯理我吗......
[charslot(slot="m",name="avg_180_amgoat_1#11$1",focus="m")]
[name="阿黛尔"]那，多利先生，你听说过火山预警花吗？它是一种会根据火山活动改变颜色的植物，你要找的是这种花的种子吗？
[name="阿黛尔

... (全文26687字符)
```

### level_act27side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g5_siestaunbuiltland_d",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_1014_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_180_amgoat_1#6$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="多利"]唔，看起来已经收拾完了。不错。
[charslot(slot="r",name="avg_180_amgoat_1#6$1",focus="r")]
[name="阿黛尔"]多利先生！你不觉得你应该管一管你的分身们吗？
[charslot(slot="r",name="avg_180_amgoat_1#10$1",focus="r")]
[name="阿黛尔"]你知道放任它们这样闹下去，会给这里的人造成多大的麻烦吗？
[Dialog]
[charslot]
毛绒绒的生物站在集装箱上，它的头压得很低，似乎想向面前的人表现出歉意。
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[charslot(slot="r",name="avg_180_amgoat_1#10$1",focus="l")]
[name="多利"]我说了，他们不完全是我。
[name="多利"]虽然确实是我把他们带到这里来的......但这也只能算是间接责任吧？
[name="多利"]所以......对不起？
[charslot(slot="r",name="avg_180_amgoat_1#10$1",focus="r")]
[name="阿黛尔"]这可不是一句对不起就能解决的呀！
[charslot(slot="r",name="avg_180_amgoat_1#6$1",focus="r")]
[name="阿黛尔"]那些商品要是受损了，那些店主们要怎么办呢？你的分身打扰了居民们的生活，就没有什么办法能阻止它们吗？
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="多利"]方法还是有的......那个，一般情况下，我会选择用“呼喊”。
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="r")]
[name="阿黛尔"]“呼喊”？
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="多利"]就像这样，对着随便哪里，可以是海，可以是荒地，两个手拢在嘴边，然后大声地：“喂——你们都在哪里！快点给我过来！”这样。
[name="多利"]阿黛尔，你也要帮帮我才行，我喊的次数太多了，他们有时会装作没听到。
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="r")]
[name="阿黛尔"]那......喊它们过来就可以了？
[charslot(slot="l",name="avg_npc_1014_1#1$1",focus="l")]
[name="多利"]还要有点能诱惑他们的东西。比如“这里有冰淇淋！”“这里有气球和滑板！”这样。
[name="多利"]但要记住，不要叫他们“小黑羊”或者“小羊”，他们会不知道这是在叫他们。
[Dialog]
[charslot(slot="l",action="jump",power=2,times=4,duration=4,isblock=false)]
[Delay(time=1.5)]
多利期待地看向身边的阿黛尔。
[Dialog]
[charslot(slot="l",posfrom="0,0",posto="-200,0",afrom=1,ato=0,duration=2,isblock=false)]
[charslot(slot="r",posfrom="0,0",posto="-200,0",duration=1.5,isblock=true)]
[Delay(time=2.2)]
[charslot(slot="r",name="avg_180_amgoat_1#1$1",posfrom="-200,0",posto="-200,0",focus="r")]
[name="阿黛尔"]咳咳......
[name="阿黛尔"]喂——！这里有冰淇淋！
[name="阿黛尔"]喂——！这里有气球和滑板！快过来吧！
[Dialog]
[charslot(slot="r",name="avg_180_amgoat_1#1$1",posfrom="-200,0",posto="-200,0",focus="none")]
[name="女游客"]什么？冰淇淋？是免费的吗？
[name="小游客"]姐姐，真的有吗？我想要草莓味的！
[name="男游客"]是在做什么活动吗？有气球可以领？
[Dialog]
[PlaySound(key="$rungeneral", volume=1,channel="1")]
[PlaySound(key="$runsand", volume=1,channel="2")]
[CameraShake(duration=2.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="r",name="avg_180_amgoat_1#9$1",posfrom="-200,0",posto="-200,0",focus="r")]
[name="阿黛尔"]欸？不是......
[Dialog]
[charslot]
阿黛尔回头，想指出始作俑者。多利已经跃上一旁的集装箱，像漏气的气球一样围着几人打圈。
但是路人们都看不到它。
[charslot(slot="m",name="avg_npc_1014_1#1$1",focus="m")]
[name="多利"]哎呀，出状况了。
[name="多利"]那你要先和他们一起去吃冰淇淋才行了，可能还要去买气球，去逛街，去晒晒汐斯塔的太阳。
[name="多利"]怎么办呢？我碰巧还知道一家非常好吃的冰淇淋店。
[name="多利"]要不要我领路带你们去？
[charslot(slot="m",name="avg_180_amgoat_1#10$1",focus="m")]
[name="阿黛尔"]......多利先生！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="41_g3_siestanewstreet_d",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="女游客"]所以这是你们火山博物馆的揽客手段吗？给路人买冰淇淋吃？那我还真的挺喜欢的！
[name="女游客"]亲爱的，我们要不下午就去博物馆转转？
[name="男游客"]好啊，逛完博物馆我们再去吃烧烤！
[name="女游客"]走走走！
[Dialog]
[charslot(slot="m",name="avg_180_amgoat_1#9$1",focus="m")]
[name="阿黛尔"]那，谢谢你们啦。
[Dialog]
[charslot]
阿黛尔目送着几人走远，环顾四周，试图找到多利的身影。
[Dialog]
[charslot(slot="m",name="avg_npc_1008_1#1$1",duration=1.5)]
[Delay(time=2)]
街上人来人往，多利早就消失不见，只有一只小黑羊正死死盯着来往游客手里那个能“变出”纸钞来的小皮夹。
[charslot(slot="m",name="avg_180_amgoat_1#11$1",focus="m")]
[name="阿黛尔"]（......它准备做什么？）
[Dialog]
[charslot]
[stopmusic]
[charslot(slot="m",name="avg_npc_1008_1#1$1",posfrom="900,0",posto="900,0",isblock=false)]
[charslot(slot="r",name="avg_npc_021",posfrom="-200,0",posto="-200,0",duration=0)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_blcksheepborn", volume=1,channel="1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[charslot(slot="m",action="jump",posto="-1900,0",power=65,times=2,duration=1.5,isblock=false)]
[PlaySound(key="$d_avg_slip", volume=1,channel="2")]
[Delay(time=1.5)]
就在游客和老板讨价还价时，小黑羊纵身一跃——
一口叼走了游客手里的钱包。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_180_amgoat_1#5$1",focus="m")]
[name="阿黛尔"]（欸？！）
[Dialog]
[charslot]
[playMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_021",focus="m")]
[name="男游客"]我的钱包呢？！谁偷走了我的钱包！
[Dialog]
[charslot]
[name="汐斯塔市民"]啊？你的钱包长什么样？黑的白的？
[name="汐斯塔市民"]就刚刚吗？但我好像没看到有什么人啊？
[charslot(slot="m",name="avg_180_amgoat_1#3$1",focus="m")]
[name="阿黛尔"]（糟糕了，多利先生也不在，我得赶紧把它抓住！）
[Dialog]
[charslot]
[PlaySound(key="$d_avg_sheeprun", volume=1,channel="1")]
[charslot(slot="m",name="avg_npc_1008_1#1$1",duration=1.5)]
[Delay(time=2)]
叼着钱包的小黑羊注意到了阿黛尔，它松了口，钱包掉了下来——
[Dialog]
[PlaySound(key="$d_avg_blcksheepborn",channel="2",volume=0.4)]
[charslot(slot="m",action="jump",posto="50,0",power=50,times=2,duration=0.3,isblock=false)]
又伸出蹄子轻轻一踢，钱包在空中划出弧线，正好落回它身上的绒毛里。
[Dialog]
[charslot(slot="m",action="jump",power=10,times=3,duration=0.5)]
[name="毛绒绒的生物"]（快乐地扑腾）
[Dialog]
[PlaySound(key="$gavel2", volume=0.5,channel="1")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=true)]
钱包像是撞到了什么东西，“咣”的一声，一块布满小孔的石头从小黑羊身上滚落出来。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_180_amgoat_1#5$1",focus="m")]
[name="阿黛尔"]那是，响石！
[Dialog]
[charslot]
小黑羊回头看看，趁石头落地之前，又忙用蹄子把石头也踢回绒毛中。
随后它向阿黛尔吐舌头做了个鬼脸，转身向风情街奔去。
[charslot(slot="m",name="avg_180_amgoat_1#5$1",focus="m")]
[name="阿黛尔"]喂！你等一等！
[charslot(slot="m",name="avg_18

... (全文26791字符)
```

### level_act27side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_sunnytown_1",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.8, block=true)]
[Delay(time=0.5)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_wdnguitarstrum", volume=0.6)]
[delay(time=1.5)]
为什么要研究火山？
我希望有一天，我可以在汐斯塔最高的地方弹吉他。不一定是在黑曜石音乐节上，最好是在火山上。
我出的第一张专辑，就准备叫《火山奏鸣曲》。
不能把火山叫醒？啊哈哈......那还是叫《火山安眠曲》吧。
火山其实睡得很熟的，哪有那么容易被你叫醒。
......
[Dialog]
[delay(time=1)]
你有没有听说过，火山上的一种石头？
风吹动它，会发出如同豆子落入碗中的响声。
浸在水里，气泡又会咕嘟咕嘟地冒出来，就像细密的鼓点。
当然是真的，如果我在哪座火山上找到了这种石头，我就把它带回来给你看。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_hotel", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true,amount=0, block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$doorknockquite")]
[Delay(time=1.5)]
[PlaySound(key="$dooropenquite")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[charslot(slot="m",name="avg_npc_997_1#9$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]医生已经来过了，今天感觉怎么样？
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="none")]
老人躺在病床上，侧着头望向窗外。
[name="疲惫的声音"]如果不是你专门来提醒我在这个夏天只能躺在床上的话，还不错。而且，病床应该也比办公室的椅子要舒服些。
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="m")]
[name="科斯达"]多谢你还有精力调侃我，但这几天我的屁股就没有沾过椅子。
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="none")]
[name="疲惫的声音"]或许我们应该换换。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1.5)]
老人回过头来，看向站在床边的自己的孙子。
[name="疲惫的声音"]那么我的好孙子，今天来找我有什么事？
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="m")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=1)]
[name="科斯达"]这份搬迁意向书，希望您能签个字。
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="none")]
市政厅职员像是认错一样低声吐出了这句话。
然后便是一段疲惫又苦涩的沉默。
[name="疲惫的声音"]看起来改建计划真的很着急，甚至等不到我咽气对不对？
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="m")]
[name="科斯达"]倒不至于这样......
[name="科斯达"]我就是觉得，总该让你知道这件事。当然，能取得你的同意是最好的。
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="none")]
[name="疲惫的声音"]你要是真的想说服我，至少该带着泰莎一起来看我。
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]她也在工作......
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="none")]
[name="疲惫的声音"]都是为了生活，对吧？真不明白，那样的女孩子为什么会同意嫁给你这样无聊的人。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]就当我继承了您哄女孩开心的天赋吧。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="none")]
[name="疲惫的声音"]哼......
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_npc_997_1#9$1",afrom=1,ato=0,duration=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_avg_cutrope",volume=0.1)]
[PlaySound(key="$d_avg_cutrope", volume=0.1, loop=false, channel="frt",delay=1.5)]
[Delay(time=1)]
病房中安静下来，只有削水果的声音低低地响起。
[name="疲惫的声音"]这几天，工作很辛苦吧。
[name="疲惫的声音"]最近总是莫名其妙做怪梦，想了想自己应该没得罪过什么人，所以我猜是你被不少人骂了。
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#9$1",afrom=0,ato=1,duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]您真聪明，对我的工作了解得真是一点不差。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="none")]
[name="疲惫的声音"]那你又是怎么想的呢？真的愿意让这片商业街拆掉，让老汐斯塔剩下的最后一点痕迹也消失不见？
[charslot(slot="m",name="avg_npc_997_1#8$1",focus="m")]
[name="科斯达"]我......
[charslot(slot="m",name="avg_npc_997_1#8$1",focus="none")]
[name="疲惫的声音"]科斯达，后面的柜子里放着一把吉他，拿出来给我弹一首吧。
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]算了吧......您知道这样没有意义......
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="none")]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1.5)]
老人不再说话，把头扭了过去，看向窗外。
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="m")]
[name="科斯达"]......我知道，知更鸟咖啡店在汐斯塔的时间比市政厅还要长。还有那条街上许多家其他的店铺，从火山那里搬到这里的时候都留了下来。
[name="科斯达"]但能让生活过不下去的困难太多了，火山甚至排不上号。
[name="科斯达"]咖啡和音乐只有在特定的时候才能养活人。如果不是我侥幸找到了市政厅的这份工作，您的医药费都会是这个家迈不过去的一道坎。
[name="科斯达"]我不是想抱怨什么，只是——
[charslot(slot="m",name="avg_npc_997_1#6$1",focus="none")]
[name="疲惫的声音"]得了，把笔给我吧。
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]......
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="none")]
[PlaySound(key="$d_avg_penrustle")]
[Delay(time=1.5)]
[name="疲惫的声音"]科斯达，我讨厌你这个臭小子。
[name="疲惫的声音"]或许我就应该在你用气泡水兑手冲咖啡的时候把你扔进海里。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]......
[name="科斯达"]多谢您没真的这么做......我还是很喜欢您。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g12_obsidianhotspringshotel", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_995_1#1$1")]
[charslot(slot="r",name="avg_1033_swire2_1#7$1")]
[delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_995_1#1$1",focus="l")]
[name="佩利佩"]你想租用我的旅馆？
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]在你允许的范围内，对这里的温泉做一点小小的改造——价钱好商量。
[charslot(slot="l",name="avg_npc_995_1#1$1",focus="l")]
[name="佩利佩"]我对钱不感兴趣，千篇一律，毫无美感！
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]欸，又不是只有钱才能作为交易的筹码，我这里绝对有你感兴趣的好东西。
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]比如这个？
[charslot(slot="l",name="avg_npc_995_1#5$1",focus="l")]
[name="佩利佩"]这照片上是......那块展品级黑曜石？！
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]把你管理的几家温泉旅馆租给我几天，我就把这块黑曜石搬到你这里怎么样？
[charslot(slot="l",name="avg_npc_995_1#8$1",focus="l")]
[name="佩利佩"]别开玩笑了，这是私人

... (全文29676字符)
```

### level_act27side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g2_siestacommercialstreet_n",screenadapt="coverall")]
[Delay(time=0.5)]
[PlayMusic(key="$SiestaCity_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_997_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_1002_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_997_1#1$1",focus="l")]
[name="科斯达"]呼......
[charslot(slot="r",name="avg_npc_1002_1#1$1",focus="r")]
[name="年迈的店主"]你怎么还在这？
[charslot(slot="l",name="avg_npc_997_1#1$1",focus="l")]
[name="科斯达"]在拿到你们所有人的签字之前，我都要像一只海滩上的四爪磐蟹一样赖在这里了。
[charslot(slot="r",name="avg_npc_1002_1#1$1",focus="r")]
[name="年迈的店主"]好啊，那你赖着吧。我要收摊回家跟自己喝一杯了。
[charslot(slot="l",name="avg_npc_997_1#1$1",focus="l")]
[name="科斯达"]您请便。
[Dialog]
[charslot(slot="l",name="avg_npc_997_1#1$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot="r",name="avg_npc_1002_1#1$1",afrom=1,ato=0,duration=1.5)]
[delay(time=2)]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_1002_1#1$1",duration=0.5)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]今天我从那个集市上买到了个新鲜玩意，好像是叫什么“源石微波按摩仪”，哥伦比亚的，弄不明白，但还挺好用，贴在腰上确实舒服。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]尝试一下新鲜事物也不是坏事。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]长毛循兽骑着冲浪板在屋顶冲浪的那个节目也是你们搞的？
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]长毛循兽？不，那个不是......
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]真可惜，我还挺喜欢那个的。没有了黑曜石音乐节之后，难得见到这么有趣的节目。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]很高兴能取悦到您......
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]对了，送你一个东西。
[Dialog]
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_throwstone",volume=0.8)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]......拇指琴？
[Dialog]
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_kalimbapizz",volume=0.6)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]这也是您从白天的集市上买来的？
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]新婚快乐，小子。
[charslot(slot="m",name="avg_npc_997_1#4$1",focus="m")]
[name="科斯达"]......
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]为了家人找了个稳定的工作，虽然是无聊了点，倒也算有责任心。
[name="年迈的店主"]能理解你喜欢安定，可是生活的方式总有很多种，别让自己过得太狼狈了，小子。
[charslot(slot="m",name="avg_npc_997_1#10$1",focus="m")]
[name="科斯达"]人只要活着就够狼狈了......随遇而安吧。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]那时候和你爷爷打赌，说你总有一天能去黑曜石音乐节拿一个大奖回来。
[name="年迈的店主"]真是......白瞎了那么好的音乐天赋。
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]等您有心情的时候，我也可以把旧吉他搬出来，再弹给您听。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="年迈的店主"]要是你早拿出吉他弹上一曲，说不定我早就在那张表上签字了。
[charslot(slot="m",name="avg_npc_997_1#1$1",focus="m")]
[name="科斯达"]您......
[charslot(slot="m",name="avg_npc_997_1#9$1",focus="m")]
[name="科斯达"]谢谢。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g9_purewhitevolcano_inside", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_180_amgoat_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_180_amgoat_1#1$1",focus="m")]
[name="阿黛尔"]哈莉太太，这里丢的冲浪板我们帮您找回来了，您看看数量对不对。
[charslot(slot="m",name="avg_180_amgoat_1#11$1",focus="m")]
[name="阿黛尔"]非常抱歉......
[charslot(slot="m",name="avg_npc_994_1#5$1",focus="m")]
[name="哈莉"]你帮了我的忙，怎么反而跟我道歉？
[charslot(slot="m",name="avg_180_amgoat_1#11$1",focus="m")]
[name="阿黛尔"]这个......
[charslot(slot="m",name="avg_npc_994_1#5$1",focus="m")]
[name="哈莉"]这几件东西，我还以为再也派不上用场了。真奇怪，到底是谁拿走的？
[charslot(slot="m",name="avg_180_amgoat_1#7$1",focus="m")]
[name="阿黛尔"]唔，那个，我也不是很清楚......
[charslot(slot="m",name="avg_npc_994_1#1$1",focus="m")]
[name="哈莉"]没事的，孩子，说不定是一些游客玩得太开心顺手拿去玩了玩，都找回来就行了。那你呢？你今天玩得开心吗？
[charslot(slot="m",name="avg_4106_bryota_1#1$1",focus="m")]
[name="埃尼斯"]是指被温泉水浇个湿透吗？
[charslot(slot="m",name="avg_npc_994_1#1$1",focus="m")]
[name="哈莉"]也算是找回了一点在海边玩水的感觉？好久没这么闹过了，连来喝酒的客人脸上都是笑眯眯的。
[charslot(slot="m",name="avg_npc_994_1#5$1",focus="m")]
[name="哈莉"]之前那几个店主天天苦着一张脸，酒都变难喝了......
[Dialog]
[charslot(duration=0.7)]
[Delay(time=1)]
哈莉看向店外还没有散去的游客，夕阳渐渐染红天空，每个人都很快乐。
[Dialog]
[Delay(time=1)]
[name="哈莉"]就像是回到了好几年前啊。
[Dialog]
[musicvolume(volume=0, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g2_siestacommercialstreet_n", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.6, fadetime=1)]
[Delay(time=1)]
男人缓缓走向陈旧的咖啡馆，又一次推开门。
[Dialog]
[playsound(key="$d_avg_key")]
[playsound(key="$dooropenquite",volume=0.9,delay=0.8)]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
他摸索着打开电闸，用抹布仔细将吧台上的灰尘抹去，又从柜子里拿出器具，再从怀中摸出一包从办公室带回来的新鲜咖啡豆。
[Dialog]
[PlaySound(key="$pourwater")]
[delay(time=2)]
像许多年前一样，烧水，磨粉，仔细注水。
[Dialog]
[Delay(time=1)]
[name="科斯达"]呼......
[name="科斯达"]这味道......还是手生了啊。
[Dialog]
[Delay(time=1)]
他看向窗外，人们趁着夕阳陆陆续续回了家，街道渐渐趋于冷落，直到街上空无一人，他才发出一声自嘲的苦笑。
[name="科斯达"]真是......我到底在等什么。
他喝完咖啡，准备收拾东西离开这里。
[Dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
一阵敲门声传来。科斯达记得自己并没有将店门关上。
[name="科斯达"]......

... (全文20283字符)
```

### level_act27side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="21_G7_decisivebattlealley_d",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1015_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_177",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]灾难，简直是灾难！
[name="破产商人"]这就是你做的室内设计？怪不得没人愿意找汐斯塔人做设计，旅游城市根本没有自己的风格，你真的是连抄都不会！
[name="破产商人"]优雅的维多利亚风格被你弄成这个样子，你看看这个桌台，我说过要做出大理石的质感，你却使用这种廉价的劣质木材！
[charslot(slot="l",name="avg_npc_1015_1#1$1",focus="l")]
[name="贫穷的少女"]或许您可以看看您给的预算够不够买半块仿、大、理、石、料。
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]哈！好吧，安麦尔小姐，看来你并没有摆清楚你的位置。
[name="破产商人"]如果不是我，你还跟着萨尔贡商队在城里迷路呢！我现在就能去举报你是一个混进维多利亚的黑户，你一分钱也拿不到！
[charslot(slot="l",name="avg_npc_1015_1#7$1",focus="l")]
[name="贫穷的少女"]那我也会举报您收留黑户、有非法雇佣行为的，先生！把工钱结算给我！
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]你、你！
[name="破产商人"]哼，不愧是来自愚蠢汐斯塔的人，这样地粗俗无礼......
[name="破产商人"]能做出淘汰黑曜石矿业这种自断手脚的蠢事的城市，自然就会有你这样不懂得尊重别人的市民！
[charslot(slot="l",name="avg_npc_1015_1#8$1",focus="l")]
[name="贫穷的少女"]（工钱，工钱，拿到了工钱再骂......）
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]哑口无言了？你的悲剧就在于你根本没有意识到汐斯塔的愚蠢，还在这里大呼小叫，指责我的不是！
[charslot(slot="l",name="avg_npc_1015_1#8$1",focus="l")]
[name="贫穷的少女"]（我不能白干，那是路费，路费......）
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]你们当年要是选择并入维多利亚，你们早就成为帝国的子民，享用帝国的丰饶，融入帝国的历史！哪还用现在祈求一点路费......
[charslot(slot="l",name="avg_npc_1015_1#1$1",focus="l")]
[name="贫穷的少女"]......
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]哼，看你也算有悟性，能听得懂我这一番高见。
[Dialog]
[PlaySound(key="$d_avg_wadmoney", volume=1)]
[Delay(time=1)]
[name="破产商人"]拿去吧，这是你的工钱。唔，要点清楚，这可是维镑。你知道怎么换算面额吗？别以为我克扣了你的，会不礼貌。
[charslot(slot="l",name="avg_npc_1015_1#7$1",focus="l")]
[name="贫穷的少女"]先生，你根本配不上我的礼貌。
[name="贫穷的少女"]你完全不了解汐斯塔的历史，甚至完全不了解让你自豪的维多利亚建筑史。何况维多利亚的辉煌是你祖先的功绩，和你没有半点关系。
[name="贫穷的少女"]你不妨去看看维多利亚的建筑，看看汐斯塔的黑曜石是如何改变了你们的建筑风格，又如何成为你们贵族追捧的奢侈品。
[name="贫穷的少女"]究竟是谁眼界狭窄？
[charslot(slot="r",name="avg_npc_177",focus="r")]
[name="破产商人"]你......！
[charslot(slot="l",name="avg_npc_1015_1#7$1",focus="l")]
[name="贫穷的少女"]关闭矿场是汐斯塔人为了保护环境做出的选择，我们始终在为家园的未来考虑，而不是念叨着过去的辉煌，无比吝啬，却希望得到崇敬。
[name="贫穷的少女"]我是回去建设我的家园，帮助它获得一次新的生命的。你是干什么的？维多利亚现在是这个样子，你现在又在做什么呢？
[Dialog]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1015_1#7$1",focus="l")]
安麦尔撇了撇嘴角，用手比划了一下纸钞的厚度。
[charslot(slot="l",name="avg_npc_1015_1#7$1",focus="l")]
[name="贫穷的少女"]哥伦比亚拆迁队的薪水都比这个要厚一点，我尊敬的雇主先生。
[name="贫穷的少女"]但愿您的品味，可以帮您东山再起。
[name="贫穷的少女"]再见！
[Dialog]
[charslot(slot="l",name="avg_npc_1015_1#7$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot="l",name="avg_npc_1015_1#7$1",afrom=1, ato=0, duration=1)]
[delay(time=1.5)]
[Dialog]
[musicvolume(volume=0, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g12_obsidianhotspringshotel", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_995_1#1$1")]
[charslot(slot="r",name="avg_1033_swire2_1#7$1")]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]用不用再检查一下？没有什么损坏哦。
[charslot(slot="l",name="avg_npc_995_1#1$1",focus="l")]
[name="佩利佩"]藏品都还在，房子没塌就行，不用检查了。
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]答应过的报酬会给你的，大概两个月后那块展品级的黑曜石连收藏证书会一起送到你的手上。
[charslot(slot="l",name="avg_npc_995_1#3$1",focus="l")]
[multiline(name="佩利佩")]那可太好了！
[charslot(slot="l",name="avg_npc_995_1#1$1",focus="l")]
[multiline(name="佩利佩")]我很期待。
[charslot(slot="l",name="avg_npc_995_1#1$1",focus="none")]
收藏家的眼神短暂地亮了一下，但兴奋似乎也没有持续太久。
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="r")]
[name="诗怀雅"]这些黑曜石，到底有什么魔力能让你这么着迷呢？
[charslot(slot="l",name="avg_npc_995_1#7$1",focus="l")]
[name="佩利佩"]你也对黑曜石感兴趣？......怎么可能，我已经长了教训。真正能懂黑曜石的美的人寥寥无几，更多的人还是不安好心！
[name="佩利佩"]算了，我也不找你聊天了！再见吧！
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]佩利佩·布朗先生，不知道您和那位汐斯塔矿产大亨贝亚特·布朗，是什么关系？
[charslot(slot="l",name="avg_npc_995_1#5$1",focus="l")]
[name="佩利佩"]......
[charslot(slot="l",name="avg_npc_995_1#8$1",focus="l")]
[name="佩利佩"]别提那个吓人的老头子......
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]现在不一定有许多人记得。在黑曜石还是汐斯塔主要经济来源的时候，这个名字应该要更广为人知一点。
[name="诗怀雅"]之前在调查资料的时候注意到了这个名字，没想到他的继承人现在只是在经营这一片区域的温泉酒店。
[charslot(slot="l",name="avg_npc_995_1#8$1",focus="l")]
[name="佩利佩"]火山给汐斯塔留下了不少财富，除了黑曜石之外，温泉也是好东西。
[charslot(slot="l",name="avg_npc_995_1#7$1",focus="l")]
[name="佩利佩"]那个老头子前年去世了，因为矿石病。
[name="佩利佩"]他一辈子没有靠近过矿场，但是在去哥伦比亚度假的路上因为车子的源石发动机出故障感染了。
[charslot(slot="r",name="avg_1033_swire2_1#4$1",focus="r")]
[name="诗怀雅"]啊，我很抱歉......
[charslot(slot="l",name="avg_npc_995_1#7$1",focus="l")]
[name="佩利佩"]他算不上什么好人，但他的矿场确实提供了不少工作岗位。如果防护措施再完备一点，说不定还会有不少采矿工人感激他。
[charslot(slot="r",name="avg_1033_swire2_1#8$1",focus="r")]
[name="诗怀雅"]我有听说，在早些年政府下令禁止开采黑曜石的时候，您的矿场是最先积极响应的。
[charslot(slot="l",name="avg_npc_995_1#7$1",focus="l")]
[name="佩利佩"]能有什么办法，总不能做违法的事情。
[charslot(slot="r",name="avg_1033_swire2_1#8$1",focus="r")]
[name="诗怀雅"]好吧，布朗先生，希望未来我们可以进一步合作。您的这家温泉酒店很棒，有没有兴趣发展成一个温泉度假区？
[charslot(slot="l",name="avg_npc_995_1#1$1",focus="l")]
[name="佩利佩"]算了吧，我可不想再折腾了——除非下次你能带来让我更加无法拒绝的条件，比如更大更好看的黑曜石。
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="r")]
[name="诗怀雅"]说起来......你这里的黑曜石藏品好像都是精心雕琢过的，为什么有一块完全没有打磨过的矿石晶洞？
[charslot(slot="l",name="avg_npc_995_1#7$1",focus="l")]
[name="佩利佩"]......噢，你可不许打它的主意。
[name="佩利佩"]它可比这家酒店里的所有黑曜石加起来还要贵重。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black", screenadapt=

... (全文22303字符)
```

### level_act27side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g10_siestapremiumhotel",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_223",duration=0.7)]
[Delay(time=1)]
[PlaySound(key="$d_avg_paper2")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_223",focus="m")]
[name="市政厅职员"]二位，这是最新的民意调查结果。
[name="市政厅职员"]施怀雅集团的“水上乐园”方案的支持率为百分之三十三，峯驰物流公司的物流中心方案支持率为百分之二十一。
[name="市政厅职员"]其余几位竞争者的支持率都在百分之十左右。
[name="市政厅职员"]虽说民意调查的结果也只是影响市政厅最终决定的一部分，但就目前调查结果来看，施怀雅集团的方案的确是占据优势的。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_990_1#10$1",focus="r")]
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]不用多说了，具体的形势，相信拜松先生自己会有判断的。
[charslot(slot="l",name="avg_npc_990_1#10$1",focus="l")]
[name="拜松"]诗怀雅小姐今天特意约市政厅和我来这里，应该不止是炫耀战果的吧？
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]当然。拜松先生，我想向您提出一个交易。
[name="诗怀雅"]施怀雅集团会退出此次竞标，但对应的，我想要入股峯驰物流在这里的公司。
[charslot(slot="l",name="avg_npc_990_1#10$1",focus="l")]
[name="拜松"]这才是你最开始的目的吗？
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]也不完全是，我后来又仔细想了想，你的存在对我来说并不全都是坏处。
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]聪明的商人总是要寻求双赢的可能，做最符合当下利益最大化的选择嘛。
[charslot(slot="l",name="avg_npc_990_1#1$1",focus="l")]
[name="拜松"]按诗怀雅小姐的话说......如果你真的很有信心的话，就不会来找我谈了。
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]那么对于拜松先生来说，用一定的股份认筹额度换最大的竞争对手的退出，算不算一笔好生意呢？
[charslot(slot="l",name="avg_npc_990_1#3$1",focus="l")]
[name="拜松"]......
[charslot(slot="l",name="avg_npc_990_1#12$1",focus="l")]
[name="拜松"]诗怀雅小姐的开价是？
[Dialog]
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_stickknock",volume=0.2)]
[PlaySound(key="$d_avg_stickknock", volume=0.2, loop=false, channel="knock",delay=0.5)]
[PlaySound(key="$d_avg_stickknock", volume=0.2, loop=false, channel="knock1",delay=1)]
[Delay(time=1.5)]
诗怀雅轻叩了三下桌子。
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]我要，这个数。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g7_siestahightechtouristzone", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_223")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_223",focus="m")]
[name="市政厅职员"]二位的协议我会汇报给市长，后续进一步的安排会继续同步给二位的。
[name="市政厅职员"]祝两位客人在汐斯塔的行程愉快。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(duration=1)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_990_1#12$1",duration=0.7)]
[charslot(slot="r",name="avg_1033_swire2_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_990_1#12$1",focus="l")]
[name="拜松"]......戏终于演完了？
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]目前为止，算是吧。
[charslot(slot="l",name="avg_npc_990_1#1$1",focus="l")]
[name="拜松"]呼——
[charslot(slot="l",name="avg_npc_990_1#4$1",focus="l")]
[name="拜松"]哈哈......哈哈哈......
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="r")]
[name="诗怀雅"]你笑什么？
[charslot(slot="l",name="avg_npc_990_1#4$1",focus="l")]
[name="拜松"]抱歉抱歉......我只是没有想到，诗怀雅局长也会用这种手段......
[charslot(slot="r",name="avg_1033_swire2_1#8$1",focus="r")]
[name="诗怀雅"]我要是大张旗鼓地投资峯驰物流的生意，那别说注册自己的公司了，恐怕来汐斯塔的第一天，峯驰物流就被以一万种理由举报停工了吧。
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]家族的人对我有戒心，但好在并不多。只要在他们眼里我还是那个莽撞的年轻警司，我就可以借这层外衣行事。
[charslot(slot="l",name="avg_npc_990_1#1$1",focus="l")]
[name="拜松"]呼——我确实庆幸，没有真的当你的竞争对手。
[charslot(slot="r",name="avg_1033_swire2_1#7$1",focus="r")]
[name="诗怀雅"]但这只是第一步，商业联合会迟早会反应过来的。接下来各种各样的刁难肯定少不了。你准备好了？
[charslot(slot="l",name="avg_npc_990_1#1$1",focus="l")]
[name="拜松"]已经走到这一步，后悔肯定是来不及了。
[charslot(slot="r",name="avg_1033_swire2_1#1$1",focus="r")]
[name="诗怀雅"]那么，合作愉快？
[charslot(slot="l",name="avg_npc_990_1#1$1",focus="l")]
[name="拜松"]嗯，合作愉——
[Dialog]
[stopmusic(fadetime=2)]
[charslot(slot="l",name="avg_npc_990_1#1$1",focus="none")]
[PlaySound(key="$phone")]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_990_1#12$1",focus="l")]
[name="拜松"]你的终端？
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="r")]
[name="诗怀雅"]不是，是你的吧？
[Dialog]
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="none")]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="all")]
[PlaySound(key="$d_avg_ringoff", volume=1)]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[delay(time=1)]
诗怀雅和拜松拿出自己的终端，两人飞快地对视了一眼，按下了接听键。
[Dialog]
[charslot(slot="r",name="avg_1033_swire2_1#10$1",focus="none")]
[name="礼貌的声音"]您好，请问是“峯联贸易”的法定代表人拜松先生吗？
[name="低沉的声音"]您好，请问是诗怀雅小姐吗？
[name="礼貌的声音"]市政厅接到举报，贵司非法雇佣没有身份注册的感染者。现在请贵司立即停止一切业务。
[name="礼貌的声音"]请准备好以下材料，配合市政厅进行调查。首先是贵司所有感染者雇员的名单......
[name="低沉的声音"]诗怀雅小姐，你的表演很有趣，确实为你争取到了一些玩闹的时间。但是集团对你私自做决定的行为十分不满。
[name="低沉的声音"]希望你能意识到一点，该做的事和不该做的事都是有限度的，投资游戏该结束了。
[name="礼貌的声音"]感谢您的配合，再见。
[name="低沉的声音"]到此为止，希望您会好好考虑自己行为的意义。
[Dialog]
[PlaySound(key="$d_avg_phonestop", volume=1)]
[PlaySound(key="$d_avg_devicebeep", volume=1,delay=0.2)]
[delay(time=2)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[charslot(slot="r",name="avg_1033_swire2_1#5$1",focus="r")]
[name="诗怀雅"]......
[charslot(slot="l",name="avg_npc_990_1#11$1",focus="l")]
[name="拜松"]......
[charslot(slot="l",name="avg_npc_990_1#7$1",focus="l")]
[name="拜松"]这是毫无理由的污蔑。
[charslot(slot="r",name="avg_1033_swire2_1#5$1",focus="r")]
[name="诗怀雅"]是谁递交的举报信，一目了然了啊。在合同快要签订的时候拖时间，他们好追上来做点其他事情。
[name="诗怀雅"]可为什么要用感染者做文章......汐斯塔什么时候出台过为难感染者的政策？
[charslot(slot="l",name="avg_npc_990_1#11$1",focus="l")]
[name="拜松"]我们没有时间对付这些无理的刁难。
[name="拜松"]如果可以说服赫尔曼市长的话——
[charslot(slot="r",name="avg_1033_swire2_1#8$1",focus="r")]
[name="诗怀雅"]你说得没错，突破口的确

... (全文17379字符)
```

### level_act27side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_cave_2",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.8, block=true)]
[Delay(time=0.5)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="迷茫的青年"]我还是搞不明白，像您这样的夫人，为什么会每天待在矿洞里，您不介意和感染者打交道？
[name="温柔的学者"]感染者不就是不幸遭遇了意外的普通人吗？
[name="温柔的学者"]就像我的孩子，这个还未出世的孩子。将来她或许会成为感染者，也有可能只是一个幸运的普通人，与感染者成为朋友。
[name="温柔的学者"]但无论如何，我希望她可以生活在一座充满爱与善意的城市里。
[name="迷茫的青年"]如果继续在这里开采只会给环境带来破坏的话，那是不是我们该停下？
[name="温柔的学者"]现在这座城市只能依靠自然的补给，但将来这里的人们一定可以凭借自己的双手开辟出自己的家园。
[name="温柔的学者"]等到那时，我希望能看到你和我，和他们每个人——每个人都能在汐斯塔找到自己喜欢的事。
[name="温柔的学者"]老了不必担心，病了不必绝望，这就是我想象中的汐斯塔......是我想让我的孩子能看到的汐斯塔。
[name="迷茫的青年"]真的能实现吗......
[name="温柔的学者"]所以，我们就先从矿场开始吧！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g7_siestahightechtouristzone", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, amount=0, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1013_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_180_amgoat_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_180_amgoat_1#1$1",focus="r")]
[name="阿黛尔"]小黑羊，为什么只剩下你一个了？你知道它们都去哪里了吗？
[name="阿黛尔"]还有，你一直在吃这些老路牌，还有信件上的地址，也是因为你迷路了，正在找路吗？
[charslot(slot="r",name="avg_180_amgoat_1#9$1",focus="r")]
[name="阿黛尔"]你......能不能听懂我说的话......？
[charslot(slot="l",name="avg_npc_1013_1#1$1",focus="l")]
[name="迷路的生物"]......
[charslot(slot="l",name="avg_npc_1013_1#1$1",focus="none")]
[PlaySound(key="$d_avg_catsmell", volume=1)]
软绵绵的生物没有应答，它嗅嗅闻闻，挑拣着适合入口的路牌。
[charslot(slot="r",name="avg_180_amgoat_1#1$1",focus="r")]
[name="阿黛尔"]是不是汐斯塔的搬迁让你找不到去矿场的路了？
[name="阿黛尔"]还是说，不是矿场，是你在未建成地块那边的家？
[Dialog]
[charslot(slot="l",name="avg_npc_1013_1#1$1",focus="l")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_sandftsingle",volume=0.7)]
[PlaySound(key="$d_avg_sandftsingle", volume=0.7, loop=false, channel="bgs1",delay=0.5)]
[PlaySound(key="$d_avg_sandftsingle", volume=0.7, loop=false, channel="bgs2",delay=1)]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_180_amgoat_1#1$1",focus="none")]
似乎有些急切地，软绵绵的生物用蹄子刨着地面，阿黛尔站在它的身后，静静地等着它。
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="r")]
[name="阿黛尔"]......究竟要去哪里呢？
[Dialog]
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="l")]
[Delay(time=0.2)]
[charslot(slot = "l", action="jump",posfrom="0,0",posto="100,0",power=5,times=0,duration=1.5,focus="l",isblock=false)]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="l")]
[PlaySound(key="$d_gen_heartbeat", channel="hb",volume=0.6)]
[stopsound(channel="hb",fadetime=4)]
[Delay(time=2.5)]
它迟疑着凑上来，脑袋贴着阿黛尔的胸口，似乎是在聆听她的心跳。
咚咚、咚咚、咚咚......
[Dialog]
[charslot(slot="l",name="avg_npc_1013_1#1$1",focus="l")]
[name="迷路的生物"]......
[Dialog]
[charslot(slot="l",name="avg_npc_1013_1#1$1",focus="none")]
不是这个声音，不是这个声音。
[Dialog]
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="all")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_pawfootstep_1",loop=true, channel="sfoot2", volume=0.7)]
[StopSound(channel="sfoot2", fadetime=3)]
[charslot(slot = "l", action="jump",posfrom="0,0",posto="-200,0",power=0,times=1,duration=1.5)]
[charslot(slot="l",name="avg_npc_1013_1#1$1",afrom=1,ato=0,duration=1)]
[Delay(time=2)]
[charslot(slot="r",name="avg_180_amgoat_1#11$1",focus="none")]
软绵绵的生物垂下头，继续顺着眼前的路走下去。
[charslot(slot="r",name="avg_180_amgoat_1#1$1",focus="r")]
[name="阿黛尔"]你是在找过去的家吗，还是过去的亲人朋友？
[name="阿黛尔"]你知道该去哪里找他们吗？
[Dialog]
[charslot]
软绵绵的生物回过头，好奇地看向她。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[CharacterCutin(widgetID="1", name="avg_npc_999_1#1$1",style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=0, width=200, block=true)]
[name="凯勒"]阿黛尔，你在哪里？
[name="凯勒"]现在有些数据需要你和我一起来处理一下，你能现在就来博物馆吗？
[Dialog]
[CharacterCutin(widgetID="1",fadetime=0,block=true)]
阿黛尔看着眼前充满期待的生物。
[charslot(slot="m",name="avg_180_amgoat_1#9$1",focus="m")]
[name="阿黛尔"]啊......凯勒老师，我、我今天......我今天生病了！
[name="阿黛尔"]头有点晕，还有点疼，我的腿也不是很舒服......我有些难受......！
[Dialog]
[charslot]
[CharacterCutin(widgetID="2", name="avg_npc_999_1#5$1",style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=0, width=200, block=true)]
[name="凯勒"]难受？阿黛尔，你还好吗？
[name="凯勒"]要不要去医院看一下？要不要我去看你？你手边有药吗？我......你的体温怎么样，有没有发烧？
[Dialog]
[CharacterCutin(widgetID="2",fadetime=0,block=true)]
[charslot(slot="m",name="avg_180_amgoat_1#9$1",focus="m")]
[name="阿黛尔"]没有，凯勒老师，我还好......我现在正在医院！
[Dialog]
[charslot(slot="m",name="avg_180_amgoat_1#9$1",focus="none")]
[PlaySound(key="$d_avg_sheeprun", volume=0.8)]
[Delay(time=0.8)]
[charslot(slot="m",name="avg_180_amgoat_1#9$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(duration=1)]
[Delay(time=1.5)]
软绵绵的生物等不到回应，有些急切地跺跺地面，转身准备离开。阿黛尔急忙跟了上去——
一辆车飞驰而过，看到迈开脚步的阿黛尔，慌张地按响喇叭。
[Dialog]
[CameraShake(duration=1, xstrength=35, ystrength=35, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_carhorn", volume=1)]
[PlaySound(key="$drift", volume=0.7,delay=0.2)]
嘀——嘀——！
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_999_1#5$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_999_1#5$1",focus="m")]
[name="凯勒"]唔，我的耳朵......
[charslot(slot="m",name="avg_npc_999_1#10$1",focus="m")]
[name="凯勒"]阿黛尔？你怎么在这里？你不是......？
[charslot(slot="m",name="avg_180_amgoat_1#9$1",focus="m")]
[name="阿黛尔"]凯、凯勒老师，我、我......
[charslot(slot="m",name="avg_npc_999_1#5$1",focus="m")]
[name="凯勒"]......
[name="凯勒"]（果然还是我给她的压力太大了，连阿黛尔这样的孩子都用生病当借口想要休息......）
[name="凯勒"]阿黛尔......
[name="凯勒"]如果你觉得最近压力很大的话，需要休息一天吗？
[Dialog]
[charslot(slot="m",n

... (全文27089字符)
```

### level_act27side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="41_g5_siestaunbuiltland_d",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[PlaySound(key="$beach", channel="bc", loop=true, volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_544_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_1003_1#11$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]......
[charslot(slot="r",name="avg_npc_1003_1#9$1",focus="r")]
[name="锡兰"]我记得这里应该是工业用地，不应该随意靠近的。
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]这是离旧汐斯塔最近的地方，就让我在这里静静吧。
[charslot(slot="r",name="avg_npc_1003_1#9$1",focus="r")]
[name="锡兰"]是吗？可是这里离旧汐斯塔那么远，还看得清什么吗？
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]罗德岛办事处应该离市政厅办公大楼不远。你回到汐斯塔有两个月，也没有来看过我。
[charslot(slot="r",name="avg_npc_1003_1#6$1",focus="r")]
[name="锡兰"]市长先生这段时间难道不该忙得焦头烂额，压根没空看家人一眼吗？
[name="锡兰"]没事的时候在街上随便走走，听听有多少人在骂你，也就大概清楚你最近过得怎么样了。
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]......有许多事，我的确做得还不够好。
[charslot(slot="r",name="avg_npc_1003_1#7$1",focus="r")]
[name="锡兰"]作为一个汐斯塔人，我也想质问市长：
[name="锡兰"]为什么汐斯塔曾经引以为傲的火山、海岸、文化、音乐全都不见了？为什么有那么多人无法融入新的生活市政厅却无能为力？
[name="锡兰"]我还想指责市政厅为什么没有早做搬迁的准备。
[charslot(slot="r",name="avg_npc_1003_1#6$1",focus="r")]
[name="锡兰"]但是作为赫尔曼·道尔科斯的女儿，我还是要说——爸爸，辛苦了。
[charslot(slot="l",name="avg_npc_544_1#9$1",focus="l")]
[name="赫尔曼"]......
[charslot(slot="r",name="avg_npc_1003_1#6$1",focus="r")]
[name="锡兰"]我这次回来，本来是打算帮罗德岛在这里建立办事处，可是我打听到，现在的汐斯塔感染者好像遇到了一些额外的困难。
[charslot(slot="l",name="avg_npc_544_1#6$1",focus="l")]
[name="赫尔曼"]哥伦比亚在法条上咬文嚼字做文章，这不过是哥伦比亚的一张牌。
[name="赫尔曼"]他们不会在意几个感染者的死活，他们只想要从汐斯塔将来的大宗跨国贸易中分一杯羹。
[charslot(slot="r",name="avg_npc_1003_1#6$1",focus="r")]
[name="锡兰"]八千五百七十三。我查过资料。这是截至上个月，在汐斯塔定居的登记在册的感染者的数量。
[name="锡兰"]要么从此禁止感染者在汐斯塔移动地块上定居，要么替他们缴纳巨额的医疗保险。在旁人来看，对于市政厅来说后者完全不能算作选项。
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]我不可能不记得，我的另一个女儿，也是感染者。
[charslot(slot="r",name="avg_npc_1003_1#1$1",focus="r")]
[name="锡兰"]......
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]在汐斯塔短暂的几十年历史中，面对过的刁难也不在少数，但汐斯塔走的路，始终掌握在汐斯塔人自己手里。
[name="赫尔曼"]我会想办法......总会找到路的。
[charslot(slot="r",name="avg_npc_1003_1#1$1",focus="r")]
[name="锡兰"]那就让我来帮一点忙吧。
[name="锡兰"]面对哥伦比亚的文字游戏，你同样可以在移动城市外划定一片地区，宣称汐斯塔会在此进行拓荒，拓荒工作交由感染者来完成。
[name="锡兰"]而至于他们具体的工作——最近来到汐斯塔的那两位朋友，也有意帮助我。一个刚刚起步的物流公司，应该可以提供许多就业岗位。
[name="锡兰"]另外，我会借助罗德岛的资源，在汐斯塔建立感染者治疗中心，这是我一直想要做的事。
[name="锡兰"]为了黑，也为了更多无辜的人。我可不只是需要你照顾的人，我也会用我的方式来保护汐斯塔。
[charslot(slot="l",name="avg_npc_544_1#9$1",focus="l")]
[name="赫尔曼"]我记得我女儿的大学专业，好像不是政治？
[charslot(slot="r",name="avg_npc_1003_1#1$1",focus="r")]
[name="锡兰"]一些不情愿的耳濡目染罢了。
[charslot(slot="l",name="avg_npc_544_1#10$1",focus="l")]
[name="赫尔曼"]虽然政治不是这么简单的事，但你能有这样的心思，我很欣慰。
[charslot(slot="l",name="avg_npc_544_1#9$1",focus="l")]
[name="赫尔曼"]你刚才说的感染者治疗中心的这一部分，我会认真考虑的。与峯驰物流的合作，我也会继续履行。
[charslot(slot="r",name="avg_npc_1003_1#1$1",focus="r")]
[name="锡兰"]从你成为市长以来，汐斯塔对感染者的态度一直都相对宽松。
[name="锡兰"]有人说你是故作姿态，争取矿工们的支持；也有人说你只是为了旅游业能赚来更多钱。
[name="锡兰"]我现在更愿意相信，你做的这些事，和妈妈有关。
[StopSound(channel="bc", fadetime=3)]
[charslot(slot="l",name="avg_npc_544_1#5$1",focus="l")]
[name="赫尔曼"]你......是什么时候知道的......？
[charslot(slot="r",name="avg_npc_1003_1#1$1",focus="r")]
[name="锡兰"]就在刚刚，我听说了一点故事，关于妈妈。
[name="锡兰"]你从来没有主动和我说起这些故事，甚至很少主动和我提起妈妈。
[charslot(slot="l",name="avg_npc_544_1#2$1",focus="l")]
[name="赫尔曼"]......
[charslot(slot="l",name="avg_npc_544_1#1$1",focus="l")]
[name="赫尔曼"]芭芭拉，是维多利亚人。在那个时候的汐斯塔人看来，想要吞并汐斯塔的维多利亚就是最大的敌人。
[name="赫尔曼"]我忙碌于那些有关哥伦比亚和维多利亚的繁重外交工作，却从来不敢让人知道自己的妻子恰好来自维多利亚。
[charslot(slot="l",name="avg_npc_544_1#9$1",focus="l")]
[name="赫尔曼"]芭芭拉却从来没有将这件事放在心上，她有自己的事业。
[name="赫尔曼"]她说，她在以她的方式保护这座城市，也在保护你。
[charslot(slot="r",name="avg_npc_1003_1#9$1",focus="r")]
[name="锡兰"]“用自己的方式保护这座城市......”
[charslot(slot="l",name="avg_npc_544_1#9$1",focus="l")]
[name="赫尔曼"]你从来没有和她共同生活过一天，但是你刚刚和她说了一模一样的话。
[charslot(slot="r",name="avg_npc_1003_1#1$1",focus="r")]
[name="锡兰"]......她是个很好的人。
[charslot(slot="l",name="avg_npc_544_1#10$1",focus="l")]
[name="赫尔曼"]她也有个很好的女儿。
[name="赫尔曼"]......谢谢你，锡兰。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_drone", volume=0.8, loop=false, channel="ph")]
[PlaySound(key="$d_avg_fastener", volume=0.6,delay=2)]
[PlaySound(key="$d_avg_button", volume=0.5,delay=2.5)]
[stopsound(channel="ph",fadetime=3)]
[Delay(time=2)]
[name="诗怀雅"]那个，机位稍微再下调一点，稍微仰拍一点，这样显得我比较有气势......等等，太低了。好，就这样。
[name="诗怀雅"]检查一下录音，接下来我说的每一句话，都要录得清清楚楚。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Image(image="41_i12_1",screenadapt="coverall", fadetime=0)]
[playsound(key="$d_avg_devicebeep")]
[delay(time=0.5)]
[timersticker(x=935,y=80,width=300,size=45,time=9999)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
尊敬的亚当斯·施怀雅先生，您好。和往常一样，先祝您身体健康。
这份光盘寄到您手中的时候，我应该已经结束了汐斯塔的旅行，也完成了我需要达成的一切商业目的。
或许您依旧认为这是一个孩子的胡闹——不，凭您的眼光应当已经认识到了这座城市的价值——一个独立自由的贸易港口能拥有的价值。
我知道从我到汐斯塔的第一天起就有家族的人跟在我周围，监视我的一举一动，或许是您的意思，或许是您的其他继承人对我的阻挠。
但是不重要了，我早就明白揣度您的心思是一件费力且毫无意义的事。
只是，如果站在我的对立面的人是您的话，那么这一次，是我赢了您。
[Dialog]
[musicvolume(volume=0.3, fadetime=1.5)]
[timerclear(afrom=1,ato=0,duration=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="bg_offce", screenadapt="coverall", block=true)]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0

... (全文20959字符)
```

### level_act27side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_beach_1",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.8, block=true)]
[Delay(time=0.5)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="玛格娜"]阿黛尔......真是个好听的名字，我可以直接叫你阿黛尔吗？
[name="玛格娜"]你有听说过吗，每个第一次爬上火山的人都会做的一件事。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="拍照吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[name="玛格娜"]是在岩浆上烤羽兽蛋。
[name="玛格娜"]但我以我爬过二十七座火山的经历向你保证，在烤羽兽蛋方面，岩浆和源石火炉没有任何区别。
[name="卡提亚"]总之都会被你烤糊就是了。
[name="玛格娜"]嘿！明明你每次都吃得很香！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="原来，火山是这个样子......和书上看起来完全不一样。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[name="卡提亚"]不用担心，阿黛尔。你可以跟在我的后面。我踩过的地面总是结实的。
[name="玛格娜"]紧张的话，要不要拉住我的手？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我......还好......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[name="玛格娜"]阿黛尔，你之前不是问我们为什么热爱火山？
[name="玛格娜"]我向你保证，只要你亲眼见过一次火山爆发，就永远无法忘记那种感受。
[name="玛格娜"]我喜欢静静地坐在火山上思考。大地和我们自身都充满谜团，可能穷尽我们一生都无法解答其万一，但我十分享受这种解谜的过程。
[name="卡提亚"]人类发明了移动城市，却至今未能完全弄清天灾形成的原因，人类利用源石创造了许多工具，却对这种石头于我们本身的反噬束手无策。
[name="卡提亚"]人类应该在面对这些自然的伟力时认清自己的渺小，这样他们就不会将太多精力投入到无意义的自相残杀上。
[name="玛格娜"]阿黛尔，不用太在意卡提亚的悲观论调，毕竟这片大地上不是每个地方都像汐斯塔一样单纯。
[name="玛格娜"]作为一个卷在贵族矛盾间的学者，卡提亚有些抱怨也是正常的。不过在这些问题上我一直和他有不同的看法。
[name="玛格娜"]人当然是渺小的，但也正因为渺小，可以让我们在这片大地上有容身之处。
......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, amount=0, block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[Subtitle(text="你说的对，玛格娜。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="生命是那样地渺小，而人偏要以如此渺小的生命向无边际的大地索要答案，那么被大地吞没也是一个可被预见、被接受的命运。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我本该做好准备......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可是在你们离开以后，我自己要怎么面对那样的深渊？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g8_siestavolcanomuseum_inside", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_devicebeep",volume=1)]
[Delay(time=1)]
[name="工作人员"]凯勒教授，这是一号监测站信号丢失前的两个小时里传送回来的数据。
[name="工作人员"]我们从来没有见过这样的异常，只能请您来判断......
[Dialog]
[charslot(slot="l",name="avg_180_amgoat_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_999_1#10$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_999_1#10$1",focus="r")]
[name="凯勒"]地表气体浓度没有变化，为什么温度突然提升了这么多？
[name="凯勒"]如果这个数值是真的，那说明汐斯塔火山里积蓄的能量突然增加了十倍......不，这怎么想都是不可能的事。
[charslot(slot="r",name="avg_npc_999_1#1$1",focus="r")]
[name="凯勒"]......当作异常数据忽视就好。
[name="凯勒"]告知市政厅火山活动更加活跃，让市民们做好准备，我们能做的也没有别的了。
[charslot(slot="l",name="avg_180_amgoat_1#1$1",focus="l")]
[name="阿黛尔"]凯勒老师，这可能不是普通的数据异常。
[name="阿黛尔"]我还记得，在爸爸妈妈的研究笔记里，也提到过几次类似的状况......火山周围的温度异常地高，与其他数值不匹配。
[name="阿黛尔"]虽然始终找不到原因，但很难用巧合解释。
[name="阿黛尔"]凯勒老师，我们不需要去现场确认一下吗？
[charslot(slot="r",name="avg_npc_999_1#1$1",focus="r")]
[name="凯勒"]一号监测站就在火山山腰上，现在正是最危险的时候。
[name="凯勒"]出现这种数据只可能是仪器出了故障，没有必要再冒险去现场查验了。最后的观测结果的数据可以根据其他观测站的数据再做校正。
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="阿黛尔"]凯勒老师，我不明白......
[name="阿黛尔"]您一直在说，这次观测很重要，是许多学者都在等待的机会。这座城市还有几十万人的生活可能会受到影响，难道不应该尽可能严谨吗？
[name="阿黛尔"]如果现在逃避......不就等于承认他们的牺牲是毫无意义的？
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="none")]
女孩声音不大，身体微微颤抖。好像只是这样认真地表达自己的心思，就要耗费她不少力气。
凯勒有些恍然。
[charslot(slot="r",name="avg_npc_999_1#5$1",focus="r")]
[name="凯勒"]是......
[Dialog]
[charslot(slot="r",name="avg_npc_999_1#5$1",focus="none")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="那样的牺牲怎么能说是有意义的？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="阿黛尔"]凯勒老师，我好像不能说服您......
[name="阿黛尔"]如果您不愿意去的话，那我可以自己去吗......
[stopmusic(fadetime=1)]
[charslot(slot="r",name="avg_npc_999_1#6$1",focus="r")]
[name="凯勒"]别开玩笑了，现在火山上状况不明，怎么可能让你自己去那么危险的地方——
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="阿黛尔"]凯勒老师......可以把妈妈的那件防护服，还给我吗？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g6_siestaunbuiltland_n", screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="路人A"]我们除了吃东西，还有什么别的事情可以做？再这么吃下去我肚子就要撑爆了......
[name="路人B"]再听两首吉他曲？
[name="路人A"]嗯......感觉应该会有点更有意思的事情才对的......
[name="路人B"]现在哪有黑曜石音乐节有意思呀？那么多人，那么多游客，看不到尾的街道和店铺，永远也停不下来的音乐声。那个时候多好！
[charslot(slo

... (全文19307字符)
```

### level_act27side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="41_i08",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_underwateramb", channel="volcano", loop=true,volume=0.4)]
[PlaySound(key="$firestorm", volume=0.3, loop=false, channel="vo")]
[PlayMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=1)]
[StopSound(channel="volcano", fadetime=2)]
[StopSound(channel="vo", fadetime=2)]
呼......很舒服的温度。虽然温泉也很有趣，但温度还是太平和了。
这样的温度可以让我头脑清醒，有助于我思考一些很重要的问题。
比如说......世界上是先有岩浆，还是先有岩石？
在最初的最初，“岩浆”并不是“岩浆”，“岩石”也不是“岩石”，物质在循环、转化中分成了不同的样貌，又被赋予了不同的名字。
人们总是在尝试用确定的语言框定世界根本无可描述的本质，仿佛只有这样才能让自己安心睡着一样，这也是缺乏智慧的体现......
嘿，小心点，不要把岩浆抖得到处都是，很危险。虽然概率很小，但万一这时候有人路过——
嗯？怎么吵吵闹闹的......真的有人想加入我们？
[Dialog]
[Delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[image]
[Background(image="41_g11_volcanomountainside", screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.6)]
[PlaySound(key="$smallearthquake", volume=0.6)]
[CameraShake(duration=4, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_sandstone")]
[PlaySound(key="$d_avg_rockfall", volume=0.7,delay=0.2)]
[Delay(time=2)]
脚下巨大的怪物喘息愈加沉重，周围温度又升高了不少。自火山口飞溅出的岩浆快速冷却，化为坚硬的石块翻滚而下。
[Dialog]
[charslot(slot="m",name="avg_1016_agoat2_1#2$1",duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_1016_agoat2_1#2$1",focus="m")]
[name="阿黛尔"]卡恩前辈，凯勒老师......这里很危险......我们还是，先离开......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_996_1#8$1",focus="l")]
[charslot(slot="r",name="avg_npc_999_1#6$1",focus="l")]
[name="卡恩"]阿黛尔，你先离开，我一定要让这个人交代清楚！
[charslot(slot="r",name="avg_npc_999_1#6$1",focus="r")]
[name="凯勒"]卡恩，别犯傻了！
[charslot(slot="l",name="avg_npc_996_1#8$1",focus="l")]
[name="卡恩"]你当初把他们扔在乌纳火山上的时候，他们面对的是比这更恐怖的景象......
[charslot(slot="l",name="avg_npc_996_1#8$1",focus="l")]
[name="卡恩"]你还算有良知吗凯勒，承认自己的罪行，比面对死亡还困难吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",focus="m")]
[name="阿黛尔"]——！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_996_1#8$1",focus="all")]
[charslot(slot="r",name="avg_npc_999_1#6$1",focus="all")]
[Delay(time=0.2)]
[PlaySound(key="$smallearthquake", volume=0.9)]
[CameraShake(duration=4, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[PlaySound(key="$bodyfalldown2",volume=0.8)]
[PlaySound(key="$bodyfalldown1",volume=0.7,delay=0.1)]
[charslot(slot="l",name="avg_npc_996_1#8$1",afrom=1,ato=0,duration=0.6)]
[charslot(slot="r",name="avg_npc_999_1#6$1",afrom=1,ato=0,duration=0.4)]
[delay(time=1.2)]
[charslot]
[PlaySound(key="$d_avg_runstop")]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",duration=0.5)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_firemagic", volume=0.6)]
[Blocker(a=0, r=0.4, g=0.1, b=0.1, fadetime=0, block=true)]
[Blocker(a=0.3, r=0.4, g=0.1, b=0.1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.4, g=0.1, b=0.1, fadetime=0.1, block=true)]
[CameraShake(duration=2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$firemagic_explosion", volume=0.5)]
[playsound(key="$d_avg_explosion_stone",volume=0.6,delay=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",focus="m")]
[name="阿黛尔"]卡恩前辈......快点离开......
[name="阿黛尔"]我可能挡不住下一波......
[Dialog]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",focus="m")]
[Delay(time=0.2)]
[Effect(name="$e_magic_fire_01",rox=73,layer = 1)]
[PlaySound(key="$b_char_fireharm", volume=1)]
[PlaySound(key="$firemag_n", volume=1,delay=0.2)]
[Blocker(a=0, r=0.4, g=0.1, b=0.1, fadetime=0, block=true)]
[Blocker(a=0.3, r=0.4, g=0.1, b=0.1, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.4, g=0.1, b=0.1, fadetime=0.3, block=true)]
[CameraShake(duration=3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[playsound(key="$d_avg_explosion_stone",volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$firemagic_explosion", volume=1)]
[playsound(key="$d_avg_explosion_stone",volume=0.7,delay=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.6, block=true)]
[delay(time=0.5)]
[charslot]
[name="卡恩"]当心身后！
阿黛尔举起了法杖，可落石如雨点般落下，她的源石技艺也来不及将它们一一熔化。
她专注于保护同伴安全，却偏偏没有听到旁边的人的警告，也没有听到身后危险的响动。
[stopmusic(fadetime=1.5)]
[name="凯勒"]——！
[Dialog]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[PlaySound(key="$bodyfalldown1", volume=1, delay=0.4)]
[CameraShake(duration=1, xstrength=15, ystrength=15,vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="r",name="avg_npc_999_1#3$1",posfrom="0,0",posto="-100,0",duration=0.2)]
[delay(time=0.2)]
[charslot(slot="r",posfrom="-100,0",posto="-150,-20",duration=0.8,isblock=false)]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",posfrom="0,0",posto="-60,-40",duration=0.7,isblock=false)]
[charslot(slot="m",name="avg_1016_agoat2_1#5$1",afrom=1,ato=0,duration=0.4)]
[charslot(slot="r",afrom=1,ato=0,duration=0.4)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_npc_1014_1#1$1",afrom=0,ato=0,action="zoom",poszoom="0.5,0.5",scale=0.2,duration=0,isblock=false)]
[Delay(time=0.1)]
[PlaySound(key="$d_avg_b

... (全文29167字符)
```

### level_act27side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act27side/SL01.mp4")]
```

### level_act27side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Sticker(id="st1", text="如今，独立城邦大都被国家吞并或接近消亡，汐斯塔这座特殊的独立城市却是镶嵌在南方漫长海岸线上的旧日遗珠，正是我们研究现代独立城邦的绝佳范例。", x=300, y=250,alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st4", text="——《大地巡旅》", x=300, y=450,alignment="right", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1")]
[Sticker(id="st4")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[delay(time=0.5)]
[PlaySound(key="$beach", volume=0.6, loop=true, channel="2")]
[PlaySound(key="$d_avg_sea", volume=1, loop=true, channel="1")]
[delay(time=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_beach_2",screenadapt="showall",xScale=1.5,yScale=1.5,x=0,y=0,fadetime=0,block=true)]
[BackgroundTween(xScaleFrom=1.5, yScaleFrom=1.5, xScaleTo=1.6, yScaleTo=1.6,xFrom=0,xto=80,yFrom=0,yto=100,duration=20, block=false,screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
搞错了，又搞错了。好，从头再数一遍。
一只、两只、三只......
五千七百六十一、五千七百六十二......是不是还有几只落在莱塔尼亚了?
算了，随他们去玩吧。是该撬动一下那些像山羊胡一样又瘦又高又古板的建筑，还有那些人脸上僵硬得和他们的音乐如出一辙的表情。
时间很宝贵，至少对他们来说是这样。如果他们不能在有限的时间里制造点有趣的新东西，我就要一起忍受停滞且空虚的岁月，真要命。
这时候竟然会有些怀念被那些长毛獠牙的家伙追着跑的日子，不过他们现在好像在叙拉古发明了一种新游戏，不再找我玩了。
唉，我也该找点新乐子了。
世界总该是富于变化的，“存在”本身就代表“变化”，为什么还有那么多人要因为这样常见的事陷入困顿？
就像是盖房子一样，今天总是要比昨天盖得更高一点。可竟然还有人想要回过头去拆掉以前的部分，真是......饶了我吧。
这些脆弱又短暂的生命能活得再长一点的话，他们就理应拥有像我这样丰富的智慧。应该理解存在，或者说存在过的意义。
可能只有少部分人能想明白这个道理的吧，就像那首歌，是怎么唱的来着？调子是啦啦啦......噔......
该死，又忘了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[delay(time=2.5)]
喂——
怎么又是你？最近我已经见过你好几次了！
这座火山很快就要爆发了，你最好别再往前走了！
说了多少遍，那些黑乎乎的石头不是什么好东西，你们为什么——
唉，忘了......为什么只有在他们眼前现身他们才能听到我讲话，这也太麻烦了。
算了，还是不要过度介入他们的生活为好......祝他好运吧。
嗯，刚才数到哪了......
[Dialog]
[StopSound(channel="1", fadetime=1)]
[StopSound(channel="2", fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2.5, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[PlaySound(key="$d_avg_guitartap", volume=1, channel="3")]
[delay(time=0.45)]
[PlaySound(key="$d_avg_guitartap", volume=1, channel="4")]
[delay(time=2)]
[PlaySound(key="$d_avg_wdnguitarpizz", volume=1, channel="2")]
[delay(time=4)]
[PlaySound(key="$d_avg_guitarmusic", volume=1, loop=true, channel="1")]
[delay(time=1.5)]
[Subtitle(text="我十七岁时出发寻找故乡，至今仍在游荡♪", x=300, y=370, alignment="center", size=24, delay=0.08, width=700)]
[Subtitle(text="给羽兽指路，向冒险家询问智慧♪", x=300, y=370, alignment="center", size=24, delay=0.08, width=700)]
[Subtitle(text="跟着商队交易宝藏，转眼又被抛在路旁♪", x=300, y=370, alignment="center", size=24, delay=0.08, width=700)]
[Subtitle(text="我会记得遇到的所有人，再给他们取别的名字♪", x=300, y=370, alignment="center", size=24, delay=0.08, width=700)]
[Subtitle(text="不用再给我寄信了♪", x=300, y=370, alignment="center", size=24, delay=0.08, width=700)]
[Subtitle(text="除非你寄信的时候，是和我一样在荒凉的路上♪", x=300, y=370, alignment="center", size=24, delay=0.08, width=700)]
[Subtitle]
[Background(image="41_g1_siestacommercialstreet_d",screenadapt="showall")]
[StopSound(channel="1", fadetime=4)]
[Delay(time=5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[PlaySound(key="$d_avg_wdnguitarstrum", volume=1, channel="3")]
[charslot(slot="m",name="avg_npc_993_1#1$1",duration=1)]
[delay(time=3.5)]
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]弹得不错。是二十年前流行的曲调。
[charslot(slot="m",name="avg_npc_993_1#8$1",focus="m")]
[name="弹吉他的歌手"]多谢夸赞。
[name="弹吉他的歌手"]希望这首老气的歌没有耽误您的生意。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]哈哈，这玩笑可一点都不好笑。看看这周围，哪还有半个游客。
[name="路边的老人"]火山把汐斯塔人赶走了，太阳把吵闹的游客赶走了。
[name="路边的老人"]只剩下不知道多少年都没体验过的清闲夏天，还有一种即将破产的无忧无虑的快乐。
[charslot(slot="m",name="avg_npc_993_1#1$1",focus="m")]
[name="弹吉他的歌手"]我猜您一定很怀念过去几年汐斯塔游人如织的时候。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]谁会和钱过不去呢。但我更怀念人们对摇滚乐还有审美的年代。
[name="路边的老人"]那时人们还有闲有钱，可以坐下来谈谈虚头巴脑的音乐艺术，畅想一下不着实际的将来。
[charslot(slot="m",name="avg_npc_993_1#2$1",focus="m")]
[name="弹吉他的歌手"]就像大家说的，“要想搞艺术，先要填饱肚”。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]摇滚的黄金年代到底是过去了，现在太多年轻人把摇滚精神粗暴地理解为躁动的节拍和电子混响，越吵闹越好。
[name="路边的老人"]却忘了在最初的最初，憧憬只存于幻想中的美好也是摇滚精神核心的一部分。
[name="路边的老人"]就像你刚才弹的那首，优雅且清爽的和弦，我很喜欢。
[charslot(slot="m",name="avg_npc_993_1#1$1",focus="m")]
[name="弹吉他的歌手"]听起来您也很懂音乐。会什么乐器吗？
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]贝斯和手风琴。
[charslot(slot="m",name="avg_npc_993_1#8$1",focus="m")]
[name="弹吉他的歌手"]喔喔，很时尚。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]再弹一首吧年轻人，刚才这杯酒算我的。
[charslot(slot="m",name="avg_npc_993_1#8$1",focus="m")]
[name="弹吉他的歌手"]感谢您的慷慨，我想您也一定不介意我为这首曲子要价高一点，“一个故事”怎么样？
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]哈，真是老掉牙的开价。
[name="路边的老人"]年轻人，是从哪来的，怎么称呼？
[charslot(slot="m",name="avg_npc_993_1#1$1",focus="m")]
[name="弹吉他的歌手"]伯德，哥伦比亚。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]哥伦比亚人，我以为每一个哥伦比亚人都应该像荒地上刨土的沙地兽一样，无时无刻不在荒地上耕作呢——就和当年的我父母一样。
[charslot(slot="m",name="avg_npc_993_1#1$1",focus="m")]
[name="伯德"]我是在拓荒，不过是精神上的拓荒。
[charslot(slot="m",name="avg_npc_993_1#8$1",focus="m")]
[name="伯德"]我想要再看看，过去的哥伦比亚人，来到这片海岸时看到了怎样的景色，又是为什么决定在这里安家的。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]那你大概是来晚了，那段海岸线已经被丢在了那座火山脚下了。
[name="路边的老人"]现在这座安在移动地块上的城市，和哥伦比亚、维多利亚，又有什么区别呢？
[name="路边的老人"]能有什么办法，“大地赐予你的，也能收回去”。
[charslot(slot="m",name="avg_npc_993_1#1$1",focus="m")]
[name="伯德"]所以我很想听听这里的故事，或许能从中一窥过去的风貌。
[charslot(slot="m",name="avg_npc_1002_1#1$1",focus="m")]
[name="路边的老人"]好啊，那我就讲讲，这些执拗的人们是如何在搬离原来的海岸线后，还要固执地把所谓的火山温泉和海滨风情街搬到新家的故事吧。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_pick_lock", volume=1, channel="1")]
[PlaySound(key="$aluminum", volume=1, channel="2")]
[PlaySound(key="$d_avg_axehitscrape", volume=1, ch

... (全文40034字符)
```

### level_act27side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g9_purewhitevolcano_inside",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_dream", volume=0.4)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[delay(time=0.5)]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.6)]
夕阳似乎是这家小店的最后一个客人，但站在柜台后的不再是熟悉的老人，而是一只咖啡色的生物。
它旋转着研磨机的手柄，咖啡的香气和细碎的豆末飞进空气中。
唱片慢慢地转着，扩音器悠悠地唱。
[Dialog]
[PlaySound(key="$d_avg_doorbell",volume=0.8)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1009_1#1$1",focus="m")]
[name="咖啡色的生物"]哦，欢迎光临。
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_1016_agoat2_1#1$2",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_1016_agoat2_1#1$2",focus="m")]
[name="阿黛尔"]之前好像从来没有见过您，您是刚到这里的吗？
[charslot(slot="m",name="avg_npc_1009_1#1$1",focus="m")]
[name="咖啡色的生物"]应该是的，因为我没有昨天的记忆。我不知道我为什么在这里，但我觉得我应该在这做一杯咖啡......唔，你想喝一杯吗？
[name="咖啡色的生物"]咖啡只有亲手冲煮才能做出灵活美妙的风味。让我找找，新到的种子放在哪里了，应该是我自己收起来的......
[name="咖啡色的生物"]好像是在什么吉他的后面，嗯......说起吉他突然觉得有点生气，奇怪，是什么让我心里堵得慌呢？
[charslot(slot="m",name="avg_1016_agoat2_1#7$2",focus="m")]
[name="阿黛尔"]吉他？生气？您还好吗？
[charslot(slot="m",name="avg_npc_1009_1#1$1",focus="m")]
[name="咖啡色的生物"]算了，可能是因为那个吉他看起来没那么有趣吧。
[name="咖啡色的生物"]请随便坐，你等的人马上就到了。
[charslot(slot="m",name="avg_1016_agoat2_1#11$2",focus="m")]
[name="阿黛尔"]我要等的人......？
[charslot(slot="m",name="avg_npc_1009_1#1$1",focus="m")]
[name="咖啡色的生物"]你要等的，还是在等你的？我分不清。
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_doorbell",volume=0.8)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1007_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]唔，你在这。
[charslot(slot="m",name="avg_1016_agoat2_1#9$2",focus="m")]
[name="阿黛尔"]我......记得您。
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]晚上好，阿黛尔，很抱歉我来迟了——今天有记得吃早餐吗？
[charslot(slot="m",name="avg_1016_agoat2_1#1$2",focus="m")]
[name="阿黛尔"]嗯，吃了。
[charslot(slot="m",name="avg_1016_agoat2_1#7$2",focus="m")]
[name="阿黛尔"]欸？您为什么问这个？
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]乖孩子。
[name="温和的生物"]你已经换好了衣服，是准备好了吗？
[charslot(slot="m",name="avg_1016_agoat2_1#7$2",focus="m")]
[name="阿黛尔"]衣服......？欸，这件外衣不是妈妈的......？
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]收拾好东西出门吧，我们一起购物，去买一些攀登火山要用的东西。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g2_siestacommercialstreet_n", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$EyjafjallaDream_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
太阳一点一点地坠了下去，沿路店铺里的灯光星星点点亮了起来。阿黛尔眼前有些模糊，她仿佛在某处某时见过这样的天空。
莱塔尼亚南境的那座小城，记忆里校园通往家的路上，是不是也有这么一小段街道？
她甚至还记得那时空气里的味道。微微湿润，带着一点点阳光和植物生长的气味，和现在的一模一样。
[Dialog]
[charslot(slot="m",name="avg_1016_agoat2_1#4$2",focus="m")]
[name="阿黛尔"]这里，是你们的商场吗？
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]是的，在爬上火山前，我们需要先做一些准备。
[charslot(slot="m",name="avg_1016_agoat2_1#1$2",focus="m")]
[name="阿黛尔"]我知道，要准备的东西有很多，指南针、防护服、相机......如果要在山上过夜的话，还要带上火石和帐篷。
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]不，在这里我们不用准备这些。
[name="温和的生物"]首先要买够的是“知识”，“勇气”和“好奇”，看看价格买一样就好，最后再买一点“好运”。
[name="温和的生物"]但是“好运”很贵，又常常是卖得最快的，所以预算不够的话也可以不用买。
[charslot(slot="m",name="avg_1016_agoat2_1#4$2",focus="m")]
[name="阿黛尔"]这样啊......
[Dialog]
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[Delay(time=0.2)]
[charslot(slot = "m", action="shake",random=true, power=5, times=60,duration=0.6)]
[PlaySound(key="$d_avg_coin")]
[PlaySound(key="$d_avg_coin", loop=false,channel="coin1",delay=0.6)]
[Delay(time=1.5)]
软绵绵的生物抖了抖身子，几枚汽水瓶盖从她的绒毛里掉了出来。丁零哐啷，瓶盖落入商人的口袋。
[Dialog]
[charslot(slot="m",name="avg_npc_1011_1#1$1",focus="m")]
[name="精明的生物"]谢谢您的慷慨！
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]唔......我可能还需要再买一点“勇气”。
[name="温和的生物"]登上火山的“勇气”已经足够，我需要一点离开家的“勇气”。
[Dialog]
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[Delay(time=0.2)]
[charslot(slot = "m", action="shake",random=true, power=8, times=80,duration=1)]
[PlaySound(key="$d_avg_coin")]
[PlaySound(key="$d_avg_coin", loop=false, channel="coin2",delay=0.6)]
[PlaySound(key="$d_avg_coin", loop=false, channel="coin3",delay=1.1)]
[Delay(time=1.5)]
软绵绵的生物再次抖了抖身子，几枚瓶盖掉了出来。商人张开口袋，等待着更多。
[Dialog]
[charslot(slot="m",name="avg_npc_1011_1#1$1",focus="m")]
[name="精明的生物"]不够呢，不够呢。
[name="精明的生物"]口袋没有满起来，口袋没有满起来，“勇气”不能给你了。
[charslot(slot="m",name="avg_1016_agoat2_1#11$2",focus="m")]
[name="阿黛尔"]买不到“勇气”的话，您是不是就没办法爬火山了？
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]没关系的，阿黛尔，这样的事总会发生。我已经渐渐地习惯于自己给自己找寻“勇气”了。
[name="温和的生物"]阿黛尔，我们走吧。而且，这一路我们都要小心点，要看好自己的东西。
[charslot(slot="m",name="avg_1016_agoat2_1#9$2",focus="m")]
[name="阿黛尔"]东西？可是我没有带什么东西呀。
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]有人想要偷走“照片”。
[name="温和的生物"]跟在我后面，帮我看好我的包裹好吗？
[charslot(slot="m",name="avg_1016_agoat2_1#7$2",focus="m")]
[name="阿黛尔"]......您刚刚说什么？我没有听清......
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]这样下去可不行，阿黛尔，这个给你。
[Dialog]
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[Delay(time=0.2)]
[charslot(slot = "m", action="shake",random=true, power=5, times=60,duration=0.5)]
[Delay(time=1)]
软绵绵的生物抖抖身子，从她身上掉下一团羊毛。
[charslot(slot="m",name="avg_1016_agoat2_1#9$2",focus="m")]
[name="阿黛尔"]这是......？
[charslot(slot="m",name="avg_npc_1007_1#1$1",focus="m")]
[name="温和的生物"]来，把它戴一点在耳朵上，你就能听到了。
[name="温和的生物"]然后，我们还要去找下一位。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="41_g2_siestacommercialstreet_n", screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]

... (全文18134字符)
```

### level_act27side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="41_g11_volcanomountainside",screenadapt="coverall")]
[Delay(time=0.5)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
有生态学者，将这片大地上所有的羽兽分为了两类，“候羽”与“留羽”。
前者会因为气候、生态的变化，不断搬迁，寻找最适合自己生存的地方；而后者一旦安家，就会永远留下，想方设法地守护好家园。
这一生物学说后来被历史学家借用，有人提出，“大地上所有族群之间的矛盾，都是只能生活在一个地方的人和四处漂流的人的矛盾”。
在这之后，又有人对这种观点提出了补充。
这片大地上原本没有留羽，但是慢慢地，羽兽们在某个地方聚集，一起建构家园，创造共同的回忆，也就出现了留羽。
......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.3, fadetime=1)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Delay(time=2)]
[name="寻找汐斯塔的少女"]这次一定不会搞错了，按地图上的路线，翻过这座山头就是汐斯塔了。
[name="寻找汐斯塔的少女"]汐斯塔，是在这里吧......
放眼望去，目之所及，只剩一片雪白。
[name="寻找汐斯塔的少女"]这......这是哪啊？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="41_g7_siestahightechtouristzone", screenadapt="coverall", block=true)]
[delay(time=1)]
[musicvolume(volume=0.6, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="char_105_emper",duration=0.7)]
[charslot(slot="r",name="avg_npc_993_1#4$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="char_105_emper",focus="l")]
[name="大帝"]哟，好久不见了。
[charslot(slot="r",name="avg_npc_993_1#4$1",focus="r")]
[name="伯德"]咦，不是为了参加黑曜石音乐节，大帝先生又为什么会光临这里？您的衣服，好像烧破了一个洞......？
[charslot(slot="l",name="char_105_emper",focus="l")]
[name="大帝"]我们应该立即马上换一个话题。
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]这几天收集到了很不错的素材，回哥伦比亚后应该可以很快创作出一张专辑。
[charslot(slot="l",name="char_105_emper",focus="l")]
[name="大帝"]能让我有所期待的音乐家已经不多了，伯德，你可以算一个。
[charslot(slot="r",name="avg_npc_993_1#7$1",focus="r")]
[name="伯德"]不禁想起了参加第一届黑曜石音乐节的时候，芭芭拉女士和我说起过她想象中的汐斯塔的将来。
[name="伯德"]如果有一天，这座城市离开了火山和黑曜石，离开了风景迷人的海岸线，那么这座城市还剩什么呢？
[name="伯德"]她说音乐是一种载体，但生活在这的人们才是最重要的载体。
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]只要还有人会愿意在开心或不开心时唱歌，愿意在傍晚来临时欣赏一会晚霞，汐斯塔就还是那个汐斯塔。
[charslot(slot="l",name="char_105_emper",focus="l")]
[name="大帝"]年轻人不要总是那么怀旧，不然创作出的音乐也会变得老掉牙的。
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]这就有点强人所难了大帝先生。
[name="伯德"]即使是在人短暂的一生当中，如果不时时回顾一下自己是怎样一路走来的，也会感到迷失方向的。
[name="伯德"]还是要偶尔回头看看，是不是有什么珍贵的东西被落在了路上。
[charslot(slot="l",name="char_105_emper",focus="l")]
[name="大帝"]如今过去的一切都埋在那座火山下了，怎么样，要不要准备策划一下黑曜石音乐节2.0？正好我有一些投资打算。
[charslot(slot="r",name="avg_npc_993_1#1$1",focus="r")]
[name="伯德"]要重新举办的话，是不是该新起一个名字？
[charslot(slot="r",name="avg_npc_993_1#8$1",focus="r")]
[name="伯德"]火山音乐节？好像还是太普通了一点......对了，这次来到汐斯塔，我见到了一种很可爱的动物。就叫“棉花糖音乐节”怎么样？
[charslot(slot="l",name="char_105_emper",focus="l")]
[name="大帝"]真棒，伯德。你起名字的品味不及你乐品的千分之一。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="41_g8_siestavolcanomuseum_inside", screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_1016_agoat2_1#1$2",duration=0.7)]
[charslot(slot="r",name="avg_npc_999_1#8$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_1016_agoat2_1#1$2",focus="l")]
[name="阿黛尔"]凯勒老师，火山观测资料都在这里了。
[name="阿黛尔"]这次观测得到了很有价值的资料，我会把它们整理完之后再回去。
[charslot(slot="r",name="avg_npc_999_1#8$1",focus="r")]
[name="凯勒"]辛苦你了......
[name="凯勒"]你果然已经是一个可以独当一面的学者了，卡提亚和玛格娜会为你感到骄傲的......
[name="凯勒"]这件防护服也......比起在展柜中，果然还是......
[charslot(slot="r",name="avg_npc_999_1#8$1",focus="none")]
学者的声音低了下去，她久久凝视着这件熟悉的外套。
[charslot(slot="l",name="avg_1016_agoat2_1#1$2",focus="l")]
[name="阿黛尔"]我想带着母亲的防护服去踏上更多的火山，它会保护我的。也谢谢您这段时间的指导，我学到了很多......
[charslot(slot="l",name="avg_1016_agoat2_1#1$2",focus="l")]
[name="阿黛尔"]对了，卡恩前辈呢？
[charslot(slot="r",name="avg_npc_999_1#8$1",focus="r")]
[name="凯勒"]因为一些工作，提前返回莱塔尼亚了。
[charslot(slot="l",name="avg_1016_agoat2_1#2$2",focus="l")]
[name="阿黛尔"]凯勒老师，我想替卡恩前辈向您道歉，他应该是误会了什么......
[charslot(slot="r",name="avg_npc_999_1#8$1",focus="r")]
[name="凯勒"]......我不会在意。
[charslot(slot="r",name="avg_npc_999_1#10$1",focus="r")]
[name="凯勒"]阿黛尔......你从来没有怀疑过我？
[charslot(slot="r",name="avg_npc_999_1#10$1",focus="none")]
阿黛尔轻轻摇了摇头。
[charslot(slot="l",name="avg_1016_agoat2_1#9$2",focus="l")]
[name="阿黛尔"]我不知道......
[name="阿黛尔"]那段时间的事我知道的很少，好像所有人都在有意瞒着我一样。
[name="阿黛尔"]但是我看过父母的笔记，还有那些照片......
[name="阿黛尔"]我没法相信，一个和他们一同去过那么多火山，共同经历过那么多次危险的人，会做出背叛他们的事......
[charslot(slot="r",name="avg_npc_999_1#1$1",focus="r")]
[name="凯勒"]我有东西，想给你看。
[charslot(slot="r",name="avg_npc_999_1#5$1",focus="r")]
[name="凯勒"]卡恩这几天一直想找的，应该就是这些东西吧。
[name="凯勒"]这些文件，除了莱塔尼亚官方档案库，只有我手上的一份。
[name="凯勒"]是废弃的文件，已经算不上什么机密，我只是希望永远不会有人再找到它......
[Dialog]
[charslot(slot="r",name="avg_npc_999_1#1$1",focus="none")]
[PlaySound(key="$d_avg_cardboard", volume=1)]
[Delay(time=1)]
学者从书柜中拿出一方纸箱，两位学者存在过的痕迹，容纳在这一方小小的箱子里。
陈旧的文件袋上写着“高级机密”之类的字样，上面还盖着“已废弃”的印章。
“阵雨计划”。
[charslot(slot="l",name="avg_1016_agoat2_1#4$2",focus="l")]
[name="阿黛尔"]这就是......爸爸的研究军用化的项目吗......
[charslot(slot="r",name="avg_npc_999_1#5$1",focus="r")]
[name="凯勒"]卡提亚和玛格娜毕生的愿望，就是当一名纯粹的学者，他们的确在竭尽全力地去践行这个理想。
[name="凯勒"]但现实往往是很难纯粹的......
[name="凯勒"]莱塔尼亚二十多年前政变的余波，贵族之间的纠纷始终在纠缠着他们。为了研究能进行下去，他们不得不做出妥协。
[name="凯勒"]卡提亚将自己一部分研究成果交给了军队，以换取相对安稳的学术环境。我则是帮他分担了后续的一些对接工作。
[name="凯勒"]但是他们将希望寄托在了你的身上。
[name="凯勒"]他们希望可以将这些不纯粹的纠纷阻隔在你的生活之外，让你可以心无旁骛地去研究你感兴趣的问题。
[name="凯勒"]这也是，我的愿望......
[Dialog]
[charslot(duration=0.3)]
[Delay(time=0.5)]
我希望多年后，人们提起瑙曼夫妇时，只会记得他们是纯粹而伟大的科研学者，我希望他们唯一的孩子，可以无忧无虑地探索知识。
[charslot(slot="l",name="avg_1016_agoat2_1#2$2",focus="l")]
[charslot(slot="r",name="avg_npc_999_1#5$1",focus="l")]
[name="阿黛尔"

... (全文21231字符)
```

### training_act27side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_01_a

[PopupDialog(dialogHead="$avatar_melan")] 博士，捣乱的生物们已经处理完毕。

[Tutorial(focusX=-200, focusY=-30, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]不过这些生物在消失时，会在地上留下洋红蒸汽。

[Tutorial(focusX=-200, focusY=-30, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这些洋红蒸汽产生时会对接触到的干员造成法术伤害与灼燃损伤。

[PopupDialog(dialogHead="$avatar_melan")] 如果持续停留在洋红蒸汽中，我方干员受到的伤害会大幅增加。
```

### training_act27side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_01_b

[PopupDialog(dialogHead="$avatar_adnach")] 而且，处于洋红蒸汽中的捣乱生物受到的伤害会大幅降低。

[PopupDialog(dialogHead="$avatar_melan")] 这些生物更喜欢在洋红蒸汽中玩乐，处理起来会更棘手。

[PopupDialog(dialogHead="$avatar_melan")] 不要被它们的外表蒙蔽了，注意躲避洋红蒸汽哦。


```

### training_act27side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_01_c

[PopupDialog(dialogHead="$avatar_amgoat")] 前辈，我来协助你。

[Tutorial(focusX=100, focusY=-20, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amgoat",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这个是汐斯塔的景观喷泉，站在它周围就不会受到洋红蒸汽的影响啦。

[Tutorial(focusX=-10, focusY=130, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amgoat",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]站在景观喷泉旁边，我攻击地面单位时它们的脚下还会生成纯白水汽。

[PopupDialog(dialogHead="$avatar_amgoat")]在纯白水汽中，这些淘气的生物受到的伤害会大幅增加，同时，我方干员受到的伤害也会大幅降低哦。
```

### training_act27side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_01_d

[Tutorial(focusX=275, focusY=-30, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amgoat",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]啊......那些生物跑去另一边了，我碰不到它们......

[Tutorial(focusX=-65, focusY=65, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightRect", anchor="BottomRight", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_bryota",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]试一试风情街的特产——水汽汽水瓶吧！打破它也会产生纯白水汽。

[PopupDialog(dialogHead="$avatar_bryota")] 水汽汽水瓶可以部署在地图的任何角落，借助它，我们可以让纯白水汽布满这一片区域。

[PopupDialog(dialogHead="$avatar_bryota")] 水汽汽水瓶数量很多，要多少有多少。纯白水汽不断增加，水汽汽水瓶的再部署时间也会随之缩短的！

[PopupDialog(dialogHead="$avatar_amgoat")] 捣乱的生物们又来啦。前辈，一起阻止它们吧！

```

### training_act27side_02_a

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_02_a

[Tutorial(focusX=95, focusY=55, focusWidth=300, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_bison",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这个地方闪闪发光，有点奇怪。

[PopupDialog(dialogHead="$avatar_ceylon")] 这是“好朋友”存在的迹象。

[PopupDialog(dialogHead="$avatar_ceylon")] 如果“好朋友”所处的地方出现了洋红蒸汽或者纯白水汽，它们就会显形。随后便立刻爆炸，产生同样颜色的气体。
```

### training_act27side_02_b

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_02_b

[PopupDialog(dialogHead="$avatar_spking")] 啊哈！我来咯！

[Tutorial(focusX=0, focusY=70, focusWidth=125, focusHeight=50, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_bison",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]呃啊——我们的攻击就像在给多利挠痒痒啊......是因为他的“绒毛护盾”吗？
```

### training_act27side_02_c

```
[HEADER(is_skippable=true, is_autoable=false)] act27side_02_c

[Tutorial(focusX=0, focusY=188, focusWidth=125, focusHeight=50, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amgoat",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]嗯，不过站在景观喷泉周围攻击他的话，可以削弱他的护盾哦。

[PopupDialog(dialogHead="$avatar_bryota")] 还有！打破水汽汽水瓶可以大幅度削弱多利的护盾！
```


> 本章节共33个脚本文件，此处展示前30个。

## 统计

- 总字符数：461662
- 对话行数：3246


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
