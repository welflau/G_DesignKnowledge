# 明日方舟 · 活动剧情 · act22side（28段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act22side」完整剧情脚本（28个文件，2414行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act22side
- 脚本文件数：28

### level_act22side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g2_reedmarshes",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_242",duration=0.7)]
[charslot(slot="r",name="avg_npc_725_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]别翻你那账本了，还想着过几天回去推上你的小车卖东西呢？
[charslot(slot="r",name="avg_npc_725_1#6$1",focus="r")]
[name="维恩"]没有，不敢想，唉。
[charslot(slot="r",name="avg_npc_725_1#6$1",focus="r")]
[name="维恩"]但是做了亏心事，我就总觉得要记下来。
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]医生都是聪明人，受的是什么伤，她看一眼就知道啦。既然她没责怪你，那就是原谅你了。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]可她说自己不是医生，只是在卖药的地方上班，学过一些急救知识，所以能指挥我们处理伤口......
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]你怎么知道她说的是实话？
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]要我说，她不是一般的医生，但更不可能是什么卖药的。她带的药品种类那么齐全，又出现在荒地上，多奇怪啊。
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]欸对了，她手提箱里都装了什么，你看清楚了吗？你是做生意的，东西值多少钱，你心里有数吗？
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]我没仔细看。
[charslot(slot="r",name="avg_npc_725_1#4$1",focus="r")]
[name="维恩"]......你总不能连救命恩人的行李都想抢吧。
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]行了，我就是随便问问。
[charslot(slot="r",name="avg_npc_725_1#6$1",focus="r")]
[name="维恩"]唉......你那里还有面包吗？
[charslot(slot="l",name="avg_npc_242",focus="l")]
[name="塔拉流民"]没多少了。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]......还是分我一个吧，拜托了。
[dialog]
[charslot]
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="34_g2_reedmarshes",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[charslot(slot="l",name="avg_npc_725_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_1020_reed2_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]医生。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]呃，不对，你不喜欢别人叫你医生......那个，吃块面包吗？
[charslot(slot="r",name="avg_1020_reed2_1#9$1",focus="r")]
[name="苇草"]不，谢谢。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]你在看什么？
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]只是，一本古旧的塔拉诗歌集。
[charslot(slot="l",name="avg_npc_725_1#8$1",focus="l")]
[name="维恩"]哦，哦，原来是塔拉语......我本来就不认识多少词，写出来的塔拉语我就更没见过啦，哈哈。
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]......你想坐在这里的话，没关系的。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[multiline(name="维恩")] 好，呃...
[charslot(slot="l",name="avg_npc_725_1#8$1",focus="l")]
[multiline(name="维恩",end=true)] ...其实我就是想为昨晚的事情谢谢你。
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]可我只是给了一些药。
[charslot(slot="r",name="avg_1020_reed2_1#2$1",focus="r")]
[name="苇草"]......清洗伤口，包扎，那些事情，我该自己做的。只是，我还做不好。
[charslot(slot="l",name="avg_npc_725_1#2$1",focus="l")]
[name="维恩"]没事，那伤口我也不敢碰，确实吓人。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]......但我是想说，要不是你放了那把火，我们恐怕都脱不了身。
[charslot(slot="r",name="avg_1020_reed2_1#6$1",focus="r")]
[name="苇草"]火......？
[charslot(slot="r",name="avg_1020_reed2_1#8$1",focus="r")]
[name="苇草"]......不，火不是我放的，我只是路过。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]好吧，既然你这么说，那就当是巧合好啦。
[charslot(slot="l",name="avg_npc_725_1#6$1",focus="l")]
[name="维恩"]唉，什么深池，那些当兵的把不听话的人都叫做深池。我们也就算了，你这样的好心人，不该背上这么重的罪名。
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]......你很憎恨深池？
[charslot(slot="l",name="avg_npc_725_1#2$1",focus="l")]
[name="维恩"]我......我说不上来。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]你是从城里来的，我还是给你提个醒吧。前段时间，深池的人来过这一带。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]听说他们跟维多利亚的一支军队撞上了，结果维多利亚人没一个活下来。
[charslot(slot="l",name="avg_npc_725_1#1$1",focus="l")]
[name="维恩"]这件事把城里的老爷们气坏了，所以他们从特伦特郡调了一批当兵的出来，在石高原野上四处抓人，村子也烧了好几座。
[charslot(slot="l",name="avg_npc_725_1#6$1",focus="l")]
[name="维恩"]......其实你真不该救我们，不值得。
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]......
[charslot(slot="r",name="avg_1020_reed2_1#12$1",focus="r")]
[name="苇草"]我如果，不去在乎别人的生命，那我答应罗德岛的事，就没有做到......
[charslot(slot="l",name="avg_npc_725_1#4$1",focus="l")]
[name="维恩"]啊？不好意思，你说话声音实在太小了......
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]不，没什么......你刚刚说的情况，我知道一些，路上我会小心的。
[charslot(slot="l",name="avg_npc_725_1#4$1",focus="l")]
[name="维恩"]欸，你这就要走？
[charslot(slot="r",name="avg_1020_reed2_1#9$1",focus="r")]
[name="苇草"]嗯，天已经亮了，我不用你们指路了。
[charslot(slot="l",name="avg_npc_725_1#6$1",focus="l")]
[name="维恩"]好吧，好吧。我明白，像你这样，把维多利亚语讲得很标准的塔拉人，都不肯跟我们多说话。
[dialog]
[charslot]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_724_1#8$1",duration=1.5)]
[delay(time=2)]
[name="塞尔蒙"]喂，你们见到凯莉了吗？差不多这么高的女人，走路时尾巴摇摇晃晃的。
[charslot(slot="m",name="avg_npc_724_1#1$1")]
[name="塞尔蒙"]没见到？那可以麻烦你在这附近找找吗，医生？她一晚上没回来。
[charslot(slot="m",name="avg_npc_725_1#4$1")]
[name="维恩"]塞尔蒙，你的态度怎么突然——
[charslot(slot="m",name="avg_npc_724_1#1$1")]
[name="塞尔蒙"]啊，维恩，你到我这边来帮忙吧。
[charslot(slot="m",name="avg_1020_reed2_1#1$1")]
[name="苇草"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="34_g3_swamp_d",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_662_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_222_bpipe_1#3",duration=0.7)]
[delay(time=1

... (全文9419字符)
```

### level_act22side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g3_swamp_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="l",name="avg_npc_662_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_222_bpipe_1#5",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_222_bpipe_1#5",focus="r")]
[name="风笛"]这些士兵是怎么回事啊？
[charslot(slot="r",name="avg_222_bpipe_1#5",focus="r")]
[name="风笛"]倒下之前没有什么像样的抵抗，对我们的喊话也没反应。
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]他们已经死了。死亡时间......超过四十八小时。
[charslot(slot="r",name="avg_222_bpipe_1#7",focus="r")]
[name="风笛"]陈陈，我知道你是警察，你的判断不会出错。可是，这些人在被我们击倒之前，明明都是站着的啊？
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]......我在整合运动的队伍中见过一种能操纵他人的源石技艺。
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]但二者甚至谈不上相似。如果阿米娅......如果罗德岛的卡特斯在，她也许能比我更清楚地感觉到那种差别。
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]那种源石技艺否认情感和思绪，将活着的萨卡兹战士磨成行走的兵器。
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]而这里的深池士兵，他们确实已经死了......只是强烈的情感在他们死后仍然燃烧。
[charslot(slot="r",name="avg_222_bpipe_1#4",focus="r")]
[name="风笛"]燃烧？
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]......一种感觉而已。
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]如果这种源石技艺有具体的模样，如果我要用我的赤霄去切开它，我会想象自己要斩断的是一团火。
[charslot(slot="r",name="avg_222_bpipe_1#7",focus="r")]
[name="风笛"]等等，我见过......
[dialog]
[PlaySound(key="$flashback",volume=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=0.7, r=255, g=255, b=255, fadetime=0.5, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.7, fadetime=0)]
[Image(image="21_I5", fadetime=0,screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="l",name="avg_npc_662_1#1$1")]
[charslot(slot="r",name="avg_222_bpipe_1#7",focus="r")]
[name="风笛"]紫火。
[charslot(slot="r",name="avg_222_bpipe_1#7",focus="r")]
[name="风笛"]奇怪的紫火，在死去的战士眼睛里燃烧着......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[image]
[delay(time=1)]
[Background(image="34_g3_swamp_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="风笛"]我在小丘郡见过你描述的这种源石技艺。
[charslot(slot="r",name="avg_222_bpipe_1#1",focus="r")]
[name="风笛"]这一路上......一路上我都没有再见过！陈陈，我们真的快追上了，是不是？那个在小丘郡带领鬼魂部队的术师，就在这附近！
[charslot(slot="r",name="avg_222_bpipe_1#1",focus="r")]
[name="风笛"]我不会忘了她的样子......只要再见到她，我一定能认出来，到那时候，我就能得到深池的真相。
[charslot(slot="l",name="avg_npc_662_1#1$1",focus="l")]
[name="陈"]......嗯。
[charslot(slot="r",name="avg_222_bpipe_1#1",focus="r")]
[name="风笛"]那快走吧！多找点人问问路，村民，或者路过的商队......我们总能找到他们的，反正他们又不是真正的鬼魂！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[charslot]
[Background(image="bg_forest",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_724_1#10$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_725_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]......呼。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]巡逻队来得也太突然了，还好咱们眼力好。
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]哈，那些维多利亚的混蛋，来抓人难道还会提前打招呼？
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]你们先走，我清点一下人数。刚刚逃得那么着急，我总担心有人掉队......
[charslot(slot="r",name="avg_npc_725_1#4$1",focus="r")]
[name="维恩"]......啊，对了！医生呢？没人去叫上她？
[charslot(slot="l",name="avg_npc_724_1#7$1",focus="l")]
[name="塞尔蒙"]她不是说今天早上就自己离开吗？管她干嘛。
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]再说，就算她被维多利亚士兵抓了，应该也不会出事吧？她又不在通缉令上。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]唉，她在呀！昨晚咱们就把她给卷进来了！
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]虽然天黑了些，当兵的可能没看清她的脸，但这一带你见过几个瓦伊凡？
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]你又没本事帮忙，一天到晚替别人操心，有什么用？
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]我......
[charslot(slot="r",name="avg_npc_725_1#7$1",focus="r")]
[name="维恩"]等等，不对，凯莉在这里......塞尔蒙，你是故意的。
[charslot(slot="r",name="avg_npc_725_1#7$1",focus="r")]
[name="维恩"]你骗她说我们有同伴不见了，求她帮忙去找找人......
[charslot(slot="r",name="avg_npc_725_1#7$1",focus="r")]
[name="维恩"]为什么？她那么好心，救了我们，还分了我们一些药......你就这么把她留给那些当兵的？
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]这还用问？把她留在后面吸引注意力，我们就能安全地逃跑一段时间。
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]而且她就算被抓，也说不出什么重要的事。她甚至根本不知道我们朝哪个方向走了，更不知道我们是要去找深池的。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]可......可她会死呀！
[charslot]
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="塔拉流民"]是啊，她自己走，迟早也会撞上巡逻队。
[name="塔拉流民"]我们之前就该把她的行李全抢走，至少别让那些东西落到维多利亚的混蛋手里。
[charslot]
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="l")]
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]是她自己选的，维恩。你没注意到她看我的表情吗？
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]她很熟悉深池，却没有表现出对深池的善意。她还讲标准的维多利亚语。
[charslot(slot="l",name="avg_npc_724_1#10$1",focus="l")]
[name="塞尔蒙"]这种人比真正的维多利亚人还恨我们。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]......我不信，塞尔蒙。我还是信我看人的直觉。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[charslot]
[Delay(time=1)]
[Background(image="bg_forest",screenadapt="coverall")]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop"

... (全文21464字符)
```

### level_act22side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$doorknockquite")]
[name="特别行动队队长"]菲舍尔，子爵的紧急信函......
[Dialog]
[charslot]
[Dialog]
[charslot(slot = "right", name = "avg_4017_puzzle_1#6$1",duration =0.3)]
[delay(time=0.5)]
[PlaySound(key="$dooropenquite")] 
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "left", name = "avg_npc_399_1#1$1",posfrom = "-200,0", posto = "0,0",duration = 1,isblock=false)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]......菲舍尔？
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]哎，你又在思索什么难题？
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[name="菲舍尔"]......抱歉。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]你对着拼图走神的时间里，那个叫阿赫茉妮的菲林可是一刻不停地在行动，就在这座特伦特郡里。
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[name="菲舍尔"]请放心，我没有片刻走神，对她的监视也没有丝毫松懈。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]看你的样子，调查应该没有什么进展。
[charslot(slot="r",name="avg_4017_puzzle_1#7$1",focus="r")]
[name="菲舍尔"]如果这段时间的观察能够证明，她依然忠于自己对维多利亚的职责，那么我会比抓住一个叛徒更高兴。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]我可从没看到过你高兴的时候。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]......我以为上次行动失败之后，我不会再在这间办公室见到你了。
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[name="菲舍尔"]请不要这么说，行动本身并没有失败。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]医院的检查结果呢？
[charslot(slot="r",name="avg_4017_puzzle_1#4$1",focus="r")]
[multiline(name="菲舍尔")]急性感染，创口中活性源石碎片较多......
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[multiline(name="菲舍尔")]当然，病情已经被控制住了，请不用担心。偶发的疼痛并不会影响我的行动。
[charslot(slot="r",name="avg_4017_puzzle_1#7$1",focus="r")]
[name="菲舍尔"]不过，诊断结果我还没有上报。
[charslot(slot="r",name="avg_4017_puzzle_1#6$1",focus="r")]
[name="菲舍尔"]我认为自己尚有能力执行对阿赫茉妮的调查任务，而且，没有谁会想接手这一地的信息碎片。
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[name="菲舍尔"]这些烟雾弹背后的真实目的，我有责任探清。
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[name="菲舍尔"]......在此期间，我会和所有人保持距离，请放心。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]以我处理紧急事态的经验，还用不着你说这句话。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]只要市政厅依然允许你进出，我们特别行动队就会持续支持你的调查。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]不说声感谢吗？
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]哈哈，算了，我只是想开个玩笑，让你别一直紧绷着。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="特别行动队队长"]记得抽空看看子爵的信。
[dialog]
[delay(time=1)]
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[PlaySound(key="$d_avg_paper1")]
[delay(time=1)]
[name="菲舍尔"]......请柬？
[charslot(slot="r",name="avg_4017_puzzle_1#1$1",focus="r")]
[name="菲舍尔"]我明白了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[charslot]
[Background(image="34_g1_victoriavillage",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_724_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_725_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_725_1#5$1",focus="r")]
[name="维恩"]......听你的？你要把我们带到哪里去？
[charslot(slot="r",name="avg_npc_725_1#5$1",focus="r")]
[name="维恩"]我们不能再这么往荒野里面走了，你指的方向根本没有聚落。
[charslot(slot="r",name="avg_npc_725_1#5$1",focus="r")]
[name="维恩"]那种寸草不生的地方，别说猎野兽，就连野莓都捡不到。再说，你也不知道哪场雨会带着小石头一起砸下来，天灾信使都不会从那里走！
[charslot(slot="l",name="avg_npc_724_1#1$1",focus="l")]
[name="塞尔蒙"]我知道穿过那片沼泽要花几天，口粮的事，找维多利亚人的商队去抢就是了。
[charslot(slot="l",name="avg_npc_724_1#8$1",focus="l")]
[name="塞尔蒙"]啊，那个医生带的药也够。
[charslot(slot="r",name="avg_npc_725_1#7$1",focus="r")]
[name="维恩"]她不是医生......她也是要去镇上的，我们说好了她送我们到镇上就走。你把她当什么了？我们的药箱子？
[charslot(slot="r",name="avg_npc_725_1#3$1",focus="r")]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="维恩"]就为了你那点私心，所有人都得把自己的东西、自己的命全搭给你，是不是？
[charslot(slot="l",name="avg_npc_724_1#3$1",focus="l")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="塞尔蒙"]闭嘴，维恩！你要是有意见，怎么不自己走？你有那个本事吗？
[charslot(slot="r",name="avg_npc_725_1#6$1",focus="r")]
[name="维恩"]......
[charslot(slot="l",name="avg_npc_724_1#9$1",focus="l")]
[name="塞尔蒙"]胆小鬼是活不下去的。
[charslot(slot="r",name="avg_npc_725_1#4$1",focus="r")]
[name="维恩"]塞尔蒙！
[dialog]
[charslot]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",duration=1,isblock=true)]
[name="苇草"]......
[charslot]
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="l")]
[charslot(slot="l",name="avg_npc_724_1#9$1",focus="l")]
[name="塞尔蒙"]啊，“苇草”。
[charslot(slot="l",name="avg_npc_724_1#1$1",focus="l")]
[name="塞尔蒙"]我真不喜欢你这个绰号，就跟什么石头泥巴似的，遍地都是，也不知道是在叫你还是叫路边的草，哈哈。
[charslot]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="苇草"]我听到你们在吵架。
[charslot]
[charslot(slot="l",name="avg_npc_724_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]是这样......我得跟你说件事。我们去不了图拉镇了。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]刚刚广播里说，军队怀疑那边有两家工厂在偷偷给深池生产物资，赶走了一批人，爆发了一些冲突。
[charslot(slot="r",name="avg_npc_725_1#1$1",focus="r")]
[name="维恩"]我们现在继续往那个方向走，别说搭上运载车了，大概刚接近镇子就会被抓。
[charslot(slot="r",name="avg_npc_725_1#2$1",focus="r")]
[name="维恩"]......唉，难得又多了一个有本事的人帮忙，好不容易才逃到这里。
[charslot(slot="l",name="avg_npc_724_1#7$1",focus="l")]
[name="塞尔蒙"]哈，说得好像扒上了一辆运载车，你的好日子就来了似的。
[charslot(slot="l",name="avg_npc_724_1#7$1",focus="l")]
[nam

... (全文14073字符)
```

### level_act22side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(screenadapt="showall", image="34_g1_victoriavillage",x=-80, y=0, xScale=1.3, yScale=1.3)]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_battlefield_environment", volume=0.4, loop=true, channel="steam")]
[charslot(slot="m",name="avg_npc_175",focus="m",duration=0.5,isblock=true)]
[name="商队首领"]你们这些该死的塔拉人！真倒霉！
[name="商队首领"]砍！用力砍！给他们点教训！告诉他们别想再伸手拿别人的东西！
[charslot]
[charslot(slot="l",name="avg_npc_007")]
[charslot(slot="r",name="avg_npc_008")]
[name="商队护卫"]说得好，给塔拉人一点教训！
[name="商队护卫"]听到没有，你们这些渣滓？
[charslot(duration=0.15,isblock=true)]
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[backgroundTween(xFrom=-80, yFrom=0, xTo=80, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=0.2, block=false)]
[delay(time=0.3)]
[charslot(slot="m",name="avg_npc_242")]
[name="塔拉流民"]呃......手臂......
[name="塔拉流民"]......你敢说，我们塔拉人......该死？
[name="塔拉流民"]哈......哈......打啊，我们打死这些做生意的！看看是谁该死！
[dialog]
[PlaySound(key="$d_avg_punch02",volume=1)]
[CameraShake(duration=0.5, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="塔拉流民"]咕——
[dialog]
[charslot(duration=0.15,isblock=true)]
[delay(time=0.5)]
[backgroundTween(xFrom=80, yFrom=0, xTo=-80, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=0.2, block=false)]
[delay(time=0.3)]
[charslot(slot="m",name="avg_npc_662_1#4$1",focus="m")]
[name="陈"]退后！
[charslot(slot="m",name="avg_npc_175",focus="m")]
[name="商队首领"]你、你怎么就用刀鞘砸？我可是给你们付了钱的，给我认真一点！
[charslot(slot="m",name="avg_npc_662_1#3$1",focus="m")]
[name="陈"]一柄刀鞘够用。你们再动手，我会连你们一起拦下。
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]再说，我和风笛只是和你们同行，不是你雇的保镖，别认错了。
[Dialog]
[Character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$fightgeneral", volume=0.3)]
[playsound(key="$d_avg_doorbreak", volume=0.5,delay=0.3)]
[Delay(time=0.6)]
[Character(name="avg_npc_724_1#6$1", name2="avg_npc_662_1#1$1")]
[delay(time=0.1)]
[characteraction(name="left", type="jump", xpos=100, power=0, times=0.4, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_stickimp",volume=0.5)] 
[PlaySound(key="$swordtsing2", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, times=0.4, fadetime=0.4,block=true)]
[dialog]
[delay(time=1)]
[Character(name="avg_npc_724_1#6$1",name2="avg_npc_662_1#1$1")]
[characteraction(name="left", type="jump", xpos=200, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-200, power=5, times=1, fadetime=1,block=true)]
[characteraction(name="left", type="jump", xpos=200, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_stickimp", volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-200, power=5, times=1, fadetime=1,block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_axehitscrape", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_724_1#6$1", name2="avg_npc_662_1#1$1", focus=1)]
[name="塞尔蒙"]嘁，你和那边拿矛的家伙一样，也是个怪物......
[name="塞尔蒙"]看来我们之前听说的消息是真的，一般的商队，不敢来这个方向。
[Character(name="avg_npc_724_1#6$1", name2="avg_npc_662_1#1$1", focus=2)]
[name="陈"]你是那个领头的......你这身衣服，很惹眼。
[dialog]
[character]
[Delay(time=0.1)]
[character(name="char_empty")]
[charslot(slot="m",name="avg_npc_175",focus="m",duration=0.5,isblock=true)]
[name="商队首领"]......快走，陈小姐，我们得走！
[charslot]
[charslot(slot="l",name="avg_npc_724_1#6$1",focus="l")]
[charslot(slot="r",name="avg_npc_662_1#1$1",focus="l")]
[name="塞尔蒙"]哈，怎么突然害怕了？我听到你这张嘴，刚刚还说要教训一下塔拉人。
[charslot]
[charslot(slot="m",name="avg_npc_175",focus="m")]
[name="商队首领"]深池......鬼魂部队，你们这些疯子！果然塔拉人多的地方，就会撞见这些鬼魂！
[charslot]
[charslot(slot="m",name="avg_npc_724_1#2$1",focus="m")]
[name="塞尔蒙"]是啊，别说惹了我们，只是看到我们的样貌，都是会被杀人灭口的。
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]真的？
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]我跟朋友追查了这么久，对那支鬼魂部队该有的样子，还是心里有数的。
[charslot(slot="m",name="avg_npc_724_1#10$1",focus="m")]
[name="塞尔蒙"]啧。
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]女士，请带着商队尽快离开。这里的流寇，我和风笛拦住。
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]之后追查深池部队的事，我们自己去，不必再麻烦你们了。
[charsl

... (全文20615字符)
```

### level_act22side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_239",fadetime=0.7,block=true)]
[delay(time=1)]
[name="衣着朴素的诗人"]历史记载中，最后的盖尔王有感于德拉克与阿斯兰之间持久的战争太过惨烈，于是签下了和平协议。
[name="衣着朴素的诗人"]传说他选择了销熔战士的兵器以示决心，而他的臣子难以接受这样的失败，因此合谋造反，刺杀了这位君主。
[name="衣着朴素的诗人"]但正如您在多次演讲中所说，一场刺杀不足以灭亡一整支红龙的血脉。
[Character(name="avg_npc_727_1#1$1")]
[name="沃里克伯爵"]维多利亚人无论如何书写史书，都无法改变我们亲眼所见的事实。
[name="沃里克伯爵"]阿斯兰曾经许诺与德拉克分享维多利亚的王位，近百年来却不曾交出那顶冠冕。
[name="沃里克伯爵"]既然狮子们的野心已经昭彰至此，当初刺死盖尔王的六处剑痕，我想，也多少出自阿斯兰之手。
[name="沃里克伯爵"]更何况自那以后，德拉克逃出王城，不知所终。而失去统治者的塔拉王国，似乎顺理成章地被纳入维多利亚君主的权柄之下。
[name="沃里克伯爵"]阻止德拉克返回王城的，想必也不是他自己的臣民。
[Character(name="avg_npc_727_1#8$1")]
[name="沃里克伯爵"]因此，我很欣赏你基于塔拉人自己的歌谣写成的剧作，你领着人们看到了更多历史的真相。
[Character(name="avg_npc_239")]
[name="衣着朴素的诗人"]多谢您的赏识。
[name="衣着朴素的诗人"]为写作这个故事，我在乡野间看过一些戏剧，也拜访过几位继承了塔拉传统的吟游诗人。
[name="衣着朴素的诗人"]——只是，我看得最多的不是塔拉文化的垂危，而是许多生命正在消逝。
[name="衣着朴素的诗人"]您或许认为，要先有塔拉人的理想国，与维多利亚划清界限，塔拉人才能得救。
[name="衣着朴素的诗人"]但我想，如果我们自身能过上更好的生活，如果为那许多不识字的塔拉人埋下思想的种子......
[name="衣着朴素的诗人"]我们是否就已经战胜了想让我们一生困于贫穷无知的维多利亚人？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[Character]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0, block=true)]
[Background(image="34_g3_swamp_d",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_724_1#6$1",name2="avg_1020_reed2_1#1$1",fadetime=0.7,block=true)]
[delay(time=1)]
[Character(name="avg_npc_724_1#6$1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="塞尔蒙"]带着那些人一起走？想都别想。
[name="塞尔蒙"]现在你要等他们休息，要把自己的食物分给他们，我还能接受。
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="塞尔蒙"]但那是我们这两天运气好躲过了巡逻队，要是下次没躲过呢？那些七八岁的小孩，又不能拿起武器反抗，又跑不快，你要怎么办？
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]我可以战斗......我会保护他们。
[name="苇草"]你们想穿过无人区，彻底逃离特伦特郡控制的区域，这一路，我都可以协助你们。
[name="苇草"]通过风笛和陈......我的同事们帮忙，我联系到了我所属的企业，确认了最近的安全屋，恰好在这个方向上。
[name="苇草"]只是几顶帐篷和少量野外应急物资的话，他们能顺利转运过来。
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]我也知道，那边......是一位好心的公爵的领地。到了那里，至少，你们不会再被军队追捕。
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="塞尔蒙"]真的？真有什么贵族老爷对我们这样的人是好心的？
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]他有......庇护塔拉人的理由。
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="塞尔蒙"]你怎么知道？
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#8$1",focus=2)]
[name="苇草"]......也许很快，所有人都会知道了。
[Character(name="avg_npc_724_1#9$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]带上那些人，我们也有办法生存下去。
[Character(name="avg_npc_243")]
[name="紧张的塔拉流民"]可是，你别忘了，他们是感染者啊。
[name="紧张的塔拉流民"]我们是逃命逃出来的，干嘛还要把死亡招到自己身边？
[name="紧张的塔拉流民"]而且得了病的人，也不知道什么时候就会发作，哪一次就彻底断气了......
[name="紧张的塔拉流民"]你救这种人，有什么意义？
[Character(name="avg_1020_reed2_1#12$1")]
[name="苇草"]......
[Character(name="avg_1020_reed2_1#13$1")]
[name="苇草"]我不知道。
[Character(name="avg_1020_reed2_1#12$1")]
[name="苇草"]我只知道，当时有人救了我......我也想问她，为什么？
[name="苇草"]明明......我就快死了。
[Character(name="avg_npc_243")]
[name="紧张的塔拉流民"]你这是什么意思？
[Character(name="avg_1020_reed2_1#2$1")]
[name="苇草"]我也是感染者。
[Character(name="avg_npc_724_1#4$1")]
[name="塞尔蒙"]......
[Character(name="avg_npc_243")]
[name="紧张的塔拉流民"]啊？啊，呃......
[name="紧张的塔拉流民"]咳，好吧，其实感染者也没什么。要是没有你帮忙，我们也不见得能比感染者活得久，哈哈。
[name="紧张的塔拉流民"]不过......
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]只是站在一起，是不会传染矿石病的。
[name="苇草"]没关系，你害怕的话，可以离远一些，我不在乎。
[Character(name="avg_1020_reed2_1#2$1")]
[name="苇草"]但是，带上那些感染者一起逃吧......相信我。
[Character(name="avg_npc_243")]
[name="紧张的塔拉流民"]......哎，我信你！塞尔蒙，你也听她一句劝告吧......
[Character(name="avg_npc_724_1#10$1")]
[name="塞尔蒙"]——我不逃。
[name="塞尔蒙"]你要带上那些不能打架的人，那就带吧，随便你好了。
[name="塞尔蒙"]但我的目的绝对不会变。我要回到深池。
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_241",name2="avg_npc_248",focus=1)]
[name="严肃的军官"]......那两支部队已经失踪一周了，可以推测，这种与曾经鬼魂部队相关事件类似的情形，与深池有关。
[Character(name="avg_npc_241",name2="avg_npc_248",focus=2)]
[name="尖刻的军官"]类似？不，我们眼下面对的情况完全不同。
[name="尖刻的军官"]以前这些叛乱者只是纠集起来的一支武装力量，出现在某一处，发动袭击，仅此而已。
[name="尖刻的军官"]现在，疑似深池引发的暴力事件在整个维多利亚南部各处发生。
[Character(name="avg_npc_241",name2="avg_npc_248",focus=1)]
[name="严肃的军官"]......特伦特侯爵还坚持他的命令吗？
[Character(name="avg_npc_241",name2="avg_npc_248",focus=2)]
[name="尖刻的军官"]当然。无论移动城市外报上来了多少可疑情况，我们都必须一一厘清，把这一地区的局势控制住。
[Character(name="avg_npc_241",name2="avg_npc_248",focus=1)]
[name="严肃的军官"]不过，在各种小型冲突里，真正可疑的似乎只有红脊镇的纵火事件，而且那次火情也没有后续。
[name="严肃的军官"]也许我们该把这一部分卷宗暂时挪走？还是留下？
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Character(name="avg_4017_puzzle_1#1$1",fadetime=1,block=true)]
[delay(time=2)]
[name="菲舍尔"]请把上述卷宗借给我吧，长官们。
[Character(name="avg_npc_241")]
[name="严肃的军官"]你是......开......
[Character(name="avg_4017_puzzle_1#1$1")]
[name="菲舍尔"]打招呼的部分还请省略。
[name="菲舍尔"]以及，和过去一样，不必将此次卷宗调阅记录在案。
[Character(name="avg_4017_puzzle_1#6$1")]
[name="菲舍尔"]这次纵火事件......或许值得开展一次深入调查。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[Character]
[Background(image="bg_forest",screenadapt="coverall")

... (全文13671字符)
```

### level_act22side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_snowconutryinside",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#8$1",fadetime=0.7,block=true)]
[delay(time=1)]
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#8$1",focus=2)]
[name="维恩"]唉，谁能想到逃难了这么多天，居然还能安安稳稳坐在屋子里吃上一顿热饭菜。
[name="维恩"]那个叫风笛的姑娘可真讨人喜欢，刚刚我们还在夸她炖的菜好吃呢。
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#8$1",focus=1)]
[name="陈"]嗯，这方面她确实不赖。
[name="陈"]安置的事，你们商量得顺利吗？
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#8$1",focus=2)]
[name="维恩"]都说定啦，赶不了路的人都可以留下，这两天先借两间仓库躲一躲。
[name="维恩"]逃难的人跟商队打了一架，又没真的抢到什么东西，这种事太常见了，办案的不会放在心上。
[name="维恩"]过个几天，广播里不报这些事情了，他们就不用躲了，可以动手建自己的房子了。
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#1$1",focus=2)]
[name="维恩"]呃，不过得了矿石病的那几位，要住到离聚落远一些的地方去。
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#1$1",focus=1)]
[name="陈"]这里的人很友善。
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#1$1",focus=2)]
[name="维恩"]唉，是啊，我们当初逃出来的时候，一路上要是有人收留，也不至于变成现在这样。
[name="维恩"]可这也不怪别人。以前聚落里收留一两批逃难的人，不是难事，只是现在大家都过得越来越糟糕了。
[name="维恩"]你瞧塞尔蒙那小孩，要是有个地方能容下他们兄妹俩，她也不至于一直在各个聚落之间窜来窜去，到处惹事。
[Character(name="avg_npc_662_1#8$1",name2="avg_npc_725_1#6$1",focus=2)]
[name="维恩"]像咱们今天晚上可以在村子里过夜，但塞尔蒙坚持自己在村外躲着，就是因为她在这里抢过人家的牧兽，现在不好意思见那位老爷子......
[name="维恩"]......唉，当我没说。让她听到了，又要说我不尊重她。
[Dialog]
[Character]
[playsound(key="$doorknockquite")]
[delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Character(name="avg_npc_728_1#1$1",fadetime=1,block=true)]
[Delay(time=1.5)]
[name="莫兰"]晚上好......
[Character(name="avg_npc_725_1#4$1")]
[name="维恩"]啊，莫兰？天都黑了，你怎么过来的？趁现在还有灯，我带你回去......
[Character(name="avg_npc_728_1#6$1")]
[name="莫兰"]谢谢，但我已经习惯摸黑走路了......
[Character(name="avg_npc_728_1#1$1")]
[name="莫兰"]......请问，苇草在吗？
[Character(name="avg_npc_662_1#1$1")]
[name="陈"]你找她？她独自出门了。
[Character(name="avg_npc_725_1#6$1")]
[name="维恩"]也许苇草是有什么烦心事吧......自从来了这里，塞尔蒙就不肯和她说话。
[Character(name="avg_npc_662_1#8$1")]
[name="陈"]别担心，风笛去找她了。
[name="陈"]嗯......或者换个说法，我们不如担心苇草会嫌太吵吧。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="34_g4_swamp_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_222_bpipe_1#2",name2="avg_1020_reed2_1#11$1",focus=-1)]
[Delay(time=0.2)] 
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=50, fadetime=0.6,isblock=true)]
[delay(time=0.2)]
[characteraction(name="left", type="move", xpos=50, fadetime=0.3,block=false)]
[characteraction(name="right", type="move", xpos=-20, fadetime=0.4,block=false)]
[Delay(time=0.6)]
[PlaySound(key="$bodyfalldown3", volume=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="jump", xpos=-100, power=10, times=1, fadetime=0.5,block=false)]
[characteraction(name="right", type="jump", xpos=20, power=5, times=0, fadetime=0.6,block=true)]
[Delay(time=0.8)]
[Character(name="avg_222_bpipe_1#2",name2="avg_1020_reed2_1#11$1",focus=1)]
[name="风笛"]哇，抱歉！
[Character(name="avg_222_bpipe_1#2",name2="avg_1020_reed2_1#11$1",focus=2)]
[name="苇草"]......没事。
[Character(name="avg_222_bpipe_1#3",name2="avg_1020_reed2_1#11$1",focus=1)]
[name="风笛"]欸，我没想到这里会有人，没太仔细看。每次钟声一响，周围就黑黢黢的，眼睛要过一会儿才能习惯。
[name="风笛"]还好撞上的是你，换成其他人，可能就要被我撞倒了。
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#11$1",focus=1)]
[name="风笛"]不过，我记得大家说好今天晚上不用放哨？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]我只是......想在外面坐坐。
[Character(name="avg_222_bpipe_1#8",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]啊，干草的味道很好闻，对吧。
[Character(name="avg_222_bpipe_1#8",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]......干草？
[Character(name="avg_222_bpipe_1#8",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]是呀，那边的干草垛。我好久没闻到过这种气味了，所以跑出来好好地闻一闻。
[name="风笛"]以前我准备考军校的时候，读理论知识读得头疼了，只要在干草垛上面躺一会儿，就感觉什么都好了。
[name="风笛"]虽然妈妈总说我这是在偷懒，不能因为想问题太辛苦就不去想......可是脑子里有太多东西的话，就是挺累人的呀。
[Character(name="avg_222_bpipe_1#8",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]......嗯。
[Character(name="avg_222_bpipe_1#8",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="风笛"]所以，把手给我一下？
[Character(name="avg_222_bpipe_1#8",name2="avg_1020_reed2_1#5$1",focus=2)]
[name="苇草"]呃......
[Character(name="avg_222_bpipe_1#9",name2="avg_1020_reed2_1#5$1",focus=1)]
[name="风笛"]来来来，一起躺嘛！就一会儿！
[name="风笛"]虽然我不擅长想事情，也许帮不了你什么，但干草垛肯定能帮上你的！
[Dialog]
[character(fadetime=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[playsound(key="$d_avg_hidehaystack", volume=0.9, delay=0.2)]
[Image(image="34_i02",screenadapt="coverall",fadetime=2.5,block=true)]
[Delay(time=1)] 
[name="风笛"]嘿——！
[Dialog]
[character]
[Delay(time=0.5)]
风笛放松地躺在草垛上，轻轻哼着刚才从农户那里学来的歌谣。
一阵温润的夜风吹过，苇草按照她的建议，深深地吸了一口气。
但她闻到的不是干草的香气，而是潮湿的泥土与灰尘的味道。
[name="风笛"]想到自己竟然三年多没有回过家了，总觉得好奇怪呀。
[name="风笛"]你想呀，地等着我去翻土，麦子等着我去收割......一年不回家，就会把所有重要的事情全部错过一遍。
[name="风笛"]就连家里寄来的信，我也要等下一次回罗德岛的时候才能收到。
[name="苇草"]你......很想家吗？
[name="风笛"]当然啦。你呢？你是小丘郡人吗？
[name="苇草"]......不是。
[name="苇草"]但我以前也生活在和小丘郡差不多的城市里......深红色的砖墙，灰色的人行道，两三层高的房子，花藤会长到窗户外面。
[Dialog]
[Delay(time=0.7)]
[name="苇草"]我......很怀念那段平静的时光。
[name="苇草"]那个时候，家里放着很多旧书，有的还是手抄本。我总是躲到书房里，锁上门，那样就不用听别人讲话。
[name="风笛"]啊，你家里人很多所以太吵了？还是经常有人做客？
[name="苇草"]......不，还好。只是躲起来就可以避免很多麻烦。
[name="苇草"]从书房的窗户，可以看到街道，看到父母结束一天的工作归来。
[name="苇草"]如果可以的话，我很想回到那里。
[name="风笛"]啊，难道你说的地方已经......
[name="苇草"]嗯。
[name="风笛"]抱歉......我是不是让你更难过了？
[name="苇草"]没关系的，那是很早以前的事情了。
[name="苇草"]我和小丘郡那些生活被毁掉的普通人，或者眼前这些背井离乡的流民，也许没有太大差别。
[name="苇草"]大家可以在这里安顿下来，重新

... (全文14546字符)
```

### level_act22side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_wild_m",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[character(name="avg_npc_242",fadetime=0.7,block=true)]
[delay(time=1)]
[name="塔拉流民"]各位，我看到前面有人！有军队！
[name="塔拉流民"]在那个方向......呃，七、七点钟？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]啊，没关系，我们差不多听懂啦。
[Character(name="avg_222_bpipe_1#7",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]可是你确定没看错吗？这一带明明是完全没有人烟的荒野呀......怎么会有军队巡逻到这种地方来？
[Character(name="avg_222_bpipe_1#7",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]望远镜给我吧。
[name="苇草"]附近能够藏身的地形很少，请大家先在这里躲一躲。
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]我跟你一起去。要说维多利亚的军队，我比你熟吧？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]......嗯，谢谢。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[Character]
[Background(image="bg_wild_m",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="维恩"]塞尔蒙，帮我看一眼......我蹲在这块岩石下面，应该哪个角度过来的敌人都看不见我吧？
[Character(name="avg_npc_724_1#1$1")]
[name="塞尔蒙"]哈，还行吧。
[Character(name="avg_npc_724_1#1$1",focus=-1)]
[name="维恩"]那就好。天啊，咱们都平安无事地在荒野里走了四天了，既没天灾也没猛兽......最后这一段路要是出了事，那也太倒霉了。
[Character(name="avg_npc_724_1#1$1",focus=-1)]
[name="维恩"]你也别探头探脑的了，快来一起蹲着。都这么久了，你还信不过苇草她们吗？
[Character(name="avg_npc_724_1#6$1")]
[name="塞尔蒙"]是啊，我最不信任的就是她那种老好人。
[name="塞尔蒙"]她就想做那些谁都不得罪的事，这样要是事情出了错，也一定不是她自己的错。
[Character(name="avg_npc_724_1#6$1",focus=-1)]
[name="维恩"]你呀，说到底就是不喜欢她阻拦我们去深池。
[Character(name="avg_npc_724_1#10$1")]
[name="塞尔蒙"]也许吧，但我对你就没什么意见。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[Character]
[Background(image="bg_wild_m",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]......已经确认了，是一支维多利亚小型部队，但从装备来看，不是附近的驻军。
[name="苇草"]他们的武器十分精良，如果交战......我们取胜的概率很小。
[name="苇草"]也许他们不是来搜捕我们的，但是以防万一，我们还是躲藏起来。按照目前的行进方向，他们不会看到我们。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[Character]
[Background(image="bg_wild_m",screenadapt="coverall")]
[Delay(time=0.5)]
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_725_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_725_1#1$1",focus=2)]
[name="维恩"]你对我没意见，那是因为我说话没人听。
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_725_1#1$1",focus=1)]
[name="塞尔蒙"]但我可不是嫉妒她抢了我的风头。
[Character(name="avg_npc_724_1#10$1",name2="avg_npc_725_1#1$1",focus=1)]
[name="塞尔蒙"]......那支队伍靠近了。往那边挪一挪，给我个好位置盯着他们。
[Character(name="avg_npc_724_1#10$1",name2="avg_npc_725_1#6$1",focus=2)]
[name="维恩"]唉，求你别在这时候惹上麻烦。
[Dialog]
[Character(name="avg_npc_724_1#10$1",name2="avg_npc_725_1#6$1",focus=-1)]
[PlaySound(key="$d_avg_battlefield_environment", volume=0.2, loop=true, channel="dublin")]
[Delay(time=1)]
[Character(name="avg_npc_724_1#10$1",name2="avg_npc_725_1#4$1",focus=2)]
[name="维恩"]怎、怎么回事？打起来了？
[Character(name="avg_npc_724_1#10$1",name2="avg_npc_725_1#4$1",focus=1)]
[name="塞尔蒙"]......有一队人在隘道埋伏他们。
[Character(name="avg_npc_724_1#10$1",name2="avg_npc_725_1#5$1",focus=2)]
[name="维恩"]那、那要是刚刚我们没停下来躲在这儿，是不是我们也要被打了？等在那里的是什么人？
[character(name="avg_npc_242")]
[name="塔拉流民"]喂......我虽然看不太清，但那些人穿的衣服，是不是跟塞尔蒙你的有点像？
[name="塔拉流民"]那就是......深池吧？
[Character(name="avg_npc_724_1#9$1")]
[name="塞尔蒙"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2,block=true)]
[stopmusic(fadetime=1.5)]
[StopSound(channel="dublin", fadetime=1)]
[Character]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_4017_puzzle_1#5$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]......深池。
[name="菲舍尔"]八个月前的一个凌晨，我刚刚结束工作，正在半岛郡的一家餐厅吃早餐。
[name="菲舍尔"]广播里传来一个声音。
[name="菲舍尔"]那个声音说，他们要用火焰净化维多利亚的污浊。
[name="菲舍尔"]他们要以塔拉人的名义......向维多利亚宣战。
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]他们自称“深池”。 
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_241",focus=2)]
[name="特别行动队士兵"]......一群贪婪的暴徒给自己找的名号罢了。
[Character(name="avg_4017_puzzle_1#10$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]暴徒？
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]符合常规认知的暴徒的那部分人，大概全都死在小丘郡了。
[name="菲舍尔"]有人想用一整座城市的塔拉人来试探那位塔拉出身的公爵......可他们没有想到的是，那位深池的领袖反过来利用了这一点。
[name="菲舍尔"]事件结束后，深池成功地肃清了内部的不安定分子，进一步博得了周边塔拉民众的支持，在维多利亚的眼皮子底下全身而退。
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_241",focus=2)]
[name="特别行动队士兵"]深池领袖确实深谙贵族的行事风格。
[name="特别行动队士兵"]考虑到她的出身以及背后的支持者，这不足为奇。
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]那位领袖以及她的情报人员很清楚，向民众扔脏弹的是驻军，因此小丘郡事件的真相永远不会被追查下去。
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]但是......我读过那些报告。所有的报告。
[name="菲舍尔"]有人说，在那天的小丘郡现身的深池“领袖”......不止一位。
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_241",focus=2)]
[name="特别行动队士兵"]这并不符合公爵收到的其他情报。
[Dialog]
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_241")]
[PlaySound(key="$d_avg_chess", volume=0.2)]
[Delay(time=1.5)]
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]你看到这两块拼图了吗？
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_241",focus=2)]
[name="特别行动队士兵"]一模一样......
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_241",focus=1)]
[name="菲舍尔"]只要形状一样，就都能填补同一个缺口。而当它们像这样放在一起的时候，许多人一眼望过来，都会把一块当成另一块的影子。
[Character(n

... (全文24257字符)
```

### level_act22side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="你害怕我的火吗？可你的火与我的是一样的，拉芙希妮。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="它会永远燃烧，想要去蒙住它的光焰，让它熄灭，是徒劳的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不用畏惧让人看到。为什么不让看到的人畏惧它呢？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character]
[Background(image="21_G7_decisivebattlealley_d",screenadapt="showall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.8, fadetime=0)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
我知道我的体内有一团火。只要去摸索就会感到灼痛，时间久了，痛觉甚至比我的想法先一步浮现。
父母告诫我们，把这天生的火焰吞下去，藏起来，不要被任何人看见。
但我知道，姐姐总是悄悄地烧掉自己不想要的东西，然后就能得到更好的。
我是不是也可以？
[Dialog]
[name="拉芙希妮"]爸爸，可以带我去书店吗？
[Dialog]
[character]
那天早上，我想试着扮演她，用她的语气跟父母讲话。
每一次她向父母提出要求的时候，父母都会像被火烫到一样，惊惶又怜爱地答应。
我和她有着一样的相貌与声音，穿着一样的衣服，为什么我不能假装成她的样子？
[name="拉芙希妮"]我想看蒸汽骑士冒险故事的续集......因为，我不想被其他人问，为什么会有维多利亚人不喜欢看蒸汽骑士的故事。
[name="父亲"]......明天吧，拉芙希妮。爸爸妈妈今天已经很累了。
[name="拉芙希妮"]爸爸......认出来我了？
[Dialog]
[character]
[name="父亲"]当然，我怎么会分不清自己的两个女儿呢？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_black",screenadapt="showall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
那个雪夜过后我才明白，他们不答应我，是因为我想要的东西太小了。
如果是她的话，是不会连一本新印的小说都要从父母那里求来的。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="21_G6_decisivebattlealley_n",screenadapt="showall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.8, fadetime=0)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$bigbell", volume=1)]
[delay(time=2)]
[PlaySound(key="$bigbell", volume=1)]
[PlaySound(key="$rungeneral", volume=0.6,delay=0.2)]
[delay(time=2)]
[PlaySound(key="$bigbell", volume=1)]
[delay(time=2)]
我跟在她身后，拼命地奔跑。
团聚的钟声响了，可是，家已经回不去了。
[Dialog]
[name="拉芙希妮"]姐姐......我们，要去哪里？
[name="爱布拉娜"]......你想去哪里呢？
[name="拉芙希妮"]我，不知道......
[name="爱布拉娜"]既然哪里都不是家，那就随便敲开一扇门吧。
[name="爱布拉娜"]你只需要坦诚地告诉来开门的人，我们在这个节日的雪夜里无家可归。
[name="爱布拉娜"]无论多么冷漠的人，应该也是能对两个孩子生出同情心的。
[name="爱布拉娜"]去吧，拉芙希妮，别害怕。我在看着你呢。
[Dialog]
[character(fadetime=0.5)]
[Delay(time=1)]
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1)]
在冰冷的紫色火焰映照下，我颤抖着敲开了第一扇门。
那是刚刚取走了我们仇人性命的火焰，我却好像知道，如果我做错了什么，它也会转头来杀死我。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="34_g6_noblelivingroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[character(name="avg_226_weed_1#2",fadetime=0.7)]
[Delay(time=1)]
[name="拉芙希妮"]——可是，老师他做错了什么？
[Dialog]
[Character]
我听说，塔拉人的街区在上演一出戏剧，所以这样的大雪夜里，老师迟迟没有回家。
姐姐领我在老师的书房里坐下。她没有直接回答我的问题，只是温和地注视着我。
我知道，她对我很失望。我应该能够自己找到答案。
[Dialog]
[character(name="avg_226_weed_1#2")]
[name="拉芙希妮"]......他教我们，毁去无辜者的生活，激化塔拉人与维多利亚人的矛盾。
[name="拉芙希妮"]他还......谋害了落魄的政敌，就像，那些维多利亚人，害死我们的父母一样。
[name="拉芙希妮"]所以，取走他的性命......是该做的事情。
[Dialog]
[Character]
姐姐总是能做出正确的事情，我却做不到。
她把枪送给了我，可每一次握住那柄燃烧着火焰的长枪，我都在发抖。
就像此时。
[Dialog]
[character(name="avg_226_weed_1#2")]
[name="拉芙希妮"]我说的......对吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=3)]
[Character]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="爱布拉娜"]不，拉芙希妮。
[name="爱布拉娜"]死亡只不过会引他去往自己的理想。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background]
[Image(image="34_i04",xFrom=100, yFrom=-50, y=100, xScale=1.2, yScale=1.2, fadetime=2)]
[Delay(time=2)]
[ImageTween(yTo=0, duration=3, block=false)]
[Image(image="34_i04", y=0, xScale=1.2, yScale=1.2, fadetime=3)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[ImageTween(xFrom=100, yFrom=-50, xTo=0, yTo=-0, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=0.85, yScaleTo=0.85, duration=27, block=false)]
[PlaySound(key="$firestorm", volume=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=10, amount=0, block=false)]
[name="爱布拉娜"]他用阴谋与权术浇灌我们，剥下我们的自由与尊严，这当然可恨，但也只是可恨。
[name="爱布拉娜"]只是他的手段业已精熟，他的野心却太过狭隘，这才真正叫人惋惜。
[name="爱布拉娜"]他想要的，不过是掌控一个易碎的空想国度，令我们做他戴冠的傀儡。
[name="爱布拉娜"]我要握在手里的权力，却比他那狂人的空想，还要庞大得多。
[name="爱布拉娜"]——你呢，拉芙希妮？你想要什么呢？
[name="爱布拉娜"]你的血脉与教养让你高尚，这是好事，可你要是一无所求，我又该在身边留什么样的位置给你呢？
[name="爱布拉娜"]说吧，这可是雪夜里的愿望......多么大的野心，我都允许。
[name="拉芙希妮"]......
[name="拉芙希妮"]......
[Dialog]
[delay(time=1)]
我没有回答。
我只有小小的梦想，像壁炉里一团温暖的火。
我不敢回答。
[Dialog]
[delay(time=0.5)]
[name="爱布拉娜"]没关系，我的妹妹。既然你不知道自己的欲望在何处，那就先成为我吧。
[name="爱布拉娜"]往后，你与我便都是“领袖”。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[image]
[Character]
[Delay(time=0.5)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
那火焰注视着我，我成为了她的影子。
[Dialog]
[stopmusic(fadetim

... (全文11960字符)
```

### level_act22side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="34_g9_tent",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",fadetime=1,block=true)]
[delay(time=1)]
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="风笛"]苇草，你那边固定了吗？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]嗯，没问题。
[Dialog]
[Character(fadetime=0.5)]
[delay(time=1)]
[charslot(slot="m",name="avg_222_bpipe_1#8",posfrom="0,0",posto="-90,0",duration=1,isblock=true)]
[charslot(slot="m",posfrom="-90,0",posto="-90,-50",duration=1,isblock=true)]
[playsound(key="$d_avg_handcuff",volume=0.7)]
[charslot(slot="m", action="shake",random=false, power=3, times=8,isblock=true,duration=0.5)]
[delay(time=1)]
[charslot(slot="m",posfrom="-90,-50",posto="140,-50",duration=1,isblock=true)]
[charslot(slot="m", action="shake",random=false, power=3, times=5,isblock=true,duration=0.5)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[delay(time=1.5)]
[charslot(slot="m",posfrom="140,-50",posto="0,-50",duration=0.3,isblock=true)]
[playsound(key="$d_avg_flag",volume=0.7)]
[charslot(slot="m",posfrom="0,-50",posto="0,0",duration=1,isblock=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_222_bpipe_1#9",action="jump",times=2,power=10,isblock=true,afrom=1,ato=1,duration=1)]
[name="风笛"]咻——好了，这是最后一顶帐篷啦。
[charslot]
[Character(name="avg_npc_242")]
[name="塔拉流民"]哎呀，你们俩的力气可真大。
[name="塔拉流民"]对了，你们是不是要走了？
[Character(name="avg_222_bpipe_1#1")]
[name="风笛"]是呀，我和陈陈要调查的就是那些被法术控制的“鬼魂士兵”，这边的事情结束之后，我们还有其他的任务。
[name="风笛"]而且这里已经是特伦特郡辖区的边界，应该不会再有驻军找你们麻烦啦。
[Character(name="avg_222_bpipe_1#5")]
[name="风笛"]......唉，要是我们把秩序维持得更好一些，这么多混乱和冤枉的事情，就都不会发生了。
[Character(name="avg_npc_242")]
[name="塔拉流民"]啊，你在说什么呢？要不是因为你们，我们都不知道能不能活到现在呢。
[name="塔拉流民"]如果这是在我家，今晚我就要请你们喝接骨木酒，给你们送行。
[name="塔拉流民"]不过我们现在手里的物资，大半还都是你们从......从那个“罗德岛”带过来的，哈哈。
[name="塔拉流民"]我们给那个罗德岛寄信，你们能收到不？到时候大家找到地方落脚了，跟你们说一声，你们要是再路过这附近，可以来做客。
[Character(name="avg_222_bpipe_1#7")]
[name="风笛"]欸，应该可以吧？要是维多利亚的纷争结束，然后陈陈也见到了那个人......
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="风笛"]......你呢，苇草？接下来你要去哪里？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]我......应该会确认所有人都安顿好了，再去做自己的事。
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]就算离开了石高原野，摆脱了罪名，没有了熄火钟的管制......塔拉人也依然生活在一片泥泞的土地上，他们还是会寸步难行。
[name="苇草"]我觉得，我应该再帮他们想想办法。
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]塔拉和维多利亚的语言，我都会说，之后如果进入城市，遇到各种不同的人，我都可以交涉......会比其他人方便一些。
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="风笛"]啊，对了，今天你去找罗德岛的安全屋时，有没有什么人跟踪你？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]......应该没有。
[name="苇草"]没关系，我记得你的提醒。如果那些士兵是冲我来的......我不怕。
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]还有......谢谢你的好心。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[Character]
[Background(image="bg_coldforest",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=1)]
[name="维恩"]你说，到时候苇草肯不肯把帐篷卖一顶给我？
[name="维恩"]那可是城里工厂做出来的帆布，暴雨浇上半个月也不会漏水，正适合拿来改造我的小拖车。
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=2)]
[name="莫兰"]她心地很善良，你也不会昧着良心出价。我猜，你们的交易应该是能谈成的。
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=1)]
[name="维恩"]哈，我开玩笑的，我哪里有钱买这么好的东西。
[Character(name="avg_npc_725_1#9$1",name2="avg_npc_728_1#6$1",focus=1)]
[name="维恩"]不过谁能想到呢，前几天我们还为怎么活命发愁，现在却能睡进工厂做出来的结实帐篷，夜里也能生火了......
[Character(name="avg_npc_725_1#9$1",name2="avg_npc_728_1#6$1",focus=2)]
[name="莫兰"]嗯，她们很有本事。
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=1)]
[name="维恩"]也懂矿石病的事。
[name="维恩"]（口哨声）
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#2$1",focus=2)]
[name="莫兰"]......
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#2$1",focus=1)]
[name="维恩"]（不连贯的口哨旋律）
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=2)]
[name="莫兰"]笼罩溪谷的雾霭啊......♪
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=1)]
[name="维恩"]......将她远行的身影遮蔽......♪
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#6$1",focus=1)]
[name="维恩"]还是很好听。
[Character(name="avg_npc_725_1#8$1",name2="avg_npc_728_1#1$1",focus=2)]
[name="莫兰"]......那些追过我的人里，现在应该只有你还记得我了。
[Character(name="avg_npc_725_1#1$1",name2="avg_npc_728_1#1$1",focus=1)]
[name="维恩"]别这么说......大家肯定都记得。
[name="维恩"]矿石病又不是你的错。
[name="维恩"]（有点跑调的口哨音）
[Character(name="avg_npc_725_1#6$1",name2="avg_npc_728_1#1$1",focus=1)]
[name="维恩"]唉。
[name="维恩"]那小子，塞尔蒙她哥，死了。说不定我们当时帮过的那一队深池都死了。
[name="维恩"]我们白忙活了。
[name="维恩"]还好......至少你还活着，失踪了那么久之后，你还活着。
[name="维恩"]我看到苇草给你塞药了，矿石病是不是其实能治好？
[Character(name="avg_npc_725_1#6$1",name2="avg_npc_728_1#4$1",focus=2)]
[name="莫兰"]不，她们都说是治不好的。
[name="莫兰"]但是，请不要埋怨那些深池的士兵。我帮他们躲进工厂的运输车，伤口渗入了源石粗矿的碎屑......这也不是他们的错。
[Character(name="avg_npc_725_1#6$1",name2="avg_npc_728_1#4$1",focus=1)]
[name="维恩"]没有，我哪有埋怨呀，我只是觉得心里难受。
[name="维恩"]你们都相信深池，可我不敢信。深池是比我们厉害，还有武器，但我们都亲眼看到了，最后那队人被打得有多惨。
[name="维恩"]深池会对塔拉人好，帮塔拉人出口气，可之后呢？我想不出来......我就只记得那天车厢上的血。
[Character(name="avg_npc_725_1#1$1",name2="avg_npc_728_1#4$1",focus=1)]
[name="维恩"]塞尔蒙到现在还是想去找深池，去跟维多利亚人打仗，我都劝不住她。
[name="维恩"]你说，那天她跟苇草聊了那么久，苇草难道没给她讲清楚道理吗？
[Character(name="avg_npc_725_1#1$1",name2="avg_npc_728_1#6$1",focus=2)]
[name="莫兰"]可是我觉得，塞尔蒙那么做，不坏。她那样的人，能为其他塔拉人做很多事。
[Character(name="avg_npc_725_1#1$1",name2="avg_npc_728_1#1$1",focus=2)]
[name="莫兰"]你还记得吗？我感染之后不久，整个感染者街区的人一起被驱赶出了小镇。
[name="莫兰"]后来，被驱赶出来的镇民里更健壮有力的那些，抢走了大家身上所有的物资，留下了羸弱的老人与孩子，还有我这样

