# 明日方舟 · 活动剧情 · act43side（24段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act43side」完整剧情脚本（24个文件，2593行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act43side
- 脚本文件数：24

### level_act43side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g3_filmset",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1834_1#6$1",duration=1)]
[Delay(time=2)]
[name="格蕾塔"]......
[name="格蕾塔"]老道尔顿的死，是个意外——这就是结论。
[name="格蕾塔"]医疗组已经收殓他的遗体，调用短驳运输车送回蓝卡坞主城，并向警方报备事故详情。
[name="格蕾塔"]谢莉也已经对剩下的所有道具进行了重新检查，排除了一切隐患。大家稍作休整，今天下午剧组就重启拍摄。
[Dialog]
[charslot]
[charslot(slot = "left", name = "avg_npc_1845_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1847_1#1$1",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "left", focus="l")]
[name="工作人员A"]这么快？
[charslot]
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]有什么问题吗？
[charslot]
[charslot(slot = "left", name = "avg_npc_1845_1#1$1",focus="l")]
[charslot(slot = "right", name = "avg_npc_1847_1#1$1",focus="l")]
[name="工作人员A"]胶卷可以更换，摄影机坏了还有备用的，可这是死了一个人啊，我们才刚刚擦干地面的血迹，就要......
[charslot(slot = "r", focus="r")]
[name="工作人员B"]为什么道尔顿明明是去找道具，最后却找到了一把开刃的真刀？
[name="工作人员B"]到底是谁哄骗酒醉的演员自己去找丢失的道具？还是说，其实是有人故意把它塞到了道尔顿的手里？
[charslot(slot = "left", focus="l")]
[name="工作人员A"]哄骗？故、故意塞？
[name="工作人员A"]道尔顿除了爱喝酒容易耽误事，和剧组的大家也没什么私仇，谁会这样做？
[name="工作人员A"]而且那把刀的形制很普通，剧组的厨房、街面的便利店，甚至我们自己的房间，到处都有差不多的......
[name="工作人员A"]我觉得只是有人无心跟道尔顿提了一嘴，他就自己......
[charslot(slot = "r", focus="r")]
[name="工作人员B"]总之，疑点很多，不是吗？
[charslot]
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]那你只能自己去问道尔顿了，“侦探”小姐。
[charslot]
[charslot(slot = "left", name = "avg_npc_1845_1#1$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_1847_1#1$1",focus="r")]
[name="工作人员B"]......
[charslot]
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]我知道大部分人，包括我，仍沉浸在失去同伴的冲击中，但现在有个最重要的问题摆在面前——
[name="格蕾塔"]拍摄日程已临近尾声。
[name="格蕾塔"]我们都知道蓝卡坞专用于拍摄的移动地块跟移动城市不同。
[name="格蕾塔"]虽然同样受到中心控制塔的管控，但部分调配权限会直接分享给剧组，我们就是受益于此才能将移动地块开出蓝卡坞主城区。
[name="格蕾塔"]租赁合约到期之后，摄影棚会陆续关闭，地块将自动返航。
[name="格蕾塔"]不过，更多操作空间也意味着更高的维护成本。根据我签署的合约，如果要临时延长租赁合约需要支付一大笔违约金——
[name="格蕾塔"]而它会直接分摊到每一个人的工资单上。
[name="格蕾塔"]作为制片人，我需要衡量全体成员的得失，保证我们的剧组正常运转。
[charslot(slot="m",name="avg_npc_1835_1#1$1")]
[name="斯蒂芬"]我同意。
[charslot(slot="m",name="avg_npc_1830_1#1$1")]
[name="米兰妮"]作为主演兼投资人，我也同意。
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]不过，这位“侦探”小姐倒是提醒了我，有些责任确实需要追究。
[charslot(slot="m",name="avg_npc_1834_1#5$1")]
[name="格蕾塔"]道具组长？
[charslot(slot = "m", focus = "n")]
[name="道具组长"]我、我在。
[charslot(slot="m",name="avg_npc_1834_1#5$1")]
[name="格蕾塔"]道具管控，这是你的本职工作，很显然，你存在严重的失职。甚至，整个拍摄过程里，你手下的实习生都比你更早就位。
[charslot(slot = "m", focus = "n")]
[name="道具组长"]抱、抱歉，格蕾塔女士。
[charslot(slot="m",name="avg_npc_1834_1#5$1")]
[name="格蕾塔"]亲爱的，抱歉没有任何意义。
[name="格蕾塔"]即日开除出组。趁我们的移动地块还没开出主城区多远，你可以尽早物色新的工作......别再说什么了，你应该清楚，我已经足够仁慈。
[Dialog]
[playsound(key="$d_avg_walkfast")]
[charslot(slot = "m", focus = "n")]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[Delay(time=0.5)]
[name="格蕾塔"]道具组接下来的工作......我希望交由莫伊拉负责。
[charslot(slot="m",name="avg_npc_1831_1#4$1")]
[name="莫伊拉"]我、我......？
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]如果你不愿意，也可以选择跟你的组长一起离开剧组，当然我相信你不会做那种愚蠢的决定。
[charslot(slot="m",name="avg_npc_1831_1#5$1")]
[name="莫伊拉"]......
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]另外，斯蒂芬，你需要抓紧了。
[name="格蕾塔"]《杜邦夫人之死》的结局还差一口气，这是我们的共识。
[name="格蕾塔"]按照原计划，你应该在上周交出那几场戏的定稿。显然，拍摄进度马上就要追上你的修改速度。
[charslot(slot="m",name="avg_npc_1835_1#7$1")]
[name="斯蒂芬"]我还要身兼导演工作，你知道我们这个剧组其实没多让人省心......
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]还是没有好的灵感？
[charslot(slot="m",name="avg_npc_1835_1#4$1")]
[name="斯蒂芬"]......嗯。
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]这是你的原创剧本，这是你最珍爱的故事，给它一个最好的结束吧，亲爱的。
[charslot(slot="m",name="avg_npc_1830_1#1$1")]
[name="米兰妮"]这也是我最在意的事情。
[charslot(slot="m",name="avg_npc_1830_1#6$1")]
[name="米兰妮"]杜邦夫人在经历一连串的变故后，到底是被哪个洛克菲勒杀死？在什么场景里？以什么姿势？她死前说了什么？
[name="米兰妮"]这直接决定了电影的质量。
[charslot(slot="m",name="avg_npc_1830_1#1$1")]
[name="米兰妮"]她怎么在戏里好看地死，决定了我怎么在蓝卡坞漂亮地重生......
[name="米兰妮"]我把我全部的身家都投给这个项目了，两位。
[charslot(slot="m",name="avg_npc_1835_1#1$1")]
[name="斯蒂芬"]......神会来找我的。
[charslot(slot="m",name="avg_npc_1830_1#6$1")]
[name="米兰妮"]什么？
[charslot(slot="m",name="avg_npc_1835_1#1$1")]
[name="斯蒂芬"]哦，文学评论里有一种说法，说所谓的“灵感”，是指神明直接附身在作者身上，代他写下新生与死亡，毁灭与希望......
[name="斯蒂芬"]总之，请放心，我会完成这个故事。
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]那好，散会，去做准备吧。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1836_1#3$1",duration=0.5)]
[delay(time=1)]
[name="谢莉"]格蕾塔女士！格蕾塔女士！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot = "left", name = "avg_npc_1834_1#6$1")]
[charslot(slot = "right", name = "avg_npc_1836_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot = "right", name = "avg_npc_1836_1#1$1",focus="r")]
[name="谢莉"]我有很重要的事要找你谈——
[charslot(slot = "left", name = "avg_npc_1834_1#6$1",focus="l")]
[name="格蕾塔"]谢莉，我知道你要说什么，但不是现在。
[charslot(slot = "left", name = "avg_npc_1834_1#8$1",focus="l")]
[name="格蕾塔"]我得先去看看卢西恩，他才刚来剧组，第一次参与电影拍摄就经历了这么严重的意外......
[name="格蕾塔"]我得确保他不会落荒而逃。
[charslot(slot = "left", name = "avg_npc_1834_1#6$1",focus="l")]
[name="格蕾塔"]至于你，无论你联想到了什么......忘了它，你想多了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l",duration = 1,afrom=1,ato=0)]
[delay(time=2.5)]
[charslot(slot = "right", name = "avg_npc_1836_1#4$1",focus="r")]
[name="谢莉"]......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[charslot(slot = "left", name = "avg_4191_tippi_1#1$1")]
[charslot(slot = "right", name = "avg_npc_1831_1#4$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[delay(time=1)]
[char

... (全文15586字符)
```

### level_act43side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="56_g12_saluzzowinery",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.2, channel="bgs",fadetime=2)]
[charslot(slot="m",name="avg_npc_1257_1#1$1",duration=1)]
[Delay(time=2)]
[name="拍卖师"]第一次参加本活动的朋友们，如果您期待的是炎国字画或是萨尔贡秘宝，就可以转身离去了。
[name="拍卖师"]“剧本拍卖”，作为蓝卡坞最具特色的活动，这里仅出售尚未成稿的剧本创意、粗纲和相关版权。
[name="拍卖师"]也就是说，不像传统拍卖行会负责鉴定拍品的真假，我们并不保证拍品的实际价值——
[name="拍卖师"]它是否具有市场潜力，是否具有艺术价值，未来会成为叫好又叫座的作品被写进蓝卡坞的历史，还是赔钱货......
[name="拍卖师"]均依赖各位自己去判断。
[name="拍卖师"]为保护拍品的知识产权，请各位收起终端，关闭录音设备，接下来请容许我介绍今晚的第一件拍品——
[name="拍卖师"]《杜邦夫人之死》，这个故事发生于哥伦比亚，讲述了两大家族在时代交替中的兴衰爱恨，最低交易价——十万金券。
[name="拍卖师"]十万！后面先生出价十万......十五！感谢左手边这位年轻美丽的小姐......还有其他来宾竞价吗？
[PlaySound(key="$d_avg_auctionhammer")] 
[name="拍卖师"]十五万一次......
[PlaySound(key="$d_avg_auctionhammer",channel="2")] 
[name="拍卖师"]十五万两次......
[charslot(slot = "m", focus = "n")]
[name="？？？"]六十万。
[Dialog]
[SoundVolume(volume=0.5, channel="bgs",fadetime=2)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="拍卖师"]！
[StopSound(channel="bgs", fadetime=3)]
[name="拍卖师"]（小声）格蕾塔女士！您今天是来砸场子的吗！第一件拍品就开价这么高，后面的气氛只会越来越冷，其他拍品可怎么办......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1834_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="格蕾塔"]按规矩抬价太浪费时间，我只是报出了我心中它值得的价格。
[charslot(slot="m",name="avg_npc_1257_1#1$1")]
[name="拍卖师"]花大价钱在剧本上赌博，是您的作风，但可不经济啊......我听说前段时间您投资制作的电影接二连三赔钱，现在手头不宽裕吧？
[charslot(slot="m",name="avg_npc_1834_1#1$1")]
[name="格蕾塔"]我还付得起你的中介费，快落槌吧，老朋友。
[name="格蕾塔"]我在你这儿看上了一个资质出挑的年轻人，正急着找他聊聊呢。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_1834_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="格蕾塔"]威士忌，不加冰，谢谢。
[name="格蕾塔"]也请你喝一杯，先生？
[Dialog]
[charslot(slot="l",name="char_250_phantom_1#1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="char_250_phantom_1#1",focus="l")]
[name="卢西恩"]我的医生规劝我不要饮酒。
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]听口音......你是萨尔贡人？
[name="格蕾塔"]真有意思，你这张冷峻忧郁的脸，明明是标准的维多利亚人长相。
[charslot(slot="l",name="char_250_phantom_1#6",focus="l")]
[name="卢西恩"]（萨尔贡语）我刚涉过萨尔贡的黄沙。
[name="卢西恩"]（口音纯正的维多利亚语）但确实生于维多利亚。
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]你的语言切换十分流畅，口音也挑不出毛病。不过除了这两个国家，我还在你身上发现了其他文化的痕迹和习惯。
[charslot(slot="l",name="char_250_phantom_1#6",focus="l")]
[name="卢西恩"]玻利瓦尔、叙拉古、莱塔尼亚、雷姆必拓......现在又来到蓝卡坞。
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]——全泰拉最具娱乐性的移动城市，气候宜人、阳光充足的拍摄地。你为什么来到这里？
[name="格蕾塔"]度假、游学？还是像外面那些慕名而来，最终都挤在群演市场的人们一样，在寻找工作机会？
[charslot(slot="l",name="char_250_phantom_1#2",focus="l")]
[name="卢西恩"]找一个人。
[charslot(slot="l",name="char_250_phantom_1#7",focus="l")]
[name="卢西恩"]漫长的时间里，我循着他的影子，走过许多地方。
[charslot(slot="r",name="avg_npc_1834_1#3$1",focus="r")]
[name="格蕾塔"]哦？什么人？我认识所有在主城区和移动地块上拍戏的剧组，说不定能帮上你的忙。
[charslot(slot="l",name="char_250_phantom_1#6",focus="l")]
[name="卢西恩"]不劳费心。
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]好吧，好吧......可惜......
[charslot(slot="l",name="char_250_phantom_1#6",focus="l")]
[name="卢西恩"]如果你没有别的事......
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]格蕾塔·斯通，我的名字，蓝卡坞电影制片人......在这一行的新闻里出现次数还挺多的。
[name="格蕾塔"]我本来还以为你是哪里的贵公子，或是来碰碰运气的电影学院的学生，想着邀请你加入我的剧组。
[name="格蕾塔"]参加蓝卡坞剧本拍卖会的人多少都会对艺术抱有热情，再加上你的气质很独特......
[charslot(slot="l",name="char_250_phantom_1#1",focus="l")]
[name="卢西恩"]我曾在维多利亚的一个小剧团担任演员。
[charslot(slot="r",name="avg_npc_1834_1#2$1",focus="r")]
[name="格蕾塔"]我就说我的眼光不可能错，你天生适合银幕！
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]不过现在说这些也没用，既然你有必须要做的事，看来今天我只能空手而归了。
[charslot(slot="l",name="char_250_phantom_1#1",focus="l")]
[name="卢西恩"]我能否看看剧本？
[charslot(slot="r",name="avg_npc_1834_1#2$1",focus="r")]
[name="格蕾塔"]当然！
[Dialog]
[playsound(key="$d_avg_paper1")]
[charslot(slot="l",name="char_250_phantom_1#6",focus="l")]
[delay(time=2)]
[charslot(slot="l",name="char_250_phantom_1#4",focus="l")]
[name="卢西恩"]......
[charslot(slot="r",name="avg_npc_1834_1#1$1",focus="r")]
[name="格蕾塔"]这份剧本原稿只是一个开始，我还会投入更多人力、资金、时间，让它成为轰动影史的旷世佳作。
[name="格蕾塔"]哪怕你只扮演一个小角色，只在一幕戏里登场，也能出彩。
[name="格蕾塔"]你身上那些特殊的小问题也不用担心。蓝卡坞出台了专门的感染者演员劳动保护条例，只要你支付了足够的保险金——
[charslot(slot="l",name="char_250_phantom_1#6",focus="l")]
[name="卢西恩"]叫我卢西恩吧，格蕾塔女士。
[name="卢西恩"]我会考虑你的提议。
[Dialog]
[stopmusic(fadetime=2)]
[CameraEffect(effect="Grayscale", fadetime=2, keep=true, initamount=0, amount=1, block=true)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="62_g10_dormitory",screenadapt="coverall")]
[charslot(slot="r",name="avg_npc_1834_1#4$1")]
[charslot(slot="l",name="avg_npc_1828_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[charslot(slot="r",name="avg_npc_1834_1#4$1",focus="r")]
[name="格蕾塔"]我必须再次向你致歉，卢西恩。
[name="格蕾塔"]你初次接触电影，深思熟虑了很长时间才下定决心在演员合约上签字。我本应像我承诺的那样，让你体会到拍摄的乐趣。
[name="格蕾塔"]谁能想到，你在蓝卡坞的第一场戏就亲历了如此可怕的事故......
[name="格蕾塔"]如果你需要一些时间来调整自己的状态，我很理解。我会让谢莉更改你下一场戏的拍摄时间。
[name="格蕾塔"]但要是你想直接毁约离开剧组，那恐怕行不通。移动地块已经开出了短驳运输车的调用范围，直到租赁合约到期才会返航......
[charslot(slot="l",name="avg_npc_1828_1#2$1",focus="l")]
[name="卢西恩"]我不会离开。
[name="卢西恩"]也不用更改日程。
[charslot(slot="r",name="avg_npc_1834_1#3$1",focus="r")]
[name="格蕾塔"]不用？这起事故造成的创伤性记忆很可能会阻碍你的表演，甚至影响你的生活。
[charslot(slot="l",name="avg_npc_1828_1#1$1",focus="l")]
[name="卢西恩"]舞台之上，意外于我并不陌生。
[charslot(slot="r",name="avg_npc_1834_1#4$1

... (全文9488字符)
```

### level_act43side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g2_setting_rooftop",screenadapt="coverall")]
[focusout(duration=0, type="bg", from=0, to=0.3)]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07,name = "avg_npc_1830_1#1$1",afrom=0,ato=0)]
[charslot(slot = "l",posfrom = "0,0", posto = "0,-70",duration = 0)]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07,name = "avg_npc_1838_1#1$1",afrom=0,ato=0)]
[charslot(slot = "r",posfrom = "0,0", posto = "0,-60",duration = 0)]
[backgroundTween(xScaleFrom=1, yScaleFrom=1, xScaleTo=1.3, yScaleTo=1.3, duration=0, block=false)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.1,block=false, fadetime=0)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.1,block=true, fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[Delay(time=2)]
[charslot(slot = "left", afrom=0,ato=1,duration=1)]
[charslot(slot = "right",afrom=0,ato=1,duration=1)]
[delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1838_1#1$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]忘记不幸遇害的兄长，跟我私奔吧，杜邦夫人！
[charslot(slot = "left", name = "avg_npc_1830_1#5$1",focus="l",posfrom = "0,0", posto = "0,-70")]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="l")]
[name="米兰妮"]清醒一点，第二个洛克菲勒！
[name="米兰妮"]你也听到了那个信使说的，根本不存在什么“杜邦夫人”，什么高贵、优雅、知性......所有我身上你们所爱的东西都是无根的浮萍......
[charslot(slot = "left", name = "avg_npc_1830_1#4$1",focus="l",posfrom = "0,0", posto = "0,-70")]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="l")]
[name="米兰妮"]我不配成为你们兄弟三人中任何一人的妻子。
[charslot(slot = "right", name = "avg_npc_1838_1#1$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]我爱你，就算你不姓杜邦我也依然爱你！
[charslot(slot = "right", name = "avg_npc_1838_1#5$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]是你的兄长，那个死掉的家伙一直在利用你，你被蒙在鼓里，你也是受害者，你又何苦为此自责？
[charslot(slot = "left", name = "avg_npc_1830_1#4$1",focus="l",posfrom = "0,0", posto = "0,-70")]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="l")]
[name="米兰妮"]可是......
[charslot(slot = "right", name = "avg_npc_1838_1#6$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]可是？
[charslot(slot = "left", name = "avg_npc_1830_1#4$1",focus="l",posfrom = "0,0", posto = "0,-70")]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="l")]
[name="米兰妮"]现在会客厅挤满了前来吊唁的宾客，虽然“杜邦”只是一个虚名，但于情于理我都不应该当着他们的面离开......
[charslot(slot = "right", name = "avg_npc_1838_1#1$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]我有方法能让我们现在就离开宅邸，从此再也不理睬家族纷争。
[charslot(slot = "left", name = "avg_npc_1830_1#6$1",focus="l",posfrom = "0,0", posto = "0,-70")]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="l")]
[name="米兰妮"]这要如何做到？
[charslot(slot = "right", name = "avg_npc_1838_1#1$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]你忘记了？我是一名军人，亲爱的。
[name="迈克尔"]你看！
[charslot(slot = "left", name = "avg_npc_1830_1#3$1",focus="l",posfrom = "0,0", posto = "0,-70")]
[charslot(slot = "l",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="l")]
[name="米兰妮"]这、这是......
[charslot(slot = "right", name = "avg_npc_1838_1#1$1",focus="r",posfrom = "0,-60", posto = "0,-60")]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07)]
[charslot(slot = "right",focus="r")]
[name="迈克尔"]我在这座宅邸的杂物间搜集了材料，制作了这副钢索......抓紧吊缆，我们就能从这个露台，直接飞跃花园，抵达屋后的森林。
[name="迈克尔"]跟我走吧，去一个不在乎财富和阶级的地方！
[Dialog]
[charslot(duration=1)]
[playsound(key="$d_avg_clothmovement")]
[CameraShake(duration=0.3, xstrength=0, ystrength=10, vibrato=5, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", action="jump",posto = "0,-300",power=50,times=1,duration = 1)]
[charslot(slot = "r", action="jump",posto = "0,-300",power=50,times=1,duration = 1)]
[delay(time=1)]
[playsound(key="$d_avg_sldrsldng", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2.5)]
[delay(time=1)]
[name="米兰妮"]啊，军人先生，你的方法还是太野蛮了！
[name="米兰妮"]万一滑轮卡住，我们会悬停在半空中好几个小时，直到有人发现我们......或者绳索断裂直接坠入森林......
[name="迈克尔"]相信我，装置非常安全。我不会让你受伤的，亲爱的。
[stopmusic(fadetime=2)]
[name="米兰妮"]真、真的吗，洛克菲勒？我、我觉得我要掉下去了——
[Dialog]
[delay(time=1)]
[playsound(key="$d_avg_wiatear")]
[CameraShake(duration=2, xstrength=10, ystrength=30, vibrato=10, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[PlayMusic(intro="$plot_intro", key="$plot_loop",volume=0.6)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="谢莉"]啊——！
[Dialog]
[delay(time=1)]
[Sticker(id="st1", text="钢索、吊缆、悬挂、坠落。",x=200,y=300, alignment="center", size=24, delay=0.04, width=900,duration=1,block=false)]
[delay(time=1.5)]
[Sticker(id="st3", text="坠落。",x=307,y=350, alignment="center", size=24, delay=0.04, width=900,duration=8,block=false)]
[delay(time=1)]
[Sticker(id="st4", text="坠落。",x=307,y=410, alignment="center", size=24, delay=0.04, width=900,duration=15,block=false)]
[delay(time=2)]
[playsound

... (全文19403字符)
```

### level_act43side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[bgeffect(name="$eb_oldtv",layer=1)]
[Background(image="62_g6_proproom",screenadapt="coverall")]
[playsound(key="$d_avg_oldtvelectricity", loop=true, channel="c")]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=3, block=true)]
深夜，本应空无一人的道具间传来细碎的声响和被压抑的悲鸣。
幽暗的角落里，道具假人没有五官的面孔被闪烁的荧光打亮。
蒂比抱着靠枕缩在沙发里，持刀的凶手发出邪恶的笑声，刀尖闪着刺眼的白光，下一秒——
[bgeffect]
[StopSound(channel="c", fadetime=0)]
[Dialog]
[charslot(slot="m",name="avg_4191_tippi_1#8$1")]
[PlaySound(key="$d_avg_orangefall")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="蒂比"]啊——
[PlaySound(key="$d_avg_clothmovement",volume=0.5)]
[charslot(slot="m",name="avg_npc_1836_1#3$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="谢莉"]啊——
[charslot(slot="m",name="avg_npc_1831_1#1$1")]
[name="莫伊拉"]......
[charslot]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$normal_loop", volume=0.6)]
[charslot(slot="m",name="avg_4191_tippi_1#1$1")]
[name="蒂比"]经典！震撼！不愧是我最喜欢的恐怖电影，哪怕是三十多年前的小成本制作，跟现在的新片比起来也毫不逊色！
[charslot(slot="m",name="avg_npc_1836_1#2$1")]
[name="谢莉"]呼......还是看恐怖片比较能发泄情绪，我好像没有那么焦虑了。谢谢你的邀请，小蒂比。
[charslot(slot="m",name="avg_4191_tippi_1#1$1")]
[name="蒂比"]大声喊出来舒服多了吧，谢莉小姐？我就说你不是故意打断拍摄的，只是最近神经太紧绷了。
[charslot(slot="m",name="avg_npc_1836_1#2$1")]
[name="谢莉"]嗯，虽然还有一些问题没解决......但今晚就让我忘记它们吧。接下来我们看什么？
[charslot(slot="m",name="avg_4191_tippi_1#1$1")]
[name="蒂比"]应有尽有，恐怖电影之夜才刚刚开始呢！
[charslot(slot="m",name="avg_4191_tippi_1#2$1")]
[name="蒂比"]咦？莫丽，你怎么一直不说话，是不喜欢这部电影吗？
[charslot(slot="m",name="avg_npc_1831_1#9$1")]
[name="莫伊拉"]我在想......
[name="莫伊拉"]电影里出现的武器刀刃太过轻薄，如果是我就干脆设计更特殊的武器，在侧面加上血槽，视觉上的冲击力也更强！
[charslot(slot="m",name="avg_4191_tippi_1#8$1")]
[name="蒂比"]别再想工作了！莫丽！你是不是跟谢莉小姐待太久了！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4198_christ_1#2$1",duration=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_MCcat_1")]
[name="Miss.Christine"]喵~
[charslot(slot="m",name="avg_4191_tippi_1#1$1")]
[name="蒂比"]欸？你怎么在这里呀，神秘的小家伙。
[charslot(slot="m",name="avg_4198_christ_1#1$1")]
美丽的生物缓步走到两个小女孩中间，展示般地伸了一个懒腰，端坐在沙发前。
[charslot(slot="m",name="avg_4191_tippi_1#1$1")]
[name="蒂比"]莫丽你看，她好像真的很喜欢我们欸。那就跟我们一起看电影吧！可别被吓到了哦。
[Dialog]
[charslot]
[PlaySound(key="$phonevibration")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4191_tippi_1#4$1")]
[name="蒂比"]嗯？谁的终端响了？莫丽，是你的吗？
[charslot(slot="m",name="avg_npc_1831_1#3$1")]
[name="莫伊拉"]不是啊。
[charslot(slot="m",name="avg_npc_1836_1#4$1")]
[name="谢莉"]......
[charslot(slot="m",name="avg_npc_1836_1#1$1")]
[name="谢莉"]抱歉，我得......先走了。
[Dialog]
[playsound(key="$d_avg_walkfast")]
[charslot(slot = "m",posfrom = "0,0", posto = "200,0",duration = 1,afrom=1,ato=0)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_1831_1#4$1")]
[name="莫伊拉"]她的脸色好差，不会是因为白天的事被格蕾塔女士问责了吧？
[charslot(slot="m",name="avg_4191_tippi_1#9$1")]
[name="蒂比"]莫丽，明天我们再帮她分担一些工作吧？谢莉小姐看上去真的很疲惫。
[charslot(slot="m",name="avg_npc_1831_1#9$1")]
[name="莫伊拉"]嗯。
[charslot(slot="m",name="avg_4191_tippi_1#1$1")]
[name="蒂比"]来！我们接着看电影，下一部恐怖片拿过最佳设计奖哦，置景、道具和武器都做得非常酷......
[charslot]
荧光闪烁，两个女孩再次沉浸在新的惊悚故事里，丝毫没注意到脚边的Miss.Christine也已悄无声息地离开。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="62_g1_setting_lobby",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[playsound(key="$d_avg_walkfast")]
[charslot(slot = "l",posfrom = "-200,0", posto = "0,0",duration = 1,name="avg_npc_1836_1#6$1")]
[delay(time=1.5)]
[name="谢莉"]......
[Dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "100,0",duration = 0.5)]
[charslot(slot = "r",posfrom = "100,0", posto = "0,0",duration = 0.5,name="avg_npc_1838_1#1$1")]
[delay(time=0.5)]
[CameraShake(duration=0.3, xstrength=15, ystrength=20, vibrato=10, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l",name="avg_npc_1836_1#6$1")]
[charslot(slot = "l",posfrom = "100,0", posto = "0,0",duration = 0.5)]
[playsound(key="$bodyfalldown2",volume=0.6)]
[delay(time=1)]
[charslot(slot = "r",name="avg_npc_1838_1#6$1",focus="r")]
[name="迈克尔"]谢莉？你不是应该在跟小蒂比她们看电影吗，急匆匆的是要到哪里去？
[dialog]
[charslot(slot = "l",name="avg_npc_1836_1#4$1",focus="all")]
[delay(time=1)]
[charslot(slot = "m", focus = "n")]
语气亲昵的男子注意到谢莉的右手紧紧抓着终端。
[charslot(slot = "r",name="avg_npc_1838_1#1$1",focus="r")]
[name="迈克尔"]哦，我知道了......突然收到了约会邀请？
[name="迈克尔"]一会儿可别对对方露出这样沉重的表情啊，他会伤心的。
[charslot(slot = "l",name="avg_npc_1836_1#1$1",focus="l")]
[name="谢莉"]跟你无关。
[charslot(slot = "r",name="avg_npc_1838_1#1$1",focus="r")]
[name="迈克尔"]你的嘴唇在颤抖。你很冷，还是说在害怕？
[name="迈克尔"]可怜的小人儿，你也跟我一样，被道尔顿的意外吓坏了是不是？
[name="迈克尔"]别忧心了，有你这样认真的统筹在，我相信接下来一切都会很顺利的。来，让我给你个拥抱，你会暖和一些......
[Dialog]
[charslot(slot = "r",posfrom = "0,0", posto = "-100,0",duration = 1)]
[delay(time=1)]
[playsound(key="$d_avg_clothmovement",volume=0.6)]
[CameraShake(duration=0.2, xstrength=15, ystrength=5, vibrato=10, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l",posfrom = "0,0", posto = "50,0",duration = 0.3)]
[charslot(slot = "r",posfrom = "-100,0", posto = "100,0",duration = 0.5)]
[delay(time=1)]
[charslot(slot = "l",name="avg_npc_1836_1#1$1",focus="l")]
[name="谢莉"]“跟你一样”？
[name="谢莉"]我从你的甜言蜜语里可听不到半点恐惧。
[charslot(slot = "l",name="avg_npc_1836_1#5$1",focus="l")]
[name="谢莉"]你的忘性已经大到能将五年前发生的事从脑子里抹得一干二净了吗？
[name="谢莉"]我没办法“跟你一样”没心没肺......别忘了，你也要为当初的坠亡事故负责。
[charslot(slot = "r",name="avg_npc_1838_1#5$1",focus="r")]
[name="迈克尔"]......
[Dialog]
[charslot(slot = "l",name="avg_npc_1836_1#1$1")]
[playsound(key="$d_avg_walkfast")]
[charslot(slot = "l",posfrom = "50,0", posto = "300,0",duration = 1,afrom=1,ato=0)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="62_g13_directorstudio",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadeti

... (全文12929字符)
```

### level_act43side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g9_outsidestudio_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$drift_intro",key="$drift_loop", volume=0.6)]
[charslot(slot="m",name="avg_4191_tippi_1#9$1",duration=1)]
[Delay(time=2)]
[name="蒂比"]......谢莉小姐死了。
[charslot]
[Dialog]
[charslot(slot="r",name="avg_npc_1839_1#3$1",duration=1)]
[charslot(slot="l",name="avg_npc_1838_1#3$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1838_1#3$1",focus="l")]
[name="迈克尔"]怎么会？
[charslot(slot="r",name="avg_npc_1839_1#3$1",focus="r")]
[name="玛丽昂"]先是道尔顿，再是谢莉......我的天，这到底是怎么一回事？
[charslot]
[charslot(slot="m",name="avg_4191_tippi_1#5$1")]
[name="蒂比"]我说，谢莉小姐死了。
[charslot]
[charslot(slot="r",name="avg_npc_1839_1#6$1",focus="r")]
[charslot(slot="l",name="avg_npc_1838_1#3$1",focus="r")]
[name="玛丽昂"]你这是什么语气？
[name="玛丽昂"]谢谢你专程来拦住我和迈克尔，通知我们剧组又出了意外，我们也很震惊。
[charslot]
[charslot(slot="m",name="avg_4191_tippi_1#5$1")]
[name="蒂比"]谢莉小姐死前见到的最后一个人，是迈克尔先生。
[charslot]
[charslot(slot="l",name="avg_npc_1838_1#2$1",focus="l")]
[charslot(slot="r",name="avg_npc_1839_1#6$1",focus="l")]
[name="迈克尔"]......
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="r")]
[name="玛丽昂"]你不要血口喷人，小蒂比。
[name="玛丽昂"]谢莉昨天明明参加了你的观影会，和你还有莫伊拉待在一起，我都听说了。
[charslot]
[charslot(slot="m",name="avg_4191_tippi_1#9$1")]
[name="蒂比"]正因为昨晚谢莉小姐是和我们在一起，正因为她中途收到了一条讯息离开，我和莫丽没有多问，也没有陪她，后来出了那样的事情......
[charslot(slot="m",name="avg_4191_tippi_1#5$1")]
[name="蒂比"]所以我和莫丽才必须调查清楚到底发生了什么，我走访了很多人——
[charslot(slot="m",name="avg_4191_tippi_1#6$1")]
[name="蒂比"]有工作人员看到了，她在离那个仓库不远的摄影棚和你会面了！
[charslot]
[charslot(slot="l",name="avg_npc_1838_1#5$1",focus="l")]
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="l")]
[name="迈克尔"]我们只是偶遇！
[name="迈克尔"]我看她一副魂不守舍的样子，以为她还在为中断拍摄的事愧疚，想安慰安慰她。
[charslot(slot="l",name="avg_npc_1838_1#4$1",focus="l")]
[name="迈克尔"]唉，没想到她真会想不开。
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="r")]
[name="玛丽昂"]安慰，摄影棚，就你们两个？
[charslot(slot="l",name="avg_npc_1838_1#3$1",focus="l")]
[name="迈克尔"]宝贝儿，相信我。我心里只有你一个。
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="r")]
[name="玛丽昂"]闭嘴！
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]所以，真的是你杀了谢莉？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="bg_warehouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1844_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="摄影助理"]才几天，已经发生两起意外了？
[charslot(slot="m",name="avg_npc_1846_1#2$1")]
[name="倒霉的场工"]而且都闹出了人命。蓝卡坞那么多剧组招工，我怎么偏偏挑了这个地方，唉，真倒霉......
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[name="摄影助理"]行了行了。无故翻倒的油漆桶，摄影棚外窜过的黑影，甚至连城际网络信号失灵，你都能怪到自己的运气上。
[charslot(slot="m",name="avg_npc_1844_1#5$1")]
[name="摄影助理"]我倒觉得是我们走大运了！事故现场的一手资料能在娱乐周刊卖出一笔好价钱——
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[name="摄影助理"]让开一点，我看不清谢莉遗体的细节了。
[charslot(slot="m",name="avg_npc_1846_1#1$1")]
[name="倒霉的场工"]别看了......我们得去摄影棚帮忙了。
[charslot(slot="m",name="avg_npc_1844_1#5$1")]
[name="摄影助理"]你先去，霍汀。我得把这些都记下来！
[charslot(slot="m",name="avg_npc_1846_1#1$1")]
[name="倒霉的场工"]......
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[playsound(key="$d_avg_penrustle")]
[Delay(time=1)]
[name="摄影助理"]......听阿布纳说，谢莉以前就神神道道的。难不成是道尔顿的死对她的冲击太大，所以自寻短见？
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[name="摄影助理"]合理但略显无聊。
[charslot(slot="m",name="avg_npc_1844_1#5$1")]
[name="摄影助理"]要是另有隐情......嘿嘿，那我上半年的房租都不用愁了，谁还要当整天举收音挑杆的人形支架啊！
[charslot(slot="m",name="avg_npc_1844_1#6$1")]
[name="摄影助理"]嗯？
[charslot(slot="m",name="avg_npc_1844_1#3$1")]
[name="摄影助理"]医疗小组不是说谢莉是被冻死的吗，那她的左手掌心怎么有那么多伤口？
[charslot(slot="m",name="avg_npc_1844_1#2$1")]
[name="摄影助理"]嘶——看着真瘆人，难道是某种诅咒仪式......
[charslot(slot = "m", focus = "n")]
[name="？？？"]并非诅咒，而是自我挣扎的痕迹。
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[name="摄影助理"]......挣扎？
[name="摄影助理"]谢莉不是被精神压力击垮，自暴自弃才走进冷库的吗？难道真的有内幕——
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1844_1#3$1")]
[name="摄影助理"]卢西恩先生！你走路怎么没声啊！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1828_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="卢西恩"]以疼痛抵抗幻觉，是我提出的建议。
[name="卢西恩"]谢莉小姐耳中回响着往事的遗音，但她仍想完成自己的工作，为电影带来圆满的结局。
[charslot(slot="m",name="avg_npc_1828_1#2$1")]
[name="卢西恩"]她不会因绝望寻死，自伤的血痂就是最好的印证。
[charslot(slot="m",name="avg_npc_1828_1#4$1")]
[name="卢西恩"]只是这次，疼痛没能引她逃脱幻境。
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[name="摄影助理"]那个固执、神经质、难以沟通的谢莉听从了你提出的建议？不可置信......
[name="摄影助理"]你似乎很了解她啊，卢西恩先生。
[charslot(slot="m",name="avg_npc_1828_1#1$1")]
[name="卢西恩"]谈不上。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_1839_1#1$1")]
[charslot(slot="l",name="avg_npc_1838_1#3$1")]
[Background(image="62_g9_outsidestudio_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[charslot(slot="l",name="avg_npc_1838_1#3$1",focus="l")]
[name="迈克尔"]哪儿跟哪儿啊！
[name="迈克尔"]我求爱不成就杀了谢莉？亲爱的，你怎么会想到这种无稽之谈？
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]......
[charslot(slot="l",name="avg_npc_1838_1#6$1",focus="l")]
[name="迈克尔"]啊对了对了，小蒂比，你刚刚不是说谢莉是突然接到了一条讯息离开的吗？
[name="迈克尔"]我当时也注意到了她拿着终端。所以，一定是那个给她发消息的人诱杀了她，对吧？
[charslot]
[charslot(slot="m",name="avg_4191_tippi_1#10$1")]
[name="蒂比"]难道那个人不是你？
[charslot]
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[charslot(slot="l",name="avg_npc_1838_1#6$1",focus="r")]
[name="玛丽昂"]我也需要一个解释，迈克尔。
[charslot]
[charslot(slot="m",name="avg_4191_tippi_1#4$1")]
[name="蒂比"]虽然冷库的低温环境冻坏了终端，记录已经无法修复，但我们的终端都是剧组统一配备的，只有同组成员在联络名单里......
[charslot]
[charslot(slot="m",name="avg_npc_1838_1#5$1")]
[nam

... (全文10667字符)
```

### level_act43side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g3_filmset",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$m_bat_imprisonment_intro",key="$m_bat_imprisonment_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1844_1#3$1",duration=1)]
[Delay(time=1.5)]
[name="摄影助理"]格蕾塔女士，我们要遭遇天灾的消息到底是不是真的？
[name="摄影助理"]蓝卡坞的城际网络覆盖范围极大，即使地块开出主城区也能接收到天灾预警！为什么我们的终端没收到提醒？
[charslot(slot="m",name="avg_npc_1846_1#4$1")]
[name="倒霉的场工"]所以最近的通讯信号时好时坏，难道不是因为我的运气，而是——
[charslot(slot="m",name="avg_npc_1844_1#3$1")]
[name="摄影助理"]通讯设备被人蓄意破坏！
[charslot(slot="m",name="avg_npc_1834_1#5$1")]
[name="格蕾塔"]好了！无凭无据的怀疑是没有任何意义的。
[charslot(slot="m",name="avg_npc_1844_1#3$1")]
[name="摄影助理"]无凭无据？
[Dialog]
[charslot(slot="m",name="avg_npc_1844_1#1$1")]
[PlaySound(key="$d_avg_paper1")]
[Delay(time=1)]
[name="摄影助理"]我偶然在办公室里找到一些纸条，拼接之后能看出一份是特里蒙大学出具的天灾预测报告，另一份则是分镜表。
[name="摄影助理"]格蕾塔·斯通女士，上面可有你的亲笔签字，你到底想做什么？
[charslot(slot="m",name="avg_npc_1843_1#1$1")]
[name="阿布纳"]小子，让我看看。
[Dialog]
[PlaySound(key="$d_avg_paper2")]
[Delay(time=1)]
[name="阿布纳"]我是摄影师，我怎么不知道新增了这几场戏？
[name="阿布纳"]为什么要在地块边缘布置摄影机？那里没有任何布景......等等，我明白了。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_1843_1#8$1")]
[name="阿布纳"]格蕾塔！你*蓝卡坞片场术语*故意的？你瞒着我们这么大的事儿，你想干什么？
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]......
[charslot(slot="m",name="avg_npc_1846_1#6$1")]
[name="倒霉的场工"]阿布纳，冷静一点......格蕾塔女士可能只是没来得及把最新的排期告诉你，谢莉小姐刚刚过世，很多事情来不及交接......
[charslot(slot="m",name="avg_npc_1843_1#8$1")]
[name="阿布纳"]你还替这个疯女人说话？她想让移动地块无限接近外层风暴拍摄实景天灾！我们所有人的命都有可能搭进去！
[charslot]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_smashtable")]
横眉怒目的摄影师将拍摄设备重重扔在地上。
[charslot(slot="m",name="avg_npc_1843_1#8$1")]
[name="阿布纳"]我受够了！我现在就要离开这个鬼地方！
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]你还是这么冲动，阿布纳。
[charslot(slot="m",name="avg_npc_1843_1#8$1")]
[name="阿布纳"]冲动？疯了的是你！
[charslot(slot="m",name="avg_npc_1843_1#4$1")]
[name="阿布纳"]为了弥补五年前那部电影票房的惨淡，你搭进去多少自己的资产？后来你的投资屡屡不顺，想用这部电影翻身......
[name="阿布纳"]告诉我，要是这部电影也变成赔钱货，道尔顿和谢莉的意外是不是会变成你利用的对象？就跟当时那个坠亡的小演员一样！
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]别这么着急，阿布纳。
[name="格蕾塔"]你记我的事情倒是清楚，但你自己的呢？这是你近三年来进的第几个剧组？第一个吧？
[charslot(slot="m",name="avg_npc_1834_1#5$1")]
[name="格蕾塔"]邋遢、易怒、毫无职业操守。有哪个剧组还会像我一样把拍摄设备放心地交到你手上？还有哪些活动会雇你担当兼职摄影师？
[name="格蕾塔"]离开？当然可以，作为老朋友我甚至可以不要你支付违约金。但你又能去哪里，阿布纳？
[charslot(slot="m",name="avg_npc_1843_1#8$1")]
[name="阿布纳"]你管得着吗？大不了——
[charslot(slot="m",name="avg_npc_1834_1#5$1")]
[name="格蕾塔"]跳槽？转行？再也不荼毒任何一块镜头，任何一台摄影设备？你可以说些言过其实的狠话，发恶毒的誓。
[name="格蕾塔"]但你要是真的嫉恶如仇，为什么还会答应我的邀约，出现在这里？
[charslot(slot="m",name="avg_npc_1843_1#4$1")]
[name="阿布纳"]......
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]还走吗？能走吗？
[charslot]
阿布纳没有拿起设备，也没有离开。他被生活和往事扣押在原地，沉默伫立。
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]你终于冷静下来了。
[name="格蕾塔"]往好的地方想想吧。如果这部电影拍成了，说不定你能再拿几个最佳摄影奖。等你片约蜂拥而至的时候，大可拒绝再次加入我的剧组。
[charslot(slot="m",name="avg_npc_1843_1#9$1")]
[name="阿布纳"]别说那些梦话，格蕾塔。
[name="阿布纳"]我从五年前开始就不相信了。
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]......
[name="格蕾塔"]好了各位，我知道因为最近的两起意外，有人想起了我们共同经历过的往事，有人听说了一些似是而非的传闻。
[name="格蕾塔"]为了我们之后的拍摄能团结一心，我正式向诸位作出回应。
[name="格蕾塔"]现在剧组中大多数人，都是我五年前的合作对象。当时拍摄现场因设备老化，发生了一件令人痛心的意外——
[charslot(slot="m",name="avg_npc_1834_1#4$1")]
[name="格蕾塔"]一位年轻的新人演员劳拉不幸命丧当场。
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]你们可以查阅警方的调查结果，一切公开透明，绝无隐情。
[name="格蕾塔"]拍摄天灾这一决定与当年的意外唯一能称为联系的地方是，我在五年前得到了非常宝贵的一项经验——
[name="格蕾塔"]我们缺少的从来不是技术，而是胆量。
[name="格蕾塔"]当然，这不意味着我将各位的安危置之度外。
[name="格蕾塔"]我们的移动地块离开蓝卡坞主城区前，我拜访了特里蒙大学的天灾预测专家。
[name="格蕾塔"]我从他手中获得了一份十分精准的分析报告，并将数据输入地块导航系统中测试过多次。拍摄地块会与天灾保持安全距离。
[name="格蕾塔"]紧急逃生舱内的陆行艇不会设置使用权限，任何一位剧组工作人员只要觉得生命受到威胁就可以自行取用。
[name="格蕾塔"]而我会成为最后一个离开移动地块的人。
[name="格蕾塔"]没有问题的话，散会。
[Dialog]
[charslot]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.8, channel="bgs",fadetime=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1844_1#1$1",posfrom = "0,0", posto = "200,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "m", focus = "n")]
[name="格蕾塔"]你，等等。
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_1834_1#6$1",duration=1)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1844_1#6$1",focus="m")]
[name="摄影助理"]格、格蕾塔女士......
[name="摄影助理"]我是不会因为把消息抖出来而道歉的！
[charslot(slot="l",name="avg_npc_1834_1#6$1",focus="l")]
[name="格蕾塔"]不用紧张，我只想知道你是从谁那里拿到的文件。
[charslot(slot="m",name="avg_npc_1844_1#6$1",focus="m")]
[name="摄影助理"]都说了，是我自己——
[charslot(slot="l",name="avg_npc_1834_1#5$1",focus="l")]
[name="格蕾塔"]跳过撒谎的环节。你没那个能力，我没那么多时间。
[charslot(slot="m",name="avg_npc_1844_1#6$1",focus="m")]
[name="摄影助理"]......对于情报提供者我有义务保护他们的隐私......
[charslot(slot="l",name="avg_npc_1834_1#5$1",focus="l")]
[name="格蕾塔"]扰乱片场拍摄违反了合同中的第二和第五款条例，你想从金融终端里看到处罚结果吗？
[charslot(slot="m",name="avg_npc_1844_1#3$1",focus="m")]
[name="摄影助理"]但出于一些特殊原因也可以对外透露——
[charslot(slot="m",name="avg_npc_1844_1#1$1",focus="m")]
[name="摄影助理"]（小声）是卢西恩先生。
[charslot]
穿过嘈杂的人群和杂乱的器材，格蕾塔一眼看到了游离于闹剧之外的那个人。
[charslot(slot="m",name="avg_npc_1828_1#1$1")]
[name="卢西恩"]......
[charslot(slot = "m", focus = "n")]
菲林男人坦然接受格蕾塔冷峻的目光，微微颔首，向她致意。
[charslot]
[charslot(slot="m",name="avg_npc_1834_1#6$1")]
[name="格蕾塔"]......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[charslot(slot="m",name="avg_4191_tippi_1#8$1")]
[Background(image="62_g9_outsidestudio_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$distressed_intro",key="$distressed_loop", volume=0.6)]
[name="蒂比"]莫丽，你是说，昨天晚上迈克尔要见的人是你？
[charslot(slot="m",name="avg_npc_1831_1#5$1")]
[name="莫伊拉"]......嗯。
[cha

... (全文8715字符)
```

### level_act43side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="62_g2_setting_rooftop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1848_1#1$1",duration=1)]
[Delay(time=2)]
[name="劳拉"]道尔顿先生，您竟然真的替我多要了一场戏......还是空中悬吊的特技镜头？
[name="劳拉"]之前我怎么求斯蒂芬导演他都不愿意，您一说他竟然就答应了？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1837_1#2$1",duration=1)]
[Delay(time=1.5)]
[name="道尔顿"]小意思。我是格蕾塔女士亲自请来的男主演，斯蒂芬怎么敢不答应我的要求？
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[name="劳拉"]我还是第一次接触威亚......一定会好好地珍惜这次机会的！我先去准备了！
[charslot(slot="m",name="avg_npc_1837_1#2$1")]
[name="道尔顿"]去吧。
[Dialog]
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2.5)]
[charslot(duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1837_1#6$1")]
[name="道尔顿"]装得倒谦卑，要是我不知道你暗地里找斯蒂芬想动我主演的戏份，大概就被你骗过去了。
[charslot(slot="m",name="avg_npc_1837_1#2$1")]
[name="道尔顿"]第一次接触威亚......正好。
[name="道尔顿"]新人就应该有新人的姿态，就算到时候在天上吊上几个小时，也得撑住，对吧？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_warehouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_1848_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="劳拉"]谢莉，谢莉！我又新加了一场戏，需要用一下威亚，你可以帮我准备一下吗？
[charslot(slot="m",name="avg_npc_1836_1#1$1")]
[name="谢莉"]......不可能。
[name="谢莉"]我知道你很爱演戏，我也知道你很有热情，但你这是第几次新加戏了？你这是第几次扰乱我为整个剧组定下的拍摄进度了？
[name="谢莉"]大小姐，你有一点点责任心吗？我不会为了你这样轻飘飘的一句话改动整个排期，这个剧组不是围着你一个人转的。
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[name="劳拉"]抱歉谢莉，我不是故意要增加你的工作难度，但是道尔顿先生说他已经征得了导演的同意，这个应该是已经定下了的......
[charslot(slot="m",name="avg_npc_1836_1#6$1")]
[name="谢莉"]道尔顿？
[name="谢莉"]......
[charslot(slot="m",name="avg_npc_1836_1#1$1")]
[name="谢莉"]我知道了。
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[name="劳拉"]谢谢你，谢莉！
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2.5)]
[charslot(duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1836_1#1$1")]
[name="谢莉"]（道尔顿昨天才和我骂过你一点新人的规矩都没有，怎么可能今天就好心给你加戏。）
[name="谢莉"]（威亚，是吧......）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="62_g12_dressingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_1838_1#1$1",duration=1)]
[Delay(time=2)]
[name="迈克尔"]哇，小劳拉，今天看上去真是光彩照人啊！下一场空中特技镜头又累又苦，没有一个演员会像你这么高兴......
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[name="劳拉"]可现在是我最兴奋最幸福的时候了。下一场戏是这部电影里唯一一场完完整整属于我的戏份，我一定要把它拍好。
[charslot(slot="m",name="avg_npc_1838_1#1$1")]
[name="迈克尔"]哦，你真是太可爱了。
[name="迈克尔"]千万别伤到自己，你要是实在累得不行了就来找我，今天晚上我会一直在自己的房间里......
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[name="劳拉"]啊！玛丽昂小姐，你是来帮迈克尔先生补妆的吗？
[charslot(slot="m",name="avg_npc_1839_1#1$1")]
[name="玛丽昂"]......
[charslot(slot="m",name="avg_npc_1848_1#1$1")]
[name="劳拉"]那我先去做准备了，晚点再见！
[Dialog]
[charslot(duration=1.5)]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=2.5)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_npc_1838_1#1$1",duration=0.5)]
[charslot(slot="r",name="avg_npc_1839_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1838_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="r")]
[name="玛丽昂"]见什么见！
[charslot(slot="l",name="avg_npc_1838_1#3$1",focus="l")]
[name="迈克尔"]不、不见......不见......你别生气啊小玛丽。
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]一不在我眼皮子底下就开始拈花惹草？我们才在一起多久你就厌倦了？
[name="玛丽昂"]演戏的时候就在眉来眼去......喜欢年轻的就去找她啊，吊着我干嘛？之后的妆造你也让劳拉帮你做吧！
[Dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "100,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1838_1#1$1",focus="l")]
[name="迈克尔"]别说气话，亲爱的。我对你是真心实意的。
[name="迈克尔"]要是你真的不喜欢，我以后再也不主动接触她了，我发誓！
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]......真的？
[charslot(slot="l",name="avg_npc_1838_1#1$1",focus="l")]
[name="迈克尔"]真的！
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]......
[name="玛丽昂"]我知道你的那点小毛病，但现在正是你事业的上升期，不要做那些蠢事，也不要辜负我对你的心意。
[name="玛丽昂"]那个叫劳拉的年轻女孩既聒噪又招摇，她一定没安好心，不值得你花心思。
[name="玛丽昂"]从现在开始，别主动接近她。
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="r")]
[name="玛丽昂"]你不能跟她说话，也不能有肢体接触，哪怕她快死了都跟你没有关系......听明白了吗？
[charslot(slot="l",name="avg_npc_1838_1#1$1",focus="l")]
[name="迈克尔"]亲爱的？
[charslot(slot = "m", focus = "n")]
玛丽昂的眼神告诉他，她没开玩笑。
[charslot(slot="l",name="avg_npc_1838_1#4$1",focus="l")]
[name="迈克尔"]我明白了，我答应你，全按你说的办。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="62_g2_setting_rooftop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1838_1#2$1",duration=0.5)]
[Delay(time=1)]
[name="迈克尔"]怎么还没到我的戏份啊，发生什么了？
[charslot(slot="m",name="avg_npc_1845_1#1$1")]
[name="工作人员"]道尔顿先生那儿有些事要处理，片场的人都调过去了，没有人给我下达指示......你看，还有个新人被晾在这儿呢。
[charslot(slot="m",name="avg_npc_1838_1#4$1")]
[name="迈克尔"]唉，真可怜......
[charslot(slot="m",name="avg_npc_1845_1#1$1")]
[name="工作人员"]你可不是同情心这么丰富的人，说吧，是不是想勾搭人家？
[charslot(slot="m",name="avg_npc_1838_1#1$1")]
[name="迈克尔"]还是你了解我。
[name="迈克尔"]让我去看看那个可怜的小美人......
[stopmusic(fadetime=2)]
[Dialog]
[playsound(key="$d_gen_walk_n")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="m",name="avg_npc_1838_1#1$1",duration=0.5)]
[Delay(time=1)]
[name="迈克尔"]小玛丽早上刚生过气，我答应过她不再主动接近小劳拉......不过......
[name="迈克尔"]让她主动接近我不就好了吗？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, bloc

