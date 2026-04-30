# 明日方舟 · 活动剧情 · act42side（31段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act42side」完整剧情脚本（31个文件，4794行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act42side
- 脚本文件数：31

### level_act42side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Image(image="39_i14",block=false,screenadapt="coverall",fadetime=0)]
[Delay(time=1)]
[PlaySound(key="$alarmenter", volume=0.6, loop=true, channel="1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1", multi = true, text="危机。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="重复警告。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n危机。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n......危机等级......评估中......",block = true)]
[Sticker(id="st1", multi = true, text="\n\n不可知......",block = true)]
[Sticker(id="st1", multi = true, text="\n\n解除锁定。",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="底层运算区域锁定解除。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n推演算力已突破上限。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n拉特兰......爆发。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n......",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[stopsound(channel="1",fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="26_g2_laterano_cathedralhall",screenadapt="showall")]
[Delay(time=3)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_361_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]哎呀，终于能喘口气了。
[charslot(slot="m",name="avg_npc_361_1#7$1",focus="m")]
[name="薇尔丽芙"]这辈子都没有说过这么多的话，一想到明天又要再说一辈子的话......
[Dialog]
[charslot]
[name="？？？"]哈哈，要不我们交换一下工作？
[name="？？？"]接待卡兹戴尔使节团的任务交给我，至于明天抵达的那十三座移动修道院，你来负责安置，怎么样？
[name="？？？"]跑来跑去对骨质疏松的老头子来说太不友好了！
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]那倒是不用，帕特里奇昂阁下。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="帕特里奇昂"]和我们的萨卡兹友人沟通还顺利吗？
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]不赖。
[charslot(slot="m",name="avg_npc_361_1#2$1",focus="m")]
[name="薇尔丽芙"]确实还有萨卡兹无法放下仇恨，比如跟随那位维什戴尔议长的古老魂灵，只是远远瞥见牧首的身影就暴跳如雷。
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]好在议长很识时务地把他们训斥得哑口无言，态度好到我都要怀疑关于她的奇妙传闻是怎么来的了。
[name="薇尔丽芙"]卡兹戴尔使节团的主要发言人是那位名叫弗莱蒙特的巫妖，可惜您没看见那场面——
[charslot(slot="m",name="avg_npc_361_1#2$1",focus="m")]
[name="薇尔丽芙"]整整三小时的外交辩论，从政治到律法，从信仰到生死，他一个人和第一厅、第六厅的十七位枢机激烈地“交换意见”......
[name="薇尔丽芙"]结束之后，口干舌燥的枢机们围着甜品机海饮番石榴汁。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]这样有活力的老家伙，真是令人神往啊！
[charslot(slot="m",name="avg_npc_361_1#1$1",focus="m")]
[name="薇尔丽芙"]总之，结论是，卡兹戴尔认同了我们的倡议——诸王庭会重新审视传承已久的王权，萨卡兹将在拉特兰的协调下团结一体。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]就在刚刚，我与女皇之声也碰了面——莱塔尼亚的使节团明天清晨就会抵达圣城。
[charslot(slot="m",name="avg_npc_361_1#7$1",focus="m")]
[name="薇尔丽芙"]哦？稀奇事。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]想想两年前，万国峰会应者寥寥，绝大多数人都认为所谓的“拉特兰主张”只是一纸空泛的解经。
[name="帕特里奇昂"]当时，伊维格娜德女皇拒绝了我们的邀请，而这次，她主动请求参加万国峰会。
[name="帕特里奇昂"]甚至已经沉寂许久的赫琳玛特女皇也现身了，这次将一同到访拉特兰......
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]莱塔尼亚的诚意很足啊。
[name="薇尔丽芙"]帕特里奇昂阁下，我们是否可以认为，第二届万国峰会已经取得了预期中的成功？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]远超预期，薇尔丽芙枢机。
[name="帕特里奇昂"]目前为止，哥伦比亚、乌萨斯、炎国，甚至是远海的阿戈尔......该来的都来了。
[charslot(slot="m",name="avg_npc_361_1#2$1",focus="m")]
[name="薇尔丽芙"]感觉像在做梦。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]这只不过是拉特兰长久发展的必然结果。
[name="帕特里奇昂"]启示中的灾异已经临近，萨米冰盖上的黑雪、莱塔尼亚上空的罅隙，甚至冲击海岸的狂潮，都是在呼应它必然的降临。
[name="帕特里奇昂"]灾异当头，任何人都会渴望秩序——拉特兰的秩序。
[charslot(slot="m",name="avg_npc_361_1#1$1",focus="m")]
[name="薇尔丽芙"]您说得是。只不过，哪怕做了这么久的准备，这场面也还是让我感到......陌生。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]你尚且如此，其他人就更不必说了。哪怕启蒙时就在布道中无数次听过拉特兰为应对启示中的灾异所铺设的道路......
[name="帕特里奇昂"]真到了亲自迎接它所导向的结果时，也还是会有所犹疑。
[charslot(slot="m",name="avg_npc_361_1#7$1",focus="m")]
[name="薇尔丽芙"]您自己呢？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]虽然不想倚老卖老，但到了我这个年纪，哪还有什么犹疑的余地呢？
[charslot(slot="m",name="avg_npc_361_1#4$1",focus="m")]
[name="薇尔丽芙"]您准备退休了？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]是啊。我老到连仙人掌挞都嚼不动啦，协助举办这届峰会恐怕就是我能为拉特兰做的最后一件事了。
[charslot(slot="m",name="avg_npc_361_1#2$1",focus="m")]
[name="薇尔丽芙"]阁下，我觉得这是您口味太过奇异的缘故。您说的那种......仙人掌挞，恐怕我也很难咬动。
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]您不会不知道，冷餐会上的仙人掌挞都是专门为您订制的吧？毕竟拉特兰城没有第二个人痴迷这种怪东西了。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]怎么可能？仙人掌挞是一个甜品鉴赏造诣极高的老朋友倾情推荐的......呃，他叫什么来着......
[name="帕特里奇昂"]算了，言归正传。
[name="帕特里奇昂"]既然还有人心存疑虑，之后将在育婴圣堂举办的那场仪式就至关重要。
[name="帕特里奇昂"]我们需要以最有力的方式向所有人展示，拉特兰能带来怎样的可能性。
[charslot(slot="m",name="avg_npc_361_1#1$1",focus="m")]
[name="薇尔丽芙"]明白。我马上交接第七厅的工作，万国峰会接下来的这段时间，我会前往圣堂，确保仪式顺利进行。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]倒也不用那么急。
[name="帕特里奇昂"]哈哈，算了。嘴上有再多抱怨，真行动起来又都是急性子......年轻人还真是相像。
[charslot(slot="m",name="avg_npc_361_1#5$1",focus="m")]
[name="薇尔丽芙"]您想起了您的“小菲”吧？
[charslot(slot="m",name="avg_npc_361_1#6$1",focus="m")]
[name="薇尔丽芙"]根据任务调遣记录——她已经回来了？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]是啊，明天是我们的家庭聚会......希望小菲喜欢我准备的礼物。
[Dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_aircraftalarm", volume=0.2, loop=true, channel="1")]
[Delay(time

... (全文18274字符)
```

### level_act42side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g11_laterano_alley",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1811_1#8$2",duration=1.5)]
[delay(time=2.5)]
[name="蕾缪安"]几个路口都查过了吗？
[charslot(slot="m",name="avg_npc_366_1#1$1",focus="m")]
[name="七厅调查员"]嗯，并未发现可疑人员。
[name="七厅调查员"]我们也在附近询问了可能目击到异常的公民，没什么有价值的线索。
[charslot(slot="m",name="avg_npc_1811_1#5$2",focus="m")]
[name="蕾缪安"]......
[name="蕾缪安"]天气太潮湿的话，柱子上可能会长蘑菇，但再怎么样都不会自己长炸弹的，对吧？
[charslot(slot="m",name="avg_npc_366_1#1$1",focus="m")]
[name="七厅调查员"]但......怎么可能？
[name="七厅调查员"]除非是教皇厅或育婴圣堂的公职人员，否则持有任何爆炸物，都意味着要受到公证所的实时监督。
[name="七厅调查员"]别说爆炸，拉特兰都多少年没出现过一声计划之外的铳响了？
[Dialog]
[charslot(slot="m",name="avg_npc_1811_1#5$2",focus="m")]
[delay(time=1.5)]
[charslot(slot="m",posfrom="0,0",posto="0,-20",duration=1.5,focus="m")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1811_1#5$2",focus="none")]
蕾缪安蹲下身子，从已经半毁的石柱里取出了一块炸弹的碎片。
[Dialog]
[charslot(slot="m",posfrom="0,-20",posto="0,0",duration=1.5,focus="m")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1811_1#5$2",focus="m")]
[name="蕾缪安"]结构很精巧......这种类型的炸弹，如果填装的是常规爆破物，受损的不可能只有这根柱子。
[charslot(slot="m",name="avg_npc_366_1#1$1",focus="m")]
[name="七厅调查员"]您是说......自制的？为了什么，恶作剧？
[charslot(slot="m",name="avg_npc_1811_1#5$2",focus="m")]
[name="蕾缪安"]拉特兰热武装管控名录是由教皇厅最资深的爆破专家编撰的，几乎所有能产生有效爆炸的材料都被考虑进去了。
[name="蕾缪安"]要用名录之外的材料拼凑出这样一枚炸弹，恐怕要费上不少力气。没人会为一时兴起的恶作剧做到这个地步。
[charslot(slot="m",name="avg_npc_1811_1#11$2",focus="m")]
[name="蕾缪安"]更何况，现在正值第二届万国峰会，如此特殊的时间点......
[Dialog]
[charslot(slot="m",name="avg_npc_1811_1#11$2",focus="none")]
蕾缪安又想起了那一抹红色，她有些不安，但更多的是疑惑。
[charslot(slot="m",name="avg_npc_1811_1#14$2",focus="m")]
[name="蕾缪安"]将约维塔街，不，整个司提望区近期人口流动的相关文件给我看看。
[charslot(slot="m",name="avg_npc_366_1#1$1",focus="m")]
[name="七厅调查员"]......
[charslot(slot="m",name="avg_npc_1811_1#8$2",focus="m")]
[name="蕾缪安"]怎么了？
[name="蕾缪安"]这些明显派得上用场的资料，在我们得到命令的同时，就应该有人负责及时调取才对啊。
[Dialog]
[charslot(slot="m",name="avg_npc_1811_1#8$2",focus="none")]
[CameraShake(duration=0.3, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]在这里在这里！
[Dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=0.4)]
[charslot(slot="m",name="avg_npc_1783_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="？？？"]（捶胸）呼——呼——
[name="？？？"]实在是抱歉，蕾缪安枢机，这是您刚刚要的资料。
[name="阿摩斯"]我是第七厅调查员阿摩斯，今后将担任您的枢机辅佐官。
[charslot(slot="m",name="avg_npc_1811_1#5$2",focus="m")]
[name="蕾缪安"]......
[charslot(slot="m",name="avg_npc_1811_1#2$2",focus="m")]
[name="蕾缪安"]你迟到了，阿摩斯辅佐官。
[charslot(slot="m",name="avg_npc_1811_1#8$2",focus="m")]
[name="蕾缪安"]按照帕特里奇昂阁下的说法，你会在我到达现场后的十分钟内赶来增援......但现在已经过去将近半小时了。
[charslot(slot="m",name="avg_npc_1783_1#4$1",focus="m")]
[name="阿摩斯"]抱歉抱歉，我本来在准备欢迎会的茶点。我以为事情没那么急......
[charslot(slot="m",name="avg_npc_1811_1#8$2",focus="m")]
[name="蕾缪安"]（嘘——）
[charslot(slot="m",name="avg_npc_1811_1#13$2",focus="m")]
[name="蕾缪安"]第七厅既然委派你当我的辅佐官，你应该对我有所耳闻吧？
[charslot(slot="m",name="avg_npc_1783_1#4$1",focus="m")]
[name="阿摩斯"]噤、噤声的蕾缪安......
[charslot(slot="m",name="avg_npc_1811_1#2$2",focus="m")]
[name="蕾缪安"]工作的时候，别说任何借口。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="26_g9_laterano_street",screenadapt="showall")]
[Delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_372_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]......
[charslot(slot="r",name="avg_npc_372_1#1$1",focus="r")]
[name="里凯莱"]费德里科，吃冰淇淋吗？我请你。
[charslot(slot="l",name="avg_1032_excu2_1#3$1",focus="l")]
[name="费德里科"]我在执行任务的过程中没有食用甜品的习惯。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]以及，在离开公证所前，我已经吃过了。
[charslot(slot="r",name="avg_npc_372_1#4$1",focus="r")]
[name="里凯莱"]原来休息室最后那点存货是你小子吃光的......
[charslot(slot="r",name="avg_npc_372_1#1$1",focus="r")]
[name="里凯莱"]看在我发现了这个秘密的分上，你应该告诉我，你突然从公证所跑出来，究竟要做什么？
[name="里凯莱"]你已经在这里站了十分钟了，但这个路口明明什么都没有。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]我没有向同僚同步私人事务的义务。
[charslot(slot="r",name="avg_npc_372_1#2$1",focus="r")]
[name="里凯莱"]你刚刚还说自己在“执行任务”......
[Dialog]
[charslot(slot="r",name="avg_npc_372_1#2$1",focus="none")]
[playsound(key="$d_avg_hastybell", volume=1)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_372_1#3$1",focus="r")]
[multiline(name="里凯莱")]这个声音......
[charslot(slot="r",name="avg_npc_372_1#10$1",focus="r")]
[multiline(name="里凯莱",end=true)]哦哦哦——你在等告解车！
[charslot(slot="r",name="avg_npc_372_1#9$1",focus="r")]
[name="里凯莱"]费德里科，虽然作为公证所投诉率最高的执行者，你确实累积了不少“罪恶”，但你想要主动忏悔还是太稀奇了......
[charslot(slot="r",name="avg_npc_372_1#1$1",focus="r")]
[name="里凯莱"]给你。
[Dialog]
[charslot(slot="r",posfrom="0,0",posto="-100,0",duration=1.5,focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[charslot(slot="r",posfrom="-100,0",posto="0,0",duration=1.5,focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]嗯？
[charslot(slot="r",name="avg_npc_372_1#10$1",focus="r")]
[name="里凯莱"]之前报销萨尔贡外勤任务的费用时，把买黄金之城文化盲盒的花销也算进去了，导致报销的钱比实际任务开支多了一倍......
[name="里凯莱"]我满怀愧疚地出门......当时正好有一辆告解车从面前经过，我就......顺便办了张年卡，给你用吧。
[Dialog]
[charslot]
[name="机械提示音"]到站通知。
[name="机械提示音"]自律告解车，编号“ELCARO-001”，即将到达，请有告解需求的公民排队等候。
[name="机械提示音"]“主愿每一位迷途之人获得救赎。”
[Dialog]
[PlaySound(key="$d_avg_hastybell", volume=1,channel="1")]
[Delay(time=

... (全文20848字符)
```

### level_act42side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
法柏尔区，博尔戈街，铳械工坊
[Dialog]
[playsound(key="$dooropenquite", volume=1)]
[Delay(time=1.5)]
[playsound(key="$d_gen_walk_n",volume=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot="l",name="avg_npc_1783_1#1$1",posfrom="200,0",posto="200,0",duration=1.5)]
[delay(time=2.5)]
[name="阿摩斯"]......你好，有人吗？
[Dialog]
[charslot]
这间工坊不大，充当货架的圣徒像随意陈列，它们以各种匪夷所思的姿势向客人展示着铳械......
但阿摩斯并未看到一个客人，他一路走来，除了自己，并没有什么人在工坊的门前停留。“冷清”——这是阿摩斯的第一感受。
也不至于连老板都不见踪影吧，他看着昏暗的灯光打在那些圣徒像上，心想。“诡异”——这是阿摩斯的第二感受。
[charslot(slot="l",name="avg_npc_1783_1#1$1",posfrom="200,0",posto="200,0",focus="l")]
[name="阿摩斯"]潘格尼尼先生在吗？
[charslot(slot="l",name="avg_npc_1783_1#10$1",posfrom="200,0",posto="200,0",focus="l")]
[name="阿摩斯"]（说真的，为什么铳械工坊的老板要叫这样滑稽的名字......）
[Dialog]
[charslot(slot="l",posfrom="200,0",posto="220,0",duration=1.5,focus="l")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[playsound(key="$bodyfalldown2",volume=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
阿摩斯四处打量，突然撞到了什么。
[Dialog]
[charslot(slot="r",name="avg_npc_1781_1#1$1",duration=1.5)]
[Background(image="61_g12_firearmsworkshop",screenadapt="coverall",fadetime=1.5)]
[delay(time=2.5)]
他猛然回头，对上了一双硕大而透亮的眼睛，那眼睛隐在阴影里，直勾勾地盯着他。
[charslot(slot="r",name="avg_npc_1781_1#1$1",focus="r")]
[name="大眼睛"]......
[charslot(slot="l",name="avg_npc_1783_1#4$1",posfrom="220,0",posto="220,0",focus="l")]
[name="阿摩斯"]救......
[charslot(slot="r",name="avg_npc_1781_1#1$1",focus="r")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="大眼睛"]*拉特兰俚语*你谁啊乱闯我的地盘——等我戴个眼镜！
[Dialog]
[stopmusic(fadetime=2)]
[charslot(slot="l",posfrom="220,0",posto="0,0",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="大眼睛"]公务员？
[name="大眼睛"]对不住啊，最近也没生意，躲在里面睡觉，没想到会有公务员先生大驾光临。
[charslot(slot="l",name="avg_npc_1783_1#10$1",focus="l")]
[name="阿摩斯"]枢机辅佐官阿摩斯，来确认这间铳械工坊的接收事宜。您就是......
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]我就是名字很滑稽的潘格尼尼。
[charslot(slot="l",name="avg_npc_1783_1#4$1",focus="l")]
[name="阿摩斯"]......
[name="阿摩斯"]等等，黎博利？
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]难不成我看起来像萨科塔？
[charslot(slot="l",name="avg_npc_1783_1#1$1",focus="l")]
[name="阿摩斯"]啊抱歉，我的意思是，我没见过黎博利从事这个职业。毕竟，守护铳只有萨科塔——
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]有什么问题？
[name="潘格尼尼"]很多厨子都不吃自己做的菜，我只是没法使用自己造的武器罢了。
[name="潘格尼尼"]你要检查我的铳械制造资质证明吗？放眼整个拉特兰，出自我手的守护铳没有一千也有八百，说不定你手上的这把......
[charslot(slot="l",name="avg_npc_1783_1#10$1",focus="l")]
[name="阿摩斯"]——
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]啧啧，一看做工就很“顶级”，我倒是没这样的手艺。
[charslot(slot="l",name="avg_npc_1783_1#1$1",focus="l")]
[name="阿摩斯"]......
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]不过如今都没什么所谓了，反正这里就要关停了。
[name="潘格尼尼"]近期所有的订单都已经退掉了，店里新完工的这一批铳，到时候让公证所的人直接带走吧。
[charslot(slot="l",name="avg_npc_1783_1#4$1",focus="l")]
[name="阿摩斯"]原、原来您已经做好了准备。我本以为......
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]会很麻烦？我这个人会很难搞？
[charslot(slot="l",name="avg_npc_1783_1#4$1",focus="l")]
[name="阿摩斯"]我、我不是这个意思。
[name="阿摩斯"]注册资料显示，这间铳械工坊已有百年历史。身为黎博利，您却选择为萨科塔造守护铳，这里对您来说一定意义非凡——
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]行了行了。这几年来谁都知道铳械工坊要成为历史了，大家都只是在等那个时候到来。
[name="潘格尼尼"]你问我愿不愿意，我当然不愿意。需要我把最近这段时间彻夜难眠的煎熬过程倾诉给你听吗？
[charslot(slot="l",name="avg_npc_1783_1#1$1",focus="l")]
[name="阿摩斯"]如果您需要倾诉，我可以帮您拦一辆告解车，告解费由七厅承担。
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]那恐怕还是你更需要告解。
[name="潘格尼尼"]我已经是个要退休的老头了，但梵里妮，我的学徒，她甚至还没来得及亲手为自己做一把守护铳。
[name="潘格尼尼"]既然铳械工坊将不复存在，你们得负责那孩子后续的发展。
[charslot(slot="l",name="avg_npc_1783_1#1$1",focus="l")]
[name="阿摩斯"]当然，铳械工坊的关停，只是为了让铳械生产的流程变得更正规、更高效。像您与您的学徒这样的铳械工匠，仍是宝贵的人才。
[name="阿摩斯"]我会向负责民政的第六厅汇报。您的学徒——梵里妮小姐，应当会被推荐到米迦莱昂区即将落成的制铳圣堂工作。
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]“制铳圣堂”......啧。但愿他们开工制铳的那天，还能像起这个名字的时候那么自信。
[charslot(slot="l",name="avg_npc_1783_1#5$1",focus="l")]
[name="阿摩斯"]我当然相信拉特兰的......
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]行了行了，这种鬼话我听得够多了。
[charslot(slot="l",name="avg_npc_1783_1#7$1",focus="l")]
[name="阿摩斯"]......那么，如果没有别的问题，请您在关停文件上签字吧，潘格尼尼先生。
[name="阿摩斯"]即时起，此铳械工坊的所有业务都将终止，后续会由中庭公证所跟进具体的接收事宜。
[Dialog]
[charslot(slot="r",posfrom="0,0",posto="-100,0",duration=1.5,focus="r")]
[Delay(time=2)]
[playsound(key="$d_avg_writerub",volume=1)]
[Delay(time=2.5)]
[charslot(slot="r",posfrom="-100,0",posto="0,0",duration=1.5,focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1783_1#7$1",focus="l")]
[name="阿摩斯"]那么，再见。
[charslot(slot="r",name="avg_npc_1781_1#3$1",focus="r")]
[name="潘格尼尼"]不送。
[Dialog]
[playsound(key="$dooropenquite", volume=1)]
[charslot(slot="l",afrom=1,ato=0,duration=1,isblock=false)]
[charslot(slot="l",posfrom="0,0",posto="-200,0",duration=1.5)]
[delay(time=2.5)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="26_g9_laterano_street",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_1041_angel2_1#1$5",duration=1.5)]
[delay(time=2.5)]
[name="能天使"]法柏尔区，博尔戈街......真是熟悉啊。
[charslot(slot="m",name="avg_1041_angel2_1#9$5",focus="m")]
[name="能天使"]哈，就是这里

... (全文19950字符)
```

### level_act42side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g4_nurseryindoor",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1785_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="保育员"]添头女士，这些都是必需的营养，还请您......
[charslot(slot="m",name="avg_npc_1807_1#5$1",focus="m")]
[name="添头"]我说了，我吃不下。
[charslot(slot="m",name="avg_npc_1785_1#1$1",focus="m")]
[name="保育员"]如果您有特别的需求，我们可以为您更换餐食。
[charslot(slot="m",name="avg_npc_1807_1#1$1",focus="m")]
[name="添头"]*萨卡兹粗口*，你难道当我是挑食？
[charslot(slot="m",name="avg_npc_1785_1#1$1",focus="m")]
[name="保育员"]那您......
[charslot(slot="m",name="avg_npc_1807_1#6$1",focus="m")]
[name="添头"]是，你们这有床有饭，你们的头头......那个“牧首”，也说了不会把我怎么样。
[name="添头"]可我就是安心不下。
[charslot(slot="m",name="avg_npc_1807_1#7$1",focus="m")]
[name="添头"]原来在荒野上，我知道什么东西能要了我的命，也知道要把这孩子好好生下来，我得做什么事。
[name="添头"]去哪里打猎，用什么取暖，怎么把山洞口封起来......只要一直想着这些，我就不害怕自己和这孩子会出事。
[charslot(slot="m",name="avg_npc_1807_1#6$1",focus="m")]
[name="添头"]可在这儿......啧。
[name="添头"]你出去吧，把这饭菜也拿出去，我没碰，你们这肯定有人更需要它。
[charslot(slot="m",name="avg_npc_1785_1#1$1",focus="m")]
[name="保育员"]......
[Dialog]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g3_nurserytemplecorridor",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1785_1#1$1",focus="m")]
[name="保育员"]您是......铳骑帕特里奇昂阁下？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]是我。牧首找我？
[charslot(slot="m",name="avg_npc_1785_1#1$1",focus="m")]
[name="保育员"]她在里面，请您稍等。
[name="保育员"]听闻新来的那位萨卡兹孕妇状态欠佳，牧首就立刻亲自前去照顾。只是，这已经一个多小时了，她还没出来......
[name="保育员"]我不愿对人妄加揣测，但出于种族仇恨，许多萨卡兹确实难以理解我们的用心。
[name="保育员"]牧首没有随身携带任何防身的武器，我担心......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]我去看看。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g4_nurseryindoor",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
铳骑帕特里奇昂为拉特兰效力数十年之久，他宽恕过或斩杀过的萨卡兹不计其数。
他从萨卡兹口中听到过愤怒的咒骂、痛苦的哀嚎、仇恨的啸叫，甚至绝望的祈求......
却唯独没听过虔信的祷词。
可怀有身孕的萨卡兹女性此刻正跪倒在圣像前，双手合十，磕磕绊绊地念诵着她还不熟悉的词句。
牧首在她背后，微微俯身，轻柔地陪她一同祷告。她磕绊时，牧首便停下来等待，两人沐浴在宁静的柔光之中。
[Dialog]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="帕特里奇昂"]......
[name="帕特里奇昂"]............
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]凡人皆冀求平安与喜乐，皆惧怕艰险与悲苦。
[name="牧首"]所以我们祈祷，不分种族。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]牧首，这位萨卡兹......
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]她刚刚脱离了流浪时那种日夜无休的生活，第一次闲下来，多年来无暇顾及的忧惧反倒一齐涌上心头。
[name="牧首"]她只是需要一种告慰自己的方式。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]是您教了她祈祷？
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]我只是与她一同念诵了几段祷词。
[name="牧首"]我们走远些说吧，别打扰到她。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g3_nurserytemplecorridor",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]牧首，您今天叫我来是为了？
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]我本想与你相谈，为你解惑。
[name="牧首"]但现在看来，我们似乎并不需要过多言语。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]“解惑”......？但我并没有疑惑。
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]没有疑惑，抑或是不敢疑惑？
[name="牧首"]拉特兰人尽皆知，我们亘古不变的秩序，从最初便是为应对启示中的灾异而创建的。
[name="牧首"]但当灾异降临，我们的秩序也被延展到极致......却无人能预知拉特兰未来会是一幅怎样的景象。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]虽然想象不到，但我相信那会是美好的。
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]因为你已为它付出太多。你无暇陪伴的孙女，你忘记了名字的老友，还有这些年间你作为秩序的守护者驱逐过的故人......
[name="牧首"]否定拉特兰的未来，便是否定你的一切付出与牺牲，便是否定你本身。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]但不必忧惧。那未来的一角，就展现在你面前。
[name="牧首"]若拉特兰的信仰能为不信者也带去慰藉，若萨卡兹亦可与萨科塔一同祈祷......
[name="牧首"]那么我们的秩序，必将包容万物。
[name="牧首"]不会再有隔阂，不会再有遗忘，更不会再有迫不得已的别离。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]您像是在描述一场梦。
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]我们将要做的，不正是在所有人的见证下，揭开梦境与现实之间的阻隔吗？
[name="牧首"]当所有人都虔信最极端的梦境也能被塑造为现实，奇迹便可以降临大地。
[name="牧首"]降生仪式必须顺利举行，帕特里奇昂。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]我会尽全力，牧首。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="26_g8_laterano_dwelling",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_213_mostma_1#3$1",focus="m")]
[name="莫斯提马"]喂喂，你挡着屏幕了，“圣责讨债人”！
[charslot(slot="m",name="avg_300_phenxi_1#3$1",focus="m")]
[name="菲亚梅塔"]谁让你坐那么远的......不过《八臂电锯侠》这种爆米花电影错过几个镜头也没所谓的。
[charslot(slot="m",name="avg_300_phenxi_1#2$1",focus="m")]
[name="菲亚梅塔"]还有，不要从正在看的台词里随便抠几个字眼就乱叫，这里不是任务现场，也不是汇报会，你们现在在我家！
[charslot(slot="m",name="avg_npc_1811_1#1$2",focus="m")]
[name="蕾缪安"]我倒是觉得这是个好名字，可以留作你下次任务的代号。
[charslot(slot="m",name="avg_300_phenxi_1#4$1",focus="m")]
[name="菲亚梅塔"]蕾缪安，你也......
[charslot(slot="m",name="avg_300_phenxi_1#8$1",focus="m")]
[name="菲

... (全文27148字符)
```

### level_act42side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
龙门，“大地的尽头”酒吧
[Dialog]
[charslot(slot="m",name="avg_npc_035",duration=1.5)]
[delay(time=2.5)]
[name="伊斯"]能天使，你竟然在？
[charslot(slot="m",name="avg_103_angel_1#1$1",focus="m")]
[name="能天使"]呃，你不是也在？
[name="能天使"]酒吧又没营业，你来干嘛？
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]不知道怎么就转到这儿来了，说不定这是社畜的天性。
[name="伊斯"]来都来了，就打扫下卫生吧。
[charslot(slot="m",name="avg_103_angel_1#3$1",focus="m")]
[name="能天使"]呀，待会儿我自己收拾就好！
[name="能天使"]我看都是给我的礼物，就顺手都给拆了。
[Dialog]
[charslot(slot="m",name="avg_103_angel_1#1$1",focus="m")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_103_angel_1#4$1",focus="m")]
[name="能天使"]水晶球？拜松这小子——等等，峯驰物流已经把生意做到察帕特了吗？
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_103_angel_1#1$1",focus="m")]
[name="能天使"]这么厚一沓可叠加的折扣券？“买得越多，折扣越大；折扣越大，买得越多”......可颂是想让我把商场搬空吗？
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_103_angel_1#3$1",focus="m")]
[name="能天使"]Sora叙拉古巡回演唱会LIVE专辑《不期而会》......空是不是忘了多寄两张门票？
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_103_angel_1#6$1",focus="m")]
[multiline(name="能天使")]狂欢节假面，这肯定是德克萨斯送的......
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_103_angel_1#3$1",focus="m")]
[multiline(name="能天使",end=true)]呀，有点勒脸，差评！
[charslot(slot="m",name="avg_103_angel_1#1$1",focus="m")]
[multiline(name="能天使")]这个软刷......
[charslot(slot="m",name="avg_103_angel_1#4$1",focus="m")]
[multiline(name="能天使",end=true)]老板这到底是送我礼物，还是给员工寄帮他保养黑胶唱片的工具！
[name="能天使"]对了伊斯，你看这个软刷到底是用什么毛做的？
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]......看着有点像鲁珀的毛。
[charslot(slot="m",name="avg_103_angel_1#8$1",focus="m")]
[name="能天使"]说起来，狂欢节早就结束了，老板和德克萨斯怎么还待在新沃尔西尼？我从萨尔贡回来，店里居然一个人都没有！
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]德克萨斯说是留在那边筹备企鹅物流的新业务，至于大帝先生......
[name="伊斯"]他和他的朋友们，有些别的事情要处理——除了做唱片办派对教育员工......之外的事情。
[charslot(slot="m",name="avg_103_angel_1#1$1",focus="m")]
[name="能天使"]懂了。那跟你报备也是一样的。
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]嗯？
[charslot(slot="m",name="avg_103_angel_1#9$1",focus="m")]
[name="能天使"]等一等啊，我快填完了！
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]填什么？
[charslot(slot="m",name="avg_103_angel_1#10$1",focus="m")]
[name="能天使"]休假申请单！
[name="能天使"]我想休一个很长很长的假，所以还是走一下正经程序比较好！
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]能天使？
[charslot(slot="m",name="avg_103_angel_1#7$1",focus="m")]
[name="能天使"]你应该知道我为什么专门接了萨尔贡的单子吧？
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]萨尔贡......那是莫斯提马作为万国信使负责的区域之一吧？
[charslot(slot="m",name="avg_103_angel_1#6$1",focus="m")]
[name="能天使"]聪明。
[charslot(slot="m",name="avg_103_angel_1#7$1",focus="m")]
[name="能天使"]我这次见到莫斯提马，她说，那个让姐姐和她变成如今这个样子的家伙，那个姐姐希望永远不会再出现的人，回到了拉特兰......
[name="能天使"]姐姐的病还没有完全好，但她已经加入了教皇厅。秘密也好，真相也好，当年的事情把他们重新卷到了一起......
[name="能天使"]而我当年本就是为了知道这些才来的龙门。
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]你要回拉特兰？
[charslot(slot="m",name="avg_103_angel_1#1$1",focus="m")]
[name="能天使"]嗯！总不能在龙门干等着姐姐来看我吧。
[charslot(slot="m",name="avg_103_angel_1#9$1",focus="m")]
[name="能天使"]德克萨斯、空、拜松、可颂......甚至是最不着调的老板，大家如今都有自己的事情要忙，天下没有不散的筵席啦。
[charslot(slot="m",name="avg_103_angel_1#6$1",focus="m")]
[name="能天使"]“不忘初心”——这可是企鹅物流的企业文化！
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]每日特供的企业文化......不过道理是没错的。
[charslot(slot="m",name="avg_103_angel_1#10$1",focus="m")]
[name="能天使"]替我保管好这些礼物。告诉我的朋友们，等一切事情都搞定的时候，我就会回来。
[Dialog]
[charslot]
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_035",focus="m")]
[name="伊斯"]接你的人？
[charslot(slot="m",name="avg_103_angel_1#4$1",focus="m")]
[name="能天使"]嗯？不是啊！我才刚做的决定！
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=0.6)]
[charslot(slot="l",name="avg_npc_089",duration=1.5)]
[charslot(slot="r",name="avg_npc_012",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_npc_089",focus="l")]
[name="罗德岛干员"]能天使。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_103_angel_1#7$1",focus="m")]
[name="能天使"]是你们......怎么了？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_089",focus="m")]
[name="罗德岛干员"]看看这个，办事处刚刚收到的。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_paper1", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_103_angel_1#7$1",focus="m")]
[name="能天使"]......
[name="能天使"]本舰的紧急机密文件？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="61_i03_3",block=false,screenadapt="coverall",fadetime=0)]
[Delay(time=2)]
[PlayMusic(key="$formal_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="能天使"]累死了。
[name="能天使"]千里迢迢的，好不容易回来一趟，结果怪事一件接一件，忙得人晕头转向！
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0,g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="“辛苦了。但我们动作还需要再快些。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“根据我这两天的观察，教皇厅毫不犹豫地将那场爆炸视作了针对万国峰会的恐怖袭击。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Image(image="61_i03_5",block=false,screenadapt="coverall",fadetime=0.5)]
[Delay(time=1)]
[name="能天使"]谁能想到一辆人畜无害的告解车，会是顶级的情报员呢！
[name="能天使"]干得不错，拍拍你的音箱以示鼓励。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0,g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="“......”", x=300, y=370, alignment="center", size=24, delay=0.04,

... (全文25238字符)
```

### level_act42side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g2_baptismlobby",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$tech_intro", key="$tech_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1811_1#1$2",duration=1.5)]
[charslot(slot="r",name="avg_npc_1780_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]薇尔丽芙枢机，好久不见。
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]别叫枢机了，我现在只是育婴圣堂里一个再普通不过的事务员。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]那我叫你前辈喽......看起来，确实是前辈的手笔。
[charslot(slot="r",name="avg_npc_1780_1#4$1",focus="r")]
[name="薇尔丽芙"]什么？
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]我刚刚一路走来看见的，从外围街道到圣堂内部，这里安防布置的思路可不输戍卫队。
[charslot(slot="r",name="avg_npc_1780_1#11$1",focus="r")]
[name="薇尔丽芙"]总得帮着干点活儿嘛。
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]说起来，还真被我猜对了。
[charslot(slot="l",name="avg_npc_1811_1#6$2",focus="l")]
[name="蕾缪安"]什么？
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]来这里确认防务的果然是你......从程序上讲这类工作明显更适合公证所的执行者，或是铳骑与戍卫队的成员。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]我姑且也还在追查前两天的爆炸事件哦，不是什么无关人士。
[charslot(slot="r",name="avg_npc_1780_1#2$1",focus="r")]
[name="薇尔丽芙"]我可没接到通知说布防的时候要把爆炸案的调查结果也考虑在内。况且，你的调查现在也还没什么实质性的成果吧？
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]难道说，你来这里，是因为受到袭击的是安多恩？
[charslot(slot="l",name="avg_npc_1811_1#8$2",focus="l")]
[name="蕾缪安"]......
[charslot(slot="l",name="avg_npc_1811_1#2$2",focus="l")]
[name="蕾缪安"]前辈，你不会是想敲打我，身为七厅枢机，眼里应该是整座圣城，而不是自己的私交吧？
[charslot(slot="r",name="avg_npc_1780_1#3$1",focus="r")]
[name="薇尔丽芙"]哈，我们都知道你是什么样的人啦。
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]头脑清醒，做事雷厉风行，又有敏锐准确的洞察力，在遴选枢机的时候确实加了很多分......
[name="薇尔丽芙"]但大家也都清楚，你的这些美好品质，一般在什么时候最能体现出来。
[charslot(slot="r",name="avg_npc_1780_1#8$1",focus="r")]
[name="薇尔丽芙"]蕾缪安枢机，我还记得你当年加入戍卫队特勤队的初衷哦，我看过那份报告书。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]哈哈，是吗，我都忘了。
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]你本来并没有加入特勤队的打算，只是去看望菲亚梅塔的，对吧？
[charslot(slot="l",name="avg_npc_1811_1#2$2",focus="l")]
[name="蕾缪安"]......还有安多恩。
[charslot(slot="r",name="avg_npc_1780_1#1$1",focus="r")]
[name="薇尔丽芙"]哦？这我倒是不知道。我以为你们是加入特勤队之后才认识的。
[charslot(slot="l",name="avg_npc_1811_1#2$2",focus="l")]
[name="蕾缪安"]要更早。
[charslot(slot="l",name="avg_npc_1811_1#8$2",focus="l")]
[name="蕾缪安"]他好像是从很远的地方一路走过来的，穿着一身破衣裳，憔悴得很。
[name="蕾缪安"]就那么一动不动地坐在礼拜堂前的长椅上，比路边的圣徒像更像圣徒像。
[charslot(slot="l",name="avg_npc_1811_1#2$2",focus="l")]
[name="蕾缪安"]那是我和莫斯提马第一次见到他。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]至于菲亚梅塔，本来就是我和莫斯提马在电影院午夜场偶然认识的好朋友。
[name="蕾缪安"]安多恩不在圣城长大，本身就格格不入；菲亚梅塔是个倔性子，那阵子大概在和她的爷爷置气......我和莫斯提马就想着去看看。
[name="蕾缪安"]这两人事先并不认识，其他的萨科塔也未必是故意排挤他们，但实际的结果是——
[charslot(slot="l",name="avg_npc_1811_1#2$2",focus="l")]
[name="蕾缪安"]整个“软胶铳弹轮盘赌，暨特勤队组队仪式”，就只有这两个家伙孤零零地被剩了下来。
[charslot(slot="r",name="avg_npc_1780_1#2$1",focus="r")]
[name="薇尔丽芙"]所以你就把在场的其他人都痛扁了一顿......
[name="薇尔丽芙"]又和莫斯提马当场填了申请表，跟他们组成了那次组队仪式的最后一个四人小队。
[name="薇尔丽芙"]最后成了整个特勤队出外勤次数最多、配合最为默契的小队，也才有了后来的意外......
[charslot(slot="r",name="avg_npc_1780_1#9$1",focus="r")]
[name="薇尔丽芙"]蕾缪安，不论我再怎么欣赏你......我也还是要提醒你，身处枢机之位，做事的出发点就永远只有圣城。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]圣城在我眼里，首先是一个又一个熟悉的名字。
[charslot(slot="l",name="avg_npc_1811_1#2$2",focus="l")]
[name="蕾缪安"]前辈，怀旧到此为止。
[charslot(slot="l",name="avg_npc_1811_1#8$2",focus="l")]
[name="蕾缪安"]第七厅有能力审视自己的职责所在。如果前辈只以“普通的事务员”自居，我应该亲自去见一下牧首。
[charslot(slot="r",name="avg_npc_1780_1#9$1",focus="r")]
[name="薇尔丽芙"]......
[charslot(slot="l",name="avg_npc_1811_1#8$2",focus="l")]
[name="蕾缪安"]她就在前面，对吧？
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_churchfootstep", volume=1)]
[charslot]
[Image(image="61_i06",block=false,screenadapt="coverall",fadetime=0)]
[ImageTween(xScaleFrom=1.15, yScaleFrom=1.15, xScaleTo=1, yScaleTo=1, duration=70, block=false)]
[Delay(time=3)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
蕾缪安见到了此行的目标。
金发萨科塔立于某道门廊之下，她在祷告，她在不安，她的呼吸急促，身体因此肉眼可见地颤栗着......
蕾缪安感觉自己快被对方汹涌的情绪淹没。
[name="蕾缪安"]牧首？
[name="牧首"]——
[name="牧首"]蕾缪安枢机，我听到了你和薇尔丽芙的谈话......但请原谅我此刻无法思绪平静地与你交谈。
[name="蕾缪安"]那里面是？
[name="牧首"]一位萨卡兹母亲。
[name="牧首"]她在荒野上耽搁了太久，来这里又拒食了两天......现在的情况不容乐观。我们的保育员正在为她治疗。
[name="牧首"]她在恐惧，她在焦躁，她不想输给疼痛，此刻仍在挣扎着保持清醒......
[name="牧首"]......她在清醒地祈祷，祈祷孩子能平安降生。
[name="牧首"]我能做的，只是与她感同身受，与她一同祈祷。
[name="蕾缪安"]您能感受到萨卡兹的情绪？
[name="牧首"]是的，枢机。
[name="牧首"]就像此刻，你也在为我的悸动而担忧。它清晰得如同你我之间与生俱来的共感。
[name="蕾缪安"]“共感”......
[name="牧首"]也许这是主对我这样一个目盲者额外的恩典，也许只是因为......这里是拉特兰专为创造新生而建的圣堂。
[name="牧首"]我们的信仰将在此夯实，在此延伸，这里不应有任何隔阂与限制。
[name="牧首"]这样说来，更应该走进这里的，是我们的同胞自己。
[name="蕾缪安"]......
[Dialog]
阳光从高处的彩窗落下，照亮空旷而肃穆的大堂。
巨大的圣像俯首合十，注视着下方两位渺小的萨科塔。
[name="蕾缪安"]这里的确很特别。
[name="蕾缪安"]见多了用各种奇怪的姿势举着铳蓄势待发的圣像，第一次见到这种造型的，还真是，唔，有些不太习惯......
[name="牧首"]相比于矗立在玻利瓦尔山间或伊比利亚海边的那些所谓的“拉特兰教造像”，拉特兰随处可见的圣像其实更难以理解，枢机。
[name="牧首"]乐园形塑了我们别样到有些失真的虔诚。
[name="牧首"]跋涉在天灾与苦难中的生灵，为生存祈愿......这才是信仰最初的形貌。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[charslot]
[image]
[hidecgitem(image="cgitem_61_i06")]
[Background(image="61_g2_baptismlobby",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$rungeneral",volume=1)]
[charslot(slot="m",name="avg_npc_1785_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="保育员"]牧、牧首，一切平安。
[name="保育员"]那位母亲的状态终于平复下来了，我们喂她吃了药，也给她补充了营养，此刻她已经睡去。
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]呼——那我就放心了。
[name="牧首"]她分娩在即，还请继续关注她的状况，不得有一丝松懈。
[charslot(slot="m",name="avg_npc_1785_1#1$1",focus="m")]
[name="保育员"]是。
[Dialog]

... (全文13299字符)
```

### level_act42side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g2_laterano_cathedralhall",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$tech_intro", key="$tech_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="帕特里奇昂"]......
[charslot(slot="m",name="avg_npc_1780_1#4$1",focus="m")]
[name="薇尔丽芙"]您为什么要用这样别扭的姿势靠墙站着？我还以为自己看见了一尊雕塑......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]你要是进来得早一些，就能听见我的关节咔咔响了，哈哈。
[name="帕特里奇昂"]看来得抽空去找一趟工匠师傅，看能不能在腰间加装一块护枕......
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]铳骑装甲的设计师估计不会考虑这种关爱老年人的特殊设计......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]这主要是为了缓冲巨铳的后坐力嘛，年轻的铳骑也需要！
[name="帕特里奇昂"]降生仪式可就在明天了，育婴圣堂那边准备得怎么样了？
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]那位母亲状态很稳定，安多恩将她照顾得相当好，相信明天她会诞下一位健康且美丽的新生儿。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]维什戴尔议长和卡兹戴尔使节团、双子女皇和莱塔尼亚使节团、阿戈尔发展规划所执政官代表团、炎国宣礼使带领的天师团......
[name="帕特里奇昂"]明天，所有到访圣城的客人都会受邀前往育婴圣堂，共同见证那个新生命的降生。
[name="帕特里奇昂"]不过，既然一切正常，你今天找我是为了？
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]我们的新人枢机......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]蕾缪安？
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]她专程去见了一趟牧首。我想——
[name="薇尔丽芙"]她应该不是在调查爆炸事件时“偶然”经过，“顺便”看看，再“心血来潮”地提出以第七厅的名义为育婴圣堂提供帮助吧？
[name="薇尔丽芙"]我起初以为她是为安多恩遇袭的事来的。但她见过牧首之后的表现......很明显她还有更多疑虑。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]我还以为我已经打消了她的疑虑。
[charslot(slot="m",name="avg_npc_1780_1#7$1",focus="m")]
[name="薇尔丽芙"]蕾缪安的敏锐很多时候无人能及，尤其在她关注某件事的时候。我很想说，她确实就是最适合成为七厅枢机的那个人。
[charslot(slot="m",name="avg_npc_1780_1#2$1",focus="m")]
[name="薇尔丽芙"]但她同时也是不适合的。毕竟，她的注意力在哪，似乎大部分时候只取决于她自己的私人判断。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]哈哈。那你觉得有必要对她加以防范吗？
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]......您这个语气，搞得好像我们是什么反派，正在酝酿颠覆拉特兰的大阴谋一样。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]难说哟。
[name="帕特里奇昂"]对于有些人来说，我们将要迎接的那个未来，恐怕确实会颠覆他们所知的生活。
[name="帕特里奇昂"]我们的共感，我们的同胞与亲族，甚至“萨科塔”这一概念本身......都将抛却旧有的局限。
[name="帕特里奇昂"]这本是拉特兰所行之道既定的终点，但这道路毕竟绵延了太长、太久。
[name="帕特里奇昂"]或许有些人反倒将过程中伴生的一些微不足道的意外现象当作了常态，以至于无法接受原本既定的终点。
[charslot(slot="m",name="avg_npc_1780_1#11$1",focus="m")]
[name="薇尔丽芙"]说得也是。
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]我们还是应该早做准备。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]蕾缪安的事情，我会处理。你就回到育婴圣堂，专心准备明天的仪式吧。
[name="帕特里奇昂"]愿主继续赐福这座城。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g4_nurseryindoor",screenadapt="showall")]
[Delay(time=2)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_comfortbell",volume=1,channel="2")]
[playsound(key="$d_gen_walk_n",volume=0.5,channel="1")]
[Delay(time=3)]
头发火红的萨科塔在苍白与幽蓝交织的丛林中东奔西走，像一撮小小的火苗在雨中摇曳。
[Dialog]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_1041_angel2_1#10$1",duration=1.5)]
[Delay(time=2)]
[name="能天使"]那个安抚铃上的云朵快赶上可颂的面包车大了......还有那能塞下两个集装箱的摇篮......
[Dialog]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",afrom=1,ato=0,duration=1)]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1.5)]
[Delay(time=2.5)]
[playsound(key="$d_avg_comfortbell",volume=1,channel="2")]
[playsound(key="$d_gen_walk_n",volume=0.5,channel="1")]
[Delay(time=3)]
安抚铃上悬挂的云朵仿佛能遮蔽天光，托举摇篮的双手似乎又要耸入云霄。
在这圣堂之中，一切活物都显得渺小。
[name="能天使"]嗯？
[name="能天使"]怎么会......
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g3_nurserytemplecorridor",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$dooropenquite", volume=1)]
[charslot(slot="m",name="avg_1041_angel2_1#11$1",duration=1.5)]
[Delay(time=2)]
[name="能天使"]看起来空荡荡的，安静得要死，但这些育婴室，起码有一半以上都住了人......
[name="能天使"]小孩子、异族人，甚至还有堕天使......保育员忙来忙去，看样子他们应该已经住进来很久了。
[charslot(slot="m",name="avg_1041_angel2_1#11$1",focus="m")]
[name="能天使"]那帮人不是说这里绝大多数设施都还没有投入使用，要等到那个什么仪式办完之后才开放吗？
[charslot(slot="m",name="avg_1041_angel2_1#8$1",focus="m")]
[name="能天使"]压根不是那么回事！
[Dialog]
[playsound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="0,-20",duration=1.5)]
[Delay(time=2.5)]
[name="能天使"]不行......得拆掉这些炸弹！
[charslot(slot="m",name="avg_1041_angel2_1#11$1",posfrom="0,-20",posto="0,-20",focus="m")]
[name="能天使"]本来以为先把场地炸掉，仪式就办不成了，结果这里面全是人......
[name="能天使"]真要命啊，好不容易才躲开那些守卫安好的......
[Dialog]
[playsound(key="$d_avg_tidyequipment", volume=1)]
[Delay(time=3.5)]
[charslot(slot="m",name="avg_1041_angel2_1#10$1",posfrom="0,-20",posto="0,-20",focus="m")]
[name="能天使"]......要是她们在就好了。
[name="能天使"]可以拜托德克萨斯把守卫全部打晕拖到外面去，或者让可颂撞开那些房间，把里面的人统统打包带走......
[charslot(slot="m",name="avg_1041_angel2_1#5$1",posfrom="0,-20",posto="0,-20",focus="m")]
[name="能天使"]实在不行，这帮人办仪式的时候，就让老板在对面开一个粉丝见面会之类的，把注意力都吸引过去......
[Dialog]
[playsound(key="$d_avg_tidyequipment", volume=1)]
[Delay(time=3.5)]
[charslot(slot="m",name="avg_1041_angel2_1#10$1",posfrom="0,-20",posto="0,-20",focus="m")]
[name="能天使"]算了，继续，没多少时间了。
[name="能天使"]拆掉这些炸弹，再想别的办法——
[Dialog]
[charslot(slot = "m",focus="none")]
[name="？？？"]先剪掉那根蓝色的线，拆起来会快很多哦。
[CameraShake(duration=0.5,xstrength=5,  ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_1041_angel2_1#6$1",posfrom="0,-20",posto="0,-20",focus="m")]
[name="能天使"]唔啊......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1811_1#1$2",duration=1.5)]
[Delay(time=2)]


... (全文15416字符)
```

### level_act42side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g1_nurserytemplesquare",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1788_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="圣堂巡卫"]这位公民，如果你是来观摩降生仪式的，请去广场那边的等候通道接受检查。
[name="圣堂巡卫"]......我看你在附近观望很久了。
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[name="梵里妮"]啊，对不起！
[name="梵里妮"]我只是在等人......
[charslot(slot="m",name="avg_npc_1788_1#1$1",focus="m")]
[name="圣堂巡卫"]是吗？
[name="圣堂巡卫"]今天进出圣堂的人流量很大，请配合我们的工作，不要在此过多逗留。
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[name="梵里妮"]对不起！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.4)]
[charslot(slot="m",afrom=1,ato=0,duration=1)]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1.5)]
[Delay(time=2.5)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g1_nurserytemplesquare",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1779_1#4$2",afrom=0,ato=1,duration=1)]
[charslot(slot="m",posfrom="200,0",posto="100,0",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",posfrom="100,0",posto="0,0",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[name="梵里妮"]小乐姐已经进去整整一天了。
[name="梵里妮"]按照原计划，她只需要炸毁圣堂里的重要建筑结构，让那个什么仪式没法如期举办就好。
[name="梵里妮"]这个时间点，她应该已经出来了才对......难道被发现了吗？
[name="梵里妮"]不对不对，我一直守在这附近，里面明明什么动静都没有......
[name="梵里妮"]不管怎么样，小乐姐肯定遇到了一些意外，没法脱身......
[name="梵里妮"]梵妮，快想想快想想，你能做点什么！
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g1_nurserytemplesquare",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_tidyequipment", volume=1)]
[Delay(time=3)]
[charslot(slot="m",name="avg_npc_1779_1#13$2",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1779_1#2$2",focus="m")]
[name="梵里妮"]我身上还剩两小管源石火药，可以组装成一个简易炸弹。
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[name="梵里妮"]虽然实际的威力可能没那么大，但足够搞出一些动静，吸引那些卫兵的注意力，让小乐姐能够......
[Dialog]
[playsound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="0,-30",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1779_1#4$2",posfrom="0,-30",posto="0,-30",focus="m")]
[name="梵里妮"]就安在这里好了。
[name="梵里妮"]呼——暂时没人注意到这里，那么只需要引爆——
[Dialog]
[playsound(key="$d_avg_clothmovement", volume=0.5)]
[charslot(slot="m",name="avg_npc_1779_1#3$2",posfrom="0,-30",posto="0,-30",focus="m")]
[Delay(time=1.5)]
[charslot(slot="m",focus="none")]
一截铳管托住了梵里妮的手臂，她没能再往下移动哪怕一寸。
[charslot(slot="m",focus="none")]
[name="？？？"]别让这小玩意“砰”出声，孩子。
[name="？？？"]慢慢站起身来。
[Dialog]
[charslot(slot="m",posfrom="0,-30",posto="0,0",duration=1.5)]
[Delay(time=3.5)]
[charslot]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[name="梵里妮"]铳、铳骑......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]看你这身装扮，你是铳械工坊的工匠？
[name="帕特里奇昂"]我还有十分钟的空闲时间。孩子，可以向我解释清楚这一切吗？
[name="帕特里奇昂"]你想做什么？或者说，你在给谁打掩护？
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[name="梵里妮"]......
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="61_g12_firearmsworkshop",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot(slot="l",name="avg_1041_angel2_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1779_1#1$2",focus="r")]
[name="梵里妮"]走吧，小乐姐。
[charslot(slot="l",name="avg_1041_angel2_1#6$1",focus="l")]
[name="能天使"]潘大师呢？
[charslot(slot="r",name="avg_npc_1779_1#1$2",focus="r")]
[name="梵里妮"]老师已经睡下了。他最近视力又变差了，医生叮嘱他早点休息。
[name="梵里妮"]我们动作轻点，应该不会吵醒他。
[charslot(slot="l",name="avg_1041_angel2_1#8$1",focus="l")]
[name="能天使"]梵妮，先别急。
[charslot(slot="r",name="avg_npc_1779_1#4$2",focus="r")]
[name="梵里妮"]小乐姐，你干嘛这么一本正经地说话，好、好不习惯啊！
[charslot(slot="l",name="avg_1041_angel2_1#8$1",focus="l")]
[name="能天使"]咳咳，听着——
[name="能天使"]如果你不小心被逮住了，不管对方是戍卫队、执行者，还是铳骑，千万不要讲什么义气，直接把我供出来就好！
[name="能天使"]你只是在一个月黑风高的晚上突然被我踹开门胁迫着做了一些炸弹，被我逼着在圣堂外面望望风而已。
[charslot(slot="l",name="avg_1041_angel2_1#4$1",focus="l")]
[name="能天使"]你什么都不知情，只是一个无辜的小天使！
[charslot(slot="r",name="avg_npc_1779_1#4$2",focus="r")]
[name="梵里妮"]啊？
[charslot(slot="l",name="avg_1041_angel2_1#8$1",focus="l")]
[name="能天使"]这是我答应你跟我一起行动的条件哦。
[charslot(slot="r",name="avg_npc_1779_1#9$2",focus="r")]
[name="梵里妮"]小乐姐，我只是有点怕生，并不是胆小！
[charslot(slot="l",name="avg_1041_angel2_1#9$1",focus="l")]
[name="能天使"]哈哈我知道。你愿意帮我，我已经很开心了。
[charslot(slot="l",name="avg_1041_angel2_1#7$1",focus="l")]
[name="能天使"]教皇厅好像非常非常看重那个仪式，很难说因此触犯律法的人，会受到什么样的惩罚。
[name="能天使"]更何况现在的拉特兰，和我记忆中的很不一样了。
[charslot(slot="r",name="avg_npc_1779_1#9$2",focus="r")]
[name="梵里妮"]我......
[charslot(slot="l",name="avg_1041_angel2_1#3$1",focus="l")]
[name="能天使"]好了好了，我一个人就够了！
[name="能天使"]再说了，企鹅物流的企业文化是——能一个人出的风头绝不分给两个人！
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="61_g1_nurserytemplesquare",screenadapt="showall")]
[charslot(slot="m",name="avg_npc_1779_1#4$2",focus="m")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1779_1#9$2",focus="m")]
[name="梵里妮"]（摇头）
[name="梵里妮"]我、我是一个人来的。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]有趣的孩子。
[name="帕特里奇昂"]我这样的老家伙，和年轻人聊天的机会不多。可惜，仪式就要开始了......
[name="帕特里奇昂"]你

... (全文26065字符)
```

### level_act42side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="49_g2_kazdelstreet_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_clothmovement", volume=1)]
[CameraShake(duration=2.5, xstrength=20,ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=3)]
[charslot(slot="l",name="avg_npc_932_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_933_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[name="萨卡兹工人A"]喂，你赶着投胎啊，走这么快！我们抬的是一块源石结晶板欸，待会儿摔了就都死翘翘了。
[name="萨卡兹工人A"]这家人也真是的，用这玩意儿压菜缸，也不怕吃进嘴里的都是源石颗粒！
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="r")]
[name="萨卡兹工人B"]别*萨卡兹粗口*啰啰嗦嗦了，赶紧的。
[name="萨卡兹工人B"]今天之内清理完这个城区，这任务可不轻，你也不想头儿被那个老巫妖骂得臭血淋头后再把我们骂得臭血淋头吧。
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[name="萨卡兹工人A"]这么多间屋子，要把沾着源石的地方都清理干净......巴别塔都组建了专门的城建队，为啥不干脆把它们推倒了重盖？
[name="萨卡兹工人A"]说起来，想到接下来哪哪儿都看不见源石，还真有点不适应。
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="r")]
[name="萨卡兹工人B"]闭上你那张臭嘴。
[name="萨卡兹工人B"]以前是没办法，只有靠着矿脉的产出才能活，现在卡兹戴尔已经不用再为能源发愁了，当然要把屋子打扫干净......
[name="萨卡兹工人B"]你还真喜欢住在源石窝里头啊——喂，巫妖，看路！
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[name="萨卡兹工人A"]巫妖，收好你的线头，鬼知道你们那些线和源石打了结，会闹出什么乱子......
[Dialog]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="none")]
[name="？？？"]这样说话很不礼貌哦。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_869_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="埃芒加德"]真要缠住了，就用你们的角帮我勾断吧。不过那样的话，我的丝弦会不会把你们拖进别的空间里去呢？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="all")]
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="all")]
[name="萨卡兹工人们"]......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_869_1#4$1",focus="m")]
[name="埃芒加德"]好啦，不吓你们了。先生们，请过去吧~
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=1,g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0.5, r=1,g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="l")]
[name="萨卡兹工人A"]喂，是我眼花了吗？刚刚的光线是怎么回事？
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="r")]
[name="萨卡兹工人B"]前面的房子？过去看看。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_869_1#2$1",focus="m")]
[name="埃芒加德"]......让我去吧。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="l")]
[name="萨卡兹工人A"]嗯？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_869_1#1$1",focus="m")]
[name="埃芒加德"]那排房子紧挨着刚整合完毕的农田地块，刚刚的光，应该是监测土壤的信标感应到了你俩搬的源石结晶板。
[charslot(slot="m",name="avg_npc_869_1#10$1",focus="m")]
[name="埃芒加德"]要是维什戴尔知道这两年好不容易开垦的农田被污染......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="r")]
[name="萨卡兹工人B"]走吧走吧。
[Dialog]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g1_kazdelroom",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_869_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_352_1#3$1",focus="m")]
[name="塞茜莉亚"]不、不要再往前了！
[charslot(slot="m",name="avg_4036_forcer_1#1$2",focus="m")]
[name="艾泽尔"]唔......
[Dialog]
[charslot]
埃芒加德看着面前紧张的小女孩，她尝试用自己小小的身子挡住来人的视线。
女孩身后，萨科塔男性脱力般跪在地板上，他的光环与光翼支离破碎，那些碎片像是活物般颤抖着，忽明忽暗，仿佛故障了的灯。
而萨科塔本人如同堕入了深深的梦中，不发一言。
[charslot(slot="m",name="avg_npc_352_1#7$1",focus="m")]
[name="塞茜莉亚"]你是谁？你是来抓我们的吗？
[Dialog]
[charslot]
小女孩很紧张，埃芒加德弯下腰，用手撑着膝盖，尽量让自己看起来没有敌意，她甚至摇了摇自己充盈着能量的大尾巴。
[charslot(slot="m",name="avg_npc_869_1#1$1",focus="m")]
[name="埃芒加德"]可爱的小妹妹，我没有恶意。
[name="埃芒加德"]你刚刚应该听到了，我支开了其他的萨卡兹。或许我能帮你们......帮他。
[charslot(slot="m",name="avg_npc_352_1#7$1",focus="m")]
[name="塞茜莉亚"]......
[Dialog]
[charslot]
埃芒加德关紧了身后的门，将可能的视线隔绝在外。
[Dialog]
[PlaySound(key="$d_avg_magic_4",volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
她正了正自己的帽子，看不见的丝弦逶迤向不可知的空间。
[Dialog]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.2, fadetime=1.5)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.2, fadetime=1.5)]
[focusout(type="bg", id="49_g1_kazdelroom", from=0, to=1, duration=1.5, block=false)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_869_1#9$1",focus="m")]
[name="埃芒加德"]老师。
[charslot(slot="m",name="avg_npc_869_1#9$1",focus="none")]
[name="弗莱蒙特"]虽然高塔上那些繁文缛节和废话连篇的经卷真的倒人胃口，但对比现在，我真的得冲那对双子羊鞠躬，感谢她们的礼遇。
[name="弗莱蒙特"]谁受得了每项政策都只能口头传达而且动不动还得翻来覆去解释好几遍，什么时候才能对我们的公务员进行普及教育......
[charslot(slot="m",name="avg_npc_869_1#2$1",focus="m")]
[name="埃芒加德"]急事。
[charslot(slot="m",name="avg_npc_869_1#2$1",focus="none")]
[name="弗莱蒙特"]......说。
[charslot(slot="m",name="avg_npc_869_1#7$1",focus="m")]
[name="埃芒加德"]我在节点炉这边发现了两个光环破碎的萨科塔......其中一个状态非常非常，不对劲。
[charslot(slot="m",name="avg_npc_869_1#7$1",focus="none")]
[name="弗莱蒙特"]......
[name="弗莱蒙特"]带他们回来，尽量别让其他人注意到，免得引起骚乱。
[name="弗莱蒙特"]我去把维什戴尔踹醒。到了需要这个议长主持紧急会议的时候了。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[focusout(

... (全文18390字符)
```

### level_act42side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g2_baptismlobby",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_comfortbell",volume=1)]
[charslot(slot="m",name="avg_npc_1790_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="木攀兽"]......
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]这个响动......别紧张，孩子。
[Dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=0.4)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="帕特里奇昂"]牧首。
[charslot(slot="m",name="avg_npc_1800_1#16$2",focus="m")]
[name="安多恩"]......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]保育员先生，你也在。真是辛苦了，感谢你在这段时间的付出。
[charslot(slot="m",name="avg_npc_1800_1#16$2",focus="m")]
[name="安多恩"]只是尽我所能。
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]这个小家伙还很脆弱。安多恩，带他回他母亲身边去吧。
[name="牧首"]我随后便去找你们。
[Dialog]
[charslot(slot="m",name="avg_npc_1800_1#16$2",focus="m")]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]牧首，您看起来有些虚弱......需要我护送您回去吗？
[charslot(slot="m",name="avg_npc_1777_1#1$1",focus="m")]
[name="牧首"]无妨，只是刚刚的心跳声仍在我的体内回响。
[name="牧首"]不止那位母亲，帕特里奇昂，我听到了不计其数的心跳在共鸣，几乎要震塌这座圣堂。
[name="牧首"]不论出身，不论种族，人们已经开始连结......但也有人已经拒绝了我们所展示的未来。
[name="牧首"]降生仪式可以到此为止了，不必让同胞们在此逗留，准备下一步的工作吧。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]我明白了。还请您去休息，这边剩下的事情交给我就好。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g2_baptismlobby",screenadapt="coverall")]
[Delay(time=2)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0.4, loop=true, channel="bse")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1.5)]
[Delay(time=2)]
[soundvolume(channel="bse",volume=0,fadetime=1)]
[Delay(time=2)]
[name="帕特里奇昂"]再次感谢各位来到育婴圣堂。
[name="帕特里奇昂"]不论诸位是否理解，又怎样看待先前牧首在峰会上提出的主张，这只木攀兽的降生与启圣，无疑都给予了我们更明晰的启示。
[name="帕特里奇昂"]关于如何跨越“国家”“种族”的隔阂，关于如何从根本上消弭仇恨、缔造和平......关于如何共同应对悬于头顶的灾异。
[name="帕特里奇昂"]以降生仪式为起点，第二届万国峰会将正式进入下一阶段——
[name="帕特里奇昂"]拉特兰将向所有萨科塔之外的种族分享光环！
[name="帕特里奇昂"]“愿主将属灵的恩典赐予每一人。”
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g1_nurserytemplesquare",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="l",name="avg_300_phenxi_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_213_mostma_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_213_mostma_1#1$1",focus="none")]
[name="能天使"]菲亚梅塔，莫斯提马，这边这边！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1041_angel2_1#3$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1811_1#8$2",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1811_1#8$2",focus="r")]
[name="蕾缪安"]......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_300_phenxi_1#3$1",focus="l")]
[charslot(slot="r",name="avg_213_mostma_1#1$1",focus="l")]
[name="菲亚梅塔"]蕾缪乐？
[name="菲亚梅塔"]你什么时候回来的？怎么也不跟我们说一声。
[charslot(slot="l",name="avg_300_phenxi_1#9$1",focus="l")]
[name="菲亚梅塔"]这身新衣服不错嘛，这副新手铐也......
[charslot(slot="l",name="avg_1041_angel2_1#5$1",focus="l")]
[charslot(slot="r",name="avg_npc_1811_1#8$2",focus="l")]
[name="能天使"]本来想过段时间给你们一个惊喜的，这不是......嘿嘿。
[name="能天使"]（试图挠头）
[Dialog]
[charslot]
[charslot(slot="l",name="avg_300_phenxi_1#9$1",focus="r")]
[charslot(slot="r",name="avg_213_mostma_1#12$1",focus="r")]
[name="菲亚梅塔"]蕾缪安，怎么回事？
[charslot(slot="l",name="avg_1041_angel2_1#5$1",focus="r")]
[charslot(slot="r",name="avg_npc_1811_1#11$2",focus="r")]
[name="蕾缪安"]......一两句话说不清楚。
[charslot(slot="l",name="avg_300_phenxi_1#9$1",focus="r")]
[charslot(slot="r",name="avg_213_mostma_1#7$1",focus="r")]
[name="莫斯提马"]要不，我帮你争取两分钟逃跑？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1041_angel2_1#9$1",focus="l")]
[charslot(slot="r",name="avg_npc_1811_1#11$2",focus="l")]
[Delay(time=2)]
[charslot(slot="l",name="avg_1041_angel2_1#3$1",focus="l")]
[multiline(name="能天使")]也行——
[charslot(slot="l",name="avg_1041_angel2_1#9$1",focus="l")]
[multiline(name="能天使",end=true)]还是别给我老姐添乱了，下次吧！
[charslot(slot="r",name="avg_npc_1811_1#1$2",focus="r")]
[name="蕾缪安"]......
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_1780_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="薇尔丽芙"]抱歉，我是不是打扰你们几位好友团聚了？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1041_angel2_1#1$1",focus="all")]
[charslot(slot="r",name="avg_npc_1811_1#8$2",focus="all")]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1811_1#8$2",focus="r")]
[name="蕾缪安"]前辈。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1780_1#1$1",focus="m")]
[name="薇尔丽芙"]蕾缪安枢机，你自己一个人就能够将嫌犯带回第七厅吗？
[charslot(slot="m",name="avg_npc_1780_1#3$1",focus="m")]
[name="薇尔丽芙"]还是说，需要支援......？毕竟试图破坏育婴圣堂，干涉万国峰会，可是干系重大！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1041_angel2_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1811_1#2$2",focus="r")]
[name="蕾缪安"]不放心的话，前辈你可以和我一起，或者让铳骑监督。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1780_1#3$1",focus="m")]
[name="薇尔丽芙"]别这么说话嘛。毕竟根据阿摩斯辅佐官的证词，你确实之前就在其他案发现场发现了蕾缪乐的踪迹......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_1041_angel2_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1811_1#5$2",focus="r")]
[name="蕾缪安"]你是想说，我试图包庇自己的妹妹？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1780_1#8$1",focus="m")]
[name="薇尔丽芙"]那倒是没有，毕竟都是间接证据，不足以说明你采取了什么行动。
[name="薇尔丽芙

... (全文16374字符)
```

### level_act42side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g1_laterano_cathedralfront",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$chill_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1810_1#10$1",duration=1)]
[delay(time=2)]
[Dialog]
[charslot(duration=0.3)]
[delay(time=0.5)]
那是圣席奥多尔综合学校建校以来最盛大的毕业典礼......不，那是整个拉特兰教育史上最盛大的毕业典礼！
[Dialog]
[PlaySound(key="$d_avg_firework_amb", volume=1, loop=true, channel="f")]
[PlaySound(key="$d_avg_wdnguitarstrum",volume=1,delay=2)]
[StopSound(channel="f", fadetime=8)]
[delay(time=2)]
十七发巨型烟花在天空炸开，十七岁的红发萨科塔放肆扫弦，开始了她的摇滚独唱会。声音响彻校园，震得附近教学楼的窗户都在动。
舞台附近的长椅上、圣像旁、水池边......到处都摆满了各式各样的苹果派，那是她为到场的听众们准备的礼物。
但是整个广场空空如也，红发萨科塔一个人弹琴，一个人唱歌，并没有一个老师或学生来捧她的场。
自己设计毕业典礼在拉特兰并不稀奇，但她毕竟还没到毕业的年龄，哪怕提前读完了大学的专业预科，还是没能获准立刻毕业。
但缺了仪式感可是罪过！大罪过！
教室里的学生们打开了窗户，远远地看着红发萨科塔忘情地弹琴，忘情地唱歌，直到最后一首。然后，他们看见了毕生难忘的画面——
[Dialog]
[PlaySound(key="$d_avg_electricguitar",volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_wheelscree", channel="wh",loop=true,volume=1)]
[PlaySound(key="$d_avg_carschant",volume=1,delay=0.2)]
[charslot(slot="m",name="avg_4188_confes_1#1$1",posfrom="60,90",posto="0,90",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",posfrom="0,90",posto="-100,90",duration=2)]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_4188_confes_1#1$1",posfrom="60,90",posto="0,90",duration=1)]
[Delay(time=1.5)]
[stopsound(channel="wh", fadetime=4)]
[charslot(slot="m",posfrom="0,90",posto="-100,90",duration=2)]
[charslot(duration=1.5)]
[Delay(time=3)]
[charslot]
红发萨科塔弹完了收尾的音符，鞠躬致谢，然后，校门在轰响中打开，上百辆自律告解车浩浩荡荡地开进校园。
在本应是宾客的位置，每一辆告解车都车门大敞，上百个声线各异的“车载电子告解师”，以最大的音量加入了红发萨科塔的演出。
不论是拉特兰规模最大的诵经团，还是最为喧闹的重金属乐队，都从没制造出过这样的响动！
终于，戍卫队赶来恢复教学秩序，他们连劝带推地试图让告解车们回归岗位。此时，骚乱的元凶却早已无影无踪......
只剩一条横幅伴着最后一枚烟花展开——
[Dialog]
[PlaySound(key="$d_avg_firework_huge", volume=1)]
[Delay(time=1.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=0.5)]
“热烈庆祝蕾缪乐开始她的冒险！”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="26_g9_laterano_street",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
蕾缪乐在拉特兰的接驳港停了下来。
[charslot(slot="m",name="avg_npc_1810_1#2$1",focus="m")]
[name="蕾缪乐"]哈，这里竟然也有一尊圣徒像欸！
[charslot(slot="m",name="avg_npc_1810_1#1$1",focus="m")]
[name="蕾缪乐"]真奇怪，为什么以前从来没注意到，这些雕像......还挺漂亮的！
[Dialog]
[charslot(duration=1)]
[delay(time=1.5)]
这是她第一次离开拉特兰，去没有光环的地方，找一些人、一些答案。
可能有很长一段时间，自己都不会回来，她没来由地想。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[Background(image="26_g3_laterano_cathedralballroom",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_1811_1#1$2")]
[charslot(slot="r",name="avg_1041_angel2_1#9$1")]
[delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="r",name="avg_1041_angel2_1#9$1",focus="r")]
[name="能天使"]老姐，他们居然肯让你来进行这场审讯。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]......还不是因为前面那七个枢机从你嘴里什么都没问出来。
[name="蕾缪安"]来，小乐，搭把手，把这个拆了。
[charslot(slot="r",name="avg_1041_angel2_1#3$1",focus="r")]
[multiline(name="能天使")]包这么严实——
[charslot(slot="r",name="avg_1041_angel2_1#6$1",focus="r")]
[multiline(name="能天使")]哇，水果千层挞？
[charslot(slot="r",name="avg_1041_angel2_1#3$1",focus="r")]
[name="能天使"]第七厅对待嫌疑犯可真够好的！
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]哪儿呀，这当然是我自己做的。喏，还有这个。
[name="蕾缪安"]......给。
[charslot(slot="r",name="avg_1041_angel2_1#3$1",focus="r")]
[name="能天使"]什么什么？
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]你的毕业证。
[charslot(slot="r",name="avg_1041_angel2_1#6$1",focus="r")]
[name="能天使"]——
[charslot(slot="l",name="avg_npc_1811_1#14$2",focus="l")]
[name="蕾缪安"]我醒来之后的某天，圣席奥多尔综合学校的负责人——也是我当年的老师——来看了我一趟，让我代为保管这个。
[name="蕾缪安"]虽然你当时的毕业申请没通过，但那场毕业典礼确实很好地证明了你具有足够优秀的专业能力。
[name="蕾缪安"]毕竟，如果不是对城际网络的防护模式特别熟悉，对告解车的程序逻辑了如指掌，哪能鼓动那么多告解车和你一起演出呢？
[name="蕾缪安"]所以学校在请示过教皇厅后，还是决定为你颁发毕业证书。
[charslot(slot="l",name="avg_npc_1811_1#10$2",focus="l")]
[name="蕾缪安"]祝贺你，小乐......虽然已经过了这么多年。
[charslot(slot="r",name="avg_1041_angel2_1#3$1",focus="r")]
[name="能天使"]嘿嘿，谢谢老姐。
[charslot(slot="l",name="avg_npc_1811_1#10$2",focus="l")]
[name="蕾缪安"]姐姐的信，你不可能没收到吧？
[charslot(slot="r",name="avg_1041_angel2_1#5$1",focus="r")]
[name="能天使"]呃......嗯。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]其实当初我和爸爸妈妈还打过赌，他们赌你上了大学会主修城际网络安全，以后会成为公证所最厉害的网络安全维护专家。
[name="蕾缪安"]但姐姐觉得你绝不会浪费自己的想象力，肯定会主修信仰辅助器械设计，以后会设计出震撼全城的新款告解车。
[name="蕾缪安"]结果你就那么离开了拉特兰。
[charslot(slot="r",name="avg_1041_angel2_1#9$1",focus="r")]
[name="能天使"]我可要说清楚哦，老姐，我一点都不觉得遗憾。
[name="能天使"]你又不是不知道，我从来不留遗憾，更不会让别人替我遗憾。
[charslot(slot="l",name="avg_npc_1811_1#1$2",focus="l")]
[name="蕾缪安"]不然你也不会那么着急地提前修完所有的专业预科课程，还搞了一场那样轰动的毕业典礼，对吧？
[charslot(slot="r",name="avg_1041_angel2_1#3$1",focus="r")]
[name="能天使"]哼哼。
[charslot(slot="l",name="avg_npc_1811_1#9$2",focus="l")]
[name="蕾缪安"]我还从莫斯提马那里问到了很多关于你的事情，你在龙门的工作、你的老板、你的同事。
[charslot(slot="l",name="avg_npc_1811_1#10$2",focus="l")]
[name="蕾缪安"]姐姐知道你去了叙拉古、萨尔贡，去了很多地方......
[name="蕾缪安"]姐姐也知道你每天都在和各种各样的人打交道，黑帮、警察、家族、王酋......忙得脚不沾地......
[charslot(slot="r",name="avg_1041_angel2_1#6$1",focus="r")]
[name="能天使"]怎么话到莫斯提马嘴里就变味儿了呢！
[charslot(slot="r",name="avg_1041_angel2_1#9$1",focus="r")]
[name="能天使"]哎呀，离开拉特兰后，我真的有在好好生活，也没有不开心啦。
[charslot(slot="r",name="avg_1041_angel2_1#10$1",focus="r")]
[name="能天使"]再说再说，那时候你在医院，不知道怎么受的伤，也不知道能不能醒，莫斯提马还偏偏一个字也不愿意说......
[charslot(slot="r",name="avg_1041_angel2_1#9$1",focus="r")]
[name="能天使"]我必须知道发生了什么！
[name="能天使"]你可是我老姐啊！
[charsl

... (全文29310字符)
```

### level_act42side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_1032_excu2_1#4$1",duration=1)]
[charslot(slot="r",name="avg_245_cello_1#7$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_245_cello_1#7$1",focus="r")]
[name="阿尔图罗"]看来我们扑了个空呢。
[charslot(slot="l",name="avg_1032_excu2_1#4$1",focus="l")]
[name="费德里科"]房间内很多地方都没有人活动的痕迹，摇椅、咖啡壶和铳靶这些他常用的器具已经积灰......
[name="费德里科"]终端上没有通讯记录或异常留言，暂时未能找到更多证据。
[charslot(slot="l",name="avg_1032_excu2_1#6$1",focus="l")]
[name="费德里科"]初步判断，教宗伊万杰利斯塔十一世，已经失踪半个月左右。
[charslot(slot="r",name="avg_245_cello_1#8$1",focus="r")]
[name="阿尔图罗"]......虽然已经有了心理准备，虽然和教宗阁下只有一面之缘，但真知道他出了事，还是......
[charslot(slot="l",name="avg_1032_excu2_1#4$1",focus="l")]
[name="费德里科"]阿尔图罗，给出解释。
[name="费德里科"]你对教宗阁下的行踪似乎有所了解。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.3, fadetime=2)]
[charslot]
[Background(image="31_g3_mini12_farmland", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.7, keep=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[PlaySound(key="$d_avg_grass",volume=0.6,delay=0.2)]
[charslot(slot="m",name="avg_npc_356_1#1$1",duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]又见面了，“拉特兰的糖果爷爷”。
[name="阿尔图罗"]不过，教皇厅的联合审理已经结束，您也签署了针对我的判决书。一位囚徒，不应该再有私下会见教宗阁下的机会。
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]考虑得怎么样了？
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]......
[name="阿尔图罗"]这么直接？我还以为您会说一些“饭后走走就到了这里”之类的玩笑话。
[charslot(slot="m",name="avg_245_cello_1#2$1",focus="m")]
[name="阿尔图罗"]关于我是否愿意成为所谓的“圣徒”，在罗德岛的时候，我们已经有过深入的交流——
[charslot(slot="m",name="avg_npc_356_1#10$1",focus="m")]
[name="伊万杰利斯塔十一世"]当然当然。
[name="伊万杰利斯塔十一世"]我还挺喜欢那艘船的，可惜相会的时间太短。我还记得那晚的霞光，和你演奏的那个很不“拉特兰”的调子......
[charslot(slot="m",name="avg_npc_356_1#9$1",focus="m")]
[name="伊万杰利斯塔十一世"]以及，你说的，希望我提供更多的证据。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]嗯。
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]孩子，还记得我说过的话吗？“我们所知的任何光亮都有寂灭如黯的那一天。”
[charslot(slot="m",name="avg_245_cello_1#11$1",focus="m")]
[name="阿尔图罗"]哈，印象很深。毕竟那是一句很有意思的表达。
[charslot(slot="m",name="avg_npc_356_1#2$1",focus="m")]
[name="伊万杰利斯塔十一世"]而这一天，快要来了......当然，只是我的预感。
[charslot(slot="m",name="avg_245_cello_1#8$1",focus="m")]
[name="阿尔图罗"]......
[Dialog]
[charslot]
教宗指了指自己头顶的光环。
[charslot(slot="m",name="avg_npc_356_1#7$1",focus="m")]
[name="伊万杰利斯塔十一世"]这段时间，它频频给予我警示，却不再回应我的任何发问。
[charslot(slot="m",name="avg_245_cello_1#8$1",focus="m")]
[name="阿尔图罗"]这是，什么意思？
[charslot(slot="m",name="avg_npc_356_1#7$1",focus="m")]
[name="伊万杰利斯塔十一世"]换句话说，我们光辉的律法突然变得不可被解读了。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]我只会拉琴，阁下。
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]当然当然，解经是教宗的工作。
[name="伊万杰利斯塔十一世"]现在工作遇到了麻烦，我会去想办法解决。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]那您需要我做什么？
[charslot(slot="m",name="avg_npc_356_1#2$1",focus="m")]
[name="伊万杰利斯塔十一世"]保持警惕......我不清楚具体会发生什么，所以我只能这样提醒你。
[charslot(slot="m",name="avg_npc_356_1#8$1",focus="m")]
[name="伊万杰利斯塔十一世"]如果整座圣城的灯都熄灭，相信你所想的“理解”，你所想的“情感”，你所想的无所保留的，纯粹而坦诚的“交流”。
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]你这样的异类，到那时或许是一剂良药，或许是一剂毒药......但总归会让事情有些转机。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]听起来，我没有什么拒绝的理由。
[charslot(slot="m",name="avg_245_cello_1#11$1",focus="m")]
[name="阿尔图罗"]不过，拉特兰的异类，可不止我一个。
[charslot(slot="m",name="avg_npc_356_1#9$1",focus="m")]
[name="伊万杰利斯塔十一世"]当然，接下来我会去联系其他圣徒。
[charslot(slot="m",name="avg_npc_356_1#8$1",focus="m")]
[name="伊万杰利斯塔十一世"]......但愿时间还来得及。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="26_g4_laterano_cathedralliving", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[charslot(slot="l",name="avg_1032_excu2_1#10$1")]
[charslot(slot="r",name="avg_245_cello_1#1$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.6, fadetime=1.5)]
[Delay(time=1)]
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]所以，你才会那么早对周遭发生的事情产生怀疑。
[charslot(slot="r",name="avg_245_cello_1#1$1",focus="r")]
[name="阿尔图罗"]也不全是如此，费迪。
[name="阿尔图罗"]一个人的心声哪怕没有变奏，但那些增补和缺失的章节融入得太过自然，我很难感受不到。席德佳修女就是个很好的例子。
[charslot(slot="r",name="avg_245_cello_1#10$1",focus="r")]
[name="阿尔图罗"]我更在意的是，教宗阁下还没有来得及找你，意外便已经发生了。
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]局势太过复杂，整个拉特兰都陷入了难以理解的灾异中，其程度与我们在巫王的帕维永中所经历的等同。
[name="费德里科"]我们需要支援。
[charslot(slot="r",name="avg_245_cello_1#11$1",focus="r")]
[name="阿尔图罗"]幸好，我带了我的琴。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g12_firearmsworkshop", screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1779_1#1$2",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1779_1#1$2",focus="m")]
[name="梵里妮"]老师？
[Dialog]
[charslot]
没有人回答。
梵里妮在铳械工坊转了一圈，没有发现老师的身影，他的眼药水在操作台上放着，甚至连盖子都还没盖回去。
[charslot(slot="m",name="av

... (全文22491字符)
```

### level_act42side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g4_nurseryindoor",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1784_1#11$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_370_1#1$1",duration=0.7)]
[delay(time=2)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]二位，就是这里了，请稍作休息。
[charslot(slot="m",name="avg_npc_1784_1#11$1",focus="m")]
[name="席德佳"]......我以为，配合调查阿尔图罗小姐越狱的事情，应该要去公证所或者大教堂。
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]领二位来的铳骑有事先走了。他托我转告二位，阿尔图罗的事情，请不必担心。
[name="保育员"]一直以来，兰登修道院的各位都在尽责尽职地守护圣城，我们不会因为一个犯人越狱，就过多苛责。
[charslot(slot="m",name="avg_npc_370_1#1$1",focus="m")]
[name="紧张的修女"]呼，那就好那就好。
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]我们请二位来，是有别的事情要商量。
[charslot(slot="m",name="avg_npc_1784_1#11$1",focus="m")]
[name="席德佳"]这里好多——
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]您希望换个安静点的地方吗？
[charslot(slot="m",name="avg_npc_1784_1#15$1",focus="m")]
[name="席德佳"]不，我的意思是，这间育婴室里......为什么全是黎博利？
[Dialog]
[charslot(duration=0.3)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_365_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_367_1#1$1",duration=1)]
[delay(time=2)]
[charslot(duration=0.3)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1254_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_1255_1#1$1",duration=1)]
[delay(time=2)]
[charslot(duration=0.3)]
[delay(time=0.5)]
[playsound(key="$d_avg_comfortbell", volume=1)]
席德佳看向前方，着装各异的黎博利们或站或坐，没多少人说话，唯有安抚铃的声音稳定地响着。
几百？成千？上万？席德佳数不清了，或许一整个城市的黎博利都在眼前。
这间育婴室有这么大吗？不，怎样的场合，需要聚集如此多的黎博利？
[charslot(slot="m",name="avg_npc_1784_1#3$1",focus="m")]
[name="席德佳"]保育员先生，你们是不是还有一间房里全是佩洛，一间房里全是菲林，一间房里全是鲁珀......
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]您很聪明。
[name="保育员"]我们也为堕天使和萨卡兹准备了专门的房间。
[charslot(slot="m",name="avg_npc_1784_1#6$1",focus="m")]
[name="席德佳"]......呃，您很坦然嘛。
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]毕竟育婴圣堂并没有在做什么见不得人的事情。
[name="保育员"]降生仪式的最后，教皇厅已经宣布，萨科塔将向所有种族分享光环。以种族为单位，操作起来是最方便的。
[charslot(slot="m",name="avg_npc_1784_1#3$1",focus="m")]
[name="席德佳"]......
[charslot(slot="m",name="avg_npc_370_1#1$1",focus="m")]
[name="紧张的修女"]......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0.4, loop=true, channel="cr")]
[SoundVolume(volume=0, channel="cr",fadetime=3.5)]
[charslot(slot="m",name="avg_npc_365_1#1$1",focus="m")]
[name="黎博利公民"]保育员先生，你是说，我们真的也能拥有光环？也能像萨科塔那样互相感受？
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]正如您在降生仪式上感受那只小木攀兽的心跳。
[charslot(slot="m",name="avg_npc_1784_1#6$1",focus="m")]
[name="席德佳"]为什么呢？
[charslot(slot="m",name="avg_npc_1786_1#1$1",focus="m")]
[name="保育员"]什么？
[charslot(slot="m",name="avg_npc_1784_1#6$1",focus="m")]
[name="席德佳"]我说，我为什么，要拥有光环呢？
[Dialog]
[StopSound(channel="cr", fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="61_g3_nurserytemplecorridor", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_1781_1#3$1")]
[charslot(slot="r",name="avg_4194_rmixer_1#1$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]所以说，把我带到这里，压根不是为梵里妮的事情，而是因为......我是个黎博利？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]是的。
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]很快，我也能拥有你脑袋顶上的这圈日光灯？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]进去吧，潘。
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]哟，看来我没有拒绝的权利呀。而且，听起来是一件大好事，对吧？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]起码对你的眼睛有好处。
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="潘格尼尼"]那可不止吧！
[name="潘格尼尼"]要是当初我有光环，是不是就能知道你把吉雅赶出拉特兰的时候，你那铁皮脑袋底下是什么心情了？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]我知道你埋怨我，潘。
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]很有自知之明。
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]如果没发生那件事，你或许不会沦落到如今的地步。
[name="帕特里奇昂"]拉特兰千百年的历史上，有很多人尝试过复刻典籍中描述的那把恐怖的大口径转管遗产铳......成功的只有你。
[name="帕特里奇昂"]那种默认使用者能承受远超常规铳械五倍后坐力的设计，真是天才又疯癫......
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]行了，你在没穿戴铳骑甲胄之前，就成功试验了我的设计，你是在变相夸自己是天生的铳骑吗？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]我当时只觉得自己是你天生的搭档。你、我、吉雅，从小学到大学，我们一直都是最好的朋友。
[name="帕特里奇昂"]可我正式成为铳骑的第一项任务，却是把吉雅驱逐出拉特兰......
[name="帕特里奇昂"]在那之后，你辞去了铳骑专属制铳师的职务，在我不知道的地方开了一家小工坊，如今又......
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]我是自愿退休的，行不行？*拉特兰俚语*的“制铳圣堂”，要是你们萨科塔都把制铳当作生产薯片，那我还掺和什么？
[name="潘格尼尼"]不是萨科塔有罪，是吗？吉雅要被赶出去，我要被套上光环......就没有黎博利能在拉特兰好好活着？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]那件事和吉雅是不是黎博利没有关系。哪怕她是萨科塔，她感染了矿石病，拉特兰也不容——
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="潘格尼尼"]你知道个屁！
[name="潘格尼尼"]不就是什么“拉特兰的秩序”“拉特兰的纯洁”吗？这些话我从你嘴里听过多少次了？
[name="潘格尼尼"]但这话你自己信吗？你想想吉雅是怎么一个人死在外面的，你*拉特兰俚语*信吗？
[charslot(slot="r",name="avg_4194_rmixer_1#1$1",focus="r")]
[name="帕特里奇昂"]......
[charslot(slot="l",name="avg_npc_1781_1#3$1",focus="l")]
[name="潘格尼尼"]我承认，我自己曾经信。直到那个时候，帕特里奇昂......
[name="潘格尼尼"]我们曾一起宿醉，一起玩铳，一起哭一起笑，我们自诩全拉特兰没有人的酒杯碰得比我们的响。
[name="潘格尼尼"]但直到吉雅的背影消失在荒野尽头，你就那么从我旁边转身回拉特兰的时候，我才意识到......
[name="潘格尼尼"]我们从来没有真正交流过。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0,