... (全文23194字符)
```

### level_act22side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="34_g9_tent",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Character(name="avg_npc_242",name2="avg_npc_243",fadetime=1,block=true)]
[delay(time=1.5)]
[Character(name="avg_npc_242",name2="avg_npc_243",focus=2)]
[name="塔拉流民"]不行，快跑！这边也有人！
[Character(name="avg_npc_242",name2="avg_npc_243",focus=1)]
[name="塔拉流民"]该死，他们是不是把这片空地都围起来了？
[Dialog]
[character]
[Delay(time=0.2)]
[Character(name="char_empty", name2="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=-500, fadetime=0, block=true)]
[delay(time=0.15)]
[Character(name="avg_npc_725_1#5$1", name2="char_empty",fadetime=0.5)]
[characteraction(name="left", type="move", xpos=700, fadetime=0.8, block=false)]
[delay(time=1)]
[characteraction(name="left", type="jump", times=1,power=10,xpos=-200, fadetime=0.6, block=false)]
[PlaySound(key="$d_avg_runstop")]
[delay(time=0.7)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="维恩"]呃......
[Character(name="avg_npc_725_1#5$1", name2="avg_npc_241",fadetime=0.5)]
[PlaySound(key="$d_avg_swordexsheath", volume=1)]
[Delay(time=1)]
[Character(name="avg_npc_725_1#5$1",name2="avg_npc_241",focus=2)]
[name="特别行动队士兵"]别动。
[Character(name="avg_npc_725_1#5$1",name2="avg_npc_241",focus=1)]
[characteraction(name="middle", type="shake", power=10, times=100, fadetime=0.3, block=false)]
[name="维恩"]好，好，我、我不动......您的刀，有点太近了......您不会失手吧？
[name="维恩"]......
[name="维恩"]救、救命啊苇草，我们怎么办？！
[Character(name="avg_1020_reed2_1#7$1")]
[name="苇草"]......面对这么多人，很难强行突破。
[Dialog]
[Character(name="avg_npc_242")]
[PlaySound(key="$d_avg_singleblunt",volume=1)]
[PlaySound(key="$d_avg_bldwhoosh", volume=1,delay=0.1)]
[PlaySound(key="$e_imp_sword_h", volume=1,delay=0.5)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[name="塔拉流民"]呼......啊......棍子被砍断了？
[Character(name="avg_1020_reed2_1#6$1")]
[multiline(name="苇草")]......他们，很有信心，
[Character(name="avg_1020_reed2_1#7$1")]
[multiline(name="苇草",end=true)]不想暴力抓捕我们，只是想压制住我们的抵抗。
[Character(name="avg_222_bpipe_1#7")]
[name="风笛"]嗯，这些人的身手也挺不赖的......
[name="风笛"]......我想不明白，能追到这里，他们是什么来历？
[Character(name="avg_222_bpipe_1#2")]
[name="风笛"]——等等，我见过那个人。
[name="风笛"]就在几天前，我们遇到那一队“鬼魂士兵”的时候。
[Dialog]
[character]
[delay(time=0.2)]
[Character(name="avg_npc_399_1#1$1",fadetime=0.7,block=true)]
[delay(time=1)]
[name="特别行动队队长"]......
[Character(name="avg_222_bpipe_1#6")]
[name="风笛"]这么说，你们不是特伦特郡的驻军，不该越权来逮捕这些流民的。
[name="风笛"]你们这样不守规矩的话，我们也只好动真格了。
[Character(name="avg_npc_399_1#1$1")]
[name="特别行动队队长"]“不守规矩”这个词，对你也一样适用。既然你的破城矛已经卸掉弹药，你就应该远离战场，士兵。
[Character(name="avg_222_bpipe_1#5")]
[name="风笛"]可是，这里本来就不该是战场呀？篝火都还没有熄灭呢......
[Character(name="avg_1020_reed2_1#7$1")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=20, randomness=90, fadeout=true, block=false)]
[name="苇草"]——小心！
[Dialog]
[character(fadetime=0)]
[stopmusic(fadetime=1)]
[Character(name="avg_4017_puzzle_1#1$1",blackstart=0.2,blackend=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$p_atk_knifethrow_n", volume=0.7)]
[PlaySound(key="$d_avg_humanchange", volume=1,delay=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
黑色的匕首无声地滑出，尖刃没有反射出寒光，而是划出一道烟雾。
[Dialog]
[Character]
匕首仅仅威胁性地指向风笛的喉咙，而握着它的人从始至终，视线都停留在苇草身上。
苇草从对方那双锐利的眼睛里清晰地读出，这一切都是冲着自己而来。
[Dialog]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Character(name="avg_4017_puzzle_1#8$1",fadetime=1,block=true)]
[delay(time=1)]
[name="菲舍尔"]你的长枪上，不该燃烧着火焰吗？
[Dialog]
[character(fadetime=0)]
[Character(name="avg_4017_puzzle_1#8$1",name2="avg_1020_reed2_1#7$1",focus=2)]
[name="苇草"]......
[Character(name="avg_4017_puzzle_1#8$1",name2="avg_1020_reed2_1#7$1",focus=1)]
[name="菲舍尔"]比起徒劳地抵抗，我更希望你能够明智地选择放下武器，听我说明来意。
[Dialog]
[character(fadetime=0)]
[Character(name="avg_4017_puzzle_1#1$1")]
[name="菲舍尔"]我对塔拉人没有敌意，更不打算伤害平民以示报复。在保护大众免于祸端的立场上，我与你们应该是站在一起的。
[Dialog]
[PlaySound(key="$d_avg_scroll",volume=1)]
[delay(time=1)]
[Character(name="avg_4017_puzzle_1#1$1")]
[name="菲舍尔"]这是政府文件。
[Character(name="avg_222_bpipe_1#5")]
[name="风笛"]欸，市议会的调查令？
[Dialog]
[PlaySound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[Character(name="avg_222_bpipe_1#4")]
[name="风笛"]......
[Dialog]
[Character(fadetime=0.5)]
[PlaySound(key="$d_avg_armour",volume=1)]
[delay(time=1.5)]
前维多利亚士兵放下了手中的武器。
[Dialog]
[Character(name="avg_4017_puzzle_1#8$1",name2="avg_1020_reed2_1#7$1",focus=1)]
[name="菲舍尔"]依照特伦特郡市议会的决定，我将对一桩纵火案里被人遗漏的疑点进行调查。
[Character(name="avg_4017_puzzle_1#8$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]......我，没有别的选择，对吗？ 
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2,block=true)]
[stopmusic(fadetime=1.5)]
[Character]
[Background(image="bg_coldforest",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="年幼的塔拉流民"]呜，呜呜......
[Character(name="avg_npc_241")]
[name="看守士兵"]——干什么？安静点。
[Dialog]
[Character]
[PlaySound(key="$d_avg_catsmell",volume=1)]
[name="年幼的塔拉流民"]......（抽泣）
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_725_1#1$1")]
[name="维恩"]......
[Character(name="avg_npc_725_1#2$1")]
[name="维恩"]（唉，真难受。）
[Character(name="avg_npc_725_1#6$1")]
[name="维恩"]（我过去一直想，要死的话，至少该先写好遗书......）
[Character(name="avg_npc_242")]
[name="塔拉流民"]（要我说，你早该写了。）
[Character(name="avg_npc_725_1#6$1")]

... (全文18187字符)
```

