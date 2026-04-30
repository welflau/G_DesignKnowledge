# 明日方舟 · 活动剧情 · act13d0（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act13d0」完整剧情脚本（7个文件，1826行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act13d0
- 脚本文件数：7

### level_act13d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 中秋 史尔特尔
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
7:10 A.M.  天气/晴
卡兹戴尔远郊
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_county_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_350_surtr_1#3",fadetime=1,blo=true)]
[delay(time=2)]
[name="史尔特尔"]  任务目的地是这儿？
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_219_meteo_1",fadetime=1,blo=true)]
[delay(time=2)]
[name="陨星"]  按照图像指示看来，应该就是这里，移动村庄——贝罗尼村。
[name="陨星"]  比起移动村庄，不如说整个村子就是一个大型矿车。
[name="陨星"]  依靠源石驱动自带的钻井进行采掘，达成自给自足的同时，多余资源出售给附近的其他城市也能获得营收。
[name="陨星"]  如果发现了大型遗迹更是能向周围的大型移动城市寻求开采的赞助费。
[Character(name="char_350_surtr_1#6",name2="char_219_meteo_1",focus=1)]
[name="史尔特尔"]  就算你这么说，这村子也太破了吧。
[name="史尔特尔"]  遍地的灰尘，栅栏也破破烂烂。明明有人来往，但是却不愿意翻修翻修。
[name="史尔特尔"]  看起来也并不是什么很有趣的地方。
[Character(name="char_350_surtr_1#6",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  泰拉的大部分地方都不有趣，但是那些居住在无趣地方的人也有他们自己的生活。
[Character]
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[name="瘦弱的小孩"]  等一下，还给我！
[name="顽皮的小孩"]  干嘛！不是你说好的这些雪糕要大家分着吃的吗！
[name="瘦弱的小孩"]  别跑！都还没到家你都要把它捏化了！
[name="瘦弱的小孩"]  白痴，快给我！
[name="顽皮的小孩"]  那不行，我比你跑得更快，得让我来把这些带回去给老爸！
[name="瘦弱的小孩"]  等等我啊！！
[PlaySound(key="$rungeneral", volume=0.9)]
[Character]
[Dialog]
[delay(time=1)]
[Character(name="char_350_surtr_1#6",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  在这样糟糕环境中努力生存着的人们不少，但是这并不意味着他们不幸福。
[Character(name="char_350_surtr_1#6",name2="char_219_meteo_1",focus=1)]
[name="史尔特尔"]  为了一份普通的雪糕跑来跑去，不顾周围的人吵吵嚷嚷，一直到长大成人也都是这样。
[name="史尔特尔"]  这样也幸福？
[Character(name="char_350_surtr_1#6",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  ......你是不是生气了。
[Character(name="char_350_surtr_1#3",name2="char_219_meteo_1",focus=1)]
[name="史尔特尔"]  我怎么会因为被这些小孩子不顾别人胡乱跑过扬起灰尘发脾气。
[Character(name="char_350_surtr_1#3",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  （这可不就是生气了吗。）
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_006",fadetime=1,blo=true)]
[delay(time=2)]
[name="村长"]  不好意思不好意思，两位就是罗德岛特派过来的干员吗。
[name="村长"]  让两位久等了。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  啊是的，您好，请问您就是本地的对接人员吗。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=1)]
[name="村长"]  啊啊是的，敝人就是现在贝罗尼村的村长。由我来给大家带路，来，别在这里站着，咱们往里走吧，这边。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=2)]
[name="陨星"]   麻烦您了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
任务出发前
罗德岛指挥室
[Character(name="char_003_kalts_1",fadetime=1,blo=true)]
[delay(time=1)]
[name="凯尔希"]   地处卡兹戴尔边界的贝罗尼村是典型的矿区村庄，几个月前因为开采导致了塌方，矿场完全封闭了起来。
[name="凯尔希"]   塌方不仅破坏了矿场，还封住了村子的移动路线，贝罗尼村一直以来的通商通道也被阻拦。
[name="凯尔希"]   村子近几个月以来一直在向临近的移动城市求助，不过并没有愿意去帮他们解决情况的城市出现。
[name="凯尔希"]   这次希望陨星你能去现场进行初步探查，确定当地受困情况。
[name="凯尔希"]   将第一波数据带回来后，我们就可以展开救助计划。
[Character(name="char_219_meteo_1")]
[name="陨星"]  了解，听起来并不是特别困难的任务。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]   村子的问题看起来并没有牵扯到天灾和矿石病，但是也要小心行事。
[Character(name="char_219_meteo_1")]
[name="陨星"]  收到，不过......
[Character(name="char_350_surtr_1")]
[name="史尔特尔"]  ......
[Character(name="char_219_meteo_1")]
[name="陨星"]  史尔特尔也要一起？这次任务没有这么困难吧。
[Character(name="char_350_surtr_1")]
[name="史尔特尔"]  这次任务地点有我想去确认的东西。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  史尔特尔因为一些个人需求申请了任务的同行，经过确认我们通过了此次申请。
[Character(name="char_350_surtr_1")]
[name="史尔特尔"]  我不会成为累赘，不用在意我就行。
[Character(name="char_219_meteo_1")]
[name="陨星"]  ......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_county_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=1)]
[name="村长"]  村子不大，麻烦两位先在这里等一等，我进去先拿一些工具。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  啊，基本的勘探工具我们都携带好了。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=1)]
[name="村长"]  村子边缘的矿区入口现在被我们用特殊的锁定设备封锁了。
[name="村长"]  如果不是特殊解锁工具的话是没办法打开的，倒不是我自夸，咱们村子在采掘方面还是很有经验的。
[Character(name="avg_npc_006",name2="char_350_surtr_1",focus=2)]
[name="史尔特尔"]  可是不也困在这里了。
[Character(name="avg_npc_006",name2="char_350_surtr_1",focus=1)]
[name="村长"]  哈哈哈确实是这样。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  啊啊抱歉她不是有心的。喂这也太没礼貌了吧。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=1)]
[name="村长"]  也是惭愧，村子虽然在采掘方面有经验，但是确实没有预料到如此大规模的塌方事件。
[name="村长"]  钻井部分陷在塌方区域里面，为了安全着想，村子也不敢安排人员接近。
[name="村长"]  即使这次能得到罗德岛的帮助，以后我们也得多钻研钻研应对手段。
[name="村长"]  两位先休息休息，稍等我去准备准备。
[Character(name="avg_npc_006",name2="char_219_meteo_1",focus=2)]
[name="陨星"]  好的，您先去忙吧。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=2)]
[Character(name="char_219_meteo_1")]
[name="陨星"]  ......
[Character(name="char_219_meteo_1",name2="char_350_surtr_1",focus=2)]
[name="史尔特尔"]  ......
[Character(name="char_219_meteo_1",name2="char_350_surtr_1",focus=1)]
[name="陨星"]  所以，你对别人也太不客气了吧。
[Character(name="char_219_meteo_1",name2="char_350_surtr_1#6",focus=2)]
[name="史尔特尔"]  只不过说说事实而已。
[Character(name="char_219_meteo_1")]
[name="陨星"]  唔......唔......
[name="陨星"]  （好尴尬啊。）
[name="陨星"]  （虽然早就听说史尔特尔很难相处了，但是没想到根本找不到话说。）
[Character(name="char_350_surtr_1")]
[name="史尔特尔"]  ......（记录）
[Character(name="char_219_meteo_1",name2="char_350_surtr_1",focus=1)]
[name="陨星"]  你是在记录村子的情况吗。
[Character(name="char_219_meteo_1",name2="char_350_surtr_1",focus=2)]
[name="史尔特尔"]  并不是。
[Character(name="char_219_meteo_1",name2="char_350_surtr_1",focus=1)]
[name="陨星"]  那是......
[Character(name="char_219_meteo_1",name2="char_350_surtr_1",focus=2)]
[name="史尔特尔"]  ......
[Chara

... (全文18304字符)
```

### level_act13d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 异域同族
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Delay(time=1)]
[name="芳汀"]  武器可靠性证明？
[name="芳汀"]  那是什么？
[name="芳汀"]  需要我本人带着武器，去工坊接受检查，然后拿工匠的签名回来？
[name="芳汀"]  使用自带武器，竟然还要走这种流程啊......啧，听起来就好麻烦。
[name="芳汀"]  老师就不能通融一下，直接帮我签掉不就好了。
[name="芳汀"]  不可以？这是罗德岛的规矩？
[name="芳汀"]  真没意思。好吧，好吧，如果您坚持的话，我就自己去一趟吧。
[name="芳汀"]  初来乍到，我也不想这么快就惹那位凯尔希医生生气。
[Dialog]
[Delay(time=0.7)]
[name="芳汀"]  那就一会见了，老师。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.9)]
[Delay(time=2)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Delay(time=1)]
罗德岛舰船，第三维修工坊，早晨
[PlaySound(key="$doorknockquite")]
[Delay(time=1)]
[Dialog]
[PlaySound(key="$d_gen_dooropen",volume=0.6)]
[Delay(time=0.5)]
[Character(name="char_271_arene_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="芳汀"]  有没有人在？
[Character]
[Dialog]
[Delay(time=1)]
[Character(name="char_211_adnach_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]  您好，现在工坊不营业，五位工匠都去参加维修竞技比赛了。
[name="？？？"]  有需要的话请下午三点再来。
[Character(name="char_271_arene_1#6")]
[name="芳汀"]  维修竞技？那是什么怪比赛。
[name="芳汀"]  要先把武器弄坏再比怎么维修吗，还是看看谁把刀柄擦得更亮？
[Character(name="char_211_adnach_1")]
[name="？？？"]  很遗憾，只是普通的针对战场上半损毁武器的修缮和改良比赛。
[Character(name="char_211_adnach_1#3")]
[name="？？？"]  但如果真的能将武器擦到足够亮，让这变成一种攻击手段，或许也不是不能取得优胜。
[Character(name="char_211_adnach_1#2")]
[name="？？？"]  ......嗯？好像是个不错的主意。下次我试试。
[Character(name="char_271_arene_1#4")]
[name="芳汀"]  哈，怪人。随便吧。
[Character(name="char_271_arene_1")]
[name="芳汀"]  我可不想为了这么点事还要再跑一趟，没有工匠在，但这里不是还有你吗。
[name="芳汀"]  反正也只是例行公事的检查，别那么较真。怎么样，这位朋友，帮我简单看一下，然后填个证明就行。
[Dialog]
[Delay(time=0.7)]
[PlaySound(key="$g_card_10cardsrelease")]
[Delay(time=0.7)]
[Character(name="char_271_arene_1",name2="char_211_adnach_1#3",focus=2)]
[name="？？？"]  武器可靠性证明？
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  没错。
[Character(name="char_271_arene_1",name2="char_211_adnach_1#6",focus=2)]
[name="？？？"]  武器可靠性证明需要两位工匠同时进行检查后签字确认。
[name="？？？"]  我算是还在实习的助手，就算签上自己的名字也不管用，帮不了你这个忙。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  需要两个人签字，这里有你我两个人，这不是正好吗。
[name="芳汀"]  我自己的法杖，自己最清楚，不会有什么问题的。只要不出事，就没人会知道，没人知道，就是没有问题，不是吗。
[Character(name="char_271_arene_1",name2="char_211_adnach_1#3",focus=2)]
[name="？？？"]  啊这个想法有意思。
[Character(name="char_271_arene_1",name2="char_211_adnach_1#2",focus=2)]
[name="？？？"]  但还是别小看这里的其他人会比较好哦，特别是比较严肃的那几位。
[name="？？？"]  万一出了事，就是重大事故了，别说我们，连不在场的工匠都要一起受罚。
[Character(name="char_271_arene_1#7",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  啧，死板，麻烦。
[Character(name="char_271_arene_1#7",name2="char_211_adnach_1#2",focus=2)]
[name="？？？"]  但是有效。有些人就是想不起来维护武器。
[name="？？？"]  总比在战场上换弦要来得轻松。
[Character(name="char_271_arene_1#7",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  哪会有那种傻子？
[Dialog]
[Character]
[Delay(time=0.5)]
[Character(name="char_271_arene_1#4")]
[name="芳汀"]  算了。既然如此，那就——
[Character(name="char_271_arene_1")]
[name="芳汀"]  只请你帮忙看下武器。
[name="芳汀"]  这还是可以的吧。总不能真的白跑一趟，那也有点让人不爽。
[Character(name="char_211_adnach_1")]
[name="？？？"]  啊......也好。稍等。
[name="？？？"]  等我拧好这最后一颗螺丝——好了。
[Dialog]
[Character]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=1)]
[Character(name="char_271_arene_1#4",name2="char_211_adnach_1",focus=2)]
[name="？？？"]  久等了。
[Character(name="char_271_arene_1",name2="char_211_adnach_1#2",focus=2)]
[name="？？？"]  ......嗯，看你的表情，看来你还是在盘算什么，并没有打算彻底放弃呢。
[Character(name="char_271_arene_1#2",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  这是说什么，我可听不明白。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  来，给你。我的法杖。
[Character(name="char_271_arene_1",name2="char_211_adnach_1#6",focus=2)]
[name="？？？"]  哎.....算了。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=2)]
[name="？？？"]  好吧，那我来检查一下。
[name="？？？"]  （小声）只要小心一些，别出事故，应该就没关系了吧......
[Character(name="char_271_arene_1#2",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  就拜托你啦。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=2)]
[name="？？？"]  武器的检查会需要一些时间，要麻烦你在这里稍微等一下。
[name="？？？"]  参观的话可以随意，但工坊里的东西最好还是不要随便碰，总有些工匠师傅喜欢做些比较危险的东西......
[Character(name="char_271_arene_1",name2="char_211_adnach_1#2",focus=2)]
[name="？？？"]  你明白吧？那种做到一半的半成品只会更危险。
[name="？？？"]  而且，这里还有不少混杂着源石成分的矿石......就算你是感染者，也最好小心一些。
[Character(name="char_271_arene_1#4",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  不劳担心。我还没有那么莽撞。
[Character(name="char_271_arene_1#6")]
[name="芳汀"]  ......等等。
[Dialog]
[Delay(time=1)]
[Character(name="char_271_arene_1")]
[name="芳汀"]  怪了，我有提过自己是感染者这件事吗？
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=2)]
[name="？？？"]  没有。但要看出来不难。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  说说，怎么看出来的？很明显吗？
[Character(name="char_271_arene_1",name2="char_211_adnach_1#6",focus=2)]
[name="？？？"]  嗯......解释起来有点难，我也说不清。
[name="？？？"]  就靠多多观察吧，从大家的神情、动作，还有行为逻辑上，都可以看出很多东西。
[Character(name="char_271_arene_1#4",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  听起来像是在糊弄人。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=2)]
[name="？？？"]  是真的啦。
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_211_adnach_1")]
[name="？？？"]  只有这根法杖要检查吗？如果还有其他的，我也可以帮你看一下。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  没有了。
[name="芳汀"]  很遗憾，我没有守护铳需要检查。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=2)]
[name="？？？"]  真巧，我也没有。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  ......
[Character(name="char_271_arene_1#6",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  你这人真奇怪，有点意思。
[Character(name="char_271_arene_1",name2="char_211_adnach_1#2",focus=2)]
[name="？？？"]  嗯......谢谢夸奖？
[Character(name="char_271_arene_1#2",name2="char_211_adnach_1",focus=1)]
[name="芳汀"]  没夸你。
[Character(name="char_271_arene_1",name2="char_211_adnach_1",focu

... (全文26262字符)
```

### level_act13d0_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 中秋 极境
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
我们一生都在飞翔，有谁想过，自己最后会停在哪儿吗？
带着湿意的家乡的风，口中总有消散不去咸盐的滋味。
刺疼人的烈日，难忍的高温，还有繁华留在皮肤上的印记和空旷城市中凝滞的气流。
我体验过，这些我都体验过。
[Dialog]
[delay(time=1)]
我想或许有一天，我终究会回到那个地方。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
10:10 A.M.  天气/晴
罗德岛舰船，第二舱室，干员休息区
[Character(name="char_385_finlpp")]
[name="清流"]  那么，这次联系大家的事情就拜托极境先生了！
[name="清流"]  要采购的食材我已经提前和后勤部门说好了，到时菜品我会和食铁兽姐一起想想办法。
[name="清流"]  家常菜我们应该都能做，但复杂点的就要找人帮忙了......
[name="清流"]  啊，对了，惊蛰姐也说可以帮忙写请柬，她字写得可好看了，动作利落又帅气，看得我都心动想去学书法了。
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1", focus=2)]
[name="极境"]  哎，准备得很周到嘛，真没想到那个惊蛰小姐竟然也会帮忙。
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1#2", focus=2)]
[name="极境"]  要联络的就是名单上这些外勤任务中的炎国和龙门干员对吧？放心交给我，绝对一个都漏不掉！
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1#2", focus=1)]
[name="清流"]  有极境先生帮忙，我当然不担心啦！
[name="清流"]  能在罗德岛遇到这么多老乡，还挺让人意外的。嘿嘿，我好喜欢大家聚在一起时的气氛，人多一点才热闹嘛，多好。
[name="清流"]  不知道在外面出任务的大家能不能回得来，希望可以赶上......唔，我也知道估计会很难啦，但是万一呢！
[name="清流"]  啊，当然也很欢迎大家一起参加！极境先生要来吗，可以带上朋友一起，这种活动如果人少就没意思了！
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1", focus=2)]
[name="极境"]  真的？那太好了，我一定多拉点人一起去，这么难得的机会那可不能错过。
[name="极境"]  是越热闹越好对吧？这个我们擅长！
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1", focus=1)]
[name="清流"]  啊哈哈......当然欢迎，不过，也不要闹得太过火哦，之后会被凯尔希医生骂的。
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1#3", focus=2)]
[name="极境"]  放心放心，我有分寸的！
[Dialog]
[Character]
[name="？？？"]  不想被骂，奉劝你还是别邀请这家伙比较好。
[name="？？？"]  如果惹祸也是天赋，那他的确天赋异禀。
[Character(name="char_385_finlpp#2")]
[name="清流"]  啊，棘刺先生，早上好！
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Dialog]
[Character]
[Character(name="char_293_thorns_n_1",fadetime=1,block=true)]
[delay(time=1)]
[name="棘刺"]  早。
[Character(name="char_401_elysm_na_1", name2="char_293_thorns_n_1", focus=1)]
[name="极境"]  喂，老兄，这么说就不对了，论惹祸明明你也没比我好多少吧？
[name="极境"]  上次把接弦区的船板弄坏的人可是你欸，为什么事后可露希尔小姐反而拉着我教训了那么久啊！
[Character(name="char_401_elysm_na_1", name2="char_293_thorns_n_1#4", focus=2)]
[name="棘刺"]  我怎么知道。
[name="棘刺"]  难道不是因为你把她的小机器抱去甲板上玩，结果掉下去摔碎了吗？
[Character(name="char_401_elysm_na_1#6", name2="char_293_thorns_n_1#4", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="极境"]  .....呃。
[Character(name="char_401_elysm_na_1#10", name2="char_293_thorns_n_1#4", focus=1)]
[name="极境"]  那、那该怪谁啊！还不是安哲拉她突然用墨弹一通乱射，我一时没反应过来才会失手啊！
[Character(name="char_385_finlpp", name2="char_401_elysm_na_1#10", focus=1)]
[name="清流"]  咦，等一下，安哲拉小姐怎么会在甲板上射击？她看起来不像是会做这种事情的人呀......
[Character(name="char_385_finlpp", name2="char_293_thorns_n_1", focus=2)]
[name="棘刺"]  试试手。我刚给她的弩加了点新东西，仿拉特兰铳的射击效果。
[Character(name="char_401_elysm_na_1#6", name2="char_293_thorns_n_1", focus=1)]
[name="极境"]  结果还不是你害的！怪不得那个拉特兰铳迷突然就兴奋了！
[Dialog]
[Character]
[Character(name="char_405_absin_4",fadetime=1,block=true)]
[delay(time=1)]
[name="苦艾"]  ......
[Character(name="char_293_thorns_n_1")]
[name="棘刺"]  嗯？
[Character(name="char_401_elysm_na_1", name2="char_293_thorns_n_1", focus=1)]
[name="极境"]  怎么了......咦，谁在那边？
[Character(name="char_405_absin_4#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="苦艾"]  ！
[Character(name="char_385_finlpp#2")]
[name="清流"]  啊！是小艾！
[Character(name="char_385_finlpp#5")]
[name="清流"]  你躲在那里干什么呢，快过来这边！
[Character(name="char_385_finlpp")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_385_finlpp", name2="char_405_absin_4#2", focus=1)]
[name="清流"]  啊，难道你是怕生？放心，这两位先生一点都不可怕的，而且这不是还有我在嘛！
[Character(name="char_385_finlpp", name2="char_405_absin_4#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="苦艾"]  那个，清流姐，别拉，我自己走。
[Character(name="char_405_absin_4")]
[name="苦艾"]  ......抱歉，打扰你们了吗？我只是想找棘刺先生商量点事情，如果不方便的话，过一会也可以......
[Character(name="char_405_absin_4", name2="char_401_elysm_na_1#5", focus=2)]
[name="极境"]  完全不会哦。没什么不方便，大家都是同事有什么打扰不打扰的，太见外了。
[Character(name="char_401_elysm_na_1", name2="char_293_thorns_n_1", focus=1)]
[name="极境"]  兄弟，找你的。
[name="极境"]  看你成天板着脸，我还以为没有女孩子敢和你说话呢，真让人欣慰。
[Character(name="char_401_elysm_na_1", name2="char_293_thorns_n_1#4", focus=2)]
[name="棘刺"]  ......啰嗦。
[Character(name="char_405_absin_4", name2="char_293_thorns_n_1", focus=2)]
[name="棘刺"]  你找我有事？
[Character(name="char_405_absin_4", name2="char_293_thorns_n_1", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="苦艾"]  是的。很抱歉，突然来打扰。
[name="苦艾"]  其实是有关武器的保养，有些想向棘刺先生请教的地方......
[Character(name="char_405_absin_4", name2="char_401_elysm_na_1#6", focus=2)]
[name="极境"]  咦，这家伙的那套武器保养这么有名的吗？
[Character(name="char_401_elysm_na_1#3", name2="char_293_thorns_n_1", focus=1)]
[name="极境"]  这么说起来，我的发信器也差不多该整修一下了。
[name="极境"]  哎，你们说，我下次任务回来给可露希尔小姐带点礼物，她会不会原谅我，帮我给发信器升个级？
[Character(name="char_401_elysm_na_1#3", name2="char_293_thorns_n_1#6", focus=2)]
[name="棘刺"]  如果你还是带她讨厌的那种蒜味零食，那么肯定不会。
[Character(name="char_405_absin_4", name2="char_293_thorns_n_1", focus=2)]
[name="棘刺"]  你的武器带了吗，让我看看。
[Character(name="char_405_absin_4#3", name2="char_293_thorns_n_1", focus=1)]
[name="苦艾"]  在这里，请看！
[Dialog]
[Character(name="char_405_absin_4#3")]
[delay(time=1)]
[Character(name="char_405_absin_4#3", name2="char_293_thorns_n_1", focus=1)]
[name="苦艾"]  我使用的武器和一般术师使用的施术单元不太一样，里面的一些零件的保养方法比较复杂......啊，请小心一些，这里的扳机有些松动了。
[Character(name="char_405_absin_4#3", name2="char_293_thorns_n_1", focus=2)]
[name="棘刺"]  很老旧。
[Charac

... (全文20684字符)
```

### level_act13d0_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 中秋 泥岩
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
鲍勃，近来可好？
我收到了你的来信，很高兴你能顺利前往哥伦比亚。
我们过得都还行，至少，我们都还活着。
烟鬼还惦记着要扳手腕赢你一次，厨子还记得你的赏金猎人欠他三枚金币。
虽然等到信使抵达哥伦比亚可能有些迟了，不过，我还是得向你道贺一声。
真庆幸你们都能摆脱这些事情，鲍勃，真的。
我还记得你的邀请，非常感谢你还能记得我们这些萨卡兹。
不过——
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$epic_intro", key="$epic_loop", volume=0.4)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_054")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨卡兹战士"]  跑！泥岩！
[Character(name="avg_npc_054")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨卡兹战士"]  跑，到卡兹戴尔去，到能活下去的地方去......！
[Character(name="avg_npc_011#2")]
[name="泥岩"]  不......不，你别说话了，你......
[Character(name="avg_npc_054")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨卡兹战士"]  泥岩——！
[name="萨卡兹战士"]  千万......不要回头！
[Character(name="avg_npc_011#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="泥岩"]  但是......
[Character(name="avg_npc_054")]
[name="萨卡兹战士"]  我.....别管我，跑，跑快点，到卡兹戴尔，只要......到......卡兹戴尔去......
[Dialog]
[PlaySound(key="$fightgeneral", volume=0.4)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="avg_npc_011#2")]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="泥岩"]  烟鬼......！烟......
[name="泥岩"]  ......
[Delay(time=1)]
[Character(name="avg_npc_011#2")]
[name="泥岩"]  我们......我们走，动作快。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.6)]
不过我们的情况并不算好。
在和你们分别之后，我们前往了莱塔尼亚。
我们遭遇了很多事情，说来惭愧，现在我们被称作“泥岩小队”。
[stopmusic(fadetime=4)]
你知道的，我不喜欢抛头露面，但是这些莱塔尼亚的感染者说，他们需要被帮助，需要被拯救。
我没法抛下他们不管，鲍勃。就像你绝不会抛下你的猎人兄弟们一样。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Character(name="avg_npc_067")]
[name="莱塔尼亚感染者"]  为、为什么斥候还是没有回应？
[Character(name="avg_npc_067")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱塔尼亚感染者"]  难道他们也......？
[Character(name="avg_npc_067", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  ......不要惊慌。
[name="萨卡兹战士"]  森林里的雾很大，他们没那么容易找到我们......
[Character(name="avg_npc_067", name2="avg_npc_053", focus=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="莱塔尼亚感染者"]  但是，但是已经过去八天了！
[name="莱塔尼亚感染者"]  我们失去了十二名同伴，我们却不知道到底是谁在追杀我们！
[Character(name="avg_npc_067", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  不要太过责难他们......遭遇这种敌人，会慌乱也是理所当然的。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  泥岩？
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  ......唯一能确定的，他们是术师。
[name="泥岩"]  就算用朋友的眼去看，也无法在迷雾中捕获他们的身影......
[Character(name="avg_npc_067", name2="avg_npc_011#2", focus=1)]
[name="莱塔尼亚感染者"]  但是火球，冰雹和飓风一直没有停歇过，他们一直就在我们身边，就在......啊！
[Character(name="avg_npc_067", name2="avg_npc_011#2", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱塔尼亚感染者"]  也许这连日大雾也是他们的法术，这天气也太反常了......！他们能让火一样的眼睛在天空飞舞，这点事情——
[Character(name="avg_npc_067", name2="avg_npc_011#2", focus=2)]
[name="泥岩"]  冷静点。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  但是，我们太被动了，这是事实。
[name="萨卡兹战士"]  我们甚至不知道是谁，有几个人，在用什么手段监视我们。
[name="萨卡兹战士"]  一旦露出空隙，就会有人遭到袭击。这种诡异的游击战，很少见。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  ......这也是莱塔尼亚法术的一种？我并没有听说过......
[Character(name="avg_npc_067", name2="avg_npc_011#2", focus=1)]
[name="莱塔尼亚感染者"]  我......我不知道......我没听说过这种法术......
[name="莱塔尼亚感染者"]  队长的法术天赋已经非常优秀了......说实在话，如果队长都没有办法，我们这些人......
[Character(name="avg_npc_067", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  ......怎么办？
[name="萨卡兹战士"]  按原计划继续前进的话，离开这片森林之前不知道还要遭到几次袭击——
[name="萨卡兹战士"]  但就算想要还击，我们连对方是谁都不知道，可见度太低，气温在下降。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  ......你带两个同胞确保行动路线，保持在队伍五百米以内，每一分钟通讯一次。
[name="泥岩"]  我亲自殿后。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  也许他们不在“后面”。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  岩石朋友们会保护主要队伍。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  ......可以，但是你要节制使用你的法术。
[name="萨卡兹战士"]  唯独你不能倒下。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  我心里有数......谢谢。
[name="泥岩"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  泥岩？
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  ......答应我一件事，厨子。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=2)]
[name="萨卡兹战士"]  你先说。
[Character(name="avg_npc_011#2", name2="avg_npc_053", focus=1)]
[name="泥岩"]  只要你还能接到主队伍的通讯，就继续带着他们往前走。
[name="泥岩"]  不要管后面发生了什么......都不要回头。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_bl

... (全文28621字符)
```

### level_act13d0_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 中秋 四月
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_365_aprl",fadetime=1,block=true)]
[delay(time=1)]
[name="四月"]  呼，今天的任务出了一身汗。
[name="四月"]  赶紧回宿舍洗个澡吧。
[Character(name="char_365_aprl#2")]
[name="四月"]  咦，那边的是......
[Character(name="avg_npc_002")]
[name="罗德岛信使"]  好了，信和每一份钱都确认完毕。
[Character(name="char_212_ansel_1", name2="avg_npc_002", focus=1)]
[name="安赛尔"]  那就麻烦你了。
[Character(name="char_212_ansel_1", name2="avg_npc_002", focus=2)]
[name="罗德岛信使"]  哈哈，放心吧，你都算是老客户了。老实说，你的家人都要认识我了。
[name="罗德岛信使"]  不过你也有一段时间没有回去了吧？不考虑回去一趟吗？伯父见到我肯定又要让我催你回一趟雷姆必拓了。
[name="罗德岛信使"]  虽然我也是一年都在外面跑的人没有资格说什么，不过多少信可都比不上你亲自回去。
[Character(name="char_212_ansel_1", name2="avg_npc_002", focus=1)]
[name="安赛尔"]  ......我知道，只是这边还有病人需要我。
[name="安赛尔"]  等空闲下来后，我会回去的。
[Character(name="char_212_ansel_1", name2="avg_npc_002", focus=2)]
[name="罗德岛信使"]  好吧，我想你在这方面也是能够把握住的，就不多说什么了。
[name="罗德岛信使"]  好，那我再去确认一下别的信件就差不多出发了。
[name="罗德岛信使"]  特产呢，还是老样子？
[Character(name="char_212_ansel_1", name2="avg_npc_002", focus=1)]
[name="安赛尔"]  嗯，帮我带一盒我家楼下小店里卖的薄荷糖吧。
[Character(name="char_212_ansel_1", name2="avg_npc_002", focus=2)]
[name="罗德岛信使"]  好好。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_212_ansel_1")]
[name="安赛尔"]  大伯，对不起......
[Character(name="char_365_aprl#5")]
[name="四月"]  ......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_365_aprl")]
[name="四月"]  原来罗德岛上也有信使。
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  你是......
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=1)]
[name="四月"]  我是新加入的干员，代号是四月，叫我四月就好。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  你好，四月，我是医疗部的安赛尔。
[name="安赛尔"]  罗德岛上有不少信使哦，而且像刚才那位那样的信使并不是我们的干员，他们是专为罗德岛上的人服务的信使。
[Character(name="char_365_aprl#2", name2="char_212_ansel_1", focus=1)]
[name="四月"]  有什么区别吗？
[Character(name="char_365_aprl#2", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  有的，虽然选择成为我们干员的人之中也有信使存在，啊你认识安洁莉娜小姐吗？
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  认识，那个和我差不多大的信使女孩子吧？
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  嗯，首先，会加入罗德岛的信使通常是因为感染得病，选择用成为干员的方式抵消医疗费用，安洁莉娜小姐就是这样的例子。
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  啊，那我也是。
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  嗯，毕竟针对矿石病的医疗费用不管怎么说都不能算低，舰内有不少各行各业的人也都是因为类似的理由留在这里的。
[Character(name="char_365_aprl#5", name2="char_212_ansel_1", focus=1)]
[name="四月"]  那不就和成为这里的信使差不多了吗？
[Character(name="char_365_aprl#5", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  啊哈哈，这方面果然容易被误解，其实不是的。
[name="安赛尔"]  信使这个职业，因为与人直接接触比较少，而且本身就需要到处跑，因此即使成为感染者也是可以继续的。
[name="安赛尔"]  或者说，大部分人根本不知道给自己送信寄信的是不是感染者......
[name="安赛尔"]  总之，他们是可以继续在自己原本的活动范围内工作的，只要定期来到罗德岛接受治疗就好了。
[Character(name="char_365_aprl#2", name2="char_212_ansel_1", focus=1)]
[name="四月"]  咦，但是这样不就等于在做自己的事吗？
[Character(name="char_365_aprl#2", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  当然，我们对这样的信使干员通常也会发出一些类似长期外勤的任务。
[name="安赛尔"]  而且他们通常也会把罗德岛当成自己的一个驿站，如果自己活动的范围内有我们的干员的亲属或者朋友，那肯定是可以拜托他们寄信的。
[name="安赛尔"]  但是像我这样，需要定期向家里寄信的人，就很难期待他们。
[name="安赛尔"]  虽然实际上罗德岛上目前来自雷姆必拓的信使也很少就是了。
[Character(name="char_365_aprl#5", name2="char_212_ansel_1", focus=1)]
[name="四月"]  这样啊，不过还是感觉没什么约束力......要是在我过去呆的公司，这种事情完全是无法想象的。
[Character(name="char_365_aprl#5", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  哪种事情？
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  就是员工拥有自己的自由啊，我觉得肯定会有那种只来了一次就再也没来过的人吧？
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  你还真敏锐，这种情况确实偶尔会发生，我们当然也会追责，但不管怎么说，不能放着病人不管。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=1)]
[name="四月"]  安赛尔医生你真是好人。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  过奖了，我只是想着能帮一个是一个而已。
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  不过这么说的话，确实罗德岛专属的信使是有必要的。
[name="四月"]  我都没有想过这样的事。
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  咦，四月，你也是雷姆必拓出身吧？
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  嗯，南边的钢铁萝卜城。
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  啊，我有听说过，你们城市每年的矿石产量都名列前茅。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=1)]
[name="四月"]  是啊，这是我们城的骄傲，虽然我没什么感觉就是了。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  我是铁腕城出身的。你在家乡没有什么要联络的亲人吗？
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  没有哦。
[name="四月"]  我的父母在我小的时候就因为矿难去世了，我是被他们供职的公司抚养大的。
[Character(name="char_365_aprl#5", name2="char_212_ansel_1", focus=1)]
[name="四月"]  在成年后我就成为了这家公司的猎人，虽然工资也不算高，不过也还算过得去，直到我感染了矿石病......
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  ......对不起。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=1)]
[name="四月"]  没事啦。
[Character(name="char_365_aprl#6", name2="char_212_ansel_1", focus=2)]
[name="安赛尔"]  不过我记得雷姆必拓的公司对感染者的待遇并不差吧？
[name="安赛尔"]  因为雷姆必拓的矿业很发达，这里的人比起其他国家的人本来接触矿石病的几率就要高不少......
[Character(name="char_365_aprl", name2="char_212_ansel_1", focus=1)]
[name="四月"]  我一开始也是这么想的，但是实际体验下来我才知道我错了。
[name="四月"]  他们表面上说得有各种福利，但其实暗中各种克扣，而且在知道你得了矿石病后，工作机会也会越来越少。
[name="四月"]  像我这样一个人生活的矿石病患者，在那里是活不下去的。
[Character(name="char_365_aprl",

... (全文18736字符)
```

### level_act13d0_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 交错光影
[Dialog]
[Character]
[StopMusic]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Delay(time=1)]
女士们，先生们，欢迎各位今夜到来，下面让我们观赏本剧团的最新剧目！
这盛大的剧目您绝不会在其他地方见到，独占、专属，正是只存在于此的至福享受！
请洗净您的双眼，磨尖您的听觉，享受这个美妙的夜晚......
[Dialog]
[Delay(time=0.5)]
欢迎各位来到猩红剧团——
[Delay(time=0.5)]
[PlaySound(key="$tactfulboost",volume=0.6)]
[Dialog]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Image(image="avg_ac13_1",xScale=1.15, yScale=1.15, y=-60, screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=false)]
[Delay(time=2)]
[ImageTween(yTo=80,duration=6,block=false)]
[name="傀影"]  ......♪
[name="傀影"]  （轻声唱歌）
Answer.
The shadow in the dark.
[Dialog]
[name="傀影"]  是谁。谁在黑夜中唤我。
[name="傀影"]  时候到了，我该准备登台。
Answer.
The shadow in the dark.
The killer on the stage.
[Dialog]
[name="傀影"]  谁在说话。谁在唱歌。
Answer.
Your darkness is asking.
[Dialog]
[name="傀影"]  帷幕拉开，灯光垂落，演员站在中央。
[name="傀影"]  这是什么声音，是谁在期待，是谁在......
[name="傀影"]  ——喝彩。
[Dialog]
[PlaySound(key="$tactfulboost",volume=0.6)]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Delay(time=1)]
[PlaySound(key="$livecrowd",volume=0.6,fadetime=1.5)]
[Delay(time=2)]
But
In the fact who you are.
Who you are.
The shadow in the dark.
[Dialog]
[image]
[Character]
[Background(image="bg_stage",screenadapt="coverall")]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_250_phantom_1",fadetime=1)]
[Delay(time=3)]
[PlaySound(key="$tactfulboost",volume=0.6)]
[Image(image="avg_ac13_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Delay(time=1)]
[name="傀影"]  我是谁？
[name="傀影"]  我是黑夜中的幽灵，幕布后的幻影，舞台上的明星。
[Character(name="char_250_phantom_1#6")]
[name="傀影"]  我是......
[Dialog]
[Delay(time=0.5)]
[StopMusic]
[image]
[PlaySound(key="$tactfulboost",volume=0.6)]
[Character(name="char_250_phantom_1#4")]
[Blocker(a=0.7, r=0, g=0, b=0, block=true)]
[Delay(time=2)]
[Image(image="avg_ac13_2",screenadapt="coverall",fadetime=1)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="演员A"]  我知道你是谁。
[name="演员B"]  我们都知道。
[name="演员C"]  你藏在破屋里，你躲在长桌后，你把自己塞在那些恶魔的言语和漆黑字符下。
[name="演员B"]  你和我们一起唱歌，我们时常练习，你唱得最好。
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Character(name="char_250_phantom_1#4")]
[name="傀影"]  你们是谁？
[name="傀影"]  你们不是这出戏的演员，那么又为什么会出现在这里？
[name="傀影"]  你们......认得我。
[Character]
[Dialog]
[Delay(time=0.5)]
[name="演员A"]  你问我们是谁，你竟已经不认得。
[name="演员A"]  怎么能够忘记？怎么胆敢忘记？魔鬼选中你，教你音乐，教你念词，教你领略这舞台。
[name="演员A"]  你着了魔，追随魔鬼的指引，可在最后却又背弃。你杀了魔鬼，离开这里，现在已将我们都忘记。
[name="演员A"]  你真认为自己能杀掉魔鬼？
[Character(name="char_250_phantom_1")]
[name="傀影"]  不，不是这样，我没有忘记。
[name="傀影"]  我......
[Character(name="char_250_phantom_1#7")]
[name="傀影"]  我已经将所有人都杀死。那些人的做法是错误的。
[name="傀影"]  沉溺是错误的，追随是错误的，觉得美是错误的，我必须要杀掉他们，我必须这样做——
[Character]
[name="演员B"]  所以，你杀死了他们，同时也夺走我们的呼吸。
[name="演员C"]  就在这舞台上，你开始唱歌。
[Character(name="char_250_phantom_1#7")]
[name="傀影"]  ......
[Character(name="char_250_phantom_1#2")]
[name="傀影"]  是的。
[name="傀影"]  你们早已经被我杀死，为什么还会出现在这里？
[Character]
[name="演员B"]  久违了，我们亲爱的兄弟。
[name="演员B"]  我们一起背井离乡，我们一起长大。我们是流淌着不同血的亲人，同吃同住，却走向不同的结局。
[name="演员B"]  我已经很久没同你说过话，自从蜡烛融化，我的血液同烛泪一起滴在舞台上，自那之后，我们就再没有说过话。
[name="演员C"]  与你不同，无缘领略艺术真谛的演员，不过是筛选后的失败品，空有喜爱，却无才华。
[name="演员C"]  而有人扑火，有人选择逃离。
[name="演员B"]  也有人仍停留在过去，在那个夜里。歌声响起，歌声一直未停息。
[name="演员B"]  啊......时间到了。属于过去的幻影不会在这里停留太久，我们不该在这舞台上。
[MusicVolume(volume=0,fadetime=1)]
[Dialog]
[image(fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_250_phantom_1#3")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="傀影"]  等等！别走——
[Character(name="char_250_phantom_1#7")]
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[name="傀影"]  咳——咳、呃，咳咳......
[name="傀影"]  我的......喉咙......
[Character]
[Dialog]
[name="演员A"]  多可悲，午夜的幽灵，分不清自己。失去歌喉，你还剩下什么？
[name="演员A"]  逃离这里，又真的能逃离今夜吗？
[name="演员A"]  你不该出声。你不该唱。
[name="演员A"]  你不该在这舞台上。
[Dialog]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bottlebroken")]
[Blocker(a=0.8, r=0, g=0, b=0,fadetime=0.05,block=true)]
[Blocker(a=0, r=0, g=0, b=0,fadetime=0.05,block=true)]
[PlaySound(key="$bottlebroken",delay=0.4)]
[CameraShake(duration=2, xstrength=5, ystrength=7, vibrato=20, randomness=90, fadeout=false, block=false)]
[PlaySound(key="$bottlebroken",delay=0.5)]
[Blocker(a=0.8, r=0, g=0, b=0,fadetime=0.05,block=true)]
[Blocker(a=0, r=0, g=0, b=0,fadetime=0.05, block=true)]
[PlaySound(key="$icespread")]
[Blocker(a=0.8, r=0, g=0, b=0,fadetime=0.05,block=true)]
[Blocker(a=0, r=0, g=0, b=0,fadetime=0.05, block=true)]
[Delay(time=0.2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Delay(time=1)]
[MusicVolume(volume=0.4,fadetime=1)]
[Delay(time=1)]
Answer.
The shadow in the dark.
Answer.
Who you are.
And what you really desire.
[Dialog]
[Delay(time=1)]
女士们，先生们，帷幕已落下......
希望各位能够有一个美好的夜晚......
[Dialog]
[Delay(time=1)]
[Character(name="char_250_phantom_1#7")]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="傀影"]  ......我是谁？
[name="傀影"]  我、想要......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[StopMusic(fadetime=2)]
[Character]
[Delay(time=3)]
[Background(image="bg_room_2",screenadapt="coverall")]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
08:10 A.M.  天气/阴雨
罗德岛舰船，第二舱室，人事后勤部门
[Dialog]
[Character(name="char_016_medic")]
[Delay(time=0.5)]
[PlaySound(key="$g_card_10cardsrelease")]
[PlaySound(key="$g_card_10cardsrelease",delay=0.3)]
[PlaySound(key="$g_card_10cardsrelease",delay=0.6)]
[Delay(time=1)]
[name="人事干员"] 这一批的干员应该都在这里了，1、2、3......好，没问题。
[name="人事干员"] 嗯？这个是......这个编号怎么是上一批的，是谁整理的时候这么不小心，居然编号都能弄混。
[PlaySound(key="$g_ca

... (全文27778字符)
```

### level_act13d0_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 天空的故事
[Dialog]
[Character]
[StopMusic]
[Blocker(a=1, r=0, g=0, b=0, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_254_Shamare_1",fadetime=1)]
[Delay(time=1)]
[name="巫恋"]你怎么了，小莫提。
[Character(name="avg_npc_131")]
[name="莫提"](萎靡地躺在沙发上。)
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=1)]
[name="巫恋"]没吃饱？
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=2)]
[name="莫提"]......
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=1)]
[name="巫恋"]今天是节日，大家都很开心。
[name="巫恋"]恶灵们也都藏起来了。
[name="巫恋"]在宴会上拿食物的时候，我看到很多人在哭泣。
[name="巫恋"]那些做不了你的食粮吗？
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=2)]
[name="莫提"]......
[Character(name="char_254_Shamare_1")]
[name="巫恋"]可能你也变得越来越挑剔了。
[name="巫恋"]今天早上，博士和我说，会在这里有个宴会。
[name="巫恋"]宴会上会有食物、朋友、以及许多平常见不到的东西——
[Character(name="avg_npc_131")]
[name="莫提"]......
[Character(name="char_254_Shamare_1")]
[name="巫恋"]你在问我，开不开心？
[Dialog]
[Delay(time=1)]
[name="巫恋"]我......不太明白。
[name="巫恋"]这个地方的情感太奇特了。
[name="巫恋"]最近收到的感情很丰富。
[name="巫恋"]有些我也不理解。
[name="巫恋"]就像刚刚看到的那样，一边欢笑，一边喝饮料。
[name="巫恋"]交谈了几句，泪水就止不住往下流。
[name="巫恋"]一边笑一边哭。
[name="巫恋"]喜悦和悲伤混杂在一起，真让人伤脑筋。
[Character(name="avg_npc_131")]
[name="莫提"]......
[Character(name="char_254_Shamare_1")]
[name="巫恋"]嗯，这也是我唯一理解了的事情。
[name="巫恋"]这些情感，不合莫提的口味。
[Dialog]
[Character]
[Delay(time=1)]
[MusicVolume(volume=0,fadetime=0.2)]
[Character(name="avg_npc_131")]
[name="莫提"]！
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[PlaySound(key="$reinforcement",volume=0.9)]
[Dialog]
[Delay(time=1.5)]
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=1)]
[name="巫恋"]又裂开了？
[name="巫恋"]......
[Dialog]
[Delay(time=1)]
[MusicVolume(volume=0.4,fadetime=1)]
[Character(name="char_254_Shamare_1")]
[name="巫恋"]还好，不算太严重。
[name="巫恋"]帮我拿些苹果，我来准备其他材料。
[name="巫恋"]去吧，别把肚子里的东西散出来。
[name="巫恋"]也别拿刀乱划，不然博士会生气的。
[Character(name="avg_npc_131")]
[name="莫提"]（点头）
[Character(name="char_254_Shamare_1")]
[name="巫恋"]快去快回。
[Dialog]
[Character(name="avg_npc_131")]
[Delay(time=1)]
[Character(fadetime=1)]
[PlaySound(key="$runsand")]
[Delay(time=2)]
[Character(name="char_254_Shamare_1")]
[name="巫恋"]......
[PlaySound(key="$g_card_10cardsrelease")]
[Delay(time=1)]
[name="巫恋"]......
[Dialog]
[PlaySound(key="$g_card_10cardsrelease")]
[Delay(time=1)]
[Character(fadetime=0.5)]
[Delay(time=0.7)]
[PlaySound(key="$rungeneral")]
[Character(name2="char_358_lisa_1",fadetime=1,focus=1,block=true)]
[Delay(time=1.5)]
[Character(fadetime=1)]
[Delay(time=0.7)]
[PlaySound(key="$rungeneral")]
[Character(name="char_358_lisa_1",name2="char_empty",fadetime=1,focus=2,block=true)]
[Delay(time=1.5)]
[Character(fadetime=1)]
[Delay(time=1)]
[Character(name="char_254_Shamare_1")]
[name="巫恋"]嗯？
[Dialog]
[Delay(time=1)]
[Character(name2="char_254_Shamare_1",focus=1)]
[delay(time=0.7)]
[Character(name="char_358_lisa_1#3",name2="char_254_Shamare_1",fadetime=0.5 ,focus=1)]
[delay(time=1)]
[CameraShake(duration=0.6, xstrength=2, ystrength=2, vibrato=10, randomness=30, fadeout=true)]
[name="铃兰"]啊，我是不是打扰到你了，巫恋姐姐？
[Character(name="char_358_lisa_1#3",name2="char_254_Shamare_1" ,focus=2)]
[name="巫恋"]有事吗？
[Character(name="char_358_lisa_1#3",name2="char_254_Shamare_1" ,focus=1)]
[name="铃兰"]只，只是看到巫恋姐姐写了半天却没有字，有些好奇......
[Character(name="char_358_lisa_1#3",name2="char_254_Shamare_1" ,focus=2)]
[name="巫恋"]哦。
[Character(name="char_358_lisa_1#3",name2="char_254_Shamare_1" ,focus=1)]
[name="铃兰"]唔......
[name="铃兰"]打扰到姐姐......工作了吗？
[CameraShake(duration=0.6, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[name="铃兰"]对不起！
[Character(name="char_254_Shamare_1")]
[name="巫恋"]......
[Dialog]
[Character(name="char_358_lisa_1",name2="char_254_Shamare_1" ,focus=1)]
[name="铃兰"]嗯，那个，我刚刚吃饱，想在这里看一会书，可以吗？
[Character(name="char_358_lisa_1",name2="char_254_Shamare_1" ,focus=2)]
[name="巫恋"]随便。
[Character(name="char_358_lisa_1#5",name2="char_254_Shamare_1" ,focus=1)]
[name="铃兰"]谢谢巫恋姐姐，嘿嘿。
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_358_lisa_1")]
[name="铃兰"]呼，这里的大沙发应该能让尾巴全垂下来——好了。
[name="铃兰"]啊，舒服~
[Character(name="char_358_lisa_1#5")]
[name="铃兰"]呜~~
[CameraShake(duration=0.6, xstrength=2, ystrength=2, vibrato=10, randomness=5, fadeout=true)]
[Delay(time=1)]
[Character(name="char_254_Shamare_1")]
[name="巫恋"]......
[Character]
[Dialog]
[Delay(time=1)]
[PlaySound(key="$runsand")]
[Character(name="avg_npc_131",fadetime=1)]
[Delay(time=2)]
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=1)]
[name="巫恋"]回来了？
[Dialog]
[Delay(time=1)]
[name="巫恋"]（小声）小莫提，拿一个苹果给铃兰。
[Character(name="char_254_Shamare_1",name2="avg_npc_131",focus=2)]
[name="莫提"](点头。)
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_358_lisa_1",name2="char_empty" ,focus=1)]
[name="铃兰"]哈——
[Dialog]
[Delay(time=1)]
[PlaySound(key="$runsand")]
[Character(name="char_358_lisa_1",name2="avg_npc_131",fadetime=1 ,focus=2)]
[Delay(time=2)]
[Character(name="char_358_lisa_1",name2="avg_npc_131",fadetime=1 ,focus=1)]
[name="铃兰"]唉，莫提？
[name="铃兰"]这是......给我的吗？！
[Character(name="char_254_Shamare_1")]
[name="巫恋"]......
[Character(name="char_358_lisa_1#5")]
[name="铃兰"]谢谢巫恋姐姐！
[name="铃兰"]谢谢莫提！
[Character(name="char_358_lisa_1")]
[name="铃兰"]唔......
[CameraShake(duration=0.6, xstrength=2, ystrength=2, vibrato=10, randomness=5, fadeout=true)]
[name="铃兰"]唔？！
[name="铃兰"]好甜！
[name="铃兰"]唔唔。
[name="铃兰"]甜甜酸酸的，温度也正好，有一点冰凉，但也没凉到会让牙齿疼。
[name="铃兰"]唔唔唔——
[Character(name="char_358_lisa_1#5")]
[name="铃兰"]哈——好开心~
[Character(name="char_358_lisa_1")]
[name="铃兰"]啊，果核要收好，一会找垃圾桶丢掉。
[name="铃兰"]嗯？
[Dialog]
[Delay(time=0.5)]
[Character(name="avg_npc_131")]
[name="莫提"]......
[Character(name="char_358_lisa_1")]
[name="铃兰"]莫提，你的意思是你来丢吗？
[name="铃兰"]好的，拜托你了。
[Character(name="char_358_lisa_1#5")]
[name="铃兰"]谢谢。
[Dialog]
[Delay(time=1)]


... (全文31280字符)
```


## 统计

- 总字符数：171665
- 对话行数：1826


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
