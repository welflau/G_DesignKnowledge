# 明日方舟 · 活动剧情 · act28side（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act28side」完整剧情脚本（23个文件，3408行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act28side
- 脚本文件数：23

### level_act28side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[warp(name="chiyu01")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_iceforest_2",screenadapt="coverall")]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="a")]
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1", focus="n")]
慌乱间，杰西卡摸向腰间的手铳。可恐惧让她的手指搭在铳套上，迟迟无法弯曲。
她隐约从寒风中嗅到了一丝腥气。
[dialog]
[charslot(slot = "m", name = "avg_1034_jesca2_1#11$1")]
[delay(time=1)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#11$1", focus="n")]
[name="？？？"]别乱动。
[dialog]
[charslot]
[StopSound(channel="a", fadetime=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_avg_gunshot", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_fmalebstwhin", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=2)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="a")]
[SoundVolume(volume=1, channel="a",fadetime=3)]
[PlaySound(key="$d_avg_wind", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=0.3, r=255, g=255, b=255, fadetime=0.8, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1.5, block=true)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=2)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[delay(time=1)]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1034_1#1$1", bstart=0.2,bend=0.7, duration=2,isblock=true)]
一位猎人从林中走进杰西卡的视线，他手里的铳还在冒烟，宽大的帽檐遮住了眼睛。
[dialog]
[charslot]
[delay(time=1)]
她转身再看向身后，一具野兽的尸体横在雪地上，头上的伤口还在汩汩地流着鲜血。
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2)]
[charslot(slot = "m", name = "avg_npc_1034_1#1$1", duration=2, isblock=true)]
[StopSound(channel="a", fadetime=2)]
[name="年老的猎人"]在这里你该多留点神。
[charslot(slot = "m", name = "avg_1034_jesca2_1#15$1")]
[name="杰西卡"]......谢谢您......救了我。
[charslot(slot = "m", name = "avg_npc_1034_1#10$1")]
[name="年老的猎人"]顺手罢了。
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(duration=1.5, isblock=true)]
老人一边收铳，一边径直走向野兽的尸体。
[dialog]
[PlaySound(key="$d_avg_knife", volume=1)]
[delay(time=1)]
他抽出小刀，破开野兽的肚腹，角度精准，没有多少血液流出。
随后，他将双手塞入尸体腹内，发出一声长长的叹息。
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1034_1#2$1", focus="l")]
[name="年老的猎人"]这鬼天气真是他妈冷得要死。
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="r")]
[name="杰西卡"]......老先生，您是附近的猎人吗？
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="年老的猎人"]算是吧。
[charslot(slot = "r", name = "avg_1034_jesca2_1#16$1", focus="r")]
[name="杰西卡"]您知道达维镇该怎么走吗？
[charslot(slot = "l", name = "avg_npc_1034_1#10$1", focus="l")]
[name="年老的猎人"]......你去那里做什么？
[charslot(slot = "r", name = "avg_1034_jesca2_1#16$1", focus="r")]
[name="杰西卡"]我打算在那里和队友会合。
[charslot(slot = "l", name = "avg_npc_1034_1#10$1", focus="l")]
[name="年老的猎人"]你不是一个人来的？
[charslot(slot = "r", name = "avg_1034_jesca2_1#14$1", focus="r")]
[name="杰西卡"]嗯，我和队友分头行动，从一伙流寇手中营救了一名人质，但任务结束后我的通讯器意外损坏，在林子里迷了路。
[charslot(slot = "l", name = "avg_npc_1034_1#10$1", focus="l")]
[name="年老的猎人"]人质？长什么样？
[charslot(slot = "r", name = "avg_1034_jesca2_1#14$1", focus="r")]
[name="杰西卡"]是位年老的丰蹄男性......
[charslot(slot = "l", name = "avg_npc_1034_1#4$1", focus="l")]
[name="年老的猎人"]......居然是你们。
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="年老的猎人"]那好，跟我走吧。
[charslot(slot = "r", name = "avg_1034_jesca2_1#3$1", focus="r")]
[name="杰西卡"]去、去哪里？
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="年老的猎人"]你不是要去达维镇吗？
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="r")]
[name="杰西卡"]但是......
[charslot(slot = "l", name = "avg_npc_1034_1#5$1", focus="l")]
[name="年老的猎人"]来不来随你便。
[dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot = "l", posfrom="0,0", posto="0,-20", duration=1, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l", posfrom="0,-20", posto="0,0", duration=0.3, isblock=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(slot = "l", posfrom="0,0", posto="-300,0",afrom=1, ato=0, duration=2, isblock=true)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="n")]
老人没再看杰西卡，起身将野兽尸体扛在肩上，快步向林子深处走去。
[charslot(slot = "r", name = "avg_1034_jesca2_1#3$1", focus="r")]
[name="杰西卡"]等等，等等！
[dialog]
[PlaySound(key="$d_avg_snowrun", volume=1, loop=true, channel="d")]
[StopSound(channel="d", fadetime=2)]
[charslot(slot = "r", posfrom="0,0", posto="-500,0", afrom=1, ato=0, duration=1, isblock=true)]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_iceforest_2",screenadapt="coverall")]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_106_franka_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="n")]
[name="芙兰卡"]哎，杰西卡一个人在外面，你真的放心吗？
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]我知道你担心杰西卡，我也一样。但是共同战斗这么多年，我相信她有能力独自处理好。
[charslot(slot = "l", name = "avg_106_franka_1#4$1", focus="l")]
[name="芙兰卡"]我只是不确定会不会还有残余的匪徒。两三个倒没问题，可万一他们还有残部呢？
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]杰西卡曾经历过的战斗可比那些乌合之众危险得多。
[charslot(slot = "l", name = "avg_106_franka_1#4$1", focus="l")]
[name="芙兰卡"]......
[charslot(slot = "r", name = "avg_107_liskam_1#2$1", focus="r")]
[name="雷蛇"]要么是箭簇贴着头皮飞过，要么是利刃擦着喉咙划过。
[name="雷蛇"]再要么，四周全是高

... (全文19665字符)
```

### level_act28side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1")]
[Background(image="42_g3_diner",screenadapt="coverall")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1035_1#10$1", focus="r")]
[name="里昂"]嘶......海伦娜，今天你这儿也太冷了吧。
[charslot(slot = "l", name = "avg_4104_coldst_1#4$1", focus="l")]
[name="海伦娜"]炭火快用完了，得省着些用......
[charslot(slot = "r", name = "avg_npc_1035_1#9$1", focus="r")]
[name="里昂"]那就烧我家里堆积成山的账单，反正烧光了银行还会寄给我更多。
[charslot(slot = "l", name = "avg_4104_coldst_1#3$1", focus="l")]
[name="海伦娜"]咳。
[charslot(slot = "r", name = "avg_npc_1035_1#6$1", focus="r")]
[name="里昂"]感冒了？哎，我这就回家把那堆废纸给你拿过来。
[charslot(slot = "l", name = "avg_4104_coldst_1#4$1", focus="l")]
[name="海伦娜"]（小声）你以为我为什么咳嗽？你也不看看谁在这里......
[dialog]
[charslot(slot = "r", name = "avg_npc_1035_1#7$1", focus="r")]
[Delay(time=1)]
[name="里昂"]哦，是西尔维娅啊！
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1039_1#1$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[name="西尔维娅"]早、早上好，里昂先生......
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#4$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1035_1#7$1", focus="r")]
[name="里昂"]银行的人光临这家小破餐馆，有何贵干？
[charslot]
[charslot(slot = "m", name = "avg_npc_1039_1#8$1")]
[name="西尔维娅"]抱、抱歉......
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#4$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_1035_1#7$1", focus="r")]
[name="里昂"]哼。
[charslot(slot = "l", name = "avg_4104_coldst_1#11$1", focus="l")]
[name="海伦娜"]咳咳......里昂，好久没见到本尼了，那孩子最近干什么呢？
[charslot(slot = "r", name = "avg_npc_1035_1#1$1", focus="r")]
[name="里昂"]忙学业啊，他现在天天看书看到凌晨才睡。
[charslot(slot = "l", name = "avg_4104_coldst_1#11$1", focus="l")]
[name="海伦娜"]学校不是早关了吗？
[charslot(slot = "r", name = "avg_npc_1035_1#2$1", focus="r")]
[name="里昂"]隔壁住的赛琳娜女士以前是老师，她觉得本尼这个年纪不上学太可惜，就让他到自己家学东西。
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1", focus="l")]
[name="海伦娜"]那可太好了，本尼是多聪明的孩子啊，当时知道自己不能再去上学，他伤心得不行。
[charslot(slot = "r", name = "avg_npc_1035_1#1$1", focus="r")]
[name="里昂"]是啊，那一整年他都焦虑得不行。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1039_1#7$1")]
[name="西尔维娅"]里、里昂先生，我......其实也可以教本尼......
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1", focus="n")]
[name="海伦娜"]对啊，西尔维娅可是从哥伦比亚最好的商学院毕业的——
[charslot(slot = "r", name = "avg_npc_1035_1#7$1", focus="r")]
[name="里昂"]跟她学什么？长大了去银行给人发账单？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1039_1#8$1")]
[name="西尔维娅"]我......
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#3$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1", focus="n")]
[name="海伦娜"]里昂，你的早饭再不吃就冷了！
[charslot(slot = "r", name = "avg_npc_1035_1#8$1", focus="r")]
[name="里昂"]哼......
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1039_1#2$1")]
[name="西尔维娅"]我、我的饭钱留在桌子上了......还有工作，我先离开了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1, isblock=true)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_4104_coldst_1#6$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1", focus="n")]
[name="海伦娜"]里昂，达维镇没有哪个人的贷款是她给放出去的，你给她甩脸色做什么？
[charslot(slot = "r", name = "avg_npc_1035_1#8$1", focus="r")]
[name="里昂"]向其他人说情去，其他人比我还凶呢。
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1", focus="l")]
[name="海伦娜"]她毕竟是我们看着长大的......
[charslot(slot = "r", name = "avg_npc_1035_1#2$1", focus="r")]
[name="里昂"]就是因为看着她长大......我才更气不过！
[charslot(slot = "l", name = "avg_4104_coldst_1#5$1", focus="l")]
[name="海伦娜"]唉......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_snow_2",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]女士，抱歉让您久等了，希望我们来得没有太晚。
[charslot(slot = "m", name = "avg_npc_1039_1#9$1")]
[name="西尔维娅"]您......您好，没关系的，完全不晚。
[charslot(slot = "m", name = "avg_107_liskam_1#9$1")]
[name="雷蛇"]请问您怎么称呼？
[charslot(slot = "m", name = "avg_npc_1039_1#9$1")] 
[name="西尔维娅"]你们可以叫我、我......
[charslot(slot = "m", name = "avg_npc_1039_1#2$1", action="shake", afrom=1 , ato=1, power=3, times=30, duration=0.3)]
[name="西尔维娅"]阿嚏——！
[charslot(slot = "m", name = "avg_107_liskam_1#7$1")]
[name="雷蛇"]女士，您究竟在这里站了多久？
[charslot(slot = "m", name = "avg_npc_1039_1#1$1")]
[name="西尔维娅"]从早上......就在等了，消息里只说你们会今天到，但是......没说具体时间。
[charslot(slot = "m", name = "avg_106_franka_1#5$1")]
[name="芙兰卡"]早上？现在已经是下午了，你一直在这站着？
[charslot(slot = "m", name = "avg_npc_1039_1#1$1")]
[name="西尔维娅"]是的......
[charslot(slot = "m", name = "avg_107_liskam_1#7$1")]
[name="雷蛇"]我们三个小时前还向地块上发送过消息，更新了我们的预计到达时间。
[charslot(slot = "m", name = "avg_npc_1039_1#3$1")]
[name="西尔维娅"]......我、我并没有接到任何通知。
[charslot(slot = "m", name = "avg_106_franka_1#4$1")]
[name="芙兰卡"]太怪了，谁派你来的？
[charslot(slot = "m", name = "avg_npc_1039_1#1$1")]
[name="西尔维娅"]是我们......经理。
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]经理？政府里也有经理？
[charslot(slot = "m", name = "avg_npc_1039_1#6$1")]
[name="西尔维娅"]您误会了，我、我不是政府的人......我在本地银行工作。
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]所以达维镇的政府呢？
[charslot(slot = "m", name = "avg_npc_1039_1#8$1")]
[name="西尔维娅"]这个......我......达维镇的政府其实......
[name="西尔维娅"]......
[dialog]
[charslot]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[delay(time=1)]
[charslot(slot = "r"

... (全文24454字符)
```

