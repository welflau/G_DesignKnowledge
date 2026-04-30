# 明日方舟 · 活动剧情 · act15mini（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act15mini」完整剧情脚本（7个文件，2393行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act15mini
- 脚本文件数：7

### level_act15mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
乌萨斯，冰原入口，莱特-科钦斯基科考补给站
[dialog]
[Background(image="40_g2_glacier",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1", duration = 2, isblock=true)]
[name="麦哲伦"]呼——终于到了。
[charslot(slot = "m", focus="none")]
[name="装置"]嘀嘀，请说出口令。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]咳咳嗯——哥伦比亚比伦哥，乌萨斯卡特斯多索雷斯，厚罗烧！
[charslot(slot = "m", focus="none")]
[multiline(name="装置")]口令内容......
[PlaySound(key="$d_avg_scan", volume=1)]
[Delay(time=1.5)]
[multiline(name="装置",end=true)]确认。Xорошо，哥伦比亚人。
[multiline(name="装置")]发声人......
[PlaySound(key="$d_avg_scan", volume=1)]
[Delay(time=1.5)]
[multiline(name="装置",end=true)]确认。
[name="装置"]莱茵生命，编号CRL005——
[name="装置"]（奇特的语调）买买买卖唉艾~哲~伦~
[name="装置"]欢迎访问莱特-科钦斯基科考补给站。
[dialog]
[PlaySound(key="$d_gen_dooropen", volume=1)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]嗯——
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]（掏出笔记本记录）“乌萨斯境内W-K站语音系统轻微受损——”
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]“——暂无维修必要。”
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]就这样好了。
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[charslot(duration=2,isblock=true)]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_lungmencommand",screenadapt="coverall")]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1", duration=1.5, isblock=true)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[charslot(slot = "m", posfrom="0,0", posto="-100,0", duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[charslot(slot = "m", posfrom="-100,0", posto="100,0", duration=1.6)]
[delay(time=2.5)]
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[delay(time=1)]
[charslot(slot = "m", posfrom="100,0", posto="0,0", duration=1.5)]
[delay(time=3)]
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]玛丽老师的队伍大概带走了一、二、三......二十人份的生存物资？！
[name="麦哲伦"]十五人却带了二十人份的东西......
[dialog]
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[delay(time=1)]
[name="麦哲伦"]（掏出笔记本记录）“物资仅剩百分之五，可供十人使用（已扣除本人将使用的份额），需要重新补给物资。”
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]再让我看看——
[dialog]
[delay(time=1.5)]
[name="麦哲伦"]结构......没有损伤。能源......不用补充。维生设备......还好，温度没有问题。
[name="麦哲伦"]急救包没有使用迹象，门窗也都没有外部破坏的痕迹......
[name="麦哲伦"]还有最后一项......
[PlaySound(key="$keyboard", volume=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]（操作科考站设备）
[name="麦哲伦"]是这条路线没错。
[PlaySound(key="$keyboard", volume=1)]
[name="麦哲伦"]（确认沿途科考站回传的讯号）
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]一路上都是例行汇报，看来没遇上麻烦。
[name="麦哲伦"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="38_g2_colombiaoffice",screenadapt="coverall")]
[Delay(time=1)]
两个月前
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
哥伦比亚特里蒙市，莱茵生命总部，科学考察科
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="none")]
[charslot(slot = "l", name = "avg_248_mgllan_1#1$1", focus="l")]
[name="麦哲伦"]那我就准备出发了，还有什么要交代的事情吗？
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]别的应该没有了。
[name="科考科成员"]（轻声）最后还有一件，但这个你千万别告诉其他人啊。
[charslot(slot = "l", name = "avg_248_mgllan_1#4$1", focus="l")]
[name="麦哲伦"]嗯？嗯嗯，我会保密的。
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]（四处张望）
[name="科考科成员"]（轻声）马里亚姆主任的队伍在冰原失踪了。
[charslot(slot = "l", name = "avg_248_mgllan_1#3$1", focus="l")]
[name="麦哲伦"]欸？！玛丽老师怎——
[dialog]
[charslot(slot = "l", focus="all")]
[charslot(slot = "r", posfrom="0,0", posto="-250,0", duration=0.5, isblock=true)]
[Delay(time=0.4)]
[charslot(slot = "r", posfrom="-250,0", posto="-230,0", duration=0.2)]
[charslot(slot = "l", posfrom="0,0", posto="50,0", duration=0.2, isblock=true)]
[charslot(slot = "l", name = "avg_248_mgllan_1#10$1", focus="l")]
[name="麦哲伦"]呜唔唔唔！！
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]（轻声）小点声！
[charslot(slot = "l", name = "avg_248_mgllan_1#1$1", focus="l")]
[name="麦哲伦"]唔，唔唔。
[dialog]
[charslot(slot = "l", posfrom="50,0", posto="0,0", duration=1.5)]
[charslot(slot = "r", posfrom="-230,0", posto="0,0", duration=2, isblock=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]（轻声）总之就是这样。
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]（轻声）你这次去，搜救主任的队伍是最优先事项。
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]（轻声）探索协会那边已经在组织搜救队了，但你也知道，那帮人效率一直不怎么样。
[charslot(slot = "r", name = "avg_npc_530_1#1$1", focus="r")]
[name="科考科成员"]（轻声）主任他们......就只能先靠你了。
[charslot(slot = "l", name = "avg_248_mgllan_1#1$1", focus="l")]
[name="麦哲伦"]（轻声）我知道了。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_lungmencommand",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$keyboard", volume=1)]
[name="麦哲伦"]（操作科考站设备）
[charslot(slot = "m", name = "avg

... (全文47280字符)
```

### level_act15mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="40_g2_glacier",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_963_1#1$1", duration=1)]
[charslot(slot = "r", name = "avg_npc_962_1#1$1", duration=1, isblock=true)]
[charslot(slot = "l", name = "avg_npc_963_1#1$1", focus="n")]
[charslot(slot = "r", name = "avg_npc_962_1#1$1", focus="r")]
[name="坚忍的萨米山地战士"]失踪的拉瑟他们有消息了？
[charslot(slot = "l", name = "avg_npc_963_1#1$1", focus="l")]
[name="严肃的萨米山地战士"]嗯，不用再找了。
[name="严肃的萨米山地战士"]邪魔来过了。
[name="严肃的萨米山地战士"]那边的冰面上有法术凿出的痕迹，是一场苦战。
[charslot(slot = "r", name = "avg_npc_962_1#1$1", focus="r")]
[name="坚忍的萨米山地战士"]......霜槭的根系，令人尊敬的战士们，难道他们连遗体都没能留下吗？
[charslot(slot = "l", name = "avg_npc_963_1#1$1", focus="l")]
[name="严肃的萨米山地战士"]冰原上总有坏天气。
[charslot(slot = "r", name = "avg_npc_962_1#1$1", focus="r")]
[name="坚忍的萨米山地战士"]最近这样的天气太多了。
[charslot(slot = "l", name = "avg_npc_963_1#1$1", focus="l")]
[name="严肃的萨米山地战士"]萨米早已借埃克提尔尼尔之口警告过我们，不是吗？
[name="严肃的萨米山地战士"]走吧，加固堡垒，盯紧每一道关隘。
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="30_ex1_snowmount",screenadapt="coverall")]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=2)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.2, loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1",duration=0.5, isblock=true)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Delay(time=1)]
[name="麦哲伦"]（在笔记本上记录）“我们进入了冬牙群山，当前气温......零下三十一度。”
[name="麦哲伦"]“目前为止，在萨米境内，还没有发现任何通讯基站......依然无法与马里亚姆主任的科考队取得联系。”
[charslot(slot = "m", name = "avg_248_mgllan_1#5$1")]
[name="麦哲伦"]唉，不知道玛丽老师不在的话，这些笔记最后要报告到哪里去呢？他每次都能从我的调查报告里发现好多我应该更仔细观察的现象......
[name="麦哲伦"]“我们经过了此前科考记录中记载的，当地人在冬牙群山脚下、森林边缘的一个定居点。”
[dialog]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]呼......就算只是脱掉了一层手套，还是好冷啊。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]需要帮忙吗，麦哲伦？
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]啊，没事的，西蒙娜姐，我马上就写完这份报告！很快就会从避风处出来，勇敢地走进风雪的！
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]刚刚记到哪里了？对了......
[PlaySound(key="$d_avg_penrustle", volume=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]“那个定居点现在已经消失了。”
[name="麦哲伦"]“我也向西蒙娜——”
[name="麦哲伦"]（匆匆划掉）
[name="麦哲伦"]“向同行的萨米人求证了这一点。萨米人的部族确实会进行迁移。”
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_wind", volume=1)]
[SoundVolume(volume=1, channel="a",fadetime=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1.5, block=true)]
[Blocker(a=0.9, r=255, g=255, b=255, fadetime=2, block=true)]
[bgeffect(name="$eb_snow",layer=0)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=3, block=true)]
[charslot(slot = "m", focus="n")]
[name="？？？"]为什么会迁移？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]我试着去调查啦，但还没搞明白原因。
[name="麦哲伦"]西蒙娜姐说，是萨米在告诉他们，危险将至，必须迁走。
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]可是目前收集到的气候资料与历史记录相比没有异常，长期数据也没有表现出明显的变化趋势，萨米究竟是哪里表现出了危险呢？
[charslot(slot = "m", focus="n")]
[name="？？？"]看来......科考科的资料......需要更新。
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]嗯，萨米确实是我们的认知盲区。
[name="麦哲伦"]不过，萨米人好像不太喜欢被打扰。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]玛丽老师，你不就一直想跟他们达成合作，但一直没成功嘛。
[name="麦哲伦"]乌萨斯那边的申请流程那么冗长，要是能从萨米方向开辟进入冰原的新道路，增设科考站点，之后的科考应该都会更加方便吧。
[charslot(slot = "m", focus="n")]
[name="？？？"]可惜萨米人......并不想让任何人进入冰原......
[charslot(slot = "m", name = "avg_248_mgllan_1#2$1")]
[name="麦哲伦"]对呀......
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]欸？
[dialog]
[Blocker(a=0.2, r=255, g=255, b=255, fadetime=1, block=true)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]我刚刚......在跟玛丽老师对话？
[dialog]
[delay(time=2)]
[charslot(slot = "m", name = "avg_248_mgllan_1#3$1")]
[name="麦哲伦"]西蒙娜姐，西蒙娜姐！
[charslot(slot = "m", name = "avg_341_sntlla_1#7$1")]
[name="寒檀"]怎么了？
[charslot(slot = "m", name = "avg_248_mgllan_1#3$1")]
[name="麦哲伦"]我刚刚——
[dialog]
[PlaySound(key="$d_avg_wind", volume=1)]
[Blocker(a=0.5, r=255, g=255, b=255, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]——那边是不是有几个人影？雪太大了，我看不清......
[charslot(slot = "m", focus = "n")]
[name="？？？"]麦......哲伦......
[charslot(slot = "m", name = "avg_248_mgllan_1#3$1")]
[name="麦哲伦"]真、真的是玛丽老师吗？！
[name="麦哲伦"]西蒙娜姐，我要去那边看看！
[dialog]
[PlaySound(key="$d_avg_snowrun", volume=1)]
[charslot(duration=1,isblock=true)]
[delay(time=2)]
[name="科考科主任？"]麦哲伦。
[charslot(slot = "m", name = "avg_248_mgllan_1#9$1")]
[name="麦哲伦"]（啊！真的是！太好了，找到你们了！我就知道你们没事！）
[name="麦哲伦"]......
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]（奇怪，怎么......发不出声音？）
[dialog]
[PlaySound(key="$d_gen_heartbeat", volume=1, loop=true, channel="d")]
[charslot(slot = "m", name = "avg_248_mgllan_1#5$1")]
[charslot(slot = "l", name = "avg_248_mgllan_1#5$1", posfrom="0,0", posto="200,0", duration=0,isCopy=true)]
[charslot(slot = "l", name = "avg_248_mgllan_1#5$1", afrom=0.8, ato=0, duration=1,isCopy=true)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=1.05,duration= 1)]
[StopSound(channel="d", fadetime=1)]
[delay(time=1)]
[name="麦哲伦"]（呼，呼......心跳得好快......我，在发抖？为什么？）
[dialog]
[charslot(slot = "m", name = "avg_248_mgllan_1#6$1")]
[name="麦哲伦"]（不行不行不行，我得叫住主任，把他们接回去！）
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1, loop=true, channel="c")]
[charslot(sl

... (全文35372字符)
```

### level_act15mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="30_ex1_snowmount",screenadapt="coverall")]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1", duration=1, isblock=true)]
[name="提丰"]吸气——
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]嘶——
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1")]
[name="提丰"]吐气——
[charslot(slot = "m", name = "avg_248_mgllan_1#2$1")]
[name="麦哲伦"]呼——
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]来，吃颗这个。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]好——好酸......
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]至少不难吃吧，习惯就好啦。
[name="提丰"]来，还有这个。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]哦呜——呜？这个果子，怎么是空心的？
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]就像泡沫一样？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]嗯......嗯。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]我们当地人就叫它“泡沫”，吃起来是没什么感觉，但对于上山的人来说却是必备的好东西。
[name="提丰"]现在有没有觉得舒服些了，头还痛吗？
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]唔——没事了，这些水果比治高原反应的药还好用。
[name="麦哲伦"]你知道它是怎么起效的吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]不知道，这样吃有效果不就行了？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]那可不行，我得记一下，再取点样本回去，我那些做医药研发的同事一定会感兴趣的。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]你有带药吗？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]治高原反应的？有啊。
[charslot(slot = "m", name = "avg_341_sntlla_1#12$1")]
[name="寒檀"]那我建议你看一下它的主要成分。
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]（在行囊中一顿翻找）
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]有了！
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]主要成分为......傍地酸浆果和泡沫果萃取物......难道说？！
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]萨米和哥伦比亚的主要贸易品之一就是医药原材料。
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1")]
[name="寒檀"]我听说你们那里的公司在能够人工制造医药成分或异地种植原材料后，便会把曾经的贸易伙伴一脚踢开。
[name="寒檀"]但很可惜，这种方法对萨米可行不通。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]哥伦比亚连复原种植环境都做不到吗？
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1")]
[name="寒檀"]不，哥伦比亚当然做得到。但就算复原环境，种下的植物也会有区别。
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]原因很简单。
[charslot(slot = "m", name = "avg_2012_typhon_1#11$1")]
[name="提丰"]（萨米语）因为一切皆由萨米给予。
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]（萨米语）一切皆由萨米给予。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]（磕磕绊绊的萨米语）一切......皆由萨米......给予？
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1")]
[name="提丰"]你学语言学得还真快啊，我记得我们刚遇上的时候，你要想说点什么和萨米有关的东西都得等西蒙娜给你翻译一下呢。
[charslot(slot = "m", name = "avg_248_mgllan_1#9$1")]
[name="麦哲伦"]嘿嘿~
[name="麦哲伦"]你的哥伦比亚语说得也很顺畅啊。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]那是，艾尔启懂得够多，所以我多少也都会些。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]我看到林地线了，山地人应该不会继续找我们麻烦了。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]呼，终于能吃顿好的了。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]有树林就代表有好吃的？
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]山里的肉还行，但没能吃的果子。
[charslot(slot = "m", name = "avg_2012_typhon_1#8$1")]
[name="提丰"]林子就不一样了，想要什么吃的都有哦。
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]喔喔。
[PlaySound(key="$d_avg_penrustle", volume=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]（掏出笔记本记录）“林地物产丰富......”
[dialog]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_iceforest_2",screenadapt="coverall")]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]提丰，这里附近有聚落吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]有，而且是个有树的部族。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]那他们应该已经在这里安宁地生活许多年了。
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]有树的部族？
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]林地的部族有自己的族树。
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1")]
[name="寒檀"]......如果没有，要么是这个部族还太年轻，要么是他们连自己的族树都丢失了。无论哪种情况，都是该遭人耻笑的。
[name="寒檀"]这个部族的人能沟通吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]印象里还挺和善的。
[name="提丰"]而且再怎么说，住林地的都要比住山上的热情好客吧。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]欸，真的吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]肯定的，那些山地的战士一年四季都在应付北边的怪物和不友好的乌萨斯人，脾气坏点再正常不过了。
[charslot(slot = "m", name = "avg_2012_typhon_1#8$1")]
[name="提丰"]有些战士离开了阵线回到家乡，脸色都没那么冷了。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]那真是太好了......
[name="麦哲伦"]所以，萨米人一般是怎么分的？
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]很好记的，最北边住在山里的就是山地人，住在正中间林地和林地附近的就是林地人，住在最南边沼泽地里的就是泽地人。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]那提丰，你在这里算什么人呢？
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]我吗？我是猎人。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]猎人？但听你刚刚的分类法，你不应该是住在什么环境里的人吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#8$1")]
[name="提丰"]啊——这个嘛......我是个萨卡兹，也没什么固定的住所和部族，自然也没办法用那套法子做区分啦。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]那，西蒙娜姐呢？
[charslot(slot = "m", name = "avg_2012_typhon_1#8$1")]
[name="提丰"]她啊......她是——
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]我是罗德岛人。
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]罗德岛？那是什么？


