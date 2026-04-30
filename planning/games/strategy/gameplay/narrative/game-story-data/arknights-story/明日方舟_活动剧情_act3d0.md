# 明日方舟 · 活动剧情 · act3d0（25段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act3d0」完整剧情脚本（25个文件，1353行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act3d0
- 脚本文件数：25

### level_act3d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Background(image="bg_forest", fadetime=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character]
[Delay(time=1)]
[playsound(key="$leaveshake", volume=0.7)]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2,fadetime=1,block=true)]
[Delay(time=1)]
[name="天火"]   普罗旺斯。
[name="天火"]   普罗旺斯，我真的真的不能把这里烧干净吗？
[name="天火"]   这些长得毫无意义的树枝和草实在是太碍事了。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   这已经是一小时内你第十次抱怨了，天火大小姐。
[name="普罗旺斯"]   本来我就只是想来验证一下我的疑惑而已，顺便帮艾雅法拉小姐收集一些样本。
[name="普罗旺斯"]   可是你自己提出要一起来实地勘察的，要是实在忍受不了这里的生态环境的话，也不用强忍着。
[name="普罗旺斯"]   现在大家应该都在海边玩，你直接回去和大家汇合就好，你完全不用跟我来受这种罪的。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]  不，我才不放心你这么乱来。
[name="天火"]  虽然有你这样的天灾信使在，只有以我的知识储备，才能保证火焰环境下的你们不出什么意外状况。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   这样的话，万一反而在山上引起大火就不妙了。
[name="普罗旺斯"]   虽然我知道你能应付那种情况......这一次我们毕竟只是来度假的，还是不要引起什么混乱比较好。
[name="普罗旺斯"]   否则到时候又要给博士他们添麻烦了。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]   好吧，看在博士和阿米娅的面子上，忍耐一下也没什么问题。
[name="天火"]   诶，那边有一堆黑色的石头你看到了吗？
[name="天火"]   好像是黑曜石什么的，我过去看看。
[Dialog]
[Character]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   小心一点，别在这一带乱跑。尤其是不要随意用火！
[name="普罗旺斯"]   呼......应付这位小姐可比实地勘察要累多了。
[name="普罗旺斯"]   不过，真奇怪......即使是夏天，这里的气温......也有些反常。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[playsound(key="$leaveshake", volume=0.7)]
[Blocker(a=0, fadetime=2, block=false)]
[Delay(time=2)]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   大尾巴。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   ......
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[CameraShake(duration=0.3, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="天火"]   我说，大尾巴！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   嗯？欸，你是在叫我？
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   你从刚才起有闻到什么奇怪的味道吗？
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   这么说的话，的确有点......
[name="普罗旺斯"]   唔。很微弱，但是我敢肯定不是错觉。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   火山气体排出的量比我想象中要多，而且艾雅法拉交给我的检测符文也已经有反应了。
[name="天火"]   看上去不用我做什么，搞不好再过一段时间，这里就自然会变成一片火海哦。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   这座火山的确有可能有问题......
[name="普罗旺斯"]   但是更多的我们只能向艾雅法拉小姐求证了。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   这边，岩壁上还有些样本。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="普罗旺斯"]   喝！
[name="普罗旺斯"]   好，这些就够了！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[playsound(key="$leaveshake", volume=0.7)]
[Blocker(a=0, fadetime=2, block=false)]
[Delay(time=2)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]    样品数据可以用临时的仪器做点检测，然后发回罗德岛。
[name="天火"]    艾雅法拉那一头应该会最快作出后续数据分析。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=1)]
[name="普罗旺斯"]   可是从这些黑曜石的触感看来......我也不知道，这里的黑曜石感觉有点特殊，不像是普通的黑曜石。
[name="普罗旺斯"]   加上刚才闻到的那股味道以及这里的气温......
[name="普罗旺斯"]   虽然我也不确定，但是......
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   你到底想说什么，支支吾吾的，干脆一点！
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[name="？？？"]   来啊！不过是几个虫子而已！看我就在这里把你们都收拾掉！
[CameraShake(duration=0.8, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="？？？"]   可恶，裙子的下摆卡住了......
[name="？？？"]   有、有没有人在这附近啊！为什么这里的源石虫会聚集这么多啊？！
[name="？？？"]   不、不要过来啊！谁来帮帮我！
[PlayMusic(intro="$indust_intro", key="$indust_loop", volume=0.8, crossfade=0.5)]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   是求救声！海滩那边传来的！
[name="普罗旺斯"]   我们快过去看看！
[Character(name="char_166_skfire_3#1")]
[name="天火"]   喂，等等我啊！
[Character(fadetiem=1)]
[Dialog]
[PlaySound(key="$runsand",volume=0.5)]
[Delay(time=0.5)]
[Dialog]
[Blocker(block=true)]
```

### level_act3d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（后）
[Background(image="bg_hotel",screenadapt="coverall", fadetime=1)]
[Dialog]
[Character]
[Delay(time=1)]
[Decision(options="原来是这样......",values="1")]
[Predicate(references="1")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   就是如此，我们在火山脚下的森林里，碰到了锡兰小姐。
[Dialog]
[Character]
[Character(name="char_348_ceylon_4#7",fadetime=1,block=true)]
[Delay(time=1)]
[name="锡兰"]   我有一个问题。
[name="锡兰"]   有必要把你们解救我之前的过程描述得这么详细吗？
[Character(name="char_348_ceylon_4#7",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   我觉得这位大小姐说得对，而且大尾巴你是不是还提到了你觉得我很麻烦？
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   欸，啊，是你的错觉！
[Decision(options="不管怎么说，大家平安无事就好。",values="1")]
[Predicate(references="1")]
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   嗯，那么，虽然比较晚了，请容我正式自我介绍一下。
[name="锡兰"]   我的名字是锡兰·道尔科斯，维多利亚国立大学毕业，专攻方向是源石研究，也是这座城市市长的女儿。
[Decision(options="市长的女儿？！",values="1")]
[Predicate(references="1")]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]   谁会想到市长的女儿会独自去未开发的火山林地呢。
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]    那也是因为不得不做一些学者必须要去尝试的冒险......
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   继续说回到刚才在火山脚下......
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_forest")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_348_ceylon_4#7")]
[name="锡兰"]   咳、咳咳。
[name="锡兰"]   谢谢你们，陌生人。
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   不用客气。
[name="普罗旺斯"]   不过，你为什么会一个人来这里？
[name="普罗旺斯"]   如果只是在沙滩上散步的话，你走得稍微有些远了呢。
[name="普罗旺斯"]   唔，从你身上带的工具来看......
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]   普罗旺斯，她也和我们一样，是来查看状况。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=1)]
[name="普罗旺斯"]   咦，是这样吗？
[Character(name="char_145_prove_1",name2="char_166_skfire_3#3",focus=2)]
[name="天火"]   带着笔记，却穿着洋装和靴子。
[name="天火"]   如果不是单纯的傻子的话，那就只能是————
[name="天火"]   忽然产生了灵感，忘记换衣服直接冲出家门，等遇到了麻烦才发现穿着问题。
[name="天火"]   我不记得因为这样的事情烧毁过多少裙子了。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#3",focus=1)]
[name="普罗旺斯"]   唔，我觉得这似乎不是应该用理所当然的口吻来描述的事？
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   姑且不论裙子的事情，大体上你的判断没有错。
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   该说什么好呢，这么做还是有些危险的哦......没有准备完全的话。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#3",focus=2)]
[name="天火"]   没事。只要我在，哪怕是两手空空出门也会很安全。
[Character(name="char_348_ceylon_4#5",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   总之，谢谢你们救了我。
[name="锡兰"]   等回到市内时，可以来找我，我会报答你们。
[name="锡兰"]   但抱歉，现在我很忙，我有重要的事要做。
[Character(name="char_348_ceylon_4#5",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   哦哦原来你还有事，那就不耽误你时间了，不过最好还是不要独自再去火山那里了。
[name="普罗旺斯"]   你刚才才被这些源石虫袭击了，一个人很危险的。
[Character(name="char_348_ceylon_4#2",name2="char_145_prove_1",focus=1)]。
[name="锡兰"]   不，刚才的事我认为只是个意外。当时我急着上山了，没有注意附近情况。
[name="锡兰"]   我在这座城市长大，如果这里的源石虫真的有那么危险，那市长应该早就采取对策了。
[Character(name="char_348_ceylon_4#2",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   ......呃，好吧。不过，我觉得，或许它们的聚集是有原因的。
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   这里一直都是这样，怎么会......
[Character(name="char_348_ceylon_4#8",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   等等，因为环境改变带来的狂躁化......原来如此，谢谢你，我的证据又多了一条！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]   ......普罗旺斯，看起来她和你发现了一样的东西。
[name="天火"]   虽然我对火山没有那么熟悉，但是作为一名专业而全面的学者，大致的了解还是有的。
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   难道说，你们也是来寻找证据的吗？
[name="锡兰"]   寻找这座火山可能会爆发的证据？
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_hotel")]
[Blocker(a=0, fadetime=2, block=true)]
[Decision(options="火山爆发？！;开玩笑吧？！",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   特殊的刺激性气味，加上异常的气温、狂躁化的源石虫.....
[name="普罗旺斯"]   况且在火山周围能遇到这种感染生物，也说明这火山也不太一般。要知道如果这山内有源石的话，矿业开采商可是会挤破头的。
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   火山的实际情况并没有多少人知道，而且通常也被市政厅和相关机构管理着。
[name="锡兰"]   因为环境改变带来的生物狂躁化......至少对比以前的状况，我多少也能对现在的异变有些猜测。
[name="锡兰"]   为了保障市民和城市的安全，我一直在到处寻找对此方面有专业经验的人。
[name="锡兰"]   希望你们务必要帮助我，帮助我让汐斯塔市度过这个难关。
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_act3d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第四关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$fesready_intro", key="$fesready_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_sunnytown_2",screenadapt="coverall", fadetime=1,block=true)]
[Dialog]
[Character(name="char_348_ceylon_4#4",fadetime=1,block=true)]
[Delay(time=1)]
[name="锡兰"]   穿过市民广场，那栋最高的建筑就是市政厅了。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Character]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_NPC_017_3",fadetime=1,block=true)]
[Delay(time=1)]
[name="D.D.D."]   分会场的大家你们还好吗！！感谢你们来到这里，我是D.——D.——D.————！
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   （震天的欢呼声）
[Character(name="avg_NPC_017_3")]
[name="D.D.D."]   在这炎炎夏日，各位聚集在这里的目的想必都是一样的，那就是——
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   音——乐——！
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   我没有听到你们在说什么？！用你们最大的音量，让整个汐斯塔都听到，你们想要什么！！！
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   音————乐————！！！
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_NPC_017_3")]
[name="D.D.D."]   那么——举起你们的双手！准备出发！！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Delay(time=0.5)]
[Character]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   黑曜石节期间，这是每天都有的事。毕竟音乐会可是黑曜石节上大家最喜爱的部分之一。
[name="锡兰"]   主LIVE到晚上才会在加里森游乐园的最大舞台举办，白天的时候也会在各个地区开展小型的现场活动。
[Decision(options="我已经热血沸腾了！;这样的音乐有点猛烈......",values="1;2")]
[Predicate(references="1;2")]
[name="锡兰"]   哈哈，我也这么觉得，我在维多利亚留学时，更喜欢古典和优雅的音乐。
[name="锡兰"]   虽然黑曜石节也有请到那样的音乐艺人，不过实际上如你们所见，还是这种音乐更能吸引游客。
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   应该是这些年流行起来的吧，我小的时候，爵士还是主流呢。
[name="锡兰"]   我最喜欢在第二大道上待着，带上几本我最喜欢的书，我就能在那里的咖啡馆坐上一天。
[name="锡兰"]   听着音乐，喝着一杯绿茶，吹着海风。
[name="锡兰"]   我在那个时候就开始相信了，汐斯塔一定是这世界上最棒的城市。
[Decision(options="看来你也爱着这个地方呢。",values="1")]
[Predicate(references="1")]
[Character(name="char_348_ceylon_4#6")]
[name="锡兰"]   当然！这里有我重要的家人，我重要的支柱。
[name="锡兰"]   除开爸爸以外，还有一位对我来说很重要的人也在市政厅工作。
[name="锡兰"]   一会儿应该也能见到她。有了她的帮助，让其他人理解事情的严重性肯定会轻松很多！
[Decision(options="听起来你很信任她？;是你的母亲吗？",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   我的母亲在生我的时候就去世了。去世后父亲也变得埋头于工作。
[name="锡兰"]   从我小时候一直照顾着我的人是我家里的保镖，她的名字叫黑。
[name="锡兰"]   父亲操劳的时候，是她陪着我忍耐着我的任性。即使没有血缘关系，但是黑就像我的姐姐一样，是我重要的家人。
[name="锡兰"]   一会儿见到她我再给博士你介绍介绍。
[name="锡兰"]   看，博士，前面就是了。我们直接进去吧。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_offce")]
[stopmusic(fadetime=3)]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$doorknockquite", volume=0.7)]
[Delay(time=1)]
[Character(name="avg_npc_020",screenadapt="coverall")]
[name="保镖"]   克洛宁先生，锡兰小姐有事情要找你。
[Character]
[name="？？？"]   ......
[Character(name="avg_npc_023_2#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="克洛宁"]   什么重要的事需要您亲自来市政厅，亲爱的大小姐？
[name="克洛宁"]   现在节日的安排紧锣密鼓地推进，大家可没什么空闲时间。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   克洛宁，我就直接开门见山地说了。汐斯塔火山可能马上就要爆发了，说不定是下一秒，说不定是几天后。
[name="锡兰"]   所有的旅客和市民的安全都会受到威胁，我们需要给他们提供指引，开始准备转移或者避难。
[name="锡兰"]   黑曜石节的各项后续活动需要马上中止。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#2",focus=1)]
[name="克洛宁"]   嚯，我的大小姐，您知道您现在在说什么吗。
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1.5)]
[name="克洛宁"]   如果是别人这么对我说话，早就被我轰出去了。
[name="克洛宁"]   但是因为是您，我愿意给您解释一下。
[name="克洛宁"]   火山的问题，您完全不必担心，虽然不知道您是从哪里听来的消息，但这显然是无稽之谈。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=2)]
[name="锡兰"]   ......你在开什么玩笑？
[name="锡兰"]   已经有很多征兆证明这座火山已经开始重新活动，很可能短期内就会爆发。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=1)]
[name="克洛宁"]   比如说？
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=2)]
[name="锡兰"]   源石虫的狂躁化、异常气温、不太对的气味等等，这些都是证据。
[name="锡兰"]   说这么多你如果还是不信，那就看下我带来的资料，里面记载有详细分析过程和结论。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=1)]
[name="克洛宁"]   明显？是源石虫开口告诉了您这一点，还是气温或者什么气味这么说了？
[name="克洛宁"]   我怎么一点也不明白，这些毫无根据的数字和火山要爆发有什么关系呢？
[name="克洛宁"]   我只知道，由市长本人亲自安排，由我提供技术设计出的火山观测系统一点问题都没有。
[name="克洛宁"]   现在的汐斯塔火山参数都跟过去几年没有什么区别。非要说的话，更稳定了？
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=2)]
[name="锡兰"]   你在说什么，事实不就正摆在你面前的吗......
[Decision(options="你是天灾信使，却不懂这些？",values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_023_2#3")]
[name="克洛宁"]   你又是什么人？
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   {@nickname}博士是专门机构的研究人员，他和他的其他同事们都有专门的火山知识。
[name="锡兰"]   这些参数也都是他们的专业部门给了我帮助并且进行验证的结果。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#2",focus=1)]
[name="克洛宁"]   原来如此，原来如此。
[name="克洛宁"]   ......呵呵，我懂了。
[name="克洛宁"]   所以就是你们这些奇怪的外来游客蒙骗了大小姐的吗。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   你在说什么？
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#2",focus=1)]
[name="克洛宁"]   这不是显而易见的事吗，大小姐，您被这个来路不明的人欺骗了。
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=2)]
[name="锡兰"]   克洛宁，你到底在说些什么。你连我的话都不相信吗？！
[Character(name="avg_npc_023_2#3",name2="char_348_ceylon_4#3",focus=1)]
[name="克洛宁"]   我在说，您一直在外留学所以并不知道，事实上眼红我们汐斯塔市发展的人是很多的。
[name="克洛宁"]   每年都会有人想要阻碍市长大人发展城市的步伐，威胁、爆破、暗杀，就连我这样的默默无闻的人都被波及过好几次了。
[name="克洛宁"]   当然，散布火山要爆发的谣言也不是第一次，但是呢，能把您都给骗了倒还是第一次。
[name="克洛宁"]   不得不说，这次的对手对市长大人了解很深啊，连大小姐您刚留学回来没多久都能摸清楚。
[name="克洛宁"]   而且胆子也很大，竟然光明正大地就这么走进来了。
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]   ......我确实不知道这些，但我说的是

... (全文7300字符)
```

### level_act3d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第四关（后）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_sunnytown_2",screenadapt="coverall", fadetime=1,block=true)]
[Character(name="char_348_ceylon_4#7")]
[name="锡兰"]   快！博士！我们往沙滩那边走！
[name="锡兰"]   沙滩上有大量游客聚集，混进人群里面他们就追不上我们了！
[Character(name="avg_npc_020")]
[name="保镖"]   站住！
[Character(name="char_348_ceylon_4#7")]
[name="锡兰"]   就凭你们！
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Blocker(a=0, fadetime=1, block=false)]
[Character(name="char_340_shwaz_2#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="黑"]   ......
[Decision(options="欸，你是——",values="1")]
[Predicate(references="1")]
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#4",focus=2)]
[name="锡兰"]   黑！太好了你终于来了！
[name="锡兰"]   还好有你在，克洛宁这是怎么了！？
[name="锡兰"]   博士，她就是我之前跟你说......
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#4",focus=1)]
[name="黑"]   小姐，老爷不在城里，你得听克洛宁的。
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#8",focus=2)]
[name="锡兰"]   黑？你在说什么？
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#8",focus=1)]
[name="黑"]   快跟我回去找克洛宁，把这些人都交给他。
[name="黑"]   我不想对小姐动手。
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#8",focus=2)]
[name="锡兰"]   ......黑？
[Delay(time=0.3)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_act3d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第五关（前）
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_sunnytown_2",screenadapt="coverall", fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#8",focus=1)]
[name="黑"]   ......
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#8",focus=2)]
[name="锡兰"]   黑？！
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#8",focus=1)]
[name="黑"]   克洛宁的命令现在就是市长的命令，所有人，动手。
[name="黑"]   把这些人都绑起来。注意不要伤到小姐了。
[Character(name="char_340_shwaz_2#2",name2="char_348_ceylon_4#3",focus=2)]
[name="锡兰"]   你说什么？！
[name="锡兰"]   你也以为我是在闹着玩吗？！
[Decision(options="走！;现在不是说话的时候！",values="1;2")]
[Predicate(references="1;2")]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_sunnytown_2")]
[Blocker(a=0, fadetime=2, block=false)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Character]
[Blocker(a=0, fadetime=0.6, block=false)]
[name="保镖A"]   他们沿着这条路往沙滩跑了！
[name="保镖B"]   啧，人太多了，不好追。联络沙滩的岗哨，围住他们！
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   别想走！
[name="黑"]   ！？
[Character]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Decision(options="欸？",values="1")]
[Predicate(references="1")]
[Character(name="char_188_helage_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]   博士，走，这里先交给我。
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   欸？！你，你是......！
[Decision(options="锡兰，我们先走！",values="1")]
[Predicate(references="1")]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Background]
[playsound(key="$beach",volume=0.8, channel="B", loop=true)]
[playsound(key="$runsand", volume=0.7)]
[playsound(key="$runsand", volume=0.7)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_348_ceylon_4#5")]
[name="锡兰"]   等一下，哈，哈......博士，我好累......
[Decision(options="终于......到了沙滩......;我也......跑不动了......",values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_020")]
[name="保镖"]   大小姐，请跟我们回去吧。
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]   我不要！
[Character(name="avg_npc_020")]
[name="保镖A"]   别伤着大小姐，那个什么博士随便你们处置。
[Character]
[stopmusic(fadetime=1)]
[name="？？？"]   谁敢随便处置博士！！
[Character(name="avg_npc_020")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="保镖B"]   好烫好烫！
[name="保镖C"]   哪儿来的臭小鬼！
[name="保镖C"]   噫！我的屁股！我的屁股！
[Character]
[Dialog]
[Character(name="char_134_ifrit_summer_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="伊芙利特"]   喂，博士，你又惹上什么好玩的事情了，怎么不叫上我？
[Character(name="avg_npc_020")]
[name="保镖A"]   啧，只是一个臭小鬼，给她点颜色瞧瞧！
[Character(name="char_134_ifrit_summer_1")]
[name="伊芙利特"]   我正愁无聊呢，嘿嘿......
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   博士，你的脸色怎么变得比刚才还差？
[Decision(options="伊芙利特，下手别太重！！;把他们衣服烧光差不多了。",values="1;2")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.8, crossfade=1.5)]
[Predicate(references="1;2")]
[Character(name="char_134_ifrit_summer_1")]
[name="伊芙利特"]   啧——
[name="伊芙利特"]   那就三成！
[Delay(time=0.3)]
[Dialog]
[Blocker(block=true)]
[Image]
[Delay(time=0.3)]
[stopsound(channel="B", fadetime=1)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_act3d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第五关（后）
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180,fadetime=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.8, crossfade=1.5)]
[playsound(key="$beach",volume=0.8, channel="B", loop=true)]
[Delay(time=1)]
[Character]
[name="保镖A"]   烫烫烫！焦了焦了！
[name="保镖B"]   噫！我的头发！
[name="保镖A"]   啧，撤退，撤退！
[Dialog]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.8, block=true)]
[Character]
[Blocker(a=0, fadetime=0.8, block=true)]
[Character(name="char_134_ifrit_summer_1")]
[name="伊芙利特"]   哈哈哈，果然还是打架有意思啊，博士！
[name="伊芙利特"]   啊，对了，博士，我这是为了救你，而且也听你的话没有下重手了，你可不许告诉赫默我打架的事！
[name="伊芙利特"]   要是被她知道了我的作业肯定又要变多了！
[Decision(options="没问题。;作业你要自己努力。",values="1;2")]
[Predicate(references="1")]
[name="伊芙利特"]   嘿嘿，我就知道博士是个好人！
[Predicate(references="2")]
[name="伊芙利特"]   哼，那我可不管！
[Predicate(references="1;2")]
[Character(name="char_134_ifrit_summer_1",name2="char_348_ceylon_4#8",focus=2)]
[name="锡兰"]   源石驱动的火焰喷射器......而且这个功率，好厉害的术师。
[Character(name="char_134_ifrit_summer_1",name2="char_348_ceylon_4#8",focus=1)]
[name="伊芙利特"]   大姐，你的眼光不错欸，我超厉害的！
[Character(name="char_134_ifrit_summer_1",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   我叫锡兰。
[name="锡兰"]   谢谢你救了我们。
[Character(name="char_134_ifrit_summer_1",name2="char_348_ceylon_4#2",focus=1)]
[name="伊芙利特"]   哦、哦......没关系。这，这是我该做的。
[name="伊芙利特"]   喂，博士，这个姐姐好懂礼貌啊，这种时候我该怎么做来着？
[Decision(options="微笑。;鞠躬。;跳舞。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_134_ifrit_summer_1")]
[name="伊芙利特"]   噢，好吧，那我试......
[name="伊芙利特"]   啊？我忘记我的烤肉还在架子上了！我不跟你们多说了！
[name="伊芙利特"]   博士，锡兰，你们之后要是想吃烧烤记得来找我啊！
[playsound(key="$runsand", volume=0.7)]
[Dialog]
[Character(fadetime=1,block=true)]
[Delay(time=1)]
[Decision(options="竟然直接就跑开了。",values="1")]
[Predicate(references="1")]
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   博士，我们也赶紧回去吧。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_hotel")]
[stopmusic(fadetime=1)]
[Blocker(a=0, fadetime=2, block=false)]
[Character(name="char_188_helage_1")]
[name="？？？"]   博士，你们平安无事，很好。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#5",focus=2)]
[name="锡兰"]   十分感谢您的相助，请问......
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#5",focus=1)]
[name="赫拉格"]   你可以叫我赫拉格。
[name="赫拉格"]   和博士一样，我也来自罗德岛。
[Character(name="char_188_helage_1")]
[name="赫拉格"]   博士，你现在有时间吗，有些话我要单独告诉你。
[stopsound(channel="B", fadetime=1)]
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_act3d0_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_sunnytown_2")]
[Blocker(a=0, fadetime=2, block=false)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Delay(time=1)]
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   A队，B队，远处盯紧了。C队，从后面包围。
[Character(name="char_188_helage_1")]
[name="赫拉格"]   佣兵团的风格吗......
[name="赫拉格"]   有几分实力，训练的人有些水准，不过，还不够。
[Dialog]
[Character(name="avg_npc_020")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_020")]
[name="保镖"]   这，这个老头好强！
[Character(name="char_340_shwaz_2#4")]
[name="黑"]   不在一个等级上。你们在旁边守好。
[Character(name="char_188_helage_1")]
[name="赫拉格"]   ......
[Dialog]
[Character(name="char_340_shwaz_2#2")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[Character(name="char_188_helage_1")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character]
[name="赫拉格"]   （这个女人......不简单。）
[name="赫拉格"]   （这些保镖虽然伤不到我，但她能够对我造成威胁。）
[Character(name="char_188_helage_1",name2="char_340_shwaz_2#4",focus=2)]
[name="黑"]   愚蠢的外地人......
[Character]
[name="赫拉格"]   （她很愤怒。）
[name="赫拉格"]   （站在她的立场上，或许真的是认为我们蒙骗了锡兰小姐。）
[name="赫拉格"]   （但是，有哪里不对。这个人到底是......）
[Character(name="char_188_helage_1",name2="char_340_shwaz_2#2",focus=1)]
[name="赫拉格"]   不愧是经验丰富的佣兵，即使你家小姐被带走也没有乱了阵脚。
[Character(name="avg_npc_020")]
[name="保镖"]   说什么废话！既然你知道我们头曾经是......咕......
[Character(name="char_340_shwaz_2#2",name2="avg_npc_020",focus=1)]
[name="黑"]   闭嘴。
[Character]
[name="赫拉格"]   （......嗯？等等......弩，菲林，这个名字。）
[name="赫拉格"]   （我在哪里听说过这个名字......）
[Character(name="avg_npc_020")]
[name="保镖"]   等等，这老头要干什么？！
[Character]
[name="赫拉格"]   （虽然有些担忧博士那边的情况。）
[name="赫拉格"]   （......不过以博士的能力，加之汐斯塔市内还有其他人在，应当问题不大。）
[Character(name="avg_npc_020")]
[name="保镖"]   他往我们这边冲了，他疯了吧！
[name="保镖"]   快，快拦住他！！！
[Character(name="char_188_helage_1")]
[name="赫拉格"]   太慢了！
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_act3d0_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background(image="bg_hotel", fadetime=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_188_helage_1")]
[name="赫拉格"]   这个菲林族女性并非泛泛之辈。
[Decision(options="这还是难不倒你的。;将军，没受伤吧？",values="1;2")]
[Predicate(references="1;2")]
[name="赫拉格"]   不必担心。她的部下都只是些庸人。你们安全之后，撤退对我来说还算轻松。
[name="赫拉格"]   只不过，关于这个保镖的身份，我有些猜测。
[Decision(options="身份;难道说......",values="1;2")]
[Predicate(references="1;2")]
[name="赫拉格"]   哥伦比亚，菲林族，女性，银发、金瞳、黑弩。是杀手，也是佣兵。
[name="赫拉格"]   杀手闻名于诸城是件可耻的事，但这些传闻实在是过于有名。
[name="赫拉格"]   譬如说，毁掉一整个哥伦比亚家族。一个强盛的家族，重要人物在数年内陆续暴毙，逐渐走向衰落，最终彻底被除名。
[name="赫拉格"]   再如，猎杀一整支巡逻队。这支巡逻队在哥伦比亚边境烧杀抢掠，自诩野蛮人的征服者，不断地向异族施加暴行和惨剧。
[name="赫拉格"]   之后的一个月内，他们在山间逃窜，不断死去，最后只剩下一个残废回到城市胡言乱语。
[name="赫拉格"]   以及向我叙说故事的人的遭遇。
[Decision(options="又发生了什么？;请说吧，我不害怕。",values="1;2")]
[Predicate(references="1;2")]
[name="赫拉格"]   不必多说了。他的伤疤从左肩延伸到右脚后跟。
[name="赫拉格"]   杀人如麻的家伙比比皆是，我也如此。
[name="赫拉格"]   当然，这个杀手失踪已久。
[name="赫拉格"]   只是，如果她就是那个人，那么摆在我们面前的，自然是腥风血雨。
[Decision(options="水比想象中的深。;锡兰被蒙在鼓里？",values="1;2")]
[Predicate(references="1;2")]
[name="赫拉格"]   也许市长并非不知情。
[name="赫拉格"]   不如说，如果她是市长的杀手，我不会感到奇怪。
[Character]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=false)]
（玻璃杯粉碎）
[Decision(options="锡兰？！;你从什么时候......",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_188_helage_1")]
[name="赫拉格"]   锡兰小姐，你不用躲着偷听。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#8",focus=2)]
[name="锡兰"]   我，我想给你们倒杯水......
[name="锡兰"]   赫拉格爷爷，那个佣兵，是从什么时候开始活动，又是在什么时候失踪的？
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#8",focus=1)]
[name="赫拉格"]   她的事迹开始闻名，甚至在我还未退伍之时。
[name="赫拉格"]   而她销声匿迹则是一年之前，随着那个家族的覆灭一起。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#8",focus=2)]
[name="锡兰"]   ......直到六年前，黑都在维多利亚照顾我的生活。
[name="锡兰"]   但是有一天，她忽然说爸爸需要她回去做事，就走了，只在每年圣诞节的时候来接我回家。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#3",focus=2)]
[name="锡兰"]   但、但是，她刚才只是态度不好，而且听了别人的命令，黑她怎么可能是那种杀人如麻的杀手！
[name="锡兰"]   而且，按照你们的说法，你们想说克洛宁的背后是我爸爸在授意吗？！
[name="锡兰"]   我不信！
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#3",focus=1)]
[name="赫拉格"]   我不作推测。但我也说过，即使是最信任的人，也未必对你毫无保留。
[name="赫拉格"]   信与不信，我不关心。只是，她身上的乌萨斯制式武器留下的伤痕，我绝不会看错。这支队伍被埋葬在大雪中。
[Character(name="char_188_helage_1")]
[name="赫拉格"]   现状如你所见，博士。
[name="赫拉格"]   如果火山的情报处理也有市政府参与，那么这件事我们未必应该插手。
[name="赫拉格"]   锡兰小姐，你也应该看清事实。
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   我......我需要冷静一下。
[Dialog]
[Character(fadetime=1,block=true)]
[PlaySound(key="$doorclosequite", volume=0.9)]
[Delay(time=1)]
[Character(name="char_188_helage_1")]
[name="赫拉格"]  博士，请。
[Decision(options="啊？;我是该做些什么吧？",values="1;2")]
[Predicate(references="1;2")]
[name="赫拉格"]   自然。现在她需要一个能够理解她的人。
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_sunnytown_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlayMusic(intro="$indust_intro", key="$indust_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Character]
[name="广播"]   所有人都有没有热火朝天地嗨起来？！
[name="广播"]   为了迎接黑曜石节最盛大的晚会。
[name="广播"]   从今天的12点起，各大商场、游乐设施，以及部分餐厅、酒吧都将举行限时的预热活动。
[name="广播"]   千万不要错过这些最盛大的宴会！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Character]
[Background(image="bg_Festival_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   你果然会来这里，小姐。
[Dialog]
[Character]
[Character(name="char_348_ceylon_4#5",fadetime=1,block=true)]
[Delay(time=1)]
[name="锡兰"]   黑......
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   你一定会来这里。在被克洛宁拒绝以后，你想用广播塔散布信息，让全城人听到你的报告。
[name="黑"]   这行不通，小姐，这只会带来更大的混乱。
[name="黑"]   也许你讨厌你的父亲，也讨厌这个城市，但老爷已经付出得够多了。黑曜石节和这个城市会因此分崩离析。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   我知道我的报告会引起轩然大波，也会引发许多后果，但大家都有权知道真相。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   我知道老爷的过错。老爷为了这座城市做了很多不好的事情，只是没有这些事，根本不会有汐斯塔。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   这次完全不一样！
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   如果小姐觉得不能解气的话，批评我就可以了，请不要做出些没法挽救的事情。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   你......你是不是觉得我还在耍小孩子脾气？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   不，小姐。我可以和你一起慢慢说服老爷，我保证。只是现在，请跟我回去。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   黑......别这么说话。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   我理解你和老爷之间有许多不快，但你应该先回家。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   别这么说话！我知道你想让我和爸爸之间的关系缓和一些，但你能不能不要是现在这个样子！
[name="锡兰"]   为什么就不能像以前一样呢，就像以前一样，像朋友一样和我说话啊，黑！
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   我只是道尔科斯家的仆人。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   我不想你这么说，黑。我不要听你这么说！怎么会变成这样的，你为什么会变成这个样子？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   ......
[Character(name="avg_npc_020")]
[name="克洛宁的手下"]   你还犹豫些什么？快把她抓起来啊？
[Character(name="char_340_shwaz_2#4")]
[name="黑"]   ——她是道尔科斯家的女儿。别太僭越。
[Character(name="avg_npc_020")]
[name="克洛宁的手下"]   但市长已经要你全力协助克洛宁先生了！你要看着她散布谣言，毁掉整个汐斯塔吗？
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   ......用用你的脑子。她一个人在这里，没有表现出哪怕一丁点的焦躁，甚至......
[name="黑"]   你觉得她真的想进入广播塔吗？
[Character(name="avg_npc_020")]
[name="克洛宁的手下"]   什么？
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   算了。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   小姐，你在把自己当成诱饵吸引我，对吗？
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   ......你还是了解我的。
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   我不敢这么说，小姐。只不过你没有否认我的猜测，我可以下结论了。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   现在这个时候，罗德岛应该已经出现在市政厅了。
[Character(name="avg_npc_020")]
[name="克洛宁的手下"]   什、什么？这可不在我们的计划里啊！市政厅那边现在是什么情况？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#5",focus=2)]
[name="黑"]   我觉得，那群酒囊饭袋，现在大概正被打得四处乱窜。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_offce")]
[stopmusic(fadetime=3)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   外面怎么没声音了？不是让他们赶紧把材料搬走，这么急的事情怎么还能偷懒？
[name="克洛宁的保镖"]   嗯？刚才那阵叫骂，难道又有人打架了？不管了，赶紧把手上的处理——
[Character]
[CameraShake(duration=0.3, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="女孩的声音"]   先生，请开门！我们是来送快递的！
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   （嗯？你们没人要收什么东西吧？）
[name="克洛宁的保镖"]   （都没有？奇怪......）
[name="克洛宁的保镖"]    你送错地方了！
[Character]
[name="女孩的声音"]   可是先生，这个快递就是写着送到这里的啊？
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   走开！再缠着我们，小心棍棒不长眼睛！
[Character]
[name="女孩的声音"]   ......
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   嘁，臭小鬼，肯定又是来骗钱的。
[Character]
[name="女孩的声音"]   哎不管了！博士，站旁边些，我来把这东西踹开！
[name="女孩的声音"]   什么？没关系的！这点力气我还是有的！
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   啊？
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$char_emp", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_290_vigna",fadetime=1,block=true)]
[Delay(time=1)]
[name="红豆"]   哈！
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   唔啊啊？！大门怎么倒了，我的天，你是什么——
[Decision(options="漂亮的一脚！;......;朋友，可不能粗鲁对待快递员啊。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_290_vigna")]
[name="红豆"]   嘿嘿，我早就想这么试试了。接下来我要试试这句话......
[name="红豆"]   嗯，咳咳，哼！
[name="红豆"]   “开门！快递！”
[Decision(options="这不是已经被你踢开了吗！",values="1")]
[Predicate(references="1")]
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Character]
[Background(image="bg_Festival_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   黑，我在维多利亚留学这么多年，并不是在虚度光阴。
[name="锡兰"]   我在那里学习了与天灾和源石有关的，最先进的科学技术。
[name="锡兰"]   对你来说或许是天方夜谭的事，对我来说却是理所当然并且正在发生的事。
[name="锡兰"]   我所学习的知识，我所信奉的理论，它们都在告诉我我的判断是正确的。
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   小姐你学的并不是法学。
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   嗯......？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   罗德岛在市政厅做什么？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   搜集克洛宁的罪证。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   嗯？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   克洛宁也许很坏，却没有那么蠢。
[name="锡兰"]   作为天灾信使他不可能不知道现在火山的状况有问题。
[name="锡兰"]   他一定是因为自己的盘算才掩盖事实的，只要暗暗搜集他的罪证......
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   我认为罗德岛和他会正面冲突，所谓暗中搜集证据，不可能成功。
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   ......
[name="锡兰"]   没，没关系！只要你不在就......
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#1",focus=2)]
[name="黑"]   小姐，我想知道你为什么要这么做。如果我能得到一个合理的答案，我不会追究罗德岛。
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]   ......我必须这么做。我不相信父亲是无血无肉的人，他绝对不会看着这种事情发生。
[name="锡兰"]   父亲爱着这个城市，比谁都爱，没有人比我更清楚这一点了。
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   你还恨他吗？
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   为什么？如果该恨的话，应该是父亲恨我，因为我的出生带走了母亲......
[name="锡兰"]   但他从来没有这么做。
[name="锡兰"]   我只是讨厌他不肯把事情说出来，把所有事情全都安排好。
[name="锡兰"]   看起来好像是在保护我，实际上却害得我什么都不知道，什么都做不了。
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   就连这次也一样！一定是克洛宁蒙骗了父亲，让他对火山爆发的事情完全不知情。
[name="锡兰"]   所以父亲才会让克洛宁阻止我发布报告！这不叫恨吧？
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#1",focus=2)]
[name="黑"]   火山爆发？
[name="黑"]   克洛宁说的是，小姐准备把老爷过去的机密事件全部抖露，让老爷退职，接受审判。
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]   啊？不，我父亲过去做了些什么？
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#5",focus=2)]
[name="黑"]   不，没什么。
[name="黑"]   ......唔，原来是这样，我知道了。
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#5",focus=1)]
[name="锡兰"]   所以克洛宁也不是因为父亲的命令才阻拦我的。呼，我也差不多明白了。
[name="锡兰"]   黑，如果真是那种事，我会请求更具备法律效力的渠道。
[name="锡兰"]   我所做的自然也是为了这个城市，为了我的故乡。
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#1",focus=2)]
[name="黑"]   我明白了。小姐并不在乎过去的事情，也不在乎所谓的名誉。
[name="黑"]   我和小姐一样，老爷也一样。
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]   呼。不管别人怎么猜想，我选择相信你，相信父亲。
[name="锡兰"]   即使是目的产生了冲突，我也知道，这是我们两个人之间的事。
[name="锡兰"]   所以我相信，和我一样了解这个城市的你，一定会知道我会在这里。
[name="锡兰"]   这样，你就会亲自来阻止我。
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]   说起来，市长是谁都无所谓吧？父亲也一定会这么觉得。他在乎的，不也是这个城市吗？
[name="锡兰"]   所以，父亲一定会同意我的观点的。
[name="锡兰"]   黑......我说的对吗？
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#5",focus=2)]
[name="黑"]   你长大了，小姐。
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background]
[PlayMusic(intro="$fesready_intro", key="$fesready_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Character]
[Background(image="bg_Festival_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="avg_NPC_017_3",fadetime=1,block=true)]
[Delay(time=1)]
[name="D.D.D."]   大家！！准备好了吧！！！
[name="D.D.D."]   黑曜石节最盛大的联合LIVE将在3小时后开始！
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   哦哦哦哦哦哦！！！
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_offce")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_023_2")]
[name="克洛宁"]    时间差不多了。只要黑能和罗德岛相互牵制，这里也就一切顺利了。
[name="克洛宁"]    让罗德岛和黑对立果然是步好棋，哼。
[name="克洛宁"]    快点！把这些东西给我搬走！动作不够快的话，你们的薪水也要打水漂！
[name="克洛宁"]    嗯？外面什么声音？
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_hotel",screenadapt="coverall" )]
[Character]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=false)]
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   博士，如果单纯的只是冲进广播塔，肯定会遭到克洛宁的埋伏。
[name="锡兰"]   如果你们和我一起行动，黑一定会先想办法解除各位的武装，那样我就更没有办法牵制她了。
[name="锡兰"]   就算粗暴地夺得了广播塔的控制权，如果没有政府的支持，我的话只会让市民陷入迷惑和恐慌。
[name="锡兰"]   如果黑保护着克洛宁，这对于各位的行动来说，也是很大的阻碍。
[name="锡兰"]   重要的是，克洛宁到底隐藏着什么，这可能需要各位去发掘。
[name="锡兰"]   也许克洛宁真的是个像纸面一样清白的人——
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=1)]
[name="赫拉格"]     那我们就会挟持他，逼他发出官方公告？
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   对。如果真的是这样的话，我也不会介意去这么做，毕竟我确实是这么想的。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=1)]
[name="赫拉格"]     锡兰小姐，你很有胆识，但是甚至可以说有些冒险。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   实验的数据和调查报告，罗德岛的各位已经帮我证实了，如果不这么做，汐斯塔的所有人都会遭殃。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=1)]
[name="赫拉格"]     我并不是要指责你什么，小姐。只是罗德岛的参与与否，并非由我决定。
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=2)]
[name="锡兰"]   你是指......
[Character(name="char_188_helage_1",name2="char_348_ceylon_4#2",focus=1)]
[name="赫拉格"]     博士。前因后果你都已经很清楚了。我们该怎么做？
[Decision(options="都到这一步了，必须做些什么！;......;让无辜的人受难，这违背了罗德岛的信条。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_188_helage_1")]
[name="赫拉格"]     所以，责任由谁承担？
[Decision(options="只要没人发现，就没有人参与过！",values="1")]
[Predicate(references="1")]
[Character(name="char_188_helage_1#2")]
[name="赫拉格"]     你啊。
[name="赫拉格"]     锡兰小姐，事不宜迟，我们启程吧。
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   博士......
[Decision(options="做你该做的事吧。",values="1")]
[Predicate(references="1")]
[name="锡兰"]   我知道了，就由我去牵制黑吧。
[name="锡兰"]   而且，我也有不得不去做的事情，我必须知道答案......
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="bg_Festival_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   黑......
[name="锡兰"]   为什么要疏远我？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   ......
[name="黑"]   小姐是在维多利亚经受过良好教育的人。你应该去更好的地方，别和我们这样的人一起留在这个城市挣扎。
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   ......不对。这一点也不对。
[name="锡兰"]   黑，你在我心里是什么样的人？我在你心里又是什么样？
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   我不是小姐看到的那样。
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   因为你杀过人？
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   ......
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   因为你杀过很多人？
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   不，小姐。别再说了。
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   可能我们都弄错了，黑。
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   小姐，我不想你知道这些！
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   对不起。
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   ......小姐？
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   我已经知道了。我知道了你的过去......哪怕只是一点。
[name="锡兰"]   如果黑不愿意我知道，对不起，我是没法说“我不知道”的。
[Character(name="char_348_ceylon_4#9",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   不，小姐！你根本不应该知道！你本应该......
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   我应该什么？应该这样，应该那样，应该好好读书，应该跻身名流，什么呀！
[name="锡兰"]   我可不是什么温室里的花，也不是什么不谙世事的大小姐了！我知道我有必须要做的事情！
[name="锡兰"]   保护汐斯塔，既是父亲的事情，是你的事情，也是我的事情！
[name="锡兰"]   你不想我卷入这种事情，是为了保护我吧？
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   我不......我......
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   你和爸爸都一样，你们觉得你们这样安排我会过得很好，但我不觉得！
[name="锡兰"]   我不觉得危险有什么，我不觉得黑的过去有什么！也许真正在经历这些的时候，我也会哭，也会悲伤，也会觉得可怕......
[name="锡兰"]   只是，只要黑说，“需要锡兰来帮助我”的话，我一定会来的！无论你说什么，我都会听的！
[name="锡兰"]   如果是朋友的话，就应该是这样啊，一直都仅仅是单方面地付出的话，算什么朋友啊！
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   所以，黑，现在可以来帮我吗？
[name="锡兰"]   你已经问过我，为什么要这样做？我已经回答过了......
[name="锡兰"]   所以，你可不可以也给我一个答案，黑？如果过去的都过去了，你可以再当一次我的朋友吗，就像小时候那样？
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#5",focus=2)]
[name="黑"]   小姐......对不起。我为过去我的言行向你道歉。我的所作所为让你误解了，这些都不该发生的。
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#5",focus=1)]
[name="锡兰"]   啊......
[Character(name="char_348_ceylon_4#5",name2="char_340_shwaz_2#1",focus=2)]
[n

... (全文7624字符)
```

### level_act3d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Character]
[Background(image="bg_Festival_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]     全、全都打倒了？我从来......都不知道你有这么厉害。
[name="锡兰"]     我也想象过，但......
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]     所以我不想让小姐知道。
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]     但你实在是太厉害了！好帅呀，黑！
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]     唔。
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]     你是怎么跳那么高的！顺着墙窜上去，然后直接翻身跃下！
[name="锡兰"]     就在空中这么旋转，所有射击都被你躲过去了！
[name="锡兰"]     然后扭过身体，啪啪啪，连着把他们全都射倒！天哪！
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]     小姐......你这么说，我的脸会很烫。
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]     不过，黑，我要纠正一点。刚才我可没有在命令你，我只是作为朋友在请求你而已。
[name="锡兰"]     你如果有什么想做的事情，也可以和我说呀。
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#1",focus=2)]
[name="黑"]     明白。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]     嗯？我们刚才怎么说来着？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#1",focus=2)]
[name="黑"]     ......啊？
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]     别这么说话！朋友，是朋友！
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]     我......好。
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]     呵呵。我们快去市政厅吧，不知道博士他们那里现在是什么情况......
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_offce")]
[Blocker(a=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   这些饭桶，连一个小姑娘都拦不住吗？！
[Character(name="avg_npc_023_2#2",name2="avg_npc_020",focus=2)]
[name="克洛宁的保镖"]   可她是萨卡兹！而且对方还有其他好几个人！
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]     那不也就只有几个人！
[name="克洛宁"]   可、可恶的罗德岛，怎么会在这里！
[Character(name="char_290_vigna")]
[name="红豆"]     什么嘛，感觉这些家伙，怎么比源石虫还弱的样子......
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   赶快把所有的人手都调过来！
[Character(name="avg_npc_020")]
[name="克洛宁的保镖"]   可是克洛宁先生......
[name="克洛宁的保镖"]   我觉得，打不过，就是打不过！
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   没什么可是！别往后退啊！
[Character(name="char_290_vigna")]
[name="红豆"]     呵欠......唉，博士，你找到没有啊？我还要去听LIVE呢，要是赶不上我可就亏大了。
[Decision(options="我得到了！;......;嗯，已经找到账簿和债券了。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_290_vigna")]
[name="红豆"]     哦？找到了啊？果然打他们一顿是有用的嘛。陨星姐也说了，暴力有时候是必要的！
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]    该，该死！
[name="克洛宁"]    不管了，只要现在能逃走，手续什么的好补得很！
[Character(name="char_290_vigna")]
[name="红豆"]     啊，博士，他从窗户逃走了！
[Decision(options="这些资料，我们把它都带上！",values="1")]
[Predicate(references="1")]
[Character(name="char_290_vigna")]
[name="红豆"]     好~
[name="红豆"]     咦，将军他还在外面吧？感觉这个克洛宁什么的的下场会很惨啊，还不如没逃走呢......
[name="红豆"]     来，博士，我帮你拿！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_Festival_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   哈，哈哈......该死。
[name="克洛宁"]   必须，必须马上把其他人叫回来！
[Dialog]
[Character(name="char_188_helage_1")]
[name="赫拉格"]     上一次，罗德岛的博士和贵市的锡兰小姐从那个窗户跳了出来。
[name="赫拉格"]     时来运转，现在是汐斯塔的天灾信使克洛宁先生跳出了窗户。
[name="赫拉格"]     人生也许很无常，先生。
[Character(name="char_188_helage_1",name2="avg_npc_023_2#2",focus=2)]
[name="克洛宁"]     你......你！我的手下呢？我的手下呢？！
[Character(name="char_188_helage_1",name2="avg_npc_023_2#2",focus=1)]
[name="赫拉格"]     放在这里会影响游客参观。
[name="赫拉格"]     顺便，这两位小姐已经在这里等你很久了。
[Dialog]
[Character]
[Character(name="char_340_shwaz_2#1",name2="char_348_ceylon_4#2",fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   黑......
[name="克洛宁"]   你们两个站在一起，也就是说......
[Decision(options="也就是说你要完蛋了！;......;证据现在都在我们手中，你难逃法网了，先生。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_188_helage_1")]
[name="赫拉格"]   博士，请小心，他也许还会做些垂死挣扎。
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]     你们......你们......
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]     你的计划败露了，克洛宁！
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Background]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Character]
[Background(image="bg_Festival_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="avg_npc_020")]
[name="工作人员"]   发生什么事了？喂？
[Character(name="avg_npc_020",name2="npc_2004_Alty",focus=2)]
[name="Alty"]    欸，出了什么事吗？外面是不是有些状况啊？
[Character(name="avg_npc_020",name2="npc_2004_Alty",focus=1)]
[name="工作人员"]   请不用担心，目前还没有异常。请您往这边走。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="avg_npc_020")]
[name="工作人员"]   嘉宾已就位，还有2分30秒准备登台。
[name="工作人员"]   快！把外面的事情处理好。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   事到如今，赫尔曼你也没有什么威望了！
[name="克洛宁"]   这些人都是这几年我发展的手下，他们才知道什么是努力换来的回报和美好的生活！
[name="克洛宁"]   今天就是音乐节的最高峰，我会带上我这么多年应得的所有利益离开这里。
[name="克洛宁"]   你还被蒙在鼓里吧。
[name="克洛宁"]   我现在就大发慈悲地告诉你，你们看到的火山监测站的数据是错的，很快它就会彻底活性化。
[name="克洛宁"]   源石会伴随着爆发蔓延，至少半个城市都逃不过被毁灭的结局！
[name="克洛宁"]   而我什么都不会失去，等到灾难结束我还会回来进行开采。
[name="克洛宁"]   汐斯塔果然是我的一片宝地！我也深爱着它啊，赫尔曼！
[Character(name="avg_npc_024")]
[name="赫尔曼"]  你胆敢说出这样的话！
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   既然我是这个城市的天灾信使，那么我当然可以。
[name="克洛宁"]   而你们所有人都会被我在此击败，然后眼睁睁地看着汐斯塔变成一片废墟！
[name="克洛宁"]   当然，最后死在光荣的汐斯塔火山爆发之中。除了我，没有人能把这些秘密带离这里。
[Decision(options="你的野心到此为止了。;做你的美梦！;你也太小看罗德岛了吧。",values="1;2;3")]
[Predicate(references="1;2;3")]
[name="克洛宁"]   ......罗，德，岛。
[Character(name="avg_npc_024")]
[name="赫尔曼"]   我对你实在太失望了，克洛宁。
[Character(name="avg_npc_024",name2="avg_npc_023_2#2",focus=2)]
[name="克洛宁"]   失望？你说失望？失望的是我！
[name="克洛宁"]   我永远也不会忘记失去了家而不得不睡在垃圾桶中躲避风雨的日子！
[name="克洛宁"]   财富才是新生活的钥匙，我自那时就明白了这个道理！而你呢？却用我们辛苦得到的钱，去救助那些感染者垃圾！？
[name="克洛宁"]   你要把汐斯塔无上的价值葬送在你的伪善之中吗！？
[Character(name="avg_npc_024",name2="avg_npc_023_2#2",focus=1)]
[name="赫尔曼"]   你好好看看你自己，克洛宁。
[name="赫尔曼"]   然后，去监狱中思考自己看到了什么吧！
[Dialog]
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$fireworks", volume=0.8)]
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Character]
[Background(image="bg_Festival_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Character(name="avg_npc_024",name2="avg_npc_023_2#2",focus=1)]
[name="赫尔曼"]   你跟在我身边十五年，什么都没有学会。
[name="赫尔曼"]   只学到了一些上不了台面的手段，真是个蠢材。
[Character(name="avg_npc_024",name2="avg_npc_023_2",focus=2)]
[name="克洛宁"]   蠢材......呵呵，呵哈哈哈哈哈哈！
[name="克洛宁"]   老东西，你该不会以为这就是我的最后一步棋了吧？
[stopmusic(fadetime=2)]
[playsound(key="$smallearthquake", volume=0.6)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Character(name="char_188_helage_1")]
[name="赫拉格"]   怎么回事？
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   这......难道是火山爆发前引起的轻型地震？！
[PlayMusic(intro="$volcano_intro", key="$volcano_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Background]
[Character(fadetime=0)]
[Image(image="ac3_volcano",x=0, y=0, xScale=1, yScale=1, fadetime=0, screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
[name="克洛宁"]   来了，呵呵，终于来了。
[name="克洛宁"]   跟这座城市一起化为尘埃吧！
[Image(image="ac3_volcano2",x=0, y=0, xScale=1, yScale=1, fadetime=2, screenadapt="coverall")]
[name="克洛宁"]   即使现在你们想去控制广播塔也晚了！市民只会陷入恐慌！
[name="克洛宁"]   火山的活动日期近在眼前，你们以为有了那些简单的样本资料就能搞清楚什么？
[name="克洛宁"]   快速的逃生渠道都在我手里！你们谁都逃不走！
[name="克洛宁"]   假装清高的家伙们，你们谁都救不了！
[name="克洛宁"]   一切都会随着城市的毁灭被消灭！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_Festival_2",screenadapt="coverall")]
[Character(fadetime=0)]
[Image]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   博士，怎么办！
[Decision(options="赶紧动员大家疏散人群！;至少先让大家离开危险地区！",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_188_helage_1")]
[name="赫拉格"]   博士，要不要通知罗德岛全体......
[Character]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="艾雅法拉"]   博士，能听到吗！火山的分析研究完成了！
[name="艾雅法拉"]   如果现在的话，还有机会能争取到更多的时间！
[name="普罗旺斯"]   博士，我们已经把火山活动的原因找到了，这次的火山活动很有可能是可以被阻止的！
[name="艾雅法拉"]   现在大家冷静下来听我说，只要按照这个方法来，一定能把火山爆发的时间推迟！
[Character(name="char_188_helage_1")]
[name="赫拉格"]   我们可以帮忙，如果真的是人力所及的话。
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   ......嗯。
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   不，这件事就交给我们吧。
[name="锡兰"]   克洛宁已经蛰伏了这么长的时间，他的残党必然布及整座城市。
[name="锡兰"]   现在正是最关键的时刻。黑，赫拉格爷爷，你们都有自己的事情要做。
[Character(name="char_348_ceylon_4#2",name2="char_340_shwaz_2#2",focus=2)]
[name="黑"]   这些事情交给其他人去做就可以——
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#2",focus=1)]
[name="锡兰"]   但这是我们的任务。
[Character(name="avg_npc_024")]
[name="赫尔曼"]   锡兰......
[Character]
[name="普罗旺斯"]   同意。
[name="普罗旺斯"]   天灾信使，火山学家，源石学者，我们之中谁都不能容忍让有所预兆的危机威胁到市民。
[name="普罗旺斯"]   更何况竟然有人利用自己的知识，蒙蔽他人，中饱私囊。作为天灾信使，我可不能忍受自己在这种人面前还依然袖手旁观！
[Character(name="char_188_helage_1")]
[name="赫拉格"]   你竟然也会有这么认真的一面，我明白了。那么市长先生，疏散群众的任务，请容我助你一臂之力。
[Character(name="char_340_shwaz_2#2",name2="avg_npc_024",focus=2)]
[name="赫尔曼"]   ......嗯。黑，你也来吧。
[Character(name="char_340_shwaz_2#3",name2="avg_npc_024",focus=1)]
[name="黑"]   我——
[Character(name="char_340_shwaz_2#3",name2="avg_npc_024",focus=2)]
[name="赫尔曼"]   锡兰说她可以做到。
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   ......小姐，请务必小心。
[Character]
[name="艾雅法拉"]   讨论好了吗？我们的时间不多了！
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]   嗯！我们赶紧出发吧！
[Dialog]
[Character(fadetime=1)]
[Delay(time=2)]
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   ......
[Character(name="char_340_shwaz_2#2",name2="avg_npc_024",focus=2)]
[name="赫尔曼"]   我们应该相信她，何况他们说的没错，我们有自己的事情要做。
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   哼哈哈哈——他们根本就是去送死！就算能拖延一时半会又如何！？
[name="克洛宁"]   不仅大半座汐斯塔要陪着你的女儿送葬，而你根本就找不到她的尸首——
[CameraShake(duration=0.4, xstrength=12, ystrength=18, vibrato=30, randomness=30, fadeout=false)]
[name="克洛宁"]   呃——
[Character(name="char_188_helage_1")]
[name="赫拉格"]   抱歉，顺手。
[Character(name="char_188_helage_1",name2="avg_npc_024",focus=2)]
[name="赫尔曼"]   无妨，何况他说的没错，不能让市民们继续身处险境了。
[name="赫尔曼"]   希望你们能助我一臂之力。
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Dialog]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.8,crossfade=1)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Background(image="bg_cave_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.7, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_348_ceylon_4#8",fadetime=1,block=true)]
[Delay(time=1)]
[name="锡兰"]   在火山的另一边，竟然有这样一个洞窟。
[Character(name="char_145_prove_1")]
[PlaySound(key="$d_gen_walk_n")]
[name="普罗旺斯"]   这个洞窟原本应该是天然形成的，但是经过了大量人为黑曜石开采，内部已经变成一个很深的矿洞了。
[name="普罗旺斯"]   大家要做好准备，我们要在里面走相当长的一段路。
[name="普罗旺斯"]   我的真正的目的地，就在这个洞窟的深处。
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Blocker(a=0, fadetime=0.7, block=true)]
[Background(image="bg_cave_2",screenadapt="coverall", fadetime=1)]
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_166_skfire_3#1")]
[name="天火"]   在研究室的时候我可是做梦也想不到，有一天我会在度假的时候深入火山深处。
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   现在可以好好解释一下了吗，刚才在通信里说的太笼统了，“这次火山爆发是可以阻止的”究竟是怎么回事？
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]    嗯......解说还是交给天火好了，你来解释吧。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   这是我和普罗旺斯之前在火山内部探索，然后跟艾雅法拉远程交流得出的结论。
[name="天火"]   提到原理，首先得从这里源石虫的生态说起......不，说不定称呼它们为火山源石虫或者熔岩源石虫更为合适吧。
[name="天火"]   虽然外表与源石虫几乎一样，但是它们以火山为巢穴，以这里特别的黑曜石为食，在汐斯塔的火山内部筑巢生根。
[name="天火"]   这些源石虫居住的地方会非常接近火山的核心，也正好是这种混合了特殊成分的黑曜石大量产生的地方。
[name="天火"]   而这里的人发现了这个特性，利用它们的踪迹来发掘黑曜石。
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   原来如此，我看过一些资料，有些地方的人，是通过生物的一些特性来寻找和发掘资源的。
[Character(name="char_145_prove_1",name2="char_166_skfire_3",focus=1)]
[name="普罗旺斯"]   人们总是能从和生物的联系中找到规律。
[Character(name="char_145_prove_1",name2="char_166_skfire_3",focus=2)]
[name="天火"]   问题就在于，这座火山距离上次喷发已经是很久以前了，这里的黑曜石是有限的。
[name="天火"]   过度开采不仅对人们产生了影响，也破坏了源石虫的居住环境。
[name="天火"]   于是它们的行为明显开始躁动起来，估计大量不正常的火山内部活动都是它们开辟居住地的行为导致的。
[name="天火"]   这种行为对源石虫来说是有效扩张居住地的手段，但是对于汐斯塔市来说大概就是灭顶之灾了。
[Character(name="char_145_prove_1",name2="char_166_skfire_3",focus=1)]
[name="普罗旺斯"]   ......“如果我们不怀抱着敬畏之心对待自然的馈赠，自然必然会赐以惩罚。”
[Character(name="char_348_ceylon_4#7")]
[name="锡兰"]   那么，我们现在到底是要怎么做呢。
[name="锡兰"]   难道我们还能通过什么手段，将火山堵上吗！？
[Character(name="char_166_skfire_3")]
[name="天火"]   换个说法，应该是，我们需要让这里的主人安稳下来。
[name="天火"]   动作快，我们往深处走吧。
[Character]
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_cave_2", screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_348_ceylon_4#7")]
[name="锡兰"]   越来越热了......
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   就在前面不远了......
[name="普罗旺斯"]   大家小心！
[Character]
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[name="？？？"]   ——————————！！！
[Character(name="char_348_ceylon_4#8",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   这声音？听起来.......好像很狂暴。
[Character(name="char_166_skfire_3")]
[name="天火"]   当然了，这些虫的智力程度并不足以让他们以个体行为扩张居住地，那么，必然有一只特别的母虫。
[name="天火"]   它才是这里的主人。
[Character(name="char_166_skfire_3",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   ......要从那么多源石虫里找到那什么母虫？
[Character(name="char_166_skfire_3",name2="char_145_prove_1",focus=1)]
[name="天火"]   你在说什么？这可是一只差点引发了火山喷发的熔岩源石虫，它主宰着整座火山！肯定是一眼就能看出来的狠角色啦！
[name="天火"]   被环境因素刺激变异的个体，可能性太多了，说不定可以瞬间融化一整支重装小队喔？
[Character(name="char_348_ceylon_4#7",name2="char_166_skfire_3",focus=1)]
[name="锡兰"]   你是说，这个让整个岩壁都在隐隐作响的声音，是一只“源石虫”发出的......？
[Character(name="char_348_ceylon_4#7",name2="char_166_skfire_3",focus=2)]
[name="天火"]   慌什么，有我在这里。就算这些熔岩源石虫再怎么变异也——
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   这，这是？！
[PlayMusic(intro="$volcano_intro", key="$volcano_loop", volume=0.8, crossfade=1.5)]
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_cave_4")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_348_ceylon_4#8",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   怎么回事......难道岩浆已经蔓延出来了吗？！
[Character(name="char_348_ceylon_4#8",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   不，是那只变异了的源石虫！在洞穴的下方！
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[Image(image="ac3_volcanoboss",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=3, block=false)]
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[name="巨大源石虫"]   ————————！
[name="巨大源石虫"]   ————————！
[Character(name="char_166_skfire_3")]
[name="天火"]   温度在升高，这样的热量，作为一只源石虫而言，的确有些超出规格了呢。
[Character(name="char_348_ceylon_4#8",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   ......那真的还能叫虫？那不就是一整座移动的火山吗？
[Character(name="char_166_skfire_3")]
[name="天火"]   嗯......毕竟没有详细的推演，与我推算的变异结果稍微有点差别。
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   我有点想念艾雅法拉了。
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]   小心！它靠近了！
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=false)]
[Character]
[name="巨大源石虫"]   ————————！
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[name="巨大源石虫"]   ————————————！！！
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   它、它能让地面融化流动？不，不对，墙壁上地面上，布满了这些滚动着的像波浪一样的东西......
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   离远些，那些全部都是熔岩源石虫，这是足够引发火山运动的数量！
[Character(name="char_166_skfire_3#1")]
[name="天火"]   那么毫无疑问，目标就是这家伙了。
[name="天火"]   我们只要让它停止躁动，并且改变它行进的路线，应该就能有效的争取到更多让市民做好避难准备的时间了！
[Character(name="char_145_prove_1",name2="char_166_skfire_3",focus=1)]
[name="普罗旺斯"]   慢着慢着！只凭我们几个到底怎么解决这座小型火山！？
[Character(name="char_145_prove_1",name2="char_166_skfire_3",focus=2)]
[name="天火"]   打啊！还能怎么办？
[Character(name="char

... (全文6351字符)
```

### level_act3d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第六关（后）
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[PlayMusic(intro="$volcano_intro", key="$volcano_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_cave_4", fadetime=1)]
[Blocker(a=0, fadetime=1, block=true)] 
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   小心！
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   喝！
[Character(name="char_166_skfire_3")]
[name="天火"]   哼！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$char_emp", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.7, block=true)]
[Blocker(a=0, fadetime=0.7, block=true)] 
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   它真的有在变虚弱吗？这模样完全看不出来啊！
[Character(name="char_166_skfire_3")]
[name="天火"]   小心岩浆！这家伙肚子里到底吞下了多少黑曜石！？
[Character]
[name="巨大源石虫"]   ————————————————！
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   虽然有些可怜，但我们也不能手下留情！天火！
[Character(name="char_166_skfire_3#1",name2="char_145_prove_1",focus=1)]
[name="天火"]   好啦，我明白！现在可不是保留实力的时候了！
[name="天火"]   那么，这招如何！？
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$char_emp", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character]
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[name="巨大源石虫"]   ————————！
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]   熔岩虫被激怒了......！我去挡住它们，攻击就交给你们！
[Character(name="char_166_skfire_3#1",name2="char_145_prove_1",focus=1)]
[name="天火"]   大尾巴！！
[Character(name="char_166_skfire_3#1",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]  总算能从岩浆的缝隙里瞄准弱点了呐，但是对方这个尺寸，我可不保证能有效喔！！
[Character]
[CameraShake(duration=1, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[name="巨大源石虫"]   ——————！！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$char_emp", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$char_emp", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)] 
[stopmusic(fadetime=5)]
[Character(name="char_166_skfire_3#3")]
[name="天火"]   成功了！它被赶回之前的方向了！
[Character(name="char_166_skfire_3#3",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   太好了！这样一来，市民们就都彻底安全了！
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=1)]
[name="天火"]   真是的！没想到解决一只虫子会这么费劲！这下我的裙子也毁了......
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   毕竟它带领着一整支族群。
[name="普罗旺斯"]   如果不是有人先破坏了它们的生存环境，也许......
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=1)]
[name="天火"]   我累了！不要再提起这种让人疲惫的话题！
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.8, crossfade=3)]
[Character(name="char_348_ceylon_4#6")]
[name="锡兰"]    哈哈，我也已经，累得快站不起来了呢。
[name="锡兰"]    但是，我们得回到汐斯塔，还有人在等我们......
[Character(name="char_348_ceylon_4#7")]
[CameraShake(duration=0.5, xstrength=4, ystrength=4, vibrato=10, randomness=20, fadeout=true)]
[name="锡兰"]    唔！
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   倒是能理解你的想法啦，不过站不稳的时候找同伴搭把手，也是成熟的女性应该学会的事情喔？
[Character(name="char_348_ceylon_4#7",name2="char_145_prove_1",focus=1)]
[name="锡兰"]   谢、谢谢。
[Character(name="char_166_skfire_3#2")]
[name="天火"]  好了，凯旋而归总是令人心情愉悦。赶紧回去吧，说不定还能剩下点度假时间。
[stopmusic(fadetime=1)]
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   ......但是......这里还是迟早会......
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=1)]
[name="天火"]   大尾巴？
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=2)]
[name="普罗旺斯"]   啊，我这就来。
[name="普罗旺斯"]   ......天火。
[Character(name="char_166_skfire_3#2",name2="char_145_prove_1",focus=1)]
[name="天火"]    我知道。
[name="天火"]    但我们应该尊重这座城市的选择，剩下的不该由我们插手，不是吗？
[Delay(time=0.6)]
[Dialog]
[Blocker(fadetime=3,block=true)]
[Image]
```

### level_act3d0_ex01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=1)]
叮铃铃，叮铃铃，叮铃铃......
咚砰叭砰咚砰叭砰擦擦擦擦擦
[PlaySound(key="$phonevibration",volume=0.6)]
欸欸欸欸欸~♪（人声vocal）
[name="经纪人"]   还不起床！
[name="D.D.D."]   哎......哎呀！
[name="D.D.D."]   昨，昨晚high太晚了啦！让我再多睡会儿......
[dialog]
[Background(image="bg_hotel",screenadapt="coverall",fadetime=2)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.8, crossfade=1.5)]
[delay(time=1)]
[Character(name="avg_NPC_017_3#1",fadetime=1,block=true)]
[delay(time=1)]
[name="D.D.D."]   呼啊，冷水澡还是很棒！我有预感，今天会是很棒的一天！
[Character(name="avg_NPC_017_3#1", focus=-1)]
[name="经纪人"]   先把青草汁喝了，已经让侍应生放在你的酒店冰箱里了。
[Character(name="avg_NPC_017_3#5")]
[name="D.D.D."]   那个也太难喝了吧！
[Character(name="avg_NPC_017_3#5", focus=-1)]
[name="经纪人"]   我可是知道的，你在昨天黑曜石节的主持节目里大喊了两分钟对吧？
[Character(name="avg_NPC_017_3#3")]
[name="D.D.D."]   是，是哦。
[Character(name="avg_NPC_017_3#3", focus=-1)]
[name="经纪人"]   虽然你不是歌手，但也要好好保养嗓子啊？不过昨天的演出很成功，祝贺你。
[Character(name="avg_NPC_017_3#6")]
[name="D.D.D."]   哎，我不知道。
[name="D.D.D."]   我试过了，不论怎么努力，我还是有那种感觉，我就是没法超过D.litHun.
[Character(name="avg_NPC_017_3#6", focus=-1)]
[name="经纪人"]   你已经做得很好了。
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   是吗？嗯......无所谓啦。我决定了，之前那张合作专辑，要比上次再多做四首remix的demo，这样合作方也有挑选的空间。
[Character(name="avg_NPC_017_3#1", focus=-1)]
[name="经纪人"]   再加量？！你这几天已经混了二十六首了，哪怕你把它当作没出席活动时的练习，也不可以这样透支体力！
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   没事的，昨天晚上，就在演出里，我摸到了个新点子，这几个方向我都想试试。
[name="D.D.D."]   我已经差不多知道自己的极限在哪里了。既然我知道它在那里，我就得不断冲击它，让它变得更高，让我更难摸到它，这才是进步。
[Character(name="avg_NPC_017_3#2", focus=-1)]
[name="经纪人"]   可演出怎么办？你的日程表可是一直排到下一年啊！
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   绝对没问题！演出的精力是放在另一个槽里的！
[Character(name="avg_NPC_017_3#1", focus=-1)]
[name="经纪人"]   已经听不懂你在说什么了！
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   哎呀，这么长时间以来，我有什么出差错的地方吗？
[Character(name="avg_NPC_017_3#2", focus=-1)]
[name="经纪人"]   上次你可是把整个录音棚里的灯全爆了！
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   那是法术的问题，不是音乐吧！
[name="D.D.D."]   不过，你也提醒到我了。
[name="D.D.D."]   如果理论是正确的，那我在构思和乐感上......绝对能达到更高的高度。
[Character(name="avg_NPC_017_3#1", focus=-1)]
[name="经纪人"]   ......源石技艺和音乐的关系只是种假说，你可不要被牵着鼻子走哦？
[Character(name="avg_NPC_017_3#3")]
[name="D.D.D."]   咦，我有鼻子的吗？
[Character(name="avg_NPC_017_3#3", focus=-1)]
[name="经纪人"]   这是该现在由你来问我的事情吗！
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   但莱塔尼亚人做到了。
[Character(name="avg_NPC_017_3#2", focus=-1)]
[name="经纪人"]   ......
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   音符、调子、曲式、织体，都和源石技艺的编织一模一样。
[name="D.D.D."]   呜啊！太沉重了！感觉这也不是那么适合我的思考！
[Character(name="avg_NPC_017_3#2", focus=-1)]
[name="经纪人"]   你能知道这一点，我已经很欣慰了，呜呜。
[Character(name="avg_NPC_017_3#3")]
[name="D.D.D."]   我可能要去放松一下。
[Character(name="avg_NPC_017_3#3", focus=-1)]
[name="经纪人"]   挺好的，别憋太久了。
[name="经纪人"]   等等，可也别再把一整个城区弄停电了！
[Character(name="avg_NPC_017_3#5")]
[name="D.D.D."]   哎呀，不会的！我会有分寸的！
[Character(name="avg_NPC_017_3#6")]
[name="D.D.D."]   对了对了，上次你说的那个什么克洛宁，我也见过一面了。
[Character(name="avg_NPC_017_3#6", focus=-1)]
[name="经纪人"]   感觉怎么样？
[Character(name="avg_NPC_017_3#6")]
[name="D.D.D."]   实话说......作为合作伙伴，应该不怎么样吧。他大概是只看钱的那种人。
[Character(name="avg_NPC_017_3#6", focus=-1)]
[name="经纪人"]   我上次看合同的时候也有这样的感觉......无所谓，赞助商这边也是塞壬说了算。我还是信得过你看人的眼光的。
[name="经纪人"]   在外面也小心点，据说汐斯塔不简单。Grace那个号也暂时别再用了。
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   安心啦，说了我是有分寸的，这可是堡垒中的堡垒，秘密中的秘密！
[Character(name="avg_NPC_017_3#1", focus=-1)]
[name="经纪人"]   你的秘密小组织，是吗？
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   音乐人总要有自己的空间！
[dialog]
[Character]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.8, block=true)]
[delay(time=1)]
[Blocker(a=0, fadetime=0.8, block=true)]
[Background(image="bg_hotel",screenadapt="coverall",fadetime=2)]
[PlaySound(key="$phonevibration",volume=0.6)]
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   嗯？有简讯......还好，不愧是旅游城市，城际网路还是很快的嘛。
[name="D.D.D."]   咦，这个频道？
[Background(fadetime=2)]
[PlayMusic(intro="$fesready_intro", key="$fesready_loop", volume=0.8, crossfade=1.5)]
[name="D.D.D."]   “From Ada.Closure.Church”......咦，居然是可露希尔吗？
[Character(name="avg_NPC_017_3#2", focus=-1)]
[name="D.D.D."]   “听说这次音乐节非常成功，祝贺你:P” 
[Character]
[Image(image="ac3_title1", fadetime=3,block=true)]
“很久没见了，Grace. 你还联系得到Dijkstra吗？找机会再叫他一起去做点大事吧！”
“对了，注意身体:3”
[name="D.D.D."]   天哪......
[name="D.D.D."]   果然今天也会是很棒的一天！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
```