### level_act28side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g3_diner",screenadapt="coverall")]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.1, channel="a",fadetime=2)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="杰西卡"]什、什么？
[dialog]
[charslot(slot = "m", name = "avg_1034_jesca2_1#11$1")]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=1, isblock=true)]
[charslot(slot = "m", name = "avg_4104_coldst_1#8$1")]
[name="海伦娜"]哎，杰西卡，你去干什么？
[charslot(slot = "m", name = "avg_4104_coldst_1#8$1", focus="n")]
[name="杰西卡"]我得去找他——
[dialog]
[charslot]
[PlaySound(key="$dooropenquite")]
[Delay(time=1)]
[name="？？？"]杰西卡？！
[dialog]
[StopSound(channel="a", fadetime=2)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_106_franka_1#5$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1")]
[name="杰西卡"]......芙兰卡？罗拉？
[charslot(slot = "m", name = "avg_4105_almond_1#7$1")]
[name="罗拉"]你怎么在这里？
[dialog]
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[PlaySound(key="$d_gen_transmissionget")]
[delay(time=2)]
[charslot(slot = "m", name = "avg_106_franka_1#3$1")]
[name="芙兰卡"]报告，已经确定杰西卡的位置，她就在那家餐厅，嘴角还油汪汪的，看起来她已经对餐厅的菜单颇有心得了。
[charslot(slot = "m", name = "avg_106_franka_1#3$1", focus="n")]
[name="雷蛇"]知道了，银行这边的事情也差不多告一段落了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g3_diner",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_107_liskam_1#1$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]优等生，我们等你等得快要饿死了。
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]这家餐厅的位置有些偏僻，我找到这里花了不少时间。
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]唉，凑合凑合算了。
[charslot(slot = "m", name = "avg_4104_coldst_1#6$1")]
[name="海伦娜"]小姑娘，你们把迈尔斯安全送回家，我心里是很感激没错，但你们要是对我的厨艺发表意见，可就是另外一码事了。
[charslot(slot = "m", name = "avg_106_franka_1#7$1")]
[name="芙兰卡"]怎么会？天寒地冻的时候有口热饭吃，我们有什么可挑剔的。你说对吧，小罗拉？
[charslot(slot = "m", name = "avg_4105_almond_1#4$1")]
[name="罗拉"]我——对，我觉得很好吃！我妈妈和我奶奶都没有你做的好吃！
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]还是有懂行的嘛！小朋友，她们是做什么的？厨师吗？
[charslot(slot = "m", name = "avg_4105_almond_1#4$1")]
[name="罗拉"]呃，我妈妈是医生，奶奶是工程师，她们都不会做饭......我爸爸才是家里做饭的人。
[charslot(slot = "m", name = "avg_npc_1035_1#3$1")]
[name="里昂"]噗、噗哈哈哈哈哈哈哈！
[charslot(slot = "m", name = "avg_4104_coldst_1#6$1")]
[name="海伦娜"]里昂，你是不是开心过头了？
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]咳，别别别，我吃饭，我这就吃饭。
[dialog]
[charslot(slot = "m", name = "avg_107_liskam_1#9$1")]
[Delay(time=1)]
[name="雷蛇"]那个......老板娘，请问这里有水吗？我想来一杯。
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]没问题，稍等。
[dialog]
[charslot]
随手拿起桌上的空杯子，老板娘推开窗户，从厚厚的积雪中铲了满满一整杯。
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]等着吧，化开就能喝了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=2, isblock=true)]
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]对了，为什么是银行的人来和我们对接，队长？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]这里的政府机构只是勉强运转，没有余力与我们对接，所以将此事全权交付给了银行。
[charslot(slot = "m", name = "avg_106_franka_1#5$1")]
[name="芙兰卡"]银行？！那好吧，银行是怎么说的？
[charslot(slot = "m", name = "avg_107_liskam_1#3$1")]
[name="雷蛇"]银行的话可以大致总结为两句：总而言之，全力支持；具体问题，容后再议。
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]啧，一听就很难缠，但你该不会就这么灰溜溜地跑来吃饭了吧？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]虽然他们既无资源，也无人手，但好歹手里有钱。
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1")]
[name="杰西卡"]可我们本来也不缺经费。不过......如果银行说到做到的话，我们在达维镇上多雇点工人怎么样？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]动力炉出事后，地块上多数人都选择了离开，现在不好说还有几名工人留在这里。
[charslot(slot = "m", name = "avg_106_franka_1#4$1")]
[name="芙兰卡"]怪不得，已经快八点了，可居民楼里没几扇窗户亮着灯。
[charslot(slot = "m", name = "avg_4105_almond_1#1$1")]
[name="罗拉"]其实不用那么多人，修理工作交给我和小队成员就可以。我们真正需要的是熟知能源塔内情况的人。银行有提供合适人选吗？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]没。
[charslot(slot = "m", name = "avg_npc_1035_1#10$1")]
[name="里昂"]那个......咳咳。
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1")]
[name="杰西卡"]里昂先生......？
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]刚刚光顾着修你的通讯器，忘记自我介绍了。
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]里昂·特雷门，本地矿厂的爆破工程师，很高兴认识你们。
[charslot(slot = "m", name = "avg_107_liskam_1#6$1")]
[name="雷蛇"]矿厂的爆破工程师......一直留到现在？
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]唉，还是有那么几个固执的老家伙不愿意离开的。我四岁时就在这片矿厂了，去别的地方我根本适应不了。
[name="里昂"]年初动力炉出问题就是我带着人去处理的。最后虽然没能修好，但好歹让它继续运转了一段时间。
[charslot(slot = "m", name = "avg_107_liskam_1#9$1")]
[name="雷蛇"]您做得很好，它直到现在还在运转。
[charslot(slot = "m", name = "avg_npc_1035_1#8$1")]
[name="里昂"]都是过去的事了，不提也罢，但你们刚刚说的酬劳......
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]啊，这个......任务要求是尽快，所以不按日结算，每天只发必要的经费和食宿费。
[name="雷蛇"]等到动力炉修好之后，报酬一次性结清，越快修好，额度越高。
[name="雷蛇"]当然，出于合作考虑，我们可以预付一部分报酬。
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]具体数字是？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]你的工作应该是顾问。顾问的话，两个月搞定的报酬是四万，一个月内搞定就翻番，要是一周内能搞定......
[charslot(slot = "m", name = "avg_npc_1035_1#5$1")]
[name="里昂"]再翻一倍？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]再多一些，你能拿到二十万。
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]成交！
[charslot(slot = "m", name = "avg_106_franka_1#5$1")]
[name="芙兰卡"]大叔，你答应得这么痛快？
[charslot(slot 

... (全文23076字符)
```

### level_act28side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Background(image="bg_labcorridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_welding", volume=1, loop=true, channel="b")]
[StopSound(channel="b", fadetime=2)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_4105_almond_1#3$1", duration=1, isblock=true)]
[name="罗拉"]我一定是出现幻觉了。
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]怎么？
[charslot(slot = "m", name = "avg_4105_almond_1#2$1")]
[name="罗拉"]按照排查的结果，能源塔里几乎没一处完好无损的地方，全是破损和坏件，还丢了一大堆东西，按说早该塌了。
[dialog]
[charslot]
[PlaySound(key="$transmission")]
[delay(time=2)]
[name="黑钢技术员"]我这边也是，备用件几乎全没了，连传送带都被拆了。
[charslot(slot = "m", name = "avg_npc_1038_1#7$1")]
[name="迈尔斯"]唉......商队大概隔两个月会来一次达维镇，用生活必需品和我们换东西，主要是用不上了的工业设备。
[charslot(slot = "m", name = "avg_npc_1035_1#7$1")]
[name="里昂"]哼，他们那是换？他们那是明抢！看到这辆叉车了吗？买来之后基本没怎么用过，八成新的叉车！
[name="里昂"]你猜那帮所谓的商队想用什么东西换它？十箱罐头！
[charslot(slot = "m", name = "avg_npc_1038_1#3$1")]
[name="迈尔斯"]大家总归是要吃饭的......
[charslot(slot = "m", name = "avg_4105_almond_1#3$1")]
[name="罗拉"]......看来这座动力炉在发生事故之前就已经处于严重的失修状态了。
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]原来操持这活计的炉工是有很多的。现在就剩下迈尔斯一个人，能保证运转就不错了，总不能把他一个人掰成十个用吧。
[charslot(slot = "m", name = "avg_4105_almond_1#8$1")]
[name="罗拉"]别说了，我现在恨不得把自己一个掰成一百个来用......这活儿根本没有任务单上说的那么轻松，弄不好要修到年后去。
[charslot(slot = "m", name = "avg_npc_1035_1#6$1")]
[name="里昂"]别啊，我还指望一周修好拿二十万呢。
[charslot(slot = "m", name = "avg_4105_almond_1#11$1")]
[name="罗拉"]二十万算什么，要是能在特里蒙投资大佬身边做安保，可不止二十万呢......
[charslot(slot = "m", name = "avg_4105_almond_1#4$1")]
[name="罗拉"]等大佬被我伺候开心了，大手一挥，给我两个亿，还会温柔地对我说：啊，这点投资你拿去，别客气。
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]啧，两个亿......
[charslot(slot = "m", name = "avg_npc_1038_1#6$1")]
[name="迈尔斯"]那么多钱，整个达维镇都能重新修一遍。
[charslot(slot = "m", name = "avg_4105_almond_1#11$1")]
[name="罗拉"]唉，也就是过过嘴瘾，我在黑钢的那点项目哪里花得了两个亿......根本不够格。
[charslot(slot = "m", name = "avg_npc_1038_1#8$1")]
[name="迈尔斯"]你这小姑娘，别做白日梦了，抓紧干活吧。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_4105_almond_1#11$1")]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot = "m", name = "avg_4105_almond_1#11$1", posfrom="0,0", posto="10,-40", afrom=1, ato=0, duration=1,isblock=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_welding", volume=1, loop=true, channel="b")]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget")]
[delay(time=2)]
[name="黑钢技术员"]老爷子，你不知道，听着罗拉小姐絮絮叨叨我们才安心，她做事时脑子转得飞快，全靠讲废话散热，要是她突然不说话了，说明......
[dialog]
[name="罗拉"]......
[dialog]
[stopmusic(fadetime=2)]
[StopSound(channel="b", fadetime=2)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_4105_almond_1#8$1", posfrom="10,-40", posto="0,0", duration=1, isblock=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4105_almond_1#8$1", posfrom="0,0", posto="0,0", duration=0, isblock=true)]
[name="罗拉"]............
[name="罗拉"]..................
[charslot(slot = "m", name = "avg_npc_1038_1#1$1")]
[name="迈尔斯"]呃，说明什么？
[charslot(slot = "m", name = "avg_npc_1038_1#1$1", focus="n")]
[name="黑钢技术员"]......说明问题太大，她脑子已经转宕机了。
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_4105_almond_1#5$1")]
[name="罗拉"]（吞咽口水）
[charslot(slot = "m", name = "avg_4105_almond_1#6$1")]
[name="罗拉"]......各队听我指示，迅速停下手中工作，沿原路退出能源塔，快！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="罗拉"]动作快！！
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="a")]
[StopSound(channel="a", fadetime=1)]
[charslot(duration=1, isblock=true)]
[charslot(slot = "r", name = "avg_npc_1038_1#6$1")]
[charslot(slot = "l", name = "avg_npc_1035_1#5$1")]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "r", name = "avg_npc_1038_1#6$1", afrom=1, ato=0, duration=1)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1035_1#5$1", afrom=1, ato=0, duration=1, isblock=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_crystal_shatter", volume=1)]
[delay(time=1.5)]
[CameraShake(duration=6, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_explosion", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[PlaySound(key="$d_avg_collapse", volume=1)]
[Effect(name="$e_sandfall_01",layer = 2)]
[delay(time=6)]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g4_bank",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$keyboard", volume=1)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_npc_223", focus="r")]
[charslot(slot = "l", name = "avg_npc_1039_1#1$1", focus="n")]
[name="无聊的银行员工"]西尔维娅，账目流水能在今晚九点前处理好吗？
[charslot(slot = "l", name = "avg_npc_1039_1#7$1", focus="l")]
[name="西尔维娅"]没、没问题。
[charslot(slot = "r", name = "avg_npc_223", focus="r")]
[name="无聊的银行员工"]那我就不管了。
[charslot(slot = "l", name = "avg_npc_1039_1#1$1", focus="l")]
[name="西尔维娅"]好......
[charslot(slot = "r", name = "avg_npc_223", focus="r")]
[name="无聊的银行员工"]啊哈......
[name="无聊的银行员工"]唉，经理和那两个人聊多久了？
[dialog]
[charslot(slot = "l", name = "avg_npc_1039_1#1$1", focus="n")]
[name="银行经理"]......账款......情况不甚乐观......
[name="雷蛇"]......这不是......擅作决断......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="42_g4_bank",s

... (全文24736字符)
```

### level_act28side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Background(image="42_g6_sonwydowntown_d",screenadapt="coverall", xScale=1.1,yScale=1.1, x=60)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1042_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1043_1#1$1", duration=1, isblock=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1042_1#1$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1043_1#1$1", focus="none")]
[name="焦虑的男性"]去银行贷款？你疯了？
[charslot(slot = "l", name = "avg_npc_1043_1#1$1", focus="l")]
[name="暴躁的女性"]那你说怎么办？就这么几天时间，你到底怎么凑齐去特里蒙的车费？这次临床试验是提比最后的机会了！
[charslot(slot = "r", name = "avg_npc_1042_1#1$1", focus="r")]
[name="焦虑的男性"]我再想想办法......
[charslot(slot = "l", name = "avg_npc_1043_1#1$1", focus="l")]
[name="暴躁的女性"]什么办法？除了贷款，已经没别的办法了！
[charslot(slot = "r", name = "avg_npc_1042_1#1$1", focus="r")]
[name="焦虑的男性"]......对、对了，我们之前给提比投过重病保险的！
[charslot(slot = "l", name = "avg_npc_1043_1#1$1", focus="l")]
[name="暴躁的女性"]你以为我昨天下午去干什么了？我去了银行想兑现保险，可提比的病根本不在他们的理赔范围内！
[charslot(slot = "r", name = "avg_npc_1042_1#1$1", focus="r")]
[name="焦虑的男性"]算我求你，那也先别想贷款的事，好不好？
[name="焦虑的男性"]想想你姐姐，她就借了一笔小钱，可就因为那笔钱破了产，被搞得那么惨，最后......
[charslot(slot = "l", name = "avg_npc_1043_1#1$1", focus="l")]
[name="暴躁的女性"]......
[name="暴躁的女性"]......一家人都死在了去拓荒地的路上。
[charslot(slot = "r", name = "avg_npc_1042_1#1$1", focus="r")]
[name="焦虑的男性"]所以你先冷静一下，一定还有别的办法......
[dialog]
[charslot(slot = "r", posfrom="0,0", posto="-120,0", afrom=1, ato=0, duration=1.5)]
[charslot(slot = "l", posfrom="0,0", posto="-120,0", afrom=1, ato=0, duration=1.5)]
[BackgroundTween(xFrom=60, xTo=-60, duration=1.5,ease="OutQuad",block=true)]
[Delay(time=1)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_106_franka_1#1$1", posfrom="150,0", posto="0,0", duration=1.5)]
[Delay(time=0.5)]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", posfrom="150,0", posto="0,0", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_106_franka_1#1$1", focus="l")]
[name="芙兰卡"]每次来银行都能看见这样的事......
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]所以我们更要来银行，更要来参加这个所谓的“答谢酒会”，芙兰卡。
[charslot(slot = "r", name = "avg_107_liskam_1#2$1", focus="r")]
[name="雷蛇"]如果不来亲眼见识见识......我们只会更加一无所知。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.8, channel="a",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[SoundVolume(volume=0.1, channel="a",fadetime=2)]
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]由巴伦基地亲自来拖拽达维镇回到原本的航路？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]此次任务是受州政府直接委托，最终结果会直接关系到黑钢的信誉与形象，我们一定会尽力而为。
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]那可真是太好了，我们不胜感激。
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]该做的而已。
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]二位要喝啤酒还是香槟？我们这种小地方，能提供的东西未免不尽如人意，二位请多担待。
[charslot(slot = "m", name = "avg_106_franka_1#3$1")]
[name="芙兰卡"]......不尽如人意？您太谦虚了。
[charslot(slot = "m", name = "avg_106_franka_1#7$1")]
[name="芙兰卡"]看看，队长，这啤酒瓶上虽然没有商标，质量可不比一些精酿厂的小众品牌差，这边的香槟也是高级货......好品味啊。
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]作为派驻艰苦地区的福利，我们的物资供应里确实会有些相对高级一点的东西，毕竟大家也是要维持士气的。
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]能让人敞开喝冰啤酒的供暖力度也是维持士气的一环？
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]......正如您所说，包括电力和取暖在内，我们有一套独立的备用供能系统。
[charslot(slot = "m", name = "avg_106_franka_1#4$1")]
[name="芙兰卡"]其他建筑好像没有这套备用系统啊。
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]这是在早期规划建设时，第一任行长出于安全考虑做下的英明决定。
[name="银行经理"]金融机构提供的服务相对特殊，大笔资金流入流出，无论系统或者资源，都是自己的用着更靠谱。
[name="银行经理"]想必黑钢在达维镇营建自己的安全屋也是出于同样的考虑，您说呢，芙兰卡女士？
[charslot(slot = "m", name = "avg_106_franka_1#4$1")]
[name="芙兰卡"]啊......来杯水就行，这瓶啤酒还是留给贵行员工加油打气吧。
[dialog]
[StopSound(channel="a", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]此次达维镇动力炉的修复情况，我们已经派人赶回黑钢总部汇报。
[name="雷蛇"]现在动力炉仍然没能恢复供应航行的能力，想必总部会拟定新的解决方案。
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]我们也很感激贵公司对达维镇的付出。
[name="银行经理"]不过，在解决方案出台之前，我们有个不情之请。
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]
[name="芙兰卡"]......不情之请？
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]我们希望各位帮助维护达维镇的治安。
[name="银行经理"]各位在地块外围应该遇见了些匪徒。他们给这里造成了很大损失，更令人担忧的是......
[name="银行经理"]这地块上有些人，说得好听些是混混，说得难听一些，就是那些匪徒的后备军。
[name="银行经理"]如果各位可以帮忙将他们清除出达维镇的话，我们不胜感激。这里有份名单......
[dialog]
[PlaySound(key="$d_avg_paper1", volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]这几天，我们已经派出人手在地块外围执行警戒的任务，根据他们的报告，我不认为地块上有这么多危险分子。
[dialog]
[PlaySound(key="$d_avg_paper2", volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]那些已经破产，却不愿用辛勤劳动来偿还债务的家伙，难保哪天不会铤而走险，不是吗？
[charslot(slot = "m", name = "avg_107_liskam_1#3$1")]
[name="雷蛇"]......既然您这么说，我们会再详细核查的。
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[name="银行经理"]“详细核查”？您确定？您不信任我们的话吗？
[charslot(slot = "m", name = "avg_107_liskam_1#2$1")]
[name="雷蛇"]如果因为核查一份名单就损伤了我们对贵行的信任，那这样的信任，未免也太脆弱。
[dialog]
[charslot(slot = "m", name = "avg_npc_1041_1#1$1")]
[delay(time=1)]
[name="银行经理"]......无妨。
[name="银行经理"]您既然想查，就彻彻底底地查一遍好了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, b

... (全文28097字符)
```

### level_act28side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Background(image="bg_indoor_u",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", duration=1)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", duration=1, isblock=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1034_1#6$1", focus="l")]
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="n")]
[name="伍德洛"]说服里昂卖他自己的股份？不可能，我不去。
[charslot(slot = "r", name = "avg_1034_jesca2_1#3$1", focus="r")]
[name="杰西卡"]为什么？你们不是朋友吗？
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]我和那小子之所以能做朋友，就是因为我从来不逼他做事。矿厂股份的事我们每个人都和他说过，但他谁的话也不听。
[charslot(slot = "r", name = "avg_1034_jesca2_1#9$1", focus="r")]
[name="杰西卡"]真的不行吗？
[charslot(slot = "l", name = "avg_npc_1034_1#2$1", focus="l")]
[name="伍德洛"]不行。
[charslot(slot = "r", name = "avg_1034_jesca2_1#10$1", focus="r")]
[name="杰西卡"]呃......我本来还想着，如果您愿意帮我劝劝里昂先生......就......
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]就怎样？
[charslot(slot = "r", name = "avg_1034_jesca2_1#15$1", focus="r")]
[name="杰西卡"]就、就用这盒巧克力作为答谢......
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]哦，巧克力啊。
[charslot(slot = "r", name = "avg_1034_jesca2_1#15$1", focus="r")]
[name="杰西卡"]出发时家里的甜品师塞给我的，说是路上嘴巴空可以嚼一块，吃到现在就剩最后一盒了......
[name="杰西卡"]我，这个，还真、真的有些舍不得送人。所以，既然伍德洛先生您不愿意，那只好算了......
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]哦。
[charslot(slot = "r", name = "avg_1034_jesca2_1#3$1", focus="r")]
[name="杰西卡"]（小声）怎么只是“哦”了一声，这和说的不一样——
[name="杰西卡"]您、您要是不愿意，就、就没有巧克力了，呃，不对......
[charslot(slot = "r", name = "avg_1034_jesca2_1#2$1", focus="r")]
[name="杰西卡"]那个......
[dialog]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#5$1", focus="r")]
[name="杰西卡"]好吧，我承认，是海伦娜女士建议我带巧克力来找您的......她说您喜欢这些......
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]她让你来，你就来了？
[charslot(slot = "r", name = "avg_1034_jesca2_1#11$1", focus="r")]
[name="杰西卡"]里昂先生的情况真的不容乐观......无论什么办法，我都要试一试。
[dialog]
[charslot]
伍德洛直直地盯着杰西卡看，而杰西卡并未注意到。
她沉浸在尴尬和挫败中，垂着头，绞尽脑汁地想着，如何让这次对话结束得快一点。
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="n")]
[charslot(slot = "r", name = "avg_1034_jesca2_1#5$1", focus="r")]
[name="杰西卡"]抱歉打扰了，我再回去想想别的办法......
[charslot(slot = "l", name = "avg_npc_1034_1#7$1", focus="l")]
[name="伍德洛"]那盒巧克力你放在柜子上就好了。
[charslot(slot = "r", name = "avg_1034_jesca2_1#16$1", focus="r")]
[name="杰西卡"]什么？
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]我去收拾下，洗把脸，一会儿就出发吧。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", afrom=1, ato=0, duration=1.5, focus="l", isblock=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_carwash", volume=0.08, loop=true, channel="a")]
[Delay(time=1.5)]
[StopSound(channel="a", fadetime=2)]
[Delay(time=2)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#3$1", focus="r")]
[name="杰西卡"]......成功了？！我明明都露馅了......
[charslot(slot = "r", name = "avg_1034_jesca2_1#4$1", focus="r")]
[name="杰西卡"]他到底看的是海伦娜女士的面子......还是这盒巧克力，算了，反正他都答应了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", posfrom = "0,0", posto = "-200,0",duration = 1.5)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.98, duration = 1.5, isblock=true)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#14$1", focus="r")]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.98, duration = 0, isblock=true)]
[name="杰西卡"]放在柜子上......应该是这个柜子。
[dialog]
[delay(time=1)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#16$1", focus="r")]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.98, duration = 0, isblock=true)]
[name="杰西卡"]......抽屉是拉开的？
[dialog]
[charslot]
老年萨科塔抽屉里的东西和他本人一样，简单质朴，不加一点修饰。
一条腰带，一副铳械皮套，一双露指手套。
放下巧克力，杰西卡注意到还有几张纸片被压在了手套下面。
在岁月的侵蚀下，纸页呈现出一种发脆的黄色。
杰西卡知道自己应该赶快撇开目光，但她的视线却不受控制地落在了上面。
[charslot(slot = "m", name = "avg_1034_jesca2_1#16$1")]
[name="杰西卡"]这......是伍德洛先生和老板的照片？还有另外一个萨科塔......照片底下有张纸......
[charslot(slot = "m", name = "avg_1034_jesca2_1#16$1", focus="n")]
那是一份身份证明，黑色的字迹在褐色的纸张上并不清晰，只能依稀辨认出其中几个词。
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1")]
[name="杰西卡"]柯略斯......营地......
[dialog]
[charslot(slot = "l", focus="n")]
[name="伍德洛"]巧克力还没有放好吗？
[dialog]
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1", posfrom = "0,0", posto = "200,0", afrom=1, ato=1, duration = 0.7, isblock=true, focus="m")]
[name="杰西卡"]啊，好、好了，我......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", duration=1, isblock=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1", focus="l")]
[name="伍德洛"]那就赶快走吧。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="33_g8_srcroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1")]
[name="杰西卡"]里昂先生，现在您的财务状况岌岌可危，迟迟不做决定的话......
[name="杰西卡"]等银行宣布您无力偿还债务，您就只有破产一条路，到时无论是股份还是住房都保不住......
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]如果您非要保留股份的话，就只能卖掉您现在居住的房子，可那样您会无家可归的......
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]这么多劝我卖股份的人里，你是第一个让我卖房子的。
[charslot(slot = "m", name = "avg_1034_jesca2_1#10$1")]
[name="杰西卡"]不，我不是让您卖房子，只是说这是可能的后果......
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]如果您不介意，我也可以......我是说，虽然这笔债务数目不小，但是我这里有些钱，可以给您的......
[charslot(slot = "m", name = "avg_npc_1035_1#7$1")]
[name="里昂"]什么？！谢谢了，我不需要你

... (全文25528字符)
```

### level_act28side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.1, channel="a",fadetime=2)]
[Background(image="42_g3_diner",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_sweep", volume=1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_4104_coldst_1#4$1", duration=1, isblock=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_4104_coldst_1#4$1", focus="l")]
[name="海伦娜"]说来也奇怪，供暖还能勉强维持，炉子也点着，为什么还是感觉这么冷？银行不会又在搞鬼吧？
[charslot(slot = "r", name = "avg_npc_1034_1#7$1", focus="r")]
[name="伍德洛"]反正我的袜子一晚上都没干。
[dialog]
[PlaySound(key="$blooddrop", volume=0.5)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1034_1#10$1", focus="r")]
[name="伍德洛"]嗯，什么声音......？
[charslot(slot = "l", name = "avg_4104_coldst_1#9$1", focus="l")]
[name="海伦娜"]伍迪，说过多少次了，刮刮胡子吧！每次你喝完水都溅得桌子上满是水点。
[charslot(slot = "r", name = "avg_npc_1034_1#6$1", focus="r")]
[name="伍德洛"]胡说，我从进门就没喝水。
[charslot(slot = "l", name = "avg_4104_coldst_1#9$1", focus="l")]
[name="海伦娜"]那这些水渍是怎么回事？
[dialog]
[PlaySound(key="$blooddrop", volume=1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1034_1#2$1", focus="r")]
[name="伍德洛"]你这餐厅有些年份了，我的脑子也有些年头了......
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍德洛"]所以到底是我的记忆出了差错，还是那片巨大的水痕真的一直在那里？
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", focus="n")]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_waterpipeburst", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_walkfast", volume=1, loop=true, channel="a")]
[StopSound(channel="a", fadetime=0.8)]
[charslot(slot = "l", name = "avg_4104_coldst_1#8$1", afrom=1, ato=1, posfrom = "0,0", posto = "80,0", duration = 0.5, isblock=true, focus="l")]
[name="海伦娜"]水管——水管炸了？！
[charslot(slot = "l", name = "avg_4104_coldst_1#9$1", focus="l")]
[name="海伦娜"]天......我这破地板哪里经得起泡一遍水啊！
[charslot(slot = "r", name = "avg_npc_1034_1#6$1", focus="r")]
[name="伍德洛"]快去关阀门，然后找个容器盛漫进来的水，楼上的东西我来收拾！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=1)]
[PlayMusic(key="$wasteland_loop", volume=0.6)]
[PlaySound(key="$d_avg_scoop", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", duration=1, isblock=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4104_coldst_1#5$1", focus="l", posfrom = "0,-20", posto = "0,0", duration = 1.5, isblock=true)]
[delay(time=1)]
[name="海伦娜"]我的老腰啊，差点直不起来......楼上的情况怎么样，伍迪？
[charslot(slot = "r", name = "avg_npc_1034_1#2$1", focus="r")]
[name="伍德洛"]我建议你找把椅子坐着听，毕竟你也一把年纪了。
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1", focus="l")]
[name="海伦娜"]算了，还有什么我没见过，你直接说吧。
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍德洛"]二楼的水已经齐膝深了，里面的家具都泡坏了。
[charslot(slot = "l", name = "avg_4104_coldst_1#8$1", focus="l")]
[name="海伦娜"]......那我柜子里的衣服呢？都还好吗？
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍德洛"]如果我没记错，你是喜欢红色的，对吧？
[charslot(slot = "l", name = "avg_4104_coldst_1#8$1", focus="l")]
[name="海伦娜"]还行吧......
[charslot(slot = "r", name = "avg_npc_1034_1#2$1", focus="r")]
[name="伍德洛"]嗯，那就好，管子里面爆出来的水是铁锈色的，我估计你之后所有衣服都是那个颜色了。
[charslot(slot = "l", name = "avg_4104_coldst_1#6$1", focus="l")]
[name="海伦娜"]......伍迪，所以你去了一趟楼上到底做了什么？
[dialog]
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_smashtable", volume=0.4)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍德洛"]都在这里了。
[charslot(slot = "l", name = "avg_4104_coldst_1#8$1", focus="l")]
[name="海伦娜"]啊......我差点把这箱子忘了，你从哪里翻出来的？
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍德洛"]还能在哪里？当然是衣柜，你就那几个藏东西的去处，也不难找。还有你床头柜上的几样东西，我一并塞进来了。
[dialog]
[charslot(slot = "l", name = "avg_4104_coldst_1#8$1", focus="l")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_open_box", volume=1)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_4104_coldst_1#11$1", focus="l")]
[name="海伦娜"]唔，还好，没有进水，看看这里面都有什么......
[name="海伦娜"]......保单在里面，今天的损失应该能用保险赔付，还有地契、房契......存折。
[charslot(slot = "r", name = "avg_npc_1034_1#5$1", focus="r")]
[name="伍德洛"]你还留着那存折？明知道里面的钱根本取不出来？
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1", focus="l")]
[name="海伦娜"]换了你，你会随手扔掉？
[charslot(slot = "r", name = "avg_npc_1034_1#2$1", focus="r")]
[name="伍德洛"]......
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1", focus="l")]
[name="海伦娜"]你看，你不是也懂吗？他那么多年攒下的已经不仅仅是钱了，那是心意。
[charslot(slot = "r", name = "avg_npc_1034_1#7$1", focus="r")]
[name="伍德洛"]啧，恋旧的家伙。
[charslot(slot = "l", name = "avg_4104_coldst_1#10$1", focus="l")]
[name="海伦娜"]我们都是老家伙了，伍迪，比起不可捉摸的未来，还是那些常年积攒下的点滴过往更加亲切。
[charslot(slot = "r", name = "avg_npc_1034_1#7$1", focus="r")]
[name="伍德洛"]不敢苟同。
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1", focus="l")]
[name="海伦娜"]......看哪，还有这本小说，放在床头，好久都没翻开过了。
[dialog]
[PlaySound(key="$d_avg_paper1", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_paper2", volume=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1034_1#10$1", focus="r")]
[name="伍德洛"]富家千金和牧场小子，千篇一律的俗套恋爱故事。
[charslot(slot = "l", name = "avg_4104_coldst_1#9$1", focus="l")]
[name="海伦娜"]伍迪......那么刻薄干什么？你就没什么好听的话吗？
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍德洛"]有啊，祝你明天去银行一切顺利。
[charslot(slot = "l", name = "avg_4104_coldst_1#6$1", focus="l")]
[name="海伦娜"]......你该庆幸，伍迪，我现在的脾气比年轻时好太多。你呢，你明天要去做什么？
[charslot(slot = "r", name = "avg_npc_1034_1#1$1", focus="r")]
[name="伍

... (全文27115字符)
```

### level_act28side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Background(image="42_g3_diner",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1038_1#8$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1035_1#9$1", duration=1, isblock=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1038_1#8$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1035_1#9$1", focus="l")]
[name="里昂"]♪她展开双臂，将我拥入怀♪
[charslot(slot = "r", name = "avg_npc_1038_1#8$1", focus="r")]
[name="迈尔斯"]♪从此她的双臂间，盛满我的家与梦♪
[charslot]
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]我还记得你们当时就这么聚在一起唱歌，唱得可真响亮啊......感觉那年冬日的雾气就是被你们的歌声驱散的。
[charslot(slot = "m", name = "avg_1034_jesca2_1#15$1")]
[name="杰西卡"]海伦娜女士，他们当时唱的就是刚刚这首歌吗？
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]哈哈，不止不止，他们会的歌可多了，矿厂里的矿工来自各地，用各种语言唱各地的歌。
[charslot(slot = "m", name = "avg_1034_jesca2_1#4$1")]
[name="杰西卡"]那......伍德洛先生也会唱歌吗？
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]他不怎么开口，大家聚在一起的时候，他要么喝酒，要么就像现在一样，埋头只顾吃。
[charslot(slot = "m", name = "avg_npc_1034_1#1$1")]
[name="伍德洛"]咳咳......海伦娜，把我带回来的那瓶香槟开了吧。
[charslot(slot = "m", name = "avg_4104_coldst_1#10$1")]
[name="海伦娜"]嗨，看我这记性，差点忘了。
[charslot(slot = "m", name = "avg_1034_jesca2_1#3$1")]
[name="杰西卡"]那个，迈尔斯先生他......
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]没关系，他说去吹吹风，那就是吹吹风。
[charslot(slot = "m", name = "avg_npc_1035_1#3$1")]
[name="里昂"]我们先把香槟打开，给他倒上一满杯，等他回来再让他喝！
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]那我就开了——
[dialog]
[charslot]
[PlaySound(key="$d_avg_decap", volume=1)]
[delay(time=1)]
瓶塞砰的一声弹射出去，金黄色的酒液和银白色的泡沫同时喷溅而出。随之而出的甜蜜酒香在室内蔓延，桌上众人的眼神不禁有些迷离。
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]给，杰西卡，你是今天的主角，第一杯先给你。
[charslot(slot = "m", name = "avg_1034_jesca2_1#4$1")]
[name="杰西卡"]谢谢......
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]然后是你，伍迪，多谢你帮杰西卡劝动了这头死犟死犟的驮兽。
[charslot(slot = "m", name = "avg_npc_1034_1#9$1")]
[name="伍德洛"]不谢。
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]这杯是迈尔斯的......这杯是我的......你的在最后，里昂，因为这么多人都替你操心。
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]应该的，应该的......
[charslot(slot = "m", name = "avg_npc_1035_1#2$1")]
[name="里昂"]说真的，我其实——
[musicvolume(volume=0.4, fadetime=2)]
[charslot(slot = "m", name = "avg_4104_coldst_1#2$1")]
[name="海伦娜"]有什么话你也该等迈尔斯回来再说，哪有你在屋子里感谢大家，倒把他一个人扔在外面的道理！
[charslot(slot = "m", name = "avg_npc_1035_1#9$1")]
[name="里昂"]说得是，说得是......
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[Delay(time=2.5)]
喧闹了一整晚的餐桌一时间安静下来，洒到桌上的香槟在看不见的暗处静静流淌。
流过碗碟。
[dialog]
[charslot(slot = "m", name = "avg_npc_1037_1#7$1", duration=1, isblock=true)]
[name="本尼"]那个......
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1")]
[name="杰西卡"]本尼，怎么了？
[dialog]
[charslot]
流过杯盘。
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]其实......我有些话想和大家说......
[charslot(slot = "m", name = "avg_npc_1035_1#3$1")]
[name="里昂"]我就说你小子今天怎么这么拘谨，原来酝酿了半天，是想抢你老爸在酒桌上的风头。
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]本尼，你的话不等迈尔斯回来再说吗？
[dialog]
[charslot]
流过空空的酒瓶。
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]不......我觉得，现在这样就好。
[name="本尼"]我......
[dialog]
[charslot]
一直流到桌边，滴在地上。
[dialog]
[PlaySound(key="$blooddrop", volume=1)]
[delay(time=1.5)]
啪。
[dialog]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[delay(time=1.5)]
[name="本尼"]我打算离开了。
[charslot(slot = "m", name = "avg_npc_1035_1#3$1")]
[name="里昂"]嗨，原来是嫌我们这些老家伙吵了。本尼，稍等一会儿，等迈尔斯回来，我们最后喝一轮，道个别——
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]不，我是说，我打算离开达维镇。
[charslot(slot = "m", name = "avg_npc_1035_1#3$1")]
[name="里昂"]这小子，滴酒未沾就醉了......
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]不，我很清醒。
[name="本尼"]我刚刚就一直想说......但是，再没机会了，我只能现在说。
[charslot(slot = "m", name = "avg_npc_1035_1#5$1")]
[name="里昂"]......
[dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1038_1#1$1", duration=1.5, isblock=true)]
[name="迈尔斯"]......怎么了？你们怎么突然这副样子？
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]迈尔斯，我......
[charslot(slot = "m", name = "avg_4104_coldst_1#5$1")]
[name="海伦娜"]本尼刚刚说要......离开达维镇......
[charslot(slot = "m", name = "avg_npc_1038_1#6$1")]
[name="迈尔斯"]什、什么......
[charslot(slot = "m", name = "avg_npc_1034_1#10$1")]
[name="伍德洛"]你从什么时候开始这么想的，本尼？
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]一年前我就在这么想了......
[name="本尼"]上个月，隔壁的赛琳娜女士找到我，说她在铸铁城的女儿找到了愿意途经此地的商队，她打算随着商队到女儿身边去了。
[name="本尼"]她问我愿不愿意同她一起离开，她觉得我很有天赋，在这里，它没法兑现。就算兑现，未来也无从施展。
[name="本尼"]她说......她不想看着我变成下一个西尔维娅。
[charslot(slot = "m", name = "avg_4104_coldst_1#11$1")]
[name="海伦娜"]生活费和学费怎么办？住的地方呢？
[charslot(slot = "m", name = "avg_npc_1037_1#1$1")]
[name="本尼"]都不用操心，铸铁城已经有几所寄宿中学愿意让我在那里就学，同时提供奖学金。
[charslot(slot = "m", name = "avg_npc_1038_1#7$1")]
[name="迈尔斯"]本尼，这么大的决定，你怎么现在才和我们商量......这不该啊。
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]抱歉，迈尔斯......
[charslot(slot = "m", name = "avg_npc_1034_1#1$1")]
[name="伍德洛"]迈尔斯，他没在和我们商量。
[charslot(slot = "m", name = "avg_npc_1034_1#2$1")]
[name="伍德洛"]他只是把他的决定说给我们听，只是这样而已。
[charslot(slot = "m", name = "avg_4104_coldst_1#5$1")]
[name="海伦娜"]......这是你深思熟虑后的决定吗，本尼？或许恢复航行后，地块上的情况就能好转，等到那个时候再做决定也不迟。
[charslot(slot = "m", name = "avg_npc_1037_1#1$1")]
[name="本尼"]我不想等了。
[name="本尼"]你们之所以愿意等待，笃信事情会有转机，是因为你们的记忆中有过这里最美好的样子。
[charslot(slot = "m", name = "avg_npc_1037_1#7$1")]
[name="本尼"]但我没有，从我记事起......这里就已经是一团糟了。
[name="本尼"]......我的养父为了这里苦苦挣扎，不惜投入生活中的一切，我的兄长代替他支撑家庭，将将成年便加入佣兵队赚钱补贴家用。
[name="本尼"]几年后......那些人把他的遗物寄回来，附上的信中没有任何解释，只有一句我们很遗憾。
[name="本尼"]他那时应该

... (全文23694字符)
```

### level_act28side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="42_g9_modernoffice",screenadapt="coverall")]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1040_1#11$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1040_1#11$1",focus="l")]
[name="黑钢情报小组成员"]......骚乱中两人死亡，四人重伤，轻伤数十人，十三家店铺与民居遭受抢劫，主街道上还有部分区域有小范围火灾爆发......
[PlaySound(key="$d_avg_telephonering", volume=0.6)]
[name="黑钢情报小组成员"]万幸，各小队已经迅速控制了局面。
[name="黑钢情报小组成员"]目前，在地块的重要设施及干道处，我们已经派驻了维持治安与秩序的佣兵小队。
[PlaySound(key="$d_avg_telephonering", volume=0.6)]
[name="黑钢情报小组成员"]请问我需要暂停汇报吗？
[charslot(slot = "right", name = "avg_npc_1036_1#7$1",focus="r")]
[name="“桥夹”克里夫"]先暂停吧。
[charslot(slot = "left", name = "avg_npc_1040_1#10$1",focus="l")]
[name="黑钢情报小组成员"]那请允许我先离开，等您通话结束，我再进来汇报。
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]没必要，一起听吧。
[dialog]
[PlaySound(key="$d_avg_ringoff")]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
[name="银行行长"]克里夫先生，抱歉在这个时候来电打扰。那笔准备金我们已经入库，感谢诸位一路押送。
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]您不必为此致谢，这些事都写在你我的合约之中。而且，比起电话，我更希望与您当面商议后续的拖拽事宜。
[charslot(slot = "m", focus = "n")]
[name="银行行长"]那您何时有空？明天下午？
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]可以，我的秘书会安排会面。
[charslot(slot = "m", focus = "n")]
[name="银行行长"]克里夫先生，我想多问一句，还请您不要介意。
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]请讲。
[charslot(slot = "m", focus = "n")]
[name="银行行长"]不知昨晚参与动乱的镇民，您......会如何处理？
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]现场抓获的暂时扣留在本舰，剩下的，我们还在追查中。
[charslot(slot = "m", focus = "n")]
[name="银行行长"]啧......那些混混之前就够让我们头痛了，自身资产情况糟糕，如今便想着劫掠别人。
[charslot(slot = "right", name = "avg_npc_1036_1#10$1",focus="r")]
[name="“桥夹”克里夫"]听起来，你对他们很熟悉？
[charslot(slot = "m", focus = "n")]
[name="银行行长"]是啊，都是银行负债名单上的老熟人了。
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]请问那份名单我们能看吗？
[charslot(slot = "m", focus = "n")]
[name="银行行长"]当然，要查的话，理应先从那些家伙查起。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g3_diner",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4104_coldst_1#1$1",duration=0.5)]
[delay(time=1)]
[name="海伦娜"]谢谢你昨晚把那家伙送过来，杰西卡。
[charslot(slot="m",name="avg_1034_jesca2_1#1$1")]
[name="杰西卡"]里昂先生还好吗？本尼离开了，连唯一保住的房子也在火灾里烧毁了，他......
[charslot(slot="m",name="avg_4104_coldst_1#2$1")]
[name="海伦娜"]他没说什么......替他处理过伤口后，他就睡着了。
[charslot(slot="m",name="avg_npc_1034_1#1$1")]
[name="伍德洛"]多亏他每天不回家，在大街上喝得醉醺醺的，所以才逃过这一劫。
[charslot(slot="m",name="avg_4104_coldst_1#2$1")]
[name="海伦娜"]够了，闭嘴，伍迪。
[charslot(slot="m",name="avg_npc_1034_1#1$1")]
[name="伍德洛"]......
[charslot(slot="m",name="avg_4104_coldst_1#5$1")]
[name="海伦娜"]算了，我上去看看里昂。
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "-150,0",duration = 0.8)]
[charslot(duration=0.8)]
[delay(time=2)]
[charslot]
[charslot(slot = "left", name = "avg_npc_1034_1#1$1",focus="l")]
[charslot(slot = "right", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="伍德洛"]杰西卡......你昨天不是在地块外迎接本舰吗？为什么突然回来了？
[charslot(slot = "right", name = "avg_1034_jesca2_1#1$1",focus="r")]
[name="杰西卡"]伍德洛先生，其实当时......我有事想找您，看到里昂先生家上方有烟升起，就先去了那里。
[charslot(slot = "left", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]为了什么找我？
[charslot(slot = "right", name = "avg_1034_jesca2_1#14$1",focus="r")]
[name="杰西卡"]其实......来地块之后，我就一直在为本舰的到来提心吊胆。
[charslot(slot = "left", name = "avg_npc_1034_1#10$1",focus="l")]
[name="伍德洛"]那是你们公司，来了不是好事吗？那些你和队友们一直觉得棘手的问题，现在有一整个基地来接手。
[charslot(slot = "right", name = "avg_1034_jesca2_1#1$1",focus="r")]
[name="杰西卡"]可......对地块上的大家来说，黑钢的到来并不是什么好事。
[name="杰西卡"]移动平台造价不菲，是极为稀缺的资源，政府不会放任它们废弃，大概率会翻修地块，将其整合升级为更大的聚居点。
[charslot(slot = "left", name = "avg_npc_1034_1#10$1",focus="l")]
[name="伍德洛"]听着仍然是好事。
[charslot(slot = "right", name = "avg_1034_jesca2_1#9$1",focus="r")]
[name="杰西卡"]可生活在上面的居民，政府却并不希望他们留在地块上，所以想尽办法让他们主动离开......
[charslot(slot = "left", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]......
[charslot(slot = "right", name = "avg_1034_jesca2_1#14$1",focus="r")]
[name="杰西卡"]所以银行来了。
[name="杰西卡"]通过大量的贷款合同与对赌协议，银行收回了不少没落平台的资产，也将大批人送去了拓荒地。
[name="杰西卡"]这样的手段合法合理......挑不出一丝不对。
[charslot(slot = "left", name = "avg_npc_1034_1#10$1",focus="l")]
[name="伍德洛"]真会有人愿意乖乖吃亏吗？
[charslot(slot = "right", name = "avg_1034_jesca2_1#10$1",focus="r")]
[name="杰西卡"]究竟有没有人被迫吃亏......您在达维镇待的时间更长，您比我更清楚。
[charslot(slot = "left", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]呵，这里还是有几块硬骨头不好啃的。
[charslot(slot = "right", name = "avg_1034_jesca2_1#11$1",focus="r")]
[name="杰西卡"]所以......像黑钢这样的佣兵公司来了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g9_modernoffice",screenadapt="coverall")]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="n")]
[charslot(slot = "left", name = "avg_npc_1040_1#10$1",focus="n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="银行行长"]彻查清楚后呢？克里夫先生，您难道打算将他们一直关押在巴伦基地吗？
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]试问在此之前你们是怎么做的？
[charslot(slot = "m", focus = "n")]
[name="银行行长"]地块上还有警员的时候，那些家伙会被送上去往拓荒地的车队。
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]那我们依例行事就是。
[charslot(slot = "m", focus = "n")]
[name="银行行长"]那辛苦诸位了。
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]小事而已，期待明天的会面。
[charslot(slot = "m", focus = "n")]
[name="银行行长"]克里夫先生，稍等，我这里还有个小小的请求希望您能答应。黑钢能否增派一些在银行的安保力量？
[charslot(slot = "right", name = "avg_npc_1036_1#7$1",focus="r")]
[name="“桥夹”克里

... (全文24331字符)
```

### level_act28side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="42_g4_bank",screenadapt="coverall")]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1039_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1039_1#3$1")]
[name="西尔维娅"]......都这么晚了，怎么外面还有人。
[Dialog]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1039_1#6$1")]
[name="西尔维娅"]那是......杰西卡小姐？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[charslot(slot="r",name="avg_1034_jesca2_1#9$1")]
[Background(image="42_g7_sonwydowntown_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=0.5)]
[charslot(slot = "left", name = "avg_npc_1039_1#1$1",posfrom = "-150,0", posto = "0,0",duration = 0.8)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_1039_1#1$1",focus="l")]
[name="西尔维娅"]杰西卡小姐，你这个时候来银行做什么？
[charslot(slot="r",name="avg_1034_jesca2_1#10$1",focus="r")]
[name="杰西卡"]我......呼、呼......我有事想找你们！
[charslot(slot = "left", name = "avg_npc_1039_1#1$1",focus="l")]
[name="西尔维娅"]至、至少......进来再说吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g4_bank",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_higheldshosfts", volume=0.5)]
[charslot(slot="m",name="avg_npc_1041_1#1$1",duration=1)]
[delay(time=1.5)]
[name="银行经理"]西尔维娅，怎么回事？我不是说了晚上不要打开大门吗，这几天黑钢的人在外面......
[dialog]
[delay(time=1)]
[name="银行经理"]啊，原来是您啊，杰西卡小姐。
[name="银行经理"]不知这么晚造访，您有何贵干？
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]别......别赶他们走！
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]赶他们走？我们赶谁了？
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]那些欠债的居民，别让黑钢赶他们走！
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]......这是谁的意思？克里夫先生的？
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]我的，我自己的意思！
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]我没听错吧，杰西卡小姐？开玩笑也要有个度。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]这不是开玩笑！如果你们要找人还债，我、我来替他们还，能不能过了冬天再让他们离开？现在去拓荒地，是在让他们去送死啊！
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]在银行，能说话的不是一个异想天开的佣兵，是实实在在的金券。
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]金券我有！这不是异想天开，我说了要替他们还，就会替他们还！
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]抱歉，银行不接待妄想症患者——
[charslot(slot="m",name="avg_1034_jesca2_1#12$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杰西卡"]我是伯尼·布林雷的女儿，伯尼·布林雷......雷神工业的负责人兼大股东！
[dialog]
[charslot(slot="m",name="avg_1034_jesca2_1#3$1")]
[delay(time=1.5)]
[charslot]
话才说出口，杰西卡便愣住了，自来到黑钢后，无论面对怎样的挫折与困难，她都不会指望自己的父亲与家族。
那是她一贯的坚持，她不希望她的姓氏给她带来特殊的优待。
可在刚刚，她搬出了父亲的名字，搬出了家徽上的姓氏。
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]伯尼·布林雷？
[name="银行经理"]那你倒也真是位大人物了，杰西卡·布林雷小姐。
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]你不用挖苦我，女士，告诉我吧，到底要多少钱？
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]嗯......一时间我也拿不出个确切数字，不过没关系，西尔维娅在这里，她一向对数字很敏感。
[name="银行经理"]愣着干什么，西尔维娅，告诉布林雷小姐啊。
[charslot(slot="m",name="avg_npc_1039_1#8$1")]
[name="西尔维娅"]......杰西卡小姐，我......
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]西尔维娅，她是布林雷家的孩子，对她而言那应该只是个小数字。
[charslot(slot="m",name="avg_npc_1039_1#8$1")]
[name="西尔维娅"]这、这样不好......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]告诉她，西尔维娅！
[charslot(slot="m",name="avg_npc_1039_1#8$1")]
[name="西尔维娅"]迄今为止......达维镇所有人的债务约计......两亿七千六百万金券，到明年春天的话，粗略算下来，一共需要偿付......
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]要多少？
[charslot(slot="m",name="avg_npc_1039_1#2$1")]
[name="西尔维娅"]两千八百四十五万金券。
[charslot(slot="m",name="avg_1034_jesca2_1#3$1")]
[name="杰西卡"]两千......八百万？
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]这点小钱，换大家在地块上安安稳稳多待三个月，很划算吧，布林雷小姐？
[dialog]
[charslot(slot="m",name="avg_1034_jesca2_1#14$1")]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]怎么又不说话了？
[charslot(slot="m",name="avg_1034_jesca2_1#11$1")]
[name="杰西卡"]我、我手头暂时没有那么多，但我、我可以尽数拿出来......
[charslot(slot="m",name="avg_npc_1041_1#1$1")]
[name="银行经理"]两千八百四十五万......看来那些有家族信托基金的大小姐也没办法一次性拿出这么多钱啊？
[name="银行经理"]倒也是新知识。
[charslot(slot="m",name="avg_1034_jesca2_1#9$1")]
[name="杰西卡"]我......我......不......
[charslot(slot="m",name="avg_npc_1039_1#8$1")]
[name="西尔维娅"]杰西卡......
[charslot(slot="m",name="avg_1034_jesca2_1#10$1")]
[name="杰西卡"]西尔维娅，我、我......
[charslot(slot="m",name="avg_npc_1039_1#8$1")]
[name="西尔维娅"]你......不是达维镇的人，为大家做到这个地步......真的没有必要。
[name="西尔维娅"]杰西卡，听我说，你先回去吧......就、就算你用钱能帮这一次，那下一次、下下一次......又要怎么办呢？
[charslot(slot="m",name="avg_1034_jesca2_1#7$1",focus="n")]
杰西卡哆嗦着嘴唇，一句话也说不出来。
她知道，西尔维娅并非在挖苦自己，只是在陈述事实。
那串躺在她账户里的数字，就算能保她一生无忧，但于这个地块上的人而言，就连一个月的安稳也无法保障。
她想起父亲曾经语重心长地提醒自己，做事要权衡利弊，要量力而为。
她学不会，所以总是一事无成。
[stopmusic(fadetime=4)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g9_modernoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[name="秘书"]克里夫先生，您在吗？
[charslot(slot="m",name="avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]在，怎么了？
[charslot(slot = "m", focus = "n")]
[name="秘书"]克里夫先生，那个人来了，请问您方便会见吗？
[charslot(slot="m",name="avg_npc_1036_1#7$1")]
[name="“桥夹”克里夫"]......
[charslot(slot = "m", focus = "n")]
[dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[name="秘书"]克里夫先生？
[charslot(slot="m",name="avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]嗯，我听到了

... (全文20023字符)
```

### level_act28side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="42_g7_sonwydowntown_n",screenadapt="coverall")]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot="m",name="avg_106_franka_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_106_franka_1#9$1")]
[name="芙兰卡"]我们真的这么早就要来吗？现在银行外面一个人也没有啊。
[charslot(slot="m",name="avg_1034_jesca2_1#1$1")]
[name="杰西卡"]我有薄荷糖可以提神。
[charslot(slot="m",name="avg_106_franka_1#3$1")]
[name="芙兰卡"]谢谢你，但我想薄荷糖应该起不了什么用，来，优等生，你来掐我一把。
[charslot(slot="m",name="avg_107_liskam_1#1$1")]
[name="雷蛇"]啧......
[charslot(slot="m",name="avg_106_franka_1#9$1")]
[CameraShake(duration=0.3,xstrength=10, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="芙兰卡"]痛！
[charslot(slot="m",name="avg_106_franka_1#3$1")]
[name="芙兰卡"]开工吧。朋友们，都清醒点！哎，说的就是你！
[dialog]
[charslot(slot="m",name="avg_npc_1045_1#1$1")]
[Delay(time=0.5)]
[name="黑钢佣兵小队成员"]哈......欠——抱、抱歉，芙兰卡小姐。
[charslot(slot="m",name="avg_106_franka_1#1$1")]
[name="芙兰卡"]好啦，接下来认真听。
[name="芙兰卡"]这间银行总共有四个出口，贝尼，你带四个人守在后门，小查，右边就交给你和安妮了。
[charslot(slot="m",name="avg_npc_1045_1#1$1")]
[name="黑钢佣兵小队成员"]收到！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "150,0",duration = 0.6)]
[charslot(duration=0.6)]
[Delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_107_liskam_1#1$1")]
[name="雷蛇"]铜板，你和硬币去车库门。
[charslot(slot="m",name="avg_npc_1045_1#1$1")]
[name="黑钢佣兵小队成员"]收到！
[dialog]
[charslot(slot = "m",posfrom = "0,0", posto = "-150,0",duration = 0.6)]
[charslot(duration=0.6)]
[Delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_107_liskam_1#1$1")]
[name="雷蛇"]剩下的人，与我们三个一起留在正门......
[dialog]
[charslot]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1042_1#1$1",duration=1)]
[delay(time=1.5)]
[name="面色不快的地块居民"]咳咳，打扰了，女士，麻烦问下......
[name="面色不快的地块居民"]你们今天一天都会在这里吗？
[charslot(slot="m",name="avg_107_liskam_1#1$1")]
[name="雷蛇"]呃，是的，先生......不过我们只是站岗值勤，不会影响大家办理业务。
[charslot(slot="m",name="avg_npc_1042_1#1$1")]
[name="面色不快的地块居民"]办理业务？前几天我在这里签了一份拓荒协议，那是我最后一份业务。
[charslot(slot="m",name="avg_107_liskam_1#8$1")]
[name="雷蛇"]那您是......？
[charslot(slot="m",name="avg_npc_1042_1#1$1")]
[name="面色不快的地块居民"]嗯......算是给他们的服务质量打个评价吧。
[name="面色不快的地块居民"]（倒立大拇指）
[name="面色不快的地块居民"]噗——
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1036_1#1$1")]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1")]
[Background(image="42_g9_modernoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]这颗子弹......是你托杰西卡带来的吗？
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]嗯，几年前我在维多利亚的一个古董店见到了它。
[name="“桥夹”克里夫"]难怪你当时把营地翻了个遍也没找到，现在想应该是某个军官把那把铳偷偷带去了维多利亚。
[name="“桥夹”克里夫"]如今铳已经没了下落，这颗子弹是他仅存的遗物了。
[charslot(slot = "l", name = "avg_npc_1034_1#2$1",focus="l")]
[name="伍德洛"]早告诉那家伙不要在铳上搞那么花里胡哨的纹样了......这颗子弹你为什么不自己留着？
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]比起我，你才应该是那个保存它的人。
[charslot(slot = "l", name = "avg_npc_1034_1#10$1",focus="l")]
[name="伍德洛"]你是觉得愧疚吗？
[charslot(slot = "r", name = "avg_npc_1036_1#7$1",focus="r")]
[name="“桥夹”克里夫"]毕竟朋友一场，最后如此收场，我也很难过。
[charslot(slot = "l", name = "avg_npc_1034_1#5$1",focus="l")]
[name="伍德洛"]那你的愧疚与难过有用吗？
[charslot(slot = "r", name = "avg_npc_1036_1#10$1",focus="r")]
[name="“桥夹”克里夫"]你想要什么，伍迪？
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]唤回你的手下，停止驱赶居民。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]伍迪，就算黑钢离开，政府还会派其他的佣兵公司来，结局还是一样。
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]你本可以拒绝这项任务的，是吗？
[charslot(slot = "r", name = "avg_npc_1036_1#2$1",focus="r")]
[name="“桥夹”克里夫"]黑钢国际虽说是“国际”，可总部毕竟是在哥伦比亚，政府委派的任务，我们没有什么拒绝的权力。
[charslot(slot = "l", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]原来你也有要夹着尾巴做人的时候。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]今时不同往日了，在哥伦比亚政府眼里，我们这些武夫比不过那些特里蒙的精尖人才。
[charslot(slot = "l", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]......
[name="伍德洛"]告诉我，大老板，在这份与银行还有政府的合同里，黑钢能得到什么？
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]这并不是份长久的合同，伍迪。
[name="“桥夹”克里夫"]政府提出要求，我们照做，事后拿报酬，除此外......我并不关心，也不容我关心。
[charslot(slot = "l", name = "avg_npc_1034_1#7$1",focus="l")]
[name="伍德洛"]我记得还在拉特兰时，你总会和我讲很多，大到国家间的摩擦，小到人群中的矛盾......那些因此而受苦的人们永远是你的话题。
[charslot(slot = "r", name = "avg_npc_1036_1#7$1",focus="r")]
[name="“桥夹”克里夫"]那都是很久远的事了，伍迪，我记不清了。
[charslot(slot = "l", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]但我记得很清楚，就在那段从图书馆到学生宿舍的路上，你告诉我，强大的人保护自己，伟大的人捍卫他人。
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]怎么到现在，亲眼看到了那些人，你却只会不咸不淡地讲，不容关心，那便不关心了。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]伍迪，我们都老了，能关心的东西非常有限。
[charslot(slot = "l", name = "avg_npc_1034_1#5$1",focus="l")]
[name="伍德洛"]是啊，我们都老了，还能关心的东西剩得不多......剩下的，都是最重要的东西了。
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]我这一把残破的老骨头，保住地块上所有人是不可能了，但身边的人......我会死死守着。
[name="伍德洛"]我发誓，如果他们因为你的到来而受到伤害，那我会把这颗子弹原封不动地还给你。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]......我衷心希望，事情不会发展到那一步，伍迪。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=2)]
[Background(image="42_g6_sonwydowntown_d",screenadapt="coverall")]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[StopSound(channel="bgs", fadetime=5)]
[charslot(slot="m",name="avg_106_franka_1#1$1")]
[name="芙兰卡"]队长，人越聚越多了......要拉封锁线吗？
[charslot(slot="m",name="avg_107_liskam_1#1$1")]
[name="雷蛇"]还不到那一步。我们并不清楚人群的意图，贸然行事只会更