... (全文16501字符)
```

### level_act43side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g6_proproom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1831_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",focus="l")]
[name="蒂比"]莫丽，昨天晚上不是迈克尔第一次找你吧？
[name="蒂比"]你刚来蓝卡坞没多久，以你的性格，如果不是对方死缠烂打，你一定不会去碰远超自己职责范围的事。
[charslot(slot = "right", name = "avg_npc_1831_1#1$1",focus="r")]
[name="莫伊拉"]......
[name="莫伊拉"]从道尔顿出了意外，组长被制片人辞退，我突然被要求接手道具组的第二天......迈克尔先生就找我了。
[name="莫伊拉"]他想要在不走正常程序、不惊动任何人的前提下离开这里。
[charslot(slot = "left", name = "avg_4191_tippi_1#4$1",focus="l")]
[name="蒂比"]他的意思是不告知格蕾塔女士，也不走解约和地块离境手续？
[charslot(slot = "left", name = "avg_4191_tippi_1#10$1",focus="l")]
[name="蒂比"]可他是男主演，总会有人发现他离开的，到时候还是需要支付违约金啊？
[charslot(slot = "right", name = "avg_npc_1831_1#1$1",focus="r")]
[name="莫伊拉"]除非......他正在面临某种更大的威胁，即使事后缴纳罚金也要立刻离开这里。
[name="莫伊拉"]他说道具组能接触到所有工具，对整个地块的构造也很熟悉，如果是我......
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",focus="l")]
[name="蒂比"]你应该能想到办法。
[charslot(slot = "right", name = "avg_npc_1831_1#1$1",focus="r")]
[name="莫伊拉"]嗯。
[charslot(slot = "left", name = "avg_4191_tippi_1#4$1",focus="l")]
[name="蒂比"]以你的能力，或许确实能想到办法，但迈克尔的拍摄还没有结束，如果他真逃了，你被发现了......格蕾塔女士不会放过你。
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]莫丽，你有没有想过，以后你就没法在蓝卡坞混下去了！
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]你有没有想过，你的姐姐该有多伤心啊！
[charslot(slot = "right", name = "avg_npc_1831_1#5$1",focus="r")]
[name="莫伊拉"]姐姐......
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]你不是说，你的家人都反对你来蓝卡坞打拼，只有你的姐姐一直在鼓励你？
[name="蒂比"]所以，你一定要做出成绩来，不为向家人证明什么......
[charslot(slot = "right", name = "avg_npc_1831_1#5$1",focus="r")]
[name="莫伊拉"]我只是希望不要让姐姐失望，希望她能一直一直为我高兴。
[charslot(slot = "right", name = "avg_npc_1831_1#4$1",focus="r")]
[name="莫伊拉"]蒂比，你......你不要生气好不好？
[name="莫伊拉"]求你！
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]我只是气你有事瞒着我。
[charslot(slot = "left", name = "avg_4191_tippi_1#9$1",focus="l")]
[name="蒂比"]我知道你不会答应迈克尔，你只是不知道该怎么拒绝他......我可以帮你的。
[charslot(slot = "right", name = "avg_npc_1831_1#5$1",focus="r")]
[name="莫伊拉"]我知道了，蒂比。我从来没见你这么生气过......
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]......
[charslot(slot = "right", name = "avg_npc_1831_1#9$1",focus="r")]
[name="莫伊拉"]看、看电影吗？
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",focus="l")]
[name="蒂比"]唉......
[charslot(slot = "left", name = "avg_4191_tippi_1#1$1",focus="l")]
[name="蒂比"]看！
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1838_1#1$1")]
[charslot(slot="r",name="avg_npc_1839_1#1$1")]
[Background(image="62_g12_dressingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$nervous_intro",key="$nervous_loop", volume=0.6)]
[charslot(slot="r",name="avg_npc_1839_1#3$1",focus="r")]
[name="玛丽昂"]......你说，你想偷偷带我走？
[charslot(slot="l",name="avg_npc_1838_1#1$1",focus="l")]
[name="迈克尔"]是的，亲爱的。让我们温存一会儿，就赶紧回房间拿行李，好吗？
[charslot(slot="r",name="avg_npc_1839_1#6$1",focus="r")]
[name="玛丽昂"]哪怕那个小道具师真的找到了法子，能让你避开地块离境程序......但你能避开合同的违约条款吗？
[name="玛丽昂"]拍摄还没有结束，你知道格蕾塔那个女人的手段，她会让你赔偿天价的违约金！
[charslot(slot="l",name="avg_npc_1838_1#5$1",focus="l")]
[name="迈克尔"]都什么时候了！还避开什么合同，能避开那个杀人狂魔就行！
[name="迈克尔"]道尔顿死了，谢莉死了......你猜还有多久会轮到你和我？
[charslot(slot="l",name="avg_npc_1838_1#4$1",focus="l")]
[name="迈克尔"]毕竟，五年前那起意外发生的时候，你和我都曾对劳拉见死不救......
[name="迈克尔"]那个杀人狂魔可能是劳拉的情人，可能是劳拉的老爸，或者某个自诩正义使者的怪侠......总之，他在找当时相关的人索命！
[name="迈克尔"]他想让我们忏悔，想让我们赎罪！
[charslot(slot="l",name="avg_npc_1838_1#5$1",focus="l")]
[name="迈克尔"]亲爱的，我要带你离开这是非之地，我们还要过漫长的余生......
[charslot(slot="r",name="avg_npc_1839_1#2$1",focus="r")]
[name="玛丽昂"]呀，真动听。
[name="玛丽昂"]亲爱的，你什么时候变得这么深情了？
[charslot(slot="l",name="avg_npc_1838_1#3$1",focus="l")]
[name="迈克尔"]啊？
[charslot(slot="r",name="avg_npc_1839_1#2$1",focus="r")]
[name="玛丽昂"]在你对着米兰妮抛媚眼，和置景组的安娜、后勤组的米拉调情的时候......
[name="玛丽昂"]天哪，你脑子里面想的竟然是和我度过漫长的余生？
[charslot(slot="l",name="avg_npc_1838_1#6$1",focus="l")]
[name="迈克尔"]这、这是重点吗？
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]重点是——我不会走的，迈克尔。
[name="玛丽昂"]而且，你也不许走。
[charslot(slot="l",name="avg_npc_1838_1#6$1",focus="l")]
[name="迈克尔"]......
[charslot(slot="r",name="avg_npc_1839_1#5$1",focus="r")]
[name="玛丽昂"]我好不容易才为你争取来了在格蕾塔的剧组里担当主演的机会，一人分饰三角，多么难得！
[name="玛丽昂"]把握住它，你将在蓝卡坞一炮而红！
[charslot(slot="l",name="avg_npc_1838_1#6$1",focus="l")]
[name="迈克尔"]我们总会有别的机会......
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]看着我，迈克尔。
[name="玛丽昂"]你在《杜邦夫人之死》里的戏服甚至要比米兰妮——绝对女主演的戏服的做工更加精致更加抢镜......
[name="玛丽昂"]你喷的香水、出席时装周的单品花的都是我的积蓄，甚至，这让你充作沃尔珀的假耳朵假尾巴也出自我的手......
[charslot(slot="r",name="avg_npc_1839_1#4$1",focus="r")]
[name="玛丽昂"]没有我，观众们会发现你这原本在镜头前光鲜亮丽的商品一下子就......没了卖相。
[name="玛丽昂"]我们在一起五年了，我为你付出了一切。如今，我的积蓄不多了，年纪也不小了......我等不起了。
[name="玛丽昂"]我爱你，迈克尔，别辜负我的爱。
[Dialog]
[charslot(slot="l",name="avg_npc_1838_1#5$1",focus="l")]
[Delay(time=1.5)]
[name="迈克尔"]你这是——爱我？
[name="迈克尔"]道尔顿死的那天，你应该很感谢米兰妮当众点破了我们俩的关系吧？
[name="迈克尔"]在所有人眼里，我是个惹是生非的花花公子，而你付出了所有，却连个名分都得不到，还要被别人揶揄......
[name="迈克尔"]多可怜，多悲情！
[charslot(slot="r",name="avg_npc_1839_1#4$1",focus="r")]
[name="玛丽昂"]难道不是吗？
[charslot(slot="l",name="avg_npc_1838_1#5$1",focus="l")]
[name="迈克尔"]你也说了，你不过是在投资一件商品......投资，自然要舍得付出。
[name="迈克尔"]如果道尔顿没有变成一个烂酒鬼，你当初想办法投资的应该就是他了吧？
[name="迈克尔"]你不过是一条想要寄生却找不到宿主的虫豸罢了，玛丽昂。
[name="迈克尔"]你让我觉得可笑......当然，我自己也可笑透了。
[charslot(slot="r",name="avg_npc_1839_1#1$1",focus="r")]
[name="玛丽昂"]......
[charslot(slot="l",name="avg_npc_1838_1#2$1",focus="l")]
[name="迈克尔"]话都说到了这个份上，我一个人走，你就留在这里吧。
[name="迈克尔"]给你个建议，你可以考虑下投资那个叫卢西恩的小白脸

... (全文13509字符)
```

