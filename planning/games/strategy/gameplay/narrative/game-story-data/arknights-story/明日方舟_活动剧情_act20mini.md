# 明日方舟 · 活动剧情 · act20mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act20mini」完整剧情脚本（6个文件，1462行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act20mini
- 脚本文件数：6

### level_act20mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g2_newvolsiniistreet_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$m_avg_elegance_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_541_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_542_1#10$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_542_1#10$1",focus="r")]
[name="甘比诺"]你有没有听到什么动静？
[charslot(slot = "l", name = "avg_npc_541_1#1$1",focus="l")]
[name="卡彭"]这里是街道，到处都是动静。
[charslot(slot = "l", name = "avg_npc_541_1#8$1",focus="l")]
[name="卡彭"]我更在意的是这股味道。
[charslot(slot = "r", name = "avg_npc_542_1#10$1",focus="r")]
[multiline(name="甘比诺")]货都是分装好的，放在地窖里，按理说不会有味道才对......
[charslot(slot = "r", name = "avg_npc_542_1#1$1",focus="r")]
[multiline(name="甘比诺")]啧，要是找到了散的，我还真想尝尝。
[charslot(slot = "l", name = "avg_npc_541_1#2$1",focus="l")]
[name="卡彭"]别想了，听说今天来的都是最高端的货。
[name="卡彭"]闻着这味儿我就不想干活了。
[charslot(slot = "r", name = "avg_npc_542_1#8$1",focus="r")]
[name="甘比诺"]你是不想干活，还是不想在这儿干活？
[charslot(slot = "l", name = "avg_npc_541_1#1$1",focus="l")]
[name="卡彭"]有区别吗？
[name="卡彭"]反正晚上要干的活也是在这街上跑来跑去、看来看去，并且希望不会有什么来找麻烦的人。
[charslot(slot = "l", name = "avg_npc_541_1#2$1",focus="l")]
[name="卡彭"]昨晚撞上的那桶红漆根本洗不掉，今天拿到报酬，我得去把我那辆车重新漆一遍。
[charslot(slot = "r", name = "avg_npc_542_1#8$1",focus="r")]
[name="甘比诺"]随便你，反正我的那份我得存着，公司以后还要雇人呢。
[Dialog]
[charslot(slot = "l", name = "avg_npc_541_1#1$1",focus="l")]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]......
[charslot(slot = "r", name = "avg_npc_542_1#10$1",focus="r")]
[name="甘比诺"]看我干嘛？
[charslot(slot = "l", name = "avg_npc_541_1#9$1",focus="l")]
[name="卡彭"]新沃尔西尼可真够神奇的，都把你这个西西里人变得勤俭持家了。卡西米尔人给的比安东尼奥大方多了吧。
[charslot(slot = "r", name = "avg_npc_542_1#1$1",focus="r")]
[name="甘比诺"]我哪知道开出租车公司要花的钱能有那么多。
[charslot(slot = "l", name = "avg_npc_541_1#2$1",focus="l")]
[name="卡彭"]不过这种巡视一下街道和会场就能完事儿的活，真是比开出租还无聊。
[name="卡彭"]“红酒锦标赛”，我想破头都想不出能有什么人会来这种闲得慌的人和傻子搞出来的比赛上搞破坏。
[charslot(slot = "r", name = "avg_npc_542_1#1$1",focus="r")]
[name="甘比诺"]行了，这条街巡逻完了，回剧场吧。
[name="甘比诺"]不过你说，活动安保这样的工作，卡西米尔人怎么会找上我们呢？
[charslot(slot = "l", name = "avg_npc_541_1#2$1",focus="l")]
[name="卡彭"]谁知道。推荐我们的，可能是个好人吧。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g4_srctheater",screenadapt="coverall", block=true)]
[delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.5, channel="bgs",fadetime=2)]
[PlayMusic(intro="$path_intro", key="$path_loop",volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_176",duration=0.7)]
[delay(time=1)]
[PlaySound(key="$clink", volume=0.6)]
[delay(time=1)]
[SoundVolume(volume=0, channel="bgs",fadetime=2)]
[charslot(slot = "m", name = "avg_npc_176",focus="m")]
[name="沙雷"]各位，请允许我占用一点时间。
[Dialog]
[charslot]
剧场内的灯光亮得有些过分，像是刻意要把每一张脸都照清楚。西装革履的商人站在舞台中央，轻轻敲了敲手中的红酒杯。
清脆的响声并不大，但依旧让周围的来宾安静了下来。
[charslot(slot = "m", name = "avg_npc_176",focus="m")]
[name="沙雷"]我知道，今晚真正让人期待的，是酒，是音乐，是接下来那段足够被记住的时光。
[name="沙雷"]但在那之前，我还是想说一句——能够在这里举办这场红酒锦标赛，对我们来说，是一件意义非凡的事。
[name="沙雷"]新沃尔西尼是一座讲秩序、讲规则的城市，这一点，从我们决定把红酒锦标赛放在这里开始，就已经得到了最充分的证明。
[name="沙雷"]红酒，是需要时间的东西。
[name="沙雷"]而时间，只有在稳定的环境里，才有意义。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_applause", volume=1)]
[delay(time=2)]
掌声过后，卡西米尔商人继续说着。从酒的年份，说到酿造工艺，又顺理成章地提到了跨城合作与物流体系。
每一个词都落在该落的位置上，没有一句多余。
[charslot(slot = "m", name = "avg_npc_176",focus="m")]
[name="沙雷"]当然，如果没有新沃尔西尼市政厅的支持，这场红酒锦标赛也许无法这么快就与大家见面。
[name="沙雷"]市长先生，能与您合作，是我们的荣幸。
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="sw")]
[stopsound(fadetime=2.5, channel="sw")]
[charslot(slot = "m", name = "avg_npc_1541_1#8$1",duration=1)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_1541_1#8$1",focus="m")]
[name="莱昂图索"]新沃尔西尼欢迎来自叙拉古之外、任何遵守这座城市规则的合作。
[name="莱昂图索"]只要是正当的生意，这里不会设门槛。
[charslot(slot = "m", name = "avg_npc_176",focus="m")]
[name="沙雷"]哈哈，这是当然。
[name="沙雷"]市长先生，我可不是在奉承啊。
[name="沙雷"]在新沃尔西尼，在这里，我几乎不用担心某个家族突然插手，也不用谈妥一件事之后，再去确认是否还有“另一层意思”。
[name="沙雷"]这种清晰，对经商来说，非常珍贵。
[charslot(slot = "m", name = "avg_npc_1541_1#8$1",focus="m")]
[name="莱昂图索"]听起来，你对新沃尔西尼的评价相当高。
[charslot(slot = "m", name = "avg_npc_176",focus="m")]
[name="沙雷"]是的，正因为如此，我们才愿意把最好的酒，和最重要的合作，都放在这里。
[charslot(slot = "m", name = "avg_npc_1541_1#7$1",focus="m")]
[name="莱昂图索"]那也真是我们的荣幸。
[Dialog]
[charslot]
[SoundVolume(volume=0.5, channel="bgs",fadetime=1)]
[delay(time=1)]
[name="来自宾客的声音"]我们已经等得够久的了，什么时候开始比赛啊？
[name="来自宾客的声音"]是啊是啊，我也想见识见识卡西米尔的红酒有多厉害呢！
不合时宜的声音从人群中传来，又消散于人群中。但如此明亮的灯光下，卡西米尔商人的脸上却未见有什么不快。
[charslot(slot = "m", name = "avg_npc_176",focus="m")]
[name="沙雷"]哈哈，看来是我有些多嘴，让我们的客人久等了。
[name="沙雷"]那么就有请新沃尔西尼的知名乐团，让接下来的曲目为我们的锦标赛决赛正式拉开帷幕！
[Dialog]
[charslot(duration=0.7)]
[StopSound(channel="bgs", fadetime=1.5)]
[delay(time=1)]
[PlaySound(key="$d_avg_spotlightc", volume=1)]
[avgdisplay(id = "1", style = "bg", name = "bg_black",afrom=0,ato=0.3,duration=1,slot = "bgover", layer = 1,isblock=true)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[delay(time=1)]
灯光暗了下来，卡西米尔商人顺势与莱昂图索一同走下舞台，在靠近角落的某处等待欣赏接下来的演奏。
莱昂图索没有看向舞台的方向，没了刺目的灯光，他反倒看清了气定神闲来到他面前的人物。
[Dialog]
[charslot(slot = "m", name = "avg_4037_demetr_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_4037_demetr_1#1$1",focus="m")]
[name="德米特里"]真是抱歉，我家的手下没怎么见过这种场合，表现得有些激动了。
[charslot(slot = "m", name = "avg_npc_1541_1#7$1",focus="m")]
[name="莱昂图索"]无妨。只是今后的新沃尔西尼，或许会有很多类似的场合。
[charslot(slot = "m", name = "avg_4037_demetr_1#1$1",focus="m")]
[name="德米特里"]看来我得教育他们早点习惯了。
[charslot(slot = "m", name = "avg_npc_176

... (全文29192字符)
```

### level_act20mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g1_newvolsiniistreet_d",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Dialog]
[PlaySound(key="$dooropenquite", volume=1)]
[PlaySound(key="$d_avg_doorbell",volume=0.6,delay=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_700_1#1$1",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="餐馆店主"]抱歉啊小贝蒂，叔叔也想帮你一把，只是......你看，我这也是小本生意。
[name="餐馆店主"]上次从你那里进的几瓶酒现在还在酒墙上落灰呢，这样，你要不去街角那家店问问？
[charslot(slot="m",name="avg_npc_700_1#1$1",focus="m")]
[name="小贝蒂"]嗯，我去问问看，谢谢保罗叔叔！
[Dialog]
[charslot(slot="m",name="avg_npc_242",focus="m")]
[delay(time=0.5)]
[charslot(duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_700_1#1$1",focus="m")]
[name="小贝蒂"]......街角那家店其实贝蒂也已经问过了，大家都说“不用了”。
[name="小贝蒂"]先把东西挪开吧，傻站在这里会影响保罗叔叔做生意的。
[Dialog]
[playsound(key="$d_avg_dragheavybox")]
[PlaySound(key="$d_avg_cloakmovement", volume=1,delay=0.9)]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 2)]
[delay(time=2.3)]
[playsound(key="$d_avg_putonwoodenfloor_xshield", volume=0.7)]
[PlaySound(key="$d_avg_bottlecollide", volume=0.7,delay=0.3)]
[charslot(slot = "m", action="shake",random=true, power=8, times=40,duration=0.8)]
[name="小贝蒂"]嘿......咻唔唔呃呃？！
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="l",name="avg_npc_2202_1#10$1",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="l",name="avg_npc_2202_1#10$1",focus="l")]
[name="路过的少女"]小心！
[charslot(slot="l",name="avg_npc_2202_1#3$1",focus="l")]
[name="路过的少女"]好险......来，拿稳了。
[charslot(slot="m",name="avg_npc_700_1#1$1",focus="m")]
[name="小贝蒂"]谢、谢谢姐姐。
[charslot(slot="l",name="avg_npc_2202_1#3$1",focus="l")]
[name="路过的少女"]这可真够沉的，怪不得你这小身板拿不动，装的什么——
[charslot(slot="l",name="avg_npc_2202_1#2$1",focus="l")]
[name="路过的少女"]咦，是“维尔蒂”啊。
[charslot(slot="m",name="avg_npc_700_1#1$1",focus="m")]
[name="小贝蒂"]姐姐你知道？
[name="小贝蒂"]这是贝蒂爷爷工作的维尔蒂酒庄生产的红酒，我们酒庄已经有几十年历史啦！姐姐要不要买一瓶尝尝？
[charslot(slot="l",name="avg_npc_2202_1#9$1",focus="l")]
[name="路过的少女"]......原来如此。
[charslot(slot="l",name="avg_npc_2202_1#5$1",focus="l")]
[name="路过的少女"]你叫贝蒂对吧？既然在这里碰到了也是缘分，认识一下吧。
[name="托希娅"]我是托希娅，喏，这是我的名片。
[charslot(slot="m",name="avg_npc_700_1#1$1",focus="m")]
[name="小贝蒂"]名片，好厉害！对不起，贝蒂没有名片......咦？
[name="小贝蒂"]卡西米尔黄金平原酒业，新沃尔西尼分公司——销售代表？
[charslot(slot="l",name="avg_npc_2202_1#5$1",focus="l")]
[multiline(name="托希娅")]虽然我想用不了多久，它就会变成“高级客户经理”了......
[charslot(slot="l",name="avg_npc_2202_1#9$1",focus="l")]
[multiline(name="托希娅")]不过，就是这么一回事。很遗憾，我们是竞争对手，所以我不会买你的酒。
[charslot(slot="l",name="avg_npc_2202_1#5$1",focus="l")]
[name="托希娅"]现在请让让吧，贝蒂小姐——我和保罗先生有约，正要谈上一笔好生意。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_manorindoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]你刚来新沃尔西尼不久，就谈成了好几单大生意。真不错！
[name="沙雷"]来，托希娅，今天就算是给我们的金牌销售补上接风洗尘的这一顿啦。
[Dialog]
[charslot(slot="r",name="avg_npc_2202_1#4$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_2202_1#4$1",focus="r")]
[name="托希娅"]您太客气啦，舅舅！
[charslot(slot="r",name="avg_npc_2202_1#1$1",focus="r")]
[name="托希娅"]这阵子您一直在主持筹备红酒锦标赛，忙也是当然的，只是希望我过来没给您添麻烦就好。
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]怎么会添麻烦呢！有你这样经验丰富的销售来加入“黄金平原”，那可是我捡着了大便宜。
[name="沙雷"]不过我听说你之前在斜屋百货，干得还不错，怎么会想到这个时候来新沃尔西尼？
[charslot(slot="r",name="avg_npc_2202_1#9$1",focus="r")]
[name="托希娅"]这......说来话长。
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]我想，是和最近大骑士领闹得沸沸扬扬的那起......“银枪天马贪腐案”有关吧？
[charslot(slot="l",name="avg_npc_176",focus="n")]
尽管沙雷压低了声音，最后的那几个字仍引得托希娅猛然抬起了头。
[charslot(slot="r",name="avg_npc_2202_1#3$1",focus="r")]
[name="托希娅"]您是怎么......
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]我听说，前些天商业联合会带人到斜屋百货的楼下，带走了你们的一名主管，刚好是你原先所在部门的管事。
[charslot(slot="r",name="avg_npc_2202_1#7$1",focus="r")]
[name="托希娅"]......看来还是瞒不过您。那位主管算是我的恩人，但......她的亲戚里有一位银枪天马。
[name="托希娅"]原本这是件脸上有光的好事，可自从商业联合会开始发难......他们有时没法直接对监正会的人出手，就把他们身边的人“带走调查”。
[name="托希娅"]这个案子如今牵扯得越来越大，有些倒霉蛋，哪怕是那些明眼人一看就知道完全无辜的人，也要被扣上这样那样的罪名......
[name="托希娅"]我们普通人要是不小心被卷入了这风波里，又怎么能跟商业联合会这样的巨兽对抗？
[charslot(slot="r",name="avg_npc_2202_1#9$1",focus="r")]
[name="托希娅"]我就想不如出来发展——
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]托希娅，我们“黄金平原”能在新沃尔西尼有如今的规模，少不了商业联合会在背后的扶持。
[name="沙雷"]上层的人锐意进取，想要拓张版图，那对我们每一个商人来说，都是好事。
[charslot(slot="r",name="avg_npc_2202_1#7$1",focus="r")]
[name="托希娅"]......您说的是。
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]你既然都已经来了这里，大骑士领的事就别再多想了。
[name="沙雷"]不如保持敢闯敢拼的劲头，好好儿干。以后舅舅的生意做得更大了，还能少得了你的好处？
[charslot(slot="r",name="avg_npc_2202_1#5$1",focus="r")]
[name="托希娅"]......那我先谢谢舅舅了。
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]你是个聪明的孩子，多的我就不说了。
[name="沙雷"]菜我已经点过了，只是不知道你喝些什么。
[charslot(slot="r",name="avg_npc_2202_1#5$1",focus="r")]
[multiline(name="托希娅")]让您费心了，我确实不太会喝酒。
[charslot(slot="r",name="avg_npc_2202_1#6$1",focus="r")]
[multiline(name="托希娅")]我看看......
[charslot(slot="r",name="avg_npc_2202_1#5$1",focus="r")]
[name="托希娅"]对了，请问这边有没有一款棕色的汽水？应该是叙拉古本地的牌子，橙子味道，但有点苦？
[Dialog]
[charslot]
[name="侍者"]您是说“金诺托”？不好意思，本店没有这款饮品。
[charslot(slot="l",name="avg_npc_176",focus="l")]
[charslot(slot="r",name="avg_npc_2202_1#5$1",focus="l")]
[name="沙雷"]怎么，你从哪里知道的那种老古董？咱们公司的软饮线进来之后，那些本地的牌子基本都被淘汰了。
[charslot(slot="r",name="avg_npc_2202_1#3$1",focus="r")]
[name="托希娅"]咦......是吗？
[charslot(slot="l",name="avg_npc_176",focus="l")]
[name="沙雷"]托希娅，你忘了咱们的广告是怎么说的了吗？“新沃尔西尼，新生活”，复古怀旧这套还是留给那些莱塔尼亚人搞吧。
[name="沙雷"]来杯咱们公司的无酒精气泡水怎么样？
[charslot(slot="r",name="avg_npc_2202_1#4$1",focus="r")]
[name="托希娅"

... (全文31384字符)
```

### level_act20mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g12_saluzzowinery",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_2201_1#1$1",duration=2)]
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,duration=2)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]露彼娜小姐，这里是我们萨卢佐酒业这次向您的酒庄采购原材料葡萄的清单与相应的价格明细。
[name="埃里奥"]麻烦您核对确认。
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[multiline(name="露彼娜")]好，我看看——
[charslot(slot="l",name="avg_npc_2201_1#1$1",focus="l")]
[multiline(name="露彼娜")]嗯，没什么问题。您做事一向妥帖。
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]......过奖了。
[name="埃里奥"]......露彼娜小姐......有句话......以我的立场，不知该不该问。
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]怎么了，突然这么严肃？
[name="露彼娜"]问吧，埃里奥大叔。我们都合作这么久了，不用这么生分。
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]自从卡西米尔人的葡萄酒进入新沃尔西尼的市场以来——
[name="埃里奥"]您酒庄上自家葡萄园中作为生产原材料的葡萄便渐渐有了富余，我们酒业出资采购，正好作为补充......
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]你们给的价格很实在。也算是帮我消耗了库存，是一桩双赢的生意。挺好的。
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]确实。但这次......您交付给我们的葡萄，这数量......
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]对你们来说也太多了？
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]不，以我们目前的生产线，自然是多多益善，但对您的酒庄来说，不是一点也没有给今后的生产留下原材料吗？
[charslot(slot="l",name="avg_npc_2201_1#7$1",focus="l")]
[name="露彼娜"]......
[name="露彼娜"]您看出来啦？
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]......露彼娜小姐......
[charslot(slot="l",name="avg_npc_2201_1#4$1",focus="l")]
[name="露彼娜"]我们......维尔蒂酒庄，前阵与“黄金平原”的商业代表有过接触。
[charslot(slot="l",name="avg_npc_2201_1#5$1",focus="l")]
[name="露彼娜"]他们提议出资收购我们酒庄，给的价格......让我无法拒绝。
[charslot(slot="l",name="avg_npc_2201_1#4$1",focus="l")]
[name="露彼娜"]我们酒庄的生意早就不行了，虽然大家还在努力想办法销售......
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]现在“黄金平原”的人愿意来找我，说明至少我们酒庄的设备和葡萄园还有价值，这对我来说也是一件好事。
[name="露彼娜"]维尔蒂酒庄与萨卢佐酒业的合作一直都很愉快，埃里奥大叔，谢谢您之前的照拂。
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]......
[name="埃里奥"]但是......你们酒庄上的其他人愿意吗？达维德怎么说？尼科洛呢？他也同意？
[charslot(slot="l",name="avg_npc_2201_1#4$1",focus="l")]
[name="露彼娜"]......我会说服他们的。
[charslot(slot="r",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="埃里奥"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Delay(time=2)]
[name="？？？"]我不同意，露彼娜！维尔蒂——我们的酒庄，怎么能就这么卖给卡西米尔人？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="l",name="avg_npc_2201_1#2$1",duration=2)]
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,duration=2)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]先冷静下，尼科洛。坐下来，我们一起吃点喝点再慢慢说。
[Dialog]
[PlaySound(key="$d_avg_pourwine", volume=1)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]这是......
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]我们酒庄的招牌“桑娇维塞”。您应该再熟悉不过了，不是吗？
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]......是啊。这个标签......我记得，它还是你的爷爷老维尔蒂亲手画的。
[name="尼科洛"]他调配出这种酒时，葡萄都是我在养护的呢！
[name="尼科洛"]葡萄藤的枝子是我一根根修剪的。冬天用的修枝剪很硬，又难用力，当时可费了不少劲，一整个冬天都要在户外忙活。
[name="尼科洛"]可是一想到这些老藤年纪比我们几个加起来都大，一切悉心呵护都是值得的。
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]卡西米尔现在都是机器修剪，一天不到就能剪完整个葡萄园。
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]那能一样吗？那些笨机器只会野蛮地扯断葡萄藤，短期来看确实是快，哼，但这样剪完之后，葡萄也活不了几年了。
[name="尼科洛"]他们根本不懂根据葡萄藤的走势来修理，让果实获得更多光照保证口味......
[name="尼科洛"]你们年轻人根本不懂叙拉古的老手艺，也没有人愿意学了。
[name="尼科洛"]叙拉古的佳酿之所以独特，就是因为酒庄的每株葡萄都和这里的家族一样长久。
[name="尼科洛"]唉......养护葡萄藤和管理一个家族是一样的。至少对你爷爷来说是一样的。
[charslot(slot="l",name="avg_npc_2201_1#11$1",focus="l")]
[name="露彼娜"]尼科洛......
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]想想吧，露帕，维尔蒂酒庄的每一颗葡萄，都是从比你爷爷年纪还大的藤上摘下的。
[name="尼科洛"]还有我们这些老工人，摘了一辈子葡萄，搬了一辈子木桶，也酿了一辈子酒。
[name="尼科洛"]我的儿子继承了我的手艺，就连我的孙女，也都在帮酒庄卖酒。
[name="尼科洛"]如果酒庄被卖了，我们这些人又该去哪儿？
[charslot(slot="l",name="avg_npc_2201_1#2$1",focus="l")]
[name="露彼娜"]大家的后续安排我也会想办法，不会让大家的手艺无处施展的。
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]我——唉！露帕，卖掉了酒庄，遣散了工人，维系着我们的大家庭还会存在吗？
[charslot(slot="l",name="avg_npc_2201_1#4$1",focus="l")]
[name="露彼娜"]对我来说，死得体面总比狼狈地在新沃尔西尼苟延残喘好。趁这块地还有价值，大家好聚好散。
[name="露彼娜"]赔偿我会严格按照合同来履行。
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]你......唉。我不是在意那些赔偿！
[name="尼科洛"]你从小就对酒庄的生意不感兴趣，但这也是老维尔蒂苦心经营下来的，作为他的孙女，难道你就没有一点留恋吗？
[charslot(slot="l",name="avg_npc_2201_1#4$1",focus="l")]
[name="露彼娜"]爷爷也不希望他的酒庄因为经营不善倒闭，为它找一个好归宿未必不好。这里是新沃尔西尼，尼科洛，我们应该试着接受新的秩序。
[charslot(slot="l",name="avg_npc_2201_1#4$1",focus="none")]
年老的工人半天没有说话。
最后，他从口袋里掏出一张请柬，放到桌子上。
[charslot(slot="l",name="avg_npc_2201_1#11$1",focus="l")]
[name="露彼娜"]这是......
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]我的孙女贝蒂，下周就是她的十岁生日。就按叙拉古的老规矩来。
[charslot(slot="l",name="avg_npc_2201_1#6$1",focus="l")]
[name="露彼娜"]咦，她也到这岁数啦，那我一定——
[charslot(slot="r",name="avg_npc_696_1#1$1",bstart=0.2,bend=0.4,focus="r")]
[name="尼科洛"]我走了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r",afrom = 1, posto = 0,duration=1,focus="all")]
[charslot(slot="r", posfrom = "0,0", posto = "100,0",duration=2.5,focus="all")]
[Delay(time=2.5)]
[PlaySound(key="$dooropenquite",

... (全文25347字符)
```

### level_act20mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="56_g6_courtsquare_n",screenadapt="coverall", block=true)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15, fadetime=0.01)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15, fadetime=0.01)]
[Delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[PlaySound(key="$d_avg_rainlight_loop", volume=0, loop=true, channel="c")]
[PlaySound(key="$d_avg_truckengine", volume=0, loop=true, channel="car")]
[SoundVolume(volume=0.6, channel="c",fadetime=1)]
[SoundVolume(volume=0.5, channel="car",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
后来很长一段时间里，每当伊雷妮又驾驶着卡车独自行驶时，她总能想到自己当晚的犹豫。
卡车在法院广场边缘停下来的时候，天色已经彻底暗了。她没有立刻熄火，发动机的震动顺着方向盘传到她的手腕上，又一点点退回去。
来的路上，伊雷妮已经打了电话给拉维妮娅，说自己有些事想和她商量一下。
[Dialog]
[charslot(slot="m",name="avg_npc_1542_1#4$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1542_1#4$1",focus="m")]
[name="伊雷妮"]呼......
[name="伊雷妮"]应该怎么说呢......拉维妮娅，我已经没有办法了......
[Dialog]
[charslot]
坐在驾驶座上的伊雷妮喃喃地重复着未说完的句子，后半句的“我只能来找你”却迟迟说不出口。
“只能”吗？想到这里，伊雷妮有些苦涩地沉默了半晌，雨声透过车窗的缝隙扑向她的脸颊。
[Dialog]
[stopsound(channel="car", fadetime=1)]
[delay(time=1.5)]
她伸手关掉了引擎。
[Dialog]
[stopmusic(fadetime=2)]
[stopsound(channel="c", fadetime=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[Background(image="56_g9_truckcamp",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1550_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_1561_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_1561_1#1$1",focus="r")]
[name="山德罗"]这一趟下来，比前半个月跑得累死累活到手的钱还要多。
[name="山德罗"]卡西米尔人可真是舍得给钱啊。
[charslot(slot="l",name="avg_npc_1550_1#1$1",focus="l")]
[name="鲁杰罗"]炫耀？
[charslot(slot="l",name="avg_npc_1550_1#2$1",focus="l")]
[name="鲁杰罗"]我这周光补账就补掉一趟的利润了。
[charslot(slot="l",name="avg_npc_1550_1#1$1",focus="l")]
[name="鲁杰罗"]卡西米尔人扣钱的时候倒是扣得挺狠的，怎么也没见你说呢。
[charslot(slot="r",name="avg_npc_1561_1#1$1",focus="r")]
[name="山德罗"]哈哈，上个月的违约金多谢你帮我出啦，正好我这笔报酬也到账了，欠你多少来着？
[charslot(slot="l",name="avg_npc_1550_1#1$1",focus="l")]
[name="鲁杰罗"]什么欠不欠的，兄弟一场，谁有困难大家都会帮的。
[charslot(slot="r",name="avg_npc_1561_1#1$1",focus="r")]
[name="山德罗"]说的也是。那我先存一部分，下次谁再被扣钱了，我也能出点力。
[charslot(slot="l",name="avg_npc_1550_1#2$1",focus="l")]
[name="鲁杰罗"]省着点吧，最近源石燃料的钱好像也涨了。我刚从卡车燃料站回来，看那数字一个劲儿往上跳，看得我肉疼。
[charslot(slot="l",name="avg_npc_1550_1#1$1",focus="l")]
[name="鲁杰罗"]倒是巧了，在燃料站碰上雷欧帝药店的伙计，那家伙人挺好，还让我蹭了他的燃料折扣卡。
[name="鲁杰罗"]下次路过他们店，我得记着给他带包烟。
[charslot(slot="r",name="avg_npc_1561_1#1$1",focus="r")]
[name="山德罗"]是吗？哈，你当心别被伊雷妮知道，不然她又要说你和家族的人私下——
[Dialog]
[charslot]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1542_1#2$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1542_1#2$1",focus="m")]
[name="伊雷妮"]私下什么？
[charslot(slot="m",name="avg_npc_1561_1#1$1",focus="m")]
[name="山德罗"]没什么没什么。
[name="山德罗"]好久不见啊，伊雷妮，我看过不了多久，我就会把你之前的送货记录给破了。
[charslot(slot="m",name="avg_npc_1542_1#1$1",focus="m")]
[name="伊雷妮"]可以啊，到时候奖励你来处理运输保障署的文书工作。
[charslot(slot="m",name="avg_npc_1561_1#1$1",focus="m")]
[name="山德罗"]哈哈，别，千万别。我得去下个单子的交接点了，回见，伊雷妮。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(duration=1)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]确实好久没在营地里见到你了，你好像瘦了不少，忙也得注意身体，不然索默尔得怪我们没照顾好你——
[charslot(slot="m",name="avg_npc_1542_1#2$1",focus="m")]
[name="伊雷妮"]别打岔。你们刚刚聊什么呢？
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]真没什么。
[charslot(slot="m",name="avg_npc_1542_1#6$1",focus="m")]
[name="伊雷妮"]唉......
[charslot(slot="m",name="avg_npc_1542_1#8$1",focus="m")]
[name="伊雷妮"]我看你和山姆就是不长记性！
[charslot(slot="m",name="avg_npc_1542_1#2$1",focus="m")]
[name="伊雷妮"]山姆怎么不在这里？我在营地里转了一圈都没找到他，看他的排期，今天和之后几天都是空着的。他去哪了？
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]他最近病得厉害，发烧好几天了，还又拉又吐的，昨晚送完订单之后，就回去躺下了。他本来今天要送的订单都换班给吉安了。
[charslot(slot="m",name="avg_npc_1550_1#2$1",focus="m")]
[name="鲁杰罗"]你知道的，卡西米尔人那边......请假扣的钱实在太多了，不如让有空的人顶上......
[charslot(slot="m",name="avg_npc_1542_1#4$1",focus="m")]
[name="伊雷妮"]......
[charslot(slot="m",name="avg_npc_1542_1#6$1",focus="m")]
[name="伊雷妮"]算了。唉，等会儿我联系医生去看看他吧。
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]怎么了？你找他有急事吗？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_lqudrppg", volume=0.8)]
[Delay(time=1)]
伊雷妮有些恼怒地晃了晃手中的物件，里面传来液体在玻璃瓶里晃荡的声音。
只看外形，也能知道包裹里放着的是一瓶酒，更不用说包裹上赫然贴着萨卢佐酒业的标志。
[charslot(slot="m",name="avg_npc_1542_1#6$1",focus="m")]
[name="伊雷妮"]萨卢佐酒业......为什么寄红酒到我们营地？
[name="伊雷妮"]要不是收件人上明明白白地写着山姆的名字，我还以为是你们谁把订单的货物落在了营地的收件室。
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]哦，这个应该是山姆他表弟一家的乔迁贺礼。
[charslot(slot="m",name="avg_npc_1542_1#2$1",focus="m")]
[name="伊雷妮"]乔迁贺礼？
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]之前他表弟一家刚搬来新沃尔西尼时，找房子的事情，德米特里先生——呃，德米特里，帮了一点忙。
[name="鲁杰罗"]应该是那个时候提过的，搬完家会送瓶红酒过来祝贺。
[charslot(slot="m",name="avg_npc_1542_1#8$1",focus="m")]
[name="伊雷妮"]......
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]只是一瓶红酒，伊雷妮，只是一瓶红酒......这酒不是给他的，山姆已经戒酒了，你也知道的呀。
[charslot(slot="m",name="avg_npc_1542_1#8$1",focus="m")]
[name="伊雷妮"]我当然知道，我只是很疑惑那位德米特里先生为什么会知道山姆表弟一家的事。
[name="伊雷妮"]还有你，鲁杰罗，你之前租下的那家小超市，我前些天去买东西，怎么改成萨卢佐酒业的专门店了？
[name="伊雷妮"]你们什么时候这么熟了？
[charslot(slot="m",name="avg_npc_1550_1#1$1",focus="m")]
[name="鲁杰罗"]呃，我转租给他们了。管理比我以为的更麻烦，我想我还是不适合当超市老板，不如早点放弃，安心做我的卡车司机。
[charslot(slot="m",name="avg_npc_1542_1#8$1",focus="m")]
[name="伊雷妮"]你是有什么难处吗？不能和我说，却能和家族的人说？
[charslot(slot="m",name="avg_npc_1550_1#2$1",focus="m")]
[name="鲁杰罗"]没那回事，伊雷妮......
[charslot(slot="m",name="avg_npc_1542_1#8$1",focus="m")]
[name="伊雷妮"]......
[name="伊雷妮"]你们什么时候能明白，这些小恩小惠也都是人情，总有一天是要还的，而且会比我们想象中的代价更大。
[charslot(slot="m",name="avg_npc_1550

... (全文27730字符)
```

### level_act20mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_499_1#1$1",duration=2)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_499_1#1$1",focus="m")]
[name="葆拉"]这灯光打得真好，衬得你的眼睛像祖母绿一样。噢，我可真幸运，拥有一个有着祖母绿眸子的好女儿。
[charslot(slot="m",name="avg_4031_liesel_1#1$1",focus="m")]
[name="莉泽尔"]又不是我要上台指挥，葆拉妈妈......
[charslot(slot="m",name="avg_4031_liesel_1#5$1",focus="m")]
[name="莉泽尔"]但你确实很幸运，拥有一个可以把演出和乐团事务安排都处理得很完美的好女儿哦！
[charslot(slot="m",name="avg_npc_499_1#1$1",focus="m")]
[name="葆拉"]呵呵，是啦。那么我的好女儿，明天与街角那家准备开业的新商场的商务会谈也交给你了，没问题吧？
[name="葆拉"]我有一些新曲目的想法，等今天的红酒锦标赛结束，我想抽点时间好好编排一下。
[charslot(slot="m",name="avg_4031_liesel_1#6$1",focus="m")]
[name="莉泽尔"]当然没问题啦，葆拉妈妈，放心交给我。
[charslot(slot="m",name="avg_4031_liesel_1#1$1",focus="m")]
[name="莉泽尔"]快准备上台吧，马上就要演出了。
[name="莉泽尔"]等今天结束，我们黑绒幕乐团的名声彻底打出去了，到时候你可有得忙啦。
[Dialog]
[charslot]
舞台上的灯光透过后台帷幕的缝隙，打在执棒的卡普里尼高高竖起的角上。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="56_g12_saluzzowinery",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_1135_1#1$1",bstart=0.3,bend=0.5,afrom = 0, posto = 1,duration=1)]
[charslot(slot="m", posfrom = "100,0", posto = "0,0",duration=2.5)]
[Delay(time=2.5)]
当时她只看到一个轮廓。
地窖顶上的射灯斜斜打下，玻璃杯的闪光随着晃动的人影隐去，又再出现。
莉泽尔本想走近，看对方是否是因为迷路而误入了地窖，想问问那人，需不需要自己指路。
可她才刚迈出脚步，那人却像提前听见了脚步声般迅速转身，动作轻快地穿过货架。
两人擦身时，灯光刚好扫过他的肩，漆黑的兜帽之上是高耸的角。
[Dialog]
[charslot(slot="m",afrom = 1, posto = 0,duration=1,focus="all")]
[charslot(slot="m", posfrom = "0,0", posto = "-100,0",duration=2.5,focus="all")]
[Delay(time=2.5)]
[charslot]
[charslot(slot="m", posfrom = "-100,0", posto = "0,0",duration=0.5,focus="all")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4031_liesel_1#7$1",focus="m")]
[name="莉泽尔"]角？卡普里尼的......角？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[name="葆拉"]......抱歉。
[name="葆拉"]咳、咳咳......！
[Dialog]
[Background(image="33_g4_srctheater",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_bwlngrlng", volume=1, loop=false, channel="a")]
[StopSound(channel="a", fadetime=1.5)]
[Delay(time=2)]
[focusout(duration=1, type="bg", from=0, to=1, block=true)]
剧场内的灯光亮得过分，照得葆拉倒下的地板上，漫开的酒液如鲜血一般刺目。
不久前还在称赞自己、还在对自己温柔笑着的母亲的嘴唇，染上了和红酒一样沉重不祥的暗红。
灯光那么亮，亮得莉泽尔眼前的景象都开始摇晃。可是那么亮的灯光下，葆拉睁着的眼睛里依旧没有半分光彩。
[name="莉泽尔"]葆拉......妈妈......？
[CameraShake(duration=0.5, xstrength=2, ystrength=2, vibrato=30, randomness=90, block=false)]
[name="莉泽尔"]妈妈！！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[focusout(duration=1, type="bg", from=1, to=0, block=true)]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Delay(time=2)]
[name="？？？"]——莉泽尔小姐？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[charslot(slot="m",name="avg_4031_liesel_1#14$1",duration=2)]
[Delay(time=2.5)]
[name="莉泽尔"]......呃？
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]按我刚刚说的，我们接下来的合作和款项支付，就按照合同上写明的方案操作吧。
[name="沙雷"]莉泽尔小姐想必也应该能理解的，对吧？
[charslot(slot="m",name="avg_4031_liesel_1#9$1",focus="m")]
[name="莉泽尔"]啊，抱歉，我刚才分神了......
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]没关系，没关系，我理解的。您刚遭受这样沉重的打击，还得勉强支撑起这个乐团，确实很不容易。
[name="沙雷"]唉，关于葆拉女士的事，我本人再次向您表达遗憾。
[name="沙雷"]这座城市就这样失去了一位如此美丽又优秀的艺术家，实在是巨大的损失！
[name="沙雷"]我都深感痛心，更不用说作为她养女的莉泽尔小姐您了。
[charslot(slot="m",name="avg_4031_liesel_1#7$1",focus="m")]
[name="莉泽尔"]谢谢您......
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]希望您能尽快打起精神来！我也为您的乐团准备了一些慰问品，一会儿您可以带回去分给大家。
[charslot(slot="m",name="avg_4031_liesel_1#7$1",focus="m")]
[name="莉泽尔"]那真是让您费心了。能与您合作真是我们乐团的荣幸。
[name="莉泽尔"]那么演出的费用问题......
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]不用担心，不用担心，我们预付的定金是肯定不会向您索要的。
[name="沙雷"]但正如我刚才所说，后续的话，我们酒业已经决定不再与贵乐团续约了。
[name="沙雷"]希望乐团的大家能够节哀，一起共渡难关，早点迈过这个坎。
[charslot(slot="m",name="avg_4031_liesel_1#9$1",focus="m")]
[name="莉泽尔"]什、什么，不再续约？
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]是啊。少了葆拉女士这么璀璨的明珠，贵乐团失了主心骨，演出的水准恐怕一时也无法回到原本的水平。
[name="沙雷"]我们毕竟是商人，不是做慈善的——抱歉，我这么说是不是有点太直白了？
[charslot(slot="m",name="avg_4031_liesel_1#9$1",focus="m")]
[name="莉泽尔"]那、那我们原本预定了的明天和后天的演出——
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]自然也是取消了——本来预定的是在剧场里再演出两天，让新沃尔西尼的市民们来共同参与品酒活动。
[name="沙雷"]但现在出了这么一档子事，剧场都得被市政厅封锁调查，活动也没法继续......
[name="沙雷"]唉，我的损失也很大啊！
[charslot(slot="m",name="avg_4031_liesel_1#13$1",focus="m")]
[name="莉泽尔"]......那之前几场的费用呢？我们为红酒锦标赛预热那几天的演出是没问题的呀！反响也很热烈......
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]我们的合同上写得很清楚，“如遇不可抗力导致演出终止或取消，甲方将不必支付相应尾款”。
[name="沙雷"]也就是说，只有全部演出都顺利完成了，我们才会支付后续款项。
[name="沙雷"]莉泽尔小姐大概是还处在悲痛之中，才会把这条给忘了？
[charslot(slot="m",name="avg_4031_liesel_1#7$1",focus="m")]
[name="莉泽尔"]不，这不......
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]唉，这次的事肯定是大家都不想看到的，我们也蒙受了很大的损失，希望您与贵乐团能够体谅。
[name="沙雷"]如果还有什么我们能帮得上忙的地方，您尽管说，我们一定会尽力的。
[charslot(slot="m",name="avg_4031_liesel_1#7$1",focus="m")]
[name="莉泽尔"]......
[name="莉泽尔"]......我知道了。
[name="莉泽尔"]如果您这边以后还有乐团演出的需求，可以联系我。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]当然，那是当然的。
[name="沙雷"]不过，没有了葆拉女士，贵乐团的工作还能顺利展开吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="28_g11_lounge",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[chars

... (全文31688字符)
```

### level_act20mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[playsound(key="$d_avg_rainlight_loop",loop=true,channel="1",volume=0.5)]
[name="？？？"]真是太感谢您了，莱昂图索少爷！
[name="？？？"]要不是有您和贝洛内家，我真不知道接下来的日子该怎么办才好。
[Dialog]
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="莱昂图索"]......别这么说，埃里奥叔叔。我也没做什么。
[charslot(slot="m",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="m")]
[name="埃里奥"]有您和贝洛内的名字就够了，本来就不需要您多做什么。
[name="埃里奥"]您能在房东上门问我讨要房租时到我家来拜访，您的露面就足以让他再掂量掂量。
[name="埃里奥"]您走之后，他很快就同意给我再宽限两周，我再自己想想办法......
[charslot(slot="m",name="avg_427_vigil_1#7$1",focus="m")]
[name="莱昂图索"]我不明白，埃里奥叔叔，为什么您会突然......您的水果摊呢？
[charslot(slot="m",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="m")]
[name="埃里奥"]水果摊？哈。已经卖啦。
[name="埃里奥"]我的小爱玛，在夏天的时候发了一场高烧，谁能想得到呢，烧退了之后，她的腿突然就不能动了。
[name="埃里奥"]幸好德米特里给介绍了一位好医生。那医生说，这是小孩儿在夏天常患的重病，要是不好好治，可能以后再也没法站起来了。
[name="埃里奥"]所以我就把摊子卖了，跟亲戚们一起凑了凑，先付了一部分诊费，剩下的以后再分期向医生还。
[name="埃里奥"]总算人是救了回来，她现在只是腿脚有点儿跛，还是个健健康康的小女孩儿。至于房租和欠医生的钱......总会有办法的。
[charslot(slot="m",name="avg_427_vigil_1#8$1",focus="m")]
[name="莱昂图索"]......您一直在街角这边摆摊，我和德米特......我们从小就喜欢您摊子上卖的橙子。
[name="莱昂图索"]大家是这么多年的街坊邻居，您要是早些来找我，我可以借您钱，那您就不用——
[charslot(slot="m",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="m")]
[name="埃里奥"]不，不，莱昂图索少爷，那可是很大的一笔钱。就算您能借给我，我也不能收。
[name="埃里奥"]再说，我要是向您借钱，应付了一时，也应付不了一辈子。房东还会再来，房租每一周都得再交。
[name="埃里奥"]好在现在有贝洛内家族的荫庇......房东不会再逼我马上交钱，不然就搬出去；面包店也会愿意先赊些吃的给我。
[charslot(slot="m",name="avg_427_vigil_1#5$1",focus="m")]
[name="莱昂图索"]......可是，您明明......从前一直不愿加入家族。
[name="莱昂图索"]您总是说，普通人根本没必要，也不应该掺和家族的事，认真工作，过好自己的日子才是最重要的。
[charslot(slot="m",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="m")]
[name="埃里奥"]哈！那是老头儿从前没经过事，太天真了。
[name="埃里奥"]家族的意义，也不只是喊打喊杀。老头儿现在可算明白了。
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[name="莱昂图索"]......
[charslot(slot="m",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="m")]
[name="埃里奥"]放心吧，莱昂图索少爷，老埃里奥不是个不知好歹的人。
[name="埃里奥"]既然受了贝洛内家的帮助，日后要是有用得着老埃里奥的时候，您尽管说一声就是！
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[name="莱昂图索"]......
[Dialog]
[charslot(slot="m",name="avg_npc_1563_1#1$1",bstart=0.2,bend=0.4,focus="m")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",afrom = 1, posto = 0,duration=1,focus="all")]
[charslot(slot="m", posfrom = "0,0", posto = "-100,0",duration=2.5,focus="all")]
[Delay(time=3.5)]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_4037_demetr_1#1$1",afrom = 0, posto = 1,duration=1,focus="all")]
[charslot(slot="m", posfrom = "-100,0", posto = "0,0",duration=2.5,focus="all")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[name="莱昂图索"]......你是故意的吧，德米特？
[name="莱昂图索"]前阵子我问你为什么近来没见到埃里奥叔叔的水果摊，你告诉我说，他带着家人回家乡去参加亲戚的葬礼了。
[charslot(slot="m",name="avg_427_vigil_1#7$1",focus="m")]
[name="莱昂图索"]你明明早就知道，埃里奥叔叔家的爱玛生了重病。
[name="莱昂图索"]前天你又突然让我到这家餐厅来买披萨......你早就知道，埃里奥叔叔会经过，能在这里找到我。
[charslot(slot="m",name="avg_4037_demetr_1#1$1",focus="m")]
[name="德米特里"]你应对得很好，莱昂。
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[name="莱昂图索"]应对？被你牵着走，算什么应对？我要是早知道——
[charslot(slot="m",name="avg_4037_demetr_1#9$1",focus="m")]
[name="德米特里"]你即使早知道，也做不了什么。你无法预测他的生活还会遇到什么困难，你个人能提供的帮助也极为有限。
[charslot(slot="m",name="avg_427_vigil_1#4$1",focus="m")]
[name="莱昂图索"]但至少能让他不至于做他不愿意做的事，选择加入家族！
[charslot(slot="m",name="avg_4037_demetr_1#8$1",focus="m")]
[name="德米特里"]在此刻，能帮助他的只有家族。
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[name="莱昂图索"]是吗？我不这么认为。用家族的名义来虚张声势，要付出于他而言多大的代价，家族又能替他撑得了多久？
[name="莱昂图索"]他应该获得更多的工作机会，而我们——叙拉古应该从制度上保证他们的生活。依靠家族的威势并不能解决根本问题。
[charslot(slot="m",name="avg_4037_demetr_1#9$1",focus="m")]
[name="德米特里"]我希望你从这件事里学到的不是乐善好施，也不是替他人着想，莱昂。
[charslot(slot="m",name="avg_4037_demetr_1#8$1",focus="m")]
[name="德米特里"]你是贝洛内家的少主，迟早要继承这个家族。
[name="德米特里"]合格的家主都知道，适时地提供一些帮助能让人们承你的情。欠你的债，总有一天，他们需要偿还。
[charslot(slot="m",name="avg_427_vigil_1#7$1",focus="m")]
[name="莱昂图索"]你说得冷酷，德米特，那你为什么私下里要给埃里奥叔叔介绍医生？
[name="莱昂图索"]如果只是为了要让我学会向人施恩，你该让我来做这件事，不是吗？
[charslot(slot="m",name="avg_427_vigil_1#1$1",focus="m")]
[name="莱昂图索"]你之所以会这样做，是因为在那时候，你不知道小爱玛的病有这么严重，你也不知道埃里奥叔叔会不得不卖掉他的水果摊。
[name="莱昂图索"]你当时只是想帮他，而这明明与家族无关。
[charslot(slot="m",name="avg_4037_demetr_1#4$1",focus="m")]
[name="德米特里"]我们......只能做到自己力所能及的事情，不是吗？
[name="德米特里"]而且，老埃里奥摊子上的橙子总是最美味的，他确实很擅长挑水果。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[stopsound(channel="1",fadetime=2)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="56_g8_governmentoffice_d",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]这只是您力所能及范围之内的一桩小事，市长先生。请把那位在我的红酒锦标赛上杀人的黑帮头子绳之以法！
[charslot(slot="m",name="avg_npc_1541_1#1$1",focus="m")]
[name="莱昂图索"]沙雷先生，对德米特里......贝洛内的审判在今日下午即将举行，在此之前，他只是嫌疑人。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]不是他还能是谁？他将我视为竞争对手，私底下小动作没少干。
[name="沙雷"]我的红酒好好地放在酒窖里，我还特地雇佣了专业的安保人员来看守，结果却被掉包成了萨卢佐酒业的红酒！
[name="沙雷"]凶杀案的最大嫌疑对象在酒会上被带走，却只是被看在家里，不能出门。
[name="沙雷"]而上门去探望、去慰问，甚至去盘算些不见光勾当的人可一点没见少！
[name="沙雷"]现在新沃尔西尼的人都说他是无辜的，萨卢佐酒业的商品在城里卖得风生水起。
[name="沙雷"]而我，可怜的老拉多斯瓦夫，花了大力气做活动，本想着在这座欣欣向荣的新城里做点小买卖，却一点也没捞到好！
[charslot(slot="m",name="avg_npc_1541_1#2$1",focus="m")]
[name="莱昂图索"]据我所知，《红酒报》在本地发行的国际版连篇累牍地报道这场谋杀案，连带着您的锦标赛也跟着声名大涨。
[name="莱昂图索"]听说您已经在为下一届红酒锦标赛招商了，甚至有从哥伦比亚和莱塔尼亚来的红酒商也表达了参赛的意向。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="沙雷"]可我原本应该获得的绝不止这些，我现在不过是在尽可能地把损失降低到最小罢了。
[charslot(slot="m",name="avg_npc_1541_1#1$1",focus="m")]
[name="莱昂图索"]沙雷先生，我们承诺会公正地按照《新都市管理法案》来管理城内的事务，但我们的政府不是专门为某一位商人服务的。
[name="莱昂图索"]无论是您，还是其他任何人。
[charslot(slot

... (全文35699字符)
```


## 统计

- 总字符数：181040
- 对话行数：1462


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
