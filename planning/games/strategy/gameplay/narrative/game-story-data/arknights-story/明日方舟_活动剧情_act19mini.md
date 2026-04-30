# 明日方舟 · 活动剧情 · act19mini（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act19mini」完整剧情脚本（7个文件，1721行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act19mini
- 脚本文件数：7

### level_act19mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkalley_intro",key="$darkalley_loop", volume=0.6)]
[playsound(key="$d_avg_lightrain_loop",loop=true,channel="1",volume=0.5)]
[Delay(time=2)]
这是家不大的茶馆，本就不甚高大的房屋被分出二层的格局。
屋里陈设简洁，大堂中不多不少，十副供六人落座的木质桌椅被摆放得整整齐齐，桌上的茶渍都被尽可能抹去，足见得这里的主人勤勉。
茶馆的跑堂把一瓢又一瓢的水洒在地上，用拖布将屋里的每一块青石板都抹得透亮。
茶馆看似许久没有迎来客人，也不知是什么样的客人值得这样的礼遇。
紧接着，客人就从门外来了。
[Dialog]
[playsound(key="$dooropenquite",channel="2")]
[stopsound(channel="1",fadetime=2)]
[charslot(slot="l",name="avg_npc_007",duration=2)]
[charslot(slot="r",name="avg_npc_008",duration=2)]
[Delay(time=3.5)]
[charslot]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_303_1#1$1",duration=2)]
[Delay(time=2.5)]
[name="茶馆跑堂"]一、二......二位客官里面请，要不要先上一壶茶？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[charslot(slot="r",name="avg_npc_008",focus="l")]
[name="凶悍的男人"]不急，我先问你——这座镇子是不是叫邙山镇？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]这座镇子是叫邙山镇。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[charslot(slot="r",name="avg_npc_008",focus="l")]
[name="凶悍的男人"]你是这家茶馆的掌柜，还是跑堂？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]我是跑堂。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[charslot(slot="r",name="avg_npc_008",focus="l")]
[name="凶悍的男人"]掌柜不在？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]掌柜不在。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[charslot(slot="r",name="avg_npc_008",focus="l")]
[name="凶悍的男人"]还真是问什么答什么，你倒是老实。
[name="凶悍的男人"]那我再问你，今日你们这家茶馆里，有没有来过面生的外地客人？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]来过的。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[charslot(slot="r",name="avg_npc_008",focus="l")]
[name="凶悍的男人"]何时来的？是什么模样的人？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]此时来的，两个人，都是劫匪模样。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="r")]
[charslot(slot="r",name="avg_npc_008",focus="r")]
[name="粗鲁的男人"]*炎国粗口*，我看你是存心消遣我们！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[delay(time=0.3)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0.5, block=true)]
[Dialog]
[delay(time=0.5)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[delay(time=0.5)]
粗鲁的男人大为恼怒，势大力沉的巴掌落在跑堂的脸上，打得他摔倒在地。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",name="avg_npc_303_1#1$1",afrom=0,ato=1,duration=1)]
[charslot(slot="m",posfrom="0,-40",posto="0,0",duration=2)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="none")]
可那跑堂的却不怒不恼，缓缓从地上爬起，又站在二人面前，全当无事发生一样。
[Dialog]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]两位客人真奇怪，不喝茶也不喝酒，我可不会招待了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[charslot(slot="r",name="avg_npc_008",focus="l")]
[name="凶悍的男人"]老二，别难为人家小兄弟。
[name="凶悍的男人"]去后厨看看还有没有别的人，顺便把后面所有门都关严实。
[Dialog]
[charslot(slot="r",name="avg_npc_008",focus="r")]
[delay(time=1.5)]
[charslot(slot="r",posfrom="0,0",posto="50,0",duration=2,focus="r")]
[charslot(slot="r",afrom=1,ato=0,duration=1,focus="r")]
[delay(time=2.5)]
[charslot(slot="l",name="avg_npc_007",focus="l")]
[name="凶悍的男人"]别急，茶当然是要喝的。
[name="凶悍的男人"]只是要在这里等一位客人，等她一块喝才行。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$dooropenquite")]
[charslot(slot="m",name="avg_npc_1871_1#12$1",duration=2)]
[Delay(time=2.5)]
不一会功夫，门外果然又来了一位客人。
[Dialog]
[charslot(slot="m",name="avg_npc_1871_1#1$1",focus="m")]
[name="伶俐的少女"]哦......？
[Dialog]
[charslot]
[playsound(key="$d_avg_exsheath")]
[Delay(time=2.5)]
少女刚踏进屋子，不及她环顾四周，弩箭和刀就分别抵在了她的后背和脖子上。
[charslot(slot="m",name="avg_npc_1871_1#6$1",focus="m")]
[name="伶俐的少女"]哈哈......
[name="伶俐的少女"]巧了，这不是陆家兄弟吗，真没想到在这里还能碰上你们。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_007",duration=2)]
[Delay(time=2.5)]
[name="陆大"]要是你能想到，应该就不会来了。
[name="陆大"]不过既然碰上了，就别走了。
[name="陆大"]跑堂的小兄弟。麻烦去将门关上，再挂上打烊的牌子。
[name="陆大"]然后，再给我们上一壶茶。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_303_1#1$1",focus="m")]
[name="茶馆跑堂"]茶上来了，几位慢用。
[charslot(slot="m",name="avg_npc_1871_1#1$1",focus="m")]
[name="伶俐的少女"]中原武林大名鼎鼎的“风云三刀”请我喝茶，我的面子还真不小。
[charslot(slot="m",name="avg_npc_007",focus="m")]
[name="陆大"]很可惜，现在只剩两个人了。
[name="陆大"]几天前，姑娘用那本秘籍栽赃我们兄弟三人。害我们被三大帮派外加玉门守军，总共上百号人追杀。
[name="陆大"]我们两人活着逃了，三弟却死在了百灶城外。
[name="陆大"]所以......我们两人怎么都该请姑娘喝一杯。
[charslot(slot="m",name="avg_npc_1871_1#6$1",focus="m")]
[name="伶俐的少女"]哈哈......两位大侠还活着，确实是件值得庆贺的事。那不如我以茶代酒，敬二位一杯，然后我们就好聚好散怎么样？
[Dialog]
[charslot(slot="m",name="avg_npc_008",focus="m")]
[playsound(key="$d_avg_smashtable")]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2.5)]
[name="陆二"]你还敢说——！
[charslot(slot="m",name="avg_npc_007",focus="m")]
[name="陆大"]我不想说废话——那本秘籍还在你的身上？
[charslot(slot="m",name="avg_npc_1871_1#1$1",focus="m")]
[name="伶俐的少女"]看来，你们是已经截获了交易的消息，才赶来在这家茶馆等着的？
[charslot(slot="m",name="

... (全文31284字符)
```

### level_act19mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Subtitle(text="有道是......书画受俗子品题，三生浩劫；鼎彝与市人赏鉴，千古异冤......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可是壶兄啊壶兄，我自诩不是个凡夫俗子，你说你我对饮那些日子，我又何时赖过酒，又怎的得罪了你？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="少了你这个酒友，我又该上何处找人对饮哟......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="唉......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="63_mini03_privateschool",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_797_1#1$1",duration=2)]
[Delay(time=2.5)]
[name="慌张的学生"]先生，先生！不好了！
[name="慌张的学生"]胡君......胡君他——他死啦！
[charslot(slot="m",name="avg_npc_1867_1#2$1",focus="m")]
[name="私塾先生"]啊——
[name="私塾先生"]这是何时的事......怎会如此......
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="慌张的学生"]就在胡君平日里待着的那个茶馆，他从二楼跌了下来，摔死啦！
[name="慌张的学生"]一定......一定是被那个坏女人杀死的！
[name="慌张的学生"]她一定，还会回来找我们的！
[charslot(slot="m",name="avg_npc_1867_1#2$1",focus="m")]
[name="私塾先生"]唉......我平时是怎么教你们的？
[name="私塾先生"]于未见之事不可轻言，你们既然没有亲眼看到，怎么能妄下定论？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="慌张的学生"]可是先生还说过，要举一反三。
[name="慌张的学生"]那个坏女人最近杀了好多人，这次胡君怎么不可能是她杀的？
[charslot(slot="m",name="avg_npc_1867_1#1$1",focus="m")]
[name="私塾先生"]举一反三，说的是理，不是事，更不是人。
[name="私塾先生"]你自己不想被别人恶意相向，便应该想到别人也不愿意被恶意相向，这叫做理。
[name="私塾先生"]但一个人做了一件错事，便说他此生只能做错事，那就叫不讲理了。
[charslot(slot="m",name="avg_npc_1867_1#6$1",focus="m")]
[name="私塾先生"]罢了罢了，其中的道理不是三两句话就能说通的，眼下还有更要紧的事。
[name="私塾先生"]胡君在茶馆坠楼身亡，那有没有人捡到他的遗骸？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="慌张的学生"]这个我可是亲眼看见了！
[name="慌张的学生"]胡君从楼上掉下来后，有一个天师打扮的人，把摔碎的胡君捡走啦。
[charslot(slot="m",name="avg_npc_1867_1#3$1",focus="m")]
[name="私塾先生"]怎么还有天师......？
[name="私塾先生"]这可不是开玩笑的事，你确定看清楚了？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="慌张的学生"]看清啦看清啦，胡君摔死的时候，那天师就在那儿。
[name="慌张的学生"]后来我还看到，那人拿着胡君的尸体，在镇上到处打听呢。
[charslot(slot="m",name="avg_npc_1867_1#2$1",focus="m")]
[name="私塾先生"]坏事坏事......既然此事已经被撞见，恐怕免不了一番纠缠。
[name="私塾先生"]可无论如何，胡君的遗骸还在那位天师手上，得想个办法......得想个办法拿回来才行。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="慌张的学生"]先生的意思，是想让我们从那天师手上把胡君的尸体偷出来？
[charslot(slot="m",name="avg_npc_1867_1#4$1",focus="m")]
[name="私塾先生"]说了多少遍，殁去的同胞，要称“遗骸”，不可称尸体......
[name="私塾先生"]还有，是“窃”，不是“偷”。我不是和你们讲过，为了一己私欲称之为“偷”，为了——
[name="私塾先生"]不说了不说了，时间紧张，那位天师随时会到。按我之前教过你们的，都各自去准备吧......
[Dialog]
[charslot]
[playsound(key="$doorknockquite")]
[Delay(time=1.5)]
[name="麟青砚"]请问......阁下可是“蒲先生”？
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="63_mini03_privateschool",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]......
[charslot(slot="m",name="avg_npc_1867_1#1$1",focus="m")]
[name="蒲先生"]......
[Dialog]
[charslot]
麟青砚自从走进了这间不大的学堂，便一言不发，仔细审视着屋里的每一件物件。
过了足有一炷香的工夫，坐在她对面的老先生终于忍不住开了口。
[charslot(slot="m",name="avg_npc_1867_1#1$1",focus="m")]
[name="蒲先生"]请问......
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]自我介绍一下，在下麟青砚，是大理......是天师府的一名天师。
[charslot(slot="m",name="avg_npc_1867_1#5$1",focus="m")]
[name="蒲先生"]从大人的打扮上是看得出来的。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]蒲先生平时也会与天师打交道？
[charslot(slot="m",name="avg_npc_1867_1#5$1",focus="m")]
[name="蒲先生"]这座小镇临近天师府，平日里镇上百姓的生活多仰仗天师们关照。当然是认得的。
[charslot(slot="m",name="avg_npc_1867_1#1$1",focus="m")]
[name="蒲先生"]这位麟天师......今天究竟是为何事到访？
[charslot(slot="m",name="avg_1043_leizi2_1#3$1",focus="m")]
[name="麟青砚"]不怕先生笑话，今天我初到这座邙山镇，就遇上了一件怪事。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]小镇南边的茶馆，有一位自称胡君的跑堂。未时三刻，在茶馆里下毒绑架了四名游客。
[name="麟青砚"]当时我正巧撞见此事，正要追捕的时候，却亲眼看见他从二楼摔了下来。
[name="麟青砚"]我赶到坠落场地的时候，在那里只看见了一个摔碎的茶壶。
[name="麟青砚"]我本以为是自己眼花。可事实证明，当时在场的所有人中，不只是我看到了这一幕。
[charslot(slot="m",name="avg_npc_1867_1#6$1",focus="m")]
[name="蒲先生"]您是说，有一个人从楼上坠亡，却变成了碎茶壶？这可是闻所未闻的奇事......
[name="蒲先生"]那......麟天师，您说的这个碎茶壶，能不能让我瞧一眼？
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]......
[Dialog]
[charslot]
麟青砚的手伸入口袋中，拿出了一个包裹放在桌上。
蒲先生正要拿过，麟青砚却一把按住了包裹。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]先生请稍等，我想先问先生几个问题。
[charslot(slot="m",name="avg_npc_1867_1#2$1",focus="m")]
[name="蒲先生"]这......天师尽管问就是。
[charslot(slot="m",name="avg_1043_leizi2_1#10$1",focus="m")]
[name="麟青砚"]今天我在镇上打听死者消息，许多人都说知道有胡君此人，而且其中不少都说这位胡君是蒲先生您的熟人。
[name="麟青砚"]让我奇怪的是，我常年住在百灶，可却从来没有听说过与百灶近在咫尺的邙山下还有这样一座小镇。
[name="麟青砚"]这座邙山镇上没有官府管事，大家有什么事都找您的这座“置锥学塾”来解决。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]听上去，先生在这座小镇名望颇高？
[charslot(slot="m",name="avg_npc_1867_1#6$1",focus="m")]
[name="蒲先生"]哪里的话......哪里的话......
[name="蒲先生"]麟天师的问题，我都能回答......
[charslot(slot="m",name="avg_npc_1867_1#2$1",focus="m")]
[name="蒲先生"]其实这座小镇，早年间也算热闹，可是后来慢慢地，百灶城建得越来越大，年轻人都跑去城里找活计了，镇上的人也就越来越少。
[name="蒲先生"]现在虽然还叫一个镇，可实际上才不过五百多户人家。再加上临近天师府，出不了什么乱子，朝廷也就放心不管啦。
[name="蒲先生"]至于老朽，之前不过是个读过几本书的穷书生，学问够不上通过考校，只能在这里教教孩子读书认字，混口饭吃。
[name="蒲先生"]许多年都是这样过来的，乡亲们称我一声先生，遇上点麻烦事愿意问问我的意见，已经是折煞人啦。
[charslot(slot="m",name="avg_1043_leizi2_1#3$1",focus="m")]
[name="麟青砚"]先生怕是谦虚了，教书育人本来就是有德之举，您自然担得起这些敬重。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]可是我注意到，您这间屋子里的收藏，书籍字画，古董文玩，怎么看都不像是凡物。
[charslot(slot="m",name="avg_npc_1867_1#3$1",focus="m")]
[name="蒲先生"]这些......
[charslot(slot="m",name="avg

... (全文23132字符)
```

### level_act19mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$calm_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1642_1#1$1",duration=2)]
[Delay(time=2.5)]
[name="顽皮的小孩"]咦......好漂亮的石头。
[name="顽皮的小孩"]啧啧，这么漂亮的花纹，摸上去还滑溜溜的，拿回去雕琢一下，说不定能在集市上卖不少钱......
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,duration=2)]
[Delay(time=2.5)]
[name="温厚的男人"]小朋友......把这块石头还给我好不好？
[charslot(slot="m",name="avg_npc_1642_1#1$1",focus="m")]
[name="顽皮的小孩"]还给你？这是我捡来的石头，怎么叫还给你？
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]这是我好不容易搜罗来的一块石头，装点园子用的。回程的路上不小心遗落在这里了。
[name="温厚的男人"]你把它还给我，等我的园林修好了，邀请你去玩好不好？
[charslot(slot="m",name="avg_npc_1642_1#1$1",focus="m")]
[name="顽皮的小孩"]不好不好......你说是你的就是你的了？我看这石头原本就在这，是我先捡到的，那就该归我。
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]唉唉，你这顽童，真是不讲理......
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]罢了，那这样如何？我用别的宝贝，来换你的这块石头好不好？
[name="温厚的男人"]只要你把这块石头给我，价钱随便你开。
[charslot(slot="m",name="avg_npc_1642_1#1$1",focus="m")]
[name="顽皮的小孩"]真的......？那我要一百......不对，一千......？
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]别说一千一万，百万千万，就算许你一辈子荣华富贵，也不在话下。
[charslot(slot="m",name="avg_npc_1642_1#1$1",focus="m")]
[name="顽皮的小孩"]你......
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]成交了？
[charslot(slot="m",name="avg_npc_1642_1#1$1",focus="m")]
[name="顽皮的小孩"]不对不对......还是不行。
[name="顽皮的小孩"]世上的人都是愿意占便宜的，你愿意拿那么多钱换这块石头，肯定说明这块石头价值更高。
[name="顽皮的小孩"]那我更要好好留着啦，我倒要看看，这块石头到底有什么不一般的地方。
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]你这小孩，倒是精明......
[charslot(slot="m",name="avg_npc_1869_1#1$1",bstart=0.3,bend=0.6,focus="m")]
[name="温厚的男人"]好吧，我倒也不急就是了。
[name="温厚的男人"]等你什么时候想通了，我再来找你买这块石头。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[focusout(duration=0, type="char", from=1, to=0, block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="骄横的男人"]荒唐......真是荒唐！
[name="骄横的男人"]这个老头子，临了还要给人添堵！
[charslot(slot="m",name="avg_npc_1625_1#1$1",focus="m")]
[name="温雅的女子"]二哥你也别这么说，爹爹的身体一天比一天差，眼看着就......
[name="温雅的女子"]我们做儿女的，平时没时间尽孝心，老人最后只有这一桩心愿，我们还是尽量满足他吧。
[charslot(slot="m",name="avg_npc_1630_1#1$1",focus="m")]
[name="矜持的男人"]二弟，小妹这几句话可比你厚道多了。
[name="矜持的男人"]百善孝为先，你现在是富贵了，但做人可不能忘本啊。
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="骄横的男人"]好好好，你们这会倒是一个个把孝字挂嘴上了，爹病了以后是谁在家里忙前忙后地伺候他？
[name="骄横的男人"]丢了这么一块破石头也要兴师动众的，我要是跑去百灶报官，大理寺都能因为我妨碍公务把我抓起来——我能怎么办？
[name="骄横的男人"]再说了......咱们家里有这么一块石头吗？
[charslot(slot="m",name="avg_npc_1630_1#1$1",focus="m")]
[name="矜持的男人"]谁知道，家里有多少产业，那还不是老二你心里最清楚吗？
[charslot(slot="m",name="avg_npc_797_1#1$1",focus="m")]
[name="骄横的男人"]我呸！你少在那里装清高。
[name="骄横的男人"]前几年没见你回过一次家，爹这一场大病你倒是跑得勤快了。你那点心思，瞒得过谁啊？
[charslot(slot="m",name="avg_npc_1625_1#1$1",focus="m")]
[name="温雅的女子"]好啦好啦，都别吵啦。帮不上忙也别添乱行不行？
[name="温雅的女子"]正巧赶上那位天师路过我们这，就等她帮我们找回来那块石头咯。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_1043_leizi2_1#14$1",focus="m")]
[name="麟青砚"]......
[charslot(slot="m",name="avg_npc_1639_1#1$1",focus="m")]
[name="管家"]老爷，这位是天师府的天师，也当过大理寺的少卿。
[name="管家"]她是来帮您找那块石头的，那块宝贝石头到底是怎么一回事，您跟她说说？
[Dialog]
[charslot]
[name="病床上的老人"]......哼......
[name="病床上的老人"]我的那几个孩子，到底是半点不上心......
[name="病床上的老人"]你就跟他们说，我的石头要是找不回来，我的钱他们一分都别想拿到。
[name="病床上的老人"]谁要是帮我把石头找回来，我就送一半家产给他。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]您就是万老先生吧......
[name="麟青砚"]您丢的，是块什么样的石头？
[Dialog]
[charslot]
[name="病床上的老人"]我小时候从河里捡到的石头，世上独一无二的石头。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]我是问，那块石头是什么样的宝物？是玉石还是什么别的宝石？
[Dialog]
[charslot]
[name="病床上的老人"]都不是......就是一块普通的石头。
[charslot(slot="m",name="avg_1043_leizi2_1#14$1",focus="m")]
[name="麟青砚"]那您是否知道，有谁会盯上您的这块石头？
[Dialog]
[charslot]
[name="病床上的老人"]我知道......但是盯上这块石头的人是万万不会来偷的......
[charslot(slot="m",name="avg_1043_leizi2_1#14$1",focus="m")]
[name="麟青砚"]那人是什么人？您又怎知......
[Dialog]
[charslot]
麟青砚还想再问些什么，可是病床上的老人却已经将头扭到一旁，显然不愿意再多说一句。
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]这块石头平时放在哪里保管？府上的人最后一次见那块石头，是什么时候？
[charslot(slot="m",name="avg_npc_1639_1#1$1",focus="m")]
[name="管家"]石头平时是保存在一个老爷专门托人打造的匣子里，藏在家里最深处的仓库里。
[name="管家"]前天晚上，我打扫库房的时候，看到里面还是一切正常，结果到第二天早上，我看到那只匣子摔在地上，里面的石头也不见了......
[charslot(slot="m",name="avg_1043_leizi2_1#1$1",focus="m")]
[name="麟青砚"]......方便带我去石头丢失的地方看看吗？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="63_mini01_market",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1622_1#1$1",focus="m")]
[name="意气风发的青年"]来来来，诸位请进！今日略备薄酒，敬答厚意。如有招待不周，还望亲友们海涵！
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="热情的农人"]老爷，恭贺你乔迁之喜，大吉大利！这是我从老家抓来的羽兽，还有这两笼羽兽卵......
[charsl

... (全文26435字符)
```

### level_act19mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="25_g08_pavilion",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="$calm_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1642_1#1$1",duration=2)]
[charslot(slot="r",name="avg_npc_1868_1#1$1",duration=2)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_1642_1#1$1",focus="l")]
[name="顽童"]大哥，你到底下不下啊。
[charslot(slot="r",name="avg_npc_1868_1#1$1",focus="r")]
[name="寡言的棋士"]不急，让我再想想。
[charslot(slot="l",name="avg_npc_1642_1#1$1",focus="l")]
[name="顽童"]可我看你想半天了，上次来你也在想，上上次也是，你是不是被什么人给骗了啊？
[name="顽童"]我来这么多回，从来没见过对面有人和你下棋。
[charslot(slot="r",name="avg_npc_1868_1#1$1",focus="r")]
[name="寡言的棋士"]不会有错的，我只是......在考虑后面的走法。
[name="寡言的棋士"]落子后对方的反应，以及之后所有变化，都要想。
[charslot(slot="l",name="avg_npc_1642_1#1$1",focus="l")]
[name="顽童"]真麻烦，想想就头疼......你就不能先把这局棋下完，然后再让那个和你下棋的人教你吗？
[name="顽童"]这只是一局棋，下输了又不会发生什么事。
[charslot(slot="r",name="avg_npc_1868_1#1$1",focus="r")]
[name="寡言的棋士"]但我不能输。
[name="寡言的棋士"]布下棋局的人承诺过，只要我赢了，就可以满足我一个愿望。
[charslot(slot="l",name="avg_npc_1642_1#1$1",focus="l")]
[name="顽童"]一个愿望？真的？
[name="顽童"]唉，可惜我算不清这些弯弯绕绕的，可能还是体力活更适合我些......
[name="顽童"]太阳好像快下山了，我也该回家了，家里还有一堆破烂要收拾呢。
[name="顽童"]再见！
[Dialog]
[charslot(slot="l",posfrom="0,0",posto="-60,0",duration=2)]
[delay(time=2.5)]
[charslot(slot="l",focus="l")]
[name="顽童"]突然想起来，我们见了那么多回，我还不知道大哥叫什么呢？
[charslot(slot="r",name="avg_npc_1868_1#5$1",focus="r")]
[name="寡言的棋士"]姓兰，名可，梅兰的兰，可否的可。
[charslot(slot="l",focus="l")]
[name="顽童"]那我的名字，大哥记得住吧。
[charslot(slot="r",name="avg_npc_1868_1#5$1",focus="r")]
[name="兰可"]洛勤？
[charslot(slot="l",focus="l")]
[name="小洛"]对咯！
[name="小洛"]那我真走咯，娘亲说我们要搬出去住一阵，等我回来了，一定会再来看你的。
[name="小洛"]再见！
[Dialog]
[playsound(key="$rungeneral")]
[charslot(slot="l",afrom=1,ato=0,duration=1)]
[charslot(slot="l",posfrom="-60,0",posto="-200,0",duration=2)]
[delay(time=2.5)]
[charslot]
步声渐远，夜色落在棋盘上，日光照亮棋子，雨雪洗净石凳。
兰可拿起一枚白子，正要落子，却又收回，摩挲了半天，最终掷回棋奁。
第十个死局了，他记得很清楚。
又是一盘算计，这一回，他得想个得胜的奇着。
......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="63_mini01_market",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1638_1#1$1",focus="m")]
[name="礼貌的先生"]云先生，在下就送您到这了。
[charslot(slot="m",name="avg_4196_reckpr_1#10$1",focus="m")]
[name="云青萍"]您之前不是说，那位在山上等我？
[charslot(slot="m",name="avg_npc_1638_1#1$1",focus="m")]
[name="礼貌的先生"]正是正是，那一位此时确实在山上，而我的任务，只是将您送至这条山路。
[name="礼貌的先生"]从此处上山只有一条路，也并不难走，周边的林子都清理过，不会有猛兽。
[name="礼貌的先生"]您只管向上走，其余的都为您安排好了。
[charslot(slot="m",name="avg_4196_reckpr_1#8$1",focus="m")]
[name="云青萍"]那要是继续追问，反而显得我不懂礼数了......
[charslot(slot="m",name="avg_4196_reckpr_1#9$1",focus="m")]
[name="云青萍"]那么，就此别过。
[charslot(slot="m",name="avg_npc_1638_1#1$1",focus="m")]
[name="礼貌的先生"]再会了，云先生。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=2)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4196_reckpr_1#1$1",focus="m")]
[name="云青萍"]话是这么说，可是......
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_forest",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4196_reckpr_1#10$1",duration=2)]
[Delay(time=2.5)]
[name="云青萍"]这哪里有进山的路啊......
[charslot(slot="m",name="avg_4196_reckpr_1#5$1",focus="m")]
[name="云青萍"]地上积叶厚重，怕是许久没人从此处登山了。
[name="云青萍"]而且连条兽道都没有......
[charslot(slot="m",name="avg_4196_reckpr_1#1$1",focus="m")]
[name="云青萍"]或许我该找位本地人问下。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1873_1#10$1",duration=2)]
[Delay(time=2.5)]
[name="彷徨的姑娘"]您好？
[charslot(slot="m",name="avg_4196_reckpr_1#8$1",focus="m")]
[name="云青萍"]您好姑娘，有什么事吗？
[charslot(slot="m",name="avg_npc_1873_1#8$1",focus="m")]
[name="彷徨的姑娘"]请问，您有没有见过我家郎君？
[name="彷徨的姑娘"]他年纪不大，有着头棕发，尾尖全白，穿着云衫土裤皮靴。
[charslot(slot="m",name="avg_4196_reckpr_1#10$1",focus="m")]
[name="云青萍"]我好像......没有见过这样的人，抱歉。
[charslot(slot="m",name="avg_npc_1873_1#8$1",focus="m")]
[name="彷徨的姑娘"]是这样啊......耽误您时间了......
[charslot(slot="m",name="avg_4196_reckpr_1#4$1",focus="m")]
[name="云青萍"]请留步，姑娘！
[charslot(slot="m",name="avg_4196_reckpr_1#1$1",focus="m")]
[name="云青萍"]您是这里的人吧，我想请问一下，这附近，可有上山的路？
[charslot(slot="m",name="avg_npc_1873_1#8$1",focus="m")]
[name="彷徨的姑娘"]您要上山？那您应该是找错路啦。
[name="彷徨的姑娘"]上山的正道在小镇另一头，这里是后山，又陡又险，镇民们都很少从此上山。
[charslot(slot="m",name="avg_4196_reckpr_1#7$1",focus="m")]
[name="云青萍"]（后山？我明明是从大道一路直行过来的，这怎么成了后山？）
[charslot(slot="m",name="avg_4196_reckpr_1#8$1",focus="m")]
[name="云青萍"]原来是这样吗......多谢姑娘。
[name="云青萍"]但我想......既然为我引路的那位先生留下话让我朝这个方向走，一定也有他的思量，我还是准备试试。
[name="云青萍"]告辞了。
[charslot(slot="m",name="avg_npc_1873_1#8$1",focus="m")]
[name="彷徨的姑娘"]......
[charslot(slot="m",name="avg_npc_1873_1#1$1",focus="m")]
[name="彷徨的姑娘"]先生，我同您一起上山吧。
[charslot(slot="m",name="avg_4196_reckpr_1#1$1",focus="m")]
[name="云青萍"]这位姑娘，您怎么......
[charslot(slot="m",name="avg_npc_1873_1#1$1",focus="m")]
[name="彷徨的姑娘"]山上路险，我们两人结伴，也能互相有个照应。
[name="彷徨的姑娘"]况且......镇里能问的地方我都问了个遍，这地界也就山上还没寻过了。若郎君还在此处，也只能在这山中了。
[charslot(slot="m",name="avg_4196_reckpr_1#8$1",focus="m")]
[name="云青萍"]那，多谢姑娘了。
[name="云青萍"]不知姑娘怎么称呼？
[charslot(slot="m",name="avg_npc_1873_1#7$1",focus="m")]
[name="彷徨的姑娘"]......白锦。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_g08_pavilion",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1627_1#1$1",focus="m")]
[name="洛勤"]兰大哥，这盘棋，你还是没头绪吗？
[charslot(slot="m",name="avg_npc_1868_1#1$1",focus="m")]
[name="兰可"]不急，不急。
[charslot(slot="m",name="avg_

... (全文24199字符)
```

### level_act19mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_avg_rainlight_loop",loop=true,channel="1",volume=0.5)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_140#2",duration=2)]
[Delay(time=2.5)]
[name="掌柜"]客人，已经是第二天了。
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]嗯，我知道。
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="掌柜"]您等的客人爽约了？
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]也许是遇上了什么事耽搁了。
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="掌柜"]你在这等着不要紧，可我这小店还要打烊呢。
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]要是嫌我白占了你一张桌子，我就出去。
[name="独自饮酒的剑客"]但我还是得待在门口......毕竟我和她约好的地方是这里。
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="掌柜"]你安心坐着吧！我能是那个意思？咱们的交情也不算浅了吧？
[name="掌柜"]第一次见你的时候，我还只是个小堂倌呢，一转眼我都成这家茶馆的掌柜了。
[name="掌柜"]说起来你这个人也真是奇怪，一个剑客，每年从......我又忘了，你是姜齐人还是玉门人来着？
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]居无定所，四海为家。
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="掌柜"]可我记得清楚，每年秋天这个时候，你都要专门跑来这个小镇，这个茶馆，和一个人见上一面——今年是第几年了？
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]第七年。
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="掌柜"]七年了......你们每次见面也就是喝喝茶聊聊天，你们不是情人，不是朋友，你甚至连她的名字都不知道吧？
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]我们有约在先，互不过问。
[charslot(slot="m",name="avg_npc_140#2",focus="m")]
[name="掌柜"]真是桩稀奇事......
[name="掌柜"]你等的这一位，到底是什么人？
[charslot(slot="m",name="avg_npc_140#2",focus="none")]
[name="独自饮酒的剑客"]我不知道......
[name="独自饮酒的剑客"]我这辈子，和很多人打过交道，奸的恶的，善的蠢的......见得多了，便觉得这世上的人也没那么难懂。
[name="独自饮酒的剑客"]只有她，我看不懂。
[Dialog]
[stopsound(channel="1",fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=2)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_glass_break")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2.5)]
......这位姑娘，你的剑把我的茶盏扫到地上了。
这屋里狭小，随身带的剑还是要收好。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1866_1#1$2",duration=2)]
[Delay(time=2.5)]
[name="带剑的女子"]不就是一杯茶，我赔你。
[charslot(slot="m",name="avg_npc_1866_1#2$2",focus="m")]
[name="带剑的女子"]我再多送你一壶酒，算交你一个朋友。
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="m")]
[name="带剑的女子"]交上朋友，也让你教我用剑。
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="none")]
我？哈哈哈......
姑娘应该是找错人了，我就是个普普通通的商人。运点货去夕城，偶然经过这个镇子，喝杯茶歇歇脚，不是什么剑客。
再说了，你看我身上哪有剑？哪有不带剑的剑客......
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="m")]
[name="带剑的女子"]别装了，你不同意，我不会放你走。
[Dialog]
[PlaySound(key="$d_avg_swordexsheath", volume=1)]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_smashtable")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="none")]
[name="慌张的堂倌"]欸欸，这位姑娘，好好的你劈店里的桌子干嘛啊？其他客人都被吓跑了......
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="m")]
[name="带剑的女子"]闭嘴。
[name="带剑的女子"]打坏的东西我一会自然会赔给你，不要破坏我和朋友聊天的兴致。
[charslot(slot="m",name="avg_npc_1866_1#3$2",focus="m")]
[name="带剑的女子"]再啰嗦，连你也劈了。
[charslot(slot="m",name="avg_npc_1866_1#3$2",focus="none")]
[name="慌张的堂倌"]好、好嘞......
[charslot(slot="m",name="avg_npc_1866_1#3$2",focus="none")]
......姑娘这般，倒是不讲道理了。
[charslot(slot="m",name="avg_npc_1866_1#2$2",focus="m")]
[name="带剑的女子"]讲道理有什么意思？还是闯荡江湖逍遥自在有意思。
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="m")]
[name="带剑的女子"]但是闯荡江湖，需要足够的本事。
[name="带剑的女子"]我知道你的剑术很高明，所以想请你教我。
[Dialog]
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="none")]
唉......
姑娘想学剑，恐怕是来迟了一步。
我的剑丢了......
......从它消失不见的那一刻起，我便已经立誓，金盆洗手，永远不再卷入江湖事。
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="m")]
[name="带剑的女子"]你的剑丢了？
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="none")]
丢了。
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="m")]
[name="带剑的女子"]什么时候丢的？
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="none")]
就在昨晚。
我刚在这小镇落脚，过了一夜，我的剑就不见了。
的确是突然不见的。没有贼来过，也没有贼能带走我的东西。 
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="m")]
[name="带剑的女子"]那是一柄怎样的剑？
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="none")]
好剑。
陪了我很多年，没有它，我做不了那么多生意，也挣不来如今在江湖上的名声。
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="m")]
[name="带剑的女子"]既然是这么重要的东西，还不赶紧去找？
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="none")]
恰恰相反，我不能去找。
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="m")]
[name="带剑的女子"]为什么？
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="none")]
这么多年过来，用剑、洗剑、再用剑，噩梦、清醒......我这辈子好像已经不剩下别的事情可做。
剑不会记得它曾经沾染的血腥，但我没法摆脱那些罪孽......我刚刚一直在想，丢剑，或许正是老天给我的警示。
我要摆脱那把剑，摆脱它带给我的身份，改头换面也好，找个地方孤老终生也好，我想要就此退隐江湖，了断此前的人生。
所以姑娘，我教不了你。
我们能在这间小小的茶馆相遇，是缘分。如果你不怪我好为人师，或许我能给你一句忠告......别学剑，也别入江湖。
[Dialog]
[charslot(slot="m",name="avg_npc_1866_1#7$2",focus="m")]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1866_1#2$2",focus="m")]
[name="带剑的女子"]你丢不掉它的。
[charslot(slot="m",name="avg_npc_1866_1#2$2",focus="none")]
为什么？
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="m")]
[name="带剑的女子"]因为你在说假话。
[charslot(slot="m",name="avg_npc_1866_1#8$2",focus="m")]
[name="带剑的女子"]你厌倦了冤冤相报的杀戮，但你打心底放不下快意潇洒、敢爱敢恨的日子。
[name="带剑的女子"]你只是想为自己金盆洗手找个理由，丢了的剑恰好就成了你的理由。
[charslot(slot="m",name="avg_npc_1866_1#8$2",focus="none")]
姑娘说这些话，好像很了解我似的......
[charslot(slot="m",name="avg_npc_1866_1#1$2",focus="m")]
[name="带剑的女子"]打个赌吗？明年这个时候，我们依然在这间茶馆见面。
[name="带剑的女子"]你大可以按你的心意，过一年不用剑的生活。
[charslot(slot="m",name="avg_npc_1866_1#2$2",focus="m")]