### level_act43side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g6_proproom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1831_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",focus="l")]
[name="蒂比"]老道尔顿的死和谢莉小姐走入冷库都不是意外......
[charslot(slot = "left", name = "avg_4191_tippi_1#9$1",focus="l")]
[name="蒂比"]现在，迈克尔先生和玛丽昂小姐也死了，还是死于那样的场景和手段......
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]幕后的凶手到底是谁？为什么要犯下这么多桩命案？为什么......如此残忍？
[charslot(slot = "right", name = "avg_npc_1831_1#4$1",focus="r")]
[name="莫伊拉"]迈克尔先生似乎早有预感。
[name="莫伊拉"]遇害的前一天晚上他来找我的时候，神情比之前几次见面还要严肃。
[name="莫伊拉"]他一定是确定了道尔顿的意外背后真正的原因，才心惊胆战想逃离这里，但......
[charslot(slot = "left", name = "avg_4191_tippi_1#9$1",focus="l")]
[name="蒂比"]无论他是不是心里有鬼，我们都没法知道了......
[name="蒂比"]可能最近发生的所有事都与他们口中说的那起五年前的意外有关，但我更担心的是......
[name="蒂比"]凶手不再将谋杀掩盖为意外，而是将自己的存在公之于众，他难道是想告诉我们——
[charslot(slot = "left", name = "avg_4191_tippi_1#5$1",focus="l")]
[name="蒂比"]在真相彻底被揭发之前，任何人都不安全。
[charslot(slot = "right", name = "avg_npc_1831_1#3$1",focus="r")]
[name="莫伊拉"]......
[charslot(slot = "left", name = "avg_4191_tippi_1#8$1",focus="l")]
[name="蒂比"]啊对不起，莫丽，我的话是不是吓到你了？
[charslot(slot = "left", name = "avg_4191_tippi_1#2$1",focus="l")]
[name="蒂比"]别担心，无论地块上是不是游荡着穷凶极恶的杀手，无论对方有多少人，我都会保护你的。
[charslot(slot = "right", name = "avg_npc_1831_1#9$1",focus="r")]
[name="莫伊拉"]不，蒂比大侦探，我只是在想......我也可以做些什么。
[charslot(slot = "left", name = "avg_4191_tippi_1#10$1",focus="l")]
[name="蒂比"]嗯？
[charslot(slot = "right", name = "avg_npc_1831_1#1$1",focus="r")]
[name="莫伊拉"]迈克尔先生已经遇难，但他之前拜托我的事情，不一定要作废。
[name="莫伊拉"]格蕾塔女士提到过的逃生舱或许已经被凶手盯上......
[name="莫伊拉"]如果真能另开辟一条逃生通道，或者造出某种连接地面的装置，或者哪怕只是找到一个可以让我们通过的排风口......
[name="莫伊拉"]说不定我们真能避开那在阴影里盯着我们的凶手，在关键的时候保护自己。
[charslot(slot = "left", name = "avg_4191_tippi_1#9$1",focus="l")]
[name="蒂比"]莫丽......
[charslot(slot = "right", name = "avg_npc_1831_1#9$1",focus="r")]
[name="莫伊拉"]蒂比，我来到这个剧组后，你是第一个跟我说话，跟我交心的人。
[name="莫伊拉"]我搞砸过很多事，也给你添过麻烦，但你凡事都挡在我的前面，哪怕玛丽昂只是一时忘记我的名字，你也会郑重其事地提醒。
[name="莫伊拉"]你一直在关心我、安慰我、保护我......
[name="莫伊拉"]现在，我也想保护你。
[charslot(slot = "left", name = "avg_4191_tippi_1#1$1",focus="l")]
[name="蒂比"]......
[Dialog]
[charslot(slot = "left",posfrom = "0,0", posto = "100,0",duration = 1)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=15, ystrength=6, vibrato=5, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
黎博利女孩轻轻抱住她在剧组里最最要好的朋友。
[charslot(slot = "left", name = "avg_4191_tippi_1#1$1",focus="l")]
[name="蒂比"]等这些事结束了，我们到你家去看电影......二十四小时恐怖片连播，搭配我们最喜欢的饮料和炸鳞块。
[name="蒂比"]我想见见你从小长大的地方，也想看看你温柔的姐姐究竟是什么样子。
[charslot(slot = "right", name = "avg_npc_1831_1#9$1",focus="r")]
[name="莫伊拉"]......好。
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[PlaySound(key="$dooropenquite")]
[charslot(slot = "m", name = "avg_npc_1830_1#1$1",duration=1)]
[delay(time=2)]
[name="米兰妮"]我似乎打扰了你们温情的姐妹谈心。
[charslot(slot = "m", name = "avg_4191_tippi_1#10$1")]
[name="蒂比"]米兰妮女士，您怎么会亲自来道具间？您的助理呢？
[charslot(slot = "m", name = "avg_npc_1830_1#6$1")]
[name="米兰妮"]你们没收到格蕾塔的终端通讯吗？她结算了所有人的酬劳，正式解散了整个剧组。
[name="米兰妮"]畏惧凶手的，忌惮天灾的，坚持拍摄的......都可以任意决定自己的去留，各行其是。
[name="米兰妮"]眨眼的功夫，我手下那个软骨头就不知道跑哪儿躲起来了。
[charslot(slot = "m", name = "avg_npc_1831_1#4$1")]
[name="莫伊拉"]各行其是？
[name="莫伊拉"]有那么多人遇害了......难道格蕾塔女士，不，剧组的其他人都不在意这背后深层的原因是什么吗？
[charslot(slot = "m", name = "avg_npc_1830_1#4$1")]
[name="米兰妮"]深层原因？在这种情况下难道还有人想要追寻真相吗？直接逃离移动地块报警不是更方便吗？
[name="米兰妮"]或者，按照格蕾塔的说法——把真相交给想当侦探的好事者吧。
[charslot(slot = "m", name = "avg_npc_1831_1#4$1")]
[name="莫伊拉"]......
[charslot(slot = "m", name = "avg_4191_tippi_1#4$1")]
[name="蒂比"]那您来找我们又是为了什么？
[charslot(slot = "m", name = "avg_npc_1830_1#1$1")]
[name="米兰妮"]不是你们，是你，场景喷绘师蒂比。
[charslot(slot = "m", name = "avg_4191_tippi_1#8$1")]
[name="蒂比"]我？
[charslot(slot = "m", name = "avg_npc_1830_1#1$1")]
[name="米兰妮"]我欣赏格蕾塔想要拍摄天灾的胆识，她的铤而走险对于我个人来说也是极佳的机遇，但戏不是光靠天然的背景就能撑起来的。
[name="米兰妮"]蒂比，我知道你对电影的热情远超剧组里的大多数成员，你也多少听说过这个项目对我有多么重要......
[charslot(slot = "m", name = "avg_npc_1830_1#2$1")]
[name="米兰妮"]所以，我真诚地请求你发挥在氛围营造和色彩搭配上的天赋，为我的谢幕戏设计最完美的场景。
[charslot(slot = "m", name = "avg_4191_tippi_1#1$1")]
[name="蒂比"]哇......
[charslot(slot = "m", name = "avg_4191_tippi_1#10$1")]
[name="蒂比"]我是很愿意啦，但......
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot = "m", name = "avg_npc_1831_1#9$2",duration=1)]
[delay(time=2)]
[name="莫伊拉"]蒂比，你去帮米兰妮女士的忙吧。
[charslot(slot = "m", name = "avg_4191_tippi_1#10$1")]
[name="蒂比"]欸，莫丽，你穿上雨披是要......你真打算去，“探险”啊？
[charslot(slot = "m", name = "avg_npc_1831_1#9$2")]
[name="莫伊拉"]嗯。
[name="莫伊拉"]放心，我在道具组也待了这么久，对地块也算熟悉，不会出什么事的。
[name="莫伊拉"]还记得我们刚刚说过的话吗？这是我必须要去做的事情。
[charslot(slot = "m", name = "avg_4191_tippi_1#1$1")]
[name="蒂比"]那好吧。
[name="蒂比"]等我帮完米兰妮女士，就去找你！
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[Background(image="62_g10_dormitory",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$doorknockquite")]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1828_1#2$1")]
[name="卢西恩"]请进，格蕾塔女士。
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite")]
[charslot(slot = "m", name = "avg_npc_1834_1#1$1",duration=1)]
[delay(time=1.5)]
[name="格蕾塔"]还没开门就知道是我了？
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]嗯，我在等你。
[charslot(slot = "m", name = "avg_npc_1834_1#6$1")]
[name="格蕾塔"]......
[name="格蕾塔"]那天你暗地里调查出的小线索，让我不得不提前向所有成员解释拍摄实景天灾的规划。
[name="格蕾塔"]那不是个好时机。阿布纳，还有剧组的其他人本就对我不满，我只能临时做了一些不可谓不大的

