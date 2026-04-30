# 明日方舟 · 活动剧情 · act25side（37段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act25side」完整剧情脚本（37个文件，5627行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act25side
- 脚本文件数：37

### level_act25side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="29_g6_mainstreet",screenadapt="coverall")]
[playMusic(intro="$plot_intro",key="$plot_loop", volume=0.6)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_536_1#1$1", duration = 1.5, isblock=true)]
[name="霍尔海雅"]唔，时间刚刚好。
[dialog]
[charslot]
黎博利踏上高楼的天台，她抬头看向天空。高处的风声藏住了隐约的尖啸，一枚模糊的光点在她的眸子里急速放大。
粗壮的尾巴轻巧而规律地移动，那是曼妙的标尺，黎博利借此对脚下的这座城市比画着看不见的网格。
[charslot(slot = "m", name = "avg_npc_536_1#1$1")]
[name="霍尔海雅"]让我来看看，这颗“星星”会砸在特里蒙的哪个位置呢？
[charslot(slot = "m", name = "avg_npc_536_1#1$1")]
[name="霍尔海雅"]三、五区主要是住宅区，十一区的新产业园正在施工......
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[name="霍尔海雅"]别是中央区吧，密集的商业写字楼像是超市里的罐头，工作日，那里面塞了多少人......啧。
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[name="霍尔海雅"]你是算准了这个试验物的落点......
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[name="霍尔海雅"]还是，你压根不在意它会引发多大的动静？
[dialog]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_536_1#10$1")]
[name="霍尔海雅"]不管怎样，你的计划进展到这一步，越来越有趣了......克丽斯腾。
[dialog]
[charslot(slot = "m", focus="none")]
[PlaySound(key="$d_avg_explosion", volume=0.8)]
[delay(time=2.5)]
[PlaySound(key="$transmission", volume=0.5)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_536_1#10$1")]
[name="霍尔海雅"]确定——十三区的特莱顿工厂。
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(duration=1)]
[delay(time=1.5)]
黎博利从高楼跃下。
[dialog]
[StopSound(channel="a", fadetime=1)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="38_g13_trimountlivingroom",screenadapt="coverall")]
[Delay(time=1)]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[charslot(slot="m",name = "avg_249_mlyss_1#1$1",action="zoom",poszoom="0.5,0.65",scale=1.4,duration=0,isblock=true)]
[PlaySound(key="$d_avg_femaleexhale", volume=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "m", name = "avg_249_mlyss_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Delay(time=1)]
[bgeffect]
[charslot(slot = "m", focus="none")]
[Decision(options="呼啊......;......;嘶......谁把窗帘拉开的？", values="1;2;3")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_249_mlyss_1#1$1")]
[name="缪尔赛思"]哈欠打得这么大，是不是没睡好啊？
[dialog]
[Predicate(references="2")]
[charslot(slot = "m", name = "avg_249_mlyss_1#9$1")]
[name="缪尔赛思"]你起床的时候，也会对着天花板发一会儿呆吗？
[dialog]
[Predicate(references="3")]
[charslot(slot = "m", name = "avg_249_mlyss_1#8$1")]
[name="缪尔赛思"]这个点，莱茵的员工已经上班一小时了。
[dialog]
[Predicate(references="1;2;3")]
[charslot(slot = "m", focus="none")]
[Decision(options="特里蒙的酒店就是这么保护客人隐私的？;莱茵生命的主任就是这么拜访客人的吗？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_249_mlyss_1#1$1")]
[name="缪尔赛思"]想见你，就来喽。
[charslot(slot = "m", name = "avg_249_mlyss_1#8$1")]
[name="缪尔赛思"]你从动力甲里救了我，我来给你送个早饭，很奇怪吗？
[charslot(slot = "m", name = "avg_249_mlyss_1#1$1")]
[name="缪尔赛思"]莱茵生命楼下咖啡店的早餐，每天限量一百份哦。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="......", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_249_mlyss_1#7$1")]
[name="缪尔赛思"]好啦，别用这种眼神看我，你的起床气好重哦。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="你是在找塞雷娅吧？", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_249_mlyss_1#1$1")]
[name="缪尔赛思"]我确实和她失去了联系。但她不在，拜托你也是一样的......
[charslot(slot = "m", name = "avg_249_mlyss_1#2$1")]
[name="缪尔赛思"]首先，看看这个吧。
[dialog]
[charslot]
[musicvolume(volume=0.2, fadetime=2)]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[delay(time=0.8)]
[PlaySound(key="$transmission", volume=0.5)]
[delay(time=2)]
[name="新闻"]各位市民，今晨，位于十三区的特莱顿第三化工厂发生了爆炸。
[name="新闻"]爆炸的具体原因尚未确认，相关部门初步判定为实验人员操作失误引发了施工机械爆炸。
[name="新闻"]特莱顿第三化工厂储存着大量的催化物和中间试剂，为防止这些化学原料泄露造成更大的危害，军方配合政府部门进行了必要的清场。
[name="新闻"]目前，十三区整体处于临时管控状态，出入受到严格限制，请有关市民调整行程，配合工作。
[name="新闻"]另外，十三区的临时管控是否会影响到杰克逊副总统在特里蒙接下来的行程，我们已经咨询了有关部门，但尚未得到回应。
[dialog]
[Decision(options="莫非又是另一个359号基地？;莫非这也和莱茵生命有关？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_249_mlyss_1#2$1")]
[name="缪尔赛思"]具体的我也不清楚。
[charslot(slot = "m", name = "avg_249_mlyss_1#1$1")]
[name="缪尔赛思"]但博士你，或者说罗德岛既然在特里蒙，一定不愿意错过这则大新闻。毕竟塞雷娅很信任你们。
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_249_mlyss_1#9$1")]
[name="缪尔赛思"]好了，博士，你有新的客人......我们很快会再见的。
[dialog]
[PlaySound(key="$d_avg_watersubbreak", volume=1)]
[Effect(name="$e_muesys_hide", layer = 1)]
[charslot(duration=1.5)]
[delay(time=4)]
[Decision(options="果然是分身。;新的客人？", values="1;2")]
[Predicate(references="1;2")]
[musicvolume(volume=0.6, fadetime=2)]
[PlaySound(key="$rungeneral", volume=0.4)]
[delay(time=2)]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot = "m", name = "avg_npc_895_1#2$1", duration=1, isblock=true)]
[name="伊芙利特"]博士，太阳晒屁股啦！
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="伊芙利特......谁带你来的？", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", posfrom="0,0", posto="100,0", afrom=1, ato=0, duration=1)]
[delay(time=1.5)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "char_003_kalts_1", duration = 2, isblock=true)]
[name="凯尔希"]好久不见，Dr.{@nickname}。
[charslot(slot = "m", name = "char_003_kalts_1")]
[name="凯尔希"]白面鸮已经在埃琳娜的陪同下返回本舰接受机能检查与治疗，Mechanist在执行新的任务。接下来，我将与你共同行动。
[charslot(slot = "m", name = "avg_npc_895_1#2$1")]
[name="伊芙利特"]还有我！还有......
[dialog]
[charslot]
[Decision(options="迷迭香。;凯尔希，我需要一个解释。", values="1;2")]
[Predicate(references="1;2")]
云朵般的菲林孩子不知何时已经进入了房间，她靠着窗边站着，安静地听你们说话。
她打量着你和你的房间。她的身后，洁白的云朵流过特里蒙的晴空。
[dialog]
[StopSound(channel="a", fadetime=2)]
[PlaySound(k

... (全文27236字符)
```

### level_act25side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g2_colombiaoffice",screenadapt="coverall", xScale=1.1,yScale=1.1)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_899_1#1$1",duration=1,isblock=true)]
[name="布莱克"]......
[dialog]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot = "r", focus="none")]
[Delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_899_1#1$1", focus="none")]
[charslot(slot = "l", name = "avg_npc_897_1#1$1", posfrom="-300,0", posto="0,0", duration=2)]
[Delay(time=2.5)]
[name="杰克逊"]上校，让你等了半小时，抱歉。
[charslot(slot = "r", name = "avg_npc_899_1#1$1", focus="r")]
[name="布莱克"]该抱歉的是我，副总统先生。您在特里蒙的行程排得很满，我突然造访，帕瓦尔秘书说您为此临时取消了一个会议。
[charslot(slot = "l", name = "avg_npc_897_1#1$1", focus="l")]
[name="杰克逊"]十三区的事情，你们的反应很迅速......
[charslot(slot = "l", name = "avg_npc_897_1#5$1", focus="l")]
[name="杰克逊"]但也很激烈。
[charslot(slot = "r", name = "avg_npc_899_1#5$1", focus="r")]
[name="布莱克"]您刚刚在公众面前进行了如此振奋人心的演讲，十三区的变故出现得很不是时候。
[charslot(slot = "l", name = "avg_npc_897_1#5$1", focus="l")]
[name="杰克逊"]看来这件事情，对你们来说，同样是不小的意外。
[charslot(slot = "r", name = "avg_npc_899_1#5$1", focus="r")]
[name="布莱克"]......我只是说，“地平弧光计划”或许并不适合这么快展示给我们的民众。
[name="布莱克"]也因此，我们希望您取消接下来的行程，离开特里蒙。我们也会尽快搞定这些“意外”。
[charslot(slot = "l", name = "avg_npc_897_1#5$1", focus="l")]
[name="杰克逊"]......
[charslot(slot = "l", name = "avg_npc_897_1#2$1", focus="l")]
[name="杰克逊"]上校，我明白你们的诉求......
[charslot(slot = "l", name = "avg_npc_897_1#1$1", focus="l")]
[name="杰克逊"]但我的行程不会改变，相反，我甚至会在特里蒙多待上一段时间。
[name="杰克逊"]在刚刚结束的会议里，我已经决定前往莱茵生命参观，和我们优秀的科研人员们好好交流。
[charslot(slot = "r", name = "avg_npc_899_1#6$1", focus="r")]
[name="布莱克"]......
[charslot(slot = "l", name = "avg_npc_897_1#1$1", focus="l")]
[name="杰克逊"]布莱克上校，我们是一个整体，我们都将为哥伦比亚这个国家奉献自己的一切。
[charslot(slot = "l", name = "avg_npc_897_1#2$1", focus="l")]
[name="杰克逊"]但是，在这座城市中，汇聚了无数的科技先锋，他们是哥伦比亚科技发展的基石，说他们能左右这个国家的未来，也并不过分。
[name="杰克逊"]你明白我的意思吗？
[charslot(slot = "r", name = "avg_npc_899_1#1$1", focus="r")]
[name="布莱克"]......
[charslot(slot = "l", name = "avg_npc_897_1#2$1", focus="l")]
[name="杰克逊"]即使在哥伦比亚最成熟的军工厂流水线上，生产一枚标准炮弹的时间也要一天半。
[name="杰克逊"]更不谈它被送往战场，真正为我们的士兵所掌握要花费的时间。
[charslot(slot = "l", name = "avg_npc_897_1#1$1", focus="l")]
[name="杰克逊"]从容，上校。越是面对“弧光一号”这种能够改变整片大地局势的超级武器，我们越应该从容。
[name="杰克逊"]这里是哥伦比亚，不是萨尔贡，也不是玻利瓦尔。
[charslot(slot = "r", name = "avg_npc_899_1#1$1", focus="r")]
[name="布莱克"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="27_g8_jail",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="锡人"]这些年，军方，确切地说，国防部在国家军事能力上不断探索。
[name="锡人"]整体而言，步子迈得还算稳健。在总统看来，这是一种良性发展，因而乐见其成。
[name="锡人"]但是，近年来国际局势不断变化，尤其是维多利亚碎片大厦的出现，让一些事情改变了。
[name="锡人"]那样可怕的超级武器，让距离不再成为距离，所有的地面防御都将形同虚设，风暴带来的烟尘随时可能落在我们的枕头上。
[name="锡人"]国防部内部主战的声音逐渐扩大，一些危险的苗头已经开始出现了，他们把宝押在了具备同样跨时代意义的战略武器的研发上。
[charslot(slot = "m", name = "avg_npc_896_1#3$1")]
[name="塞雷娅"]克丽斯腾在这个时候进入了军方的视野？
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]是的。克丽斯腾成为了军方的核心技术顾问。
[name="锡人"]她很快交出了代号“地平弧光计划”的企划案，计划建造名为“弧光一号”的超级武器，并迅速落地执行。
[name="锡人"]军方对此投入了大量的资源，莱茵生命也在很长一段时间里，获得了更多的政策支持。
[name="锡人"]它能从特里蒙众多的科技企业中脱颖而出，也与此有关。
[name="锡人"]根据我们掌握的情报，建造“弧光一号”需要在特里蒙挖建复杂的能量井，并在飞行器的极限高度升起聚焦发生器......
[name="锡人"]这是一项庞大的工程，军方几乎倾尽全力......
[name="锡人"]你面前的这个从天上砸下来的家伙，想必就是计划的一部分。
[dialog]
[charslot]
塞雷娅将视线从工厂的废墟上移，看向天空。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]将天空作为中转站？
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]具体的概念设计与实现原理，我们并不清楚......
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]将天空作为中转站，将巨量的能源进行聚焦或变向，从而实现在超远距离发动强力打击......
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]理论上说，这确实是可行的......
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]但克丽斯腾真的会帮军方建造所谓的超级武器？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g12_trimountrestarea",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot = "l", name = "avg_npc_899_1#1$1",duration=1)]
[delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_890_1#1$1", posfrom="300,0", posto="0,0", duration=2, isblock=true)]
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="none")]
[name="斐尔迪南"]看来，你没有得到你想要的回复。
[charslot(slot = "l", name = "avg_npc_899_1#3$1", focus="l")]
[name="布莱克"]我从一开始就知道会这样，只是现在更加确认了而已。
[charslot(slot = "l", name = "avg_npc_899_1#3$1", focus="l")]
[name="布莱克"]合格的政治家从来不会拥有那么明确的立场，起码目前，他们不想我们那么快地接管这个项目。
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]他们要怎么做？
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]很简单，只需要拖延。如果说科学研究追求效率，那么斐尔迪南，“拖延”就是这帮政客的惯用伎俩。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]当初辛嘉斯政府想要收回伍兹公司的林场而与议会协商，直到后者失去了对那块区域的控制权，那场已经持续三年的谈判都没有结果。
[charslot(slot = "l", name = "avg_npc_899_1#3$1", focus="l")]
[name="布莱克"]他们想拖着，拖到我们无法解决遇到的问题，拖到我们对那该死的“地平弧光计划”丧失信心，直至不了了之。
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]斐尔迪南，你已经去过现场了吧，有什么结论？
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]确实是“弧光一号”中“聚焦发生器”的试飞版本。
[name="斐尔迪南"]天空看似澄澈，但绝非净土，克丽斯腾需要反复试验新的压力和导航系统，这样的试飞可能不止一次。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]......
[charslot(slot = "r", n

... (全文23943字符)
```

### level_act25side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[gridbg(imagegroup="38_g21_skystarry_L1/38_g21_skystarry_r1/38_g21_skystarry_L2/38_g21_skystarry_r2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-640,fadetime=1)]
[largebgtween(duration = 80,yFrom = 720, yTo = 360,block = false)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
这些星辰自古以来就在泰拉的天顶闪耀。
它们承载了多少浪漫的迷思，多少探求的目光。
星象学家们穷极一生为星座与天体赋予象征意义，萨满和德鲁伊们试图解释每一道流星留下的痕迹。
触不可及。正因为触不可及，天空才是湎于幻想之人的归宿。
对于这片大地，抬头仰望毫无意义。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[gridbg]
[charslot]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_537_1#1$1", duration=1, isblock=true)]
[name="克丽斯腾"]6152.31米，这就是泰拉天空的高度。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]也是莱特夫妇那架飞行器上最后的记录。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]无人质疑这份狭窄。
[charslot(slot = "m", name = "avg_npc_537_1#4$1")]
[name="克丽斯腾"]无人愤怒，无人困惑，无人好奇。
[charslot(slot = "m", name = "avg_npc_537_1#3$1")]
[name="克丽斯腾"]人们生活在这枚被豆荚轻柔包裹的豌豆上，并对此漠不关心。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "m", name = "avg_npc_891_1#1$1", duration=2, isblock=true)]
[name="娜斯提"]所以，才会有几百年前乌萨斯诗人那首蹩脚的诗。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_537_1#3$1")]
[name="克丽斯腾"]“星荚”。
[charslot(slot = "m", name = "avg_npc_891_1#2$1")]
[name="娜斯提"]哼，对阻隔层的浪漫修辞。
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[name="娜斯提"]我读过所有有关阻隔层的那些论文，维多利亚和莱塔尼亚的学者们做了些轻浮又潦草的理论建构......
[name="娜斯提"]《空间压力的分析》《外物质密度差与阻隔层的原理》......陈旧，过时，漏洞百出。
[name="娜斯提"]自诩有“开拓精神”的哥伦比亚学界也无非就是在这些垃圾上修修补补，偶尔有年轻学者在学报上发表些看似新奇的理论。
[charslot(slot = "m", name = "avg_npc_891_1#6$1")]
[name="娜斯提"]但他们盯着教职头衔和科研津贴所费的精力，恐怕比花在这片天空上的多得多。
[name="娜斯提"]哦，顺便，前些日子发射的试验平台掉下来了，还是撞上了阻隔层内的那些老问题。
[name="娜斯提"]基础空气动力学的突变，源石环境的大幅紊乱，还有外源动力的极速衰减。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]递质的数据分析结果怎么样？
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[name="娜斯提"]经过重新调整的那批很可靠。
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[name="娜斯提"]导能电缆我也已经全部铺设完毕，接到了你之前告诉我的那个端口。
[charslot(slot = "m", name = "avg_npc_891_1#10$1")]
[name="娜斯提"]不过，克丽斯腾，你知道你需要的能量是个什么规模。
[charslot(slot = "m", name = "avg_npc_891_1#10$1")]
[name="娜斯提"]理论虽然可行，但是......
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]没有问题。
[charslot(slot = "m", name = "avg_npc_891_1#2$1")]
[name="娜斯提"]......好吧。
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[name="娜斯提"]试验平台的坠毁惹出了点麻烦，你的失踪给军方带去的焦虑被彻底点燃了。
[charslot(slot = "m", name = "avg_npc_891_1#6$1")]
[name="娜斯提"]克丽斯腾，在他们接下来的行动里，死亡恐怕是对你最仁慈的结果。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]这根本算不上代价。
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_537_1#2$1")]
[name="克丽斯腾"]娜斯提，你喜欢看星星吗？
[charslot(slot = "m", name = "avg_npc_891_1#2$1")]
[name="娜斯提"]没兴趣。
[charslot(slot = "m", name = "avg_npc_891_1#2$1")]
[name="娜斯提"]看着遥不可及的东西只会让我感觉虚无。
[charslot(slot = "m", name = "avg_npc_537_1#2$1")]
[name="克丽斯腾"]然而，遥不可及的东西时而会成为你的道标。
[charslot(slot = "m", name = "avg_npc_537_1#3$1")]
[name="克丽斯腾"]不过，有一点你说得很对。
[charslot(slot = "m", name = "avg_npc_537_1#3$1")]
[name="克丽斯腾"]死亡只是最仁慈的结果。
[charslot(slot = "m", name = "avg_npc_891_1#6$1")]
[name="娜斯提"]那就别在给我答应好的东西之前死，总辖。
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[name="娜斯提"]......小心点。
[charslot(slot = "m", name = "avg_npc_537_1#2$1")]
[name="克丽斯腾"]谢谢，我会的。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g12_trimountrestarea",screenadapt="coverall")]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_890_1#1$1")]
[charslot(slot = "l", name = "avg_npc_899_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="none")]
[name="斐尔迪南"]......
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]上校，我该如何理解这道命令？
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]......
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]让我猜猜......派去监视克丽斯腾的特工已经失踪，你压下了这个消息。
[name="斐尔迪南"]与其说那些特工已经被克丽斯腾灭口，你的上级更担忧的是，他们是否跟随克丽斯腾背叛了这个国家。
[name="斐尔迪南"]他们甚至在怀疑，你是否已经背叛了这个国家？
[charslot(slot = "r", name = "avg_npc_890_1#6$1", focus="r")]
[name="斐尔迪南"]难怪你会如此急于找到克丽斯腾。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]......
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]我的上一个服役地点，是玻利瓦尔。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]四十年代末，国防部支持的联合政府在自己的辖区表现得像是一个不会走路的婴儿，我们对玻利瓦尔内战的干预政策宣告失败。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]国防部在市民间的声望一落千丈，将军甚至就此让渡了对于武装部队的总领导权......
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]......
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]国防部需要“弧光一号”来重新挽回形象，获取国民的信任，而我也需要用它证明自己还能将军功章从灰尘里捡起来。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]这确实是我最后的机会。
[charslot(slot = "l", name = "avg_npc_899_1#3$1", focus="l")]
[name="布莱克"]但是，轮不到你来冷嘲热讽，斐尔迪南。
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]算了吧，上校，你觉得你刚才说的话能骗过谁？
[charslot(slot = "r", name = "avg_npc_890_1#6$1", focus="r")]
[name="斐尔迪南"]这根本不足以解释国防部为何会冒进至此，也不能作为你孤注一掷的理由。
[charslot(slot = "l", name = "avg_npc_899_1#6$1", focus="l")]
[name="布莱克"]你不是自诩是不逊色于克丽斯腾的科学家吗，为什么不用你那聪明的脑瓜想一想？
[charslot(slot = "r", name = "avg_npc_

... (全文29584字符)
```

### level_act25side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g13_trimountlivingroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_895_1#9$1", duration=1, isblock=true)]
[charslot(slot = "l", name = "avg_npc_895_1#9$1", focus="l")]
[name="伊芙利特"]......
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]你不说话......房间好安静。
[charslot(slot = "l", name = "avg_npc_895_1#9$1", focus="l")]
[name="伊芙利特"]我不太想说话......你觉得无聊吗？
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]还好。就是有些不习惯。
[charslot(slot = "l", name = "avg_npc_895_1#9$1", focus="l")]
[name="伊芙利特"]......
[dialog]
[charslot(slot = "m", focus = "n")]
从回到房间开始，准确地说，从和塞雷娅分开后，伊芙利特就一直皱着眉头。
桌面上散落着做工精细的几何体，那是酒店免费赠送的特里蒙等比例城市模型。
迷迭香和伊芙利特各自坐在沙发的一角，有一搭没一搭地聊着天。
你看着两个孩子，没有打扰她们。
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="none")]
[charslot(slot = "l", name = "avg_npc_895_1#2$1", focus="l")]
[name="伊芙利特"]你要不要试试拼一遍“特里蒙”？很有挑战性，要拼好久。
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]已经两遍了。
[charslot(slot = "l", name = "avg_npc_895_1#5$1", focus="l")]
[name="伊芙利特"]......啊，这么快？
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]我记下来了......本子上。有几个步骤很难，每个城区的建筑密度都很高，造型又很像，特别容易弄混。但我记下来了。
[charslot(slot = "l", name = "avg_npc_895_1#1$1", focus="l")]
[name="伊芙利特"]你会一直记东西吗？
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]嗯。不然会忘记。
[charslot(slot = "l", name = "avg_npc_895_1#8$1", focus="l")]
[name="伊芙利特"]都记了什么，可以跟我说吗？
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]博士、阿米娅、凯尔希医生、煌、温蒂......
[charslot(slot = "r", name = "avg_391_rosmon_1#2$1", focus="r")]
[name="迷迭香"]还有一些更远的人和事......
[dialog]
[charslot(duration=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]	
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="长长的走廊......自己走丢了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="哥哥们明明比自己大不了多少，但很可靠，他们很快就能找过来，抚摸着我的脑袋让我不要害怕。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="哥哥们的后脑有着相似的伤口，像是分不清名字的自己昨晚给花卉统一做的标记......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......哥哥们？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]	
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_895_1#1$1", focus="none")]
[charslot(slot = "r", name = "avg_391_rosmon_1#2$1", focus="r")]
[name="迷迭香"]......
[charslot(slot = "l", name = "avg_npc_895_1#6$1", focus="l")]
[name="伊芙利特"]你看起来很不舒服......放松，别想了。
[name="伊芙利特"]我比你好一些，但也没有好多少......要是记忆可以自己选择就好了。
[name="伊芙利特"]我老是想起那些嘀嘀乱响的仪器，墙壁统一刷成白色的房间，一层套着一层，像为了捉弄人故意建成那样似的，一想起来我就烦躁......
[charslot(slot = "l", name = "avg_npc_895_1#1$1", focus="l")]
[name="伊芙利特"]但赫默和塞雷娅跟我说了什么做了什么，我又想牢牢地记住！
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]所以你闷闷不乐是因为刚刚的事。塞雷娅她......
[charslot(slot = "l", name = "avg_npc_895_1#6$1", focus="l")]
[name="伊芙利特"]......
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]也许她是怕你受伤？你看凯尔希医生也没有让博士跟着去找那个“弧光一号”。
[dialog]
[charslot(slot = "r",  focus="none")]
[Decision(options="......",values="1")]
[Predicate(references="1")]
[charslot(slot = "l", name = "avg_npc_895_1#9$1", focus="l")]
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="none")]
[name="伊芙利特"]赫默不许我见塞雷娅，塞雷娅不许我跟着帮她的忙......
[name="伊芙利特"]可能她们并不是怕我添乱，可能她们觉得以前没有保护好我，可能她们觉得我还是个小孩子，只会闹脾气。
[name="伊芙利特"]她们都很有道理。
[charslot(slot = "l", name = "avg_npc_895_1#3$1", focus="l")]
[name="伊芙利特"]但我超级讨厌这种感觉。
[charslot(slot = "r", name = "avg_391_rosmon_1#5$1", focus="r")]
[name="迷迭香"]我好像，明白......
[charslot(slot = "l", name = "avg_npc_895_1#6$1", focus="l")]
[name="伊芙利特"]真的吗？
[charslot(slot = "r", name = "avg_391_rosmon_1#5$1", focus="r")]
[name="迷迭香"]嗯。离开罗德岛的时候，煌和温蒂一直在劝我，煌还差点烧了那封信。
[name="迷迭香"]虽然阿米娅和凯尔希医生最后还是同意了，但我能看出，她们其实并没有那么想我回哥伦比亚......她们很担心，就像塞雷娅一样？
[charslot(slot = "l", name = "avg_npc_895_1#7$1", focus="l")]
[name="伊芙利特"]那些大人都一个样。
[charslot(slot = "r", name = "avg_391_rosmon_1#5$1", focus="r")]
[name="迷迭香"]但我想要记起来那些被我遗忘的东西，哪怕这会让我丢失得更多......
[charslot(slot = "r", name = "avg_391_rosmon_1#1$1", focus="r")]
[name="迷迭香"]我应该回来......这是我唯一确定的事情。
[charslot(slot = "r", name = "avg_391_rosmon_1#9$1", focus="r")]
[name="迷迭香"]你记性比我好，那你一定比我更清楚自己应该做什么。
[charslot(slot = "l", name = "avg_npc_895_1#8$1", focus="l")]
[name="伊芙利特"]我就是这个意思！
[name="伊芙利特"]你和我，咱们俩主动回到哥伦比亚，回到特里蒙，可都是有自己的事情要做。
[charslot(slot = "l", name = "avg_npc_895_1#2$1", focus="l")]
[name="伊芙利特"]呼，心情好多了。迷迭香，等事情忙完，咱们俩跟博士请个假，一起出去好好逛逛怎么样？
[name="伊芙利特"]特里蒙的天老是灰蒙蒙的，难得这阵子天气好，我可以给你当导游......哦不对，你已经把“特里蒙”拼了两遍，比我熟悉......
[charslot(slot = "r", name = "avg_391_rosmon_1#9$1", focus="r")]
[name="迷迭香"]嗯，好。
[dialog]
[charslot(slot = "r",  focus="none")]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_895_1#1$1", focus="l")]
[name="伊芙利特"]凯尔希回来了？我去开门。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "r",  focus="none")]
[charslot(duration=1)]
[charslot(slot = "l", posfrom="0,0", posto="-300,0", afrom=1, ato=0, focus="l", duration=1)]
[delay(time=1)]
[charslot(slot = "r",  focus="none")]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=2)]
[stopmusic(fadetime=2)]
[name="伊芙利特"]你......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="伊芙利特"]你是那个一口气吃四份超大热狗的锡人！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(imag

... (全文24584字符)
```

### level_act25side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="29_g6_mainstreet",screenadapt="coverall")]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[playMusic(intro="$Tremont_intro",key="$Tremont_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=3)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot="l",name="avg_npc_524_1#1$1",duration=0.5)]
[charslot(slot="r",name="avg_npc_523_1#1$1",duration=0.5)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_524_1#1$1",focus="l")]
[name="记者A"]别磨蹭了，快走。明天全媒体的头版头条估计都是副总统访问莱茵，要是拍到的照片没有其他同行的角度好，会被主编骂死。
[Dialog]
[charslot(slot="r",name="avg_npc_523_1#1$1",focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[Delay(time=1)]
[name="记者B"]等等，我的证件好像不见了......
[charslot(slot="l",name="avg_npc_524_1#1$1",focus="l")]
[name="记者A"]那怎么办？！这可没法进场。
[charslot(slot="r",name="avg_npc_523_1#1$1",focus="r")]
[name="记者B"]你先去占个好位置，我回去找！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.7)]
[charslot(slot = "right",posfrom = "0,0", posto = "300,0",afrom = 1, ato = 0,duration = 1)]
[Delay(time=1.5)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_529_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_530_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_529_1#1$1",focus="l")]
[name="莱茵职员A"]人怎么这么多......
[name="莱茵职员A"]我还想去楼下咖啡店买份早餐......进都进不去。
[charslot(slot="r",name="avg_npc_530_1#1$1",focus="r")]
[name="莱茵职员B"]副总统公开到访公司，还要进行直播，各大报社的记者全都来了，没把路堵死算不错了。
[Dialog]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_534_1#1$1",duration=1)]
[delay(time=1.5)]
[name="普通市民？"]......
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot="l",name="avg_npc_895_1#1$1",duration=1)]
[charslot(slot="r",name="avg_391_rosmon_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_895_1#1$1",focus="l")]
[name="伊芙利特"]迷迭香，你发现没有？
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="r")]
[name="迷迭香"]发现什么？
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]先是那个工厂，再是莱茵生命，特里蒙老是喜欢在一个地方有事的时候，把它封锁起来。
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="r")]
[name="迷迭香"]莱茵生命和那个工厂不一样吧？他们只是对通往莱茵生命的部分关键路段实施了禁行，应该是副总统的车队会经过，出于安全考虑......
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]所以其他几条街人就越来越多了。
[name="伊芙利特"]封锁起来别人就看不到了吗？粗暴，很不聪明。
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="r")]
[name="迷迭香"]......嗯。
[charslot(slot="r",name="avg_391_rosmon_1#4$1",focus="r")]
[name="迷迭香"]博士，你在看什么？
[Dialog]
[charslot(slot="l",focus="n")]
[Decision(options="今天会下雨吗？", values="1")]
[Predicate(references="1")]
[charslot(slot="l",name="avg_npc_895_1#2$1",focus="l")]
[name="伊芙利特"]今天可是个大晴天！出门的时候，酒店的电视正好在播报气象信息，博士你记性不好。
[name="伊芙利特"]再说现在也不是特里蒙的雨季。
[Dialog]
[charslot(duration=0.5)]
[delay(time=1)]
确实是又一个晴日。
特里蒙的城建规划很精细，虽然高楼林立，但彼此错落，避开遮挡，还是足以从容地筛下阳光，初冬的暖阳均匀地涂抹着每一条街。
你抬头看，一朵乌云在很远的地方慢吞吞地晃荡着，风往云的方向吹，它看起来离这座城市越来越远。
可它一直在视线里。
同时出现在你视线里的，还有忙碌的路口、暂停的车辆、高处一闪而过的光，以及那些伪装得很好的“行人”......
你不动声色，只是催了催两个孩子快点走。
[Dialog]
[charslot(slot="l",name="avg_npc_895_1#1$1",focus="n")]
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="r")]
[name="迷迭香"]博士，你发现什么了吗？
[Dialog]
[charslot(slot="l",focus="n")]
[Decision(options="可能是梅兰德基金会的间谍。;可能是军方的特工。;快走吧，缪尔赛思在等我们。", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot="l",name="avg_npc_895_1#2$1",focus="l")]
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="n")]
[name="伊芙利特"]放心吧，博士，我们会保护你的。
[Dialog]
[charslot(slot="l",focus="n")]
[Decision(options="别忘了今天的任务......", values="1")]
[Predicate(references="1")]
[charslot(slot="l",name="avg_npc_895_1#7$1",focus="l")]
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="n")]
[name="伊芙利特"]知道了，博士。出门前你都唠叨好几遍了。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]本大爷答应的事情一定说到做到，保证听你的指挥。
[charslot(slot="r",name="avg_391_rosmon_1#1$1",focus="r")]
[name="迷迭香"]我们应该到了。
[Dialog]
[delay(time=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="29_g9_headquarter",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot="m",name="avg_249_mlyss_1#1$1",duration=1.5)]
[delay(time=2)]
[name="缪尔赛思"]Dr.{@nickname}，又见面了。
[name="缪尔赛思"]这次又是我在等你。
[charslot(slot="m",focus="n")]
[Dialog]
[Decision(options="我应该没有迟到。;......;我还早到了一分钟。", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot="m",name="avg_249_mlyss_1#10$1",focus="m")]
[name="缪尔赛思"]呀，谁让我到得比你早呢，我可是收到你的信息就在准备了。
[charslot(slot="m",focus="n")]
[Dialog]
[Decision(options="这本来就是你的公司......", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[playsound(key="$d_avg_paper2")]
[name="缪尔赛思"]好了。这些是你要的东西......莱茵生命大楼的建筑图纸，以及你和你两位小助手的通行证。
[name="缪尔赛思"]我动用生态科的关系为你们赋予了临时权限，今天之内，你们可以自由地出入大楼内的绝大多数地方，调取相应的信息。
[name="缪尔赛思"]对了，为了方便实验材料的运送，大楼的地上楼层和地下结构都有大量隔断的隐藏空间，我建议你分一个人专门负责地下结构。
[charslot(slot="m",focus="n")]
[Dialog]
[Decision(options="那么你呢？", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_249_mlyss_1#1$1",focus="m")]
[name="缪尔赛思"]我当然得陪同副总统先生参观莱茵咯。
[name="缪尔赛思"]本来克丽斯腾就不在，十科的主任也到不齐，人再少未免太不礼貌了。
[charslot(slot="m",name="avg_249_mlyss_1#9$1",focus="m")]
[name="缪尔赛思"]好了博士，等事情结束，我再单独答谢你。
[Dialog]
[Effect(name="$e_muesys_hide",layer = 1)]
[playsound(key="$d_avg_divebubble",volume=0.6)]
[charslot(duration=1)]
[delay(time=2.5)]
[Decision(options="怎么总是用分身敷衍人......;伊芙利特，你可能要单独行动了。", values="1;2")]
[Predicate(references="1;2")]
[stopmusic(fadetime=2)]
[delay(time=0.5)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=tr

... (全文27066字符)
```

### level_act25side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_893_1#1$1")]
[charslot(slot="r",name="avg_npc_897_1#1$1")]
[Background(image="29_g9_headquarter",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$skill_flash",volume=0.5,channel="x")]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]“科技是哥伦比亚的未来”并不是一句漂亮话或者广告语，雅拉主任，我今天像是一个第一次上科学课的孩子，真是大开眼界。
[name="杰克逊"]可惜时间太短，还有好多感兴趣的项目没来得及听你们讲解。
[charslot(slot="l",name="avg_npc_893_1#1$1",focus="l")]
[name="雅拉"]莱茵生命随时欢迎您的再次到来，杰克逊先生。
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]多谢你，雅拉主任。今天太过兴师动众，希望没有给你带来不便。
[charslot(slot="l",name="avg_npc_893_1#1$1",focus="l")]
[name="雅拉"]您太客气了，我今天只是您的导游而已。
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]能让曾经红极一时的玛丽安娜·布莱克女士充当导游，是我特里蒙之行的又一大收获。
[charslot(slot="r",name="avg_npc_897_1#6$1",focus="r")]
[name="杰克逊"]不瞒您说，我也是您的粉丝。
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]我收藏了您出道作品的签名海报，并把它贴在了我办公室的墙壁上。
[charslot(slot="l",name="avg_npc_893_1#10$1",focus="l")]
[name="雅拉"]真的吗？
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]实不相瞒，那正是我太太送我的就职礼物，哈哈。
[name="杰克逊"]帕瓦尔，有关莱茵生命在特区新建研发基地的申请，或许可以关照一下特区政府的推进。
[charslot(slot="r",focus="n")]
[name="副总统秘书"]记下来了，先生。
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]那么，今天的行程就到这里了，雅拉女士。
[charslot(slot="l",name="avg_npc_893_1#1$1",focus="l")]
[name="雅拉"]也祝您在特里蒙接下来的旅程顺利。
[charslot(slot="r",name="avg_npc_897_1#5$1",focus="r")]
[name="杰克逊"]......
[charslot(slot="r",name="avg_npc_897_1#1$1",focus="r")]
[name="杰克逊"]很好的祝福。
[name="杰克逊"]这一天已经过去，希望接下来也都是晴天。
[Dialog]
[charslot(duration=0.5)]
[Delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside",volume=0.5)]
[playsound(key="$skill_flash",volume=0.3,channel="x")]
[playsound(key="$skill_flash",volume=0.3,channel="y",delay=0.15)]
[name="记者"]快拍、快拍......
[playsound(key="$skill_flash",volume=0.3,channel="y",delay=0.3)]
[name="记者"]副总统先生，请问您如何评价这次的莱茵之旅？
[Dialog]
[charslot(slot="m",name="avg_npc_529_1#1$1",duration=0.5)]
[Delay(time=0.5)]
[name="莱茵职员"]各位不要着急，副总统先生特意留出了十分钟的时间接受采访，请有序发言。
[Dialog]
[charslot(duration=0.5)]
[Delay(time=1)]
[name="记者"]......
[Dialog]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playsound(key="$transmission")]
[charslot(slot="m",name="avg_249_mlyss_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_strangeclap")]
[Delay(time=0.5)]
[name="缪尔赛思"]你没有听错，我正在鼓掌。
[name="缪尔赛思"]“副总统与莱茵生命人力资源科主任相谈甚欢”“副总统访问助推莱茵生命的科技巨头之路”，我都能猜到这帮记者会配什么标题。
[name="缪尔赛思"]活动已经结束，现场没有异常情况，副总统将在十分钟后离开莱茵生命。
[name="缪尔赛思"]......博士。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_cherunder_2",screenadapt="coverall")]
[playsound(key="$transmission")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_895_1#1$1",duration=0.5)]
[Delay(time=0.5)]
[name="伊芙利特"]博士，已经收到了你传过来的路线图。
[charslot(slot="m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]也就是说，还有一条可供潜入的秘密路线，直通地下结构，但不在缪尔赛思给你的图纸上？
[charslot(slot="m",name="avg_npc_895_1#2$1")]
[name="伊芙利特"]交给我好了！
[name="伊芙利特"]你和迷迭香在上面跟动力甲打得热火朝天，我在连接层蹲守了半天，别说可疑的人了，压根就没有人......
[charslot(slot="m",name="avg_npc_895_1#5$1")]
[name="伊芙利特"]塞雷娅会来找我？
[charslot(slot="m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]那我也得先前往地下结构，不是说副总统还有几分钟就要离开了吗，得尽快排除风险才行。
[name="伊芙利特"]（压低声音）就这样，伊芙利特开始行动，博士。
[Dialog]
[playsound(key="$d_gen_transmissionget")]
[delay(time=1)]
[playsound(key="$rungeneral")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_901_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_901_1#1$1",posfrom = "-200,0", posto = "0,0",duration=1)]
[delay(time=1.5)]
[charslot(slot="r",focus="l")]
[name="特工A"]我回来了。
[charslot(slot="r",focus="r")]
[name="特工B"]上面怎么样了？
[charslot(slot="r",focus="l")]
[name="特工A"]听不太清楚，我没上到地面，但好像没什么特别的动静。
[name="特工A"]我估计，没得手。
[charslot(slot="r",focus="r")]
[name="特工B"]那我们？
[charslot(slot="r",focus="l")]
[name="特工A"]按照上校的命令，开启了讯号干扰，不支援任何其他单位......应该没有人查到这里来，斐尔迪南提供的潜入路径很隐蔽。
[name="特工A"]执行作战计划吧。对一下表......嗯，也差不多到时间了。
[name="特工A"]炸药怎么样了？
[charslot(slot="r",focus="r")]
[name="特工B"]你刚刚去查探情况的时候已经布置好了......两管改造过的塑性炸药，足够破坏这层防泄漏装置。
[name="特工B"]不过斐尔迪南也真够狠的，这可是他们能量科专用的液化源石气管道，他不是还说要回莱茵生命吗？
[charslot(slot="r",focus="l")]
[name="特工A"]按上校的说法，他和咱们现在是拴在一条线上的虫子，没得选择。
[charslot(slot="r",focus="r")]
[name="特工B"]不过我不明白现在搞这么一场爆破的意义在哪里......
[name="特工B"]副总统这个时间点应该已经离开莱茵生命了，大楼地下结构的液化源石气管道爆炸，能伤得到他吗？
[charslot(slot="r",focus="l")]
[name="特工A"]上校自有他的安排，执行命令就好了。
[Dialog]
[stopmusic(fadetime=1)]
[charslot(slot="r",focus="n")]
[CameraShake(duration=2, xstrength=25, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$e_imp_rockthrow")]
[playsound(key="$d_avg_sandstone")]
[delay(time=2)]
[charslot(slot="r",focus="l")]
[name="特工A"]什么人？
[charslot(slot="r",focus="r")]
[name="特工B"]一个......孩子？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_895_1#1$1",duration=1)]
[delay(time=1.5)]
[name="伊芙利特"]博士的情报真准，还真有人......
[charslot(slot="m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]喂，你们两个，虽然不知道你们躲在这里想干什么，但是可以投降了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[charslot(slot="r",name="avg_npc_899_1#1$1",focus="r")]
[charslot(slot="l",name="avg_npc_901_1#1$1",focus="l")]
[Background(image="29_g11_monitoringroom",screenadapt="coverall")]
[playMusic(intro="$m_bat_imprisonment_intro",key="$m_bat_imprisonment_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="av

... (全文17523字符)
```

### level_act25side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="38_g13_trimountlivingroom",screenadapt="coverall")]
[playMusic(intro="$lab_intro",key="$lab_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_391_rosmon_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_894_1#8$1",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_391_rosmon_1#7$1",focus="l")]
[name="迷迭香"]信是你写的吗？你想让我来到这里？
[charslot(slot="r",name="avg_npc_894_1#8$1",focus="r")]
[name="洛肯"]是的，孩子，我总是想着自己去找你。
[name="洛肯"]但时间实在太紧张了，我不得不拜托一位朋友把信送到了......罗德岛。对，罗德岛，就是这个名字。
[name="洛肯"]在那场灾难之后......我听说那家机构接纳了你。他们对你还好吗？
[charslot(slot="l",name="avg_391_rosmon_1#1$1",focus="l")]
[name="迷迭香"]他们是......家人。
[charslot(slot="l",name="avg_391_rosmon_1#9$1",focus="l")]
[name="迷迭香"]凯尔希医生，阿米娅，博士，煌，Raidian......还有小队里的大家，都是我的家人。
[charslot(slot="r",name="avg_npc_894_1#8$1",focus="r")]
[name="洛肯"]家人......这么说，你找到了一个新家......咳咳咳......
[charslot(slot="l",focus="n")]
瘦削的男人剧烈地咳嗽起来，本就不那么挺拔的身躯显得越发佝偻。
他注视着迷迭香，似乎想要走得更近一些，然而一道薄薄的水墙拦住了他的脚步。
不止缪尔赛思记起了他是谁，你同样也记得他的名字，那个在迷迭香的档案中被反复提及的名字。
这样一位理应待在监狱里的罪犯，竟突然出现在你们面前，就仿佛一位下班路上匆匆赶来看望孩子的长辈。
[dialog]
[Decision(options="你是一个人来的？;你独自......来找迷迭香？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="r",name="avg_npc_894_1#1$1",focus="r")]
[name="洛肯"]这只是我的愿望，和其他人都没关系。
[name="洛肯"]让我......让我好好看一看......
[charslot(slot="l",name="avg_391_rosmon_1#1$1",focus="l")]
[name="迷迭香"]......
[charslot(slot="r",name="avg_npc_894_1#8$1",focus="r")]
[name="洛肯"]......你长大了，孩子。
[name="洛肯"]这四年......不，是不是快五年了？这么长时间以来，我常常想起你。
[charslot(slot="r",name="avg_npc_894_1#5$1",focus="r")]
[name="洛肯"]每次想到我们分别的时刻，我总是感到......遗憾。
[charslot(slot="r",name="avg_npc_894_1#1$1",focus="r")]
[name="洛肯"]咳咳......咳咳咳。
[charslot(slot="r",name="avg_npc_894_1#5$1",focus="r")]
[name="洛肯"]我很遗憾......我没能从那些人手中保护你。那些眼里只有浅薄利益的庸人......他们彻底毁去了我们本可以一起抵达的未来。
[charslot(slot="l",name="avg_391_rosmon_1#4$1",focus="l")]
[name="迷迭香"]我们的未来？我们原本在一起生活吗？
[charslot(slot="l",name="avg_391_rosmon_1#7$1",focus="l")]
[name="迷迭香"]可是我不记得你。
[charslot(slot="l",name="avg_391_rosmon_1#2$1",focus="l")]
[name="迷迭香"]唔......我是不是应该记得的？我把所有不想忘记的事情都记在了终端上。
[charslot(slot="r",name="avg_npc_894_1#10$1",focus="r")]
[name="洛肯"]你忘了我？难道你丧失了记忆，完全忘记了我犯过的错？
[charslot(slot="l",name="avg_391_rosmon_1#10$1",focus="l")]
[name="迷迭香"]你是坏人吗？你对我做过很坏的事？
[charslot(slot="r",name="avg_npc_894_1#2$1",focus="r")]
[name="洛肯"]这不该由我来告诉你，孩子。这会让这次会面失去意义。
[charslot(slot="r",name="avg_npc_894_1#10$1",focus="r")]
[name="洛肯"]你的记忆损伤......不应该是当年实验的结果。难道还有人？梅兰德，还是莱茵生命？
[charslot]
[charslot(slot="m",name="avg_249_mlyss_1#8$1")]
[name="缪尔赛思"]别瞪我啊，威廉姆斯先生，我只是小小的生态科主任。
[name="缪尔赛思"]再说了，就算老山羊在这里，他那岌岌可危的道德底线也不会比你更低吧？
[charslot]
[charslot(slot="l",name="avg_391_rosmon_1#10$1",focus="n")]
[charslot(slot="r",name="avg_npc_894_1#6$1",focus="r")]
[name="洛肯"]这与道德无关。
[name="洛肯"]罗德岛，是你们删除了这孩子的记忆，操控了她的情绪吗？
[charslot(slot="l",focus="n")]
[dialog]
[Decision(options="我不接受这无端指责。;这不是罗德岛会做的事。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="r",name="avg_npc_894_1#2$1",focus="r")]
[name="洛肯"]是啊，不可能是你们做的。那可是我的作品......那样地精密，没有人能在她的生命机能照常运转的同时，剥夺掉特定的部分。
[charslot(slot="r",name="avg_npc_894_1#5$1",focus="r")]
[name="洛肯"]我明白了......还是因为我？只是当时没有足够的观察......对了......我们确实没有很多时间......意识的压力本就不是正常人能想象的......
[charslot(slot="r",name="avg_npc_894_1#7$1",focus="r")]
[name="洛肯"]......难道你把那些记忆交给了你的手足？
[charslot(slot="l",name="avg_391_rosmon_1#2$1",focus="l")]
[name="迷迭香"]唔......
[charslot(slot="l",name="avg_391_rosmon_1#1$1",focus="l")]
[name="迷迭香"]我......没有办法回答你。
[charslot(slot="r",name="avg_npc_894_1#2$1",focus="r")]
[name="洛肯"]让我想想，一定还有办法。
[name="洛肯"]那些事件的碎片毫无意义，就像当年那些记录与数据一样，活该被扫进垃圾堆。情感，形状，气味......气味......没错。
[charslot(slot="r",name="avg_npc_894_1#1$1",focus="r")]
[dialog]
[charslot(slot = "r",posfrom = "0,0", posto = "-100,0",duration = 1)]
[delay(time=2)]
[charslot(slot="l",name="avg_391_rosmon_1#4$1",focus="l")]
[name="迷迭香"]花......香？
[name="迷迭香"]这个味道......碾碎的汁水......涂抹在墙上，还有手上......
[dialog]
[delay(time=1)]
[charslot(slot="l",name="avg_391_rosmon_1#5$1",focus="l")]
[charslot(slot="l",focus="l",posfrom = "0,0", posto = "-50,0",duration=1)]
[name="迷迭香"]不......不......
[CameraShake(duration=0.3, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="迷迭香"]停下来，不要去想这些！我不要！
[charslot(slot="r",name="avg_npc_894_1#4$1",focus="r")]
[name="洛肯"]我知道，我就知道！我还留在你的大脑里！
[CameraShake(duration=0.3, xstrength=30, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="洛肯"]快想起来吧，求你了，孩子，记起对我的仇恨，让愤怒充满你的躯体，你的头脑，你无所不在的精神！
[dialog]
[charslot(slot ="l", action="shake", power=15, times=30, duration=0.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_391_rosmon_1#2$1",focus="l")]
[name="迷迭香"]呃......
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_894_1#1$1",focus="n")]
[Decision(options="停下。", values="1")]
[Predicate(references="1")]
[charslot]
[charslot(slot="m",name="avg_npc_894_1#1$1",focus="n")]
[Decision(options="请离开这里。;你正在伤害迷迭香。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]......伤害她？
[name="洛肯"]不，她的痛苦来自过去，而并非现在。我只是想送她一份她渴望已久的礼物。
[dialog]
[charslot(slot="m",focus="n")]
[Decision(options="这不是礼物。;这是折磨。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_npc_894_1#7$1")]
[name="洛肯"]你们真正理解过她的痛苦吗？
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]你们从梅兰德那里接收了关于她的全部信息，知晓了她所经历过的一切，难道不认为她有资格愤怒，有资格仇恨？
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]我知道了，你们和梅兰德是同路的，哈哈。你们希望更方便地掌控她，因为你们在害怕她，害怕......
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]......一件重拾怒火的武器。
[charslot(slot="m",focus="n")]
“武器”。
与迷迭香一起经历过的切尔诺伯格的一切都涌到了你眼前。那些拼命战斗时的决绝，那些生离死别时的疼痛。
是的，你过去听过很多遍这个词语，用来形容你身旁这个菲林女孩。每一次你都觉得非常刺耳，可只有这一次最难以忍受。
因为说出这句话的是洛肯·威廉姆斯，把迷迭香的命运推到这里的根源。
你已经想好了很多话来反驳他。你还想到，如果凯尔希在的话，应该能想出更多句子来反驳他。
但另一个念头先于一切字词冒了出来。
[dialog]
[Decision(options="（给他一拳）;（给他一脚）;（给他一巴

... (全文22389字符)
```

### level_act25side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="29_g8_alley_n",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_900_1#1$1",duration=1)]
[delay(time=2)]
[name="锡人"]呼......熟悉的下水道的气味，熟悉的路灯照不到的地方。
[name="锡人"]这些小巷真是每一条都长得差不多啊。
[name="锡人"]整座城市在那么短的时间内就从荒野上拔地而起，大概做城市规划的人也想不出那么多新主意。
[name="锡人"]唯一的问题大概是，走得多了也会想念一些新的风景。
[name="锡人"]我说得对吧，我的好部下？从上面俯瞰这座城市的感觉，是不是会好一些？
[dialog]
[playsound(key="$d_avg_wind")]
[charslot]
空无一人的小巷里起了一阵风。
还未来得及吐出去的烟圈全部钻回了金属缝隙里。锡人考虑着自己是否应该合时宜地呛咳几声。
[playsound(key="$d_avg_lighter")]
香烟一头的火星刚刚熄灭，打火机就已递到他面前。
[name="？？？"]对于这样一座没有历史的城市来说，“缺乏新意”还真是可悲的评价啊。
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]......霍尔海雅。
[name="锡人"]你的联络比预定时间晚了三天。
[dialog]
[charslot(slot="l",name="avg_npc_536_1#3$1",duration=1)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_536_1#3$1",focus="l")]
[name="霍尔海雅"]哦？在我的印象中，您也不是什么守时的人。
[dialog]
[playsound(key="$d_avg_elevator", loop=true,volume=0, channel="bgs")]
[soundVolume(volume=0.4, channel="bgs",fadetime=3)]
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]噪音很大。为什么选在这里见面？
[charslot(slot="l",name="avg_npc_536_1#1$1",focus="l")]
[name="霍尔海雅"]您忘了吗？这里距离十三区的工厂很近。
[StopSound(channel="bgs", fadetime=5)]
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]你找到那天的坠落物了？
[charslot(slot="l",name="avg_npc_536_1#9$1",focus="l")]
[name="霍尔海雅"]是啊，可惜只剩下碎片了。星星的......碎片，没有办法给迷途之人任何指引。
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]那克丽斯腾的下落呢？
[charslot(slot="l",name="avg_npc_536_1#1$1",focus="l")]
[name="霍尔海雅"]唔......
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]你在观察天空？
[charslot(slot="l",name="avg_npc_536_1#1$1",focus="l")]
[name="霍尔海雅"]还没有建起高楼的地方，果然能更清晰地看到星空啊。
[name="霍尔海雅"]您说克丽斯腾会不会躲到某颗星星上去？真要是那样的话，我们谁都没有办法找到她吧？
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]......霍尔海雅，你在两个月前进入了图书馆。
[charslot(slot="l",name="avg_npc_536_1#3$1",focus="l")]
[name="霍尔海雅"]我是一名历史学家，去图书馆难道不是我的本职工作吗？
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]是梅兰德的“图书馆”。
[name="锡人"]我并不记得自己批准过这次行动。
[charslot(slot="l",name="avg_npc_536_1#3$1",focus="l")]
[name="霍尔海雅"]您知道的，我总是容易控制不住自己的好奇心。
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]就像现在......
[dialog]
[charslot(slot="l",focus="all",posfrom = "0,0", posto = "60,0",duration=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_536_1#9$1",focus="l")]
[name="霍尔海雅"]上司先生，请容许我......说出一直以来我最好奇的问题。
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]什么问题？
[charslot(slot="l",name="avg_npc_536_1#3$1",focus="l")]
[name="霍尔海雅"]......那些烟。
[name="霍尔海雅"]除了吐出来的部分，进入您身体里的那几缕......究竟会钻去哪里呢？
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]这就是......你用尾巴尖抵着我胸口的原因吗？
[charslot(slot="l",name="avg_npc_536_1#6$1",focus="l")]
[name="霍尔海雅"]在您身上......我闻到了我最喜欢的历史的味道。
[name="霍尔海雅"]如果可能的话，我真的很想仔细地......仔细地探究您身上的每一个零件......从哪里开始比较好呢？您的头颅，胸膛，还是四肢？
[playsound(key="$d_avg_elevator", loop=true,volume=0, channel="bgs")]
[soundVolume(volume=0.6, channel="bgs",fadetime=1)]
[StopSound(channel="bgs", fadetime=2)]
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]......霍尔海雅。
[name="锡人"]你真的认为......背叛梅兰德基金会是个正确的选择？
[charslot(slot="l",name="avg_npc_536_1#3$1",focus="l")]
[name="霍尔海雅"]当然......不。
[name="霍尔海雅"]梅兰德掌握了这个国家最多的秘密。而在哥伦比亚，秘密能换取财富......秘密也是杀人的武器。
[name="霍尔海雅"]我花了整整三年的时间，才取得了进入历史协会的资格，又花了三年时间，取得了您的信任。
[charslot(slot="l",name="avg_npc_536_1#1$1",focus="l")]
[name="霍尔海雅"]您知道对我而言，六年时间意味着什么吗？梅兰德特工的身份，已经......等同于我七分之一的人生。
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r")]
[name="锡人"]那你就更不该在监狱里或者逃亡路上浪费你的余生。
[charslot(slot="l",name="avg_npc_536_1#1$1",focus="l")]
[name="霍尔海雅"]我知道......我知道。
[stopmusic(fadetime=1)]
[charslot(slot="l",name="avg_npc_536_1#9$1",focus="l")]
[name="霍尔海雅"]然而......假如仅剩的时间并不足以让我拥抱那些梦寐以求的秘密，那能再活十年还是一分钟，又有什么差别呢？
[dialog]
[charslot(slot="l",name="avg_npc_536_1#10$1",focus="l")]
[playMusic(intro="$m_bat_jakiller_intro",key="$m_bat_jakiller_loop", volume=0.6)]
[PlaySound(key="$d_avg_singleblunt", volume=1)]
[CameraShake(duration=0.5, xstrength=50, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[charslot(slot="l",focus="all",posfrom = "60,0", posto = "200,0",duration=0.5)]
[charslot(slot="r",name="avg_npc_900_1#1$1",focus="r",posfrom = "0,0", posto = "350,0",afrom = 1, ato = 0,duration=0.3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_npc_900_1#1$1",duration=0.5)]
[delay(time=0.5)]
[name="锡人"]梅兰德不会容许任何人，尤其是一名叛逃特工触碰不应触碰的信息。
[name="锡人"]很遗憾，你这最后一分钟，见到的只有我。
[dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_900_1#1$1")]
[PlaySound(key="$d_avg_magic_5", volume=1)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.01, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=false)]
[delay(time=0.3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.03, block=true)]
[charslot]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(slot = "m",name="avg_npc_536_1#10$1",posfrom = "0,0", posto = "300,0",afrom=0,ato=0,duration=0.1)]
[delay(time=0.1)]
[PlaySound(key="$d_avg_windmagic", volume=1)]
[charslot(slot = "m",posfrom = "300,0", posto = "0,250",duration = 0.6)]
[charslot(slot = "m",afrom = 1, ato = 0,duration = 0.5)]
[delay(time=1)]
[charslot(slot = "m",posfrom = "0,250", posto = "-50,0",afrom = 0, ato = 1,duration = 0.8)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_536_1#10$1")]
[name="霍尔海雅"]那我就只能向星辰祈祷......死人不会轻易开口了。
[charslot]
[charslot(slot="m",name="avg_npc_900_1#1$1")]
[name="锡人"]

... (全文42056字符)
```

### level_act25side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="29_g8_alley_n",screenadapt="coverall")]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_895_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_896_1#1$1",duration=1)]
[Delay(time=1)]
[PlaySound(key="$transmission", volume=1)]
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[delay(time=2)]
[name="塞雷娅"]果然，无法接通。
[charslot(slot="l",name="avg_npc_895_1#1$1",focus="l")]
[name="伊芙利特"]塞雷娅，你在给谁打电话？
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]锡人。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]那个铁皮大叔？他是不是出事了？
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]恐怕是的，否则，梅兰德不会加入对我们的追踪。
[name="塞雷娅"]军方和梅兰德达成协议了吗......为何掉转矛头针对我们，锡人身上究竟发生了什么？
[charslot(slot="l",name="avg_npc_895_1#1$1",focus="l")]
[name="伊芙利特"]塞雷娅，我按你教的方法侦察了一圈，士兵都撤走了，围堵我们的特工也撤退了。
[charslot(slot="r",name="avg_npc_896_1#5$1",focus="r")]
[name="塞雷娅"]如果她只是留下殿后，追兵不会消失。
[name="塞雷娅"]除非——她给出了能让对方满意的东西。
[charslot(slot="l",name="avg_npc_895_1#5$1",focus="l")]
[name="伊芙利特"]会不会是那个银色液体？刚才我在她身边看见过！
[charslot(slot="r",name="avg_npc_896_1#9$1",focus="r")]
[name="塞雷娅"]......递质？
[charslot(slot="r",name="avg_npc_896_1#10$1",focus="r")]
[name="塞雷娅"]她在359号基地和多萝西有所接触，递质无疑是从多萝西手上得到的，是多萝西希望她做些什么？
[name="塞雷娅"]不，多萝西还被军方扣押着，不可能想通过她去找军方和斐尔迪南。
[name="塞雷娅"]那么，是帕尔维斯还是......
[charslot(slot="l",name="avg_npc_895_1#6$1",focus="l")]
[name="伊芙利特"]塞雷娅......
[charslot(slot="r",name="avg_npc_896_1#10$1",focus="r")]
[name="塞雷娅"]别慌，伊芙利特。
[name="塞雷娅"]她会没事的。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]塞雷娅，我是想说，通讯器快被你捏坏了。
[dialog]
[charslot(slot="r",name="avg_npc_896_1#8$1",focus="r")]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]......多谢提醒。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]我才没慌，赫默又不是莽撞的人。
[name="伊芙利特"]她是和你聊过之后才留下的，我想，她肯定也是想了许多才做出这个决定。
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]......
[name="塞雷娅"]她不知道自己将要面对的是什么，国家机器的运转方式，远比她想象的要残酷。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]为什么你觉得她不知道？我觉得，赫默肯定也把这些都考虑进去了。
[name="伊芙利特"]赫默很努力的，我去找她的时候，她总是在工作，周围的人都说她好像在被什么无形的东西追赶着一样拼命。
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="l")]
[name="伊芙利特"]说不定等我们会合的时候，她已经漂漂亮亮地把事情搞定了！
[name="伊芙利特"]到时候我就会告诉她，虽然你丢下我我是有点生气啦，但是，我就知道你肯定能做到的。
[charslot(slot="l",focus="n")]
塞雷娅注意到伊芙利特的手在微微颤抖，她下意识地想要说些什么安慰伊芙利特。
但她发现，自己什么话也说不出口。
她意识到，即使伊芙利特的话语中有安慰自己的成分，但自己并不了解伊芙利特口中的那个赫默。
赫默做好了准备，赫默知道自己即将面临什么......
她从未这样考虑过。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]塞雷娅，你看那边。
[charslot(slot="r",name="avg_npc_896_1#3$1",focus="r")]
[name="塞雷娅"]嗯？
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]军方的人正在撤离......可去的并不是军方驻地的方向......
[name="塞雷娅"]难道递质真的是找到克丽斯腾的线索？
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]塞雷娅，我们偷偷跟上去吧。
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]......赫默最不希望的就是你再次陷入危险。
[charslot(slot="l",name="avg_npc_895_1#4$1",focus="l")]
[name="伊芙利特"]她刚刚都答应我们要一起行动了！
[name="伊芙利特"]她还说，“等塞雷娅醒了，她一定会回来的”“她就是这样的人”。
[charslot(slot="r",name="avg_npc_896_1#8$1",focus="r")]
[name="塞雷娅"]这并不是......
[charslot(slot="l",name="avg_npc_895_1#7$1",focus="l")]
[name="伊芙利特"]“这并不是最理性的做法”，好啦好啦，我知道你想说这个。
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="l")]
[name="伊芙利特"]我们不是去冒险，不是想浪费赫默的勇敢，而是一起去终点等她。
[charslot(slot="r",name="avg_npc_896_1#4$1",focus="r")]
[name="塞雷娅"]伊芙利特......
[charslot(slot="l",focus="n")]
不知怎的，她忽然发现，伊芙利特原来已经比几年前从实验室中被救出来时长高了不少。
在面临即将到来的危险时，她的眼中不是急躁和莽撞，而是勇敢和聪慧。
[charslot(slot="r",name="avg_npc_896_1#6$1",focus="r")]
[name="塞雷娅"]好，我们走。
[charslot(slot="l",name="avg_npc_895_1#2$1",focus="l")]
[name="伊芙利特"]太好了！
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="l")]
[name="伊芙利特"]对了，塞雷娅，我刚刚来到特里蒙的时候，看到了一颗坠落的星星。
[charslot(slot="r",name="avg_npc_896_1#3$1",focus="r")]
[name="塞雷娅"]星星？你是说十三区特莱顿工厂的坠落物......
[charslot(slot="l",name="avg_npc_895_1#3$1",focus="l")]
[name="伊芙利特"]就是星星啦！
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]赫默的故事里说，在星星落下来的时候，所有的分歧都会消失。
[name="伊芙利特"]你和赫默......一定会和好的，对吗？
[charslot(slot="r",name="avg_npc_896_1#1$1",focus="r")]
[name="塞雷娅"]......会的。
[charslot(slot="l",name="avg_npc_895_1#2$1",focus="l")]
[name="伊芙利特"]那就好！
[dialog]
[charslot(duration=1)]
[delay(time=1.5)]
会吗？
塞雷娅转头看向熟悉的特里蒙街道。
她忽然对自己即将踏上的道路感到了一丝陌生。
她经历过无数考验，眼下的情况还远没有到称得上糟糕的地步。
但她却第一次感到了失控。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="29_g7_mainstreet_n",screenadapt="coverall")]
[playMusic(intro="$sjoyasorrow_intro",key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "r",posfrom = "0,0", posto = "-200,0",duration = 0.1)]
[delay(time=0.2)]
[charslot(slot="r",name="avg_npc_534_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="无家可归的居民"]这该死的天，可太冷了！
[dialog]
[playsound(key="$bodyfalldown2",volume=0.7)]
[playsound(key="$d_avg_drivestop",volume=0.7)]
[charslot(slot="l",name="avg_npc_890_1#1$1",posfrom = "-150,0", posto = "-0,0",duration = 0.3,focus="all")]
[CameraShake(duration=0.3, xstrength=20, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r",posfrom = "-200,0", posto = "0,0",duration = 0.5)]
[Delay(time=0.8)]
[charslot(slot="l",name="avg_npc_890_1#1$1",focus="l")]
[name="斐尔迪南"]小心，有车过来了。
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="r")]
[name="无家可归的居民"]哎哟，差一点儿，都怪这天，把我冻糊涂了！
[name="无家可归的居民"]您相信吗，好心的先生，这天气都是对面那家科技公司操控的。
[name="无家可归的居民"]他们用无人机在天上喷洒药剂，使得我们每次呼吸都会加剧肺部结冰。
[name="无家可归的居民"]他们还想把我们都抓走，把我们的脑子浸泡在水缸里，让我们成为人造太阳的养料。
[charslot(slot="l",name="avg_npc_890_1#1$1",focus="l")]
[name="斐尔迪南"]......
[charslot(slot="r",name="avg_npc_534_1#1$1",focus="r")]
[

... (全文29359字符)
```

### level_act25side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="38_g3_rhinelab_corridor",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_894_1#1$1",duration=1)]
[Delay(time=2)]
[name="洛肯"]刚才很吵，大概是你们那个工程科主任又送东西来了。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_537_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="克丽斯腾"]......最后的调试工作还需要四十五分钟。
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[name="洛肯"]足够了。
[name="洛肯"]只要完成这些数据的传输......我这一生最具开创性的成果就完成了。
[charslot(slot="m",name="avg_npc_537_1#1$1")]
[name="克丽斯腾"]我会留下你的研究记录。
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[name="洛肯"]我知道。给那个叫霍尔海雅的年轻姑娘，或者随便谁......我不在乎。
[charslot(slot="m",name="avg_npc_894_1#8$1")]
[name="洛肯"]在我的生命即将走到尽头的时候，还能有机会完成这个研究，我差点就要忘记自己这一生的缺憾。
[name="洛肯"]哈哈......咳咳咳。
[name="洛肯"]还记得你第一次把这东西展现给我看的时候，我有多么难以接受。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]......哈哈。
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[name="洛肯"]哈哈哈......咳咳......咳......
[name="洛肯"]可笑。太可笑了。你摆在我面前的东西足以讽刺过往数百年来每一位自作聪明的科研者。
[name="洛肯"]......该死。我们的研究就好像毫无价值似的......
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]......
[name="洛肯"]......这是什么，克丽斯腾？
[name="洛肯"]你为什么能对它的原理和结果言之凿凿，哪怕你连实验都没有真正做过一次？
[charslot(slot="m",name="avg_npc_894_1#4$1")]
[name="洛肯"]这个东西......它的存在已经远超了我的理解。最可怕的是，你描述的那些关于这个黑色方块的天方夜谭，都是真的。
[charslot(slot="m",name="avg_npc_894_1#7$1")]
[name="洛肯"]告诉我，克丽斯腾。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]告诉我！我马上要研究的究竟是什么？！
[charslot(slot="m",name="avg_npc_537_1#1$1")]
[name="克丽斯腾"]这是你的工作。
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]......你从哪里得到它的？你从哪里得到这些知识的？
[charslot(slot="m",name="avg_npc_537_1#1$1")]
[name="克丽斯腾"]......
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]我就要死了，克丽斯腾。你总不能为难一个将死之人。
[name="洛肯"]谁赋予了你这些？谁把它交给你的？
[charslot(slot="m",name="avg_npc_537_1#3$1")]
[name="克丽斯腾"]......神。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_894_1#4$1")]
[name="洛肯"]......
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]难道是我高看了你了吗，年轻的天才？你也会装神弄鬼，对未知抱着多余的敬畏？
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]......不。你不是个会开玩笑敷衍我的人，你没那么下作。而你也不至于去寄希望于一些虚妄的信仰，那更可耻。
[name="洛肯"]我就当是这样吧。哼......多讽刺啊。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="38_g3_rhinelab_corridor",screenadapt="coverall")]
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="洛肯"]“神”。
[name="洛肯"]距离“神”垂怜我，又过去了一个多月。
[name="洛肯"]在这期间，我完成的工作，超越了我自己之前几十年的想象。
[name="洛肯"]哼，连我都不禁好奇......
[charslot(slot="m",name="avg_npc_894_1#7$1")]
[name="洛肯"]你想给我们......给生活在这片土地上的人们带来什么新的“神迹”？
[charslot(slot="m",name="avg_npc_537_1#4$1")]
[name="克丽斯腾"]......
[charslot(slot = "m", focus = "n")]
克丽斯腾没有答话。
她无言地望着窗外的漫天繁星，陷入沉思。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="38_g14_energywell",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_530_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="研究员"]怎么还有半个小时才下班啊......算了算了，先想想夜宵吃什么。
[name="研究员"]甜甜圈，炸羽兽，还是热狗？
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_890_1#1$1",duration=1)]
[Delay(time=2)]
[name="斐尔迪南"]整个特里蒙都为了这里乱成一团了，没想到里面竟然这么悠闲。
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]咳、咳咳......你是谁？
[charslot(slot="m",name="avg_npc_890_1#1$1")]
[name="斐尔迪南"]把整个能量井及附属设施的结构图纸和能源效率数据拿给我。
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]呃，先生，这都是绝密的。
[charslot(slot="m",name="avg_npc_890_1#6$1")]
[name="斐尔迪南"]你看清楚我的衣服和通行证了。还是说你想让我给你接通通讯，让布莱克亲自跟你解释？
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]不，不需要！我这就去整理......
[charslot(slot="m",name="avg_npc_890_1#1$1")]
[name="斐尔迪南"]不用了。就这台终端，打开它。
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]长官，这些都是比较粗糙的原始数据，缺乏可视化图表的话，可能不那么好、好理解......
[charslot(slot="m",name="avg_npc_890_1#1$1")]
[name="斐尔迪南"]......我是斐尔迪南·克鲁尼。
[name="斐尔迪南"]我是莱茵生命能量科主任。
[name="斐尔迪南"]整个特里蒙的能量循环系统是我设计的。你面前这台大型计算终端核心处理器所使用的源石能源转换公式以我的名字命名。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]斐尔迪南......公式？！您、您是......
[charslot(slot="m",name="avg_npc_890_1#6$1")]
[name="斐尔迪南"]你浪费了我整整两分钟时间。数据，现在。
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]好，好！当然！
[charslot(slot="m",name="avg_npc_890_1#1$1")]
[name="斐尔迪南"]......
[playsound(key="$keyboard")]
[charslot(slot="m",focus="n")]
时间一分一秒地过去。
斐尔迪南仿佛能听到军方的车队碾过街道的声音。布莱克极有可能就快找到克丽斯腾了。
他必须尽快......尽快干什么？
[charslot(slot="m",name="avg_npc_890_1#7$1")]
[name="斐尔迪南"]......这里，还有这里。
[name="斐尔迪南"]这两处数据有没有被修改过？
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]没有！先生，这些数据都是需要实时传给军方下辖的研究所的！有那么多双眼睛盯着，我怎么敢上传不真实的数据？
[name="研究员"]这都不是造假的问题，得罪军方的话，可是要......要......
[charslot(slot="m",name="avg_npc_890_1#5$1")]
[name="斐尔迪南"]......匹配不上。
[charslot(slot="m",name="avg_npc_530_1#1$1")]
[name="研究员"]您说什么？
[charslot(slot="m",name="avg_npc_890_1#6$1")]
[name="斐尔迪南"]我说，能量井的结构图、能源管线的分配和现有推进装置的效能都有问题。
[name="斐尔迪南"]很巧妙，啧。
[charslot(slot="m",name="avg_npc_530_1#1$1"

... (全文32493字符)
```

### level_act25side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="29_g4_corridor",screenadapt="coverall")]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_grass")]
[Delay(time=1)]
花......好漂亮呀。
你又来看我了吗？今天的花我不认识，你能不能教我怎么拼？
[dialog]
[charslot(slot="m",name="avg_npc_894_1#1$1",duration=1.5,bstart=0.9,bend=1,afrom=0,ato=0.7)]
[Delay(time=2)]
[name="熟悉的影子"]当然，纳西莎。你学会之后，想做什么呢？
和以前一样，我想把这些花瓣留下来，放进我的画本里。
妈妈最喜欢花，爸爸和你一样，懂很多植物知识。
虽然他们都不在了，但我想把这些新认识的花都记录下来，等去墓园的时候，讲给他们听。
你会带我去的，对吗？很快就要到四月了。
[name="熟悉的影子"]纳西莎，我的好孩子，你总是最坚强的那一个。
[name="熟悉的影子"]来吧，先把花放在那边的桌子上。等我忙完，我就教你拼写。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
好香。今天吃什么呢？
[dialog]
[charslot(slot="m",name="avg_npc_894_1#1$1",duration=0.5,bstart=0.9,bend=1,afrom=0,ato=0.7)]
[Delay(time=1)]
[name="熟悉的影子"]你怎么过来了？
[name="熟悉的影子"]快去那边乖乖坐好。今天我们吃你最爱的土豆汤。
好饿。能不能切快一些？
[name="熟悉的影子"]那你要不要自己试试看？没关系的，不要害怕，我来握住你的手。
[dialog]
[CameraShake(duration=0.5, xstrength=25, ystrength=6, vibrato=5, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_clothmovement",volume=0.5)]
[Delay(time=1.5)]
像......这样吗？
[name="熟悉的影子"]是的，孩子。你做得很好。你以后还会做得更好。
以后？是不是长大以后？我也会长得跟你一样高，一样有力气，变成很厉害的科学家？
[name="熟悉的影子"]不，你会比我更厉害，厉害得多。
[name="熟悉的影子"]纳西莎，后脑的伤口还痛吗？
不痛了。
哥哥们给了我很多糖吃。他们说，每天晚上睡觉之前吃一片，就不会感觉到痛，而且还会做棉花糖一样的梦。
[name="熟悉的影子"]乖孩子。
[name="熟悉的影子"]吃完饭之后，把这几片糖也吃掉，好不好？我想带你去一个地方。
走廊那边吗？
是不是哥哥们昨天去的地方？
他们说那里有一座很好看的植物园，就和你念的那些童话故事书里写的一样，你每次带来抚养院的花都是从那里采的。
[name="熟悉的影子"]是的。
[name="熟悉的影子"]进过那座植物园的，都会变成最被命运宠爱的孩子。
走廊的尽头是......
[dialog]
[MusicVolume(volume=0.2, fadetime=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Subtitle(text="迷迭香，迷迭香！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这扇门为什么打不开了？缪尔赛思，能不能想想办法，我们得跟上去！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="迷迭香......Rosmontis。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不要过去，至少不要一个人过去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[MusicVolume(volume=0.6, fadetime=3)]
[Delay(time=0.5)]
迷迭香。
Rosmontis是谁？
纳西莎......又是谁？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_npc_894_1#8$1",duration=1.5)]
[Delay(time=2)]
[name="洛肯"]欢迎。
[charslot(slot="m",name="avg_391_rosmon_1#1$1")]
[name="迷迭香"]你在等我？
[charslot(slot="m",name="avg_npc_894_1#8$1")]
[name="洛肯"]自始至终。
[charslot(slot="m",name="avg_391_rosmon_1#7$1")]
[name="迷迭香"]博士他们去哪里了？
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[name="洛肯"]他们留在原地。这场审判不需要多余的旁观者。
[charslot(slot="m",name="avg_391_rosmon_1#1$1")]
[name="迷迭香"]审判？
[name="迷迭香"]你说这里是法庭。那原告和被告都是谁？
[charslot(slot="m",name="avg_npc_894_1#2$1")]
[name="洛肯"]我，洛肯·威廉姆斯。
[name="洛肯"]都是我自己。
[charslot(slot="m",name="avg_npc_894_1#5$1")]
[name="洛肯"]在命运即将吞噬我的这最后一刻——
[name="洛肯"]我恳请你，来旁观我的一生。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="洛肯"]在此时此地，我承认我所有的罪。
[charslot(slot="m",name="avg_npc_894_1#1$1",bstart=0.2,bend=0.5)]
[name="“洛肯”"]贪婪。
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[name="洛肯"]当然。我的老师也曾这么痛斥过我。
[name="洛肯"]他斥责我的冒进，认为我从将死之人身上摘取感染器官的行径既违背法律，又有悖人伦。
[name="洛肯"]他认为我不仅没有帮到病人，反而加速了他们的死亡。
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]但他们本就快死了，甚至就连意识都不再清醒。我无意制造更多痛苦，也并未扭转他们的命运。
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[name="洛肯"]然而老师并不认同我的观点。在一场毫无公正可言的私下审判中，他和他的老师一起宣判了我在学术界的死刑。
[name="洛肯"]他们不愿承认，对于一名科学家来说，“贪婪”更像是一种美德。
[name="洛肯"]一个在小镇长大的孩子，从小受过的生物学教育仅限于如何为驮兽接生，除非他能够鼓起勇气，在半夜偷偷对刚出生的幼兽挥动解剖刀。
[name="洛肯"]是的，对知识的渴望足以压抑他共情生命的本能。他必须抓住一切机会，不断不断地攀登，才能继续在这条路上求索。
[charslot(slot="m",name="avg_npc_894_1#1$1",bstart=0.2,bend=0.5)]
[name="“洛肯”"]怯懦。
[charslot(slot="m",name="avg_npc_894_1#2$1")]
[name="洛肯"]我并不常常缺乏勇气，却唯独只为一件事情让步。
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]由于老师的举报，梅兰德给我下了禁令。这个可耻的烙印使得所有的大学和政府资助的研究机构都将我拒之门外。
[name="洛肯"]对一名正当盛年的科学家来说，这无疑是最残酷的刑罚。他们剥夺了我继续做研究的资格，等同于一次灵魂层面的谋杀。
[name="洛肯"]我甚至开始酗酒。长达一年零十个月的时间里，我强迫自己直面颤抖的双手，好忘掉没法握住解剖刀的痛苦。
[name="洛肯"]他们就是在那个时候找上我的。
[charslot(slot="m",name="avg_npc_894_1#1$1",bstart=0.2,bend=0.5)]
[name="“洛肯”"]他们，最无耻的人。
[charslot(slot="m",name="avg_npc_894_1#6$1")]
[name="洛肯"]国防部。他们愿意资助我成立洛肯水箱，条件是我必须在五年之内为他们制造出最有力的武器。
[name="洛肯"]科学是中性、纯粹且自由的，而实用价值——尤其是应用到武器研究的部分——只会拖累科学本身。
[name="洛肯"]我并不愿意为他们贡献自己的研究，但他们掐住了我的软肋。
[name="洛肯"]知识是昂贵的。我是一名实验科学家，仪器、设备、材料，甚至实验室的一砖一瓦，都需要钱来支撑。
[name="洛肯"]想要达成梦想，建成一座符合条件的实验室，远比修建特里蒙市中心耸立的高楼更费钱。
[charslot(slot="m",name="avg_npc_894_1#2$1")]
[name="洛肯"]我不得不承认自己的软弱，匍匐在他们的权威之下。
[charslot(slot="m",name="avg_npc_894_1#1$1",bstart=0.2,bend=0.5)]
[name="“洛肯”"]多么可悲。
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]这个国家、这个时代难道不比我更可悲？他们竟能容忍最野蛮的力量掌握科学前进的命脉！
[name="洛肯"]更何况军人先天是最为短视的人，他们掌着科学研究的舵，竟只想着把宝贵的知识应用到同类之间的互相厮杀上。
[charslot(slot="m",name="avg_npc_894_1#1$1",bstart=0.2,bend=0.5)]
[name="“洛肯”"]愚蠢。
[charslot(slot="m",name="avg_npc_894_1#4$1")]
[name="洛肯"]啊，愚蠢。对于一名科学家来说，愚蠢确实是最不能够被原谅的罪行。
[name="洛肯"]刚刚说到了军方那帮蠢货。他们其实很好糊弄，几亿的投资换来可以植入皮下的施术单元，就能堵上他们的嘴了。
[charslot(slot="m",name="avg_npc_894_1#1$1")]
[name="洛肯"]可我那时候太忙了。我醉心于自己的研究，无视了身边人的懦弱和野心。
[charslot(slot="m",name="avg_npc_894_1#10$1")]
[name="洛肯"]我的一个蠢笨的学生，竟然把我的实验数据的一部分交给了国防部。


... (全文33243字符)
```

### level_act25side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall")]
[playMusic(intro="$act25side_01_intro",key="$act25side_01_loop", volume=0.6)]
[Blocker(a=0.3, r=0.4, g=0.1, b=0.1, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_rosoutofcontrol", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.2, fadetime=3,channel="bgs")]
[PlaySound(key="$d_avg_broadswordblood")]
[CameraShake(duration=0.8, xstrength=50, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
切开。土豆被横向切开，一块又一块，抛进沸腾的水里。被手术刀切开的颅骨则要硬得多。
撕扯。人体最柔软的组织，就和棉花糖一样，只要被戴着胶套的手轻轻一撕就会散落一地。
[PlaySound(key="$d_avg_tear")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=20, randomness=90, fadeout=true, block=false)]
揉碎。花朵在颤抖的掌心被揉成一团，鲜艳的汁水把掌心弄得很黏很黏，还弄脏了新买的皮鞋。
尖叫。只要神经被仪器切断的速度足够快，就和巨量的麻醉剂一样，能在不被注意的情况下夺走生命。
哭泣。我死去的兄弟在手术台上哭泣。为什么被杀死的是他们？为什么被迫活下来的人是我？
不。不。
他们还没有死去。他们就站在我身后，拼命地捶打和呐喊。
从来都没有什么花园。有的只有残酷的囚禁、切割、摆弄我们生命的樊笼。
他们想要毁去这座樊笼。
我也想。
[Dialog]
[SoundVolume(volume=0, fadetime=2,channel="bgs")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="29_g4_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=3.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse")]
[delay(time=2)]
[charslot(slot = "m",name="avg_249_mlyss_1#11$1")]
[name="缪尔赛思"]实验室的外墙正在......被撕碎？这都是最新最坚硬的材料打造的，怎么会......就跟土豆一样？
[dialog]
[charslot(slot="m",focus="n")]
[Decision(options="迷迭香。;她可能失控了。;这是我最不想看见的事。", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot = "m",name="avg_249_mlyss_1#7$1")]
[name="缪尔赛思"]呜哇哇！那边的地面正在跟苹果皮一样卷起来呀！
[name="缪尔赛思"]再这样下去，我们都会变成压扁的果泥吧！
[dialog]
[charslot(slot="m",focus="n")]
[Decision(options="得有人去拉住她。", values="1")]
[Predicate(references="1")]
[Decision(options="阿米娅可以安抚迷迭香，但她不在这里。;我去试试......", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m",name="avg_249_mlyss_1#11$1")]
[name="缪尔赛思"]博士，你该不会是想自己......
[charslot(slot = "m",name="avg_249_mlyss_1#5$1")]
[name="缪尔赛思"]你没看见吗？动力甲都跟个小纸片一样被她撕来撕去，你只是个寻常的人类欸！你真的只是个人类吧？
[dialog]
[charslot(slot="m",focus="n")]
[Decision(options="如假包换。;......;那我也不会丢下迷迭香。", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot]
[delay(time=0.5)]
[charslot(slot = "m",name="avg_npc_895_1#9$1",duration=0.5)]
[delay(time=1)]
[name="伊芙利特"]......我去。
[dialog]
[charslot(slot="m",focus="n")]
[Decision(options="伊芙利特？", values="1")]
[Predicate(references="1")]
[charslot(slot = "m",name="avg_249_mlyss_1#11$1")]
[name="缪尔赛思"]这不是开玩笑的啊伊芙芙！
[name="缪尔赛思"]你体内的炎魔......唔，你的力量本来也很危险，你该不会是想......
[charslot(slot = "m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]不。
[name="伊芙利特"]我不会用它的力量。我自己去。
[name="伊芙利特"]这是......我和迷迭香之间的约定。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall")]
[charslot]
[SoundVolume(volume=0.2, fadetime=3,channel="bgs")]
[Blocker(a=0.3, r=0.4, g=0.1, b=0.1, fadetime=1.5, block=true)]
[delay(time=0.5)]
[charslot(slot = "m",name="avg_npc_526_1#1$1")]
[name="动力甲士兵"]申请......支援......
[dialog]
[PlaySound(key="$d_avg_maskbreakk")]
[delay(time=1)]
[name="动力甲士兵"]通讯器......被捏碎了？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="动力甲士兵"]你是什么......
[charslot(slot = "m",name="avg_npc_895_1#4$1")]
[name="伊芙利特"]别喊。
[charslot(slot = "m",name="avg_npc_526_1#1$1")]
[name="动力甲士兵"]什么？
[charslot(slot = "m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]我知道你想喊那两个字，但别喊出来。
[dialog]
[charslot(slot = "m",name="avg_npc_895_1#4$1")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.02, block=true)]
[PlaySound(key="$fireburst")]
[Effect(name="$e_magic_fire_01",y=-650,x=300,layer = 2,delay=0.2)]
[Effect(name="$e_magic_fire_01",y=-650,x=-300,layer = 5,delay=0.2)]
[Blocker(a=0.3, r=0.4, g=0.1, b=0.1, fadetime=1.5, block=false)]
[Effect(name="$e_magic_fire_01",y=-550,x=450,layer = 3,delay=0.4)]
[Effect(name="$e_magic_fire_01",y=-550,x=-450,layer = 6,delay=0.4)]
[Effect(name="$e_magic_fire_01",y=-450,x=650,layer = 4,delay=0.6)]
[Effect(name="$e_magic_fire_01",y=-450,x=-650,layer = 7,delay=0.6)]
[CameraShake(duration=2, xstrength=18, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2.5)]
[charslot(slot = "m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]她是我的朋友，我很喜欢的朋友。
[name="伊芙利特"]不，不止是朋友。我们还是同事，可以走在一条路上勾肩搭背，一起揍敌人的同事。
[name="伊芙利特"]迷迭香......
[dialog]
[charslot]
[CameraShake(duration=1.5, xstrength=15, ystrength=10, vibrato=40, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_391_rosmon_1#3$2",duration=1.5,action="shake", power=10, times=100)]
[delay(time=2)]
[name="迷迭香"]......不正确的，我都会毁掉。
[name="迷迭香"]这样的实验室，本来就......
[charslot(slot = "m",name="avg_npc_895_1#3$1")]
[name="伊芙利特"]本来就不该存在。
[charslot(slot = "m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]你想说的，我都明白。
[charslot(slot = "m",name="avg_npc_895_1#3$1")]
[name="伊芙利特"]这该死的白大褂，混蛋的实验室，那些害我们倒霉的玩意儿，早就该一把火全部烧掉了！
[name="伊芙利特"]我们当然有资格愤怒，有资格叫骂，有资格毁掉这一切！
[name="伊芙利特"]但我们同样可以不用这么做的！
[charslot(slot="m",name="avg_391_rosmon_1#3$2")]
[name="迷迭香"]为什么？
[name="迷迭香"]你也要......挡在正确的路前面？
[dialog]
[charslot(duration=0.5)]
[CameraShake(duration=3.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_skill_asyouwish",volume=0.3)]
[delay(time=2.5)]
[charslot(slot = "m",name="avg_npc_895_1#6$1")]
[name="伊芙利特"]好强......但是......也没什么大不了的！
[charslot(slot = "m",name="avg_npc_895_1#9$1")]
[name="伊芙利特"]迷迭香，我不会让你和达莉娅一样，在我面前......我们约好了一起好好看看这座城市，也约好了要一起回到罗德岛！
[charslot(slot = "m",name="avg_npc_895_1#3$1")]
[name="伊芙利特"]虽然我不太想承认，但你一直比我厉害得多！你已经是罗德岛的精英干员了，你做过很多很多了不起的事。
[name="伊芙利特"]想想阿米娅，想想那个叫煌的大猫，想想博士！他们的手掌很软，他们衣服上的味道很干净，他们的拥抱就像最厚实的毯子一样！
[charslot(slot="m",name="avg_391_rosmon_1#6$2")]
[name="迷迭香"]毯子......？
[charslot(slot = "m",name="avg_npc_895_1#3$1")]
[name="伊芙利特"]

... (全文26409字符)
```

### level_act25side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[delay(time=1)]
1099年11月21日
7:11 P.M. 聚焦发生器起飞三分钟后
[dialog]
[Background(image="38_g12_trimountrestarea",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$Tremont_intro",key="$Tremont_loop", volume=0)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_npc_223", duration=1, isblock=true)]
[name="研究员"]唔......嗯......
[name="研究员"]呼，好冷，他们又把暖气关了。
[name="研究员"]要投诉几次他们才能意识到会有人夜里在实验室加班......
[dialog]
[PlaySound(key="$d_avg_telephonering", volume=0.6, loop=true, channel="a")]
[delay(time=2)]
[playsound(key="$d_avg_telephone")]
[StopSound(channel="a", fadetime=0.5)]
[delay(time=1)]
[name="研究员"]喂，亲爱的，你怎么打电话来了？
[name="研究员"]等一下......我去外面和你说。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="29_g7_mainstreet_n",screenadapt="coverall",xScale=1.3,yScale=1.3,y=80)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="a")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="研究员"]今天是什么日子？
[name="研究员"]嗯......离项目死线还有九天，我们的进度很不乐观。
[name="研究员"]今天我也不回去了。
[dialog]
[delay(time=1)]
[name="研究员"]结婚纪念日？......啧。
[name="研究员"]抱歉，最近几天实在太忙了......我知道，亲爱的，那家餐馆你期待了很久......我知道，我知道，对不起。
[name="研究员"]副总统最近公开去了一趟莱茵生命，因为这事，董事会那些秃脑袋蠢货快疯了。
[name="研究员"]他们勒令所有项目组都要马上拿出阶段性成果，否则就滚蛋。
[name="研究员"]......我不是在找借口，亲爱的，这关乎......你听我说，今天真的不行，我之后一定会想办法补偿你。
[name="研究员"]喂？亲爱的，喂？
[dialog]
[PlaySound(key="$d_avg_phonestop", volume=1)]
[delay(time=2)]
[name="研究员"]......该死。
[name="研究员"]......如果发生点什么就好了。
[name="研究员"]办公楼大爆炸，暴徒袭击银行，特里蒙城的履带突然断了半边。
[name="研究员"]什么都好。
[dialog]
[charslot(slot = "m", focus = "n")]
夜色渐渐浓稠，办公楼的灯还要亮上一夜，阴影笼罩了可怜的研究员。
他打了个哆嗦，过几个星期该下雪了。突然有人撞了他一下。
[dialog]
[charslot(slot = "m", name = "avg_npc_223")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=0.5)]
[charslot(slot = "m", action="jump", posto="20,0", power=10, times=1, duration=0.5)]
[playsound(key="$bodyfalldown3")]
[delay(time=1.5)]
[name="研究员"]好吧，什么都没有。
[dialog]
[charslot(duration=0.5)]
[stopmusic(fadetime=3)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
他最终还是迈开脚步，向大楼走去。他强压下了想要再在外面待会儿的冲动，可此时，远处却有恼人的嗡鸣声传来。
[PlaySound(key="$d_avg_airdefensealert", volume=1, loop=true, channel="b")]
天灾警报无征兆地响起，要求避难的广播在街道上回荡，研究员下意识地想要加快脚步。
可是他猛然注意到，周围的人群渐渐停了下来，不约而同望向了天空。
他再次疑惑地抬起头。
[dialog]
[backgroundtween(yFrom=80,  yTo=-80, duration=2, block=false)]
[delay(time=1.5)]
[Image(image="38_i10", fadetime=1, screenadapt="coverall", xScale=1.1, yScale=1.1)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=10, block=false)]
[delay(time=1)]
[background]
[charslot(slot = "m", name = "avg_npc_223")]
[name="研究员"]......那是......什么？
[charslot]
[StopSound(channel="a", fadetime=1)]
[PlaySound(key="$d_avg_airshiptakeoff", volume=0, loop=true, channel="c")]
[SoundVolume(volume=1, channel="c",fadetime=2)]
缓缓旋转的巨大环形结构体正从楼宇背面浮出。
黑暗中，随着某些机械装置的展开，上面反射的城市霓虹为之变化，金属的色泽照得人睁不开眼睛。
它是如此宏伟磅礴，如此优美典雅，只该来自于人们最瑰丽的梦中，它在云层中穿行，它竟然......还在上升。
[SoundVolume(volume=0, channel="c",fadetime=5)]
[name="研究员"]一个，圈？
[dialog]
[StopSound(channel="a", fadetime=2)]
[StopSound(channel="b", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
7:13 P.M. 聚焦发生器飞行中
[dialog]
[Background(image="38_g1_rhinemeetingroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "r", name = "avg_npc_524_1$1", focus="none")]
[charslot(slot = "l", name = "avg_npc_892_1#1$1", focus="l")]
[name="小贾斯汀"]我很感兴趣，当然，我很感兴趣。
[charslot(slot = "r", name = "avg_npc_524_1$1", focus="r")]
[name="紧张的创业者"]真的吗？太好了！如果我们的项目能得到莱茵的赞助......
[charslot(slot = "l", name = "avg_npc_892_1#1$1", focus="l")]
[name="小贾斯汀"]请坐吧，女士，要喝点什么吗？
[charslot(slot = "r", name = "avg_npc_524_1$1", focus="r")]
[name="紧张的创业者"]啊......白水就好，贾斯汀先生。
[charslot(slot = "l", name = "avg_npc_892_1#1$1", focus="l")]
[name="小贾斯汀"]别这么见外，您可以喊我小贾斯汀。
[charslot(slot = "l", name = "avg_npc_892_1#1$1", focus="l")]
[name="小贾斯汀"]要来杯酒吗？高卢帝国虽然毁于战火，但感谢参战的将军们，他们依然为我们留下了那些最好的葡萄产区。
[charslot(slot = "l", name = "avg_npc_892_1#1$1", focus="l")]
[name="小贾斯汀"]请。
[charslot(slot = "r", name = "avg_npc_524_1$1", focus="r")]
[name="紧张的创业者"]好、好的，谢谢。
[dialog]
[charslot(slot = "r",  focus="none")]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_892_1#1$1", focus="l")]
[name="小贾斯汀"]请进。
[dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot = "m", name = "avg_npc_529_1#1$1", duration=1, isblock=true)]
[name="商务科文员"]主任，您办公室里的电话一直在响。
[charslot(slot = "m", name = "avg_npc_892_1#2$1")]
[name="小贾斯汀"]告诉他们，我现在正忙。
[charslot(slot = "m", name = "avg_npc_529_1#1$1")]
[name="商务科文员"]有些......您的朋友正在找您。
[charslot(slot = "m", name = "avg_npc_892_1#2$1")]
[name="小贾斯汀"]本杰明市长、克里斯市议员、费罗警长、柯莱特中校，还有谁？
[charslot(slot = "m", name = "avg_npc_529_1#1$1")]
[name="商务科文员"]负责工业区安保的那位刘易斯先生。
[charslot(slot = "m", name = "avg_npc_892_1#7$1")]
[name="小贾斯汀"]哼。
[charslot(slot = "m", name = "avg_npc_529_1#1$1")]
[name="商务科文员"]他们说——这位女士是？
[charslot(slot = "m", name = "avg_npc_524_1$1")]
[name="紧张的创业者"]啊，抱歉！我在外面等着！
[charslot(slot = "m", name = "avg_npc_892_1#7$1")]
[name="小贾斯汀"]没关系，您不用回避。
[name="小贾斯汀"]请继续。
[charslot(slot = "m", name = "avg_npc_529_1#1$1")]
[name="商务科文员"]啊，好的。
[name="商务科文员"]......他们表示，他们对您之前存在七号地块里的东西非常不满，他们原本以为只是一些，更“平常”的项目。
[name="商务科文员"]柯莱特中校去了刘易斯先生那里，恐怕明天所有七号地块的监控文件就会丢失了。
[name="商务科文员"]市长和市议员退回了这几年我们送去的所有手提箱，并声明往后的竞选活动不会再寻求您的帮助。
[name="商务科文员"]警长先生做了些很......激进的表述，听说他已经紧急拿到了州检察官的逮捕令，恐怕现在正在来这里的路上。
[name="商务科文员"]我已经通知了防卫科，但拖延不了他们多少时间。
[charslot]
[charslot(slot = "r", name = "avg_npc_524_1$1", focus="none")]
[charslo

... (全文24407字符)
```

### level_act25side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Dialog]
[Background(image="29_g7_mainstreet_n",screenadapt="coverall")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]博士，我们必须马上离开这里。
[name="凯尔希"]我找到了克丽斯腾的能量源。
[charslot(slot = "m", name = "char_003_kalts_1#3")]
[name="凯尔希"]趁一切还没有不可挽回，趁我预想中的那种最坏的可能还没有发生......
[name="凯尔希"]我们仍然有机会阻止她。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="这里怎么会有石棺？",values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]克丽斯腾的计划需要大量的能量，这种能量的规模和纯度都是现代泰拉人无法掌握，乃至无法想象的。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="所以，她使用了这座石棺的技术？",values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]这能量之庞大，一座石棺也无法支撑。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="那，她是怎么......",values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]我说的是，“一座”石棺也无法支撑。
[name="凯尔希"]我没想到......居然在哥伦比亚。
[name="凯尔希"]居然就在这片荒野之下。
[name="凯尔希"]博士，我需要你的帮助。
[name="凯尔希"]能帮助我的......也只能是你。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="迷迭香呢？;我很担心迷迭香的状况。",values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]......
[name="凯尔希"]战斗已经结束，她不会有危险。
[name="凯尔希"]请相信迷迭香，她还是个孩子，但她也是罗德岛的精英干员。
[name="凯尔希"]也请你相信......你与她共度的岁月。
[name="凯尔希"]无论是我们在切尔诺伯格的行动，还是她在罗德岛的日子，这些过去都没有被虚掷，这些经历同样在塑造着她。
[name="凯尔希"]她会做出自己的选择，我们也只能尊重这种选择。
[name="凯尔希"]只是......现在，同样也轮到我们了。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
7:45 P.M. 聚焦发生器抵达能量井上方
[dialog]
[Background(image="38_g2_colombiaoffice",screenadapt="coverall")]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_526_1#1$1")]
[charslot(slot = "l", name = "avg_npc_526_1#1$1")]
[PlaySound(key="$d_gen_surfacefrozen", volume=1, loop=false, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Effect(name="$e_fist_hit_02",x=180,layer = 1)]
[Effect(name="$e_fist_hit_02",x=-180,layer = 1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[StopSound(channel="a", fadetime=2)]
[charslot(slot = "l", posfrom="0,0", posto="0,-100", afrom=1, ato=0, duration=1)]
[charslot(slot = "r", posfrom="0,0", posto="0,-100", afrom=1, ato=0, duration=1)]
[CameraShake(duration=0.8, xstrength=60, ystrength=60, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_mechadown")]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_896_1#10$1",duration=1.5, isblock=true)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_896_1#10$1",focus="n")]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[PlaySound(key="$d_avg_strangeclap", volume=1)]
[delay(time=1.5)]
[charslot]
[name="？？？"]精彩。
[name="？？？"]我一直很好奇，你是怎么在面对那一堆研究项目的同时，还练出这么好的身手的。
[name="？？？"]我以为我已经把时间利用得够好了，你不睡觉的吗？
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]你怎么会在这里？
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]斐尔迪南。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_890_1#6$1",duration=1.5)]
[delay(time=2)]
[name="斐尔迪南"]这问题该我问，塞雷娅，你闯进军方在特里蒙的特种作战办公室，想干什么？
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......
[charslot(slot = "m", name = "avg_npc_890_1#2$1")]
[name="斐尔迪南"]我猜，你想找一个能追上天上那玩意的东西。
[name="斐尔迪南"]比如，劫持一架军方的重型无人机，然后把自己绑在上面？
[charslot(slot = "m", name = "avg_npc_890_1#1$1")]
[name="斐尔迪南"]是不是想得太简单了些，塞雷娅主任？我原本以为你没有这么感情用事。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]让开，斐尔迪南。现在我没时间和你啰嗦。
[charslot(slot = "m", name = "avg_npc_890_1#2$1")]
[name="斐尔迪南"]瞧瞧，多可怜，唯三......好吧，科考科的那家伙不算，唯二被总辖排除在她的那些了不起的大计划之外的主任，居然在这里相会了。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]......
[charslot(slot = "m", name = "avg_npc_890_1#2$1")]
[name="斐尔迪南"]你想做什么，阻止那个疯子？
[charslot(slot = "m", name = "avg_npc_890_1#1$1")]
[name="斐尔迪南"]还是......挽救她？
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]我不需要向你汇报什么。
[charslot(slot = "m", name = "avg_npc_890_1#1$1")]
[name="斐尔迪南"]放心，我也无意评价你与克丽斯腾之间的关系。
[name="斐尔迪南"]我在这里就是为了等你。
[name="斐尔迪南"]听好了，塞雷娅，我不是来找你麻烦的。
[charslot(slot = "m", name = "avg_npc_896_1#2$1")]
[name="塞雷娅"]我说，让开。
[charslot(slot = "m", name = "avg_npc_890_1#6$1")]
[name="斐尔迪南"]我说，“听好了”。
[dialog]
[PlaySound(key="$d_avg_plane", volume=1)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="38_i01", xScale=1.3, yScale=1.3, screenadapt="coverall")]
[ImageTween(xScaleFrom=1.15, yScaleFrom=1.15, xScaleTo=1, yScaleTo=1, duration=60, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="塞雷娅"]......飞行器的声音。
[name="塞雷娅"]斐尔迪南，这架飞行器是哪里来的？
[name="斐尔迪南"]“地平弧光计划”不仅是现在克丽斯腾开着的飘在天顶的超级武器，它是一整套战略方案。
[name="斐尔迪南"]我动用了点关系，借用了一架用于“弧光一号”检修的飞行器，顺便把剩下的都炸了。
[name="斐尔迪南"]要知道，整个哥伦比亚，能在接近阻隔层高度安全行驶的载人飞行器可不多。
[name="斐尔迪南"]他们从特区重新调配高空飞行器需要的时间不会很多，但对于你，对于我，都已经足够了。
[name="塞雷娅"]你在向我提出合作。
[name="塞雷娅"]你以为，你真的有这个资格？
[name="斐尔迪南"]你还是老样子，塞雷娅。
[name="斐尔迪南"]一副就算没有我帮忙，你也有本事解决一切麻烦的样子。
[name="斐尔迪南"]不过，我对此倒是没有丝毫怀疑。
[name="斐尔迪南"]塞雷娅，就像我之前说的，我们之间没有必要起冲突。
[name="斐尔迪南"]聚焦发生器已经飞抵能量井上空，能量井已经开始聚能。
[name="斐尔迪南"]如果放任现在的局势发展，无论克丽斯腾想干什么，这件事的结局最终如何，国防部势必遭到清算。
[name="斐尔迪南"]而莱茵生命，作为“帮凶”，我们都能猜到它的下场。
[name="塞雷娅"]而无论是作为军方的白

... (全文22810字符)
```

### level_act25side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="bg_cave_2",screenadapt="coverall")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="凯尔希"]......
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[name="霍尔海雅"]你的表情很有意思。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="（她的尾巴缠上来了喔。）;......;（该让Mon3tr出场了吧！凯尔希！）",values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]......放开博士吧。
[name="凯尔希"]你可以去找你想要的东西，如果那真的能解决你的疑惑。
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[name="霍尔海雅"]......嗯哼......
[charslot(slot = "m", name = "avg_npc_536_1#1$1")]
[name="霍尔海雅"]......什么？就这样？
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]我们保证不会对你的行动做出任何反应。
[charslot(slot = "m", name = "avg_npc_536_1#10$1")]
[name="霍尔海雅"]......看塞雷娅和锡人对你的态度，我还以为你是个很危险的人物，怎么？
[name="霍尔海雅"]你的弱小是真的吗？你表露出的神态可不像一个真的没有反抗能力的人。
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]任君想象。
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]但你明白，为了博士的安全，我不会以身犯险。
[charslot(slot = "m", name = "avg_npc_536_1#11$1")]
[name="霍尔海雅"]......似乎是这样。
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[name="霍尔海雅"]既然已经和梅兰德基金会撕破了脸皮，少几个敌人也是好事......克丽斯腾的计划已经启动，自由活动的时间想必也不多了。
[name="霍尔海雅"]话就说到这里，在特区过激的反应开始之前——
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_536_1#1$1")]
[name="霍尔海雅"]——！
[dialog]
[PlaySound(key="$d_avg_magic_2", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot = "m", action="shake", power=10, times=100, isblock=true, duration=0.5)]
[charslot(slot = "m", action="jump", posto="-200,0", power=20, times=1, afrom=1, ato=0, duration=0.5)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[delay(time=1)]
[name="霍尔海雅"]什么？
[dialog]
[charslot]
[PlaySound(key="$d_avg_cavewaterdrop", volume=0.6, loop=true, channel="a")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_900_1#1$1", duration=1.5, isblock=true)]
[name="锡人"]......唉，确实。总不能真的让特区陷入危险，我们要加快控制事态的速度了。
[name="锡人"]既然是梅兰德基金会的叛徒，确实不该让外人解决，凯尔希勋爵。
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]你没有那么愚钝，你是故意放纵霍尔海雅的，想借机行事。
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]......哦，你猜到我会顺着叛徒追过来？被勋爵利用了一把，真是令人怀念的事情。
[name="锡人"]谈不上故意放纵，派到克丽斯腾身边的特工们接二连三地叛变，不禁让我产生了自我怀疑......做检讨可是要花时间的。
[name="锡人"]那么，事关二位性命，勋爵您是不是有些太托大了？如果放出您漆黑的仆从，擒住她也不是什么难事。
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]......“这里”没有办法使用任何武器。
[name="凯尔希"]我们已经在“正上方”了。
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]......您这一句话已经足以引起梅兰德基金会相当程度的重视，凯尔希勋爵，除非您在故弄玄虚。
[dialog]
[PlaySound(key="$d_avg_windmagic", volume=1)]
[bgeffect(name="$eb_windburst",layer=1)]
[charslot(slot = "m", action="shake", power=8, times=100, duration=0.5, isblock=true)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", action="jump", posto="200,0", power=5, times=1, duration=0.5,isblock=true)]
[charslot(slot = "m", posfrom="200,0", posto="300,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_536_1#3$1", posfrom="-300,0", posto="200,0", duration=2, isblock=true)]
[name="霍尔海雅"]真是......意料之外，锡人。您有几副身体？
[name="霍尔海雅"]您的可怜的金属脑袋不是被我扔在洛肯那里了吗？
[charslot(slot = "l", name = "avg_npc_536_1#10$1")]
[name="霍尔海雅"]这次您会放过我吗？还是说，我得再杀您一次，才能从梅兰德基金会的控制下逃脱？
[charslot]
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]（古老的萨卡兹语）我们一会再聊，叛徒。
[dialog]
[charslot(slot = "m", name = "avg_npc_536_1#3$1")]
[PlaySound(key="$d_avg_magic_2", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[charslot(slot = "m", action="shake", power=8, times=100, isblock=true, duration=0.5)]
[charslot(slot = "m", name = "avg_npc_536_1#1$1")]
[name="霍尔海雅"]唔......！
[charslot(slot = "m", name = "avg_npc_536_1#11$1")]
[name="霍尔海雅"]（视野在变黑？他对我的眼睛——不，是精神上——四肢动不了——）
[dialog]
[charslot(slot = "m", action="shake", power=4, times=40, isblock=true, duration=0.5)]
[charslot(slot = "m", posfrom="0,0", posto="0,-50", duration=0.5)]
[delay(time=1)]
[charslot(slot = "m", posfrom="0,-50", posto="0,-100", afrom=1, ato=0, duration=0.5)]
[playsound(key="$bodyfalldown2")]
[delay(time=1)]
[charslot]
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]......看来法术在这里还是有用的。
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]源石技艺不在对“武器”的检测范围内。
[name="凯尔希"]况且即使是以一位死魂灵全部的力量，也无法对其重要的部分造成丝毫损伤。
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]那么我怀里的源石炸药与施术单元呢？
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]太原始了。
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]这可是哥伦比亚最顶尖的技术，可以轻而易举地把我们埋在这大地深处。
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]所以您还有什么没有告诉梅兰德基金会的？
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]......
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]无论是作为哥伦比亚人还是作为萨卡兹，都不足以让我与您同行？
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]从始至终，我就只希望博士一人抵达那里。
[name="凯尔希"]那位莱茵生命的总辖，已经是个意外了。
[dialog]
[charslot(slot = "m", focus="none")]
[Decision(options="......我？",values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[name="锡人"]这恐怕不是您说了算的。除开我在梅兰德基金会的职责，我也对这片曾是古老家乡的土地兴趣浓厚。
[name="锡人"]也许那里有关于卡兹戴尔的线索，恐怕我不能就这么——
[dialog]
[PlaySound(key="$transmission", volume=1)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_900_1#1$1")]
[na

... (全文27960字符)
```

### level_act25side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="38_g8_storage",screenadapt="coverall")]
[delay(time=1)]
[playMusic(intro="$act17_intro", key="$act17_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_energybody", volume=1)]
[delay(time=1.5)]
[name="？？？"]我命令你回答我，仆从。
[dialog]
[Decision(options="仆、仆从......？;......;我可不是凯尔希的仆从......",values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot = "m", name = "char_003_kalts_1#1", duration=1, isblock=true)]
[name="凯尔希"]......Dr.{@nickname}失去了记忆。博士并不是你认识的那些人中的任何一个，不再是了。
[name="凯尔希"]博士现在是泰拉的一员，罗德岛的一员。
[name="凯尔希"]我们已经共同经历了许多，直至今日。
[charslot]
[name="？？？"]......罗德岛？
[name="？？？"]（未知语言）罗德岛？
[name="？？？"]......原来如此。
[name="？？？"]所以，“失忆”。为什么你不把所有事情重新告诉这个......“博士”？
[charslot(slot = "m", name = "char_003_kalts_1#1")]
[name="凯尔希"]......
[charslot]
[name="？？？"]啊，我知道了。
[name="？？？"]你始终在怀疑这个“博士”的真实性。比起复原一段不再可信的记忆，你更相信一个重新认识世界的他。
[name="？？？"]嗯......也不奇怪。地面上发生的一切都做不得假，如果真的有足够的干预，泰拉不该是如今的形态。
[name="？？？"]看来并没有任何事情如我们所愿。尽管你不记得了......Dr.{@nickname}。
[name="？？？"]这是多么难得的机会。在这里，遇见你们。却是这样的情况......
[dialog]
[Decision(options="......",values="1")]
[Predicate(references="1")]
[name="？？？"]那么，失忆的“Dr.{@nickname}”与自称凯尔希的AMa-10，你们来这里又是为了什么？
[name="？？？"]克丽斯腾让你们感到紧张吗？这一切超出了你们的控制吗？
[dialog]
[Decision(options="你好像还没有回答我的问题。;别这么高高在上！;自我介绍是平等交谈的开始。",values="1;2;3")]
[Predicate(references="1;2;3")]
[name="？？？"]......
[name="？？？"]我是计划的人格模拟，数万年来始终守望着这座黑暗的大厅，还有数十万同胞冰冷的身体。
[name="？？？"]我曾是最后的希望，一次悲观的尝试，一个虚无主义的代名词。
[name="？？？"]但现在，或许对渺小的你们而言......我是克丽斯腾疯狂计划的帮凶和幕后黑手。
[name="？？？"]我是行将就木的“保存者”，敬畏你眼里的所有，我是文明的消亡本身。
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="38_g15_energywell_glowed",screenadapt="coverall")]
[delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_1031_slent2_1#1$2", duration=1.5, isblock=true)]
[name="赫默"]位置没错，递质的反应......很强烈......
[charslot(slot = "m", name = "avg_1031_slent2_1#4$2")]
[name="赫默"]我——
[dialog]
[charslot(slot = "m", posfrom="0,0", posto="0,-80", duration=0.5)]
[charslot(slot = "l",  name = "avg_npc_893_1#9$1", posfrom="-300,0", posto="0,-50", duration=0.5, isblock=true)]
[PlaySound(key="$bodyfalldown3", volume=1)]
[delay(time=1)]
[charslot(slot = "m", posfrom="0,-80", posto="0,0", duration=1.5)]
[charslot(slot = "l", posfrom="0,-50", posto="0,0", duration=1.5, isblock=true)]
[charslot(slot = "m", posfrom="0,0", posto="250,0", duration=2, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_1031_slent2_1#9$2", focus="m")]
[name="赫默"]雅拉主任......？
[name="赫默"]您怎么在这里？
[charslot(slot = "l", name = "avg_npc_893_1#9$1", focus="l")]
[name="雅拉"]你带着我的祝福，走到了这里，也好。
[charslot(slot = "m", name = "avg_1031_slent2_1#1$2", focus="m")]
[name="赫默"]......
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]您......是为了阻止我而来的。
[charslot(slot = "l", name = "avg_npc_893_1#10$1", focus="l")]
[name="雅拉"]你没有松开我送你的武器，我很高兴。
[name="雅拉"]看起来你也并不是因为一腔热血才站在这里的。
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]是的。
[charslot(slot = "l", name = "avg_npc_893_1#9$1", focus="l")]
[name="雅拉"]这是你最后的机会了，孩子。
[name="雅拉"]抽身而出，还是继续？
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]我会......学着成为您所说的战士的，雅拉主任。
[charslot(slot = "l", name = "avg_npc_893_1#9$1", focus="l")]
[name="雅拉"]......
[name="雅拉"]赫默，你很清楚，克丽斯腾不会把聚焦发生器接收的能量对准大地上任何一处城镇。
[name="雅拉"]你没有必要阻止她。
[name="雅拉"]她只是和所有科学家一样，准备向无人曾踏足的地方前进罢了。
[charslot(slot = "m", name = "avg_1031_slent2_1#1$2", focus="m")]
[name="赫默"]也许吧，雅拉主任。
[charslot(slot = "m", name = "avg_1031_slent2_1#2$2", focus="m")]
[name="赫默"]我并不如您一样了解总辖，但如果是您说的话，我愿意相信。
[charslot(slot = "m", name = "avg_1031_slent2_1#1$2", focus="m")]
[name="赫默"]但我会继续试着停下这一切，就算是您挡在我面前也不例外。
[charslot(slot = "l", name = "avg_npc_893_1#1$1", focus="l")]
[name="雅拉"]......为什么？
[charslot(slot = "m", name = "avg_1031_slent2_1#1$2", focus="m")]
[name="赫默"]因为，如果总辖就这么进行了她无论是什么的实验，并且获得了成功——
[name="赫默"]我们都知道，她可是莱茵生命的总辖，无论是出于情感上的信任还是理性的判断，她都很有可能成功。
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]您认为，哥伦比亚的研究者们会怎么看待她？
[name="赫默"]您在莱茵生命的人力资源考察科工作了这么久，这里的人您再了解不过。
[charslot(slot = "l", name = "avg_npc_893_1#8$1", focus="l")]
[name="雅拉"]......英雄。
[name="雅拉"]克丽斯腾会成为哥伦比亚科学界的英雄和偶像。
[charslot(slot = "m", name = "avg_1031_slent2_1#1$2", focus="m")]
[name="赫默"]是啊，她会成为科学家的榜样，成为研究者的标杆。
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]......然后，这样的事就再也不会停止。
[name="赫默"]一桩一桩，一件一件，研究者们乐此不疲。
[name="赫默"]但是，雅拉主任，只有她是克丽斯腾·莱特，只有她。
[charslot(slot = "m", name = "avg_1031_slent2_1#10$2", focus="m")]
[name="赫默"]其他的那些自诩引领者与天才的人呢？其他的那些被这种所谓的“不择手段的拓荒精神”鼓舞的人呢？
[name="赫默"]其他那些将自己的偏执或理想付诸实践，无所顾忌的人呢？
[name="赫默"]那些贪婪的，狂妄的，冒进的，顽固的，与我们一样的人呢？
[name="赫默"]如果他们都把如同莱茵生命的总辖一般行事作为美德——
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]如果是您，一定能想象到，那是怎样一种未来。
[charslot(slot = "m", name = "avg_1031_slent2_1#4$2", focus="m")]
[name="赫默"]或许我们都不用想象......
[name="赫默"]您对莱茵生命已经做过的那些研究，也从来不是一无所知。
[charslot(slot = "l", name = "avg_npc_893_1#9$1", focus="l")]
[name="雅拉"]我很清楚，赫默。
[name="雅拉"]我很清楚，特里蒙，不，哥伦比亚的国土内，曾发生过，且正发生着多少这样的事情。
[name="雅拉"]曾有无数疯狂而诱人的计划摆在我的面前，拿出这些东西的人眼神明亮，笑容真诚。
[name="雅拉"]他们衷心地以为他们在为“纯粹的科学”效力，是我们认知原野的拓荒者。
[charslot(slot = "m", name = "avg_1031_slent2_1#5$2", focus="m")]
[name="赫默"]而您和您的同僚们，只需要评估他们的实验计划里，宏伟蓝图下，会不会偶尔也要付出一点点“代价”和“损耗”。
[charslot(slot = "l", name = "avg_npc_893_1#9$1", focus="l")]
[name="雅拉"]“代价”。
[name="雅拉"]这种代价有时是一片肥沃的土地，有时是若干个绝症病人或者死刑犯；有时是一个村落或一个城镇，有时是某个特定的种族乃至国家。
[charslot(slot = "l", name = "avg_npc_893_1#6$1", focus="l")]
[name="雅拉"]在我看来，也有时，是他们自己。
[charslo

... (全文20536字符)
```

### level_act25side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[playMusic(intro="$newhope02_intro",key="$newhope02_loop", volume=0.6)]
曾经，对于这片大地，抬头仰望没有意义。
那里不值得被观察，那里不值得被探索，那里是湎于幻想之人的归宿。
可是，现在，每个人都在抬头仰望，抬头仰望那道连接天与地的光束。
仰望着从来便触不可及的天空。
[Dialog]
[Background(image="38_g18_1",screenadapt="coverall",y=100)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
星辰中，在光流中显得如此渺小的人造物，正酝酿着属于这个时代的，人类的野心。
[Dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="38_g3_rhinelab_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$rungeneral", volume=1)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_896_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_890_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]克丽斯腾，克丽斯腾......
[name="斐尔迪南"]你果然早就做好了计划，国防部之前所有的行动都只是在做无用功。
[charslot(slot = "right", name = "avg_npc_890_1#6$1",focus="r")]
[name="斐尔迪南"]哈！这到底是什么原理？这种高能约束场的效率与稳定性......我从没听说过。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]我记得你在刚加入莱茵的时候，向我吹嘘过，你是高能物理领域最好的科学家。
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]......之一。
[dialog]
[PlaySound(key="$keyboard", volume=1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_890_1#5$1",focus="r")]
[name="斐尔迪南"]天哪。
[name="斐尔迪南"]塞雷娅，你该庆幸，你所涉猎的学术领域里没有一位克丽斯腾这样的人物。
[charslot(slot = "right", name = "avg_npc_890_1#7$1",focus="r")]
[name="斐尔迪南"]很不公平。而她......甚至不屑于发表这些成果。
[charslot(slot = "left", name = "avg_npc_896_1#10$1",focus="l")]
[name="塞雷娅"]聚焦发生器正在蓄能。
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]按照军方的“地平弧光计划”，等充能阶段结束，这些能量将会聚焦并二度激发，在大范围内进行强力打击。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]好。还要充多久？
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]克丽斯腾把计划书变成了废纸......我只能说，不会太久。
[charslot(slot = "left", name = "avg_npc_896_1#10$1",focus="l")]
[name="塞雷娅"]这是我们停下它的最后机会。
[name="塞雷娅"]也是停下她的最后机会。
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]......
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]斐尔迪南，你还在发什么愣，我们的时间不多。
[charslot(slot = "right", name = "avg_npc_890_1#6$1",focus="r")]
[name="斐尔迪南"]塞雷娅，看看那边的密度仪。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]指针好像很不稳定。
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]不，不是指针，摇摆是高能约束场的正常现象。我说的是......读数单位。
[name="斐尔迪南"]你可以猜猜，这个单位，是我实验室里仪表的多少倍。
[name="斐尔迪南"]它刚才吸收的能量，足足能够维持整个哥伦比亚所有移动城市至少半年的消耗。
[name="斐尔迪南"]它甚至依然没有停下的迹象。
[name="斐尔迪南"]而我们，现在就在承载了如此庞大能量的实验室中央。
[charslot(slot = "left", name = "avg_npc_896_1#5$1",focus="l")]
[name="塞雷娅"]......
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]即使娜斯提天纵之才，她也制造不出能储存超出现有认知水平的能量的容器。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]你的意思是——
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]无论它最终将能量聚焦向什么方向，只要二度激发开始，这座实验室就一定无法幸免于难。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]她的目标从未变过。
[charslot(slot = "right", name = "avg_npc_890_1#6$1",focus="r")]
[name="斐尔迪南"]如果她的目标真的是天空，如果天空必须要用这个等级的能量才能挑战......
[name="斐尔迪南"]天上究竟有什么？
[charslot(slot = "left", name = "avg_npc_896_1#5$1",focus="l")]
[name="塞雷娅"]......我不关心。
[name="塞雷娅"]我只知道，这是一场冒进而无谋的实验。
[charslot(slot = "right", name = "avg_npc_890_1#6$1",focus="r")]
[name="斐尔迪南"]而且注定坠落。
[name="斐尔迪南"]塞雷娅，你现在完全可以打道回府，找个视野开阔的山坡，一边喝酒，一边欣赏一朵或许将永载哥伦比亚史册的烟花。
[charslot(slot = "left", name = "avg_npc_896_1#9$1",focus="l")]
[name="塞雷娅"]那种情况不会发生。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]你呢？你不会这么冒险。
[charslot(slot = "right", name = "avg_npc_890_1#7$1",focus="r")]
[name="斐尔迪南"]我？
[dialog]
[charslot(slot = "right",focus="n")]
[PlaySound(key="$d_gen_soldiersrun", volume=0.7)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]看来是我的老朋友来了，他们的速度比我想的要快。
[name="斐尔迪南"]你说得对，我可不打算冒险，技术手册上记录了逃生舱段的位置，我知道在哪。
[name="斐尔迪南"]我没兴趣去见开除我的那个人，你也用不上我帮忙。
[name="斐尔迪南"]记录眼下这种高能物理现象的机会很少，我不会错过这样的机会。也许下个季度你能在学报上看到我的新论文。
[name="斐尔迪南"]我保证，那一定会是划时代的一篇。
[name="斐尔迪南"]克丽斯腾把她所有的智慧都绑在了个人的偏执上，我和她不一样。
[charslot(slot = "right", name = "avg_npc_890_1#6$1",focus="r")]
[name="斐尔迪南"]我不会同意......她把这些足以改变整个泰拉学界的知识就此葬送。
[name="斐尔迪南"]忙你的去吧，塞雷娅，我们的时间都不多。
[charslot(slot = "left", name = "avg_npc_896_1#1$1",focus="l")]
[name="塞雷娅"]保重。
[dialog]
[charslot(slot = "left",posfrom = "0,0", posto = "-100,0",afrom = 1, ato = 0,duration = 0.5)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "left",name="avg_npc_899_1#1$1",posfrom = "-200,0", posto = "0,0",duration = 1.5)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_899_1#1$1",focus="l")]
[name="布莱克"]斐尔迪南。
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]好久不见，上校。
[charslot(slot = "left", name = "avg_npc_899_1#1$1",focus="l")]
[name="布莱克"]你能活下来，我不意外，但如果我是你，我会假装自己已经死了。
[name="布莱克"]离开这里，跑去维多利亚或者莱塔尼亚，凭你的本事，谋一份教职总是可以的。
[charslot(slot = "right", name = "avg_npc_890_1#1$1",focus="r")]
[name="斐尔迪南"]这不像是你会说出的话，上校。
[charslot(slot = "left", name = "avg_npc_899_1#3$1",focus="l")]
[name="布莱克"]我再说一遍，斐尔迪南，已经结束了。
[name="布莱克"]我和副总统已经谈过了，国防部输得很彻底。
[name="布莱克"]至于这件事还能不能被挽回，我的命最终会交到谁的手上，我其实已经没那么关心了。
[name="布莱克"]让我们留些体面吧，斐尔迪南，滚开，我可以省下一支弩箭留给自己。
[charslot(slot = "right", name = "avg_npc_890_1#7$1",focus="r")]
[name="斐尔迪南"]......你在说什么？抱歉，我刚刚没注意听。
[name="斐尔迪南"]还有，你挡住射线仪的显示屏了。
[stopmusic(fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=2)]
[name="赫默"]这座能量井，比我想象的要深得多......
[name="赫默"]恐怕军方根本没有完全掌握它的结构。
[name="赫默"]这里......是递质反应最强的地方

