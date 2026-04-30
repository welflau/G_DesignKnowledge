# 明日方舟 · 活动剧情 · act34side（25段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act34side」完整剧情脚本（25个文件，3556行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act34side
- 脚本文件数：25

### act34side_06

```
[HEADER(is_skippable=true, is_autoable=false)] 活动act34side_06关剧情
[PopupDialog(dialogHead="$avatar_skadi")] 蠕动的地面......之前在伊比利亚海岸上也遇到过这种现象。
[Tutorial(focusX=-5, focusY=15, focusWidth=220, focusHeight=220,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="BottomRight",           protectTime=0.5, dialogHead="$avatar_glady", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 伊比利亚人称之为“溟痕”......是海嗣的另一种扩张方式。记得利用<@tu.kw>“小帮手”</>，它可以高效地<@tu.kw>清理溟痕</>。
[PopupDialog(dialogHead="$avatar_glady")] 此次配发的“小帮手”还搭载了工程钻具，如果有需要，也可以用它来<@tu.kw>破坏</>海嗣结成的<@tu.kw>赘生甲壳</>。
```

### level_act34side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g4_aegirstreet_1",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1393_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1395_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left",focus="l")]
[name="阿戈尔研究员A"]......从地质条件上看，是一座很有潜质的火山，但位置就不那么合适了。
[name="阿戈尔研究员A"]不论用什么样的手段，都很难顶着海嗣的围攻建立起长距离的能源输送线路。
[charslot(slot = "r",focus="r")]
[name="阿戈尔研究员B"]您已经看过技术院的报告了，对吧？
[name="阿戈尔研究员B"]来源于海水的氢能虽然可以稳定维持军团舰队的正常运作，却很难保障信标塔的供能不出现缺口。
[name="阿戈尔研究员B"]从开始运转以来，那座塔几乎吃掉了整座城市一半的能源。
[charslot(slot = "left",focus="l")]
[name="阿戈尔研究员A"]根据资料，它曾经的能源消耗比现在夸张得多。前人甚至专门为它设计了由十几座城市协力才能维持的生物供能系统。
[name="阿戈尔研究员A"]可惜，放在现在这个年代，规模如此庞大的生物供能系统大概在启动之前就会引来海嗣的围攻吧。
[charslot(slot = "r",focus="r")]
[name="阿戈尔研究员B"]言归正传，我们还是需要找到能为信标塔稳定供能的方式。
[charslot(slot = "left",focus="l")]
[name="阿戈尔研究员A"]或许亚庇乌斯会有办法？我去联......哦！
[charslot(slot = "r",focus="r")]
[name="阿戈尔研究员B"]您忘了，亚庇乌斯还在本境，而我们的城市已经进入通讯静默了。
[name="阿戈尔研究员B"]在海嗣的重围之下，我们很难再大张旗鼓地用原先的方式架设通讯光缆。
[charslot(slot = "left",focus="l")]
[name="阿戈尔研究员A"]唉，我还是更习惯以前能随时从全国任何一个角落拉人开全息会议的日子。
[charslot(slot = "r",focus="r")]
[name="阿戈尔研究员B"]等等。
[name="阿戈尔研究员B"]我刚刚想到，如果改进一下能源转换设施的输出模式呢？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "left", name = "avg_npc_1392_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1394_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left",focus="l")]
[name="阿戈尔医师"]我们之前很少有类似的经验，不是吗？安全方面总归是存在隐患的。
[charslot(slot = "r",focus="r")]
[name="阿戈尔学者"]既然是由你来负责精神连接的操作，我相信安全隐患不会太大。
[charslot(slot = "left",focus="l")]
[name="阿戈尔医师"]我不放心的就是我自己。与海嗣化的同胞建立精神连接，进行长时间的对话，我不敢确定这会对双方产生怎样的影响。
[charslot(slot = "r",focus="r")]
[name="阿戈尔学者"]相关的研究已经很充分了。只要临床操作的时候你别因为不安而手抖，就不会出问题。
[charslot(slot = "left",focus="l")]
[name="阿戈尔医师"]即使在本境，为海嗣化的同胞提供临终对谈的案例也相当少见。他们多数都只能接受寻常的安乐死。
[name="阿戈尔医师"]唉......克莱门莎执政官的主张还是那么激进。
[charslot(slot = "r",focus="r")]
[name="阿戈尔学者"]所以我才愿意跟她来到这里。
[name="阿戈尔学者"]如果我能通过对话厘清理性的丝线，那些海嗣化的同胞就还有机会在世上留下自己思想的痕迹。
[name="阿戈尔学者"]一次酣畅的思辨，难道不是送别他们的最好方式？
[name="阿戈尔学者"]只可惜，海巡队带回的幸存者多数都已经不成人形，有机会回到城市接受临终对谈的，少之又少......
[charslot(slot = "left",focus="l")]
[name="阿戈尔医师"]我说——
[charslot(slot = "r",focus="r")]
[name="阿戈尔学者"]嗯？
[charslot(slot = "left",focus="l")]
[name="阿戈尔医师"]我们可能真的在见证历史了。
[charslot(slot = "r",focus="r")]
[name="阿戈尔学者"]也可能只是在平常地完成本职工作。我相信发展规划所没有看错你，去做准备吧。
[charslot(slot = "left",focus="l")]
[name="阿戈尔医师"]谢谢。隔离室见。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1380_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1380_1#2$1")]
[name="乔迪"]那个，两位，我想请问——
[Dialog]
[charslot]
[playsound(key="$d_avg_seacitytransform", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.5, channel="bgs",fadetime=2)]
[CameraShake(duration=3.5, xstrength=8, ystrength=6, vibrato=40, randomness=90, fadeout=true, block=false)]
[delay(time=2.5)]
[StopSound(channel="bgs", fadetime=3)]
[PlaySound(key="$bodyfalldown1", volume=0.6)]
[delay(time=1)]
[name="乔迪"]怎么回事？天灾？！大海里面也有天灾？
[charslot]
毫无防备的年轻人重重摔倒在地，可更诡异的画面将他的惊呼堵回了喉咙——
[CameraShake(duration=5, xstrength=2, ystrength=8, vibrato=1, randomness=90, fadeout=false, block=false)]
[playsound(key="$d_avg_seahumansurface",volume=0.5)]
不远处，路人纷纷悬空而起，毫无依凭地在空中浮游，好像水中游曳的鳞。城市在他们身下剧烈地倾斜、摇晃，然而人们对此视若无睹。
片刻，一切恢复正常，有些人落回地面，交谈着走远，也有人索性就那样在空中游动着前行，不再落地。
他突然想起了小时候，格兰法洛的镇民们煞有介事地向他讲述过阿戈尔的邪教仪式。
[name="乔迪"]......
[charslot(slot = "m", focus = "n")]
[name="？？？"]乔迪，快爬起来吧。
[Dialog]
[charslot(slot = "m", name = "avg_npc_1380_1#8$1",posfrom = "0,-60", posto = "0,0",duration=0.8)]
[delay(time=1)]
[name="乔迪"]啊，啊好的！
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]艾丽妮阁下？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_4009_irene_1#1$1",duration = 1)]
[delay(time=1.5)]
[name="艾丽妮"]昨天下船的时候，海巡队给我们分发的装置，下次出门要记得戴上。
[charslot(slot = "m", name = "avg_npc_1380_1#4$1")]
[name="乔迪"]这种情况应该是......第几份介绍影像里提到过来着......
[charslot(slot = "m", name = "avg_4009_irene_1#1$1")]
[name="艾丽妮"]第四份影像。刚刚在港口枢纽的时候，那里的技术人员也好心提醒了我。
[name="艾丽妮"]这是城市在进行重力参数调整，弥利亚留姆长期维持着低重力的人工重力环境，这是必要的定期调整......
[charslot(slot = "m", name = "avg_4009_irene_1#2$1")]
[name="艾丽妮"]呃，简单理解为，鳞在调节自己的鳔......他是这么说的。
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]原来您突然消失，是去港口参观了。
[charslot(slot = "m", name = "avg_4009_irene_1#1$1")]
[name="艾丽妮"]嗯，我很在意他们的船只和港口，他们的武装......那些宏伟的舰船往来穿行，好像羽兽在礁石与峭壁间自由地穿梭。
[name="艾丽妮"]我看见了“愚人号”的影子，布雷奥甘确实在伊比利亚复现了阿戈尔的科技，或许......
[charslot(slot = "m", name = "avg_4009_irene_1#7$1")]
[name="艾丽妮"]或许我们曾经引以为傲的舰队，本应直抵更宽广的海域，而不是为了震慑那些公爵和帕夏，披戴着黄金的外衣在内海巡航。
[charslot(slot = "m", name = "avg_npc_1380_1#4$1")]
[name="乔迪"]布雷奥甘......
[charslot(slot = "m", name = "avg_4009_irene_1#1$1")]
[name="艾丽妮"]你完全没有听到重点。乔迪，你看起来非常不安。
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]只是有点不适应......
[charslot(slot = "m", name = "avg_npc_1380_1#3$1")]
[name="乔迪"]这里比我想象的还要陌生。空气厚重得让人喘不过气，头顶的海水让人脊背发凉，路边这些一直在发光的植物也让人脑袋发晕。
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]以及刚刚的这种情况......
[name="乔迪"]身体上的不适应，我都还能克服，但有更多陌生的事物，是不得不从头去了解的。
[name="乔迪"]阿戈尔提供的介绍影像确实很详细，可来来回回看了那么多遍，我还是有很多事没法理解。
[name="乔迪"]食物不需要刀叉就可以隔空移动，衣服不用脱下来就可以直接清洁——这些简单的我能明白。
[charslot(slot = "m", name = "avg_npc_1380_1#4$1")]
[name="乔迪"]但终端上提供的“可食用叙事诗”“咀嚼式定理”，我还是搞不懂怎么吃......我只能先打印了那种能直接供应养分的应急装置。
[name="乔迪"]我在格兰法洛出生，也在格兰法洛长大，我没有离开过那里，我在想是不是......
[charslot(slot = "m", name = "avg_4009_irene_1#1$1")]
[name="艾丽妮"]不，这种变化，并不等同于一个伊比利亚人从某座边境小镇来到了富庶的港都——尽管那座黄金般的宏伟城市早已消失。
[name="艾丽妮"]并非贫乏与繁华的区别，我们似乎来到了......另一种文明。
[charslot(slot = "m", name = "avg_npc_1380_1#10$1")]
[name="乔迪"]我刚刚只是想找前面的人问路，但我完全无法理解他们对话的内容，也不知道什么时候开口打断比较合适......
[name="乔迪"]更重要的是，我不确定他们会怎么看待我——一个与阿戈尔格格不入的阿戈尔人。
[charsl

... (全文20260字符)
```

### level_act34side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g1_beaconsquare",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="char_263_skadi#5",duration=1)]
[Delay(time=2)]
[name="斯卡蒂"]博士，你误以为我们刚才参观的建筑是博物馆了对吧？你看那些仪器的眼神很像在欣赏什么展品。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="这已经是我误认成博物馆的第三幢建筑了。", values="1")]
[Predicate(references="1")]
[Decision(options="建筑内部的重力为什么可以是颠倒的？;那些在立柱间自主穿行的水流是怎么回事？;那片能让我的手指扭曲变形的空间是什么？", values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]有些原理，我也解释不清。
[name="斯卡蒂"]这五年来，我们也错过了很多新的科技进展。
[Dialog]
[charslot]
[Decision(options="等等，前面的那座高塔......", values="1")]
[Predicate(references="1")]
[Decision(options="城市的核心建筑，是一座发射井？", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]你没猜错，博士，那是一座信标发射井。它的历史已经不短了。
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]鲨鱼，你居然认识。
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]很小的时候，父母带我游历过本境，不少城市都存在类似的建筑。
[Dialog]
[charslot]
[Decision(options="我以为阿戈尔人都是集体抚养长大的。", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="char_263_skadi#3")]
[name="斯卡蒂"]我确实是，但鲨鱼和她的血缘父母一直维持着很特别的关系。
[charslot(slot = "m", name = "avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]比起父母，更像是朋友吧。
[name="幽灵鲨"]他们和公共养育所达成了奇妙的共识，基础的抚养由公共养育所负责，但他们每接手一座城市的穹顶建设，就把我也带过去。
[name="幽灵鲨"]领着我满城参观、学习，甚至让我也参与一点他们的工作......当然，大部分时候我还是住在公共养育所。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="说回来，这座信标发射井是用来做什么的？", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]字面意思——负责发射信标，引领航道。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="一般的信标发射井不会有这样的规模。;它所引领的究竟是什么尺度下的航道？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#10$1")]
[name="幽灵鲨"]大概三百年前，阿戈尔对海洋的开发就已经趋近完全。天然存在的各种能源得到利用，海床的每一道沟壑都在海图上留有记录。
[name="幽灵鲨"]那时候，人们将目光投向了另一片闪烁着繁星的海洋。
[name="幽灵鲨"]在当初的设想中，我们的舰队，乃至我们的城市都将穿越那层本不应存在的界限，在阻隔层外点亮文明的火。
[Dialog]
[charslot]
[Decision(options="阻隔层外......", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_003_kalts_1#1$1")]
[name="凯尔希"]博士，保存者的判断是准确的，克丽斯腾的壮举在阿戈尔看来并非遥不可及。
[name="凯尔希"]海洋国家与天空的距离，比我们一直以来想象的还要更近。
[charslot(slot = "m", name = "avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]那时的人们抱着巨大的热情做出了诸多尝试——勘测与破解电子云层，革新推进技术和材料技术，探索能适应太空环境的生命形式......
[name="幽灵鲨"]我们眼前的信标发射井，便是当时的产物。
[name="幽灵鲨"]至少在最初的设想中，它可以捕捉星空中最微小的讯号，也能在星图的特定坐标上竖立永不熄灭的信标。
[name="幽灵鲨"]信标之间，不计其数的微型浮游机械将以身躯连缀成路网，让阿戈尔能在转瞬间跨越悠远的空间......至少，人们是如此设想的。
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]鲨鱼，你从来没跟我说过这些。
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]在陆地的时候，我清醒的时间很少，斯卡蒂。
[charslot(slot = "m", name = "avg_1023_ghost2_1#10$1")]
[name="幽灵鲨"]但就在昨天，我做了一个梦，又一次梦见自己从斗智场走入那段历史。
[name="幽灵鲨"]然后，我看见劳伦缇娜在跳舞。
[name="幽灵鲨"]她的舞步从浪涛跃上星空，星尘追逐着她的裙摆。有一个声音，从很遥远很遥远的地方传来。那是万物之主，万物之主以歌声回应她。
[name="幽灵鲨"]宇宙没有尽头，想象无法穷尽，劳伦缇娜的舞步永不停止。
[charslot(slot = "m", name = "avg_1023_ghost2_1#3$1")]
幽灵鲨闭上了眼睛，仿佛回到了那个梦里。
[charslot(slot="m",name="char_263_skadi#4")]
[name="斯卡蒂"]唔......
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]怎么了？
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]鲨鱼，我在想象那个画面。
[Dialog]
[charslot]
[Decision(options="很美的梦，劳伦缇娜。;说不定真有那样的时刻，劳伦缇娜。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#12$1")]
[name="幽灵鲨"]在真正推开星海之门前，人们总试图为阻隔层外的威胁做出更充分的准备......直到海嗣的出现打断了这场漫长的梦。
[name="幽灵鲨"]不知从何时起，“海嗣”几乎成了我们唯一的课题。艺术、科技，我们所有面向未来的想象，都被迫搁置。
[name="幽灵鲨"]海嗣改变了阿戈尔的许多事物。
[Dialog]
[charslot]
[Decision(options="斯卡蒂，成为深海猎人之前，你在做什么？;幽灵鲨，成为深海猎人之前，你在做什么？", values="1;2")]
[Predicate(references="1")]
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]我吗？
[name="斯卡蒂"]我当时可是设施管理所最好的技术员，一个人就能维护一整座城市的海底灯光阵列。
[name="斯卡蒂"]发展规划所给出的建议正好和我的想法差不多。我就接受了。
[name="斯卡蒂"]虽然一个人是孤独了点，但偶尔逗逗那些藏在珊瑚礁里的巨型鳞，一边发呆一边点亮海洋什么的，蛮惬意的。
[Predicate(references="2")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]我当时还只是一个雕塑学徒。
[name="幽灵鲨"]发展规划所会结合实际情况，为每个公民提供建议，而且一般和我们自己的意愿都能对得上。
[name="幽灵鲨"]我想进入的领域......大概会是穹顶设计、雕塑艺术，或者舞蹈吧。
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]博士，凯尔希，说起来，并肩走来的这段时间，我们分享过无数情报，却没有分享过曾经的生活。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="因为它已经被改变了。", values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "avg_1023_ghost2_1#1$1")]
[name="幽灵鲨"]也是。博士，明明是带你们参观城市，聊起这样沉重的话题过于不合时宜了。
[name="幽灵鲨"]无限的波涛正悬于我们的头顶。在面对那些令人不愉快的事情之前，博士，我们或许还来得及在此共舞一曲？
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="51_g7_consuloffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$act18d3d0_intro",key="$act18d3d0_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1382_1#1$1",duration=1.5)]
[delay(time=2)]
[name="温柔的女性"]......歌蕾蒂娅。
[PlaySound(key="$d_avg_higheldshosfts", volume=0.7)]
[charslot(duration=1)]
斜持仪仗剑的女性缓步走来，歌蕾蒂娅下意识地把手搭上了槊柄。
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
但对方只是将双臂轻轻环过她的肩头，歌蕾蒂娅嗅到神经活性剂的气味在身边晕开。
阿戈尔人不常以亲昵的肢体接触表达问候，歌蕾蒂娅甚至不记得母亲有对自己做过这个动作。
但此刻，对方的这个动作却显得那么自然。
[charslot(slot="m",name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]克莱门莎执政官？
[name="歌蕾蒂娅"]我不记得总战争设计师之间有这种军礼。
[charslot(slot="m",name="avg_npc_1382_1#1$1")]
[name="克莱门莎"]歌蕾蒂娅，能看到猎人们清醒地归来，是我此行最大的收获。
[charslot(slot="m",name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]从军士们见到我时的失态反应来看，你们或许困扰居多。
[charslot(slot="m",name="avg_npc_1382_1#9$1")]
[name="克莱门莎"]斩杀“初生”的行动，令阿戈尔失去了全部的深海猎人。
[name="克莱门莎"]西昆妲那孩子尝试组织了多次搜救，但“初生”死亡后，疯狂的海嗣封锁了那整片海域，她每一次都只能无功而返。
[charslot(slot="m",name="avg_npc_1382_1#6$1")]
[name="克莱门莎"]赫拉提娅——你的母亲，只能向国民通报了你们的死亡。
[charslot(slot="m",name="avg_npc_1382_1#2$1")]
[name

... (全文13998字符)
```

### level_act34side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g11_aegirroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4137_udflow_1#1$1",duration=1)]
[delay(time=1.5)]
[name="西昆妲"]这段时间，都没人进来过吗？
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[name="海巡队队员"]没有。
[name="海巡队队员"]房间内小帮手的中控元件也确认过了，没有发现被篡改过的痕迹。
[charslot(slot="m",name="avg_4009_irene_1#1$1")]
[name="艾丽妮"]您好，请问这里这个记录要怎么查看？
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]给她打开权限。
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[name="海巡队队员"]是。
[charslot(slot="m",name="avg_4009_irene_1#2$1")]
[name="艾丽妮"]啊，谢谢你！
[charslot(slot="m",name="avg_4137_udflow_1#1$1",focus="n")]
西昆妲取下了腰间挂着的装置。她的笔尖飞舞，仿佛水藻般纠缠不清的线条不断地在装置的表面浮现。
[charslot(slot="m",name="avg_4009_irene_1#1$1")]
[name="艾丽妮"]你们的指挥官这是在？
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[name="海巡队队员"]写写画画有助于她快速思考，这是西昆妲的习惯，听说她还是研究员的时候就这样。
[name="海巡队队员"]旁人理解不了，上面也没记什么关键词，全是一些只有她自己才能看懂的......呃，抽象画。
[Dialog]
[charslot(slot="m",name="avg_4137_udflow_1#3$1")]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[delay(time=1.5)]
[name="西昆妲"]（书籍按照薄厚的顺序排列，贝壳装饰物按照大小顺序摆放，从斗智场下载的所有资料则根据时间进行了归类。）
[name="西昆妲"]（浮藻脂质霜剂，能有效防止皮肤干燥脱水，是因为弥利亚留姆要靠近海岸？）
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]（这个分量，几乎够用三年。）
[name="西昆妲"]（一名普通的阿戈尔女性。谨慎，甚至有些胆小和刻板，与发展规划所提供的资料相符。）
[charslot(slot="m",name="avg_4137_udflow_1#5$1")]
[name="西昆妲"]（那些微型水培箱——）
[charslot(slot="m",name="avg_4009_irene_1#1$1")]
[name="艾丽妮"]那些箱子是干什么用的？明明都空了，却还挂在墙上？
[charslot(slot="m",name="avg_4137_udflow_1#5$1")]
[name="西昆妲"]是的。水培箱应该是切入点。
[name="西昆妲"]对房间里所有与植物栽培相关的设备进行扫描。
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[name="海巡队队员"]是。
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]以及，从图利娅的档案里调取相关的信息，她或许有这方面的爱好。
[Dialog]
[PlaySound(key="$d_avg_scan", volume=1)]
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[delay(time=1)]
[name="海巡队队员"]图利娅曾就职于生态艺术创作所，主要负责濒危深海藻类的培育。
[name="海巡队队员"]根据生态艺术创作所的资料......
[name="海巡队队员"]经过艺术家的精心培育，这些深海藻类能够在生长的过程中相互交织，组成一幅不断反映着生命进程的、动态的画。
[name="海巡队队员"]这些微型水培箱是图利娅的个人资产，这里有她当时的作品影像。
[Dialog]
[charslot]
[charslot(slot = "left", name = "avg_4137_udflow_1#7$1")]
[charslot(slot = "right", name = "avg_4009_irene_1#6$1")]
[delay(time=1)]
[name="西昆妲＆艾丽妮"]很漂亮。
[charslot(slot = "left", name = "avg_4137_udflow_1#9$1")]
[charslot(slot = "right", name = "avg_4009_irene_1#3$1")]
[name="西昆妲＆艾丽妮"]......
[charslot]
[charslot(slot="m",name="avg_4009_irene_1#1$1")]
[name="艾丽妮"]但这些水培箱看起来已经空置了很长时间。
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]档案刚刚提到，图利娅是转岗后才加入的航道计划。
[charslot(slot="m",name="avg_4009_irene_1#7$1")]
[name="艾丽妮"]她是因为某些原因放弃了过去的生活吗？
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]嗯。她的失踪很可能与职业生涯的变故有关。
[name="西昆妲"]扫描结果怎么样？
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[name="海巡队队员"]各类植物栽培设备并无异常，但我们在房间的集成终端上发现了一份操作记录。
[name="海巡队队员"]图利娅在失踪前两天，从信标塔中控室下载过一份数据，并在自己的房间内制作了一份备份。
[name="海巡队队员"]但我们在房间内并没有发现它。
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]追踪她的行程，同时联系中控室，从他们那边的下载记录去追溯数据内容。
[charslot(slot="m",name="avg_4009_irene_1#7$1")]
[name="艾丽妮"]如果她在失踪前还能正常地在工作场所与住所之间往来，那她的同僚或亲友也许对她的行为有所了解？
[charslot(slot="m",name="avg_4137_udflow_1#1$1")]
[name="西昆妲"]是的。
[name="西昆妲"]对主要社会关系的问询安排好了吗？报案人呢？
[charslot(slot="m",name="avg_npc_1391_1#1$1")]
[name="海巡队队员"]已经安排妥当，很快就可以与她们会面。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.12,block=false)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15,block=true)]
[Background(image="51_g6_aegirarena",screenadapt="coverall",xScale=1.2,yScale=1.2,x=60)]
[backgroundTween( duration=40,xTo=-60,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[delay(time=1)]
[name="乔迪"]......
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[delay(time=2)]
[name="阿维图斯"]乔迪，有什么我能帮到你的吗？
[name="乔迪"]抱歉，我脑袋里问题太多，有点不知道......
[name="乔迪"]这棵......金属的“树”？我只要对它提问就好了吗？我小时候也听过古树保管知识的传说，但我从没见过这样的......
[name="阿维图斯"]被你称作“树”的珊瑚状装置是一个巨型集成终端，它是阿戈尔千百年来知识与文化的沉淀。
[name="阿维图斯"]我们的所想、所知、所作、所赏，乃至许多仍待解答的问题，都储存在这里。它构成了斗智场的核心。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[curtain]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1386_1#5$1",duration=1)]
[charslot(slot = "l", name = "avg_npc_1380_1#2$1",duration=1)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_npc_1380_1#2$1",focus="l")]
[name="乔迪"]所以，斗智场究竟是......
[charslot(slot = "r", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]最早由伟大的人类学家暨先史文明研究者玛利图斯提出创意并主持修建的公共设施，对整个国家都影响深远的伟大设计。
[name="阿维图斯"]除了海面上互相支撑的环礁城市群和海沟下模块化的城市网络，我们的其他城市大多形态各异，很少有同质化的设计。
[name="阿维图斯"]但许多城市都不约而同地采纳了玛利图斯的设计，设立了自己的斗智场。
[name="阿维图斯"]看看周围的人，他们在此思考、质疑、辩论，最后取得理解，做出决定。
[name="阿维图斯"]最复杂的公式，最古老的图纸，最优美的诗歌......还有最适合的道路，都在这里诞生。这正是玛利图斯希望看到的景象吧。
[charslot(slot = "l", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]您一直在提的玛利图斯......那是个怎样的人？
[charslot(slot = "r", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]要细数他为阿戈尔做出的所有贡献，恐怕一整天的时间也不够用。不过除此之外，我倒是还了解一些他的性格特质。
[charslot(slot = "l", name = "avg_npc_1380_1#2$1",focus="l")]
[name="乔迪"]您认得他？
[charslot(slot = "r", name = "avg_npc_1386_1#3$1",focus="r")]
[name="阿维图斯"]没有没有，玛利图斯生活在两百多年前，早在我出生之前，他就已经从阿戈尔消失了。
[charslot(slot = "r", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]不过，他的怪脾气是我们学科的导师们津津乐道的话题。玛利图斯的理论推演能力极为出众，却很不喜欢自己得出结论。
[name="阿维图斯"]在别人看来已经确凿无疑的事情，他也还要与自己辩论良久，才愿意得出结论。
[name="阿维图斯"]有人认为他是过分在意事物的价值与意义，才会陷入这无休止的辩论，但这不正是我们身为人类的天性？
[name="阿维图斯"]正因如此，他才主持修建了斗智场。事实证明，我们确实需要一个随时能让我们与自己、与他人展开思辨的场所。
[charslot(slot = "l", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]我没有什么可以用来辩论的观念，阿维图斯先生......

... (全文17952字符)
```

### level_act34side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1400_1#1$1",duration=1.5)]
[delay(time=2)]
[name="军团长官"]歌蕾蒂娅执政官，您认为问题并不在于那场战役本身？
[charslot(slot="m",name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]是的。详细的作战部署此刻正投影在各位面前，如果其中存在我没能注意到的纰漏，你们每个人都有义务指出。
[charslot(slot="m",name="avg_npc_1400_1#1$1")]
[name="军团长官"]不，我对具体的作战部署没有疑问。结合当时的认知条件，那无疑是最合理的作战部署。
[name="军团长官"]但我希望知道，现在的您会如何评判当时的认知条件？
[charslot(slot="m",name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]必须承认，阿戈尔当时对海嗣的认知存在严重的缺陷......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "left", name = "avg_1023_ghost2_1#12$1")]
[charslot(slot = "right", name = "char_263_skadi#4")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "right", name = "char_263_skadi#4",focus="r")]
[name="斯卡蒂"]这些人想说什么？
[charslot(slot = "left", name = "avg_1023_ghost2_1#12$1",focus="l")]
[name="幽灵鲨"]以前还在阿戈尔的时候，你就不喜欢想太多，你还是不习惯那些人的思考方式。
[name="幽灵鲨"]他们对我们没有恶意，他们只是在寻求必要的事实。
[name="幽灵鲨"]寻找所有可能的缺陷，质疑所有完美的成果。然后，真实与美，还有正确的道路，将在最激烈的争论中彰显自身。
[name="幽灵鲨"]一切交给剑鱼吧。
[name="幽灵鲨"]要是不想听，就闭着眼睛睡一会儿。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="m",name="avg_474_gladiia_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="歌蕾蒂娅"]......综上，五年前那次战争设计最大的失误，就是没能为我们的认知缺陷留出余地。
[name="歌蕾蒂娅"]在泰拉的真相被揭开之前，我们需要承认自己对海嗣的认知总会存在缺陷，我们的战争设计必须将其考虑在内。
[charslot(slot="m",name="avg_npc_1400_1#1$1")]
[name="军团长官"]同意。您刚刚得出的结论，应当被用于审视未来可能诞生的各项作战计划。
[name="军团长官"]能与您一同反思一场已经被尘封的战役，并得出有效的结论，是我的荣幸，歌蕾蒂娅执政官。
[charslot(slot="m",name="avg_npc_1397_1#1$1")]
[name="科学院研究员"]不过，除了五年前的那场战役......
[name="科学院研究员"]还有更加现实的问题值得我们担心。
[name="科学院研究员"]根据体检报告，您、斯卡蒂、劳伦缇娜，三位都发生了不容忽视的身体异变。
[name="科学院研究员"]我无意质疑各位对国家的忠诚，但我需要知道海嗣基因对各位的同化，会对各位接下来的行动产生怎样的影响。
[name="科学院研究员"]请原谅我这么发问。
[name="科学院研究员"]弥利亚留姆很快就要完成对所有巢穴的定位，在那之后，海嗣将在第Ⅳ级武器的作用下被驱离，航道正式开启。
[name="科学院研究员"]在这个时间点上，深海猎人，是否会成为阿戈尔的敌人、你们自己的敌人？
[dialog]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, channel="bgs",fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="l",name="avg_4145_Ulpia_1#1$1",posfrom = "0,0", posto = "200,0")]
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",bstart=0.2,bend=0.5,focus="m",isCopy=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[StopSound(channel="bgs", fadetime=2)]
[name="？？？"]对阿戈尔来说，失控的猎人比海嗣本身更加危险。
[name="？？？"]深海猎人，就像是阿戈尔的反面。他们诞生于阿戈尔最卑劣的伤口，阿戈尔怜悯他们，也畏惧他们。
[dialog]
[charslot(slot = "m", focus = "n")]
[charslot(slot = "l", focus = "n")]
[Decision(options="深海猎人，乌尔比安，对吧？", values="1")]
[Predicate(references="1")]
[Decision(options="按理说，你更应该在底下接受质询。", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",duration=1,focus="m")]
[delay(time=2)]
[charslot(slot="l",name="avg_4145_Ulpia_1#1$1",afrom=0,ato=0,isCopy=true)]
[name="乌尔比安"]你比我想象中要冷静很多，也知道我的身份。
[name="乌尔比安"]看来歌蕾蒂娅在陆地上建立的信任关系，并不只是对那位医生一人。
[name="乌尔比安"]我没有在之前的任何一次行动中见过你。你不是伊比利亚的审判官，也不是岛民。
[name="乌尔比安"]那位罗德岛的医生将你带到阿戈尔，却又有意隐藏你的身份。
[dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="我只是凯尔希的同僚。;我和她同属于罗德岛。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",isCopy=true)]
[name="乌尔比安"]随你怎么定性自己。
[name="乌尔比安"]总之，你能帮到猎人们。
[dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="有事为什么不直接找斯卡蒂？;有事为什么不直接找幽灵鲨？;有事为什么不直接找歌蕾蒂娅？", values="1;2;3")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_4145_Ulpia_1#3$1",isCopy=true)]
[name="乌尔比安"]斯卡蒂不太擅长这样的事情。
[Predicate(references="2")]
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",isCopy=true)]
[name="乌尔比安"]你是说劳伦缇娜？
[charslot(slot="m",name="avg_4145_Ulpia_1#3$1",isCopy=true)]
[name="乌尔比安"]她不太擅长这样的事情。
[Predicate(references="3")]
[charslot(slot="m",name="avg_4145_Ulpia_1#3$1",isCopy=true)]
[name="乌尔比安"]现在并不是合适的时机。
[Predicate(references="1;2;3")]
[dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="你不信任猎人们？", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_4145_Ulpia_1#2$1",isCopy=true)]
[name="乌尔比安"]恰恰相反，我信任她们，而且太过了解她们。
[charslot(slot="m",name="avg_4145_Ulpia_1#3$1",isCopy=true)]
[name="乌尔比安"]斯卡蒂的行动快过思考，劳伦缇娜清醒的时日尚浅，最终决定一切的人只会是歌蕾蒂娅。
[name="乌尔比安"]此前我已经向她分享过许多情报，她应该有了警惕。她并非不清楚自己会遭遇多少限制，但仍然选择回到阿戈尔。
[name="乌尔比安"]她太急于回到熟悉的环境，殊不知自己已经被摆在了最显眼的位置，一切可信任的和不可信任的都有十足的权力来审视她。
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",isCopy=true)]
[name="乌尔比安"]现在并不是深海猎人返乡的最好时机，这是一场豪赌。
[dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="既然如此，你为什么还要潜入这座城市？;看来你还是很关心猎人们。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",isCopy=true)]
[name="乌尔比安"]歌蕾蒂娅她们的处境不容乐观。
[name="乌尔比安"]与我不同，她们三人虽然接受了改造，却没有参与深海猎人计划最核心的研发工作。她们很难解释清楚自己身体的异变。
[name="乌尔比安"]我会告诉你一些相关的信息，必要的时候，我需要你想办法为歌蕾蒂娅解围。事后，再向她传达我的提醒。
[charslot(slot="m",name="avg_4145_Ulpia_1#3$1",isCopy=true)]
[name="乌尔比安"]至于更多的事情——
[stopmusic(fadetime=2)]
[charslot(slot = "m", focus = "n")]
[name="布兰都斯"]或许，各位可以听我说两句。
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",isCopy=true)]
[name="乌尔比安"]......布兰都斯。他也来到了这里？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot="m",name="avg_474_gladiia_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="歌蕾蒂娅"]布兰都斯？
[charslot]
[dialog]
[playMusic(intro="$newhope01_intro",key="$newhope01_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1381_1#8$1",duration=1)]
[delay(time=2)]
[name="布兰都斯"]每次都是这样，以前在研究所的时候，你也好，乌尔比安也好，总是趁我打盹的时候和研究员们吵起来。
[charslot(slot="m",name="avg_npc_1382_1#1$1")]
[name="克莱门莎"]顾问，你的意见确实会很有参考价值。
[charslot(slot="m",name="avg_npc_1381_1#8$1")]
[name="布兰都斯"]不胜荣幸。
[charslot(slot="m",name="avg_npc_138

... (全文14110字符)
```

### level_act34side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g4_aegirstreet_1",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[PlaySound(key="$rungeneral", volume=1)]
[Delay(time=0.5)]
[name="？？？"]呼，呼——得赶快才行！
[name="？？？"]！
[name="？？？"]古球藻？这里怎么会出现古球藻，难道弥利亚留姆还有其他人在培育濒危藻类？
[dialog]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1385_1#1$1",duration=1.5)]
[delay(time=2)]
[name="？？？"]......
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "80,0",duration = 1)]
[delay(time=1.15)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[charslot(slot = "m",posfrom = "80,0", posto = "80,-30",duration = 0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1385_1#1$1")]
[name="？？？"]团窗藻、石花膜、紫苔......
[dialog]
[charslot(slot = "m",posfrom = "80,-30", posto = "50,-30",duration = 0.5)]
[delay(time=0.7)]
[charslot(slot="m",name="avg_npc_1385_1#4$1")]
[name="？？？"]等等，这个色型的千灯英，这是我自己培育的......
[name="？？？"]你们在街道上挣扎......还是太干燥了，你们会枯死的。
[name="？？？"]这里发生了什么？有人对你们做了什么吗？
[Dialog]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m",posfrom = "50,-30", posto = "100,0",duration = 0.3)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1385_1#8$1")]
[name="？？？"]你们要迁移到哪里？有人在......
[name="？？？"]等、等等！
[Dialog]
[charslot(slot = "m",posfrom = "100,0", posto = "-200,0",duration = 1.5,afrom=1,ato=0)]
[PlaySound(key="$rungeneral", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=0.2)]
[charslot]
[Background(image="51_g5_aegirstreet_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="m",name="avg_npc_1385_1#4$1",duration=1)]
[delay(time=1.5)]
[name="？？？"]消失了？
[charslot(slot="m",name="avg_npc_1385_1#3$1")]
[name="？？？"]这个管道口......
[charslot(slot="m",name="avg_npc_1385_1#7$1")]
[name="？？？"]唔！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "0,-150",duration = 1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Dialog]
[playsound(key="$d_avg_jump_water")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot]
[playsound(key="$d_avg_sea", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=3)]
[Background(image="51_g12_seabed",screenadapt="coverall")]
[focusout(duration=3, type="bg", from=1, to=0, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1385_1#5$1",duration=1)]
[delay(time=1.5)]
[name="？？？"]这里是......
[CameraShake(duration=0.2, xstrength=10, ystrength=15, vibrato=15, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1385_1#7$1")]
[name="？？？"]咳咳，咕——
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_divebubble",volume=0.5)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1385_1#7$1")]
[name="？？？"]（是谁？为什么？）
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_rampartclose",volume=0.1)]
[CameraShake(duration=3.5, xstrength=3, ystrength=2, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1385_1#5$1")]
[name="？？？"]（好大的轰鸣......城市要开始移动了吗？）
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_divebubble",volume=0.5)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1385_1#6$1")]
[name="？？？"]（有东西在动——是谁在那里？）
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[focusout(duration=2.5, type="char", from=1, to=1)]
[charslot(slot="m",name="avg_npc_1388_1#1$1",afrom=0,ato=0,posfrom = "0,-200", posto = "0,-200")]
[charslot(slot = "m",action="zoom", poszoom = "0.5,0.5", scale=0.8,duration = 0)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.18,fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.18,fadetime=0.01)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=1)]
[charslot(slot="m",afrom=0,ato=1,duration=2)]
[focusout(duration=2, type="char", from=1, to=0.5)]
[focusout(duration=3, type="bg", from=0, to=1)]
[charslot(slot = "m",action="zoom", poszoom = "0.5,0.5", scale=0.8,duration = 2)]
[charslot(slot = "m",posfrom = "0,-200", posto = "0,-100",duration = 2)]
[delay(time=3)]
[focusout(duration=2, type="char", from=0.5, to=0)]
[charslot(slot = "m",action="zoom", poszoom = "0.5,0.5", scale=1,duration = 2)]
[charslot(slot = "m",posfrom = "0,-100", posto = "0,50",duration = 2)]
[delay(time=2.5)]
[playsound(key="$d_avg_seabornattack",volume=0.5)]
[name="海嗣"]（愉悦地鼓胀液泡）
[stopmusic(fadetime=2)]
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=0.7, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[focusout(type="char", from=0, to=0)]
[focusout(type="bg", from=0, to=0)]
[delay(time=1)]
[curtain]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="51_g4_aegirstreet_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4137_udflow_1#1$1",duration=1.5)]
[delay(time=2)]
[name="西昆妲"]抱歉，希望不会耽误两位的工作。
[dialog]
[charslot]
[charslot(slot = "left", name = "avg_4079_haini_1#2$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]没关系，我和卢契拉只是在对城市单元骨架进行例行检修和维护。
[charslot(slot = "left", name = "avg_4079_haini_1#9$1",focus="l")]
[name="卢契拉"]......所以，还是

... (全文25289字符)
```

### level_act34side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[Delay(time=3)]
[playsound(key="$transmission")]
[Subtitle(text="语音记录#13", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="（未知语言，未知时间）", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[subtitle]
[Delay(time=1)]
[Subtitle(text="联合航运星舰的反应堆还是那么耀眼。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="大气控制中枢坠毁之后，这里就只剩下乏味的阴云了，很少还能见到像这样激动人心的光芒。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="与星舰一同不期而至的是我的瓦莱莉娅。直到她落地，我才知道她是为母亲的告别仪式而来的。自从加入星门的改造项目以后，她就在自己的使命中越陷越深，我没想到她还愿意回来参与这些世俗事务。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="既然她还关心这些俗事，我想，或许还有机会向她提起我们那场拖了十年的婚礼？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......我很快放弃了这个愚蠢的想法。她人确实回来了，但她的状态陌生得可怕。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在母亲的维生舱前，她露出了我从未见过的表情。既不是悲伤，也不是不舍......那是羡慕的表情。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="对一个行将就木的老人，她能羡慕什么？她是羡慕母亲能在模拟出的幻景中安然得到解脱吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Delay(time=2)]
[dialog]
[playMusic(intro="$act18d3d0_intro",key="$act18d3d0_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_1380_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]乔迪，原来你还在这里。其他人都已经离开了......
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]抱歉，我不知道今天会有一场评议会。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]没关系的。
[charslot(slot = "right", name = "avg_npc_1386_1#3$1",focus="r")]
[name="阿维图斯"]啊，这些检索记录......你提了很多问题。“海洋究竟有多辽阔，如果它比陆地大的话，大多少？”
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]“阿戈尔的城市就一直待在海底吗，它可不可以升到海面上去？”
[name="阿维图斯"]“海底没有日夜，阿戈尔人如何区分日夜？”
[name="阿维图斯"]乔迪，你试图通过这样的方式来理解阿戈尔吗？我担心这只会徒增你的困惑。
[charslot(slot = "left", name = "avg_npc_1380_1#4$1",focus="l")]
[name="乔迪"]我......
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]阿维图斯先生，其实，我觉得很激动，没有来由地。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image(image="51_i04",screenadapt="coverall",xScale=1.1,yScale=1.1)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=60, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="乔迪"]我看过审判庭绘制的海图，离开海岸线几海里，就只剩下了代表未知的蓝灰色空白。
[name="乔迪"]甚至在一些条件极度恶劣的地区，我们连海岸线都无法接近。
[name="乔迪"]可在你们的海图上，每一个角落都有那么多信息。地质、能源、生态，我甚至点不完那些无穷无尽的页面。
[name="乔迪"]大洋腹地的森林、永恒不化的冰山、海沟深处的热泉......
[name="乔迪"]就在刚刚，有那么一个瞬间，我觉得大地、天空、海洋，都触手可及。这世间的一切都是为我而准备的。
[name="乔迪"]抱歉，真是狂妄至极的想法。
[name="阿维图斯"]不，年轻人。这只是一种对于世界最质朴的向往。
[name="乔迪"]可我......
年轻的阿戈尔人抬起头，怔怔望着眼前的珊瑚状终端。流动着字符的全息影像在他的脸庞上跃动，点亮那双柔软的眼睛。
[name="乔迪"]阿维图斯先生，我来到这座城市已经一天多了。
[name="乔迪"]我学不会使用你们的科技，听不懂你们在讨论的话题，甚至连方向都搞不明白。
[name="乔迪"]刚刚那场评议会......我也理解不了你们解决争议的方式。
[name="乔迪"]我刚刚搜索了船舶设计师布雷奥甘——我曾以为他是我的先人。我看到了他的相貌，听到了他的录音，见到了他做过的设计......
[name="乔迪"]影像里的那个人真的和我有任何相似之处吗？他的后裔......真的会是我这个样子吗？
[name="乔迪"]我、我找不到自己属于这里的痕迹。
[name="乔迪"]“阿戈尔”就像一座高大而醒目的灯塔，我一直都知道它，可等到我终于看见了它的光亮，走到塔下......
[name="乔迪"]却反而什么都看不清了？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[image]
[charslot(slot = "left", name = "avg_npc_1380_1#1$1")]
[charslot(slot = "right", name = "avg_npc_1386_1#5$1")]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_1386_1#3$1",focus="r")]
[name="阿维图斯"]“布雷奥甘”，我有多久未曾听人提起这个名字了。
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]布雷奥甘在阿戈尔也算得上是位奇人。他曾是技术院最有天赋的设计师，却在阿戈尔最需要他的时候，抛弃了一切前往陆地。
[name="阿维图斯"]说起来，这座城市和布雷奥甘还有些缘分，尽管这缘分有些，微妙。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]微妙？
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]当年，布雷奥甘便是从这座城市前往的陆地，听说几位执政官还因为没能将他留下，险些受到了发展规划所的问责。
[charslot(slot = "left", name = "avg_npc_1380_1#2$1",focus="l")]
[name="乔迪"]这......
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]好了，乔迪，我不能断言你与他是否存在血缘上的联系，但这种联系本身并不重要。
[name="阿维图斯"]你是一名阿戈尔人，这是不言自明的事实。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]我懂，我是阿戈尔人，可如果连先人的血脉也无法追溯，我又该如何证明自己属于这里？
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]我们不需要证明自己的归属。
[name="阿维图斯"]但我能理解你。我们都希望能从过往找到答案。
[name="阿维图斯"]就像我。
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]自豪地说，我是整个阿戈尔最为优秀的先史研究者之一，我相信历史的重量，历史蕴藏着真相与规律，它能告诉我们该往何处去。
[charslot(slot = "right", name = "avg_npc_1386_1#2$1",focus="r")]
[name="阿维图斯"]（轻声）可如果历史告诉我，我们的家园和文明注定毁灭呢？
[charslot(slot = "left", name = "avg_npc_1380_1#5$1",focus="l")]
[name="乔迪"]......您刚刚说什么？
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="51_g4_aegirstreet_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$calm_loop", volume=0.6)]
[delay(time=1)]
[Decision(options="斯卡蒂，你还好吗？", values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="char_263_skadi#3",duration=1)]
[delay(time=2.5)]
[name="斯卡蒂"]博士，你刚刚说了什么？
[name="斯卡蒂"]抱歉。我只是在想鲨鱼和剑鱼的情况。
[dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="她们大概正在屠杀海里

... (全文21042字符)
```

### level_act34side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g1_beaconsquare",screenadapt="coverall")]
[Delay(time=3)]
[playsound(key="$transmission")]
[Subtitle(text="语音记录#21", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="（未知语言，未知时间）", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[subtitle]
[Delay(time=1)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="瓦莱莉娅已经回来半个月了，但从塔罗斯发出的包裹恐怕是到不了了。那些珍贵的技术原型和生物样本，连带着我订购的那台民用级环境模拟单元，一同丧失了音讯。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="没有播报，也没有事故报告，宇宙毫无征兆地对我们关上了门。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可怜的母亲，得在维生舱再熬些时日了。凭私心讲，是我坚持要在模拟环境里与她告别的。直到进入休眠的前一刻她还想着见见孙辈，我该怎么告诉她，她想象中的孙辈根本不存在？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她一定是还活在那个枢纽铺满星海的辉煌年代，才会相信生命的延续不是徒增苦痛。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我为求稳妥才选了塔卫联合工业的产品。母亲太机敏，上一代的模拟技术她一定能识破。可我早该料到如今的星际运输有多大风险。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="瓦莱莉娅的假期用完了，她回去的时候仍在絮絮叨叨地谈着她那些宏大的使命，没有表现出一点遗憾。我不知道她是刚刚放下，还是早就不在乎了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我早晚也会在那张同意书上签字，关停母亲的维生舱吧。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Delay(time=2)]
[dialog]
[charslot(slot = "r", name = "avg_npc_1387_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]您怎么来了？
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",focus="l")]
[name="阿维图斯"]我来看看你，卡西娅。
[name="阿维图斯"]你刚接受过胚胎分离手术，设施管理所应该允许你暂停工作好好休息。
[charslot(slot = "r", name = "avg_npc_1387_1#4$1",focus="r")]
[name="卡西娅"]您知道，胚胎分离手术对身体的损害几乎可以忽略不计，不至于需要休息那么久。
[name="卡西娅"]我一时分不清您是关心我，还是关心孵育室里的那个小家伙，阿维图斯老师。
[charslot(slot = "l", name = "avg_npc_1386_1#5$1",focus="l")]
[name="阿维图斯"]我自然是关心你的，但一个新生的孩子，在如今的阿戈尔也同样值得关注。
[name="阿维图斯"]他降生之后，你会选择亲自抚养他吗，还是交给公共养育所？
[charslot(slot = "r", name = "avg_npc_1387_1#2$1",focus="r")]
[name="卡西娅"]我倾向于不去考虑这个问题。太遥远......太遥远了。
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",focus="l")]
[name="阿维图斯"]来见你之前，我去了趟医院。
[charslot(slot = "r", name = "avg_npc_1387_1#6$1",focus="r")]
[name="卡西娅"]医院？
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",focus="l")]
[name="阿维图斯"]昨天的那场战斗你肯定知道。你不会错过任何消息，对吧？
[name="阿维图斯"]两支舰队，一千多名军团战士，最后仅仅只有二十六人幸存。
[name="阿维图斯"]航道计划已经进行到最紧要的关头，弥利亚留姆却在此时遭遇了远航以来最惨重的牺牲。最近城市里也发生了许多异常......
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]阿维图斯老师，您想说什么？
[charslot(slot = "l", name = "avg_npc_1386_1#6$1",focus="l")]
[name="阿维图斯"]海巡队已经去找过你了吧，卡西娅？
[name="阿维图斯"]关于那个失踪的数据员......
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]阿维图斯老师。
[charslot(slot = "l", name = "avg_npc_1386_1#2$1",focus="l")]
[name="阿维图斯"]......
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]您知道吗，在您整理的所有文献里，我最喜欢的其实是那本《生活的死亡》，尽管它谈不上有什么学术价值。
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",focus="l")]
[name="阿维图斯"]那本书的出现只是个意外。
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]三百多年前，四位伟大的先史文明研究者在地幔遗迹群取得重大发现，无数珍贵的技术资料被带回了阿戈尔。
[name="卡西娅"]相比所有那些技术图纸和理论著作，一份日记般的语音文件确实是不值一提。
[name="卡西娅"]所以它静静地在科学院的资料库里躺着，是您出于好奇，将它们解译，制作成了通俗读物。
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",focus="l")]
[name="阿维图斯"]那不过是一个普通的前人类在漫长旅程中的喃喃自语。
[charslot(slot = "r", name = "avg_npc_1387_1#5$1",focus="r")]
[name="卡西娅"]但我很喜欢这个前人类的故事，老师。
[name="卡西娅"]我喜欢经由他的眼睛所见到的真实。
[name="卡西娅"]曾将无数星球统筹为一体的体制在崩塌，曾使诸多族类连成一心的信任在瓦解。物资的匮乏，技术的失利，哲学与艺术的沉默......
[name="卡西娅"]不论寄托了多少憧憬与想象，那些伟业最终都悄无声息地沦为死灰......就像信标塔里已经死去的那些浮游机械。
[charslot(slot = "l", name = "avg_npc_1386_1#6$1",focus="l")]
[name="阿维图斯"]卡西娅，你在共情他的绝望？
[name="阿维图斯"]我之前从没有在你身上看到过绝望的影子。你甚至选择让自己的孩子降生在一个随时可能面临毁灭的未来。
[name="阿维图斯"]这不是绝望之人所能做出的选择。
[charslot(slot = "r", name = "avg_npc_1387_1#2$1",focus="r")]
[name="卡西娅"]我确实完全不感到绝望。
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]那个古板、颓唐的中年男人......我甚至很难以任何方式与他共情。
[name="卡西娅"]我只是很欣赏您借由他过去的见闻，巧妙地撕开了如今蒙在所有阿戈尔人眼前的这块华美的画布。
[name="卡西娅"]“我们必须接受曾引以为傲的事物和品质在此刻毫无作用，或许它们本来就存在瑕疵或谬误，是这场浩劫让它们暴露了出来。”
[name="卡西娅"]摆脱了生存的忧虑，人就会开始在意价值。我们期望自己的思想、作为，乃至存在本身都有价值。
[name="卡西娅"]阿戈尔的全套体制，都是为发掘人的价值而设计的。
[name="卡西娅"]然而价值是脆弱的。只需要换一个角度去解读，伟大的就会显得渺小，丑陋的就会显得美丽。
[name="卡西娅"]可惜，出于某种惰性，人们大多不愿脱离自己所熟悉的角度。
[charslot(slot = "l", name = "avg_npc_1386_1#1$1",focus="l")]
[name="阿维图斯"]所以人们总是仰赖一成不变的价值而活，当这些价值崩塌的时候，他们也会随之崩溃。
[charslot(slot = "r", name = "avg_npc_1387_1#1$1",focus="r")]
[name="卡西娅"]是啊，就像您现在这样。
[name="卡西娅"]您的绝望是从什么时候开始滋长的？从弥利亚留姆离开本境开始，还是更早些，从您的密人离世时？
[charslot(slot = "l", name = "avg_npc_1386_1#6$1",focus="l")]
[name="阿维图斯"]......卡西娅？
[charslot(slot = "r", name = "avg_npc_1387_1#11$1",focus="r")]
[name="卡西娅"]不过还是感谢您今天来看望我。
[charslot(slot = "r", name = "avg_npc_1387_1#7$1",focus="r")]
[name="卡西娅"]您提醒了我，我确实还有需要完成的事，而时间已经不多了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_474_gladiia_1#1",duration=1)]
[delay(time=2)]
[name="歌蕾蒂娅"]克莱门莎，你竟然允许类似的悲观情绪在自己的城市蔓延？
[charslot(slot="m",name="avg_npc_1382_1#2$1")]
[name="克莱门莎"]《生活的死亡》，阿维图斯整理出版的先史日记。它在问世当年，成了最受公民们欢迎的读物。
[charslot(slot="m",name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]窥伺一种陌生的生活，无聊而愚蠢的猎奇心态。
[charslot(slot="m",name="avg_003_kalts_1#1$1")]
[name="凯尔希"]歌蕾蒂娅，这其中的只言片语，已经足以在陆地上的任何国家引发轩然大波。
[c

... (全文17631字符)
```

### level_act34side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g8_oldinstitute",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1401_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="“小帮手”"]检测结果更新，手术室的生物安全条件达到容许水平。
[name="“小帮手”"]手术随时可以开始。
[charslot(slot="m",name="avg_npc_1381_1#1$1")]
[name="布兰都斯"]猎人们，和以前一样，你们会在自动化手术中保持深度睡眠。
[name="布兰都斯"]在此之外，我会手动修补你们体内老化的自适应接点。
[charslot(slot = "m", focus = "n")]
[name="幽灵鲨"]这满屋子的标本，还有这些实验台，真是熟悉的布置。距离我们上次躺在这样的环境中，已经过了多久？
[charslot(slot="m",name="avg_npc_1381_1#1$1")]
[name="布兰都斯"]五年，劳伦缇娜。
[name="布兰都斯"]我本应等到髓质替换手术的全套流程结束，你的体细胞与源石融合率得到控制，再去处理你作为深海猎人的那部分问题。
[name="布兰都斯"]但时间仓促，我只好尽可能帮你恢复应有的稳定状态。
[charslot(slot="m",name="avg_npc_1381_1#7$1")]
[name="布兰都斯"]抱歉，劳伦缇娜。
[charslot(slot = "m", focus = "n")]
[name="幽灵鲨"]您还是那么多愁善感。
[name="幽灵鲨"]对了，按照老规矩......
[charslot(slot="m",name="avg_npc_1381_1#8$1")]
[name="布兰都斯"]在你的身旁点亮一根蜡烛，让我们的小美人鱼睡着时看起来别太苍白。我已经让他们准备好了。
[charslot(slot = "m", focus = "n")]
[name="幽灵鲨"]您果然还记得。
[charslot]
[charslot(slot="m",name="avg_npc_1401_1#1$1")]
[name="“小帮手”"]休眠溶胶填注中，请您保持舒适的姿势，不要移动。
[charslot]
[name="斯卡蒂"]现在这个情景，跟以前差不多。除了人少了很多。
[name="斯卡蒂"]解决完海沟里那些杂碎，闭上眼睛，听听顾问的唠叨，泡进休眠溶胶，睡上一觉。
[name="斯卡蒂"]等到睡醒，残留在身上的那些令人作呕的味道就全都消失了。
[charslot(slot="m",name="avg_npc_1381_1#1$1")]
[name="布兰都斯"]在恶劣多变的陆地环境里长期无人照管，你们的身体状况非常不稳定。
[name="布兰都斯"]自适应接点能自主监视你们体内的海嗣基因，但五年的磨损足以让最精密的仪器变得迟钝。
[name="布兰都斯"]况且，在长时间与海嗣基因相抗争的过程中，你们身体的免疫系统也难免失调。
[name="布兰都斯"]我会尽可能让你们恢复到最佳状态，不过这五年岁月拿走的东西，我可就找不回来了。
[charslot(slot = "m", focus = "n")]
[name="斯卡蒂"]嗯。
[charslot(slot="m",name="avg_npc_1381_1#1$1")]
[name="布兰都斯"]歌蕾蒂娅，我们在评议会上的接触并不愉快，我更愿意将此时此刻，当作你们回到家乡后，你我的第一次见面。
[name="布兰都斯"]但你从刚刚开始，一直没怎么说话。
[charslot(slot = "m", focus = "n")]
[name="歌蕾蒂娅"]布兰都斯，关于这场手术，你是否还有什么其他的事项需要交代？
[name="歌蕾蒂娅"]没有的话，更多的话题就留在之后——关于这五年来，我们发生了怎样的变化，以及，你发生了怎样的变化。
[charslot(slot="m",name="avg_npc_1381_1#1$1")]
[name="布兰都斯"]......
[charslot(slot="m",name="avg_npc_1401_1#1$1")]
[name="“小帮手”"]请保持静止，休眠程序将在十秒后启动。
[charslot(slot="m",name="avg_npc_1381_1#8$1")]
[name="布兰都斯"]那么，好眠，猎人们。
[dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[name="？？？"]布兰都斯顾问，有些情况需要您重新确认。
[charslot(slot="m",name="avg_npc_1381_1#5$1")]
[name="布兰都斯"]我不是说过了，手术室已经封锁，接下来我要为猎人们修补自适应接点，任何人都不得打扰。
[charslot(slot = "m", focus = "n")]
[name="？？？"]中控层发现了异样，保险起见，您还是亲自确认一下。
[charslot(slot="m",name="avg_npc_1381_1#1$1")]
[name="布兰都斯"]......稍等，我给你们开门。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1")]
[charslot(slot = "right", name = "avg_4009_irene_1#1$1")]
[Background(image="51_g4_aegirstreet_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1",focus="l")]
[name="西昆妲"]穹顶上的监测单元对城市进行了紧急扫描，在这里发现了密集的藻类生物信号。
[charslot(slot = "right", name = "avg_4009_irene_1#1$1",focus="r")]
[name="艾丽妮"]感谢你通知我。
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1",focus="l")]
[name="西昆妲"]没什么。
[name="西昆妲"]图利娅的调查你既然已经参与，没有中途退出的道理。
[charslot(slot = "left", name = "avg_4137_udflow_1#3$1",focus="l")]
[name="西昆妲"]地面与穹顶的交界处......这里原本是行道珊瑚的试验田。
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1",focus="l")]
[name="西昆妲"]虽然比不上生态艺术创作所的专业环境，但相比私人房间内的小型水培箱，这里确实更适合藻类培育。
[name="西昆妲"]或许是性格使然，又或者动机不纯，图利娅始终没有通过正规渠道申请过场地，她私自找到了这里。
[charslot(slot = "right", name = "avg_4009_irene_1#1$1",focus="r")]
[name="艾丽妮"]图利娅......
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]我们并不清楚具体的情况，里面是否是深海教会的藏身之所，图利娅又是否身处其中......总之，要小心。
[name="西昆妲"]一队已经在附近的街区布防，对道路进行监视。艾丽妮，你跟着二队，从地面的道路突入。
[name="西昆妲"]至于与穹顶夹层联通的这条路，交给我。
[charslot(slot = "right", name = "avg_4009_irene_1#1$1",focus="r")]
[name="艾丽妮"]好。
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]行动。
[dialog]
[charslot(slot = "r",posfrom = "0,0", posto = "200,0",duration = 1)]
[charslot(slot = "l",posfrom = "0,0", posto = "-200,0",duration = 1)]
[charslot(duration=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g5_aegirstreet_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_4137_udflow_1#5$1")]
[name="西昆妲"]谁？
[dialog]
[playsound(key="$d_gen_transmissionget")]
[charslot(slot = "m", focus = "n")]
[delay(time=1)]
[name="海巡队队员"]西昆妲指挥官，你那边发生了什么，是否需要增援？
[charslot(slot = "m", focus = "n")]
有人挡在了她的面前，准确说，是她出现在了对方离开的路上。
对方身处建筑夹角形成的阴影当中，全身上下与阴影同色，唯有那双眼睛，那双西昆妲再熟悉不过的眼睛......
[charslot(slot = "m", name = "avg_4137_udflow_1#1$1")]
[name="西昆妲"]......按照原计划行动。
[playsound(key="$transmission")]
西昆妲掐断了通讯。
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4145_Ulpia_1#1$1",duration=1.5)]
[delay(time=2)]
[name="乌尔比安"]......
[charslot(slot = "m", name = "avg_4137_udflow_1#1$1")]
[name="西昆妲"]......好久不见，“老师”。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="51_g8_oldinstitute",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1392_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1397_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", focus="r")]
[name="“研究员A”"]航道计划的武器技术顾问，第Ⅳ级武器的研发专家，布兰都斯，是吧？
[charslot]
[playMusic(intro="$escape_intro",key="$escape_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1381_1#5$1")]
[name="布兰都斯"]......你们不是研究所的人。
[charslot]
[charslot(slot = "right",name = "avg_npc_1397_1#1$1", focus="r")]
[charslot(slot = "left", name = "avg_npc_1392_1#1$1",focus="r")]


... (全文22066字符)
```

### level_act34side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[Delay(time=3)]
[playsound(key="$transmission")]
[Subtitle(text="语音记录#33", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="（未知语言，未知时间）", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[subtitle]
[Delay(time=1)]
[Subtitle(text="星门的改造计划显然成功了，我们与塔罗斯重新建立了连接。两年来积压的讯息像潮水般涌来，可其中并无喜讯。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="先是小行星带之外的考察站，随后是整个系统的星际枢纽，最后，宜居行星轨道上的巡航舰队也陷入沉寂。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="就连已经成为移动博物馆的那支古老的殖民舰队，也未能幸免。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="与这些骇人的消息一同不期而至的，是瓦莱莉娅最后留下的一点材料。她的笔记还像她本人那样，总是絮叨个不停。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="只是，除了技术文献外，她在最后的时间里似乎还反复翻看着文学和历史，那些伟人与英雄死亡的场面、他们的遗言与墓志铭......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="仿佛一个孩子，在参加成人礼的前一天，迷茫地翻找着父母的衣柜，试图找出一件足够庄重的衣服。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她是觉得自己的一生不够伟大、不够沉重吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不，她几乎把自己的一切都留在了星门。若是放在过去，她的成就怎么可能不被载入史册？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可如今看来，那也不过是在两间闭锁的小黑屋之间，打开了一扇狭窄的门。恐怕过不了多久，这扇小门还会再一次被关上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="人类的历史终于还是超出了人类的尺度，哈。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_microrobot")]
[charslot(slot="m",name="avg_npc_1401_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="设施管理所的“小帮手”"]读数误差，第二次报错。
[name="设施管理所的“小帮手”"]是否运行故障测试？
[charslot]
[charslot(slot="r",name="avg_npc_1386_1#1$1")]
[name="阿维图斯"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1380_1#2$1",focus="l")]
[name="乔迪"]阿维图斯先生，需要我帮您吗？
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]不，不用。我只是在观察这台被人抛下的小帮手。
[charslot(slot = "left", name = "avg_npc_1380_1#5$1",focus="l")]
[name="乔迪"]被谁......抛下？
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]没什么，那不重要。乔迪，你为什么来这里？
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]我希望找到一件自己能做的事情。情况分明很紧急，这座城市里一定有很多亟待解决的问题，我只是，还没发现。
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]一般来说，遇到这种情况，你应该去找发展规划所，请他们帮你做评估。
[name="阿维图斯"]不过如果你想找的是我，我也愿意尽量帮你。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]当然，您是备受尊敬的学者，城市里许多人都称呼您为老师。
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]老师？我出版的最后一部作品，还是那本《生活的死亡》，一本没法教会别人任何东西的书。
[charslot(slot = "left", name = "avg_npc_1380_1#8$1",focus="l")]
[name="乔迪"]我、我读过。可我看不懂里面的内容，那些名词都太过晦涩了。什么星舰、星门，像是天外读物。
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]“天外读物”，哈，你的形容倒也没错。
[name="阿维图斯"]可我确实称不上什么老师，我自己也时常陷入迷茫。
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]乔迪，你还记得我和你说过血缘上的联系并不重要吗？
[charslot(slot = "left", name = "avg_npc_1380_1#8$1",focus="l")]
[name="乔迪"]我记得，但我已经......
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]我当时的话或许有些误导性。我们确实不在意血缘上的联系，但“联系”本身，是一个很好的切入点。
[name="阿维图斯"]在迷茫的时候，人应该顺着自己与现实的联系——无论那是一种生活，还是一种理想——去寻找方向。
[name="阿维图斯"]不然就会像我一样，长久地陷入对自我存在价值的质疑。
[charslot(slot = "left", name = "avg_npc_1380_1#2$1",focus="l")]
[name="乔迪"]阿维图斯先生，冒昧地问一下，您自己的“联系”......
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]我的密人。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]密......人？
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]与我志同道合，能够丰盈我的精神与思想的人。我热爱她，一如我热爱阿戈尔，以及我们为它所做的一切。
[name="阿维图斯"]先史文明那些卷帙浩繁的史料，陌生的文字、难以理解的语法......我享受将它们一点点解译成阿戈尔文字的过程。
[name="阿维图斯"]我和我的密人也在这个过程中相识，我还记得她投入工作的模样......聊到兴头上，她几乎能用眉毛跳起舞来。
[name="阿维图斯"]我这样夸过她之后，她还饶有兴致地去找形体艺术研究所的人，琢磨怎么真的用眉毛跳舞。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]好奇怪的艺术......他们成功了吗？
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]严格来说没有，不过受她启发，形体艺术研究所的人后来研究出了可以凭意志让头发自主舞动的技术。
[name="阿维图斯"]哪怕经历过那场让整片海洋都失声的灾难，哪怕海嗣已经威胁到阿戈尔的存续，我们依然没有放弃对科学和艺术的探索，对未来的想象。
[name="阿维图斯"]将能源泵出地幔的熔岩导桥、将洋流化作喷泉的水脉中枢、照亮海渊最深处的人工太阳、在不毛的海床铺满生机的生态基站......
[name="阿维图斯"]我们仍在努力将前人类的失落之物，转化成一座座神奇的巨构。我们仅凭一时兴起的想象，便能激发许多新事物的诞生。
[name="阿维图斯"]一百五十年，实在是太过短暂了。
[charslot(slot = "left", name = "avg_npc_1380_1#2$1",focus="l")]
[name="乔迪"]一百五十年？
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]是啊，阿戈尔的人均寿命只有短短的一百五十年。
[charslot(slot = "left", name = "avg_npc_1380_1#4$1",focus="l")]
[name="乔迪"]“短短”......
[charslot(slot = "right", name = "avg_npc_1386_1#5$1",focus="r")]
[name="阿维图斯"]越是被危机追赶的年代，我们的创造越有价值。
[name="阿维图斯"]我们坚信自己会度过充实的时光，不留遗憾地走向生命的终结，将文明的火种传承下去。
[name="阿维图斯"]我们规划好了教育的流程，我们相信自己能做得比公共养育所更好。
[name="阿维图斯"]孩子从孵育室诞生之后，我们将亲自抚养他长大。他将拥有激荡的精神与鲜活的思想，成为更具创造力的一代。
[name="阿维图斯"]亲自抚养孩子确实不常见，但我们的人生如此充实，我们希望能将自己珍视的价值亲手传承下去。
[charslot(slot = "left", name = "avg_npc_1380_1#1$1",focus="l")]
[name="乔迪"]那您的密人？
[charslot(slot = "right", name = "avg_npc_1386_1#2$1",focus="r")]
[name="阿维图斯"]死了。
[charslot(slot = "left", name = "avg_npc_1380_1#10$1",focus="l")]
[name="乔迪"]......
[charslot(slot = "right", name = "avg_npc_1386_1#1$1",focus="r")]
[name="阿维图斯"]还记得《生活的死亡》中的那个前人类吗？
[name="阿维图斯"]缩在某个不知名的避难所，日复一日地盯着压向大地的天空。他已经预感到了自己最后的结局。
[name="阿维图斯"]除了平静地迎接它的到来，他无事可做。
[charslot(slot = "left", nam

... (全文20085字符)
```

### level_act34side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="51_g11_aegirroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1392_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]海巡队。你是来审问我的？
[name="受伤的“研究员”"]“审问”，哈，我从没想过这个词居然会和自己有关。
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1",focus="l")]
[name="西昆妲"]你在侵入研究所的时候就应该想到了。
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]在那之前呢？你我之间究竟有什么区别？
[name="受伤的“研究员”"]为什么你在这里“审问”，而我在这里“受审”？
[charslot(slot = "left", name = "avg_4137_udflow_1#1$1",focus="l")]
[name="西昆妲"]我有时候会觉得我们的手段太温和了。
[name="西昆妲"]听伊比利亚的使节说，他们会在审问阶段就应用刑罚。
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]......
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]如果没有更多废话了，交代你的身份。
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]我先前负责培育行道珊瑚。
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]作案动机？
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]你有仔细观察过路边的行道珊瑚吗，海巡队？
[name="受伤的“研究员”"]我们希望每一条街道的每一株行道珊瑚，都呈现出不同的形态、色泽，甚至承载不同的功能。
[name="受伤的“研究员”"]斗智场东侧的那一株，物流缆线从它满是空洞的身躯间穿行，在缆线微光的映照下，一只只珊瑚虫反射出点点明光......
[name="受伤的“研究员”"]就像是一片小小的星云。
[name="受伤的“研究员”"]还有港口枢纽外围——
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]就在刚刚，我仔细观察了不止一株行道珊瑚，在你们先前的试验田。
[name="西昆妲"]一位无辜的数据员就在那里死去。
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]......
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]她的理想，她的执念，她所喜爱的那些藻类......与你所描述的行道珊瑚一样美。
[name="西昆妲"]但你们谋害了她。
[name="西昆妲"]你问得很对。那你与她之间究竟有什么区别？
[name="西昆妲"]为什么你能活着，而她必须死去？
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]因为她发现......
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]发现了什么？怎么不说了？
[name="西昆妲"]还是说，我应该把这个问题拿去问卡西娅？
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]你......
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]深海教会对航道计划动了什么手脚？
[name="西昆妲"]你们集中攻击的是信标，还是武器？
[charslot(slot = "left", name = "avg_4137_udflow_1#6$1",focus="l")]
[name="西昆妲"]说。
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]唉，深海教会，深海教徒。
[name="受伤的“研究员”"]我还是很不习惯被这么称呼，好陌生的名字。真不是你们海巡队为了方便抓人才起的这些名字吗？
[charslot(slot = "left", name = "avg_4137_udflow_1#5$1",focus="l")]
[name="西昆妲"]......
[charslot(slot = "right",focus="r")]
[name="受伤的“研究员”"]所谓教会、教徒，它的神圣性在哪里？
[name="受伤的“研究员”"]我甚至没在崇拜什么虚无缥缈的存在，我只是认同卡西娅的看法。
[name="受伤的“研究员”"]从弥漫在阿戈尔的绝望当中，她看到了这个国家的脆弱性。
[name="受伤的“研究员”"]人们太过看重事物的价值，却又不肯承认这些价值是多么脆弱而多变，他们变成了某种既定价值的忠实信徒。
[name="受伤的“研究员”"]可现在，这种价值正在崩塌。在阿戈尔完全陷入绝望之前，总有人得敲响警——
[dialog]
[charslot(slot = "m", focus = "all")]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[delay(time=1.5)]
[charslot(slot = "right",focus="r")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="受伤的“研究员”"]*阿戈尔感叹词*！你在套我的话。
[name="受伤的“研究员”"]我不会再说一个字了。你要是不耐烦，大可以解析我的脑波，又不费什么事——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "left", name = "avg_4137_udflow_1#6$1",focus="l")]
[name="西昆妲"]提问是对你身为人的最后一点尊重，渣滓！
[name="西昆妲"]你可以认为自己是无辜的，也可以认为自己的所作所为不属于阴谋。但你会一点不落地吐出这些信息。
[name="西昆妲"]现在，说。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="51_g9_shipport",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$rebel_intro",key="$rebel_loop", volume=0.6)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_474_gladiia_1#1",duration = 1)]
[charslot(slot = "right", name = "char_263_skadi#3",duration = 1)]
[delay(time=2)]
[charslot(slot = "right", name = "char_263_skadi#3",focus="r")]
[name="斯卡蒂"]二队长。
[charslot(slot = "left", name = "avg_474_gladiia_1#1",focus="l")]
[name="歌蕾蒂娅"]斯卡蒂，离我们出发的时间很近了。
[charslot(slot = "right", name = "char_263_skadi#3",focus="r")]
[name="斯卡蒂"]我知道情况很紧急。
[charslot(slot = "left", name = "avg_474_gladiia_1#1",focus="l")]
[name="歌蕾蒂娅"]前线的军力只能勉强与海嗣维持均势，整整两支舰队完全覆灭的恶果到现在完全显现了出来。
[name="歌蕾蒂娅"]按照他们刚刚传回的消息，第八、第十军团几次尝试变阵都以失败告终，他们陷入了苦战。
[charslot(slot = "left", name = "avg_474_gladiia_1#5",focus="l")]
[name="歌蕾蒂娅"]如果无法将信标投放到巢穴内的指定位置，继续僵持......意味着航道计划的失败。
[charslot(slot = "right", name = "char_263_skadi#9",focus="r")]
[name="斯卡蒂"]我明白。
[charslot(slot = "left", name = "avg_474_gladiia_1#1",focus="l")]
[name="歌蕾蒂娅"]军团的舰队即将不计代价地向海嗣发起全线进攻，吸引海嗣的注意力，至于我们——
[charslot(slot = "right", name = "char_263_skadi#3",focus="r")]
[name="斯卡蒂"]我们会切入战场的死角，深入巢穴，投放信标。
[charslot(slot = "left", name = "avg_474_gladiia_1#1",focus="l")]
[name="歌蕾蒂娅"]嗯。斯卡蒂，你觉得自己的状态怎么样？
[charslot(slot = "right", name = "char_263_skadi#5",focus="r")]
[name="斯卡蒂"]至少刚才我睡得很好。自那场战役以来，我还是第一次体验无梦的睡眠。
[charslot(slot = "left", name = "avg_474_gladiia_1#1",focus="l")]
[name="歌蕾蒂娅"]现在城内的局势越发动荡......你知道博士去哪了吗？
[charslot(slot = "right", name = "char_263_skadi#3",focus="r")]
[name="斯卡蒂"]（摇头）
[name="斯卡蒂"]二队长，我知道你提博士是想说什么。你想让我去维持秩序，保护博士......总之，你想让我继续留在城里。
[charslot(slot = "left", name = "avg_474_gladiia_1#1",focus="l")]
[name="歌蕾蒂娅"]坦白地说，我在犹豫。
[name="歌蕾蒂娅"]清扫海洋里的渣滓是深海猎人的责任，但我也需要为你们的安全负责。
[name="歌蕾蒂娅"]斯卡蒂，回到海洋后，伊莎玛拉是否有醒转的迹象？
[charslot(slot = "right", name = "char_263_skadi#3",focus="r")]
[name="斯卡蒂"]如果它在，那它很安静。
[name="斯卡蒂"]如果它说话，那我会让它闭嘴。
[name="斯卡蒂"]二队长，我找你其实有话要说。
[charslot(slot = "right", name = "char_263_skadi#8",focus="r")]
[name="斯卡蒂"]我们之前做事从来不像现在这样谨小慎微。我们有一套应对这种情况的做法。
[name="斯卡蒂"]如果那些深海教徒的神，那些渣滓口中的“伊莎玛拉”真的存在在我的身体里，一旦我失控，那么你当场处决我，很简单。
[name="斯卡蒂"]我的心脏就在这里，你不会失手。
[charslot(slot = "left", name = "avg_474_gladiia_1#5",focus="l")]
[name="歌蕾蒂娅"]斯卡蒂——
[charslot(slot = "right", name = "char_263_skadi#8",focus="r")]
[name="斯卡蒂"]还没完，二队

... (全文12740字符)
```

### level_act34side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g12_seabed",screenadapt="coverall")]
[PlaySound(key="$d_avg_underwtr", volume=1, loop=true, channel="u")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1023_ghost2_1#5$1", duration = 1, isblock=true)]
[name="幽灵鲨"]唔，真难闻。
[name="幽灵鲨"]这么多年了，他们还是懒得改良伪装霜剂——明明可以让它对我们和对海嗣呈现出两种不同气味的。
[charslot(slot = "m", name = "char_263_skadi#3")]
[name="斯卡蒂"]别做多余的动作，鲨鱼，那样只会让气味变得更重。
[name="斯卡蒂"]如果你一直散发出这么浓重的海嗣气味，我会忍不住想要砍你。
[dialog]
[charslot]
[PlaySound(key="$d_avg_erthshkng", volume=1, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=6)]
[PlaySound(key="$d_avg_rockfall", volume=0.8)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]整片台地都在震动......那些蠕虫状的巨型海嗣正在从我们身下的岩层钻过。
[name="歌蕾蒂娅"]注意隐蔽。
[dialog]
[charslot]
[SoundVolume(volume=0.2, channel="u",fadetime=2)]
[PlaySound(key="$d_avg_swimdeepsea", volume=1)]
[charslot(slot = "r", name = "avg_npc_1388_1#1$1", posfrom="0,-50", posto="0,50", duration=1.5)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1388_1#1$1", posfrom="0,-50", posto="0,50", duration=1.5)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_seabornactivity_1", volume=1)]
[charslot(slot = "r", action="shake", power=1, times=10, duration=0.8)]
[charslot(slot = "r", focus="r")]
[name="海嗣"]（轻微地颤动液泡）
[PlaySound(key="$d_avg_seabornactivity_2", volume=1)]
[charslot(slot = "l", action="shake", power=5, times=30, duration=0.8)]
[charslot(slot = "l", focus="l")]
[name="海嗣"]（剧烈地抖动内核）
[dialog]
[PlaySound(key="$d_avg_swimdeepsea", volume=1)]
[charslot(slot = "r", name = "avg_npc_1388_1#1$1", posfrom="0,50", posto="0,150", afrom=1, ato=0, duration=1)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1388_1#1$1", posfrom="0,50", posto="0,150", afrom=1, ato=0, duration=1, isblock=true)]
[delay(time=1)]
[SoundVolume(volume=1, channel="u",fadetime=2)]
[charslot(slot = "m", name = "avg_1023_ghost2_1#5$1")]
[name="幽灵鲨"]这个数量，该说是海流裹挟着海嗣，还是海嗣组成了海流？
[name="幽灵鲨"]它们在向前线涌去，很难想象......
[charslot(slot = "m", name = "char_263_skadi#8")]
[name="斯卡蒂"]很难想象前线的战士们在遭遇什么样的战斗。
[charslot(slot = "m", name = "avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]斯卡蒂，冷静，不要把你的剑柄捏断了。
[name="歌蕾蒂娅"]完成任务是对前线战士最好的哀悼。
[name="歌蕾蒂娅"]军团舰队实现了对海嗣集群的牵制，我们才得以潜入巢穴深处投放信标。
[name="歌蕾蒂娅"]哪怕只是一株被海嗣同化的植物，也随时可能让我们暴露在海嗣的视线当中。前面这段路容不得一点疏忽。
[name="歌蕾蒂娅"]现在，以那些枯死的巨型珊瑚为掩体，向裂谷深处下潜。
[charslot]
[charslot(slot = "r", name = "char_263_skadi#3")]
[charslot(slot = "l", name = "avg_1023_ghost2_1#12$1")]
[name="幽灵鲨&斯卡蒂"]明白。
[dialog]
[PlaySound(key="$d_avg_swimdeepsea", volume=1)]
[charslot(slot = "l", afrom=1, ato=0, duration=1.5)]
[delay(time=0.5)]
[charslot(slot = "r", afrom=1, ato=0, duration=1.5, isblock=true)]
[StopSound(channel="u", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g1_beaconsquare",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_1380_1#1$1")]
[charslot(slot = "r", name = "avg_npc_1396_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]乔迪，对吧？你上手很快。
[name="信标塔技术员"]以前来我们这做职业体验的学生，不花上一天时间理清操作流程，都很容易误触。你倒是在旁边看一会儿就会了。
[name="信标塔技术员"]有基础？
[charslot(slot = "l", name = "avg_npc_1380_1#1$1", focus="l")]
[name="乔迪"]只有一点点。我曾经在伊比利亚的大灯塔上工作过，灯塔和信标塔的原理稍有些相通的地方。
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]既然你的兴趣是工程学，那就不奇怪了。
[charslot(slot = "l", name = "avg_npc_1380_1#11$1", focus="l")]
[name="乔迪"]不过我做得最久的工作其实是护工。
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]“护工”？那是一种什么职业？
[charslot(slot = "l", name = "avg_npc_1380_1#5$1", focus="l")]
[name="乔迪"]欸？
[charslot(slot = "l", name = "avg_npc_1380_1#1$1", focus="l")]
[name="乔迪"]啊，就是看护老人和病人，照料他们的起居，也打理打理杂务。
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]原来如此，听起来像是小帮手同时加装153号和274号组件。
[charslot(slot = "l", name = "avg_npc_1380_1#8$1", focus="l")]
[name="乔迪"]呃，我记得小帮手是没有人格的......对、对吧？
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]对的。
[name="信标塔技术员"]你看起来很紧张，乔迪。我又不是你的阿戈尔小常识考官。
[charslot(slot = "l", name = "avg_npc_1380_1#2$1", focus="l")]
[name="乔迪"]我是想问，如果小帮手没有人格，那它要怎么应对老人或病人的情感需求？
[name="乔迪"]毕竟，护工要面对的是人最脆弱、最难堪的一面。
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]我们倒是很少因为身体上的脆弱而产生额外的情感需求。安然走向死亡的人，哪怕疾病缠身，也没什么难堪的。
[name="信标塔技术员"]老人或病人确实可以在接受安乐死之前申请临终对谈，通常会由极富名望的哲学家或其他领域的学者来接待他们。
[charslot(slot = "l", name = "avg_npc_1380_1#2$1", focus="l")]
[name="乔迪"]我、我完全不懂什么哲学......
[name="乔迪"]我只会聊些最普通的话题，饭菜、花草与阳光之类的。但不知道为什么，听到的人都会很开心。
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]很了不起，乔迪。
[name="信标塔技术员"]这说明你能敏锐地把握住他人的情绪。搞不好，你在发展规划所或者公共养育所都能找到大展身手的机会。
[charslot(slot = "l", name = "avg_npc_1380_1#8$1", focus="l")]
[name="乔迪"]我、我能吗？
[name="乔迪"]......不管怎么说，还是谢谢您！这里的存储设备我已经重置完成了！
[charslot(slot = "r", name = "avg_npc_1396_1#1$1", focus="r")]
[name="信标塔技术员"]很完美的操作。所以说——
[dialog]
[stopmusic(fadetime=2)]
[delay(time=1)]
[name="信标塔技术员"]等等。刚刚全息影像上是不是闪过去什么东西？
[charslot(slot = "l", name = "avg_npc_1380_1#5$1", focus="l")]
[name="乔迪"]什么——
[dialog]
[charslot]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_aircraftimpact", volume=1, channel="1")]
[CameraShake(duration=2, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=25

... (全文19686字符)
```

### level_act34side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g8_oldinstitute",screenadapt="coverall")]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r",  focus="r")]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", posfrom="0,-50", posto="0,0", duration=1.5, isblock=true)]
[Delay(time=0.8)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", posfrom="-200,0", posto="0,0", duration=1.5)]
[Delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", focus="l")]
[name="布兰都斯"]啊，你醒了？
[name="布兰都斯"]伤口我已经帮你处理过了。旁边有两支神经活性剂，能让你快速恢复精神。我来注射，还是交给小帮手？
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]......
[charslot(slot = "l", name = "avg_npc_1381_1#10$1", focus="l")]
[name="布兰都斯"]好吧，你自己来。
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", focus="l")]
[name="布兰都斯"]......动作真熟练，看起来恢复得不错。
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]虽然劝也没用，但我还是得多说一句。
[name="布兰都斯"]你不能一直在自己身上做实验，不然光戴上面罩还不够，你得把眼睛也遮住，才能不至于看起来像受过虐待。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]我的着装习惯与改造实验无关。
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", focus="l")]
[name="布兰都斯"]也是，你一直是这副模样。当年你只要阴暗地走进教室坐下，就足够让我们所有人打个寒战了。
[name="布兰都斯"]我们认识这么多年，我平时都见不到你的脸。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#8$1", focus="r")]
[name="乌尔比安"]布兰都斯，你既然开起了玩笑，看来结果并不算糟糕？
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]很难用糟不糟糕来评价，我刚刚的情绪体验，就像是西昆妲闭着眼睛开巡逻舰，而我坐在她旁边一样——天翻地覆。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#3$1", focus="r")]
[name="乌尔比安"]......
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]起初，我观察到自适应接点技术产生了预料之外的效果......
[name="布兰都斯"]你的身体没有像预期中那样，在海嗣基因表现出异常的性状控制力时，加强对海嗣基因的排斥。排异的表现反而有所减轻。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]这意味着我的海嗣化进程正在加快？
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", focus="l")]
[name="布兰都斯"]不，恰恰相反。
[name="布兰都斯"]就在准备中断手术的时候，我观察到了奇妙的现象。在你身体的排异反应减轻之后，海嗣基因也放缓了对你的性状控制。
[name="布兰都斯"]简直就好像——你的身体与海嗣的基因达成了某种共识。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]这种现象有进一步研究的价值。不过现在，我需要知道，这种情况是否会影响深海猎人接下来的作战。
[name="乌尔比安"]斩杀“初生”，这将会是深海猎人诞生以来最重要的一次行动。
[name="乌尔比安"]在这个时间节点上，我不允许出现任何变故。
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]目前还没有观察到负面的影响，在你们出发之前，我会继续安排几次安全性测试。
[name="布兰都斯"]不过，要真正摸清这种现象背后的原理，最好是你能活着回来，帮我做进一步的研究。
[charslot(slot = "l", name = "avg_npc_1381_1#5$1", focus="l")]
[name="布兰都斯"]说实话，我很不放心。
[name="布兰都斯"]毕竟我们从来没有发起过如此规模的战争，将所有的深海猎人，三支完整的正规军团，派往一处海沟......
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]没有这样的一场战争，我们如何斩杀海嗣的生代，它们的源头，它们的“神”？
[charslot(slot = "l", name = "avg_npc_1381_1#10$1", focus="l")]
[name="布兰都斯"]你真的相信我们能就此一劳永逸地解决海嗣问题吗？
[charslot(slot = "r", name = "avg_4145_Ulpia_1#8$1", focus="r")]
[name="乌尔比安"]哪怕已经与我们共事十多年，你还是没有消除对深海猎人计划的怀疑。
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]你要听实话吗？
[charslot(slot = "r", name = "avg_4145_Ulpia_1#8$1", focus="r")]
[name="乌尔比安"]......
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]说实话，这种以扭曲演化的轨迹、牺牲同胞的人性为前提的计划，在审核阶段就应该被驳回。
[name="布兰都斯"]若不是因为你，我根本不会去考虑它的可行性，更不可能为它付出十多年的努力。
[name="布兰都斯"]......既然已经身陷其中，那么越是怀疑，我越要成为最核心的参与者，亲手掌控它的走向。
[charslot(slot = "l", name = "avg_npc_1381_1#2$1", focus="l")]
[name="布兰都斯"]但我还是忘不掉，这间研究所创造出了多少“怪物”。
[name="布兰都斯"]他们大多数由你亲手处决，乌尔比安。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]是。
[charslot(slot = "l", name = "avg_npc_1381_1#7$1", focus="l")]
[name="布兰都斯"]他们的死甚至算不上“牺牲”，对吧？
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]被海嗣摧毁了家园，夺去了生命的阿戈尔人更多。
[name="乌尔比安"]布兰都斯，这样的辩论我们进行了很多遍，没有必要在临行前再来一次。
[name="乌尔比安"]尽快安排安全性测试吧。另外，正在进行中的深海猎人改造实验也需要全部暂停。
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]你的意思是？
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]没有猎人在场的情况下，实验中如果出现任何异样，会很难处理。
[charslot(slot = "l", name = "avg_npc_1381_1#1$1", focus="l")]
[name="布兰都斯"]“异样”。
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1381_1#10$1", focus="l")]
[name="布兰都斯"]乌尔比安，十多年来，深海猎人计划始终由你主持，但你自己同样无法完全信任它，对吗？
[name="布兰都斯"]这才是你选择做第一个受试者的理由。
[name="布兰都斯"]这场战役能否一劳永逸地解决海嗣危机，你其实也没有十足的把握。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#4$1", focus="r")]
[name="乌尔比安"]布兰都斯......
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", focus="l")]
[name="布兰都斯"]不，乌尔比安，时至今日，我比谁都期待这场战役能够取得胜利。
[name="布兰都斯"]或许等你们平安返航的时候，深海猎人计划已经没有存在的必要。到时候，我们甚至可以重新拾起曾经的研究项目。
[name="布兰都斯"]你是不是都快忘了？之前在评议会上，我还遇见了我们的导师。他还问起了我们的理想。
[charslot(slot = "r", name = "avg_4145_Ulpia_1#1$1", focus="r")]
[name="乌尔比安"]“阿戈尔细胞演变史”。
[charslot(slot = "l", name = "avg_npc_1381_1#9$1", focus="l")]
[name="布兰都斯"]不是多么宏大的课题，但从一个微小的切面审视我们自身的源流，我坚信那是一种美的追求。
[name="布兰都斯"]从千万年前在江河中摆动附肢的先祖，到如今在此畅谈科学与理想的你我，这之中蕴藏着一种内在秩序的流变。
[charslot(slot = "l", name = "avg_npc_1381_1#8$1", focus="l")]
[name="布兰都斯"]乌尔比安，或许我们还有机会见证它？
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g3_beaconctrlroom",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4145_Ulpia_1#1$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1381_1#8$1")]
[name="布兰都斯"]咳咳......你终于来了，乌尔比安。
[charslo

... (全文15033字符)
```

### level_act34side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_deepseaamb", volume=1, loop=true, channel="u")]
总有铃铛般的乐声从穹顶上传来，那是无数须腕状的生物监测单元在解析海流最微小的动向。
港口处时而传来隐隐的钝响，出港或是返航的舰船如同庞大的鳞，优雅地破开万钧海水。
压缩态的物资顺着半空中的光缆进入千家万户，它们流淌时传出细微的嗡鸣。
......
万千声响，繁多而不杂乱，居住在弥利亚留姆的十余万军民，早已熟悉这座孤城的声音。
但所有人都在此刻停了下来，怀疑起自己的耳朵。
[dialog]
[StopSound(channel="u", fadetime=2)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.3, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.3, fadetime=0.1)]
[PlayMusic(intro="$m_bat_act17side_03_intro", key="$m_bat_act17side_03_loop", volume=0.6)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Background(image="51_g1_beaconsquare", y=60, xScale=1.3, yScale=1.3, screenadapt="coverall")]
[backgroundTween(xFrom = 170, xTo = -170, duration=30, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
起初，仿佛只是一缕风掠过礁石的夹角。
继而，一只幼小的生命从母胎的温暖中探出脑袋。
紧接着，是一个群体、一个巢穴、一片海域。
[dialog]
[curtain(direction = 0,fillfrom = 0.3,fillto = 0, fadetime=4)]
[curtain(direction = 4,fillfrom = 0.3,fillto = 0, fadetime=4)]
[Background(image="51_g1_beaconsquare", xScale=1.05, yScale=1.05, fadetime=2, screenadapt="coverall")]
[backgroundTween(xScaleFrom = 1.05, xScaleTo = 1, yScaleFrom = 1.05, yScaleTo = 1, duration=10, block=false)]
[delay(time=4)]
[PlaySound(key="$d_avg_ropytissuegrow", volume=1)]
[Background(image="51_g2_beaconsquare_nest", fadetime=4, screenadapt="coverall")]
[delay(time=3)]
......生命集中绽放的异响，清晰可闻。
海的子嗣反哺海洋。
它吻过文明，于是文明变得愈发生机盎然。
[dialog]
[PlaySound(key="$d_avg_emgseaalarm", volume=1)]
[Blocker(a=0.2, r=0.92, g=0.4, b=0.3, fadetime=0.6, block=true)]
[Blocker(a=0, r=0.92, g=0.4, b=0.3, fadetime=0.4, block=true)]
[delay(time=0.4)]
[PlaySound(key="$d_avg_emgseaalarm", volume=1)]
[Blocker(a=0.2, r=0.92, g=0.4, b=0.3, fadetime=0.6, block=true)]
[Blocker(a=0, r=0.92, g=0.4, b=0.3, fadetime=0.4, block=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1392_1#1$1", duration=1, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1392_1#1$1", focus="l")]
[name="紧张的阿戈尔人"]快看！
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="r")]
[name="神秘的阿戈尔人"]——！
[charslot]
那座高耸在城市中央的塔不复存在，取而代之的是某种深海溶洞里才能见到的巨型“石柱”。
绵密而多孔的海嗣组织，湿滑而细腻的海嗣组织，层层叠叠地包裹住了信标塔的外墙。
但仍有照明设备的灯光从深处透出，将周围的一切晕染得诡异又绮丽。
石柱上的菌落簌簌飘落，在广场上展开成造型奇特的生物。
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1392_1#1$1", focus="l")]
[name="紧张的阿戈尔人"]如果不是那几尊雕塑还能看出个大概，我甚至想不到眼前的一切与文明有何关联！
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="r")]
[name="神秘的阿戈尔人"]......“巢穴化”。
[charslot(slot = "l", name = "avg_npc_1392_1#1$1", focus="l")]
[name="紧张的阿戈尔人"]城市里怎么会出现海嗣？我们明明都还没有......
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="r")]
[name="神秘的阿戈尔人"]只要结果符合预期，过程是不是由我们亲手推动，都无所谓。
[name="神秘的阿戈尔人"]但愿这对于正在沉沦的阿戈尔人来说，会是无法忘记的一课。
[charslot(slot = "l", name = "avg_npc_1392_1#1$1", focus="l")]
[name="紧张的阿戈尔人"]我们现在怎么做？
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="r")]
[name="神秘的阿戈尔人"]扩大现有的结果，阻止这座城市进行反击。
[charslot(slot = "r", focus="n")]
[name="？？？"]谋害图利娅还不够，你们还要从内部彻底破坏城市？
[name="？？？"]我本来还指望再观察一会，顺着你们将其他人一网打尽。
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_4137_udflow_1#1$1", duration=1.5, isblock=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4137_udflow_1#1$1")]
[name="西昆妲"]事态紧急，收网。
[name="西昆妲"]你们将是海巡队本月内处理的第三十三、三十四个深海教徒。
[charslot]
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1392_1#1$1", focus="l")]
[name="紧张的阿戈尔人"]海巡队......
[charslot(slot = "r", name = "avg_npc_1394_1#1$1", focus="r")]
[name="神秘的阿戈尔人"]这段时间，你已经伤害了我们太多手足。
[name="神秘的阿戈尔人"]一味地服从既有秩序毫无意义，阿戈尔需要的不是在绝望中苟延残喘——
[dialog]
[charslot(slot = "all", focus="all")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_seagunshoot", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.03, block=true)]
[delay(time=0.1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_seagunshoot", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.03, block=true)]
[delay(time=0.4)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[charslot(slot = "r",  posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5, isblock=true)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[charslot(slot = "l",  posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=0.4)]
[charslot(slot = "m", name = "avg_4137_udflow_1#5$1")]
[name="西昆妲"]啰嗦。没时间和你们辩论。
[charslot(slot = "m", name = "avg_npc_1390_1#1$1")]
[name="海巡队队长"]西昆妲指挥官，生物信号异常密集，在短时间内暴涨了三倍。
[name="海巡队队长"]海嗣似乎已经把那座塔筑成了巢穴，它们正在源源不断地从中生成......
[charslot(slot = "m", name = "avg_4137_udflow_1#6$1")]
[name="西昆妲"]不能让这些海嗣向其他城区扩散！
[charslot(slot = "m", name = "avg_4137_udflow_1#5$1")]
[name="西昆妲"]附近的民众已经在自发疏散，你带领一个小队引导大家向避难仓撤离。
[name="西昆妲"]记得清空路面上的所有辅助机械，如果被海嗣污染，它们会成为对付我们的武器。
[name="西昆妲"]其他人，结成战斗编队，开启屏障，将海嗣限制在信标塔周边的区域！
[charslot(slot = "m", name = "avg_npc_1390_1#1$1")]
[name="海巡队队长"]明白！
[charslot(slot = "m", name = "avg_4137_udflow_1#3$1")]
[name="西昆妲"]第Ⅳ级武器明明已经启动，难道说......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[charslot]
[Background(image="51_g7_consuloffice",screenadapt="coverall")]
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[playsound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1)]
[name="克莱门莎"]......我在听。
[

... (全文26260字符)
```

### level_act34side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$m_avg_opening_intro", volume=0.6)]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1383_1#2$1", duration=1.5, isblock=true)]
[name="“海嗣”"]凯尔希，你已在大地上奔行良久，天空上的剧变，你不会注意不到。
[charslot]
海嗣微微仰起头颅。尽管已经没有眼睛，但它似乎仍在习惯性地仰望。
穹顶之上，无垠的海水之上，仿佛有什么遥远的物事吸引了它的注意。
[charslot(slot = "m", name = "avg_npc_1383_1#2$1")]
[name="“海嗣”"]告诉我，那个被撕开的空洞，还有多久愈合？
[charslot(slot = "m", name = "avg_003_kalts_1#3$1")]
[name="凯尔希"]......原来是这样。
[name="凯尔希"]阿戈尔的判断没有错，海嗣摒弃对海洋的依恋，向陆地大举进发，确实是出于一个明确的目的。
[name="凯尔希"]你们留意到了阻隔层的变化，你们为此而来。
[charslot(slot = "m", name = "avg_npc_1383_1#2$1")]
[name="“海嗣”"]大群在海岸上的眼睛，向我传递它的所见。
[name="“海嗣”"]天空漾起涟漪，万古不变的膜被撕破。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]“生存”的本能驱使着你们捕捉环境里的每一丝变化......以及变化所预示的危险。
[charslot(slot = "m", name = "avg_npc_1383_1#1$1")]
[name="“海嗣”"]危险？是的。
[name="“海嗣”"]果然。凯尔希，你很敏锐，你的程序运行得相当流畅。
[name="“海嗣”"]我们的交流，会十分有效。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]......
[charslot(slot = "m", name = "avg_npc_1383_1#1$1")]
[name="“海嗣”"]高悬泰拉之上的灾厄，凝视着我们的眼睛，是否会窥见天空的异常？还是说，它已经......
[name="“海嗣”"]凯尔希，你了解泰拉，也了解它所面临的危机。
[name="“海嗣”"]你能做到，你应当做。帮助大群理解，帮助大群进化。
[dialog]
[charslot]
[Decision(options="凯尔希，我应该没有听错吧？;罗德岛来到这里的目标可是解决你们。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]凯尔希医生，我希望眼下的话题只是这只海嗣的一厢情愿，而不是你们之间的某种共识。
[charslot(slot = "m", name = "avg_003_kalts_1#3$1")]
[name="凯尔希"]执政官阁下，让它说完。
[charslot(slot = "m", name = "avg_npc_1383_1#1$1")]
[name="“海嗣”"]最后的时机，正在消逝。泰拉的海洋，太过狭隘。
[name="“海嗣”"]更多知识，更多养分，更多空间。大群需要加速，大群需要帮助。
[dialog]
[charslot(slot = "m", focus="n")]
[Decision(options="难道你们不仅想要爬上陆地？;难道你们还想要飞上太空？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_npc_1383_1#1$1")]
[name="“海嗣”"]长出翅膀，不难，但远远不够。突破天空，需要族群进行本质性的蜕变。
[name="“海嗣”"]凯尔希，你掌握足够的知识，你帮助大群理解一切，我们摆脱灾厄。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]哪怕来历特殊，海嗣也终归只是被本能驱动的非智慧生物。而深海教会，也不过是在海嗣身上寄予了太多妄想的痴愚之人。
[name="凯尔希"]但你所知晓的，远超这二者所能触及的极限。怎么会？
[charslot(slot = "m", name = "avg_npc_1383_1#1$1")]
[name="“海嗣”"]我们一样，凯尔希。族群与你，拥有同样使命。
[charslot(slot = "m", name = "avg_003_kalts_1#14$1")]
[name="凯尔希"]我应该换一个问题......
[name="凯尔希"]海嗣为什么会演变成如今的模样？你与深蓝之树的失控究竟存在怎样的联系？
[charslot(slot = "m", name = "avg_npc_1383_1#1$1")]
[name="“海嗣”"]对你而言很重要吗，这个答案？
[charslot(slot = "m", name = "avg_npc_1383_1#3$1")]
[name="“海嗣”"]在我身上发生的一切，我可以告诉你。如果这能帮助你理解我的来意。
[charslot(slot = "m", name = "avg_npc_1382_1#10$1")]
[name="克莱门莎"]......一场迟来两百余年的质询。
[charslot(slot = "m", name = "avg_npc_1382_1#11$1")]
[name="克莱门莎"]玛利图斯，那次失败的科考任务，背后的真相是什么？你究竟为什么变成了现在这副模样？
[PlaySound(key="$d_avg_brainnucleiturn", volume=1)]
[charslot(slot = "m", name = "avg_npc_1383_1#5$1")]
[name="“海嗣”"]失败？不。那是最大的成功。
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1383_1#3$1")]
[name="“海嗣”"]我们首次进入了地幔遗迹群的最下层。
[name="“海嗣”"]前人类挖空整片岩层，建造了迷宫般的综合体。改造的痕迹直达下地幔层，我们此前数千年的发掘，依然只停留在它的外围。
[name="“海嗣”"]地幔遗迹群，阿戈尔文明的原点，我们以为它的深处埋藏着更多遗产、更多秘密、更多答案。
[name="“海嗣”"]但我们所期待的，都不存在。埋藏在深处的，只有一个渺小的希望。
[charslot(slot = "m", name = "avg_003_kalts_1#14$1")]
[name="凯尔希"]......说下去。
[charslot(slot = "m", name = "avg_npc_1383_1#3$1")]
[name="“海嗣”"]我的队员们都在路途中走失，只有我，只有我来到了道路的尽头。
[name="“海嗣”"]在那里，我看见......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="51_i07_1", screenadapt="coverall", xScale=1.1, yScale=1.1)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[PlaySound(key="$d_avg_giantseamonster", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="“海嗣”"]巨物。巨物在深蓝的树影中沉眠。
[name="“海嗣”"]没法看清祂的全貌，仅仅一小截触肢，就已经占据我视野的全部——
[name="“海嗣”"]祂的触肢贴在透明的密封舱壁上。祂始终保持那个姿势，或许在等待一次触碰，又或许......
[name="“海嗣”"]反应过来的时候，我已经站在祂的面前，伸出了手。
[name="“海嗣”"]舱壁是冷的，但我能感受到祂的体温。然后，海潮般的景象从四面八方向我涌来，将我淹没。
[name="凯尔希"]一只巨兽向你分享了它的视界。你看到了什么？
[name="“海嗣”"]坠落的城市、低垂的天幕、燃烧的大地、熄灭的星门、破碎的星环、断裂的路网......
[name="凯尔希"]那是......先史文明的覆灭？
[name="“海嗣”"]是。阿戈尔始终没能确证先史文明覆灭的原因，但那一刻，毁灭的景象就在我的眼前复现。
[name="“海嗣”"]但那不是终点。那之后仍有景象源源不断地涌出——远超出我认知边界的景象。
[name="“海嗣”"]永远离散的粒子与再无波澜的沙海......
[name="“海嗣”"]冰冷无光的荒原与永无尽头的黑暗......
[name="“海嗣”"]燃烧崩毁的群星与无限扩张的黑洞......
[name="“海嗣”"]那里不存在任何熟悉的要素，我丧失了知觉，所有知觉。或者说，就连与我分享视界的巨兽，也感知不到祂自己的存在......
[name="“海嗣”"]那是一个完全陌生的所在——没有生命、没有意义、没有信息——
海嗣的话语突然中断了，透过它透明的颅腔，你能看见那些色泽诡异的核状物聚拢又散开。
[PlaySound(key="$d_avg_brainnucleiturn", volume=1)]
它似乎在思考，那些核的运动轨迹便是它思考的过程。
[name="“海嗣”"]凯尔希，你一定能理解那些景象的含义。
[name="凯尔希"]......那些景象所代表的危机曾摧毁一切，它无法被具象化，现存的语言中没有任何一个词足以描绘它。
[name="“海嗣”"]那是先史文明的结局，也是泰拉将要面临的灾厄——那是一切事物的终点。
[name="“海嗣”"]我松开手，那些可怖的景象离我而去，取而代之的是另一番景象，破碎，模糊，混沌。
[name="“海嗣”"]祂与祂的子嗣将生灵悉数吞噬，将星月悉数分解。生者与死者皆成为祂的养分，祂在时间尽头的黑暗中呢喃——
[name="“海嗣”"]“存续”。
[name="“海嗣”"]一遍一遍，唯有存续。
[name="凯尔希"]“混沌”“呢喃”......那只巨兽并不清醒？
[name="“海嗣”"]祂深陷梦境之中。梦境停滞，蜕变停滞，使命停滞——祂被困在那深蓝洞穴。
[name="“海嗣”"]所以，我必须将祂唤醒。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[image]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Background(image="51_g2_beaconsquare_nest",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1387_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_dripink", volume=0.2)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_mechafault", volume=0.6)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1)]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1386_1#4$1", posfrom = "-200,0", posto = "0,0", duration=0.5, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1386_1#4$1", focus="l")]
[name="阿

... (全文44921字符)
```

### level_act34side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_erthshkng", volume=1, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=6)]
[PlaySound(key="$d_avg_rockfall", volume=0.6)]
[PlaySound(key="$d_avg_deepseaamb", volume=0.4, loop=true, channel="en")]
[StopSound(channel="e", fadetime=10)]
[Background(image="51_g4_aegirstreet_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1387_1#7$1", duration=1.5, isblock=true)]
[name="卡西娅"]咳咳——
[name="卡西娅"]还好，差点被那家伙追上......
[charslot(slot = "r", focus="n")]
[name="？？？"]卡、卡西娅，我一直在找你，你怎么消失了这么久？
[charslot(slot = "r", name = "avg_npc_1387_1#5$1", focus="r")]
[name="卡西娅"]......卢契拉？
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_4079_haini_1#1$1", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1387_1#8$1", focus="r")]
[name="卡西娅"]你这孩子，傻站在这里干嘛？
[charslot(slot = "l", name = "avg_4079_haini_1#9$1", focus="l")]
[name="卢契拉"]城市单元骨架需要检修，这也是战斗的一部分。信标塔的方向......城市里究竟发生了什么？
[charslot(slot = "r", name = "avg_npc_1387_1#8$1", focus="r")]
[name="卡西娅"]海嗣侵入了弥利亚留姆，那座塔已经变成了巢穴。
[name="卡西娅"]这里交给我吧，你赶紧去避险。
[charslot(slot = "l", name = "avg_4079_haini_1#2$1", focus="l")]
[name="卢契拉"]太危险了......我留下来，我和你一起。
[charslot(slot = "r", name = "avg_npc_1387_1#2$1", focus="r")]
[name="卡西娅"]不用，呼——
[charslot(slot = "l", name = "avg_4079_haini_1#5$1", focus="l")]
[name="卢契拉"]卡西娅，你受伤了？！
[charslot(slot = "r", name = "avg_npc_1387_1#7$1", focus="r")]
[name="卡西娅"]嗯。
[charslot(slot = "l", name = "avg_4079_haini_1#7$1", focus="l")]
[multiline(name="卢契拉")]你赶过来的时候，被那些海嗣——
[charslot(slot = "l", name = "avg_4079_haini_1#6$1", focus="l")]
[multiline(name="卢契拉",end=true)]不对，这种擦伤不可能是海嗣造成的......
[name="卢契拉"]有人攻击了你？
[charslot(slot = "r", name = "avg_npc_1387_1#2$1", focus="r")]
[charslot(slot = "r", action="shake", afrom=1 , focus="r", ato=1, power=3, times=30, duration=0.3)]
[name="卡西娅"]咳咳！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", posfrom="0,0", posto="100,0", duration=1.5, afrom=1, ato=0, isblock=true)]
[delay(time=0.5)]
[charslot]
[PlaySound(key="$d_avg_metaldoorclose", volume=1)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_4079_haini_1#5$1")]
[name="卢契拉"]等等，你把安全阀拉出来做什么？
[dialog]
[charslot(slot = "m", posfrom="0,0", posto="100,0", duration=0.5, afrom=1, ato=1, isblock=true)]
[name="卢契拉"]欸欸，别往前推，这样会切断底层的自检系统，这里的城市单元骨架会停止运作的......
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[name="卢契拉"]不对，你当然比我清楚......
[dialog]
[SoundVolume(volume=0.2, channel="en",fadetime=2)]
[PlayMusic(key="$wasteland_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1.5)]
[charslot(slot = "m", posfrom="100,0", posto="0,0", duration=1.5, afrom=1, ato=1, isblock=true)]
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[name="卢契拉"]卡西娅，这才是你的目的吗？你是，你是深海教会的人？
[name="卢契拉"]......
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[multiline(name="卢契拉")]所以你才在海巡队调查图利娅的时候，故意引导她们去怀疑她？难道说，她的失踪，就是你......
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[multiline(name="卢契拉",end=true)]你在我脖子上放了什么？
[charslot(slot = "m", name = "avg_npc_1387_1#1$1")]
[name="卡西娅"]长须栉齿草，一个负责培育行道珊瑚的朋友的作品。别乱动，如果被它的触须扎破皮肤，会很痛苦地死去。
[name="卡西娅"]现在，孩子，咳......离开这里。等你走得足够远，它会自动脱落。
[dialog]
[charslot(slot = "m", name = "avg_npc_1387_1#7$1")]
[delay(time=1)]
[name="卡西娅"]你想走的，对吗？
[name="卡西娅"]其实在我们成为同僚之前，我就在发展规划所偶然看过你的评估资料。
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[name="卢契拉"]......
[charslot(slot = "m", name = "avg_npc_1387_1#7$1")]
[name="卡西娅"]你之所以在意那个数据员，是因为自己始终没有忘记弥利亚留姆的那次撤离，对吧？
[name="卡西娅"]眼看着远处的火山能源站的光亮一点点熄灭，周围只剩下无尽的黑暗，黑暗中只剩下海流的轰鸣和窸窣的异响......
[name="卡西娅"]那才是海洋原本的模样。
[charslot(slot = "m", name = "avg_npc_1387_1#2$1")]
[name="卡西娅"]那一刻，你是整个弥利亚留姆离海洋最近的人，你站在穹顶的夹层，周围一个人都没有。
[name="卡西娅"]发展规划所评估你的心理压力过大，才同意你从穹顶系统转来地面。至于“恐高”，只是个无伤大雅的玩笑。
[charslot(slot = "m", name = "avg_npc_1387_1#7$1")]
[name="卡西娅"]恐怕连你自己都没有意识到，自己的内心深处藏着怎样的......
[charslot(slot = "m", name = "avg_4079_haini_1#10$1")]
[name="卢契拉"]......
[charslot(slot = "m", name = "avg_npc_1387_1#1$1")]
[name="卡西娅"]剩余的海嗣很快就会发现这条路还能通过，你不会想再次面对它们的。
[name="卡西娅"]快走吧，还来得及。
[charslot(slot = "m", name = "avg_4079_haini_1#10$1")]
[name="卢契拉"]......
[dialog]
[charslot]
[PlaySound(key="$d_avg_gatecloz", volume=1)]
卡西娅握住了安全阀，继续向前推着，她没有再看旁边这个总是爱开玩笑的后辈。
安全阀突然停住，发出刺耳的锐响，卡西娅没能再推动一丝一毫——
一双纤细的手抵住了另一端。
[charslot(slot = "m", name = "avg_npc_1387_1#6$1")]
[name="卡西娅"]卢契拉？
[charslot(slot = "m", name = "avg_4079_haini_1#2$1")]
[name="卢契拉"]哈，要是在平时，我一定会很生气地反驳你，或者把这株什么草塞进我的墨水瓶里，跟你说这种恶作剧的水平太低。
[charslot(slot = "m", name = "avg_4079_haini_1#4$1")]
[name="卢契拉"]可是，好亮啊......信标塔沉下去的方向，还有我们头顶的穹顶，整块大陆架上的海嗣都在朝弥利亚留姆涌过来，对吧？
[name="卢契拉"]这些色彩诡异的光亮背后是什么？
[name="卢契拉"]卡西娅，你说的没错，海嗣在侵蚀我们的生活，我已经真真切切经历过一次了，我没法忘记。
[name="卢契拉"]我很羡慕图利娅，我们经历了类似的事情，可是从始至终，她都能守着自己珍视的东西，她很厉害！
[charslot(slot = "m", name = "avg_4079_haini_1#3$1")]
[name="卢契拉"]而我却从穹顶逃到了地面，刚刚你来之前，我也真的想过从这里逃开......
[name="卢契拉"]可是我应该去哪里呢？
[charslot(slot = "m", name = "avg_4079_haini_1#6$1")]
[name="卢契拉"]卡西娅，我不能让你破坏城市单元骨架，我不能让海嗣涌进弥利亚留姆的其他城市单元，哪怕这株草真的能要了我的命！
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[name="卢契拉"]因为，因为我的身后已经没有路了。
[charslot(slot = "r", action="shake", afrom=1 , ato=1, power=3, times=30, duration=0.3)]
[charslot(slot = "m", name = "avg_npc_1387_1#2$1")]
[name="卡西娅"]咳咳......
[charslot(slot = "m", name = "avg_npc_1387_1#7$1")]
[name="卡西娅"]你这孩子，力气还真大......
[charslot(slot = "m", name = "avg_4079_haini_1#1$1")]
[name="卢契拉"]劳伦缇娜小姐的父母让我知道，穹顶可以很漂亮，可这块透明的结构，实际上是阿戈尔城市的眼睛。
[charslot(slot = "m", name = "avg_4079_haini_1#9$1")]
[name="卢契拉"]其实，我最近一直在问我自己......我们身处在一场战争里，眼睛就应该负责注视危险，不是吗？

... (全文32471字符)
```

### level_act34side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Background(image="51_g6_aegirarena",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1390_1#1$1", posfrom="200,0", posto="0,0", duration=0.5, isblock=true)]
[name="海巡队队长"]克莱门莎执政官，您在这里。
[name="海巡队队长"]我们在斗智场发现了极为特殊的生物信号，好在您没有遇到危险。
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]前线的情况如何？
[charslot(slot = "m", name = "avg_npc_1390_1#1$1")]
[name="海巡队队长"]按照您的部署，第八、第十军团以及海巡队轮流出港护航。
[name="海巡队队长"]城市单元骨架已经重组完成，人造力场完全展开，弥利亚留姆正在对抗海嗣潮。
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]知会城市内的所有相关科研人员，我需要知道这片海域在接下来每一分钟里的变化。
[name="克莱门莎"]哪怕已经启动了应急预案，我们依然太过被动。
[charslot(slot = "m", name = "avg_npc_1390_1#1$1")]
[name="海巡队队长"]您......可能需要确认一下无人机矩阵刚刚传回的画面。
[dialog]
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[PlaySound(key="$d_avg_bionicuavs_tech", volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1382_1#3$1")]
[name="克莱门莎"]嗯？
[name="克莱门莎"]这些在海嗣间蔓延的、发光的通路......
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]“航道”？
[dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "m", name = "avg_npc_1396_1#1$1", duration=1, isblock=true)]
[delay(time=0.5)]
[name="阿戈尔技术员"]克莱门莎执政官，我们与本境的通讯已经恢复！刚刚收到一则本境的通讯，来自科学发展规划所。
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]......
[name="克莱门莎"]猎人们有消息了吗？
[charslot(slot = "m", name = "avg_npc_1390_1#1$1")]
[name="海巡队队长"]三位深海猎人已经回到弥利亚留姆，她们正在东侧的城市单元清剿残留的海嗣。
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]联系歌蕾蒂娅，请她立刻来找我们。
[charslot(slot = "m", name = "avg_npc_1390_1#1$1")]
[name="海巡队队长"]是。
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]凯尔希，博士，我们走吧。
[name="克莱门莎"]二位需要与阿戈尔有更进一步的接触。
[dialog]
[charslot]
[Decision(options="让我和这位长官一起去通知猎人吧。;如果是外交场合，凯尔希去就好了。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_003_kalts_1#3$1")]
[name="凯尔希"]（低语）博士？
[dialog]
[charslot(slot = "m", focus="n")]
[Decision(options="（低语）那只海嗣离开的方向，也是东侧......;（低语）那只海嗣可能会遇上斯卡蒂......", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot = "m", name = "avg_003_kalts_1#3$1")]
你与凯尔希短暂交换了眼神。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]执政官阁下，博士还有一些事情需要解决。
[charslot(slot = "m", name = "avg_npc_1382_1#2$1")]
[name="克莱门莎"]......好。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g7_consuloffice",screenadapt="coverall")]
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_474_gladiia_1#5", duration=1.5, isblock=true)]
[name="歌蕾蒂娅"]航道计划的最终作战以弥利亚留姆被海嗣入侵收场。克莱门莎执政官，我需要你的解释。
[charslot(slot = "m", name = "avg_003_kalts_1#1$1")]
[name="凯尔希"]歌蕾蒂娅。
[name="凯尔希"]你们还好吗？
[charslot(slot = "m", name = "avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]凯尔希，你也在。
[name="歌蕾蒂娅"]猎人们遭遇了一些意外，但没有大碍。
[name="歌蕾蒂娅"]我想，作为伊比利亚的使节，凯尔希医生或许也需要一个解释。
[charslot(slot = "m", name = "avg_npc_1382_1#4$1")]
[name="克莱门莎"]或许同样希望得到解答的，还有我。
[charslot(slot = "m", name = "avg_npc_1382_1#9$1")]
[name="克莱门莎"]有人想见你们。
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[charslot(slot = "m", name = "avg_npc_1401_1#1$1", duration=1, isblock=true)]
[name="“小帮手”"]——
[dialog]
[PlaySound(key="$d_avg_microrobot", volume=1)]
[charslot(slot = "m", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=2, isblock=true)]
[PlaySound(key="$d_avg_holographicholyamb", volume=0, loop=true, channel="h")]
[SoundVolume(volume=1, channel="h",fadetime=2)]
小帮手移动到冥思间中央，投影模块发出冷色的光，光的粒子在空气中舞蹈，一点点描绘出一个阿戈尔人的身形。
那是一位面带笑意的金发女性，她注视着在场的所有人，仿佛已经等待了，或者观察了许久。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[Image(image="51_i12", screenadapt="coverall")]
[Delay(time=1)]
[StopSound(channel="h", fadetime=6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
[name="歌蕾蒂娅"]......赫拉提娅执政官。
[name="赫拉提娅"]你看起来为什么这么疲惫，我的小歌蕾蒂娅？
[name="赫拉提娅"]虽然“航道”的信息传输效率高得超乎我的预想，但拟像技术终归无法真实地传达我的感受。
[name="赫拉提娅"]否则，我应该好好地拥抱你，摸摸你的头发。
[name="歌蕾蒂娅"]不必了，你应该知道这很危险。
[name="歌蕾蒂娅"]此时此刻海面上的异变，那些突然生成的“航道”，是你的手笔？
[name="赫拉提娅"]阿戈尔，海嗣，我们双方都在争抢时间。
[name="赫拉提娅"]为了尽快将整块大陆架筑成巢穴，海嗣不得不向它们侵占的每一片海域源源不断地输送养分。
[name="赫拉提娅"]任何事情都有两面，一场灾难，也为我们带来了难以计量的生物能源。
[name="赫拉提娅"]两百多年前，信标发射井需要一套由十余座城市协力维持的生物供能系统，才能持续地孵化出组成航道的微型浮游机械。
[name="赫拉提娅"]而如今，这些微型浮游机械由海嗣哺育，也被它们视作无害的同胞。
[name="赫拉提娅"]依托浮游机械之间的信息流，压缩态的舰队与城市集群将能在转瞬间跨越大洋。
[name="赫拉提娅"]虽然，这些浮游机械没能像前人设想中那般，将阿戈尔推向星际文明的高度......但它们足以在危急存亡的关头为人类文明开辟一条生路。
[name="歌蕾蒂娅"]但这也意味着未来很长一段时间里，阿戈尔不得不与海嗣“共生”，利用那些杂碎的活动，也被它们利用。
[name="歌蕾蒂娅"]......这又是你所谓的博弈？
[name="赫拉提娅"]这是我们突破重围的手段。
[name="赫拉提娅"]“航道”，阿戈尔所行之路，从来都不只狭隘地指代一方纯净的水域。
[name="赫拉提娅"]你从一开始便展露出了对航道计划的怀疑，这很好。但如果怀疑只是让你自乱阵脚，那它就毫无裨益。
[name="赫拉提娅"]既然阿戈尔决心要打开一条联通陆地与海洋的航道，那阿戈尔便一定能做到。
[name="凯尔希"]阿戈尔成事的能力毋庸置疑，但阿戈尔行事的手段或许还有待商榷。
[name="赫拉提娅"]想必您就是凯尔希医生。科学发展规划所的执政官赫拉提娅，向您致意。
[name="赫拉提娅"]我很高兴看到陆地上依然有您这样的人在沿承先史文明的意志，这意味着阿戈尔并不是独行者。
[name="赫拉提娅"]我也很高兴看到，您能以如此强势的姿态展开对话。
[name="赫拉提娅"]这是否意味着，您有能力代表陆地文明发言，为我们省去与陆上诸国一一建交的时间？
[name="凯尔希"]能看到阿戈尔放下偏安一隅的想法，主动提出与陆地合作，我同样倍感欣喜。
[name="凯尔希"]但很遗憾，执政官阁下，我无法代表陆地文明，我只是比许多人更了解它。
[name="凯尔希"]不过我想，阿戈尔此刻需要的，正是对陆地文明的深入了解。
[name="凯尔希"]您与我都清楚，眼前的这条航道，并非仅仅为了对抗海嗣......阿戈尔看向了这片大地上一切非自然的存在。
[name="赫拉提娅"]唯有如此，我们才能探明泰拉的本质，从源头上消除那悬在我们头顶的灾厄。
[name="凯尔希"]那么您理应意识到，对陆上诸国而言，这样的举动意味着什么。
[name="凯尔希"]相比海嗣，你们才是更加直接的威胁。
[name="赫拉提娅"]我们对陆上诸国没有恶意，我们不必有恶意。
[name="赫拉提娅"]我们能做出的最残忍的事情，不过是在解决危机的路上，不再理会其他步履蹒跚的文明。
[dialog]
[StopSound(channel="h", fadetime=1)]
[Blocker(a=0, r=0, g=0

... (全文32018字符)
```

### level_act34side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g18_lighthouse_square",screenadapt="coverall")]
[playsound(key="$d_avg_sea", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.7, channel="bgs",fadetime=3)]
[Delay(time=3)]
[Subtitle(text="一个猎人他走上海岸♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他的家乡在后，他的路在身前♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="父母与儿女都与他失散♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他的恋人已经葬身大海♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=1)]
[Subtitle(text="一个猎人他走上海岸♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他的家乡在后，徒余哀叹♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他的路没有尽头♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他的路浓雾弥漫♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=1)]
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=3, block=true)]
[Subtitle(text="一个猎人他回到海岸♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他的旅程结束，他的家乡近在眼前♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="旧日的涛声呢喃♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可他为什么却步♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="又为什么不安♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Delay(time=3)]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[Decision(options="好久不见，斯卡蒂。;你好啊，斯卡蒂。", values="1;2")]
[Predicate(references="1;2")]
[Delay(time=1)]
[charslot(slot="m",name="char_263_skadi#3",duration=1.5)]
[delay(time=2)]
[name="斯卡蒂"]好久不见，博士。
[name="斯卡蒂"]按照约定，来接你的应该是那个脸皮很厚话又多的黎博利，但你好像并不惊讶。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="你和极境都是罗德岛的干员。;毕竟这里更靠近你的故乡。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]嗯，也是。
[name="斯卡蒂"]你比凯尔希估计的晚到了快一个小时。
[charslot(slot="m",name="char_263_skadi#3")]
[name="斯卡蒂"]看来就算有圣徒开具的公函，审判庭该有的审查程序还是一样没落。
[name="斯卡蒂"]才不到三个月，除了能派上用场的工人外，这里的居民全都迁去了内陆城镇，取而代之的是几个大阵的惩戒军。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="他们在紧锣密鼓地筹备着什么。;他们看起来非常紧张。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="char_263_skadi#9")]
[name="斯卡蒂"]自从一周前，伊比利亚收到了来自阿戈尔的联络，这座被遗忘的小镇就不再安静了。
[name="斯卡蒂"]遍地的海洋残渣刺激着这些年轻战士的神经，阿戈尔的声音只会加重他们的焦虑。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="阿戈尔的行动确实值得关注甚至戒备。;远海中的国家突然发声，没人能充耳不闻。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="char_263_skadi#3")]
[name="斯卡蒂"]沿着雕塑左侧的这条街道过去，走得快一点，十分钟就能看到大海。
[name="斯卡蒂"]我们待会儿直接前往伊比利亚之眼。
[Dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_sea", volume=0.7, loop=true, channel="sea")]
[delay(time=2.5)]
[charslot(slot="m",name="char_263_skadi#3")]
[name="斯卡蒂"]喂，博士，你听见海浪了吗？
[charslot(slot = "m", focus = "n")]
斯卡蒂微微侧过了头，迎向海风吹来的方向，她的长发在风中舞动，与眼中的阴翳同色。
[charslot(slot="m",name="char_263_skadi#4")]
[name="斯卡蒂"]浪的层次变得很复杂，我还听见了——星空流动的声音，永不停歇的自然的歌，还有，不被理解的语言......
[StopSound(channel="sea", fadetime=3)]
[Dialog]
[stopmusic(fadetime=2)]
[charslot(duration=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2.5, block=true)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Sticker(id="st1", text="Ishar-mla。", x=320,y=340, alignment="center", size=22, delay=0.001, width=700,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[delay(time=1.1)]
[Sticker(id="st1", text="我在。", x=320,y=340, alignment="center", size=22, delay=0.001, width=700,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[delay(time=1.1)]
[Sticker(id="st1", text="我们遭受的苦永在。", x=320,y=340, alignment="center", size=22, delay=0.001, width=700,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[delay(time=1.1)]
[Sticker(id="st1", text="我们渴望的生永在。", x=320,y=340, alignment="center", size=22, delay=0.001, width=700,duration=1)]
[Sticker(id="st1",duration=1,block = false)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="char_263_skadi#7")]
[name="斯卡蒂"]......
[Dialog]
[charslot(slot = "m", focus = "n")]
[playMusic(intro="$tech_intro",key="$tech_loop", volume=0.6)]
[Decision(options="斯卡蒂，你还好吗？;和家乡恢复联系，反而让你心神不宁？", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="char_263_skadi#3")]
[name="斯卡蒂"]近乡情怯吧......算了，这种感受很难总结。
[name="斯卡蒂"]也可能只是没睡好觉，上次回了一趟海里，好像鲨鱼把她的梦都转移给我了一样。
[name="斯卡蒂"]说起来，凯尔希医生为什么这么着急地叫你过来？
[name="斯卡蒂"]我不记得你接触过海洋，博士。
[Dialog]
[charslot(slot = "m", focus = "n")]
[Decision(options="不一定，但我记不清了。;但似乎，并不陌生。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="char_263_skadi#3")]
[name="斯卡蒂"]这个回答很模糊。
[name="斯卡蒂"]好吧，我忘了你的情况。这个回答其实很正常。
[charslot(slot="m",name="char_263_skadi#5")]
[name="斯卡蒂"]算了，凯尔希医生把你叫过来，总有她的原因。
[name="斯卡蒂"]走吧，天快要黑下来了。
[Dialog]
[charslot(duration=1)]
[playsound(key="$d_gen_walk_n")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_jump_water", volume=1)]
[charslot(slot = "left", name = "avg_474_gladiia_1#1",posfrom = "0,-100", posto = "0,0",duration = 1)]
[delay(time=0.5)]
[Effect(name="$e_shuihua",layer = 1,y=-350)]
[CameraShake(duration=0.5, xstrength=5, ystrength=10, vibrato=15, randomness=70, fadeout=true, block=false)]
[charslot(slot = "right", name = "avg_1023_ghost2_1#1$1",posfrom = "0,-100", posto = "0,0",duration 

... (全文20517字符)
```

### level_act34side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="51_g3_beaconctrlroom",screenadapt="coverall")]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_4145_Ulpia_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1.5)]
[charslot]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1)]
[charslot(slot = "m", name = "avg_npc_1380_1#1$1", posfrom="-200,0", posto="0,0", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]乌尔......比安阁下？
[charslot(slot = "m", name = "avg_4145_Ulpia_1#7$1")]
[name="乌尔比安"]你？
[charslot(slot = "m", name = "avg_npc_1380_1#6$1")]
[name="乔迪"]呼，看来我没有认错。
[name="乔迪"]我们见过的，在格兰法洛，还是您找上的我......虽然我来到这里后才知道您叫什么。
[name="乔迪"]您不能闯入这里，这里是......
[charslot(slot = "m", name = "avg_4145_Ulpia_1#7$1")]
[name="乌尔比安"]信标塔核心中控室。
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]地上的这个人，您把他？
[charslot(slot = "m", name = "avg_4145_Ulpia_1#4$1")]
[name="乌尔比安"]一个堕落者最应有的下场。
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]他做了什么？
[charslot(slot = "m", name = "avg_4145_Ulpia_1#7$1")]
[name="乌尔比安"]这和你无关，年轻人。为了你自己的人身安全，离开这里。
[dialog]
[charslot(slot = "m", name = "avg_4145_Ulpia_1#4$1")]
[delay(time=0.6)]
[PlaySound(key="$d_avg_scan", volume=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_4145_Ulpia_1#4$1")]
[name="乌尔比安"]所有的巢穴信标都已经激活，被篡改的武器也已经激发，还能如何提醒猎人们......
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]劳伦缇娜小姐她们有危险？
[name="乔迪"]是地上这个人做的，所以您才......
[charslot(slot = "m", name = "avg_4145_Ulpia_1#4$1")]
[name="乌尔比安"]......
[charslot(slot = "m", name = "avg_npc_1380_1#6$1")]
[name="乔迪"]您沉默了。您不相信我......其实我也不相信您。毕竟您总是这么突然出现，而且眼前这个情况，更值得怀疑的是您。
[name="乔迪"]但劳伦缇娜小姐她们是我的朋友。您也是猎人，你们之间的故事，我大概知道一点。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#2$1")]
[name="乌尔比安"]她们在出发前被动了手脚。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#3$1")]
[name="乌尔比安"]此刻，她们仍在海嗣潮中。我不确定具体会发生什么，但危险只大不小。
[charslot(slot = "m", name = "avg_npc_1380_1#6$1")]
[name="乔迪"]如果她们是去投放信标，而且还在巢穴的话，或许我们可以通过这座塔向信标发送讯号，来提醒她们。
[name="乔迪"]我之前就在这里帮忙，大概的操作原理也懂一点。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#1$1")]
[name="乌尔比安"]......去做。
[charslot(slot = "m", name = "avg_npc_1380_1#8$1")]
[name="乔迪"]好、好的。
[dialog]
[PlaySound(key="$d_avg_typewriter", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.2, channel="a",fadetime=2)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]怎么样？
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]虽然实际上要复杂很多，但信标塔的运行框架看起来和大灯塔的主控系统确实很像。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]据我所知，布雷奥甘曾经途经这座城市，为这座塔的工程重构提供过帮助。
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]技术员先生说过，信标全部激活后，信标塔会自主为武器提供导航，其他的相关操作在程序上都是被禁止的。
[name="乔迪"]如果要向其中的一个信标发送讯号——我看看......
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1380_1#8$1")]
[name="乔迪"]确实无法继续操作了。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]你有办法绕开封锁程序吗？
[charslot(slot = "m", name = "avg_npc_1380_1#8$1")]
[name="乔迪"]布雷奥甘先生参与过这座塔的工程重构......那么或许，只是或许，我有一个很笨的方法。
[name="乔迪"]在弥利亚留姆的这段时间，我一直在试图了解那位布雷奥甘。
[name="乔迪"]他是个习惯记录的人，总在记录自己的思考，记录自己的怀疑，哪怕到了陆地上，这个习惯也没有改过。
[charslot(slot = "m", name = "avg_npc_1380_1#6$1")]
[name="乔迪"]记录是为了防止遗忘？我想，我可以试着暂时关闭主控面板上的数据解算系统，像这样——
[dialog]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[PlaySound(key="$d_avg_dripink", volume=0.4)]
[PlaySound(key="$d_avg_scan", volume=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]乌尔比安阁下，当时您向我提起过......我的身世......
[name="乔迪"]您说我是布雷奥甘的后裔，可只要看过他影像的人，都能看出来我和那位天才设计师没有一丁点相似的地方。
[charslot(slot = "m", name = "avg_npc_1380_1#10$1")]
[name="乔迪"]我的父母只是“土生土长”的阿戈尔人。在伊比利亚，在其他陆上国家，有很多这样的阿戈尔人，严格意义上，我们并不属于......
[charslot(slot = "m", name = "avg_4145_Ulpia_1#7$1")]
[name="乌尔比安"]那又如何？
[charslot(slot = "m", name = "avg_npc_1380_1#2$1")]
[name="乔迪"]我、我曾经为此困惑过，但这段时间，我在慢慢学会让自己释怀，不去想这么多。
[name="乔迪"]只是，您是第一个向我提起这件事的人，我还是想跟您确认，您为什么认为我......
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]的确，我猜错了，但我从不做毫无根据的猜测。
[name="乌尔比安"]你们之间并非毫无渊源。
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]渊源？
[charslot(slot = "m", name = "avg_4145_Ulpia_1#4$1")]
[name="乌尔比安"]大静谧摧毁了伊比利亚。海岸上的明灯陷入沉默，怀疑与猜忌随之开始喧嚣。
[name="乌尔比安"]布雷奥甘不得不逃离自己亲手设计的辉煌。逃亡期间，他也曾在格兰法洛藏身，你父母留下的那些研究笔记毫无疑问与他有关。
[name="乌尔比安"]他们是布雷奥甘认定值得托付自己心血的人。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]看看你此刻在做的事情，年轻人，或许你并非布雷奥甘的后裔，但你无疑继承了他的某些智慧。
[charslot(slot = "m", name = "avg_npc_1380_1#2$1")]
[name="乔迪"]我......
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]弥利亚留姆，是你来到的第一座阿戈尔城市，而它恰巧是布雷奥甘离开阿戈尔前的最后一站。
[name="乌尔比安"]他沿着绵延的海床一路游历，他尝试向各地卓有声望的人物分享自己对陆地的推论，对未来泰拉局势的猜想。
[name="乌尔比安"]他希望有人能够与他共同前往陆地，为将来海洋与陆地能够共抗危机寻找可能性。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#2$1")]
[name="乌尔比安"]很多人都欣赏他的才华，但或许是因为他的提议过于超前，最终回应他邀请的人寥寥无几。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]来到弥利亚留姆的时候，他主动参与了这座信标塔的工程重构，以此换取了与当时的执政官沟通的机会。
[charslot(slot = "m", name = "avg_npc_1380_1#5$1")]
[name="乔迪"]那这一次？
[charslot(slot = "m", name = "avg_4145_Ulpia_1#4$1")]
[name="乌尔比安"]毫无疑问，遭到了拒绝。
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]但在工程重构完成之时，他毅然决定结束自己漫长的游历，正式前往那遥远的土地......
[name="乌尔比安"]尽管这一路以来，他几乎没有收获任何的支持。
[charslot(slot = "m", name = "avg_npc_1380_1#1$1")]
[name="乔迪"]......
[charslot(slot = "m", name = "avg_4145_Ulpia_1#8$1")]
[name="乌尔比安"]再想想你过去做的事情，你离开了自己熟悉的小镇，来到素未谋面的所谓家乡，这同样需要莫大的勇气。
[name

... (全文22448字符)
```

### level_act34side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.2, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.2, fadetime=0.1)]
[gridbg(imagegroup="47_g14_skyovercast_L1/47_g14_skyovercast_R1/47_g14_skyovercast_L2/47_g14_skyovercast_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720", x=-640, xScale=0.5, yScale=0.5)]
[largebgtween(duration = 30, yFrom = 510, yTo = 220, block = false)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=4, block=true)]
[name="温柔的男声"]你真的要回去吗？
[name="冷酷的女声"]我好不容易打探到了那个人的下落。
[name="冷酷的女声"]无论他是谁，无论他藏在那座泥潭的哪一处，他伤害了我们的女儿，就必须为此付出代价。
[name="温柔的男声"]那我和你同去。无论挡在前面的是家族，残酷的天灾，无尽的海潮，还是天穹上落下的火雨，我们共同面对。
[name="冷酷的女声"]神社离得开你吗？
[name="冷酷的女声"]放心，杀几个人而已，那些家伙早该去往生了。
[name="温柔的男声"]又到了离别的时刻了......
[name="温柔的男声"]天也醉樱花，云脚乱蹒跚~
[name="冷酷的女声"]这是你新读到的俳句？节奏感很好，很适合挥刀的时候念......
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[gridbg]
[curtain]
[Background(image="33_g11_mansionhall", screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(key="$comedy_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_699_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_698_1#1$1", duration=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_699_1#1$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_698_1#1$1", focus="n")]
[name="家族成员A"]（抽鼻子）
[charslot(slot = "l", name = "avg_npc_698_1#1$1", focus="l")]
[name="家族成员B"]我看得一头雾水，你哭什么？
[charslot(slot = "r", name = "avg_npc_699_1#1$1", focus="r")]
[name="家族成员A"]一个杀手，当年为了给自己的女儿报仇，同时得罪了两大家族，被迫远走。
[name="家族成员A"]多年以后她告别自己温柔的丈夫，再次将自己放在旋涡的最中心，还是为了女儿。
[name="家族成员A"]一想到这个角色还是有人物原型的，我就忍不住......依我看，这部电影就应该以她的视角来拍！
[charslot(slot = "l", name = "avg_npc_698_1#1$1", focus="l")]
[name="家族成员B"]......
[name="家族成员B"]我希望你不要忘了一件事，这部电影是家族递给那座新城市的名片，你和我是代表家族审片。
[name="家族成员B"]我们关注的重点，应该是家主，还有咱们的生意在电影里到底被表现成了什么样子......
[charslot(slot = "r", name = "avg_npc_699_1#1$1", focus="r")]
[name="家族成员A"]你上次不是还说挺好的？
[charslot(slot = "l", name = "avg_npc_698_1#1$1", focus="l")]
[name="家族成员B"]挺好？这个女杀手为什么出现在这里？
[name="家族成员B"]还有什么“残酷的天灾”“无尽的海潮”“天穹上落下的火雨”，台词谁写的？
[name="家族成员B"]哥伦比亚人是在天上捅了个窟窿，可下火雨是哪儿的事，几月几号的，我怎么不知道？
[charslot(slot = "r", name = "avg_npc_699_1#1$1", focus="r")]
[name="家族成员A"]你什么时候能有点大局观？
[name="家族成员A"]一个冷血杀手，最后在咱们的感化下，在新沃尔西尼为了一个和平的未来放下屠刀......没有比这更顺应现在的潮流的了。
[charslot(slot = "l", name = "avg_npc_698_1#1$1", focus="l")]
[name="家族成员B"]呃，叫你这么一说，我觉得这电影更烂了。但你说得对，只要能对得上那位女士的胃口......
[dialog]
[charslot]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_spotlightc", volume=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_signlntrfrnc", volume=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=0.1)]
[PlaySound(key="$d_avg_oldtvelectricity", volume=1, loop=true, channel="o")]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", name = "avg_npc_698_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_699_1#1$1", focus="n")]
[name="家族成员B"]有混蛋动了开关？突袭？！
[charslot(slot = "r", name = "avg_npc_699_1#1$1", focus="r")]
[name="家族成员A"]不，你快看屏幕！
[dialog]
[StopSound(channel="o", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g1_rhinemeetingroom",screenadapt="coverall")]
[PlaySound(key="$d_avg_telephonering", volume=1, loop=true, channel="t")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_891_1#7$1", posfrom="200,0", posto="0,0", duration=1, isblock=true)]
[delay(time=0.5)]
[name="娜斯提"]......
[dialog]
[StopSound(channel="t", fadetime=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_telephone", volume=1)]
[delay(time=0.5)]
[PlayMusic(key="$formal_loop", volume=0.6)]
[interlude(maskid = "group_interclude_vertical_common" ,size = "290,760",tsfrom="0,1", tsto ="1,1",tsduration = 0.5, switch = true, style = 0,offset = "-250,0", channel = 3)]
[interlude(channel = 3, switch = false, type = 3, slot = "m", pfrom = "-250,0", pto="-250,0", name = "avg_npc_900_1#1$1", duration = 0)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_891_1#1$1", focus="r")]
[name="娜斯提"]锡人先生？
[name="娜斯提"]我们很快有一场发布会要开始，请您长话短说。
[charslot(slot = "r", focus="n")]
[interlude(channel = 3, switch = true)]
[name="锡人"]在你们不断往空中抛射各色试验品的这段时间里，我回卡兹戴尔转了转。
[charslot(slot = "r", name = "avg_npc_891_1#1$1", focus="r")]
[interlude(channel = 3, switch = false)]
[name="娜斯提"]......您知道我对这件事的态度。
[charslot(slot = "r", focus="n")]
[interlude(channel = 3, switch = true)]
[name="锡人"]是的，年轻的女妖，我知道。
[name="锡人"]我的结论是，他们对你的态度和你对他们的态度，区别不大。
[name="锡人"]当然，考虑到他们与泰拉诸国的恶劣关系，如果他们真的决定对你的计划给予全力支持，那才是十足的麻烦。
[charslot(slot = "r", name = "avg_npc_891_1#2$1", focus="r")]
[interlude(channel = 3, switch = false)]
[name="娜斯提"]多谢您的告知。发布会的时间很近了——
[charslot(slot = "r", focus="n")]
[interlude(channel = 3, switch = true)]
[name="锡人"]别急，听完我接下来要说的话。
[name="锡人"]娜斯提·鲁诺瑞伊，莱茵生命工程科主任。
[name="锡人"]你明知道那个被人许诺的梦，从来都不只有萨卡兹能够与你分享。
[name="锡人"]对你与你的精灵朋友共同推进的这项大胆计划，梅兰德基金会将会予以一切可能的支持。
[charslot(slot = "r", name = "avg_npc_891_1#2$1", focus="r")]
[interlude(channel = 3, switch = false)]
[name="娜斯提"]......
[charslot(slot = "r", focus="n")]
[interlude(channel = 3, switch = true)]
[name="锡人"]梅兰德基金会将择日与你们商讨围绕该计划的各项事宜，包括在未来的发射计划中重新建立一座更加完备的......
[charslot(slot = "r", name = "avg_npc_891_1#1$1", focus="r")]
[interlude(channel = 3, switch = false)]
[name="娜斯提"]“万星园”。
[charslot(slot = "r", 

... (全文25826字符)
```

### training_act34side_01_a

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动34side教学关1_a

[Battle.Pause]


[Tutorial(protectTime=0.5, dialogHead="$avatar_popka", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
好多海怪，根本清理不过来......

[PopupDialog(dialogHead="$avatar_kroos")] 我~来~支——欸，完全没有可以落脚的地方......






```

### training_act34side_01_b

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动34side教学关1_b

[InputBlocker(blockInput=true)]

[Delay(time=3)]  

[Battle.Pause]

[PopupDialog(dialogHead="$avatar_doberm")] 注意观察战场环境！刚刚那只海嗣死亡时，它头顶的<@tu.kw>甲壳极速增生</>，完全占据了所在的地块。其他海嗣应该<@tu.kw>不会从那里通过</>了。

[Tutorial(focusX=-50, focusY=90, focusWidth=140, focusHeight=140, anchor="Center",\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 占据了地块的<@tu.kw>赘生甲壳</>，恰好可以充当高台干员的落脚点。克洛丝，<@tu.kw>去赘生甲壳上待命</>。
```

### training_act34side_01_c

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动34side教学关1_c

[Battle.Pause]

[Tutorial(protectTime=0.5, dialogHead="$avatar_stward", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 又有大批海怪出现了！

[Tutorial(focusX=50, focusY=30, focusWidth=160, focusHeight=150, anchor="Center",\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
注意利用我们带来的<@tu.kw>航道信标</>！

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 部署在航道信标<@tu.kw>周围高台</>上的我方单位，可以为其充能。周围高台上的我方单位越多，航道信标的充能速度就越快。

[Tutorial(protectTime=0.5, dialogHead="$avatar_kroos", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 可是，航道信标周围没有高台哦......
```

### training_act34side_01_d

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动34side教学关1_d

[Battle.Pause]

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
像刚才那样，利用海嗣死亡时甲壳增生的习性，创造可部署高台干员的赘生甲壳！
```

### training_act34side_01_e

```
[HEADER(is_tutorial=true, is_skippable=false)] 活动34side教学关1_e

[Battle.SwitchToDefaultUIState] 

[Battle.Pause]

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 航道信标充能完成后，会在一定范围内令所有敌方单位的行动速度减缓，同时我方单位的攻击可造成<@tu.kw>灼燃损伤</>。

[Tutorial(protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
现在，利用航道信标清剿剩余的海嗣！





```


## 统计

- 总字符数：427421
- 对话行数：3556


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