... (全文9952字符)
```

### level_act43side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g12_dressingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_1830_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_4191_tippi_1#2$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1830_1#1$1",focus="l")]
[name="米兰妮"]蒂比，我对“杜邦夫人”谢幕的场景构建有几个初步的构想。
[name="米兰妮"]你干过的工种多，又是专业的场景喷绘师，我需要你帮我一起做出最佳的场景设计。
[name="米兰妮"]这是我随手整理的一些资料，可以先看看......
[Dialog]
[charslot(slot = "right", name = "avg_4191_tippi_1#2$1",focus="r")]
[PlaySound(key="$d_avg_paper1",volume=1)]
[Delay(time=1)]
[charslot(slot = "right", name = "avg_4191_tippi_1#1$1",focus="r")]
[name="蒂比"]哇......这么多美术元素和影片参考？
[name="蒂比"]色调、氛围、设计理念......包括建筑的细节和不同构件之间的光感差异都有标注！
[charslot(slot = "right", name = "avg_4191_tippi_1#8$1",focus="r")]
[name="蒂比"]米兰妮女士，您到底从多久前就开始研究这场戏了？
[charslot(slot = "left", name = "avg_npc_1830_1#1$1",focus="l")]
[name="米兰妮"]近几年，我最不缺的就是时间。想拍出优秀的作品，只是把戏照本宣科地演完是远远不够的。
[charslot(slot = "right", name = "avg_4191_tippi_1#10$1",focus="r")]
[name="蒂比"]明明斯蒂芬导演都还没修改出满意的剧本，您就为“杜邦夫人”的结局做了那么多的想象？
[charslot(slot = "left", name = "avg_npc_1830_1#4$1",focus="l")]
[name="米兰妮"]到现在那个小伙子都没交出结局的台本。我想，作为《杜邦夫人之死》的主演兼投资人，我有义务对作品负责。
[charslot(slot = "left", name = "avg_npc_1830_1#2$1",focus="l")]
[name="米兰妮"]而且我说过，杜邦夫人怎么在戏里好看地死，决定了我怎么在蓝卡坞漂亮地重生。
[charslot(slot = "right", name = "avg_4191_tippi_1#1$1",focus="r")]
[name="蒂比"]《鲁珀坎假日》《艾琳·达斯的画像》《断桥遗梦》......这些背景氛围的参考影片不都是玛丽安娜女士的作品吗？
[charslot(slot = "left", name = "avg_npc_1830_1#3$1",focus="l")]
[name="米兰妮"]你......喜欢玛丽安娜·布莱克？
[name="米兰妮"]她可在你出生之前就告别银幕了。
[charslot(slot = "right", name = "avg_4191_tippi_1#8$1",focus="r")]
[name="蒂比"]呃......我、我老爹很喜欢她的作品！再说了，经典永不过时。
[charslot(slot = "left", name = "avg_npc_1830_1#1$1",focus="l")]
[name="米兰妮"]她的演技和挑选剧本的品味无可挑剔。
[charslot(slot = "right", name = "avg_4191_tippi_1#2$1",focus="r")]
[name="蒂比"]真意外......我本来以为您会很不喜欢玛丽安娜女士，毕竟你们被放在一起比较了那么多年。
[charslot(slot = "left", name = "avg_npc_1830_1#4$1",focus="l")]
[name="米兰妮"]是啊，那么多年......
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1, block=true)]
[Background(image="29_g7_mainstreet_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.4, channel="bgs",fadetime=2)]
[playMusic(key="$victorianormal_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=true)]
[charslot(slot="m",name="avg_npc_1840_1#1$1",duration=1)]
[delay(time=2.5)]
[PlaySound(key="$skill_flash", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Delay(time=1)]
[charslot(slot = "m", focus = "n")]
[name="记者"]玛丽安娜女士，恭喜您斩获演艺生涯的第八个最佳女主角奖！
[name="记者"]自入行以来，您几乎每一年都有作品提名或获奖，业内都认为您将是新人演员无法逾越的高山。
[name="记者"]在您看来，现在的影坛是否有值得期待的后辈呢？
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="玛丽安娜"]感谢您的赞扬，记者先生，不过“无法逾越的高山”言过其实，我也仍在攀登的路上。
[name="玛丽安娜"]蓝卡坞无时无刻不在涌入极富潜力的新人，我很难说出某个具体的名字——
[charslot]
[name="？？？"]米兰妮·卢瑟福德。
[Dialog]
[playsound(key="$d_avg_highheelfts")]
[delay(time=2)]
[name="米兰妮"]玛丽安娜女士，请接受我的鞠躬致意。
[name="米兰妮"]我今天拿到了最佳女配角，相比您获得这个奖项所花费的时间，慢了整整两年。
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="玛丽安娜"]......
[charslot(slot = "m", focus = "n")]
[name="米兰妮"]我看过您的所有作品，如刚刚那位记者朋友所说，您确实是天生的演员，是蓝卡坞目前难以逾越的高山......但也只是目前。
[name="米兰妮"]请再给我一段时间，我一定会超越您。
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="玛丽安娜"]我很期待。
[stopmusic(fadetime=2)]
[StopSound(channel="bgs", fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="62_g2_setting_rooftop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[name="新人助理"]哇......米兰妮跟玛丽安娜在同场飙戏欸，好酷。
[name="新人助理"]她俩不对付很久了吧？最近一段时间两人拿奖的速度像在比赛似的......怎么会答应出演同一部戏？
[charslot]
[name="米兰妮"]......
[charslot]
[name="资深统筹"]嘘！没礼貌的小子，你进组的时候没经过培训吗！快跟米兰妮女士鞠躬道歉！
[name="新人助理"]对、对不起！
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="玛丽安娜"]何苦对新来的孩子那么严苛呢，米兰妮？
[charslot(slot = "m", focus = "n")]
[name="米兰妮"]“我们的电影建立在一套又一套规则之上”，玛丽安娜女士，您入行比我久，应该对这句话体会更深。
[name="米兰妮"]所谓女明星的礼遇，都是我们靠一个个角色、一部部电影挣来的，它让我这样一个小城市来的小女孩，如今能站在您的对面。
[name="米兰妮"]如果没有规则，电影将没有标准，那我们之间的输赢要怎么衡量呢？
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="玛丽安娜"]你提醒我了，我还没祝贺你前几天凭新作获得了莱塔尼亚“高塔电影展”最佳女主演。
[charslot(slot = "m", focus = "n")]
[name="米兰妮"]那只是一个很小的评选，而您的新片再一次包揽了蓝卡坞的各大奖项。
[name="米兰妮"]我还没真正超越您，玛丽安娜女士。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="62_g1_setting_lobby",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playMusic(intro="$Tremont_intro",key="$Tremont_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1840_1#1$1",duration=1)]
[delay(time=2)]
[name="玛丽安娜"]很感谢各位前来参加《在永夜里燃烧的晨星》的发布会......
[name="玛丽安娜"]这段时间感谢各位的关心。剧组确实在拍摄过程中遭遇了天灾，我受了伤，现在仍在恢复当中。
[name="玛丽安娜"]所幸，那次拍摄不是无功而返，在众人的帮助下我们依旧留下了一些珍贵的画面......
[charslot(slot="m",name="avg_npc_1840_1#3$1")]
[name="玛丽安娜"]但我想，或许这是上天冥冥之中给我的启示——是的，玛丽安娜即将告别银幕。
[name="玛丽安娜"]作为《在永夜里燃烧的晨星》的主演兼投资人，我宣布，这部电影及我本人，不会参与任何奖项的评选。
[charslot(slot="m",name="avg_npc_1840_1#1$1")]
[name="玛丽安娜"]它仅仅是“玛丽安娜”，留给影迷朋友的最后的礼物。
[name="玛丽安娜"]当然，我不会马上离开蓝卡坞，我会暂时转入幕后......
[name="玛丽安娜"]但或许不久后，我就会尝试接触其他机会......作为“雅拉·布克·威尔森”，开启新的人生。
[Dialog]
[charslot]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true

... (全文17157字符)
```