... (全文50498字符)
```

### level_act15mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_darkforest", volume=0, loop=true, channel="e")]
[SoundVolume(volume=1, channel="e",fadetime=1)]
[name="？？？"]嘶——
[name="？？？"]呼——
[dialog]
[StopSound(channel="e", fadetime=2)]
[Delay(time=2)]
[Background(image="40_g1_blackforest",screenadapt="coverall")]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1", duration=1, isblock=true)]
[name="麦哲伦"]嘶——
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]把呼吸器摘下来吧麦哲伦。这里没有孢子了。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]啊，好的。
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]呜，哈啊......
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_248_mgllan_1#5$1")]
[name="麦哲伦"]啊，蘑菇好可怕。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]我可早就提醒过你了麦麦，不要乱碰不要乱碰不要乱碰。
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]不听劝，现在吃苦头了吧。
[charslot(slot = "m", name = "avg_248_mgllan_1#5$1")]
[name="麦哲伦"]我的，我的——
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]你给我的那个空盒子？我给装好蘑菇封起来了。喏。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]对，谢、谢谢。
[charslot(slot = "m", name = "avg_248_mgllan_1#5$1")]
[name="麦哲伦"]哈，哈啊——
[charslot(slot = "m", name = "avg_248_mgllan_1#5$1")]
[name="麦哲伦"]我没想到孢子浓度会那么高，还、还会麻痹呼吸系统。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]这蘑菇是吃肉的，你猜肉是怎么来的？
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]呃......
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]那你们怎么没事......
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]我可是猎人，肯定有对付它们的方法。
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]要是被人知道我死在蘑菇沼里，很丢人的。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]（萨米语）提丰，拿贡品。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=2, isblock=true)]
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]（萨米语）贡品......我们到地方了？
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]（深吸一口气）
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]嗯——确实。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=2, isblock=true)]
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]你们去哪里？等等我！
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=0.8, isblock=true)]
[Delay(time=1)]
[name="麦哲伦"]什么是“贡品”啊，我吗？
[dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1", duration=1.5, isblock=true)]
[name="提丰"]当然不是，你个呆头羽。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]这里是萨米的心脏，原初的森林。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]我们的来处与去处。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]准备些食物当作献给萨米的贡品，我们就可以进去了。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]不准备会发生坏事吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]谁知道，万一呢？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]我明白了。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]压缩饼干可以吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]我不知道。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]碾碎撒在地上就行。
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]喔，好！
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]（萨米语）大地啊，我们将要行过您的躯体。
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]（萨米语）将这贡品敬献给您，愿我们能得到您的注视，不流血，不遭猎。
[dialog]
[charslot]
[musicvolume(volume=0.2, fadetime=2)]
[delay(time=1.5)]
[charslot(slot = "m", focus="n")]
[name="？？？"]（萨米语）萨米允诺了，诸位。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[musicvolume(volume=0.6, fadetime=2)]
[charslot(slot = "m", name = "avg_npc_964_1#1$1", duration=2, isblock=true)]
[delay(time=1.5)]
[name="？？？"]（萨米语）而它将因诸位的慷慨好好吃一顿。
[charslot(slot = "m", name = "avg_341_sntlla_1#9$1")]
[name="寒檀"]您的用词......是否有些轻浮，年轻的萨满。
[name="寒檀"]......不，萨满学徒。
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]毕竟不是正式场合，用不着太计较，寒檀木裔，萨米不会介意的。
[charslot(slot = "m", name = "avg_npc_964_1#4$1")]
[name="？？？"]哦......哦？
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]一位萨满，一位猎手，一个外乡人？这组合在萨米可不常见。
[name="？？？"]各位来这里，恐怕不是来体验生活的吧。
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1")]
[name="寒檀"]我们只是急着去南方，没时间绕路，借道原初之地而已。
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]哦，理解，师父也经常这样干。
[charslot(slot = "m", name = "avg_npc_964_1#5$1")]
[name="？？？"]不过这回不一样啦，他把我一个人丢在这里，要我体悟什么“萨米的意志”。
[name="？？？"]我在这好几天了，每天就是在这片树林里兜来逛去，什么启示和旨意都没有。
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]您应该很熟悉吧，木裔。
[charslot(slot = "m", name = "avg_341_sntlla_1#9$1")]
[name="寒檀"]请叫我寒檀。
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]那么，寒檀，你能不能告诉我，那些当老师的究竟想让我们从这里拿些什么回去？
[charslot(slot = "m", name = "avg_341_sntlla_1#9$1")]
[name="寒檀"]我并不清楚，橡树之子，我只来此瞻仰过，我的试炼并不在这里。
[charslot(slot = "m", name = "avg_npc_964_1#6$1")]
[name="？？？"]是这样吗？真可惜。
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]之后的路不太好走，我们得抓紧时间。出发吧。
[charslot(slot = "m", name = "avg_npc_964_1#6$1")]
[name="？？？"]嗯......
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]等等！
[name="？？？"]我和你们一起走吧。
[name="？？？"]我知道好几棵适合休息的树、几处清澈的溪流，恰好还走过几条安全的兽道。
[charslot(slot = "m", name = "avg_npc_964_1#8$1")]
[name="？？？"]一个“指木人”，一位，嗯......向导！
[charslot(slot = "m", name = "avg_npc_964_1#9$1")]
[name="？？？"]这儿没有比我更合适的向导了！
[name="？？？"]让我和你们同行吧，寒檀，不然我会无聊到变成木头的。
[charslot(slot = "m", name = "avg_npc_964_1#1$1")]
[name="？？？"]怎么样，尊敬的萨满？
[name="？？？"]还有你，猎手，以及我们的外乡朋友，嗯？
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]


... (全文41838字符)
```