... (全文19971字符)
```

### level_act25side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_prison_commandroom",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[playsound(key="$d_avg_labamb", loop=true, channel="a",volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_1031_slent2_1#1$1",duration=1)]
[charslot(slot = "right", name = "avg_npc_531_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_1031_slent2_1#1$1",focus="l")]
[name="赫默"]您......
[charslot(slot = "right", name = "avg_npc_531_1#1$1",focus="r")]
[name="帕尔维斯"]我......我最近总是在背中枢神经系统的基本结构，一遍又一遍，从头背到尾。
[charslot(slot = "left", name = "avg_1031_slent2_1#9$1",focus="l")]
[name="赫默"]......这难道不是生物学入门课程的作业吗？
[charslot(slot = "right", name = "avg_npc_531_1#1$1",focus="r")]
[name="帕尔维斯"]是啊，基础中的基础，如果我的学生被我问到这个问题，哪怕愣上一秒钟，我都会给他的课程成绩打C。
[name="帕尔维斯"]但是......这些日子，我没有完整背出来过一次，没有一次。
[name="帕尔维斯"]不停地中断，不停地遗忘，不停地从头开始，然后循环。
[name="帕尔维斯"]每天早晨，我在莱茵总部对面的早餐店里，从五点坐到七点，我用尽了一切方法。
[name="帕尔维斯"]我的神经在退行。我研究了一辈子的东西，却在这个时候弃我而去。
[name="帕尔维斯"]也许只要五年，或者三年，我就会变成一个只会晒太阳的痴呆老人，把我五十八年以来所有的骄傲与满足，遗忘得干干净净。
[name="帕尔维斯"]赫默，我不能以这样的方式退场。
[charslot(slot = "left", name = "avg_1031_slent2_1#4$1",focus="l")]
[name="赫默"]......老师......
[charslot(slot = "right", name = "avg_npc_531_1#1$1",focus="r")]
[name="帕尔维斯"]我的终点已经注定了。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="帕尔维斯"]现在，离开我的实验室。别碰它！
[charslot(slot = "left", name = "avg_1031_slent2_1#5$1",focus="l")]
[name="赫默"]......我不能。
[name="赫默"]“超人”“强大的灵魂”......或许真的有这种人，他们超越时代，超越局限，超越这片大地，但绝不会是您，老师。
[name="赫默"]您说的这些话，正属于被您嘲笑的，卑微的、弱小的“庸众”。
[name="赫默"]一个“人”的愿望。
[charslot(slot = "right", name = "avg_npc_531_1#1$1",focus="r")]
[name="帕尔维斯"]......超越时代，超越局限，超越这片大地？
[name="帕尔维斯"]我......
[charslot(slot = "left", name = "avg_1031_slent2_1#5$1",focus="l")]
[name="赫默"]在米诺斯或者谢拉格的故事里，神祇是万事万物的恩赐者、掌握者、决定者。
[name="赫默"]但科学绝不是神，科学是供人通行的道路罢了。它需时时被审视，时时被修缮，时时被规范。
[name="赫默"]它带给我们的不该是狂人创想中的奇伟未来，而正是“人们的平庸期待”。
[dialog]
[charslot(slot = "left",focus="all")]
[charslot(slot = "left",posfrom = "0,0", posto = "50,0",duration = 0.5)]
[delay(time=0.5)]
[charslot(slot = "r",posfrom = "0,0", posto = "80,0",duration = 0.8)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_531_1#1$1",focus="r")]
[name="帕尔维斯"]不......不。离它远点，赫默！
[charslot(slot = "left", name = "avg_1031_slent2_1#1$1",focus="l")]
[name="赫默"]老师，结束了。
[name="赫默"]您需要的是充足的休息，之后，我会陪您去医院。
[dialog]
[charslot]
[StopSound(channel="a", fadetime=1)]
[Stopmusic(fadetime=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_glass_break")]
[delay(time=2)]
[charslot(slot = "m", name = "avg_1031_slent2_1#1$1")]
[name="赫默"]......递质的中枢已经被摧毁。
[charslot(slot = "m", name = "avg_1031_slent2_1#5$1")]
[name="赫默"]无论是您的实验，还是克丽斯腾的计划，缺少了递质的参与，应该——
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]......哈哈。
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[name="帕尔维斯"]超越这片大地啊......
[name="帕尔维斯"]是啊，也许......我还有一项了不起的成就，这连我自己都没有在意。
[name="帕尔维斯"]没投入多少时间，只是顺手为之，甚至，不来自于我自己的项目。
[name="帕尔维斯"]不过，也没什么关系吧。
[name="帕尔维斯"]当然，当然，我为什么没有注意到呢？
[name="帕尔维斯"]我们都被她所吸引......从一开始，我们就是一起上的路。
[charslot(slot = "left",focus="n")]
老人呆呆地看着显示屏，监控画面中，悬浮于天顶的人造巨环被能量束照亮，磅礴的银白色聚集其间。
或许是因为递质中枢被破坏，或许是因为能量束的冲刷太过猛烈，聚焦发生器正在微微抖动着。
[charslot(slot = "m", name = "avg_1031_slent2_1#9$1")]
[name="赫默"]唔——
[name="赫默"]为什么，递质的反应还没有停下？
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]赫默，我问你，如果无法成为那个引领者，那么，成为追随者是可耻的吗？
[name="帕尔维斯"]如果我承认我的羸弱和犹疑，那么，跟随那个真正强大的灵魂，也是一种选择，对吧？
[name="帕尔维斯"]这原本只是我的保险方案，但是现在......
[charslot(slot = "m", name = "avg_1031_slent2_1#9$1")]
[name="赫默"]您......在干什么......
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]我已经庸碌太久了，我必须......
[name="帕尔维斯"]我仍可以追上她，她也必须闪耀。
[name="帕尔维斯"]我所有的努力，我所有的追索......必须有意义。
[name="帕尔维斯"]至少，这比成为一个昏聩的痴呆老人......要好得多。
[name="帕尔维斯"]能量的密度已经够大了，只要......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_1031_slent2_1#10$1")]
[name="赫默"]老师，老师！帕尔维斯，你在做什么！
[charslot]
赫默感受到，递质对于自己的影响正在褪去，与此同时，眼前这位年迈的卡普里尼，意识也在飞速消散。
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]超越者踏上她的旅程，我想......她不在意，自己的长路跟上了个......胆小的搭车客。
[name="帕尔维斯"]至少，我参与其中......
[multiline(name="帕尔维斯",delay=0.1)]赫默，看啊——
[charslot(slot = "m", name = "avg_1031_slent2_1#10$1")]
[name="赫默"]您在把自己的意识和递质融合？以弥补中枢被破坏的——不！
[dialog]
[charslot(slot = "m", name = "avg_1031_slent2_1#5$1")]
[playsound(key="$d_avg_typewriter")]
[delay(time=1)]
[name="赫默"]该死，这些数据——相位完全紊乱，会有什么后果？
[name="赫默"]该怎么把这些反应停下！老师！帕尔维斯！
[name="赫默"]这种尝试没有意义！您的意识无法保留在递质中！
[name="赫默"]这种传递，只会彻底破坏您的神经系统——
[charslot]
一声微微的叹息，或许是一声轻笑。
帕尔维斯的身体已经成了一具空壳，再没有任何一点意志存于其间，那些执着，那些怯懦，都消散无痕。
[charslot(slot = "m", name = "avg_1031_slent2_1#9$1")]
[name="赫默"]老师？
[charslot]
[name="帕尔维斯"]——
监控中，微微抖动着的聚焦发生器似乎在渐渐平稳下来。
他完成了自己的实验，以意料之外的方式。
[charslot(slot = "m", name = "avg_1031_slent2_1#9$1")]
[name="赫默"]......不......
[dialog]
[charslot(slot = "m", name = "avg_1031_slent2_1#4$1", posfrom = "0,0", posto = "0,-50", afrom=1, ato=1, duration = 0.6,isblock=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=20, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2", volume=0.7)]
[delay(time=1.5)]
[name="赫默"]怎么会......
[charslot(slot = "left",focus="n")]
[dialog]
[delay(time=2)]
[name="？？？"]赫默，赫默——
[name="？？？"]赫默，你在这里吗？
[charslot(slot = "m", name = "avg_1031_slent2_1#4$1", posfrom = "0,-50", posto = "0,-50", duration = 0,isblock=true)]
[name="赫默"]我......
[charslot(slot = "left",focus="n")]
[name="？？？"]赫默，你真的在这里！
[name="？？？"]我来了，退后一点！
[dialog]
[charslot]
[delay(time=0.5)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.03, block=true)]
[CameraShake(duration=1, xstrength=30, ystrength

... (全文25498字符)
```