### level_act43side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_lungmencommand",screenadapt="coverall")]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="en")]
[SoundVolume(volume=0.8, channel="en",fadetime=2)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
漆黑一片的楼层里，身形娇小的札拉克女孩独自摸索着。
[dialog]
[charslot(slot = "m", name = "avg_npc_1831_1#1$2", duration=1.5, isblock=true)]
[name="莫伊拉"]嗯......原来如此。
[name="莫伊拉"]虽然构造和系统看上去很复杂，但只要搞清楚原理......
[charslot(slot = "m", name = "avg_npc_1831_1#9$2")]
[name="莫伊拉"]就算是小小的道具师也能操作。
[name="莫伊拉"]比如这里，先调整一下方向......
[dialog]
[PlaySound(key="$d_avg_keyboard_console", volume=1, loop=true, channel="key")]
[Delay(time=1)]
[StopSound(channel="key", fadetime=1)]
[charslot(slot = "m", name = "avg_npc_1831_1#9$2")]
[name="莫伊拉"]设置好时间，再扳下拉杆，打开闸口，然后......
[name="莫伊拉"]成了。
[charslot(slot = "m", name = "avg_npc_1831_1#10$2")]
[name="莫伊拉"]嗯，跟我想的完全一致。
[name="莫伊拉"]这样一来就算发生意料之外的事情......也不用担心了。
[dialog]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1831_1#1$2")]
[name="莫伊拉"]现在，只剩下最后一件事......
[name="莫伊拉"]我要去找她。
[dialog]
[StopSound(channel="en", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="62_g10_dormitory",screenadapt="coverall")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1834_1#6$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="n")]
[name="格蕾塔"]我知道你有顾虑，卢西恩。
[name="格蕾塔"]现在地块上危机重重，人人自危，一个不管不顾撂下狠话要将拍摄进行下去的制片人，怎么看都不是值得信任的对象。
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="l")]
[name="卢西恩"]我们之间无需信任。
[charslot(slot = "r", name = "avg_npc_1834_1#7$1", focus="r")]
[name="格蕾塔"]呵......没错。
[charslot(slot = "r", name = "avg_npc_1834_1#6$1", focus="r")]
[name="格蕾塔"]在蓝卡坞从业二十年，我从来没有信任过任何合作伙伴，我相信的只有自己的眼光。
[name="格蕾塔"]我在米兰妮最需要机会的时候发出邀约，我在拍卖会上一眼看出你是演戏奇才，我吃准阿布纳恨我但还是会加入剧组。
[name="格蕾塔"]......我还确信五年前劳拉之死是挽救电影的唯一解。
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="l")]
[name="卢西恩"]你与那起意外并无关联，但你利用了她的死。
[charslot(slot = "r", name = "avg_npc_1834_1#6$1", focus="r")]
[name="格蕾塔"]劳拉是个有天分的新人。她好学、勤奋、对电影充满热情，只是有时候积极得过了头，破坏了一些规矩。
[name="格蕾塔"]当时斯蒂芬经验浅薄，拍摄并没有达到预期的效果。项目进行到中途，我就意识到这部电影一定会掏空我的资产，甚至葬送我的声誉。
[charslot(slot = "r", name = "avg_npc_1834_1#5$1", focus="r")]
[name="格蕾塔"]我需要“场外因素”帮我渡过这次危机......
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="l")]
[name="卢西恩"]劳拉的坠亡。
[charslot(slot = "r", name = "avg_npc_1834_1#5$1", focus="r")]
[name="格蕾塔"]用媒体炒作片场故事缺乏意义，好事者只会唏嘘几句，转头就会遗忘。
[name="格蕾塔"]所以我花重金压下了警方的调查和电视台对此的关注，给劳拉的家人一笔可观的抚恤金......
[name="格蕾塔"]让剪辑师完整保留了阿布纳拍摄的坠亡片段，故意做成剧中的一幕高潮......
[name="格蕾塔"]到现在还有人认为她是早早息影的天才演员......
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="l")]
[name="卢西恩"]你隐瞒了她的死。
[charslot(slot = "r", name = "avg_npc_1834_1#5$1", focus="r")]
[name="格蕾塔"]我让她在电影中永生。
[charslot(slot = "l", name = "avg_npc_1828_1#2$1", focus="l")]
[name="卢西恩"]总有人会注意到你的手段。
[charslot(slot = "r", name = "avg_npc_1834_1#7$1", focus="r")]
[name="格蕾塔"]每年劳拉的祭日，我都会去看望她。五年过去，她的墓前只有我带去的花。
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="l")]
[name="卢西恩"]你毫不愧疚？
[charslot(slot = "r", name = "avg_npc_1834_1#6$1", focus="r")]
[name="格蕾塔"]我难辞其咎。但忏悔，不是现在。
[charslot(slot = "r", name = "avg_npc_1834_1#5$1", focus="r")]
[name="格蕾塔"]此时此刻我最想做的只有一件事——把电影拍完。
[name="格蕾塔"]等《杜邦夫人之死》上映后，拍摄中发生的几起命案势必会引来媒体的关注，我也会借此正式公开劳拉死亡的真相。
[name="格蕾塔"]到时候会有更多人为她悼念，而我将承担我应承担的罪责。
[charslot(slot = "l", name = "avg_npc_1828_1#3$1", focus="l")]
[name="卢西恩"]......
[charslot(slot = "r", name = "avg_npc_1834_1#8$1", focus="r")]
[name="格蕾塔"]你应该明白，刚刚的自我坦陈并非有感而发。
[charslot(slot = "l", name = "avg_npc_1828_1#1$1", focus="l")]
[name="卢西恩"]你想用自己的真相跟我交易。
[charslot(slot = "r", name = "avg_npc_1834_1#6$1", focus="r")]
[name="格蕾塔"]遇见你之初我还以为是命运的垂青，为我即将开拍的电影送来一份大礼。
[name="格蕾塔"]然而你进组后的种种表现，让我确认你的身份异于常人。
[name="格蕾塔"]老道尔顿死在你的面前，你神情镇定，甚至还期待之后的拍摄。
[name="格蕾塔"]找到我打算拍摄天灾的线索之后，你将它在绝妙的时机分享给最会传播消息的摄影助理。
[name="格蕾塔"]现在，剧组正式解散，几乎所有人都陷入绝境，而你却在房间内等待我的拜访，仿佛早已习惯突如其来的悲剧和死亡。
[charslot(slot = "r", name = "avg_npc_1834_1#5$1", focus="r")]
[name="格蕾塔"]你到底是谁，你到底为什么答应加入剧组？
[charslot(slot = "l", name = "avg_npc_1828_1#5$1", focus="l")]
[name="卢西恩"]我只是被你拍下的剧本吸引，别无二因。
[charslot(slot = "r", name = "avg_npc_1834_1#7$1", focus="r")]
[name="格蕾塔"]或许吧。
[charslot(slot = "r", name = "avg_npc_1834_1#6$1", focus="r")]
[name="格蕾塔"]事到如今盘问你的来历也无助于我的拍摄，但我希望我的坦诚也能换来你的坦诚。
[name="格蕾塔"]卢西恩先生，我相信自己的眼光，就算我在你身上发现了无数可疑之处，我依然不会收回向你发出的主演邀约。
[charslot(slot = "r", name = "avg_npc_1834_1#5$1", focus="r")]
[name="格蕾塔"]但是——
[name="格蕾塔"]如果你真正的目的无法明说，如果你的视角远高于我......
[name="格蕾塔"]如果你认为劳拉之死，以及五年后由此引发的一切，才是这个地块上真正在拍摄的“故事”，而你正是为此而来......
[name="格蕾塔"]格蕾塔·斯通愿意再一次向你发出邀请......
[name="格蕾塔"]去成为接下来的“主演”吧，卢西恩先生。
[dialog]
[charslot(slot = "l", name = "avg_npc_1828_1#5$1", focus="l")]
[Delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1828_1#11$1", focus="l")]
[name="卢西恩"]如你所愿......如我所愿，格蕾塔女士。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.2, grad=true, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.2, grad=true, fadetime=0.1)]
[PlaySound(key="$d_avg_darkforest", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.2, channel="a",fadetime=2)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="“......格蕾塔......结算了所有人的酬劳，正式解散了整个剧组......”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“畏惧凶手的，忌惮天灾的，坚持拍摄的......都可以任意决定自己的去留，各行其是。”", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="坚持拍摄？格蕾塔到现在还想着自己的电影？", x=300, y=350, alignment="center", size=24, delay=0

... (全文13377字符)
```

### level_act43side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$m_sys_rglk1phantomcastle_intro", key="$m_sys_rglk1phantomcastle_loop", volume=0.6)]
[Background(image="62_g10_dormitory",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1831_1#13$2", duration=1.5, isblock=true)]
[name="莫伊拉"]......
[charslot(slot = "m", name = "avg_npc_1831_1#14$2")]
[name="莫伊拉"]看来你在格蕾塔女士解散剧组之后给出的各种选择里，选择了侦探，卢西恩先生。
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]不用虚张声势。我知道，你并不害怕我点破它。
[name="卢西恩"]如果能让更多人知道劳拉坠亡的真相以及剧组成员的所作所为，你甚至会在合适的时机主动暴露自己。
[charslot(slot = "m", name = "avg_npc_1831_1#14$2")]
[name="莫伊拉"]......但不是现在。
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]都结束了，莫伊拉。
[name="卢西恩"]你一直隐藏得很好，单纯的身份和无辜的外表是很理想的掩护。
[name="卢西恩"]几乎每次凶案发生时，你都与蒂比在一起，那位场景喷绘师对你很信任，她为你提供了不在场证明......哪怕你曾中途离开。
[charslot(slot = "m", name = "avg_npc_1828_1#5$1")]
[name="卢西恩"]现在想来，剧组发生的每起“意外”，都或多或少与你有关。
[name="卢西恩"]道尔顿死于被替换的道具刀，原先的道具组长被辞退，你顺理成章接手他的工作，获得了更多作案的机会。
[name="卢西恩"]第二起“意外”......
[charslot(slot = "m", name = "avg_npc_1834_1#6$1")]
[name="格蕾塔"]——谢莉走入冷库。
[charslot(slot = "m", name = "avg_npc_1828_1#5$1")]
[name="卢西恩"]不，在那之前她已起了杀心，只是未能成功。
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]格蕾塔女士，还记得吗？谢莉小姐曾因陷入幻觉耽误了拍摄。
[name="卢西恩"]当她僵在原地无法动弹的时候，沉重的货箱从天而降......
[charslot(slot = "m", name = "avg_npc_1834_1#3$1")]
[name="格蕾塔"]你救下了谢莉，莫伊拉仅凭一人之力拉住了货箱的绳索，避免你们受伤......
[charslot(slot = "m", name = "avg_npc_1828_1#2$1")]
[name="卢西恩"]那可不是好心的顺手之劳。
[name="卢西恩"]当时所有人都被谢莉小姐的行动吸引，极少有人会注意到空中悬吊的货箱......
[name="卢西恩"]更别提第一时间出现在绳索的另一端。
[charslot(slot = "m", name = "avg_npc_1834_1#5$1")]
[name="格蕾塔"]只有在绳索上做手脚的人，才能做出如此迅速的反应......
[charslot(slot = "m", name = "avg_npc_1831_1#10$2")]
[name="莫伊拉"]......
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]也正是这次杀人未遂让“谢莉小姐会被幻觉影响”成为剧组人人皆知的事实，于是你顺水推舟......
[charslot(slot = "m", name = "avg_npc_1831_1#14$2")]
[name="莫伊拉"]我知道她最深的噩梦。
[name="莫伊拉"]她把我误认成劳拉姐姐，对我吐露了罪恶的秘密......
[charslot(slot = "m", name = "avg_npc_1831_1#15$2")]
[name="莫伊拉"]但直到最后，她都没向姐姐忏悔，反倒开始责怪姐姐的逾矩......她该死。
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]至于玛丽昂和迈克尔......
[charslot(slot = "m", name = "avg_npc_1831_1#14$2")]
[name="莫伊拉"]迈克尔只当我是个任人支使的无辜女孩，他猜不到我才是要向他索命的凶手，连偷偷逃离地块这样性命攸关的事也委托我帮忙。
[charslot(slot = "m", name = "avg_npc_1831_1#15$2")]
[name="莫伊拉"]而玛丽昂甚至认为自己丝毫不需要为当年的事情负责，她更该死！
[dialog]
[delay(time=1)]
[name="莫伊拉"]逃？一个都逃不掉！
[name="莫伊拉"]你们知道吗，姐姐承受了那么多痛苦与恶意，可她只字不提，只说自己在剧组里收获了多少经验与快乐......
[name="莫伊拉"]当我忧心自己无法胜任道具师工作时，当我在剧组受到排挤偷偷掉眼泪时......她都会拿自己举例子安慰我，鼓励我......
[charslot(slot = "m", name = "avg_npc_1831_1#16$2")]
[name="莫伊拉"]但直到她过世之后，我才知道，你们提供给她的究竟是哪种待遇！
[charslot(slot = "m", name = "avg_npc_1834_1#6$1")]
[name="格蕾塔"]......
[charslot(slot = "m", name = "avg_npc_1831_1#15$2")]
[name="莫伊拉"]格蕾塔，而你现在看着我的眼神里竟然充满了......疑惑？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1831_1#17$2")]
[name="莫伊拉"]你难道忘了自己是怎样买通警方和媒体，压下姐姐的死，把意外变成电影中亦真亦假的戏，让她死后都不得安宁的吗！
[charslot(slot = "m", name = "avg_npc_1828_1#2$1")]
[name="卢西恩"]不，莫伊拉。
[name="卢西恩"]格蕾塔女士并未遗忘自己的所作所为，她只是在怀疑你的真实身份。
[charslot(slot = "m", name = "avg_npc_1831_1#7$2")]
[name="莫伊拉"]身份？剧组的道具师，不起眼的札拉克，犯下累累罪行的复仇者......
[dialog]
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1828_1#4$1")]
[name="卢西恩"]劳拉，并没有妹妹。
[name="卢西恩"]......她从不存在于你的人生。
[charslot(slot = "m", name = "avg_npc_1831_1#15$2")]
[name="莫伊拉"]你在......说什么？
[name="莫伊拉"]这又是哪种逼问的手段？
[charslot(slot = "m", name = "avg_npc_1834_1#6$1")]
[name="格蕾塔"]五年前的事故之后，我曾给劳拉的家人发放了一笔抚恤金。
[name="格蕾塔"]为了保证劳拉的家庭成员，甚至是远亲都不会向外透露她已死的真相，我雇人仔细调查了她的家庭情况。
[name="格蕾塔"]卢西恩告诉我他推理出的真相后，我一度难以置信，所以再次对照了劳拉的家庭成员名单......
[name="格蕾塔"]很遗憾......里面并没有“莫伊拉”。
[charslot(slot = "m", name = "avg_npc_1831_1#16$2")]
[name="莫伊拉"]......你撒谎！
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]关于你身上发生的一切，我知道该如何解释。但你需要花时间接受它。
[charslot(slot = "m", name = "avg_npc_1828_1#2$1")]
[name="卢西恩"]放下那把匕首，莫伊拉。
[name="卢西恩"]它本不该属于你。
[charslot(slot = "m", name = "avg_npc_1831_1#13$2")]
[name="莫伊拉"]......
[charslot(slot = "m", name = "avg_npc_1831_1#14$2")]
[name="莫伊拉"]放下......？
[name="莫伊拉"]已经来不及了。
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_erthshkng", volume=1, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=6)]
[delay(time=1)]
[PlaySound(key="$d_avg_recorderglitch", volume=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "m", name = "avg_npc_1834_1#3$1")]
[name="格蕾塔"]发生什么了！
[charslot(slot = "m", name = "avg_npc_1828_1#7$1")]
[name="卢西恩"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="62_g11_dormitory_corridor",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_erthshkng", volume=1, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_rockfall", volume=0.3)]
[Effect(name="$e_sandfall_01",layer = 1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_audience_chaos", volume=1)]
[SoundVolume(volume=0.4, channel="e",fadetime=2)]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", bstart=0.9,bend=1, posfrom = "-200,30", posto = "0,30", duration = 0.8)]
[charslot

... (全文15847字符)
```

### level_act43side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect(name="$eb_wind",layer=1)]
[PlaySound(key="$d_avg_wind_howling", volume=0, loop=true, channel="sn")]
[SoundVolume(volume=0.6, channel="sn",fadetime=2)]
[Background(image="62_g8_mobileplotstreet_ruined",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlayMusic(intro="$jealous_intro", key="$jealous_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", duration=1)]
[charslot(slot = "r", name = "avg_npc_1847_1#1$1", duration=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", focus="l")]
[name="愤怒的工作人员"]这就是*蓝卡坞片场术语*格蕾塔的拍摄计划？！
[name="愤怒的工作人员"]都贴在源石风暴脸上了！摆明让我们送死啊！
[charslot(slot = "r", name = "avg_npc_1847_1#1$1", focus="r")]
[name="害怕的工作人员"]不......不......一定是凶手干的！你没听到之前的爆炸声吗？
[name="害怕的工作人员"]地块的驾驶室被人为炸毁了......我们现在根本没办法改变地块的移动速度和航向......
[name="害怕的工作人员"]现在地块接触的还只是天灾的最外围，真等我们撞向它的正中心......
[name="害怕的工作人员"]整个地块估计连一块完整的砖都不会剩下吧......呜呜呜......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", focus="l")]
[name="愤怒的工作人员"]好了别说了！
[name="愤怒的工作人员"]到底是谁？连着死了这么多人，还不够，现在要把所有人的命都搭上？！
[dialog]
[PlaySound(key="$transmission", volume=1)]
[delay(time=1.5)]
[charslot(slot = "l", focus="n")]
[name="无线电中的声音"]凶、凶手是道具组的莫伊拉......
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", focus="l")]
[name="愤怒的工作人员"]什么？谁在说话？
[dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1.5)]
[charslot(slot = "m", name = "avg_npc_1844_1#4$1", duration=1)]
[delay(time=1.5)]
[name="摄影助理"]我说！地块上发生的三起凶案，凶手就是莫伊拉！
[charslot(slot = "m", name = "avg_npc_1847_1#1$1")]
[name="害怕的工作人员"]莫伊拉......天......就是那个不起眼的小札拉克？
[charslot(slot = "m", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]格蕾塔女士亲眼所见！
[name="摄影助理"]要不是有卢西恩先生在，我们的制片人也遇害了！
[charslot(slot = "m", name = "avg_npc_1845_1#1$1")]
[name="愤怒的工作人员"]......那个混蛋在哪里？我要去找她！
[charslot(slot = "m", name = "avg_npc_1844_1#3$1")]
[name="摄影助理"]你自己的命都要保不住了，找一个丧心病狂的杀人犯理论还有什么用！
[charslot(slot = "m", name = "avg_npc_1845_1#1$1")]
[name="愤怒的工作人员"]难道她不用付出一点代价吗？如果有不知情的剧组成员又遇害该怎么办！
[charslot(slot = "m", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]你都能想明白的问题，难道我想不到吗？
[name="摄影助理"]为了保命，我已经把无线电对讲机调成广播模式，真相现在应该已经传到所有人的耳朵里了。
[name="摄影助理"]凶手绝不敢轻举妄动。
[charslot(slot = "m", name = "avg_npc_1844_1#6$1")]
[name="摄影助理"]我得保住自己这条值钱的命......等回到蓝卡坞主城区，我就能用这几天收集到的重磅八卦在汐斯塔买套度假别墅了——
[dialog]
[charslot]
[PlaySound(key="$d_avg_erthshkng", volume=1, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=10, ystrength=10, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=6)]
[PlaySound(key="$d_avg_rockfall", volume=0.3)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_1845_1#1$1")]
[name="愤怒的工作人员"]不好！地块又往源石风暴的方向偏移了！
[charslot(slot = "m", name = "avg_npc_1847_1#1$1")]
[name="害怕的工作人员"]对了，陆行艇！那些陆行艇能救我们！
[charslot(slot = "m", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]......没了。
[charslot(slot = "m", name = "avg_npc_1845_1#1$1")]
[name="愤怒的工作人员"]你说什么？
[charslot(slot = "m", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]我去紧急逃生舱看过了，所有的陆行艇都已经被源石风暴毁坏了......所有的......
[charslot(slot = "m", name = "avg_npc_1847_1#1$1")]
[name="害怕的工作人员"]我们已经无路可逃了......
[name="害怕的工作人员"]......让我死在风暴里还不如从地块上跳下去呢......我......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "m", name = "avg_npc_1844_1#3$1")]
[name="摄影助理"]别说傻话！
[name="摄影助理"]快走，哪里都比拍摄区安全，先到地下动力层躲一躲！
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=2)]
[charslot(duration=1, isblock=true)]
[StopSound(channel="sn", fadetime=2)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect]
[Background(image="62_g12_dressingroom",screenadapt="coverall")]
[Delay(time=1)]
[playsound(key="$d_avg_oldtvelectricity", volume=0, loop=true, channel="fi")]
[StopSound(channel="fi", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[StopSound(channel="fi", fadetime=0.5)]
[PlaySound(key="$d_avg_filmprojection")]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_4191_tippi_1#2$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1830_1#2$1", focus="l")]
[name="米兰妮"]恐怖片的场景设计确实有很多值得参考的地方......谢谢你，蒂比。
[charslot(slot = "r", name = "avg_4191_tippi_1#1$1", focus="r")]
[name="蒂比"]小意思！
[name="蒂比"]大致的呈现效果我需要先回去打个样，等到斯蒂芬导演修改完剧本，我们再慢慢敲定细节。
[charslot(slot = "r", name = "avg_4191_tippi_1#11$1", focus="r")]
[name="蒂比"]我答应过您，一定会设计出让“杜邦夫人”留名影史的落幕场景！
[charslot(slot = "l", name = "avg_npc_1830_1#2$1", focus="l")]
[name="米兰妮"]嗯，合作愉快。
[charslot(slot = "r", name = "avg_4191_tippi_1#4$1", focus="r")]
[name="蒂比"]（唉，怎么都这个点了？不知道莫丽有没有找到离开地块的方法——）
[dialog]
[PlaySound(key="$d_avg_erthshkng", volume=0.4, loop=true, channel="e")]
[CameraShake(duration=4, xstrength=5, ystrength=5, vibrato=90, randomness=90, fadeout=true, block=false)]
[StopSound(channel="e", fadetime=4)]
[delay(time=2)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot = "r", name = "avg_4191_tippi_1#8$1", focus="r")]
[name="蒂比"]啊——！
[name="蒂比"]什、什么情况？
[charslot(slot = "l", name = "avg_npc_1830_1#5$1", focus="l")]
[name="米兰妮"]不太对劲。
[charslot(slot = "r", name = "avg_4191_tippi_1#2$1", focus="r")]
[name="蒂比"]等等，米兰妮女士，无线电有声音......
[dialog]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1)]
[charslot(slot = "r", focus="n")]
[name="无线电中的声音"]......天灾......（杂音）......中控驾驶室......毁......
[charslot(slot = "r", name = "avg_4191_tippi_1#10$1", focus="r")]
[name="蒂比"]信号怎么这么差？这个声音好像是阿布纳的摄影助理？他又在乱传什么八卦——
[charslot(slot = "r", focus="n")]
[name="无线电中的声音"]中控驾驶室......炸毁了......
[name="无线电中的声音"]地块......正冲向天灾......
[name="无线电中的声音"]....

... (全文16903字符)
```

### level_act43side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cherunder_2",screenadapt="coverall")]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="en")]
[SoundVolume(volume=0.8, channel="en",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1.5)]
[charslot(slot = "m", name = "avg_4191_tippi_1#2$1", duration=1.5, isblock=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4191_tippi_1#3$1")]
[name="蒂比"]（用力喘息）
[charslot(slot = "m", name = "avg_4191_tippi_1#4$1")]
[name="蒂比"]蒂比，冷静、冷静......好好想想，在那部电影里，对应的情节是什么样子的——
[name="蒂比"]......女主角让朋友拿上武器，躲进左侧的杂物间，自己跑向另一个方向......
[multiline(name="蒂比")]杂物间......
[charslot(slot = "m", name = "avg_4191_tippi_1#8$1")]
[multiline(name="蒂比",end=true)]没错，路线能对上！
[charslot(slot = "m", name = "avg_4191_tippi_1#2$1")]
[name="蒂比"]再往下、再往下，有点黑......黑是对的，最角落有一道隐藏的闸门......
[name="蒂比"]......再一路向前，走廊的尽头就是备用的机械控制室......
[name="蒂比"]......她知道追杀小队成员的傀儡是朋友的杰作，所有成员都在指责朋友，她也很生气......
[charslot(slot = "m", name = "avg_4191_tippi_1#5$1")]
[name="蒂比"]出发！
[dialog]
[StopSound(channel="en", fadetime=2)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1.5)]
[charslot(duration=1.5, isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
[playMusic(intro="$jealous_intro",key="$jealous_loop", volume=0.6)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="a")]
[StopSound(channel="a", fadetime=1.5)]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", duration=1)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1847_1#1$1", duration=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", focus="l")]
[name="慌乱的工作人员"]蒂比，你在这里做什么？
[charslot]
[charslot(slot = "m", name = "avg_4191_tippi_1#5$1")]
[name="蒂比"]我想到了改变地块航向的方法，可以让人员伤亡降低到最小，请尽快让我过去！
[charslot]
[charslot(slot = "r", name = "avg_npc_1847_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", focus="l")]
[name="慌乱的工作人员"]获救的方法......
[charslot(slot = "r", name = "avg_npc_1847_1#1$1", focus="r")]
[name="怀疑的工作人员"]别听她胡说！罪魁祸首不就是这个黎博利丫头的朋友吗？
[name="怀疑的工作人员"]说不定就是她在隐瞒情报，不然我们怎么死到临头才知道这个连环杀人魔的真面目！
[charslot]
[charslot(slot = "m", name = "avg_4191_tippi_1#3$1")]
[name="蒂比"]不去想朋友对自己的背叛，她还有没说完的话......
[name="蒂比"]不去想周围人的冷嘲热讽，攻击是他们的自我保护......
[charslot]
[charslot(slot = "l", name = "avg_npc_1845_1#1$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1847_1#1$1", focus="n")]
[name="慌乱的工作人员"]原来......原来是你一直躲在背后！不让我们顺利地拍完电影，不让我们回家！
[charslot]
[charslot(slot = "m", name = "avg_4191_tippi_1#5$1")]
[name="蒂比"]她要救下所有人，包括那个背叛了自己的朋友，给自己一个答案......
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1.5)]
[charslot(duration=1.5, isblock=true)]
[delay(time=0.5)]
[name="怀疑的工作人员"]不能让她过去，拦住她！
[dialog]
[PlaySound(key="$d_avg_spryngjy", volume=1)]
[charslot(slot = "m", name = "avg_npc_1845_1#1$1")]
[charslot(slot = "m", action="shake", power=4, times=40, isblock=true, duration=0.5)]
[name="慌乱的工作人员"]啊，我的眼睛——！
[dialog]
[charslot(slot = "m", posfrom="0,0", posto="0,-50", afrom=1, ato=0, duration=0.5)]
[playsound(key="$bodyfalldown2")]
[delay(time=1)]
[charslot]
[charslot(slot = "l", focus="n")]
蒂比拿起别在腰带上的喷绘枪，紧盯着手持武器、面目狰狞的剧组成员们。
[charslot(slot = "m", name = "avg_4191_tippi_1#6$1")]
[name="蒂比"]我真的会对你们不客气......
[charslot(slot = "r", focus="n")]
[name="怀疑的工作人员"]你们还怕一个小姑娘吗？快上！
[dialog]
[charslot]
[PlaySound(key="$d_avg_riot", volume=0, loop=true, channel="r")]
[SoundVolume(volume=1, channel="r",fadetime=2)]
[PlaySound(key="$d_avg_crowdrun", volume=1)]
[CameraShake(duration=4, xstrength=15, ystrength=15, vibrato=90, randomness=90, fadeout=true, block=false)]
[charslot(duration=1.5, isblock=true)]
凶案、天灾......被迫躲进动力层的剧组成员们神经本就紧绷到了极点，喷绘师的行为彻底激怒了他们。
用来防身的武器在壁板上刮出噪音，众人朝蒂比扑过来。
蒂比的手在发抖，她只有一个人，不可能对抗如此多失控的成员，她祈祷着身后的浮空装置能发挥作用......
这是她最后的手段。 
[dialog]
[SoundVolume(volume=0.2, channel="r",fadetime=2)]
[charslot(slot = "m", name = "avg_4198_christ_1#1$1", duration=1.5, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "m", focus="n")]
黑色的生物出现在了走廊的拐角。
[charslot(slot = "m", name = "avg_4198_christ_1#5$1")]
[name="Miss.Christine"]......
[dialog]
[StopSound(channel="r", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[Image(image="62_i06", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
像是被此间的热闹吸引，又仿佛只是偶然经过。
没有一个人注意到她，人群只是被种种极端的情绪牵引着向前，从她的身侧冲过。
Miss.Christine吸了吸鼻子，奔跑的人群在她眼中一点点慢了下来......直至定格。
[name="Miss.Christine"]愤怒，辛辣刺激，但若没有一点嫉妒的酸味作为调剂，还是差点意思......
[name="Miss.Christine"]恐慌，苦涩难咽，不过加点慰藉的甜蜜就会变成不错的甜点......
[name="Miss.Christine"]悲哀，泪水和叹气声中夹杂的咸味，品味过多会引起不必要的麻烦，得注意搭配......
[name="Miss.Christine"]痛苦，最复杂多变的情绪，过去我的心头好......
[name="Miss.Christine"]不过，在遇到卢西恩之后，普通人的痛苦尝起来就变得味同嚼蜡了。
[name="Miss.Christine"]唔，那边还有一个......好像是那个小札拉克的朋友。
[name="Miss.Christine"]原先我只注意到了那个与卢西恩相似的孩子，那个人为自己的新剧目选定的小主演，却没想到你们之间的关系会让你变得如此可口。
Miss.Christine摇晃着尾巴，她的目光在地面的影子间穿梭，最终锁定在了蒂比的影子上......
女士的双尾扭成了一个怪异的形状，像是淑女在用餐前擦拭刀叉。
[dialog]
[delay(time=1.5)]
[name="Miss.Christine"]（晃动尾巴）
[name="Miss.Christine"]（餐后舔爪）
[name="Miss.Christine"]......应该给予你一点小小的报答。
女士看了一眼冲向黎博利的人群。
吃饱后正好需要一点运动以助消化，她想。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="bg_cher

... (全文35995字符)
```

### level_act43side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$m_sys_act43side_loop", volume=0.6)]
[PlaySound(key="$d_avg_drkcludsthdr", volume=1, loop=true, channel="d")]
[Background(image="62_g5_duelscene",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1828_1#1$1", duration=1, isblock=true)]
[name="卢西恩"]破坏了你的演出，我深表遗憾。
[charslot(slot = "m", name = "avg_npc_1829_1#1$1")]
[name="剧团长"]如若你是指自己解决了那个名叫莫伊拉的孩子......那我应当谴责你不合时宜的谦逊，卢西恩。
[name="剧团长"]以你之颖悟，应当猜到了故事原本的结局。
[charslot(slot = "m", name = "avg_npc_1828_1#4$1")]
[name="卢西恩"]一桩五年前的旧案，一场恰是时候的天灾，风暴与迟来的审判同时降临在这个地块......
[name="卢西恩"]而那个原本游离于故事之外的札拉克，慢慢走到了舞台中央，杀死所有背负着罪孽的人。
[multiline(name="卢西恩")]尔后，她将意识到自己的所作所为不过是出于一种虚妄的执念，她将清醒，她将万念俱灰，她将审判最后一人——
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[multiline(name="卢西恩",end=true)]她自己。
[charslot(slot = "m", name = "avg_npc_1829_1#1$1")]
[name="剧团长"]而你呢？
[name="剧团长"]你是剧本中偶然经过的信使，你是剧组里无足轻重的新人，你离核心矛盾如此遥远，却最终成了所有线索的收束。
[charslot(slot = "m", name = "avg_npc_1829_1#3$1")]
[name="剧团长"]“偶然”越出人意料，那无从更改的“必然”上演时，越是震撼人心......这便是戏剧的魅力，你我早已无数次领略。
[name="剧团长"]所以啊，你并未破坏什么，你只是在为演出增色。
[charslot(slot = "m", name = "avg_npc_1829_1#1$1")]
[name="剧团长"]......就像你曾在剧团的所作所为。
[charslot(slot = "m", name = "avg_npc_1828_1#7$1")]
[name="卢西恩"]......
[name="卢西恩"]我途经这种种惨剧，只是为了走向你。
[charslot(slot = "m", name = "avg_npc_1829_1#12$1")]
[name="剧团长"]哈哈，当然。
[name="剧团长"]拍卖会上的一个剧团印记，并不足以让你确认我的存在，对吧？
[charslot(slot = "m", name = "avg_npc_1828_1#1$1")]
[name="卢西恩"]幸好。
[name="卢西恩"]时隔多年，“死亡”，抑或说“毁灭”，依然是你善用的桥段，钟爱的结局。
[charslot(slot = "m", name = "avg_npc_1829_1#11$1")]
[name="剧团长"]孩子啊孩子，我多么希望，你由衷认可它的美。
[charslot(slot = "m", name = "avg_npc_1828_1#5$1")]
[name="卢西恩"]由衷认可吗......
[name="卢西恩"]谈不上，剧团长。我只是比谁都熟悉它。
[charslot(slot = "m", name = "avg_npc_1828_1#2$1")]
[name="卢西恩"]我演过很多戏，我杀过很多人，我的双手满是血腥。
[name="卢西恩"]这是我幼时便接受的教育，这是你灌输给我的人生。
[charslot(slot = "m", name = "avg_npc_1829_1#11$1")]
[name="剧团长"]你是我最好的学生，卢西恩。
[name="剧团长"]在最后的高潮戏到来前，且让我们复盘此前的演出。你我都对这个流程再熟悉不过。
[dialog]
[charslot(duration=1, isblock=true)]
剧团长微笑着向卢西恩优雅鞠躬，他尾巴卷起的权杖遥指向越来越逼近的天灾云，像是一支蘸墨的笔......
熟悉的景象在卢西恩眼前展开。他知道自己无从拒绝，不，他为此而来。
卢西恩轻轻颔首。
[charslot(slot = "m", name = "avg_npc_1829_1#1$1")]
[name="剧团长"]那么，首先是道尔顿。
[dialog]
[SoundVolume(volume=0.2, channel="d",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background]
[Image(image="62_i01_2", screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=1, keep=true)]
[bgeffect(name="$eb_blackmask",layer=1)]
[Delay(time=1)]
[PlaySound(key="$d_avg_filmprojection")]
[playsound(key="$d_avg_filmprojection_loop", loop=true, channel="fi")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[SoundVolume(volume=0.5, channel="fi",fadetime=2)]
[name="剧团长"]对这个行尸走肉般的中年演员而言，这场戏原本无足轻重。
[name="剧团长"]贡献几分难得的清醒，调动仅剩的已成本能的技巧，背诵不多的台词，挨到导演喊停，换取足以支撑下一个长夜的酒资......
[name="剧团长"]他从未哀悼那个因自己而死的女演员，从未缅怀意气风发的曾经，甚至不会因如今的潦倒失意有所羞惭。
[name="卢西恩"]你操纵了他。
[name="剧团长"]诚然，没有我的介入，他不会主动找来那把被调换了的刀，并交到你的手中......
[name="剧团长"]可我并未命令他将胸膛迎向刀锋。
[name="剧团长"]你与他对戏的那一刻，他已然清醒，已然知晓自己身处怎样的危险之中。
[name="卢西恩"]......
[name="剧团长"]卢西恩，戏剧到电影的转换，丝毫没有妨碍你自如地挥洒自己的天赋。
[name="剧团长"]你的表演唤醒了他的记忆，你让他想起了自己曾是一个多么优秀的演员——沉浸其中，赋予虚拟的喜怒哀乐以真实。
[name="剧团长"]那一刻，“信使”入了戏，“杜邦爵士”也彻底被破产的可能性扭曲了内心......
[name="剧团长"]他必须掩盖真相，他必须拼尽全力杀死眼前人，不及思索刀锋反而伤到自己的可能......
[name="剧团长"]你当时就在他的对面，没有人比你更清楚，那一刻，他的愤怒与恐惧多么有感染力。
[name="卢西恩"]作为谢幕演出，近乎完美。
[name="剧团长"]是啊，近在咫尺的死亡，反而激起了他被酒精麻痹许久的胜负欲，他尽情表演，意兴盎然！
[dialog]
[PlaySound(key="$d_avg_filmprojection")]
[cgitem(image="cgitem_62_i03", style="cg", afrom=0, ato=1, duration=0.2, layer = 1)]
[Image(image="62_i03", screenadapt="coverall", fadetime=0.2)]
[name="剧团长"]还有迈克尔与玛丽昂。
[name="剧团长"]拈花惹草的演员与精明的服装师被双双吊在拍摄现场，他们那可笑的私情就这么被晾晒在所有人面前。
[name="剧团长"]他们的结合可耻而滑稽，他们放纵自己的欲望，醉心于钻营，互相鄙夷却又互相利用......
[name="剧团长"]在他们身上从内到外看不见一丝真实，那个迈克尔，甚至连耳朵和尾巴都是伪造的。
[name="剧团长"]他们的死毫无价值，除了为那个摄影助理提供了一则可以兜售的八卦。
[name="剧团长"]可是，卢西恩，你查看过现场，那只猫也舔舐过此地残留的情绪——
[name="剧团长"]你应当清楚，当莫伊拉敲响这扇门，当死亡的脚步声逼近，在那不容思索的片刻间，他们各自做了什么。
[name="卢西恩"]泪痕。
[name="剧团长"]唔，有趣的细节。
[name="卢西恩"]迈克尔的眼角留有泪痕，“洛克菲勒”三兄弟的任意一位都未曾向“杜邦夫人”表露过这般深情......
[name="卢西恩"]......这柄消防斧原本是砍向玛丽昂的。
[name="卢西恩"]迈克尔护住了她，将自身的要害暴露在了利刃之下。
[name="卢西恩"]在生命的最后关头，这对前一刻仍在互相攻讦的男女，下意识的反应是守护彼此。
[dialog]
[StopSound(channel="fi", fadetime=0.5)]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[delay(time=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[hidecgitem(image="cgitem_62_i03")]
[image]
[bgeffect]
[Background(image="62_g5_duelscene",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[charslot(slot = "m", name = "avg_npc_1828_1#5$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="卢西恩"]他们确认了对彼此的，真情。
[charslot(slot = "m", name = "avg_npc_1828_1#3$1")]
[name="卢西恩"]这本身并不值得歌颂。
[charslot(slot = "m", name = "avg_npc_1829_1#12$1")]
[name="剧团长"]你说得没错，我的孩子。
[charslot(slot = "m", name = "avg_npc_1829_1#1$1")]
[name="剧团长"]只是，观众已经落座，他们期待在这灯光与声响围筑成的幻梦中看到什么？
[name="剧团长"]钻营者到头来一无所有，纵欲者终被欲望反噬？当然，这是最顺理成章的编排，用以展示一些无聊的大道理。
[charslot(slot = "m", name = "avg_npc_1829_1#3$1")]
[name="剧团长"]他们何曾想过，并不值得歌颂的真情也足以让人意外。
[name="剧团长"]这两人又何曾想过，他们有那么一刻，会为彼此动容。
[charslot(slot = "m", name = "avg_npc_1828_1#2$1")]
[name="卢西恩"]死亡赋予他们可能？
[charslot(slot = "m", name = "avg_npc_1829_1#1$1")]
[name="剧团长"]死亡赋予他们可能。
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1829_1#11$1")]
[name="剧团长"]当然，还有莫伊拉——在你现身之前，我最看好的孩子。
[dialog]
[PlaySound(key="$d_avg_filmprojection")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background]
[CameraEffect(effect="Grayscale", amount=1, keep=true)]
[Image(image="62_i04_2", screenadapt="coverall")]
[bgeffect(name="$eb_blackmask",layer=1)]
[Delay(time=0.

... (全文14210字符)
```

### level_act43side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_atmosphere_horror", volume=0, loop=true, channel="sn")]
[SoundVolume(volume=1, channel="sn",fadetime=2)]
灯火摇曳的古堡、老师们染血的尸体、黑暗中空洞的风声......遗忘那一切并不难。
直到，已成刺客的卢西恩做了一个梦。
[dialog]
[PlayMusic(key="$m_avg_rglk1secretevent_loop", volume=0.6)]
[Image(image="24_RL03", screenadapt="coverall", xScale=1.05, yScale=1.05, fadetime=0)]
[ImageTween(xScaleFrom=1.05, yScaleFrom=1.05, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[SoundVolume(volume=0.2, channel="sn",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
还是古堡，还是那间空荡的大厅，他独坐在灯光下歌唱，身后是所有过去的剧团成员——
鲜活如昨。
[dialog]
[name="剧团长"]孩子啊，人无法抹掉自己的过去。
[name="剧团长"]它们总有迹可循。
[name="卢西恩"]你以为我恐惧？
[name="卢西恩"]不，我只是确认了，你加之于我人生的飞页并未完全撕去——你仍存在。
[name="卢西恩"]但你说得对，“人无法抹掉自己的过去，它们总有迹可循。”
[name="卢西恩"]所以，为了了结你，在这漫长的时间里，我行你所行之路......
[name="卢西恩"]我走遍整片大地！
[dialog]
[StopSound(channel="sn", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[bgeffect(name="$eb_whitemask",layer=1)]
[PlaySound(key="$d_avg_filmprojection")]
[playsound(key="$d_avg_filmprojection_loop", loop=true, volume=0.4, channel="fi")]
[focusparam(blur=false, effect="Grayscale")]
[focusout(duration=1, type="bg", from=0, to=1)]
[Background(image="21_G8_cammunibase",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", duration=1)]
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="n")]
[name="卢西恩"]加莱，高卢的一座边陲城市。
[name="卢西恩"]同盟邦突然发动叛乱，加莱陷于重围，可是依靠威力强劲的城防炮，以及那位被誉为“帝国旗帜”的将军，加莱固守了数月。
[name="卢西恩"]将军立于城墙之上，不眠不休，不退不移。旗帜仍在，已经疲惫的士兵便不会心生动摇......
[charslot(slot = "r", name = "avg_npc_1828_1#6$1", focus="r")]
[name="卢西恩"]直到一场无人设想的叛乱发生，将军最为信任的副将打开了城门。
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]......
[name="剧团长"]高卢皇室放弃了加莱，它的失陷已是必然。
[name="剧团长"]荣耀让帝国旗帜不愿意倒下，副将觉得自己应该陪着这位将军，一如数十年间他们一起出生入死。
[name="剧团长"]可固守只会加重伤亡，这座城市终会成为死城。
[charslot(slot = "l", name = "avg_npc_1829_1#3$1", focus="l")]
[name="剧团长"]可能那位饱受折磨的军人只是突然想通了......没有两全的选择，但他有赎罪的方式。
[name="剧团长"]他劝下早已体力不支的将军。就在对方小憩的十分钟里，他打开了城门。
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]而在同盟邦的军队进城前，他用剑捅穿了自己的心脏......这个叛徒，成了那场战役中最可悲的死者。
[name="剧团长"]古早的事了，卢西恩，古早到许多细节早已淹没在了历史的长河中。
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]维多利亚、莱塔尼亚......我在不同国家的十余座城市间寻访数月，终于找到了一位垂垂老矣的近卫军。
[name="卢西恩"]他曾亲眼见过加莱冲天的火光，他曾在那位叛徒的尸体上发现了一枚徽章——背对的两张面容，盛放着极致的微笑与眼泪。
[charslot(slot = "r", name = "avg_npc_1828_1#7$1", focus="r")]
[name="卢西恩"]我们都知晓那个标志意味着什么，老师。
[charslot(slot = "l", name = "avg_npc_1829_1#12$1", focus="l")]
[name="剧团长"]哈哈。
[name="剧团长"]想必，你还有更多的发现？
[dialog]
[charslot(slot = "l", focus="all")]
[PlaySound(key="$d_avg_openftstpwalk", volume=1)]
[Background(image="26_g1_laterano_cathedralfront",screenadapt="coverall", fadetime=2)]
[Delay(time=2.5)]
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]更早之前的拉特兰。
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]......
[charslot(slot = "r", name = "avg_npc_1828_1#2$1", focus="r")]
[name="卢西恩"]距今已经两百多年，某位惊才绝艳的枢机在大教堂前的广场上被铳骑格杀。
[name="卢西恩"]他聪颖而仁慈，被称为“离主最近的萨科塔”，年仅三十便已经是众望所归的下一任教宗。
[charslot(slot = "r", name = "avg_npc_1828_1#5$1", focus="r")]
[name="卢西恩"]可变化就那么发生了，他变得偏执而激进，布道、召集信徒、联络外使，试图向教宗问责......
[name="卢西恩"]......直到局势恶化成一场危及拉特兰全城的宗教政变。教宗重伤，铳骑出动，他成了拉特兰历史上唯一一位死于政变的枢机。
[name="卢西恩"]无人知晓他到底发生了什么......在某间安魂教堂偶遇一位途经拉特兰的菲林，当然也算不上值得深究的线索。
[charslot(slot = "l", name = "avg_npc_1829_1#12$1", focus="l")]
[name="剧团长"]你能挖出这些线索，想必费了不少功夫。
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]很麻烦。
[charslot(slot = "l", name = "avg_npc_1829_1#11$1", focus="l")]
[name="剧团长"]我只是施予了那位萨科塔一点“真相”——他已罹患绝症。
[name="剧团长"]庸碌的教宗只知解经，而对信仰有着无限热忱的自己却已时日无多，可能再无法将那些理想付诸实践，聆听新时代的钟声。
[name="剧团长"]但其实，他在戕害教宗的那一刻清醒了过来，发觉自己从未被死亡追上......
[charslot(slot = "r", name = "avg_npc_1828_1#8$1", focus="r")]
[name="卢西恩"]清醒即癫狂，他看着自己酿成的恶果，主动迎向了那些铳？
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]政治悲剧的缩影，剧团许多场演出的剧本自其中萌芽。
[name="剧团长"]令人唏嘘，不是吗？
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]......
[dialog]
[Background(image="27_g22_goldenboat_hall",screenadapt="coverall", fadetime=2)]
[Delay(time=3)]
[charslot(slot = "r", name = "avg_npc_1828_1#5$1", focus="r")]
[name="卢西恩"]伊比利亚。
[name="卢西恩"]那个灿若黄金的时代，灯塔照亮靠近的大船，人们却发现它只装载着海洋深处的风声，印着双生相的演出票根在甲板上飘荡......
[name="卢西恩"]已经消失的水手在唱——
[charslot(slot = "r", focus="n")]
唆使一只幼羽，去啄取痛苦的果实。
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]......
[dialog]
[Background(image="44_g3_ludwigsuniv_outside",screenadapt="coverall", fadetime=2)]
[Delay(time=3)]
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]莱塔尼亚的高塔之间，古老的术式记录着贵族的悲鸣与疾呼。
[charslot(slot = "r", focus="n")]
放逐一个婴孩，去抵达欢欣的死亡。
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]......
[dialog]
[Background(image="40_g5_samitribe",screenadapt="coverall", fadetime=2)]
[Delay(time=3)]
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]厚雪覆盖的聚落。
[charslot(slot = "l", name = "avg_npc_1829_1#1$1", focus="l")]
[name="剧团长"]杂草总能自行其道。
[name="剧团长"]......
[dialog]
[Background(image="53_g3_menatmainstreet_river",screenadapt="coverall", fadetime=2)]
[Delay(time=3)]
[charslot(slot = "r", name = "avg_npc_1828_1#1$1", focus="r")]
[name="卢西恩"]黄沙深处的城市。
[charslot(slot = "l", name = "avg_npc_1829_1#6$1", focus="l")]
[name="剧团长"]多亏眼泪、诳语与迷思。
[name="剧团长"]他离开凋零花朵筑成的寝床。
[name="剧团长"]......
[dialog]
[charslot(slot = "l", focus="all")]
[PlaySound(key="$d_avg_openft

... (全文38495字符)
```

### level_act43side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="24_RL_castlehall",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(intro="$m_sys_rglk1phantomcastle_intro",key="$m_sys_rglk1phantomcastle_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Sticker(id="st1",multi = true, text="他离开凋零花朵筑成的寝床，",x=200,y=200, alignment="center", size=24, delay=0.04, width=900,block = true)]
[Sticker(id="st1", multi = true,text="\n\n那是丰收的征兆，世人说。",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n于是有人在夜的怀抱中行走，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n于是有人在篝火前分享琼浆，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n于是有人相携着迷失在，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n故事分岔的地方。",size=24, alignment="center",block = true)]
[Sticker(id="st1",duration=1)]
[Delay(time=2)]
[Sticker(id="st1",multi = true, text="封住即将吹响号角的嘴唇，他说。",x=200,y=200, alignment="center", size=24, delay=0.04, width=900,block = true)]
[Sticker(id="st1", multi = true,text="\n\n蒙紧即将见证不朽的眼睛，他说。",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n唆使一只幼羽，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n去啄取痛苦的果实。",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n放逐一个婴孩，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n去抵达欢欣的死亡。",size=24, alignment="center",block = true)]
[Sticker(id="st1",duration=1)]
[Delay(time=2)]
[Sticker(id="st1",multi = true, text="杂草总能自行其道，",x=200,y=200, alignment="center", size=24, delay=0.04, width=900,block = true)]
[Sticker(id="st1", multi = true,text="\n\n多亏眼泪、诳语与迷思，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n他离开凋零花朵筑成的寝床。",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n他将墓志铭写进飞扬的尘土里，",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n等待自己终有一日——",size=24, alignment="center",block = true)]
[Sticker(id="st1",multi = true, text="\n\n瞻仰。",size=24, alignment="center",block = true)]
[Sticker(id="st1",duration=1)]
[Delay(time=2)]
[subtitle]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="62_g1_setting_lobby",screenadapt="coverall")]
[focusout(duration=0, type="bg", from=0, to=0.3)]
[backgroundTween(xScaleFrom=1.6, yScaleFrom=1.6, xScaleTo=1.6, yScaleTo=1.6, block=true, fadetime=0.1)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.1,block=false, fadetime=0)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.1,block=true, fadetime=0)]
[charslot(slot = "r",action="zoom", poszoom = "0.5,0.5", scale=1.07,name = "avg_npc_417_1#1$1",afrom=0,ato=0)]
[charslot(slot = "r",posfrom = "0,0", posto = "0,-30",duration = 0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=0.1)]
[charslot(slot = "left", name = "avg_npc_243",duration = 1)]
[charslot(slot = "right",duration = 1,afrom=0,ato=1)]
[delay(time=1.5)]
[charslot(slot = "right",focus="r")]
[name="八卦的男佣"]怎么说，杜邦夫人还是把自己关在房间里不肯出来？
[charslot(slot = "l",focus="l")]
[name="忧心的女仆"]已经三天了，食物也没怎么动，再这样下去可怎么办......
[charslot(slot = "right",focus="r")]
[name="八卦的男佣"]照我说，夫人压根没必要这么纠结。
[name="八卦的男佣"]作为杜邦家族的遗孤，维多利亚曾经最高贵的血脉的继承者，她优雅、知性，那三个人里，她选择谁作为伴侣都不为过。
[charslot(slot = "l",focus="l")]
[name="忧心的女仆"]正因如此，夫人才如此痛苦。
[name="忧心的女仆"]洛克菲勒家族那三兄弟，有着如同一个模子刻出来的英俊面容，性格与事业却截然不同。
[name="忧心的女仆"]聪慧的学者、勇敢的军人和浪漫的诗人同时向你展开追求，你能够想象自己将和谁共度余生吗？
[name="忧心的女仆"]更何况，夫人无论选择哪个洛克菲勒，都会伤透另外两个洛克菲勒的心。
[name="忧心的女仆"]哦，我的天哪！
[charslot(slot = "right",focus="r")]
[name="八卦的男佣"]哦，我的天哪！我只求她赶紧决定，最好下个月就举行婚礼。洛克菲勒家族坐拥万贯家产，到时候给我们的打赏少不了！
[charslot(slot = "l",focus="l")]
[name="忧心的女仆"]你这人——
[stopmusic(fadetime=2)]
[charslot(slot = "l",focus="n")]
[name="？？？"]Cut！
[charslot(slot = "l",focus="l")]
[name="忧心的女仆"]斯蒂芬导演？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[curtain]
[focusout(duration=0, type="bg", from=0, to=0)]
[Background(image="62_g3_filmset",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$victorianormal_loop", volume=0.6)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1835_1#1$1",duration=1.5)]
[delay(time=2)]
[name="斯蒂芬"]唉......生硬刻板的演技。
[charslot(slot="m",name="avg_npc_1835_1#7$1")]
[name="斯蒂芬"]（小声）本来也只是向观众传递信息的功能性戏份，不如整场砍掉，后续补几个更有象征意味的空镜......
[charslot(slot="m",name="avg_npc_1835_1#1$1")]
[name="斯蒂芬"]（小声）但愿我们热爱干预导演工作的制片人女士不会为这种小事较真。
[name="斯蒂芬"]你们下去吧，剧本临时有了一些“调整”......一会儿正式拍摄的时候不用来了。
[charslot]
[charslot(slot = "left", name = "avg_npc_243",focus="r")]
[charslot(slot = "right", name = "avg_npc_417_1#1$1",focus="r")]
[name="八卦的男佣"]又有“调整”？我们的导演真是优柔寡断。
[charslot(slot = "left", name = "avg_npc_243",focus="l")]
[name="忧心的女仆"]嘘——
[Dialog]
[charslot(slot = "r",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[charslot(slot = "l",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, channel="bgs",fadetime=2)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_1835_1#5$1")]
[name="斯蒂芬"]好了各位，还没到休息时间，闭嘴......闭嘴！
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1835_1#5$1")]
[name="斯蒂芬"]我知道连续拍了两个月大家都很疲惫，现在移动地块又开出了主城区，没有赌场和商店街，自助酒吧的存货也难喝得要死......
[name="斯蒂芬"]但是！无论好坏都只剩下最后一周了，拍摄时间很宝贵，我的胶片也是。
[name="斯蒂芬"]《杜邦夫人之死》，蓝卡坞近期少见的上个时代的悲剧题材，通过一位贵族女性的荒唐婚变来反映哥伦比亚时代交替的阵痛......
[name="斯蒂芬"]我不希望它最后上映时看起来只是拿来洗钱的垃圾！
[charslot(slot="m",name="avg_npc_1835_1#1$1")]
[name="斯蒂芬"]继续走戏。
[name="斯蒂芬"]《杜邦夫人之死》，宅邸露台，第三场......米兰妮，迈克尔，到你们了。
[Dialog]
[Blocker(a=1, r=0

... (全文35945字符)
```

### level_act43side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="62_g3_filmset",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot = "left", name = "avg_npc_1845_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1847_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left",focus="l")]
[name="工作人员A"]喂喂，你也看到迈克尔和玛丽昂的尸体了，对吧？
[charslot(slot = "right",focus="r")]
[name="工作人员B"]哎哟，我好不容易才把那个恐怖的景象从脑子里面赶出去，你怎么又说起来了！
[name="工作人员B"]我、我的手都在抖，感觉要握不住录音杆了......
[charslot(slot = "left",focus="l")]
[name="工作人员A"]你怎么还想着工作！我们现在待着的地方真的有一个连环杀人魔！
[charslot(slot = "right",focus="r")]
[name="工作人员B"]那我们赶紧逃吧？
[charslot(slot = "left",focus="l")]
[name="工作人员A"]逃？你忘了迈克尔和玛丽昂是为什么被凶手盯上的吗？
[charslot(slot = "left",focus="l")]
[name="工作人员A"]迈克尔的脚下还放着行李，听说他做了充足的准备，找到了私下开溜的路子......
[name="工作人员A"]但他还是在离开这个地块的前一刻被找上了。
[name="工作人员A"]那个凶手不会让任何人离开的。
[name="工作人员A"]就像《开膛黎博利杰克》一样，这里是他的猎场，我们每个人都可能是他的猎物。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1843_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1844_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "right",focus="r", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]阿布纳，你多久没检查胸架了？
[name="摄影助理"]看，升降臂这边的几个螺丝都已经松了，一个不小心，摄影机就得在地上砸个粉碎......
[charslot(slot = "left",focus="l", name = "avg_npc_1843_1#1$1")]
[name="阿布纳"]碎了就碎了。
[charslot(slot = "right",focus="r", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]那我帮你保养下这几组镜头吧。
[charslot(slot = "left",focus="l", name = "avg_npc_1843_1#1$1")]
[name="阿布纳"]不用。
[charslot(slot = "right",focus="r", name = "avg_npc_1844_1#1$1")]
[name="摄影助理"]我是你的助理，阿布纳。
[charslot(slot = "left",focus="l", name = "avg_npc_1843_1#4$1")]
[name="阿布纳"]别以为我不知道你献殷勤是为了什么——滚远点，小子。
[charslot(slot = "right",focus="r", name = "avg_npc_1844_1#3$1")]
[name="摄影助理"]道尔顿的死不是意外，对不对？还有谢莉、迈克尔和玛丽昂......
[name="摄影助理"]凶手不可能是无差别杀人，所有的受害者，都和五年前的那起意外有关。
[charslot(slot = "left",focus="l", name = "avg_npc_1843_1#4$1")]
[name="阿布纳"]你该去当娱乐记者，而不是摄影助理。
[charslot(slot = "right",focus="r", name = "avg_npc_1844_1#5$1")]
[name="摄影助理"]不矛盾啦，前者更好讨生活......阿布纳，我的好阿布纳，五年前你也在，反正现在有时间，你就跟我说说嘛！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_1835_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1830_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1835_1#1$1",focus="l")]
[name="斯蒂芬"]米兰妮女士，这会儿没有您的戏......
[charslot(slot = "right", name = "avg_npc_1830_1#6$1",focus="r")]
[name="米兰妮"]我难道能安心继续在房间里研究“杜邦夫人”死前的妆造？
[charslot(slot = "left", name = "avg_npc_1835_1#7$1",focus="l")]
[name="斯蒂芬"]这关系到结尾那几场高潮戏，抱歉，我还没有......
[charslot(slot = "right", name = "avg_npc_1830_1#1$1",focus="r")]
[name="米兰妮"]啊，你的神迟到了。但我现在没有心情责怪你和你的神，亲爱的。
[name="米兰妮"]发生了这么大的事，如果不是离主城区太远，蓝卡坞的警察这会儿已经封锁整个地块，项目也早已停工......
[name="米兰妮"]当然，现在的情况也没有好到哪儿去。
[charslot(slot = "right", name = "avg_npc_1830_1#5$1",focus="r")]
[name="米兰妮"]斯蒂芬，我开始担心自己的投资要血本无归了。
[name="米兰妮"]这几天发生的事情，你知道多少隐情？格蕾塔知道多少？
[charslot(slot = "left", name = "avg_npc_1835_1#4$1",focus="l")]
[name="斯蒂芬"]......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1845_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="工作人员C"]斯蒂芬导演，米兰妮女士，原来二位也在啊。
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.7, channel="bgs",fadetime=3)]
[name="工作人员C"]制片人呢？格蕾塔应该给所有人一个说法！
[Dialog]
[charslot]
[Delay(time=0.5)]
[Dialog]
[charslot(slot="m",name="avg_npc_1834_1#5$1",duration=1)]
[Delay(time=2)]
[name="格蕾塔"]......
[charslot(slot = "m", focus = "n")]
窃窃私语。
到处都是窃窃私语的声音，整个摄影棚内，没有一个人在工作。
三起命案、四个死者，接二连三的变故摧毁了这些人的状态，恐慌、愤怒、困惑、无所适从......整个剧组在失控的边缘。
真吵啊，吵得人心里乱糟糟的。她讨厌这种感觉。
[stopmusic(fadetime=3)]
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_spotlight", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1834_1#6$1",duration=1)]
[Delay(time=2)]
[charslot(slot = "m", focus = "n")]
格蕾塔径直走向摄影棚的中央，她打开了最亮的那盏场灯，刺目的光亮逼停了每一个人的动作和话头，人们注意到了她。
格蕾塔深深呼吸。
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[charslot(slot = "m", focus = "m")]
[name="格蕾塔"]各位，我要宣布一些事情。
[name="格蕾塔"]我不是演员，台词功底没那么好，听不清的往我这边靠。
[charslot(slot = "m", focus = "n")]
[playsound(key="$d_avg_footsteps_flock",volume=0.5)]
[name="米兰妮"]......
[name="斯蒂芬"]......
[name="阿布纳"]......
[name="工作人员们"]......
[Dialog]
[Delay(time=1)]
[charslot(slot = "m", focus = "m")]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.3, channel="bgs",fadetime=2)]
[name="格蕾塔"]几分钟后，各位可以查看自己在蓝卡坞的专属金融终端。来之前，我已经委托财务，付清了剧组每一位成员酬劳的尾款。
[name="格蕾塔"]当然，道尔顿、谢莉、迈克尔、玛丽昂，除了为这几位朋友结算应得的酬劳之外，还会给他们的家属发放抚恤金，我事后会专门处理。
[name="格蕾塔"]是的，《杜邦夫人之死》的拍摄还没有结束，合同还有效力，我本不需要这么做——但毕竟，已经没几个人的心思还在工作上了。
[charslot(slot="m",name="avg_npc_1830_1#1$1")]
[name="米兰妮"]嘿，格蕾塔，这不像你。
[name="米兰妮"]剧组只不过是出了一些......不算小的意外，还没到放弃的时候。
[name="米兰妮"]还是说，经历这些事情之后，作为制片人，你已经对电影最后的质量不抱任何信心了。
[charslot(slot="m",name="avg_npc_1834_1#1$1")]
[name="格蕾塔"]放弃？亲爱的，你想多了。
[name="格蕾塔"]我从不怀疑自己的眼光，自然也谈不上会放弃。
[charslot(slot="m",name="avg_npc_1830_1#3$1")]
[name="米兰妮"]可是你现在......
[dialog]
[charslot(slot="m",name="avg_npc_1834_1#1$1")]
[StopSound(channel="bgs", fadetime=2)]
[name="格蕾塔"]我给大家讲个故事吧。
[name="格蕾塔"]喂，小子......
[charslot(slot="m",name="avg_npc_1844_1#6$1")]
[name="摄影助理"]格蕾塔女士，您是在叫我？
[charslot(slot="m",name="avg_npc_1834_1#1$1")]
[name="格蕾塔"]拿出你的录音笔、笔记本、速记终端......随便什么，然后坐好，用心听。
[charslot(slot="m",name="avg_npc_1844_1#6$1")]
[name="摄影助理"]什、什么意思？
[charslot(slot="m",name="avg_np

... (全文11162字符)
```

### level_act43side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Background(image="bg_cellroomC",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>哥伦比亚，蓝卡坞郊外，联邦移动监狱</><p=2>两个月后</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot = "l", name = "avg_4191_tippi_1#2$1", duration=1.5)]
[charslot(slot = "r", name = "avg_npc_1831_1#1$3", duration=1.5)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_4191_tippi_1#2$1", focus="l")]
[charslot(slot = "r", name = "avg_npc_1831_1#1$3", focus="n")]
[name="蒂比"]莫丽，你瘦了好多啊！
[charslot(slot = "r", name = "avg_npc_1831_1#9$3", focus="r")]
[name="莫伊拉"]毕竟在床上躺了两个月嘛。
[charslot(slot = "l", name = "avg_4191_tippi_1#9$1", focus="l")]
[name="蒂比"]当时地块停下来的第一时间我就去找你了。我看到医护人员抬着你出来，你浑身都是血，一动不动，我以为你已经......
[charslot(slot = "r", name = "avg_npc_1831_1#1$3", focus="r")]
[name="莫伊拉"]他的歌声......很可怕。
[name="莫伊拉"]但他只是想让我停下来，没有对我下死手。
[name="莫伊拉"]他绝对不是像格蕾塔说的那样，在剧本拍卖会上与她偶遇，被说服后跟来剧组的，他另有目的。
[charslot(slot = "l", name = "avg_4191_tippi_1#10$1", focus="l")]
[name="蒂比"]另有目的？
[charslot(slot = "r", name = "avg_npc_1831_1#1$3", focus="r")]
[name="莫伊拉"]他在找某个存在，某个就在我们身边但我们一无所知的存在。
[charslot(slot = "l", name = "avg_4191_tippi_1#10$1", focus="l")]
[multiline(name="蒂比")]啊，我本来就觉得卢西恩很神秘，你这么一说我更云里雾里了......
[charslot(slot = "l", name = "avg_4191_tippi_1#3$1", focus="l")]
[multiline(name="蒂比",end=true)]算了不说他了！
[charslot(slot = "l", name = "avg_4191_tippi_1#9$1", focus="l")]
[name="蒂比"]真对不起啊莫丽，过了这么久才来看你。主要是、主要是联邦移动监狱的探视申请有点麻烦......
[charslot(slot = "r", name = "avg_npc_1831_1#5$3", focus="r")]
[name="莫伊拉"]我知道的，蒂比。
[name="莫伊拉"]我利用了你，害你被误会......
[name="莫伊拉"]卢西恩先生说得没错，我甚至忽略了我本就拥有的真实。在我陷入癫狂的最后时刻，我甚至，没能想起你......
[charslot(slot = "l", name = "avg_4191_tippi_1#2$1", focus="l")]
[name="蒂比"]莫丽，你听我说。
[name="蒂比"]无论你经历了什么，无论你出于什么目的，你都伤害了那些和我们朝夕相处的人，你犯下了罪孽，我永远、永远都不会原谅你！
[charslot(slot = "l", name = "avg_4191_tippi_1#9$1", focus="l")]
[name="蒂比"]......但是莫丽，这并不影响我怀念那些我们两个人窝在沙发里看恐怖片的时光。
[name="蒂比"]那么快乐，那么真实，不是吗？
[charslot(slot = "r", name = "avg_npc_1831_1#5$3", focus="r")]
[name="莫伊拉"]......是啊。
[charslot(slot = "r", name = "avg_npc_1831_1#12$3", focus="r")]
[name="莫伊拉"]躺在病床上的时候，伤口很疼，睡不着，我就一直在回想这段时间发生的一切......
[name="莫伊拉"]一整夜过去，只有我自己的疼痛是最真实的。
[charslot(slot = "r", name = "avg_npc_1831_1#5$3", focus="r")]
[name="莫伊拉"]其实，无论故事被写得多么荒唐，无论我们是不是命运的傀儡，我并不是没有机会。
[name="莫伊拉"]如果我们在一起看电影的时候，我能更专心一些，而不是去想那些我以为自己看到的真相，仇恨和疯狂，鲜血和人偶......
[name="莫伊拉"]对不起，蒂比。
[charslot(slot = "l", name = "avg_4191_tippi_1#9$1", focus="l")]
[name="蒂比"]如果我可以早点遇见你的话，或许你就不需要“劳拉”了......
[dialog]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_4191_tippi_1#9$1", focus="l")]
[name="蒂比"]过两天就是最终的庭审了吧？我咨询过几位律师，好像......
[charslot(slot = "r", name = "avg_npc_1831_1#1$3", focus="r")]
[name="莫伊拉"]......
[charslot(slot = "l", name = "avg_4191_tippi_1#9$1", focus="l")]
[name="蒂比"]......
[charslot(slot = "r", name = "avg_npc_1831_1#9$3", focus="r")]
[name="莫伊拉"]不用在意结果，蒂比。
[name="莫伊拉"]典狱长人很好，他允许我最后这几天待在监狱的后勤部门，去做一些犯人们用得着的东西。
[name="莫伊拉"]我并不是，像之前那样，虚妄地等待最后的......
[charslot(slot = "l", name = "avg_4191_tippi_1#2$1", focus="l")]
[name="蒂比"]那就好、那就好。
[charslot(slot = "r", name = "avg_npc_1831_1#9$3", focus="r")]
[name="莫伊拉"]哈哈，你探视的时间好像不多了，说点开心的事情吧。
[name="莫伊拉"]剧组拍的那部电影最后怎么样了？
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlaySound(key="$d_avg_crwddiscuss_inside",loop=true,channel="cr",volume=0)]
[SoundVolume(volume=0.2, channel="cr",fadetime=2)]
[Background(image="62_g1_setting_lobby",screenadapt="coverall")]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>哥伦比亚，蓝卡坞主城区，“另类电影节”展映现场</><p=2>一天前</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[StopSound(channel="cr", fadetime=2)]
[PlaySound(key="$d_avg_carpet_normal_fts", volume=1)]
[charslot(slot = "r", name = "avg_npc_1835_1#1$1", posfrom="70,0", posto="70,0", duration=1.5)]
[charslot(slot = "l", name = "avg_npc_1834_1#1$1", posfrom="-70,0", posto="-70,0", duration=1.5)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1830_1#1$1", duration=1.5, isblock=true)]
[delay(time=2)]
[charslot]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="a")]
[StopSound(channel="a", fadetime=1.5)]
[charslot(slot = "m", name = "avg_4191_tippi_1#1$1", duration=1, isblock=true)]
[Delay(time=0.5)]
[name="蒂比"]哇，大家都已经在了啊，对不起我来迟了！
[dialog]
[charslot(slot = "m", name = "avg_npc_1835_1#7$1")]
[name="斯蒂芬"]......
[charslot(slot = "m", name = "avg_npc_1834_1#1$1")]
[name="格蕾塔"]斯蒂芬，紧张吗？
[charslot(slot = "m", name = "avg_npc_1835_1#7$1")]
[name="斯蒂芬"]有一点。
[charslot(slot = "m", name = "avg_npc_1834_1#1$1")]
[name="格蕾塔"]放轻松。
[name="格蕾塔"]最后的拍摄以那样荒唐的方式结束，剪辑、调色、音乐制作......两个月的时间完成后期制作，每个人都已经尽力了。
[charslot(slot = "m", name = "avg_npc_1830_1#2$1")]
[name="米兰妮"]斯蒂芬，很高兴在电影名的修改上，我们达成了共识。
[charslot(slot = "m", name = "avg_npc_1835_1#2$1")]
[name="斯蒂芬"]米兰妮女士，也感谢您最后在天灾中的那段表演。否则，删去那两个字只是我个人的一些矫情的自我斗争。
[charslot(slot = "m", name = "avg_npc_1830_1#2$1")]
[name="米兰妮"]《杜邦夫人》显然没《杜邦夫人之死》那么有噱头，宣发的事情就让格蕾塔去头疼吧......但毫无疑问，这是最适合故事的名字。
[charslot(slot = "m", name = "avg_npc_1834_1#1$1")]
[name="格蕾塔"]交给我吧。
[multiline(name="格蕾塔")]我会让《杜邦夫人》顺利上映......
[charslot(slot = "m", name = "avg_npc_1834_1#6$1")]
[multiline(name="格蕾塔",end=true)]然后我会去一趟警局，做我该做的事情。
[dialog]
[PlaySound(key="$d_avg_crwddiscuss_inside",loop=true,channel="cr",volume=1)]
[charslot(duration=0.5, isblock=true)]
[Delay(time=1)]
[playsound(key="$skill_flash",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetim

... (全文18549字符)
```

### training_act43side_01_a

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_popka", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]原来蓝卡坞的移动拍摄地块长这样！咦，这些人怎么了，看上去有些奇怪......
[battle.pause(pause=false)]
```

### training_act43side_01_b

```
[header(is_skippable=false, is_tutorial=true)]
[battle.lockfunction(mask="SYSTEM_MENU_INTERACT")]
[battle.delay(time=0.3)]
[battle.pause(pause=true)]
[popupdialog(dialogHead="$avatar_aprot2", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]......这里弥漫着令人不安的气息，我们快些收集情报吧。
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_aprot2", tileY=2, tileX=4)]那边有一台<@tu.kw>摄影机</>？看起来还可以使用......
[popupdialog(dialogHead="$avatar_aprot2")]泡普卡干员，我会<@tu.kw>对着你拍摄</>，记录这里的情况！
[inputblocker(blockInput=false)]
[battle.ensuremincost(cost=14)]
[tutorial(animStyle="Drag", protectTime=0.5, waitForSignal="put_down", cardIndex=0, startCardIndex=0, endTileX=4, endTileY=1, charId="char_4025_aprot2", posX=4, posY=1)]
[tutorial(animStyle="Drag", waitForSignal="select_direction", startTileX=4, startTileY=1, endTileX=4, endTileY=3)]
[inputblocker(blockInput=true)]
[battle.unlockfunction(mask="SYSTEM_MENU_INTERACT")]
[battle.pause(pause=false)]
```

### training_act43side_01_c

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_popka", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]看那边，泡普卡发现那个<@tu.kw>打光道具</>会<@tu.kw>干扰摄影区域</>！
[popupdialog(dialogHead="$avatar_catap", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]碍事的东西吗？交给我！
[battle.pause(pause=false)]
```

### training_act43side_01_d

```
[header(is_skippable=false, is_tutorial=true)]
[battle.delay(time=0.3)]
[battle.lockfunction(mask="SYSTEM_MENU_INTERACT")]
[battle.pause(pause=true)]
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_catap", tileY=3, tileX=1)]糟糕，敌人从摄影机拍摄不到的地方过来了！
[popupdialog(dialogHead="$avatar_spot", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]放心，我来改变<@tu.kw>摄影机的朝向</>。
[inputblocker(blockInput=false)]
[battle.ensuremincost(cost=15)]
[tutorial(animStyle="Drag", protectTime=0.5, waitForSignal="put_down", cardIndex=0, startCardIndex=0, endTileX=5, endTileY=2, charId="char_284_spot", posX=5, posY=2)]
[tutorial(animStyle="Drag", waitForSignal="select_direction", startTileX=5, startTileY=2, endTileX=3, endTileY=2)]
[inputblocker(blockInput=true)]
[battle.unlockfunction(mask="SYSTEM_MENU_INTERACT")]
[battle.pause(pause=false)]
```

### training_act43side_01_e

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_popka", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]呜哇，这些人在摄影区域就无法对泡普卡造成神经损伤了！
[popupdialog(dialogHead="$avatar_aprot2", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]太好了，没想到这个摄影机还能够<@tu.kw>削弱他们的战力</>！
[battle.pause(pause=false)]
```


## 统计

- 总字符数：337485
- 对话行数：2593


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