... (全文17400字符)
```

### level_act28side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[name="访谈嘉宾"]广袤的拓荒区还潜藏着相当的发展潜力，我们衷心欢迎那些才华得不到施展的公民前往拓荒区。
[name="访谈嘉宾"]而对那些坚守自己家乡的人，我们也为他们准备了地块再开发计划。
[name="主持人"]地块再开发计划？
[name="访谈嘉宾"]对于一些产业落后的地块，我们制定了令其焕然一新的再开发计划。州政府吸引的高科技企业将利用这些宝贵的地块发展高新产业。
[name="主持人"]令人振奋的消息！我想这些地块的居民已经迫不及待要见证光明的未来了。
[name="访谈嘉宾"]州政府已经为数个地块制定了再开发计划，例如贝斯伍德镇、戴德霍斯镇、达维镇......
[name="主持人"]不知道这些地块上有没有我们的观众呢？这对他们来说应该是新年的第一个好消息！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g9_modernoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_176",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1036_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "left", name = "avg_npc_176",focus="l")]
[name="银行行长"]克里夫先生，一想到此时能有机会亲眼目睹巴伦基地的壮观，我的心情就很激动。
[charslot(slot = "r", name = "avg_npc_1036_1#8$1",focus="r")]
[name="“桥夹”克里夫"]您太客气了......和贵行这样的企业合作才是我们的幸运。
[charslot(slot = "left", name = "avg_npc_176",focus="l")]
[name="银行行长"]哈哈，克里夫先生，如果可能的话，有些在拓荒地的业务，我们依然想要继续双方的合作。
[charslot(slot = "r", name = "avg_npc_1036_1#8$1",focus="r")]
[name="“桥夹”克里夫"]这也正是我们的想法。
[charslot(slot = "left", name = "avg_npc_176",focus="l")]
[name="银行行长"]和您谈话的过程总是很愉快，希望这种状态能一直保持下去。毕竟拖拽也是个漫长的过程，直到春天彻底雪融，我们才能互道分别。
[charslot(slot = "r", name = "avg_npc_1036_1#8$1",focus="r")]
[name="“桥夹”克里夫"]那可真的是太短暂了，我会为此感到遗憾——
[Stopmusic(fadetime=2)]
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杰西卡"]克里夫先生！克里夫先生！
[PlaySound(key="$doorknockquite")]
[name="杰西卡"]克里夫先生，请开开门，我有很紧急的事情要向你汇报。
[charslot(slot = "r", name = "avg_npc_1036_1#8$1",focus="r")]
[name="“桥夹”克里夫"]如果您有任何合作上的需要，可以随时联系——
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杰西卡"]开开门，求你了，事情真的很紧急！克里夫先生！！
[charslot(slot = "left", name = "avg_npc_176",focus="l")]
[name="银行行长"]......看来您有些要紧事？
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]请您稍等。
[dialog]
[charslot]
[playsound(key="$d_avg_glassdooropen")]
[charslot(slot = "m", name = "avg_1034_jesca2_1#11$1",duration=1)]
[delay(time=2)]
[playMusic(key="$formal_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1036_1#6$1")]
[name="“桥夹”克里夫"]杰西卡，你来做什么？谁让你在我门口大吼大叫的？
[charslot(slot = "m", focus = "n")]
[name="秘书"]抱歉，克里夫先生，杰西卡小姐要汇报的事情的确紧急。
[charslot(slot = "m", name = "avg_npc_1036_1#6$1")]
[name="“桥夹”克里夫"]那就快说。
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1")]
[name="杰西卡"]那位先生......
[charslot(slot = "m", name = "avg_npc_176")]
[name="银行行长"]克里夫先生，请问我可以借用一下您的洗手间吗？
[charslot(slot = "m", name = "avg_npc_1036_1#8$1")]
[name="“桥夹”克里夫"]请用。
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n",volume=0.7)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",duration=0.5)]
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]到底出了什么事，要你来敲我的门？
[charslot(slot = "l", name = "avg_1034_jesca2_1#11$1",focus="l")]
[name="杰西卡"]银行拿着州政府的授权书，要求我们对人群动手。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]那你们动手了吗？
[charslot(slot = "l", name = "avg_1034_jesca2_1#10$1",focus="l")]
[name="杰西卡"]至少在我离开时还没有，现在的情况我、我不知......
[charslot(slot = "l", name = "avg_1034_jesca2_1#11$1",focus="l")]
[name="杰西卡"]不......
[name="杰西卡"]不，我们不会动手。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]好，我知道了，出去吧。
[charslot(slot = "l", name = "avg_1034_jesca2_1#10$1",focus="l")]
[name="杰西卡"]那些居民要怎么办？
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]这和你没有关系。
[charslot(slot = "l", name = "avg_1034_jesca2_1#10$1",focus="l")]
[name="杰西卡"]但您至少可以......
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]如果你听不懂，我可以再说得更明确一点。
[charslot(slot = "r", name = "avg_npc_1036_1#10$1",focus="r")]
[name="“桥夹”克里夫"]这和你、和我，都没有关系。
[charslot(slot = "l", name = "avg_1034_jesca2_1#11$1",focus="l")]
[name="杰西卡"]是吗......？
[name="杰西卡"]那什么与您有关系呢......银行回报给您的高额酬劳，军方额外赋予您的特殊权力？还是肆意将别人踩在脚下时，给您的那种......
[name="杰西卡"]高人一等的快感？
[charslot(slot = "m", focus = "n")]
克里夫眯起眼睛，上下打量着眼前突然有些陌生的佣兵。
[charslot(slot = "r", name = "avg_npc_1036_1#2$1",focus="r")]
[name="“桥夹”克里夫"]我九十多岁了，不会那么轻易就感到快乐，杰西卡。
[charslot(slot = "l", name = "avg_1034_jesca2_1#11$1",focus="l")]
[name="杰西卡"]那为什么呢......与那些人为伍您能得到什么呢？
[name="杰西卡"]我很难不为此感到疑惑，在我看来......您为了得到那些，几乎丧失了一切人性。
[charslot(slot = "r", name = "avg_npc_1036_1#10$1",focus="r")]
[name="“桥夹”克里夫"]人性......这词对我来说是有些遥远了。作为黑钢这家佣兵公司的老板，那些美好的词汇有什么用？
[name="“桥夹”克里夫"]反倒是你，杰西卡小姐，如果你那样看重这些品质......那你来黑钢做什么呢？
[charslot(slot = "l", name = "avg_1034_jesca2_1#10$1",focus="l")]
[name="杰西卡"]我......
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]我记得你父亲曾经和我讲过，你留在这里是想解决一些问题，保护一些东西......
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]是......
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]既然如此，你为什么不去做警察、法官或者治安官？再不济入伍也可以，做个士兵保家卫国不好吗？
[name="“桥夹”克里夫"]可你选择了做佣兵，你选择了一份用武力换取金钱的工作，一份伴随着杀戮与暴力的工作，一份称不上光彩也得不了荣誉的工作。
[name="“桥夹”克里夫"]你也不缺钱，杰西卡，那你到底是为了什么呢？
[charslot(slot = "l", name = "avg_1034_jesca2_1#14$1",focus="l")]
[name="杰西卡"]......
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]如果你没想清楚，我可以作为过来人，给你一个答案。
[charslot(slot = "l", name = "avg_1034_jesca2_1#11$1",focus="l")]
[name="杰西卡"]野心......为了我自己的野心，为了证明我自己不比哥哥姐姐差，为了证明我不是家族里的......平庸之辈。
[name="杰西卡"]所以我来到了这里。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹

... (全文16424字符)
```