... (全文14456字符)
```

### level_act42side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g8_laterano_dwelling",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1811_1#1$1",focus="m")]
[name="蕾缪安"]请进。
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="aw")]
[stopsound(fadetime=2, channel="aw")]
[charslot(slot="m",name="avg_npc_1783_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]蕾缪安枢机......
[charslot(slot = "m", name = "avg_npc_1811_1#1$1",focus="m")]
[name="蕾缪安"]得改口了哦。
[name="蕾缪安"]我已经被禁足，原则上教皇厅应该不允许任何人前来探视才对啊。
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]报备过了。
[name="阿摩斯"]我刚刚接任，在事务交接上难免有一些仓促，来请教前任枢机，再正常不过。
[charslot(slot = "m", name = "avg_npc_1811_1#10$1",focus="m")]
[name="蕾缪安"]哈哈，你适应得很快嘛，阿摩斯枢机。
[charslot(slot = "m", name = "avg_npc_1811_1#1$1",focus="m")]
[name="蕾缪安"]我记得你之前可是说，自己是个没什么追求的人。
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]蕾缪安枢......小姐，我不是来趁机炫耀什么的，我们之间本来也不是什么勾心斗角的上下级关系吧。
[charslot(slot = "m", name = "avg_npc_1811_1#1$1",focus="m")]
[name="蕾缪安"]抱歉。
[name="蕾缪安"]但如果你是来问蕾缪乐的行踪，我已经在前几轮询问中说过很多次——确实无可奉告。
[charslot(slot="m",name="avg_npc_1783_1#2$1",focus="m")]
[name="阿摩斯"]不，我想问您另外一个问题。
[charslot(slot="m",name="avg_npc_1783_1#10$1",focus="m")]
[name="阿摩斯"]蕾缪安小姐，您愿意牺牲自己的事业，只是为了保护妹妹，还是，您真的相信她说的......
[name="阿摩斯"]从降生仪式，到万国峰会......拉特兰最近发生的所有事都很不对劲。我们像是，患上了某种疾病。
[charslot(slot = "m", name = "avg_npc_1811_1#6$1",focus="m")]
[name="蕾缪安"]......
[charslot(slot = "m", name = "avg_npc_1811_1#14$1",focus="m")]
[name="蕾缪安"]对我来说，这是一码事。
[Dialog]
[charslot(slot="m",name="avg_npc_1783_1#10$1",focus="m")]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1783_1#2$1",focus="m")]
[name="阿摩斯"]我、我想请您看一样东西。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_devicebeep",volume=1)]
[delay(time=1)]
阿摩斯点开了自己的终端，递给蕾缪安。
[charslot(slot = "m", name = "avg_npc_1811_1#11$1",focus="m")]
[name="蕾缪安"]这是？
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]万国信使的申请函。我希望能够成为万国信使，负责玻利瓦尔一带的政府沟通任务。
[charslot(slot = "m", name = "avg_npc_1811_1#11$1",focus="m")]
[name="蕾缪安"]你想离开拉特兰？为什么？
[charslot(slot="m",name="avg_npc_1783_1#5$1",focus="m")]
[name="阿摩斯"]我和我妻子......
[name="阿摩斯"]当年我们大吵了一架，不欢而散。等我再回到家，她已经去出任务了，前往卡兹戴尔附近的荒野，处理萨卡兹侵扰商队的事情。
[name="阿摩斯"]她一直是这样的脾气，听不进去别人的话。那时候是冬天，我估摸着她春天才能回来，我还来得及做点什么......
[charslot(slot="m",name="avg_npc_1783_1#2$1",focus="m")]
[name="阿摩斯"]后来的事情，我也告诉过您，堕天啊驱逐啊什么的。
[charslot(slot="m",name="avg_npc_1783_1#5$1",focus="m")]
[name="阿摩斯"]第七厅专司情报、国安和外交，工作上有一些便利，我花了很长的时间，终于打听到了她的下落。于是我就想着......
[charslot(slot = "m", name = "avg_npc_1811_1#11$1",focus="m")]
[name="蕾缪安"]我能理解。
[name="蕾缪安"]可是，你刚刚说的怪事是指？
[charslot(slot="m",name="avg_npc_1783_1#7$1",focus="m")]
[name="阿摩斯"]我知道万国信使的选拔标准有多严格，凭我的能力，实在是......所以这份申请，一直躺在我的邮箱里。直到......
[charslot(slot = "m", name = "avg_npc_1811_1#11$1",focus="m")]
[name="蕾缪安"]你接任第七厅枢机后，批准了自己的那份申请？
[charslot(slot="m",name="avg_npc_1783_1#10$1",focus="m")]
[name="阿摩斯"]是、是。
[name="阿摩斯"]通知我接任枢机一职的时候，帕特里奇昂阁下说我从来都只是缺乏一个契机......
[name="阿摩斯"]虽然他肯定另有所指，但我这没出息的脑子，第一时间想到的就是这件事。
[name="阿摩斯"]可是，我点过批准之后，这份申请就......消失了。没有收到任何申请被驳回的消息，没有任何记录可查。
[name="阿摩斯"]它就那么消失在了我的终端里，像是、像是从来没有存在过。
[charslot(slot = "m", name = "avg_npc_1811_1#3$1",focus="m")]
[name="蕾缪安"]——！
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]流程上，那份申请不论我批准与否都不会被通过，我不可能被允许立刻辞去枢机职务，成为万国信使。
[charslot(slot="m",name="avg_npc_1783_1#8$1",focus="m")]
[name="阿摩斯"]更何况所有万国信使都已经被召回拉特兰，哪怕真的当上了，我也没机会去见奥罗拉。
[name="阿摩斯"]批准那份申请对我来说，连弥补都算不上，那就只是一丝微不足道的慰藉。
[charslot(slot="m",name="avg_npc_1783_1#7$1",focus="m")]
[name="阿摩斯"]谁会想着把这微不足道的慰藉也给抹消？
[name="阿摩斯"]对我来说，这足以成为一条线索......让我怀疑这个拉特兰是否真实。
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]或许......您妹妹想做的事情，是正确的。
[charslot(slot = "m", name = "avg_npc_1811_1#8$1",focus="m")]
[name="蕾缪安"]阿摩斯枢机，你有向其他人提起这件事吗？
[charslot(slot="m",name="avg_npc_1783_1#4$1",focus="m")]
[name="阿摩斯"]没、没有。整整一个晚上，我都没法合眼......想来想去，也只有您可以分享了。
[charslot(slot = "m", name = "avg_npc_1811_1#6$1",focus="m")]
[name="蕾缪安"]阿摩斯枢机，我在想，这是否是什么新的审讯手段。
[charslot(slot="m",name="avg_npc_1783_1#8$1",focus="m")]
[name="阿摩斯"]您可以相信我，蕾缪安小姐。
[name="阿摩斯"]我们都有自己真正在意的东西......也都不多。
[charslot(slot = "m", name = "avg_npc_1811_1#1$1",focus="m")]
[name="蕾缪安"]很有意思的发言，阿摩斯先生。
[charslot(slot="m",name="avg_npc_1783_1#1$1",focus="m")]
[name="阿摩斯"]哦对了，今天，育婴圣堂会举行一场更为盛大的降生仪式。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g4_nurseryindoor", screenadapt="coverall", block=true)]
[backgroundTween(xFrom=100, yFrom=0, xTo=-100, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=35, block=false)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15,grad = true,fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15,grad = true,fadetime=0.1)]
[delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
“每个人终其一生，都在为死亡这件事做准备。”
哪怕在潮石镇那样被饥荒和瘟疫冲刷得一无所有的地方，也会有年迈的老人在闭眼前一刻，舔舔干裂的嘴唇，悠悠说出类似的话。
这是一句老生常谈，只不过对有些人来说是饮恨的总结，而对另一些人来说是不怀遗憾的感喟。但它们的前提是一样的——
死亡，是生命的终点。
[Dialog]
[curtain(fadetime=1)]
[delay(time=2)]
[Background(image="61_g4_nurseryindoor",screenadapt="coverall",fadetime=1.5,block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1800_1#2$1",duration=1)]
[delay(time=2)]
[Dialog]
[charslot]
[name="？？？"]——
[Dialog]
[charslot(slot="m",name="avg_npc_1790_1#1$1",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="m",name="avg_npc_1790_1#1$1",focus="m")]
[name="木攀兽"]（疑惑地拱头）
[name="木攀兽"]（紧张地扇翅）
[charslot(sl

... (全文18490字符)
```

