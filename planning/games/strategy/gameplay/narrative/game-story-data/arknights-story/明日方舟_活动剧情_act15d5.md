# 明日方舟 · 活动剧情 · act15d5（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act15d5」完整剧情脚本（7个文件，1856行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act15d5
- 脚本文件数：7

### level_act15d5_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lungmen_o",screenadapt="coverall")]
[playMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_136_hsguma_ns_1",fadetime=1,block=true)]
[delay(time=1)]
[name="星熊"]  （哈欠）
[name="星熊"]  被褥叠成豆腐干，这样就成了。
[Dialog]
[Character(name="char_136_hsguma_ns_1")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="星熊"]  钱包，钥匙，外套......
[name="星熊"]  通讯设备，不带了。
[name="星熊"]  盾......也算了，老伙计，今天你就休息一下。
[name="星熊"]  鞋就穿这双吧，嗯，不对，不好，要不然还是穿这双限定版的？啊，这双感觉也不错，和今天的衣服挺搭。
[Character(name="char_136_hsguma_ns_1")]
[name="星熊"]  ......
[delay(time=0.4)]
[Character(name="char_136_hsguma_ns_1")]
[name="星熊"]  唉，不然还是换回这双吧。
[Dialog]
[Character]
[Character(name="char_308_swire_1#1",fadetime=1,block=true)]
[Delay(time=1)]
[name="诗怀雅"]  （白眼）
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#1",focus=1)]
[name="星熊"]  Missy，正好，你觉得哪双最顺眼？
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#5",focus=2)]
[name="诗怀雅"]  别问我，我现在看你哪儿都不顺眼。
[Character(name="char_136_hsguma_ns_1#3",name2="char_308_swire_1#5",focus=1)]
[name="星熊"]  怎么了，你今天脾气不太好。特殊日子？
[Character(name="char_136_hsguma_ns_1#3",name2="char_308_swire_1#6",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="诗怀雅"]  我好你*龙门粗口*！
[name="诗怀雅"]  一大早敲我门到底干嘛？！就为了看你数鞋？你收藏了这么多鞋我都看不出有什么大区别！
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#6",focus=1)]
[name="星熊"]  那怎么能一样，版型和材质都差远了......哎，我和你说这些干什么。
[name="星熊"]  看在咱们宿舍挨着，算邻居的份上，互帮互助嘛。
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#6",focus=2)]
[name="诗怀雅"]  我管你啊！
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#5",focus=2)]
[name="诗怀雅"]  搞清楚，今天可是休息日！现在还差三分钟到六点，我只要按下这个报警器，立刻就能告你扰民！
[name="诗怀雅"]  你想加班就自己去，整天这么工作迟早脱发谢顶，少拖上我一起！
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#5",focus=1)]
[name="星熊"]  加班就算了吧，难得的休假，近卫局加班费发得又不多，还挺抠门的。我又不是老陈那个工作狂。
[name="星熊"]  而且Missy，这一点上你也不好说我吧？你是不是才刚从近卫局回来，我听见你开门又摔门的声音了，真够响的。
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#6",focus=2)]
[name="诗怀雅"]  啰嗦！我烦得很！
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#1",focus=2)]
[name="诗怀雅"]  最近事情那么多，又有整合运动留下的烂摊子，还有那只臭老鼠那边的事......那个扑街龙关键时候又不在，哪一件不要处理？
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#5",focus=2)]
[name="诗怀雅"]  你升个职，他们还想着要把你调走，调到哪去？特别督查组难道就交给别人？！
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#6",focus=2)]
[name="诗怀雅"]  真是气死我了！
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#6",focus=1)]
[name="星熊"]  别气，别气。魏先生不是没考虑，这是要练你。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#6",focus=1)]
[name="星熊"]  将来近卫局还要靠你撑着，要我说，迟早的事。
[name="星熊"]  你可以的。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#6",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="诗怀雅"]  ......你......你又说这样的话，这些我当然知道！
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#1",focus=2)]
[name="诗怀雅"]  可、可担着近卫局的本来可以是......本来应该是......
[name="诗怀雅"]  ......
[Character(name="char_136_hsguma_ns_1#2",name2="char_308_swire_1#1",focus=1)]
[name="星熊"]  唉，你可别又哭了。
[Character(name="char_136_hsguma_ns_1#2",name2="char_308_swire_1#6",focus=2)]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="诗怀雅"]  谁哭了！
[Character(name="char_136_hsguma_ns_1#2",name2="char_308_swire_1#5",focus=2)]
[name="诗怀雅"]  等着瞧，那条臭龙不回来拉倒，迟早有一天我会拿下近卫局。都给我等着瞧。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#5",focus=1)]
[name="星熊"]  哈哈，那还真是令人期待。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#1",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="诗怀雅"]  唉，不对，等等，你刚刚说，听到我回来时候开门的声音了？所以你是知道我一晚上没睡？
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#6",focus=2)]
[name="诗怀雅"]  那你还来叫我干嘛，还说自己不是故意的？！
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#6",focus=1)]
[name="星熊"]  哎，哎，别激动。
[name="星熊"]  这不是怕你把自己逼得太紧。最近事太多，咱们也有挺久没碰面了吧。
[name="星熊"]  喏，是不是又没吃早饭？我买了早茶，你喜欢的炒粉，吃一点再去睡吧。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#5",focus=2)]
[name="诗怀雅"]  哼，多管闲事。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#5",focus=1)]
[name="星熊"]  好，好，就算我多管闲事。你还吃吗？
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#2",focus=2)]
[name="诗怀雅"]  当然吃！拿来！
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#3",focus=2)]
[name="诗怀雅"]  咦，你怎么还买两份？这么多，怎么吃得完。
[Character(name="char_136_hsguma_ns_1#3",name2="char_308_swire_1#3",focus=1)]
[name="星熊"]  啊......是两份？可能是习惯了，顺手就买了。
[Character(name="char_136_hsguma_ns_1#3",name2="char_308_swire_1#1",focus=2)]
[name="诗怀雅"]  ......
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#5",focus=2)]
[name="诗怀雅"]  三菌禽肉丝，沙鲜酱，多加了粉根。......哼，也就那家伙才喜欢这个味儿。
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#3",focus=2)]
[name="诗怀雅"]  这家粉选得不怎么样，味太淡，料不足，勉勉强强吧。下次记得要近卫局楼下转角第二家，外面挂了个蓝色招牌的，那家更好。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#3",focus=1)]
[name="星熊"]  行了，知道了，下回再给你带。先凑合吃点，唉，别急，慢点吃。
[Character(name="char_136_hsguma_ns_1#5",name2="char_308_swire_1#3",focus=2)]
[name="诗怀雅"]  （哈欠）
[name="诗怀雅"]  对了，你今天要去哪？反正我都醒了，要逛街可以算我一个。
[name="诗怀雅"]  我要去把舒尔洛夫斯基的那条首饰给买下来，新品，JOKER系列，上个礼拜刚出的。
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#3",focus=1)]
[name="星熊"]  哦，就是老陈早就看中的那条？
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#2",focus=2)]
[name="诗怀雅"]  没错，就是那个，这方面她眼光倒是还行，对衣服首饰比我会挑。
[Character(name="char_136_hsguma_ns_1",name2="char_308_swire_1#2",focus=1)]
[name="星熊"]

... (全文22538字符)
```

### level_act15d5_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
漫无边际的荒野上，一名红发沃尔珀男性正蹲在地上聚精会神地看着什么。
在他身后不远处有一辆车，一名白发鲁珀男性和一名黑发菲林正在检查车辆。
三人看起来是同行者，而他们的车似乎出了故障。
[Dialog]
[Character(name="char_349_chiave#4",fadetime=1,block=true)]
[delay(time=1)]
[name="贾维"]  喂，奥斯塔，快过来。
[Dialog]
[Character(name="char_349_chiave#4", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  干什么？
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[name="贾维"]  你来看这些虫子。
[name="贾维"]  它们排成一排走得好有规律啊。
[name="贾维"]  而且它们的队伍拉得还挺长的，让我看看它们打算去哪里。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  ......你看起来精神了不少。
[Character(name="char_349_chiave#4", name2="char_346_aosta", focus=1)]
[name="贾维"]  没错，我现在感觉我好多了！
[Character(name="char_349_chiave#4", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  但是，我不太相信你对自己身体的判断。
[Character(name="char_349_chiave#3", name2="char_346_aosta", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="贾维"]  你是我老妈吗！
[Character(name="char_349_chiave#3", name2="char_346_aosta#5", focus=2)]
[name="奥斯塔"]  你半小时前还咳血了。
[Character(name="char_349_chiave#4", name2="char_346_aosta#5", focus=1)]
[name="贾维"]  哈哈，但是我现在没有。
[Character(name="char_349_chiave", name2="char_346_aosta#5", focus=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="贾维"]  啊，糟了，光顾着跟你说话，虫子爬走了。
[Character(name="char_349_chiave", name2="char_346_aosta#2", focus=2)]
[name="奥斯塔"]  算了，我去继续修车了。
[Character(name="char_349_chiave", name2="char_346_aosta#2", focus=1)]
[name="贾维"]  哦，车子什么问题你们查出来没有啊，要不要我来帮忙？
[Character(name="char_349_chiave", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  管道出了一些故障，发动机发动不起来了。
[name="奥斯塔"]  我和布洛卡应付得来，你别到处乱跑就好。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[name="贾维"]  就算你让我到处乱跑，这边什么都没有，我也跑不到哪儿去啊。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$sportscarstart", volume=0.6)]
[delay(time=0.4)]
随着一阵轰鸣声，引擎终于重新发动了起来。
[Character(name="char_356_broca", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  呼......布洛卡，去把贾维叫回来吧。
[Character(name="char_356_broca", name2="char_346_aosta", focus=1)]
[name="布洛卡"]  好。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Dialog]
[Character(fadetime=0.6)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_349_chiave#4")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="贾维"]  喂，布洛卡，来比赛谁尿得比较远啊！
[Character(name="char_349_chiave#4", name2="char_356_broca#2", focus=2)]
[name="布洛卡"]  ......我现在尿不出来。
[Character(name="char_356_broca", name2="char_346_aosta#5", focus=2)]
[name="奥斯塔"]  别在这种时候正经回答他，布洛卡。
[Character(name="char_349_chiave#4")]
[name="贾维"]  真是可惜，现在可是适合尿尿的天气！
[Character(name="char_349_chiave#4", name2="char_346_aosta#2", focus=2)]
[name="奥斯塔"]  我觉得除了极寒的地方，大概也没有不适合尿......解手的天气。
[Character(name="char_349_chiave#4", name2="char_346_aosta#2", focus=1)]
[name="贾维"]  这你就不懂了，奥斯塔，这种事讲究一个感觉！
[Character(name="char_349_chiave#2", name2="char_346_aosta#2", focus=1)]
[name="贾维"]  啊，完美的弧线——*叙拉古常用语*！
[Character(name="char_349_chiave#2", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  怎么了？
[Character(name="char_349_chiave#4", name2="char_346_aosta", focus=1)]
[name="贾维"]  忽然刮来一阵大风把我完美的弧线吹到我的鞋上了！啧，真倒霉。
[Character(name="char_349_chiave#4", name2="char_346_aosta#2", focus=2)]
[name="奥斯塔"]  ......别闹了，该出发了，如果我们不能在日落前找到一个聚集地，今天就要在荒野上睡觉了。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[name="贾维"]  荒野不好吗？
[name="贾维"]  这么说起来，我还没有露营过呢！我们今天来露营吧！
[Character(name="char_349_chiave", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  荒野上很危险，而且从根本上来说，这辆偷来的车上并没有露营装备，我们只能睡在车上。
[name="奥斯塔"]  还有，燃料也是一个问题。
[Character(name="char_349_chiave#3", name2="char_346_aosta", focus=1)]
[name="贾维"]  切，真是不上道的车主。
[Character(name="char_349_chiave#3", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  我觉得一般城里的车主也不会在车上准备露营的东西，更不会准备额外的燃料。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[name="贾维"]  但是准备一下又没有坏处，谁知道自己的车哪天会不会被人借走开去露营呢！
[Character(name="char_349_chiave", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  你会吗？
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[name="贾维"]  嗯......不会。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  那就闭嘴准备出发了。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[name="贾维"]  哦。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_356_broca#3", name2="char_346_aosta", focus=1)]
[name="布洛卡"]  要出发了吗？
[Character(name="char_356_broca#3", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  嗯。我来开吧。
[Character(name="char_349_chiave", name2="char_346_aosta", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="贾维"]  什么，该我了吧？
[Character(name="char_349_chiave", name2="char_346_aosta", focus=2)]
[name="奥斯塔"]  你好好休息。
[Character(name="char_349_chiave#3", name2="char_346_aosta", focus=1)]
[name="贾维"]  奥斯塔，我最近发现你越来越像老妈了。
[Character(name="char_349_chiave#3", name2="char_346_aosta#2", focus=2)]
[name="奥斯塔"]  ......
[Character(name="char_349_chiave", name2="char_346_aosta#3", focus=1)]
[name="贾维"]  喂，布洛卡，你有没有这么觉得？
[Character(name="char_349_chiave", name2="char_356_broca#3", 

... (全文34490字符)
```

### level_act15d5_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Character(name="avg_npc_151#3",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  你今天就要出发了吗？
[name="？？？"]  教母才刚把这柄杖交给你，城堡里的东西还没理清呢，真的有必要这么急？
[Character(name="avg_npc_151#3", name2="char_338_iris#2", focus=2)]
[name="？？？"]  时间就要到了，不论如何，我必须按时把东西送去。
[name="？？？"]  别忘了，我们恪守约定，从不失信。
[Character(name="avg_npc_151#3", name2="char_338_iris#2", focus=1)]
[name="？？？"]  我没说这个。我只是觉得太仓促了。
[name="？？？"]  你完全可以先做些简单点的，比如挑个好孩子招待到城堡里来，或者让那些小伙子小姑娘做个美梦什么的。
[name="？？？"]  总比上来就去找一个十多年前的姑娘要强。我们就知道个名字，爱丽丝你又还没经验......
[Character(name="avg_npc_151#3", name2="char_338_iris", focus=2)]
[name="？？？"]  我确实经验不足。
[name="？？？"]  但我的那么多位前辈，可没有一个因为艰难就放弃履约。
[Character(name="avg_npc_151#3", name2="char_338_iris", focus=1)]
[name="？？？"]  哈......行吧，如果你坚持的话，我拦不住你。
[name="？？？"]  那这个铁疙瘩，喏，你拿好。
[Character(name="avg_npc_151#3", name2="char_338_iris#3", focus=2)]
[name="？？？"]  这是，收音机？
[Character(name="avg_npc_151#3", name2="char_338_iris#3", focus=1)]
[name="？？？"]  淘汰款。现在估计也就勉强在小范围里收收电波吧。
[Character(name="avg_npc_151#3", name2="avg_npc_150", focus=2)]
[name="？？？"]  你这样戳，小心把它给戳散了。
[Character(name="char_338_iris", name2="avg_npc_150", focus=2)]
[name="？？？"]  来，这个给你。是路上用得着的东西，我把资料也一起放进去了。
[Character(name="char_338_iris", name2="avg_npc_150", focus=1)]
[name="？？？"]  唔，谢谢。
[Character(name="avg_npc_151#5", name2="avg_npc_150", focus=1)]
[name="？？？"]  我才没那么不小心！
[name="？？？"]  我可是原样保管的，让别人拿着我才不放心呢，千万别在路上碰坏了！
[Character(name="avg_npc_151", name2="char_338_iris", focus=2)]
[name="？？？"]  你想多了，这绝不可能！
[Character(name="avg_npc_151#4", name2="char_338_iris", focus=1)]
[name="？？？"]  那可说不准。
[Character(name="avg_npc_151#4", name2="char_338_iris#3", focus=2)]
[name="？？？"]  什么......！
[Character(name="char_338_iris#3", name2="avg_npc_150#2", focus=2)]
[name="？？？"]  好啦，别闹了。没人怀疑你的能力，我们都很清楚。
[name="？？？"]  毕竟是你第一次出门，大家会担心也是正常的。
[Character(name="avg_npc_151#4", name2="avg_npc_150#2", focus=1)]
[name="？？？"]  哼哼。
[Character(name="char_338_iris", name2="avg_npc_150", focus=2)]
[name="？？？"]  在外面要注意安全，对陌生人要更警惕一些。载具都准备好了，记得走一段路就要好好维护零件，在进荒野之前千万要注意......
[name="？？？"]  哎，我说太多了。不管怎么样，优先保护好自己。
[Character(name="char_338_iris")]
[name="？？？"]  我知道......我明白的。不用担心，虽然可能很难，但这不算什么。
[name="？？？"]  我一定得要完成这个约定才行。我们已经太久没有在外面活动过了。
[name="？？？"]  孩子们因为信任所以将他们珍惜的东西教给我们保管，我们就一定也要如约归还，不能让这信任落空。
[name="？？？"]  这样一来，就算他们长大了，已经不再相信了，我也会向他们证明。
[name="？？？"]  我会证明——
[name="？？？"]  童话永存。
[Character(name="avg_npc_150")]
[name="？？？"]  是吗，那祝你一切顺利了。
[name="？？？"]  期待你的归来。爱丽丝。
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_338_iris",fadetime=1,block=true)]
[delay(time=1)]
[name="爱丽丝"]  （唔，终于到了。）
[name="爱丽丝"]  （按照记录，当时应该是在这个地点招待的孩子。）
[name="爱丽丝"]  （托内尔村。那孩子的名字是叫......玛佩尔。好，没问题。）
[name="爱丽丝"]  （但是这......这是村子吗？）
[Dialog]
[Character]
[Character(name="avg_npc_001",fadetime=1,block=true)]
[delay(time=1)]
[name="工人"]  嗳，小心，小小姐。
[name="工人"]  别向里走了，会弄脏你的鞋。这么好的鞋，弄脏了多可惜，我们可赔不起！
[Character(name="char_338_iris", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  ......谢谢你的提醒。
[Character(name="char_338_iris", name2="avg_npc_001", focus=2)]
[name="工人"]  这有什么。
[name="工人"]  小小姐，你一看就是好人家的小姐，没有随从跟着你吗？你做什么到这种地方来？
[Character(name="char_338_iris", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  我不用随从。我只是来找一个人。
[name="爱丽丝"]  况且，这里可是维多利亚。维多利亚人在我们自己的土地上能出什么事？
[Character(name="char_338_iris", name2="avg_npc_001", focus=2)]
[name="工人"]  哈！说得好！说得好，小小姐，我们的人在自己的家里当然最安全！
[name="工人"]  不过，还是多注意点吧，你还太小了。唉，城里最近有些不太平，小心行事没有坏处。
[Character(name="char_338_iris", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  城里......？
[name="爱丽丝"]  唔，算了。城里的事与我无关。
[name="爱丽丝"]  我已经回答你了。现在该你答我的问题了。
[Character(name="char_338_iris", name2="avg_npc_001", focus=2)]
[name="工人"]  你要问什么？
[Character(name="char_338_iris", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  我是来这里找人的，但是......
[name="爱丽丝"]  这里不应该是一个村庄吗？怎么看不到其他人？
[Character(name="char_338_iris", name2="avg_npc_001", focus=2)]
[name="工人"]  村庄？
[name="工人"]  你自己看看，小小姐，这哪里看起来像是村庄了？
[name="工人"]  之前倒是有几个村子就在这附近，但现在也走了。贵族老爷要了这块地，今春就要动工，要建工厂哩！
[Character(name="char_338_iris", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  ......工厂......
[Character(name="char_338_iris", name2="avg_npc_001", focus=2)]
[name="工人"]  看这个，看这个铁皮，还有这大家伙！气派吧，嗡嗡响！
[Character(name="char_338_iris#3", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  很、很酷。
[name="爱丽丝"]  但是工厂......为什么选这里，怎么不建在移动地块上？
[Character(name="char_338_iris#3", name2="avg_npc_001", focus=2)]
[name="工人"]  贵族老爷爱建在哪儿就建哪儿，哪轮得着我们问这个。
[Character(name="char_338_iris", name2="avg_npc_001", focus=1)]
[name="爱丽丝"]  ......
[name="爱丽丝"]  能告诉我之前在这里的那些村子迁去哪儿了吗？
[Character(name="char_338_iris", name2="avg_npc_001", focus=2)]
[name="工人"]  啊？那谁知道啊......
[name="工人"]  反正他们搬也搬不了太远。这一片还算好的，离城市的轨道也近，再往荒地里走一段，就真的只有些没处可去的流民才会去了！
[Character(name="char_338_iris")]
[name="爱丽丝"]  唔......
[name="爱丽丝"]  我知道了。谢谢你。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_338_iris")]
[name="爱丽丝"]  （......还算在预料之中。）
[name="爱丽丝"]  （已经过了快二十年，当年那个孩子所在的村子搬迁了也不奇怪......）
[name="爱丽丝"]  （看来只能在周围一点点找了。至少村子的名字，还有当年那个孩子的名字都还在记录里，实在不行，就进城想办法查一查。）
[Character(name="char_338_iris")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="爱丽丝"]  （哼，这么点小问题，才不可能拦得住我！）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_village",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_338_iris",fadetime=1,block=true)

... (全文30052字符)
```

### level_act15d5_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
我们的姐妹，席德佳。今日，我们将为你送行。
愿光芒铺陈你的前路，愿虔诚与信念永伴你身。
兰登修道院的钟声将穿过漫长......呃？什么？
咳，兰登修道院的钟声将穿过漫长的岁月，将这数百年来的......葡萄酒！？
喂，怎么还剩下葡萄酒？哪来......呃，瞒着老头子偷偷带来的？嘘！嘘！
总而言之愿兰登百年的荣光与你同在！席德佳！快来帮忙！帮忙把酒桶撬开！
嘿嘿，送别的话果然还是少不了这个吧？在老头子回来之前，干杯！
......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[PlaySound(key="$doorknockquite", volume=0.6)]
[Character(name="char_332_archet",fadetime=1,block=true)]
[delay(time=1)]
[name="席德佳"]  啊......我睡着了？
[Dialog]
[Character]
[PlaySound(key="$doorknockquite", volume=0.6)]
[Character(name="char_332_archet#3")]
[name="席德佳"]  有人在敲门......已经这个点了！？
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_325_bison_1",fadetime=1,block=true)]
[delay(time=1)]
[name="拜松"]  早安，席德佳修士。
[Character(name="char_325_bison_1", name2="char_332_archet#4", focus=2)]
[name="席德佳"]  ......早安，或者说午安，拜松先生，久违地躺在床上，我似乎有些懈怠了。
[Character(name="char_325_bison_1", name2="char_332_archet#4", focus=1)]
[name="拜松"]  长途劳累，辛苦您了。我是来向您确认今天的行程的，没有打扰到您休息吧？
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  没有的事，也辛苦你们了。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  从拉特兰......那个遥远的国家来到龙门，不是一场轻松的旅途吧。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  是啊。
[name="席德佳"]  这是我第一次离开拉特兰这么远......原来长途旅行，不止是欣赏风景那么简单。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  哈哈，就算是经验老道的信使，也会选择各种各样的办法排解情绪......
[Character(name="char_325_bison_1", name2="char_332_archet#3", focus=2)]
[name="席德佳"]  信使们也很不容易呢。
[Character(name="char_325_bison_1", name2="char_332_archet#3", focus=1)]
[name="拜松"]  那席德佳小姐，请问昨晚的住宿还满意吗？
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  嗯。距离市中心很近，价格也很便宜，你的眼光很不错。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  其实费用这方面，您不用担心的。峯驰物流会报销您在龙门期间的出行费用。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  不，作为兰登修道院的一员，我并不愿在财富上仰仗他人，请原谅。
[name="席德佳"]  更何况，我正是为了解决修道院的各种难题才远走他乡，总不能过分奢求别人的地主之谊，自己享乐吧。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  是这样......真是令人钦佩的精神。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  只是必修课罢了。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  和欧厄尔先生的会面安排在明天晚上，那请问您今天有什么打算吗？
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  唔......在附近稍微逛逛吧。这还是我第一次来大炎。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  这样的话，需要安排导游或是随行人员吗？
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  啊，不。我想自己随便看看。只是满足自己的好奇心而已，不好麻烦各位。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  如果是这样的话......我也就不打扰您的雅兴了。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  感谢理解。
[Character(name="char_325_bison_1", name2="char_332_archet#3", focus=2)]
[name="席德佳"]  ......冒昧地问一下，欧厄尔先生，是您的父亲，是吧？
[Character(name="char_325_bison_1", name2="char_332_archet#3", focus=1)]
[name="拜松"]  嗯？啊，是的，怎么了吗？
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  不，是我失礼了。只是拜松先生在工作的时候，完全把欧厄尔先生当做上司看待......
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  啊，如果我总是依赖着老爹这层关系的话，那还怎么越过他这道高墙呢？
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  ......哈哈，拜松先生原来也是个很有野心的人嘛。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=1)]
[name="拜松"]  哪里，要不是和席德佳修士聊得来，我也不会和客户说这种话题喔。
[name="拜松"]  那么，不打扰您了......
[name="拜松"]  不过如果您有空的话，我想听听拉特兰的故事。就像您对龙门的好奇心一样，我对那里......也有着各种想象。
[Character(name="char_325_bison_1", name2="char_332_archet#5", focus=2)]
[name="席德佳"]  没问题。
[Character(name="char_325_bison_1")]
[name="拜松"]  好，祝您今天玩得愉快。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_332_archet")]
[name="席德佳"]  ......龙门吗。
[name="席德佳"]  虽然没有什么旅游经费......随便逛逛吧。
[name="席德佳"]  毕竟“机遇和信仰，都在集市与钟声里”。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_lungmen_m",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_032", name2="avg_npc_033", focus=2)]
[name="龙门男性"]  你爹太顽固啦！这里可是龙门哎！
[Character(name="avg_npc_032", name2="avg_npc_033", focus=1)]
[name="龙门女性"]  可这手艺，是我们老家那边代代传下来的......
[Character(name="avg_npc_032", name2="avg_npc_033", focus=2)]
[name="龙门男性"]  这都什么年代了，手工怎么挣钱嘛。
[Character(name="avg_npc_032", name2="avg_npc_033", focus=1)]
[name="龙门女性"]  ......也对。那是得说服说服我爹去。
[Character(name="char_332_archet")]
[name="席德佳"]  ......
[Character(name="avg_npc_032", name2="avg_npc_033", focus=2)]
[name="龙门男性"]  还有几号排到我们？
[Character(name="avg_npc_032", name2="avg_npc_033", focus=1)]
[name="龙门女性"]  21号，快了，马上就到我们了。这家甜品店怎么这么火啊......
[Character(name="char_332_archet#4")]
[name="席德佳"]  ......我是31号啊。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_332_archet#3",fadetime=1,block=true)]
[delay(time=1)]
[name="席德佳"]  好甜......
[name="席德佳"]  唔？
[Character(name="char_383_snsant_1")]
[name="雪雉"]  啊......？
[Character(name="char_383_snsant_1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="雪雉"]  欸......您、您是不是拉

... (全文32321字符)
```

### level_act15d5_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
2:42 P.M.  天气/多云     
雷姆必拓边陲，天灾预警区域
[Dialog]
[delay(time=1)]
[PlaySound(key="$drift", volume=0.6)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=15, randomness=45, fadeout=true, block=false)]
[PlaySound(key="$drift", volume=0.6)]
[name="莱恩哈特"]  安全带系好没？
[Dialog]
[name="断崖"]  你慢......
[PlaySound(key="$drift", volume=0.6)]
[name="莱恩哈特"]  你这不是系好了嘛，走你！
[name="断崖"]  你不考虑后座上的仪器也至少考虑一下后座上的乘客！
[Dialog]
[Character(fadetime=0.6,block=true)]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[PlaySound(key="$drift", volume=0.6)]
[Character(name="char_373_lionhd#5",fadetime=1,block=true)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱恩哈特"]  喔！引擎声不错，不愧是紧急任务的配给，这个功率真是没说的！
[Character(name="char_373_lionhd#5",name2="char_294_ayer",focus=2)]
[name="断崖"]  要是给你折腾坏了怕就一年全白干了，还有你注意点能耗。
[Character(name="char_373_lionhd",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  这次预估最短可能20个小时后飓风就会成形，要是没能赶在天灾抵达之前撤离，咱们连人带车全得让砂土跟活性源石尘给活埋了。
[Character(name="char_373_lionhd#2",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  而且咱不是有带储罐嘛，这里还有两名术师呢，不用担心能耗问题。对吧，后座的小术师？
[Character(name="char_373_lionhd#2",name2="char_253_greyy",focus=2)]
[name="格雷伊"]  嗯......不过要是我也有驾驶许可就好了。如果我能自己骑沙地车赶过去的话会更快更方便吧？
[Character(name="char_294_ayer",name2="char_253_greyy",focus=1)]
[name="断崖"]  那可不行。
[Character(name="char_294_ayer",name2="char_253_greyy#4",focus=2)]
[name="格雷伊"]  咦？
[Character(name="char_373_lionhd",name2="char_253_greyy#4",focus=1)]
[name="莱恩哈特"]  对哦，你应该还没参加过这类救援任务。
[name="莱恩哈特"]  但凡远离了移动城市去跑外勤，就总会有些说不清的麻烦找上门的，到头来还是不会让你一个人行动啦，总是有帮手的好。
[name="莱恩哈特"]  “在天灾预警区域内展开的行动都应当有天灾信使随行以便应对各种突发状况。”
[name="莱恩哈特"]  何况这次收到的求援信号嘛，是雷姆必拓地方城镇的加密制式。呼......心情复杂啊。
[Character(name="char_373_lionhd",name2="char_253_greyy",focus=2)]
[name="格雷伊"]  因为是同胞发出的信号......吗？
[Character(name="char_373_lionhd#4",name2="char_253_greyy",focus=1)]
[name="莱恩哈特"]  那倒不是。
[Character(name="char_373_lionhd#6",name2="char_253_greyy",focus=1)]
[name="莱恩哈特"]  也不对，说不定是。雷姆必拓嘛......哼哼......我想想怎么和你说——
[Character(name="char_373_lionhd#6",name2="char_294_ayer",focus=2)]
[name="断崖"]  别想入神了，前面有个沟。
[Dialog]
[Character]
[CameraShake(duration=1.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[Character(name="char_253_greyy#4")]
[name="格雷伊"]  呜哇！？
[Character(name="char_373_lionhd#2",name2="char_253_greyy#4",focus=1)]
[name="莱恩哈特"]  呜哦，小心别咬到舌头。不好意思时间要紧，没法照顾到各位乘客的体验啦。
[Character(name="char_373_lionhd#2",name2="char_294_ayer",focus=2)]
[name="断崖"]  那你当初倒是也反对一下这个任务......
[Character(name="char_294_ayer",name2="char_253_greyy#7",focus=2)]
[name="格雷伊"]  对、对不起！都怪我坚持要......
[Character(name="char_294_ayer",name2="char_253_greyy#7",focus=1)]
[name="断崖"]  唉......不怪你。要怪也是怪某位当时第一个跳出来说有自己跟着去就没问题的天灾信使。
[Character(name="char_373_lionhd#6",name2="char_294_ayer",focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱恩哈特"]  我不去也会有别人去的呀！
[Character(name="char_373_lionhd",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  前面有个坡，小心了！
[Character(name="char_294_ayer",name2="char_253_greyy",focus=-1)]
[CameraShake(duration=1.5, xstrength=10, ystrength=12, vibrato=20, randomness=70, fadeout=true, block=false)]
[Character(name="char_253_greyy#4")]
[PlaySound(key="$bodyfalldown2", volume=0.6)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="格雷伊"]  呃！
[Character(name="char_294_ayer")]
[name="断崖"]  ！
[Dialog]
[PlaySound(key="$bodyfalldown3", volume=0.6)]
[Character(name="char_294_ayer")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character]
[Character(name="char_253_greyy#4",fadetime=0.5,block=true)]
[delay(time=0.5)]
[Character(name="char_294_ayer",name2="char_253_greyy#6",focus=2)]
[name="格雷伊"]  啊......那个，谢谢你！
[Dialog]
[Character(name="char_373_lionhd#2",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  我倒是没想过你这武器继上次罗德岛给你加装了信号增幅器后，现在还能拓展出搀扶人的业务啊。
[Character(name="char_373_lionhd#2",name2="char_294_ayer",focus=2)]
[name="断崖"]  如果有必要的话甚至还能缠上绳子把敌人捆起来再打个死结。
[Character(name="char_373_lionhd#3",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  你认真的？
[Character(name="char_373_lionhd#3",name2="char_294_ayer",focus=2)]
[name="断崖"]  想试试？
[Character(name="char_373_lionhd#5",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  算了吧，你那宝贝漏电，到时候再给我整出个仰望天空的发型。你不如研究一下怎么用它表演剥毛豆，好跟人推荐你的喜好。
[Character(name="char_373_lionhd",name2="char_253_greyy",focus=1)]
[name="莱恩哈特"]  说正事。格雷伊，麻烦你看下你旁边那个座位上的箱子上的仪表指针。
[Character(name="char_373_lionhd",name2="char_253_greyy",focus=2)]
[name="格雷伊"]  嗯！现在还在绿色的区域，很接近浅黄色区域，读数是......呃，好多行刻度，该看哪行......
[Character(name="char_373_lionhd#2",name2="char_253_greyy",focus=1)]
[name="莱恩哈特"]  啊，那个不看也没关系，反正我们都闯进这片地带啦。目前也不像有天灾云要成形的样子，前方路况也不错，只要......
[Character(name="char_373_lionhd#2",name2="char_294_ayer",focus=2)]
[name="断崖"]  你打住。这种任务最忌讳做不吉利的预言。
[Character(name="char_373_lionhd#6",name2="char_294_ayer",focus=1)]
[name="莱恩哈特"]  哎呀我都来当天灾信使了还搞什么吉不吉利、预不预言的。
[name="莱恩哈特"]  天灾信使自己就比什么都不吉利。
[characteraction(name="middle", type="jump", xpos=20, power=60, times=1, fadetime=0.6, block=false)]
[Character(name="char_253_greyy#2")]
[name="格雷伊"]  凭什么呀！
[delay(time=0.5)]
[Character(name="char_253_greyy#4")]
[delay(time=0.2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_253_greyy#6")]
[name="格雷伊"]  呃，不好意思，我是说，天灾信使难道不是通知人们将有危险到来的好人......吗？
[Dialog]
[Character]
[

... (全文22891字符)
```

### level_act15d5_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing2", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing3", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing6", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="char_010_chen_1#2")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="陈"]  ——停下！
[Character(name="char_010_chen_1")]
[name="陈"]  到此为止。别再逃了，警察很快就会追到这里，已经太迟了。
[Dialog]
[Character]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_094",fadetime=1,block=true)]
[delay(time=1)]
[name="感染者"]  所以，你也是他们派来的追兵？说什么罗德岛的任务，什么有医生愿意治感染者也全是骗人的，是不是？
[name="感染者"]  老汤姆警告过我们，别相信那些外来的人。哈，我没听他的，我觉得你够义气，和那些有几个钱就斜眼看人的蠢货不一样......
[name="感染者"]  结果就是这样。我才是那个蠢货！
[Character(name="avg_npc_094", name2="char_010_chen_1#5", focus=2)]
[name="陈"]  ......随你怎么想。不管你相不相信，我都要说，我和外面的那些警察没关系。
[Character(name="avg_npc_094", name2="char_010_chen_1#5", focus=1)]
[name="感染者"]  那你就放我离开这里！
[Character(name="avg_npc_094", name2="char_010_chen_1", focus=2)]
[name="陈"]  抱歉，这我做不到。
[name="陈"]  你在去警局的路上突然发难，打伤了两名看守又连夜逃出城，这种情况下，我不能就这么放你走。
[name="陈"]  现在有三支小队在搜捕你，我只是恰好先他们一步。只要踏出这里，你就会被其他人发现。
[Character(name="avg_npc_094", name2="char_010_chen_1#4", focus=2)]
[name="陈"]  那么多人里，只有我知道你没做过他们控告里写的那些事。
[Character(name="avg_npc_094", name2="char_010_chen_1#4", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="感染者"]  ——我当然没有！
[name="感染者"]  那帮混蛋要抓我，就因为我和那个死在街头的外国佬多说了一句话！就这一句话，他们就控告我杀了人，可不可笑啊？
[name="感染者"]  “现场残留有法术痕迹，经推断或为感染者作案”......我呸！我要真有那个本事，他们还有命在？我有什么本事啊？我连把火都放不出！
[Character(name="avg_npc_094", name2="char_010_chen_1", focus=2)]
[name="陈"]  我知道......
[name="陈"]  在光天化日下杀掉一个武装过的雇佣兵，你没这个能耐。这是我还站在这里和你说话的唯一理由。
[name="陈"]  我信你没杀人。但你袭警伤人，拒捕逃窜，这些罪名都是逃不掉的。
[Character(name="avg_npc_094", name2="char_010_chen_1#2", focus=2)]
[name="陈"]  别再抵抗了，这对你没有好处。哥伦比亚比我见过的很多地方都强许多，我看过法院的审判，你们有陪审团，还有民众可以旁听。
[Character(name="avg_npc_094", name2="char_010_chen_1#5", focus=2)]
[name="陈"]  你有可以为自己辩白的场所。你可以把一切告诉所有人。
[Character(name="avg_npc_094", name2="char_010_chen_1#6", focus=2)]
[name="陈"]  尽管有限，但这里的感染者至少有公正......
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[name="陈"]  阿米娅，听说哥伦比亚是个法制十分健全的地方，那里有法官，有关押感染者的监狱，我想去亲眼看一看。
[Dialog]
[Character(name="char_002_amiya_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="阿米娅"]  当然可以。陈长官想去哪里都可以，不如说，我也更希望陈长官能够多去各种地方看一看呢。
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]  啊......是不是不该叫长官了？
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]  陈小姐。哎？不需要这么尊敬？可是......好，好的，那，陈？
[Character(name="char_002_amiya_1#5")]
[name="阿米娅"]  不行，总觉得有点不好意思......
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  咳咳，言归正传。我对哥伦比亚并没有太多了解，在法制和刑事这方面，陈小姐也一定比我要知道得多，所以对这些，我就不多说了。
[Character(name="char_002_amiya_1")]
[name="阿米娅"]  只是，我却很清楚一件事。
[name="阿米娅"]  人与人之间的相互轻贱与敌视，可以发生在任何地点，任何场合。
[name="阿米娅"]  它可以发生在健康的人和感染者之间，也可以发生在富有的人和贫穷的人之间，甚至是一些被人为划分出的界限......
[name="阿米娅"]  总有人会将同胞割裂，分出高低，分出贵贱。
[name="阿米娅"]  请不要急着否认，陈小姐。我听说过哥伦比亚有很多感染者，他们能去拓荒，能赚到钱，有一些甚至能得到公民身份......这生活听起来很有希望。
[name="阿米娅"]  但是，陈小姐，好不好是需要亲自去看，去判断的。乌萨斯的土地是直白的残酷，而许多地方，只是将这份残酷遮掩在了干净的餐布下。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]  我从来没有忘记过，在指挥塔的那天，陈小姐说过的话。
[name="阿米娅"]  公平地对待所有人，公平地审判所有人......那很美好，也会很难。
[name="阿米娅"]  因为从来没人走过那条路，所以就连方向也没有，只能靠陈小姐，靠我们自己，一步一步去踏出一条路来。
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"]  ......我有些担心陈小姐。
[name="阿米娅"]  我很怕你会失望。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_094", name2="char_010_chen_1#6", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="感染者"]  什么狗屁公正？！你这是在做梦！
[name="感染者"]  谁会听我辩白？难道有哪一个被押上法庭的“罪犯”，没有为自己痛哭流涕，没有说自己是清白无辜的吗？！
[name="感染者"]  但他们把你捉到那一圈木头栏杆里，就像捉只羽兽关进笼子，然后掐着脖子把你的肚子剖开，给别人看里头是不是生着一副黑心肠！
[name="感染者"]  你知道那些陪审老爷里有多少人会花钱请人来演讲，就在街上说“染病的穷光蛋在占领城市，在掏空我们的钱袋”？！
[Character(name="avg_npc_094", name2="char_010_chen_1#6", focus=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="感染者"]  你知道什么，你才来多久，你什么都不知道！
[Character(name="avg_npc_094", name2="char_010_chen_1#6", focus=2)]
[name="陈"]  我......
[Character(name="avg_npc_094", name2="

... (全文17387字符)
```

### level_act15d5_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_117_myrrh#2",fadetime=1,block=true)]
[delay(time=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="末药"]  这次真是太感谢宴小姐，还有豆苗小姐了，愿意陪我出来找草药。
[name="末药"]  如果只有我一个人的话，肯定不会这么顺利......
[Character(name="char_117_myrrh#2",name2="char_337_utage_story_1#5",focus=2)]
[name="宴"]  没什么，我也难得接这样的外勤任务，还挺新鲜的。
[name="宴"]  别叫得这么生疏啦，叫我宴就好。女孩子结伴一起外出应该高高兴兴，亲亲密密的。
[Character(name="char_117_myrrh#2",name2="char_337_utage_story_1",focus=2)]
[name="宴"]  我们不已经是朋友了吗。
[Character(name="char_117_myrrh",name2="char_337_utage_story_1",focus=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=70, fadeout=true, block=false)]
[name="末药"]  啊，是、是这样吗？！朋友......可是我......
[name="末药"]  我......我一点也不懂时尚，也不太会聊天......真的可以和宴小姐做朋友吗？
[Character(name="char_117_myrrh",name2="char_337_utage_story_1",focus=2)]
[name="宴"]  说什么呢，有什么可以不可以的？只要在我通讯录上，能叫出来一起逛街的，就都是朋友。
[name="宴"]  看，我也把末药加进去了哟。
[Character(name="char_117_myrrh#2",name2="char_337_utage_story_1",focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=70, fadeout=true, block=false)]
[name="末药"]  好厉害！宴小姐......宴认识好多人啊！
[name="末药"]  咦，这里的分组是？
[Character(name="char_117_myrrh#2",name2="char_337_utage_story_1",focus=2)]
[name="宴"]  啊，那是“午休时间美甲”组，算是我通讯录里人数最多的分组了吧？
[Character(name="char_117_myrrh",name2="char_337_utage_story_1",focus=1)]
[name="末药"]  呃......
[name="末药"]  这个呢？
[Character(name="char_117_myrrh",name2="char_337_utage_story_1",focus=2)]
[name="宴"]  这是“团购优惠券分享”组。
[Character(name="char_117_myrrh",name2="char_337_utage_story_1",focus=1)]
[name="末药"]  那，这个......
[Character(name="char_117_myrrh",name2="char_337_utage_story_1#5",focus=2)]
[name="宴"]  “不参加活动但愿意来付钱”组！哈哈，这里面的可都是需要好好珍惜的好朋友。
[Character(name="char_117_myrrh#4",name2="char_337_utage_story_1#5",focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="末药"]  ......
[Character(name="char_117_myrrh#6")]
[name="末药"]  （如果被加在这个分组里......我可能......会哭......）
[name="末药"]  （......应该不会吧？）
[Dialog]
[Character(name="char_452_bstalk")]
[name="？？？"]  哦，听起来很不错嘛，这个组里的好朋友也介绍给我认识一下吧！
[Dialog]
[Character(name="char_117_myrrh#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="末药"]  啊！豆苗小姐，你回来了！
[Dialog]
[Character(name="char_452_bstalk#4",fadetime=1,block=true)]
[delay(time=1)]
[name="豆苗"]  久等了~
[Character(name="char_117_myrrh#2",name2="char_452_bstalk",focus=2)]
[name="豆苗"]  前头的路稍微有点难走，多费了点时间。
[Character(name="char_337_utage_story_1",name2="char_452_bstalk#4",focus=2)]
[name="豆苗"]  顺便一问，宴你把我和末药分在哪里？不是那个好朋友组吧？
[Character(name="char_337_utage_story_1",name2="char_452_bstalk#4",focus=1)]
[name="宴"]  放心，你就是想进也进不去。
[name="宴"]  你是“下次一定换我请客”，她在“医疗部”里。
[Character(name="char_337_utage_story_1",name2="char_452_bstalk#2",focus=2)]
[name="豆苗"]  哈？等下，你这什么意思？明明我请客的次数也不少吧！
[Character(name="char_337_utage_story_1",name2="char_452_bstalk#3",focus=2)]
[name="豆苗"]  而且，为什么只有末药的分组这么朴素啊？
[Character(name="char_117_myrrh#2",name2="char_452_bstalk#3",focus=1)]
[name="末药"]  啊哈哈......我觉得挺好的......
[Character(name="char_337_utage_story_1#4",name2="char_452_bstalk",focus=1)]
[name="宴"]  人家替我治病呢，多少也要尊重点吧。
[Character(name="char_337_utage_story_1#6",name2="char_452_bstalk",focus=1)]
[name="宴"]  （小声）况且谁敢随便得罪医生啊。我又不傻。
[Character(name="char_337_utage_story_1#5",name2="char_452_bstalk",focus=1)]
[name="宴"]  哎呀别在意这种小事。你刚刚不是探路去了吗，怎么样，这周围还有没有我们这次要找的药草？
[Character(name="char_337_utage_story_1",name2="char_452_bstalk",focus=1)]
[name="宴"]  我看这次也已经采集了不少了，要是没有的话，差不多就能收工了吧？
[Character(name="char_337_utage_story_1",name2="char_452_bstalk#2",focus=2)]
[name="豆苗"]  哼，我正要说这事！分组的账之后再和你算......
[Character(name="char_337_utage_story_1",name2="char_452_bstalk",focus=2)]
[name="豆苗"]  嗯咳。
[name="豆苗"]  先从结论上来说——我确实有点收获。
[name="豆苗"]  刚刚我让阿盘它们分头去找，发现从这儿再往北边去一点的地方，确实有一片我们还没去过的绿地。
[Character(name="char_337_utage_story_1#2",name2="char_452_bstalk",focus=1)]
[name="宴"]  阿盘就是你养的那些小宠物？还挺有本事嘛。
[Character(name="char_337_utage_story_1#2",name2="char_452_bstalk#4",focus=2)]
[name="豆苗"]  那当然！嘿嘿，这么点小事根本难不倒我的小家伙们。
[Character(name="char_117_myrrh",name2="char_452_bstalk#4",focus=1)]
[name="末药"]  这里往北......从湿度、光照和地形上来说，确实很适合药草生长！
[name="末药"]  太好了，那我们快点过去吧！
[Character(name="char_117_myrrh",name2="char_452_bstalk#2",focus=2)]
[name="豆苗"]  哎，等等，听我说完！
[Character(name="char_452_bstalk")]
[name="豆苗"]  嗯......配给的区域图，我找找......有了！你们看这个。
[name="豆苗"]  我们现在的位置在我标了红点的这里，那片绿地大概在这个位置，就这里。
[Character(name="char_117_myrrh",name2="char_452_bstalk",focus=1)]
[name="末药"]  啊，这里是......
[Character(name="char_337_utage_story_1#2",name2="char_452_bstalk",focus=1)]
[name="宴"]  唔？我看看。
[Character(name="char_337_utage_story_1#4",name2="char_452_bstalk",focus=1)]
[name="宴"]  啊哦，原来我们离舰后已经走了这么远？前面这块，上面写的是......伊什么......啧，这字也太小了，伊比利亚？
[Character(name="char_337_utage_story_1#4",name2="char_452_bstalk#3",focus=2)]
[name="豆苗"]  伊比利亚啊......
[name="豆苗"]  我听说那边的移动城市会变色，驶过的土地都寸草不生，不知道是不是真的。
[Character(name="char_337_utage_story_1#2",name2="char_452_bstalk#3",focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="宴"]  欸，骗人吧？
[Character(name="char_117_myrrh",name2="char_337_utage_story_1#2",focus=1)]
[name="末药"]  如果是源石能源技术问题带来的污染，对土地造成一定影响还是有可能的。
[name="末药"]  但是寸草不生......是不是有点太夸张了？
[Character(name="char_117_myrrh",name2="char_452_bstalk",focus=2)]
[name="豆苗"]  这才哪到哪儿啊，这根本不算夸张的。还有人说伊比利亚的城市都会变形呢！
[name="豆苗"]  城市里的地块都能飞起来重组到一起，变成没手没脚，会把所有东西都吞掉的巨大怪物！
[Character(name="char_117_myrrh#4",name2="char_452_bstalk",focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, ra

... (全文22702字符)
```


## 统计

- 总字符数：182381
- 对话行数：1856


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