### level_act28side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[playsound(key="$d_avg_snowstormlp", loop=true, channel="b",volume=0)]
[SoundVolume(volume=0.4, fadetime=3,channel="b")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1043_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1042_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(duration=1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1042_1#1$1",duration = 1)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1042_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(duration=0.5)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_4105_almond_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_1034_jesca2_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "l",posfrom = "0,0", posto = "-50,0",duration = 1,afrom=1,ato=0)]
[charslot(slot = "r",posfrom = "0,0", posto = "50,0",duration = 1,afrom=1,ato=0)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1038_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot]
新年已过，但达维镇的风雪依然冰冷刺骨，不带一丝暖意。
站在地块外等车的人群中间，迈尔斯迷迷糊糊地想，在寒风里等车，似乎是很久以前的事了。
[charslot(slot="m",name="avg_4105_almond_1#2$1")]
[name="罗拉"]老爷子，你们要去的拓荒地，到底是个什么样的地方？
[charslot(slot="m",name="avg_npc_1038_1#8$1")]
[name="迈尔斯"]......至少应该比达维镇暖和。
[name="迈尔斯"]别替我担心了，他们至少还算留了点情面，让我能和老邻居们埋在一起。
[charslot(slot="m",name="avg_1034_jesca2_1#9$1")]
[name="杰西卡"]抱歉......抱歉......
[charslot(slot="m",name="avg_npc_1038_1#8$1")]
[name="迈尔斯"]孩子，既然一切都已经改变不了了，不如想想别的事情，别钻这个牛角尖。
[charslot(slot="m",name="avg_npc_1038_1#2$1")]
[name="迈尔斯"]比如，我刚刚想起来，上次这么等车，还是去别的移动城市给我小妹妹奔丧那次。
[name="迈尔斯"]也是这么冷的天，海伦娜、伍德洛、里昂，三个人陪我一起等车队来。
[charslot(slot="m",name="avg_npc_1038_1#8$1")]
[name="迈尔斯"]我拿着海伦娜餐厅花瓶里攒起来的花束，披着里昂借我的旧礼服，冻了好几个小时。
[name="迈尔斯"]说来也怪，我连等车那天伍德洛胡子多长都记得清清楚楚，可上了车之后，一切都模模糊糊的，好像隔着一层毛玻璃似的。
[charslot(slot="m",name="avg_npc_1038_1#10$1")]
[name="迈尔斯"]我好像去了很大的移动城市，又觉得那里还没达维镇大；我好像哭了一场，又好像没哭出来......
[charslot(slot="m",name="avg_npc_1038_1#6$1")]
[name="迈尔斯"]再之后，就只剩我从回达维镇的车上下来，他们把我扶下车的事了。
[charslot(slot="m",name="avg_npc_1038_1#8$1")]
[name="迈尔斯"]之后的事我反而又都能记起来了，我去海伦娜那儿喝了不少酒，醉得很厉害，连那天晚上的醉话我还记得一清二楚......
[charslot(duration=1)]
[dialog]
[playsound(key="$d_avg_truckengine", loop=true, channel="a",volume=0)]
[SoundVolume(volume=0.6, fadetime=3,channel="a")]
[Delay(time=3)]
[name="车队首领"]往拓荒地去的车队到了！达维镇的人，开始上车了！
[SoundVolume(volume=0, fadetime=1,channel="b")]
[StopSound(channel="a", fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[delay(time=1)]
“我最疼的小妹妹也没了，从此之后，我就和达维镇绑死在一起了，妈的。”
“里昂，听见了吗，我要在地块上老死！到那时候......”
[dialog]
[charslot(slot="m",name="avg_npc_1035_1#2$1",focus="n")]
[Background(image="42_g3_diner",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1035_1#4$1")]
[name="里昂"]迈尔斯，别以为我记不住！
[charslot(slot="m",name="avg_npc_1035_1#6$1")]
[name="里昂"]你说：“到那时候，麻烦你把我推进动力炉里，我倒要看看自己的骨灰......能不能呛得达维镇......打个喷嚏......”
[PlaySound(key="$d_avg_plateplace")]
[charslot(slot = "m", focus = "n")]
[CameraShake(duration=0.2, xstrength=20, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=false)]
工程师仰起头，又往嘴里灌了一大口。
[charslot(slot="m",name="avg_npc_1035_1#6$1")]
[name="里昂"]你刚说完，达维镇还没怎么样，我先打了个惊天动地的喷嚏。
[charslot(slot="m",name="avg_npc_1035_1#3$1")]
[name="里昂"]哈哈，哈哈哈......
[charslot(slot="m",name="avg_npc_1035_1#6$1")]
[name="里昂"]当年谁也没笑，谁都笑不出来，可我现在觉得这事真他妈滑稽，你不觉得吗？
[charslot(slot="m",name="avg_npc_1035_1#7$1")]
[name="里昂"]别不说话呀！喝，迈尔斯，喝！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_snow_2",screenadapt="coverall")]
[SoundVolume(volume=0.4, fadetime=2,channel="b")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_snowrun")]
[charslot(slot = "r", name = "avg_npc_1034_1#1$1",duration=1)]
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1",duration=1)]
[delay(time=1.6)]
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1",focus="l")]
[name="海伦娜"]抱歉......我们来迟了。
[charslot]
[charslot(slot="m",name="avg_1034_jesca2_1#1$1")]
[name="杰西卡"]伍德洛先生，海伦娜女士......里昂先生呢？
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#2$1",focus="l")]
[charslot(slot = "r", name = "avg_npc_1034_1#10$1",focus="l")]
[name="海伦娜"]我们临出门之前，他说自己只需要一些时间，想通了会过来的......说完就又给自己开了一瓶。
[charslot(slot = "r", name = "avg_npc_1034_1#10$1",focus="r")]
[name="伍德洛"]......可我们哪还有时间。
[charslot]
[charslot(slot="m",name="avg_npc_1038_1#3$1")]
[name="迈尔斯"]没什么，这对他......或许也算好事。
[dialog]
[charslot(slot = "m", focus = "n")]
[SoundVolume(volume=1, fadetime=1,channel="b")]
[delay(time=1.5)]
[SoundVolume(volume=0.5, fadetime=1,channel="b")]
[charslot(slot="m",name="avg_npc_1038_1#10$1")]
[name="迈尔斯"]嘶，这鬼天气......怎么就这么冷！
[charslot(slot="m",name="avg_npc_1034_1#1$1")]
[name="伍德洛"]等上了车，你就可以和这里的鬼天气说再见了。
[charslot(slot="m",name="avg_1034_jesca2_1#3$1")]
[name="杰西卡"]伍德洛先生！
[charslot(slot="m",name="avg_npc_1038_1#1$1")]
[name="迈尔斯"]他没说错。
[charslot(slot="m",name="avg_1034_jesca2_1#9$1")]
[name="杰西卡"]抱歉......
[charslot(slot="m",name="avg_npc_1038_1#7$1")]
[name="迈尔斯"]唉，杰西卡，你真的不用再道歉了。这件事里，银行有错，黑钢有错，就连我们也有不对的地方，唯独你......你没做错任何事情。
[name="迈尔斯"]所以，别自责了，毕竟我们从一开始，就不指望你能做到什么事情——
[charslot(slot = "m", focus = "n")]
迈尔斯立刻意识到自己的失言，他刚想解释什么，可车队首领已经拉住了他的手臂。
[charslot]
[playsound(key="$d_avg_truckengine", loop=true, channel="a",volume=0.6)]
[name="车队首领"]老头儿，有什么话也不该留到现在再说，就差你一个了，赶紧上车！
[charslot(slot="m",name="avg_npc_1038_1#6$1")]
[name="迈尔斯"]杰西卡，我......
[charslot]
[name="车队首领"]再拖下去，在荒地上遇见锈锤或者天灾什么的，到时候你负责吗？
[name="车队首领"]走了！
[dialog]
[PlaySound(key="$d_avg_snowbootwalk")]
[charslot(slot="m",name="avg_npc_1038_1#1$1")]
[charslot(duration=1)]
[delay(time=1.5)]
[St

... (全文20110字符)
```

### level_act28side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[warp(name="chiyu01")]
[Dialog]
[Delay(time=1)]
[Background(image="42_g10_blacksteelarmory",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_106_franka_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="芙兰卡"]全队整装完毕，随时可以出发回到本舰。
[charslot(slot = "m", name = "avg_107_liskam_1#7$1")]
[name="雷蛇"]杰西卡呢，还是联系不上？
[charslot(slot = "m", name = "avg_4105_almond_1#9$1")]
[name="罗拉"]她的通讯器......又坏了。
[charslot(slot = "m", name = "avg_106_franka_1#9$1")]
[name="芙兰卡"]一次行动里坏两次，哪有这么巧的事？她到底在干什么？
[charslot(slot = "m", name = "avg_4105_almond_1#10$1")]
[name="罗拉"]......
[dialog]
[charslot]
[PlaySound(key="$dooropenquite",volume=1)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_4105_almond_1#11$1")]
[name="罗拉"]杰西卡，你终于回来了！
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]......对不起。
[charslot(slot = "m", name = "avg_106_franka_1#3$1")]
[name="芙兰卡"]没什么，罗拉已经把你的行李都打包好了。
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]不......我......
[charslot(slot = "m", name = "avg_1034_jesca2_1#10$1")]
[name="杰西卡"]我来向大家......告别。
[charslot(slot = "m", name = "avg_106_franka_1#9$1")]
[name="芙兰卡"]告别？
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]你申请临时脱队？
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]......算是吧。
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]临时脱队的理由？
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$1")]
[name="杰西卡"]一些私事，我必须去做的私事。
[charslot(slot = "m", name = "avg_107_liskam_1#1$1")]
[name="雷蛇"]你要走多长时间？
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]我不知道，或许一周，或许一年......
[charslot(slot = "m", name = "avg_107_liskam_1#4$1")]
[name="雷蛇"]杰西卡，你还清醒吗？怎么可能有人给你批一整年的临时脱队？
[charslot(slot = "m", name = "avg_1034_jesca2_1#10$1")]
[name="杰西卡"]如果临时脱队不行，那我......我可以申请退队吗？
[charslot(slot = "m", name = "avg_106_franka_1#5$1")]
[name="芙兰卡"]退队？！
[charslot(slot = "m", name = "avg_1034_jesca2_1#9$1")]
[name="杰西卡"]......
[charslot(slot = "m", name = "avg_106_franka_1#4$1")]
[name="芙兰卡"]我懂了。你一开始就说了，你是来告别的，告别用不着申请。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_107_liskam_1#4$1")]
[delay(time=1)]
[name="雷蛇"]杰西卡，我不知道到底是什么事让你突然这么想，但我必须提醒你，离开小队，你在黑钢的一切努力都很可能会付诸流水。
[name="雷蛇"]你要做的事情，值得你用过去的努力做交换吗？
[charslot(slot = "m", name = "avg_1034_jesca2_1#14$1")]
[name="杰西卡"]......
[MusicVolume(volume=0.4, fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="bg_labcorridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",duration=1)]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",focus="r")]
[name="里昂"]这是矿厂剩的最后一些炸药了，一起拿出来吧。
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]嗯。
[dialog]
[charslot(slot = "m", focus = "all")]
[playsound(key="$d_avg_clothmovement",volume=0.4)]
[CameraShake(duration=0.2, xstrength=7, ystrength=5, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r",posfrom = "0,0", posto = "0,-30",duration = 0.5)]
[delay(time=0.8)]
[playsound(key="$d_avg_clothmovement",volume=0.4)]
[CameraShake(duration=0.2, xstrength=7, ystrength=5, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l",posfrom = "0,0", posto = "0,-30",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "r",posfrom = "0,-30", posto = "0,0",duration = 0.5)]
[charslot(slot = "l",posfrom = "0,-30", posto = "0,0",duration = 0.5)]
[delay(time=0.8)]
[charslot(slot = "l",posfrom = "0,0", posto = "-100,0",duration = 1)]
[charslot(slot = "r",posfrom = "0,0", posto = "100,0",duration = 1)]
[delay(time=1)]
[CameraShake(duration=0.2, xstrength=7, ystrength=15, vibrato=10, randomness=90, fadeout=true, block=false)]
[playsound(key="$bodyfalldown1",volume=0.4)]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_1035_1#9$1",focus="r")]
[name="里昂"]检查我做，你休息一会儿吧。
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]那个，里昂先生......
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",focus="r")]
[name="里昂"]怎么了？
[charslot(slot = "l", name = "avg_1034_jesca2_1#10$1",focus="l")]
[name="杰西卡"]炸掉动力炉......真的好吗？
[name="杰西卡"]我知道我不该说这种话，但商议要炸塔的时候，我以为你会很抗拒......
[charslot(slot = "r", name = "avg_npc_1035_1#8$1",focus="r")]
[name="里昂"]不炸塔，我怎么封锁密道，怎么掩护海伦娜的去向？
[charslot(slot = "l", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]......
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",focus="r")]
[name="里昂"]至于我怎么想......不重要了，已经不重要了。
[name="里昂"]这里，这个达维镇，镇子里的一切都已经无法挽回了。
[name="里昂"]但如果有那笔钱，在未来，在拓荒地，一切都还是有希望的......对吗？
[charslot(slot = "l", name = "avg_1034_jesca2_1#11$1",focus="l")]
[name="杰西卡"]......一定会的。
[charslot(slot = "r", name = "avg_npc_1035_1#9$1",focus="r")]
[name="里昂"]呵，希望，希望......这点儿希望真他妈贵啊。
[charslot(slot = "r", name = "avg_npc_1035_1#7$1",focus="r")]
[name="里昂"]可为了这点儿希望，为了让这张车票不至于在今天就到站......就算把人的一生搭进去，也只能认了。
[MusicVolume(volume=0.6, fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="42_g10_blacksteelarmory",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_106_franka_1#1$1")]

... (全文28490字符)
```

### level_act28side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="42_g7_sonwydowntown_n",screenadapt="coverall")]
[playMusic(intro="$escape_intro",key="$escape_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_airdefensealert",volume=0.5)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#11$2",duration=0.5)]
[Delay(time=1)]
[name="杰西卡"]顶多十分钟，黑钢的车队就会赶来。
[charslot(slot = "m", name = "avg_npc_1035_1#1$1")]
[name="里昂"]那都不够我们跑到能源塔。
[charslot(slot = "m", name = "avg_npc_1034_1#1$1")]
[name="伍德洛"]我留在这里......你们先走。
[charslot(slot = "m", name = "avg_4104_coldst_1#2$2")]
[name="海伦娜"]你能争取多少时间？
[charslot(slot = "m", name = "avg_npc_1034_1#1$1")]
[name="伍德洛"]你们需要多少时间？
[charslot(slot = "m", name = "avg_1034_jesca2_1#10$2")]
[name="杰西卡"]最少......半个小时？
[charslot]
从腰间拿出左轮，伍德洛数了数子弹。
[charslot(slot = "m", name = "avg_npc_1034_1#1$1")]
[name="伍德洛"]......一个小时？毕竟你们之后还要装配炸药。
[charslot(slot = "m", name = "avg_4104_coldst_1#1$2")]
[name="海伦娜"]绰绰有余。
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$2")]
[name="杰西卡"]伍德洛先生......
[charslot(slot = "m", name = "avg_npc_1035_1#7$1")]
[name="里昂"]......保重，伍德洛。
[charslot(slot = "m", name = "avg_npc_1034_1#1$1")]
[name="伍德洛"]快去吧。对了，杰西卡......
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$2")]
[name="杰西卡"]伍德洛先生，什么事？
[charslot(slot = "m", name = "avg_npc_1034_1#2$1")]
[name="伍德洛"]谢谢......谢谢你一路将它带过来。
[charslot(duration=0.5)]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
伍德洛整了整帽檐转身向长街走去。很快，他的背影消失在夜色中，只留了一句告别在空气中。
[name="伍德洛"]期待下一次见面，朋友们。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g11_blacksteelplatform",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1045_1#1$1",duration=0.5)]
[delay(time=1)]
[name="黑钢佣兵"]克里夫先生，动力推进设备的调试已经结束，工程小队正在第二遍确认连接结构的稳固性。
[charslot(slot = "m", name = "avg_npc_1036_1#7$1")]
[name="“桥夹”克里夫"]......
[charslot(slot = "m", name = "avg_npc_1045_1#1$1")]
[name="黑钢佣兵"]......克里夫先生？
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]预计什么时候可以离开？
[charslot(slot = "m", name = "avg_npc_1045_1#1$1")]
[name="黑钢佣兵"]这周三一切都能准备妥当。  
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]好......我知道了。
[dialog]
[PlaySound(key="$rungeneral",volume=0.6)]
[charslot(slot = "m", focus = "n")]
[delay(time=2)]
[name="秘书"]克、克里夫先生......打扰了，有件事需要向您汇报。
[charslot]
[charslot(slot = "m", name = "avg_npc_1045_1#1$1")]
[name="黑钢佣兵"]那克里夫先生，我先行离开了。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]嗯......
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1045_1#1$1")]
[charslot(slot = "m",posfrom = "0,0", posto = "-200,0",duration = 1)]
[charslot(duration=0.8)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1036_1#10$1")]
[name="“桥夹”克里夫"]什么事？
[charslot(slot = "m", focus = "n")]
[name="秘书"]驻扎在地块上的小队向本部请求支援，说是有一伙劫匪炸开了银行金库的大门，将里面的准备金悉数劫走。
[name="秘书"]劫匪共有四人......身份已经确认。是伍德洛先生和他的朋友，还有......
[charslot(slot = "m", name = "avg_npc_1036_1#10$1")]
[name="“桥夹”克里夫"]还有谁？
[charslot(slot = "m", focus = "n")]
[name="秘书"]还有杰西卡小姐。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]......呵。
[charslot(slot = "m", focus = "n")]
[name="秘书"]那我们需要派人去吗？毕竟前些日子您撤回了所有部署在银行的安保人员......
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]还是以拖拽地块的准备工作为重，手头有工作的都不必停下，剩下的......都派出去吧。
[charslot(slot = "m", focus = "n")]
[name="秘书"]还有一件事，杰西卡小姐身份特殊，我们......？
[charslot(slot = "m", name = "avg_npc_1036_1#10$1")]
[name="“桥夹”克里夫"]不要伤到她，毕竟还要顾及布林雷的面子。至于伍迪......制服他的同时还不伤到他，应该没人能做到。
[name="“桥夹”克里夫"]算了......保全他的性命就好，剩下的人就交给底下的人看着办吧。
[charslot(slot = "m", focus = "n")]
[name="秘书"]好的，我明白了。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]对了，他们中谁带着钱？
[charslot(slot = "m", focus = "n")]
[name="秘书"]还不清楚。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]无论是谁，派蒂拉盯紧他。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot = "right", name = "avg_107_liskam_1#1$1")]
[Background(image="42_g10_blacksteelarmory",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$dooropenquite")]
[charslot(slot = "left", name = "avg_106_franka_1#1$1",posfrom = "-150,0", posto = "0,0",duration = 0.7)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_106_franka_1#8$1",focus="l")]
[name="芙兰卡"]你、你收到消息了吗？杰西卡他们......
[name="芙兰卡"]我们得想个办法，上面下了命令，除了杰西卡和伍德洛先生，其他人......消息只说让各小队随机应变。
[charslot(slot = "right", name = "avg_107_liskam_1#2$1",focus="r")]
[name="雷蛇"]......芙兰卡。
[charslot(slot = "right", name = "avg_107_liskam_1#1$1",focus="r")]
[name="雷蛇"]你得去通知其他人准备出发，我们小队也接到了追捕命令。
[charslot(slot = "left", name = "avg_106_franka_1#5$1",focus="l")]
[name="芙兰卡"]......你是打算遵命吗？
[charslot(slot = "right", name = "avg_107_liskam_1#8$1",focus="r")]
[name="雷蛇"]......芙兰卡，无论我们是要帮助他们......还是要抓捕他们，留给我们的时间都不多了。
[charslot(slot = "right", name = "avg_107_liskam_1#4$1",focus="r")]
[name="雷蛇"]我们必须赶在所有人之前，先找到他们。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g1_mine",screenadapt="coverall")]
[playsound(key="$d_avg_truckengine", loop=true, channel="a",volume=0)]
[SoundVolume(volume=0.8, fadetime=3,channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[StopSound(channel="a", fadetime=1)]
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$2",duration=0.5)]
[delay(time=1)]
[name="杰西卡"]海伦娜女士，里昂先生，我只能送你们到这里了。
[name="杰西卡"]载具声音不是从主街方向传来的，黑钢应该是加派人手来追捕了，和我们当初预计的一样。
[charslot]
[charslot(slot = "l", name = "avg_4104_coldst_1#2$2",focus="l")]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",focus="l")]
[name="海伦娜"]按计划进行吗？
[charslot]
[charslot(slot = "m", name = "avg_1034_jesca2_1#1$2")]
[name="杰西卡"]嗯，我留在外面吸引他们。
[charslot]
[charslot(slot = "l", name =

... (全文34992字符)
```

### level_act28side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="42_g11_blacksteelplatform",screenadapt="coverall")]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_npc_1036_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="“桥夹”克里夫"]......现在是什么情况？
[charslot(slot = "m", focus = "n")]
[name="秘书"]杰西卡小姐的踪迹已经在掌握中......因为有命令在，底下的佣兵难免束手束脚的，不过算算时间，她的弹药差不多也要耗尽了。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]蒂拉那边有消息吗？
[charslot(slot = "m", focus = "n")]
[name="秘书"]海伦娜女士和矿工带着钱进了能源塔......两人都没有出来。
[charslot(slot = "m", name = "avg_npc_1036_1#7$1")]
[name="“桥夹”克里夫"]在众目睽睽下消失吗？那里肯定有其他的出路，告诉蒂拉继续搜寻。
[charslot(slot = "m", focus = "n")]
[name="秘书"]是。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]伍迪呢？他离开了吗？
[charslot(slot = "m", focus = "n")]
[name="秘书"]伍德洛先生......他没有离开地块，看样子他似乎放弃了原本定下的逃脱计划。
[name="秘书"]毕竟一开始据蒂拉报告，伍德洛先生打算在一切结束后带那位矿工先生躲进深山中。
[charslot(slot = "m", name = "avg_npc_1036_1#10$1")]
[name="“桥夹”克里夫"]伍迪往哪里去了......
[charslot(slot = "m", focus = "n")]
[name="秘书"]他......正朝这边来。
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]......
[charslot(slot = "m", focus = "n")]
[name="秘书"]要派人拦截吗？
[charslot(slot = "m", name = "avg_npc_1036_1#1$1")]
[name="“桥夹”克里夫"]算了，让他来吧，如果他执意要来，没人能够阻拦。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[playsound(key="$d_avg_woodcracle", loop=true, channel="a")]
[Background(image="42_g2_mine_ruined",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "left", name = "avg_106_franka_1#1$1",duration=0.5)]
[charslot(slot = "right", name = "avg_107_liskam_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_106_franka_1#1$1",focus="l")]
[name="芙兰卡"]雷蛇，前面有燃烧的障碍物，车子开不进去，我们只能下来步行了。
[charslot(slot = "right", name = "avg_107_liskam_1#7$1",focus="r")]
[name="雷蛇"]那些是......黑钢的载具？
[charslot(slot = "left", name = "avg_106_franka_1#5$1",focus="l")]
[name="芙兰卡"]是伍德洛先生......还是杰西卡她......
[charslot(slot = "right", name = "avg_107_liskam_1#4$1",focus="r")]
[name="雷蛇"]至少说明刚刚能源塔爆炸时，不是所有人都在里面。
[charslot(slot = "left", name = "avg_106_franka_1#8$1",focus="l")]
[name="芙兰卡"]等等，雷蛇......上面有消息来了。
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_gen_transmissionget")]
[delay(time=1.5)]
[name="通讯音"]各小组注意，现在的情况是，在方才的爆炸事故中目标工程师生死不明，目标海伦娜失踪......
[charslot(slot = "left", name = "avg_106_franka_1#5$1",focus="l")]
[name="芙兰卡"]天......
[charslot(slot = "m", focus = "n")]
[name="通讯音"]上级指令，放弃目标伍德洛，全力追捕目标杰西卡，目标在矿厂东部废弃巷道内，持有大量武器。
[charslot(slot = "left", name = "avg_106_franka_1#11$1",focus="l")]
[name="芙兰卡"]......雷蛇，我们......该怎么......？
[charslot(slot = "right", name = "avg_107_liskam_1#4$1",focus="r")]
[name="雷蛇"]......总有些事情我们能做，这片矿厂，我们比其他小队都熟悉，想想......怎么能以最快的速度赶到她的身边。
[Dialog]
[StopSound(channel="a", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g11_blacksteelplatform",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "m", name = "avg_npc_1034_1#1$1",duration=1)]
[delay(time=2.5)]
[charslot]
[charslot(slot = "l", name = "avg_npc_1034_1#1$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]你来得比我预想中要快些......伍迪。
[charslot(slot = "l", name = "avg_npc_1034_1#1$1",focus="l")]
[name="伍德洛"]这一路上，所有建筑都空无一人，我也只能来找你了。
[charslot(slot = "r", name = "avg_npc_1036_1#10$1",focus="r")]
[name="“桥夹”克里夫"]你是在怪我吗？
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]不该吗？有时，人们背负上恶孽不是因为做了什么，而是因为什么也没做。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]那几十年前你就该射出子弹，伍迪。
[name="“桥夹”克里夫"]但你落荒而逃了，为什么？
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]因为我的共感在长久的沉寂后，终于他妈意识到，我身边再次出现了萨科塔，也就是你。
[charslot(slot = "r", name = "avg_npc_1036_1#5$1",focus="r")]
[name="“桥夹”克里夫"]我当时可是一团糟，伍迪，与我共感一定不太好受。
[charslot(slot = "l", name = "avg_npc_1034_1#2$1",focus="l")]
[name="伍德洛"]没办法，萨科塔的天性......我们总是共享一切。
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]和从你脑袋里共感到的玩意相比，战俘营里的遭遇可能还真算不上什么。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]真是残忍啊，伍迪，你这样痛恨我，但我的痛苦却无法取悦你。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g8_abandonedblock",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_drone")]
[delay(time=1)]
[playsound(key="$transmission")]
[name="通讯音"]汇报，我看到杰西卡了，坐标已共享。
[name="通讯音"]目标正向矿厂外移动，身上携有一架重型能源炮、半自动冲锋铳......还有一把手铳，型号不明。
[name="通讯音"]她一个人背了这么多吗？
[name="通讯音"]哦，对了，她还背了一扇重盾，必要时可以变成炮架的那种。
[name="通讯音"]真是厉害，看来我们的大小姐过了这么多年，变得还挺......不简单的。
[name="通讯音"]她怎么样，攻击性强吗？一些末路穷途的劫匪很容易一惊一乍，随便做点什么就能让他跳脚。
[name="通讯音"]嗯......看起来，她挺安静的，就那么向前走，什么也没有做。
[dialog]
[playsound(key="$d_avg_snowbootwalk")]
[charslot(slot="m",name="avg_1034_jesca2_1#1$2",duration=1.5)]
[delay(time=2)]
[charslot(slot = "m", focus = "n")]
小巷中，女孩背着武器吃力地在风雪中向前方行进，道路两旁残败的墙群从她身侧缓缓后退。
直到一个分岔路口，她在那里呆住了片刻，然后捏了捏领口，转向了需要逆风才能前行的那条道路。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1036_1#1$1")]
[charslot(slot = "l", name = "avg_npc_1034_1#6$1")]
[Background(image="42_g11_blacksteelplatform",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "l", name = "avg_npc_1034_1#6$1",focus="l")]
[name="伍德洛"]在战俘营里的时间是静止的，但在外面，战争仍在继续。
[charslot(slot = "r", name = "avg_npc_1036_1#5$1",focus="r")]
[name="“桥夹”克里夫"]是啊，伍迪，你和他被俘虏后，我带着更多的人去了更广阔的战场。
[charslot(slot = "r", name = "avg_npc_1036_1#1$1",focus="r")]
[name="“桥夹”克里夫"]一月份顶着炮火渡河，八月份又得守在滚烫的沙漠里寸步不能退让。
[name="“桥夹”克里夫"]有时夺取胜利，就踏着敌人的尸体前进，有

... (全文32379字符)
```

### level_act28side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Background(image="bg_iceforest_2",screenadapt="coverall")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Background(image="bg_cher_9",screenadapt="coverall")]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="预计半个小时后还会有一波攻势，你要喝口水吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="算了，看你这么紧张，估计喝了也会吐......吸气，呼气......放轻松，你从哪里来的，小姑娘？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1.5)]
[Subtitle(text="哥伦比亚啊......那你听说过达维镇吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1.5)]
[Subtitle(text="没有？太可惜了。那地方不错，虽然航线围绕东部林带，冬天漫长又寒冷，不过，地块上有座矿厂，中心的能源塔会一直燃烧。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="光是靠余热，就能让地块上所有人温暖一整个冬天。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="屋子里太热，外面又很冷，所以无论去哪里，一打开门就有一股热腾腾的白汽冲你扑来，最后凝成水滴挂在你的睫毛上，要落不落，像颗泪珠。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你得赶紧擦掉，不然屋子里的小朋友会使劲笑话你的。不过那也没关系，你可以反击，用双手架住他的胳肢窝，然后狠狠把他丢进外面厚厚的雪地。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="接下来就该你嘲笑他满头满脸的雪粒了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1.5)]
[Subtitle(text="啊......你有点想去看看了？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="确实，那是个好地方，大家都想去看一眼。我也很想......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=false)]
[delay(time=3)]
[Sticker(id="st1", text="回去再看一眼。", alignment="center", x=300,y=370,size=24,delay=0, width=700,block = true,duration=1)]
[Sticker(id="st1",duration=3,block = false)]
[delay(time=2)]
[stopmusic(fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="42_g1_mine",screenadapt="coverall")]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bgs")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_snowbootwalk")]
[charslot(slot = "m", name = "avg_npc_1035_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="里昂"]嘶——这鬼天气怎么这么冷！我就不明白了！
[charslot(slot = "m", name = "avg_npc_1035_1#7$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="里昂"]它怎么就能这么冷，能他妈这么冷！
[dialog]
[charslot]
[PlaySound(key="$dooropenquite")]
[delay(time=1.5)]
[name="海伦娜"]赶紧进来吧！既然知道冷，还站在餐馆门口抱怨天气干什么？
[stopsound(channel="bgs",fadetime=2)]
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="42_g3_diner",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_doorbell")]
[delay(time=1)]
[PlayMusic(intro="$bar_intro", key="$bar_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",duration=0.5)]
[delay(time=1)]
[name="里昂"]我这是不想把地给踩脏了。
[dialog]
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", focus = "l")]
[name="海伦娜"]说得好像你能把雪跺干净似的......给，热茶。
[dialog]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1035_1#10$1",focus="r")]
[CameraShake(duration=0.1, xstrength=15, ystrength=10, vibrato=15, randomness=90, fadeout=false, block=false)]
[multiline(name="里昂",delay=0.01,end=true)] 噗......好烫！
[name="里昂"]......今天餐馆的地也够脏的，早知道我就直接进来了。
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1",focus="l")]
[name="海伦娜"]雪下得这么大，只要来个人就会踩脏，打烊之后我会再擦一遍的。
[name="海伦娜"]要来点什么，豆子还是干面包？
[charslot(slot = "r", name = "avg_npc_1035_1#9$1",focus="r")]
[name="里昂"]这也算选择？
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1",focus="l")]
[name="海伦娜"]只有这些，不想吃你也可以不吃。
[charslot(slot = "r", name = "avg_npc_1035_1#9$1",focus="r")]
[name="里昂"]不能都来点吗？
[charslot(slot = "l", name = "avg_4104_coldst_1#1$1",focus="l")]
[name="海伦娜"]行，看在你是今晚光顾的第一个正经人，我再给你来勺免费的黄油。
[dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "-150,0",duration = 1,afrom=1,ato=0)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_1035_1#10$1",focus="r")]
[name="里昂"]海伦娜......
[charslot(slot = "r", name = "avg_npc_1035_1#10$1",focus="l")]
[name="海伦娜"]又怎么了？
[charslot(slot = "r", name = "avg_npc_1035_1#1$1",focus="r")]
[multiline(name="里昂")]你这怎么连椅子上也都是泥水——
[charslot(slot = "r", name = "avg_npc_1035_1#7$1",focus="r")]
[multiline(name="里昂",end=true)]哎，你们两个，这不是你家，把脚给我放下来！
[dialog]
[charslot]
[playsound(key="$d_avg_smashtable")]
[delay(time=0.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "left", name = "avg_npc_1044_1#1$1",duration = 0.3)]
[charslot(slot = "right", name = "avg_npc_1044_1#1$1",duration = 0.3)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1044_1#1$1",focus="r")]
[name="蛮横的混混"]老东西，你跟谁说话呢？
[charslot]
[charslot(slot = "m", name = "avg_4104_coldst_1#2$1")]
[name="海伦娜"]唉......你们冷静些。
[charslot]
[charslot(slot = "left", name = "avg_npc_1044_1#1$1",focus="l")]
[charslot(slot = "right", name = "avg_npc_1044_1#1$1",focus="l")]
[name="粗鲁的混混"]不关你的事，老板娘。
[charslot]
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]别这样，都是来吃口热饭的，有什么话好好说嘛。
[charslot]
[charslot(slot = "left", name = "avg_npc_1044_1#1$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_1044_1#1$1",focus="r")]
[name="蛮横的混混"]哟，老板娘，你这么护着他啊？
[charslot]
[charslot(slot = "m", name = "avg_4104_coldst_1#1$1")]
[name="海伦娜"]拌几句嘴而已，不至于要拿刀吧，你说呢？
[charslot]
[charslot(slot = "left", name = "avg_npc_1044_1#1$1",focus="r")]
[charslot(slot =

... (全文31006字符)
```

### level_act28side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_snow_2",screenadapt="coverall", screenadapt="coverall", xScale=1.1,yScale=1.1, x=60)]
[PlaySound(key="$d_avg_woodcracle", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.2, channel="a",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
半个月后
[dialog]
[charslot(slot = "l", name = "avg_106_franka_1#1$1", duration=1)]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", duration=1, isblock=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_106_franka_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="n")]
[name="芙兰卡"]优等生，我们快在这儿傻等一天了。
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]总部信使给我们带回来的消息，你应该也看了。
[charslot(slot = "l", name = "avg_106_franka_1#1$1", focus="l")]
[name="芙兰卡"]消息说他们预计会在明天下午到来。
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]消息上还说，我们需要提前一天准备接驳需要的各项事宜。
[charslot(slot = "l", name = "avg_106_franka_1#4$1", focus="l")]
[name="芙兰卡"]达维镇的接驳功能本来就没什么问题，罗拉花了半天就全准备好了，然后我们就带着所有人在这儿干站着。
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]如果你觉得太冷，随时可以去那边临时搭的帐篷里烤烤火。
[charslot(slot = "l", name = "avg_106_franka_1#10$1", focus="l")]
[name="芙兰卡"]可如果我不是觉得冷，而是......害怕呢？
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]害怕什么？
[charslot(slot = "l", name = "avg_106_franka_1#4$1", focus="l")]
[name="芙兰卡"]我不知道，我只是......不知道达维镇的事到底会怎么收场。
[charslot(slot = "r", name = "avg_107_liskam_1#4$1", focus="r")]
[name="雷蛇"]......
[dialog]
雷蛇略显焦躁地把通讯器贴到耳边。
[dialog]
[PlaySound(key="$transmission")]
[delay(time=2)]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="n")]
没有可接收的信号，这证明那艘被黑钢干员们称为“本舰”的巴伦基地还未进入通讯的范围。
[dialog]
[charslot(slot = "r", posfrom="0,0", posto="-80,0", afrom=1, ato=0, duration=0.7)]
[charslot(slot = "l", posfrom="0,0", posto="-80,0", afrom=1, ato=0, duration=0.7)]
[SoundVolume(volume=1, channel="a",fadetime=2)]
[BackgroundTween(xFrom=60, xTo=-60, duration=3,ease="OutQuad")]
[delay(time=2)]
[charslot]
[charslot(slot = "l", name = "avg_4105_almond_1#2$1", posfrom="60,0", posto="0,0", duration=1)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", posfrom="60,0", posto="0,0", duration=1)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_4105_almond_1#2$1", focus="l")]
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="n")]
[name="罗拉"]杰西卡，不再烤一会儿火了吗？
[charslot(slot = "r", name = "avg_1034_jesca2_1#14$1", focus="r")]
[name="杰西卡"]不了......天马上就要黑了，无论如何都会觉得冷的。
[dialog]
[PlaySound(key="$d_avg_wind", volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4105_almond_1#11$1", focus="l")]
[name="罗拉"]杰西卡，你也别太担心，虽然银行确实让人生气，但本舰马上就要来了。
[charslot(slot = "r", name = "avg_1034_jesca2_1#14$1", focus="r")]
[name="杰西卡"]......
[charslot(slot = "l", name = "avg_4105_almond_1#11$1", focus="l")]
[name="罗拉"]老板可不会让银行那些家伙骑到我们头上来。
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="r")]
[name="杰西卡"]......老板？哪个老板？
[charslot(slot = "l", name = "avg_4105_almond_1#1$1", focus="l")]
[name="罗拉"]还能有哪个老板，克里夫先生啊！
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="r")]
[name="杰西卡"]他......
[charslot(slot = "r", name = "avg_1034_jesca2_1#14$1", focus="r")]
[name="杰西卡"]我也说不好，毕竟......说到底克里夫先生是个生意人。
[dialog]
[charslot]
杰西卡沉默着看向平台的方向，手习惯性地伸进口袋，摩挲着其中的子弹。
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_4105_almond_1#2$1", focus="l")]
[name="罗拉"]嗯......？
[charslot(slot = "l", name = "avg_4105_almond_1#7$1", focus="l")]
[name="罗拉"]......杰西卡，你看那里，是不是有火光......
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="r")]
[name="杰西卡"]哪里？
[charslot(slot = "l", name = "avg_4105_almond_1#7$1", focus="l")]
[name="罗拉"]就地块上，靠近矿厂厂区的部分，可能是取暖失火了——
[dialog]
[PlayMusic(intro="$corrosion_intro", key="$corrosion_loop", volume=0.6)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_4105_almond_1#6$1", focus="l")]
[name="罗拉"]等等，不对，起火点不止一个......这、这究竟......
[dialog]
[StopSound(channel="a", fadetime=2)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#1$1", focus="r")]
[delay(time=1)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#11$1", focus="r")]
[delay(time=1)]
[PlaySound(key="$d_avg_snowrun", volume=1, loop=true, channel="b")]
[StopSound(channel="b", fadetime=2)]
[charslot(slot = "r", name = "avg_1034_jesca2_1#11$1", posfrom="0,0", posto="300,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[charslot(slot = "l", name = "avg_4105_almond_1#6$1", focus="l")]
[name="罗拉"]杰西卡？！
[dialog]
[charslot(slot = "l", name = "avg_4105_almond_1#6$1", posfrom="0,0", posto="60,0", afrom= 1, ato=0, duration=0.7)]
[SoundVolume(volume=0.2, channel="a",fadetime=2)]
[BackgroundTween(xFrom=-60, xTo=60, duration=1.5,ease="OutQuad")]
[Delay(time=0.71)]
[charslot]
[charslot(slot = "l", name = "avg_106_franka_1#1$1", posfrom="-80,0", posto="0,0", duration=0.7)]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", posfrom="-80,0", posto="0,0", duration=0.7, isblock=true)]
[PlaySound(key="$transmission")]
[delay(time=2)]
[charslot(slot = "r", focus="n")]
[name="通讯音"]......小队，黑钢......舰预计将在......后到达......
[charslot(slot = "r", name = "avg_107_liskam_1#3$1", focus="r")]
[name="雷蛇"]收到。
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r")]
[name="雷蛇"]杰西卡，你去告诉大家——
[PlaySound(key="$d_avg_snowrun", volume=0.4, loop=true, channel="b")]
[StopSound(channel="b", fadetime=2)]
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="n")]
[name="杰西卡"]队长，地块上有数个起火点，不知道出了什么问题，我得去看看！
[charslot(slot = "l", name = "avg_106_franka_1#5$1", focus="l")]
[name="芙兰卡"]怎么偏偏是这种时候......但我们已经收到了本舰发来的信号，巴伦基地离我们已经不远了——
[dialog]
[charslot(slot = "l", name = "avg_106_franka_1#6$1", focus="l")]
[name="芙兰卡"]杰西卡——杰西卡！你到底要去哪？！队长，怎么办？
[charslot(slot = "r", name = "avg_107_liskam_1#1$1", focus="r" )]
[name="雷蛇"

... (全文38107字符)
```

### level_act28side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[image(image="42_i10",screenadapt="coverall")]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[name="鲁伯特"]战争结束了，伍迪，你自由了。你可以回到拉特兰，回到那栋父母留给你的小房子，在门廊前种满玫瑰与月季......
[name="鲁伯特"]然后，找一家附近的教堂，把它们绘在天顶上，倾听每一位来者的祷告，然后让这些声音伴你入梦，这样，你便能安眠一整晚。
[name="鲁伯特"]我在仓库里找到了你的铳，他的......实在是找不到了，伍迪，就带上它回去吧。
[name="伍德洛"]那你呢？你要去哪里？
[name="鲁伯特"]我要留在这里......
[name="伍德洛"]你要留在哥伦比亚吗......可战争已经结束了。
[name="鲁伯特"]伍迪，你的战争结束了，我的才刚刚开始。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[delay(time=1)]
[Background(image="42_g9_modernoffice",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",duration = 1)]
[delay(time=1.5)]
[name="“桥夹”克里夫"]伍迪，嘿，伍迪......
[dialog]
[charslot(slot = "left", name = "avg_npc_1034_1#5$2",duration = 1.5)]
[delay(time=2)]
[charslot(slot = "m", focus = "l")]
[name="伍德洛"]嘶......
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]你还好吗？
[charslot(slot = "left", name = "avg_npc_1034_1#5$2",focus = "l")]
[name="伍德洛"]我昏迷了多长时间......
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]三天。
[name="“桥夹”克里夫"]那些孩子看到我受伤了都很紧张，一时下手没轻重。你被推倒时脑袋撞在了阶梯上，当场就昏过去了。
[charslot(slot = "left", name = "avg_npc_1034_1#1$2",focus = "l")]
[name="伍德洛"]杰西卡她们......
[charslot(slot = "right", name = "avg_npc_1036_1#8$2",focus = "r")]
[name="“桥夹”克里夫"]放心，她毫发无损。至于海伦娜女士，我派了人护送。
[name="“桥夹”克里夫"]估计半个月后，她就能安然抵达那家赌场，将所有钱洗得干干净净，再交给那位早已等在拓荒地的西尔维娅。
[charslot(slot = "left", name = "avg_npc_1034_1#1$2",focus = "l")]
[name="伍德洛"]......你没让人去追吗？
[charslot(slot = "right", name = "avg_npc_1036_1#10$2",focus = "r")]
[name="“桥夹”克里夫"]伍迪，我一早就说了，我只关心合同上的事，上面要求我拖拽地块到指定的位置，并在拖拽期间维护地块治安。
[charslot(slot = "right", name = "avg_npc_1036_1#7$2",focus = "r")]
[name="“桥夹”克里夫"]地块外的事情，里面没提到，我不关心。
[charslot(slot = "left", name = "avg_npc_1034_1#1$2",focus = "l")]
[name="伍德洛"]......
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]伍迪，我是个冷血的混蛋，但我也不喜欢趴在别人的血肉上饱餐。
[charslot(slot = "left", name = "avg_npc_1034_1#1$2",focus = "l")]
[name="伍德洛"]你打算怎么处置我？
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]我在哥伦比亚南部有一幢私宅，里面有一间很大的花房，是个好地方。
[name="“桥夹”克里夫"]你可以更名换姓去那里安度晚年，我会安排好一切。
[charslot(slot = "left", name = "avg_npc_1034_1#10$2",focus = "l")]
[name="伍德洛"]你在那里住过？
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]从没有，听房产商是这么跟我说的。
[charslot(slot = "left", name = "avg_npc_1034_1#1$2",focus = "l")]
[name="伍德洛"]......谢谢你的好意，但房产商的话信不得。
[name="伍德洛"]既然你无意把我交给法庭，那我就要离开了。
[charslot(slot = "right", name = "avg_npc_1036_1#10$2",focus = "r")]
[name="“桥夹”克里夫"]去找你的朋友？
[charslot(slot = "left", name = "avg_npc_1034_1#7$2",focus = "l")]
[name="伍德洛"]去找我的家人。
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]你的铳我放在了桌子上，半个月后有最后一列去往拓荒地的车队......
[dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_telephonering", volume=1)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]你可以......
[dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_telephonering", volume=1)]
[delay(time=1.5)]
[charslot(slot = "right", name = "avg_npc_1036_1#1$2",focus = "r")]
[name="“桥夹”克里夫"]你可......
[charslot(slot = "left", name = "avg_npc_1034_1#1$2",focus = "l")]
[name="伍德洛"]你可以先接电话。
[charslot(slot = "right", name = "avg_npc_1036_1#7$2",focus = "r")]
[name="“桥夹”克里夫"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="42_g10_blacksteelarmory",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_222",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]你要喝茶吗，先生？一路赶来，真的辛苦了......
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]......呃，谢谢，杰西卡小姐。既然您的家族花费高薪将我雇佣，我理当竭诚为您服务。
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]抢劫银行是重罪......这官司很难吧。
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]分情况，不同的需求，不同的难度。
[name="风尘仆仆的律师"]如果您对监狱没有那么抗拒的话，我们会为您争取最短的刑期，舒适的环境，出来后没人会记得您所做的事情。
[name="风尘仆仆的律师"]这种事我们经常做，只要钱到位就没什么难度。
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]嗯，还有呢？
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]当然，很少有人想待在牢狱里面，我们还有另一套计划，您可以在家里面，或者某个风景秀美的别墅里待上一阵子。
[name="风尘仆仆的律师"]当然，也在当局的监视下。
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]对你们有难度吗？
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]有，但不大。
[charslot(slot = "left", name = "avg_1034_jesca2_1#14$1",focus="l")]
[name="杰西卡"]......
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]如果您一天牢也不想坐，只想假装无事发生，立刻恢复正常的生活......很难，但不是不可能。
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]......在哥伦比亚，去监狱的罪犯其实很少，更多人是会被发往拓荒地的，对吗？
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]您放心，杰西卡小姐......有我们在，结果不会糟糕到那个地步。
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]不......我是说自己想去拓荒地，先生。
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]什么？
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]我应该在那里。我触犯了法律，这是我应付出的代价。
[charslot(slot = "right", name = "avg_npc_222",focus="r")]
[name="风尘仆仆的律师"]您要我这样向布林雷先生回复吗，杰西卡小姐？对我来说，这才是最有难度的事情。
[charslot(slot = "left", name = "avg_1034_jesca2_1#1$1",focus="l")]
[name="杰西卡"]不......阻止我做想做的事情，才是最难的。
[charslot(s

... (全文19444字符)
```

### training_act28side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 黑钢教学_a

[Tutorial(focusX=-40, focusY=220, focusWidth=250, focusHeight=196, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_franka", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
雷蛇，看这个旧式废热喷口，它正在被我“加热”喔。

[Tutorial(dialogHead="$avatar_liskam", black="$f_tut_black")] \
它确实在因吸收你的攻击而充能升温，芙兰卡。我们需要继续采集该地区装置和敌人的数据，以备之后的作战。

[Tutorial(dialogHead="$avatar_franka", black="$f_tut_black")] \
小意思，交给我吧。
```

### training_act28side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 黑钢教学_b

[Tutorial(dialogHead="$avatar_liskam", black="$f_tut_black")] \
废热喷口到达临界温度后会主动散热，对前方一条直线上的所有单位造成持续法术伤害，并<@tu.kw>减速</>其中的敌人。

[Tutorial(dialogHead="$avatar_liskam", black="$f_tut_black")] \
但散发的热量同时在为敌人的热能增幅装备充能，他们的<@tu.kw>攻击力</>和<@tu.kw>防御力</>正随着能量增加而逐渐<@tu.kw>增强</>。

[Tutorial(dialogHead="$avatar_liskam", black="$f_tut_black")] \
现在立即为我方干员提供医疗支援。
```

### training_act28side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 黑钢教学_c

[Tutorial(focusX=-135, focusY=27, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_liskam",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]\
敌人能量充满后会进入<@tu.kw>过载</>，该状态下<@tu.kw>攻击速度、防御力和法术抗性都会大幅增加</>——啧。

[Tutorial(dialogHead="$avatar_franka", black="$f_tut_black")] \
不愧是优等生小姐，这么快的攻击都能全部挡住。

[Tutorial(dialogHead="$avatar_liskam", black="$f_tut_black")] \
敌人的状态无法持久，我来承受敌人的攻击！
```

### training_act28side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 黑钢教学_d

[Tutorial(dialogHead="$avatar_franka", black="$f_tut_black")] \
看来，他们在<@tu.kw>过载</>结束后就会失去所有能量。

[Tutorial(dialogHead="$avatar_liskam", black="$f_tut_black")] \
能量清空的敌人也会失去所有攻击力和防御力的加成。现在正是反攻的时机！

[Tutorial(dialogHead="$avatar_jesica", black="$f_tut_black")] \
干员杰西卡，前来支援！
```


## 统计

- 总字符数：480914
- 对话行数：3408


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
