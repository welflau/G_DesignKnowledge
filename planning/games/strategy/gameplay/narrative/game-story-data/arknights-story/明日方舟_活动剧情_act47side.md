# 明日方舟 · 活动剧情 · act47side（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act47side」完整剧情脚本（23个文件，3155行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act47side
- 脚本文件数：23

### level_act47side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g5_rhinelab_indoor",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_magic_3", volume=1)]
[name="娜斯提"]（萨卡兹语）凝结。
[playMusic(intro="$chasing_intro",key="$chasing_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=1, amount=0, block=true)]
[PlaySound(key="$d_avg_labamb",channel="lab",loop=true, volume=0.4)]
[charslot(slot = "m", name = "avg_npc_896_1#1$1", isblock=true)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", action="zoom", poszoom = "0.5,0.5", scale=1.1, duration = 0.3)]
[charslot(slot = "m", afrom = 1, ato = 0, duration = 0.4,isblock=true)]
[delay(time=0.3)]
[charslot]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$d_avg_punch",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.15, block=true)]
[delay(time=0.3)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.1, block=true)]
[PlaySound(key="$d_avg_punchairwall",volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.15, block=true)]
[delay(time=0.2)]
[Blocker(a=0.8, r=1, g=1, b=1, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_punchairwall",volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.4, block=true)]
[delay(time=0.5)]
密集的拳击声。
咒言在空气中捏塑出无形的墙，精准挡下瓦伊凡的每一拳，汗水打湿了旧拳套上“特里蒙理工”的字样。
[stopmusic(fadetime=2)]
[delay(time=0.5)]
良久，瓦伊凡停了下来。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=1.2)]
[charslot(slot = "l",posfrom="-50,0",posto="-50,0",name = "avg_npc_896_1#1$1", duration=1.5)]
[charslot(slot = "r",posfrom="50,0",posto="50,0",name = "avg_4212_nasti_1#4$1", duration=1.5,isblock=true)]
[delay(time=0.5)]
[charslot(slot="l",focus="l",name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]呼——就到这里吧，谢谢你当我的陪练，娜斯提。
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[stopsound(channel="lab",fadetime=2)]
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]这才到你平日运动量的一半。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]是你该出发了。和其他人道过别了？
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]我没通知他们。马里亚姆就不用说了，缪尔赛思人在谢拉格，人事科和结构科的两位新主任我还不太熟。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#8$1")]
[name="娜斯提"]至于小贾斯汀和斐尔迪南，还是让他俩单独见面吧......
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]这样不管是对自己刚从哪位高官的宴会上离开夸夸其谈，还是宣讲那些能让一个人成为科学界国王的新理论，两个人都有听众。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]再说，我只是出一趟差而已。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#6$1")]
[name="塞雷娅"]需要工程科主任出的差可不多。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#5$1")]
[name="塞雷娅"]特区政府批准了我们的申请，整合“地平弧光计划”的资源，以万星园的技术遗留为基础，继续推进浮空科技领域的革新。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]但他们同时对哥伦比亚全境的科技公司大开方便之门，甚至为此特批了一整个地块。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]进驻人员名单中不仅有烟酒施术单元以及源石制品管理局的官员，连梅兰德也下场了。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]我们的计划书，变成了万千计划书中的一份。让莱茵为整个地块提供基础工程支持，已经是他们对莱茵生命这个发起方最大的尊重了。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#9$1")]
[name="塞雷娅"]政府官员、科技公司代表......毫无疑问，那个地块会很热闹。娜斯提，你并不擅长处理这类事情。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#1$1")]
[name="娜斯提"]这段时间，我也没有听你抱怨过什么......总辖。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#1$1")]
[name="塞雷娅"]......
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#8$1")]
[name="娜斯提"]星荚已经慢慢恢复如初，但人们望向天空的目光不会收回来。常识被颠覆之后，原本被忽视的地方便自然而然成了热土。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#10$1")]
[name="塞雷娅"]自然而然？特殊贷款政策出台后，三分之一的企业增加了天空事业部门，中小型企业也纷纷转型，为了搭上“天空热”的便车不计代价。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#1$1")]
[name="娜斯提"]你意有所指，但我对政治游戏不感兴趣。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#2$1")]
[name="娜斯提"]哪怕一切的发展不是我们所能控制的，莱茵生命也必须做这个发起方。尽可能地掌握主动权，才能尽可能地守住克丽斯腾留下的东西。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#2$1")]
[name="娜斯提"]这并不难理解。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#6$1")]
[name="塞雷娅"]嗯。那么，辛苦了。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#11$1")]
[name="娜斯提"]顺便问一句，你为什么不搬去克丽斯腾的办公室，而是在这间旧办公室外面加挂了一块“总辖构件科”的标牌？
[charslot(slot="l",focus="l",name = "avg_npc_896_1#6$1")]
[name="塞雷娅"]我习惯了这里。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#6$1")]
[name="塞雷娅"]缪尔赛思也这样问过。她红着眼睛，掐着我的胳膊问我是不是因为怀念克丽斯腾，以及莱茵是不是总会为克丽斯腾留一个位置。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]看来，你只是觉得老地方比较舒适。毕竟这里的每一个细节都是你亲自确认过的。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]当初替你装修办公室的时候，你在我身后从头盯到尾，我一度怀疑你的强迫症比帕尔维斯还要严重。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#7$1")]
[name="塞雷娅"]......
[charslot(slot="l",focus="l",name = "avg_npc_896_1#6$1")]
[name="塞雷娅"]相比以前，莱茵生命并不会有什么变化，娜斯提。
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]唔，还是有的，起码现在员工们来找总辖，不至于总是扑空了。
[charslot(slot="l",focus="l",name = "avg_npc_896_1#5$1")]
[name="塞雷娅"]......或许，你没有立场说这句话？
[charslot(slot = "r",focus="r",name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]所以，这也是你选我出这趟差的原因？
[dialog]
[charslot]
[charslot(slot = "r",focus="all")]
[stopmusic(fadetime=2)]
[CameraEffect(effect="Grayscale", fadetime=3, keep=true, initamount=0, amount=1, block=true)]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=1, amount=0)]
[charslot]
[Background(image="68_g1_groundparkstreet_d

... (全文21122字符)
```

### level_act47side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[PlaySound(key="$d_avg_snowstormflp",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.4, channel="f",fadetime=2)]
[Background(image="29_g8_alley_n",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=1, amount=0, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral")]
[charslot(slot="l",name="avg_npc_1043_1#1$1",afrom=0,ato=0, action="zoom",poszoom="0.5,0.5",scale=0.9,duration=0,isblock=true)]
[charslot(slot="l",afrom=0,ato=1,posfrom="-200,0",posto="0,0",duration=1.2, isblock=true)]
[PlaySound(key="$d_avg_runstop")]
[delay(time=0.5)]
[charslot(slot="l",posfrom="0,0",posto="20,0",duration=0.8,isblock=true)]
[charslot(slot="l",focus="l")]
[name="惊慌的女孩"]哥......安德鲁！你又被他们打了吗？
[dialog]
[charslot(slot="r",focus="r",name="avg_npc_2039_1#8$2",duration=0.8, isblock=true)]
[name="斯凯"]叫我斯凯。
[charslot(slot="l",focus="l")]
[name="惊慌的女孩"]可那是你自己取的名字，爸妈说......
[charslot(slot="r",focus="r",name="avg_npc_2039_1#11$2")]
[name="斯凯"]别提他们！自己没出息就只会在咱俩身上撒气的畜生，他们有什么资格决定我叫什么？
[charslot(slot="r",focus="r",name="avg_npc_2039_1#11$2")]
[name="斯凯"]我在特里蒙理工擦了六年的地板，偷听完了所有本科课程，就是为了以后不像他们一样窝囊、愚蠢、没用！
[charslot(slot="l",focus="l")]
[name="惊慌的女孩"]可是......
[charslot(slot="r",focus="r",name="avg_npc_2039_1#3$2")]
[name="斯凯"]还有你！除了每天往我包里贴唠唠叨叨的便签，还能做点别的吗？我又不是不知道吃饭——
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=0.8)]
[charslot(slot = "r", name = "avg_npc_1044_1#1$1", duration=1)]
[delay(time=0.8)]
[charslot(slot = "l", name = "avg_npc_1044_1#1$1", duration=1,isblock=true)]
[delay(time=1.2)]
[charslot]
[charslot(slot="r",name="avg_npc_2039_1#3$2",focus="l",isblock=true)]
[charslot(slot="l",name="avg_npc_1043_1#1$1",afrom=0,ato=0, action="zoom",poszoom="0.5,0.5",scale=0.9,duration=0,isblock=true)]
[charslot(slot="l",afrom=0,ato=1,focus="l",isblock=true)]
[name="惊慌的女孩"]那群人又来了......
[dialog]
[charslot(slot="r",posfrom="0,0",posto="-130,0",duration=0.5)]
[charslot(slot="l",posfrom="0,0",posto="130,0",duration=0.5)]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="r",focus="r",name="avg_npc_2039_1#6$2",isblock=true)]
[name="斯凯"]他妈的......没完了是吗？赶紧的，躲我身后。
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_1044_1#1$1", focus="l",isblock=true)]
[charslot(slot = "r", name = "avg_npc_1044_1#1$1", focus="l",isblock=true)]
[name="街头混混A"]穿一身白大褂，真以为自己是什么人物了？你和那个小姑娘就是穿上总统的衣服，也是贫民窟来的贱种。
[dialog]
[charslot]
[PlaySound(key="$d_avg_punch", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.3)]
[PlaySound(key="$d_avg_punch02", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[charslot(slot = "m",name="avg_npc_2039_1#10$2",posfrom = "0,-60", posto = "0,0",duration = 2,isblock=false)]
[charslot(slot ="m", action="shake", power=7, times=30, duration=0.5, isblock=false)]
[delay(time=1.5)]
[name="斯凯"]哈......阴沟里的鼷兽，一辈子都理解不了什么叫伟大。
[charslot(slot="m",focus="m",name="avg_npc_1044_1#1$1")]
[name="街头混混B"]你再说一句试试？！
[dialog]
[charslot]
[PlaySound(key="$d_avg_punchsp2", volume=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1043_1#1$1",afrom=0,ato=0, action="zoom",poszoom="0.5,0.5",scale=0.9,duration=0,isblock=true)]
[charslot(slot="m",afrom=1,ato=1)]
[name="惊慌的女孩"]哥！
[stopsound(channel="f",fadetime=1)]
[dialog]
[charslot]
[delay(time=0.5)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2, block=false)]
[PlaySound(key="$d_avg_energybeamfire", volume=0.6)]
[delay(time=1.5)]
[Image(image="38_i16", screenadapt="coverall", xScale=2.5, yScale=2.5, fadetime=0.1)]
[delay(time=1)]
[CameraShake(duration=6, xstrength=10, ystrength=10, vibrato=50, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse", volume=1)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.7)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=3)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[playMusic(intro="$act25side_intro",key="$act25side_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[name="街头混混A"]什、什么东西？
[name="街头混混B"]天灾？快跑！
[name="斯凯"]还“天灾”？那他妈叫探索！叫进步！
浑身青紫的青年望向天空，忘记了自己在一个肮脏的小巷里，忘记了身后还有一个惊慌的女孩。
他不受控制地向那束伟大的天光追去。
[dialog]
[ImageTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.2, yScaleTo=1.2, duration=7, block=false)]
[PlaySound(key="$rungeneral")]
[CameraShake(duration=6, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="29_g7_mainstreet_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_892_1#1$1", bstart=0.2,bend=0.7,duration = 0.8)]
[charslot(slot = "r", name = "avg_npc_891_1#1$1", bstart=0.2,bend=0.7,duration = 0.8,isblock=true)]
[charslot(slot="l",focus="l")]
[name="？？？？"]你就不担心总辖？
[charslot(slot="r",focus="r")]
[name="？？？"]她什么时候需要我们担心。
[name="？？？"]我们是同行者，我们只是同行者。
[name="？？？"]我们只需要做好自己的事，然后......祝她好运。
[name="？？？"]（萨卡兹语）若有一天，卡兹戴尔亦悬于天顶，我将在火炉上镌刻你的名字。
[dialog]
[charslot]
[PlaySound(key="$rungeneral")]
[CameraShake(duration=1.2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.2)]
[charslot(slot="m",name="avg_npc_2039_1#5$2",duration=1,isblock=true)]
[name="斯凯"]呼......呼......
[charslot(slot="m",name="avg_npc_2039_1#5$2")]
[name="斯凯"]不、不好意思，女士......
[charslot(slot="m

... (全文17704字符)
```

### level_act47side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="68_g7_airrestaurant",screenadapt="coverall")]
[playMusic(intro="$farce_intro",key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1000_1#3$1",posfrom="100,0",posto="100,0",duration=1.5)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",posfrom="-80,0",posto="-80,0",duration=1.5,isblock=true)]
[delay(time=0.5)]
[charslot(slot="l", name = "avg_4214_cairn_1#8$1",posfrom="-80,0",posto="-30,0",duration=0.8,afrom=1,ato=1,focus="l",isblock=true)]
[name="奥克里？"]哥们儿，要是你真喜欢这个名字，拿去用也就算了，没必要剽窃我的人生经历啊！
[dialog]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1",posfrom="100,0",posto="50,0",afrom=1,ato=1,duration=0.8,focus="r",isblock=true)]
[name="奥克里！"]你怎么好意思倒打一耙，所有资料和简历都是我亲自写的！
[dialog]
[charslot(slot="l", name = "avg_4214_cairn_1#6$1",posfrom="-30,0",posto="20,0",afrom=1,ato=1,duration=0.8,focus="l",isblock=true)]
[name="奥克里？"]你能原样复述吗？
[charslot(slot = "r",name = "avg_npc_1000_1#2$1",focus="r",isblock=true)]
[name="奥克里！"]这......这都是我一年前写的东西了，怎么可能一字不差！
[charslot(slot="l", name = "avg_4214_cairn_1#4$1",focus="l")]
[name="奥克里？"]“奥克里，堡垒山人，毕业于特里蒙文理学院，曾在特区会展中心工作，担任人类发展与技术跌新部门的讲解专员......”
[charslot(slot="l", name = "avg_4214_cairn_1#3$1",focus="l",isblock=true)]
[name="奥克里？"]“迭新”还写错了。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1",focus="r",isblock=true)]
[name="奥克里！"]你！可恶，要不是我弄丢了终端和资料简历——
[dialog]
[charslot]
[charslot(slot="m", name = "avg_npc_2034_1#4$1")]
[name="高登"]......
[dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="高登的头从来没有这么疼过。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="再次确认资料后，他一眼就看出了报到流程上的漏洞，但最大的问题不在于此——", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她究竟为什么要假冒讲解员？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="她是莱塔尼亚派来刺探科技实力的间谍，受国防部直接命令的情报探子，还是特区政府安插在自己身边的眼睛？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="预展上，这个冒牌货已经跟大部分企业有过接触，现在处理她就等同于把自己的疏忽昭告天下。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="更要命的是，高登完全不知道她究竟探听到了多少消息，是否会对自己不利、对哥伦比亚不利......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
高登不敢想下去了。
[charslot(slot="m", name = "avg_npc_2034_1#9$1")]
[name="高登"]......
[charslot]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1",posfrom="50,0",posto="50,0")]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",posfrom="20,0",posto="20,0",isblock=true)]
[charslot(slot="l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="奥克里？"]......你说话的时候眼神游移，语无伦次，声音发颤。
[charslot(slot="l", name = "avg_4214_cairn_1#1$1",focus="l")]
[name="奥克里？"]我想以长官的眼光也不会选择这样一位“奥克里”担任宣传工作吧？
[charslot(slot = "r", name = "avg_npc_1000_1#2$1",focus="r")]
[name="奥克里！"]你少把长官扯进来！我告诉你——
[charslot]
[charslot(slot="m", name = "avg_npc_2034_1#7$1")]
[name="高登"]都别吵了！
[charslot(slot = "m", name = "avg_npc_1000_1#2$1",focus="l")]
[charslot(slot = "l", name = "avg_4214_cairn_1#5$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="奥克里？"]......
[charslot(slot = "m", name = "avg_npc_1000_1#3$1",focus="m")]
[name="奥克里！"]......
[dialog]
[PlaySound(key="$d_avg_highheeledshoe_carpet_fts", volume=1)]
[charslot(slot="r",name="avg_npc_2037_1#1$1",posfrom="280,0",posto="140,0",duration=1.2,isblock=true)]
[charslot(slot="r",focus="r")]
[name="梅希亚"]奥克里“先生”，您需要冷静一下，跟我来吧，我带您去贵宾室休息。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r",posfrom="140,0",posto="80,0",duration=1.2,isblock=true)]
[charslot(slot="r",posfrom="80,0",posto="250,0",afrom=1,ato=0,duration=1.1)]
[charslot(slot="m",posfrom="0,0",posto="150,0",afrom=1,ato=0,duration=1.1,isblock=true)]
[delay(time=1.2)]
[PlaySound(key="$doorclosequite", volume=1)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_4214_cairn_1#4$1")]
[delay(time=0.8)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_4214_cairn_1#4$1",posfrom="-150,0",posto="-180,0",afrom=1,ato=0,duration=1,isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot]
[charslot(slot="l", name = "avg_npc_2034_1#9$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r", name = "avg_4214_cairn_1#4$1",posfrom="200,0",posto="50,0",duration=2,isblock=true)]
[delay(time=1)]
[charslot(slot="r", name = "avg_4214_cairn_1#4$1",focus="r",isblock=true)]
[name="奥克里？"]高登长官，我......
[charslot(slot="l",name = "avg_npc_2034_1#7$1",focus="l")]
[name="高登"]你给我听好了，我刚刚调取了你在园区里的行为记录，弄清你的真实身份也易如反掌。
[charslot(slot="l",name = "avg_npc_2034_1#7$1",focus="l")]
[name="高登"]你要是再撒一次谎，我会立刻把你从六百多米的高空扔下去。不管你是什么人，最后都会变成地上的一摊烂泥，明白吗？
[charslot(slot="l",name = "avg_npc_2034_1#7$1",focus="l")]
[name="高登"]说，你是谁。
[charslot(slot="r", name = "avg_4214_cairn_1#7$1",focus="r")]
[name="奥克里？"]......讲解员......
[charslot(slot="l",name = "avg_npc_2034_1#7$1",focus="l")]
[name="高登"]有骨气。
[charslot(slot="r", name = "avg_4214_cairn_1#9$1",focus="r")]
[name="奥克里？"]旅、旅行时需要的那种讲解员！
[charslot(slot="r", name = "avg_4214_cairn_1#9$1",focus="r")]
[name="费尔南"]我叫费尔南，是个......导游。
[dialog]
[delay(time=0.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.5)]
[charslot]
[Background(image="bg_hotel",screenadapt="coverall")]
[charslot(slot = "l", name = "avg_npc_1000_1#3$1")]
[charslot(slot = "r", nam

... (全文18222字符)
```

### level_act47side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g12_trimountrestarea",screenadapt="coverall")]
[playMusic(intro="$farce_intro",key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4214_cairn_1#1$1",posfrom="300,0",posto="0,0",duration=1, isblock=true)]
[Delay(time=0.2)]
[charslot(slot = "m", name = "avg_4214_cairn_1#2$1")]
[name="费尔南"]哎呀，这就是莱茵生命最年轻的主任，克丽斯腾女士曾经的左膀右臂，生态园和园区工程部的双料负责人——娜斯提主任吗？
[charslot]
[charslot(slot = "r", name = "avg_4212_nasti_1#1$1")]
[charslot(slot = "l", name = "avg_npc_2037_1#1$1",isblock=true)]
[charslot(slot="r", name = "avg_4212_nasti_1#1$1",focus="r",isblock=true)]
[name="娜斯提"]......梅希亚，这就是你说的“后续事宜”？
[charslot(slot = "l", name = "avg_npc_2037_1#6$1",focus="l")]
[name="梅希亚"]呃，是的。讲解员可以帮工程部提高沟通效率，也能加大对莱茵生态园的宣传力度，避免莱茵再次受到预展时的冷遇。
[charslot(slot="r", name = "avg_4212_nasti_1#11$1",focus="r")]
[name="娜斯提"]......
[charslot]
[charslot(slot = "m", name = "avg_4214_cairn_1#3$1")]
[name="费尔南"]娜斯提主任，我听说园区上空飘浮的种植单元并未装配螺旋桨，而是利用咒言产生升力？
[charslot(slot="m", name = "avg_4212_nasti_1#4$1")]
[name="娜斯提"]不完全是，不以声音为媒介的咒言需要与机械结合才能维持动力。
[charslot(slot = "m", name = "avg_4214_cairn_1#4$1")]
[name="费尔南"]既然如此，骨笔对于您来说一定十分重要。如果遗失会造成严重的后果吗，比如丧失记忆或者生病？
[charslot(slot="m", name = "avg_4212_nasti_1#1$1")]
[name="娜斯提"]骨笔于我只是工具，不会对......生理造成影响。
[charslot(slot = "m", name = "avg_4214_cairn_1#3$1")]
[name="费尔南"]那平时您在工作之余是怎么缓解压力、恢复精神的呢？
[charslot(slot="m", name = "avg_4212_nasti_1#5$1")]
[name="娜斯提"]......
[dialog]
[charslot(slot = "r", name = "avg_4214_cairn_1#1$1",posfrom="250,0",posto="120,0",duration=1, isblock=true)]
[charslot(slot="r",focus="r",isblock=true)]
[name="费尔南"]全套的羽角护理会让您放松一点吗？您推荐哪个品牌的护理套装？啊，我可以摸一下您的角，来判断产品效果——
[dialog]
[charslot(slot="m", name = "avg_4212_nasti_1#2$1",afrom=1,ato=1,posfrom="0,0",posto="-30,0",duration=0.8, isblock=true)]
[charslot(slot="m", name = "avg_4212_nasti_1#2$1",focus="m")]
[name="娜斯提"]讲解员小姐，你的问题已经与我们的工作无关了。我会让研究员带你参观生态园，他们可以解答你的疑惑。
[charslot(slot = "r", name = "avg_4214_cairn_1#5$1",focus="r")]
[name="费尔南"]可是——
[charslot(slot="m", name = "avg_4212_nasti_1#2$1",focus="m")]
[name="娜斯提"]有些事情，我想要向梅希亚小姐单独确认。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="38_g10_ecolab",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_4212_nasti_1#1$1")]
[charslot(slot = "l", name = "avg_npc_2037_1#1$1",isblock=true)]
[charslot(slot="r", name = "avg_4212_nasti_1#1$1",focus="r")]
[name="娜斯提"]高登又想做什么？
[charslot(slot = "l", name = "avg_npc_2037_1#1$1",focus="l")]
[name="梅希亚"]您何出此言？长官知道莱茵现在的处境难免会让一些同行得寸进尺，要是影响到检修工作，得不偿失。
[charslot(slot = "l", name = "avg_npc_2037_1#6$1",focus="l")]
[name="梅希亚"]他只是出于好心。
[charslot(slot="r", name = "avg_4212_nasti_1#1$1",focus="r")]
[name="娜斯提"]我一直以为他身上那套昂贵的西装就是用良知换来的。
[charslot(slot = "l", name = "avg_npc_2037_1#17$1",focus="l")]
[name="梅希亚"]......
[charslot(slot="r", name = "avg_4212_nasti_1#5$1",focus="r")]
[name="娜斯提"]况且，我很难想象一名特聘讲解员的询问会如此文不对题，除非，从一开始她就另有目的。
[charslot(slot="r", name = "avg_4212_nasti_1#1$1",focus="r")]
[name="娜斯提"]我知道，你必须维护自己的上司，所以我不会对此加以指责，但你也知道，在我面前你可以说实话。
[charslot(slot = "l", name = "avg_npc_2037_1#15$1",focus="l")]
[name="梅希亚"]......我确实觉得这件事不太对劲，但我认为高登长官绝不是在针对您。
[charslot(slot="r", name = "avg_4212_nasti_1#6$1",focus="r")]
[name="娜斯提"]理由？
[charslot(slot = "l", name = "avg_npc_2037_1#15$1",focus="l")]
[name="梅希亚"]娜斯提主任，我们才达成协议不久，没有道理在这么短的时间内向您二次施压。
[charslot(slot = "l", name = "avg_npc_2037_1#11$1",focus="l")]
[name="梅希亚"]如果长官真的另有所图，以他的谨慎，一定会把计划原委详尽地告诉我，避免出任何岔子。除非......
[charslot(slot="r", name = "avg_4212_nasti_1#2$1",focus="r")]
[name="娜斯提"]除非他藏着秘密。
[charslot(slot = "l", name = "avg_npc_2037_1#11$1",focus="l")]
[name="梅希亚"]......
[charslot(slot = "l", name = "avg_npc_2037_1#11$1",focus="l")]
[name="梅希亚"]每天总有一些时段，他会从办公区域消失，一开始我以为他只是去跟客户谈投资。
[charslot(slot = "l", name = "avg_npc_2037_1#11$1",focus="l")]
[name="梅希亚"]几天前一名投资人与我寒暄的时候，夸赞长官只用一次谈判就完成了所有合约。
[charslot(slot = "l", name = "avg_npc_2037_1#15$1",focus="l")]
[name="梅希亚"]可我记得长官说过，他与这名投资人的谈判很不顺利，需要安排更多时间......
[charslot(slot = "l", name = "avg_npc_2037_1#12$1",focus="l")]
[name="梅希亚"]欸，娜斯提主任，您干嘛这样看着我？
[charslot(slot="r", name = "avg_4212_nasti_1#9$1",focus="r")]
[name="娜斯提"]你违反了秘书的第一条准则。
[charslot(slot = "l", name = "avg_npc_2037_1#13$1",focus="l")]
[name="梅希亚"]啊！
[charslot(slot="r", name = "avg_4212_nasti_1#1$1",focus="r")]
[name="娜斯提"]而且你在梳理线索的时候，没有之前那么紧绷。
[charslot(slot = "l", name = "avg_npc_2037_1#1$1",focus="l")]
[name="梅希亚"]......是吗？
[charslot(slot = "l", name = "avg_npc_2037_1#1$1",focus="l")]
[name="梅希亚"]依照准则，我应该关上耳朵，闭紧嘴巴，只为长官着想，但现在我也不知道他到底在想什么了。
[charslot(slot="l",focus="n")]
[name="？？？"]你们是在聊我吗？
[charslot(slot = "l", name = "avg_npc_2037_1#12$1",focus="l")]
[name="梅希亚"]！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[charslot(slot="l", name = "avg_4212_nasti_1#1$1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r", name = "avg_npc_2034_1#1$1",posfrom="50,0",posto="50,0",duration=1.5, isblock=true)]
[charslot(slot="r",focus="r")]
[name="高登"]很高兴看到你们相处得如此融洽，我还以为小梅这样不善言辞的孩子，除了工作，不会交到朋友。
[charslot]
[charslot(slot = "m", name = "avg_npc_2037_1#5$1")]
[name="梅希亚"]高登长官，我......
[charslot]
[charslot(slot="l", name = "avg_4212_nasti_1#11$1",focus="l")]
[charslot(slot="r", name = "avg_npc_2034_1#1$1",focus="l",posfrom="50,0",posto="50,0",isblock=true)]
[name="娜斯提"]这条规则也在她的秘书准则里？
[charslot(slot="r", name = 

... (全文13782字符)
```

### level_act47side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g1_kazdelroom",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=3, keep=true, initamount=1, amount=0, block=false)]
[Delay(time=3)]
[charslot(slot = "m", name = "avg_npc_2048_1#1$1", duration=1.5, isblock=true)]
[name="拂哀菈"]感谢招待。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m", name = "avg_npc_2043_1#1$1",duration=1.2, isblock=true)]
[name="石翼魔"]客气什么，这些年难得还能见到女妖，我高兴还来不及。
[charslot(slot = "m", name = "avg_npc_2048_1#8$1",focus="m")]
[name="拂哀菈"]高兴又是为何？
[dialog]
[charslot]
[charslot(slot="m", name = "avg_npc_2043_1#1$1")]
[name="石翼魔"]这样我们也算认识了。等我或我的家人活到头了，也好请你来唱挽歌。
[name="石翼魔"]这年头，卡兹戴尔还是那个卡兹戴尔，但很少有女妖会来了。
[name="石翼魔"]没你们引渡，死去的同胞会找不到众魂的。
[charslot(slot = "m", name = "avg_npc_2048_1#4$1",focus="m")]
[name="拂哀菈"]抱歉。
[charslot(slot = "m", name = "avg_npc_2048_1#4$1",focus="m")]
[name="拂哀菈"]我会......尽我所能。
[charslot(slot="m", name = "avg_npc_2043_1#1$1")]
[name="石翼魔"]哈哈，我开玩笑的。你来，是为了给你们那棵“栖脚树”治病吧？
[dialog]
[charslot(slot="m", name = "avg_npc_2043_1#1$1",focus="n")]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[delay(time=2)]
[charslot(slot="m", name = "avg_npc_2043_1#1$1")]
[name="石翼魔"]这就是它的枝条？
[charslot(slot = "m", name = "avg_npc_2048_1#8$1",focus="m")]
[name="拂哀菈"]我们试过用咒言解析，但找不出它枯败的缘由。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]所幸，有朋友介绍了您这样一位熟识草木的土石之子。它是女妖一族生活的依凭，请务必——
[charslot(slot="m", name = "avg_npc_2043_1#1$1")]
[name="石翼魔"]我会帮忙。等我备上土......
[charslot(slot="m", name = "avg_npc_2043_1#1$1")]
[name="石翼魔"]方便的话，帮我去后院拿个盆？可能会有几只来偷菜的羽兽，赶走就是。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="49_g4_kazdelstreet_shabby",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[PlaySound(key="$e_atk_magic_m", volume=1)]
[name="拂哀菈"]“散去。”
[dialog]
[charslot]
[PlaySound(key="$d_avg_wing", volume=1)]
羽兽四散惊飞，破败的菜园却没有归于平静，一株菜苗在拂哀菈面前剧烈地摇晃着。
而后，在沾满尘埃的叶片之间，缓缓浮现出枝条般的黑色尖角。
[charslot(slot = "m", name = "avg_npc_2048_1#8$1",focus="m")]
[name="拂哀菈"]“偷菜的羽兽”......吗？
[charslot(slot="m",focus="n")]
[name="？？？"]滚开，不然我把你脑袋拧下来。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]这样扯着喉咙吓唬人，对嗓子不好的。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]别害怕，好吗？我无意伤害一个孩子。
[dialog]
[charslot]
[PlaySound(key="$d_avg_hidehaystack", volume=0.6)]
[charslot(slot="m",name="avg_npc_2052_1#1$1",duration=1.5, posfrom = "0,-50", posto = "0,0",isblock=true)]
幼小的女妖从叶片后面探出头来，下意识地把啃了一半的菜叶藏在了身后。
[name="幼小的女妖"]也别打我的菜叶的主意。
[charslot(slot = "m", name = "avg_npc_2048_1#7$1",focus="m")]
[name="拂哀菈"]......假如那是“你”的菜叶的话。
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#5$1")]
[name="幼小的女妖"]你拿的什么？
[dialog]
[charslot]
拂哀菈反应过来时，小女妖已经一把抢过她手中栖脚树的枝条，费劲地咧开嘴，试图从上面啃下点什么。
[charslot(slot="m",name="avg_npc_2052_1#6$1")]
[name="幼小的女妖"]呸。就是泥地里的普通树枝，都发臭了。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]饿了吗？稍等......雾湖边的露盏草刚刚成熟，出发前我还采来做了些糕点......
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#9$1")]
[name="幼小的女妖"]从死人身上扒吃的还更安全点。能不能别缠着我了？
[charslot(slot="m",name="avg_npc_2052_1#6$1")]
[PlaySound(key="$d_avg_enchantress_threat", volume=0.6)]
[name="幼小的女妖"]（威胁的低啸）
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]......
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#10$1")]
[name="幼小的女妖"]......你不害怕？明明就连那些大块头佣兵都怕这种声音。
[charslot(slot = "m", name = "avg_npc_2048_1#2$1",focus="m")]
[name="拂哀菈"]这是女妖的声音，我们族群的声音。
[charslot(slot = "m", name = "avg_npc_2048_1#4$1",focus="m")]
[name="拂哀菈"]我已经很久不曾在女妖曲中听到这个音符了。上一次唱出它的那个人，几年前就......
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]......你就是那个孩子。
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#5$1")]
[name="幼小的女妖"]教我这种声音的人，你认识她？
[name="幼小的女妖"]但我从没见过你。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]我们已经不常在卡兹戴尔行走。我们住在遥远的河谷，一个长着很多大树，能结出很多果子的地方。
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#3$1")]
[name="幼小的女妖"]吃上饭是要费劲的，要挨打的。
[charslot(slot="m",name="avg_npc_2052_1#1$1")]
[name="幼小的女妖"]如果有你说的那种地方，果子就那么白白结出来......那代价是什么？
[charslot(slot = "m", name = "avg_npc_2048_1#3$1",focus="m")]
[name="拂哀菈"]......真是聪明的孩子。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]或许，你该跟我回去，你属于那里，你会喜欢那里。
[charslot(slot = "m", name = "avg_npc_2048_1#1$1",focus="m")]
[name="拂哀菈"]哪怕你不相信那里存在。
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#1$1")]
[name="幼小的女妖"]我凭什么相信？
[charslot(slot = "m", name = "avg_npc_2048_1#2$1",focus="m")]
[name="拂哀菈"]你的名字......是娜斯提，对吗？
[dialog]
[charslot(slot="m",name="avg_npc_2052_1#5$1")]
[name="娜斯提"]——！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_hotel",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_plantwither_slow", channel="bgs", volume=0)]
[SoundVolume(volume=0.5, channel="bgs",fadetime=2)]
[charslot(slot = "m", name = "avg_npc_2035_1#4$1",duration=0.8, isblock=true)]
[name="拂哀菈"]那个方向......有女妖的气息？还有......什么东西，在枯萎、腐败？
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_2035_1#4$1")]
[name="拂哀菈"]不......娜斯提，你难道......
[charslot(slot = "m", name = "avg_npc_2035_1#4$1")]
[name="拂哀菈"]要重蹈覆辙？
[dialog]
[PlaySound(key="$d_avg_crutch_snow", volume=0.8)]
[charslot(slot = "m", name = "avg_npc_2035_1#4$1",posfrom="0,0",posto="-200,0",afrom=1, ato=0, 

... (全文22135字符)
```

### level_act47side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="68_g5_floatingstation",screenadapt="coverall")]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_2039_1#4$1", duration=1.5, isblock=true)]
[name="斯凯"]......
[charslot(slot = "m", name = "avg_npc_2039_1#4$1")]
[name="斯凯"]优胜劣汰，园区准则......莱茵什么时候也被归到淘汰者的队伍里了？
[dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "r", name = "avg_npc_2041_1#1$1", posfrom="300,0", posto="0,0", duration=1)]
[Delay(time=0.5)]
[PlaySound(key="$bodyfalldown3", volume=1)]
[charslot(slot = "r", name = "avg_npc_2041_1#4$1", focus="n")]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1", afrom=1, ato=1, posfrom="0,0", posto="-60,0", duration=0.4, focus="m",isblock=false)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1.2)]
[charslot(slot = "r", afrom=1, ato=1, posfrom="0,0", posto="60,0", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r",focus="r",isblock=true)]
[name="雅斯彭"]抱歉......呃，斯凯先生？你怎么在这里！
[charslot(slot = "m", name = "avg_npc_2039_1#3$1",focus="m")]
[name="斯凯"]这话应该我来问吧？“幸运瘤兽”应该已经办完进驻资质注销手续了，你在这儿干嘛？
[charslot(slot = "r", name = "avg_npc_2041_1#4$1",focus="r")]
[name="雅斯彭"]我没有利用任何非法途径！在注销进驻资质前，我们靠自己解决了技术难题，实在太幸运了......
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]解决了？为什么没有人通报工程部？
[charslot(slot = "r", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]可能是事出突然，交接上出了问题......
[charslot(slot = "r", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]再、再说了，刚刚高登长官都在广播里通报了——莱茵生命主导的工程检修全面暂停。
[charslot(slot = "r", name = "avg_npc_2041_1#3$1",focus="r")]
[name="雅斯彭"]现在，我也不需要向你汇报了吧？
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]......
[dialog]
[PlaySound(key="$rungeneral")]
[charslot(slot = "r", name = "avg_npc_2041_1#1$1",posfrom="70,0",posto="-30,0",afrom=1, ato=0, duration=0.8, isblock=true)]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]三天都没法解决的问题，突然就搞定了？
[charslot(slot = "m", name = "avg_npc_2039_1#3$1",focus="m")]
[name="斯凯"]幸运的“幸运瘤兽”吗......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[Background(image="68_g6_floatinglabmodule",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]快点，读数，快点！他们的人指不定什么时候就回来了......
[charslot(slot = "m", name = "avg_npc_2039_1#5$1",focus="m")]
[name="斯凯"]......数据完全达标。不如说达标得有点太精准了，简直像是对着标准刻意调整过一样。
[charslot(slot = "m", name = "avg_npc_2039_1#5$1",focus="m")]
[name="斯凯"]嗯？这几个......不是园区通用的螺丝型号吧？
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]拧不动。完全焊住了......整个核心动力装置都被封死了。
[dialog]
[charslot]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="en")]
[SoundVolume(volume=0.5, channel="en",fadetime=2)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_2039_1#8$1",focus="m")]
[name="斯凯"]......但我听也能听出来，园区允许使用的动力元件里，没有任何一个型号的能发出这种声响。
[stopsound(fadetime=2, channel="en")]
[charslot(slot = "m", name = "avg_npc_2039_1#3$1",focus="m")]
[name="斯凯"]他们是从哪搞来的这种不合规的奇怪元件？园区所有零件的采购权不是都归——
[charslot(slot = "m", name = "avg_npc_2039_1#1$1",focus="m")]
[name="斯凯"]哈......原来是这样，我还以为园区的准则真的是优胜劣汰。
[dialog]
[charslot]
[PlaySound(key="$d_avg_makephonecall")]
[delay(time=1.5)]
[PlaySound(key="$d_avg_telephonebusy")]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]......忙着帮那个混蛋整理莱茵的事故报告吗？
[charslot(slot = "m", name = "avg_npc_2039_1#7$1",focus="m")]
[name="斯凯"]算了，就算上报给娜斯提主任，她也会质疑我没有证据。
[charslot(slot = "m", name = "avg_npc_2039_1#3$1",focus="m")]
[name="斯凯"]还有谁能帮我......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="29_g9_headquarter",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraEffect(effect="Grayscale", fadetime=3, keep=true, initamount=1, amount=0, block=true)]
[charslot(slot = "r", name = "char_249_muesys_1#1", duration=1.5)]
[charslot(slot = "l", name = "avg_4212_nasti_1#4$1", duration=1.5,isblock=true)]
[charslot(slot="l", name = "avg_4212_nasti_1#4$1",focus="l")]
[name="娜斯提"]我的车还有五分钟到。要是实验园区有吉祥物玩偶，我会给你带一个。
[charslot(slot = "r", name = "char_249_muesys_1#4",focus="r")]
[name="缪尔赛思"]我可不是需要人哄的小孩子。
[charslot(slot="l", name = "avg_4212_nasti_1#4$1",focus="l")]
[name="娜斯提"]那再见？
[charslot(slot = "r", name = "char_249_muesys_1#5",focus="r")]
[name="缪尔赛思"]你从塞雷娅办公室出来之后，就一直待在走廊里跟你的“树枝”玩抛接球。
[charslot(slot = "r", name = "char_249_muesys_1#4",focus="r")]
[name="缪尔赛思"]故意拖延时间不见我？我都看到了哦。
[charslot(slot="l", name = "avg_4212_nasti_1#4$1",focus="l")]
[name="娜斯提"]利用水分身侵犯个人隐私应当被追究法律责任。
[charslot(slot = "r", name = "char_249_muesys_1#5",focus="r")]
[name="缪尔赛思"]在哥伦比亚出现第二个水精灵之前，你无处申诉。
[dialog]
[charslot]
[PlaySound(key="$d_avg_swordwhoosh", volume=1)]
话音刚落，娜斯提腰间的“树枝”突然向上伸长了一截，枝端对准水精灵的方向，旋开工具片。
[dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[charslot(slot="m",name="avg_249_mlyss_1#11$1")]
[delay(time=0.5)]
[Effect(name="$e_muesys_hide",layer = 4,rox=-7,roy=79,roz=100)]
[playsound(key="$d_avg_watersubbreak",volume=0.7)]
[charslot(slot="m",name="avg_249_mlyss_1#11$1",posfrom="0,0",posto="80,0",afrom=1, ato=0, duration=0.3, isblock=true)]
[delay(time=2)]
缪尔赛思像排练

... (全文20202字符)
```

### level_act47side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="68_g7_airrestaurant",screenadapt="coverall")]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_1260_1#1$1")]
[charslot(slot = "l", name = "avg_npc_2039_1#7$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",afrom=1, ato=1, posfrom="0,0",posto="150,0",duration=1, isblock=false)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1260_1#1$1",afrom=1, ato=1, posfrom="0,0",posto="50,0",duration=0.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", focus="r")]
[name="行政秘书"]我说了，你不能进去。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]我也说了，我隶属于莱茵生命，比你更清楚园区设施的管理规定，进入云中餐厅根本不需要特殊权限。
[charslot(slot = "r", focus="r")]
[name="行政秘书"]平时是不需要，但现在里面有贵客。
[stopmusic(fadetime=1)]
[dialog]
[charslot]
[name="？？？"]让他进来吧，这位年轻人应该是来找我的。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_2042_1#1$1",posfrom="0,0",posto="50,0",duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(key="$m_avg_creepy_loop", volume=0.6)]
[stopsound(channel="f",fadetime=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_2039_1#1$1",posfrom="-200,0",posto="0,0",duration=2, isblock=true)]
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r",isblock=true)]
[name="古斯塔夫"]看来莱茵生态园的事故已经处理完了？
[charslot(slot = "l", name = "avg_npc_2039_1#1$1",focus="l")]
[name="斯凯"]古斯塔夫先生的消息真灵通。
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]哈哈，只是恰好有几个熟人在这个园区为哥伦比亚的新事业尽忠职守。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]其中包括高登·谭农？
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]看来你来这里，并非为了替莱茵挽回损失。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]就算越级申请应急补助，也无法让莱茵赶上展会。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]请您先看看这份检查报告。
[dialog]
[charslot(slot="r", name = "avg_npc_2042_1#8$1",focus="r",isblock=true)]
[PlaySound(key="$d_avg_paper1", volume=1)]
[delay(time=1.3)]
[name="古斯塔夫"]一家新兴科技公司为了留在园区，紧急解决了检修时发现的工程缺陷......有什么问题？
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]“幸运瘤兽”根本没有通过工程复检，按规定在今天之内必须撤出园区。
[charslot(slot = "l", name = "avg_npc_2039_1#3$1",focus="l")]
[name="斯凯"]但就在刚才，我见到了他们的经理，发现困扰了他们数月之久的供能问题，已经被完全解决了。
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]展会在即，死限、科学、奇迹......“薯片的经典口味”而已。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]不，您看这一页——
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]我额外关注了几个常规检查中不会涉及的元件，它们的输出功率均高出额定功率十倍不止。呃，简单点说——
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]不用解释那些名词，年轻人。你随身带着的那本《哥伦比亚源石元件制式与标准》还是由我主导拟定的。
[charslot(slot="r", name = "avg_npc_2042_1#6$1",focus="r")]
[name="古斯塔夫"]你是想说，“幸运瘤兽”在短短几小时内，“发明”了远超整个国家通行标准的动力元件？
[charslot(slot = "l", name = "avg_npc_2039_1#1$1",focus="l")]
[name="斯凯"]“发明”？他们没那个本事。我认为，有人为那只活不下来的蠢物移植了一颗不属于哥伦比亚的新心脏。
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]年轻人，你知道园区的规定。现在各个国家都在关注我们在浮空技术领域的进展，为保障安全，所有零件只能是哥伦比亚制造。
[charslot(slot = "l", name = "avg_npc_2039_1#1$1",focus="l")]
[name="斯凯"]不用紧张，古斯塔夫先生，这并不是管理局的失职。
[charslot(slot = "l", name = "avg_npc_2039_1#3$1",focus="l")]
[name="斯凯"]普通的执行专员怎么可能让企业躲过莱茵的定期检查和不定期抽检，除非有人能操纵工程部的检修顺序。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]巧的是，娜斯提主任正好跟一位长官达成了协议......
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]高登·谭农。
[charslot(slot = "l", name = "avg_npc_2039_1#7$1",focus="l")]
[name="斯凯"]那家伙千方百计地想要捆住莱茵的手脚，因为我们才是“螺旋桨天堂”真正的发起方，工程部是一双随时可能发现他秘密的眼睛。
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]所以你猜测，高登·谭农非但没有当好管理者，反倒监守自盗，做起了“供应商”？
[charslot(slot="r", name = "avg_npc_2042_1#8$1",focus="r")]
[name="古斯塔夫"]这是很严重的指控，年轻人。
[charslot(slot = "l", name = "avg_npc_2039_1#1$1",focus="l")]
[name="斯凯"]所以我才只能找您，古斯塔夫先生。
[charslot(slot = "l", name = "avg_npc_2039_1#1$1",focus="l")]
[name="斯凯"]在园区抵达特区之前，只有您才有心也有力对付这个“尽忠职守”的下属。
[dialog]
[charslot(slot="r", name = "avg_npc_2042_1#4$1",focus="r")]
[delay(time=0.8)]
[charslot(slot="r", name = "avg_npc_2042_1#1$1",focus="r")]
[name="古斯塔夫"]我突然好奇一件事——你的上司知道这件事吗？
[charslot(slot = "l", name = "avg_npc_2039_1#3$1",focus="l")]
[name="斯凯"]如果娜斯提主任能有所作为，莱茵生命何至于现在......
[charslot(slot="r", name = "avg_npc_2042_1#3$1",focus="r")]
[name="古斯塔夫"]那就好。
[charslot(slot = "l", name = "avg_npc_2039_1#5$1",focus="l")]
[name="斯凯"]唔，什么意思？
[charslot(slot="r", name = "avg_npc_2042_1#3$1",focus="r")]
[name="古斯塔夫"]难得遇见你这样敏锐又勇敢的年轻人。娜斯提如果知道的话，恐怕不会同意你留下来陪我一段时间。
[dialog]
[charslot]
[PlaySound(key="$d_avg_doorbreak")]
[charslot(slot = "m", name = "avg_npc_2039_1#12$1", focus="m",isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_901_1#1$1",posfrom="-150,0",posto="-30,0",duration=0.5, focus="m",isblock=false)]
[charslot(slot="r", name = "avg_npc_901_1#1$1",posfrom="150,0",posto="30,0",duration=0.5, focus="m",isblock=true)]
[charslot(slot = "m", name = "avg_npc_2039_1#12$1",afrom=1, ato=1, posfrom="0,0",posto="0,-30", focus="m",duration=0.5)]
[charslot(slot = "m", action="shake", power=3, times=30, duration=0.3, focus="m", isblock=true)]
[delay(time=0.5)]
[charslot(slot = "m",name = "avg_npc_2039_1#11$1",posfrom="0,-30",posto="0,-30",focus="m",isblock=true)]
[name="斯凯"]古斯塔夫——
[dialog]
[charslot]
[charslot(slot="m", name = "avg_npc_2042_1#2$1")]
[name="古斯塔夫"]只有我才“有心也有力”对付高登......哈哈，有趣的说法。早年间他确实经常和我作对，但那只是年轻人的一时莽撞，正如你。
[charslot(slot="m", name = "avg_npc_2042_1#3$1")]
[name="古斯塔夫"]而我教给他的第一条规矩就是：代表哥伦比亚时，我们永远是一体的。
[charslot(slot = "l", name = "avg_npc_901_1#1$1",posfro

... (全文22353字符)
```

### level_act47side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playMusic(key="$monastery_sad_loop", volume=0.6)]
[Delay(time=1)]
[Background(image="bg_hotel",screenadapt="coverall",fadetime=0, block=true)]
[focusout(type="bg", id="68_g2_groundparkstreet_n", from=0, to=0.8, duration=0, block=false)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_highheeledshoe_carpet_fts", volume=1)]
[delay(time=1.5)]
[name="？？？"]抱歉，我来晚了。今天的工作有些忙。
[name="疲惫的女声"]梅、梅希亚......请你......
[name="疲惫的女声"]我需要......想起，更多......
[dialog]
[charslot(slot = "m", name = "avg_npc_2037_1#1$1", bstart=0.2, bend=0.5, duration=0.8, isblock=true)]
[name="梅希亚"]您的情况很特殊。
[name="梅希亚"]您的记忆像是枯枝上仅存的败叶，拂去灰尘或许能令它们恢复些许色泽，但太过用力，只会造成伤害。
[charslot(slot = "m", name = "avg_npc_2037_1#9$1", bstart=0.2, bend=0.5)]
[name="梅希亚"]我甚至不该去拨弄它们的，若不是......
[charslot(slot = "m", name = "avg_npc_2037_1#9$1", bstart=0.2, bend=0.5)]
[name="梅希亚"]抱歉，拂哀菈女士。
[charslot]
[name="拂哀菈"]我需要......知道，需要......想起。
[charslot(slot = "m", name = "avg_npc_2037_1#8$1", bstart=0.2, bend=0.5)]
[name="梅希亚"]离开家乡之后的回忆对您来说并不愉快，但如果您坚持......那就闭上眼睛吧，我们继续尝试。
[dialog]
[charslot]
[delay(time=1)]
[PlaySound(key="$d_avg_bowl_smash", volume=0.6)]
有些费力地，梅希亚把她总带在身边的那台老旧的幻灯机搬上了桌子。
[PlaySound(key="$d_avg_mgcdevcstartp", volume=1)]
随着她指尖滑动，玻璃幻灯片落入卡槽，一幅陌生的景象笼罩了女妖衰老的身躯。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="44_g4_towerroom",screenadapt="coverall")]
[focusout(type="bg", id="44_g7_ludwigsuniv_inside", from=0.8, to=0, duration=0, block=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_signlntrfrnc", volume=1)]
[bgeffect(name="$eb_tvnoise",layer=1)]
[CameraEffect(effect="Grayscale", amount=0.5, keep=true)]
[PlaySound(key="$d_avg_filmprojection")]
[playsound(key="$d_avg_filmprojection_loop", loop=true, channel="bgs",delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[delay(time=2)]
[name="拂哀菈"]......我记得，那个地方。
[name="梅希亚"]莱塔尼亚？
[name="拂哀菈"]她......提过。
[name="拂哀菈"]那里，高塔......镣铐，血。
缓慢地，模糊地，一段记忆在幻灯机投射出的背景上晕开。梅希亚辨认出一具衰老的身躯被锁在墙边，几个穿着长袍的人影进进出出。
一些血的气味，一段可怖的旋律，一些术式的痕迹。
[name="梅希亚"]莱塔尼亚的高塔，您被囚禁在那里过？......作为实验对象？
[name="梅希亚"]若不是一位巫妖出手相助，您几乎就要被埋葬在高塔术师的书页之下。
[dialog]
[PlaySound(key="$d_avg_button", volume=0.8)]
[Background(image="26_g5_laterano_chapelout",screenadapt="coverall",fadetime=0.5, block=true)]
[name="梅希亚"]圣城的安魂教堂，您在那里为人送葬？是为您流落在外的同胞，还是为您族群的......仇敌？
[name="梅希亚"]但那些天使并不领情，对吗？他们的葬礼上需要的是欢笑，而不是您的......哀哭。
[name="梅希亚"]您差点被戍卫队逮捕。
[dialog]
[PlaySound(key="$d_avg_button", volume=0.8)]
[Background(image="29_g2_edgeofbase",screenadapt="coverall",fadetime=0.5, block=true)]
[name="梅希亚"]您来到哥伦比亚......是横穿了整片拓荒地，甚至......骸骨荒原？
[name="梅希亚"]那片野兽都不敢踏足的、被风沙切割得千疮百孔的土地？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[StopSound(channel="bgs", fadetime=0.5)]
[bgeffect]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="bg_hotel",screenadapt="coverall",fadetime=0, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_2037_1#5$1", duration=1.5, isblock=true)]
[name="梅希亚"]您最后还是来到了这里。
[charslot(slot = "m", name = "avg_npc_2037_1#7$1")]
[name="梅希亚"]为什么，偏偏是这座园区？您是来寻找什么......
[charslot(slot = "m", name = "avg_npc_2035_1#1$1")]
[name="拂哀菈"]这里，这里也有......树。
[charslot(slot = "m", name = "avg_npc_2035_1#1$1")]
[name="拂哀菈"]这里的树，也在枯萎、腐败......
[charslot(slot = "m", name = "avg_npc_2035_1#1$1")]
[name="拂哀菈"]枯萎、腐败。
[charslot(slot = "m", name = "avg_npc_2037_1#15$1")]
[name="梅希亚"]原来如此。
[charslot(slot = "m", name = "avg_npc_2037_1#15$1")]
[name="梅希亚"]这里的确有一座生态园，它也确实刚刚发生过一场令人不忍注目的事故，枯萎、腐败，如您所说。
[charslot(slot = "m", name = "avg_npc_2037_1#11$1")]
[name="梅希亚"]而那座生态园的主人......
[charslot(slot = "m", name = "avg_npc_2037_1#11$1")]
[name="梅希亚"]是另一位女妖。
[charslot(slot = "m", name = "avg_npc_2037_1#11$1")]
[name="梅希亚"]或许，您认识它吗？
[dialog]
[charslot]
那支在生态园酿成大祸，后来又被高登收缴的骨笔，就这样洁白无辜地躺在梅希亚的手中。
[dialog]
[charslot(slot = "m", name = "avg_npc_2035_1#4$1",duratin=0.8,isblock=true)]
[name="拂哀菈"]......她。
[charslot(slot = "m", name = "avg_npc_2035_1#4$1")]
[name="拂哀菈"]她的气息......她在。
[charslot(slot = "m", name = "avg_npc_2037_1#1$1")]
[name="梅希亚"]所以，您是来找人的。
[charslot(slot = "m", name = "avg_npc_2035_1#3$1")]
[name="拂哀菈"]我想......我想见她......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cherunder_2",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=1)]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1", posfrom="50,0",posto="50,0", duration=0.8)]
[charslot(slot = "r", name = "avg_npc_1000_1#1$1", posfrom="50,0",posto="50,0",duration=0.8, isblock=true)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1", focus="l")]
[name="费尔南"]不用把身子压得这么低，奥克里，你背上的施术装置已经歪了。
[charslot(slot = "r", name = "avg_npc_1000_1#3$1",focus="r")]
[name="奥克里"]这可是莱茵生命的地下通道，说不定连墙壁里都有纳米监听器！
[charslot(slot = "r", name = "avg_npc_1000_1#3$1",focus="r")]
[name="奥克里"]再说了，我们还要当心园区的报警系统......既然是帮高登长官办事，为什么还得躲着警卫队？
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]你觉得有几个下属能得到他的完全信任？
[charslot(slot = "r", name = "avg_npc_1000_1#1$1",focus="r")]
[name="奥克里"]唔......
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]看电梯的小警卫都有可能是哪位大人物的第三只眼睛。要是出了岔子，牵扯出的问题可比这几箱违禁品严重得多。
[charslot(slot = "r", name = "avg_npc_1000_1#1$1",focus="r")]
[name="奥克里"]所以我们这两个没有相关利益的外来人，反倒是替他“销赃”的最佳人选？
[charslot(slot = "l", name = "avg_4214_cairn_1#7$1",focus="l")]
[name="费尔南"]没错。
[charslot(slot = "l", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="

... (全文16015字符)
```

### level_act47side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g13_trimountlivingroom",screenadapt="coverall")]
[playMusic(intro="$act15_intro",key="$act15_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside",channel="f", volume=0)]
[SoundVolume(volume=0.3, channel="f",fadetime=2)]
[name="愤怒的公司代表"]*哥伦比亚粗口*天上飘着的那棵树到底是怎么回事？
[name="愤怒的公司代表"]展会没几天就要开幕了，你数数它占了几家公司的展位？莱茵生命可没有申请上层的展示权限！
[name="急切的公司代表"]一定是莱茵和管理局官员私相授受！昨晚我亲眼看到了全程，园区负责人高登长官就在那棵树上！
[name="急切的公司代表"]前管理局局长古斯塔夫在广播里打包票，声称第二天早上一定会给我们一个交代，结果呢？
[name="急切的公司代表"]都这个时候了，听证会一点动静都没有，故意拖时间是不是！
[StopSound(channel="f", fadetime=2)]
[dialog]
[charslot(slot = "m", name = "avg_npc_1041_1#1$1", duration=0.8, isblock=true)]
[name="工作人员"]请各位少安毋躁。
[name="工作人员"]本次事件关乎数百家企业对园区的工程部和行政部的信任问题，我们需要时间谨慎处理，力求给各位最满意的处理方案。
[dialog]
[charslot]
[name="愤怒的公司代表"]谁要你们谨慎处理了？
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="工作人员"]嗯？
[dialog]
[charslot]
[name="愤怒的公司代表"]上天的又不是第二个环形实验室，有什么大惊小怪的？
[name="愤怒的公司代表"]工程部负责的检修早就停了，行政部的资质审查也结束了，现在这个节骨眼谁还会计较园区的部门负责人是否渎职？
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="工作人员"]可举行听证会是必要的监察流程......
[dialog]
[charslot]
[name="急切的公司代表"]要调查还是审判是你们的事，我们只想立马知道听证会的最终结果——
[name="急切的公司代表"]这场必定能轰动哥伦比亚乃至整个泰拉的“天空生活展会”，到底还能不能开？
[dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="68_g9_treeplatform_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_901_1#1$1", posfrom="-200,0", posto="0,0", duration=2, isblock=true)]
[delay(time=0.5)]
[name="园区警卫"]让开。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1", isblock=true)]
[name="斯凯"]......
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1", posfrom="0,0", posto="0,-80",afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_sit_tatami", volume=1)]
[delay(time=1.5)]
[charslot]
[charslot(slot = "m", name = "avg_npc_901_1#1$1")]
[name="园区警卫"]我再说一遍，让开。
[dialog]
[charslot]
[name="斯凯"]......
[charslot(slot = "m", name = "avg_npc_901_1#1$1")]
[name="园区警卫"]你们这些研究员，真当自己坐在这里我就没办法动你们背后的非法设备了？
[dialog]
[charslot]
[name="斯凯"]在听证会正式开始之前，它仍是莱茵生命的财产。再说了，非法设备？
[name="斯凯"]警卫先生，你难道没认出来这只是一个“浮空种植单元”吗？你身边飘浮的那些树苗，跟我们背后的这棵，没有区别啊？
[charslot(slot = "m", name = "avg_npc_901_1#1$1")]
[name="园区警卫"]强词夺理......来人！
[dialog]
[charslot]
[playsound(key="$d_gen_soldiersrun")]
[charslot(slot = "r", name = "avg_npc_901_1#1$1",posfrom="300,0",posto="30,0", duration=1.2)]
[charslot(slot = "l", name = "avg_npc_901_1#1$1",posfrom="-300,0",posto="-30,0", duration=1.2, isblock=true)]
[delay(time=1)]
[charslot]
[charslot(slot = "l", name = "avg_npc_529_1#1$1",focus="l", isblock=true)]
[name="研究员"]......斯凯，我们人手不够，如果对方动用强制手段，我们撑不了多久。
[name="研究员"]更何况我们也不知道身后的树形装置是否违规、有没有危险。毕竟两年前，克丽斯腾总辖不就是......
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_2039_1#7$1", posfrom="0,-80", posto="0,0", duration=0.5, isblock=true)]
[charslot(slot = "r", focus="r",isblock=true)]
[name="斯凯"]我只问你一个问题，作为一名科学家，你甘心把娜斯提主任的科研成果拱手让人吗？
[charslot(slot = "l", name = "avg_npc_529_1#1$1",focus="l",isblock=true)]
[name="研究员"]不，但......
[charslot(slot = "r", name = "avg_npc_2039_1#7$1",focus="r")]
[name="斯凯"]那就先行动起来，别让自己后悔。
[charslot(slot = "r", name = "avg_npc_2039_1#3$1",focus="r")]
[name="斯凯"]啧，莱茵留驻园区的人数受限，我们的人还是太少了，要是......
[charslot(slot = "l",focus="n")]
[name="？？？"]你是不是忘了我们也是莱茵生命的雇员，斯凯先生？
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_2044_1#1$1",duration=1.2, isblock=false)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_2045_1#1$1",duration=1.2, isblock=true)]
[delay(time=1.7)]
[charslot]
[charslot(slot = "m", name = "avg_npc_2039_1#7$1")]
[name="斯凯"]我不想把你们牵扯进来。
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_2044_1#1$1",focus="r")]
[charslot(slot = "l", name = "avg_npc_2045_1#1$1",focus="r", isblock=true)]
[name="体验员B"]你是指听证会的调查？别瞎担心了，诬告和罪名我们哪样见得少过？
[charslot(slot = "l", focus="l")]
[name="体验员A"]早点喊我们，这群警卫说不定都上不了这个浮空平台。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_901_1#1$1")]
[name="园区警卫"]怎么，从贫民窟征集来的体验员还想逞英雄？
[name="园区警卫"]藏匿非法设备、破坏他人财物、知情不报......光这些罪名就足够把你们打包送进监狱！
[dialog]
[charslot]
[charslot(slot = "r", name = "avg_npc_2044_1#1$1",focus="r")]
[charslot(slot = "l", name = "avg_npc_2045_1#1$1",focus="r", isblock=true)]
[name="体验员B"]要不是娜斯提主任收留我，我现在可能已经在监狱里了。
[charslot(slot = "l", focus="l")]
[name="体验员A"]要动树，就从我们身上跨过去。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_901_1#1$1")]
[name="园区警卫"]好......那就别怪我动手了！
[dialog]
[charslot]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=1)]
莱茵研究员和体验员组成的人墙死死拦着蛮横的警卫，好事的围观者站在外围，仰头看着这棵突兀的“树”。
人群背后，一个陌生高大的黑影走过，脚步铮铮。
[dialog]
[PlaySound(key="$d_avg_woodfloor_fts", volume=1)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_2038_1#5$1", bstart=0.2, bend=0.7, duration = 0.8, isblock=true)]
[name="？？？"]......
[name="？？？"]这就是莱茵的......“树”。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_hotel",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_2037_1#1$1",isblock=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_outside", channel="crowd",loop=true, volume=0.4)]
[charslot(slot="m",focus="n")]
[PlaySound(key="$d_avg_telephonering", channel="phone")]
[delay(time=1.5)]
[PlaySound(key="$d_avg_telephone", channel="phone")]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_2037_

... (全文17596字符)
```

### level_act47side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_wilderness_m",screenadapt="coverall")]
[focusout(type="bg", id="51_g13_seabornnest", from=0, to=1, duration=0, block=false)]
[Delay(time=1)]
[PlaySound(key="$blizzard",loop=true, channel="w", volume=0.5)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_mouse", volume=1)]
[delay(time=0.3)]
[name="父亲"]树林里，一只沙地兽吸引了我的注意，我的常识告诉我，这种小型生物只会出现在荒野。
[name="父亲"]它受了惊吓，往灌木丛里逃窜，好奇心驱使我向前追去，扒开荆棘和藤蔓，我的眼前出现了意想不到的景象......
[dialog]
[PlaySound(key="$d_avg_hidehaystack", volume=1)]
[delay(time=2)]
[name="父亲"]小费妮，你看到了吗？
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=false)]
[focusout(type="bg", id="51_g13_seabornnest", from=1, to=0.8, duration=0.5, block=false)]
[Delay(time=0.5)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[focusout(type="bg", id="51_g13_seabornnest", from=0.8, to=0.7, duration=1, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="女儿"]嗯！
[name="女儿"]好大一片沙漠和天空，它们接在一起的地方是粉色的，跟课本里的插图完全不一样，而且......
[name="女儿"]闻起来甜甜的。
[name="父亲"]哈哈，那是你妈妈在烤小蛋糕，一会儿就能开饭啦。
[name="女儿"]爸爸，你再讲一遍去东部荒原探险的故事好不好？唔......不，还是讲飘浮在天上的城市吧。
[name="父亲"]别着急孩子，奇妙的经历数不胜数，我们还有很多时间。
[name="父亲"]等小费妮长大，小脚迈得更利索了，会见到我看到过的一切的。我向你保证。
[dialog]
[stopsound(channel="w",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[focusout(type="bg", id="51_g13_seabornnest", from=0.7, to=0, duration=1, block=false)]
[Background(image="bg_snowconutryinside",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=false)]
[CameraEffect(effect="Grayscale", fadetime=3, keep=true, initamount=1, amount=0, block=true)]
[charslot(slot = "r", name = "avg_npc_1254_1#1$1", duration=1.5)]
[charslot(slot = "l", name = "avg_4214_cairn_1#6$1", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_4214_cairn_1#6$1",focus="l")]
[name="费尔南"]你能不能别对我的客人说些有的没的？
[charslot(slot = "r", name = "avg_npc_1254_1#1$1",focus="r")]
[name="老伯恩"]是你这个实习导游没做好，他们显然更喜欢我的故事。
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]我的工作是带客人游览真实存在的地方。
[charslot(slot = "r", name = "avg_npc_1254_1#1$1",focus="r")]
[name="老伯恩"]难道只有你们公司标记出来的景点才是真实存在的？荒谬，那我年轻时的那些经历算什么？
[name="老伯恩"]我早就说过，你不应该照着导游手册一板一眼地讲，你要探索没人走过的路——
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]然后一事无成，被邻居嘲笑，到了晚年只能给镇上的小孩编瞎话吗？
[charslot(slot = "l", name = "avg_4214_cairn_1#10$1",focus="l")]
[name="费尔南"]我相信过你的故事——会飞的循兽、飘浮的城市、金粉色的骸骨荒原......它们现在依旧是我珍贵的回忆。
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]但你太相信自己的故事了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",posfrom="0,0",posto="-150,0",afrom=1, ato=0, duration=0.8, isblock=true)]
[delay(time=1.8)]
[PlaySound(key="$d_avg_closedoorheavy", volume=1)]
[delay(time=0.3)]
[charslot(slot = "r", name = "avg_npc_1254_1#1$1",focus="r")]
[name="老伯恩"]费尔南！咳咳，你给我回来！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[name="工作人员"]恭喜您，费尔南·伯恩小姐，您的资质审核已经通过，从今天起您就是独立旅行社的社长了。
[charslot(slot = "m", name = "avg_4214_cairn_1#3$1")]
[name="费尔南"]太感谢了。虽然旅行社的成员只有我一个，但也算是顺利起步了！
[dialog]
[charslot]
[name="工作人员"]一个？我记得您提交的名单上还有一位成员的名字啊，好像是......
[charslot(slot = "m", name = "avg_4214_cairn_1#3$1")]
[name="费尔南"]马丁·伯恩，我老爹的名字，他去年就过世啦。
[dialog]
[charslot]
[name="工作人员"]抱歉......
[charslot(slot = "m", name = "avg_4214_cairn_1#7$1")]
[name="费尔南"]不用道歉，要不是他，我也不会下定决心开一家属于自己的旅行社。
[charslot(slot = "m", name = "avg_4214_cairn_1#3$1")]
[name="费尔南"]虽然没办法跟他一起旅行，但至少在名义上，老伯恩永远是我社的重要成员。
[dialog]
[charslot]
[name="工作人员"]您的父亲会很欣慰的。对了，您制定好开业后的第一条旅游路线了吗？我可以向您推荐几个热门景点。
[charslot(slot = "m", name = "avg_4214_cairn_1#4$1")]
[name="费尔南"]唔......有没有从来没人去过的地方？
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot]
[charslot(slot = "r", name = "avg_4212_nasti_1#1$1")]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",isblock=true)]
[Background(image="bg_cellroomB",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]在大多数同行眼里，闯禁区只是我的商业噱头，只有我跟我的客人知道，我们见证了多少奇妙的景象，完成了多少不可能的事。
[charslot(slot = "l", name = "avg_4214_cairn_1#4$1",focus="l")]
[name="费尔南"]“螺旋桨天堂”是这趟旅程的目的地，我想提前看看未来的景象，而我的客人想实现一个模糊的心愿。
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]娜斯提主任，我真的不是故意跟莱茵作对......客人的状况不佳，我只能从同为女妖的您身上搜集线索，我——
[charslot(slot = "r", name = "avg_4212_nasti_1#1$1",focus="r")]
[name="娜斯提"]不用向我道歉，费尔南小姐。我不是来兴师问罪的，我只是想知道你和你的客人的来历。
[charslot(slot = "r", name = "avg_4212_nasti_1#1$1",focus="r")]
[name="娜斯提"]要是今后你出版自传，我会拜读，但现在时间有限。
[charslot(slot = "l", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]您是在担心听证会？放心吧，召开时间一直在调整，估计是园区的调查还没结束。
[charslot(slot = "r", name = "avg_4212_nasti_1#2$1",focus="r")]
[name="娜斯提"]审判会比你想象的来得更快。
[charslot(slot = "r", name = "avg_4212_nasti_1#5$1",focus="r")]
[name="娜斯提"]请你尽可能简短地告诉我那名女妖客人的情况。你们在哪里相识，为什么会来这里，以及......她的身体状况如何？
[charslot(slot = "l", name = "avg_4214_cairn_1#4$1",focus="l")]
[name="费尔南"]我记得那是两个月前，在骸骨荒原......
[dialog]
[PlaySound(key="$flashback", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot

... (全文22686字符)
```

### level_act47side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="29_g1_outdoorbase",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_2032_1#1$1",duration=1.5)]
[delay(time=2)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[name="娜斯提"]......
[Dialog]
[playsound(key="$d_avg_wind")]
[playMusic(key="$calm_loop", volume=0.6)]
[charslot(slot = "m", focus = "n")]
风吹动年轻女妖手中的树叶，声音从其间掉落。
[playsound(key="$d_avg_childrenlaugh",volume=0.3)]
[playsound(key="$d_avg_warmbonfire_loop", loop=true, channel="f",volume=0.3)]
[name="河谷孩子们的声音"]（萨卡兹语）再讲一个，再讲一个！
[name="拂哀菈的声音"]（萨卡兹语）想不想听铁皮游侠的故事？
[name="拂哀菈的声音"]（萨卡兹语）他还来过我们的河谷呢。如今笼罩着雾湖的雾，最早就是从他的大烟斗里飘出来的......
[StopSound(channel="f", fadetime=2)]
[charslot(slot="m",name="avg_npc_2032_1#6$1")]
[name="娜斯提"]......
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_magic_4",volume=0.5)]
[name="菈玛莲的声音"]（萨卡兹语）这样，就能让羽角收拢，遮住你的双眼。
[name="哀珐尼尔的声音"]（萨卡兹语）为了白天睡觉的时候当眼罩用？
[name="菈玛莲的声音"]（萨卡兹语）不是，当然不是。是为了你在葬仪上流泪时，能从容地将那泪水编织成挽歌......
又一段声音播放完毕，年轻的女妖将叶片收进了怀里，她的眼神骤然变得警惕起来。
[stopmusic(fadetime=2)]
[charslot(slot="m",name="avg_npc_2032_1#2$1")]
[name="娜斯提"]再偷听的话，我会把你扔进混凝土搅拌机里。
[Dialog]
[delay(time=1)]
[Image(image="68_i16", xScale=1.4, yScale=1.4,screenadapt="coverall",x=250,y=-80,fadetime=2)]
[playMusic(key="$DecisiveBattle_loop", volume=0.6)]
[ImageTween(  xTo=100, duration=60)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Background]
[name="克丽斯腾"]刚刚那是......女妖的咒言？
[name="娜斯提"]是。
[name="克丽斯腾"]哥伦比亚与卡兹戴尔远隔千里，你走了这么远的路，却将族人的声音刻录下来带在身边，反反复复地聆听？
[name="娜斯提"]怀乡，很难理解？
[name="克丽斯腾"]......不难。但我确实很少见一个人怀乡时表情专注得像在看图纸。
[name="克丽斯腾"]你在试图解读女妖的语言与行为模式，为什么？为了寻找一条足以改变整个族群数千年来生存困境的新路径？
[name="娜斯提"]你......
[name="娜斯提"]我没那么自命不凡。
[name="娜斯提"]我只是，希望能让一个爱操心的家伙余生不那么有负担。
[name="克丽斯腾"]理解，虽然听起来是同一件事情。
[name="克丽斯腾"]请问有突破了吗？
[name="娜斯提"]我不至于那么急躁。
[name="克丽斯腾"]听起来，你已经把那些录音听过成百上千遍......
[name="娜斯提"]......
[name="克丽斯腾"]老是泡在同一个语料库里，直到溺死，也发明不出一种新的语言。
[name="克丽斯腾"]目光与思维的局限会让我们溺死在“常识”里，然后一切都将变成所谓的“命运”......
[name="克丽斯腾"]我以为你正是意识到了这一点，才离开卡兹戴尔的。
[name="克丽斯腾"]删除那些录音......一个残忍的建议。
[name="娜斯提"]很合理。
[name="克丽斯腾"]你好，我叫克丽斯腾，莱茵生命的总辖。
[name="娜斯提"]娜斯提。
[name="克丽斯腾"]斯特莱建筑公司新招的天才工程师，只需要旁人三分之一的时间便能完成工程的女妖，业内人都在传你的图纸上附着了巫术......
[name="克丽斯腾"]莱茵生命正在筹建工程科，或许你会有兴趣？
[name="娜斯提"]我昨天无意中听到了你和老板聊天......“莱茵生命”，是一家涉及生物技术的科技公司？
[name="克丽斯腾"]娜斯提，抬头......看见那些羽兽和它们背后的晨星了吗？
[name="克丽斯腾"]我只是在寻找一种能让我们突破天空的力量。
[name="娜斯提"]天空......
[name="娜斯提"]正如你刚刚的建议，如果要做成的事情已经超越常识，你需要的力量或许也并不来自我们身边......
[name="娜斯提"]莱茵生命更应该筹建的是科考科。
[name="克丽斯腾"]很合理。我可以将这视作工程科主任给公司的第一条建议？
[Dialog]
[stopmusic(fadetime=2)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=0.7, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot="m",name="avg_4212_nasti_1#9$1")]
[Background(image="68_g5_floatingstation",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="娜斯提"]......
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2046_1#1$1")]
[name="协会成员"]娜斯提女士？
[charslot(slot="m",name="avg_4212_nasti_1#1$1")]
[name="娜斯提"]我以为你们会直接把我押去听证会的现场，或者其他更隐秘的监狱......而我们此刻却在索道站等缆车，看起来接下来是要参观浮空层？
[charslot(slot="m",name="avg_npc_2046_1#1$1")]
[name="协会成员"]想见你的那个人，确实是这样安排的。
[charslot(slot="m",name="avg_4212_nasti_1#1$1")]
[name="娜斯提"]......
[Dialog]
[charslot]
[playsound(key="$d_avg_cablecar_loop", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2)]
[delay(time=1.5)]
[playsound(key="$d_avg_cablecar_arrive")]
[delay(time=0.5)]
[charslot(slot="m",name="avg_4151_tinman_1#1$1",duration=1)]
[delay(time=1.5)]
[name="锡人"]好久不见，娜斯提。
[charslot(slot="m",name="avg_4212_nasti_1#1$1")]
[name="娜斯提"]......原来是你。
[charslot(slot="m",name="avg_4151_tinman_1#1$1")]
[name="锡人"]我刚到没多久，这里真是个好地方啊。我还差一半没有逛完，陪我一起？
[charslot(slot="m",name="avg_4212_nasti_1#1$1")]
[name="娜斯提"]也好。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[delay(time=1)]
[Background(image="68_g6_floatinglabmodule",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4212_nasti_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_4151_tinman_1#10$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_4151_tinman_1#10$1",focus="r")]
[name="锡人"]......为什么只有我们刚刚穿过的区域在下雨？
[charslot(slot = "left", name = "avg_4212_nasti_1#1$1",focus="l")]
[name="娜斯提"]云端影棚。蓝卡坞开发了一套实时天空塑景系统，再等五分钟，你甚至可以看到极光。
[charslot(slot = "right", name = "avg_4151_tinman_1#1$1",focus="r")]
[name="锡人"]一百年前，那个被如今的人称作摄影之父的家伙在片场跟我感慨，说什么时候真的能在天上拍电影就好了......
[name="锡人"]“天空热”还真的推动了电影技术革命啊。
[name="锡人"]这里真热闹，娜斯提。我自认为早就对生活的日新月异习以为常，此刻也不得不感慨哥伦比亚人的创造力。
[charslot(slot = "left", name = "avg_4212_nasti_1#1$1",focus="l")]
[name="娜斯提"]很难想象此时此刻你还有这样的闲情逸致。
[name="娜斯提"]按照特区政府专为“螺旋桨天堂”制定的管理法案，紧急事件发生后的十二小时内，相关部门必须召开听证会，处理并公示调查结果。
[name="娜斯提"]高登闯入莱茵的生态园，破坏了我们的在研项目，顺带着把他那些见不得光的生意暴露在了世人面前。
[name="娜斯提"]整件事情的证据链条完整且详实，你们很快来到了园区，却一直在推迟召开听证会......
[charslot(slot = "right", name = "avg_4151_tinman_1#1$1",focus="r")]
[name="锡人"]这可不是拖延，娜斯提。
[name="锡人"]两年前，哥伦比亚人绝不会想到自己有一天会和天上的云争抢居住权。可如今呢？
[name="锡人"]“螺旋桨天堂”已经成为整个哥伦比亚最受关注的存在，特殊地块备案名录里，它的名字被挪到了第一页。
[name="锡人"]花上一点时间，坐缆车兜上一圈，看看身边的这些设施，看看堵在注册中心门口的公司代表们......
[name="锡人"]这所有的一切已经告诉了我们，听证会需要给出怎样的结论，不是吗？
[charslot(slot = "left", name = "avg_4212_nasti_1#1$1",focus="l")]
[name="娜斯提"]......
[charslot(slot = "right", name = "avg_4151_tinman_1#1$1",focus="r")]
[name="锡人"]“螺旋桨天堂”，啧，听听，“天堂”代表扶摇直上的狂热野心，而“螺旋桨”的意思也很明确——绝不能停下来。
[name="锡人"]走私网络曝光，总长官牵头，涉及近百家入驻企业，园区这半年的科研工作存在大量违规......一旦彻查，接下来的展会便不得不叫停。
[name="锡人"]你说得没错，娜斯提，听证会必须召开，这段时间的所有意外都必须要有一个交代——
[charslot(slot = "

... (全文19990字符)
```

### level_act47side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_cellroomB",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[playsound(key="$d_avg_femalecommentator")]
[name="园区广播"]请各位公司代表和体验员注意，“螺旋桨天堂”将在两小时后与特区接驳。
[name="园区广播"]进入城际网络的覆盖范围之后，园区直播将自行开启，请各位将展品调试至最佳状态，“天空生活展会”即将开幕！
[Dialog]
[charslot(slot = "left", name = "avg_4214_cairn_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1000_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right",focus="r",posfrom = "0,0", posto = "50,0",duration=0.3)]
[name="奥克里"]快看，那是塔山生物科技的鳞兽飞艇！听说他们在最后关头做了不少改造，材质的耐热性有很大提升。
[multiline(name="奥克里")]还有太阳能浮空厨房套组！哪怕在星荚之外依旧能有源源不断的动力，看宣传资料的时候我就好奇了......
[Dialog]
[playsound(key="$d_avg_headknock")]
[charslot(slot ="r", action="shake", power=20, times=10, duration=0.1, block=true)]
[charslot(slot = "right", name = "avg_npc_1000_1#1$1",focus="r")]
[multiline(name="奥克里")]哎哟！
[Dialog]
[charslot(slot = "right",focus="r",posfrom = "50,0", posto = "0,0",duration=0.5)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_4214_cairn_1#1$1",focus="l")]
[name="费尔南"]还好只是撞到窗户的栏杆，不是整个头卡进去。
[charslot(slot = "right", name = "avg_npc_1000_1#1$1",focus="r")]
[name="奥克里"]展会马上就要开始了，你一点都不着急？
[charslot(slot = "left", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]放心，专业人士早就想好整套越狱方案了，等时机一到我就带你逃出去。
[charslot]
[stopmusic(fadetime=2)]
[name="？？？"]就这么想出去？
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_901_1#1$1",duration=1)]
[delay(time=2)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1000_1#3$1")]
[name="奥克里"]不、不想......长官我们哪敢啊！
[charslot(slot="m",name="avg_npc_901_1#1$1")]
[name="园区警卫"]行了，我只是来给你们送东西的。
[Dialog]
[playsound(key="$d_avg_paper1")]
[delay(time=1)]
[charslot(slot="m",name="avg_4214_cairn_1#4$1")]
[name="费尔南"]......
[charslot(slot="m",name="avg_npc_1000_1#3$1")]
[name="奥克里"]好厚一沓，这是案卷和审批表？追责对象是——费尔南·伯恩？
[charslot(slot="m",name="avg_4214_cairn_1#6$1")]
[name="费尔南"]损害公共财产、窃取文物、私闯禁区、冒充讲解员......一个小小的独立导游，值得你们把她五年的从业经历全部翻遍？
[charslot(slot="m",name="avg_npc_901_1#1$1")]
[name="园区警卫"]只差一个签名，你下半辈子就要在监狱里给人讲解手铐和脚镣了。
[charslot(slot="m",name="avg_4214_cairn_1#8$1")]
[name="费尔南"]你们想怎么样？
[charslot(slot="m",name="avg_npc_901_1#1$1")]
[name="园区警卫"]展会很快就要开始了，演播室的人手不够。我们不可能把园区仅有的两名讲解员锁在屋子里，暴殄天物，耽误所有后续进程。
[name="园区警卫"]但你的前科太多，又跟娜斯提有关联。
[charslot(slot="m",name="avg_4214_cairn_1#8$1")]
[name="费尔南"]所以你们决定威胁我？
[charslot(slot="m",name="avg_npc_901_1#1$1")]
[name="园区警卫"]只要你安分守己，这也是一个把罪名一笔勾销的机会。
[charslot(slot="m",name="avg_4214_cairn_1#8$1")]
[name="费尔南"]看来我没有选择。
[charslot(slot="m",name="avg_npc_901_1#1$1")]
[name="园区警卫"]感谢古斯塔夫先生吧，是他向梅兰德应急管理监督协会提议，你们才能有幸参加这场划时代的展会。
[name="园区警卫"]广播你们也听到了，在园区地块驶入直播所需的城际网络覆盖范围内之前，你们必须做好向每个哥伦比亚人介绍未来的准备。
[charslot(slot="m",name="avg_4214_cairn_1#7$1")]
[name="费尔南"]我明白了，我会完成演播室的所有工作，在展会结束前我们不会离开园区。
[charslot(slot="m",name="avg_npc_901_1#1$1")]
[name="园区警卫"]很好。
[name="园区警卫"]两个人都给我出来，该干活了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="38_g2_colombiaoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_897_1#1$1",duration=1)]
[delay(time=2)]
[name="杰克逊"]“谨代表莱塔尼亚全体人民，对‘螺旋桨天堂’实验园区即将举办的‘天空生活展会’，致以最诚挚的祝贺。”
[name="杰克逊"]猜猜落款是什么？
[charslot]
[name="？？？"]金律的领奏人，九区的守护者......总之是带着那一串您与我都念不明白的头衔的——
[name="？？？"]女皇本人。
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]老梅兰德生前总说敏锐的政治嗅觉能伴人终生，看来不假。
[name="杰克逊"]雅拉女士。
[charslot]
[Dialog]
[playsound(key="$d_avg_highheelfts")]
[charslot(slot="m",name="avg_npc_1840_1#1$1",duration=1.5)]
[delay(time=2)]
[name="雅拉"]我还是更希望伴我终生的是对葡萄酒的敏锐嗅觉。
[charslot(slot="m",name="avg_npc_897_1#7$1")]
[name="杰克逊"]拉特兰筹备了半个世纪之久的“万国峰会”，堪称泰拉近两百年最大规模的外交活动，莱塔尼亚只去了几个无关紧要的公爵。
[name="杰克逊"]而一场小小的“天空生活展会”，却能让女皇亲笔来函祝贺......
[Dialog]
[playsound(key="$doorknockquite")]
[charslot(slot = "m", focus = "n")]
[delay(time=1.5)]
[name="副总统秘书"]副总统先生，“螺旋桨天堂”送来了礼物，一簇以大总统先生为原型的特制气球，大部分已经装饰在走廊上了。
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]谢谢你，帕瓦尔。
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="雅拉"]或许您可以回赠女皇一只这样的气球？
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]然后让金律法卫和高塔术师花上三天把它细细拆成橡胶渣？
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="雅拉"]它看起来只是个普通的装饰气球。
[charslot(slot="m",name="avg_npc_897_1#2$1")]
[name="杰克逊"]恐怕从女皇亲笔来函的那一刻起，就不是了。它会“变成”最尖端的军事科技产物——可以伪装成气球飘入别国领空的航空炸弹。
[charslot(slot="m",name="avg_npc_1840_1#4$1")]
[name="雅拉"]这样规格的贺函，您已经收到了多少？
[charslot(slot="m",name="avg_npc_897_1#7$1")]
[name="杰克逊"]维多利亚的大公爵、乌萨斯的议长、卡西米尔的大骑士长......恐怕我的手指要不够用了。
[name="杰克逊"]上一任副总统为边境移民和关税政策发愁了四年，可我这四年，发愁的都是些什么事？
[name="杰克逊"]永不陷落的城市被攻占，恒常不变的天空被撕破，沉寂已久的海洋也开始发声。
[name="杰克逊"]这些事之后，核心圈的所有国家都不约而同地进入了那套“只有航空炸弹，没有气球”的语境当中。
[name="杰克逊"]而我们呢？
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]哦，我们这只气球甚至飞不起来。
[charslot(slot = "m", focus = "n")]
[name="副总统秘书"]这批气球在送来之前，里面易燃的氢气已经被换成了普通的空气......出于安全考虑。
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]多安全啊，哥伦比亚。
[charslot(slot="m",name="avg_npc_1840_1#3$1")]
[name="雅拉"]听起来，这已经是关乎国家安全的重要话题了，您却偏偏选择与我这样一位退休了的老妇人来聊......
[name="雅拉"]还选在进步大厦，整个特区最好的会客厅？
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]很难想象退休与否会让雅拉·布克·威尔森变得有什么不同。
[name="杰克逊"]不论是对曾在永夜里燃烧的“晨星”，还是对莱茵生命的前任人力资源科主任，这都谈不上是像样的招待。
[name="杰克逊"]这个时代，比起某种政见、某些承诺，人们似乎更愿意被一段传奇、一个奇迹所感召。
[name="杰克逊"]哪怕我们最为理智的议员，也是如此。
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="雅拉"]如果是为了我和韦恩议员的那几次会面，我相信您之前已经表示过谢意了......用您从谢拉格带回的那些特色纪念品。
[charslot(slot="m",name="avg_npc_897_1#1$1")]
[name="杰克逊"]那只是我个人的谢意，况且，我后来才意识到，那些驻扎在观测站的莱茵科学家们应该早就送过你同样的东西。
[name="杰克逊"]如果你出面，能让正确的人有机会把哥伦比亚气球里的空气换回氢气，那么想要对你表达谢意的，肯定不止我一人。
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="雅拉"]依我的常识，如果给气球换气也分“正确的人”，那只会是制造气球的人。
[name="雅拉"]为了他们，我已经出面过不少次了。
[name="雅拉"]科研工作者总是真挚得像一群孩子，我也总是最

... (全文13583字符)
```

### level_act47side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="68_g6_floatinglabmodule",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_2046_1#1$1",posfrom = "-150,0", posto = "0,0",duration = 0.8)]
[charslot(slot = "right", name = "avg_npc_2046_1#1$1",posfrom = "150,0", posto = "0,0",duration = 0.8)]
[Delay(time=1.5)]
[charslot(slot = "left",focus="l")]
[name="特工A"]第三浮空平台第二次巡逻，目标舱室就位，暂未发现可疑人员。
[name="特工A"]除了我们，这个小型浮空平台已经没有人了，你那边呢？
[charslot(slot = "r",focus="r")]
[name="特工B"]四个舱室的引擎系统都进行了断点测试，就等园区开进城际网络的覆盖范围。
[charslot(slot = "left",focus="l")]
[name="特工A"]记得对外统一口径，将人员聚集到地面是暂时的，直播的展品概览环节结束后就能返回各自的展区。
[charslot(slot = "r",focus="r")]
[name="特工B"]明白。
[Dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_metalroll",volume=0.5)]
[Delay(time=1.5)]
[charslot(slot = "r",focus="r")]
[name="特工B"]你确定没人？锡人长官强调过，必须确认园区人员全部安全撤离后，才能发送行动信号。
[charslot(slot = "left",focus="l")]
[name="特工A"]主干通路一小时前已经封死，辅助平台的应急跳台全部关闭，索道站的缆车昨晚就改成了单向通行，没人上得来。
[charslot(slot = "r",focus="r")]
[name="特工B"]保险起见......
[Dialog]
[charslot(slot = "right",posfrom = "0,0", posto = "100,0",duration = 1)]
[Delay(time=1)]
[playsound(key="$transmission")]
[Delay(time=1.5)]
[charslot(slot = "m", focus = "n")]
[name="通讯音"]......索道站需要支援，莱茵的那个助理研究员带着一群体验员把通行枢纽堵住了，很难缠......
[charslot(slot = "left",focus="l")]
[name="特工A"]啧，先去支援。计划的时间节点非常重要，一定要赶在直播前完成所有布置。
[charslot(slot = "r",focus="r")]
[name="特工B"]那刚刚的动静......
[charslot(slot = "left",focus="l")]
[name="特工A"]喏，你看。
[charslot(slot = "r",focus="r")]
[name="特工B"]汽水瓶盖？
[charslot(slot = "left",focus="l")]
[name="特工A"]估计是浮空舱不稳，瓶盖从桌子上滚下来了。应该没什么事，走吧。
[Dialog]
[playsound(key="$d_avg_walkfast",volume=0.4)]
[playsound(key="$d_avg_walkfast",volume=0.8,delay=0.3,channel="b")]
[charslot(slot = "left",posfrom = "0,0", posto = "-150,0",duration = 0.8,afrom=1,ato=0)]
[Delay(time=0.5)]
[charslot(slot = "right",posfrom = "100,0", posto = "-150,0",duration = 1.2,afrom=1,ato=0)]
[Delay(time=2.5)]
[charslot]
[playsound(key="$d_avg_clothmovement")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[charslot(slot = "left", name = "avg_4214_cairn_1#10$1",posfrom = "0,-80", posto = "0,0",duration = 0.8)]
[charslot(slot = "right", name = "avg_npc_2041_1#1$1",posfrom = "0,-80", posto = "0,0",duration = 0.8)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_4214_cairn_1#10$1",focus="l")]
[name="费尔南"]呼......雅、雅斯彭先生......
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot = "left", name = "avg_4214_cairn_1#6$1",focus="l")]
[name="费尔南"]你到底对那只气球有什么执念啊！沙发里就那点地方，你还要护着气球，我都要被挤死啦！
[charslot(slot = "right", name = "avg_npc_2041_1#2$1",focus="r")]
[name="雅斯彭"]不好意思，费尔南小姐......但我就是为了这点执念，才求你带我来这儿的......
[charslot(slot = "left", name = "avg_4214_cairn_1#6$1",focus="l")]
[name="费尔南"]从他们眼皮子底下开溜，又把你带过来，可是费了我好大的力气！
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]实在不好意思......能帮我递一下柜子里的工具箱吗？撤离的通知来得太突然，我还没来得及确认浮空舱不会在直播里出现任何问题......
[charslot(slot = "left", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]你就那么想让“幸运瘤兽”在展会上亮相？
[name="费尔南"]不顾听证会公示的结果，跟一个有多项前科的导游临时签约，还帮她从园区警卫的监视下逃走，只为了让她带你回到封锁的浮空层......
[name="费尔南"]你们这帮人啊，对天空真的是太狂热了！
[charslot(slot = "right", name = "avg_npc_2041_1#1$1",focus="r")]
[name="雅斯彭"]我背负的债款可是天文数字。只有“幸运瘤兽”在展会上亮相，拉来投资，我才能有一线生机。
[charslot(slot = "left", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]知道知道，“天空会给所有向往未来的人一个答案”嘛，“螺旋桨天堂”的宣传标语，就连贫民窟的垃圾桶盖上都能看到。
[charslot(slot = "right", name = "avg_npc_2041_1#1$1",focus="r")]
[name="雅斯彭"]就算是盲信，我也走到了这一步，绝不会现在放手。
[Dialog]
[playsound(key="$d_avg_guitartap",volume=0.8)]
[playsound(key="$d_avg_guitartap",volume=0.8,channel="2",delay=0.3)]
[Delay(time=1)]
[charslot(slot = "right", name = "avg_npc_2041_1#3$1",focus="r")]
[name="雅斯彭"]呼......元件没有任何问题，可以撑到展会结束。走吧。
[Dialog]
[playsound(key="$d_avg_doorknob")]
[charslot(slot = "right",posfrom = "0,0", posto = "20,0",duration = 0.3,isblock=true)]
[charslot(slot = "right",posfrom = "20,0", posto = "0,0",duration = 0.3,block=true)]
[Delay(time=0.5)]
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]门怎么锁上了？
[charslot(slot = "left", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]等等，你有没有听到什么声音？
[Dialog]
[playsound(key="$d_avg_devicebeep", loop=true, channel="bgs",volume=0.7)]
[charslot(slot = "m", focus = "n")]
[Delay(time=2)]
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]听到了......难道我的产品真出了什么问题？
[charslot(slot = "left", name = "avg_4214_cairn_1#9$1",focus="l")]
[name="费尔南"]不，不是从展示柜传来的，是从——
[charslot(slot = "left", name = "avg_4214_cairn_1#5$1",focus="l")]
[name="费尔南"]我们脚下？
[stopmusic(fadetime=2)]
[Dialog]
[StopSound(channel="bgs", fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[Background(image="68_g5_floatingstation",screenadapt="coverall",xScale=1.05, yScale=1.05,y=15)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="急切的公司代表"]啧，前面怎么一动不动啊？再拖下去，直播都要开始了！
[name="好奇的体验员"]别着急，梅兰德的人好像过来处理了......有个人被他们围起来了，看制服样式像是莱茵的研究员？
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$formal_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_2039_1#12$1",duration=0.5)]
[delay(time=1)]
[name="斯凯"]请让我过去！装置树的硬盘和主板还没拆——
[charslot(slot="m",name="avg_npc_2046_1#1$1")]
[name="协会成员"]得寸进尺！
[name="协会成员"]让装置树参与展会已经是各方能为莱茵做出的最大让步，而且都大发慈悲允许你们拷走数据用于后续研究了，你还想提要求？
[charslot(slot="m",name="avg_npc_2039_1#10$1")]
[name="斯凯"]只要五

... (全文17343字符)
```

### level_act47side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="68_g4_floatingplatform",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_2046_1#1$1",posfrom = "0,0", posto = "0,0",duration = 0.8)]
[charslot(slot = "right", name = "avg_npc_2046_1#1$1",posfrom = "0,0", posto = "0,0",duration = 0.8)]
[delay(time=1.5)]
[charslot(slot = "left",focus="l")]
[name="特工A"]怎么回事，干扰器和备用引爆器都没起作用？
[charslot(slot = "r",focus="r")]
[name="特工B"]根据回传的信号，所有装置都已启动，九个目标舱室的核心引擎已经停止运作。
[name="特工B"]但不知道为什么，接收到的信号异常混乱，没有安装发信器的舱室也在发送信号......
[charslot(slot = "left",focus="l")]
[name="特工A"]派一组人去调查事故原因，清除一阶段行动时留下的所有安装痕迹，回收发信器。
[charslot(slot = "r",focus="r")]
[name="特工B"]队长......那相当于宣告行动失败。
[charslot(slot = "left",focus="l")]
[name="特工A"]忘了梅兰德的准则了吗？实际情况与计划发生重大偏差时，立即停止行动。我们可不是蓝卡坞谍战片里逞英雄的主角。
[Dialog]
[playsound(key="$d_avg_walkfast")]
[charslot(slot = "r",afrom=1,ato=0,duration=1,posfrom = "0,0", posto = "150,0")]
[Delay(time=2)]
[playsound(key="$d_gen_transmissionget")]
[interlude(maskid = "group_interclude_vertical_common" ,size = "290,760", style=0 , offset = "200,0" ,channel = 3,tsfrom = "0,1", tsto="1,1",tsduration = 0.5)]
[interlude(channel = 3, type = 3, slot = "r", pfrom = "190,0", pto="190,0", name = "avg_4151_tinman_1#1$1",duration = 0.5)]
[interlude(channel = 3, type = 3, slot = "r", switch = true)]
[Delay(time=1)]
[charslot(slot="m",focus="n")]
[name="锡人"]看来你对卖座的商业电影有些偏见。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l")]
[name="特工A"]我们没有重拍的机会。
[interlude(channel = 3, type = 3, slot = "m", switch = true)]
[charslot(slot = "m", focus = "n")]
[name="锡人"]并非别无选择。
[name="锡人"]不用派人检查目标舱室了，应该是女妖的咒言控制了那些本应下坠的“玩具”。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l")]
[name="特工A"]可娜斯提应该在监狱里。
[interlude(channel = 3, type = 3, slot = "m", switch = true)]
[charslot(slot = "m", focus = "n")]
[name="锡人"]我说的女妖不是她。
[name="锡人"]现在浮空层设施的连接方式受咒言影响发生了本质性的改变，接收器报点错乱恰好印证了这一点。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l")]
[name="特工A"]......浮空层的供能管路结构可以被咒言连通，发送电信号并同步指令？简直是天方夜谭。
[interlude(channel = 3, type = 3, slot = "m", switch = true)]
[charslot(slot = "m", focus = "n")]
[name="锡人"]整座园区的管路和系统都是娜斯提一手设计，她能成为莱茵十杰之一，靠的可不仅仅是工程学上的天赋。
[name="锡人"]不过，借用现在的上层供能网络，只要引爆一处引擎，就能使整个浮空层坠落。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l")]
[name="特工A"]整、整个浮空层......
[name="特工A"]您的意思是......
[interlude(channel = 3, type = 3, slot = "m", switch = true)]
[charslot(slot = "m", focus = "n")]
[name="锡人"]二十五分钟后，园区将与特区接驳。我们应该在那一刻，为“螺旋桨天堂”献上一支倒放的礼花。
[name="锡人"]改变原定计划。上层负责调集人手，把浮空层外围的辅助平台也连上通用供能管路；下层负责测算坠落点，随时准备疏散人群。
[name="锡人"]我会通知古斯塔夫，让行政部的人手配合工作，推迟开幕致辞的时间。
[name="锡人"]另外，派人去监狱确认娜斯提的动向，在电梯广场以及任何可攀援的通路上安排至少三支精英小队，她重返浮空层只是时间问题。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l")]
[name="特工A"]您不参与？
[interlude(channel = 3, type = 3, slot = "m", switch = true)]
[charslot(slot = "m", focus = "n")]
[name="锡人"]啊，我一会儿要督导我的后辈，你知道梅兰德特工的考评制度，很麻烦的。等我结束后，很快跟你们会合。
[name="锡人"]各小组，行动。
[interlude(channel = 3, clear = true,tsto="0,1",tsduration=0.5)]
[Dialog]
[playsound(key="$transmission")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="68_g7_airrestaurant",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",duration = 1)]
[delay(time=1.5)]
[name="高登"]......
[charslot(slot = "m", focus = "n")]
一块巨大的直播屏悬吊在云中餐厅，鲜亮浮夸的公司商标和新奇的浮空装置在屏上不断切换，奥克里激昂的声音从音响里传来。
屏幕左下角，是驾驶中控室传来的实时图像，定位地图上代表“螺旋桨天堂”的小红点，正闪烁着朝特区进发。
云朵般的绒毯上架着两台摄像机，对准了一把孤零零的椅子——像是等待着高登的被告席。
[Dialog]
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",focus="l")]
[name="古斯塔夫"]你迟到了。 
[charslot(slot = "l", name = "avg_npc_2042_1#8$1",focus="l")]
[name="古斯塔夫"]......怎么穿成这样就来了？二十分钟后就要开幕致辞了，没时间给你准备套新衣服。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]管理局配发的制服领带太紧，勒得慌。
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",focus="l")]
[name="古斯塔夫"]呵，六年前你在管理局转正、领到新制服时，我亲自为你整装。那时你看起来高兴得发疯。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]当时你告诉我，为了能配得上那身制服，我要学的还有很多，之后我就在最基础的岗位上待了六年。
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",focus="l")]
[name="古斯塔夫"]没有一个新人最先精通的是检讨书的写法，我不是没有后悔过为你整装。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]那现在呢？
[charslot(slot = "r", name = "avg_4213_skybx_1#7$1",focus="r")]
[name="高登"]“螺旋桨天堂”事故责任人的这件衣服，又是谁给我披上的？
[charslot(slot = "l", name = "avg_npc_2042_1#6$1",focus="l")]
[name="古斯塔夫"]哦，你发现了？
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]走私暴露当晚，我的两箱货物被你扣下，原以为你是为了帮我处理赃物，但刚才我发现它们出现在了你和梅兰德的人手里。
[name="高登"]长官，这篇用来谢罪的演讲稿，恐怕也不是那个晚上写好的吧？
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",focus="l")]
[name="古斯塔夫"]接着说。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]我从哥伦比亚之外引进源石装置显然不符合管理局的规定，但凡其安全性出了问题，我就会成为整座园区的罪人。
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",focus="l")]
[name="古斯塔夫"]所以你依旧觉得这是我们之间的私人恩怨？
[charslot(slot = "r", name = "avg_4213_skybx_1#7$1",focus="r")]
[name="高登"]难道不是吗？在你眼里，我一直都是从贫民窟出来的混混，不守规矩也没有教养。现在我靠自己的努力平步青云，你更看不过眼......
[charslot(slot = "l", name = "avg_npc_2042_1#3$1",focus="l")]
[name="古斯塔夫"]靠自己？你认为一个背过处分、有上百份检讨书留档的废物，真能靠自己调职到炙手可热的浮空实验园区？
[charslot(slot = "r", name = "avg_4213_skybx_1#5$1",focus="r")]
[name="高登"]什么......？
[charslot(slot = "l", name = "avg_npc_2042_1#1$1",focus="l")]
[name="古斯塔夫"]真让我失望，你对现状的洞察依旧如此浅薄。
[name="古斯塔夫"]从你踏进“螺旋桨天堂”开始，你的头衔、你的投资、你的所有业绩和成果，都是我“送”给你的。
[name="古斯塔夫"]高登·谭农，你是不是从来没想过，自己为什

... (全文27817字符)
```

### level_act47side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="68_g5_floatingstation",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_2047_1#1$1",posfrom = "0,0", posto = "0,0",duration = 0.8)]
[charslot(slot = "l", name = "avg_npc_2046_1#1$1",posfrom = "0,0", posto = "0,0",duration = 0.8)]
[delay(time=1.5)]
[charslot(slot = "r",focus="r")]
[name="资深特工"]汇报情况。
[charslot(slot = "l",focus="l")]
[name="特工"]浮空层所有舱室都已连入爆破网络，下层人员正在疏散广场上的民众。
[name="特工"]人们对展会的热情很高，还需要再耗费一些时间，但不会耽误计划。
[name="特工"]只要“螺旋桨天堂”与特区接驳，就可以引爆整个浮空层。
[charslot(slot = "r",focus="r")]
[name="资深特工"]莱茵的人没动静了？
[charslot(slot = "l",focus="l")]
[name="特工"]已经收押了二十三名相关人员，还有十几名在浮空平台流窜。
[name="特工"]八处制高点已被我们控制，这些人一味在展品区和各个索道站进出，身上除了普通检修工具之外没携带莱茵制造的特殊设备。
[charslot(slot = "r",focus="r")]
[name="资深特工"]没有后手，只想捉迷藏？
[name="资深特工"]继续盯着，他们不知道梅兰德的详细计划，也没有联络手段，就算想在最后关头反扑也无济于事。
[charslot(slot = "l",focus="l")]
[name="特工"]是。
[charslot]
从索道站的候客区眺望，麦克斯特区的外轮廓映入眼帘，哥伦比亚最繁华的移动城市已经越来越近。
自进入园区以来，特工们从未好好端详过它的样貌，极高的能见度让浮空层所有奇异精巧的设施格外明亮鲜活。
成片的吊舱如水生生物般轻盈地飘浮着，浮空种植单元被有序地安插在各个小型平台之间，形成供能网络，支撑着整个浮空层......
[charslot(slot = "r",focus="r", name = "avg_npc_2047_1#1$1")]
[charslot(slot = "l",focus="r", name = "avg_npc_2046_1#1$1")]
[name="资深特工"]等等......你刚刚说莱茵的人出现在哪里？
[charslot(slot = "l",focus="l")]
[name="特工"]展品区和索道站。
[charslot(slot = "r",focus="r")]
[name="资深特工"]给我看看具体位置。
[Dialog]
[charslot(slot = "left",focus="all")]
[playsound(key="$d_avg_paper1")]
[delay(time=1.5)]
[charslot(slot = "r",focus="r")]
[name="资深特工"]把那些人的动线汇总在一起看，他们既没法到达莱茵那棵“树”的平台，也没法前往其他公司的浮空舱......
[name="资深特工"]还是说，他们压根就不是为了夺回自己的地盘？！
[name="资深特工"]可莱茵的人也好，那些体验员和公司代表也好，他们明明只是像没头苍蝇一样在乱转......
[name="资深特工"]这有什么意义呢？
[charslot(slot = "m", focus = "n")]
特工瞥了一眼最近的种植单元，毫不起眼的莱茵造物静默地挺立着。
他才发现，这些小玩意边缘的防撞灯在白天也十分耀眼，而且，它们已经不规则地闪烁了很久。
[Dialog]
[playsound(key="$phonevibration")]
[delay(time=1.5)]
[charslot(slot = "l",focus="l")]
[name="特工"]侦察员报告，莱茵的人全部从视野里消失了！
[charslot(slot = "r",focus="r")]
[name="资深特工"]不、不是消失！
[name="资深特工"]他们应该是去往了同一个地方......他们的行动是有规律的！
[name="资深特工"]所有人听好，破坏沿途看见的所有种植单元——这些莱茵的玩意不是什么摆件，那些人在拿它们当通讯工具！
[name="资深特工"]截断展品区和索道站之间的所有通路，找出每一个和我们捉迷藏的家伙，找到他们的目的地！
[name="资深特工"]这些家伙，到底想干什么......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="68_g6_floatinglabmodule",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4214_cairn_1#4$1",duration = 0.5)]
[charslot(slot = "right", name = "avg_npc_2041_1#1$1",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]费尔南小姐，你从刚刚开始就一直看着窗外。
[charslot(slot = "left", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]你说自己有个必须赌赢的理由。
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]是的。
[charslot(slot = "left", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]而我也正身处一场赌局之中。
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]从你的态度和我们刚刚自由落体的经历里，我大概能猜到园区里正发生着什么。
[name="雅斯彭"]你不会无缘无故地陪我冒这么大的风险，不过很遗憾，我已经没有什么东西能和你交易了，除了——
[charslot(slot = "left", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]唔......
[charslot(slot = "right", name = "avg_npc_2041_1#5$1",focus="r")]
[name="雅斯彭"]你想要“幸运瘤兽”？
[charslot(slot = "left", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]也可以这么说。
[name="费尔南"]我想要的是高登·谭农卖给你的违禁品。
[Dialog]
[MusicVolume(volume=0.4, fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="29_g11_monitoringroom",screenadapt="coverall")]
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1")]
[charslot(slot = "l", name = "avg_4214_cairn_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4214_cairn_1#1$1",focus="l")]
[name="费尔南"]不去准备自己的演讲，反倒来演播室给我添麻烦？你的脸皮不薄啊，高登长官。
[charslot(slot = "r", name = "avg_4213_skybx_1#3$1",focus="r")]
[name="高登"]要是和每个与我交恶的人都断绝合作的可能，我活不到现在。
[charslot(slot = "l", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]合作？爱莫能助。
[name="费尔南"]梅兰德的人搜集了我从业以来的所有违法记录，我不想下辈子只能给人讲解牢饭有多好吃。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]你不是安分的人，而且我要谈的合作就与梅兰德有关。
[name="高登"]这里是最能看清园区动向的地方，奥克里正在兴头上没看出来也就罢了，我不信你没发现异常。
[charslot(slot = "l", name = "avg_4214_cairn_1#4$1",focus="l")]
[name="费尔南"]非要说的话......
[name="费尔南"]浮空层的直播画面切得太频繁，设备调试更像是个借口；广场上至少有十个我没见过的体验员，他们不像是在闲逛，倒像是在巡逻。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]就像提前得知危险即将降临。
[charslot(slot = "l", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]又想骗我参与阴谋？
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]园区即将遭遇一场有预谋的事故，这是事实；我不允许古斯塔夫把“螺旋桨天堂”变成千万哥伦比亚人口中的笑话，也是事实。
[name="高登"]十秒，合作与否，给我一个答复。
[charslot(slot = "l", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]成功概率有多大？
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]一成。
[charslot(slot = "l", name = "avg_4214_cairn_1#5$1",focus="l")]
[name="费尔南"]不像是你会下注的赌局啊。
[charslot(slot = "r", name = "avg_4213_skybx_1#4$1",focus="r")]
[name="高登"]如果牌桌对面是那只老狐狸，我必须赌。
[charslot(slot = "l", name = "avg_4214_cairn_1#3$1",focus="l")]
[name="费尔南"]几乎不可能成功的计划......有意思，说说你的打算。
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]我需要你游说尽可能多的人返回浮空层，回收这张名单上的源石制品和施术单元。
[charslot(slot = "l", name = "avg_4214_cairn_1#5$1",focus="l")]
[name="费尔南"]这些......全是你交易出去的违禁品？
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]它们的潜力远不止做展品的心脏。
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]你是想......
[charslot(slot = "r", name = "avg_4213_skybx_1#1$1",focus="r")]
[name="高登"]带着整座园区，逃亡。
[Dialog]
[Blocker(a=1, r=0, 

... (全文47990字符)
```

### level_act47side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="68_g4_floatingplatform",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$act19side_01_intro",key="$act19side_01_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_4214_cairn_1#1$1",duration=0.5)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_gunload", volume=1)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_4214_cairn_1#5$1")]
[delay(time=0.5)]
[charslot(slot = "r",focus="r")]
[name="特工A"]别动。
[charslot(slot = "m", name = "avg_4214_cairn_1#5$1")]
[name="费尔南"]有话好说，有话好说。哎——
[Dialog]
[charslot(slot = "l",posfrom = "200,0", posto = "200,0",duration = 0.5, name = "avg_npc_2046_1#1$1",focus="m")]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4214_cairn_1#9$1")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot ="m", action="shake", power=6, times=20, duration=0.3,focus="m")]
[delay(time=0.5)]
[charslot(slot = "m",afrom = 1, ato = 0,duration = 1,focus="m")]
[delay(time=1.5)]
[charslot(slot = "l",posfrom = "200,0", posto = "0,0",duration =1,focus="l")]
[delay(time=1.5)]
[name="特工A"]所有参与暴动的人员都在这里了。
[Dialog]
[charslot(slot="r",name="avg_npc_2047_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "r",focus="r")]
[name="特工B"]把他们都关进下层监狱，等到了特区送交法庭。
[name="特工B"]快到行动时间了，所有人再检查一遍降落装备，以防不测。
[Dialog]
[charslot]
[playsound(key="$d_avg_erthshkng", loop=true, channel="es", volume=0.7)]
[CameraShake(duration=-1, xstrength=1, ystrength=1, vibrato=30, randomness=90, fadeout=false, block=false)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_npc_2047_1#1$1",focus="r")]
[charslot(slot="l",name="avg_npc_2046_1#1$1",focus="r")]
[name="特工B"]怎么回事！有人提前按了引爆按钮？
[charslot(slot="l",focus="l")]
[name="特工A"]不可能，地块离特区只剩下最后几百米......不对，看远处政府大楼的塔尖大小，我们正在远离特区？
[charslot(slot = "m", focus = "n")]
[name="费尔南"]计划赶不上变化对吗，各位先生？
[charslot(slot="r",focus="r")]
[name="特工B"]......
[name="特工B"]你们从来没想过直接阻止爆炸，只是想拖延时间，让地块完成转向？
[charslot(slot = "m", focus = "n")]
[name="费尔南"]我们没有任何资本跟训练有素的队伍对抗，不是吗？
[charslot(slot="r",focus="r")]
[name="特工B"]......计划赶不上变化吗......
[Dialog]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1.5)]
[name="特工B"]更改任务内容。
[name="特工B"]在下层驻守的特工按照预定路线撤退，上层小队保护身边的平民，准备跳伞。
[name="特工B"]零号点位，引爆。
[Dialog]
[charslot]
[delay(time=1)]
[CameraShake(duration=2, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n", volume=0.7)]
[StopSound(channel="es", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraShake(duration=-1, xstrength=1, ystrength=1, vibrato=30, randomness=90, fadeout=false, block=false)]
[Background(image="68_g1_groundparkstreet_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_npc_1000_1#2$1",duration=0.5)]
[delay(time=1)]
[name="奥克里"]发生了什么！演播室的画面怎么全没了......外面的直播屏还有信号吗？
[charslot(slot = "m", name = "avg_npc_2045_1#1$1")]
[name="体验员"]你还关心直播？没听到监督协会的疏散通知吗？！
[name="体验员"]浮空结构层发生了非常严重的能源事故，不出十分钟，所有的浮空设施都会陆续坠毁！快点躲到应急设施里去！
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2.5)]
[charslot(slot = "m",posfrom = "0,0", posto = "300,0",duration = 1,afrom=1,ato=0)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1000_1#3$1")]
[name="奥克里"]坠毁......？
[charslot(slot = "m", focus = "n")]
奥克里抬头，数百个小型浮空舱在六百米的高空燃起火团，漫天的灰烬封锁了明媚的天空。
失去阳光的照拂，如云朵般轻盈透亮的舱室，又变回了构成它们的沉重金属，旋转着朝园区下层袭来。
[name="？？？"]小心。
[Dialog]
[charslot(slot = "r",duration = 0.3, name = "avg_npc_2044_1#1$1",posfrom = "-50,0", posto = "-50,0")]
[delay(time=0.7)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=0.7)]
[charslot(slot = "r",duration = 0.7, posfrom = "-50,0", posto = "-250,-50",afrom=1,ato=0)]
[charslot(slot = "m",duration = 0.7, posfrom = "0,0", posto = "-200,-50",afrom=1,ato=0)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.7, block=true)]
[charslot]
[PlaySound(key="$d_avg_container_smash", volume=0.7)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1000_1#3$1")]
[charslot(slot = "r", name = "avg_npc_2044_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_npc_1000_1#3$1",focus="l")]
[name="奥克里"]咳咳......好险，谢谢。
[name="奥克里"]嗯？你是哪个科技公司的体验员，我怎么没见过你？
[charslot(slot = "r",focus="r")]
[name="体验员？"]......
[name="体验员？"]现在不是自我介绍的时候，奥克里先生。
[name="体验员？"]街道两边没有太多遮挡物，你会被这些掉下来的碎片砸伤的，尽快躲进应急设施。
[charslot(slot = "l", name = "avg_npc_1000_1#3$1",focus="l")]
[name="奥克里"]好、好......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_snowstormlp", loop=true, channel="fs", volume=0.6)]
下坠。
失控地下坠。
费尔南的心脏狂跳不止，仿佛下一秒就要蹦出胸腔。
她极力控制自己的呼吸。头盔两侧的绑带拍打着她的脸颊，疼痛帮她抵御对坠落的恐惧。
引爆器的信号沿着连通的工程管路，几乎在一瞬间点燃了所有浮空设施，在七号平台彻底失去动力之前，她向地面纵身一跃。
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[bgeffect(name="$eb_smoke_01",layer=1,y=-100)]
[Image(image="68_i12", xScale=1.3, yScale=1.3,screenadapt="coverall",fadetime=0)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=1, block=true)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=1, g=1, b=1, fadetime=1, block=false)]
[CameraShake(duration=1.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=-1, xstrength=1, ystrength=1, vibrato=30, randomness=90, fadeout=false, block=false)]
[PlaySound(key="$d_avg_churchfire", volume=0.4,channel="f", loop=true)]
[playMusic(intro="$Tremont_intro",key="$Tremont_loop", volume=0.6)]
坠落的舱室像是漆黑的流星，嘶鸣着从费尔南的身侧划过。
糖果色的广告颜料被大火燎尽，熔断的柔性钢缆在气流的牵引下飞舞，空气中满是焦油的苦味。
整个浮空层如一只被扎破的气球，在空中依依不舍地摇曳。
“幸运瘤兽”“一只靴子”“沙滩伞”......
费尔南辨认着与自己一同坠落的公司商标

... (全文30090字符)
```

### level_act47side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_wilderness_y",screenadapt="coverall")]
[bgeffect(name="$eb_cnclouds",layer=1)]
[BackgroundTween(image="bg_wilderness_y", duration=8, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.06, yScaleTo=1.06)]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>卡兹戴尔地区，女妖河谷</>
[delay(time=3)]
[animtextclean]
[PlaySound(key="$d_avg_rowboat_lake_loop",loop=true,channel="water",volume=0)]
[SoundVolume(volume=0.6, channel="water",fadetime=2)]
[delay(time=1)]
[name="大拉里"]呜——啊~
[name="老科利"]呀——哈~
[name="小默"]嘿——咻~
[stopsound(channel="water",fadetime=0.5)]
[dialog]
[charslot(slot = "r", name = "avg_4151_tinman_1#1$1", posfrom="50,0",posto="50,0",duration=1.5, isblock=false)]
[charslot(slot = "l", name = "avg_npc_1071_1#1$1", posfrom="-50,0",posto="-50,0",duration=1.5, isblock=true)]
[charslot(slot="l", name = "avg_npc_1071_1#1$1",focus="l")]
[name="菈玛莲"]穿过这片芦苇滩，离栖脚树还有些路途......还是让我来吧？河谷的船由咒言雕琢，也能由咒言驱动，不费什么力气。
[charslot(slot = "r", name = "avg_4151_tinman_1#9$1", focus="r")]
[name="锡人"]没事，这三个家伙还在兴头上，就让他们卖卖力气吧。
[charslot(slot="l", name = "avg_npc_1071_1#1$1",focus="l")]
[name="菈玛莲"]他们比我想象中......有活力得多。
[PlaySound(key="$d_avg_rowboat_lake_loop",loop=true,channel="water",volume=0)]
[SoundVolume(volume=0.6, channel="water",fadetime=2)]
[charslot(slot = "r", name = "avg_4151_tinman_1#9$1", focus="r")]
[name="锡人"]这已经算安静的了。你不会想听他们一边划船，一边比拼哭声高低，或是模仿裂兽嘶吼的。
[charslot(slot = "r", name = "avg_4151_tinman_1#2$1", focus="r")]
[name="锡人"]毕竟在熔炉里不分你我地烧了几百年，难得有了具看得见摸得着的身体，有了个分得清辨得明的身份，换谁都得好好闹腾一番。
[charslot(slot="l", name = "avg_npc_1071_1#8$1",focus="l")]
[name="菈玛莲"]......
[charslot(slot = "r", name = "avg_4151_tinman_1#3$1", focus="r")]
[name="锡人"]......真宁静啊，河谷。
[stopsound(channel="water",fadetime=0.5)]
[charslot(slot="l", name = "avg_npc_1071_1#8$1",focus="l")]
[name="菈玛莲"]嗯？
[charslot(slot = "r", name = "avg_4151_tinman_1#1$1", focus="r")]
[name="锡人"]在哥伦比亚，哪怕是我这样贪图新鲜的家伙，也会有尴尬地站在计程车前，不知道新样式的车门把手该怎么用的时候。
[charslot(slot = "r", name = "avg_4151_tinman_1#8$1", focus="r")]
[name="锡人"]变化和喧嚣是哥伦比亚的常态。永远在拓荒、永远在前进的国度，不会停下来等任何人，哪怕一秒。
[charslot(slot = "r", name = "avg_4151_tinman_1#8$1", focus="r")]
[name="锡人"]但这里......我上次来这里是什么时候？
[PlaySound(key="$d_avg_rowboat_lake_loop",loop=true,channel="water",volume=0)]
[SoundVolume(volume=0.6, channel="water",fadetime=2)]
[charslot(slot="l", name = "avg_npc_1071_1#1$1",focus="l")]
[name="菈玛莲"]两百年前，卡兹戴尔被那场惨烈的战争洗劫之后。那时拂哀菈才刚刚把这片河谷变成女妖的家。
[charslot(slot = "r", name = "avg_4151_tinman_1#8$1", focus="r")]
[name="锡人"]是啊。在被源石犁过不知多少遍的山岭之间，找到这样一方天地，可不容易。
[charslot(slot = "r", name = "avg_4151_tinman_1#9$1", focus="r")]
[name="锡人"]雾湖的水镜、芦苇滩的沉木、为大地铺金毯的林地......还有女妖们摇动船桨、吹起叶哨的声音，轻柔得像是河谷在呼吸。
[stopsound(channel="water",fadetime=0.5)]
[charslot(slot = "r", name = "avg_4151_tinman_1#9$1", focus="r")]
[name="锡人"]这么多年过去，河谷里的一切好像都没有变。
[charslot(slot = "r", name = "avg_4151_tinman_1#8$1", focus="r")]
[name="锡人"]除了......当初摆渡我入谷的那个人。
[charslot(slot="l", name = "avg_npc_1071_1#3$1",focus="l")]
[name="菈玛莲"]拂哀菈。
[charslot(slot = "r", name = "avg_4151_tinman_1#8$1", focus="r")]
[name="锡人"]拂哀菈，我的老友，她已经搬进栖脚树下的木屋了吗？
[charslot(slot="l", name = "avg_npc_1071_1#5$1",focus="l")]
[name="菈玛莲"]上个月的事情了，锡人。
[PlaySound(key="$d_avg_rowboat_lake_loop",loop=true,channel="water",volume=0)]
[SoundVolume(volume=0.6, channel="water",fadetime=2)]
[charslot(slot="l", name = "avg_npc_1071_1#5$1",focus="l")]
[name="菈玛莲"]当时我还听到她把你编进童话故事，告诉孩子们河谷里的雾都是从你的烟斗里飘出来的......
[charslot(slot="l", name = "avg_npc_1071_1#3$1",focus="l")]
[name="菈玛莲"]可就在一天后，当孩子们缠着她追问你是怎样说服那副空盔甲，逃脱被扔进熔炉的宿命时，她却对你的名字感到困惑。
[charslot(slot = "r", name = "avg_4151_tinman_1#6$1", focus="r")]
[name="锡人"]......她开始遗忘了。
[charslot(slot="l", name = "avg_npc_1071_1#3$1",focus="l")]
[name="菈玛莲"]是啊，遗忘——死亡对女妖的提醒。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot]
[curtain(direction = 0, fillfrom = 0.18, fillto = 0.18, afrom=0, ato=1, fadetime=0.1, block=false)]
[curtain(direction = 4, fillfrom = 0.18, fillto = 0.18, afrom=0, ato=1, fadetime=0.1, block=true)]
[Background(image="68_g12_valleytree",screenadapt="coverall")]
[BackgroundTween(image="68_g12_valleytree", duration=18, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.2, yScaleTo=1.2, xFrom=80, xTo=-80, block=false)]
[focusout(type="bg", id="68_g12_valleytree", from=0, to=1, duration=0, block=true)]
[focusout(type="bg", id="68_g12_valleytree", from=1, to=0.3, duration=8, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3.5, block=true)]
[PlaySound(key="$d_avg_magneticwaterfall_loop",volume=0, channel="f", loop=true)]
[SoundVolume(volume=0.2, channel="f",fadetime=2)]
[name="菈玛莲"]那之后，她就搬进了栖脚树下的木屋，像她这些年送走的每一位女妖那样，平静地等待死亡到访。
[name="锡人"]为一位已经遗忘了我的老友送别......没想到这次回来会遇到这么严峻的考验。
[PlaySound(key="$d_avg_brdchrp", volume=0.6)]
[name="菈玛莲"]总之，用你的方式，给她些安慰吧。
[name="菈玛莲"]拂哀菈为我们、为河谷，也为萨卡兹付出了太多。
[name="菈玛莲"]你也知道，她那样的人，总是执拗而不自知地活在痛苦里。我只是......
[name="菈玛莲"]我只是希望，当三百多年的记忆一点一点弃她而去时......她还能得到一丝慰藉。
[name="锡人"]我明白。
[dialog]
[StopSound(channel="water", fadetime=1)]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_arriveshore", volume=0.6)]
[delay(time=1)]
[name="菈玛莲"]......我们到了。
[stopsound(channel="water",fadetime=2)]
[stopsound(channel="f",fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[curtain]
[bgeffect]
[charslot]
[delay(time=1)]
[Background(image="68_g12_valleytree",screenadapt="coverall")]
[focusout(type="bg", id="68_g12_valleytree", from=0.3, to=0, duration=0.1, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fade

... (全文31670字符)
```

### level_act47side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cherunder_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$blooddrop", loop=true, channel="water", volume=0.5)]
[PlaySound(key="$d_avg_openftstpwalk", volume=1)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1", posfrom="50,0",posto="50,0", duration=1.5)]
[charslot(slot = "r", name = "avg_npc_1000_1#1$1", posfrom="50,0",posto="50,0",duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1",focus="l")]
[name="费尔南"]怎么还没有到运输口？按照园区地图的指引，我们应该能看到建材安检闸机了啊......
[charslot(slot = "r", name = "avg_npc_1000_1#3$1",focus="r")]
[name="奥克里"]还、还要再往前吗？这里怎么一个人都没有，简直安静得过分......
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2034_1#9$1",isblock=true)]
[name="高登"]废话，要是出现第四个人，我们不就暴露了吗？都给我打起精神来！
[dialog]
[charslot]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4214_cairn_1#8$1", posfrom="50,0",posto="50,0")]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1", posfrom="50,0",posto="50,0",isblock=true)]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1",focus="r",isblock=true)]
[name="奥克里"]噫！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="奥克里"]是、是红色的液体......天花板在往下滴血，都滴到我脸上了！
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2034_1#7$1",isblock=true)]
[name="高登"]那是管道的锈水......别逼我把你的嘴缝起来。
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4214_cairn_1#9$1", posfrom="50,0",posto="50,0")]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1", posfrom="50,0",posto="50,0",isblock=true)]
[charslot(slot = "l", name = "avg_4214_cairn_1#9$1",focus="l")]
[name="费尔南"]呃，长官，您刚刚说过，要是出现第四个人，就意味着我们暴露了对吧......？
[dialog]
[charslot]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",bstart=0.2, bend=0.7, duration=1.5,isblock=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",bstart=0.2, bend=0.7, afrom=1, ato=0, duration=0.5, isblock=true)]
顺着费尔南示意的方向，所有人都清楚地看见了“第四个人”。
[dialog]
暗道的尽头，那个模糊的人影被忽明忽暗的灯光勾勒得如同鬼魅，正缓步向他们走来。
[dialog]
[charslot(slot = "l", name = "avg_4214_cairn_1#5$1", posfrom="50,0",posto="50,0")]
[charslot(slot = "r", name = "avg_npc_1000_1#2$1", posfrom="50,0",posto="50,0",isblock=true)]
[charslot(slot = "l", name = "avg_4214_cairn_1#5$1",focus="l")]
[name="费尔南"]唔，这人看上去有点眼熟？
[charslot(slot = "r", name = "avg_npc_1000_1#2$1",focus="r")]
[name="奥克里"]妈、妈呀......
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_2034_1#5$1",isblock=true)]
[name="高登"]继续走。我对莱茵实验区的管控和调查权正当得不能再正当，不管那是哪号人物都没差——
[charslot(slot = "m",focus="n")]
[name="？？？"]是吗？
[dialog]
[charslot]
[Effect(name="$e_muesys_show",layer = 4,rox=-7,roy=79,roz=100)]
[playsound(key="$d_avg_watersubbreak",volume=0.7)]
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",isblock=true)]
[delay(time=3)]
[charslot(slot = "m", name = "avg_npc_2034_1#5$1",isblock=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="高登"]......
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",isblock=true)]
[name="娜斯提？"]长官，请说明情况。
[charslot(slot = "m", name = "avg_npc_2034_1#1$1",isblock=true)]
[name="高登"]娜斯提，莱茵实验区本就在接受调查，你已经同意全面配合行政人员和园区警卫的所有行动。
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",isblock=true)]
[name="娜斯提？"]完全不让当事人知情的调查，又该怎么配合？
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",isblock=true)]
[name="娜斯提？"]况且，讲解员也算是“行政人员”？我还是第一次知道。
[charslot(slot = "m", name = "avg_npc_2034_1#1$1",isblock=true)]
[name="高登"]那场实验事故前后，讲解员来拜访过莱茵，带她来取证再正常不过。
[charslot(slot = "m", name = "avg_npc_2034_1#3$1",isblock=true)]
[name="高登"]至于预先不通知，是期望能确保调查结果的可信度，我完全有权做这样的判断......
[dialog]
[charslot]
出发前，高登考虑过一切风险，甚至预演了被古斯塔夫盘问的情况。
他知道梅希亚靠不住，也有信心镇住场面，但此刻，他身后粗重的尾巴却不由自主地拍打着地面，仿佛感知到了某种不受掌控的威胁。
眼前的娜斯提紧盯着自己，好像想到了什么阴谋，诡异感和不安让高登攥紧了插在裤兜里的左手。
[charslot(slot = "m", name = "avg_npc_2033_1#1$1",isblock=true)]
[name="娜斯提？"]......
[charslot(slot = "m", name = "avg_npc_2033_1#3$1",isblock=true)]
[name="娜斯提？"]（唉，我只是让水分身躲在盆栽里，替娜斯提当个监控探头，她也没跟我说过园区长官这么难糊弄呀？）
[charslot(slot = "m", name = "avg_npc_2033_1#3$1",isblock=true)]
[name="娜斯提？"]（要是跟他吵上一晚上......也太累了！还是用我自己的办法吧。）
[charslot(slot = "m", name = "avg_npc_2033_1#2$1",isblock=true)]
[name="娜斯提？"]咳咳！
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[bgeffect(name="$eb_068cg_rain",layer=2, block=false)]
[delay(time=2)]
[Background(image="68_g17_cgi04", xScaleTo=2, yScaleTo=2, x=300, screenadapt="coverall")]
[BackgroundTween(image="68_g17_cgi04", duration=5, xScaleFrom=2, yScaleFrom=2, xScaleTo=1.8, yScaleTo=1.8)]
[focusout(type="bg", id="68_g17_cgi04", from=0, to=1, duration=0, block=false)]
[stopsound(channel="water", fadetime=2)]
[PlaySound(key="$d_avg_seawaterinflux",channel="sea", volume=1)]
[playMusic(intro="$m_avg_nasty_intro",key="$m_avg_nasty_loop", volume=0)]
[MusicVolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[focusout(type="bg", id="68_g17_cgi04", from=1, to=0.5, duration=1, block=false)]
[PlaySound(key="$d_avg_timestop",channel="time", volume=1)]
[Delay(time=2)]
[focusout(type="bg", id="68_g17_cgi04", from=0.5, to=0, duration=1, block=false)]
[Delay(time=3)]
[playsound(key="$d_avg_watersubbreak",volume=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[Image(image="68_i04_2", screenadapt="coverall", xScale=1.2, yScale=1.2, x=0, fadetime=0)]
[ImageTween(xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
从进入通道开始就在耳

... (全文30739字符)
```

### level_act47side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="38_g1_rhinemeetingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$Tremont_intro",key="$Tremont_loop", volume=0.6)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[charslot(slot="l",name="avg_npc_896_1#1$1",duration=0.5)]
[interlude(maskid = "group_interclude_vertical_common" ,size = "290,760", style=0 , offset = "200,0" ,channel = 3,tsfrom = "0,1", tsto="1,1",tsduration = 0.5)]
[interlude(channel = 3, type = 3, slot = "r", pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1",duration = 0.5)]
[interlude(channel = 3, type = 3, slot = "r", switch = false)]
[Delay(time=1.5)]
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]精彩的演讲，副总统先生。
[name="塞雷娅"]甚至在莱茵的休息室，我都能听见哭声。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]我倒是没想过自己能打动哥伦比亚最特立独行的科研工作者们。
[name="杰克逊"]不过，花束、横幅、言辞激烈的支持信、涂装成我的模样的士兵模型......这几个小时里我已经收到够多了。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]莱茵没送。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#6$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]......哈哈，挺好。那就言归正传吧，塞雷娅总辖。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#7$1")]
[name="杰克逊"]从科学的角度，我们该怎么定性那棵飘在天上的“树”？
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#1$1")]
[name="塞雷娅"]如果您真的在意它的科学原理，我不介意花整个下午向您解释它如何将根系扎进整片大地，让枝叶蔓及整片天空。
[name="塞雷娅"]但我想，从科学的角度，您只需要知道它的完全形态可以汇集哥伦比亚全境的能量与信息，再进行集中处理。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#3$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]你是说，一座生效范围广及整个哥伦比亚的......能量井？
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#1$1")]
[name="塞雷娅"]以及服务器，而且是双向运行。
[name="塞雷娅"]不仅从大地向天空汇集，也可以反向地从天空向大地输送——既有根系，也有枝叶。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]哈哈。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]就别勉强自己理解这些了，副总统阁下。您当初在特里蒙访问莱茵的时候是怎么走神的，现在也还是。
[name="塞雷娅"]国防部的几十架城防炮，与梅兰德所控媒体的数百颗镜头一齐对准那棵“树”的时候，是您开口把它保了下来。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]雅拉女士的一番话确实感人肺腑，哪怕我这样的老家伙，也难免想起了些年轻时候的不羁。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]原来如此。
[name="塞雷娅"]我还以为您是不想把给这棵“树”定性的机会，白白让给国防部或梅兰德呢。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#5$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]......
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]一次展会、一场演讲，飞天狂热、爱国情怀，在几个小时之内为您换来了遥遥领先于其他候选人的支持率。
[name="塞雷娅"]但下一场演讲，您需要描绘一个怎样的未来，才能回应得了那些支持，您现在想清楚了吗？
[name="塞雷娅"]还是说，您本来就计划对着这棵“树”看图说话？
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]你知道国防部当初和克丽斯腾达成的共识。克丽斯腾造好“弧光一号”，国防部用它炸谁，与莱茵无关。
[name="杰克逊"]“树”的定性权已经在我手里。我在想，如果我给它定性的时候没找莱茵商量，它不会当场冲破星荚吧？
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]您当然可以不找任何人商量，不论是娜斯提和我、将军和议员们，还是您肩上的那只玩偶。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]......哈哈。
[name="杰克逊"]我突然想收回之前和秘书闲聊时对你的评价。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#6$1")]
[name="塞雷娅"]什么？
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]你比克丽斯腾更好打交道。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#5$1")]
[name="塞雷娅"]......
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]说说你的要求吧。
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#1$1")]
[name="塞雷娅"]解除对“螺旋桨天堂”的封锁，让那个逃亡的地块回到特区的航道上休整，至于一干人等的追责......
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#3$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]“逃亡”？特区政府不会这么定性刚刚发生的事情。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[name="杰克逊"]面对别国的蓄意破坏，哥伦比亚最前沿的科研人员最不可能选择的就是懦弱的“逃亡”，对吧？
[name="杰克逊"]还有呢？
[interlude(channel = 3, type = 3, slot = "m", switch = false)]
[charslot(slot = "left",focus="l",name="avg_npc_896_1#1$1")]
[name="塞雷娅"]解除对莱茵生命的封锁......您知道我在说什么。
[interlude(channel = 3, type = 3, slot = "r", switch = true, pfrom = "190,0", pto="190,0", name = "avg_npc_897_1#1$1")]
[charslot(slot = "m", focus = "n")]
[name="杰克逊"]尽快为你我安排一场正式的会议吧，塞雷娅总辖。你不能要求哥伦比亚去做并不存在的事情。我们向来只是好奇......
[name="杰克逊"]未来的莱茵生命能做到什么。
[interlude(channel = 3, type = 3, 

... (全文22535字符)
```

### ref_act47side

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 

[Image(image="ac5_2_on_a",screenadapt="coverall", fadetime=0)]

[Image(image="avg_5_5_a",screenadapt="coverall", fadetime=0)]

[Image(image="42_i11_a",screenadapt="coverall", fadetime=0)]

[Image(image="44_i04_a",screenadapt="coverall", fadetime=0)]
[Image(image="44_i17_a",screenadapt="coverall", fadetime=0)]
[Image(image="44_i18_a",screenadapt="coverall", fadetime=0)]

[Image(image="53_i04_a",screenadapt="coverall", fadetime=0)]
[Image(image="53_i05_a",screenadapt="coverall", fadetime=0)]
[Image(image="53_i15_a",screenadapt="coverall", fadetime=0)]
[Image(image="53_i17_a",screenadapt="coverall", fadetime=0)]

[Image(image="56_i01_a",screenadapt="coverall", fadetime=0)]
[Image(image="56_i12_a",screenadapt="coverall", fadetime=0)]


[Image(image="57_i06_1_a",screenadapt="coverall", fadetime=0)]
[Image(image="57_i06_2_a",screenadapt="coverall", fadetime=0)]

[Image(image="60_i01_1_a",screenadapt="coverall", fadetime=0)]
[Image(image="60_i01_2_a",screenadapt="coverall", fadetime=0)]
[Image(image="60_i06_a",screenadapt="coverall", fadetime=0)]
[Image(image="60_i07_a",screenadapt="coverall", fadetime=0)]
[Image(image="60_i12_1",screenadapt="coverall", fadetime=0)]
[Image(image="60_i12_1_a",screenadapt="coverall", fadetime=0)]
[Image(image="60_i13_2_a",screenadapt="coverall", fadetime=0)]


[Image(image="61_i02_a",screenadapt="coverall", fadetime=0)]


[Image(image="62_i03_a",screenadapt="coverall", fadetime=0)]
```

### training_act47side_01_a

```
[header(is_skippable=true, is_tutorial=true, is_autoable=false)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]这里就是“螺旋桨天堂”的浮空结构层。眼前的几个大小、形状不一的<@tu.kw>“可浮空区块”</>，就是这里的重点实验对象。
[popupdialog(dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]<@tu.kw>无论是地面干员，还是高台干员，都能登上“可浮空区块”</>，阻挡空中的目标，但它的承重能力相当有限。
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y",tileY=4.2, tileX=6.2)]<@tu.kw>热气球</>是“可浮空区块”的主要浮力来源。一个“可浮空区块”挂载了多少热气球，就能承载多少名干员。
[battle.pause(pause=false)]
```

### training_act47side_01_b

```
[header(is_skippable=false, is_tutorial=true)]
[battle.delay(time=0.3)]
[battle.pause(pause=true)]
[popupdialog(dialogHead="$avatar_ardign", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]我在天上，我在天上耶！我来阻挡那个飞过来的目标！
[popupdialog(dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]卡缇，小心。你所在的“可浮空区块”只挂载了<@tu.kw>一个</>热气球，它只能承载你一个人。
[battle.pause(pause=false)]
```

### training_act47side_01_c

```
[header(is_skippable=false, is_tutorial=true)]
[battle.delay(time=0.3)]
[battle.pause(pause=true)]
[popupdialog(dialogHead="$avatar_ardign", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]啊，我不在天上了！怎么回事，热气球被吹跑了！
[popupdialog(dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]每当“可浮空区块”上浮或下沉时，出于安全考虑，部署在上面的干员会立即重新部署。干员的<@tu.kw>生命值和技力会得到保留，开启中的技能则会被重置</>。
[popupdialog(dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]实验须知我已经交代完毕，接下来需要各位配合完成这场浮空实验。 呼，但愿他们没忘了给志愿者配呕吐袋，呕——
[battle.pause(pause=false)]
```


## 统计

- 总字符数：436895
- 对话行数：3155


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