### level_act15mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="40_g1_blackforest",screenadapt="showall")]
[Delay(time=1)]
[playmusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_965_1#1$1", duration=1, isblock=true)]
[name="萨米泽地萨满"]拉格娜，拉格娜。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="萨米泽地萨满"]你想要我们如何迎接你呢？
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="萨米泽地萨满"]无论向南还是向北，所有离开的人里，最不可能回来的就是你。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_109_fmout_1#1$1",duration=2)]
[delay(time=2)]
[name="远山"]......
[charslot(slot = "m", name = "avg_109_fmout_1#1$1")]
[name="远山"]我知道，没有人邀请我回来。
[charslot(slot = "m", name = "avg_109_fmout_1#3$1")]
[name="远山"]只是，我在水晶球中看到了一个预言。
[name="远山"]......我的兄长遭遇不幸的预言。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="40_g5_samitribe",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[playmusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]唔哦，好漂亮的木雕！这个坐在果壳里的小人真的会指路吗？真的？
[charslot(slot = "m", name = "avg_248_mgllan_1#9$1")]
[name="麦哲伦"]还有这个，异色的源石晶体！
[name="麦哲伦"]要用什么样的工艺，才能在雕刻的时候保持晶体稳定呢......
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]不不不，把一块源石放在家里做摆件，是不是太危险了？
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]上次带回去的源石冰晶碎片还没有分析完，但是这个比起研究价值，更重要的是......真的很漂亮！
[charslot]
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]......
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]我找找......去乌萨斯时准备的钱币还剩下几十切尔文！
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]还是说，你们也和萨米本地人一样，只接受用东西作交换？
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]那我可以拿一整罐调料来换——但那样的话，西蒙娜姐和提丰就要陪我一起吃没什么味道的萨米食物了。
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]......我们本来就是萨米人啊。
[charslot]
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]......小姑娘，你想要什么？没有东西要换的话，我们就走了。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]欸，我是不是太吵了，哈哈......
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]抱歉，没想到还会有乌萨斯商队到这么远的集市来做生意，还带着这么多我没见过的东西！
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]唔，西蒙娜姐，你之前说我们要交换什么来着？
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]......咦，西蒙娜姐？
[charslot]
[charslot(slot = "l", name = "avg_248_mgllan_1#4$1",focus="r")]
[charslot(slot = "r", name = "avg_2012_typhon_1#9$1",focus="r")]
[name="提丰"]唉。你真的没听见？
[charslot(slot = "l", name = "avg_248_mgllan_1#10$1",focus="l")]
[name="麦哲伦"]没、没啊。
[charslot(slot = "r", name = "avg_2012_typhon_1#9$1",focus="r")]
[name="提丰"]刚刚有人认出了她，请她去帮忙了。
[charslot(slot = "r", name = "avg_2012_typhon_1#6$1",focus="r")]
[name="提丰"]有几名死者的遗体被带回了部族，但是部族没有雪祀，所以他们拜托西蒙娜帮忙检查一下遗体。
[charslot(slot = "l", name = "avg_248_mgllan_1#5$1",focus="l")]
[name="麦哲伦"]欸，有人去世了啊......
[charslot(slot = "l", name = "avg_248_mgllan_1#5$1",focus="l")]
[name="麦哲伦"]难怪我顺着集市一路走过来，没听到什么吆喝声，也没什么人主动接我的话。
[charslot(slot = "l", name = "avg_248_mgllan_1#5$1",focus="l")]
[name="麦哲伦"]大家看起来都好消沉。
[charslot(slot = "l", name = "avg_248_mgllan_1#5$1",focus="l")]
[name="麦哲伦"]唔，就连摆出来的东西也挺少的。
[charslot(slot = "l", name = "avg_248_mgllan_1#1$1",focus="l")]
[name="麦哲伦"]那我们等等西蒙娜姐，让她来做决定吧，是她说一定要来集市交换物资的。
[charslot]
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]可以吗，来自乌萨斯的朋友？
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="40_g5_samitribe",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[playmusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]......淌过萨米土地的流水啊，请接纳我，我将与您的孩子们对话。
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]（低声的哼鸣）
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="悲愁的萨满学徒"]起风了。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="悲愁的萨满学徒"]从老树最低的枝桠，到祖母瓦丽门前的火把......
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="悲愁的萨满学徒"]......慈悲的命运啊。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="悲愁的萨满学徒"]既然他们已经同意，请检查吧，寒檀木之女。他们的遗物都在这里了。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]一介黜人游历至此，得受霜槭之根系的信任，我很感激。
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1",posfrom="0,0",posto="0,-100",afrom=1,ato=1,duration=1.8,isblock=true)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1")]
[name="寒檀"]......
[charslot(slot = "m", name = "avg_341_sntlla_1#11$1")]
[name="寒檀"]这些武器上还结着暗红的冰凌，他们经历了一场苦战。
[dialog]
[charslot(slot = "m", name = "avg_341_sntlla_1#10$1",posfrom="0,-100",posto="0,0",afrom=1,ato=1,duration=0.8,isblock=true)]
[name="寒檀"]他们是从北地阵线上被带回来的战士吗？
[charslot]
[charslot(slot = "l", name = "avg_341_sntlla_1#10$1",focus="n")]
[charslot(slot = "r", name = "avg_npc_965_1#1$1",focus="r")]
[name="悲愁的萨满学徒"]嗯，这几位战士七八年前就离开部族去了北方。
[name="悲愁的萨满学徒"]谁能想到呢，辞别故乡最久、最不肯回头的两位族人，在同一天里回来了。
[charslot(slot = "l", name = "avg_341_sntlla_1#8$1",focus="l")]
[name="寒檀"]您是指死者？
[charslot(slot = "r", name = "avg_npc_965_1#1$1",focus="r")]
[name="悲愁的萨满学徒"]......是一对分道扬镳的兄妹。
[name="悲愁的萨满学徒"]既然命运让您在今天来到这里，或许这个故事也该说给您听。
[name="悲愁的萨满学徒"]当年那场覆盖半个黑森林的异常雪灾，您一定记得。
[charslot(slot = "l", name = "avg_341_sntlla_1#10$1",focus="l")]
[name="寒檀"]我记得。
[charslot(slot = "r", name = "avg_npc_965_1#1$1",focus="r")]
[name="悲愁的萨满学徒"]那时我们部族也受了影响。
[name="悲愁的萨满学徒"]就和困在暴风雪中的其他部族一样，我们祈求萨米的谕示，顶着风雪寻找树上显现的密文，想知道如何保全自己。
[name="悲愁的萨满学徒"]但......我们是一个没有雪祀的部族。
[name="悲愁的萨满学徒"]我们祈祷啊，祈祷啊，但萨米回应的只有沉默。
[name="悲愁的萨满学徒"]得不到命运的指引，萨满们也无法判断，是留还是走，要去往何处。
[name="悲愁的萨满学徒"]直到最后，那对兄妹坚定了想法，站出来领头。