### level_act42side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g9_laterano_street",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_bicyclegallop", volume=1, loop=true, channel="a")]
[StopSound(channel="a", fadetime=2.5)]
[charslot(slot="l",name="avg_4179_monstr_1#6$1",posfrom="70,0",posto="0,0",duration=1)]
[charslot(slot="r",name="avg_4188_confes_1#2$1",posfrom="100,0",posto="0,0",duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_4179_monstr_1#6$1",focus="l")]
[name="Mon3tr"]博士，这边。
[name="Mon3tr"]往里挪挪，让这辆甜品车在前面。
[Dialog]
[charslot(slot="l",name="avg_4179_monstr_1#6$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(duration=1)]
[delay(time=1.5)]
[Dialog]
[PlaySound(key="$d_avg_transpthrn", volume=1)]
[charslot(slot="m",name="avg_npc_1794_1#1$1",duration=1)]
[delay(time=2)]
[Dialog]
[charslot]
[PlaySound(key="$d_avg_crowdrun", volume=0.8)]
[charslot(slot="l",name="avg_npc_1788_1#1$1",posfrom="170,0",posto="0,0",duration=0.8)]
[charslot(slot="r",name="avg_npc_1789_1#1$1",posfrom="170,0",posto="0,0",duration=0.8)]
[delay(time=1.2)]
[charslot(duration=0.7)]
[delay(time=1)]
[PlaySound(key="$d_gen_soldiersrun", volume=0.6)]
[charslot(slot="l",name="avg_npc_371_1#1$1",posfrom="80,0",posto="0,0",duration=0.7)]
[charslot(slot="r",name="avg_npc_371_1#1$1",posfrom="80,0",posto="0,0",duration=0.7)]
[delay(time=1.2)]
[charslot(duration=1)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_4179_monstr_1#6$1",posfrom="50,0",posto="-70,0",afrom=0,ato=1,duration=1)]
[charslot(slot="r",name="avg_4188_confes_1#2$1",posfrom="50,0",posto="100,0",afrom=0,ato=1,duration=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_4179_monstr_1#3$1",focus="l")]
[name="Mon3tr"]总算能够喘口气了。
[Dialog]
[charslot]
[Decision(options="辛苦。;这辆甜品车是谁的？", values="1;2")]
[Predicate(references="1;2")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1793_1#3$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1793_1#3$1",focus="m")]
[name="缺牙的小女孩"]姐姐，你也是慕名来参加仪式的吧！
[charslot(slot="m",name="avg_npc_1793_1#3$1",focus="m")]
[name="缺牙的小女孩"]要、要尝尝我的冰淇淋吗？
[charslot(slot="m",name="avg_npc_1793_1#3$1",focus="n")]
不容Mon3tr拒绝，小女孩已经开心地将手中的冰淇淋筒塞到了她手中。
[charslot(slot="m",name="avg_npc_1793_1#3$1",focus="m")]
[name="缺牙的小女孩"]是在、在拉特兰其他地方绝对吃不到的新口味哦——
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4179_monstr_1#6$1",focus="l")]
[charslot(slot="r",name="avg_4188_confes_1#2$1",focus="l")]
[name="Mon3tr"]（我可以控制住她，不会惊动其他人。）
[charslot(slot="l",name="avg_4179_monstr_1#6$1",focus="n")]
Mon3tr一边警惕地向你提议，一边无意识地尝了一口冰淇淋。
[charslot(slot="l",name="avg_4179_monstr_1#8$1",focus="l")]
[name="Mon3tr"]好吃欸......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1793_1#1$1",focus="m")]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1793_1#3$1",focus="m")]
[delay(time=1)]
[Dialog]
[charslot]
[Decision(options="咳咳，孩子，能告诉我你的名字吗？", values="1")]
[Predicate(references="1")]
[charslot(slot="l",name="avg_npc_1793_1#3$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_transpthrn", volume=1)]
[charslot(slot="r",name="avg_npc_1794_1#1$1",posfrom="-100,0",posto="0,0",duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1793_1#10$1",focus="l")]
[name="缺牙的小女孩"]它已经替我回答了，告解师。
[charslot(slot="l",name="avg_npc_1793_1#11$1",focus="l")]
[name="伊蒂达"]嘀嗒嘀嘀嗒，我叫伊蒂达。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4179_monstr_1#10$1",focus="m")]
[name="Mon3tr"]你用甜品车的音效给自己取名？
[charslot(slot="m",name="avg_npc_1793_1#1$1",focus="m")]
[name="伊蒂达"]什么嘛。当然是我根据自己的名字定制了它的出餐音效啊！
[Dialog]
[charslot(slot="m",name="avg_npc_1793_1#1$1",focus="n")]
[Decision(options="伊蒂达，你认识刚刚过去的戍卫队吗——;伊蒂达，你不害怕这个姐姐吗——", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_npc_1793_1#5$1",focus="m")]
[name="伊蒂达"]哇，我从来没听过告解车有这样的声线欸！
[charslot(slot="m",name="avg_4179_monstr_1#11$1",focus="m")]
[name="Mon3tr"]最新款。
[Dialog]
[charslot(slot="m",name="avg_4179_monstr_1#11$1",focus="n")]
[Decision(options="（叹气）;她好像完全没有在意。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_4179_monstr_1#12$1",focus="m")]
[name="Mon3tr"]伊蒂达，你刚刚在替我们打掩护？
[charslot(slot="m",name="avg_npc_1793_1#10$1",focus="m")]
[name="伊蒂达"]嗯......因为整个拉特兰都需要做出改变！
[name="伊蒂达"]你们也是这样想的，对吧？！
[charslot(slot="m",name="avg_4179_monstr_1#1$1",focus="m")]
[name="Mon3tr"]......
[Dialog]
[charslot]
[Decision(options="......", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_npc_1793_1#7$1",focus="m")]
[name="伊蒂达"]难、难道是我自作多情吗？姐姐，你可是第一个夸我做的无糖气泡水口味冰淇淋好吃的人！
[charslot(slot="m",name="avg_4179_monstr_1#5$1",focus="m")]
[name="Mon3tr"]（......难怪那么解渴。）
[charslot(slot="m",name="avg_npc_1793_1#7$1",focus="m")]
[name="伊蒂达"]爸爸妈妈说得对，这是一条很难走的路......可是，我终于取得了一点小成绩了！
[charslot(slot="m",name="avg_4179_monstr_1#5$1",focus="m")]
[name="Mon3tr"]什么......意思？
[charslot(slot="m",name="avg_npc_1793_1#6$1",focus="m")]
[name="伊蒂达"]“甜食连接了每一个拉特兰人”——可是摄取过量糖分的话，不仅仅是长蛀牙那么简单，我们头顶上的光环也会被慢慢蛀掉的！
[name="伊蒂达"]爸爸是牙医，每次他说起这番话，大家都以为他是为了给诊所揽生意。
[charslot(slot="m",name="avg_npc_1793_1#9$1",focus="m")]
[multiline(name="伊蒂达")]可这段时间，我头顶的光环，唔，就像我刚掉的蛀牙一样，让我感到不舒服......
[charslot(slot="m",name="avg_npc_1793_1#12$1",focus="m")]
[multiline(name="伊蒂达")]我相信，这是主给我的启示！
[charslot(slot="m",name="avg_npc_1793_1#11$1",focus="m")]
[name="伊蒂达"]所以我要身体力行，一点点改善拉特兰人的饮食习惯。重建彼此之间的联系，从推广无糖冰淇淋做起！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4188_confes_1#2$1",focus="m")]
[playsound(key="$d_avg_robotwalk", volume=1)]
[delay(time=1.5)]
[charslot]
[Decision(options="很伟大的事业，伊蒂达。;客人，您愿意支持这位公民的理想吗？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_4179_monstr_1#3$1",focus="m")]
[name="Mon3tr"]......
[charslot(slot="m",name="avg_4179_monstr_1#10$1",focus="m")]
[name="Mon3tr"]介意我们和你多走一段路吗？我想多听你讲讲......光环与蛀牙之间的关系。
[charslot(slot="m",name=

... (全文47587字符)
```

### level_act42side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_churchbell",loop=true, channel="bell", volume=1)]
[StopSound(channel="bell", fadetime=6)]
[Delay(time=2)]
钟声。
经久不绝的钟声传遍整座城市。它清晰，稳定，为迷途者指引方向。
传说，圣徒们苦行长路后建起石塔，借钟声驱散魔鬼，尔后拉特兰城拔地而起，洁白的城墙历风雨而不倒，那口钟也就此沉默了数千年。
此刻它再次鸣响——距离上次回应一位混血萨科塔女孩的歌声，仅仅过去了两年多的时间。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="26_g10_laterano_roof", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_1801_1#2$1")]
[charslot(slot="r",name="avg_npc_1802_1#2$1")]
[Delay(time=1)]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[bgeffect]
[charslot(slot="l",name="avg_npc_1801_1#2$1",focus="n")]
[name="安多恩"]嘶......
[charslot(slot="l",name="avg_npc_1801_1#2$1",focus="l")]
[name="恐慌的小孩"]呜呜，保育员叔叔......
[charslot(slot="r",name="avg_npc_1802_1#2$1",focus="r")]
[name="惊惧的小孩"]你、你疼吗？
[Dialog]
[charslot]
[name="？？？"]别乱动，好不容易替你包扎好的。
[Dialog]
[charslot(slot="m",name="avg_npc_1800_1#2$2 ",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1800_1#2$2 ",focus="m")]
[name="安多恩"]帕蒂亚？
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_npc_357_1#5$1 ",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_357_1#5$1 ",focus="m")]
[name="帕蒂亚"]我们赶到育婴圣堂的时候，你已身负重伤，我们只来得及带出你，和这些正在找你的孩子。
[charslot(slot="m",name="avg_npc_1800_1#6$2 ",focus="m")]
[name="安多恩"]别哭，吉赛尔，洛米雅......只是一场噩梦而已，现在我们已经醒了。
[charslot(slot="m",name="avg_npc_357_1#10$1 ",focus="m")]
[name="帕蒂亚"]梦吗？梦里受的伤可不会带到现实。
[charslot(slot="m",name="avg_npc_1800_1#10$2 ",focus="m")]
[name="安多恩"]......其他的兄弟姐妹们呢？
[charslot(slot="m",name="avg_npc_357_1#1$1 ",focus="m")]
[name="帕蒂亚"]在附近警戒......看来你终于恢复了记忆，想听他们叫一声“先导”吗？
[charslot(slot="m",name="avg_npc_1800_1#2$2 ",focus="m")]
[name="安多恩"]抱歉，帕蒂亚。
[name="安多恩"]明明你们一直在试图叫醒一个再次迷路的人。
[charslot(slot="m",name="avg_npc_357_1#6$1 ",focus="m")]
[name="帕蒂亚"]那么，安多恩，你为什么扔下寻路者？
[name="帕蒂亚"]离开安布罗修修道院后，我们在荒野上短暂歇脚，按照原定行程，队伍很快便会穿过伊比利亚的边境，重回那片你熟悉的土地。
[name="帕蒂亚"]我们都已经和审判庭的人搭上了线，你却突然消失得无影无踪......
[charslot(slot="m",name="avg_npc_1800_1#3$2 ",focus="m")]
[name="安多恩"]于我而言，这场梦境从那时便已开始。
[charslot(slot="m",name="avg_npc_357_1#10$1 ",focus="m")]
[name="帕蒂亚"]什么意思？
[charslot(slot="m",name="avg_npc_1800_1#6$2 ",focus="m")]
[name="安多恩"]只是一个念头，一个凭空出现的念头。
[name="安多恩"]它催促我转身，不顾一切地转身，重回拉特兰。
[charslot(slot="m",name="avg_npc_357_1#10$1 ",focus="m")]
[name="帕蒂亚"]你的意思是，你并没有真的遇见那个瞎眼的家伙，不是为了带孩子而和她一起回到拉特兰......你像是，被什么东西蛊惑了？
[charslot(slot="m",name="avg_npc_357_1#6$1 ",focus="m")]
[name="帕蒂亚"]*拉特兰俚语*，这些话听起来像是一个发癫的神棍会说的。
[charslot(slot="m",name="avg_npc_1800_1#3$2 ",focus="m")]
[name="安多恩"]......
[charslot(slot="m",name="avg_npc_1800_1#6$2 ",focus="m")]
[name="安多恩"]我知道这难以理解，连我自己也未曾明了......
[charslot(slot="m",name="avg_npc_357_1#2$1 ",focus="m")]
[name="帕蒂亚"]算了，难以理解的事情多了。
[charslot(slot="m",name="avg_npc_357_1#6$1 ",focus="m")]
[name="帕蒂亚"]你，还有那座圣堂！你们想要往所有人脑袋上安光环，把我们变成连感情都没法自己做主的怪物！
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_357_1#6$1 ",focus="m")]
[name="帕蒂亚"]算了，最终你还是靠自己回到了现实。要不是你搞出那么大动静，破坏了降生仪式，整个拉特兰估计都还在做梦。
[Dialog]
[charslot]
[name="？？？"]二者的界限在一开始便已混淆，他在梦境中的所作所为，应受到同等评判。
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#1$1 ",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_1032_excu2_1#1$1 ",focus="m")]
[name="费德里科"]公证所执行者，费德里科。安多恩·雅迦坦哲罗思，我看过你的卷宗。
[charslot(slot="m",name="avg_npc_357_1#10$1 ",focus="m")]
[name="帕蒂亚"]雅迦......安多恩，这是你的姓吗？
[charslot(slot="m",name="avg_npc_1800_1#1$2 ",focus="m")]
[name="安多恩"]......
[charslot(slot="m",name="avg_1032_excu2_1#10$1 ",focus="m")]
[name="费德里科"]在第一届万国峰会期间造成混乱后，你已被教皇厅驱逐。如今你私自返回拉特兰，并策划参与了所谓的降生仪式。
[name="费德里科"]拉特兰此时此刻的混乱，你应负一定的责任，接受第一、第五、第六、第七厅的联合调查。
[charslot(slot="m",name="avg_npc_1800_1#3$2 ",focus="m")]
[name="安多恩"]......
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="r",name="avg_npc_357_1#6$1", posfrom = "-100,-50", posto = "-100,-50",afrom=0,ato=0,duration=0,focus="r")]
[charslot(slot="r",name="avg_npc_357_1#6$1",action="zoom",poszoom="0.5,0.5",duration=0,focus="r",isblock=true)]
[charslot(slot="r",afrom=0,ato=1,duration=0.7,focus="r",isblock=true)]
[Delay(time=0.5)]
[name="帕蒂亚"]喂，这家伙已经受了重伤，你没看出来吗？
[name="帕蒂亚"]而且眼下有比抓他更重要的事情吧！
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_npc_1782_1#12$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1782_1#12$1",focus="m")]
[name="奥罗拉"]执行者，要帮忙吗？你带我们进城，我们帮你打架。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1800_1#3$2 ",focus="r")]
[charslot(slot="r",name="avg_npc_357_1#10$1", posfrom = "-100,-50", posto = "-100,-50",afrom=0,ato=0,duration=0,focus="r")]
[charslot(slot="r",name="avg_npc_357_1#10$1",action="zoom",poszoom="0.5,0.5",duration=0,focus="r",isblock=true)]
[charslot(slot="r",afrom=0,ato=1,duration=0,focus="r",isblock=true)]
[name="帕蒂亚"]你们是......
[Dialog]
[charslot(duration=0.3)]
[Delay(time=0.4)]
[charslot(slot="m",name="avg_4187_graceb_1#17$1",focus="m")]
[name="努艾达"]那、那个——
[charslot(slot="m",name="avg_npc_1782_1#12$1",focus="m")]
[name="奥罗拉"]努艾达，怎么了？
[charslot(slot="m",name="avg_4187_graceb_1#3$1",focus="m")]
[name="努艾达"]你们看看那边！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[Sticker(id="st1", multi = true, text="“小乐，得到守护铳，意味着你迈进人生的新阶段啦！”", x=300,y=330, alignment="center", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n“嗯嗯！姐

... (全文33623字符)
```

### level_act42side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g1_laterano_cathedralfront",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_213_mostma_1#8$1",duration=0.7)]
[charslot(slot="r",name="avg_300_phenxi_1#7$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_213_mostma_1#8$1",focus="l")]
[name="莫斯提马"]菲亚梅塔，先把手从扳机上挪开。
[name="莫斯提马"]你现在的臭脸，好像不射出几枚榴弹气就没法消一样。
[charslot(slot="r",name="avg_300_phenxi_1#7$1",focus="r")]
[name="菲亚梅塔"]......一想到刚刚做了那么恶心的梦，气就不打一处来。
[charslot(slot="l",name="avg_213_mostma_1#1$1",focus="l")]
[name="莫斯提马"]恐怕不完全是梦哦。
[name="莫斯提马"]看那边，虽然隔得很远......
[charslot(slot="r",name="avg_300_phenxi_1#3$1",focus="r")]
[multiline(name="菲亚梅塔")]育婴圣堂居然还在......
[charslot(slot="r",name="avg_300_phenxi_1#7$1",focus="r")]
[multiline(name="菲亚梅塔")]莫斯提马，走，去医院。
[charslot(slot="r",name="avg_300_phenxi_1#6$1",focus="r")]
[name="菲亚梅塔"]不管刚刚经历的是不是梦，我们都得赶紧确认——
[Dialog]
[charslot]
[name="？？？"]真感动啊菲亚梅塔，你第一时间就想到了我。
[Dialog]
[playsound(key="$d_avg_electrcwhlchrrll",volume=1)]
[charslot(slot="m",name="avg_4193_lemuen_1#10$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_300_phenxi_1#2$1",focus="m")]
[multiline(name="菲亚梅塔")]蕾缪安？
[charslot(slot="m",name="avg_300_phenxi_1#9$1",focus="m")]
[multiline(name="菲亚梅塔")]太好了，你没事。
[charslot(slot="m",name="avg_213_mostma_1#11$1",focus="m")]
[name="莫斯提马"]......你的腿？
[charslot(slot="m",name="avg_4193_lemuen_1#1$1",focus="m")]
[name="蕾缪安"]有点疼。
[charslot(slot="m",name="avg_213_mostma_1#11$1",focus="m")]
[name="莫斯提马"]怎么了？
[charslot(slot="m",name="avg_4193_lemuen_1#1$1",focus="m")]
[name="蕾缪安"]在梦里一直跑来跑去累到了，这么一比，还是坐着舒服......好了好了，你们俩不用紧张。
[charslot(slot="m",name="avg_300_phenxi_1#3$1",focus="m")]
[name="菲亚梅塔"]这到底是怎么回事？
[charslot(slot="m",name="avg_4193_lemuen_1#2$1",focus="m")]
[name="蕾缪安"]（摇头）我只是在接到枢机任命的第二天，正常去上班。或许是在我走出家门的那一刻，或许是在我看见育婴圣堂的那一刻......
[charslot(slot="m",name="avg_4193_lemuen_1#12$1",focus="m")]
[name="蕾缪安"]说不清是什么时候，我已不再身处现实，一切都那么自然而然地发生了。
[charslot(slot="m",name="avg_300_phenxi_1#2$1",focus="m")]
[name="菲亚梅塔"]......
[charslot(slot="m",name="avg_4193_lemuen_1#11$1",focus="m")]
[name="蕾缪安"]菲亚梅塔，你怎么了？
[Dialog]
[charslot]
[delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_1800_1#1$3",duration=1)]
[delay(time=2)]
[charslot(duration=0.3)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="sw")]
[PlaySound(key="$d_avg_highheelfts",volume=0.7,channel="aw",loop=false)]
[stopsound(fadetime=2, channel="sw")]
[stopsound(channel="aw",fadetime=2)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",duration=1)]
[charslot(slot="r",name="avg_245_cello_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1800_1#1$3",focus="m")]
[name="安多恩"]......各位。
[charslot(slot="m",name="avg_213_mostma_1#4$1",focus="m")]
[name="莫斯提马"]队......
[charslot(slot="m",name="avg_300_phenxi_1#2$1",focus="m")]
[name="菲亚梅塔"]——
[charslot(slot="m",name="avg_300_phenxi_1#7$1",focus="m")]
[name="菲亚梅塔"]你、你还留着——
[charslot(slot="m",name="avg_300_phenxi_1#6$1",focus="m")]
[name="菲亚梅塔"]这是什么意思？！
[charslot(slot="m",name="avg_npc_1800_1#1$3",focus="m")]
[name="安多恩"]一位友人替我保存至今。菲亚梅塔，你有一位非常善良的后辈。
[charslot(slot="m",name="avg_npc_1800_1#3$3",focus="m")]
[name="安多恩"]她对我说，这不是能轻易丢掉的东西。也许今天，我就会抵达终点......以此身衣袍前行，或许亦是注定。
[charslot(slot="m",name="avg_300_phenxi_1#7$1",focus="m")]
[name="菲亚梅塔"]你......
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]安多恩干系重大，各位的纠葛并非此刻需要优先处理的事项......
[charslot(slot="m",name="avg_4193_lemuen_1#1$1",focus="m")]
[name="蕾缪安"]费德里科，好久不见。
[name="蕾缪安"]我知道你的身份和行事风格，根据教皇厅的工作准则，圣徒在应对紧急灾害时享有最高权限......但请给我们一点时间。
[charslot(slot="m",name="avg_1032_excu2_1#6$1",focus="m")]
[name="费德里科"]......
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]请尽快。
[stopmusic(fadetime=1.5)]
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]......
[Dialog]
[PlaySound(key="$d_avg_highheelfts",volume=0.7,channel="aw2",loop=false)]
[stopsound(channel="aw2",fadetime=2)]
[charslot(duration=1)]
[delay(time=2)]
[Dialog]
[playMusic(key="$wasteland_loop", volume=0.6)]
[gridbg(imagegroup="47_g15_eveningglow_L1/47_g15_eveningglow_R1/47_g15_eveningglow_L2/47_g15_eveningglow_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-640,fadetime=1.5)]
[largebgtween(duration = 60,yFrom = 360, yTo = 720,block = false)]
[delay(time=2)]
[name="蕾缪安"]我们四个上次像这样面对面站在一起，还是那次出任务吧？
[name="莫斯提马"]......十年了。
[name="莫斯提马"]我们抵达那个地宫，菲亚梅塔接到其他小队的求援信息离开，安多恩在入口临时修改战术布置。
[name="莫斯提马"]我们笑着分吃了最后一块栗子司康饼......那是小队一直以来的习惯。那天的场景，我记得很清楚。
[name="菲亚梅塔"]在此之前，我们多么快乐......我本以为那段时光会永远延续下去，没有人想过后面的事情会发展成那样......
[name="菲亚梅塔"]而你，安多恩，你造成了这一切，却不愿说出半句真相或者忏悔。
[name="安多恩"]......我们的短暂相逢，或许只是人生中的意外。
[name="安多恩"]那是一个......难能可贵的意外。
[name="安多恩"]我确实毁了它......以我也未曾预料的方式。
[name="安多恩"]菲亚梅塔，你钟爱那段时光，我全都明了。你的爱真切赤诚，能烫热你周遭的每一颗心。我......
[name="安多恩"]我一直想要感谢你一件事。我是从你身上学会喜欢拉特兰的。
[name="安多恩"]但在同一个瞬间我就知道，我一定会伤害你，会毁坏你珍爱的事物。
[name="安多恩"]我就是这样的恶徒。以你的正义，你应当恨我。
[name="菲亚梅塔"]......安多恩，你在故意激怒我吗？
[name="菲亚梅塔"]我是否恨你，由我决定，不由你决定。
[name="安多恩"]我很明白这一点，亦很感谢这一点。得遇你这样一位朋友，我非常幸运。
[name="菲亚梅塔"]......
[name="菲亚梅塔"]去做你的事吧。
[name="菲亚梅塔"]但你记住，我不会原谅你，永远不会。
[name="安多恩"]......
[Dialog]
[delay(time=1)]
[name="蕾缪安"]安多恩，这两位要带你去大教堂，对吗？
[name="安多恩"]是我要带他们去，蕾缪安。
[Dialog]
[Image(image="61_i26",screenadapt="coverall",fadetime=3.5,block=true)]
[delay(time=2)]
[gridbg]
[name="蕾缪安"]所以，接下来的路，依然是你确定要走的？
[name="安多恩"]当然。
[name="蕾缪安"]很危险？
[name="安多恩"]更多的是未知。
[name="蕾缪安"]你没想过停下？
[name="安多恩"]无论是当年攻击你的队长，还是梦境里那个狂妄天真的保育员......我的疑惑、我的偏执、我的过错，推着我走到这里。
[name="安多恩"]我已不可能停下。
[name="蕾缪安"]明白了。
[name="蕾缪安"]此时此刻的拉特兰，确实很难再称得上是“乐园”。
[name="蕾缪安"]那个怪物正在城里横行，到处都是她孵育出来的怪东西，没人知道到底是怎么回事，接下来还会发生什么..

... (全文39530字符)
```

### level_act42side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g6_pcsderivativemaze",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[name="安多恩"]（嘶——）
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]......暂时只能进行一些紧急处理。
[name="费德里科"]安多恩，无节制地使用光学类源石技艺，已经对你的视神经造成了不可逆的损伤。
[name="费德里科"]我没有修复此类创伤的资质和能力......条件允许的话，你需要就医。
[Dialog]
[charslot(duration=0.3)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_cloakmovement", volume=0.8)]
[charslot(slot="m",name="avg_npc_1800_1#6$5",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1800_1#10$5",focus="m")]
[name="安多恩"]无妨。
[name="安多恩"]路已经在脚下显形，目不能视，也不影响我们前进。
[charslot(slot="m",name="avg_npc_1800_1#1$5",focus="m")]
[name="安多恩"]请沿着地面上的光标走吧......这座迷宫的构成太过复杂，我的源石技艺坚持不了多久。
[Dialog]
[charslot(duration=0.3)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_deeplion", volume=0.6, channel="monster", loop=false)]
[StopSound(channel="monster", fadetime=5)]
[charslot(slot="l",name="avg_npc_1792_1#1$1",posfrom="50,0",posto="-60,0",duration=1)]
[charslot(slot="r",name="avg_npc_1792_1#1$1",posfrom="100,0",posto="50,0",duration=1)]
[Delay(time=2)]
[charslot(slot="l",posfrom="-60,0",posto="-130,0",afrom=1,ato=0,duration=1)]
[charslot(slot="r",posfrom="50,0",posto="0,0",afrom=1,ato=0,duration=1)]
[Delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="m")]
[name="费德里科"]......
[name="费德里科"]走。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="61_g13_pcsdoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_labamb", volume=0.6, loop=true, channel="a")]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step1",loop=false)]
[stopsound(channel="step1",fadetime=3)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1800_1#6$5",focus="m")]
[name="安多恩"]就是这里了。
[name="安多恩"]无论灾异是否由此而起，门后的事物或许都能给我们答案。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]跟上，阿尔图罗。
[Dialog]
[charslot]
[StopSound(channel="a", fadetime=2)]
[delay(time=1)]
费德里科没有得到回应。
从在育婴圣堂外追到阿尔图罗以来，对方一直都对他的种种安排相当配合。
但此刻，黑发的萨科塔就站在几步之外，优雅地拨弄着琴弦，并没有跟上来的意思。
[charslot(slot="m",name="avg_245_cello_1#11$1",focus="m")]
[name="阿尔图罗"]这一次，我真的要越狱了，费迪。
[name="阿尔图罗"]安多恩受了伤，你只有一个人，没有比此刻更好的时机了，不是吗？
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="m")]
[name="费德里科"]阿尔图罗，我们已经抵达真相的门口，你应该清楚该行为缺乏意义。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]真相......意义......？
[name="阿尔图罗"]......或许吧。
[name="阿尔图罗"]费迪，你是最优秀的执行者，“行走的条律”，除教宗外第一位受封的圣徒......你可是“送葬人”。
[name="阿尔图罗"]你的“理性”，你的“冷酷”，甚至你对这两种品质产生的怀疑，都指向律法的存续本身。
[charslot(slot="m",name="avg_245_cello_1#11$1",focus="m")]
[name="阿尔图罗"]如果圣城本身即是如此，或许只有你能听懂祂会说什么，哈哈。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]......
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]至于安多恩先生......很抱歉，虽然并非我的本意，但刚刚在你施放源石技艺的时候，我无意中触摸了你的心声。
[name="阿尔图罗"]很复杂，比我认识的许多人都复杂。但......又确实没多特别。
[name="阿尔图罗"]太过偏执的主旋律，让它们统统变成了同一首曲子的改编或者往复。它们诉说着——
[charslot(slot="m",name="avg_245_cello_1#8$1",focus="m")]
[name="阿尔图罗"]你的起点和终点都在拉特兰。
[name="阿尔图罗"]只不过，那时你或许将孤身一人。
[charslot(slot="m",name="avg_245_cello_1#3$1",focus="m")]
[name="阿尔图罗"]啊，请原谅我的冒犯。
[charslot(slot="m",name="avg_npc_1800_1#12$5",focus="m")]
[name="安多恩"]（颔首）阿尔图罗小姐，您所谓的“冒犯”，何尝不是我趁机进行了一次别样的告解呢？
[charslot(slot="m",name="avg_npc_1800_1#11$5",focus="m")]
[name="安多恩"]至于您最后的话，我更愿意视之为祝福......那说明，我真的抵达了终点。
[charslot(slot="m",name="avg_245_cello_1#11$1",focus="m")]
[name="阿尔图罗"]哈哈，有趣的回答。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_highheelfts",volume=1,channel="step2",loop=false)]
[stopsound(channel="step2",fadetime=1.2)]
阿尔图罗转过了身。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[image(image="61_i16",screenadapt="coverall",xScale=1.1,yScale=1.1,fadetime=1,y=-30,block=true)]
[delay(time=0.5)]
[playMusic(intro="$lab_intro",key="$lab_loop", volume=0)]
[musicvolume(volume=0.4, fadetime=3)]
[ImageTween(yFrom=-30,yTo=0,xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[name="阿尔图罗"]但不是每个人都对拉特兰的“真相”和“意义”那么有执念的。
[name="阿尔图罗"]起码，那对我毫无吸引力。
[name="阿尔图罗"]刚刚我已经窥见了祂的一角，门后面......是一台机器，对吧？
[name="安多恩"]是。
[name="阿尔图罗"]既然如此，答案注定是无聊的。
[name="阿尔图罗"]想想我们在崔林特尔梅的经历，费迪。
[name="阿尔图罗"]一场同等级的灾异正在侵袭城市，人们在其中迷失或挣扎......此刻，拉特兰有几百万值得倾听的心声。
[name="费德里科"]......
[name="费德里科"]阿尔图罗，你现在转身，意味着你将独自面对迷宫里的敌人。
[name="阿尔图罗"]本来也需要有人帮你们把那些家伙引开，不是吗？
[name="费德里科"]你的守护铳已经遗失，你缺乏基本的防卫手段。
[name="阿尔图罗"]或许，我可以想办法让他们成为我的听众？
[name="阿尔图罗"]别紧张，费迪，我也是拉特兰钦定的危险分子呀。
[Dialog]
[delay(time=1)]
[name="费德里科"]......
[name="费德里科"]现状评级，高危；存活概率，低；执行者决定......放行。
[name="阿尔图罗"]哈哈。
[name="阿尔图罗"]时间不等人，两位。没想过转身的话，就不用为我送别了。
[name="阿尔图罗"]那么，再见，我亲爱的弟弟。
[Dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_higheldshosfts",volume=0.6,channel="step2",loop=false)]
[SoundVolume(volume=0, channel="step2",fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[image]
[StopSound(channel="step2", fadetime=1)]
[Background(image="61_g9_catastrophicalley",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$dar

... (全文25419字符)
```

### level_act42side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="61_g7_pcsserverroom",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
并无繁复的仪式，并无冗长的流程。
费德里科注视着冰冷的信息端口。只在光环明灭间，他就瞥见景象万千。
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#9$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_1032_excu2_1#9$1",focus="m")]
[name="费德里科"]......
[charslot(slot="m",name="avg_1032_excu2_1#5$1",focus="m")]
[name="费德里科"]光环可以如此快速地传输这种量级的信息？
[name="费德里科"]医学文献或信仰典籍均不曾记载过类似的现象。光环自古以来都只被用于传递简单的情绪......“共感”。
[name="费德里科"]为什么？
[Dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[PlaySound(key="$d_avg_scan", volume=1)]
[Sticker(id="st1", multi = true, text="交互对象信息承载阈值不足，需在交互前预先进行信息转译。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n若在交互时进行即时信息转译，可能导致交互对象的信息处理器受损，陷入暂时或永久性失能。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n安多恩·雅迦坦哲罗思正处于此种状态。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
费德里科向身侧看去。
安多恩颓唐地跪倒在地，眼目浑浊。干结的血迹以一种令人不安的方式勾勒出他的面容。
片刻，他挣扎着抬起头，再一次将头顶的光环对准机器的信息端口......
而后再一次无力地垂下头去。
[stopmusic(fadetime=1.5)]
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]安多恩，按照这台机器——或是律法——的说法，你已无法再承受更多信息的负载。
[name="费德里科"]......此前过度使用源石技艺已经对你的身体造成了严重影响。
[name="费德里科"]请立刻停止尝试接入这台机器，避免对自己造成永久性的失能。
[Dialog]
[charslot]
[delay(time=0.5)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1800_1#9$4",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1800_1#9$4",focus="m")]
[name="安多恩"]更多信息......？
[charslot(slot="m",name="avg_npc_1800_1#5$4",focus="m")]
[name="安多恩"]不，我还什么也没看见，什么也没知晓！
[name="安多恩"]但不该如此......怎会如此？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="安多恩"]十多年来，这些苦痛，这些罪孽......难道只为见证神的沉默？！
[charslot(slot="m",name="avg_npc_1800_1#9$4",focus="m")]
[name="安多恩"]费德里科，我不会停下。
[Dialog]
[charslot]
安多恩·雅迦坦哲罗思再一次倔强地向机器昂起光环。
[Dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.3, block=true)]
[charslot]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=0.1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1790_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_1800_1#7$2",duration=1)]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_npc_1800_1#7$2",focus="r")]
[name="安多恩"]......孩子。
[name="安多恩"]这是另一场梦？
[charslot(slot="l",name="avg_npc_1790_1#1$1",focus="l")]
[name="木攀兽"]不是哦。律法不会为你单独构建一个梦境。
[name="木攀兽"]费德里科选择用律法的语言与律法交流，你却无论如何都不能理解，也不愿接受那种冰冷的语言。
[name="木攀兽"]是你自己一字一句地，将那语言“翻译”成了我们现在所见的这幅景象。
[charslot(slot="r",name="avg_npc_1800_1#7$2",focus="r")]
[name="安多恩"]如果不是梦，那你为什么......还活着？
[charslot(slot="l",name="avg_npc_1790_1#1$1",focus="l")]
[name="木攀兽"]因为你想让我活着，保育员先生。
[charslot(slot="r",name="avg_npc_1800_1#2$2",focus="r")]
[name="安多恩"]我亲手引爆了炸弹......你就在那里。
[charslot(slot="l",name="avg_npc_1790_1#1$1",focus="l")]
[name="木攀兽"]你不只想让我活着，你对我还有很多期望呢。
[name="木攀兽"]你希望我能活得快乐。你希望我能冲破育婴圣堂的穹顶，自己去定义天空的高度。
[name="木攀兽"]你希望看见我的羽毛在晴空中闪耀，看见我的趾爪钳着活蹦乱跳的鼷兽。
[name="木攀兽"]你在城际网络上查找过泰拉最高的树在哪里，不是吗？你想着，既然是“木攀兽”，比起安抚铃一定更喜欢爬真正的树。
[charslot(slot="r",name="avg_npc_1800_1#10$2",focus="r")]
[name="安多恩"]......我查过。萨米的山脊上，玻利瓦尔的树海间，都有像是从传说里破土而出的巨树，比启示石塔还要粗，比大教堂还要高......
[charslot(slot="r",name="avg_npc_1800_1#6$2",focus="r")]
[name="安多恩"]我确实想过要带你去。我只在城际网络上看过其他木攀兽在树冠顶层对着太阳鸣叫的模样。
[name="安多恩"]我想看到你也能像那样畅快地鸣叫。
[charslot(slot="l",name="avg_npc_1790_1#1$1",focus="l")]
[name="木攀兽"]呜，那事情是从哪里开始出错的呢？
[name="木攀兽"]你是从什么时候开始，不再把我当作一个真实的生命？
[charslot(slot="r",name="avg_npc_1800_1#1$2",focus="r")]
[name="安多恩"]......你知道的，不是吗？
[charslot(slot="l",name="avg_npc_1790_1#1$1",focus="l")]
[name="木攀兽"]那场葬礼，我母亲的葬礼。
[name="木攀兽"]没关系的，保育员先生。跟我走吧，这一次，我们不会再留下遗憾。
[charslot(slot="r",name="avg_npc_1800_1#7$2",focus="r")]
[name="安多恩"]什么意思？那场葬礼，还在举办吗？
[charslot(slot="l",name="avg_npc_1790_1#1$1",focus="l")]
[name="木攀兽"]葬礼是永远都不会结束的呀。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[musicvolume(volume=0.3, fadetime=2)]
[charslot]
[Background(image="61_g7_pcsserverroom",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="m")]
[name="费德里科"]他已不再答话。
[name="费德里科"]......和教宗阁下一样的症状？
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="不同。安多恩·雅迦坦哲罗思仍然适格，并且正在处理前置信息。", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n费德里科·吉亚洛，对你的前置信息同步已完成。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n现在，协助完成转化程序。",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_1032_excu2_1#5$1",focus="m")]
[name="费德里科"]......
[Dialog]
[charslot]
费德里科曾对一些现象产生过疑虑，因一些行为而感到困扰，但他从未质疑过律法。
毕竟，圣徒践行律法，执行者维护律法，天经地义。
但此时此刻，面对律法本身，他只感到困惑。
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]我仍有疑问。
[name="费德里科"]律法的最终目的在于为一切生物与非生物赋予光环，我已知悉。
[name="费德里科"]但选取万国峰会作为实现这一目的的途径，是否也是律法的裁定？
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, blo

... (全文35714字符)
```

### level_act42side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g9_catastrophicalley",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[PlaySound(key="$d_avg_warfire_loop", volume=1, loop=true, channel="w")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_armour",volume=0.6)]
[PlaySound(key="$d_gen_walk_n",volume=1,delay=0.1)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[Dialog]
[charslot]
[StopSound(channel="w", fadetime=1.5)]
[delay(time=1)]
“圣徒”拖动巨大的身躯，行走在队伍的最前面，那个叫蕾缪乐的萨科塔仍在上蹿下跳，变魔术般地掏出一把把铳，向着她倾泻火力......
但“圣徒”仍然回头看了一眼。
[Dialog]
[charslot(slot="m",name="avg_npc_1778_1#1$1",afrom=0,ato=0.6,duration=1.5)]
[delay(time=2)]
她头顶的光环闪烁，哪怕隔着那么远的距离，帕特里奇昂仍清晰地听到了对方的“声音”。
毫无疑义，共感在加强，这说明这场漫长的旅程越来越靠近终点。
[name="“圣徒”"]帕特里奇昂，将你的挚友暂时交给其他的同胞吧，我们无需为他致哀。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]圣徒......
[charslot(slot = "m", name = "avg_npc_1778_1#1$1",afrom=0.6,ato=0.6,focus="m")]
[name="“圣徒”"]还记得那只木攀兽的幼崽吗？
[name="“圣徒”"]若我们行至终点，拉特兰将复现生命的奇迹——一切奇迹。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]您是说？
[charslot(slot = "m", name = "avg_npc_1778_1#1$1",afrom=0.6,ato=0.6,focus="m")]
[name="“圣徒”"]所以，向前走吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="61_g8_catastrophicsquare",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
浩浩荡荡的队伍经过一尊又一尊圣像，一座又一座铳械工坊，城市就这么一点一点被点亮。
帕特里奇昂沉默地向前走着。
[Dialog]
[name="？？？"]站......站住。
[Dialog]
[charslot(slot="m",name="avg_npc_1779_1#13$4",duration=1)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_sldrpllgn", volume=1)]
[delay(time=1)]
[charslot]
年轻的制铳师学徒逆着人流走来，最终在帕特里奇昂面前站定。面对这个比自己高出许多的铳骑，梵里妮举起了铳。
队伍从他们身侧经过，但没人往这边看一眼。梵里妮紧咬着嘴唇，尽量控制自己的手臂不要颤抖。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[name="帕特里奇昂"]啊，你是那个学徒？
[charslot(slot="m",name="avg_npc_1779_1#9$4",focus="m")]
[name="梵里妮"]老师......在哪？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]他......
[charslot(slot="m",name="avg_npc_1779_1#7$4",focus="m")]
[name="梵里妮"]老师警告我。所以在梦里，我、我......藏在工坊。醒来后，我也犹豫了很久......
[name="梵里妮"]现在的你......很可怕，拉特兰很可怕，我不清楚发生了什么，我连守护铳都还没有......
[name="梵里妮"]可我不能躲着、等着......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]所以，你为自己做了这把铳，然后来阻拦我？
[charslot(slot="m",name="avg_npc_1779_1#4$4",focus="m")]
[name="梵里妮"]嗯。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]真勇敢。
[name="帕特里奇昂"]可是孩子，看到这支队伍了吗？我们在孕育一个奇迹，而几乎所有的拉特兰人都参与其中......
[name="帕特里奇昂"]这并不“可怕”。
[charslot(slot="m",name="avg_npc_1779_1#8$4",focus="m")]
[name="梵里妮"]（摇头）和我，没关系。
[name="梵里妮"]我说话，不太会......想不到更、更糟糕的词......
[name="梵里妮"]老师，我唯一亲人......
[name="梵里妮"]我和拉特兰，唯一，联系。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]唯一的联系啊......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[MusicVolume(volume=0.3, fadetime=2)]
[Character]
[Background(image="61_g9_catastrophicalley",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="帕特里奇昂"]潘，既然你在梦境里没能成功长出光环，为什么会在队伍里？
[Dialog]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="n")]
[name="潘格尼尼"]混进来，当然是为了能找机会弄死你。
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="n")]
[name="潘格尼尼"]那个狙击手，是你曾经的学生吧？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="n")]
[name="潘格尼尼"]很难过？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="n")]
[name="潘格尼尼"]和吉雅走的时候比呢？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="n")]
[name="潘格尼尼"]你还要听那个怪物的，继续护着这支队伍往前？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[Dialog]
[charslot]
[name="潘格尼尼"]别以为我不懂你在想什么。
[name="潘格尼尼"]五十年前的拉特兰，让你不得不驱逐一个感染了的黎博利......十年前的拉特兰，让你不得不驱逐一个堕天了的铳骑......
[name="潘格尼尼"]甚至现在你的孙女，也有太多偏执的想法，说不定哪天也会......
[name="潘格尼尼"]所以，你渴望一个更好的拉特兰？
[name="潘格尼尼"]那个拉特兰会像个医术突然精进的医生一样，能够治疗矿石病，能够修补性格里的缺陷，能够让所有人毫无保留地接纳彼此？
[name="潘格尼尼"]这样，所有你经历过的离别就都不会再发生？
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]......
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="潘格尼尼"]咳咳......帕特里奇昂，你可真是个懦夫啊！
[name="潘格尼尼"]离别就像是化了的冰淇淋和报废的铳。可不管怎么样，冰淇淋总会化，铳也总会报废，不是吗？
[name="潘格尼尼"]哪怕没法阻止，你也可以在那时候送上祝福，哪怕只是一句再见......
[name="潘格尼尼"]你又不像梵里妮那样有语言障碍，让自己少一些遗憾的方法，很难找吗？
[Dialog]
[delay(time=1)]
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]别说了，坚持住！
[Dialog]
[charslot]
[CameraShake(duration=0.3, xstrength=10, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="潘格尼尼"]坚持个屁，咳咳，这可是......能洞穿铳骑盔甲的子弹......
[name="潘格尼尼"]别动我，让我把话说完，不然我死得更快......
[charslot(slot="m",name="avg_4194_rmixer_1#1$1",focus="m")]
[name="帕特里奇昂"]好、好......
[Dialog]
[charslot]
[name="潘格尼尼"]你这是什么语气？帕特里奇昂，别在那想一些矫情的事！
[name="潘格尼尼"]你以为我为什么要救你？
[name="潘格尼尼"]别跟我说什么灾异、危机、拉特兰该何去何从......
[name="潘格尼尼"]如果拉特兰真要毁灭，难道我们就只能去指望一个不知道从哪儿蹦出来的怪物？一种我们从来没有想象过的生活？
[name="潘格尼尼"]奥罗拉、菲亚梅塔，还有那么多你认识的拉特兰人......这些联系，在你看来那么脆弱吗？
[name="潘格尼尼"]*拉特兰俗语*，你可是铳骑啊！拉特兰最优秀的铳骑！
[CameraShake(duration=0.5, xstrength=20, ystrength=25, vibrato=30, randomness=90,

... (全文63674字符)
```

### level_act42side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act42side/MT01.mp4")]
```

### level_act42side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="26_g1_laterano_cathedralfront",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1798_1#3$1",duration=1.5)]
[Delay(time=2.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="咳咳，我祈祷！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="祈祷法柏尔区中心医院生病的叔叔阿姨们能够康复！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="祈祷爸爸妈妈姐姐没病没灾，永远健康快乐！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="祈祷主常在！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="祈祷属灵的光永远笼罩拉特兰！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
“蕾缪乐，实验不是结束了吗？”
“你还不知道啊，调查员今天来学校告诉我们结果啦，还特地带了水果挞当礼物呢！”
“法柏尔区中心医院的那两组病人都在今天出院了......唔，也就是说，他们的康复情况，和我们这两个月的祈祷没有关系，哈哈。”
“调查员让我们不要难过，说那本身就只是第六厅的社会实验而已。”
[Dialog]
[charslot(slot="l",name="avg_npc_1798_1#1$1",posfrom="200,0",posto="200,0",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[Delay(time=2.5)]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="若祈祷无用——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那我们因何祈祷？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Blocker(a=0.6, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="56_g7_tailorshop",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_paper1", volume=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_npc_692_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_691_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_691_1#1$1",focus="r")]
[name="西西里夫人"]又一封有关新沃尔西尼的简报。
[name="西西里夫人"]这半年来，它已经和十七座移动城市建立了贸易联系，几乎没有一刻停下来，像一只不知疲倦的凶豕兽......
[name="西西里夫人"]当然，它也顺便将新的种子带往了整个叙拉古。
[charslot(slot="l",name="avg_npc_692_1#1$1",focus="l")]
[name="阿格尼尔"]听你的语气，你鼓励新沃尔西尼和叙拉古的其他城市往来，但不打算为他们推广《新都市管理法案》的行为背书？
[charslot(slot="r",name="avg_npc_691_1#1$1",focus="r")]
[name="西西里夫人"]阿格尼尔，是你从狂欢节回来后，告诉我那些年轻人还需要更多考验。
[charslot(slot="l",name="avg_npc_692_1#1$1",focus="l")]
[name="阿格尼尔"]......好像是。
[charslot(slot="r",name="avg_npc_691_1#1$1",focus="r")]
[name="西西里夫人"]特尔尼城传来消息，鲁珀坎有些不寻常的动作。
[charslot(slot="r",name="avg_npc_691_1#6$1",focus="r")]
[name="西西里夫人"]金色的女皇最近政令不断，而另一位已经很久不曾露面了......我们的邻居似乎正急于寻求某些改变。
[name="西西里夫人"]其实不止莱塔尼亚，这片大地的新苗头已经够多了。叙拉古不该再花更多时间在“家族事务”上。
[charslot(slot="l",name="avg_npc_692_1#1$1",focus="l")]
[name="阿格尼尔"]嗯嗯。
[charslot(slot="r",name="avg_npc_691_1#1$1",focus="r")]
[name="西西里夫人"]你一副随时会睡过去的样子。
[charslot(slot="l",name="avg_npc_692_1#5$1",focus="l")]
[name="阿格尼尔"]快到我午休的时间了。
[charslot(slot="r",name="avg_npc_691_1#5$1",focus="r")]
[name="西西里夫人"]这块料子怎么样？
[name="西西里夫人"]给你定做一身套装？这家店的裁缝手艺不错。
[charslot(slot="l",name="avg_npc_692_1#5$1",focus="l")]
[name="阿格尼尔"]哈哈，不用了。
[charslot(slot="r",name="avg_npc_691_1#5$1",focus="r")]
[name="西西里夫人"]还是习惯穿着这身修士服？
[charslot(slot="l",name="avg_npc_692_1#5$1",focus="l")]
[name="阿格尼尔"]我是神父，西西里。
[charslot(slot="r",name="avg_npc_691_1#5$1",focus="r")]
[name="西西里夫人"]但是这座城市没有教堂。你离开拉特兰已经快七十年了吧？
[charslot(slot="l",name="avg_npc_692_1#5$1",focus="l")]
[name="阿格尼尔"]六十八年。萨科塔对自我身份的认同与我们对甜品的热爱同样持久。
[charslot(slot="r",name="avg_npc_691_1#1$1",focus="r")]
[name="西西里夫人"]可你从没想过回去看看。不过也没什么必要就是了，城墙依然洁白，人们依然快乐，乐园不会有变化......
[name="西西里夫人"]不然你当年也不会随我来到叙拉古。
[charslot(slot="l",name="avg_npc_692_1#1$1",focus="l")]
[name="阿格尼尔"]不好说......
[charslot(slot="r",name="avg_npc_691_1#1$1",focus="r")]
[name="西西里夫人"]哦？
[charslot(slot="l",name="avg_npc_692_1#1$1",focus="l")]
[name="阿格尼尔"]最近握守护铳时手总是有点抖，说不定是我在圣城的老房子漏水了之类的......
[multiline(name="阿格尼尔")]我们都是上个时代的人了，西西里。你知道老家伙对一些事情的直觉向来准确......
[charslot(slot="l",name="avg_npc_692_1#2$1",focus="l")]
[multiline(name="阿格尼尔",end=true)]啊哈——
[charslot(slot="r",name="avg_npc_691_1#5$1",focus="r")]
[name="西西里夫人"]你还是去那边的沙发上睡会儿吧。
[name="西西里夫人"]等付完这块料子的定金，或许我们可以换个地方好好谈谈。
[charslot(slot="l",name="avg_npc_692_1#5$1",focus="l")]
[name="阿格尼尔"]抱歉抱歉。
[Dialog]
[charslot(slot="l",name="avg_npc_692_1#5$1",focus="l")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1,channel="1")]
[charslot(slot="l",posfrom="0,0",posto="-150,0",duration=2.5,isblock=true)]
[stopsound(channel="1")]
[charslot(slot="l",focus="l")]
[name="阿格尼尔"]Zzz~
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1,channel="1")]
[charslot(slot="l",afrom=1,ato=0,duration=1.5,isblock=false)]
[charslot(slot="l",posfrom="-150,0",posto="-300,0",duration=2.5,isblock=true)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=0.6, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="l",focus="none")]
[name="惊慌的学徒"]这是怎么了，您刚刚是站着睡着了吗？神父，神父，您没事吧？
[name="阿格尼尔"]嘶——
[Dialog]
[stopmusic(fadetime=2)]
[charslot(slot="r",name="avg_npc_691_1#6$1",focus="r")]
[Delay(time=1.5)]
[charslot(slot="r",posfrom="0,0",posto="-200,0",duration=2.5,isblock=true)]
[name="西西里夫人"]......
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g9_modernoffice",screenadapt

... (全文27720字符)
```

### level_act42side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g10_laterano_roof",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1784_1#15$1",duration=1.5)]
[delay(time=2.5)]
[name="席德佳"]等等，执行者先生，所以你压根没想过将阿尔图罗小姐带回兰登修道院？
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]我没有表达过这样的意图。
[charslot(slot="m",name="avg_npc_1784_1#15$1",focus="m")]
[name="席德佳"]那我就带她回兰登修道院了。
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]我还需要借助阿尔图罗确认一些事情。
[charslot(slot="m",name="avg_npc_1784_1#15$1",focus="m")]
[name="席德佳"]......
[charslot(slot="m",name="avg_npc_1784_1#15$1",focus="none")]
[name="？？？"]费德里科，不能这样欺负一位修女哦！
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_372_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot]
[playsound(key="$d_gen_soldiersrun",volume=1,channel="1")]
[charslot(slot="l",name="avg_npc_371_1#1$1",afrom=0,ato=1,duration=1)]
[charslot(slot="r",name="avg_npc_371_1#1$1",afrom=0,ato=1,duration=1)]
[charslot(slot="l",posfrom="-200,0",posto="-100,0",duration=1.5)]
[charslot(slot="r",posfrom="200,0",posto="100,0",duration=1.5)]
[Delay(time=3.5)]
[charslot]
[stopsound(channel="1")]
[charslot(slot="m",name="avg_1032_excu2_1#9$1",focus="m")]
[name="费德里科"]里凯莱？
[charslot(slot="m",name="avg_npc_372_1#10$1",focus="m")]
[name="里凯莱"]真是的，不就是在告解车面前开了你两句玩笑，至于跑那么快吗。
[charslot(slot="m",name="avg_1032_excu2_1#9$1",focus="m")]
[name="费德里科"]什么玩笑？
[Dialog]
[charslot(slot="m",name="avg_npc_372_1#10$1",focus="m")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_372_1#1$1",focus="m")]
[name="里凯莱"]呃，好吧......总之，我知道这个通缉犯的事情很棘手，所以特意带了人来支援你。
[charslot(slot="m",name="avg_npc_372_1#3$1",focus="m")]
[name="里凯莱"]我可是特意放弃了去观摩降生仪式的机会，感动吧？
[charslot(slot="m",name="avg_1032_excu2_1#3$1",focus="m")]
[name="费德里科"]我并未向公证所申请任何形式的支援。
[charslot(slot="m",name="avg_npc_372_1#1$1",focus="m")]
[name="里凯莱"]我知道我知道，你甚至没怎么和其他执行者一起行动过。
[name="里凯莱"]唉，你以为我想掺和啊，这可是教皇厅七个分厅联合发布的特别行动指令。
[charslot(slot="m",name="avg_npc_372_1#8$1",focus="m")]
[name="里凯莱"]说实话，我接到通讯的时候吓了一跳......搞得我以为阿尔图罗蛊惑你一起叛国了。
[charslot(slot="m",name="avg_1032_excu2_1#5$1",focus="m")]
[name="费德里科"]？
[charslot(slot="m",name="avg_245_cello_1#11$1",focus="m")]
[name="阿尔图罗"]......
[charslot(slot="m",name="avg_1032_excu2_1#3$1",focus="m")]
[name="费德里科"]我没有此类倾向，她也不具备这个能力。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]评估完毕，教皇厅的风险预期可以排除。执行者里凯莱，请现在带人返回。
[charslot(slot="m",name="avg_npc_372_1#5$1",focus="m")]
[name="里凯莱"]我没理解错的话，你拒绝了特别行动指令？
[name="里凯莱"]费德里科，你没有拒绝的权利哦。
[charslot(slot="m",name="avg_npc_372_1#6$1",focus="m")]
[name="里凯莱"]我接到的任务是——降生仪式开始前，监督费德里科将阿尔图罗缉拿归案，如果这两人有任何异动，便将他们一同带回！
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]还太早，执行者先生。
[charslot(slot="m",name="avg_npc_372_1#6$1",focus="m")]
[name="里凯莱"]阿尔图罗小姐，你是在对我说话吗？
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]当然。
[charslot(slot="m",name="avg_245_cello_1#2$1",focus="m")]
[name="阿尔图罗"]回来之后，我一直待在修道院里，好不容易出来一趟，还不想那么早回去呢。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]我有十多年没看过圣城一点点沉入夜色了......这里的视野很好。
[charslot(slot="m",name="avg_npc_372_1#9$1",focus="m")]
[name="里凯莱"]所以你是要负隅顽抗了......真是的，又要加班了呀。
[charslot(slot="m",name="avg_npc_372_1#6$1",focus="m")]
[name="里凯莱"]席德佳修女，请躲到我们身后。
[Dialog]
[charslot(slot="m",name="avg_npc_1784_1#15$1",focus="m")]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1, duration = 0)]
[Delay(time=1)]
[playsound(key="$d_gen_soldiersrun",volume=1,channel="1")]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=0.95, duration = 1)]
[charslot(slot="l",name="avg_npc_371_1#1$1",afrom=0,ato=1,duration=1,focus="l,r")]
[charslot(slot="r",name="avg_npc_371_1#1$1",afrom=0,ato=1,duration=1,focus="l,r")]
[charslot(slot="l",posfrom="-200,0",posto="0,0",duration=1.5,focus="l,r")]
[charslot(slot="r",posfrom="200,0",posto="0,0",duration=1.5,focus="l,r")]
[Delay(time=3.5)]
[charslot]
[stopsound(channel="1")]
[charslot(slot="m",name="avg_npc_372_1#6$1",focus="m")]
[name="里凯莱"]费德里科，接下来交给你指挥吧。长久以来，重大通缉犯阿尔图罗都是你在负责，你最熟悉她的种种手段。
[charslot(slot="m",name="avg_245_cello_1#1$1",focus="m")]
[name="阿尔图罗"]看来拉特兰一直在注视着你呢，费迪。
[charslot(slot="m",name="avg_245_cello_1#2$1",focus="m")]
[name="阿尔图罗"]举起你的铳吧，反正你不是第一次这么做了。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]......
[Dialog]
[charslot]
阿尔图罗站在天台的边缘，费德里科还有许多问题要问她，但他注意到对方的手指已经抚上了琴弦。
越过她，费德里科看到了高不见顶的育婴圣堂，和络绎不绝拥向其中的人群。
里凯莱和其他同僚站在自己身后，费德里科听见了武器上膛的声音。
场面变得微妙起来，好像作为执行者的自己突然需要去证明些什么。
几乎没有思考的时间，费德里科举起了守护铳。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]阿尔图罗，你对自己的越狱行为供认不讳，我代表公证所，正式重启对你的危险评估与抓捕程序。
[name="费德里科"]你应履行拉特兰公民之义务，配合我们解除拉特兰之风险。
[Dialog]
[charslot]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[playSound(key="$staplegun_n",volume=0.6,channel="1")]
[PlaySound(key="$d_avg_cellodoubth", volume=1,channel="2")]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
没有任何征兆，费德里科的守护铳喷吐出火舌。
同一个瞬间，大提琴的声音如流水般倾泻，与育婴圣堂方向传来的赞歌声融为一体，淹没了天台上的异响。
[Dialog]
[charslot(slot = "m",name="avg_npc_1784_1#15$1",action="zoom", poszoom = "0.5,0.5", scale=0.95)]
[charslot(slot="l",name="avg_npc_371_1#1$1",focus="l,r")]
[charslot(slot="r",name="avg_npc_371_1#1$1",focus="l,r")]
[Delay(time=0.5)]
[playSound(key="$a_bat_buildingshaking_2",volume=0.6,channel="1")]
[CameraShake(duration=1.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[CameraShake(duration=4, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[playsound(key="$d_avg_explosion", volume=0.8,delay=0.3)]
[PlaySound(key="$d_avg_statuecollapse",volume=0.7,delay=1.2)]
[bgef

... (全文34250字符)
```

### level_act42side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_356_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="伊万杰利斯塔十一世"]......你来了啊，费德里科。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="费德里科"]教宗阁下。
[charslot(slot="m",name="avg_npc_356_1#9$1",focus="m")]
[name="伊万杰利斯塔十一世"]看到茶几上的新品了吗？
[name="伊万杰利斯塔十一世"]“伊万杰利斯塔十一世冰淇淋蛋糕塔”，十一个冰淇淋球，十一种仙人掌融合口味，第十一款以教宗封号命名的蛋糕......
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]相较于执行者事务，我并不能保证自己在新甜品反馈方面的专业性。
[charslot(slot="m",name="avg_npc_356_1#10$1",focus="m")]
[name="伊万杰利斯塔十一世"]哎呀，只是为了感谢你在撤离时没忘记我这个濒死的老家伙。
[name="伊万杰利斯塔十一世"]当然，我也计划把它向全城推广，希望能让大家早日找回自己生活的质感。
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[playsound(key="$d_avg_humaneat",volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_1032_excu2_1#6$1",focus="m")]
[name="费德里科"]从口味上考量，这款甜品更可能引起不必要的争议。
[name="费德里科"]但拉特兰公民确实亟需恢复正常的生活秩序。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]过去三个月内，不仅公民的自杀率居高不下，各类恶性事件也频频发生。
[name="费德里科"]从局部的骚乱，到大规模的公民离境......公证所记录在案的事件有千起之多，以至于城市重建工作都不得不拖到现在才启动。
[charslot(slot="m",name="avg_npc_356_1#8$1",focus="m")]
[name="伊万杰利斯塔十一世"]灾异揭露了太多，也改变了太多。
[name="伊万杰利斯塔十一世"]我们的律法是一台冰冷的机器，我们的圣徒是一只丑陋的怪物，我们每一个人都与魔族同源......
[charslot(slot="m",name="avg_npc_356_1#2$1",focus="m")]
[name="伊万杰利斯塔十一世"]这之中的任何一个真相，都足以摧毁一个人的信仰。
[name="伊万杰利斯塔十一世"]拉特兰这一次的重建，可是大工程。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]三、四厅的受损地块重建工作刚刚启动，经济恢复工作也在推进。
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]......拉特兰已经许久没有这么忙碌过了，但愿人们能在这种忙碌之中找到修复自己内心裂痕的方式。
[name="伊万杰利斯塔十一世"]说起来......费德里科，你自己怎么看待这整件事情？
[name="伊万杰利斯塔十一世"]萨科塔、拉特兰、信仰、共感、交流、我们的社会......圣城在千万年间做出的许多重要决定，甚至你获封圣徒......
[name="伊万杰利斯塔十一世"]都是祂——一台机器推演的结果。属灵的光从来都是冰冷的。
[charslot(slot="m",name="avg_npc_356_1#8$1",focus="m")]
[name="伊万杰利斯塔十一世"]病理性的共感缺失赋予了你生来的极端理性，祂选择你，或许因为你是最能理解祂推演逻辑的个体......
[name="伊万杰利斯塔十一世"]你与祂的谈话，我朦朦胧胧地听到了只言片语。
[charslot(slot="m",name="avg_npc_356_1#9$1",focus="m")]
[name="伊万杰利斯塔十一世"]哪怕和祂交流了几十年之久，我也不得不承认......你才更适合与祂对话。
[name="伊万杰利斯塔十一世"]如果不是熟悉你们的说话方式，我甚至分不清哪句话是谁说的。
[charslot(slot="m",name="avg_1032_excu2_1#3$1",focus="m")]
[name="费德里科"]既然律法是一台机器、一套系统，那么最有效的交流方式只能是以祂的逻辑思考，用祂的语言对话。
[charslot(slot="m",name="avg_npc_356_1#9$1",focus="m")]
[name="伊万杰利斯塔十一世"]但是孩子，你最终却得出了与祂相反的结论。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]......
[name="费德里科"]我记得条律的每一个字，也记得在委托中接触过的每一个名字。
[name="费德里科"]就拉特兰而言，机器构建的秩序与生命所需的秩序，只是相似。
[charslot(slot="m",name="avg_1032_excu2_1#6$1",focus="m")]
[name="费德里科"]生命的存在即是奇迹，强大与脆弱构成它的两面。出于生存与生活之必要，我们不断建构与完善秩序。律法，不过其中之一。
[name="费德里科"]秩序，是为了维护生而为人......
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="none")]
费德里科突然停顿了一下，向来以“机器般冷酷”著称的执行者罕见地斟酌起了用词——
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]珍贵的脆弱。
[charslot(slot="m",name="avg_npc_356_1#10$1",focus="m")]
[name="伊万杰利斯塔十一世"]“珍贵的脆弱”......哈，有趣的搭配。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]所以我们拒绝了祂，这是我们共同的决定，教宗阁下。尽管它是否正确，还需要时间验证。
[Dialog]
[charslot]
[playsound(key="$d_gen_transmissionget",volume=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]请讲。
[name="伊万杰利斯塔十一世"]唔，还有这样的事？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="61_i22_1",block=false,screenadapt="coverall",fadetime=0)]
[ImageTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.1, yScaleTo=1.1, duration=55, block=false)]
[Delay(time=2)]
[PlayMusic(key="$chill_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_spryngjy",volume=1)]
[Delay(time=2)]
[playsound(key="$d_avg_spryngjy",volume=1)]
[Delay(time=2)]
[name="萨科塔修女"]——！
[name="萨科塔修女"]蕾缪乐，你手上拿的什么？
[name="能天使"]嘿嘿，喷漆罐。
[name="能天使"]这地方又深又冷，这块大石头又光秃秃灰扑扑的，难怪每个人来到这儿后都没精打采，跟得了重感冒一样......
[name="能天使"]我忍了很久，实在是忍不下去了！
[name="能天使"]我这就给它换身新衣，这样看到它的人都能有个好心情......一起？
[name="萨科塔修女"]......
[name="能天使"]别这副眼神，前年龙门创意涂鸦大赛，我可是第三名！
[name="萨科塔修女"]喂，你没忘记它是什么，对吧？
[name="能天使"]这样，你们把这当成一种特殊的许愿好了！把想不明白的、没完成的事情，都喷在石头上，说不定就会实现！
[name="萨科塔修女"]许......愿？
[name="能天使"]当年，圣徒不就是向它许了个愿，然后才有的萨科塔和拉特兰吗？
[name="萨科塔修女"]可它已经报废了......
[name="能天使"]哎呀，石头就是石头，怎么会报废！
[name="能天使"]再说还有你自己嘛。还有我、后面这位卖冰淇淋的小妹妹、那边的制铳师大哥，在场的所有萨科塔都会见证你的愿望......
[name="能天使"]谁说帮你实现它的就一定是这块石头呢？
[name="萨科塔修女"]......
[name="能天使"]这三个月以来发生的那些匪夷所思的事情，放在以前，一桩桩一件件哪个不是大新闻？圣城的底都被掀了个干净！
[name="能天使"]但这么多人最后都留在了这片废墟里......我们的光环还亮着，生活还没有结束，不是吗？
[name="能天使"]那就许个新愿望嘛！这又不难！
[name="能天使"]我先来我先来！
[name="能天使"]作为教皇厅扶持的第一个民间物流公司，我的“苹果派物流”下周就要开张了！
[name="能天使"]祈祷我能借此机会做大做强，接很多单，顺便还能有很多时间陪爸爸妈妈姐姐......
[name="伊蒂达"]蕾缪乐姐姐，那我能为无糖冰淇淋许愿吗？
[name="能天使"]呃......
[name="能天使"]当然可以啦！
[name="伊蒂达"]祈祷拉特兰人的基因发生改变，大家都能衷心支持我在饮食方面的研究，牙齿和光环永远不会蛀掉！
[name="萨科塔路人A"]......
[name="萨科塔路人B"]......
[Dialog]
[playsound(key="$d_avg_spryngjy",volume=1)]
[Delay(time=2)]
新一天的阳光顽强地照进了拉特兰的最深处，照亮了绿色的涂鸦和早已黯淡的石头。
萨科塔们就这样抬头仰望着......光在尘埃中舞蹈。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="coverall")]
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[Delay(time=2)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_356_1#1$1",focus="m")]
[name="伊万杰利斯塔十一世"]......
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]..

... (全文27179字符)
```

### level_act42side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="61_g10_fadedbalcony",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[delay(time=1)]
你终于确定，现实中那场声势浩大的迁徙已经结束。
迁徙的结果同样映射在了你们所在的空间——那道仿佛被天灾犁过的鸿沟横亘在大教堂前。鸿沟旁，是一个更醒目的深坑。
在这本应静滞的城市，它们像是丑陋的疤痕。
而环形的机器在其中沉默——
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]......
[Dialog]
[charslot]
[Decision(options="PCS系统......宕机了？", values="1")]
[Predicate(references="1")]
你看向了普瑞赛斯，她依旧冷静，似乎对这场意外毫不在意。
你感到了不安。
[charslot(slot="m",name="avg_4179_monstr_1#8$2",focus="m")]
[name="Mon3tr"]分析确认完毕！十个标准秒之前，大教堂广场发生了至少两次当量惊人的爆炸。
[name="Mon3tr"]实施者基本可以确定为能天使、送葬人和另一个银发萨科塔。爆炸点附近不断闪动的定格画面足以佐证这一点。
[Dialog]
[charslot]
[Decision(options="我们帮能天使做的程序炸弹奏效了。;可那台机器的结构不该如此脆弱。", values="1;2")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_4179_monstr_1#6$2",focus="m")]
[name="Mon3tr"]但还没到庆祝的时候，博士！
[name="Mon3tr"]（普瑞赛斯还没有下一步的动作。）
[name="Mon3tr"]（无论如何，我们必须想办法阻止她改写局面。）
[Predicate(references="2")]
[charslot(slot="m",name="avg_4179_monstr_1#6$2",focus="m")]
[name="Mon3tr"]没错。它的结构绝对能扛住天使们所能制造的任何冲击能量，毕竟它是以能在更严酷的环境中运行而被设计的。
[name="Mon3tr"]（普瑞赛斯理应有能力重启PCS系统。必须阻止她。）
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_4179_monstr_1#9$2",focus="m")]
[name="Mon3tr"]呼，抱歉，博士。
[name="Mon3tr"]我应该独自过来执行这次任务，尽量不让你涉险的——
[Dialog]
[charslot]
[Decision(options="你已经习惯站在我身前了，Mon3tr。", values="1")]
[Predicate(references="1")]
[Decision(options="（微笑）;谢谢。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_4179_monstr_1#5$2",focus="m")]
[name="Mon3tr"]欸？
[Dialog]
[charslot]
[Decision(options="事情的发展也许没有你想得那么坏。", values="1")]
[Predicate(references="1")]
[Dialog]
[charslot]
[Decision(options="我现在已经可以确认普瑞赛斯的状态了。", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_4179_monstr_1#5$2",focus="m")]
[name="Mon3tr"]她的......状态？
[Dialog]
[charslot]
你越过Mon3tr走向了普瑞赛斯，Mon3tr瞬间紧张起来，拉住了你的手臂。
[charslot(slot="m",name="avg_4179_monstr_1#6$2",focus="m")]
[name="Mon3tr"]博士！
[Dialog]
[charslot]
[Decision(options="无妨。;相信我。", values="1;2")]
[Predicate(references="1;2")]
迟疑片刻后，Mon3tr松开了你的手臂，但还是紧紧地跟在你的身侧，寸步不离。
你与普瑞赛斯并肩而立。
[Dialog]
[charslot]
[Decision(options="这些城市的伤痕如此不和谐。;你放任这些冗余参数混杂在你的数据中。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]{@nickname}，那些不起眼的字符，最终使得整个程序瘫痪......我们没法保证一套语言能够永远完美地运行下去。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]我知道你想说什么，即使是源石，这套由我们创造的语言也依旧存在局限。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]它需要更多的时间去调整，去自我迭代。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]甚至有时我会忍不住胡思乱想，真正限制源石向完美形态演化的因素，或许并非其自身的设计瑕疵......而是我们自己。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]人类的感性，抑或理性，都有可能为语言的发展套上枷锁。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]创造源石的那段岁月里，我们也曾数次辩论过这一主张，但从无定论。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]好在我们都接受这一不确定性存在于源石之中。
[Dialog]
[charslot]
[Decision(options="......我并不理解你的意思。", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_npc_1718_1#4$1",focus="m")]
[name="普瑞赛斯"]......记忆损伤可能也影响到了你发散思考的能力？
[charslot(slot="m",name="avg_npc_1718_1#1$1",focus="m")]
[name="普瑞赛斯"]不过能看到你困惑的样子，我很开心。这与过往我和{@nickname}的交流模式截然不同。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]完美，意味着确定的上限。但缺陷，却意味着我们仍有突破的可能性。这是{@nickname}的主张。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]当我们必须解决的危机尚且无法言明时，所谓的完美只是自掘坟墓。
[Dialog]
[charslot]
[Decision(options="不，这和眼下的情况并无关系。", values="1")]
[Predicate(references="1")]
[Dialog]
[charslot]
[Decision(options="你......根本无法改变局面。;这次与我们在甲板上的初遇不一样。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_npc_1718_1#5$1",focus="m")]
[name="普瑞赛斯"]......
[charslot(slot="m",name="avg_npc_1718_1#1$1",focus="m")]
[name="普瑞赛斯"]什么时候意识到的？
[Dialog]
[charslot]
[Decision(options="就在刚刚。", values="1")]
[Predicate(references="1")]
[Dialog]
[charslot]
[Decision(options="......你本可以阻止程序炸弹被引爆。;......你本可以用源石弥合那道鸿沟。;......你本可以让圣徒们永远受困于迷宫。", values="1;2;3")]
[Predicate(references="1")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Image(image="61_i20", fadetime=2,screenadapt="coverall")]
[delay(time=2)]
[image(fadetime=2)]
[delay(time=2)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Predicate(references="2")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="61_g8_catastrophicsquare",screenadapt="coverall", fadetime=2,block=true)]
[delay(time=2)]
[Background(image="61_g10_fadedbalcony",screenadapt="coverall",fadetime=2, block=true)]
[delay(time=2)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Predicate(references="3")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="61_g6_pcsderivativemaze",screenadapt="coverall", fadetime=2,block=true)]
[delay(time=2)]
[Background(image="61_g10_fadedbalcony",screenadapt="coverall", fadetime=2,block=true)]
[delay(time=2)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Predicate(references="1;2;3")]
[Dialog]
[charslot]
[Decision(options="对你来说，做到这些轻而易举。;就像你苏醒时带给罗德岛的灾难那样。", values="1;2")]
[Predicate(references="1;2")]
[Dialog]
[charslot]
[Decision(options="甚至你没有从一开始就彻底解决我和Mon3tr。", values="1")]
[Predicate(references="1")]
[Dialog]
[charslot]
[Decision(options="你的状态出了问题。", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]这并不难看出来，{@nickname}。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]可直到此刻，你才敢鼓起勇气与我并肩而立。
[charslot(slot="m",name="avg_npc_1718_1#2$1",focus="m")]
[name="普瑞赛斯"]我更希望此刻站在我身边的人，能平和地与我分享漫长休眠中，深深扎根于我们思维深处的孤独。
[charslot(slot="m",name=

... (全文28216字符)
```

### mark1

```
铳械制作完成，连日的工作结束，你蜷缩在沙发，闭上双眼进入梦乡。
你梦到小时候，那条来圣城的路，母亲抱着你走了很久很久。
你什么也不敢看，只敢用耳朵去听这一路的动静，小镇里的恶意议论，树林中的可怕嘶吼，还有那片荒地上，劫掠者的砍杀声与人们的惨叫声。
你不住地颤抖，将脑袋彻底埋在母亲的羽翼下也不能将那些声音阻隔分毫，直到铳声响起，震耳欲聋——很快四周变得安静，你开始觉得安宁。
从母亲怀中抬起头，转过一百八十度，你看到一顶光环下，一支长长的铳械正在冒烟。
那一刻你清楚，拉特兰就在前方。
```

### mark2

```
铳械制作完成，连日的工作结束，你蜷缩在沙发，闭上双眼进入梦乡。
你梦到青年时，在导师的举荐下，你以优异的成绩进入铳械制造系。
在学校，每个人都认为你是最优秀的学生，但从没人认为毕业后，你会成为同辈中最优秀的制铳师。
上课时老师对你说：“潘格尼尼，如果你是萨科塔就好了，你会更加理解我在讲什么。”
小组内的同学对你说：“潘格尼尼——哦，忘记你不是萨科塔了，没关系，我再解释一遍。”
你不知道该如何应对，只能笑笑，然后低头盯着桌子上散乱的零件。老师曾说，铳械组装是一门精深的语言，你或许不懂萨科塔们在说什么，但你懂这些零件。
你是与铳械对话的大师。
```

### mark3

```
铳械制作完成，连日的工作结束，你蜷缩在沙发，闭上双眼进入梦乡。
你梦到终于盘下工坊的那天。那只是博尔戈街最不起眼的角落里最不起眼的一间工坊，但能够拥有它，却让你无比满足。
你的人生与铳械联系紧密。它拯救了你，成为你的伙伴，如今又将成为你生活的支柱。你感恩它为你带来的一切。
那天，你和帕特里奇昂合影，他怀抱着那架大口径转管遗产铳笑得很傻，吉雅拿着相机，让你们不要笑得那么傻，你俩沉浸在幸福中，谁都没能做到。
你将相片装进相框，就像你将帕特里奇昂与吉雅一起装进你的未来，连同铳械一起，永远永远。
```

### mark4

```
最后一支铳械制作完成，工作结束，你蜷缩在沙发，闭上双眼进入梦乡。
但你失败了，辗转几次，最终无奈地从沙发上爬起。铳械工坊即将关停，相关工作以后将由制铳圣堂全权接管。
此刻，工坊里只有你一个人，没有顾客，没有学徒，你终于对工坊即将关停这件事有了实质感受。和铳械相伴一生，想到不久后便要同它分离，你就觉得心酸。
默默叹口气，你坐在黑暗中，与付出多年心血的工坊告别，此刻，你有很多话想说。
不巧的是，一阵敲门声打断了你的思绪，你本不想理会，但那个身着公务员制服的家伙却直接走了进来。
“......你好，有人吗？
```

### mark5

```
清晨，一缕阳光从窗户洒进工坊，提醒你该结束工作离开工坊了。
你拿起钥匙，起身走出工坊，关闭大门，从黑夜走进温暖的阳光。
```


> 本章节共31个脚本文件，此处展示前30个。

## 统计

- 总字符数：649968
- 对话行数：4794


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
