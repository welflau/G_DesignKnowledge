# 明日方舟 · 活动剧情 · act14mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act14mini」完整剧情脚本（6个文件，1616行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act14mini
- 脚本文件数：6

### level_act14mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_light",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
娘，爹又要出远门了吗？这次会走多久？
江上的冰雪快要融了，今年的雨水正好，看起来应该是无旱无涝的一年。
上游新垦的那块地，虽然不大，但种些水稻，应该还是够我们一家吃的。
[Dialog]
[Delay(time=1)]
娘，你能不能劝劝爹？让他别再做“生意”了。我不想要新衣服，也不要什么漂亮首饰，一家人过个安稳日子，比什么都强。
[Dialog]
[Delay(time=1)]
我有些，害怕......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[Subtitle(text="贫一乡来富一乡，青苗荒草一头长。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="芒鞋踏破行千里，山高水阔成一乡。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[charslot]
[Background(image="35_g11_yumendesert",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.6)]
[PlaySound(key="$d_avg_runstop", volume=1,delay=1.5)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_820_1#6$1",posfrom="300,0",posto="0,0",afrom=0,ato=1,duration=1,isblock=true)]
[Delay(time=1)]
[name="慌张的少年"]呼——呼——
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="慌张的少年"]前面......是悬崖......
[Dialog]
[PlaySound(key="$d_avg_vallyrck", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="慌张的少年"]该死，该死！这下是真的跑不掉了......
[charslot(slot="m",name="avg_npc_820_1#6$1",focus="m")]
[name="慌张的少年"]别慌，不能慌......就算打不过，这一路上的陷阱也该够她喝一壶的。
[name="慌张的少年"]等一会逮住她，非得狠狠教训她一顿，居然敢小瞧我......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_787_1#6$1",duration=1)]
[Delay(time=1.5)]
[name="仇白"]终于跑累了？
[charslot(slot="m",name="avg_npc_820_1#5$1",focus="m")]
[name="慌张的少年"]你怎么——
[charslot(slot="m",name="avg_npc_820_1#6$1",focus="m")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="慌张的少年"]别过来！
[charslot(slot="m",name="avg_npc_787_1#1$1",focus="m")]
[name="仇白"]年纪不大，花样倒是不少。教你打猎的人有没有说过，对付野兽的陷阱不能用来对付人？
[charslot(slot="m",name="avg_npc_787_1#11$1",focus="m")]
[name="仇白"]万一让旁人中了陷阱，你就不怕再多一条故意伤人的罪名？
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="慌张的少年"]笑话......故意伤人算什么，我干过的坏事，那叫一个......罄竹难书！
[charslot(slot="m",name="avg_npc_787_1#1$1",focus="m")]
[name="仇白"]那就是说，我在这杀了你，你也算是死有余辜？
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="慌张的少年"]对！
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="慌张的少年"]不......不对！
[charslot(slot="m",name="avg_npc_820_1#4$1",focus="m")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="慌张的少年"]你别过来！
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[Delay(time=1)]
[name="慌张的少年"]看到我怀里的这一袋炸药了吗？你再过来一步，我就拉了引线，就算你武功再高，咱俩也得同归于尽！
[charslot(slot="m",name="avg_npc_787_1#4$1",focus="m")]
[name="仇白"]......
[charslot(slot="m",name="avg_npc_787_1#1$1",focus="m")]
[name="仇白"]好，我就站在这，你老实回答我的问题。
[charslot(slot="m",name="avg_npc_820_1#4$1",focus="m")]
[name="慌张的少年"]别想从我这里套到什么话！
[charslot(slot="m",name="avg_npc_787_1#11$1",focus="m")]
[name="仇白"]你是怎么认识山洞里那伙歹徒的？
[charslot(slot="m",name="avg_npc_820_1#6$1",focus="m")]
[name="慌张的少年"]什么怎么认识的，我就是他们的头儿。
[name="慌张的少年"]我的手下是都被你收拾了，但你别得意，我一定会为他们报仇的！
[charslot(slot="m",name="avg_npc_787_1#6$1",focus="m")]
[name="仇白"]头儿？你才多大年纪？
[charslot(slot="m",name="avg_npc_820_1#6$1",focus="m")]
[name="慌张的少年"]呵，年纪小又怎么了？这方圆十里的村子镇子，你去打听打听，谁不知道我“方小石”的恶名。
[name="慌张的少年"]小爷干过的事，说出来吓死你！
[charslot(slot="m",name="avg_npc_787_1#6$1",focus="m")]
[name="仇白"]荒唐......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.2, fadetime=1)]
[charslot]
[delay(time=1)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.8, fadetime=0)]
[Background(image="bg_caveentrance", screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
半日前
[Dialog]
[charslot(slot="m",name="avg_npc_794_1#1$1",focus="m")]
[name="惊慌的山海众成员"]小石头！小石头！
[Dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=0.6)]
[charslot(slot="m",name="avg_npc_820_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="方小石"]咋了咋了，仇人找上门了？
[charslot(slot="m",name="avg_npc_820_1#8$1",focus="m")]
[name="方小石"]是不是终于要去和别人打架了？这回能不能带上我？
[charslot(slot="m",name="avg_npc_794_1#1$1",focus="m")]
[name="惊慌的山海众成员"]该死的，去玉门的那帮人不知道怎么惹了一个女魔头过来，我们的人差不多全折她手上了！
[name="惊慌的山海众成员"]来不及收拾东西了，赶快逃吧！
[charslot(slot="m",name="avg_npc_820_1#5$1",focus="m")]
[name="方小石"]你说啥，对面只有一个人？
[charslot(slot="m",name="avg_npc_820_1#1$1",focus="m")]
[name="方小石"]你们跟我比画的时候不都还挺厉害的，怎么连人家一个人都打不过......
[charslot(slot="m",name="avg_npc_794_1#1$1",focus="m")]
[name="惊慌的山海众成员"]闭嘴！
[name="惊慌的山海众成员"]少废话，让你管的驮兽呢？！
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="方小石"]那个......卖了。
[charslot(slot="m",name="avg_npc_794_1#1$1",focus="m")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="惊慌的山海众成员"]卖了？！
[charslot(slot="m",name="avg_npc_820_1#11$1",focus="m")]
[name="方小石"]不是你说拿去换点吃的？
[charslot(slot="m",name="avg_npc_794_1#1$1",focus="m")]
[name="惊慌的山海众成员"]你个呆子！我让你骑驮兽去镇上拿我们掠来的珠宝换点东西，你连驮兽一块卖了？！
[charslot(slot="m",name="avg_npc_820_1#1$1",focus="m")]
[name="方小石"]那几袋石头？肉铺的老板又不认那些玩意。
[name="方小石"]他看我们养的那只驮兽还挺壮实，就用好价钱买了

... (全文39816字符)
```

### level_act14mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="35_mini02_wanedtemple",screenadapt="showall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_797_1#1$1",duration=0.7)]
[Delay(time=1.5)]
[name="愤怒的村民"]方小石！你在房梁上干什么？赶紧下来！
[name="愤怒的村民"]在别的地方撒野也就算了，这儿可是“移山庙”啊！
[Dialog]
[charslot]
[name="方小石"]我就不！
[name="方小石"]村子这么大，非要把这破庙迁到我们家的“三亩三”，这不是欺负人是什么？周六，怎么不迁到你家地上去呢？
[Dialog]
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="愤怒的村民"]你个小孩子懂什么，移山庙守的是谋善村上千年的气脉，迁庙的选址都是有讲究的。
[name="愤怒的村民"]全村商量好的事，由不得你胡来！
[Dialog]
[charslot]
[name="方小石"]呸！
[name="方小石"]“三亩三”之前就是块寸草不生的荒碱地，那时候怎么不说它风水好？这么多年，我爹一担水一担肥把地种好了，风水也跟着变了？
[name="方小石"]说白了，不就是看我们家是村里唯一的外姓人好欺负吗？告诉你们，想都别想！
[name="方小石"]我爹是我爹，但小爷可不是好说话的主！
[name="方小石"]你们想靠这破庙保佑丰收？小爷今天偏偏要把这破庙炸了，腾出地方大家好种田！
[Dialog]
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="愤怒的村民"]你别——
[Dialog]
[charslot]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=1)]
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="35_mini01_villagevacancy", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_820_1#2$1")]
[charslot(slot="r",name="avg_npc_787_1#5$1")]
[delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[PlaySound(key="$d_avg_crwddiscuss_outside",loop=true, channel="crwd", volume=0.2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_787_1#5$1",focus="r")]
[name="仇白"]刚回到家就被很多人找上门的，我只见过欠了一屁股债的赌棍。
[charslot(slot="l",name="avg_npc_820_1#2$1",focus="l")]
[name="方小石"]......
[charslot(slot="r",name="avg_npc_787_1#1$1",focus="r")]
[name="仇白"]不过路上你倒是讲了一句实话，村里人确实不欢迎你。
[charslot(slot="l",name="avg_npc_820_1#2$1",focus="l")]
[name="方小石"]都说了别让我回来。
[charslot(slot="r",name="avg_npc_787_1#11$1",focus="r")]
[name="仇白"]可你还是没讲，到底为什么......
[Dialog]
[charslot]
小小的院子站满了人，村民们也不搭话，只是将仇白和方小石围着，好像两人是哪里冒出来的新奇野兽，万万不能让其逃走。
[Dialog]
[musicvolume(volume=0, fadetime=2)]
[SoundVolume(channel="crwd", volume=0, fadetime=2.5)]
[Delay(time=1)]
[name="？？？"]咳、咳......让让......
[name="？？？"]大家伙儿堵在这儿做啥，小石满月的酒席上都没这么热闹......
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_822_1#1$1",duration=1.5,isblock=true)]
[Delay(time=1.5)]
攒动的人群中挤出一个男人，瘦高的个子，脚步蹒跚，喘着粗气。他背着一截木头，脊背弯得就和腰上的弓一样。
[Dialog]
[charslot(slot="m",name="avg_npc_822_1#4$1",focus="m")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_822_1#4$1",afrom=1,ato=0,duration=0.5)]
[Delay(time=1)]
男人看到方小石，先是愣了一愣，很快又把目光撇开，缓缓转过身去。
[charslot]
[charslot(slot="m",name="avg_npc_820_1#2$1",focus="m")]
[name="方小石"]爹......
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="紧张的村民"]猎户......
[name="紧张的村民"]你别忘了......
[charslot(slot="m",name="avg_npc_822_1#2$1",focus="m")]
[name="猎户"]我说过的话我肯定记得。
[charslot(slot="m",name="avg_npc_822_1#1$1",focus="m")]
[name="猎户"]但小石三年没回家了，大家伙儿难道不打算让他先喝口水，吃顿饭？
[Dialog]
[charslot(slot="m",name="avg_npc_822_1#1$1",focus="m")]
[SoundVolume(channel="crwd", volume=0.2, fadetime=1.5)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_822_1#1$1",focus="m")]
[name="猎户"]都先回地里去吧，我们爷俩一定会给村里一个交代。
[name="猎户"]地里的活儿本来就耽搁了，再过几天，春分都过去了......
[Dialog]
[charslot]
[stopSound(channel="crwd", fadetime=2)]
[charslot(slot="l",name="avg_npc_140",focus="all")]
[charslot(slot="r",name="avg_npc_141",focus="all")]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="l",name="avg_npc_140",afrom=1,ato=0,duration=1)]
[charslot(slot="r",name="avg_npc_141",afrom=1,ato=0,duration=1)]
[Delay(time=3)]
[musicvolume(volume=0.4, fadetime=1.5)]
[charslot(slot="m",name="avg_npc_822_1#7$1",focus="m")]
[name="猎户"]......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_820_1#2$1",focus="l")]
[charslot(slot="r",name="avg_npc_787_1#4$1",focus="l")]
[name="方小石"]......
[charslot(slot="r",name="avg_npc_787_1#4$1",focus="r")]
[name="仇白"]一路上话那么多，见了自己爹，反倒成了哑巴？
[Dialog]
[charslot]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_820_1#2$1",focus="m")]
[name="方小石"]爹......原来你在啊。
[charslot(slot="m",name="avg_npc_787_1#2$1",focus="m")]
[name="仇白"]......
[Dialog]
[charslot(slot="m",name="avg_npc_822_1#1$1",focus="m")]
[Delay(time=0.7)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_822_1#1$1",afrom=1,ato=0,duration=1,isblock=true)]
[Delay(time=1.5)]
[charslot]
猎户抿了抿发白的嘴唇，没有答儿子的话，转身走进了屋子，把背着的木头放在墙边。
少年僵在原地没有动弹，仇白用剑柄推了他一把。
[Dialog]
[Delay(time=1)]
[name="猎户"]姑娘你坐，你坐。辛苦你送这小子回来，我给你倒杯水去。
[charslot(slot="m",name="avg_npc_787_1#8$1",focus="m")]
[name="仇白"]不用麻烦。你们父子重逢，我就不打扰了。
[charslot(slot="m",name="avg_npc_787_1#12$1",focus="m")]
[name="仇白"]我去村子里转转。
[charslot(slot="m",name="avg_npc_820_1#2$1",focus="m")]
[name="方小石"]我带你去——
[charslot(slot="m",name="avg_npc_787_1#1$1",focus="m")]
[name="仇白"]好好待着。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_787_1#1$1",afrom=1,ato=0,duration=1,isblock=true)]
[Delay(time=1.5)]
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(screenadapt="showall", image="35_mini01_villagevacancy

... (全文32577字符)
```

### level_act14mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Subtitle(text="有什么办法，能让眼前的这座大山消失？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
聚落里的人世世代代都在这里，向大山讨生活。
野果生涩有毒，野兽狡猾凶猛，稍不留神就会丧了性命，但除此之外，没有食物可以果腹。
雨水洗刷过岩缝土壑，汇到山脚时已经变成黄浆，但除此之外，没有水源能够止渴。
他将一块石头磨得锋利，又撅断藤葛，将石头绑在细长的树干上。
现在他有了一把锄头。
他在山脚找到一小块相对湿润平坦的地方，用锄头挖出垄沟，把收集筛选过的种子撒下去。
现在他有了一块地。
可是单靠一块地养活不了所有人，但眼前的山......
山高万仞，上接流云，横迂百里，目不能及，回环陡峭，何其险峻！
风吹不进来，人走不出去，眼前的大山断绝了更多的生机。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="那就先用手里的锄头，把大山挖开。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
打那以后，他劳作和歇息都在这山脚下，一锄头一箕畚，醒了挖山累了睡。
半年的光阴，大山身上只多了几道浅浅的伤痕。但旁观的族人放下了手里的野果和黄浆。
越来越多的人加入了挖山的队伍，于是有了越来越多的锄头，有了越来越多的田地。
叩石垦壤，循环往复，叮当作响，日夜不绝。
[Dialog]
[delay(time=1)]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[charslot(slot="m",name="avg_npc_140",duration=3,isblock=true)]
[Delay(time=2)]
[bgeffect]
[charslot(slot="m",name="avg_npc_140",focus="none")]
[name="？？？"]你，挖了多久？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="挖山人"]三年？五年？记不清了......
[charslot(slot="m",name="avg_npc_140",focus="none")]
[name="？？？"]你，打算挖多久？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="挖山人"]挖到挖不动为止。
[charslot(slot="m",name="avg_npc_140",focus="none")]
[name="？？？"]何其愚蠢！你的锄头再锋利，拿坚硬厚重的岩层又有什么办法呢？你的箕畚再宽大，拿亿万方的土石又有什么办法呢？
[name="？？？"]就算耗尽你的生命，难道还真能挖空这座大山？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="挖山人"]那又有什么关系？
[name="挖山人"]我挖不动了，还有我的族人，还有我的子女；我的族人和子女挖不动了，还有他们的子女......
[name="挖山人"]这座大山不会再改变，但对付它的人永远在增多，无穷尽也。
[name="挖山人"]更何况也不需要把山挖空，只是多挖一天，我们就能多开垦一块田地，多养活一个孩子。
[charslot(slot="m",name="avg_npc_140",focus="none")]
[name="？？？"]你，不打算停下来？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="挖山人"]停下来等于向它妥协。
[charslot(slot="m",name="avg_npc_140",focus="none")]
[name="？？？"]人，又为何非要和这山为敌呢？！
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="挖山人"]它又为何非要横在这里呢？！是这天地先与人作对。
[name="挖山人"]莫要再劝，从何处来回何处去罢。我要继续干活了。
[Dialog]
[charslot(slot="m",name="avg_npc_140",afrom=1,ato=0,duration=1,isblock=true)]
[Delay(time=1)]
[PlaySound(key="$swordtsing1",volume=0.6)]
[PlaySound(key="$d_avg_axehitscrape",volume=1,delay=0.5)]
[playsound(key="$d_avg_shovel",volume=0.7,delay=1)]
[Delay(time=4)]
[name="？？？"]......
[name="？？？"]何其不讲理！何其聒噪！
[name="？？？"]你们已经在我的尾巴上叮叮当当了五年三个月又七天......
[name="？？？"]罢了罢了，你们不停，那我走吧......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="大山是突然间消失的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="没有什么响动，没有什么异状，劳累了一天，他枕着箕畚睡去，一夜好梦。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="次日清晨，眼前只剩下零落的土石，和前所未有的开阔土地，他不禁怀疑大山是否真的存在过。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="族人说，他的勤勉和赤诚感动了神明，神明替他们挪走了大山。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g11_yumendesert", screenadapt="coverall", block=true)]
[playsound(key="$smallearthquake", volume=0.6)]
[delay(time=5)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[PlaySound(key="$d_avg_crwddiscuss_outside",loop=true, channel="mes", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
几天前
[Dialog]
[charslot(slot="m",name="avg_npc_798_1#1$1",focus="m")]
[name="围观的村民"]族长来了，族长来了。
[Dialog]
[charslot]
[StopSound(channel="mes", fadetime=1.5)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_821_1#4$1",duration=1,isblock=true)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_821_1#4$1",focus="m")]
[name="老族长"]......
[charslot(slot="m",name="avg_npc_141",focus="m")]
[name="报信的村民"]昨天暴雨下了一夜，我担心泥灰材料被雨水泡坏，早上来检查的时候，就发现这段驰道已经被泥石流冲毁了......
[name="报信的村民"]这个孩子当时就躺在边上的泥滩里，我上去看的时候，就、就已经......没了气。
[charslot(slot="m",name="avg_npc_821_1#4$1",focus="m")]
[charslot(slot = "m", action="shake",random=true, power=5, times=60,duration=0.3)]
[name="老族长"]......
[charslot(slot="m",name="avg_npc_141",focus="m")]
[name="报信的村民"]族长？族长！您怎么了？
[charslot(slot="m",name="avg_npc_821_1#4$1",focus="m")]
[name="老族长"]怎么会......怎么会有人......
[charslot(slot="m",name="avg_npc_141",focus="m")]
[name="报信的村民"]我估摸着，他应该是沿着驰道走夜路，碰巧遇上了山体滑坡......
[name="报信的村民"]已经在村子里问过一遍了，谁都不认识这个孩子，附近其他村子好像也没有人见过这个面孔。
[charslot(slot="m",name="avg_npc_798_1#1$1",focus="m")]
[name="围观的村民"]看他的穿着打扮，根本就不像咱们山里的人......这么年轻的孩子，孤身一人来这大山里做什么呢？
[name="围观的村民"]族长，您还是说句话吧，现在该怎么办，大伙儿都等您拿主意呢。
[charslot(slot="m",name="avg_npc_821_1#5$1",focus="m")]
[name="老族长"]他......
[charslot(slot="m",name="avg_npc_821_1#1$1",focus="m")]
[name="老族长"]他身上带着什么能证明身份的东西没有？
[charslot(slot="m",name="avg_npc_141",focus="m")]
[name="报信的村民"]没找到......有想必也被泥石流冲不见了......
[charslot(slot="m",name="avg_npc_821_1#10$1",focus="m")]
[name="老族长"]他手上是什么？
[Dialog]
[charslot(slot="m",name="avg_npc_141",focus="m")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_141",posfrom="0,0",posto="0,-50",duration=1,isblock=false)]
[charslot(slot="m",name="avg_npc_141",afrom=1,ato=0,duration=0.5)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_cloakmovement", volume=0.7)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_open_box", volume=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_141",posfrom="0,-50",posto="0,0",duration=1,isblock=false)]
[charslot(slot="m",name="avg_npc_141",afrom=0,ato=1,duration=0.5)]
[Delay(time=1.5)]
[charslot(slot="m"

... (全文31317字符)
```

### level_act14mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="35_mini01_villagevacancy",screenadapt="showall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_animal_loop",volume=0.4, channel="bd", loop=true)]
[PlayMusic(key="$normal_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
羽兽空荡荡地叫了几声，又一个日头爬过山来。
太阳的脸色一天一变，昨天还是明晃晃的，今天就变得有气无力。厚重的云层里漏下几缕稀疏的光线，在村庄空地上镀上一层灰白。
一个老人坐在轮椅上，愣愣地盯着眼前的仓库。
有人嘱咐过他，只要里面传出一点声响，或是看到有人逃出来，就大声呼喊，叫人过来帮忙。
他年纪很大了，走路都需要人搀扶，能做的事已经不多了。
有人嘱咐过他，最近村里在干一件重要的事，只要事成了，大伙儿就能过上好日子。
为了办成这件事，一定不能让仓库里的人逃出来。
他老了，但还有派得上用场的地方，还能帮到村子。
[StopSound(channel="bd", fadetime=2)]
晨风骤起，毯子离开了他的肩膀，落在了身后一米开外的地方。
他刚想喊人来帮忙，又觉得比起被委托的任务，这样的事不该惊动大伙儿。
有人捡起了地上的毯子，掸了掸尘土，重新给他披上。
[name="年迈的老人"]谢谢哟......
[name="年迈的老人"]你是谁家的孩子？
[name="？？？"]不客气。
[name="年迈的老人"]那个，官府来人了吗？他们什么时候才来把人带走？那“事”办成了吗？
[name="？？？"]您知不知道，这里面关的人是谁？知不知道，大伙儿准备干的“事”是什么？
[name="年迈的老人"]你说啥？我耳朵不好使，说话大点声——
[name="？？？"]......
[name="年迈的老人"]好，我知道啦。我就在这守着，哪都不去。
[name="年迈的老人"]行啦，别管我这个老头子啦。年轻人忙该忙的事去......
[name="年迈的老人"]放心，我盯着呢，这里的人跑不了。
[name="年迈的老人"]我过了一辈子苦日子，总不能让你们年轻人还过苦日子。交给我的事，我总得办好喽。
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_787_1#5$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_787_1#5$1",focus="m")]
[name="仇白"]......
[Dialog]
[charslot(slot="m",name="avg_npc_787_1#5$1",afrom=1,ato=0,duration=0.5)]
[Delay(time=0.7)]
剑客将老人的轮椅向前推了几步，好让他能晒到太阳，然后悄然离去。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_desert_1", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[name="桑葚"]这里路应该还是向西的，我应该没有搞错吧......
[name="桑葚"]过了那道急弯向前走，走到第三个岔路口再左转......
[name="桑葚"]可是这个路，到底哪里才算岔路口啊......
[Dialog]
[delay(time=1)]
[name="桑葚"]啊，太好了，终于见到人了！
[Dialog]
[charslot(slot="m",name="avg_473_mberry_1#11$1",duration=0.7)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_473_mberry_1#11$1",focus="m")]
[name="桑葚"]大伯您好......请问，您是住在这附近村子里的人吗？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="路过的村民A"]欸，你是？
[charslot(slot="m",name="avg_473_mberry_1#2$1",focus="m")]
[name="桑葚"]我是灾害救援队的一名成员，听说这里前几天发生了一场泥石流，我来调查这里的受灾情况，但是我的地图好像有些误差......
[charslot(slot="m",name="avg_473_mberry_1#10$1",focus="m")]
[name="桑葚"]请问您有没有听说过，这附近有受到泥石流影响的村子？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="路过的村民A"]这深山里的路，从来都是靠常走的人自己记着，就没听说过地图好使的。
[name="路过的村民A"]你问的是谋善村吧，我就是那儿的人。
[name="路过的村民A"]前两天连天暴雨，是有一段驰道被冲垮了......但是没影响到村子。
[charslot(slot="m",name="avg_473_mberry_1#9$1",focus="m")]
[name="桑葚"]太好了，看来没有找错，就是在这个方向......
[charslot(slot="m",name="avg_473_mberry_1#11$1",focus="m")]
[name="桑葚"]请问大伯，这里到谋善村该怎么走？
[charslot(slot="m",name="avg_npc_140",focus="m")]
[name="路过的村民A"]沿着这条路继续往前，遇到岔路就向北走。大概还有小半天的路。
[charslot(slot="m",name="avg_473_mberry_1#11$1",focus="m")]
[name="桑葚"]多谢大伯！
[Dialog]
[PlaySound(key="$runsand", volume=0.6)]
[charslot(slot="m",name="avg_473_mberry_1#11$1",afrom=1,ato=0,duration=1)]
[Delay(time=1.5)]
[charslot]
[charslot(slot="l",name="avg_npc_140")]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_797_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="r")]
[name="路过的村民B"]按族长嘱咐的，旁边的陷阱都已经装好了......希望还是别用上。
[name="路过的村民B"]毕竟平时她也总是帮村子里的忙，还是尽量别伤人，把她拖在村外就行。
[charslot(slot="l",name="avg_npc_140",focus="l")]
[name="路过的村民A"]反正我就是出力气的，你让我干嘛我就干嘛。
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="r")]
[name="路过的村民B"]唉，你说怎么就这么巧。本来就是天知地知的事，偏偏让那个一根筋的信使撞上了。
[name="路过的村民B"]对了，刚和你说话那小姑娘是谁，来干嘛的？
[charslot(slot="l",name="avg_npc_140",focus="l")]
[name="路过的村民A"]哦，说是什么救援队，来查泥石流的。
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="r")]
[name="路过的村民B"]那你就放她过去了？！
[charslot(slot="l",name="avg_npc_140",focus="l")]
[name="路过的村民A"]族长让我们在这里拦信使，关救援队什么事？
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="r")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="路过的村民B"]你个呆子！族长让我们在这里拦信使，不就是怕外人进来坏了我们事？
[name="路过的村民B"]那救援队，不就是官府派来的？
[name="路过的村民B"]官府提前来了人，村里还没做好准备，事情搞砸了怎么办？
[charslot(slot="l",name="avg_npc_140",focus="l")]
[name="路过的村民A"]我倒也没想这么多......那现在咋整？
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="r")]
[name="路过的村民B"]还能咋整？赶紧抄近道回村子里通知族长啊！
[name="路过的村民B"]让他们赶快把方小石好好藏起来，千万别被发现了！
[charslot(slot="l",name="avg_npc_140",focus="l")]
[name="路过的村民A"]这......我该咋说......
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="r")]
[name="路过的村民B"]算了，还是你在这守着，我去报信！
[Dialog]
[charslot(slot="r",name="avg_npc_797_1#1$1",focus="all")]
[Delay(time=0.3)]
[PlaySound(key="$rungeneral", volume=0.6)]
[charslot(slot="r",name="avg_npc_797_1#1$1",posfrom="0,0",posto="300,0",duration=1)]
[charslot(slot="r",name="avg_npc_797_1#1$1",afrom=1,ato=0,duration=0.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_140",focus="l")]
[charslot(slot="l",name="avg_npc_140",posfrom="0,0",posto="200,0",afrom=1,ato=1,duration=1)]
[Delay(time=1)]
[name="路过的村民A"]等——
[name="路过的村民A"]跑这么急，你这陷阱是怎么用的也没跟我说明白。
[name="路过的村民A"]这陷阱看起来还挺像样，一眼看过去还真不知道坑藏在哪——
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="l",name="avg_npc_140",posfrom="200,0",posto="200,-50",duration=1,isblock=false)]
[charslot(slot="l",name="avg_npc_140",afrom=1,ato=0,duration=0.5)]
[Delay(time=2)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4083_chimes_1#10$1",duration=1)]
[Delay(time=1.5)]
[name="信使"]这是怎么回事......？
[name="信使"]你......需要帮忙吗？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g13_yanlivingroom", screenadapt="coverall", block=true)]
[delay(time=1)]
[P

... (全文38786字符)
```

### level_act14mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="35_mini01_villagevacancy",screenadapt="showall")]
[Delay(time=1)]
[playmusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="着急的小孩"]怎么样怎么样？
[name="霸道的小孩"]拿到了......
[name="着急的小孩"]没被族长发现吧？
[name="霸道的小孩"]族长不在家。好像是去移山庙给先祖换贡品了......
[name="着急的小孩"]那就好，不然又得挨骂了......快拿出来快拿出来。
[Dialog]
[PlaySound(key="$d_avg_cardboard", volume=1)]
[PlaySound(key="$d_avg_open_box",volume=1,delay=0.6)]
[Delay(time=2)]
[name="着急的小孩"]这些按钮是干嘛用的，这个圆圆的，像是嵌着一个手电筒......它真的是信使姐姐说的那个摄......什么机吗？
[name="霸道的小孩"]“摄像机”。
[name="霸道的小孩"]肯定没错啦，之前信使姐姐带过来给我们看的杂志里就有这台机器的广告......
[name="霸道的小孩"]昨天族长他们从那个哥哥身上发现它的时候，我一下子就注意到了。
[name="着急的小孩"]这个“摄像机”真的能把人收进去吗？
[name="霸道的小孩"]什么叫“收进去”？那叫“拍摄”！
[name="着急的小孩"]好好好，快点打开看看里面拍摄了什么。
[name="霸道的小孩"]我在试，但是没有反应......
[name="霸道的小孩"]有可能是昨天被泥石流一冲，里面的零件被水泡坏了......
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=40, randomness=90, block=false, fadeout=true)]
[name="着急的小孩"]你就是不懂装懂，让我试试！
[name="霸道的小孩"]别抢、别抢......
[Dialog]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_throwstone",volume=1)]
[PlaySound(key="$d_avg_punchsp5", volume=0.4,delay=0.2)]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=40, randomness=90, block=true, fadeout=true)]
[Delay(time=1)]
[name="？？？"]哎哟......
[name="？？？"]小僧的脑袋！
[Dialog]
[charslot(slot="m",name="avg_362_saga_1#7$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="m")]
[name="嵯峨"]二位小施主为何要拿石头砸小僧？
[Dialog]
[charslot]
[name="霸道的小孩"]......
[name="着急的小孩"]......
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="m")]
[name="嵯峨"]不必愁苦不必愁苦，一点都不疼......小僧没有怪罪二位的意思。
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="none")]
[name="着急的小孩"]可以还给我们吗？
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="m")]
[name="嵯峨"]若是还给了你们，你们又拿着去砸别人可就不好了。
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="none")]
[name="着急的小孩"]这是摄像机，不是石头！
[charslot(slot="m",name="avg_362_saga_1#8$1",focus="m")]
[name="嵯峨"]......
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="m")]
[name="嵯峨"]原来此物便是摄像机啊，小僧还在东国时，就听师兄们提起过。如此轻便的物件，却能将所见所闻以影像的形式永远留存。
[name="嵯峨"]小僧告别住持爷爷后，在大炎境内云游，又在某位先生的画卷中盘桓许久，见过奇景奇物无数，可惜过目便再难相逢，留下了不少遗憾。
[name="嵯峨"]如若身边有这样的机器，那小僧便不必为再难得见之物、再难得见之人而苦恼。
[charslot(slot="m",name="avg_362_saga_1#5$1",focus="m")]
[name="嵯峨"]这个摄像机可以借小僧看看吗？
[charslot(slot="m",name="avg_362_saga_1#5$1",focus="none")]
[name="霸道的小孩"]看吧，看吧，反正也坏了。
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="m")]
[name="嵯峨"]如此一方小小的屏幕，竟然还可以翻转整整一周，好生精巧......
[charslot(slot="m",name="avg_362_saga_1#8$1",focus="m")]
[name="嵯峨"]唔......机器的后面有个盖子是可以抠开的。
[Dialog]
[PlaySound(key="$d_avg_open_box", volume=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_362_saga_1#8$1",focus="m")]
[name="嵯峨"]——
[charslot(slot="m",name="avg_362_saga_1#7$1",focus="m")]
[name="嵯峨"]呀，屏幕亮了......
[Dialog]
[charslot]
[name="霸道的小孩"]开机了？你是怎么弄的......
[name="着急的小孩"]快看看里面有什么？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[musicvolume(volume=0.2, fadetime=1)]
[charslot]
[Background(image="bg_coldforest",screenadapt="showall")]
[charslot(slot="m",name="avg_4083_chimes_1#4$1",focus="m")]
[delay(time=1)]
[PlaySound(key="$d_avg_devicebeep",volume=1)]
[curtain(direction = 2,fillfrom = 0.05,fillto = 0.05,fadetime=0.01)]
[curtain(direction = 6,fillfrom = 0.05,fillto = 0.05,fadetime=0.01)]
[curtain(direction = 0,fillfrom = 0.2,fillto = 0.2,fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0.2,fadetime=0.01, block = true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
你一个从来没有真正了解过这里的人，又凭什么来评价我们的生活？又凭什么空谈“改变”？
[charslot(slot="m",name="avg_4083_chimes_1#6$1",focus="m")]
你口口声声说的“关怀”，说到底都是居高临下的同情罢了。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_4083_chimes_1#6$1",afrom=1,ato=0,duration=1,isblock=true)]
[Delay(time=2.5)]
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
不要再跟着我！
[Dialog]
[playsound(key="$transmission", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[curtain]
[charslot]
[Background(image="35_mini01_villagevacancy", screenadapt="coverall", block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
上面的人呆呆地眨了眨眼睛，嵯峨突然反应过来那是自己的脸。
画面已经消失，再次变回了一块反光的屏幕。
[name="着急的小孩"]这就没了？
[name="霸道的小孩"]是不是你强行开机，把它弄坏了？
[Dialog]
[charslot(slot="m",name="avg_362_saga_1#8$1",focus="m")]
[name="嵯峨"]唔......
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_laccolith",screenadapt="coverall")]
[delay(time=1)]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_799_1#1$1",posfrom = "-100,0", posto = "-100,0",duration=0.7)]
[charslot(slot="r",name="avg_npc_797_1#1$1",posfrom = "140,0", posto = "140,0",duration=0.7)]
[charslot(slot="m",name="avg_npc_820_1#6$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_820_1#6$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="方小石"]放开——放开我！
[charslot(slot="l",name="avg_npc_799_1#1$1",focus="l")]
[name="着急的村民"]嘘，臭小子，你别乱喊！
[Dialog]
[charslot(slot="m",name="avg_npc_820_1#6$1",focus="all")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_punchsp4",volume=0.6)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m", posfrom = "0,0", posto = "50,0",afrom=1,ato=1,duration=0.1)]
[charslot(slot="r", posfrom = "140,0", pos

... (全文47057字符)
```

### level_act14mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="<i>感染日记：</i>", x=200, y=170, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>今天去过医院，心里一块大石头也算落了地。也确实没想到，原来自己的身体里真有“石头”。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我从小就是医院里的常客，面对医生下达的最终判决时，心里反而没有什么实感。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>“生命的意义是什么？”这个被无数电影和书本探讨过的问题，对我来说也不再有意义。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>只是在最后的这段时间里，我想完成一部真正属于自己的作品。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>常常在想，我们的眼界是否已经不知不觉被局限在眼前所见的环境，还有电视上描绘的那片大地当中？</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我们见惯了光鲜亮丽的高楼、霓虹璀璨的夜晚，却忽视了庞大得仿佛可以包容一切的移动城市，其实也只是这片大地的很小一部分。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>而人，又是何等的渺小。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>所以这最后的作品，我希望是一部纪录片。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我会走出我所熟悉的环境，走到尽可能遥远的地方，去看从未看过的风景。我想知道，在那些无人知晓的角落，住着哪些人，他们又在过着怎样的人生？</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>话说回来，独自完成一部纪录片的拍摄，肯定会有很多困难吧......何况是要去那么远的地方，光是要带的设备就让人吃不消了。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>嗐，顾忌那么多做什么？说不定走了一半，矿石病突然发作，生命和作品就一起结束了。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>倒不如想想，这部作品的名字，应该叫什么呢？</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stickerclear]
[charslot]
[Background(image="35_g9_yumensuburb", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4083_chimes_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]一共是三百三十七封信，还有二十五件包裹，你看，再核对一下？
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="none")]
[name="邮局员工"]数量没问题......就是这么多东西，你搬得动吗？
[charslot(slot="m",name="avg_4083_chimes_1#8$1",focus="m")]
[name="信使"]小意思，不是每次都一样嘛。
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]这次大概是半个月的行程，中途还要去一趟西边的镇子，听说有件很紧急的货物要送。
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="none")]
[name="邮局员工"]每年刚开春的时候都格外忙一点，你多受累。
[charslot(slot="m",name="avg_4083_chimes_1#8$1",focus="m")]
[name="信使"]哪里，应该的。
[charslot(slot="m",name="avg_4083_chimes_1#8$1",focus="none")]
[name="邮局员工"]就是......还有那个......
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]怎么了？有话就说啊。
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="none")]
[name="邮局员工"]最近开春，给家里人买了几件衣服，还有一些保养品。本来想你要是得闲的话......
[charslot(slot="m",name="avg_4083_chimes_1#8$1",focus="m")]
[name="信使"]得啦，还废什么话，快拿出来吧。
[charslot(slot="m",name="avg_4083_chimes_1#8$1",focus="none")]
[name="邮局员工"]谢谢信使姐！
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]你怎么老是叫我姐，我记得你还比我大几岁来着......
[Dialog]
[charslot]
[Delay(time=1)]
[PlaySound(key="$d_avg_bodyfallvalley", volume=0.6)]
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1.5)]
[name="邮局员工"]嘿咻——
[charslot(slot="m",name="avg_4083_chimes_1#10$1",focus="m")]
[name="信使"]这叫......几件？
[charslot(slot="m",name="avg_4083_chimes_1#10$1",focus="none")]
[name="邮局员工"]所以没好意思说......
[name="邮局员工"]要是不方便的话......
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]行啦，放上来吧。这么多东西都装上了，不差你这点。
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="none")]
[name="邮局员工"]多谢你！
[name="邮局员工"]对了，你要是见到我爸妈，还是麻烦帮我带个好。就说明年过年，我一定回去。
[charslot(slot="m",name="avg_4083_chimes_1#8$1",focus="m")]
[name="信使"]好，我记着了。
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]走了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g9_yumensuburb", screenadapt="coverall", block=true)]
[Delay(time=1)]
[curtain(direction = 2,fillfrom = 0.05,fillto = 0.05,fadetime=0.01)]
[curtain(direction = 6,fillfrom = 0.05,fillto = 0.05,fadetime=0.01)]
[curtain(direction = 0,fillfrom = 0.2,fillto = 0.2,fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0.2,fadetime=0.01, block = true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
您好，可以打扰一下吗......？
[Dialog]
[charslot(slot="m",name="avg_4083_chimes_1#1$1",duration=0.7)]
[Delay(time=1)]
[name="信使"]欸，是在叫我吗？
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="none")]
是的！
抱歉冒昧向您搭话......请问，您是这里的信使吗？
[Dialog]
[charslot(slot="m",name="avg_4083_chimes_1#1$1",focus="m")]
[name="信使"]这片山区的信和货物都是我负责送的......也算是吧。
[charslot(slot="m",name="avg_4083_chimes_1#5$1",focus="m")]
[name="信使"]你是......？
[charslot(slot="m",name="avg_4083_chimes_1#5$1",focus="none")]
您好，自我介绍一下。我是一名电影导演......我正在拍一部关于这片山区的纪录片。
我能跟着您一起走一段路吗？如果可以的话，也希望您能同意对您的拍摄......
[charslot(slot="m",name="avg_4083_chimes_1#10$1",focus="m")]
[name="信使"]......
[charslot(slot="m",name="avg_4083_chimes_1#10$1",focus="none")]
我......我不是坏人！
我的身份证件应该是丢在了从上一个村子来这里的路上，好像也没有什么其他可以证明身份的东西......
您看！我的这

... (全文33039字符)
```


## 统计

- 总字符数：222592
- 对话行数：1616


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
