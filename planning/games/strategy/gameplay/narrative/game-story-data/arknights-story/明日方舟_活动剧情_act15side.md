# 明日方舟 · 活动剧情 · act15side（20段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act15side」完整剧情脚本（20个文件，4162行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act15side
- 脚本文件数：20

### level_act15side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 1上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
客栈在尚蜀有十数个分号。不过，分号并不叫行裕，也许叫行禄，也许叫行福，而叫行裕的，只此一家。
当然也只此一家，既能见近处高楼夜景，亦能眺远方双月映湖。掌柜的选址，从来只看风景。至于什么客流，租价，那是从来不在意的。
风景好了，客人心情就好。风景好了，便是与天地同心，想不赚钱都难。
[dialog]
[Character(name="avg_322_lmlee_1#9$1",fadetime=1,block=true)]
[delay(time=1)]
[name="老鲤"]  嗯......确实是好茶，好景。
[Character(name="avg_322_lmlee_1#9$1", name2="avg_npc_294_1#8$1", focus=2)]
[name="老船夫"]  初来乍到，挑个好地方落脚。对尚蜀有个好印象。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#8$1", focus=1)]
[name="老鲤"]  行裕客栈，很古雅的名字。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  是家名店，但最早不是做餐饮这行的，不过这些年突然转了行，掌柜的有本事，做起生意来也是顺风顺水。
[name="老船夫"]  即便家大业大，老掌柜的也......
[dialog]
[character]
[Character(name="avg_npc_300_1#2$1")]
[dialog]
[characteraction(name="middle", type="move", xpos=-200, ypos=0,fadetime=1, block=true)]
[delay(time=1.5)]
[characteraction(name="middle", type="move", xpos=400, ypos=0,fadetime=2, block=true)]
[delay(time=1.5)]
[characteraction(name="middle", type="move", xpos=-200, ypos=0,fadetime=1, block=true)]
[delay(time=1.5)]
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  ......是那位忙忙碌碌的老先生？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  可不是。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  半点看不出老板模样，兢兢业业，令人心生敬佩。
[name="老鲤"]  就是不知道我那位姓梁的昔日同窗......如今在做什么。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  你自己说了嘛，兢兢业业。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  ......是个好官？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  街上随便拉个路人，擦鞋的，卖山芋的，或者出租车司机，谁提到梁大人都竖大拇指。
[Character(name="avg_322_lmlee_1#9$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  ......哈哈，那也算是他得偿所愿了，羡慕不来啊。
[Character(name="avg_322_lmlee_1#9$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  我听梁大人提起，你与他，已有十多年没见了？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  是。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  可梁大人依然选你，来送这件货物。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  没错。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#8$1", focus=2)]
[name="老船夫"]  那你俩的关系，也要竖大拇指了。
[name="老船夫"]  我没见识，看不出这东西的好坏，只是看梁大人那神色就知道，此事大意不得。
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#8$1", focus=1)]
[name="老鲤"]  哪里哪里，我可不敢与“梁大人”高攀什么关系，不过要说梁洵此人，倒确实算个朋友。
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#4$1", focus=2)]
[name="老船夫"]  朋友？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#4$1", focus=1)]
[name="老鲤"]  好朋友。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#2$1", focus=2)]
[name="老船夫"]  好朋友难得。十几年没见过了，还能当好朋友的，更难得。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#2$1", focus=1)]
[name="老鲤"]  那你呢，慎师傅？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#4$1", focus=2)]
[name="老船夫"]  我？
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#4$1", focus=1)]
[name="老鲤"]  码头渡口有那么多摆渡师傅，我偏偏上了你的船，你就不奇怪？
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  不奇怪。梁大人交代过我，那多半也交代过你。具体的，我没必要问。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  这是替梁大人从走私贩手里抢来的，费了不少功夫。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#8$1", focus=2)]
[name="老船夫"]  ......我没问，你倒也说了，憋得慌吧。
[Character(name="avg_322_lmlee_1#9$1", name2="avg_npc_294_1#8$1", focus=1)]
[name="老鲤"]  千里迢迢，实在缺个说话的伴。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#8$1", focus=1)]
[name="老鲤"]  你倒是信得过那姓梁的，明明他长了副生人勿近的冷淡嘴脸。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  哎。你信他，是因为他是你朋友，我信他，是因为他是尚蜀的父母官。
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  两位认识？
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  认识，梁大人对我们好，就认识。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  慎师傅做这行多少年了？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  记不清啦......谁掰着手指头数自个儿漂泊了多少年呢？约莫有个......二三十年？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  慎师傅也值得敬佩。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=2)]
[name="老船夫"]  船夫而已，有啥好敬佩的。这几年船都装上发动机了，再过几年，我怕我都要失业。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", focus=1)]
[name="老鲤"]  那也得靠人引航寻路，看一路天况如何。想来走水路的船夫，但凡水路长些，岁月久些，也都和天灾信使相去无几了吧。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#2$1", focus=2)]
[name="老船夫"]  ......天灾啊。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#5$1", focus=2)]
[name="老船夫"]  不常遇到，但要是遇到了，终生难忘。
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#5$1", focus=1)]
[name="老鲤"]  慎师傅遇见过天灾？
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#2$1", focus=2)]
[name="老船夫"]  遇见过，但也见过比天灾更吓人的，不过不是在江上——得了，说这些做什么。
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#4$1", focus=2)]
[name="老船夫"]  ......唔。
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#4$1", focus=1)]
[name="老鲤"]  怎么？
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_294_1#4$1", focus=2)]
[name="老船夫"]  ......稀奇，好像是外国人。
[dialog]
[character]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#2$1",fadetime=2,block=true)]
[delay(time=4)]
[Character(name="avgnew_npc_140_1#1$1")]
[name="客栈伙计"]  欸，客人两位？
[Character(name="avgnew_455_not

... (全文29339字符)
```

### level_act15side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 1下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$normalbattle_intro", key="$normalbattle_loop", volume=0.4)]
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_npc_296_1#1$1")]
[delay(time=1)]
[characteraction(name="left", type="move", xpos=-30, ypos=0,fadetime=1.5, block=true)]
[characteraction(name="right", type="move", xpos=30, ypos=0,fadetime=1.5, block=true)]
[delay(time=1)]
[characteraction(name="left", type="jump", xpos=100, ypos=0,fadetime=0.2, block=false)]
[characteraction(name="right", type="jump", xpos=-250, power=0, times=1, fadetime=0.2, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_punch",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="move", xpos=-80, ypos=0,fadetime=1, block=false)]
[characteraction(name="right", type="move", xpos=130, ypos=0,fadetime=1, block=true)]
[CameraShake(duration=0.5, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[characteraction(name="left", type="jump", xpos=160, ypos=0,fadetime=0.2, block=false)]
[characteraction(name="right", type="jump", xpos=-20, power=0, times=1, fadetime=0.2, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="move", xpos=-80, ypos=0,fadetime=0.7, block=true)]
[characteraction(name="right", type="move", xpos=200, ypos=0,fadetime=0.7, block=true)]
[delay(time=1)]
[characteraction(name="left", type="jump", xpos=50, ypos=0,fadetime=0.2, block=false)]
[characteraction(name="right", type="jump", xpos=-50, power=0, times=1, fadetime=0.2, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="move", xpos=-200, ypos=0,fadetime=1, block=false)]
[characteraction(name="right", type="move", xpos=200, ypos=0,fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_296_1#6$1")]
[name="杜小姐"]  ......嘁。
[stopmusic(fadetime=3)]
[Character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"]  嗯？怎么停下了？
[name="乌有"]  莫不是刚才我出手太重，不小心伤了姑娘？
[Character(name="avg_npc_296_1#3$1")]
[name="杜小姐"]  ......哼，会点花里胡哨的功夫，得意什么？
[name="杜小姐"]  既然已经被那江洋大盗跑了，再和你纠缠也没有什么意义，你这种——
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_296_1#1$1")]
[name="杜小姐"]  ——你叫什么？
[Character(name="avgnew_455_nothing_1#1$1")]
[name="乌有"]  乌有。
[Character(name="avg_npc_296_1#1$1")]
[name="杜小姐"]  呵，哪有贼人会自报姓名的，想必是什么江湖名号吧。
[Character(name="avgnew_455_nothing_1#2$1")]
[name="乌有"]  欸，您真聪明。
[Character(name="avg_npc_296_1#1$1")]
[name="杜小姐"]  那我要是接着追，你是不是就不打算让开了？
[Character(name="avgnew_455_nothing_1#7$1")]
[name="乌有"]  不然怎么说您聪明呢？
[Character(name="avg_npc_296_1#5$1")]
[name="杜小姐"]  ......还敢嘴硬！
[Character(name="avg_npc_305_1#1$1",name2="avg_npc_305_1#1$1",focus=1)]
[name="街头青年"]  还愣着干什么！一起上啊！
[Character(name="avg_npc_305_1#1$1")]
[name="街头青年"]  小姐！我们来帮忙了！
[dialog]
[character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="郑掌柜"]  ——慢着！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_300_1#1$1",fadetime=1.5,block=true)]
[delay(time=2)]
[Character(name="avg_npc_305_1#1$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="街头青年"]  咿......
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  咳。
[name="郑掌柜"]  这里怎么说也是客栈的地儿，二位再这么闹下去，疮痍满目，白给路人看笑话，怕是不太妥当。
[Character(name="avg_npc_296_1#7$1")]
[name="杜小姐"]  ......嘁。
[Character(name="avg_npc_300_1#5$1")]
[name="郑掌柜"]  不过，二位打得精彩，给我们这些人开了眼界，赔偿呢......我就不要了。
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  但现在还请给我一个薄面，今天就先算了吧。
[Character(name="avg_npc_296_1#3$1")]
[name="杜小姐"]  ......哼。
[Character(name="avgnew_455_nothing_1#1$1")]
[name="乌有"]  对不住了，掌柜的。事后解开误会，我们自会登门道歉。
[Character(name="avg_npc_296_1#7$1")]
[name="杜小姐"]  ......看在掌柜的面子上，这次就放过你吧。
[Character(name="avg_npc_296_1#1$1")]
[name="杜小姐"]  我不知道你们和他是什么关系，劝你们好自为之，乖乖把他交出来。
[Character(name="avg_npc_296_1#6$1")]
[name="杜小姐"]  要是包庇他，你们就都是同罪。放过你一时无妨，但尚蜀容不下你们这样的法外之徒。
[Character(name="avgnew_455_nothing_1#1$1")]
[name="乌有"]  真要是法外之徒，报警就是了，杜小姐何必私下动武呢？
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  乌有兄弟说的是，再怎么占理，也不该一言不合就动起手来。
[Character(name="avg_npc_296_1#5$1")]
[name="杜小姐"]  ......你！
[Character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"]  这位小姐。
[name="郑掌柜"]  让你的人退下吧。
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1",focus=2)]
[name="街头青年"]  小、小姐，就这么放走他......？抓着他一个，等着那个龙门人上钩——
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1",focus=1)]
[name="杜小姐"]  ......别嚷嚷。
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1", focus=1)]
[name="杜小姐"]  反正那个龙门人已经跑了，留住这一个也没多大用。
[Character(name="avg_npc_296_1#6$1",name2="avgnew_455_nothing_1#1$1", focus=1)]
[name="杜小姐"]  ......再说了，当真能留得住吗？你是不是还有什么手段没使？
[Character(name="avg_npc_296_1#6$1",name2="avgnew_455_nothing_1#7$1", focus=2)]
[name="乌有"]  没有的事，和气生财，和气生财。既然这位小姐愿意退一步，那是再好不过......
[Character(name="avg_npc_296_1#1$1",name2="avgnew_455

... (全文18495字符)
```

### level_act15side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 2上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g10_lianghouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
春寒料峭。
让人回想起了不少过去的画面，求学，经商，习武，从政。
那段岁月里，我们似乎形影不离。身边有良师益友，各怀抱负，想大展宏图。
现在呢？
青砖许久未曾打扫，虽然开春已久，仍有残雪，白如玉。
不知道门关着时，门后人在想什么。只知道门开了后，你知道的，就都是那人想让你知道的。
男人抬起头，大门吱呀作响。
[dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_295_1#1$1",fadetime=1,block=true)]
[delay(time=1.5)]
[name="不苟言笑的男子"]  ......
[dialog]
[character]
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#1$1", fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1.5)]
[character]
[Character(name="avgnew_455_nothing_1#1$1", name2="avg_1021_kroos2_1#1$1", fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1.5)]
[Character(name="avg_npc_294_1#1$1")]
[name="老船夫"]  梁大人。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#9$1",focus=2)]
[name="老鲤"]  ......梁洵，很久没见了。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#9$1",focus=1)]
[name="梁洵"]  很久不见。
[Character(name="avg_npc_295_1#8$1",name2="avg_322_lmlee_1#9$1",focus=1)]
[name="梁洵"]  一路辛苦了，鲤。
[Character(name="avg_npc_295_1#8$1",name2="avg_322_lmlee_1#10$1",focus=2)]
[name="老鲤"]  千里迢迢，很难说句不辛苦。梁大人好大的排场，就为了让我送个小物件，要我走这么远的路。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#10$1",focus=1)]
[name="梁洵"]  有空我会和你解释的。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  慎师傅，你也辛苦了，早春时分，江上游客挺多的吧？
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=2)]
[name="老船夫"]  哪里，答应了梁大人的事，我自然会优先照顾。
[name="老船夫"]  既然人已带到......我就先回码头了。
[name="老船夫"]  对了。刚才在城里起了些风波，具体的就让鲤小子告诉你吧。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  ......风波？
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=2)]
[name="老船夫"]  梁大人，您也要多多注意才是。
[name="老船夫"]  我就先走一步啦，码头那边估计缺人手，我得赶紧回去了。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  嗯，辛苦了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_npc_295_1#1$1",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  “从争山渡进入尚蜀，找一位姓慎的船夫。”
[name="老鲤"]  梁大人挺大牌面，只靠这一句话，就打发了我一个初来乍到的外乡人。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  你也不算第一次来尚蜀。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  慎师傅是什么人？
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  只是个信得过的码头师傅。一位经验老道的船夫，比什么都可信。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  有理。
[Character(name="avg_npc_295_1#1$1")]
[name="梁洵"]  不过这几位是......
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  （我才反应过来，梁大人，说的是尚蜀知府！？）
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#5$1",focus=2)]
[name="克洛丝"]  （我已经习惯你才反应过来这件事了。这算是个什么概念？）
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#5$1",focus=1)]
[name="乌有"]  （哦，就是市长！）
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#5$1",focus=2)]
[name="克洛丝"]  （......可按大炎官职，不该比魏彦吾低多了吗？）
[Character(name="avg_322_lmlee_1#1$1")]
[name="老鲤"]  这二位是我如今的......合作伙伴。
[Character(name="avgnew_455_nothing_1#7$1",name2="avg_npc_295_1#1$1",focus=1)]
[name="乌有"]  见过梁大人。在下楚......
[dialog]
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_npc_295_1#1$1",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.8)]
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_npc_295_1#1$1",focus=1)]
[delay(time=0.51)]
[name="乌有"]  乌有。
[Character(name="avg_npc_295_1#1$1",name2="avg_1021_kroos2_1#1$1",focus=2)]
[name="克洛丝"]  请叫我克洛丝，我是来自罗德岛制药公司的行动干员，如今与鲤先生是合作关系。
[name="克洛丝"]  不过这一次其实是在尚蜀偶然碰见的，总之打扰梁大人啦。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  偶然？我还以为，他们是你从龙门招来的信使......
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  如果你还记得有“信使”这个职业，你就该让信使来替你跑腿，不是我。
[Character(name="avg_npc_295_1#2$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  兹事体大，路途遥远，我不放心。
[Character(name="avg_npc_295_1#2$1",name2="avg_322_lmlee_1#5$1",focus=2)]
[name="老鲤"]  让我来就放心了？你可饶了我吧，要是遇到什么剪径贼，我怎么脱身？
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#5$1",focus=1)]
[name="梁洵"]  你如果真嫌麻烦，大可以回信拒绝我。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#8$1",focus=2)]
[name="老鲤"]  得了吧，得到那物件的机会转瞬即逝，你的信前脚刚到，那些走私贩后脚就到龙门了。
[name="老鲤"]  我哪有回信让你另请高明的时间？还不是得赶紧安排人手调查，顺便捣毁一下走私团伙的老巢？
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#2$1",focus=2)]
[name="老鲤"]  唉，幸好我家几位员工能者多劳，我才有空帮你这个忙。
[Character(name="avg_1021_kroos2_1#8$1")]
[name="克洛丝"]  （听上去像是槐琥小姐做的啊......鲤先生大概是觉得待在龙门事儿更多，索性找个借口溜走的吧......）
[Character(name="avg_npc_295_1#1$1")]
[name="梁洵"]  既然几位都是鲤的合作伙伴，那就别站在门口发呆了，快进来吧，府上还是有几间客房的。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  有幸受到尚蜀知府亲自招待，那我们便恭敬不如从命了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_npc_295_1#1$1",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_295_1#1$1")]
[name="梁洵"]  几位也请。
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_npc_295_1#1$1",focus=1)]
[name="乌有"]  ......谢过梁大人。
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#1$1",focus=1)]
[name="乌有"]  恩人，正好愁不知何处落脚呢，反正离约定的时辰还早，不如我们先休憩一会儿？
[Character(name="avg_1021_kroos2_1#2$1")]
[name="克洛丝"]  ......嗯。
[dialog]
[Character]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200

... (全文42689字符)
```

### level_act15side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 2下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
“尚蜀山峦多栈道，峰回路转现长烟。”
这块标牌突兀地杵在这里，标牌是新的，字是新的，只有标语是老的。
而山是老的，石台阶是老的，索道和人，又都是新的。
[dialog]
[Character(name="avg_322_lmlee_1#1$1",fadetime=1,block=true)]
[delay(time=1.5)]
[character]
我摸了摸头，发梢并没有像想象中那般湿成一团。无法言说的感觉正如醍醐灌顶，浸染身心。
所有清晰的关于白天的记忆都在迅速远去，可当你需要时，它们又会贴心地钻回脑海。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_322_lmlee_1#1$1",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1.5)]
[character]
我决定向上走。
我也不知道为什么要向上走。哪怕我确信此刻左脚踩右脚就能触碰天空，我也选择了一步一个台阶地向上走。
就像是响应诚意一般，又一块牌子出现在了栈道拐角。
新的牌子，新的字，如同所有刻着到此一游的景区标牌那样。
“攥江峰”。
[Character(name="avg_322_lmlee_1#1$1")]
[name="老鲤"]  攥江峰......这是哪里？
[Character(name="avg_322_lmlee_1#4$1")]
[name="老鲤"]  喂——有人吗——
[Character(name="avg_322_lmlee_1#1$1")]
[name="老鲤"]  ......
[Character(name="avg_322_lmlee_1#1$1", focus=-1)]
[name="隐隐的回音"]  喂......有人吗......
[Character(name="avg_322_lmlee_1#8$1")]
[name="老鲤"]  ......罢了，既来之则安之，既来之则安之。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g08_pavilion",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_322_lmlee_1#4$1")]
[name="老鲤"]  （......远处好像有个亭子。）
[name="老鲤"]  （怪了，我怎么记得在哪里见过......）
[Character(name="avg_npc_304_1#1$1")]
[name="扫雪的路人"]  这个点不常有人来的，你要去那个亭子那儿？
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  啊，不是......只是看看。
[name="老鲤"]  这里是......
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  攥江峰。
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  尚蜀三山十七峰之一？
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  ......是十八峰啦。
[name="扫雪的路人"]  那个亭子路很不好走的，也不知道是谁那么闲，在那儿建了个亭子。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  ......好像有人？
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  有的啊，没人要亭子做什么。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  你在这里扫雪？
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  是啊。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  山顶没什么人吧？
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  扫了雪才有人来呀。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  谁会来？
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  天知道，你不就来了？
[name="扫雪的路人"]  亭子里的人是不是在向你招手？
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="老鲤"]  ......有吗？
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="扫雪的路人"]  多留意脚下。
[name="扫雪的路人"]  雪天路滑。
[stopmusic(fadetime=3)]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g02_yanalley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_296_1#1$1")]
[name="杜小姐"]  ......都在这里了吗？
[Character(name="avg_npc_296_1#1$1",name2="avg_npc_305_1#1$1",focus=2)]
[name="街头青年"]  是啊。
[Character(name="avg_npc_305_1#1$1")]
[name="街头青年"]  师傅们不让我们掺和，大掌柜的又天天忙他的酒楼客栈，不想混吃等死的，都在这儿了。
[Character(name="avg_npc_305_1#1$1",name2="avg_npc_303_1$1",focus=2)]
[name="软弱的学徒"]  真不需要听郑......郑掌柜的，退一步行事？
[Character(name="avg_npc_305_1#1$1",name2="avg_npc_303_1$1",focus=1)]
[name="街头青年"]  啊？听他的？听他的大家一起改行当厨师啦，还学什么武艺？
[name="街头青年"]  其他地方的物流公司，哪个不是风风火火的？大掌柜宁可改行开餐厅都不乐意打破那些规矩和物流公司竞争，我看他是老糊涂了。
[Character(name="avg_npc_305_1#1$1",name2="avg_npc_303_1$1",focus=2)]
[name="软弱的学徒"]  在郑掌柜眼里，做餐饮生意也是正经买卖，可砸了招牌变成行裕物流，他是绝对不同意的......
[Character(name="avg_npc_305_1#1$1",name2="avg_npc_303_1$1",focus=1)]
[name="街头青年"]  你说为啥啊？
[Character(name="avg_npc_305_1#1$1",name2="avg_npc_303_1$1",focus=2)]
[name="软弱的学徒"]  你问我，我哪知道啊。
[Character(name="avg_npc_296_1#3$1")]
[name="杜小姐"]  郑老头这些年有多怕事，你我心知肚明。干镖局这么多年，临老了才悟过来，一辈子光得罪人了。
[Character(name="avg_npc_296_1#6$1")]
[name="杜小姐"]  再这样下去，没人砸镖局招牌，镖局也一样会完蛋。
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1",focus=2)]
[name="街头青年"]  ......但这次，是笔和朝廷有关的大生意来着？故意搞砸，会不会有问题？
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1",focus=1)]
[name="杜小姐"]  就因为是大生意我才打算这么做，本小姐自然有分寸。
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1",focus=-1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="远处的叫喊声"]  有贼！抓贼！！
[name="远处的叫喊声"]  别让他跑了！！
[Character(name="avg_npc_296_1#6$1",name2="avg_npc_305_1#1$1",focus=2)]
[name="街头青年"]  呃......杜小姐，这也是你安排的？
[Character(name="avg_npc_296_1#5$1",name2="avg_npc_305_1#1$1",focus=1)]
[name="杜小姐"]  ......当然不是！快跟去看看！
[dialog]
[character]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="25_g10_lianghouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#1$1",focus=1)]
[name="宁小姐"]  您的朋友好像都睡下了。
[Character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#1$1",focus=2)]
[name="梁洵"]  ......时候其实不早了。
[Character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#1$1",focus=1)]
[name="宁小姐"]  只是闲聊几句就到这个时辰了？
[name="宁小姐"]  ......那看戏的事？
[Character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#2$1",focus=2)]
[name="梁洵"]  再说吧，你应该先养好身

... (全文19271字符)
```

### level_act15side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 3上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_300_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="郑掌柜"]  ......东西不对。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  事情如果有这么简单，那我倒要担心梁先生挑人的眼光了。
[name="左乐"]  郑前辈，关于那个龙门来客，身份可知晓了？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  是梁洵的好友。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  有没有什么别的身份？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  虽然有几处模糊不清的线索，但至少有一事可做担保，此事与魏公绝无联系。
[Character(name="avg_npc_297_1#7$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......如此一来，家父最大的顾虑，也就不复存在了。
[name="左乐"]  想来也是，若是以龙门魏公的手段......恐怕咱们现在，也别指望安安静静喝茶了。
[Character(name="avg_npc_297_1#7$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  早年听闻过不少魏公逸闻，一直没机会去龙门一睹风采，很可惜。
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  没想到掌柜的也会对魏公此等人物感兴趣。
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  早年用刀，行走江湖。听闻魏公剑法卓绝，如此而已。
[Character(name="avg_npc_297_1#7$1",name2="avg_npc_300_1#2$1",focus=1)]
[name="左乐"]  原来是这样。魏公确实佩剑......不过剑法一事，我也只听闻过一些传闻罢了。
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_300_1#2$1",focus=1)]
[name="左乐"]  可这样的话，挑那个龙门人入局的，岂不变成了梁先生自己？
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  多半是。
[Character(name="avg_npc_297_1#2$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......嗯。那个龙门人是唯一的变数，也是梁先生唯一一枚子。
[Character(name="avg_npc_297_1#2$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  梁大人本该是我们的人。他挑选的对象，也不该骗我，不该有这一记无理手。
[Character(name="avg_npc_297_1#2$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  梁先生也是个身不由己的苦人儿。要是......唉，也没那么多要是。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  不正是因为她在尚蜀，才整出了这么多麻烦吗？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  ......三山十七峰，有仙则灵。
[name="郑掌柜"]  古时，尚蜀多梦，不仅人有梦，万物皆梦中。俗话说，众物有灵皆神仙，万语千言只一呵。
[name="郑掌柜"]  传闻千年之前，那会的大炎城镇分布，与现代大不相同，尚蜀人的祖先们正是梦见了同一个梦，才来此地安居乐业。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......尚蜀传说总是如此悠扬壮美。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  外人看是传说，本地人都觉得这是历史。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  那个医疗公司的干员......是叫克洛丝来着？
[name="左乐"]  若非郑前辈接应，我怕真会在街上被她追上，还要谢过前辈。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  先前小女操之过急，险些误事，我出手相助，算是补救，理所当然。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......罗德岛到底是个变数。掌柜怎么看？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  局外人罢了。
[Character(name="avg_npc_297_1#6$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  可他们离桌子太近了。
[Character(name="avg_npc_297_1#6$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  嗯......其实那样的身手可不多见，先前看她追逐时的动作，我心中已经有数了。 
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......大约是个什么印象？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  年纪轻轻，身经百战。
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  哦？这个身经百战，是以郑掌柜的眼光来看，还是以问霜客郑清钺的眼光来看呢？
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  都是。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=1)]
[name="左乐"]  ......郑前辈一直在看这只假盏。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  我只是在回忆......回忆那只酒盏原本的样子。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=1)]
[name="左乐"]  ......
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  ......那年过荒野，遇到了一伙贼。荒野上的人，连大炎话都听不懂，不知道是从哪里冒出来的。
[name="郑掌柜"]  他们炸翻了车队，想抢走货物，但是被镖局的同僚阻拦了。可劫匪人数众多，贼心不死，一路尾随了我们二百里地。
[name="郑掌柜"]  当时下大雨，视野模糊，灯火扑朔，那些熟悉地形的劫匪就像影子一样黏在身后。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  我们不敢反击，怕暗箭。也不敢一股脑地没命逃，怕逃不出。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......晚辈只听说，司岁台曾秘密委托名震一方的行裕镖局，押运一件奇物。中途发生了意外，那物下落不明......
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  是我的错。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=1)]
[name="左乐"]  ......我不会说什么安慰人的话语，郑前辈。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  我只是没想到，再一次遇到那么咄咄逼人的弓弩好手，竟然是在我的家乡，在城内，在一个灯火通明的夜晚，因为同一只酒盏。
[name="郑掌柜"]  实在是......一言难尽啊。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  ......后来郑前辈是如何脱险的？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  哪次？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=1)]
[name="左乐"]  啊......自然是过去那次。家父说了，晚辈年轻，缺乏眼界阅历，要多向各位前辈学习。
[name="左乐"]  既然前辈提起了话茬，那晚辈自然洗耳恭听。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  那晚啊......只是运气好。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#1$1",focus=2)]
[name="郑掌柜"]  负伤的两个好伙计，再没能挺过来，瞑目了。
[name="郑掌柜"]  镖局的规矩是“先救货，再救人”，既然做这行，就得有准备。
[name="郑掌柜"]  不过队伍里没了伤员，货也未必保得住了，倒反而能放开手脚。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_300_1#2$1",focus=2)]
[name="郑掌柜"]  那晚雨大，正好洗刀。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[Background(image="25_g11_yanroom",screenadapt="coverall",fadetime=0.2)]
[delau(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#4$1",focus=2)]
[name="老鲤"]  找到这只酒盏的主人就好？
[Characte

... (全文23095字符)
```

### level_act15side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 3下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g09_teahouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
晌午，晴，仿佛前一日的风雨欲来只是个不痛不痒的玩笑。
尚蜀三山十七峰，第二高山，是居奇山。而居奇山只有二峰，其中第二高的峰，即是泥泥峰。
泥泥峰又有二千二百二十二级台阶，本来没这么凑巧，是为了取个噱头，后来特地加算进去的。
台阶向天，穿云踱雾。愈往高处，游客越少，人踪渐薄，徒留青山。
而零星可见的身影，一眼望去，皆是挑夫。
[dialog]
[Character(name="avg_npc_303_1#1$1")]
[name="茶馆歇脚人"]  虽然比不得天岳，可当真是一座高峰啊。
[name="茶馆歇脚人"]  你说这些修不得公路的半山腰上，是怎么建起一家家茶馆凉亭的？
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="茶馆观光客"]  嗨，能怎么的，靠人力呗。
[name="茶馆观光客"]  咱们上来的时候，不是看见一个挑夫走下山去嘛？他们每天就这一趟趟的，小到干粮茶水，大到石砖青瓦，不都是挑上来的。
[name="茶馆观光客"]  听说他们一趟路要爬个好些时辰，辛苦得很。就算到了今天，有些偏僻山头啊，还是离不开挑夫......
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="茶馆歇脚人"]  就不能拉个索道，或者起个吊车之类的？
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="茶馆观光客"]  那也得先有个施工的地儿吧？
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="茶馆歇脚人"]  也对，不过我也不太明白这是怎么整的......不过他们还真了不起啊。
[name="茶馆歇脚人"]  他们应该赚挺多吧？
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="茶馆观光客"]  以前不多，不过前段时间看新闻说，尚蜀知府非常重视这些卖力气的，甚至这些茶馆的茶水都是政府掏钱免费提供的......呃？
[dialog]
[character]
[Character(name="avg_npc_302_1#1$1",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1.5)]
[name="挑山人"]  ......抱歉，让让。
[name="挑山人"]  晌午茶。
[Character(name="avgnew_npc_140_1#1$1")]
[name="茶馆伙计"]  好嘞，尚师傅。
[name="茶馆伙计"]  最近怎么样？有几天没见着你了......
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  不怎么样。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="茶馆伙计"]  做什么去了？
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  看望我儿子。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="茶馆伙计"]  啊......又到了这个时候啦......我都忙忘了。
[name="茶馆伙计"]  尚师傅早点打声招呼，我们可以陪着去的。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#5$1",focus=2)]
[name="挑山人"]  ......算了吧。
[name="挑山人"]  他喜欢清静。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#5$1",focus=1)]
[name="茶馆伙计"]  唉，都过去好多年啦......我是和你熟悉，才和你说这些话，你别介意啊。
[name="茶馆伙计"]  人总是要向前看的。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......你在替郑清钺说话？
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="茶馆伙计"]  废话，我们这家店都是郑掌柜投资的。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  拿人钱，替人说话，那我就不怨你了。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="茶馆伙计"]  也有一半是真心话。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......那我怨你一半。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="茶馆伙计"]  这么多年了，多劝你一句不多，少劝你一句不少。
[name="茶馆伙计"]  好好喝茶，好好想想。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#2$1",focus=2)]
[name="挑山人"]  ......
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="茶馆歇脚人"]  ......我们刚才在山路上，是不是看见过那人下山？
[Character(name="avg_npc_303_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="茶馆观光客"]  是、是啊？这才多久？爬回来了？
[name="茶馆观光客"]  应该是路上遇到同事，接了个力吧......不然这才半个时辰，就从半山腰到这儿走了个来回？
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[PlaySound(key="$d_avg_telephonebusy",channel="bgs", volume=0.6, loop=true, block=false, volume=0.6)]
[delay(time=0.6)]
[soundvolume(channel="bgs",volume=0,fadetime=1.5)]
[delay(time=2)]
[PlaySound(key="$transmission", volume=0.6)]
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#10$1",focus=2)]
[name="克洛丝"]  ......不行，联系不上。
[name="克洛丝"]  通讯没有反应，就说明年和夕还不在尚蜀地界......也可能他们根本没有按照行动守则行动。
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#10$1",focus=1)]
[name="乌有"]  ......恩人。
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  嗯，我知道你要说什么。
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  虽然我不是什么过目不忘的聪明人，可我要是没看错......
[name="乌有"]  鲤先生交给梁先生的那只匣子，和那位年小姐当时手里的东西，是一个图样。
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#7$1",focus=2)]
[name="克洛丝"]  果然和她们俩的突然离队有关。
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#7$1",focus=1)]
[name="乌有"]  恩人，咱们怎么办？
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  嗯......其实我也不是没有预料到这个情况。
[name="克洛丝"]  我和小炎熔说好啦，等她到了办事处，立刻联络尚蜀附近的干员来接我们。
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  呃？原来恩人早有准备？
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  我就猜到年一路上鬼鬼祟祟的，准没好事。
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  那意思是，我们果然还是先留在这里？
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  既然这么巧遇上了鲤先生，自然是要帮忙的。合同上是这么写的嘛。
[Character(name="avgnew_455_nothing_1#2$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  原来如此，恩人秉公办事，兢兢业业，令人钦佩。
[Character(name="avgnew_455_nothing_1#2$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  ......可毕竟鲤先生是个聪明人。客栈偶遇之后，他一直没开口请求罗德岛的协助，也许本来就是在暗示我们不必掺和此事。
[name="克洛丝"]  但如果事情真的和年有关......再加上那个太合和左乐说的话......
[name="克洛丝"]  总之，到时先去约定好的地点瞧瞧。虽然我想年多半不会守约，但夕不是那样的人。说不定能见她一面。
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  说的是，夕小姐应该会透露一些线索吧。
[Character(name="avgnew_455_nothing_1#1$1",name2="avg_1021_kroos2_1#10$1",focus=2)]
[name="克洛丝"]  唉。
[name="克洛丝"]  不管怎么想，有些事情也实在是——
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#10$1",focus=1)]
[name="乌有"]  ——实在

... (全文27768字符)
```

### level_act15side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 4上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我出生在离如今尚蜀百里外的村庄里，那是一处世外桃源。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="从村庄里眺望远方，能看见山。 山与山，连成一条线，那条线圈住了一片地，就叫作尚蜀。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="很小的时候，山里头发生过一次天灾。 山区很大，那朵云更大。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="天灾信使的动作很快，撤离的时候，能看见天上有火花在闪耀。 所有人都知道，这场风暴过后，尚蜀三山地界，就会变个样子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="那时候我确实很小。 大人们摇晃的背，强颜欢笑的脸，是我唯一记住的东西。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="救援队的动作很快，但所有人心里都清楚， 那些宅子、田地、一排排的果树，都会在风暴中荡然无存。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g08_pavilion",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="那时，我们路过一座山头。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="我亲眼见着山巅凉亭里有一个人。一个喝醉的人。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我看见她向天敬酒。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="我看见她，醉倒在亭中，不省人事。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="但救援队没有停留，身边大人也仿佛没有看见。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[stopmusic(fadetime=3)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_295_1#2$1",fadetime=1,block=true)]
[delay(time=1)]
[name="梁洵"]  ......黑色的酒盏。
[Character(name="avg_npc_295_1#7$1")]
[name="梁洵"]  那时，那个人用的，是否是这只酒盏呢......
[Character(name="avg_npc_295_1#2$1")]
[name="梁洵"]  ......
[Character(name="avg_npc_295_1#1$1")]
[name="梁洵"]  ......李小姐。
[dialog]
[character]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_304_1#1$1",fadetime=0.7)]
[delay(time=2)]
[name="杂役"]  在！有什么事吗？
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="梁洵"]  刚才来访的客人，记住长相了吗？
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="杂役"]  记住了......那么大块头的丰蹄老爷，想不记住都难啦。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="梁洵"]  ......你带两盒糕点，去探望一下宁小姐。
[Character(name="avg_npc_295_1#2$1",name2="avg_npc_304_1#1$1",focus=1)]
[name="梁洵"]  若是在宁小姐那儿见到了那位丰蹄老爷......回来告诉我一声。
[Character(name="avg_npc_295_1#2$1",name2="avg_npc_304_1#1$1",focus=2)]
[name="杂役"]  好，可您为啥不亲自去——呃......抱歉，我不该问哈，我这就去看看。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_npc_295_1#2$1",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_295_1#6$1")]
[name="梁洵"]  ......
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g09_teahouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  恩人，我打听好了。咱们沿着这条山路往上，就到会合的地方了。
[name="乌有"]  不过万一我们真的谁都没见着，到时候可如何是好？
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  那就只能回梁府找鲤先生，他说梁知府正委托他调查酒盏的主人，我们也去帮帮忙。
[Character(name="avgnew_455_nothing_1#10$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  ......如果那个杜小姐说的话是真的，取盏的是位大人物......那位梁知府，真的一无所知？
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  可如果从头到尾都是谋划，梁知府又何必如此麻烦，演这么大一出戏？
[Character(name="avgnew_455_nothing_1#12$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  我们也不是没见过大人物。
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="乌有"]  ......那个自称信使的少年郎？
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#11$1",focus=2)]
[name="克洛丝"]  哈哈......要是博士在，这些费脑子的事就都能丢给他了。
[Character(name="avgnew_455_nothing_1#6$1",name2="avg_1021_kroos2_1#10$1",focus=2)]
[name="克洛丝"]  唉......好想念宿舍里软乎乎的床啊。
[Charac

... (全文27359字符)
```

### level_act15side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 4下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_322_lmlee_1#6$1")]
[name="老鲤"]  今天还真是一无所获......
[Character(name="avg_322_lmlee_1#5$1")]
[name="老鲤"]  ......在龙门的侦探事务所待着的时候，不会这么麻烦的。
[Character(name="avg_322_lmlee_1#5$1", name2="avg_npc_294_1#4$1", focus=2)]
[name="老船夫"]  是梁大人给你的线索太少了？
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#4$1", focus=1)]
[name="老鲤"]  不，因为我在龙门......有很多朋友。
[name="老鲤"]  而我在尚蜀的朋友，除了那位足不出户的梁大人，就只剩您啦，慎师傅。
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#5$1", focus=2)]
[name="老船夫"]  ......唉。
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_294_1#6$1", focus=2)]
[name="老船夫"]  门口是不是站了太多人了？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_294_1#6$1", focus=1)]
[name="老鲤"]  他们可没打算藏。
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=1)]
[name="可疑的路人"]  ......喂，那个龙门人也在这儿，对......别轻举妄动，别让他们离开就行。
[name="可疑的路人"]  看好他们。
[Character(name="avg_322_lmlee_1#5$1", name2="avg_npc_294_1#6$1", focus=1)]
[name="老鲤"]  唉，我们这算是自投罗网了？
[Character(name="avg_322_lmlee_1#5$1", name2="avg_npc_294_1#6$1", focus=2)]
[name="老船夫"]  ......奇怪，他们过去再怎么风光，如今也不过开几家饭馆酒楼而已，真有这么多人能攀上关系？
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=2)]
[name="奇怪的过客"]  这周围没其他——等、等等！
[dialog]
[character]
[Character(name="avg_npc_302_1#1$1",fadetime=1.5,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=0)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="可疑的路人们"]  尚......尚师傅。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  ......
[name="挑山人"]  我来了。
[Character(name="avg_npc_294_1#4$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老船夫"]  ......
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  ......坐，请坐。喝杯茶不？
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......我打听过了。
[name="挑山人"]  有这么几个地方，人迹罕至，但有一些古时候留下来的亭子，我都替你标在地图上了。
[name="挑山人"]  至于卖酒水的地方，但凡有村落的，九成都有卖酒的铺子。硬要说，这几处都符合。
[Character(name="avg_322_lmlee_1#8$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  唔......
[Character(name="avg_npc_294_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老船夫"]  取江峰边有一处？
[Character(name="avg_npc_294_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......我是没印象。不过告诉我的老钱，非说有。
[name="挑山人"]  这些地儿，都是偏僻山路。寻常游客不会走的，要注意安全。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  原来如此，多谢尚师傅。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......那我走了。
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  尚师傅，您和门外那些人......？
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=0)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="可疑的路人们"]  ——！
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......不熟。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  走了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="avg_npc_305_1#1$1")]
[name="可疑的路人"]  怎、怎么......
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=1)]
[name="可疑的路人"]  （快去告诉掌柜的......尚师傅和这个龙门人有来往！）
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=2)]
[name="奇怪的过客"]  （那我们还堵门吗？）
[Character(name="avg_npc_305_1#1$1", name2="avg_npc_303_1#1$1", focus=1)]
[name="可疑的路人"]  （堵啥呀，先撤吧，走走走。）
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g10_lianghouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  你回了。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  徒劳无功，梁大人就别问了。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  我只是担心有贼人惦记你。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#10$1",focus=2)]
[name="老鲤"]  ......只要梁大人还惦记着贼人，贼人就不敢惦记我。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  何况，这烫手酒盏也不在我手里了，梁大人反倒该小心才是。
[Character(name="avg_npc_295_1#2$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  ......无妨。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#1$1",focus=1)]
[name="梁洵"]  袭击你的人查到了，一场误会，将你误认为偷窃文物的走私贩。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#4$1",focus=2)]
[name="老鲤"]  看来尚蜀侠风仍在啊。只是“误会”，就如此大打出手。
[Character(name="avg_npc_295_1#1$1",name2="avg_322_lmlee_1#4$1",focus=1)]
[name="梁洵"]  你就莫怪他们了。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  慎师傅，老鲤他毕竟不是本地人，这些天，恐怕都要麻烦你了。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=2)]
[name="老船夫"]  没有的事儿，听您吩咐。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  正是码头繁忙的时候，这些日子落下的工钱，我会加倍付给你。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=2)]
[name="老船夫"]  别，梁大人，咱们可是向来不谈钱的。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  可我却是不能亏待百姓的。
[name="梁洵"]  你帮过我太多了，也许以后还需要你帮我更多。
[Character(name="avg_npc_295_1#1$1",name2="avg_npc_294_1#1$1",focus=2)]
[name="老船夫"]  ......好。既然梁大人有这个心，我也就不推辞了。
[name="老船夫"]  这些时日，我都陪着鲤小子就是，尚蜀三山十七峰，挑山走水两路人，门清。
[Character(name="avg_npc_295_1#2$1",name2="avg_npc_294_1#1$1",focus=1)]
[name="梁洵"]  有劳。
[Character(name="avg_npc_295_1#2$1",name2="avg_322_lmlee_1#1$1",focus=2)]
[name="老鲤"]  ——梁洵。
[Character(name="avg_npc_295_1#1$1",name2="avg_

... (全文27988字符)
```

### level_act15side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 5上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Background(image="25_g05_mountaincity_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
山上的风，总是清爽的。
一个清爽的早晨，总是适合解决一些不清不楚的事情。
山间小镇刚起炊烟，春雪未散，一老一小，相顾无言。
只听远方一声击锣。
[dialog]
[character]
[Character(name="avg_npc_300_1#1$1",fadetime=1,block=true)]
[delay(time=2)]
[name="郑掌柜"]  等你很久了。
[dialog]
[character]
[Character(name="avg_476_blkngt_1#8$1",fadetime=1,block=true)]
[delay(time=1.5)]
[name="夜半"]  ......嘁，这家伙......阿灯，先不要轻举妄动。
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  我见过你，嗯，原来是你。
[name="郑掌柜"]  的确是出人意料，一个雷姆必拓人，一个从一开始就悄悄蛰伏在尚蜀的人。
[Character(name="avg_476_blkngt_1#1$1")]
[name="夜半"]  我可听不懂啊。
[Character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"]  ......哼。
[Character(name="avg_476_blkngt_1#11$1")]
[name="夜半"]  阿灯！
[dialog]
[character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_476_blkngt_1#4$1")]
[name="夜半"]  什——！？
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  套索？
[name="郑掌柜"]  你把这些眠兽训练得不错，如果是寻常人，此刻就该倒栽葱扎在地里了。
[Character(name="avg_476_blkngt_1#8$1")]
[name="夜半"]  （不仅能立刻发现背后的陷阱，还能稳稳把绳索踩在脚下......这老头......）
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  别担心，我不难为你一个姑娘家。
[name="郑掌柜"]  你知道你怀里的那只酒盏，是什么东西吗？
[Character(name="avg_476_blkngt_1#11$1")]
[name="夜半"]  ......我不关心，也不在乎。问太多的赏金猎人，都是新手。
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  那就要怪你自己了。
[stopmusic(fadetime=1)]
[Character(name="avg_476_blkngt_1#4$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夜半"]  别这么得意！小帽！钻头！
[dialog]
[playMusic(intro="$normal02_intro", key="$normal02_loop", volume=0.4)]
[Character(name="avg_npc_300_1#4$1")]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_avg_punch")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_476_blkngt_1#5$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="夜半"]  ——
[Character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"]  既然不知道是什么，就老老实实把东西交出来，不要白白遭人利用。
[Character(name="avg_476_blkngt_1#4$1")]
[name="夜半"]  你、你竟然对小帽——！你自找的！
[dialog]
[Character(name="avg_npc_300_1#4$1")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[delay(time=1)]
[name="郑掌柜"]  ......无头箭。
[Character(name="avg_476_blkngt_1#5$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="夜半"]  （用、用手抓住了？这个距离！？我可是才给弩换过弦的——！）
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  好。
[name="郑掌柜"]  念在你不愿意伤人性命的份上，我给你一个机会。
[name="郑掌柜"]  把这酒盏给我，然后告诉你背后的人：慎行，忌私。
[Character(name="avg_476_blkngt_1#8$1")]
[name="夜半"]  哼，你知道我背后是谁？
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  知不知道不重要，重要的是，我能在这条路上堵住你。
[Character(name="avg_476_blkngt_1#8$1")]
[name="夜半"]  ......我凭什么听你的？
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  你没得选。
[name="郑掌柜"]  你自己也许逃得掉，但你总不忍心看见，自己饲养的这些小畜生遭了殃。
[Character(name="avg_476_blkngt_1#8$1")]
[name="夜半"]  你威胁我？
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  你有些身手，可除了摆弄弓弩，也没啥功夫。
[name="郑掌柜"]  大可不必敬酒不吃吃罚酒，混江湖，是要靠眼力识人的。
[Character(name="avg_476_blkngt_1#1$1")]
[name="夜半"]  ......确实，那个人也没和我说，会有你这样的高手来碍事。
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  如果我拜托一个人去做一件危险的事，那我也多半不会全盘托出的。
[name="郑掌柜"]  外乡人，一份工作而已，何必搭上身家性命？
[name="郑掌柜"]  把盏给我，我以镖局的名义担保，那人许你多少钱财，我们双倍奉上。
[Character(name="avg_476_blkngt_1#2$1")]
[name="夜半"]  ......哈，本来就是亏本买卖，义务劳动。
[Character(name="avg_476_blkngt_1#1$1")]
[name="夜半"]  算是帮朋友忙吧。
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  朋友。
[name="郑掌柜"]  原来你这样的荒野流寇，也愿意为朋友两肋插刀。
[Character(name="avg_476_blkngt_1#11$1")]
[name="夜半"]  你好像对我们有点意见。
[Character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"]  ......没有的事。
[name="郑掌柜"]  生意做久了，贵人多了，朋友也就少了。
[Character(name="avg_476_blkngt_1#11$1")]
[name="夜半"]  那你就老老实实回去做生意。
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  是啊，山上的生意是最好做的。
[name="郑掌柜"]  这三山十七峰几百条山道，哪条道上没有供人歇脚休憩的茶馆驿站，哪条道上......没有我们的人？
[Character(name="avg_476_blkngt_1#1$1")]
[name="夜半"]  ......
[Character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"]  望姑娘知晓轻重。
[Character(name="avg_476_blkngt_1#1$1")]
[name="夜半"]  你还真不把我放在眼里。
[name="夜半"]  虽然正面开战不是我的风格，但是都被挑衅到这个份上了......对吧，小家伙们。
[Character(name="avg_476_blkngt_1#4$1")]
[name="夜半"]  （雷姆必拓语）让这个老家伙知道厉害！我们摸爬滚打这么多年，也不是吃干饭的！
[Character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"]  唉......
[name="郑掌柜"]  执迷不悟。
[Character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"]  若是如此，那就得罪——
[stopmusic(fadetime=1)]
[dialog]
[character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing2", volume=0.6)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
哪怕有第三个人站在一旁，他也绝对看不清这一步，是怎么踏上前来的。
只因为这个人擅长走路，擅长爬山。他每天抬步踏步的次数，实在是太多太多。
一声脆响，地上，青砖碎裂，身前，烟尘蒙蒙，眼旁，是一根朴素无奇的竹木扁担，微微发青。
远方，又一声击锣。
[Character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"]  ......
[Character(name="avg_476_blkngt_1#4$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夜半"]  ——怎、怎么......这个人是从哪里......啊，阿灯，别怕，钻头！快到我这里......！
[Character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"]  ......是你。
[dialog]
[characte

... (全文12486字符)
```

### level_act15side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 5下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g09_teahouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  一杯晌午茶。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="茶馆伙计"]  好，尚师傅慢坐！
[name="茶馆伙计"]  今天怎么上工这么迟？
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  一早遇见了个老熟人。
[Character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"]  什么熟人？
[Character(name="avg_322_lmlee_1#10$1",name2="avg_npc_302_1#4$1",focus=2)]
[name="挑山人"]  ......是你。
[Character(name="avg_322_lmlee_1#10$1",name2="avg_npc_302_1#4$1",focus=1)]
[name="老鲤"]  哎呀，实在没想到今天又能见到师傅您。
[Character(name="avg_322_lmlee_1#10$1",name2="avg_npc_302_1#4$1",focus=2)]
[name="挑山人"]  怎么，还在找那什么凉亭？
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#4$1",focus=1)]
[name="老鲤"]  有师傅替我划出范围，轻松不少，但我要找的，毕竟是人不是亭，还是有点难的。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#4$1",focus=2)]
[name="挑山人"]  那边坐着的，是你情人？
[Character(name="avg_npc_296_1#5$1",name2="avg_npc_302_1#4$1",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杜小姐"]  ......什！
[Character(name="avg_322_lmlee_1#5$1",name2="avg_npc_302_1#4$1",focus=1)]
[name="老鲤"]  咳，我还没那胆子......
[Character(name="avg_322_lmlee_1#5$1",name2="avg_npc_302_1#4$1",focus=2)]
[name="挑山人"]  哦，难不成是你女儿？
[Character(name="avg_322_lmlee_1#5$1",name2="avg_npc_302_1#4$1",focus=1)]
[name="老鲤"]  我哪像是为人父的样子？
[Character(name="avg_322_lmlee_1#5$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  倒也是。
[Character(name="avg_npc_296_1#5$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="杜小姐"]  喂，你刚刚说什么！我和这个龙门骗子是什么？！
[Character(name="avg_npc_296_1#5$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  一对男女，在早春的这个时间登山，多半是闲得没事。
[Character(name="avg_npc_296_1#9$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="杜小姐"]  我——
[Character(name="avgnew_npc_140_1#1$1")]
[name="茶馆伙计"]  尚师傅，晌午茶。
[Character(name="avgnew_npc_140_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  好。
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  晌午茶？这还没到晌午吧。
[Character(name="avg_322_lmlee_1#4$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  凡是在尚蜀山上行走的挑夫，都可以在山腰山脚的茶馆白喝两顿茶水。上午一顿晌午茶，下午一顿日落茶，各送些小菜。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  白喝的茶水，滋味总是不错。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  茶水罢了。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  可毕竟是在山上，山上的茶水，总是贵一些的。那既然是不要钱的，还是赚到了。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#5$1",focus=2)]
[name="挑山人"]  你倒是会算账。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#5$1",focus=1)]
[name="老鲤"]  可店家真的这么好心？都是做慈善来的？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  当然是官府掏钱补贴。
[Character(name="avg_npc_296_1#1$1",name2="avg_npc_302_1#4$1",focus=2)]
[name="挑山人"]  ......你懂？
[Character(name="avg_npc_296_1#1$1",name2="avg_npc_302_1#4$1",focus=1)]
[name="杜小姐"]  家里也是做餐饮生意的，当然懂得多点。
[Character(name="avg_npc_296_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......喔。
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_296_1#1$1", focus=1)]
[name="老鲤"]  尚蜀官府如此贴心？
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  梁大人上任之后一直如此。
[name="杜小姐"]  前几任尚蜀官员，兴建土木，开发山林，不仅让城市从百废待兴中恢复过来，而且变得更加生机勃勃。
[name="杜小姐"]  到了梁洵梁大人这儿，兴许是认为尚蜀已经修葺一新，便把重心转移到安民厚民之上......这些事，无非是其中最细末的琐事。
[Character(name="avg_322_lmlee_1#8$1", name2="avg_npc_296_1#1$1", focus=1)]
[name="老鲤"]  ......
[Character(name="avg_npc_296_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  ......年纪轻轻，懂得不少。
[Character(name="avg_npc_296_1#7$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="杜小姐"]  家父从商，耳濡目染罢了。
[Character(name="avg_npc_296_1#7$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  你有个好父亲。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  茶喝完了，我也该走了。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=1)]
[name="老鲤"]  后会有期，尚师傅。
[Character(name="avg_322_lmlee_1#1$1",name2="avg_npc_302_1#1$1",focus=2)]
[name="挑山人"]  后会有期。
[dialog]
[PlaySound(key="$d_avg_footstep_stonestep", volume=0.6)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_322_lmlee_1#1$1",name2="char_empty",fadetime=0.5)]
[delay(time=3)]
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#5$1", focus=2)]
[name="杜小姐"]  ——喂！姓鲤的，酒盏怎么会在他身上！？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#5$1", focus=1)]
[name="老鲤"]  不清楚。但他根本没有藏的意思，那么坦荡荡挂在腰上，就像是......
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  故意让人来找他似的？
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#1$1", focus=1)]
[name="老鲤"]  ......罢了，我们也喝壶茶，静观其变。
[Character(name="avg_322_lmlee_1#1$1")]
[name="老鲤"]  小二！上两壶茶，两碗烂肉面。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  我不吃。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#1$1", focus=1)]
[name="老鲤"]  我吃两碗。
[Character(name="avgnew_npc_140_1#1$1")]
[name="茶馆伙计"]  客官，这是两壶茶水，只是面要等等，今天人多。
[PlaySound(key="$d_avg_glassclink", volume=0.6)]
[Character(name="avg_322_lmlee_1#10$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="老鲤"]  多谢......
[dialog]
[character]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_spiritwhoosh", volume=0.6)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_306_1#1$1",fadetime=0.7)]
[delay(time=2)]
[name="奇妙的物件"]  嗷？
[Character(name="avg_322_lmlee_1#3$1")]
[

... (全文22311字符)
```

### level_act15side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 6上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g08_pavilion",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
再过一两个时辰，夕色便要染满青天。
三山十七峰，不知这是哪一山，又是哪一峰。
只知道山上有座亭子，亭里能一眼看遍尚蜀的今昔景色，美不胜收。
可惜如今亭子里空空荡荡，也就没人看这风景。
而紧接着，人就来了。
[dialog]
[Character(name="avgnew_2014_nian_1#1$1",fadetime=1,block=true)]
[delay(time=1.5)]
[name="年"]  就是这儿吧。
[dialog]
[character]
[Character(name="avgnew_2015_dusk_1#2$1",fadetime=1,block=true)]
[delay(time=1.5)]
[name="夕"]  ......
[Character(name="avgnew_2014_nian_1#5$1",name2="avgnew_2015_dusk_1#2$1",focus=1)]
[name="年"]  干嘛，这么不乐意见她？
[Character(name="avgnew_2014_nian_1#5$1",name2="avgnew_2015_dusk_1#5$1",focus=2)]
[name="夕"]  ......嫌她烦。
[Character(name="avgnew_2014_nian_1#8$1",name2="avgnew_2015_dusk_1#5$1",focus=1)]
[name="年"]  她又不会烦你。
[Character(name="avgnew_2014_nian_1#8$1",name2="avgnew_2015_dusk_1#2$1",focus=2)]
[name="夕"]  所以嫌她烦。
[Character(name="avgnew_2014_nian_1#1$1",name2="avgnew_2015_dusk_1#2$1",focus=1)]
[name="年"]  ......哎。
[name="年"]  怎么说也是咱们的大姐头，给点面子吧。
[Character(name="avgnew_2014_nian_1#1$1",name2="avgnew_2015_dusk_1#1$1",focus=2)]
[name="夕"]  她又不在。
[Character(name="avgnew_2014_nian_1#6$1",name2="avgnew_2015_dusk_1#1$1",focus=1)]
[name="年"]  ......是啊。怎么会不在呢？
[name="年"]  山下如此喧嚣......藏在崇山峻岭中，倒也有几分她的脾气。
[Character(name="avgnew_2014_nian_1#6$1",name2="avgnew_2015_dusk_1#5$1",focus=2)]
[name="夕"]  为什么我躲着你就要说我孤僻，她躲着你就这个态度？！
[Character(name="avgnew_2014_nian_1#8$1",name2="avgnew_2015_dusk_1#5$1",focus=1)]
[name="年"]  欸......那毕竟她又没一直躲着。
[Character(name="avgnew_2014_nian_1#1$1",name2="avgnew_2015_dusk_1#5$1",focus=1)]
[name="年"]  只是醉了乏了，寻一处横河断海之浮云，酣眠片刻，没差啦。
[Character(name="avgnew_2014_nian_1#1$1",name2="avgnew_2015_dusk_1#3$1",focus=2)]
[name="夕"]  啧，差别对待。
[Character(name="avgnew_2014_nian_1#5$1",name2="avgnew_2015_dusk_1#3$1",focus=1)]
[name="年"]  哪有。
[Character(name="avgnew_2014_nian_1#5$1",name2="avgnew_2015_dusk_1#2$1",focus=2)]
[name="夕"]  但愿她别整出什么事儿来。
[name="夕"]  她半醉半梦半醒，我们倒要被那群人找麻烦。
[Character(name="avgnew_2014_nian_1#6$1",name2="avgnew_2015_dusk_1#2$1",focus=1)]
[name="年"]  ......真亏她还能睡得着啊。她真的还能睡得着吗？
[name="年"]  你说她的梦里有什么呢？
[Character(name="avgnew_2014_nian_1#6$1",name2="avgnew_2015_dusk_1#5$1",focus=2)]
[name="夕"]  ......不知道，别问我。
[name="夕"]  ......
[Character(name="avgnew_2014_nian_1#6$1",name2="avgnew_2015_dusk_1#2$1",focus=2)]
[name="夕"]  天知道她神游何时何地，反正觉得无聊了，自己就会回来吧。
[Character(name="avgnew_2014_nian_1#6$1",name2="avgnew_2015_dusk_1#2$1",focus=1)]
[name="年"]  我听说这处山峰本来应该被毁了才是。
[Character(name="avgnew_2014_nian_1#8$1",name2="avgnew_2015_dusk_1#2$1",focus=1)]
[name="年"]  不知道克洛丝和乌有小哥，要花多久才能找到此处山巅呢。
[stopmusic(fadetime=3)]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_300_1#2$1",fadetime=1,block=true)]
[delay(time=1)]
[name="郑掌柜"]  ......唉。
[Character(name="avg_npc_300_1#2$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  掌柜的，您这是？
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  该来的麻烦总要来。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  ......遇着姓尚的了？
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  嗯。盏被他抢了。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[name="客栈伙计"]  这个混账！怎么这么一根筋呢——！
[Character(name="avg_npc_300_1#2$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  算了，一笔糊涂账。
[dialog]
[Character(name="avg_npc_300_1#2$1")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_bldwhoosh", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_300_1#2$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[name="客栈伙计"]  嚯，好刀总是不容易生锈的。
[name="客栈伙计"]  掌柜的，多少年没见您拔刀了。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  刀剑无情，还是用来砍瓜切菜的好。
[name="郑掌柜"]  可我要是想让夜儿顺顺当当地接我的班，尚冢的事，是终究要解决的。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  尚老儿虽然糊涂，也不是那种嚷嚷着父债子偿去针对大小姐的窝囊。
[name="客栈伙计"]  掌柜的，您还是自个儿过不去，对不对？
[Character(name="avg_npc_300_1#2$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  ......谁能过得去呢。
[name="郑掌柜"]  一场大雨，两条人命。他的儿子因为我的失误而死，对我有怨，我无话可说。
[name="郑掌柜"]  我比谁都知道他这些年怎么过来的。
[Character(name="avg_npc_300_1#2$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  掌柜的......
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  放心吧，起码酒盏还是要抢回来的。
[name="郑掌柜"]  不抢回来，没法交差。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g05_mountaincity_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_294_1#1$1",name2="avg_1021_kroos2_1#8$1",focus=2)]
[name="克洛丝"]  慎师傅，就没什么快点上山的法子吗？
[Character(name="avg_npc_294_1#9$1",name2="avg_1021_kroos2_1#8$1",focus=1)]
[name="老船夫"]  有倒是有，但是对于没怎么走过山路的人来说，恐怕......
[Character(name="avg_npc_294_1#9$1",name2="avg_1021_kroos2_1#1$1",focus=2)]
[name="克洛丝"]  没关系的，我习惯了。
[Character(name="avg_npc_294_1#1$1",name2="avg_1021_kroos2_1#1$1",focus=1)]
[name="老船夫"]  ......那好。这边。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_npc_306_1#1$1", name2="avg_npc_296_1#1$1", focus=1)]
[name="器伥"]  嗷——！
[dialog]
[Character(name="avg_npc_306_1#1$1",name2="avg_npc_296_1#1$1")]
[characteraction(name="right", type="jump", xpos=-100, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake

... (全文19842字符)
```

### level_act15side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 6下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_305_1#1$1")]
[name="街头青年"]  ......没看到掌柜的？
[Character(name="avg_npc_305_1#1$1",name2="avgnew_npc_140_1#2$1",focus=2)]
[name="客栈伙计"]  没看到。
[Character(name="avg_npc_305_1#1$1",name2="avgnew_npc_140_1#2$1",focus=1)]
[name="街头青年"]  咋回事，哪家店都找不到掌柜的，终于想通了，回家享清福了？
[Character(name="avg_npc_305_1#1$1",name2="avgnew_npc_140_1#2$1",focus=2)]
[name="客栈伙计"]  但愿吧。
[Character(name="avg_npc_305_1#1$1",name2="avgnew_npc_140_1#2$1",focus=1)]
[name="街头青年"]  ......咋了刘二，心情不好？
[Character(name="avg_npc_305_1#1$1",name2="avgnew_npc_140_1#2$1",focus=2)]
[name="客栈伙计"]  好，好得很。
[name="客栈伙计"]  怎么不好？
[stopmusic(fadetime=1.5)]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[PlaySound(key="$rungeneral", volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[playsound(key="$d_avg_rockfall", volume=0.6)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=0.4)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$d_avg_punch")] 
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$d_avg_axehitscrape", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_302_1#4$1")]
[name="挑山人"]  ——你这身手，土石法术？
[Character(name="avg_npc_299_1#1$1")]
[name="太合"]  正是。
[name="太合"]  只可惜你一身功夫，却不知善用。
[Character(name="avg_npc_302_1#6$1")]
[name="挑山人"]  你方才飞沙裹手，打裂我的扁担，这是什么鬼掌法？
[Character(name="avg_npc_299_1#4$1")]
[name="太合"]  ......吃我一掌，只是微微寸裂，如此扁担，反倒稀奇，有何来历？
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  ......我用的只是寻常青竹扁担。
[Character(name="avg_npc_299_1#6$1")]
[name="太合"]  那我使的便是毫无章法之掌法。
[Character(name="avg_npc_302_1#5$1")]
[name="挑山人"]  ......你叫什么？
[Character(name="avg_npc_299_1#1$1")]
[name="太合"]  太合。
[Character(name="avg_npc_302_1#5$1")]
[name="挑山人"]  好，了不起。
[name="挑山人"]  能在最后和你这样的高手过上两招，不亏。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  你是当官的吧，告诉我，你们在做的事，这只酒盏的事，是在图谋什么？
[Character(name="avg_npc_299_1#1$1")]
[name="太合"]  谋天下万世昌宁。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  ......哈哈，好大口气！
[name="挑山人"]  只可惜，这东西还是不能给你们。
[Character(name="avg_npc_299_1#1$1")]
[name="太合"]  你逃无可逃。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  未必。
[Character(name="avg_npc_299_1#5$1", name2="avg_npc_302_1#1$1", focus=1)]
[name="太合"]  ——想走！？
[dialog]
[StopMusic(fadetime=3)]
[Character(name="avg_npc_299_1#1$1", name2="avg_npc_302_1#5$1", focus=0)]
[characteraction(name="right", type="jump", xpos=60, power=20, times=1, fadetime=0.5,block=false)]
[delay(time=1)]
挑山人向后跃出一步。
十年登山，千百万步中的一步。
风筝断线，风起而身动。
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_299_1#3$1")]
[name="太合"]  ......唔，你方才藏了身法？
[Character(name="avg_npc_302_1#5$1")]
[name="挑山人"]  在山上，你追不上我。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"]  太合，告诉那个小子，取江峰峰顶，忘水坪。
[name="挑山人"]  莫忘了。
[dialog]
[characteraction(name="middle", type="move", ypos=200, fadetime=0.8, block=false)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_299_1#2$1")]
[name="太合"]  ......
[delay(time=0.6)]
[dialog]
[character]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.5)]
[Character(name="avg_npc_297_1#3$1",fadetime=1,block=true)]
[delay(time=1)]
[name="左乐"]  ......太合叔！
[Character(name="avg_npc_297_1#4$1")]
[name="左乐"]  没追上？
[Character(name="avg_npc_297_1#4$1",name2="avg_npc_299_1#2$1",focus=2)]
[name="太合"]  若舍身相追，并非难事。只是......
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_299_1#2$1",focus=1)]
[name="左乐"]  他要以酒盏为威胁，逼郑掌柜与他相见。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_299_1#1$1",focus=2)]
[name="太合"]  峰顶忘水坪，二者相见，必死其一。
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_299_1#1$1",focus=1)]
[name="左乐"]  ......没有余地？
[Character(name="avg_npc_297_1#1$1",name2="avg_npc_299_1#5$1",focus=2)]
[name="太合"]  方才交手，知根知底，绝无余地。
[Character(name="avg_npc_297_1#6$1",name2="avg_npc_299_1#5$1",focus=1)]
[name="左乐"]  ......峰顶忘水坪是吧。
[name="左乐"]  得抢占先机。
[dialog]
[Character(name="avg_npc_297_1#6$1", name2="avg_npc_299_1#5$1", focus=0)]
[PlaySound(key="$rungeneral", volume=0.5)]
[characteraction(name="right", type="move", xpos=800, fadetime=2.5,block=false)]
[character(name="avg_npc_297_1#6$1",name2="char_empty",fadetime=0.5)]
[characteraction(name="left", type="move", xpos=600, fadetime=2.5,block=false)]
[character(name="char_empty",name2="char_empty",fadetime=0.5)]
[delay(time=1.55)]
[character]
[delay(time=3)]
[Character(name="avg_322_lmlee_1#5$1",fadetime=1,block=true)]
[PlaySound(key="$d_avg_footstep_stonestep", volume=0.6)]
[delay(time=1.5)]
[name="老鲤"]  ......幸好没和那个挑山人起什么冲突，看那身手，都让我想起十几年前最后一次见到槐天裴的时候了。
[Character(name="avg_npc_296_1#6$1")]
[name="杜小姐"]  ......
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#6$1", focus=1)]
[name="老鲤"]  你认识那两个人，对吧。
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#6$1", focus=2)]
[name="杜小姐"]  ......我说过，爹是领了朝廷密令，那两个人，就是朝廷的信使。
[Character(

... (全文15653字符)
```

### level_act15side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]07上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g07_fairyland_2",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
......唔。
头疼头疼......何事如此喧哗......嗯？
啊......原来是落子声响，叮叮当当。
棋罢不知人换世，梦醒只道是何年......何年......何年......
呃......
......怎么酒又没了。
这都是何苦呢。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Character]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[character(name="avg_npc_302_1#1$1",fadetime=1.5)]
[delay(time=2)]
尚冢摸了摸脖子上的膏药，这是他的习惯。
十年如一日地挑起扁担，上山下山，这也是他的习惯。
取江峰确实很高，很险。高到没有人烟，险到万籁俱寂。
数不清这是在尚蜀看见的第几个春天，他抬头远眺，只见人踪尽灭的山道那头，有一个人。
一个他等了很久的人。
[dialog]
[delay(time=1)]
[name="挑山人"] ......我们终于还是再见了。
[character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"] 方才见过。
[character(name="avg_npc_302_1#6$1")]
[name="挑山人"] 那时你没有带刀，就不算见过。 
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 那现在我带刀来了。
[character(name="avg_npc_302_1#2$1")]
[name="挑山人"] ......话先说明了。
[character(name="avg_npc_302_1#4$1")]
[name="挑山人"] 我知道错不在你。我也知道，那个雨夜，死的不止是我的儿子。
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 你当然知道。
[character(name="avg_npc_302_1#2$1")]
[name="挑山人"] 你收养了他的女儿，她现在怎么样了？
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] ......我打算让她接我的班。
[character(name="avg_npc_302_1#6$1")]
[name="挑山人"] 是打算接镖局的班，还是像你这些年做的，安安分分当个老板娘？
[character(name="avg_npc_300_1#5$1")]
[name="郑掌柜"] 都行，看她喜欢。
[character(name="avg_npc_302_1#5$1")]
[name="挑山人"] 找着心上人没？
[character(name="avg_npc_300_1#5$1")]
[name="郑掌柜"] 没呢。
[character(name="avg_npc_302_1#1$1")]
[name="挑山人"] 可惜了。
[character(name="avg_npc_302_1#3$1")]
[name="挑山人"] 你活不到看她出嫁的那天。
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] ......也许今天我们不用打打杀杀的呢？
[character(name="avg_npc_302_1#3$1")]
[name="挑山人"] 不可能，我知道你的为人，你心里有愧，但我心里有怨。
[character(name="avg_npc_302_1#1$1")]
[name="挑山人"] 怨了十年。
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] ......所以呢？
[character(name="avg_npc_302_1#1$1")]
[name="挑山人"] 所以你一开始就没打算今天赢我。酒楼茶馆客栈，哪一个不都是为了给你的女儿留条退路？
[name="挑山人"] 你知道镖局是个得罪人的行当。你也知道，如果你不在了，镖局会是什么样。
[character(name="avg_npc_300_1#6$1")]
[name="郑掌柜"] 别忘了，你挂刀而去，不守规矩，于情，大家体谅你，可于理，你还是个叛徒。
[character(name="avg_npc_302_1#3$1")]
[name="挑山人"] 那夜之后，你若是背负着那些罪过，带领镖局继续前行，我又怎么会叛出镖局！？
[name="挑山人"] 我儿走镖，也是有所觉悟的，我何尝不知？可你的行为，开客栈开餐厅，难道不是践踏他们的死吗？
[name="挑山人"] 是你！一蹶不振，逃避过去！
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 是啊......我是知道的，但咱们话说得有点多了。
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] 行裕镖局总镖头，问霜客，郑清钺。
[dialog]
[characteraction(name="middle", type="move", xpos=150, fadetime=1, block=false)]
[delay(time=2)]
[character]
[character(name="avg_npc_302_1#1$1")]
[name="挑山人"] ......尚家棍，尚冢。
[dialog]
[characteraction(name="middle", type="move", xpos=-150, fadetime=1, block=false)]
[delay(time=2)]
[character]
早春，垂暮，树影婆娑，落雪如银。
一阵风起，一把刀落。
[dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing6", volume=0.6,delay=0.6)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing3", volume=0.6,delay=0.6)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_300_1#4$1", name2="avg_npc_302_1#1$1",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_300_1#2$1", name2="avg_npc_302_1#1$1", focus=1)]
[name="郑掌柜"] ......唔。
[Character(name="avg_npc_300_1#2$1", name2="avg_npc_302_1#6$1", focus=2)]
[name="挑山人"] 你实在是歇息得太久了，郑清钺。
[Character(name="avg_npc_300_1#1$1", name2="avg_npc_302_1#6$1", focus=1)]
[name="郑掌柜"] ......未必是我歇息得久了，也许是你爬山爬得太多，步法又精进了。
[Character(name="avg_npc_300_1#1$1", name2="avg_npc_302_1#2$1", focus=2)]
[name="挑山人"] 谁知道。
[Character(name="avg_npc_300_1#2$1", name2="avg_npc_302_1#2$1", focus=1)]
[name="郑掌柜"] 可你这样的英雄好汉，下半辈子却注定无法行走，也实在可惜。
[Character(name="avg_npc_300_1#2$1", name2="avg_npc_302_1#6$1", focus=2)]
[name="挑山人"] ......只是刀势太快，雪光晃眼，被你稍微擦破裤腿，我就无法行走了？
[Character(name="avg_npc_300_1#4$1", name2="avg_npc_302_1#6$1", focus=1)]
[name="郑掌柜"] 下一刀，你挡不住。你拿的，毕竟不是家传的宝棍。只是根破木棍罢了。
[Character(name="avg_npc_300_1#4$1", name2="avg_npc_302_1#1$1", focus=2)]
[name="挑山人"] ......
[Character(name="avg_npc_300_1#4$1", name2="avg_npc_302_1#1$1", focus=1)]
[name="郑掌柜"] ......
[dialog]
[character]
[playsound(key="$rungeneral")]
[character(name="avg_npc_296_1#5$1",fadetime=1.5)]
[delay(time=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杜小姐"] ——爹！
[Character(name="avg_npc_300_1#3$1", name2="avg_npc_302_1#1$1", focus=1)]
[name="郑掌柜"] 夜儿！？你怎么......
[Character(name="avg_npc_300_1#3$1", name2="avg_npc_302_1#4$1", focus=2)]
[name="挑山人"] ......你果然是杜遥夜。转眼间，已经长这么大了......
[Character(name="avg_npc_300_1#3$1", name2="avg_npc_302_1#2$1", focus=2)]
[name="挑山人"] 唔。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_322_lmlee_1#9$1",fadetime=1.5)]
[delay(time=2)]
[name="老鲤"] 二位好闲情，天色渐晚，还有空在这......比武练习。
[Character(name="avg_npc_302_1#4$1")]
[name="挑山人"] 是你。你在这里做什么？
[character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"] 不瞒尚师傅你说，你腰间那只盏，是我一朋友托我寻来的。我要找亭子，也和那只酒盏分不开呀。
[character(name="avg_322_lmlee_1#4$1")]
[name="老鲤"] 我怕刀剑无眼，二位切磋之间......误碰了酒盏，得不偿失。
[Character(name="avg_npc_302_1#1$1")]
[name="挑山人"] ......
[Character(name="av

... (全文22218字符)
```

### level_act15side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]07下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
[playsound(key="$rungeneral")]
[character(name="avg_322_lmlee_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="老鲤"] ......到哪儿去了......
[Dialog]
[Character]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[playsound(key="$d_avg_spiritwhoosh")]
[character(name="avg_npc_306_1#1$1",fadetime=1.5)]
[delay(time=2)]
[playsound(key="$d_avg_monsterroar")]
[name="器伥"] 嗷嗷！
[Dialog]
[Character]
[playsound(key="$d_avg_spiritwhoosh")]
[character(name="avg_npc_306_1#1$1", name2="avg_npc_306_1#1$1", fadetime=1.5)]
[delay(time=2)]
[character(name="avg_322_lmlee_1#5$1")]
[name="老鲤"] 唔。
[name="老鲤"] 在那边的树杈上......而且还聚起了这么一大批古灵精怪......
[character(name="avg_npc_306_1#1$1")]
[name="器伥"] 嗷......
[character(name="avg_322_lmlee_1#8$1")]
[name="老鲤"] ......哈哈，这下我要怎么取来呢......
[Dialog]
[playsound(key="$d_avg_spiritwhoosh")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="25_g07_fairyland_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
一枚黑子。
万物皆有所待，这些器伥的脾性，是和这些器物的“意”相通的。
那么，扰我清静的......
是我那摆弄画卷泼墨江山的妹妹呢，还是那一字千金口含天宪的妹妹呢？
又或者......
只是他一子拍下，砸起的片刻杂音呢？
[Dialog]
[playsound(key="$d_avg_spiritwhoosh")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[character(name="avg_322_lmlee_1#3$1",blackstart=0.2,blackend=0.7,fadetime=1.5)]
[delay(time=2)]
[name="老鲤？"] ......让开。
[character(name="avg_npc_306_1#1$1")]
[name="器伥"] ——！
[name="器伥"] 呜——呜呜！
[Dialog]
[delay(time=0.7)]
[playsound(key="$d_avg_spiritwhoosh")]
[characteraction(name="middle", type="move", xpos=300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[character(name="avg_322_lmlee_1#1$1",blackstart=0.2,blackend=0.7)]
[name="老鲤？"] ......
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n")]
[character(name="avgnew_2014_nian_1#7$1",fadetime=1.5)]
[delay(time=2)]
[name="年"] ......好久不见。
[character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"] ......嗯？您应该是......罗德岛的......
[character(name="avgnew_2014_nian_1#1$1")]
[name="年"] 啊啊。原来是老鲤啊。
[character(name="avgnew_2014_nian_1#7$1")]
[name="年"] 好久不见，怎么从龙门来尚蜀了？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="街头青年"] 哎，你说掌柜的抽刀而走，是不是找谁干架去了？
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"] 谁知道。
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="街头青年"] 我们这些新来的，已经不见掌柜的用刀啦。想来也是，家大业大的，光靠酒楼就能在尚蜀站稳脚跟了吧。
[name="街头青年"] 掌柜的到底怎么用刀？
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"] 掌柜的这些年，用刀的次数实在不多。真要说，那就是砍瓜切菜，剁肉杀鳞。
[name="客栈伙计"] 比起过去打打杀杀的日子，郑掌柜已经很久不以“伤人”为目的用刀了。
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="街头青年"] ......有一种江湖高人隐退的感觉？那现在他带刀出去做啥？
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"] 切菜吧。切了这么久的菜了，掌柜的也就会切切菜了。
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="街头青年"] 无聊哦。
[Character(name="avg_npc_303_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"] 那咋的，切那么多年菜，还能变厉害不成？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing2", volume=0.6)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing3", volume=0.6)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[character(name="avg_npc_302_1#5$1",fadetime=1.5)]
[delay(time=2)]
[name="挑山人"] 好刀法！看来你这几年不光是在当一个掌柜的！
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] ......不，我确实没有再用过刀了。
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] 习惯了持筹握算，柴米油盐......我也没想到，这把霜刀如今还能如此顺手。
[character(name="avg_npc_300_1#5$1")]
[name="郑掌柜"] 意料之外。
[character(name="avg_npc_302_1#5$1")]
[name="挑山人"] ......我还在想，要是遇到的是一个郁郁寡欢的郑清钺，打赢了又怎样，输了又怎样？
[character(name="avg_npc_302_1#2$1")]
[name="挑山人"] 看来是天意如此。
[Dialog]
[character]
[Character(name="avg_npc_296_1#6$1",fadetime=0.7)]
[delay(time=1)]
[name="杜小姐"] ——什么天意，不过是你一厢情愿想要报仇罢了吧！
[character(name="avg_npc_302_1#3$1")]
[name="挑山人"] 唔......！
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] 夜儿！你别插手！快去追那个龙门人，找到酒盏！
[Character(name="avg_npc_296_1#2$1")]
[name="杜小姐"] 抱歉了爹，这件事你可做不了主——
[dialog]
[character(name="avg_npc_300_1#4$1")]
[PlaySound(key="$fightgeneral",volume=0.6)] 
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[dialog]
[Character(name="avg_npc_296_1#1$3")]
[name="杜小姐"] 呃！
[dialog]
[character(fadetime=1.5)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=2)] 
[character(name="avg_npc_302_1#6$1")]
[name="挑山人"] 我就猜到会这样。
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] ......我从来没打过她。
[name="郑掌柜"] 你会后悔的。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0

... (全文17218字符)
```

### level_act15side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]07下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g02_yanalley_n",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_301_1#1$1",blackstart=0.2,blackend=0.7,fadetime=1,block=true)]
[delay(time=1.5)]
[name="路过的老人"] ......年轻人。
[Character(name="avg_npc_303_1#1$1")]
[name="街头青年"] 嗯？
[Character(name="avg_npc_301_1#1$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=1)]
[name="路过的老人"] 请问尚蜀知府梁大人的梁府，怎么走？
[Character(name="avg_npc_301_1#1$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=2)]
[name="街头青年"] 啊啊......就在这附近来着，前面右转走到底，看到个牌坊，左转就是梁府。
[Character(name="avg_npc_301_1#4$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=1)]
[name="路过的老人"] 宽敞吗？
[Character(name="avg_npc_301_1#4$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=2)]
[name="街头青年"] 谁知道，我又进不去。
[name="街头青年"] 不过从外面看上去......好像和其他地方没啥区别，反而显得有点寒酸。
[Character(name="avg_npc_301_1#4$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=1)]
[name="路过的老人"] 牌坊上写的什么？
[Character(name="avg_npc_301_1#4$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=2)]
[name="街头青年"] 谁记得。
[Character(name="avg_npc_301_1#5$1",blackstart=0.2,blackend=0.7,name2="avg_npc_303_1#1$1",focus=1)]
[name="路过的老人"] ......谢谢了。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[Character(name="avg_npc_303_1#1$1")]
[name="街头青年"] 喂，老头。
[name="街头青年"] 天都要黑了，要不要我带个路啊？怕你路上出车祸哎。
[Character(name="avg_npc_301_1#5$1",blackstart=0.2,blackend=0.7)]
[name="路过的老人"] ......不必了。
[name="路过的老人"] 我看得见路。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$fightgeneral",volume=0.6)] 
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral",volume=0.6)] 
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$rockhit",volume=1)]
[PlaySound(key="$d_sp_ballista",volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[delay(time=1)]
[character(name="avgnew_455_nothing_1#4$1",fadetime=1.5)]
[Delay(time=2)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="乌有"] ——呃！
[name="乌有"] （脚......陷进石块里了！？）
[Dialog]
[Character]
[Character(name="avg_npc_299_1#1$1",fadetime=1.5,block=true)]
[delay(time=2)]
[name="太合"] 到此为止。
[name="太合"] 三十三招，了不起。
[character(name="avgnew_455_nothing_1#8$1",name2="avg_npc_299_1#1$1",focus=1)]
[name="乌有"] ......你压根没动真格的吧。
[character(name="avgnew_455_nothing_1#8$1",name2="avg_npc_299_1#1$1",focus=2)]
[name="太合"] 你若是有意投身军伍，必然大有可为。
[character(name="avgnew_455_nothing_1#7$1",name2="avg_npc_299_1#1$1",focus=1)]
[name="乌有"] 哈哈......我离开勾吴城的时候确实想过这样做，不过俗话说得好，饭要一口口吃，我还是得先还了罗德岛的恩情。
[character(name="avgnew_455_nothing_1#7$1",name2="avg_npc_299_1#1$1",focus=2)]
[name="太合"] ......知恩图报，难得。
[name="太合"] 可惜你如今寸步难行。
[character(name="avgnew_455_nothing_1#12$1",name2="avg_npc_299_1#1$1",focus=1)]
[name="乌有"] ......这倒是字面意思。
[character(name="avgnew_455_nothing_1#10$1")]
[name="乌有"] （把腿打折有机会拉出来吗......试试看吧......）
[Character(name="avg_npc_299_1#5$1")]
[name="太合"] 郑清钺，我来助阵！
[character(name="avgnew_455_nothing_1#4$1")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="乌有"] 别想走！
[character(name="avg_npc_299_1#3$1")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="太合"] ——！
[character]
[Dialog]
[character(name="avgnew_455_nothing_1#4$1")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fan", volume=1)]
[PlaySound(key="$swordtsing6", volume=0.6)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[character(name="avgnew_455_nothing_1#4$1")]
[name="乌有"] 哈......哈......
[character(name="avgnew_455_nothing_1#4$1",name2="avg_npc_299_1#3$1",focus=2)]
[name="太合"] ......你......
[name="太合"] ......
[name="太合"] 我把这场乱斗视作闹剧，并未上心。
[name="太合"] 但你告诉我，是我错了。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]	
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[PlaySound(key="$swordtsing2", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=20, ystrength=22, vibrato=50, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[character(name="avg_npc_300_1#4$1")]
[name="郑掌柜"] ......
[chara

... (全文40721字符)
```

### level_act15side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]07上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g01_yanstreet_d",screenadapt="coverall")]
[delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
[Character(name="avg_npc_303_1#1$1")]
[name="街头青年"] 怎么回事？在打雷吗？
[Character(name="avg_npc_304_1#1$1")]
[name="逛街的路人"] 好像山那头在打雷啊，最近的天气是怎么了......
[Character(name="avg_npc_304_1#1$1")]
[name="逛街的路人"] 嗯？山上是不是有什么东西......？
[Character(name="avg_npc_303_1#1$1")]
[name="街头青年"] 啊？这谁看得清啊？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_plankroad",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_299_1#2$1")]
[name="太合"] ......
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 我们在这里，待了有两三日了吧。
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 若是再找不到出去的办法，岂不是......
[Character(name="avg_npc_299_1#2$1")]
[name="太合"] 静待即可。
[character(name="avgnew_455_nothing_1#1$1")]
[name="乌有"] 哈哈......指不定哪天外头那位夕小姐心情好，就把咱们放出去了呢。
[character(name="avgnew_455_nothing_1#1$1")]
[name="乌有"] 不过，那位挑夫老先生呢？
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] ......他儿子葬在山上，他不想在这种地方和我碰面。
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 二位的恩怨我也听说了......只是......一定要以这种方式做个了断吗？
[character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"] 不然呢？
[character(name="avgnew_455_nothing_1#5$1")]
[name="乌有"] 我只是觉得......
[character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"] 你就莫要觉得了。
[character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"] 旁人总以为自己什么都看得明白，但人与人之间的共情终归是有限的。
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 我心里也清楚怎么做才对，什么叫“有必要”什么叫“没有必要”。大道理嘛，谁都懂。
[character(name="avg_npc_300_1#2$1")]
[name="郑掌柜"] 只是偶尔，人情还是不讲道理的。
[dialog]
[character]
[PlaySound(key="$d_avg_lightrain_loop", volume=0.5, delay=0.4, loop=true, fadetime=2,channel="bgs")]
[delay(time=1)]
[character(name="avg_npc_294_1#4$1")]
[name="老船夫"] ......下雨了。
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] ......
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 唉，我们就这么干等着，也不是个事。
[Character(name="avg_npc_143#1")]
[name="墨魉"] 嘎......
[character(name="avgnew_455_nothing_1#7$1")]
[name="乌有"] ......不然各位也试试养一只墨魉？我发现这小东西，你心平气和待它，它还挺可爱的......
[Character(name="avg_npc_143#1")]
[name="墨魉"] 嘎......？
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] ......由此可见，司岁台警戒其人，不无道理。
[character(name="avgnew_455_nothing_1#7$1")]
[name="乌有"] 好了好了，在这里争这个也没啥意义......不然还是进屋避雨？
[character(name="avg_npc_300_1#1$1")]
[name="郑掌柜"] 这地儿也会下雨，稀奇。
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 掉下来的居然不是墨水，确实稀奇。
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 太合先生？真不进来？
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] ......
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 那慎师傅呢？
[character(name="avg_npc_294_1#5$1")]
[name="老船夫"] ......
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 慎师傅在做什么？刚才开始，他就低头看着手心......
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] ......你在看雨？
[character(name="avg_npc_294_1#5$1")]
[name="老船夫"] ......是啊。
[character(name="avg_npc_294_1#5$1")]
[name="老船夫"] 听乌有所说，这一方天地，不过是那人画卷之物。处处雕琢，栩栩如生。
[character(name="avg_npc_294_1#2$1")]
[name="老船夫"] 日出时，羽出山林，雾蒙大地，见天光而不见大日，映影楼层千百栋，悄无声息。
[character(name="avg_npc_294_1#2$1")]
[name="老船夫"] 若是画，不知道这个画家，究竟从大炎山水之中，看到了什么......
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] 雨师好雅兴。
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] 只知道浮萍雨师慎楼曾从军十载，殊不知还略通文采风骚？
[character(name="avg_npc_294_1#8$1")]
[name="老船夫"] ......唉。日子过多了而已。
[character(name="avg_npc_294_1#2$1")]
[name="老船夫"] 只可惜，早春的雨水，不该是这个温度。
[character(name="avg_npc_294_1#1$1")]
[name="老船夫"] 去，破开。
[PlaySound(key="$tactfulboost", volume=1)]
[Dialog]
[StopSound(channel="bgs", fadetime=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.6, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[character(name="avgnew_455_nothing_1#6$1")]
[name="乌有"] 呃......！？
[character(name="avg_npc_300_1#3$1")]
[name="郑掌柜"] 这、这是？
[Character(name="avg_npc_299_1#1$1")]
[name="太合"] ......雨师高明。
[character(name="avg_npc_294_1#8$1")]
[name="老船夫"] 只是误打误撞罢了。
[character(name="avg_npc_300_1#3$1")]
[name="郑掌柜"] 尚冢。
[dialog]
[character]
[character(name="avg_npc_302_1#4$1",fadetime=1,block=true)]
[delay(time=1)]
[name="挑山人"] ......这就是，你们要争抢那只酒盏的目的？
[name="挑山人"] 山上云海翻滚，那里又有什么？
[Dialog]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="25_g07_fairyland_1",screenadapt="coverall")]
[Character]
[playMusic(intro="$duskdragon_intro", key="$duskdragon_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[character]
[dialog]
[PlaySound(key="$tactfulboost", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=20, ystrength=22, vibrato=50, randomness=90, fadeout=true, block=true)]
[character]
[dialog]
[PlaySound(key="$tactfulboost", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=20, ystrength=22, vibrato=50, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[CameraShake(duration=3, xstrength=50, ystrength=50, vibrato=60, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_gen_explo_n", volume=1)]
[PlaySound(key="$d_gen_explo_n", volume=1,delay=0.05)]
[PlaySound(key="$d_gen_explo_n", volume=1,delay=0.1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=2)]
[CameraShake(duration=2, xstrengt

... (全文35911字符)
```

### level_act15side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act15side/IW01.mp4")]
```

### level_act15side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 纯1
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="爹，墙上为什么挂着把刀？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="那是爹年轻时候讨饭吃的伙计。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="爹，那为什么刀下面还有个空架子？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="那是留给一个老前辈的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="老前辈人呢？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="和爹闹掰了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="为什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="因为......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.51)]
[stopmusic(fadetime=3)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="25_g01_yanstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
清晨时分，多云天气。 
[dialog] 
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g04_yaninn",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
大炎尚蜀，应峰路，有一家客栈。
大炎如今，还叫客栈的店，多也不多。
不过这里古色古香，好酒好茶，有尚蜀最好的风情在。
红色的牌匾，金色的字。
“行裕”。
[dialog]
[Character(name="avg_npc_300_1#1$1",fadetime=2,block=true)]
[delay(time=3)]
[name="掌柜模样的人"]  湖松酒十坛，云辽酒三坛，归行老酒六坛......嗯......
[name="掌柜模样的人"]  刘二，你这儿的业绩，怎么比渡口那边少了这么多？
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[name="客栈伙计"]  这您不能怪我啊，渡口那儿月初不知怎么的，热热闹闹地办了好几次宴，卖得比咱们这好不是理所当然的吗！
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="掌柜模样的人"]  摆几次席，能差多少？
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[name="客栈伙计"]  哎哟喂，您别站着说话不腰疼。
[name="客栈伙计"]  您那几天不在尚蜀，是不知道那排场有多夸张......说那是开张吃半年，一点都不过分啊。
[name="客栈伙计"]  再说了，前几个月分明是咱们业绩更好，就这两天翻了船。郑大掌柜，您可不能拉偏架啊。
[name="客栈伙计"]  要知道咱们这家门店，可是最早做起来，最早做火的。其他店铺——要我说啊——见着咱都得喊一声老汉儿。
[name="客栈伙计"]  您可不能搞隔代亲，有了孙子忘了儿啊。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  哭丧什么，谁是你老汉儿？我还什么都没说呢。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  真等您说出口，那不就全完喽。
[name="客栈伙计"]  我就是运气不好，没碰上那几个贵人......
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  那怎么不见你运气好一回？
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  唉！贵人贵人，哪来这么多贵人......
[name="客栈伙计"]  咱们一直都靠的老主顾捧场，广告也不肯打，哪怕请几个漂亮姑娘帅小伙也好啊......
[Character(name="avg_npc_300_1#4$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  （瞪）......
[Character(name="avg_npc_300_1#4$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="客栈伙计"]  我啥也没说。刚才那是在放屁呢。
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  开酒楼客栈，凭的是贵人，靠的是关系，这话是不假。可你又怎么知道谁是贵人，谁不是呢？
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#1$1", focus=2)]
[name="客栈伙计"]  我要是什么都懂，我也当掌柜啦。
[Character(name="avg_npc_300_1#5$1", name2="avgnew_npc_140_1#1$1", focus=1)]
[name="郑掌柜"]  那就好好学着。
[name="郑掌柜"]  有钱有势有牌面的爷，是个明眼人都看得出来，哪轮得到你这不开窍的？
[Character(name="avg_npc_300_1#5$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[name="客栈伙计"]  呃......
[Character(name="avg_npc_300_1#1$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  走江湖也好，在城里安家立业也好，只要人活着，少不了和别人打交道。
[name="郑掌柜"]  只要打交道，就少不得一双眼。识人，识事，咱们才有今天的好日子。
[Character(name="avg_npc_300_1#2$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  整天办灯儿，打烊就去麻将馆，你能有什么出息......
[Character(name="avg_npc_300_1#4$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  ......
[Character(name="avg_npc_300_1#4$1", name2="avgnew_npc_140_1#2$1", focus=2)]
[name="客栈伙计"]  ......咋不骂了？
[Character(name="avg_npc_300_1#4$1", name2="avgnew_npc_140_1#2$1", focus=1)]
[name="郑掌柜"]  没见门前有俩客人吗！还不快去迎客！
[Character(name="avgnew_npc_140_1#2$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="客栈伙计"]  哎哟......我还真没看见，快快，里边请！本日头两位客人，送盐花生两碟，菊花茶一壶！
[dialog]
[charact

... (全文13769字符)
```

### level_act15side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 纯2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="25_g11_yanroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="天将亮。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="我突然意识到，自从来了尚蜀，还从未睡过一个好觉。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="门外动静很大。似是有两个人打了起来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="但我知道，他们打起来，并非因为对方。 他们打起来，是为了我，和那只盏。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="我自认看人看事向来不差。我也猜到，这件事不会这么简单。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="我的预感也是向来不差的。所以我备了两封信，就在桌上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_322_lmlee_1#1$1")]
[name="老鲤"]  ......还是别麻烦我们梁大人了。
[name="老鲤"]  不过我倒好奇了，这梁府莫非是想来就来想走就走的地儿？梁洵再怎么不摆官架子，这也太疏忽了些吧。
[name="老鲤"]  唉......
[stopmusic(fadetime=2)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="25_g10_lianghouse",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_296_1#5$1")]
[name="杜小姐"]  别跑！
[Character(name="avg_476_blkngt_1#4$1")]
[name="风尘仆仆的女性"]  （雷姆必拓语）啧，这家伙可不在说好的名单上......！
[dialog]
[PlaySound(key="$rungeneral", volume=0.6)]
[character(fadetime=2,block=true)]
[delay(time=2)]
[dialog]
[Character(name="avg_476_blkngt_1#4$1", name2="char_empty")]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_476_blkngt_1#4$1", name2="avg_npc_296_1#6$1",fadetime=0.7)]
[delay(time=2)]
[Character(name="avg_476_blkngt_1#4$1", name2="avg_npc_296_1#6$1",focus=2)]
[name="杜小姐"]  ......哼，你跑不了的。
[name="杜小姐"]  你是谁派来的！？
[Character(name="avg_476_blkngt_1#8$1", name2="avg_npc_296_1#6$1", focus=1)]
[name="风尘仆仆的女性"]  ......
[Character(name="avg_476_blkngt_1#8$1", name2="avg_npc_296_1#5$1", focus=2)]
[name="杜小姐"]  ......不对，你根本不是大炎人！你来自哪儿？
[dialog]
[character]
[Character(name="avg_322_lmlee_1#4$1",fadetime=1.5,block=true)]
[delay(time=2)]
[name="老鲤"]  ......怎么了？
[Character(name="avg_322_lmlee_1#4$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  我还以为你睡死过去了。
[Character(name="avg_476_blkngt_1#8$1", name2="avg_322_lmlee_1#4$1", focus=2)]
[name="老鲤"]  你是......
[name="老鲤"]  （这些野兽，长吻眠兽？）
[Character(name="avg_476_blkngt_1#1$1", name2="avg_322_lmlee_1#1$1", focus=1)]
[name="风尘仆仆的女性"]  ......
[Character(name="avg_322_lmlee_1#1$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  这个人分明在你的屋外盘算什么，她能是什么善茬？
[Character(name="avg_476_blkngt_1#4$1")]
[name="风尘仆仆的女性"]  （雷姆必拓语）既然都被发现了，干脆一不做二不休......
[Character(name="avg_476_blkngt_1#4$1", name2="avg_322_lmlee_1#1$1", focus=2)]
[name="老鲤"]  呃，这位雷姆必拓来的小姐可别这么着急......
[name="老鲤"]  这里是尚蜀知府的地盘，我倒是无所谓，只怕真把官差惹来，你不好对付。
[Character(name="avg_476_blkngt_1#5$1", name2="avg_322_lmlee_1#1$1", focus=1)]
[name="风尘仆仆的女性"]  （雷姆必拓语）......你听得懂？
[Character(name="avg_476_blkngt_1#1$1", name2="avg_322_lmlee_1#1$1", focus=2)]
[name="老鲤"]  略懂。
[name="老鲤"]  不知姑娘尊姓大名？如此冒昧来访，又是为了什么？
[Character(name="avg_476_blkngt_1#2$1", name2="avg_322_lmlee_1#1$1", focus=1)]
[name="风尘仆仆的女性"]  ......
[Character(name="avg_476_blkngt_1#1$1", name2="avg_322_lmlee_1#1$1", focus=1)]
[name="夜半"]  夜半。
[Character(name="avg_476_blkngt_1#1$1", name2="avg_npc_296_1#5$1", focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="杜小姐"]  你会说大炎话干嘛不搭理人！？
[Character(name="avg_476_blkngt_1#1$1", name2="avg_322_lmlee_1#4$1", focus=2)]
[name="老鲤"]  雷姆必拓人，却有个大炎名字？
[Character(name="avg_476_blkngt_1#2$1", name2="avg_322_lmlee_1#4$1", focus=1)]
[name="夜半"]  这不关键。虽然我很少遇到这种情况，不过在这座城市里，我也不太想自找麻烦。
[name="夜半"]  一次没有陷阱和预谋的狩猎，实在是太容易失败了。
[Character(name="avg_476_blkngt_1#2$1", name2="avg_npc_296_1#1$1", focus=2)]
[name="杜小姐"]  死心吧，有本小姐在，你有什么阴谋诡计，那都是不成的。
[Character(name="avg_322_lmlee_1#10$1", name2="avg_npc_296_1#1$1", focus=1)]
[name="老鲤"]  ......杜小姐倒是性情中人。
[Character(name="avg_476_blkngt_1#4$1", name2="avg_322_lmlee_1#10$1", focus=1)]
[name="夜半"]  ......原来你们是一伙的。
[Character(name="avg_476_blkngt_1#8$1")]
[name="夜半"]  不过正好，你们把注意力放在我身上了......
[Character(name="avg_476_blkngt_1#4$1")]
[name="夜半"]  阿灯，钻头！
[dialog]
[character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="不远处的兽鸣"]  嗷——！
[Character(name="avg_322_lmlee_1#3$1")]
[name="老鲤"]  （还有其他眠兽！）
[Character(name="avg_npc_296_1#5$1")]
[name="杜小姐"]  啧！它嘴里叼着的是那只酒盏！
[Character(name="avg_476_blkngt_1#8$1")]
[name="夜半"]  后会无期！
[dialog]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=1,block=false)]
[Character(fadetime=0.5)]
[delay(time=1.5)]
[Character(name="avg_npc_296_1#5$1")]
[name="杜小姐"]  你给我站住！！
[Character(name="avg_322_lmlee_1#8$1", name2="avg_npc_296_1#5$1", focus=2)]
[name="杜小姐"]  喂，你还愣着做什么，快追啊！
[Character(name="avg_322_lmlee_1#8$1", name2="avg_npc_296_1#5$1", focus=1)]
[name="老鲤"]  ......长吻眠兽可不会在大炎栖息，更别提驯服那么多只眠兽一同作案了。这家伙多半是从其他地方一路追来的。
[Character(name="avg_322_lmlee_1#2$1", name2="avg_npc_296_1#5$1", focus=1)]
[name="老鲤"]  ......嗯......
[Character(name="avg_322_lmlee_1#2$1", name2="avg_npc_296_1#5$1", focus=2)]
[name="杜小姐"]  你在想什么？要不是本小姐帮忙，你刚才可是差点被她布陷阱杀了欸！
[Character(name="avg_322_lm

... (全文38814字符)
```

### level_act15side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]07下
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="25_g06_mountainroad_d",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
[character(name="avg_2023_ling_1#8$1")]
[name="令"] 罗德岛之后有什么打算？
[Character(name="avg_1021_kroos2_1#2$1")]
[name="克洛丝"]  啊......欸......嗯？我有做过自我介绍吗？
[character(name="avg_2023_ling_1#8$1")]
[name="令"] 你又是什么打算？
[character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"] 我总算了了这桩事，当然是回去问那个高高挂起的梁大人......好好算算账。
[character(name="avg_2023_ling_1#8$1")]
[name="令"] 嗯。
[name="令"] 也许他说得对，你和我们的缘分，还不止于此。
[character(name="avg_2023_ling_1#1$1")]
[name="令"] 只是......
[Character(name="avg_1021_kroos2_1#2$1")]
[name="克洛丝"]  惊蛰小姐是怎么......
[Character(name="avg_npc_039_1")]
[name="惊蛰"] ......偶然从师兄弟口中得知灰齐山的事情，立刻赶到了尚蜀。
[name="惊蛰"] 虽然来迟一步，但不算为时已晚。
[Character(name="avg_1021_kroos2_1#2$1")]
[name="克洛丝"]  ......好吧。
[character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"] 令小姐。
[character(name="avg_2023_ling_1#1$1")]
[name="令"] 嗯？
[character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"] 我有一个问题。
[name="老鲤"] 你们这样的存在，是怎么分辨......呃，长幼的？
[character(name="avg_2023_ling_1#2$1")]
[name="令"] ......长幼之分啊。
[name="令"] 在一片混沌鸿蒙之中，谁最先找到那个答案，谁就能先立于人间。
[character(name="avg_322_lmlee_1#7$1")]
[name="老鲤"] 什么答案？
[character(name="avg_2023_ling_1#8$1")]
[name="令"] 一个简单到不行的问题......
[character(name="avg_2023_ling_1#8$1")]
[name="令"] ......“我是谁”。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[Background(image="25_g10_lianghouse",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]	
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_298_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="宁小姐"] ......太合先生，左乐先生。幸会。
[Character(name="avg_npc_297_1#1$1", name2="avg_npc_299_1#1$1", focus=1)]
[name="左乐"] 宁小姐，幸会。
[Character(name="avg_npc_297_1#1$1", name2="avg_npc_299_1#1$1", focus=2)]
[name="太合"] 见过宁侍郎。
[character(name="avg_npc_295_1#5$1")]
[name="梁洵"] ......
[character(name="avg_npc_298_1#9$1")]
[name="宁小姐"] 尚蜀之行，未能礼待，失了礼数。
[character(name="avg_npc_297_1#7$1")]
[name="左乐"] 不请自来，多有打扰，冒犯在先。
[character(name="avg_npc_298_1#10$1")]
[name="宁小姐"] 左公子是承父命而来，代表司岁台处理酒盏与灰齐山两案，雷厉风行。
[character(name="avg_npc_297_1#5$1")]
[name="左乐"] 宁小姐慧眼如炬。
[character(name="avg_npc_297_1#10$1")]
[name="左乐"] 而梁先生举动，旨在破局，更是令人钦佩。
[character(name="avg_npc_298_1#6$1")]
[name="宁小姐"] ......若非司岁台激进，梁大人想必不至于如此举动。
[character(name="avg_npc_295_1#7$1")]
[name="梁洵"] 梁某人问心无愧，想必肃政院得知此事后，自有公道。
[character(name="avg_npc_299_1#1$1")]
[name="太合"] 我已草拟奏呈，大可开诚布公，绝无偏颇。
[character(name="avg_npc_295_1#10$1")]
[name="梁洵"] ......如太合先生所说，“取忠舍义”。
[character(name="avg_npc_299_1#2$1")]
[name="太合"] 不错。
[character(name="avg_npc_298_1#7$1")]
[name="宁小姐"] 可司岁台此次越俎代庖，无论太傅如何定夺，我都会如实禀告尚书大人。
[character(name="avg_npc_297_1#5$1")]
[name="左乐"] 本就该如此。
[character]
[name="？？？"] 不必了。
[Dialog]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1.5, block=true)]
[Background]
[Image(image="25_i08",x=-25,xScale=1, yScale=1, fadetime=0)]
[ImageTween(xFrom=-25, xTo=25, duration=20, block=false)]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="太傅"] 左乐。
[name="左乐"] 在......在！
[name="太傅"] 依你推演，若三人岁相流窜人间，为害尚蜀，以当时局势，你需要多久镇压局面？
[name="太傅"] 又若是岁兽苏醒，大炎备以一城迎战，代价如何？
[name="左乐"] ......前者需三日工夫，后者恐两败俱伤，巨兽死，而军队十不存三。
[name="太傅"] 梁洵。
[name="梁洵"] 在。
[name="太傅"] 若是今日判你身死，以保礼部与司岁台平安，你如何做？
[name="梁洵"] 理当服法。
[name="太傅"] 那如果你今日作为，阴差阳错，导致尚蜀城市受损，百姓蒙受损害，你如何做？
[name="梁洵"] 苟求生路，亡兽补牢。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[image]
[Background(image="25_g10_lianghouse",screenadapt="coverall")]
[character(name="avg_npc_301_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[name="太傅"] 棋局至此，五五之间。
[name="太傅"] 梁洵挑选的那个龙门人，本是一记出奇无理手，却被他抓住了什么蛛丝马迹，棋差一筹。
[name="太傅"] 事已至此，又有多少事在他算计之中？又有多少他没算到的事情，终归还是有利于他？
[character(name="avg_npc_298_1#7$1")]
[name="宁小姐"] ......太傅果然知晓此事。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 梁洵，替你知府职位之人，一月内抵达尚蜀。做好交接，随我离开。
[character(name="avg_npc_298_1#4$1")]
[name="宁小姐"] ......！
[character(name="avg_npc_295_1#4$1")]
[name="梁洵"] 梁某人......不知太傅用意。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 随我入京。
[character(name="avg_npc_298_1#6$1")]
[name="宁小姐"] ......
[character(name="avg_npc_295_1#7$1")]
[name="梁洵"] ......谢过太傅。
[character(name="avg_npc_295_1#4$1")]
[name="梁洵"] 可梁某人还是......
[character(name="avg_npc_298_1#7$1")]
[name="宁小姐"] ——宁辞秋祝贺梁大人高升。
[character(name="avg_npc_295_1#4$1")]
[name="梁洵"] ......我......
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] ......宁侍郎。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 玉门已从既定航线归国。昨日与龙门接触，准备补给。
[character(name="avg_npc_297_1#1$1")]
[name="左乐"] ——！
[character(name="avg_npc_298_1#7$1")]
[name="宁小姐"] 玉门城......是躲避天灾？还是......
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 另有用途。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 你先一步前往玉门。我与梁洵在京城事了，自会前往。
[character(name="avg_npc_298_1#7$1")]
[name="宁小姐"] ......！明白。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 太合。
[character(name="avg_npc_299_1#1$1")]
[name="太合"] 诸事顺遂。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 好。
[character(name="avg_npc_297_1#1$1")]
[name="左乐"] ......太合叔，原来早就......
[character(name="avg_npc_299_1#1$1")]
[name="太合"] “取忠舍义”，公子莫怪。
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 司岁台此次失误，先不予追究。眼下，确定那一百八十一枚黑子落向何处，才是关键。
[character(name="avg_npc_297_1#1$1")]
[name="左乐"] ......明白。
[character(name="avg_npc_298_1#8$1")]
[name="宁小姐"] 太傅何日离开尚蜀？
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 明晚。
[character(name="avg_npc_298_1#1$1")]
[name="宁小姐"] ......这么着急，不需要等待信使队伍护送......
[character(name="avg_npc_301_1#1$1")]
[name="太傅"] 不必。
[character(name="avg_npc_298_1#6$1")]
[name="宁小姐"] 白天师有意为太傅送行。
[character(name="avg_npc_301_1#1$

... (全文25713字符)
```


## 统计

- 总字符数：480895
- 对话行数：4162


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