... (全文31890字符)
```

### level_act19mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="35_g8_yumenarena",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkalley_intro",key="$darkalley_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_788_1#1$1",duration=2)]
[Delay(time=2.5)]
[name="左宣辽"]怎么回事......？
[charslot(slot="m",name="avg_npc_795_1#1$1",focus="m")]
[name="玉门守军"]那疯汉闯到了演武场，不由分说就打伤了我们好几十号兄弟。我们看那人面貌，似乎是半年前，和宗师在这里比过武的那位汉子。
[name="玉门守军"]我们不知道他为什么发疯，只是尽量没伤着他。他就在这乱打了一通，转眼间又跑了！
[charslot(slot="m",name="avg_npc_788_1#8$1",focus="m")]
[name="左宣辽"]槐天裴......？
[name="左宣辽"]他做出这种疯事，那宗师的剑又如何了......
[Dialog]
[charslot]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_796_1#1$1",duration=2)]
[Delay(time=2.5)]
[name="玉门守军"]将军！
[name="玉门守军"]我们刚刚发现，军武库遭人闯入！
[charslot(slot="m",name="avg_npc_788_1#7$1",focus="m")]
[name="左宣辽"]......丢了什么东西？
[charslot(slot="m",name="avg_npc_796_1#1$1",focus="m")]
[name="玉门守军"]宗师留下的那本《武典》......丢了。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g7_zuosroom",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0.5, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Sticker(id="st1", multi = true, text="问左军侯安", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n战事将起，当惜将士性命，恤百姓民生", x=380,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n上兵伐谋，义在非攻",block = true)]
[Sticker(id="st1", multi = true, text="\n\n借宝书一用，不日即还",block = true)]
[Sticker(id="st1", multi = true, text="\n\n山海众 莫佚",block = true)]
[Sticker(id="st1", multi = true, text="\n\n敬上",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
军武库中一切物件完好无损，只有那书架中空出了一本书的位置。
一封信赫然留在了书架上。
[charslot(slot="m",name="avg_npc_788_1#7$1",focus="m")]
[name="左宣辽"]......
[name="左宣辽"]来人！
[charslot(slot="m",name="avg_npc_796_1#1$1",focus="m")]
[name="玉门守军"]在！
[name="玉门守军"]将军有什么吩咐？
[charslot(slot="m",name="avg_npc_788_1#1$1",focus="m")]
[name="左宣辽"]让信使准备好，替我送一封信去京城，给司岁台。
[charslot(slot="m",name="avg_npc_796_1#1$1",focus="m")]
[name="玉门守军"]得令。
[charslot(slot="m",name="avg_npc_788_1#1$1",focus="m")]
[name="左宣辽"]慢着，再找一人，送密信，去天师府。
[charslot(slot="m",name="avg_npc_796_1#1$1",focus="m")]
[name="玉门守军"]是。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="35_g6_yumengate",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_785_1#2$1",duration=2)]
[charslot(slot="r",name="avg_npc_1871_1#6$1",duration=2)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1871_1#6$1",focus="r")]
[name="伶俐的少女"]槐大侠果然好身手，出入万军阵中如入无人之境的武艺，大炎古往今来也找不出第二位了吧。
[Dialog]
[charslot(slot="l",name="avg_npc_785_1#2$1",focus="l")]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_785_1#2$1",focus="none")]
槐天裴并没有答话，只是晃晃悠悠地原地徘徊着，口中重复着几个含糊的音节。
[charslot(slot="r",name="avg_npc_1871_1#3$1",focus="r")]
[name="伶俐的少女"]槐大侠放心，你帮我取来了这本书，我自然也会帮你。
[charslot(slot="r",name="avg_npc_1871_1#1$1",focus="r")]
[name="伶俐的少女"]一场万众瞩目的擂台，让你和那位宗师，再好好打上一架。
[name="伶俐的少女"]十天后，邙山山顶，我会备好宴席静候阁下。
[charslot(slot="l",name="avg_npc_785_1#2$1",focus="l")]
[name="槐天裴"]......嗯。
[charslot(slot="r",name="avg_npc_1871_1#12$1",focus="r")]
[name="伶俐的少女"]不过我倒想问问槐大侠，你武功已经无人可敌，而且明知道那位宗师根本不是什么“正常人”，你就非要胜过他不可？
[name="伶俐的少女"]人兽本就有别，人与兽斗了上万年，从来靠的也不是以己之短搏彼之长啊。
[charslot(slot="l",name="avg_npc_785_1#11$1",focus="l")]
[name="槐天裴"]......你说的话，听不明白。
[name="槐天裴"]有人的武功比我高，那就练到胜过那个人，天地造化比我深，那就练到胜过这片天地。
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot="l",afrom=1,ato=0,duration=0.5)]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=1)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1871_1#12$1",focus="r")]
[name="伶俐的少女"]唉......要说你是人，你身上的这股痴劲已经多少不像是人所有的了。
[name="伶俐的少女"]但要说你不像人，要不是还有那点忘不掉的人情，你又怎会被那个“商人”逼到这般境地。
[charslot(slot="r",name="avg_npc_1871_1#3$1",focus="r")]
[name="伶俐的少女"]真不知道该说你是可怜还是可笑。
[charslot(slot="r",name="avg_npc_1871_1#6$1",focus="r")]
[name="伶俐的少女"]有趣......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="bg_wilderness_m",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_243_waaifu_1#1$1",duration=2)]
[charslot(slot="r",name="avg_322_lmlee_1#1$1",duration=2)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_243_waaifu_1#2$1",focus="l")]
[name="槐琥"]鲤叔，阿爸是往这里走的吗？
[charslot(slot="r",name="avg_322_lmlee_1#1$1",focus="r")]
[name="老鲤"]唔......我看地上这足迹，步距极宽，步频稳健，每一个脚印都深浅一致。
[name="老鲤"]看上去，一定是一位功力深厚的人留的。
[charslot(slot="l",name="avg_243_waaifu_1#2$1",focus="l")]
[name="槐琥"]我没看错的话，这应该是裂兽的爪痕才对......
[charslot(slot="l",name="avg_243_waaifu_1#6$1",focus="l")]
[name="槐琥"]鲤叔......你还在逗我。
[charslot(slot="r",name="avg_322_lmlee_1#9$1",focus="r")]
[name="老鲤"]哈哈哈......
[charslot(slot="r",name="avg_322_lmlee_1#10$1",focus="r")]
[name="老鲤"]唉，上次匆匆见过一面，结果又让他给跑了......从目前的线索来看，也只有这一条路了。
[name="老鲤"]对付精明人有精明人的办法，找你那武痴老爹，也只能用最“笨”的办法。
[name="老鲤"]慢慢找吧......
[charslot(slot="l",name="avg_243_waaifu_1#6$1",focus="l")]
[name="槐琥"]......
[charslot(slot="r",name="avg_322_lmlee_1#10$1",focus="r")]
[name="老鲤"]是担心他的安危，还是怨他又惹出这么大的麻烦？
[charslot(slot="l",name="avg_243_waaifu_1#5$1",focus="l")]
[name="槐琥"]我只是......不理解。
[name="槐琥"]他虽然一点也不靠谱，但是在武艺武德方面，向来是个正直的人......
[charslot(slot="l",name="avg_243_waaifu_1#1

... (全文37882字符)
```