... (全文37417字符)
```

### level_act15mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="34_g4_swamp_n",screenadapt="coverall")]
[Delay(time=1)]
[playmusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_081",duration=1, isblock=true)]
[name="乌萨斯商队成员"]雪又大了。
[charslot(slot = "m", name = "avg_npc_007")]
[name="乌萨斯商队护卫"]来吧，喝口酒。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]唉，我还是后悔把那个萨米人的酒壶送给了那个小姑娘。
[charslot(slot = "m", name = "avg_npc_007")]
[name="乌萨斯商队护卫"]别想了。被边防军查出来的话，你可就麻烦了。
[name="乌萨斯商队护卫"]再说，你真相信他的鼓和酒壶上写了两句话，就能保佑人平安无事？
[name="乌萨斯商队护卫"]这冰天雪地里，能保佑咱们的只有伏特加。
[name="乌萨斯商队护卫"]——好吧，至少现在只有伏特加。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]我不是那个意思。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]只是......出事的前一天晚上，我们大家还坐一起聊天来着。
[charslot(slot = "m", name = "avg_npc_007")]
[name="乌萨斯商队护卫"]是啊，你们俩的妹妹年纪差不多大。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]他跟他妹妹还没来得及和好呢。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]你就当......我是在替他遗憾吧。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]唉，我知道有那种打仗打得太久、手上血太多所以不敢回家的人，我能理解。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]可他跟我们讲了那么多家长里短的事，到最后也没说他们在跟什么人打仗。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]他们是为了救我们而死的，可我们连是怎么回事都没搞清楚。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]我该把酒壶留下来纪念他的。除了一个实实在在摸得着的东西，我实在不知道该怎么怀念那些神神秘秘的萨米人了。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]......哈哈，对待一帮萨米的野人，我是不是太伤感了点？
[charslot(slot = "m", name = "avg_npc_007")]
[name="乌萨斯商队护卫"]......你记不记得，那天晚上聊天的时候，他们还说过，萨米人并不认为死亡是终点。
[name="乌萨斯商队护卫"]比如，有时候你没感觉到风，可是风把什么东西吹动了，那就是死者的灵魂走过去了。
[name="乌萨斯商队护卫"]说实话，我觉得不傻。
[charslot(slot = "m", name = "avg_npc_081")]
[name="乌萨斯商队成员"]什么不傻？我，还是萨米人的迷信？
[charslot(slot = "m", name = "avg_npc_007")]
[name="乌萨斯商队护卫"]都不。
[name="乌萨斯商队护卫"]行了，该把其他人叫起来，准备好做生意了。
[name="乌萨斯商队护卫"]下一个部族应该不远了，我看见雪里有人来了。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="40_g1_blackforest",screenadapt="coverall")]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]萨米赐我们冰雪洗濯新生，萨米赐我们泥土承接福泽。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]我们不愿离开，却行在告别的水上。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]请送我们的族亲归来，如滴水归川。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]请让灾厄远离我们的长路，直到您无法眷顾的土地。
[charslot]
萨米的埃拉菲亚们垂下提灯，俯身掬起一捧泽水，随着萨满低声唱诵。
死者的船只沉入水中，油烛一根接一根熄灭。
黑暗逐渐漫上水面。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]......
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]即使不是我们的族人，也应当对仪式有基本的尊重。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]放下武器，背着黑弓的猎人。低头。
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]......
[charslot]
[charslot(slot = "m", name = "avg_npc_966_1#1$1")]
[name="萨米泽地居民"]（低声）看啊，那个猎人......
[name="萨米泽地居民"]您在北方的冰原上，见过这种事，是不是？她会不会染黑我们的命运——
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]......“谈论厄运的人越多，厄运的阴影就越清晰。”
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]我不会谈论它。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]有人会说的，埃克提尔尼尔会说的。但有能力在这片土地上公开讲出一切的人，绝不是我们。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]我再警告一次，猎人。
[charslot(slot = "m", name = "avg_npc_965_1#1$1")]
[name="主持仪式的萨满"]否则，我们也将拿起武器应对。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]等、等一下！她只是在警戒！
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]提丰，你跟大家解释一下，他们会明白的！
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[stopmusic(fadetime=2)]
[name="提丰"]......嘘。
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]我感觉到它的动向了。
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]立刻让开。
[PlaySound(key="$d_avg_bowstring_tightened", volume=1)]
[charslot(slot = "m", name = "avg_2012_typhon_1#2$1")]
[name="提丰"]所有人离开这里！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="40_g1_blackforest",screenadapt="coverall")]
[charslot]
[PlaySound(key="$d_avg_darkforest", volume=0, loop=true, channel="a")]
[SoundVolume(volume=1, channel="a",fadetime=2)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
半小时前
[charslot(slot = "m", name = "avg_109_fmout_1#1$1")]
[name="远山"]就快到了。
[charslot(slot = "m", name = "avg_248_mgllan_1#2$1")]
[name="麦哲伦"]呼......太好了。
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]没想到我竟然会有点晕船......唔，应该是晕船吧。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]可是，远山姐，你不是说自己没有在搬迁之后的部族生活过吗，怎么知道船葬的地点在哪里？
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]看那些警示的木篱。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]喔......
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]在泽地，一个部族葬下死者的水域，平时是不会让人进入的。
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]木篱不仅是为了警戒醒着的人，更重要的是提醒睡梦中的人。
[charslot(slot = "m", name = "avg_2012_typhon_1#5$1")]
[name="提丰"]因为大家都会在梦中与离去的亲人和朋友见面，不够警惕的话，很容易漫游到这种地方来。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]原来如此！好，这一条我也记下来。
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]（记笔记）“做梦的时候要小心。”
[charslot(slot = "m", name = "avg_248_mgllan_1#7$1")]
[name="麦哲伦"]......唔。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]（小声）那我要是想研究一下这里的水，是不是又要被骂了？
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]唉。你要做什么？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]是这个，信标。我想在水底设置一个信标，收集一些数据。
[charslot(slot = "m", name = "avg_2012_typhon_1#4$1")]
[name="提丰"]唔......你是不是说过这个小东西能定位？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]嗯。

... (全文38530字符)
```