### level_act22side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_coldforest",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_241",fadetime=0.7,block=true)]
[delay(time=1)]
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_241",focus=2)]
[name="看守士兵"]我知道你在想什么，但你的大呼小叫可不会分散我们的注意力。
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_241",focus=1)]
[name="塞尔蒙"]真的？那边似乎有打起来的响动，你们不用去支援？
[Character(name="avg_npc_724_1#7$1",name2="avg_npc_241",focus=2)]
[name="看守士兵"]安静。
[Character(name="avg_npc_724_1#6$1",name2="avg_npc_241",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="塞尔蒙"]哈，别对我大喊大叫的，维多利亚人！
[Dialog]
[Character(name="avg_npc_724_1#6$1",name2="avg_npc_241")]
[Delay(time=0.5)]
[PlaySound(key="$bullet_loading",volume=0.8)]
[PlaySound(key="$d_avg_gunload",volume=1,delay=0.7)]
[delay(time=1.2)]
[Character(name="avg_npc_724_1#5$1",name2="avg_npc_241",focus=1)]
[characteraction(name="left", type="shake", power=5, times=100, fadetime=0.3, block=false)]
[name="塞尔蒙"]咕——！
[Character(name="avg_npc_724_1#5$1",name2="avg_npc_241",focus=2)]
[name="看守士兵"]安静，不然小心自己的头骨碎开。
[Character(name="avg_npc_724_1#6$1",name2="avg_npc_241",focus=1)]
[name="塞尔蒙"]你们......维多利亚人，凭什么？
[Character(name="avg_npc_724_1#6$1",name2="avg_npc_241",focus=2)]
[name="看守士兵"]不要太把自己当回事，塔拉人。我对你们没有什么偏见或者仇恨，最多觉得你们可悲。
[name="看守士兵"]你们不过是一支被利用的政治势力，公爵的一枚棋子。
[name="看守士兵"]出于礼貌，我们对你们已经很友善，但要知道，一帮流民死在这里，不会给我们带来任何损失。
[Dialog]
[Character(fadetime=0.3)]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_241")]
[name="看守士兵"]......来命令了吗？
[name="看守士兵"]如果需要支援，我们就按照队长的安排，先处理这里的人。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2,block=true)]
[Character]
[Background(image="34_g9_tent",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[Character(name="avg_npc_241")]
[name="特别行动队士兵"]目标往一队方向逃脱，一二队保持追击，其余人后撤。
[name="特别行动队士兵"]给她们会合的机会，一并逮捕。
[Dialog]
[Character(fadetime=1)]
[Delay(time=1)]
[Character(name="char_empty", name2="avg_1020_reed2_1#6$1")]
[delay(time=0.2)]
[characteraction(name="left", type="move", xpos=-500, fadetime=0.3, block=true)]
[delay(time=0.5)]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="left", type="move", xpos=500, fadetime=1, block=false)]
[Character(name="avg_222_bpipe_1#2", name2="avg_1020_reed2_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_222_bpipe_1#2",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]苇草，你是怎么摆脱那个调查官的？我跟陈陈正要去救你！
[Character(name="avg_222_bpipe_1#2",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]......
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="风笛"]哎，别发呆呀。
[name="风笛"]这边人少，我们抓紧机会突围！
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#7$1",focus=2)]
[name="苇草"]......其他人......还在树林那边吗？
[Character(name="avg_222_bpipe_1#1",name2="avg_1020_reed2_1#7$1",focus=1)]
[name="风笛"]应该是。我们先想办法冲出去，然后去救他们！
[Dialog]
[Character(name="avg_npc_662_1#1$1")]
[delay(time=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_atk_arrow_h", volume=1)]
[PlaySound(key="$d_avg_arrow_rain", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing2")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[delay(time=0.2)]
[PlaySound(key="$d_avg_pendrop",volume=0.7)]
[delay(time=1)]
[name="陈"]——有弩手？
[Character(name="avg_npc_241")]
[name="特别行动队士兵"]你们真以为能逃脱？
[Character(name="avg_npc_662_1#7$1")]
[name="陈"]这些弩手之前没有出手过。
[name="陈"]他们还有埋伏，数量未知。
[Character(name="avg_npc_662_1#3$1")]
[name="陈"]我们能被这么多精锐战力迎接，真挺有排面。
[Character(name="avg_222_bpipe_1#6",name2="avg_1020_reed2_1#7$1",focus=1)]
[name="风笛"]可是不管有多少人，现在也只能一个一个打过去了。
[Character(name="avg_222_bpipe_1#6",name2="avg_1020_reed2_1#7$1",focus=2)]
[name="苇草"]不......等等，风笛。
[name="苇草"]除我们之外，他们还要面对其他对手......
[Character(name="avg_222_bpipe_1#2",name2="avg_1020_reed2_1#7$1",focus=1)]
[name="风笛"]欸，你说得对。他们在调度队伍。
[Character(name="avg_npc_662_1#1$1")]
[name="陈"]......执行很快，应该是事先确定的作战计划。眼前可能是有意留给我们的缺口。
[Character(name="avg_222_bpipe_1#4")]
[name="风笛"]可是，这荒野上难道还有人会来吗......
[Character(name="avg_npc_241")]
[name="特别行动队士兵"]敌对武装部队出现！
[name="特别行动队士兵"]投弹准备，警惕诱饵小队。
[Character(name="avg_222_bpipe_1#7")]
[name="风笛"]......
[Dialog]
[character(fadetime=0)]
[PlaySound(key="$d_gen_soldiersrun",volume=1)]
[Character(name="avg_npc_244",name2="avg_npc_244",fadetime=1,block=true)]
[delay(time=2.5)]
[Character(fadetime=0.5)]
从黑夜中现身的部队，与小丘郡街道上浮现的鬼魂如出一辙。
风笛握紧了手中的破城矛。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement",volume=0.7)]
[Character(name="avg_222_bpipe_1#4")]
[name="风笛"]......深池。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[Character]
[Background(image="bg_coldforest",screenadapt="coverall")]
[Delay(time=0.5)]


... (全文25171字符)
```

### level_act22side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_727_1#8$1",fadetime=0.7,block=true)]
[delay(time=1)]
[name="沃里克伯爵"]年轻的诗人啊，我无法给你答案。让后来的人回答吧！
[name="沃里克伯爵"]正好，今晚我还有一件重要的事情必须告诉各位。
[Character(name="avg_npc_727_1#1$1")]
[name="沃里克伯爵"]——这恐怕是我们“塔拉人之家”最后一次相聚了。
[Character(name="avg_npc_175")]
[name="风趣的贵族"]哎呀，伯爵阁下，您在说什么呢？我们的事业，难道不是刚刚开始吗？
[Character(name="avg_npc_727_1#8$1")]
[name="沃里克伯爵"]不用害怕，塔拉人寻找自我的事业，的确刚刚开始。将要消失的，只是我个人主导的小小集会而已。
[name="沃里克伯爵"]——你说是吗，我忠心耿耿的侍从？
[Character(name="avg_npc_727_1#5$1")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="沃里克伯爵"]咳，咳咳......
[character(name="avg_npc_418_1#1$1")]
[name="伯爵侍从"]......抱歉，阁下，我只是个仆人，不懂这些。
[name="伯爵侍从"]外面雪已经很大了，您的身体不好......我随时为您备车。
[Character(name="avg_npc_727_1#8$1")]
[name="沃里克伯爵"]不必了。
[name="沃里克伯爵"]威廉姆斯先生，你愿意陪我在这风雪天里走一段路吗？
[Character(name="avg_npc_239")]
[name="衣着朴素的诗人"]......荣幸之至，阁下。我寄身的旅社，原本也没有柴火，风雪天不是大碍。
[Character(name="avg_npc_727_1#5$1")]
[name="沃里克伯爵"]是吗？......是啊，我没有阻止议会实施针对塔拉人街区的冬季税务法令。
[name="沃里克伯爵"]这样阴冷的天气，是应该有一簇火的。
[Character(name="avg_npc_727_1#1$1")]
[name="沃里克伯爵"]走吧，也许我们可以再聊一聊你的剧作，还有你自乡间采撷的故事，以及塔拉本来应有的模样。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[Character]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Subtitle(text="“愿死亡将我们与一切传奇相连。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character]
[Background(image="bg_coldforest",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0.2,r=1, g=1, b=1, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_724_1#7$1")]
[name="塞尔蒙"]安静，你们听到那个过来的脚步声了吗？那么重，是不好对付的士兵。
[Character(name="avg_npc_724_1#6$1")]
[name="塞尔蒙"]走走走，我们往另一个方向躲！
[Character(name="avg_npc_728_1#1$1")]
[name="莫兰"]篝火还在燃烧......我可以去抽一根木柴做火把。
[Character(name="avg_npc_724_1#1$1")]
[name="塞尔蒙"]行，等会儿我跟你去。
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_724_1#3$1")]
[name="塞尔蒙"]喂——苇草！听得到吗！
[Character(name="avg_npc_242")]
[name="塔拉流民"]苇草——
[Character(name="avg_npc_724_1#6$1")]
[name="塞尔蒙"]没有回应......这边，往这边躲！等下我们分两队去找她！
[name="塞尔蒙"]就算找不到苇草，也要找到风笛和陈！
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.7)]
[Character(name="avg_npc_241",name2="avg_npc_241",fadetime=1.5)]
[Delay(time=1.5)]
[name="特别行动队士兵"]......
[Character(name="avg_npc_724_1#6$1")]
[name="塞尔蒙"]......嘁。
[Character(name="avg_npc_241",name2="avg_npc_241")]
[name="特别行动队士兵"]你们敢干扰军方的行动？
[Character(name="avg_npc_724_1#3$1")]
[name="塞尔蒙"]怎么了？躲不掉就打，我又不是没跟你们维多利亚的军人交过手。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="34_g9_tent",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0.2,r=1, g=1, b=1, fadetime=1, block=true)]
[Delay(time=1)]
“苇草”。
一遍又一遍的呼喊，穿越了烟尘与浓雾。
苇草知道自己该去哪个方向。
[Character(name="avg_1020_reed2_1#6$1")]
[name="苇草"]他们不该被卷入这场纷争。我得去帮他们——
[Dialog]
[Character(name="avg_1020_reed2_1#7$1")]
[Delay(time=0.3)]
[CameraShake(duration=0.5,xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_bldwhoosh", volume=1)]
[playsound(key="$d_avg_broadswordblood",volume=0.5,delay=0.1)]
[Blocker(a=0.2, r=1, g=1, b=1, fadetime=1, block=true)]
[delay(time=1)]
[name="苇草"]——唔！
[Dialog]
[character(fadetime=0.5)]
[Delay(time=0.7)]
[Character(name="avg_npc_723_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="“校官”"]遗憾，刺偏了一些。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[Delay(time=1)]
[musicvolume(volume=0.2, fadetime=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#7$1",focus=1)]
[name="阿赫茉妮"]嗯？我不记得我曾将这件事汇报给领袖之外的任何人......
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#7$1",focus=2)]
[name="“校官”"]你总不会天真地以为，深池之中只有你一人组织了自己的情报网。
[name="“校官”"]你要动手把那个傀儡带回来，眼下恐怕也没有比我的部队更适合调动的。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#7$1",focus=1)]
[name="阿赫茉妮"]哎呀，那我真是感激不尽......你想监督我办事？还是想自己动手除掉她？
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=2)]
[name="“校官”"]如果她不再甘于影子的身份，我的剑比你的法术更快一些。
[name="“校官”"]我已经看够了无主的维多利亚人心各异，这样的闹剧，没有必要在深池继续上演。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="34_g9_tent",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Blocker(a=0.2, r=1, g=1, b=1, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_1020_reed2_1#7$1")]
[name="苇草"]你动身来追杀我了......深池是不是，已经准备好了？
[Character(name="avg_npc_723_1#1$1")]
[name="“校官”"]你是仅剩的不稳定因素。
[name="“校官”"]我以为作为一个傀儡，你至少也学会了装模作样地思考，能够将目光放得更长远一些，但你的愚善实在令人失望。
[name="“校官”"]如果你从一开始就按照鬼魂部队的行动准则，清除所有目击证人，事情本来不会一错再错，发展到现在的局面。
[Character(name="avg_1020_reed2_1#7$1")]
[name="苇草"]......

... (全文27997字符)
```

### level_act22side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g4_swamp_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_shallowswalk", volume=0.9,loop=true, channel="walksp")]
[Character(name="avg_npc_723_1#1$1",fadetime=1,block=true)]
[delay(time=1.5)]
[StopSound(channel="walksp", fadetime=1)]
[name="“校官”"]等一等，阿赫茉妮。
[name="“校官”"]前方公路关卡的驻军数量有些异常。
[Character(name="avg_4017_puzzle_1#8$1")]
[name="菲舍尔"]您注意到了？我恰好还告诉过他们留意......这里也许会发生一些破坏公爵间关系的事件。 
[Character(name="avg_npc_723_1#6$1")]
[name="“校官”"]......所以你必须赶在那些人离开特伦特郡辖区之前动手围捕，这样你留的后手才能够起效。
[Character(name="avg_npc_723_1#1$1")]
[name="“校官”"]不算意外。
[Character(name="avg_4017_puzzle_1#8$1")]
[name="菲舍尔"]......威灵顿公爵手下，赤铁近卫队的长官，当然，这个身份很快就威胁不到您了。
[name="菲舍尔"]不过，您至少很清楚，继续追击下去，事情会变成两位大公爵的领地争端。在当前维多利亚的局势下，恐怕没人想看到这样的冲突发生。
[Character(name="avg_npc_228_1#1")]
[name="阿赫茉妮"]哎呀，为什么你总是不给我留一些选择余地呢？
[name="阿赫茉妮"]不过，现在这样也够了，我的任务也已经完成了。
[Character(name="avg_4017_puzzle_1#5$1")]
[name="菲舍尔"]你的失误造成了这样的恶果。作为身份已经暴露的间谍，你没有必要再如此尽职地虚张声势。
[Character(name="avg_npc_228_1#1")]
[name="阿赫茉妮"]是吗？我可是真心希望，我们能共同为有朝一日的合作付出努力——
[Character(name="avg_npc_723_1#5$1")]
[name="“校官”"]阿赫茉妮。
[name="“校官”"]你在台上说的话已经够多了。
[Character(name="avg_npc_228_1#3")]
[name="阿赫茉妮"]咳......
[Character(name="avg_4017_puzzle_1#5$1")]
[name="菲舍尔"]......
[Character(name="avg_npc_723_1#1$1")]
[name="“校官”"]所有人，收队。
[name="“校官”"]这原本就是一场败仗，先放过他们。
[Dialog]
[playsound(key="$d_avg_shallowswalk",volume=0.9, loop=true, channel="walksp1")]
[Character(fadetime=1)]
[StopSound(channel="walksp1", fadetime=2)]
[delay(time=2)]
[Character(name="avg_npc_228_1#3")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_shallowswalk", volume=0.4, loop=true, channel="ahmnwalk")]
[Character(fadetime=1)]
[StopSound(channel="ahmnwalk", fadetime=2)]
[delay(time=2)]
[Character(name="avg_4017_puzzle_1#5$1",name2="avg_npc_399_1#1$1",focus=1)]
[name="菲舍尔"]嘶......
[Character(name="avg_4017_puzzle_1#5$1",name2="avg_npc_399_1#1$1",focus=2)]
[name="特别行动队队长"]......我提醒过你，菲舍尔。矿石病发展到一定程度之后，这些止疼药就不管用了。
[name="特别行动队队长"]现在的情况，就是你长时间持续使用源石技艺的后果。
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_399_1#1$1",focus=1)]
[name="菲舍尔"]我当然知道。
[name="菲舍尔"]......
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_399_1#1$1",focus=2)]
[name="特别行动队队长"]......好吧，如果我话说得太重，我道歉。
[Character(name="avg_4017_puzzle_1#6$1",name2="avg_npc_399_1#1$1",focus=1)]
[name="菲舍尔"]不，我只是在想......
[Character(name="avg_4017_puzzle_1#1$1",name2="avg_npc_399_1#1$1",focus=1)]
[name="菲舍尔"]尊敬的开斯特公爵竟然派来了一位“灰礼帽”。
[name="菲舍尔"]而我甚至不知道......那位公爵的密使是什么时候取代了我的人。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2,block=true)]
[Character]
[Background(image="34_g4_swamp_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_725_1#5$1")]
[name="维恩"]呼......哈......我们，我们是不是逃出来了？
[Character(name="avg_npc_662_1#1$1")]
[name="陈"]嗯，后面看不到追兵了。
[name="陈"]先停下来检查一下受伤的情况吧，及时处理。
[Character(name="avg_1020_reed2_1#2$1")]
[name="苇草"]我们......失去了几名伙伴。
[Character(name="avg_npc_662_1#7$1")]
[name="陈"]在这里等等吧，烟雾里有人被冲散了，也许还躲在树林里。
[Character(name="avg_npc_662_1#1$1")]
[name="陈"]之前你跟他们说好的前进方向是这边，如果他们还记得，应该会找过来。
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]嗯，我们只稍微停留一会儿。天就要亮了，我不会耽误你们的行程。
[name="苇草"]其他人也可以放下武器，暂时休息......
[stopmusic(fadetime=1.5)]
[Character(name="avg_1020_reed2_1#1$1",focus=-1)]
[name="风笛"]......
[Character(name="avg_1020_reed2_1#6$1")]
[name="苇草"]......风笛？
[Dialog]
[PlaySound(key="$d_avg_clothmovement",volume=0.7)]
[Image(image="34_i06", xScale=1.2, yScale=1.2,fadetime=0.2)]
[background]
[ImageTween(xFrom=200, yFrom=0, xTo=-100, yTo=-100, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.2, yScaleTo=1.2, duration=0.3, block=false)]
[Delay(time=0.3)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.7)]
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.4)]
[name="风笛"]“苇草”。
[name="风笛"]所以你就是小丘郡的那个术师。
[name="风笛"]你就是那场火的操纵者。我认识你的法术，你让整条街道变成了灰烬。
[name="风笛"]你让Outcast为救你而死。
[name="风笛"]......你就是深池的“领袖”，是吗？
[name="苇草"]......
[Dialog]
[Delay(time=1)]
所有人全都在看着她，在等一个回答。
这个问题，她从过去到现在听过许多次。每次听到的时候，她都需要拼命遏制自己摇头的欲望。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character]
[charslot]
[musicvolume(volume=0.2, fadetime=1)]
[delay(time=-0.4)]
[Image(image="34_i02",screenadapt="coverall",block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
可她想起了干草垛的触感和晚风的味道。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Image(image="34_i01",screenadapt="coverall",block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
她想起帐篷前跃动的篝火，和枪尖上的火截然不同。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[image]
[Background(image="bg_coldforest",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[bgeffect(name="$eb_dim_closeeye",layer=1)]
[bgeffect]
她想起远处还未完全消散的浓烟，那一声声呼喊仿佛仍有回声。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[background]
[Delay(time=1)]
[Subtitle(text="这一次，她不再想摇头。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Dialog]
[Image(image="34_i06", xScale=1.1, yScale=1.1,fadetime=1,x=-30,y=-30)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[ImageTween(xFrom=-30, yFrom=-30, xTo=0, yTo=0, xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=0.85, yScaleTo=0.85, duration=20, block=false)]
[Delay(time=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[name="苇草"]我是。
[name="苇草"]在小丘郡的时候，我想以死永远摆脱我的身份，所以源石炮弹落下时我没有躲开。
[name="苇草"]罗

... (全文13615字符)
```

### level_act22side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Subtitle(text="“我将我的心迹写入诗韵。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“你啊，将到来的混沌时代中的你。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“会知道我的灵魂是如何将其追寻。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5,block=true)]
[Character]
[Background(image="34_g7_galekingruins",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[Character(name="avg_npc_242",fadetime=0.7,block=true)]
[delay(time=1)]
[name="塔拉流民"]我就知道，他们不会来这堆被天灾砸烂的石头里面找人。
[name="塔拉流民"]多亏早上起了那么大的雾，不然咱们还没这么容易脱身。
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]啊，小心。我们毕竟没有防护装备，在这里受伤的话，是有感染风险的。
[Dialog]
[Character(fadetime=0)]
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]莫兰，你也是。源石多发环境，对感染者来说更加危险。
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="莫兰"]好，我会注意的。
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]......凯莉睡着了？
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="莫兰"]是，应该只是睡了，不是昏迷，我能感觉到她的呼吸还很平稳。睡着能让她少受一些痛苦。
[Character(name="avg_npc_728_1#3$1",name2="avg_1020_reed2_1#1$1",focus=1)]
[name="莫兰"]......但我还是怕，再不停下来处理凯莉的伤势的话，她撑不过去。
[Character(name="avg_npc_728_1#3$1",name2="avg_1020_reed2_1#12$1",focus=2)]
[name="苇草"]嗯。
[name="苇草"]......你们，失望吗？
[Character(name="avg_npc_728_1#6$1",name2="avg_1020_reed2_1#12$1",focus=1)]
[name="莫兰"]不会的。你不是说过了吗？我们现在不得不和一些深池士兵战斗，是因为他们不想要第二位“领袖”。
[name="莫兰"]但他们还有更大的目标，不会一直追捕我们的。
[name="莫兰"]现在这样逃亡的生活，我们也已经习惯了，可以忍耐下去。
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#12$1",focus=1)]
[name="莫兰"]不过在那之后呢？你还没有告诉过我们你的想法。
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#12$1",focus=2)]
[name="苇草"]......
[name="苇草"]我还没有把握，抱歉。
[name="苇草"]对了，废墟深处，也许有源石晶簇少一些的地方，我想去看看，能不能找到一个暂时的藏身处。
[Dialog]
[Delay(time=0.7)]
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]大家都应该停下来休息一下了。
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="莫兰"]可那个方向，是不是有人在？
[Character(name="avg_npc_728_1#3$1",name2="avg_1020_reed2_1#9$1",focus=1)]
[name="莫兰"]虽然看上去只是普通人，可我们应该也要躲开。就像你之前说的一样，这种地方有人出没，太异常了，一定要小心......
[Character(name="avg_npc_728_1#3$1",name2="avg_1020_reed2_1#6$1",focus=2)]
[name="苇草"]......
[Character(name="avg_npc_728_1#3$1",name2="avg_1020_reed2_1#12$1",focus=2)]
[name="苇草"]......不用。
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#12$1",focus=1)]
[name="莫兰"]......你看起来很害怕。怎么了？
[Character(name="avg_npc_728_1#1$1",name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]没关系，不用担心我。
[Dialog]
[Character(fadetime=0)]
[Character(name="avg_1020_reed2_1#2$1")]
[name="苇草"]（......她来过这里？在这附近？）
[Character(name="avg_npc_242")]
[name="塔拉流民"]哎，那边的人，走路的样子是不是有些奇怪？
[Character(name="avg_1020_reed2_1#7$1")]
[name="苇草"]别看。
[Character(name="avg_npc_242")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="塔拉流民"]咿——她怎么已经——
[Dialog]
[Character(name="avg_1020_reed2_1#7$1")]
[Delay(time=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$e_skill_ignite_cast", volume=0.6)]
[PlaySound(key="$d_avg_magic_1", volume=1,delay=0.7)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Delay(time=1)]
[name="苇草"]她应该，离世有一段时间了。
[Character(name="avg_1020_reed2_1#2$1")]
[name="苇草"]只是，那种源石技艺操控着这具身体在行动，就像我们之前见到的那些深池士兵一样。
[Character(name="avg_npc_728_1#3$1")]
[name="莫兰"]为什么要操纵一个普通人？
[Character(name="avg_1020_reed2_1#7$1")]
[name="苇草"]我还不知道。
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]——跟我走吧，这些被源石技艺控制的死者，我来应对。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_black",screenadapt="showall")]
[delay(time=0.5)]
[stopmusic(fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_walk_stage")]
[name="苇草"]这里光线很暗，沿着石阶往下走的时候，小心裸露的碎晶簇......莫兰，你背着凯莉方便行动吗？
[name="莫兰"]我没问题。只要你的火一直燃着，我看得见东西。
[name="苇草"]好。我们尽量往深处走，别发出太大声音。
[Dialog]
[delay(time=1)]
[name="苇草"]——
[name="莫兰"]这是......
[Dialog]
[Delay(time=0.7)]
......盖尔王的王城？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[PlayMusic(key="$calm_loop", volume=0.4)]
[Background(screenadapt="showall", image="34_g8_galekingruins_inside",x=100, y=0, xScale=1.3, yScale=1.3)]
[backgroundTween(xFrom=100, yFrom=0, xTo=-100, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=20, block=false)]
[curtain(direction = 0,fillfrom = 0,fillto = 0.2,fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0,fillto = 0.2,fadetime=0.1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=1.5)]
对于那业已覆灭的王朝，有人想象它灰石的骸骨间堆满死战不退的将士盔甲，有人声称它仍将黄金的王冠藏匿于古老阴森的机关之下。
有人以现代伦蒂尼姆的高墙去衬托王城的恢弘，以无边的克拉斯德内海比拟英雄时代美德的兴荣，又哀叹它被维多利亚的阴影日渐销蚀。
人们想象这座古城是塔拉悲情的墓碑，怨恨的亡魂。
[dialog]
[Background(image="34_g8_galekingruins_inside",screenadapt="showall",fadetime=2)]
[curtain(direction = 0,fillfrom = 0.2,fillto = 0,fadetime=3)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0,fadetime=3)]
[delay(time=3)]
但它只是安静地坐在山丘上，袒露出此地未有王城时的核心。
生出野草，爬满藤蔓。
[Dialog]
[delay(time=2)]
[Character(name="avg_npc_242")]
[name="塔拉流民"]这得是多久以前的东西了？五百年？一千年？
[Charact

... (全文16159字符)
```

### level_act22side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
她想象过一切结束的可能，哪怕德拉克的火永远无法平息。
她想象着盛怒的烈焰从她灼痛的胸口迸发，焚毁她被赋予的外壳与身份，令她从此挣脱自己的枷锁。
但当她真的去触摸自己的火焰，想要将其握住的时候，她突然在想，会不会自己从来都没有控制过它。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5,block=true)]
[Character]
[Background(image="34_g8_galekingruins_inside",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "middle", name = "avg_npc_722_1#1$1", afrom =0, ato = 0.8,duration =0.7)]
[Delay(time=1)]
[name="爱布拉娜"]做得好，拉芙希妮。
[name="爱布拉娜"]你想要我真心地夸赞你，这就够了吗？
[name="爱布拉娜"]还是说，你已经准备好了......影子要寻回自己，你想要取代我成为“领袖”？
[name="爱布拉娜"]我可以给你这个机会。你的下一簇火就能将我烧成灰烬。
[charslot(slot = "middle", name = "avg_npc_722_1#4$1", afrom =0, ato = 0.8,duration =0)]
[name="爱布拉娜"]你要......向我伸出手吗？
[charslot(slot="middle",name="avg_1020_reed2_1#12$1")]
[name="苇草"]......
[Dialog]
[charslot]
火焰燃烧着，她的影子微微摇动。
但苇草移开了视线。
不远处刚刚醒来的凯莉在垫着的旧围裙上慢慢地撑起身体，莫兰哼着歌帮她清洗伤口。
[Dialog]
[charslot(slot="middle",name="avg_1020_reed2_1#1$1")]
[name="苇草"]......姐姐，你为什么会来这里？
[name="苇草"]站在这里的时候，你看到的是什么？
[Dialog]
[charslot]
那天夜里的篝火很明亮。
那时，维恩正走来走去祈求新的落脚地好做生意，塞尔蒙给自己的武器缠上更多铁丝。
大家开着玩笑叫她领袖，又认真地说，多谢她把大家领到这里。
[Dialog]
[charslot(slot="middle",name="avg_1020_reed2_1#1$1")]
[name="苇草"]我听说，维多利亚人为盖尔王授衔，然后才在仪式石阵的上方建起了王城。
[name="苇草"]在那以前......它先是塔拉人栖居的家园。
[Dialog]
[charslot]
她想起很早以前的节日冬夜。
她们在壁炉前换上一模一样的新外套，留下了一张两人都微笑着的照片。
那是令人喜爱的......一小团温暖的火。
[Dialog]
[charslot(slot="middle",name="avg_1020_reed2_1#9$1")]
[name="苇草"]所以......不。
[name="苇草"]自己是影子，这件事，我不在乎。
[name="苇草"]但我不是你的影子。我只是，人们理想中“领袖”的影子。
[name="苇草"]他们想要一条逃生的路，想找回自己的生活，而我恰好在那里，被他们所需要。
[name="苇草"]姐姐，我为什么要战胜你呢？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[charslot]
[Background(image="34_g8_galekingruins_inside",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_243",name2="avg_npc_728_1#6$1",focus=2)]
[name="莫兰"]不怕死？请别这么说，凯莉，怕死也不是一件坏事。
[name="莫兰"]我们还没有帮到其他塔拉人，就死在同样想救塔拉人的深池手里，多遗憾。
[Character(name="avg_npc_243",name2="avg_npc_728_1#6$1",focus=1)]
[name="塔拉流民"]......你啊，比以前，能说会道多了。
[multiline(name="塔拉流民")]还好，我们还有消炎药......
[characteraction(name="left", type="shake", power=5, times=2, fadetime=0.02, block=true)]
[multiline(name="塔拉流民")]嘶......
[Character(name="avg_npc_243",name2="avg_npc_728_1#4$1",focus=2)]
[name="莫兰"]弄疼你了？抱歉......
[Character(name="avg_npc_243",name2="avg_npc_728_1#6$1",focus=2)]
[name="莫兰"]啊，苇草，你回来了。
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Character(name="avg_1020_reed2_1#1$1",fadetime=1,block=true)]
[Delay(time=1.5)]
[name="苇草"]我们今晚躲在这里的话，应该不会再遇到那些被源石技艺控制的死者。
[Character(name="avg_npc_728_1#1$1")]
[name="莫兰"]你去检查附近的情况了？那就好。
[Character(name="avg_npc_728_1#4$1")]
[name="莫兰"]我也希望能多停留一段时间，凯莉的伤......情况很差。
[Character(name="avg_1020_reed2_1#12$1")]
[name="苇草"]......
[Character(name="avg_npc_243")]
[name="塔拉流民"]怎么，你的表情......
[name="塔拉流民"]......呵呵，我还记得，一开始，我们把你当成医生，后来才知道，我们所有人，都只是负伤的人。
[name="塔拉流民"]我的伤，很严重？
[Character(name="avg_1020_reed2_1#9$1")]
[name="苇草"]不，不是那样......你的伤是可以痊愈的，不用这么担心。
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]......只是，你们害怕我的火吗？
[Character(name="avg_npc_728_1#6$1")]
[name="莫兰"]当然不会。
[Character(name="avg_1020_reed2_1#9$1")]
[name="苇草"]......
[Dialog]
[Character(fadetime=0.5)]
于是她向眼前受伤的塔拉人伸出手。
德拉克的怒火在她的血液中翻涌。昔日红龙替他的子民流血，一滴血便烧毁整片原野。
她咽下炙热的吐息，被抑制的火灼烧着她。
但如果，这样能抚平伤痛，她愿意忍受。
[Dialog]
[PlaySound(key="$p_field_healfield_loop", volume=0.6, channel="heal", loop=false)]
[delay(time=1)]
[soundvolume(channel="heal",volume=0,fadetime=2)]
——她的手中并未真的燃起火焰，甚至没有任何光芒闪过。
只是所有人都产生了一种感觉——生命在流淌，轻柔得像清晨里的第一次睁眼。
[Dialog]
[Character(name="avg_npc_243",fadetime=0.7,block=true)]
[Delay(time=1)]
[name="塔拉流民"]呼......
[Character(name="avg_npc_728_1#1$1")]
[name="莫兰"]看你的表情......感觉好受一些了？
[Character(name="avg_npc_243")]
[name="塔拉流民"]是啊......你啊，苇草，难道你真的是医生？但是医生也不是像你这样办事的呀。
[Character(name="avg_1020_reed2_1#6$1")]
[multiline(name="苇草")]......
[Character(name="avg_1020_reed2_1#9$1")]
[multiline(name="苇草",end=true)]不，只是，这终于是我自己的火焰了。
[Character(name="avg_1020_reed2_1#9$1")]
[name="苇草"]愿你今晚能睡个好觉，凯莉。
[Dialog]
[stopmusic(fadetime=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=4, block=true)]
[Character]
[delay(time=5)]
[Background(image="34_g11_hispdwarshipdeck",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$stranger_intro", key="$stranger_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_241",name2="avg_npc_406_1#1$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_241",name2="avg_npc_406_1#1$1",focus=1)]
[name="维多利亚军官"]我从未想过，维多利亚军队之外的人，也能登上这艘高速战舰。
[Character(name="avg_npc_241",name2="avg_npc_406_1#1$1",focus=2)]
[name="深池军官"]我以为在它降下维多利亚旗帜的时候，你们就该想到这一点。
[Character(name="avg_npc_241",name2="avg_npc_406_1#1$1",focus=1)]
[name="维多利亚军官"]我对你没有敌意，塔拉人，我只是对你们的军事素养，还有你们那位领袖感到好奇。
[name="维多利亚军官"]我不希望公爵难得的客人，只是倚仗了自己的德拉克血统。
[Character(name="avg_npc_241",name2="avg_npc_406_1#1$1",focus=2)]
[name="深池军官"]你的骨子里充满对我们的傲慢，维多利亚人。
[name="深池军官"]可等她登上台开始演讲，你会发现，她才是这艘战舰上所有势力的主人。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_avg_snowstormflp",channel="wind",volume=0.4,  loop=true)]
[Character]
[Character(name="avg_npc_729_1#1$1")]
[Background(image="34_g2_reedmarshes",screenadapt="coverall",xScale=1.3, yScale=1.3,y=50)]
[Delay(time=1)]
[PlaySound(key="$d_avg_reedmarshes", volume=0, loop=tru

... (全文17986字符)
```

### level_act22side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
八年前
1090年
橡林郡
[dialog]
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",fadetime=0.7)]
[delay(time=1)]
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=1)]
[name="风趣的贵族"]伯爵阁下，不少人都在打听您，想要了解我们下一步的行动计划。
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=1)]
[name="风趣的贵族"]多亏了您的支持，我们的剧目大获成功。
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=1)]
[name="风趣的贵族"]塔拉人自己的剧院，塔拉人自己的历史，首场演出就有两百人前来观看，多么令人欢欣鼓舞。
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=1)]
[name="风趣的贵族"]接下来，我们可以寻求与麦卡内尼男爵领地上的数家工厂合作，或者接受这几名银行家的联合邀约......
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]这些事情请在宴会后再谈吧，珀斯爵士。或者，您交给一个打字员去安排，也不会出太多差错。
[character(name="avg_npc_175",name2="avg_npc_727_1#8$1",focus=2)]
[name="沃里克伯爵"]今天的宴会上，我们最好只谈论刚结束的演出，谈论塔拉的文明，抛下那些维多利亚人的繁文缛节和奔走钻营。
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]各位，这些身份和礼仪，这些高雅的语句，我们赖以交流思想的体面词汇，全都是维多利亚人教给我们的。
[character(name="avg_npc_175",name2="avg_npc_727_1#2$1",focus=2)]
[name="沃里克伯爵"]这些东西就和维多利亚人的机器一样，让塔拉人的身心都染上了现代病。
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]原本我们只知道我们天性里的高洁与勇毅，我们那继承自盖尔王的血液只要听到战斗的号令就激动不已......
[character(name="avg_npc_175",name2="avg_npc_727_1#6$1",focus=2)]
[name="沃里克伯爵"]但现在，我们学会了维多利亚人的精明与虚荣，以至于面对一项正确的事业，一种理想的感召，许多人却只能在其中进行利益的博弈。
[character(name="avg_npc_175",name2="avg_npc_727_1#6$1",focus=2)]
[name="沃里克伯爵"]不仅我们自身如此，我们在大街上时常看到的，小市民中的塔拉人，也是如此。
[character(name="avg_npc_175",name2="avg_npc_727_1#6$1",focus=2)]
[name="沃里克伯爵"]他们因为沾染了维多利亚人的恶德，而变成矿石病人，变成无赖与暴徒。
[character(name="avg_npc_175",name2="avg_npc_727_1#1$1",focus=1)]
[name="风趣的贵族"]您说得真好，伯爵阁下——
[Dialog]
[musicvolume(volume=0.2, fadetime=0.5)]
[character(fadetime=0.3)]
[delay(time=0.5)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[PlaySound(key="$bottlebroken", volume=0.6)]
[delay(time=1.5)]
[character(name="avg_npc_239",fadetime=0.5)]
[delay(time=0.5)]
[name="衣着朴素的诗人"]——抱歉，我失手打碎了酒杯。
[dialog]
[musicvolume(volume=0.4, fadetime=1)]
[character]
[Dialog]
[charslot(slot = "left", name = "avg_npc_239")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "right", name = "avg_npc_727_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1,isblock=false)]
[delay(time=1.5)]
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]看来您的杯子有话要说。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=1)]
[name="衣着朴素的诗人"]我也想问问您的看法，伯爵阁下。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]......原谅我这记性吧，请问您是......？
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=1)]
[name="衣着朴素的诗人"]威廉姆斯，诗人，今晚那一出戏剧的执笔人。但您不必费心记住我的名字，我在文坛还不能说有什么建树。
[character(name="avg_npc_239",name2="avg_npc_727_1#8$1",focus=2)]
[name="沃里克伯爵"]威廉姆斯先生，别客气。我说过，我最不喜欢维多利亚人的繁文缛节。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]请问吧。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=1)]
[name="衣着朴素的诗人"]......您将塔拉人比作染病之人，那您认为，我们要如何自愈？要怎么去救治其他塔拉人？
[character(name="avg_npc_239",name2="avg_npc_727_1#9$1",focus=2)]
[name="沃里克伯爵"]恐怕我们无论多么努力，都不能根治我们身上的疾病，就像已经浑浊的水不能再将自己洗净。
[character(name="avg_npc_239",name2="avg_npc_727_1#9$1",focus=1)]
[name="衣着朴素的诗人"]所以您认为，那些无赖与暴徒，我们是不可能救助的。
[character(name="avg_npc_239",name2="avg_npc_727_1#9$1",focus=1)]
[name="衣着朴素的诗人"]您不相信他们其实缺少知识和教育，而我们的笔能够帮助他们吗？
[character(name="avg_npc_239",name2="avg_npc_727_1#5$1",focus=2)]
[name="沃里克伯爵"]唉，太过精致的知识正是我们的敌人。
[character(name="avg_npc_239",name2="avg_npc_727_1#6$1",focus=2)]
[name="沃里克伯爵"]当然，我们写，我们呐喊，我们梦想一个塔拉的理想国......我们试图唤醒血脉中沉睡的，关于塔拉的记忆。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]但你我将是不得不留在这个旧时代的人。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]您看，我很喜欢您的剧作，只是，我们都不得不使用维多利亚的语言。
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=1)]
[name="衣着朴素的诗人"]......
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]“我放下战士的荣誉，只为以后塔拉的土地不必再被鲜血浸泡，德拉克的同族不必再刀剑相向。”
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=2)]
[name="沃里克伯爵"]“除非有朝一日，红龙的火焰能令死去的战士从熔炉中复生。”
[character(name="avg_npc_239",name2="avg_npc_727_1#1$1",focus=1)]
[name="衣着朴素的诗人"]承蒙您的谬爱，这些只是民间歌谣的记录，我做的最多不过是音韵上的润色。
[character(name="avg_npc_239",name2="avg_npc_727_1#9$1",focus=2)]
[name="沃里克伯爵"]不，我只是在想......
[character(name="avg_npc_239",name2="avg_npc_727_1#8$1",focus=2)]
[name="沃里克伯爵"]塔拉未必不会再有下一条红龙。
[character(name="avg_npc_239",name2="avg_npc_727_1#8$1",focus=2)]
[name="沃里克伯爵"]毕竟，如今我们谁也没见过德拉克，又怎么知道自己身边走过的人其实不是瓦伊凡呢？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0, block=true)]
[Background(image="25_mini02_victoria_street_n",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
1098年
石高原野，红脊镇
[dialog]
[character(name="avg_1020_reed2_1#1$1",fadetime=0.7,block=true)]
[delay(time=1)]
[name="苇草"]......
[character(name="avg_1020_reed2_1#1$1",focus=-1)]
[name="巡逻队队员"]找到了，在大街上活动的人就这两个。刚才砸碎窗户玻璃的声音一定是他们弄出来的。
[dialog]
[character(name="avg_1020_reed2_1#1$1")]
[Delay(time=0.5)]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=3)]
[character(name="avg_npc_248",name2="avg_npc_248")]
[name="巡逻队队员"]喂，你们俩老实点，不然下次绳子就不是套在你们的手腕上了。
[character(name="avg_npc_

... (全文25387字符)
```

### level_act22side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_4017_puzzle_1#1$1",fadetime=0.7,block=true)]
[Delay(time=1)]
[name="菲舍尔"]......“阿赫茉妮”的间谍身份得以确认，但她安插的情报人员已经全部在掩护下提前撤离。
[name="菲舍尔"]那名感染者的确是另一条德拉克。她的动向已经在我们的掌控之中，只要得到指令，我的部队会继续追捕。
[Character(name="avg_4017_puzzle_1#10$1")]
[name="菲舍尔"]......另外，恕我冒昧，请问在屏风后听取汇报的人，您是头领，还是......公爵阁下？
[Dialog]
[Character(name="avg_npc_726_1#7$1",fadetime=1,block=true)]
[Delay(time=1)]
[name="开斯特公爵"]你很敏锐，上一个能指出这一点的孩子，我已经不记得是在几年前遇见的了。
[name="开斯特公爵"]抱歉，我只是想享用完这杯红茶。请坐过来吧。
[Character(name="avg_4017_puzzle_1#10$1")]
[name="菲舍尔"]......
[Character(name="avg_4017_puzzle_1#1$1")]
[name="菲舍尔"]不，作为感染者，我站在这里就好。
[Character(name="avg_npc_726_1#1$1")]
[name="开斯特公爵"]你来的时候，看到街角那家小剧院了吗？
[Character(name="avg_4017_puzzle_1#1$1")]
[name="菲舍尔"]是，我看到了......剧院没有开张，也没有可疑的人在附近徘徊。
[Character(name="avg_npc_726_1#1$1")]
[name="开斯特公爵"]那是一些自称塔拉人的艺术家建起的剧院，每晚那里都会上演基于塔拉文化创作的剧目。
[Character(name="avg_4017_puzzle_1#10$1")]
[name="菲舍尔"]......需要我去调查他们吗？
[Character(name="avg_npc_726_1#1$1")]
[name="开斯特公爵"]不，我很欣赏他们的存在。
[name="开斯特公爵"]追捕那条德拉克的事，你不用担心，我会交给其他人去做。你带来的情报很有价值，以你的才能，不必把时间消耗在收尾的工作上。
[Character(name="avg_npc_726_1#7$1")]
[name="开斯特公爵"]我想请你，为我去特定地点监视威灵顿公爵的行动。
[Character(name="avg_4017_puzzle_1#1$1")]
[name="菲舍尔"]......是，感谢您的赏识。
[Character(name="avg_npc_726_1#1$1")]
[name="开斯特公爵"]对了，之前那个问题，你想好答案了吗？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2,block=true)]
[Character]
[Background(image="34_g1_victoriavillage",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[Character(name="avg_npc_729_1#1$1")]
[name="受伤的流民"]哎，信使小姐，你能把信捎多远？多远都行？
[name="受伤的流民"]那，你能帮忙写信吗？
[name="受伤的流民"]就写几句话，我只是想跟家里人说一声我还活着......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1,block=true)]
[Character]
[Background(image="34_g1_victoriavillage",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]刚刚那位农户说的，你们应该听到了。这里定时会有商队路过，半小时后就会有一支。
[name="苇草"]你们跟着商队走，能藏进载具的话，最好。靠近橡林郡的地区，应该是威灵顿公爵直属的领地，他不会容许针对塔拉人的暴行。
[name="苇草"]错过这次机会的话，会很危险。搜捕队从附近的移动城市赶到这里，以最快的速度，应该不用一小时。
[Character(name="avg_1020_reed2_1#9$1")]
[name="苇草"]......但你们只要能逃出去，之后的生活就不用太担心。那些人想要的是我，跟丢了你们的踪迹之后，他们不会再追的。
[Character(name="avg_npc_725_1#4$1")]
[name="维恩"]呃，等等......所以，风笛说你是什么深池的领袖，不是我听错了？
[Character(name="avg_1020_reed2_1#9$1")]
[name="苇草"]嗯，如果你们之中还有人想要跟着深池战斗，可以和我一起，继续走。
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]但深池的身份没有办法成为你们的保护伞。之后的路，或许也会像现在一样......被很多人监视，继续被人追赶。
[Dialog]
[Character(fadetime=0)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Character(name="avg_npc_729_1#1$1",fadetime=1,block=true)]
[Delay(time=1.5)]
[name="受伤的流民"]我回来了，嘿。
[name="受伤的流民"]我照着你的话跟她说了，说我跟村里逃出来的人一起，在这边落脚了，然后编了个石高原野上找不到的地名。
[name="受伤的流民"]......可那个信使看起来人挺好的，要是她是真的信使，不是来查我们动向的人，那我不是害得她白跑一趟？
[Character(name="avg_1020_reed2_1#1$1")]
[name="苇草"]......我大部分时间，都过着东躲西藏的生活。像她那样假扮信使的追踪者，我见过许多。
[Character(name="avg_npc_729_1#1$1")]
[name="受伤的流民"]唉，好吧。以后还要继续这么过。
[Character(name="avg_npc_242")]
[name="塔拉流民"]别叹气了，我们抓紧时间分一分手上的物资。
[name="塔拉流民"]你这样受伤了的，就别勉强自己跟着苇草走了。为塔拉人打仗的事，我们帮你。
[Character(name="avg_npc_729_1#1$1")]
[name="受伤的流民"]哈哈，那我这算不算是，已经为塔拉人打过啦......
[Character(name="avg_npc_725_1#1$1")]
[name="维恩"]......苇草，过来过来。
[name="维恩"]我得跟你说件事。
[Dialog]
[Character(fadetime=0)]
[Character(name="avg_npc_725_1#1$1", name2="char_empty")]
[Delay(time=0.2)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_725_1#1$1", name2="avg_1020_reed2_1#9$1",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_725_1#1$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]本来我是写在遗书上的，唉，但我活下来了嘛。
[Character(name="avg_npc_725_1#1$1", name2="avg_1020_reed2_1#9$1",focus=2)]
[name="苇草"]嗯。怎么了？
[Character(name="avg_npc_725_1#1$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]......
[Character(name="avg_npc_725_1#2$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]......一开始，用锄头砸倒那个士兵，害得所有人都得逃跑的人，是我。
[Character(name="avg_npc_725_1#1$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]那天晚上，我见到当兵的在打人，打图利家的小女儿，就从别人家的墙根抄了一把锄头，摸了过去。
[Dialog]
[characteraction(name="left", type="shake", power=2, times=60, fadetime=0.4, block=true)]
[delay(time=0.8)]
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]我是不是抖得厉害？......真对不起，唉。过去这么久了，我还老是梦见那个场景。
[name="维恩"]女孩才十四岁，尖声尖气的，哭得让人心慌。
[name="维恩"]我想，天那么黑，也不许点灯，就算这一锄头砸破了头，流了血，样子再怎么惨，我也看不清楚。
[Character(name="avg_npc_725_1#5$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]我就是......我没想到害了那么多人。
[name="维恩"]后来我想陪着他们，给所有人想办法安顿下来，自己再离开，算是偿还我犯的错......
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#9$1",focus=1)]
[name="维恩"]可是有的人最后也没能走到落脚的地方。
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#6$1",focus=2)]
[name="苇草"]......证件不齐的罪名，是你给自己编的吗？
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#6$1",focus=1)]
[name="维恩"]唉，对不起。
[name="维恩"]一开始通缉令上面没有我，我怕他们起疑心，才特地跟费加尔一块去抢药店......结果又把你也牵扯进来。
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#1$1",focus=2)]
[name="苇草"]不要这么说，维恩。我的身份，总有一天会追上我。
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#2$1",focus=2)]
[name="苇草"]......塔拉人的悲哀，也总有一天会追上每个人。
[Character(name="avg_npc_725_1#6$1", name2="avg_1020_reed2_1#2$1",focus=1)]
[name="维恩"]......好，好，唉。
[Dialog]
[Character(fadetime=0.5)]
[delay(time=1)]
[Character(nam

... (全文13470字符)
```

### level_act22side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g11_hispdwarshipdeck",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_loop", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget", volume=0.6)]
[delay(time=1)]
[name="电台通讯声"]前方小雨天气，航道已确认，沿途侦测站将默认放行。
[name="电台通讯声"]收到道森子爵的电报，对方希望借此次放行的契机，与深池代表会面。
[Dialog]
[PlaySound(key="$transmission",volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",fadetime=0.7,block=true)]
[delay(time=1)]
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#7$1",focus=2)]
[name="“校官”"]又是一些倒向我们的贵族。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#7$1",focus=1)]
[name="阿赫茉妮"]放心吧，领袖不打算对他们有什么表示。
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#7$1",focus=1)]
[name="阿赫茉妮"]只是简单示好就想获得深池的和平保证，控制住领地内塔拉人的激昂情绪，是不是有点太吝啬了？
[name="阿赫茉妮"]他们迟早要学会，怎么付出代价才算诚意十足。
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#8$1",focus=2)]
[name="“校官”"]领袖依然派你去交涉？
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#8$1",focus=1)]
[name="阿赫茉妮"]或许我更需要花一段时间，让大家先忘记我。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=2)]
[name="“校官”"]是个好消息。以我的标准，你失误的行动不少。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=1)]
[name="阿赫茉妮"]呵呵......既然你独自登舰汇报，看来，你还是没抓到拉芙希妮。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=2)]
[name="“校官”"]你不必明知故问。
[name="“校官”"]你阻拦了我的队伍继续搜捕，事后又把她去过的地点暗示给我的士兵，这种搭救方式于你而言，算不上高明。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=1)]
[name="阿赫茉妮"]你又怎么知道，我搭救的不是你呢？
[name="阿赫茉妮"]我记得，领袖从来没有说过自己想处死她吧？
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=2)]
[name="“校官”"]领袖允许她肆意逃窜，也同样允许我自行判断，要如何对待她。
[name="“校官”"]不要怪我对你的熟人太过苛刻，阿赫茉妮。没人能放任一条德拉克在眼下的维多利亚随意行动。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=1)]
[name="阿赫茉妮"]别在意，我想我和她的关系也没有那么好。
[name="阿赫茉妮"]你瞧，我正打算去她此前藏身的那家医疗公司看看。
[name="阿赫茉妮"]呵呵，也说不定，先抓到她的人是我呢。
[Dialog]
[character(fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_npc_241")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="维多利亚军官"]......喂，等等，航道上有建筑物？能见度太低，发现得太晚了！
[name="维多利亚军官"]这一带的航道规划是谁完成的？前天的勘测组是哪一组？
[name="维多利亚军官"]现在全舰队偏转方向已经来不及了，优先确认建筑内有无人员。
[name="维多利亚军官"]......好。砖木结构房屋，体积很小，不会对战舰履带造成任何威胁。按照原定航道继续行驶。
[Dialog]
[character(fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#1$1",focus=1)]
[name="阿赫茉妮"]......啊，又是一个小小的失误。
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#1$1",focus=2)]
[name="“校官”"]战争总要忍受一些牺牲。
[Character(name="avg_npc_228_1#7",name2="avg_npc_723_1#1$1",focus=1)]
[name="阿赫茉妮"]我明白你的意思。但是，我也有我的“自行判断”。
[name="阿赫茉妮"]让拉芙希妮牺牲？代价恐怕太大了。
[Character(name="avg_npc_228_1#1",name2="avg_npc_723_1#1$1",focus=1)]
[name="阿赫茉妮"]毕竟，那可是流着德拉克之血的战士，就算感染了矿石病，也还是很有用呢。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_723_1#1$1")]
[name="“校官”"]是的，我没有将她带回来。
[name="“校官”"]她没有战斗的决心，反而很擅长逃亡。
[Character(name="avg_npc_723_1#6$1")]
[name="“校官”"]另外......我们追踪到了她进入塔拉王城旧址的痕迹。遗迹内的火熄灭了。
[name="“校官”"]成为感染者，或许让她的源石技艺发生了变化。
[Dialog]
[Character]
[Delay(time=0.2)]
[Character(name="avg_npc_722_1#1$1",fadetime=0.7,block=true)]
[delay(time=1)]
[name="爱布拉娜"]你似乎认为，是矿石病增强了她的力量？
[name="爱布拉娜"]呵呵......当然不。
[name="爱布拉娜"]她是我的妹妹，要是连与我稍微抗衡的力量都没有，那才实在是令人失望。
[name="爱布拉娜"]告诉我，她身边有谁？
[Character(name="avg_npc_723_1#1$1")]
[name="“校官”"]有几个流民跟在她身边，她在那些人面前坚持自称领袖。
[Character(name="avg_npc_722_1#1$1")]
[name="爱布拉娜"]那么，你就不用跟着她了。
[name="爱布拉娜"]既然她终于醒来，意识到自己作为德拉克的权能......
[name="爱布拉娜"]那她很快就会回到我身边。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="21_G7_decisivebattlealley_d",screenadapt="coverall")]
[Delay(time=0.5)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_662_1#6$1",name2="avg_222_bpipe_1#1",fadetime=0.7,block=true)]
[delay(time=1)]
[Character(name="avg_npc_662_1#6$1",name2="avg_222_bpipe_1#1",focus=1)]
[name="陈"]你确定能从这里搭长途货车？
[Character(name="avg_npc_662_1#6$1",name2="avg_222_bpipe_1#1",focus=2)]
[name="风笛"]是呀，我以前逃出维多利亚的时候就坐过。
[Character(name="avg_npc_662_1#6$1",name2="avg_222_bpipe_1#7",focus=2)]
[name="风笛"]......
[Character(name="avg_npc_662_1#1$1",name2="avg_222_bpipe_1#7",focus=1)]
[name="陈"]......风笛。
[Character(name="avg_npc_662_1#1$1",name2="avg_222_bpipe_1#4",focus=2)]
[name="风笛"]欸？
[Character(name="avg_npc_662_1#1$1",name2="avg_222_bpipe_1#4",focus=1)]
[name="陈"]......你记不记得，我之前就问过你，你想要的真相是什么，以及，知道之后你又想做什么。
[name="陈"]其实这个结果，你早该知道。维多利亚的许多事情，最终大抵是这样的权力斗争。
[Character(name="avg_npc_662_1#1$1",name2="avg_222_bpipe_1#7",focus=2)]
[name="风笛"]嗯，话是这样说......可是每一件事里，被卷进去的还是不一样的人。
[name="风笛"]我的想法还是没有变，我必须把自己的报告书递出去。
[Character(name="avg_npc_662_1#1$1",name2="avg_222_bpipe_1#4",focus=2)]
[name="风笛"]只不过，我在想，什么时候维多利亚才会有一个地方能真正收下这份报告书？
[name="风笛"]我到底能用自己的双手做些什么，来让维多利亚快些变成这样的地方？
[Character(name="avg_npc_662_1#8$1",name2="avg_222_bpipe_1#4",focus=1)]
[name="陈"]经历了这么多事，你还是想要改变维多利亚？你还真是......
[Character(name="avg_npc_662_1#8$1",name2="avg_222_bpipe_1#8",focus=2)]
[name="风笛"]真什么？真傻，还是真倔？
[Character(name="avg_npc_662_1#8$1",name2="avg_222_bpipe_1#8",focus=1)]
[name="陈"]......真顽强。
[Character(name="avg_npc_662_1#8$1",name2="avg_222_bpipe_1#9",focus=2)]
[name="风笛"]这也是为什么我们一直都是好朋友吧？认定的目标轻易不会改变，陈陈，我跟你，跟队长，都是一样的欸！
[Character(name="avg_npc_662_1#8$1",name2="avg_222_bpipe_1#9",focus=1)]
[name="陈"]哈。从你嘴里说出来，就不像夸我。
[Character(name="avg_npc_662_1#8$1",name2="avg_222_bpipe_1#8",focus=2)]
[name

... (全文11075字符)
```

### training_act22side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 接下来我们要模拟沼泽地环境进行作战，大家打起精神来。

[PopupDialog(dialogHead="$avatar_beagle")] 发现了巡逻的敌方狙击手，需要支援......呃，克洛丝到哪里去了？
```

### training_act22side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关_b

[PopupDialog(dialogHead="$avatar_kroos")] 在这里哦，这边的敌人就交给我吧。

[Tutorial(focusX=60, focusY=75, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
芦苇丛可以让干员获得<@tu.kw>迷彩</>效果，合理利用是不错的策略。

[Tutorial(focusX=60, focusY=75, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
拥有<@tu.kw>迷彩</>的干员，不阻挡敌人时不会成为敌方一般攻击的目标，但无法躲避溅射类伤害。
```

### training_act22side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关_c

[PopupDialog(dialogHead="$avatar_beagle")] 啊，我的脚好像陷进去了。

[Tutorial(focusX=-180, focusY=-50, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
注意这些沼泽地段，经过的敌人移动速度和攻击速度会逐渐降低，我方单位的攻击速度同样会受到影响。

[PopupDialog(dialogHead="$avatar_beagle")] 没关系，我能保护好其他人，相信大家一定可以击溃敌人的！
```

### training_act22side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关_d

[Tutorial(focusX=-240, focusY=145, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_kroos", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这个敌人，看起来不太对劲呢......

[Tutorial(focusX=-240, focusY=145, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
根据情报，这似乎是被某种源石技艺操控行动的死者，需要小心应对。
```

### training_act22side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关_e

[Tutorial(focusX=-250, focusY=160, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
他们即使被击倒，也会留下源石技艺燃烧后的“余烬”，不尽快清除的话，源石技艺会让他们再次站起来。

[PopupDialog(dialogHead="$avatar_doberm")] “余烬”本身并不会对接触到它的人造成伤害，但其具有<@tu.kw>隐匿</>的特性，且<@tu.kw>需要数次伤害才能清除</>。

[PopupDialog(dialogHead="$avatar_beagle")] 我明白了，我会站在这里拦住他们。但另一边要怎么办？

[PopupDialog(dialogHead="$avatar_melan")] 我会尽快赶到。
```

### training_act22side_02_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关02_a

[Tutorial(focusX=-45, focusY=45, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
啊，怎么......

[Tutorial(focusX=-45, focusY=45, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
一些情形下战场上的芦苇丛会被点燃。

[Tutorial(focusX=-45, focusY=45, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
燃烧的芦苇丛不再提供<@tu.kw>迷彩</>，并且站在其中的干员会受到法术伤害与<@tu.kw>灼燃损伤</>。

[PopupDialog(dialogHead="$avatar_melan")] 抱歉......我正在想办法应对火情。

[PopupDialog(dialogHead="$avatar_doberm")] 再坚持一下，玫兰莎。火势正在逐渐减小。
```

### training_act22side_02_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关02_b

[Tutorial(focusX=-45, focusY=45, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
呼，终于熄灭了。

[Tutorial(focusX=-45, focusY=45, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
将干员部署在燃烧的芦苇丛中，能够使火焰逐渐熄灭。
```

### training_act22side_02_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关02_c

[Tutorial(focusX=145, focusY=200, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
在相连的芦苇丛中，火焰每隔一定时间还会<@tu.kw>向四周蔓延</>。
```

### training_act22side_02_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关02_d

[Tutorial(focusX=145, focusY=64, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_jesica", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
啊，火焰就快蔓延过来了。

[Tutorial(focusX=145, focusY=64, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
部署在芦苇丛中的干员不仅能灭火，还能抑制火焰的蔓延。

[Tutorial(focusX=145, focusY=64, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这次就由我来示范吧。
```

### training_act22side_02_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动22side教学关02_e

[Tutorial(focusX=300, focusY=230, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
谨慎应对眼前的敌人，靠近火焰会让他们的攻击额外造成<@tu.kw>灼燃损伤</>。

[PopupDialog(dialogHead="$avatar_doberm")] 及时灭火和抑制火势蔓延非常重要！

[PopupDialog(dialogHead="$avatar_doberm")] 接下来就交给你们了。
```


## 统计

- 总字符数：328656
- 对话行数：2414


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