### level_act3d0_ex03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.6, crossfade=1.5)]
[Background(image="bg_Festival_2", fadetime=2,block=true)]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Delay(time=2)]
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[name="女游客"]   刚才是不是地震了？
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   对啊！！
[name="男游客"]   毕竟我们离舞台这么近哎！看到了吗！？你看到D.D.D.的表情了吗！？她是怎么做到的！？
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="女游客"]   她已经下台了啦，你不要老是这么......等等，这不是又在震了？
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   哎呀，说不定是低音炮的缘故......慢着。
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[name="女游客"]   哎...哎？你也察觉到了？
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   ......快走！
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[name="女游客"]   什、什么？
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   别问那么多了，快跟我走！
[Dialog]
[playsound(key="$runsand", volume=0.7)]
[Character(fadetime=1,block=true)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true,block=true)]
[name="观众"]   不要挤啊！离我远点！
[name="观众"]   你踩着我的脚了！！滚开啊！！
[name="观众"]   有人晕倒了！小心！
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[name="女游客"]   怎、怎么突然都躁动起来，难道真的是......
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   ......我的天。
[name="男游客"]   ......是大帝。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, fadetime=1, block=false)]
[Delay(time=1)]
[Character(name="char_105_emper",fadetime=1,block=true)]
[Delay(time=1)]
[name="大帝"]   嗯哼，天气不错。
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
（欢呼声）
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   大帝！是真人！！啊啊——！
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[name="女游客"]   ......
[Character(name="avg_npc_022",name2="avg_npc_021",focus=2)]
[name="男游客"]   别蠢了！这都什么时候了，你竟然还在意地震！？
[Character(name="avg_npc_022",name2="avg_npc_021",focus=1)]
[name="女游客"]   不，只是，看见大帝，等等，我有点，喘不过气......
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.5)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_020")]
[name="保镖"]   大帝先生，这边请。
[name="保镖"]   各位观众！请退后！退至线后！
[Character(name="char_105_emper")]
[name="大帝"]   喂，那个萨弗拉年轻人。
[name="大帝"]   没关系，让他们靠近点。
[Character(name="avg_npc_020",name2="char_105_emper",focus=1)]
[name="保镖"]   可是大帝先生，您一会还有演出，如果出了什么意外......
[Character(name="char_105_emper")]
[name="大帝"]   意外？
[name="大帝"]   枪击，刺杀，绑架，自杀威胁，意外是指这些东西？
[name="大帝"]   这些东西能阻止什么？阻止我吗？
[name="大帝"]   不，它们会变成我舞台的一部分，就像语言的意义被节奏消解，你明白吗？
[Character(name="avg_npc_020",name2="char_105_emper",focus=1)]
[name="保镖"]   不、不明白......
[Character(name="char_105_emper")]
[name="大帝"]   简单来说就是节目效果。放轻松，塞壬唱片绝对不会追究你们失责。
[Dialog]
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
（欢呼声）
[name="观众"]   大帝！！大帝！！大帝！！
[stopmusic(fadetime=1)]
[Delay(time=1)]
[name="表情古怪的游客"]   ......
[Character(name="char_105_emper")]
[name="大帝"]   喔，总算来了，快，不要紧张，放轻松，大胆点，相信你自己。
[Character]
[name="表情古怪的游客"]   什么西哥伦比亚的说唱之神，你，你就是个痞子，一个走狗屎运的幸运儿......
[Character(name="char_105_emper")]
[name="大帝"]   大声点，伙计，大声说话！喂，萨弗拉人，不要赶他走，把麦克风给他。不要慌，这里听我的。
[Character]
[name="表情古怪的游客"]   你毁了我们的生活，你却坐拥那么多产业，你......你该去死！！
[Character(name="avg_npc_022")]
[name="女游客"]   咿呀——他拔出了一把弩！快躲开！
[Character]
[name="表情古怪的游客"]   不怪我，对，都是你的错，你所谓的说唱帝国建立在多少歌手的牺牲之下——
[name="表情古怪的游客"]   什么大帝啊，吃屎去吧，你这只下作的企鹅！
[Character(name="char_105_emper")]
[name="大帝"]   啊哈，让我想想，到底是谁在耍一些不入流的小手段？媒体，舆论，人身攻击，还有枪杀，哼？
[name="大帝"]   你以为在下水道和垃圾堆里打一圈滚我就认不出你了吗？对那些年轻人开枪让你满足吗，“歌手”？
[Character]
[name="表情古怪的游客"]   你——！
[Character(name="char_105_emper")]
[name="大帝"]   如果不是我恰好有那么点看不顺眼，你们又会继续“排除”掉多少不合口味的新星。
[name="大帝"]   然后把捞来的钞票堆在自己的澡盆里，唾弃着整个哥伦比亚？
[Character]
[name="表情古怪的游客"]   闭嘴！给我去死！
[Character(name="avg_npc_020")]
[name="保镖"]   快保护大帝先生！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$p_imp_amiyamag_h", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_020")]
[name="保镖"]   大帝先生中弹了，快......欸？
[name="保镖"]   开枪的是大帝先生？那家伙的弩被打飞了？
[Dialog]
[Character]
[Character(name="char_105_emper",fadetime=1,block=true)]
[Delay(time=1)]
[PlayMusic(intro="$emperor_intro", key="$emperor_loop", volume=0.6, crossfade=1.5)]
[name="大帝"]   哒哒哒哒哒，哒！砰！
[name="大帝"]   真奇怪。同你废话了这么多，枪口冒烟的人怎么是我？猜猜看？
[name="大帝"]   是因为你太没种，还是我光芒万丈，你睁不开眼？
[Character]
[name="表情古怪的游客"]   咕——呃——你随身带着铳械......
[Character(name="char_105_emper")]
[name="大帝"]   如果一个人每天多死个几次，就会养成随身携带武器的好习惯。
[Character]
[name="表情古怪的游客"]   咳咳——你以为，只有我一个人吗？想想你过去招惹的敌人，你走不出这座汐斯塔市的！
[Character(name="char_105_emper")]
[name="大帝"]   我的过去比这边虚假的海洋还要宽广，你说的敌人又在哪个犄角旮旯？
[Character(name="avg_npc_020",name2="char_105_emper",focus=1)]
[name="保镖"]   大帝先生！观众里面混着很多他们的同伙，我们处理不过来......
[Character(name="avg_npc_020",name2="char_105_emper",focus=2)]
[name="大帝"]   行了，不要这么慌张。你们就维护好现场的秩序，剩下的交给专业人士。
[name="大帝"]   比如我的，企鹅物流。
[Character]
[Dialog]
[Dialog]
[Character]
[Character(name="char_101_sora_1",name2="char_103_angel_1",fadetime=1,block=true)]
[Delay(time=2)]
[Dialog]
[Character]
[Character(name="c

... (全文7662字符)
```

### level_act3d0_ex06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[PlayMusic(intro="$lab_intro", key="$lab_loop", volume=0.8, crossfade=1.5)]
[Character(name="npc_2004_Alty")]
[name="Alty"]  唔嗯。
[Character(name="npc_2004_Alty")]
[name="Alty"]  这就是传闻中的罗德岛啊，感觉确实是个充满了谜团的地方。
[Background(image="bg_infirmary", fadetime=1,block=true)]
[name="Alty"]  空气中还夹杂着一股非常熟悉的气息。嗯......
[name="Alty"]  要不是真的登上这艘载具，我还以为自己依然呆在海边呢。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  这里近期确实接待过几个阿戈尔人。
[name="凯尔希"]  你也是阿戈尔的访客，但我没在访客名单上看到你的名字。我也许没法接待你。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]  啊啊，抱歉抱歉，不过不劳烦你了，我说点事就走，不会在这里呆太久的。
[name="Alty"]  咦，你居然还知道我的名字？
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  这几天会待在汐斯塔一带的人，没有人不知道你的名字。
[name="凯尔希"]  虽然我并没有去，但我也早有耳闻。日落即逝的贝斯手Alty女士，罗德岛不是个可以随意进出的地方。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   啊呀，唉，不要那么有敌意啊。毕竟我们有很多共同话题，对吧，比如说还能看到星星的时候？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  ——请坐。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   谢谢。你肯定会好奇我是怎么进来的吧？
[name="Alty"]  这不重要的，你不用担心罗德岛的安保设施有什么漏洞，单纯是我运气好罢了。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  话语掩盖不了你的实力。请放心，我不怎么担忧，至少它只会对重要的访客网开一面。
[name="凯尔希"]  不过，一位音乐巨星是怎么对这狭小的病房产生兴趣的？
[name="凯尔希"]  如果是想和你的阿戈尔朋友叙旧，你可能走错房间了。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   朋友？嗯......谈不上吧？不，该说，离朋友有点远呢......
[name="Alty"]   其实我是来找你的。或者说，是来看看你的。
[Character(name="char_003_kalts_1#2")]
[name="凯尔希"]  很抱歉，我不认识你，我也不是动物园的展品。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1#2",focus=1)]
[name="Alty"]   阿戈尔人的传闻，我从Frost那里听说了很多。她很少讲故事的，但那次她说了很多。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  我没兴趣听你说些你朋友的奇异冒险故事......
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   那唱出来怎么样？
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  ......或是面目全非的有关我的逸闻。我希望你能更直接一点。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   有人告诉过我闲聊可以缓和气氛，我做的似乎不太成功......
[name="Alty"]   那就开始吧。我其实有些讨厌他们阿戈尔人。当然我也知道，他们确实挺可怜的。
[name="Alty"]   只是，如果没有你出现的话，这几个阿戈尔人可能都会沉入海底，被幽暗的海洋吞噬。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  我并没有做什么重要的事情。
[Character(name="npc_2004_Alty")]
[name="Alty"]   你救了他们，而且这里就有好几个。
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]  ......
[Character(name="npc_2004_Alty")]
[name="Alty"]   这些特别的阿戈尔人，他们一点都不尊敬你，明明你为他们做了这么多。
[name="Alty"]   你平时是不是对他们太凶了？
[Character(name="npc_2004_Alty",name2="char_003_kalts_1#3",focus=2)]
[name="凯尔希"]  我只是在阻止他们自取灭亡。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1#3",focus=1)]
[name="Alty"]   那也是种慈悲心的体现，医生。
[name="Alty"]   只不过，我的问题也就在这里。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  请说。
[Character(name="npc_2004_Alty")]
[name="Alty"]   你知道阿戈尔人的敌人是什么吗？
[name="Alty"]   或者，你其实知道我的身份吧？
[Character(name="char_003_kalts_1#2",name2="npc_10002",focus=2)]
[name="Mon3tr"]  ！！
[Character(name="char_003_kalts_1#2",name2="npc_10002",focus=1)]
[name="凯尔希"]   Mon3tr，停下！
[Character(name="char_003_kalts_1#2",name2="npc_10002",focus=1)]
[name="凯尔希"]  你很年轻。
[Character(name="npc_2004_Alty")]
[name="Alty"]   是的，我们很年轻，我们没有经历过那些悲伤的事情，所以我们还在这，还可以说话，还可以唱歌。
[Character(name="char_003_kalts_1#2",name2="npc_10002",focus=1)]
[name="凯尔希"]  深海猎人们在做他们应该做的事情。
[Character(name="npc_2004_Alty")]
[name="Alty"]   我明白，这些我都明白。只不过，我们也想知道答案。
[name="Alty"]   我们一点也不想和这些小家伙敌对。
[Character(name="npc_2004_Alty")]
[name="Alty"]   Frost她啊，从小就只对音乐和食物这两样东西感兴趣。就连休息对她来说都是浪费时间。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  这位朋友你可以等到我们真正会面了再介绍给我。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   对不起，我的老毛病又犯了......
[name="Alty"]   我信任医生你，以及你掌握着的真相。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  我不认为你对真相的了解比我少。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   不，只是我们有各自擅长的事情而已，比如说，我觉得你唱歌也许不会那么动听。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  ......
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   啊，嗯，只是举个例子！没有要冒犯你的意思。
[name="Alty"]   但阿戈尔的平静，就像你知道的那样，只是个表面现象。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  大多数人对大海一无所知。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   大地的孩子又怎么会知道这些呢？对他们要求太高也不好。
[name="Alty"]   只是，哪怕是这表面上的平静，可能也没法坚持太久了。欲望果然是可怕的东西。
[name="Alty"]   所以，我需要一些，嗯，信息。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  又是信息？
[Character(name="npc_2004_Alty")]
[name="Alty"]   是的。
[name="Alty"]   这么说......哦哦，原来对这些感兴趣的不止我一个啊，哈哈。
[name="Alty"]   我有些好奇，上一个人是谁呢？
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  是个阿戈尔人，也是个深海猎人。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   那我们也许真的能做朋友呢，呼呼。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  当然。我能理解你为什么来找我。
[name="凯尔希"]  活得越久，故事越多，伤痕越疼，脾气越差。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   抱歉，我不是想揭你的伤疤......
[Background(fadetime=3, block=false)]
[Character(name="npc_2004_Alty")]
[name="Alty"]   只是你确实不像其他人。他们会被过多的感情束缚、被言论利用，甚至变成某种灾难。
[name="Alty"]   也难怪那个人让你作为最后的底牌来帮助小兔子和Dr.{@nickname}。
[name="Alty"]   你其实是台X光机对吧？
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  我也希望自己是台单纯的机器。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   唔，不好意思，我其实只是想说，虽然你不会选择告知别人，但里面的东西，你其实已经全看到了吧？
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=2)]
[name="凯尔希"]  这个问题，我不能回答你。
[Character(name="npc_2004_Alty",name2="char_003_kalts_1",focus=1)]
[name="Alty"]   那就让我切入主题吧。这个问题你是可以回答的。
[Character(name="npc_2004_Alty

... (全文6877字符)
```

### level_act3d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.8,crossfade=1)]
[name="？？？"]   火山监测站那边的样本数据已经调出来了，请您查看一下。
[name="女性的声音"]   直接告诉我结果吧。
[Image(image="ac3_report",screenadapt="coverall",x=0, y=0, xScale=1, yScale=1, fadetime=4)]
[name="？？？"]   那边的人说样本的温度还没超过今年的最高温度。
[name="？？？"]   而且比过去三年的峰值还低不少。蒸汽状况也正常。
[name="？？？"]   所以......
[name="女性的声音"]   所以?
[name="？？？"]   所以监测站那边判断火山并不会有什么异常，再次驳回了您的公告请求，市长也......
[CameraShake(duration=2, xstrength=14, ystrength=6, vibrato=30, randomness=60, fadeout=true, block=false)]
[name="女性的声音"]   开什么玩笑！！
[name="女性的声音"]   虽然方法简陋了一些，但我手头的样本明显有问题。
[name="女性的声音"]   去年那个时候，火山的状况就已经很危险了！
[name="女性的声音"]   但是他们一点警告都没有准备，甚至是新闻都没有！一点都没有！！
[name="？？？"]   锡兰小姐，请、请您冷静点。
[name="？？？"]   如果监测站说没有异常，那我们采取任何行动都不会有人相信。
[Image(fadetime=2)]
[name="锡兰"]   ......抱歉。
[name="锡兰"]   观测站的样本数据可靠吗？
[name="？？？"]   说实话汐斯塔市政厅对这方面一直不是很重视，也许检测仪器真的出了点问题。
[name="锡兰"]   那火山可能会发生异常的事实也会因此被掩盖。
[name="？？？"]   所以，下一步您打算怎么做？
[name="锡兰"]   现在的现象并不能用我所学到的专业知识解释，如果通过机构里的人无法得到正确的报告，就要依靠外人了。
[stopmusic(fadetime=2)]
[name="锡兰"]   如今情况还算稳定，我们还有时间。能花点时间从这些游客里找到专业人员吗？
[name="锡兰"]   虽然不能奢望能找到合适的人，更不能指望他们能给出结论，但是这是我们最后的机会了......
[name="锡兰"]   已经有不少赶在这个时候来到汐斯塔的游客了。
[name="锡兰"]   毕竟，马上就是黑曜石节举办的时间了，再不采取行动的话就来不及了。
[Image(image="ac3_title1", fadetime=3,block=true)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[name=""]   10:10 A.M.  天气/晴
[name=""]   汐斯塔
[Blocker(a=0, fadetime=2, block=false)]
[Image(image="ac3_title2", fadetime=2)]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[largebgtween(xFrom=-180,xTo=-720,  duration=25, ease="1", block=false)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="广播"]   亲爱的旅客，您好，欢迎在一年一度的黑曜石节期间来到汐斯塔市。
[name="广播"]   既然选择了来我们汐斯塔度假消暑，那么这座城市就一定不会让您失望！
[name="广播"]   在这里，炎热会变成高涨的热情，您将会忘记一切不快和疲劳，彻底沉醉于汐斯塔市这个迷人的城市！
[name="广播"]   而今年的汐斯塔有的可不仅仅是碧海蓝天、阳光沙滩，还有盛大召开的黑曜石节！
[name="广播"]   持续半个月的黑曜石节中，除了美食和娱乐，全天开放的一切娱乐活动，还有我们最为盛大的全城音乐节！
[name="广播"]   我们请到了各地的音乐大咖作为我们的特别嘉宾，带来这最热烈的音乐盛典！
[name="广播"]   在节日持续日期中，我们特意为大家准备了各项免费设施和活动，大家可以按照喜好进行游玩！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Image]
[Character]
[largebg]
[Blocker(a=0, fadetime=0.6, block=false)]
[Background(image="bg_sunnytown_2",x=-80, y=0, xScale=1.1, yScale=1.1,block=true)]
[BackgroundTween(image="bg_sunnytown_2", xFrom=-80, yFrom=0, xTo=20, yTo=0,duration=15)]
[name="广播"]   在市民广场上，“摇滚派对”和无限供应的汐斯塔自产啤酒是绝对的主角！
[name="广播"]   放开一切，跟随着鼓点尽情舞动。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Character]
[Background]
[Blocker(a=0, fadetime=0.6, block=false)]
[Dialog]
[Background(image="bg_sunnytown_1",x=80, y=0, xScale=1.1, yScale=1.1,block=true)]
[BackgroundTween(image="bg_sunnytown_1", xFrom=80, yFrom=0, xTo=-20, yTo=0,duration=15)]
[name="广播"]   想要享受悠扬？前往第二大道的赫尔曼大酒店门前广场，那里是爵士的天堂。
[name="广播"]   无限制无规则，只要你愿意，你就能融入！
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.6, block=true)]
[Character]
[Background]
[Blocker(a=0, fadetime=0.6, block=false)]
[Dialog]
[Background(image="bg_Festival_1",x=-80, y=0, xScale=1.1, yScale=1.1,block=true)]
[BackgroundTween(image="bg_Festival_1", xFrom=-80, yFrom=0, xTo=20, yTo=0,duration=15)]
[name="广播"]   座落在城东火山脚下的加里森游乐场，在继续24小时免费开放的同时，搭建了城中最大的音乐舞台。
[name="广播"]   除开每天的固定表演，我们还迎来了众多神秘嘉宾，是喜欢说唱文化的您绝对不容错过的存在。
[name="广播"]   除此之外，也还有众多演出伴随着我们的各项活动分布在全城，等待着您的到来。
[name="广播"]   请各位前往在各个路口岗哨处的STAFF人员处领取黑曜石节特制城市地图。
[name="广播"]   我们为您标注了节日期间，市内所有演出的地点与时间，方便您提前规划路线与行程。
[name="广播"]   狂欢之际，大家也要注意天气。
[name="广播"]   今天的气温高达36度，是入夏以来最热的一天。出行期间，请注意防晒，避免中暑。
[name="广播"]   祝大家玩得愉快！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_sunnytown_1",screenadapt="coverall",block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[Dialog]
[Character(name="char_002_amiya_1#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="阿米娅"]   不愧是专门的旅游度假都市汐斯塔，气氛真是高涨呢。
[Decision(options="没想到会这么热闹。;竟然会举办这么大型的活动。",values="1;2")]
[Predicate(references="1;2")]
[name="阿米娅"]   我也没有想到！
[name="阿米娅"]   在来之前我们都没猜到这里这么特别，本来还以为是个普通的海边小城。
[name="阿米娅"]   多亏了给我们推荐这里的凯尔希医生了。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(screenadapt="coverall", image="bg_ri_1")]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]   ......这地方我没有什么兴趣，你们去就可以了。
[Character(name="char_017_homura_3#1")]
[name="煌"]   等等我！我也想去。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]   站住。你的伤还没好，不准走。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sunnytown_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Decision(options="我也不讨厌这样的地方。;真是积极的推荐手法。",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1#10")]
[name="阿米娅"]   博士能喜欢这里那就最好了。
[name="阿米娅"]   这段时间遇到了太多事情，博士也辛苦了。
[name="阿米娅"]   这次，有不少罗德岛的干员们也都一起过来了，趁这个机会好好放松一下吧。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]   啊，博士，你看那边，有人在露天弹钢琴。
[name="阿米娅"]   那边有人在弹吉他，还有小提琴，哇，跳舞的也有......
[name="阿米娅"]   让我想起以前天天练习演奏的日子。
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   整条街上的气氛都跟刚才的海滩完全不同。
[name="阿米娅"]   第一见到这么多喜欢演奏的人，果然让人很想融入他们呢。
[Decision(options="阿米娅把小提琴带来了吗？",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   啊没有没有，我并不是这个意思。我并不是说自己要去加入他们！
[name="阿米娅"]   可能要完全恢复到之前的水平，我还要重新练一练才行。
[Decision(options="可是阿米娅现在也不输他们啊。",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#10")]
[name="阿米娅"]   哪，哪里有啊！
[name="阿米娅"]   不过，博士能这么说，我好高兴。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=

... (全文17560字符)
```

### level_act3d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第三关（前）
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8,crossfade=1)]
[Delay(time=1)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(image="ac3_volcano",x=0, y=0, xScale=1, yScale=1, fadetime=0, screenadapt="coverall")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[name="艾雅法拉"]   最后，根据同位素的对比情况以及多种样本的最终分析，基本可以确认你们的猜想是对的。
[name="艾雅法拉"]   火山活动频率确实处于一个异常的爬升状态，虽然不至于马上爆发天灾，但是并不能对其视而不见。
[name="艾雅法拉"]   火山活动应该会在二至四周之内到达临界点，之后就会引起火山天灾的爆发。
[name="艾雅法拉"]   可能的话，最好马上安排市民进行避难准备。                    
[name="艾雅法拉"]   ......以上，就是根据你们给出的情报得出的结论。
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Background(image="bg_hotel", fadetime=0)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   不愧是艾雅法拉，隔着联络竟然也能整整说了40分钟。
[name="普罗旺斯"]   博士，你听懂了吗？
[Decision(options="什么都没说一样。;嗯，结论我懂。",values="1;2")]
[Predicate(references="1")]
[name="普罗旺斯"]   我也觉得，反应过来的时候好像就结束了。
[Predicate(references="2")]
[name="普罗旺斯"]   哇，博士真厉害，我完完全全没有听明白......
[Predicate(references="1;2")]
[name="普罗旺斯"]   看那边那两个人的样子，我还以为只有我听不懂呢。
[Character(name="char_348_ceylon_4#7",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]   不愧是艾雅法拉，连我都重新上了一课呢。
[Character(name="char_348_ceylon_4#7",name2="char_166_skfire_3#2",focus=1)]
[name="锡兰"]   原来如此，不愧是专家，收集的这些数据原来还能从这个方向解读。
[name="锡兰"]   没想到在这里能够学到这样的知识，天哪，我应该全部用笔记下来！
[Character]
[name="艾雅法拉"]   虽然目前情报还比较有限，不过我的判断和你们是一样的，这座火山很有可能已经从休眠状态进入了活化状态。
[name="艾雅法拉"]   可惜我不在现场，没办法对于火山的活动原因进行进一步的探索。
[name="艾雅法拉"]   ......对不起，如果有更多的现场情报我们甚至能找到火山活动的契机，更精确地确定活动的周期。
[name="艾雅法拉"]   如果那样的话也能方便市民们做好转移安排。
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   大家都明白你对火山的执着，艾雅法拉。
[name="普罗旺斯"]   你已经帮了我们大忙了。辛苦你了。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Blocker(a=0, fadetime=1, block=false)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.8, crossfade=1.5)]
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   有你们这样专业的团队帮助我进行确认实在是太好了。
[name="锡兰"]   可能是因为仪器的问题，汐斯塔的观测点一直都读不出任何数据异常来。
[name="锡兰"]   看来为此我的东奔西走还是值得的。
[name="锡兰"]   我们得赶快把这些消息带给市政府才行，不然后果肯定不堪设想。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   你的意思不会是说，汐斯塔市在这个时候举办了如此大规模的节日活动，却一点天灾的准备都没有吧。
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   现在别说准备了，市民和游客甚至连天灾有可能产生都不知道。
[name="锡兰"]   我父亲在三个月前前往新开发区进行工作了，要在几天后才能回来，现在城里大大小小的事情都交给了他的秘书克洛宁处理。
[name="锡兰"]   而克洛宁也是这座城市的天灾信使，我们只需要现在回去市政府，带回数据和其他样本，就可以让他了解情况了。
[name="锡兰"]   虽然我是市长的女儿，但是关于城市政府的事情我并没有太多参与。
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   不过现在既然已经得到了确实的证明，就可以让家里的人帮助我了。
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   博士，我有一个想法，我去火山进一步确认情况，我想试着找一找艾雅法拉提到的契机。
[name="普罗旺斯"]   锡兰这边能拜托你和其他人吗？
[Decision(options="进入火山？那也太危险了？！",values="1")]
[Predicate(references="1")]
[Character(name="char_145_prove_1")]
[name="普罗旺斯"]   天灾信使的工作总是危险的，放心吧，在这方面我还是很有经验的。
[name="普罗旺斯"]   虽然远程通讯只能在旅馆进行，不过我会随时和博士保持联络的。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   我也和你一起去。
[CharacterCutin(widgetID="1")]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   欸。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]   你有什么意见？我可不放心，万一你破坏了重要的研究数据怎么办。
[name="天火"]   我当然是要跟你一起去。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]   呃，没有意见没有意见。
[name="普罗旺斯"]   说起来，我们需要通知一下阿米娅吗？
[Character(name="char_145_prove_1",name2="char_166_skfire_3#2",focus=2)]
[name="天火"]   不用啦。小事一桩而已，有博士知道就够了。
[Dialog]
[Character]
[Delay(time=0.5)]
[Character(name="char_348_ceylon_4#2")]
[name="锡兰"]   既然如此那我们就说定了，博士。也请你准备一下资料，我们下午两点就出发去市政厅。
[Decision(options="没问题。",values="1")]
[Predicate(references="1")]
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   呼，事情定下来后，总算可以稍微放松一下了。
[name="锡兰"]   博士，我这里有一些从维多利亚带来的茶叶，来喝一杯茶吧。
[Decision(options="好吧。;不必了。",values="2;3")]
[Predicate(references="2")]
[name="锡兰"]   我想你一定会喜欢的。
[Predicate(references="3")]
[name="锡兰"]   是不会泡茶吗？那我亲手帮你泡一杯吧。
[Decision(options="好吧。;......不必了。",values="4;5")]
[Predicate(references="4")]
[name="锡兰"]   嗯哼，我想你一定会喜欢的。
[Predicate(references="5")]
[name="锡兰"]   真是个麻烦的人。
[name="锡兰"]   这可是在维多利亚中数一数二的茶叶哦？
[Decision(options="败给你了。;............不必了。",values="6;7")]
[Predicate(references="6")]
[name="锡兰"]   这就对了，我想你一定会喜欢的。
[Predicate(references="7")]
[name="锡兰"]   我的泡茶手艺可是很好的，不尝一下会抱憾终身哦？
[Decision(options="...................好吧。",values="8")]
[Predicate(references="8")]
[name="锡兰"]   真是个顽固的人，非要我这么说才能接受。
[name="锡兰"]   那么，请稍等片刻。
[Predicate(references="2;4;6;8")]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=0.6)]
[Dialog]
[Blocker(block=true)]
[Image]
```

### level_act3d0_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第三关（前）
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[playsound(key="$beach", volume=0.7, channel="B",loop=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   ......可以陪我逛逛吗，博士。
[Decision(options="我有些担心你。",values="1")]
[Predicate(references="1")]
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   博士，你知道吗，我小的时候，这片沙滩没有这么多人的。我很喜欢一个人在那里堆沙子城堡。
[name="锡兰"]   ......这座城市在我父亲的治理下，每一年都在变得更好。
[name="锡兰"]   我和我的父亲，该怎么说呢，话并不多。
[name="锡兰"]   我一直在想，是不是比起跟我多说说话，城市和赚钱对他才更重要。
[name="锡兰"]   母亲在生我的时候就去世了，我有时候也会想是不是因为这样，他才不喜欢我。
[name="锡兰"]   仿佛也不在乎我喜不喜欢他，自我记事起，他就经常不在家里。与其说是父女，更像是住在同一座房子里的陌生人。
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.8, crossfade=1.5)]
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[largebg]
[Background(image="bg_hotel",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]   黑，我要出门去观察海边的生态！
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#1",focus=2)]
[name="黑"]   不行，小姐，老爷吩咐过，不能随便出门的。
[Character(name="char_348_ceylon_4#1",name2="char_340_shwaz_2#1",focus=1)]
[name="锡兰"]   可家里的书我已经看腻了！黑你又一点也不好玩。
[Character(name="char_348_ceylon_4#1",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   对不起，小姐。这也是为了您的安全着想，外面是很危险的。
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   不是有你在吗，难道你会让我身处危险吗？
[Character(name="char_348_ceylon_4#4",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   ......那自然是肯定不会的。
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   那还有什么问题？我们走！
[Character(name="char_348_ceylon_4#6",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   ......那么，请您绝对不要离开我的视线。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sunnytown_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_348_ceylon_4#5")]
[name="锡兰"]   可以说，黑在我的身边这件事，对我来说，是我的生活中最理所当然不过的一部分了。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[stopsound(channel="B", fadetime=1)]
[delay(time=1)]
[Background(image="bg_sunnytown_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[name="男市民"]   快点，这批装饰是今晚的LIVE要用到的。
[name="男市民"]   要是赶不上了可就麻烦了！
[Character(name="char_348_ceylon_4#5")]
[name="锡兰"]   啊，那个人......
[Character(name="char_348_ceylon_4#4")]
[name="锡兰"]   没记错的话，是第二大道那家“知更鸟咖啡店”的店主爷爷的孙子。
[name="锡兰"]   那里是我以前常去的地方，店主爷爷很和蔼。店里装饰着他去世的妻子奇幻的花和盆栽，放着他们以前一起喜欢的音乐。
[name="锡兰"]   这么说来，他确实说过，身体不行了，要把店传给孙子了呢。
[name="锡兰"]   时间过得真快。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_hotel",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_348_ceylon_4#7",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   为什么？
[Character(name="char_348_ceylon_4#7",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   因为我得了矿石病，小姐。
[name="黑"]   靠近我对您的身体不好，您只要在需要的时候叫我就好。
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   那是什么，很痛吗？
[Character(name="char_348_ceylon_4#8",name2="char_340_shwaz_2#3",focus=2)]
[name="黑"]   ......不会很痛，但是，会死。
[name="黑"]   这种病是治不了的，小姐。
[name="黑"]   而且......
[Character(name="char_348_ceylon_4#3",name2="char_340_shwaz_2#3",focus=1)]
[name="锡兰"]   我偏要把它治好！
[name="锡兰"]   哼，你等着吧！将来有一天，我会把它给打败，然后把黑从它手里抢回来。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[largebg]
[Background(image="bg_sunnytown_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   我会想要研究源石，也是因为她是感染者，我想要把她治好。
[name="锡兰"]   这是一直以来支持我的动力啊，为了这个梦想，我可是去了维多利亚读书欸。
[name="锡兰"]   晦涩难懂的源石研究，我一开始完全搞不懂，好几次都想放弃了，最后还是坚持了下来。
[name="锡兰"]   维多利亚也好远啊，本来我一开始还完全不习惯那里的。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=2, block=true)]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Character(fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   结果到了现在，我与其说是一个汐斯塔人，不如说是一个维多利亚人了。
[name="锡兰"]   博士，难道说，我所拥有的一切，都是假的吗？
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Character]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=false)]
[Character(name="char_340_shwaz_2#1")]
[name="黑"]   为了守护这里，我可以付出很多东西。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Blocker(a=0, fadetime=2, block=false)]
[Decision(options="我也不知道。;她说不定也有苦衷。",values="1;2")]
[Predicate(references="1")]
[Character(name="char_348_ceylon_4#5")]
[name="锡兰"]   ......呼。是啊，博士又怎么会知道呢。
[Predicate(references="2")]
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   有什么苦衷，连我也不能告诉吗？
[name="锡兰"]   而且，无论有什么样的苦衷，做了坏事就是做了坏事，这是无法回避的。
[Predicate(references="1;2")]
[Character(name="char_348_ceylon_4#9")]
[name="锡兰"]   博士，你说，我应该放弃吗？
[Dialog]
[Decision(options="我很难就这件事给你答案......",values="3")]
[Predicate(references="3")]
[Decision(options="但是我知道的是，你也是研究源石的学者。",values="4")]
[Predicate(references="4")]
[Character]
[Dialog]
[

... (全文7812字符)
```

### level_act3d0_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第三关（前）
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_Festival_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.8, crossfade=1.5)]
[Delay(time=1)]
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   ......
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   所以你们都知道了。
[Character(name="char_348_ceylon_4#3")]
[name="锡兰"]   这样简单的骗局，又能欺瞒多久呢？
[Character(name="char_290_vigna")]
[name="红豆"]   啊，LIVE快开始了......
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_Festival_2",xScale=1.1, yScale=1.1)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_NPC_017_3#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="D.D.D."]   女士们，先生们，欢迎你们来到黑曜石节！
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   你们过得愉快吗！！！
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   （狂热的欢呼声）
[Character(name="avg_NPC_017_3#2")]
[name="D.D.D."]   多么热情的回应，但是我要告诉你们，你们还没有见识到黑曜石节真正的魅力！
[name="D.D.D."]   今晚，所有邀请的音乐家们将齐聚一堂，为你们带来无上的听觉与视觉的盛宴！
[Character(name="avg_NPC_017_3#1")]
[name="D.D.D."]   一个主场舞台，四个大舞台，十二个小舞台，四十位来自各领域的知名音乐家，十八个小时，将会一直演出直到明天的太阳升起！
[Character(name="avg_NPC_017_3#5")]
[name="D.D.D."]   告诉我，你们准备好了吗！！！
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   （疯狂的欢呼声）
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[playsound(key="$fireworks", volume=0.8)]
[playsound(key="$fireworks", volume=0.8)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_340_shwaz_2#2")]
[name="黑"]   ......锡兰告诉了我火山的事情了。
[name="黑"]   所以你不仅篡改了火山监测数据，而且宣称小姐要散布谣言。
[Character(name="avg_npc_023_2#2",name2="char_340_shwaz_2#2",focus=1)]
[name="克洛宁"]   因为你我都知道啊。赫尔曼做的那些事，我们都知道！
[Character]
[Dialog]
[name="？？？"]    知道什么的话，就说吧。
[Character(name="avg_npc_024",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]    克洛宁，说下去吧。但你也要把我“因事务出差”的时候，你到底做了些什么，全都说出来。
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   爸——父亲？！
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   你怎么在这里？！
[Character(name="avg_npc_024")]
[name="赫尔曼"]  很意外吗，克洛宁。
[name="赫尔曼"]  在我明令禁止了从火山中开采黑曜石之后，在市场上依然有新开采的黑曜石流通。
[name="赫尔曼"]  开采队很多次出现在火山口，却没有人向我报告。
[name="赫尔曼"]  最终开采的货物经过多次转送，已经被送到了市政厅的废弃仓库。
[name="赫尔曼"]  在我下令拨款为汐斯塔出现的矿石病患者提供各方面资助后，市里反而出现了各种他们受到的不公待遇的流言。
[name="赫尔曼"]  这些事情有没有让你意外过？
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   嘁......
[Character(name="avg_npc_024")]
[name="赫尔曼"]  这些事情让我意外到愤怒难安！！
[name="赫尔曼"]  为了找到这些事情的真相，我放出了离开城市的消息，让黑作为我的下属替我在城市调查真相。
[Dialog]
[Character]
[Character(name="char_188_helage_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="赫拉格"]  看来，只要调查一下这些记录和相关人员就行了。
[Character(name="char_348_ceylon_4#8")]
[name="锡兰"]   赫拉格爷爷，你们也平安无事！
[Character(name="avg_npc_024")]
[name="赫尔曼"]  真遗憾，克洛宁。
[name="赫尔曼"]  原本，我是不介意和你分享一些东西的，但你太急躁了。
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   我？急躁？
[name="克洛宁"]   我这些不都是为了这个城市，不都是你教我的吗！
[name="克洛宁"]   十年前的巴鲁一家，八年前的电视塔倒塌案，还有你如何说服......
[name="克洛宁"]   哦，我想是不是用吞并更好一些？你是如何吞并塔拉克部族的，我都看在眼里。
[name="克洛宁"]   我的一切都是从您那里学来的......
[name="克洛宁"]   盈利，处理。手段不重要，结果才是重要的。
[name="克洛宁"]   这个破烂的乡下，你以为我为它付出了多少心血，换来的又有什么？
[name="克洛宁"]   好不容易因为黑曜石带来的收益，却要全部变成给那些根本治不好的病人的补贴？
[name="克洛宁"]   与其如此，还不如就让火山爆发好了！而我只需要保护好汐斯塔的物资和财产，一样可以东山再起！
[Character(name="avg_npc_024")]
[name="赫尔曼"]  我做过许多事。但我不会拿汐斯塔做赌注。
[name="赫尔曼"]  矿工和研究者的生命，全城的生命都被你视作什么了。
[name="赫尔曼"]  克洛宁，你被解雇了。
[Character(name="avg_npc_023_2#2")]
[name="克洛宁"]   哈哈哈哈糊涂的老头，那可还说不清楚！
[name="克洛宁"]   多亏你的喋喋不休，我的人手已经全都到了！
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background]
[Blocker(a=0, fadetime=2, block=false)]
[name="伊芙利特"]  嗯？等等，我怎么烤糊了？
[name="伊芙利特"]  角峰叔！你来看一下！
[name="伊芙利特"]  搞什么，感觉温度流向都变了......
[Dialog]
[Delay(time=2)]
[name="古米"]  嗯嗯嗯！海浪好大！
[name="古米"]  欸！海浪变得好大哦！也太大了吧哈哈哈哈哈！
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background]
[Blocker(a=0, fadetime=2, block=false)]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     ......
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     ......
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     怎么不说话了，你刚刚明明话很多的。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     我在想。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     唔，像你这样的人居然还有这么沉默寡言的时候。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     我感觉我的大脑有些激动，先让我冷静一下。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     不是，虽然我不是地质学家，也不懂什么源石物理啊高能源石技艺啊......
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     高能源石技艺和火山生态学是两回事，肯定没办法解决我们现在的问题。
[name="天火"]     硬要说的话，造一个巨大的容器把所有能量抽出来，也许......
[name="天火"]     可这种法术，就连我也要编个好几年。不可能的，完全不可能。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     我说了我不懂啊！但现在的情况，很不妙吧！非常有问题啊！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     是不妙啊！你以为什么情况下我才会激动啊！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     想想办法啊！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     我不是在想吗！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]     必须赶紧把这件事告诉博士才行......
[name="普罗旺斯"]     那就拜托你好好想想了，我立刻去发报！可别被热昏头脑！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]     我很冷静。
[Character(name=

... (全文6293字符)
```

### level_act3d0_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第三关（前）
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-720)]
[Delay(time=1)]
[playsound(key="$beach", volume=0.7, channel="B",loop=true)]
[Character(name="char_002_amiya_summer_2#1",fadetime=1,block=true)]
[delay(time=1)]
[name="阿米娅"]   博士，这次我可要批评你了。
[name="阿米娅"]   大家身上都多多少少有些轻伤，作为领队你也有责任的！
[name="阿米娅"]   虽然古米已经给他们处理过了，但是下水的话，还是会影响到伤口的。
[name="阿米娅"]   真是的，带队玩耍也别太过火呀......
[Decision(options="抱歉。;这身泳装很适合你，阿米娅。",values="1;2")]
[Predicate(references="1")]
[Character(name="char_002_amiya_summer_2#1")]
[name="阿米娅"]   唔，我也不是想破坏博士的好心情......
[Predicate(references="2")]
[Character(name="char_002_amiya_summer_2#2")]
[name="阿米娅"]   是、是这样吗？是暴行姐姐给我挑的这件泳装，我还在害怕博士会不会不喜欢——
[Character(name="char_002_amiya_summer_2#1")]
[name="阿米娅"]   等等！不要想着岔开话题，Dr.{@nickname}！
[Decision(options="我们这次可能确实做得有些过火......",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_summer_2#1")]
[name="阿米娅"]   真是的，我也要好好说说赫拉格先生了！
[name="阿米娅"]   明明让他监督你的，结果他也对你们睁一只眼闭一只眼......
[name="阿米娅"]   在没有签订合约前，罗德岛不能插手任何独立城邦的内部问题。
[name="阿米娅"]   要是被卷进城邦本地的麻烦，罗德岛的处境会变得非常艰难，甚至难以脱身。
[Decision(options="其实，我们已经......",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_summer_2#1")]
[name="阿米娅"]   是啊，我知道的。
[name="阿米娅"]   博士可真是做了件很危险的事情。
[Character(name="char_002_amiya_summer_2#2")]
[name="阿米娅"]   ——和狂热的歌迷起冲突什么的！博士好歹要有些大人样子呀。
[name="阿米娅"]   再怎么喜欢一支乐队，也要和其他观众和平相处哦，更别说参与斗殴什么的了！
[Decision(options="......？可我们是......",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_summer_2#2")]
[name="阿米娅"]  （嘘！）
[name="阿米娅"]  总之不要再问啦！整件事就是这样了！嗯！
[name="阿米娅"]  下次可要好好注意哦？
[Decision(options="我知道了。",values="1")]
[Predicate(references="1")]
[Character(name="char_002_amiya_summer_2#2")]
[name="阿米娅"]  嗯！
[name="阿米娅"]  博士，快来吧，我在礁石另一边发现了很多好看的贝壳！海滩什么的，好有趣呀！
[name="阿米娅"]  水不凉，嗯......
[Decision(options="（跟着阿米娅走）;（向阿米娅泼水）;（拉住阿米娅的手）",values="1;2;3")]
[Predicate(references="1")]
[name="阿米娅"]  来，博士，这里走！
[Predicate(references="2")]
[name="阿米娅"]  哎！博士！别这样！
[name="阿米娅"]  可恶！看招！哈哈哈哈......
[Predicate(references="3")]
[name="阿米娅"]  嘿嘿......
[Predicate(references="1;2;3")]
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_024")]
[name="赫尔曼"]   Dr.{@nickname}，你来了。
[name="赫尔曼"]   我听锡兰说了你们罗德岛的事情，我很想跟你聊聊。
[name="赫尔曼"]   如何，就陪我出去走走吧。
[Decision(options="......好的。",values="1")]
[Predicate(references="1")]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_024")]
[name="赫尔曼"]   感谢你，罗德岛的博士。
[name="赫尔曼"]   这次如果没有你的帮助，小女的鲁莽行动恐怕只会惨淡收场。
[Decision(options="那不是鲁莽。;我并没有做太多的事情。;你应该感谢的人是锡兰才对。",values="1;2;3")]
[Predicate(references="1;2;3")]
[name="赫尔曼"]   克洛宁是我一手栽培起来的，他有野心，但也有这个能力，所以我这些年对他的一些小动作总是睁一只眼闭一只眼。
[name="赫尔曼"]   但是，这几年，他有些走偏了，我对他并不放心。
[name="赫尔曼"]   这一次，借着前往新开发区的机会，我留下黑，也是想让她看看这小子还能不能用。
[name="赫尔曼"]   结果很遗憾。
[Decision(options="为什么和我说这些？",values="1")]
[Predicate(references="1")]
[name="赫尔曼"]   ......我很喜欢沿着这片海滩散步。
[name="赫尔曼"]   因为，芭芭拉——我的妻子，她就沉睡在这片海里。
[name="赫尔曼"]   我还记得那一天，天气有点热，夕阳很好，就在这里，她和我说，“要是我们能永远生活在这里就好了”。
[name="赫尔曼"]   转眼，就只留下了我一个人。
[name="赫尔曼"]   博士，回头看看。
[name="赫尔曼"]   你能明白吗？这座城市是我为她打造的天堂。
[name="赫尔曼"]   而我为什么要告诉你这些......
[name="赫尔曼"]   因为我看得出，你和我是同一种人。
[name="赫尔曼"]   这个世界上，有些事不是靠好的那些东西就能解决的，有时候，必须借助一些所谓不好的东西。
[Decision(options="我是。;我不是。;谁知道呢。",values="1;2;3")]
[Predicate(references="1;2;3")]
[name="赫尔曼"]   对我来说，善良与否在很久以前就没有任何意义了，有的只有结果，有的只有这座城市。
[Decision(options="为什么不告诉锡兰？",values="1")]
[Predicate(references="1")]
[name="赫尔曼"]   我不是来寻求理解的，博士。
[name="赫尔曼"]   我如果需要我女儿的理解，我和她就不会是现在这个样子。
[name="赫尔曼"]   而且，告诉了她她就会理解吗？
[name="赫尔曼"]   不会的，她还要很长时间才会理解，这个世界不是她想的那样条理有序。
[name="赫尔曼"]   黑希望她永远不会理解，而我......很遗憾，我失去了选择的机会。
[name="赫尔曼"]   博士，锡兰她想要加入你们，我让黑和她一起去，这些我都允许。
[name="赫尔曼"]   因为这座汐斯塔已经不再是她的天堂了。
[name="赫尔曼"]   我已经看过新的地质报表了。照这样下去，汐斯塔迟早会在迸发的岩浆中落下帷幕。
[name="赫尔曼"]   我们推迟了那一天的到来。对你们今天的努力，我表示感激。
[name="赫尔曼"]   这些年来我一直在寻找彻底解决这件事的办法。我找到了，但代价也很一样巨大。
[name="赫尔曼"]   我一直投入精力的高新区，那将会是一座全新的移动城市，现在看来，那将会成为新的汐斯塔。
[name="赫尔曼"]   我对这里的执着很深，但这并不意味着我会对身旁浅睡的火山熟视无睹。
[name="赫尔曼"]   这次黑曜石节结束后，我们将迁进移动城市；现在的汐斯塔城将会被我们抛弃，迟早淹没在滚热的岩浆中。
[Decision(options="那黑曜石节......",values="1")]
[Predicate(references="1")]
[name="赫尔曼"]   据说这片海洋有着它的边界。也有人对我说过，这里不是真正的大海，它的边界也许宽广，却有尽头。
[name="赫尔曼"]   那么我们会环着这片海走下去。或许有一天，我们会真正回到起点。
[name="赫尔曼"]   只是，这座有着美丽海滩和盛大的黑曜石节，以及这座能感受到火山气息的海滨城市本身——
[name="赫尔曼"]   这座有着无数汐斯塔人回忆的汐斯塔，终究是不复存在了。
[name="赫尔曼"]   也许有一天，你可以把我说的这些告诉她。
[name="赫尔曼"]   你也可以永远都不告诉她。
[name="赫尔曼"]   而有一天，当她需要一些帮助时，你可以来找我。
[name="赫尔曼"]   无论汐斯塔在哪里，变换成何种模样，这座城市，永远会是她的后盾。
[name="赫尔曼"]   不——该这么说。只要汐斯塔人还在，汐斯塔就永远在。她们这些年轻人才是真正的汐斯塔。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0.5, block=true)]
[Character]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="avg_npc_024")]
[name="赫尔曼"]   趁现在，好好享受这次的黑曜石节吧。
[name="赫尔曼"]   至少在找到新的理想场地之前，我们只能搁置和塞壬唱片之间的合作啦。我该去和他们好好谈谈了。
[name="赫尔曼"]   黑似乎也有话想跟你说，她在那边。
[name="赫尔曼"]   如果我说太多，她就更没话可说了。让她自己和你说吧。
[Dialog]
[Character]
[Character(name="char_340_shwaz_2#3",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=1)]
[name="黑"]   ......老爷。
[Character(name="avg_npc_024")]
[name="赫尔曼"]   别介意。之后是你们年轻人的事情了。
[Character]
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_340_shwaz_2#1")]
[name="黑"]   你好。
[Decision(options="你的目的是什么？;你好，陌生人？;要不要喝一杯？",values="1;2;3")]
[Predicate(references="1")]
[name="黑"]   不用紧张，我已经不是你的敌人了。
[Predicate(references="2")]
[Character(name="char_340_shwaz_2#1")]
[name="黑"]   呵，你好，陌生人。
[Predicate(references="3")]
[name="黑"]   现在就免了。
[Predicate(references="1;2;3")]
[name="黑"]   其实，也没有什么特别的。
[name="黑"]   原本我是想教训你一顿的。小姐不该遇到这种危险。
[name="黑"]   但我也要谢谢你。没有你，我和小姐也许永远没法解开误会。

... (全文8294字符)
```

### ui_act3d0_campselect

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Character]
[Dialog]
[Image(image="ac3_title1", fadetime=1)]
[ImageTween(xScaleTo=1.1, yScaleTo=1.1, duration=6)]
[PlayMusic(intro="$fesmetal_intro", key="$fesmetal_loop", volume=0.6, crossfade=1.5)]
[Delay(time=2)]
[Background(image="bg_Festival_2", fadetime=3)]
[name="主持人"]   欢迎你们来到一年一度的汐斯塔黑曜石节！
[name="主持人"]   汐斯塔！让我听到你们的声音！！
[Image(fadetime=1)]
[Character]
[CameraShake(duration=2, xstrength=8, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="观众"]   （狂热的欢呼声）
[Character(name="avg_npc_017_3#4",fadetime=1, block=true)]
[name="主持人"]   无论你是什么种族，从哪个城市来，从今天开始，抛弃自己的身份，忘掉所有的烦恼！
[name="主持人"]   黑曜石节日需要的是每一个人的参与！！融入！！
[name="主持人"]   把你们每个人的手都举到最高，让我能看到你们每一个人！
[Character]
[PlaySound(key="$livecrowd", volume=0.5, loop=false, channel="people")]
[CameraShake(duration=2, xstrength=12, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="观众"]   （狂热的欢呼声）
[Character(name="avg_npc_017_3#4")]
[name="主持人"]   老规矩，今年我们也会选出我们黑曜石节的最受欢迎艺人！！
[name="主持人"]   所以，在狂欢之余，也别忘了给自己最喜欢的音乐艺人进行<color=#ee4321>投票</color>。
[name="主持人"]   注意！你<color=#ee4321>只有一次机会</color>做出选择，选择的结果将不会有机会做变更。
[name="主持人"]   但是也请不要担心，投票结果的高低都<color=#ee4321>不会影响</color>大家获得的奖励！
[name="主持人"]   只要你做出了选择并<color=#ee4321>完成了所有里程碑任务</color>，你将获得相应的里程碑奖励！
[PlaySound(key="$livecrowd", volume=0.6, loop=false, channel="people")]
[Character]
[CameraShake(duration=3, xstrength=15, ystrength=13, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="观众"]   噢噢噢噢噢噢！
[Character(name="avg_npc_017_3#4")]
[name="主持人"]   所以，请不要犹豫，为你最喜欢的艺人投上宝贵的一票吧！
[name="主持人"]   那么接下来，做出你的选择！！告诉我，你最爱的音乐艺人到底在哪里！！
[Dialog]
[Blocker(block=true)]
[Image]
```


## 统计

- 总字符数：135448
- 对话行数：1353


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