### level_act19mini_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="63_mini04_mountaintop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$m_bat_bitw2_intro",key="$m_bat_bitw2_loop", volume=0.6)]
[Delay(time=2)]
[Effect(name="$e_slash_cross",x = 0, y = 8, rox = -4, roy = 52, roz = -5, layer = 2)]
[delay(time=0.1)]
[Effect(name="$e_slash_cross_hit",x = 0, y = 8, rox = -4, roy = 52, roz = -5, layer = 2)]
[PlaySound(key="$swordtsing4", volume=1)]
[charslot(slot="l",name="avg_4121_zuole_1#4$1",afrom=0,ato=1,duration=1)]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=1.5)]
[charslot(slot="r",name="avg_npc_1871_1#9$1",afrom=0,ato=1,duration=1)]
[charslot(slot="r",posfrom="0,0",posto="100,0",duration=1.5)]
[delay(time=1.5)]
[charslot(slot="r",posfrom="200,0",posto="-200,0",duration=0.5)]
[PlaySound(key="$d_avg_spear", volume=1,channel=1)]
[Effect(name="$e_slash_02_s",x = -30, y = 10, rox = 69, roy = 54, roz = -58, layer = 2)]
[CameraShake(duration=0.3, xstrength=100, ystrength=100, vibrato=40, randomness=90, fadetime=0.3,fadeout=true, block=false)]
[charslot(slot="l",afrom=1,ato=0,duration=0.5)]
[charslot(slot="l",posfrom="-100,0",posto="-200,0",duration=0.5)]
[Delay(time=0.7)]
[playsound(key="$d_avg_lightningmagic",channel="2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.02, block=true)]
[charslot(slot="r",afrom=1,ato=0,duration=1)]
[charslot(slot="r",posfrom="-200,0",posto="-270,-50",duration=1.5)]
[CameraShake(duration=0.3, xstrength=100, ystrength=100, vibrato=40, randomness=90, fadetime=0.3,fadeout=true, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$bodyfalldown3", volume=1)]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=40, randomness=90, fadetime=0.3,fadeout=true, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_1043_leizi2_1#4$1",duration=1.5)]
[Delay(time=2)]
[name="麟青砚"]还敢造次？
[Dialog]
[charslot]
惊雷破空，崩飞了少女的佩刀，她也被巨大的力量冲击倒地。
黑色的浓云在她的头顶盘踞，更大的雷霆似乎随时会从天而落。
[charslot(slot="m",name="avg_1043_leizi2_1#9$1",focus="m")]
[name="麟青砚"]不想这道雷落在你的头顶，就不要乱动。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",name="avg_npc_1871_1#13$1",afrom=0,ato=1,duration=1)]
[charslot(slot="m",posfrom="0,-50",posto="0,0",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1871_1#13$1",focus="m")]
[name="莫佚"]麟天师和左秉烛还真是咬死不放啊......
[name="莫佚"]事情已经圆满解决，又没有造成什么损伤，两位真的有必要这样苦苦相逼吗？
[charslot(slot="m",name="avg_4196_reckpr_1#6$1",focus="m")]
[name="云青萍"]莫姑娘你说自己只想看戏，可已有不少人，被卷入了这场“好戏”......
[charslot(slot="m",name="avg_4121_zuole_1#4$1",focus="m")]
[name="左乐"]用巨兽代理人之物召唤岁相，这样的能耐绝非常人可及。
[name="左乐"]老实交代，你究竟是什么人？又从哪里学会的这些禁术？
[charslot(slot="m",name="avg_npc_1871_1#1$1",focus="m")]
[name="莫佚"]哈，原来你在意的就只有这个啊。
[charslot(slot="m",name="avg_npc_1871_1#9$1",focus="m")]
[name="莫佚"]司岁台的秉烛人，这片大地上最古老的秘密就在你触手可及的地方，你想做的事，竟然只有把试图了解这些的人挨个捉回去？
[name="莫佚"]只听说过物件有主人，知识又何来主人？凭什么这些事只有司岁台能知道，别人就不能知道？
[charslot(slot="m",name="avg_4121_zuole_1#4$1",focus="m")]
[name="左乐"]......凭你在邙山镇的所作所为，让人如何相信你没有包藏祸心？
[name="左乐"]跟我们走一趟，把你知道的事情，还有谋划，统统交代清楚。
[charslot(slot="m",name="avg_npc_1871_1#6$1",focus="m")]
[name="莫佚"]哈哈，这样听起来我还是有些被活捉的价值嘛，那我要是执意要逃，你们是不是也没办法了？
[charslot(slot="m",name="avg_1043_leizi2_1#9$1",focus="m")]
[name="麟青砚"]执迷不悟......
[charslot(slot="m",name="avg_1043_leizi2_1#4$1",focus="m")]
[name="麟青砚"]既然如此，将你打晕带回去也没什么区别——
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=1, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$firestorm", volume=1)] 
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.1, block=true)]
[CameraShake(duration=3,xstrength=20, ystrength=20, vibrato=20, randomness=40, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[name="？？？"]等一下！
天空中传来一道声响，但比那声音更快的，是一道烈火。
如刃的烈火劈散雷霆，一道身影落在黎博利面前。
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(slot="m",name="avg_npc_1238_1#1$1",duration=1.5)]
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Delay(time=2)]
[name="“老天师”"]年纪轻轻，这一手雷法还挺有模有样的。
[charslot(slot="m",name="avg_npc_1238_1#10$1",focus="m")]
[name="“老天师”"]这源石技艺的手法还有点眼熟，难道白定山那一辈小孩也收徒弟了？
[charslot(slot="m",name="avg_1043_leizi2_1#7$1",focus="m")]
[name="麟青砚"]这样的火焰法术......
[name="麟青砚"]您该不会是——祖师？！
[charslot(slot="m",name="avg_4121_zuole_1#6$1",focus="m")]
[name="左乐"]——？！
[charslot(slot="m",name="avg_4196_reckpr_1#10$1",focus="m")]
[name="云青萍"]（这个小姑娘，不是大荒城的时候，小满姑娘的玩伴吗......）
[charslot(slot="m",name="avg_1043_leizi2_1#8$1",focus="m")]
[name="麟青砚"]天师府雷法传人......麟青砚......拜见祖师。
[charslot(slot="m",name="avg_npc_1238_1#10$1",focus="m")]
[name="“老天师”"]行了行了，又不是什么正经场合，别来这些规矩。
[name="“老天师”"]小丫头，你也来打个招呼吧。
[charslot(slot="m",name="avg_npc_1871_1#1$1",focus="m")]
[name="莫佚"]......山海众莫佚，见过老天师。
[charslot(slot="m",name="avg_4121_zuole_1#10$1",focus="m")]
[name="左乐"]（这家伙还真是山海众。）
[charslot(slot="m",name="avg_npc_1871_1#1$1",focus="m")]
[name="莫佚"]有什么好惊讶的？有机会的话去翻翻你们藏书阁最里面的那几卷书吧，要论对巨兽的研究，你们才是后来的呢。
[charslot(slot="m",name="avg_4121_zuole_1#4$1",focus="m")]
[name="左乐"]如今我只看到山海众举着巨兽的旗号，为非作歹无恶不作。
[charslot(slot="m",name="avg_npc_1871_1#9$1",focus="m")]
[name="莫佚"]别人用山海众的名号做杀人放火的事，那和我又有什么关系？我还要管别人做什么不成？
[name="莫佚"]你穿着这身漂亮制服，就能保证每一个穿这衣服的都是好人？
[charslot(slot="m",name="avg_4121_zuole_1#5$1",focus="m")]
[name="左乐"]你——
[charslot(slot="m",name="avg_npc_1238_1#8$1",focus="m")]
[name="“老天师”"]这不着调的做事方式，还有这伶牙俐齿......还真是和你们祖师爷一个样。
[charslot(slot="m",name="avg_npc_1238_1#10$1",focus="m")]
[name="“老天师”"]我本来以为这么多年都过去了，那个老木匠早就没什么传人了，没想到今天还能在这里再碰到一个。
[charslot(slot="m",name="avg_npc_1871_1#12$1",focus="m")]
[name="莫佚"]毕竟一千年前的那场狩猎和祖师他的理念相悖，他老人家晚年也的确因此心灰意冷，不再发声......
[charslot(slot="m",name="avg_npc_1871_1#3$1",focus="m")]
[name="莫佚"]但是他老人家想要制止战事的初衷，总还是有人记得的。
[charslot(slot="m",name="avg_npc_1238_1#1$1",focus="m")]
[name="“老天师”"]口气倒不小，那你说说，就在当下，你打算如何制止战事？
[charslot(slot=

... (全文28499字符)
```


## 统计

- 总字符数：203321
- 对话行数：1721


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