### level_act15mini_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="40_g7_samiresort",screenadapt="coverall")]
[Delay(time=1)]
[playmusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot]
[name="哥伦比亚游客"]漂亮！再来一个！
[charslot]
[name="哥伦比亚游客"]哥们，我敢说，你这技术去蓝卡坞表演也毫不逊色！
[dialog]
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1", duration=1, isblock=true)]
[name="麦哲伦"]欸，那个转广告牌的人看起来有点眼熟，以前他是不是......在莱茵总部附近那家快餐店门口表演来着？
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]唔，也对，快餐店隔壁就是卡拉万国际旅行社的营销点嘛。
[charslot(slot = "m", name = "avg_248_mgllan_1#10$1")]
[name="麦哲伦"]不过他转得这么快，根本看不清广告牌上写的是什么呀......
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]是温泉。
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]哦——欸，你去过吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]没有，但是从外面来这里的人我见得太多了，大家都只会一边冷得打哆嗦一边问“温泉在哪里”。对他们有吸引力的，肯定就是这个了。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]欸嘿，其实对我来说也挺有吸引力的。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]如果得到萨米的意志眷顾，找到林间的温泉并不是难事。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]我虽不曾在过去几年里来到萨米南部，但也听说过这一带的居民常常路遇焦急的南方人。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]南方人会塞给他们一把没有雕饰过的赤金，请他们占卜附近温泉的地点。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]那他们得到答案了吗？
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]呵，谁知道呢。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]我只听说，因为他们给的金条并不好看，有些人甚至误以为，南方来的大多数人还没开化出审美能力。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]听起来......大概是没达成合作吧。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]不过，后来他们找了一些有经验的人，跟麦麦你差不多的人，自己找到了温泉。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]你看那个，一直在唱歌的东西。
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]啊，广告车。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]嗯，广告车。跟着广告车一直走，就能走到他们正在搭房子的另一处温泉。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]这样的情况，好像还挺多的。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]你对这座小镇也很了解。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]当然，这可是萨米的土地。
[charslot(slot = "m", name = "avg_2012_typhon_1#7$1")]
[name="提丰"]就算这里不太出现异象，很少有人托我帮忙，我也不至于搞不清楚这里的情况。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]唔，但是这里和萨米的大部分地区都不太一样。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]我的导览手册放在哪里了......啊，找到了。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]按照地图，从这——里到这——里，都是用来迎接游客的度假村，没什么萨米人居住。
[charslot(slot = "m", name = "avg_248_mgllan_1#2$1")]
[name="麦哲伦"]我们现在走过的这片街区，不仅有电力，有信号，甚至连城际网络也有......（深吸气）嗯，还有净水剂的味道。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]虽说各大科技公司办事处聚集的街区，确实需要比较方便的通讯设施......
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]不过办事处内部看起来，真的好像莱茵总部的办公室啊......
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]还有，他们还用钢筋和混凝土模拟大树的样子，在上面建房子欸。萨米本地人见了不会生气吗？
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]我觉得不会吧？
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]我能理解，你们那边的人到了萨米总是很害怕，所以要把自己关在铁笼子里保护起来。
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]这么说好像也没错......就算是我这样进入冰原好几次的科考人员，也不能像你们一样随心所欲地在户外活动。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]没关系，就算这样做，也不意味着跟萨米的土地分隔开。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]艾尔启一直都是这么说的。
[charslot(slot = "m", name = "avg_341_sntlla_1#13$1")]
[name="寒檀"]......麦哲伦，你手里这本手册，可以让我看一下吗？
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]好呀，不过这还是我之前从乌萨斯进入无尽冰原时拿到的手册，所以标注的都是乌萨斯语。西蒙娜姐要查什么，我来帮忙辨认吧！
[charslot(slot = "m", name = "avg_248_mgllan_1#1$1")]
[name="麦哲伦"]啊，不是这一面，这是针对乌萨斯疗养院的萨米度假村广告。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]没事，麦哲伦，我自己可以看懂的。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]......通讯中的坐标......找到了。
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]......我该去处理我的事情了。提丰，麦哲伦，恐怕到不得不说分别的时刻了。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]欸嘿，下次我会从这里出发前往无尽冰原的，肯定还会再碰到西蒙娜姐！
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]要是遇到暴风雪，拜托你一定要再来帮忙哦。
[charslot(slot = "m", name = "avg_341_sntlla_1#12$1")]
[name="寒檀"]呵呵，好啊。
[charslot(slot = "m", name = "avg_341_sntlla_1#3$1")]
[name="寒檀"]下次......是啊，这一次小小的行动结束后，不知道我会去哪里呢？
[charslot(slot = "m", name = "avg_341_sntlla_1#1$1")]
[name="寒檀"]祝你顺利，麦哲伦。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]拜拜，西蒙娜姐！
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]那你呢，小台风？
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]莱茵生命的办事处就在前面拐角的地方，我也要去报到啦。
[charslot(slot = "m", name = "avg_248_mgllan_1#4$1")]
[name="麦哲伦"]可是你的委托人在哪里呀？
[charslot(slot = "m", name = "avg_2012_typhon_1#11$1")]
[name="提丰"]不知道。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]艾尔启只说，在察帕特，有人在等我。
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]不过......
[charslot(slot = "m", name = "avg_2012_typhon_1#9$1")]
[name="提丰"]......唔，总之随便走走，自然就会遇到的。
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]欸？那好吧，你在这里找找！
[charslot(slot = "m", name = "avg_248_mgllan_1#8$1")]
[name="麦哲伦"]对了，给你一点零钱！这样你就可以坐着巡回游览车在小镇里找人了！
[charslot(slot = "m", name = "avg_248_mgllan_1#9$1")]
[name="麦哲伦"]我先走啦！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[charslot(slot = "m", name = "avg_2012_typhon_1#6$1")]
[name="提丰"]唉，“小台风”到底是什么啊？
[charslot(slot = "m", name = "avg_2012_typhon_1#1$1")]
[name="提丰"]——啊。
[dialog]
[charslot]
提丰抬起头，屋檐下站着一个熟悉的高大身影。
猎手一向机警，但并没有注意到她是什么时候走到那里的。
[charslot(sl

... (全文27461字符)
```


## 统计

- 总字符数：278396
- 对话行数：2393


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