### level_act25side_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[Background(image="38_g4_rhinelab_corridor_rised",screenadapt="coverall")]
[playMusic(intro="$act15_intro",key="$act15_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playsound(key="$alarmenter")]
[Blocker(a=0.3, r=0.7, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]——
[charslot(slot = "m", name = "avg_npc_902_1#1$1")]
[name="总辖构件科雇员"]这边！
[name="总辖构件科雇员"]围住她，别让她过去！
[dialog]
[charslot]
[CameraShake(duration=1.5, xstrength=10, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_npc_902_1#1$1")]
[name="总辖构件科雇员"]全体注意，做好准备！
[charslot(slot = "m", name = "avg_npc_896_1#5$1")]
[name="塞雷娅"]......
[charslot]
[playsound(key="$d_avg_weightloss", loop=true, channel="bgs")]
[CameraShake(duration=-1, xstrength=10, ystrength=6, vibrato=30, randomness=90, fadeout=false, block=false)]
失重感再次袭来。
[playsound(key="$d_avg_curdlesaipunch")]
钙质结晶迅速生长，将塞雷娅的手与走廊地面相连。
[charslot(slot = "m", name = "avg_npc_902_1#1$1")]
[name="总辖构件科雇员"]第二波“失序”开始！
[charslot(slot = "m", name = "avg_npc_896_1#3$1")]
[name="塞雷娅"]......失序？
[charslot(slot = "m", name = "avg_npc_896_1#9$1")]
[name="塞雷娅"]娜斯提的杰作。
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[MusicVolume(volume=0.4, fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[CameraShake(duration=0.1, xstrength=10, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="29_g9_headquarter",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_891_1#1$1",duration=1)]
[delay(time=1.5)]
[name="娜斯提"]你跟着我兜兜转转好几天了。防卫科原来这么闲？
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]你对莱茵园区的改建有十六处不符合之前制定的安全规范。
[charslot(slot = "m", name = "avg_npc_891_1#7$1")]
[name="娜斯提"]（萨卡兹语）失序。
[dialog]
[bgeffect(name="$eb_dim_closeeye",layer=1)]
[delay(time=0.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[dialog]
[name="塞雷娅"]......
[name="塞雷娅"]你......
[name="娜斯提"]放弃你脑子里的平衡。不要对抗混乱，去尝试着适应它的节奏。
[name="塞雷娅"]......
[dialog]
[bgeffect]
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="娜斯提"]看到你想看的了吗？
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]你重组了园区几处关键结构。看起来没什么规律......但部件之间的连接关系是自洽的。
[name="塞雷娅"]我很难想象这样的建筑能够成立。
[charslot(slot = "m", name = "avg_npc_891_1#1$1")]
[name="娜斯提"]线性的语言约束了大部分人的想象力。
[name="娜斯提"]想要抵达某个未来的话，你首先得与终点建立对话，而不是去强行规划它的路线。
[Dialog]
[MusicVolume(volume=0.6, fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot = "m", name = "avg_npc_896_1#9$1")]
[Background(image="38_g4_rhinelab_corridor_rised",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="塞雷娅"]放弃......平衡。
[name="塞雷娅"]感受终点......
[dialog]
[charslot(duration=0.5)]
她松开双手。
[playsound(key="$d_avg_weightloss", loop=true, channel="bgs")]
[CameraShake(duration=-1, xstrength=10, ystrength=6, vibrato=30, randomness=90, fadeout=false, block=false)]
下一轮重力变换突然到来，她撞上了天花板，趁势调转方向，刚好跃过了一众追兵的头顶。
钙质结晶跟着在她身侧飘起来，在半空中划出一道弧线。
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[MusicVolume(volume=0.4, fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraShake(duration=0.1, xstrength=10, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]用微生物结构形态变化的思路去操控钙元素......极具启发性。
[name="帕尔维斯"]这样的材料转化很快，而且适应性极强，能与人体各部分器官快速结合，有很好的医学应用前景。
[name="帕尔维斯"]这是你在大学时候就一直在做的研究方向吧？为什么不继续做下去？
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]......因为它很危险。
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]你是指人造器官的应用伦理问题？
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]不止。
[name="塞雷娅"]新的技术交给医生，可以拯救生命；落入罪犯手里，就可能沦为凶器。
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]哈哈，差点忘了，人体本身富含钙元素。
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]所以我判断，在行之有效的管控手段被确立之前，这项研究必须被中止。
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]你知道这很可惜，对吧？
[name="帕尔维斯"]要是你改主意的话，莱茵生命完全可以拥有两个专攻生命科学的科室。
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]莱茵生命更需要有防卫科。
[name="塞雷娅"]我把自己的数据交给你，是希望你结合我的经验，更好地评估嵌合实验的风险。
[name="塞雷娅"]别走得太远了，帕尔维斯。触碰边界的代价对所有人来说都过于高昂。
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]那么，边界在哪里呢？
[charslot(slot = "m", name = "avg_npc_532_1#1$1")]
[name="塞雷娅"]嗯？
[charslot(slot = "m", name = "avg_npc_531_1#1$1")]
[name="帕尔维斯"]无数研究表明，生命的演化并不像最早的学者猜想的那样循序渐进。一步一回头的话，我们甚至都走不到这里。
[name="帕尔维斯"]而且，假设确实有一个更高意志存在，是它划定了边界，决定了人类的来路和去路——
[name="帕尔维斯"]那在决定成为仆从还是举起反旗之前，我们不都该尝试着直视它的眼睛吗？
[Dialog]
[MusicVolume(volume=0.6, fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="38_g4_rhinelab_corridor_rised",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_896_1#9$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......“边界”。走廊就是边界。
[name="塞雷娅"]如果继续沿着走廊走......永远走不到“眼睛”的位置。
[charslot(slot = "m", focus = "n")]
“聚焦发生器”。
这座环形的实验室自诞生之初，就准备好了颠覆人们的认知。
它是克丽斯腾梦想的实现，是真

... (全文20831字符)
```

### level_act25side_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$act25side_01_intro",key="$act25side_01_loop", volume=0.6)]
[Delay(time=1)]
[Background(image="38_g7_arc_on",screenadapt="coverall")]
[Background(image="38_g6_arc",screenadapt="coverall")]
[CameraShake(duration=2.5, xstrength=20, ystrength=20, vibrato=50, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[Background(image="38_g6_arc",screenadapt="coverall",fadetime=0.1,block=true)]
[Background(image="38_g7_arc_on",screenadapt="coverall",fadetime=0.3)]
[Background(image="38_g6_arc",screenadapt="coverall",fadetime=0.3,block=true)]
[Background(image="38_g7_arc_on",screenadapt="coverall",fadetime=0.2,block=true)]
[Background(image="38_g6_arc",screenadapt="coverall",fadetime=0.1)]
[PlaySound(key="$d_avg_spiritwhoosh")]
[Background(image="38_g7_arc_on",screenadapt="coverall",fadetime=1)]
[Delay(time=2)]
星星与大地相撞。
满地洁白的碎屑中，一个人抬起头来。
[Dialog]
[charslot(slot = "m", name = "avg_npc_896_1#10$1",duration=1)]
[Delay(time=1.5)]
[name="塞雷娅"]怎么了总辖？你比以前退步了。
[name="塞雷娅"]既然你这一下没能杀我，我就要还击了。
[name="塞雷娅"]别眨眼。
[dialog]
[charslot(slot = "m", name = "avg_npc_896_1#11$1")]
[charslot(slot="m",action="zoom",poszoom="0.47,0.5",scale=1.2,duration=0.2,afrom = 1, ato = 0.5)]
[Effect(name="$e_fist_02",layer = 1,x = -150,y=180,roz=120)]
[Blocker(a=0.7, r=1, g=1, b=1, fadetime=0.5, block=false)]
[charslot(duration=0.3)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_punchairwall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=false)]
[charslot(slot = "m", name = "avg_npc_537_1#7$1")]
[Effect(name="$e_fist_hit_02",y=150,x=100,layer = 1)]
[PlaySound(key="$b_char_defboost")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="克丽斯腾"]......
[charslot(slot = "l", name = "avg_npc_537_1#7$1",posfrom = "0,0", posto = "200,0",duration = 0,isblock=true)]
[charslot(slot = "m", focus = "n")]
被塞雷娅击落的星星们重新浮起，形成全新的轨道。
[dialog]
[curtain(direction = 6,fillfrom = 0.5,fillto = 1,grad = true,fadetime=1,a=0)]
[charslot(slot = "m",posfrom = "0,0", posto = "50,0",afrom = 1, ato = 0,duration = 1)]
[Delay(time=1)]
克丽斯腾的手指划向一侧。
[charslot]
[playsound(key="$d_avg_weightloss", loop=true, channel="bgs",volume=0.5)]
[charslot(slot = "m", name = "avg_npc_896_1#10$1",focus="n")]
[CameraShake(duration=-1, xstrength=0, ystrength=3, vibrato=40, randomness=90, fadeout=false, block=false)]
塞雷娅的双脚突然变得重若千钧。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]引力......变化？
[name="塞雷娅"]你用这一招送走了缪尔赛思。
[name="塞雷娅"]但这对我无效。
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_gen_surfacefrozen")]
珐琅质在塞雷娅的脚下生长，就像一双沉重的靴子，将她钉在原地。
随后，是一点点地前进。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]你没有再提升钙质化对粒子的重构精密度，而是大幅度提升了释放速度。
[name="克丽斯腾"]你生成的珐琅质甚至变得更脆弱了。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]强硬地对抗......并不足以走到终点。
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$bottlebroken")]
一颗金属星球突破了珐琅质的屏障，砸中了塞雷娅的肩膀。
塞雷娅没有停下脚步。
[dialog]
[Effect(name="$e_fist_hit_01",x=-90,y=110,layer = 1)]
[charslot(slot = "m",posfrom = "0,0", posto = "5,0",duration=0.2,focus="n")]
[CameraShake(duration=0.3, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_punchsp4",volume=0.8)]
[Delay(time=0.31)]
[charslot(slot = "m",posfrom = "5,0", posto = "0,0",duration=0.3,focus="n")]
[CameraShake(duration=-1, xstrength=0, ystrength=3, vibrato=40, randomness=90, fadeout=false, block=false)]
[Delay(time=1)]
[Effect(name="$e_fist_hit_01",x=90,y=95,layer = 1)]
[charslot(slot = "m",posfrom = "0,0", posto = "-5,0",duration=0.2,focus="n")]
[CameraShake(duration=0.3, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_punchsp5",channel="a")]
[Delay(time=0.31)]
[charslot(slot = "m",posfrom = "-5,0", posto = "0,0",duration=0.3,focus="n")]
[CameraShake(duration=-1, xstrength=0, ystrength=3, vibrato=40, randomness=90, fadeout=false, block=false)]
第二颗，第三颗。
塞雷娅越走越快。
[charslot(slot = "m", name = "avg_npc_537_1#7$1")]
[name="克丽斯腾"]停下，塞雷娅。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]“停下”？
[name="塞雷娅"]这句话我对你说过了。
[charslot(slot = "m", name = "avg_npc_537_1#7$1")]
[name="克丽斯腾"]我可以告诉你我全部的计划......
[charslot(slot = "m", name = "avg_npc_896_1#9$1")]
[name="塞雷娅"]我知道。
[charslot(slot = "m", name = "avg_npc_537_1#6$1")]
[name="克丽斯腾"]那你为何还要阻止我？这次计划里并不会出现更多的牺牲者。我只不过......
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]只不过......想在特里蒙上空放一朵无害的烟花。
[name="塞雷娅"]在聚焦完成的那一刻，军方和梅兰德就会松一口气。
[name="塞雷娅"]特里蒙的居民会在瞬间被天空的异象吸引，但很快又会被其他更值得关注的事情抓走注意力。
[name="塞雷娅"]莱茵生命......或许是受影响最大的一方。莱茵会失去她的总辖，可能还有几名主任，以及哥伦比亚权力机构的信任。
[charslot(slot = "m", name = "avg_npc_537_1#7$1")]
[name="克丽斯腾"]那你更应该留在地面上。
[name="克丽斯腾"]收拾残局，保护那些可能因这件事受伤的人，带着我们的莱茵渡过难关。你向来做得很好。
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]你又忘了，我早就......辞职了。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]......
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]许多像布莱克一样的人喜欢把科学家叫作“疯子”。
[charslot(slot = "m", name = "avg_npc_537_1#1$1")]
[name="克丽斯腾"]我们不在乎。
[charslot(slot = "m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]可科学本该是理性的。
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]克丽斯腾，当我第一次听你说起你父母的故事，我就产生了一个想法......他们不应该仅仅拥有那样的结局。
[name="塞雷娅"]要是他们没有死在那场事故里，而是在撞上阻隔层之前就返航......
[name="塞雷娅"]那他们带给人们的，将是无比珍贵的数据，以及下一次探索的可能性。
[charslot(slot = "m", name = "avg_npc_537_1#8$1")]
[name="克丽斯腾"]你明明......
[charslot(slot = "m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]......我敬佩他们的意志与决心。
[name="塞雷娅"]可我从来都无法赞同理所当然的牺牲。
[name="塞雷娅"]斐尔迪南，娜斯提，帕尔维斯......他们很多人都以为我过于保守。
[name="塞雷娅"]他们认为我拘泥于规则，始终都在阻挠你们前进。
[name="塞雷娅"]哈......“这样的人也配被称作科学家吗？”
[charslot(slot = "m", name = "avg_npc_896_1#9$1")]
[n

... (全文34936字符)
```

### level_act25side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act25side/CW01.mp4")]
```

### level_act25side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Image(image="29_i10", fadetime=1, xScale=1.4, yScale=1.4, screenadapt="coverall",y=-60)]
[ImageTween(image="29_i10", fadetime=0.5, yTo=-140, duration=12)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", text="<i>“如若此后百年千年，来人漫步于繁星身侧，人们便要赞颂她的名。”</i>", x=320,y=340, alignment="center", size=22, delay=0.001, width=700,block = true,duration=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1",duration=1,block = false)]
[delay(time=3)]
[image]
[PlaySound(key="$d_avg_reedmarshes", volume=0, loop=true, channel="reed")]
[SoundVolume(volume=0.4, fadetime=1,channel="reed")]
她坐在树桩上一边哼着歌，一边观察云朵的形状。等到母亲喊她，她才蹦跳着跑过去。
即将进行的低空飞行对于父母来说已经是轻车熟路，不然也不会带上她。
[SoundVolume(volume=0, fadetime=2,channel="reed")]
[PlaySound(key="$d_avg_clothmovement", volume=0.5)]
[PlaySound(key="$factory_low_drone", channel="slide",loop=true,volume=0)]
[SoundVolume(volume=0.4, fadetime=1.5,channel="slide")]
戴好护目镜，绑上安全带，伴随着引擎的轰鸣声，飞行器开始在跑道上滑行。
[playsound(key="$d_avg_snowstormlp", channel="wind",loop=true,volume=0)]
[SoundVolume(volume=0.7, fadetime=1.5,channel="wind")]
刮过脸庞的风越来越强烈，她有些害怕地闭上双眼。
[SoundVolume(volume=0.2, fadetime=3,channel="slide")]
[playsound(key="$d_avg_plane")]
随后，她感到身体一轻，同时一阵反胃的感觉翻涌到喉头，她的心悬到了嗓子眼，紧紧地缩进母亲的怀里。
[SoundVolume(volume=0.2, fadetime=1.5,channel="wind")]
好在这种感觉并没有持续太久，等到飞行器不再颠簸，她也慢慢地放松下来。
但她依然不敢睁开双眼......
直到母亲轻轻拍了拍她的肩膀。
她终于鼓起勇气睁开眼，看向周围。
一直生活的城市从这个角度看去是如此地陌生而又新奇，平时她总挤不过去的人潮，此时就像虫子一样渺小。
母亲向上指了指，她抬起头。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[gridbg(imagegroup="38_g20_skyblue_L1/38_g20_skyblue_r1/38_g20_skyblue_L2/38_g20_skyblue_r2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720",x=-640,fadetime=1)]
[largebgtween(duration = 25,yFrom = 720, yTo = 360,block = false)]
[stopsound(channel="wind", fadetime=2)]
[stopsound(channel="slide", fadetime=2)]
[delay(time=3.5)]
天空是如此明亮。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[gridbg]
[charslot]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Delay(time=1)]
[Sticker(id="st1", multi = true, text="1099年，哥伦比亚，麦克斯哥伦比亚特区郊外，", x=320,y=340, alignment="left", size=24, delay=0.04, width=640,block = true)]
[Sticker(id="st1", multi = true, text="\n联邦移动监狱",block = true)]
[Sticker(id="st1",duration=0.5,block = false)]
[Delay(time=1.5)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Delay(time=2)]
[Dialog]
[charslot(slot = "left", name = "avg_npc_134",duration = 0.5,isblock=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "right", name = "avg_npc_892_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1.5,isblock=false)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="精英打扮的男性"]先生，您生病了。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]什么？我好得很。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="精英打扮的男性"]不。我看得出。酗酒，暴饮暴食，夜不能寐。在这座压抑的移动监狱里，您又能过上什么好日子呢？
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]......呵。您说的是。
[charslot(slot = "r", name = "avg_npc_892_1#3$1",focus="r")]
[name="精英打扮的男性"]哈哈，无意冒犯。
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="精英打扮的男性"]我想，也许您需要一次疗养。您去过汐斯塔吗？米诺斯呢？
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]别笑话我了，先生。
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="精英打扮的男性"]不。我这是在邀请您。请选一个吧，就当是在这无聊的等待中打发时间。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]......米诺斯。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="精英打扮的男性"]米诺斯啊......街道上特有的果香会顺着清风划过白墙，更重要的是，留在米诺斯丽人们骨子里的典雅一定能让您流连忘返......
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]好的，好的，先生，能想象出您过着怎样奢靡的生活，我真羡慕——
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="精英打扮的男性"]不。我是说，我为您准备好了。“为您准备好了。”
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]......您什么意思？
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="精英打扮的男性"]我相信您的疾病一定需要这样的环境才能治愈。而您，又是为我做了这么多事的好帮手，我当然会善待您这样的人。
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="精英打扮的男性"]只要待上几个月，您的阴霾就会一扫而空，您会像米诺斯的工匠那样健全强壮，还有可能收获一段美妙的艳遇——
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]——贾斯汀·菲茨罗伊先生，我再说一遍，我没病。别拿我寻开心了。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]您可以喊我小贾斯汀。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]唉......好吧，小贾斯汀先生，莱茵生命就连商务科的要员都是精通医术的？
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]不不不，我完全不懂。谁会对那么复杂还没办法立刻变现的东西感兴趣呢？
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]那您还说什么——
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]我想您一定很想知道自己得了什么病，以及，是谁把这种疾病传染给了您。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]看看您的周围，然后回想一下——
[name="小贾斯汀"]您的上司，或是那个尖酸刻薄、一无是处的法官大人，还有那个退休了都不愿给您好脸色看的前任典狱长......
[charslot(slot = "r", name = "avg_npc_892_1#2$1",focus="r")]
[name="小贾斯汀"]您本该在退伍之后成为一名备受瞩目的拓荒英雄，再不济也该是舒舒服服享受着政府津贴，在移动城市的小别墅里品味生活才是。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]可现在呢？
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]你、你调查过我？
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]这叫作对症下药，先生，依我看——
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="小贾斯汀"]——您病入膏肓了啊。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]......
[charslot(sl

... (全文37555字符)
```

### level_act25side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="29_g8_alley_n",screenadapt="coverall")]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_895_1#8$1",duration=1)]
[charslot(slot="r",name="avg_1031_slent2_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_895_1#2$1",focus="l")]
[name="伊芙利特"]赫默！太好了，进城之后我就一直在想，什么时候才能见到你......
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]......
[charslot(slot="l",name="avg_npc_895_1#5$1",focus="l")]
[name="伊芙利特"]呃......赫、赫默？
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]......伊芙利特，过来一些。
[dialog]
[charslot(slot="l",name="avg_npc_895_1#1$1")]
[charslot(slot="l",posfrom = "0,0", posto = "80,0",duration = 1.2)]
[Delay(time=1.5)]
[playsound(key="$d_avg_medicalbeep",volume=0.6)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="l")]
[name="伊芙利特"]放心吧，赫默，我这好好的，能再撂倒一排坏家伙，还能单手抱着你跑几圈！你不信的话，我另一只手抱塞雷娅！哈......哈哈......
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]先别说话，会影响医疗无人机的读数。
[dialog]
[charslot(slot="l",name="avg_npc_895_1#6$1",focus="l")]
[name="伊芙利特"]噢......好吧。
[charslot(slot="l",focus="n")]
垂着头为她检查身体的赫默看上去就和往常一样，细致又温柔，但伊芙利特还是觉得很紧张。
她从不害怕赫默对自己发怒。
她在成长中学到的第一件事就是，赫默对她发怒就意味着，赫默在关心她。
她知道，赫默在生气之后，会帮她摆平那些伤害她的东西，会帮她赶走那些让她害怕的东西。
那不是真的愤怒。
但伊芙利特很害怕沉默的赫默。
当赫默没有表现出愤怒，而是比任何时候都要平静的时候，她会意识到——
一定有什么事触碰到了赫默的底线。
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="l")]
[name="伊芙利特"]原来特里蒙的天总是灰蒙蒙的，乌云大得像怪兽，难怪你以前走进房间的时候，头发经常是湿的......
[name="伊芙利特"]......还有“热狗”，你喜欢吃热狗吗？博士给我和迷迭香一人买了两个，我想下次试试淋点草莓味的糖浆一起吃......
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]......
[charslot(slot="l",name="avg_npc_895_1#6$1",focus="l")]
[name="伊芙利特"]赫默......
[name="伊芙利特"]我是自己想来的。我缠了凯尔希医生好久，一路上还给博士写了好长的保证书。
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="l")]
[name="伊芙利特"]这几年我完成了全部课程与训练，我能做很多任务，就和你还有塞雷娅一样......
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]血液源石结晶密度有小幅度上升。
[charslot]
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......上升速度与体细胞融合趋势预测呢？
[charslot]
[charslot(slot="l",name="avg_npc_895_1#8$1",focus="r")]
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]暂时在可控范围内。
[name="赫默"]其他结果得等伊芙利特回本舰后再做一次全面检查才知道。
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[name="伊芙利特"]你要我回本舰......你们还是不相信......
[charslot(slot="r",name="avg_1031_slent2_1#2$1",focus="r")]
[name="赫默"]不，伊芙利特，我相信你。
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="r")]
[name="赫默"]但是......
[charslot]
[charslot(slot ="m", name = "avg_npc_896_1#5$1")]
[name="塞雷娅"]......
[charslot]
[charslot(slot="l",name="avg_npc_895_1#9$1",focus="l")]
[charslot(slot="r",name="avg_1031_slent2_1#1$1",focus="n")]
[name="伊芙利特"]有塞雷娅在，不会有什么但是！
[charslot(slot="r",name="avg_1031_slent2_1#5$1",focus="r")]
[name="赫默"]......四年多以前，就在这座城市，在同一块招牌下面。
[name="赫默"]我几乎永远失去了你。而在那一刻，她就在你身边，与此时此刻没什么分别。
[charslot(slot="l",name="avg_npc_895_1#3$1",focus="l")]
[name="伊芙利特"]但我活下来了，而且活得好好的！塞雷娅保护了我，这回我可以和她一起保护你，保护所有人！
[charslot]
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]伊芙利特，听赫默的话。赫默是你的医生，是你最该信任的人。
[charslot]
[charslot(slot="l",name="avg_npc_895_1#4$1",focus="l")]
[charslot(slot="r",name="avg_1031_slent2_1#5$1",focus="n")]
[name="伊芙利特"]可我一样信任你！我还信任博士，信任迷迭香，这些信任没有高低。
[charslot]
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......
[charslot(slot="m",name="avg_1031_slent2_1#6$1")]
[name="赫默"]......塞雷娅，那天我看见你了。你和穿着风衣的神秘人一起，出现在十三区的工厂。就在同一天，有东西从天上掉了下来。
[charslot(slot ="m", name = "avg_npc_896_1#3$1")]
[name="塞雷娅"]原来你也在现场。
[charslot(slot="m",name="avg_1031_slent2_1#1$1")]
[name="赫默"]又一个与莱茵有关的秘密实验，对不对？
[charslot(slot ="m", name = "avg_npc_896_1#5$1")]
[name="塞雷娅"]......
[charslot(slot="m",name="avg_1031_slent2_1#2$1")]
[name="赫默"]当然，你不会回答。因为......这是对我和伊芙利特的“保护”。
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......就在十分钟前，伊芙利特阻止的是一场针对副总统的刺杀。
[charslot(slot="m",name="avg_1031_slent2_1#9$1")]
[name="赫默"]......什么？
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]并非我有意隐瞒，赫默，我掌握的情报也很有限。此事背后牵涉势力实在太多，我能做的也只有竭尽所能阻止事态恶化。
[charslot(slot="m",name="avg_1031_slent2_1#6$1")]
[name="赫默"]......
[charslot(slot="m",name="avg_1031_slent2_1#1$1")]
[name="赫默"]“必须让事情回归正轨”——这句话我听塞雷娅主任说过许多次了。
[name="赫默"]在莱茵的时候，你总是在控制事态，但那些可怕的实验还是一茬接着一茬冒出来。
[name="赫默"]永远有人在因为另一些人的野心受伤，而这些伤害并不能因为事后的正义审判而得到弥补，更不必提......本该有的审判从未发生。
[name="赫默"]我忍不住想......等这场火终于被你们扑灭的时候，有多少人会像当年的伊芙利特一样，躺在废墟中奄奄一息？
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......
[charslot(slot="m",name="avg_1031_slent2_1#1$1")]
[name="赫默"]......你只会比我想得更多更清楚。
[name="赫默"]但你还是习惯性地选择帮他们“控制”。你希望损伤尽可能地小，最好小到让人们察觉不到，而并非在源头上扼杀所有的不道德。
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......我无法否认。
[charslot(slot="m",name="avg_1031_slent2_1#1$1")]
[name="赫默"]塞雷娅......这些年我一直想问你一个问题。
[charslot(slot="m",name="avg_1031_slent2_1#5$1")]
[name="赫默"]你做不到真的站在莱茵的对面，是不是因为在骨子里，你始终和他们......和总辖才是同类？
[charslot(slot ="m", name = "avg_npc_896_1#9$1")]
[name="塞雷娅"]......
[charslot(slot ="m", name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]我......
[dialog]
[charslot(slot = "m", focus = "n")]
[stopmusic(fadetime=1)]
[playsound(key="$d_avg_arrowshot")]
[delay(time=1)]
[charslot(slot ="m", name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]有狙击手！
[charslot(slot ="m", name = "avg_npc_896_1#11$1")]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="塞雷娅"]赫默，蹲下！伊芙——
[charslot(slot="m",name="avg_1031_slent2_1#10$1")]
[name="赫默"]什——
[dialog]
[charslot]
[playsound(key="$d_avg_gunshot")]
[delay(time=0.5)]
[Effect(name="$e_spark_02_large",x=100,y=50,layer = 1)]
[PlaySound(key="$d_avg_axeimp", volume=1)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot ="m

... (全文30896字符)
```

### level_act25side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="32_RL2_cliffday",screenadapt="coverall")]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
伊比利亚随处可见的海岸。
不远处的断壁残垣昭示着这里曾经或许是一座繁荣的村庄，而如今，只有墙上残留的风铃孤独地应和着海浪拍打沙滩的声音。
[name="恐鱼"]......（迷茫的窸窣声）
海浪将一只恐鱼冲上了沙滩。
不，许是它顺着海浪来到了陆地。
无论如何，它看起来并没有下一步的目的，它只是徘徊着，张望着，如同它所有的同族那样。
它本应一无所获。这里一片荒芜，站在这里，能看到的仅有漫无边际的海洋以及天空。
但是下一刻，它却如同感应到了什么一般，向着某个方向看去。
亘古不变的天空被一道涟漪扫过。
[dialog]
[playsound(key="$d_avg_fish_howl",volume=0.7)]
[charslot(slot = "m", name = "avg_npc_457_1#1$1",duration=1)]
[Delay(time=0.5)]
[name="恐鱼"]（疑惑的低鸣）
[charslot(slot = "m", focus = "n")]
它望向那个方向，那里只有一望无际的天空。
随后是它的同胞。它的亲代。它的大群。
所有的眼都望向那个方向。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="28_g3_slumstreets_night",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$dooropenquite")]
[charslot(slot = "r", name = "avg_npc_496_1#1$1",duration=1)]
[charslot(slot = "l", name = "avg_npc_493_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", focus = "n")]
侍从一边向老板道歉，一边将自己的主人——一名宫廷音乐家从酒吧中搀扶出来。
[Dialog]
[charslot(slot = "m", focus = "all")]
[charslot(slot = "r",posfrom = "0,0", posto = "-100,0" ,duration=0.8)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]先生，您不能再喝了，先生。
[Dialog]
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[CameraShake(duration=0.3, xstrength=20, ystrength=10, vibrato=15, randomness=90, fadeout=true, block=false)]
[charslot(slot ="left", action="shake", power=20, times=30, duration=0.3)]
[playsound(key="$bodyfalldown2",voluyme=0.7)]
[charslot(slot = "r",posfrom = "-100,0", posto = "0,0" ,duration=0.5)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[name="音乐家"]别......别拦我......
[name="音乐家"]写不出，写不出曲子，我，我还不如就这么醉......醉死！
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]哎呀，我的先生啊，您昨天不是已经写了好几首草稿了吗？至少我觉得，第三首已经非常不错了。
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[name="音乐家"]嘿嘿，还是你，你懂我。
[name="音乐家"]但是，不对，不行，不够！
[name="音乐家"]还、还差一点，一点最关键的东西。
[name="音乐家"]你明白吗？一种迷幻的，壮丽的，疯狂的......意象。
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]我明白，我当然明白，您总是在追求这种东西。
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[name="音乐家"]嗯？嗯......嗯？
[name="音乐家"]哦，我大概是真的醉了。
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]怎么了？
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[name="音乐家"]我看到了......波浪划过天际。
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]波浪？我该带您去看一看医......那是什么？
[charslot(slot = "m", focus = "n")]
侍从抬头看向天空，光晕一样的波纹从天空荡过。
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]这......难道醉意能通过空气传播？
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[name="音乐家"]哈，哈哈！云层如海浪，天空是一块幕布！好，好啊！
[name="音乐家"]特隆，走，走！快！扶我回家！
[name="音乐家"]不，把笔给我！快！
[charslot(slot = "r", name = "avg_npc_496_1#1$1",focus="r")]
[name="侍从"]在这里。您找到灵感了？
[charslot(slot = "l", name = "avg_npc_493_1#1$1",focus="l")]
[name="音乐家"]灵感？不，我看到的是一座泉水！
[charslot(duration=0.5)]
昏暗的路灯下，音乐家丝毫不顾形象，趴在地上奋笔疾书。
这一夜，无数艺术家彻夜未眠。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_176",duration=1)]
[delay(time=1.5)]
[name="维多利亚伯爵"]瞧瞧这些乐观的人们。
[name="维多利亚伯爵"]他们以为风波已经过去，维多利亚只是经历了一场小小的动荡。
[name="维多利亚伯爵"]他们拥有的东西依然存在，并且将会继续存在下去。
[name="维多利亚伯爵"]我多么希望我也能有这样健康的心态。
[charslot]
[Dialog]
[charslot(slot = "l", name = "avg_npc_176")]
[charslot(slot = "r", name = "avg_npc_248",duration=0.5,posfrom = "100,0", posto = "0,0")]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_176",focus="n")]
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]阁下，有一样东西需要您过目。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]你不是会在这种时候扫我兴的人，发生了什么？
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]哥伦比亚似乎出了一些状况。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]似乎？
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]是的，我们正在紧急收集情报。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]我们叛逆的孩子又用他引以为傲的科学技术做了一些难以理解的事？
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]不，这一点尚未确定，眼下，我唯一能够确定的是，您有必要知道这件事。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]究竟是多重要的事情需要让我迈开脚步，而不是由你端到我的面前？
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]这......实在超出了我的能力。
[charslot(slot = "m", focus = "n")]
伯爵发现，自己最为信任的手下，脸上竟带了一丝苦笑，这让本只是调侃的他感到了一丝惊讶。
他的参谋只会讲述事实，这意味着，确实有什么发生了。
[playsound(key="$d_gen_walk_n")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=0.5)]
伯爵走到窗边，立刻意识到参谋所言非虚。
那是绝对无法端到他面前的情报，却也是谁都无法忽视的现实。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]这是什么自然现象？
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]我们紧急招来了相关方面的专家，结合日前从哥伦比亚传来的情报，他们给出了一些有价值的猜想。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]......《359号基地间谍报告》《梅兰德基金会调查报告》。
[name="维多利亚伯爵"]这又是什么？学术论文？阻隔层......
[name="维多利亚伯爵"]告诉我重点。
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]这层涟漪从哥伦比亚方向扩散而来，它非常不自然。
[name="参谋"]而经过一些简单的观测，我们认为这与一个早已被科学界遗忘的猜想十分相符——
[name="参谋"]我们头顶上的天空是虚假的。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]......
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]有什么事情发生了。
[charslot(slot = "l", name = "avg_npc_176",focus="l")]
[name="维多利亚伯爵"]而我们一无所知。
[charslot(slot = "r", name = "avg_npc_248",focus="r")]
[name="参谋"]我们已经动员了所有在哥伦比亚方面的间谍，他们很快就会得到结果。

... (全文60830字符)
```

### level_act25side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cellroomB",screenadapt="coverall")]
[playMusic(intro="$Tremont_intro",key="$Tremont_loop", volume=0)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[charslot(slot = "r", name = "avg_npc_890_1#1$1", duration=1, isblock=true)]
[name="斐尔迪南"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_899_1#1$1", duration=1.5, isblock=true)]
[charslot(slot = "l", focus="l")]
[name="布莱克"]......
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]我听说过特区监狱的章程，这里不允许使用尖锐物品，包括笔。你在违反规定。
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]也不允许戴墨镜，布莱克。
[name="斐尔迪南"]在我们被关在一起的第一天，我告诉过你，别打扰我，我有很重要的工作要做，你在前些日子里一直做得很好。
[name="斐尔迪南"]我很希望你能继续保持。
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]......
[charslot(slot = "r", name = "avg_npc_890_1#6$1", focus="r")]
[name="斐尔迪南"]该死，稿纸又用完了......背面这些还能写。
[charslot(slot = "r", name = "avg_npc_890_1#5$1", focus="r")]
[name="斐尔迪南"]布莱克，帮我个忙，找典狱长再要些稿纸，哥伦比亚的学界会感谢你的贡献。
[charslot(slot = "l", name = "avg_npc_899_1#6$1", focus="l")]
[name="布莱克"]你究竟在干什么？
[name="布莱克"]你不会觉得我们能活下来吧，斐尔迪南。
[name="布莱克"]哥伦比亚的法律从不心慈手软，你就不能安静地等着我们的终点来临吗？
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]如果你真的想忙活，想想自己的临终菜单不好吗？
[charslot(slot = "r", name = "avg_npc_890_1#1$1", focus="r")]
[name="斐尔迪南"]你浪费了我两分钟时间，布莱克。
[charslot(slot = "r", name = "avg_npc_890_1#7$1", focus="r")]
[name="斐尔迪南"]......我刚刚推论到哪一步了？
[charslot(slot = "l", name = "avg_npc_899_1#1$1", focus="l")]
[name="布莱克"]临终菜单。
[charslot(slot = "r", name = "avg_npc_890_1#7$1", focus="r")]
[name="斐尔迪南"]你觉得你很幽默，嗯？你根本不明白我现在的工作多么有意义。
[charslot(slot = "r", name = "avg_npc_890_1#4$1", focus="r")]
[name="斐尔迪南"]在往后的一百年里，每一个妄图涉足高能物理领域的研究者，都必须要铭记我的这些理论。
[name="斐尔迪南"]他们会赞颂我的名字，视我如国王，视我如先知。
[name="斐尔迪南"]死，死又算什么？
[charslot(slot = "r", name = "avg_npc_890_1#6$1", focus="r")]
[name="斐尔迪南"]等着吧，等着吧，克丽斯腾，你以为你很了不起？
[charslot(slot = "r", name = "avg_npc_890_1#4$1", focus="r")]
[name="斐尔迪南"]是斐尔迪南·克鲁尼把这些真理带回了大地，蠢货！
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_134")]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "left", name = "avg_npc_134")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "right", name = "avg_npc_892_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1.5,isblock=false)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="小贾斯汀"]先生，我很高兴看到您现在这么健康。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]当然，当然，这都多亏了您。
[name="监狱负责人"]前些日子，听说特里蒙有一些不好的传言......不过，现在这些都过去了。
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="小贾斯汀"]感谢我们的哥伦比亚拥有很多像您这样杰出的执法者。
[name="小贾斯汀"]听说您要高升了。州检察官这个职位，对于您可称得上是相得益彰。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]与您的生意相比，实在是算不得什么。
[name="监狱负责人"]莱茵生命扩大了在技术方面的投资，购入了十数家各个领域的小型实验室......哈哈哈，放在以前，我是一点都不关心这些金融新闻的。
[name="监狱负责人"]不过，有了小贾斯汀先生您这样的朋友，我也不能再像以前那样，只是每天盯着这些铸铁栏杆发呆了。
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="小贾斯汀"]我会向您推荐好的投资项目的。
[name="小贾斯汀"]我很高兴看到，您愿意把握住自己的命运。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]不过，我这次来还是有些正事的。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]那两个人？上面已经通知过我了。
[name="监狱负责人"]请便吧，小贾斯汀先生。
[name="监狱负责人"]一如既往，合作愉快。
[charslot(slot = "r", name = "avg_npc_892_1#1$1",focus="r")]
[name="小贾斯汀"]合作愉快。
[charslot(slot = "l", name = "avg_npc_134",focus="l")]
[name="监狱负责人"]多问一句，您要带走的，究竟是哪一个？
[charslot(slot = "r", name = "avg_npc_892_1#9$1",focus="r")]
[name="小贾斯汀"]和以往一样，疯子和怪胎。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g12_trimountrestarea",screenadapt="coverall")]
[PlaySound(key="$d_avg_crwddiscuss_inside", volume=1, loop=true, channel="a")]
[charslot(slot = "l", name = "avg_249_mlyss_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[SoundVolume(volume=0.2, channel="a",fadetime=2)]
[charslot(slot = "r", name = "avg_npc_891_1#1$1", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_249_mlyss_1#1$1",focus="l")]
[name="缪尔赛思"]你也来了啊，娜斯提。
[charslot(slot = "r", name = "avg_npc_891_1#1$1",focus="r")]
[name="娜斯提"]以已经解散的总辖构件科的名义发出临时会议通知......才过去半个月的时间，就有人要重整莱茵生命？
[charslot(slot = "l", name = "avg_249_mlyss_1#1$1",focus="l")]
[name="缪尔赛思"]不止是莱茵生命哦，沃尔沃特科钦斯基、沙滩伞......这座城市最顶尖的科技公司都收到了参会通知，而且派出了代表。
[dialog]
[charslot(slot = "l", posfrom="0,0", posto="50,0", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_249_mlyss_1#9$1",focus="l")]
[name="缪尔赛思"]你猜到底是谁组织的这场会议？
[charslot(slot = "r", name = "avg_npc_891_1#1$1",focus="r")]
[name="娜斯提"]待会儿自然就知道了......别把头靠过来，我不想肩膀被弄湿。
[dialog]
[charslot]
娜斯提微微皱了下眉头，她腰间枯枝状的装置突然伸长了一节，触碰到缪尔赛思的瞬间，对方消失在了视野里，像是戳破了一个气泡。
[dialog]
[charslot(slot = "l", posfrom="0,0", posto="50,0", duration=0, isblock=true)]
[charslot(slot = "r", name = "avg_npc_891_1#1$1")]
[charslot(slot = "l", name = "avg_249_mlyss_1#9$1", afrom=1, ato=0, duration=1)]
[PlaySound(key="$d_avg_watersubbreak", volume=1)]
[Effect(name="$e_muesys_hide", x=-150, layer = 1)]
[delay(time=4)]
[charslot(slot = "r", name = "avg_npc_891_1#2$1",focus="r")]
[name="娜斯提"]又有了力气耍弄这套小把戏，看来你恢复得很快，缪尔赛思。
[dialog]
[charslot(slot = "l", posfrom="50,0", posto="0,0", duration=0, isblock=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charsl

... (全文24796字符)
```

### ref_01_act25side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 

[Image(image="38_ex05",screenadapt="coverall", fadetime=0)]

[Image(image="38_ex06",screenadapt="coverall", fadetime=0)]

[Image(image="38_ex03",screenadapt="coverall", fadetime=0)]
```

### ref_02_act25side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 

[Image(image="38_ex01",screenadapt="coverall", fadetime=0)]

[Image(image="38_ex02",screenadapt="coverall", fadetime=0)]

[Image(image="38_ex04",screenadapt="coverall", fadetime=0)]
```

### training_act25side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动25side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 成功进入实验室了，等等，我们监听到了敌人的通话。

[PopupDialog(dialogHead="$avatar_cbshld")] 怎么回事，为什么这里的地势忽然发生了变化？

[PopupDialog(dialogHead="$avatar_cbshld")] 刚才还是平地，现在却不自然地倾斜了起来......

[PopupDialog(dialogHead="$avatar_cbshld")] 敌人就在眼前，没办法，前进！
```

### training_act25side_01_b

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动25side教学关_b

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(dialogHead="$avatar_jesica")] 敌人好像......移动得很吃力？

[Tutorial(dialogHead="$avatar_doberm")] 没错，实验室有特殊的御敌机制，可以让整块架空地板倾斜。我们现在就像在一块巨大的跷跷板上。

[Tutorial(focusX=-330, focusY=220, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]现在地板是<@tu.kw>向下</>倾斜的，也就是说，有一个<@tu.kw>向下的重力分力</>在影响着我们。

[Tutorial(focusX=-30, focusY=-45, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5,dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 所以现在敌人<@tu.kw>向上</>移动，相当于在对抗重力，<@tu.kw>移动速度会减缓</>，并且<@tu.kw>越重</>的敌人越为显著。

[InputBlocker(blockInput=true, black=0)]

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(dialogHead="$avatar_doberm")] 而对我们来说，<@tu.kw>向下</>部署，也就是顺着重力方向部署的干员<@tu.kw>攻击速度会增加</>。

[Tutorial(dialogHead="$avatar_doberm")] 趁现在占领有利的高处，痛击敌人！

[Tutorial(dialogHead="$avatar_cammou")] 我赶到啦！

```

### training_act25side_01_c

```
[HEADER(is_tutorial=true, is_skippable=true, is_autoable=false)] 活动25side教学关_c

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]

[Battle.Pause]

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(dialogHead="$avatar_jesica", black="$f_tut_black")] 发生了什么，地板在转动！敌人现在移动得好快！

[Tutorial(dialogHead="$avatar_doberm", black="$f_tut_black")] 分析结果出来了。

[InputBlocker(blockInput=true, black=0)]

[Tutorial(focusX=0, focusY=130, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_doberm",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]<@tu.kw>重量等级3及以上</>的敌人踩到了<@tu.kw>上方</>的<@tu.kw>重力感应机关</>，让地板旋转，使倾斜方向向上了。

[Tutorial(dialogHead="$avatar_doberm", black="$f_tut_black")] 上坡时敌人对抗重力会减速，而下坡敌人利用重力会加速。对我方的影响也会相反。

[Tutorial(focusX=200, focusY=-40, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_doberm",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]对应地，<@tu.kw>阻挡数1及以上</>的我方干员，也可以踩机关，现在我们只要......

[InputBlocker(blockInput=true, black=0.2)]

[Tutorial(dialogHead="$avatar_jesica", black="$f_tut_black")] 我理解了，像跷跷板一样！踩哪边哪边就会下沉。

[Tutorial(dialogHead="$avatar_doberm", black="$f_tut_black")]没错，在更多敌人袭来之前，踩住下方机关，延缓敌人进攻！

[InputBlocker(blockInput=false, black=0)]

[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_nblade", animStyle="Drag", \
          startX=-60, startY=60, startAnchor="BottomRight",endAnchor="BottomRight", endX=-414, endY=350)] 交给我吧。

[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
```


> 本章节共37个脚本文件，此处展示前30个。

## 统计

- 总字符数：690992
- 对话行数：5627


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
