# 明日方舟 · 活动剧情 · act45side（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act45side」完整剧情脚本（23个文件，1877行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act45side
- 脚本文件数：23

### level_act45side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="25_mini02_victoria_street_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>维多利亚偏僻小镇</><p=2>9:37 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.6)]
[PlaySound(key="$d_avg_runstop", volume=1,delay=1.5)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_338_iris_1#5$1",posfrom="200,0",posto="0,0",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_338_iris_1#5$1",focus="m")]
[name="爱丽丝"]比之前预计的时间晚了整整四个小时......
[name="爱丽丝"]没有多少时间了......
[charslot(slot="m",name="avg_369_bena_1#3$1",focus="m")]
[name="贝娜"]街上完全没有人，这种地方也不可能有地图......这下麻烦了。
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]不如我们分头去找，有情况就用通讯器联络。
[charslot(slot="m",name="avg_369_bena_1#11$1",focus="m")]
[name="贝娜"]是个不错的主意......
[charslot(slot="m",name="avg_290_vigna_1#6$1",focus="m")]
[name="红豆"]等等，其他人我都没有意见......
[name="红豆"]但祥子你没有单独行动的经验，我不会让你一个人去的。
[charslot(slot="m",name="avg_4182_oblvns_1#9$2",focus="m")]
[name="丰川祥子"]现在不是考虑这种事情的时候吧？
[name="丰川祥子"]她信里不是已经写了，“这是我的最后一封信。”
[charslot(slot="m",name="avg_4182_oblvns_1#7$2",focus="m")]
[name="丰川祥子"]万一出现什么意外，那个少女......
[charslot(slot="m",name="avg_290_vigna_1#6$1",focus="m")]
[name="红豆"]可是......！
[dialog]
[charslot(slot="m",name="avg_4182_oblvns_1#1$2",focus="m")]
[PlaySound(key="$d_avg_slapcloth_light", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#1$2",focus="m")]
[name="丰川祥子"]......红豆，没事的。
[name="丰川祥子"]鞭刃小姐不是说过吗，以我现在的能力，我已经可以加入行动小组了。
[name="丰川祥子"]（拿出通讯器）要是遇到麻烦，我一定第一时间联系你，好吗？
[charslot(slot="m",name="avg_369_bena_1#1$1",focus="m")]
[name="贝娜"]嗯，还有我们呢！
[charslot(slot="m",name="avg_290_vigna_1#1$1",focus="m")]
[name="红豆"]......好吧。那你一定要小心。
[charslot(slot="m",name="avg_4182_oblvns_1#1$2",focus="m")]
[name="丰川祥子"]嗯。爱丽丝小姐，那个孩子的名字和地址是？
[charslot(slot="m",name="avg_338_iris_1#9$1",focus="m")]
[name="爱丽丝"]她叫“安”......地址是“花园街33号”。
[charslot(slot="m",name="avg_4182_oblvns_1#1$2",focus="m")]
[name="丰川祥子"]好。那我们就从这个十字路口开始，分头去找吧！
[dialog]
[charslot(duration=0.5)]
[Delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=0.7)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="step1")]
[PlaySound(key="$d_avg_keeprunning",volume=1,channel="step2",loop=true,delay=0.2)]
[PlaySound(key="$d_avg_openftstprun", volume=0.8, loop=true, channel="step3",delay=0.5)]
[stopsound(channel="step1",fadetime=2.5)]
[StopSound(channel="step2", fadetime=2)]
[StopSound(channel="step3", fadetime=3.5)]
[Delay(time=2.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="25_mini02_victoria_street_n",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="a")]
[stopsound(channel="a",fadetime=2.5)]
[delay(time=2)]
[name="丰川祥子"]呼——呼——怎么这里的路都这么复杂？
[name="丰川祥子"]那边好像有个人......在卖花？
[multiline(name="丰川祥子")]为什么这个时间了还有人在卖花......
[multiline(name="丰川祥子")]不管了，找人要紧！
[name="丰川祥子"]您好——！
[Dialog]
[stopSound(channel="a", fadetime=1)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]您好，请问您知道花园街在哪吗？
[charslot(slot="m",name="avg_npc_1255_1#1$1",focus="m")]
[name="卖花的妇人"]这里就是花园街。小姑娘，你要买花吗？
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]不，我不买花......请问您知道花园街33号怎么走吗？
[charslot(slot="m",name="avg_npc_1255_1#1$1",focus="m")]
[name="卖花的妇人"]你抬头看看天上，朝着夕阳，往西边一直走到巷尾，最后那家就是33号了。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]老奶奶，现在已经是晚上了......
[charslot(slot="m",name="avg_npc_1255_1#1$1",focus="m")]
[name="卖花的妇人"]唔，我真是老糊涂了......我说怎么这路上一点脚步声都没有，我也该收摊回家了。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]您看不见吗......？
[charslot(slot="m",name="avg_npc_1255_1#1$1",focus="m")]
[name="卖花的妇人"]不用管我，你不是还在找地方吗？快去吧。
[name="卖花的妇人"]夜黑灯暗，可不要再迷路了。
[charslot(slot="m",name="avg_4182_oblvns_1#1$2",focus="m")]
[name="丰川祥子"]谢谢......您也注意安全。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="25_mini02_victoria_street_n",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[charslot]
[animtext(id = "at1", name = "group_location_stamp", style="avg_only_heavy", pos = "-400,-200", block = false)]<p=1>花园街33号</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]往西边一直走......这里就是那个老奶奶说的地方了。
[charslot]
[dialog]
[delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Background(image="bg_snowconutryinside",screenadapt="coverall", fadetime=1.5,block=true)]
[Delay(time=1)]
祥子缓缓推开破旧的木门，门框发出尖锐的吱呀声。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]唔......好大的酒味？！
[dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_npc_416_1#1$1",duration=1)]
[Delay(time=2)]
[charslot]
地板上满是带着泥水的鞋印，而房间的尽头是一个穿着邋遢的男人。
男人环顾四周，接着一个个地拿起角落里摆放整齐的酒瓶。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="醉酒的男人"]空的......
[dialog]
[PlaySound(key="$bottlebroken", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="醉酒的男人"]空的......
[dialog]
[PlaySound(key="$bottlebroken", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name

... (全文23331字符)
```

### level_act45side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Subtitle(text="<i>童话书里说，在维多利亚的某处，矗立着一座只有孩子才能看见的城堡。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>城堡里住着几位善良的仙女，她们会定期举办宴会招待孩子们，并用美梦一一实现他们的愿望。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>可具体说起“梦城堡”究竟是何种模样，却没有一个孩子能答得上来。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>精心塑造的美梦，从孩子们离开梦境的那一刻起，就在不断地被淡忘。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>美梦不断被塑造，然后又不断被遗忘。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>重复塑造，重复遗忘。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>这一切对于善良而忙碌的仙女们来说，是不是有些过于不公平了？</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>“是的，莫菲丝。”</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g2_dreamcastlehall", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1942_1#18$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="？？？"]欢迎来到梦城堡，我是这里的现任主人，莫菲丝。
[charslot(slot="m",name="avg_4182_oblvns_1#9$1",focus="m")]
[name="丰川祥子"]梦城堡......的主人......不对，你做了什么？！
[charslot(slot="m",name="avg_npc_1942_1#20$1",focus="m")]
[name="莫菲丝"]和你梦里演的一样啊？只不过是让你们做了一个梦罢了。
[charslot(slot="m",name="avg_npc_1942_1#17$1",focus="m")]
[name="莫菲丝"]唉——不过你的梦实在太无趣了，尽是些无聊的东西。
[charslot(slot="m",name="avg_npc_1942_1#16$1",focus="m")]
[name="莫菲丝"]（小声）还有那两个......讨厌的家伙。
[charslot(slot="m",name="avg_4182_oblvns_1#14$1",focus="m")]
[name="丰川祥子"]你认识爱丽丝......还有贝娜？
[charslot(slot="m",name="avg_npc_1942_1#17$1",focus="m")]
[name="莫菲丝"]不熟。
[charslot(slot="m",name="avg_4182_oblvns_1#14$1",focus="m")]
[name="丰川祥子"]她们不是梦里的角色，是真实存在的人？
[charslot(slot="m",name="avg_npc_1942_1#17$1",focus="m")]
[name="莫菲丝"]我倒希望她们只存在在梦里。
[charslot(slot="m",name="avg_npc_1942_1#9$1",focus="m")]
[name="莫菲丝"]你能不能别老提那两个家伙。
[charslot(slot="m",name="avg_npc_1942_1#10$1",focus="m")]
[name="莫菲丝"]你在和我说话欸！现在我才是这里的主人！
[charslot(slot="m",name="avg_4182_oblvns_1#9$1",focus="m")]
[name="丰川祥子"]快让我离开这里。
[charslot(slot="m",name="avg_npc_1942_1#17$1",focus="m")]
[name="莫菲丝"]那不可能。
[charslot(slot="m",name="avg_npc_1942_1#15$1",focus="m")]
[name="莫菲丝"]最近都没什么孩子来梦城堡了，我怎么可能随便放你走？
[name="莫菲丝"]卡尔顿们又不能说话，沃尔夫只有一个，而且现在说话还说不顺溜。
[charslot(slot="m",name="avg_npc_1937_1#5$1",focus="m")]
[PlaySound(key="$d_avg_yingying_ked_2", volume=1)]
[name="卡尔顿们"]（失落的哼唧声）
[charslot(slot="m",name="avg_npc_1938_1#2$1",focus="m")]
[name="沃尔夫"]抱、抱歉。
[charslot(slot="m",name="avg_4182_oblvns_1#9$1",focus="m")]
[name="丰川祥子"]你是因为自己太无聊了，所以才把我关在这个城堡里的吗？
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]不要说得好像我来者不拒一样。
[charslot(slot="m",name="avg_npc_1942_1#20$1",focus="m")]
[name="莫菲丝"]你的经历都很有意思——记忆里的那些经历，还有那些陌生的场景，我反复研究了很多遍呢。
[charslot(slot="m",name="avg_4182_oblvns_1#9$1",focus="m")]
[name="丰川祥子"]你偷看了我的记忆？
[charslot(slot="m",name="avg_npc_1942_1#20$1",focus="m")]
[name="莫菲丝"]那个家伙没有和你说过吗？了解孩子们的过去，也是塑造梦境很重要的一部分。
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]但你确实是个例外......
[name="莫菲丝"]明明经历了那么多无法忘却的事情，脑子却还是一如既往地清醒。
[name="莫菲丝"]为了弥补这个小小的遗憾，我愿意为你重新塑造一个美梦。正好我们现在面对面，你可以和我说说——
[charslot(slot="m",name="avg_4182_oblvns_1#9$1",focus="m")]
[name="丰川祥子"]沉溺在梦境和过往的痛苦中，都是懦弱的表现。
[charslot(slot="m",name="avg_npc_1942_1#20$1",focus="m")]
[name="莫菲丝"]呵，你还真是嘴硬！
[name="莫菲丝"]如果按照你说的，没法直面现实的人全都是懦夫的话......
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]那这样的人，真的很多呢。
[stopmusic(fadetime=1.5)]
[Dialog]
[PlaySound(key="$d_avg_snapping", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background]
[Image(image="65_i02_2",screenadapt="coverall",block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_craneworking", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=2)]
帷幕渐渐拉开，座椅从台下缓缓升起。
而座椅上坐着的，是祥子再熟悉不过的人。
[playMusic(key="$darkness_03_loop", volume=0.6)]
[name="丰川祥子"]初华......睦？
[name="丰川祥子"]祐天寺......还有八幡？
[name="丰川祥子"]......大家怎么都睡着了？
周围的一切如舞台布景一般。
沉睡的少女们，就是巨大布景中安眠的人偶。
无声，无息。
祥子一遍遍地尝试唤醒自己的同伴，可无济于事。
[Dialog]
[name="莫菲丝"]别白费力气了——没用的。
[Dialog]
[Image(image="65_i02_1",screenadapt="coverall",fadetime=2.5,block=false)]
[Delay(time=1)]
[name="莫菲丝"]我对自己的能力还是很有信心的。她们正沉浸在自己的美梦里，你叫不醒她们的。
[name="莫菲丝"]在我为你们塑造的梦境里有什么不好？
[name="莫菲丝"]罗德岛的朋友们都相信你，这样不好吗？没有任何你不想看到的别离，你也不用隐藏自己 。
[name="莫菲丝"]看看她们，难道你要说她们都是懦夫吗？
[name="丰川祥子"]既然我有办法从你的梦中醒来，她们也一定可以......
[Dialog]
[PlaySound(key="$d_avg_strngspllstght", volume=1, loop=true, channel="s")]
[StopSound(channel="s", fadetime=3)]
[Delay(time=2)]
突然，祥子感到几股巨大的拉力拽住了自己，等她反应过来时，她的四肢已经被丝线牢牢捆住。
无法控制身体的紧张感瞬间侵占了她的思维，她努力地想要保持冷静。
然而，紧绷的丝线将她身上一切微弱的抖动毫无保留地放大。
[name="莫菲丝"]你这嘴硬的家伙，就不能承认梦境是美好的吗！
[name="丰川祥子"]你......
祥子努力想办法让自己的呼吸变得平顺。
[name="丰川祥子"]你......似乎对自己的能力很自信。
[name="丰川祥子"]也许在我之前，你的梦境从没有被人打破过。
[name="莫菲丝"]当然！我本来就是这个城堡里最擅长造梦的仙女。
[name="莫菲丝"]你的苏醒，只不过是一个意外。再来一次肯定就没问题了！
祥子清楚地看到，莫菲丝说出最后那几个字时，表情是咬牙切齿的，可转眼间，她的表情又变得无比天真灿烂。
[name="莫菲丝"]嗯......丰川祥子，对吧？
[name="莫菲丝"]既然你这么自信，那我就跟你打个赌！
[name="丰川祥子"]......打赌？
[name="莫菲丝"]嗯！绝对公平的打赌哦！
[name="丰川祥子"]......
眼前的对手越是露出孩童般的微笑，就越显得无比危险。
[name="莫菲丝"]哈哈，很简单！
虽然那孩子绕着舞台转着圈，但祥子很清楚她肯定一直在盯着自己。并且，黑暗中还有无数双眼睛也在紧盯着自己。
[name="莫菲丝"]我会邀请你进入她们每一个人的梦境，给你唤醒她们的机会。
[name="莫菲丝"]你可以认识她们，了解她们，看看她们到底在梦境中过着怎样的生活。如果你能让她们像你一样醒来，我就让你们离开。


... (全文15175字符)
```

### level_act45side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g10_dreamcastlestage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Subtitle(text="<i>数千数万双眼睛之下，如人偶一般，动弹不得。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>去到他们要求我去往之处，发出他们期望我发出之声。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我，毋畏爱意。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_wilderness_m", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4185_amoris_1#3$2",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4185_amoris_1#3$2",focus="m")]
[name="迷途的少女"]已经两天两夜没有见到人烟了......
[name="迷途的少女"]龙门......龙门究竟在哪里？家在哪里？
[name="迷途的少女"]爸爸，妈妈......我好渴......好累......
[name="迷途的少女"]远处的......是高楼吗？
[charslot(slot="m",name="avg_4185_amoris_1#1$2",focus="m")]
[name="迷途的少女"]快要到了......还不能睡......
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(duration=1)]
[Delay(time=1.5)]
[name="迷途的少女"]......
[Dialog]
[Delay(time=1)]
[name="？？？"]咔！
[Dialog]
[Delay(time=1)]
[Background(image="65_g7_filmandtvstudio", screenadapt="coverall",fadetime=1.5, block=true)]
[Delay(time=1)]
[playMusic(key="$comedy_loop", volume=0.6)]
[name="导演"]太精彩了，若麦小姐！我心里所想的，完全就是这个感觉！
[name="导演"]平凡的乡村少女决然抛下所有，踏上了追寻音乐梦想的旅程。
[name="导演"]这场戏拍的就是她的至暗时刻，从此以后，她便会遇到赏识自己的贵人，成为龙门最受欢迎的乐手。
[charslot(slot="m",name="avg_4185_amoris_1#8$3",focus="m")]
[name="祐天寺若麦"]谢谢导演夸奖~
[name="祐天寺若麦"]在看这个剧本的时候，我意外地很能理解女主角的心境。
[Dialog]
[charslot]
[name="导演"]那当然！这个剧本、这个角色就是为若麦小姐你量身定制的啊！
[name="编剧"]*尚蜀方言*明明是为了抢新年档期，临时修改的剧本......
[charslot(slot="m",name="avg_4185_amoris_1#1$3",focus="m")]
[name="祐天寺若麦"]嗯......？
[Dialog]
[charslot]
[name="编剧"]投资方眼红《少女鼓手》大卖，指定由你来主演我们这部电影。
[name="编剧"]然后你的经纪公司要求电影必须在新年档上映，导演逼着我一周内改完剧本......
[name="编剧"]原本的结局......应该是少女在弥留之际，做了一个似真似幻的梦。
[name="编剧"]在一片眩光中，资质平平的少女晃晃悠悠地走上了领奖台。
[name="编剧"]平凡的少女在梦里赢得了所有人的认可，也终于和一切达成了和解。
[name="编剧"]这才是这个片子应该有的具有讽刺意味的结局啊！
[name="导演"]*龙门粗口*，你那破本子，要是没若麦小姐的加持，能拿到这种级别的资源？
[name="编剧"]谁稀罕你的那些资源？我看你就是捧投资方捧惯了，忘记了自己的艺术追求！
[name="编剧"]现实里哪有那么美好的事情，普通人怎么可能有机会走到万众瞩目的台前？！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="编剧"]*尚蜀方言*你不是乡下出身，当然不会懂啊！但我是，我懂啊！
[name="导演"]臭码字的，看我怎么收拾你——
[Dialog]
[PlaySound(key="$d_avg_punchsp5")]
[PlaySound(key="$d_avg_punch02",delay=0.4)]
[PlaySound(key="$fightgeneral", volume=0.6,delay=0.7)]
[CameraShake(duration=1.5, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2)]
言语的交锋之间，两人的距离越来越近，口舌之争最终演变成了拳脚角力。
[charslot(slot="m",name="avg_4185_amoris_1#3$4",focus="m")]
[name="祐天寺若麦"]你们有话好好说......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_punch02")] 
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.5)]
[name="编剧"]你拍的那些破镜头，我早*尚蜀粗口*就想吐槽了！
[name="导演"]你等着，等这次我飞黄腾达，*龙门粗口*第一个就把你踢了！
[Dialog]
[PlaySound(key="$d_avg_punch", volume=0.6)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4185_amoris_1#4$3",focus="m")]
[name="祐天寺若麦"]哈？不是——！
[Dialog]
[charslot(duration=0.5)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="c")]
[SoundVolume(volume=0.5, channel="c",fadetime=1)]
[Delay(time=2)]
[Dialog]
[stopmusic(fadetime=2)]
[stopsound(channel="c", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_deluxeroom", screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1260_1#1$1",focus="m")]
[name="助理"]医院那边来消息了，编剧和导演被分到同一个病房，两个人正好对床。
[name="助理"]不过好在都上了护颈，现在两个人只能互相干瞪眼。
[name="助理"]麻烦的是，这戏短时间内应该是拍不了了......
[charslot(slot="m",name="avg_4185_amoris_1#1$3",focus="m")]
[name="祐天寺若麦"]反正最近都没有好好休息过，现在这样说不定还正好~
[charslot(slot="m",name="avg_npc_1260_1#1$1",focus="m")]
[name="助理"]等后续的拍摄计划确定后我会再联系你，这段时间要麻烦你先维持随时待命的状态了。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4185_amoris_1#2$3",focus="m")]
[name="祐天寺若麦"]（小声）唉，不知道为什么，总感觉轻松一点了......
[charslot(slot="m",name="avg_4185_amoris_1#7$3",focus="m")]
[name="祐天寺若麦"]不行不行，还不能放松下来——
[Dialog]
[charslot(slot="m",name="avg_4185_amoris_1#7$3",focus="n")]
[PlaySound(key="$phonevibration",volume=0.8)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4185_amoris_1#3$4",focus="m")]
[name="祐天寺若麦"]妈妈......？
[Dialog]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="nw")]
[stopsound(fadetime=3, channel="nw")]
[charslot(duration=1)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_trnpndor", volume=0.7)]
[Delay(time=1)]
[Background(image="bg_rooftop_2",screenadapt="coverall", fadetime=1,block=true)]
[Delay(time=1)]
少女拿起电话，推开滑门，走到了阳台上。
[name="电话里的声音"]*方言*若麦，吃过晚饭了没？最近忙不忙呀？
[charslot(slot="m",name="avg_4185_amoris_1#1$3",focus="m")]
[name="祐天寺若麦"]*方言*吃过啦。
[charslot(slot="m",name="avg_4185_amoris_1#1$3",focus="n")]
[name="电话里的声音"]*方言*最近家里的麦子又丰收了，我们每天一大早就要出门，得忙到太阳落山才能做完。
[charslot(slot="m",name="avg_4185_amoris_1#8$3",focus="m")]
[name="祐天寺若麦"]*方言*唉，不是早就说过了吗？你们就好好在乡下享福吧。
[charslot(slot="m",name="avg_4185_amoris_

... (全文10027字符)
```

### level_act45side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g8_interviewstage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[name="主持人"]各位观众朋友们好！下面让我们有请今天的人气嘉宾——空小姐！
[Dialog]
[charslot(slot = "l", name = "char_101_sora_1#6",duration=0.7)]
[delay(time=1)]
[PlaySound(key="$d_avg_takphtrptly",volume=0.7)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot(duration=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot(slot="r",name="char_101_sora_1#6",posfrom="-50,0", posto="-50,0",duration=0,isblock=true)]
[charslot(duration=0.2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot(slot="m",name="char_101_sora_1#6",duration=0,isblock=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="char_101_sora_1#6",focus="m")]
[name="空"]左边的朋友——右边的朋友——还有中间的朋友！
[name="空"]嗨！我是来自塞壬唱片的，大家的偶像空~！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_cheer_street", volume=0.4)]
[delay(time=2)]
[name="主持人"]大家的热情都很高涨啊！！
[charslot(slot="m",name="char_101_sora_1#1",focus="m")]
[name="空"]有这么多人喜欢我，我真的很开心！
[name="空"]不过我想，肯定也有很多人是因为临时官宣的另一位嘉宾而欢呼，她同样也是我的偶像哦！
[Dialog]
[charslot(slot="m",name="char_101_sora_1#1",focus="n")]
[PlaySound(key="$d_avg_crwdcheerup", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="char_101_sora_1#3",focus="m")]
[multiline(name="空")]唔，大家已经等不及了吗？
[charslot(slot="m",name="char_101_sora_1#1",focus="m")]
[multiline(name="空")]那就让我们欢迎——若麦小姐！
[Dialog]
[charslot(duration=0.3)]
[Delay(time=0.8)]
[charslot(slot="m",name="avg_4185_amoris_1#5$3",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4185_amoris_1#5$3",focus="m")]
[name="祐天寺若麦"]晚上好喵呣喵呣~~
[name="祐天寺若麦"]粉丝朋友们好呀，我是若麦~见到大家我太开心了！
[Dialog]
[PlaySound(key="$d_avg_cheer_street", volume=0.8)]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="in")]
[SoundVolume(volume=0.4, channel="in",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_020",focus="m")]
[name="忙碌的保安"]有入场凭证的才能进场！
[name="忙碌的保安"]无关人士都往外面站，不要拥挤！
[name="忙碌的保安"]*龙门粗口*，人太多了，根本管不过来啊！
[charslot(slot="m",name="avg_npc_033",focus="m")]
[name="激动的粉丝"]空小姐......若麦小姐！我爱你们啊！！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.6)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_020",focus="m")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="忙碌的保安"]喂，那个人冲进去了——快拦住他！
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot = "l", name = "avg_npc_020",duration=0.3)]
[charslot(slot = "r", name = "avg_npc_020",duration=0.3)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_crowdrun", volume=1)]
[charslot(duration=1)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]......这里已经完全一团乱了。
[name="丰川祥子"]人实在太多了。
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]......完全没有混进去的可能。
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="n")]
[name="？？？"]小姑娘，想进场看大明星吗？
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]欸？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]你喜欢哪个？空，还是若麦？
[name="奇怪的男人"]我有办法带你进去，亲眼见到本人哦。
[charslot(slot="m",name="avg_4182_oblvns_1#9$2",focus="m")]
[name="丰川祥子"]......你为什么要帮我？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]哎，别这么紧张嘛~
[name="奇怪的男人"]我要价也不高......喏，这个数。
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]......我给不起。
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]哎，这价格已经很低了啊！你可别想着再砍一刀！
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]就算你这么说......
[Dialog]
[PlaySound(key="$d_avg_pcket", volume=1)]
[delay(time=1)]
[name="丰川祥子"]（虽然这个男人看着就很可疑，但是现在也没什么别的更好的办法了，如果错过这次机会......）
[name="丰川祥子"]（只能先相信他了。）
[name="丰川祥子"]（翻找口袋）
[name="丰川祥子"]一共只有这么多......这是我身上全部的钱，你看行不行？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]也成！跟我来吧！
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[delay(time=0.2)]
[charslot(duration=0.7)]
[delay(time=1)]
[Dialog]
[StopSound(channel="in", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_indoor_3",screenadapt="coverall",block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]员工专用通道......？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]嗯，咱们就从这里进。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]入场凭证呢？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]没有啊。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]那你是内部人员？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]不是啊。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]那我们怎么进去？要是被发现了怎么办？！
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]我和你说了我有办法啦！你到底想不想见到明星？
[charslot(slot="m",name="avg_npc_305_1#1$1",focus="m")]
[name="奇怪的男人"]（小声）*龙门粗口*，声音太大了......
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slo

... (全文22050字符)
```

### level_act45side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g10_dreamcastlestage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Subtitle(text="<i>大雨如泪水一般落下，我只是无垠海水中的一滴。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>独行的夜，不再迷茫。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我，毋畏恐惧。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cellroomC", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[PlayMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_dooropen", volume=0.4)]
[Delay(time=1)]
[name="狱警"]犯人48038，出来。
[name="激动的犯人"]长官，您有什么吩咐？
[name="狱警"]检查个人物品，有没有遗漏？
[name="激动的犯人"]没有，东西我都带齐了！
[name="狱警"]沿着走廊往前面走，走到尽头的那个小窗，签个字离开就行了。
[name="激动的犯人"]好、好的，谢谢长官！
[Dialog]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="a")]
[PlaySound(key="$d_gen_walk_n", volume=1,delay=1.5)]
[StopSound(channel="a", fadetime=4)]
[Delay(time=2.5)]
有力的小跑声在长廊上回荡。
而沉闷的皮靴声则一点点向走廊的最深处靠近。
[Dialog]
[charslot(slot = "m", name = "avg_npc_134",duration=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_134",focus="m")]
[name="狱警"]海铃。
[Dialog]
[charslot]
[delay(time=0.5)]
[charslot(slot="m",name="avg_4186_tmoris_1#1$3",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4186_tmoris_1#1$3",focus="m")]
[name="八幡海铃"]在。
[charslot(slot = "m", name = "avg_npc_134",focus="m")]
[name="狱警"]滚吧，今年别让我再看到你。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_dooropen", volume=0.8)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4186_tmoris_1#1$3",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=4)]
[charslot(duration=1)]
[Delay(time=2)]
海铃熟练地拿起自己的琴盒，慢悠悠地走出了监狱。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g6_newtown_street", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_rainlight_loop", volume=0, loop=true, channel="c")]
[SoundVolume(volume=1, channel="c",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
叙拉古还是和从前一样，用连绵的小雨迎接她的回归。
[Dialog]
[stopsound(channel="c", fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g10_smallrestaurant", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crowdrun",volume=0.8)] 
[charslot(slot="l",name="avg_npc_698_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_699_1#1$1",duration=1)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_npc_698_1#1$1",focus="l")]
[name="领头的打手"]这条街，还有前后两条街，每家店都派人盯着，绝对不能让她跑了！
[charslot(slot="r",name="avg_npc_699_1#1$1",focus="r")]
[name="谨慎的打手"]是！
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_699_1#1$1",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="m",name="avg_npc_699_1#1$1",focus="m")]
[name="慌张的打手"]大哥，北街那边传来消息，她朝这边过来了！
[charslot]
[charslot(slot="r",name="avg_npc_698_1#1$1",focus="r")]
[charslot(slot="l",name="avg_npc_699_1#1$1",focus="r")]
[charslot(slot="l",name="avg_npc_699_1#1$1",focus="r")]
[name="领头的打手"]盯紧她，别让她跑了！
[charslot(slot="l",name="avg_npc_699_1#1$1",focus="l")]
[name="慌张的打手"]她......她好像没有要躲的意思。
[charslot(slot="r",name="avg_npc_698_1#1$1",focus="r")]
[name="领头的打手"]......让其他人都聚过来！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g2_srcalley", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_rainlight_loop", volume=0, loop=true, channel="d")]
[SoundVolume(volume=1, channel="d",fadetime=2)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
狭窄的胡同里，一群凶神恶煞的打手，正将提着琴盒的少女团团围住。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="领头的打手"]又见面了......海铃。
[name="领头的打手"]呵，我一开始还在想，你这种高手，怎么没有一个家族把你纳入麾下。
[name="领头的打手"]我们家族遭难后，四处打听，才知道你原来是个臭名昭著的“叛徒”。
[name="领头的打手"]你前后换过十几个名字，在各个家族间来回接活。
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="m")]
[name="八幡海铃"]我们的合同里没有写我不能替别人干活。
[name="八幡海铃"]而且我早就说过——我只是拿人钱财，替人消灾。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[CameraShake(duration=0.3, xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="领头的打手"]所以你就把我们的机密告诉了对家？！
[charslot(slot="m",name="avg_4186_tmoris_1#12$3",focus="m")]
[name="八幡海铃"]......我不懂你在说什么。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="领头的打手"]*哥伦比亚粗口*，别装傻了！自从你来过后，我们的人就不断遭到暗算！
[name="领头的打手"]亏我和老大当时那么信任你，还邀请你加入我们！
[charslot(slot="m",name="avg_4186_tmoris_1#7$3",focus="m")]
[name="八幡海铃"]弗朗西斯，我不记得我有做过什么对不起你们的事......
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]哼，是你亏欠的人实在太多，想都想不起来了吧？！
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="弗朗西斯"]老大死了，大家都死了，几百号人现在只剩我们十几个了！
[charslot(slot="m",name="avg_4186_tmoris_1#7$3",focus="m")]
[name="八幡海铃"]......什么意思？
[charslot(slot="m",name

... (全文14205字符)
```

### level_act45side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
一开始，我只当作接到了一份再普通不过的工作。
一个籍籍无名的小家族需要我的力量，以便在风雨飘摇的叙拉古站稳脚跟。
可随着日子一天天过去，他们越来越信任我，甚至带我参加家族的核心会议。
我明知这不符合最开始合同上的条款，却又很享受待在这些人中的感觉。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="33_g10_smallrestaurant",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]哟！海铃小妹，好几天不见了，你还好吗？
[name="弗朗西斯"]喏，橘子味奶冻。我没记错的话，你是喜欢这个口味吧？
[charslot(slot="m",name="avg_4186_tmoris_1#1$3",focus="m")]
[name="八幡海铃"]不用，我自己有。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]*哥伦比亚粗口*，别那么不领情啊！
[name="弗朗西斯"]我是听说你单枪匹马，把之前骚扰我们的那帮家伙赶走了，想感谢感谢你啊！
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="m")]
[name="八幡海铃"]离我远点。我只是个拿钱办事的打手，干完这票就会离开。
[name="八幡海铃"]要是等会你们老大看到我们两个混在一起，你肯定没好下场。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]没关系啦，老大上次和我说了，他早就想邀请你加入我们......
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="m")]
[name="八幡海铃"]......建议你们还是在叙拉古多打听打听我的名声吧。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]不需要打听，你已经是我们见过的最强的人了！
[name="弗朗西斯"]要我说，你不如现在就答应得了。今晚家族聚餐，一起去啊——
[charslot(slot="m",name="avg_4186_tmoris_1#12$3",focus="m")]
[name="八幡海铃"]与其说是家族聚餐，不如说是乐队表演吧......
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]哎，我们家族虽然势力小了点，但成员之间的情谊是别人比不了的啊！
[name="弗朗西斯"]况且你不是和我们一起表演了很多次吗，大家都很默契了啊。
[charslot(slot="m",name="avg_4186_tmoris_1#3$3",focus="m")]
[name="八幡海铃"]......等我哪天有空再说吧。
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]你之前也是这样说的——
[charslot(slot="m",name="avg_4186_tmoris_1#1$3",focus="m")]
[name="八幡海铃"]走了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="33_g11_mansionhall",screenadapt="coverall", block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
我拒绝了他的盛情邀请。
但回家的路上，我的心中却涌起一种莫名的感觉。
一种从未有过的感觉。
那晚，我躺在床上，辗转反侧，整夜未眠。
太阳还未升起之时，我就收拾好了所有的行李——
[Dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_4186_tmoris_1#6$3",focus="m")]
[name="八幡海铃"]......谁会找到这里？
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_699_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_699_1#1$1",focus="m")]
[name="严肃的打手"]海铃，老爷那边出了点状况，想让你帮忙背点罪。
[charslot(slot="m",name="avg_4186_tmoris_1#7$3",focus="m")]
[name="八幡海铃"]可我已经决定......
[charslot(slot="m",name="avg_npc_699_1#1$1",focus="m")]
[name="严肃的打手"]监狱那边我们已经安排好了，他们正在下面等着。
[name="严肃的打手"]这些是报酬，你要是觉得不够，还可以再加。
[charslot(slot="m",name="avg_4186_tmoris_1#3$3",focus="m")]
[name="八幡海铃"]......
[charslot(slot="m",name="avg_npc_699_1#1$1",focus="m")]
[name="严肃的打手"]海铃，你今天怎么回事，是我说错什么了吗？
[name="严肃的打手"]之前不一直都是这样吗——我们出钱，你办事。
[name="严肃的打手"]快去吧，我们会想办法帮你减到半年，半年就能出来了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_cellroomC",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$doorclosequite", volume=1)]
[delay(time=1)]
[focusout(duration=2, type="bg", from=0, to=1, block=false)]
[delay(time=1)]
作为被雇佣的打手，替人背罪是再正常不过的事，我对监狱的生活也再熟悉不过。
但这次，唯独这次，我却无比地煎熬。
半年里，我无时无刻不想着出狱，想回到那个家族中，回到他们的乐队派对里。
我已经决定好了自己的归宿。
可我没想到，最后的结局却是——
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="33_g2_srcalley",screenadapt="coverall", block=true)]
[focusout(duration=0.1, type="bg", from=1, to=0, block=true)]
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[delay(time=1)]
[playsound(key="$d_avg_rainlight_loop", loop=true, channel="bgs",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_698_1#1$1",focus="m")]
[name="弗朗西斯"]老大死了，大家都死了，几百号人现在只剩我们十几个了！
[name="弗朗西斯"]我们一帮兄弟好不容易从哥伦比亚漂泊到这鬼地方，全栽在你一个人手上了！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[StopSound(channel="bgs", fadetime=2)]
[charslot]
[Background(image="33_g2_srcalley",screenadapt="coverall", block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
这半年里究竟发生了什么？
我不知道，但我唯一知道的是——
我又一次失去了“家”。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g7_reception",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="苍老的声音"]海铃，你替我做了这么多件事，卖了这么多次命，我应当给你一个身份。
[name="苍老的声音"]我允许你加入我的家族。
[charslot(slot="m",name="avg_4186_tmoris_1#12$3",focus="m")]
[name="八幡海铃"]......你知道我从来都是独来独往，不会加入任何一个家族。
[charslot(slot="m",name="avg_4186_tmoris_1#12$3",focus="n")]
[name="苍老的声音"]是不愿，还是不能？
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="m")]
[name="八幡海铃"]......
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="n")]
[name="苍老的声音"]海铃，我和那些自称“家族领袖”的地痞流氓不一样。
[name="苍老的声音"]我在这个地方和那帮阴险狡诈的大家族斗了大半辈子，从来没有离开过牌桌。
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="m")]
[name="八幡海铃"]你希望我帮你登上更大的牌桌？
[charslot(slot="m",name="avg_4186_tmoris_1#9$3",focus="n")]

... (全文9193字符)
```

### level_act45side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g10_dreamcastlestage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Subtitle(text="<i>包裹住最脆弱柔软的记忆，直至无人知晓。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>可声嘶力竭的呐喊，又如何让那人听见？</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我，毋畏悲伤。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="65_g3_islandharbor", screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[PlaySound(key="$d_avg_harbor_busy", volume=1)]
[PlaySound(key="$d_avg_shipwhistle", volume=1,delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2.5)]
[PlaySound(key="$d_avg_openftstpwalk", volume=1, loop=true, channel="o")]
[StopSound(channel="o", fadetime=3)]
[charslot(slot = "l", name = "avg_npc_1000_1#1$1",duration=1)]
[charslot(slot = "r", name = "avg_4182_oblvns_1#1$2",duration=1)]
[delay(time=3)]
[charslot]
从摇摇晃晃的甲板走上坚硬的土地，重新脚踏实地的感觉让祥子有些安心。
[charslot(slot = "l", name = "avg_npc_1000_1#1$1",focus="l")]
[charslot(slot = "r", name = "avg_4182_oblvns_1#1$2",focus="l")]
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[name="热心的船夫"]姑娘，谢谢你一直陪我聊天。
[name="热心的船夫"]这岛离陆地实在太远，要是没你，我一个人盯着海面开船，准无聊疯了。
[charslot(slot = "r", name = "avg_4182_oblvns_1#1$2",focus="r")]
[name="丰川祥子"]和您聊天，也让我听到了许多海上的趣事。
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[name="热心的船夫"]你这装扮看起来也不像是本地人，你怎么会来这种无人问津的小岛？
[charslot(slot = "r", name = "avg_4182_oblvns_1#10$2",focus="r")]
[name="丰川祥子"]......有一个想找的人。
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[name="热心的船夫"]她是本地人？
[charslot(slot = "r", name = "avg_4182_oblvns_1#10$2",focus="r")]
[name="丰川祥子"]......应该不是。
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[name="热心的船夫"]那真是稀奇了，这岛上只有往外面跑的，从没见过主动来的。
[charslot(slot = "r", name = "avg_4182_oblvns_1#10$2",focus="r")]
[name="丰川祥子"]其实我也不能确定她在不在这......
[charslot]
祥子手中只有这张前往小岛的船票，不论是不是莫菲丝的恶作剧，她都只有这一个选择。
[charslot(slot = "l", name = "avg_npc_1000_1#1$1",focus="l")]
[charslot(slot = "r", name = "avg_4182_oblvns_1#10$2",focus="l")]
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[PlaySound(key="$d_avg_slapcloth_light",volume=1)]
[name="热心的船夫"]（拍肩）哎，没事的！这岛上就这么点人，问问住在这的居民，肯定很快就能找到的！
[charslot(slot = "r", name = "avg_4182_oblvns_1#1$2",focus="r")]
[name="丰川祥子"]......嗯。
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[name="热心的船夫"]不过姑娘，不管最后找没找到，你过了正午一定要回到这啊。
[name="热心的船夫"]这里的船班次实在太少，你要是错过，至少得等下个月才能离开了。
[charslot(slot = "r", name = "avg_4182_oblvns_1#14$2",focus="r")]
[name="丰川祥子"]可现在已经快......
[charslot(slot="l",name="avg_npc_1000_1#1$1",focus="l")]
[name="热心的船夫"]唉，这也没办法啊。
[name="热心的船夫"]我也能多等你一会，但晚上出航不安全，咱们日落前一定得返航。
[charslot(slot = "r", name = "avg_4182_oblvns_1#6$2",focus="r")]
[name="丰川祥子"]......那我现在就出发！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[musicvolume(volume=0.3, fadetime=2)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$beach", channel="bc", loop=true, volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="？？？"]（大声）哆——来——咪——
[name="？？"]嗯，能听见。
[Dialog]
[PlaySound(key="$d_avg_fssand", channel="ystep", loop=true, volume=0.5)]
[StopSound(channel="ystep", fadetime=3)]
[Delay(time=2)]
[name="？？？"]（小声）哆——来——咪——
[name="？？"]......
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[Delay(time=1.5)]
[name="？？？"]我刚刚在远处重复了一遍......是听不见了吗？
[name="？？"]......嗯。刚刚，没有声音。
[name="？？？"]......我先帮你把眼罩摘下来吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[StopSound(channel="bc", fadetime=1.5)]
[charslot]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Delay(time=0.5)]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[musicvolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[bgeffect]
[charslot(slot = "l", name = "avg_180_amgoat_1#1$1",duration=0.7)]
[charslot(slot = "r", name = "avg_4184_dolris_1#9$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_180_amgoat_1#1$1",focus="l")]
[name="艾雅法拉"]结果怎么样？
[charslot(slot = "r", name = "avg_4184_dolris_1#9$2",focus="r")]
[name="三角初华"]不容乐观......和上次比起来，又近了一些。
[charslot(slot="l",name="avg_180_amgoat_1#2$1",focus="l")]
[name="艾雅法拉"]这样吗......我知道了。以后外出考察，我会多注意周围状况的。
[charslot(slot = "r", name = "avg_4184_dolris_1#11$2",focus="r")]
[name="三角初华"]艾雅法拉，你该多为自己的安全着想。
[name="三角初华"]你来岛上有多久了？
[charslot(slot="l",name="avg_180_amgoat_1#1$1",focus="l")]
[name="艾雅法拉"]两个月前到的岛上。
[charslot(slot = "r", name = "avg_4184_dolris_1#11$2",focus="r")]
[name="三角初华"]你听力的情况一直在恶化，但这里没有正规的医生能给予你帮助。
[name="三角初华"]今天码头应该有航船停靠，我帮你收拾行李，你待会就启程回去。
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="艾雅法拉"]不行，这里的火山还有最后一组数据没收集完......
[charslot(slot = "r", name = "avg_4184_dolris_1#9$2",focus="r")]
[name="三角初华"]可是你的身体——
[charslot(slot="l",name="avg_180_amgoat_1#8$1",focus="l")]
[name="艾雅法拉"]来这个小岛前，我请罗德岛的医生帮我做了健康评估。
[name="艾雅法拉"]嗯......情况的确不容乐观，但我和医生做了保证，三个月内一定会回去。
[name="艾雅法拉"]医生她知道火山研究对我来说很重要，所以最后还是同意让我来了。
[charslot(slot = "r", name = "avg_4184_dolris_1#9$2",focus="r")]
[name="三

... (全文18336字符)
```

### level_act45side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
当重复的事情做了无数次，人总会丧失对其的感知。
当重复的一天度过了无数遍，人便会陷入这个循环之中。
无从自觉，无法自拔。
就像一个漫长的、无尽的、无解的梦一样。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_hotel",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
伴随着山中羽兽的啼鸣，每天清晨从床上自然地苏醒。
倘若想睡个懒觉，也不会有人催促，把头重新埋进被子里就好。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
收拾好被子和床铺，在厨房简单地做一顿早餐。
煎蛋，面包，牛奶......
想吃什么，想喝什么，全凭自己的心意。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_ltroom",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
一个人坐在钢琴旁，按下一个琴键，将未调的琴弦一点点调成正确的音调。不知过了多久，再调下一根琴弦。
等到调完最后一根琴弦，第一根琴弦的音调又变得不准。
于是，如此反复。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[gridbg(imagegroup="38_g21_skystarry_L1/38_g21_skystarry_R1/38_g21_skystarry_L2/38_g21_skystarry_R2", solidwidth="1280/1280/1280/1280", solidheight="720/720/720/720", x=-105, fadetime=1)]
[largebgtween(duration = 60,yFrom = 720, yTo = 360,block = false)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
一个人躺在盛夏的草地上，看着一览无余的星空。
她知道，即使星星的位置看起来和昨天并无区别，但其实它们一直在永不停歇地变化。
两颗现在相邻的星星，即使被人们赋予意义，在千万年后，也会变得无比遥远，毫无瓜葛。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[gridbg]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
就和人与人之间的关系一样。
今天，她也没有回来。
在渺无人烟的小岛，仅凭脑海中微弱的记忆，构建一个不可确信的梦。
囿于记忆的牢笼，如同人偶一般。
执念与悲伤填充着身体，膨胀，膨胀。
却动弹不得。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[charslot(slot = "l", name = "avg_180_amgoat_1#11$1")]
[charslot(slot = "r", name = "avg_4184_dolris_1#12$2")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_4184_dolris_1#12$2",focus="r")]
[name="三角初华"]一开始，我以为她只是突发奇想，去附近散了散步。
[name="三角初华"]后来，我从码头工人的口中得知，她那天独自登上了离岛的航船......
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="艾雅法拉"]你为什么不去找她呢？
[charslot(slot = "r", name = "avg_4184_dolris_1#12$2",focus="r")]
[name="三角初华"]这样的一天实在有过太多太多次，多到我不能确认它究竟是否真实。
[charslot(slot = "r", name = "avg_4184_dolris_1#9$2",focus="r")]
[name="三角初华"]我......我已经想不起她的模样，也记不起她的名字了。
[name="三角初华"]也许这就是我的归宿......在这静静地等待。
[Dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="等待她的归来，抑或是我的死亡。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="悲伤的源泉终有一天会干涸，没有更多的眼泪，便不会再哭泣了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这样无人关心的角落，就是我最好的归宿。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Sticker(id="st1", text="“不行！”", x=300, y=350, alignment="center", size=28, delay=0, duration=1, width=700)]
[Sticker(id="st1", duration=0.5,block = false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_180_amgoat_1#11$1",focus="r")]
[charslot(slot = "r", name = "avg_4184_dolris_1#8$2",focus="r")]
[name="三角初华"]——！
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[name="艾雅法拉"]初华小姐，你在哭，说明你还不想放弃，对吧？
[name="艾雅法拉"]这不是你想要的结局，对吧？！
[charslot(slot="l",name="avg_180_amgoat_1#11$1",focus="l")]
[multiline(name="艾雅法拉")]至少......
[charslot(slot="l",name="avg_180_amgoat_1#8$1",focus="l")]
[multiline(name="艾雅法拉")]至少，应该站在她的面前，表达自己的想法吧。
[charslot(slot = "r", name = "avg_4184_dolris_1#7$2",focus="r")]
[name="三角初华"]......
[charslot(slot="l",name="avg_180_amgoat_1#8$1",focus="l")]
[name="艾雅法拉"]我能听出来的话，她一定也能明白你的心意。
[name="艾雅法拉"]不用尽全力呐喊，又怎么能传达给她呢？
[name="艾雅法拉"]连我都能听到你的声音，她肯定也可以的。
[charslot(slot = "r", name = "avg_4184_dolris_1#7$2",focus="r")]
[name="三角初华"]我......可是你的听力状况，我不能留下你一个人——
[charslot(slot="l",name="avg_180_amgoat_1#8$1",focus="l")]
[name="艾雅法拉"]再怎么说，我也是接受过罗德岛训练的干员，你就放心好啦。
[name="艾雅法拉"]作为本就是萍水相逢的人，初华小姐，你已经为我做了很多事了。
[charslot(slot="l",name="avg_180_amgoat_1#1$1",focus="l")]
[name="艾雅法拉"]你该问问自己的内心——现在到底想要做什么？
[charslot(slot = "r", name = "avg_4184_dolris_1#12$2",focus="r")]
[name="三角初华"]（小声）我想找到她......
[Dialog]
[charslot(slot = "r", name = "avg_4184_dolris_1#14$2",focus="r")]
[delay(time=1)]
[charslot(slot = "r", name = "avg_4184_dolris_1#9$2",focus="r")]
[name="三角初华"]......没什么。
[Dialog]
[charslot(slot="l",name="avg_180_amgoat_1#8$1",focus="l")]
[delay(time=1)]
[name="艾雅法拉"]初华小姐，我看得懂唇语哦。
[Dialog]
[charslot(duration=0.5)]
[delay(time=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", multi = true, text="“看吧，你已无路可逃”", x=300,y=220, alignment="center", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n“将逐渐虚弱的你，紧紧关住——”",block = true)]
[Sticker(id="st1", multi = tru

... (全文16000字符)
```

### level_act45side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g10_dreamcastlestage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Subtitle(text="<i>我们一同欢笑，我们一同哭泣。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>在华丽的舞台上，上演一出热闹非凡的独角戏。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>我，毋畏死亡。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="65_g9_warmrabbitnest", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4183_mortis_1#1$3",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4183_mortis_1#1$3",focus="m")]
[name="若叶睦"]祥，来，喝下去。
[Dialog]
[charslot(slot="m",name="avg_4182_oblvns_1#3$2",focus="m")]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_drinkswllw", volume=0.6)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#1$2",focus="m")]
[name="丰川祥子"]喉咙没有那么痛了......
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]那就好。这个给你，雷姆必拓到处都是沙尘，水袋和护目镜是必需的。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_pcket",volume=0.7)]
[delay(time=1)]
祥子接过睦递来的物资，她的双手紧紧地攥着它们，鼓胀的水袋好像随时都要被挤破。
[charslot(slot="m",name="avg_4183_mortis_1#16$3",focus="m")]
[name="若叶睦"]祥，你有点奇怪。是不是不舒服？
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]不，没什么......
[name="丰川祥子"]睦，你......还记得我？
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="若叶睦"]当然。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]你还记得我们经历过的那些事？
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="若叶睦"]嗯，我全都记得。
[Dialog]
[charslot]
祥子感觉自己终于变得冷静了些，她开始环顾四周——
方才她们顺着狭长的矿道一直深入，最终来到了这里。
这里阴暗潮湿，只有油灯和炉火提供着微弱的光亮。
床与餐桌之间仅有一人宽的空隙，而从桌上水杯的数目来看，这里住着的绝不止睦一人。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]睦，你在这里......已经生活多长时间了？
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]一年，也许更久。在这里需要考虑的事很简单，时间的流逝也没有那么明显。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]不......你对时间没有任何感觉，是因为你身处在梦里。
[name="丰川祥子"]睦，你为什么会做这样一个梦......
[charslot(slot="m",name="avg_4183_mortis_1#16$3",focus="m")]
[name="若叶睦"]梦......？
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]睦，我有重要的事和你说。这里不是现实，我们现在应该——
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[name="？？？"]啊呀——小睦，你怎么现在就回来啦？
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[PlaySound(key="$d_avg_kneelsnow_s", volume=1,delay=1)]
[Delay(time=1)]
[CameraShake(duration=1, xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
一个身影从身后跑了进来，径直将睦扑倒在柔软的小床上。
[name="若叶睦"]妈、妈妈，身上有灰，不要蹭......
[name="？？？"]哎，都快一天没见了，让我抱抱怎么了嘛！
[name="若叶睦"]有、有人......
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot="l",name="avg_npc_1939_1#1$1",duration=1)]
[charslot(slot="r",name="avg_4183_mortis_1#1$3",duration=1)]
[Delay(time=2)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]啊，小祥在这呀！
[name="睦的母亲"]你好久没来我们家了吧？
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]南小姐......
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]哎，怎么这么见外啦，叫“南”就行啦。
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]嗯，我有时也会这么叫妈妈。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]......
[name="丰川祥子"]睦，你和南小姐的关系什么时候这么好了......？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]我们一直关系很好啊，毕竟是母女嘛~
[name="睦的母亲"]小睦，今天的收获如何？
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]（翻找口袋）今天天气有点热，买黄瓜汁的人比平时多一点。
[Dialog]
[charslot]
睦小心翼翼地将手中的布袋打开，里面是一些零星的硬币。
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]嗯——小睦，你好棒！
[name="睦的母亲"]（翻翻口袋）喏，这是我的。
[charslot(slot="m",name="avg_4183_mortis_1#15$3",focus="m")]
[name="若叶睦"]哇......妈妈，好厉害。
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]哼哼，不知道为什么，今天找我修补衣服的人格外多哦！
[name="睦的母亲"]你爸爸今天也很努力哦，在工地里忙活了一整天。我给他送午饭时，看他那副灰头土脸的样子实在不忍心，就特批他下工后去喝一小杯。
[name="睦的母亲"]他现在啊——估计已经一大瓶啤酒下肚了吧！
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]刚好今天小祥来了，机会难得，不如我们请大家一起来吃饭吧！
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]大家能聚在一起吃饭，好开心。
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]是呀！而且今天收入不错，不多吃点怎么行！
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]......
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]小祥千万别客气！
[charslot(slot="m",name="avg_4183_mortis_1#16$3",focus="m")]
[name="若叶睦"]祥，怎么了？
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]不......没有......
[Dialog]
[charslot]
眼前这个明显就不富裕的家，光秃秃的泥巴墙、微弱的油灯......
为什么睦的梦里，会出现这些？
[Dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4081_warmy_1#11$2",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4081_warmy_1#11$2",focus="m")]
[name="温米"]小睦，还有南......这位是？
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]她是我从小认识的朋友，祥。
[charslot(slot="m",name="avg_4081_warmy_1#4$2",focus="m")]
[name="温米"]你好~
[charslot(slot="m",name="avg_4081_warmy_1#1$2",focus="m")]
[nam

... (全文14020字符)
```

### level_act45side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="46_g6_rmbtmine",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="nrun")]
[StopSound(channel="nrun", fadetime=2)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]呼......呼......唔......！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_airshiptakeoff", volume=0, loop=true, channel="machine")]
[SoundVolume(volume=0.8, channel="machine",fadetime=1)]
[Delay(time=3)]
[SoundVolume(volume=0, channel="machine",fadetime=3)]
沉闷的声音在空旷的洞穴中回荡，那是附近仍未停止作业的掘地机发出的声响。
气温越来越低。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_wilderness_n",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
跑出洞穴的那一刻，寒意同时到来。
而寒冷，只会让她心脏的跳动不断加快。
[charslot(slot="m",name="avg_4182_oblvns_1#2$2",focus="m")]
[name="丰川祥子"]我该......该怎么面对她？
[Dialog]
[charslot]
无法开口，无法面对。
[stopmusic(fadetime=2)]
[name="？？？"]啧啧啧，该如何是好呢？
[Dialog]
[PlaySound(key="$d_avg_openftstpwalk", volume=1, loop=true, channel="o")]
[StopSound(channel="o", fadetime=2)]
[delay(time=1.5)]
无须回头，她已然知道来者是谁。
[Dialog]
[charslot(slot="m",name="avg_npc_1942_1#18$1",duration=0.7)]
[Delay(time=1.5)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]这个孩子的梦境，我真的很满意呢~
[name="莫菲丝"]梦城堡的职责就是让每个孩子都有一场好梦，我一一实现了她的愿望。
[name="莫菲丝"]没想到这个梦境意外地运行得很稳定——不，甚至完美无缺，完全超出了我的预期。
[name="莫菲丝"]而且在这里，有一些很有趣的事情正在发生哦。
[charslot(slot="m",name="avg_4182_oblvns_1#9$2",focus="m")]
[name="丰川祥子"]......你在欺骗她。
[charslot(slot="m",name="avg_npc_1942_1#20$1",focus="m")]
[name="莫菲丝"]不不不，这可不算欺骗。我和她交易了很多次，她很清楚我的身份。
[name="莫菲丝"]看到这个结果，我也很开心呢。
[name="莫菲丝"]就算意识到是梦境，依旧不愿意离开，那不正说明我的造梦技艺无人能比吗？
[Dialog]
[charslot(slot="m",name="avg_npc_1937_1#3$1",focus="m")]
[PlaySound(key="$d_avg_yingying_ked_1", volume=1)]
[name="卡尔顿们"]（赞同的哼唧声）
[Delay(time=1)]
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_4183_mortis_1#14$3",duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]哦，最后来的竟然是......？
[charslot(slot="m",name="avg_npc_1942_1#1$1",focus="m")]
[name="莫菲丝"]有点意思。
[name="莫菲丝"]我就不打扰你们了~丰川祥子，相信你很快也会发现这个梦境的有趣之处。
[Dialog]
[PlaySound(key="$d_avg_shdwblwvr", volume=0.6)]
[charslot(duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="若叶睦"]祥子，大家都在等着你呢。回去吧。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]回哪去？
[name="丰川祥子"]你看着莫菲丝消失，却没有一点惊讶......？
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="若叶睦"]当然。
[name="若叶睦"]这里的一切，都是我们虚构出来的。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]“我们”？
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="若叶睦"]你，不属于我们。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g9_warmrabbitnest",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[PlaySound(key="$d_avg_electricguitar",volume=0.6)]
[delay(time=2)]
[Dialog]
[charslot]
[PlaySound(key="$d_avg_cheer_street", volume=0.8)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1939_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]小睦，你弹得好棒！
[charslot(slot="m",name="avg_4183_mortis_1#13$3",focus="m")]
[name="若叶睦"]祥......
[charslot(slot="m",name="avg_4183_mortis_1#16$3",focus="m")]
[name="若叶睦"]不对，妈妈......祥，她去哪了？
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]小祥？可能去别的什么地方了吧......？
[charslot(slot="m",name="avg_4183_mortis_1#6$3",focus="m")]
[name="若叶睦"]不对，不对。祥......祥她不可能丢下我。
[stopmusic(fadetime=2)]
[Dialog]
[charslot(duration=0.7)]
[delay(time=1)]
欢呼的人群突然变得一片死寂，所有人都直勾勾地盯着睦。
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="m")]
[name="睦的母亲"]小睦，你好像忘记了——
[name="睦的母亲"]这里不是你一个人的梦。
[Dialog]
[charslot(slot="m",name="avg_npc_1939_1#1$1",focus="all")]
[delay(time=0.2)]
[charslot(slot="m",name="avg_npc_1939_1#1$1",afrom=1,ato=0,duration=1)]
[delay(time=1)]
[playsound(key="$d_avg_humanchange")]
[charslot(slot="r",name="avg_4183_mortis_1#14$3",posfrom="-200,0",posto="-200,0",afrom=0,ato=1,duration=1)]
[delay(time=1.5)]
[PlayMusic(key="$monastery_sad_loop", volume=0.6)]
[name="“睦的母亲”"]这里是“我们”的梦。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_wilderness_n",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="“睦”"]“我们”。
[name="“睦”"]在这个梦境里，每一个“睦”都有机会实现自己的愿望。
[name="“睦”"]我们和小睦一起，构建出了只属于我们的美梦——大家都能得到幸福的梦。
[name="“睦”"]我们在小睦的脑海中存在，观看了无数遍她的人生。
[name="“睦”"]最后，我们一致认为，对于所有的“睦”来说，这就是最好的结局——
[name="“睦”"]而你，丰川祥子，你是这个美梦的敌人。
[charslot(slot="m",name="avg_4182_oblvns_1#2$2",focus="m")]
[name="丰川祥子"]睦，你这是在说什么？
[charslot(slot="m",name="avg_4182_oblvns_1#9$2",focus="m")]
[name="丰川祥子"]我也不希望你痛苦下去，但是我们都不该躲在这样的梦里——
[charslot(slot="m",name="avg_4183_mortis_1#10$3",focus="m")]
[name="“睦”"]......
[name="“睦”"]不，小睦能在这里幸福地生活下去才是最重要的事。
[name="“睦”"]我和大家不一样，我想和祥子好好谈谈。
[name="“睦”"]你可以留在这里，和我一起，守护小睦的美梦。
[charslot(slot="m",name="avg_4183_mortis_1#14$3",focus="m")]
[name="“睦”

... (全文10382字符)
```

### level_act45side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
寒风在耳边呼啸而过。
下坠，越来越快。
可深渊仍不见底。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[cameraEffect(effect="Grayscale", keep=true, amount=0.5, fadetime=0)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]我那些强人所难的要求，除了你还有其他鼓手能满足吗？
[charslot(slot="m",name="avg_4182_oblvns_1#13$2", focus="m")]
[name="丰川祥子"]你是我见过的，最努力的鼓手。
[charslot(slot="m",name="avg_4182_oblvns_1#13$2", focus="m")]
[name="丰川祥子"]你明明......只需要做你自己就好。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="33_g2_srcalley",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]在各个组织间忙碌，却找不到一个真正的落脚点......这就是你想要的生活吗？
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]你本不该承受这种痛苦......
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]海铃，和我一起离开吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g4_islandharbor_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#2$2", focus="m")]
[name="丰川祥子"]我一定要找到你......
[charslot(slot="m",name="avg_4182_oblvns_1#2$2", focus="m")]
[name="丰川祥子"]初华......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_wilderness_n",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]睦，这里不是现实，我们现在应该......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
砰——！
[PlaySound(key="$bodyfalldown2", volume=1)]
[PlaySound(key="$d_avg_land_impact")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[dialog]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="65_g2_dreamcastlehall", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#6$1", focus="m")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=false)]
[name="丰川祥子"]——！
[charslot]
急促的心跳，失控的呼吸，还有背脊上的冷汗。
知觉再次回到了祥子体内，却是以这种狼狈不堪的方式。
[dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m",duration=1)]
[delay(time=2)]
[name="莫菲丝"]	很真实吧？
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]	从不知道多高的地方，向地面坠落。
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]	还有梦境破碎，被困在“无梦之境”又无法逃脱......感觉如何呢？
[charslot(slot="m",name="avg_4182_oblvns_1#9$1", focus="m")]
[name="丰川祥子"]即使那些梦都是美梦，它们也不该继续下去。
[charslot(slot="m",name="avg_4182_oblvns_1#9$1", focus="m")]
[name="丰川祥子"]窥窃她们心里最脆弱的部分，再将它们不断编排演绎......
[charslot(slot="m",name="avg_npc_1942_1#1$1",focus="m")]
[name="莫菲丝"]	我可不这么认为哦。
[charslot(slot="m",name="avg_npc_1942_1#1$1",focus="m")]
[name="莫菲丝"]	在你闯进她们的梦前，她们几乎就要忘记你，还有那个根本无足轻重的乐队了。
[charslot(slot="m",name="avg_4182_oblvns_1#9$1", focus="m")]
[name="丰川祥子"]Ave{@nbs}Mujica是我们的契约，她们把人生托付给了我——
[charslot(slot="m",name="avg_npc_1942_1#13$1",focus="m")]
[name="莫菲丝"]	在乎它的只有你一个人吧！
[charslot(slot="m",name="avg_4182_oblvns_1#4$1", focus="m")]
[name="丰川祥子"]什么——！
[charslot(slot="m",name="avg_npc_1942_1#18$1",focus="m")]
[name="莫菲丝"]你不是都亲耳听见了吗？
[charslot(slot="m",name="avg_npc_1942_1#15$1",focus="m")]
[name="莫菲丝"]她们一个个，全都拒绝了你。
[Dialog]
[PlaySound(key="$d_avg_spiritwhoosh", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4185_amoris_1#2$3", focus="m")]
[name="祐天寺若麦"]我不要。这里的人爱着身为女演员的我。
[charslot(slot="m",name="avg_4185_amoris_1#7$3", focus="m")]
[name="祐天寺若麦"]我为了这些，拼尽了一切......结果你告诉我这些全是假的？
[charslot(slot="m",name="avg_4185_amoris_1#2$4", focus="m")]
[name="祐天寺若麦"]什么荒唐话，我不可能接受！
[charslot(slot="m",name="avg_4185_amoris_1#2$4", focus="m")]
[name="祐天寺若麦"]这里是我的梦境，只有我自己就好了！
[Dialog]
[PlaySound(key="$d_avg_spiritwhoosh", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="33_g2_srcalley",screenadapt="coverall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4186_tmoris_1#9$3", focus="m")]
[name="八幡海铃"]你怎么可能懂我？
[charslot(slot="m",name="avg_4186_tmoris_1#9$3", focus="m")]
[name="八幡海铃"]这样的生活就很好......这样更适合我。
[charslot(slot="m",name="avg_4186_tmoris_1#3$3", focus="m")]
[name="八幡海铃"]我不需要谁来拯救。
[charslot(slot="m",name="avg_4186_tmoris_1#3$3", focus="m")]
[name="八幡海铃"]也没有人能救我。
[Dialog]
[PlaySound(key="$d_avg_spiritwhoosh", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g4_islandharbor_n",screenad

... (全文13827字符)
```

### level_act45side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g1_victoriavillage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[delay(time=0.5)]
[charslot]
[name="激动的孩子们"]爱丽丝姐姐，还有贝娜姐姐——！
[charslot(slot="m",name="avg_369_bena_1#6$1",focus="m")]
[name="贝娜"]我有遵守约定给你们带糖果哦，人人有份！
[charslot]
[name="激动的孩子们"]好耶——
[charslot(slot="m",name="avg_369_bena_1#1$1",focus="m")]
[name="贝娜"]那你们有按照约定，想好自己心里重要的东西吗？
[charslot]
[name="激动的孩子A"]我的是存钱罐！你听，里面都是攒下来的硬币！
[charslot]
[name="激动的孩子B"]这是我前段时间种出的小花......很好看，所以想让贝娜姐姐帮忙保存。
[charslot(slot="m",name="avg_369_bena_1#6$1",focus="m")]
[name="贝娜"]好好好，大家排好队——一个个来！
[dialog]
[charslot]
爱丽丝和贝娜尝试让孩子们有序地介绍他们心中的珍视之物，但似乎每个孩子身上都散发着无限的热情。
稚嫩的童声此起彼伏，眼下的光景却丝毫不见混乱，反而充满了温馨。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2", focus="m")]
[name="丰川祥子"]......
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_243",focus="m",duration=1)]
[delay(time=1.5)]
[name="和善的镇民"]这不是祥子吗？
[name="和善的镇民"]你怎么突然回来啦？
[charslot(slot="m",name="avg_4182_oblvns_1#14$2", focus="m")]
[name="丰川祥子"]	你是......？
[charslot(slot="m",name="avg_290_vigna_1#8$1",focus="m")]
[name="红豆"]我们最近正好在这有外勤任务，我就带祥子一起过来了，顺便让她回家看看。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="和善的镇民"]你爸爸每天都在念叨你呢，说你在一家大公司实习，忙得都不回信了。
[name="和善的镇民"]我就没见过他这么多话的时候，看来是真想你了！
[name="和善的镇民"]你快回去吧。给他一个惊喜，然后好好安慰一下他！
[charslot(slot="m",name="avg_4182_oblvns_1#14$2", focus="m")]
[name="丰川祥子"]	......
[charslot(slot="m",name="avg_290_vigna_1#11$1",focus="m")]
[name="红豆"]	（小声）祥子，你从刚才就很奇怪......感觉反应老是慢半拍！
[charslot(slot="m",name="avg_4182_oblvns_1#10$2", focus="m")]
[name="丰川祥子"]	请问......我家往哪走？
[charslot]
[charslot(slot="l",name="avg_290_vigna_1#11$1",focus="all")]
[charslot(slot="r",name="avg_npc_243",focus="all")]
[name="红豆&和善的镇民"]......？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="34_g1_victoriavillage",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
虽然之后的对话异常尴尬，但祥子还是按好心人的指引，顺利地找到了回家的路。
顺着蜿蜒的小路，她终于走到了自己“家”门前。那是一栋洁白的、陌生的房子。
庭院里的花草被修剪得整整齐齐，她能听见花坛里设备浇水的细微声响。屋顶的烟囱冒出一缕缕炊烟，屋子的主人正在准备今日的午餐。
可她知道，即将前往的，并不是她真正的“家”。
她真正的家，在遥远而不可及之处。
提到家，祥子会先想起丰川家的宅邸，然后是那个有着一股酒气、飘散着灰尘的小小的出租屋。
她想起了那个曾经诚实勤奋的父亲。
可惜真正的父亲，现在或许正提着酒瓶，游走在街头。也许他会提到自己的名字，可搭配的修饰词绝无可能与“美好”有关。
没错，这才是丰川祥子的现实。
而眼前的这些，是莫菲丝为她创造的梦境，也是用来囚禁她的牢笼。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g5_sakikodininghall",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=1)]
一股食物的香气扑鼻而来。
[name="？？？"]哼哼——♪哼哼哼——♪哼哼——♪哼哼哼——♪
[dialog]
[charslot(slot="m",name="avg_npc_1940_1#2$1", focus="m",duration=1)]
[delay(time=2)]
[name="“父亲”"]......祥子？！
[charslot(slot="m",name="avg_npc_1940_1#2$1", focus="m")]
[name="“父亲”"]你怎么突然回来了，不是说在公司工作很忙吗？
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]	嗯......正好有外派任务，所以回来看看。
[charslot(slot="m",name="avg_npc_1940_1#6$1", focus="m")]
[name="“父亲”"]你也不常寄信回来，我每天只能拿你以前的信翻来覆去地看。
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]	普通的信而已，倒也没有必要......
[charslot(slot="m",name="avg_npc_1940_1#6$1", focus="m")]
[name="“父亲”"]宝贝女儿寄回来的信，怎么可能普通呢！
[charslot(slot="m",name="avg_4182_oblvns_1#6$2", focus="m")]
[name="丰川祥子"]	父亲，好像有什么东西烧煳了......
[charslot(slot="m",name="avg_npc_1940_1#2$1", focus="m")]
[name="“父亲”"]——！
[charslot(slot="m",name="avg_npc_1940_1#4$1", focus="m")]
[name="“父亲”"]稍等我一下！
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=0.5)]
[delay(time=4)]
[PlaySound(key="$d_avg_meatbakingtray", volume=1)]
[delay(time=3)]
[PlaySound(key="$d_avg_makesoup", volume=1)]
[delay(time=3)]
[PlaySound(key="$d_avg_soup", volume=1)]
[delay(time=3)]
[charslot(slot="m",name="avg_npc_1940_1#3$1", focus="m",duration=1)]
[delay(time=1.5)]
[name="“父亲”"]忘记注意时间了......这下得重新做了......
[charslot(slot="m",name="avg_npc_1940_1#1$1", focus="m")]
[name="“父亲”"]为了能做出祥子喜欢的料理，我专门去学习了好一阵子，你不想尝尝吗？
[charslot(slot="m",name="avg_4182_oblvns_1#6$2", focus="m")]
[name="丰川祥子"]	父亲，你以前好像从不做饭？
[charslot(slot="m",name="avg_npc_1940_1#6$1", focus="m")]
[name="“父亲”"]现在日子过得悠闲了，没事就喜欢捣鼓点新玩意。
[charslot(slot="m",name="avg_npc_1940_1#3$1", focus="m")]
[name="“父亲”"]而且你的脸都瘦成这样了......
[charslot(slot="m",name="avg_4182_oblvns_1#12$2", focus="m")]
[name="丰川祥子"]	罗德岛有定期体检——我体重还是和以前一样，没有变化。
[charslot(slot="m",name="avg_npc_1940_1#3$1", focus="m")]
[name="“父亲”"]肯定瘦了！
[dialog]
[charslot]
“父亲”心疼地伸出了手，摸了摸女儿的头。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2", focus="m")]
[name="丰川祥子"]——！
[charslot(slot="m",name="avg_npc_1940_1#5$1", focus="m")]
[name="“父亲”"]嗯......？
[dialog]
[charslot]
父亲的手让她感到既陌生又熟悉。
记忆里她总是弯下腰，将烂醉的父亲的手臂搭在自己肩上，然后半步半步地往家的方向走去。
他的手总是无力地垂在她眼前，就像刚才那样近在咫尺，可又那么不同......
[charslot(slot="m",name="avg_4182_oblvns_1#2$2", focus="m")]
[name="丰川祥子"]......
[name="丰川祥子"]又不是小孩子了，不要这样了......
[charslot(slot="m",name="avg_npc_1940_1#5$1", focus="m")]
[name="“父亲”"]对我来说，祥子永远都是我可爱的女儿。
[charslot(slot="m",name="avg_npc_1940_1#5$1", focus="m")]
[name="“父亲”"]即使出去工作了，也不能忘记保持笑容啊~
[charslot(slot="m",name="avg_4182_oblvns_1#13$2", focus="m")]
[name="丰川祥子"]......嗯。
[dialog]
[charslot]
父女两人面对面地笑了起来，刚才的犹豫也全被祥子抛在了脑后。
她能确信，自己现在正发自内心地笑着。
[dialog]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_smoothpiano", volume=0.2)]
[delay(time=4)]
[charslot(slot="m",name="avg_4182_oblvns_1#6$2", focus="m")]
[name="丰川祥子"]楼上为什么会有钢琴声......今天家里有客人吗？
[charslot(slot="m",name="avg_npc_1940_1#2$1", focus="m")]
[name="“父亲”"]嗯？你在说什么呀，祥子？
[charslot(slot="m",name="avg_npc_1940_1#2$1", focus="m")]
[name="“父亲”"]肯定是瑞穗在琴房练琴呀。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2", focus="m")]
[name="丰川祥子"].

... (全文8380字符)
```

### level_act45side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g6_sakikopianoroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_piano_start", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=3)]
[charslot(slot = "m", name = "avg_npc_1941_1#6$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1941_1#6$1",focus="m")]
[playMusic(key="$victorianormal_loop",volume=0)]
[musicvolume(volume=0.6, fadetime=2)]
[name="母亲"]祥子的琴弹得越来越好了啊~
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]有、有吗？
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]祥子的变化，我当然清楚，我可是你的妈妈呀。
[name="母亲"]我能听出来，祥子一直都很努力，即使在外辛苦工作，对于钢琴的练习也从未松懈过。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]欸？
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]感觉祥子在外面经历了很多呢......
[Dialog]
[charslot]
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1)]
[name="父亲"]虽然很不想打扰你们练琴，但饭已经做好咯？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g5_sakikodininghall", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_dishes", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#11$2",focus="m")]
[name="丰川祥子"]唔——好吃！
[charslot(slot = "m", name = "avg_npc_1940_1#6$1",focus="m")]
[name="父亲"]怎么样，我手艺又长进了吧？
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]你是不知道......他逼我尝了多少次，才有了现在这个味道。
[Dialog]
[charslot(slot = "m", name = "avg_npc_1940_1#5$1",focus="m")]
[PlaySound(key="$d_avg_plateplace", volume=1)]
[delay(time=1)]
[name="父亲"]这盘沙拉，快试试怎么样？
[charslot(slot="m",name="avg_4182_oblvns_1#11$2",focus="m")]
[name="丰川祥子"]唔，很好吃！
[charslot(slot = "m", name = "avg_npc_1940_1#6$1",focus="m")]
[name="父亲"]为了祥子能喜欢，我做了很多细微的调整哦！还不赖吧。
[name="父亲"]还有很多别的祥子喜欢的菜哦！
[charslot(slot="m",name="avg_4182_oblvns_1#11$2",focus="m")]
[name="丰川祥子"]嗯！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g5_sakikodininghall", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", action="shake",random=true, power=5, times=50,duration=0.4)]
[name="丰川祥子"]呃......呃......
[charslot(slot = "m", name = "avg_npc_1941_1#3$1",focus="m")]
[name="母亲"]祥子？祥子！
[charslot(slot = "m", name = "avg_npc_1940_1#2$1",focus="m")]
[name="父亲"]怎、怎么了？
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]不知不觉，吃得有点多......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="31_g3_mini12_farmland", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1941_1#7$1",focus="m")]
[name="母亲"]现在好点了吗......？
[charslot(slot = "m", name = "avg_npc_1941_1#3$1",focus="m")]
[name="母亲"]真是的，你爸爸就是这样的......
[charslot(slot = "m", name = "avg_npc_1941_1#1$1",focus="m")]
[name="母亲"]不过这就是他的行事风格，大多数时候也挺可爱的。
[name="母亲"]祥子，你会原谅他的吧？
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]我......
[dialog]
[charslot]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="我......真的能原谅他吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那个和他有着相同面貌的男人，曾无数次地伤透我的心。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]他真的很爱你哦。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]——！
[charslot(slot = "m", name = "avg_npc_1941_1#6$1",focus="m")]
[name="母亲"]我也一样。
[name="母亲"]我真的很爱你们。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]妈妈，怎么突然这么说......
[charslot(slot = "m", name = "avg_npc_1941_1#1$1",focus="m")]
[name="母亲"]你出远门的这段时间，我开始越来越频繁地翻相册了。
[name="母亲"]从你出生时的照片，翻到一岁、两岁、三岁......
[charslot(slot = "m", name = "avg_npc_1941_1#1$1",focus="m")]
[name="母亲"]在父母的眼中，孩子永远是最重要、最特殊的存在哦。
[name="母亲"]你刚出生的时候，手掌只有我的一半不到。
[name="母亲"]但现在你看，已经比我的要大一点点啦。
[dialog]
[charslot]
母亲拉起祥子的手，将两人的掌心慢慢对齐。
不知为何，祥子用五指紧紧地扣住了妈妈的手。
[charslot(slot="m",name="avg_4182_oblvns_1#13$2",focus="m")]
[name="丰川祥子"]妈妈，你的手好暖和......
[dialog]
[charslot]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="这就是妈妈手心的温度吗......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这一切，是真实的吗？我享受的这一切，是合理的吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="为什么会如此温暖，却又如此哀伤？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1941_1#6$1",focus="m")]
[name="母亲"]嗯，我在哦。
[charslot(slot="m",name="avg_4182_oblvns_1#8$2",focus="m")]
[name="丰川祥子"]妈妈......
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]哭鼻子也没关系哦。你以前哭鼻子的时候，我也是这么安慰你的。
[charslot(slot="m",name="avg_4182_oblvns_1#8$2",focus="m")]
[name="丰川祥子"]欸......我以前有那么爱哭鼻子吗？
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]在你很小很小的时候吧，那时祥子经常为了一颗糖又哭又闹呢。
[name="母亲"]虽然祥子现在是个坚强的孩子，但那时真的是个爱哭包呀。
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]是、是吗，我一点都不记得了......
[charslot(slot = "m", name = "avg_npc_1941_1#6$1",focus="m")]
[name="母亲"]哈哈哈哈哈，妈妈可不会骗你哦。
[dialog]
[charslot(slot="m",name

... (全文8642字符)
```

### level_act45side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="31_g3_mini12_farmland",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$comedy_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_carcrash_wreck", volume=0.6)]
[CameraShake(duration=1.5, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]妈妈，稍等我一下好吗？
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[name="母亲"]嗯，去吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(image="31_g3_mini12_farmland",screenadapt="coverall", block=true)]
[Delay(time=0.7)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]你们还好吗？！
[Dialog]
[charslot]
[delay(time=0.2)]
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
[charslot(slot="m",name="avg_290_vigna_1#5$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_290_vigna_1#5$1",focus="m")]
[name="红豆"]唔......还好还好，就是屁股有点痛......
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]刚刚不是还见到了爱丽丝小姐......
[Dialog]
[charslot]
[name="？？？"]唔......唔......唔......！
麦草垛的深处传来一阵熟悉的声音。
[charslot(slot="m",name="avg_290_vigna_1#4$1",focus="m")]
[name="红豆"]呃......快把爱丽丝挖出来！
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]好、好的！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_hidehaystack", volume=1)]
[CameraShake(duration=1.5, xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2)]
[charslot(slot="m",name="avg_338_iris_1#5$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_338_iris_1#5$1",focus="m")]
[name="爱丽丝"]（大口喘气）差......差点就要闷死了！
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]你们不是还要收集孩子们的愿望吗？为什么会出现在这？
[charslot(slot="m",name="avg_369_bena_1#10$1",focus="m")]
[name="贝娜"]嘿嘿，工作比想象中顺利得多。这边的孩子们意外地乖巧，所以就提前结束啦。
[charslot(slot="m",name="avg_290_vigna_1#5$1",focus="m")]
[name="红豆"]我本来是想体验体验在乡间开车的感觉，没想到半路出了毛病......
[charslot(slot="m",name="avg_369_bena_1#11$1",focus="m")]
[name="贝娜"]我也修理过这种载具，我们赶紧一起把它修好吧。
[Dialog]
[charslot(duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_290_vigna_1#5$1",focus="m")]
[Delay(time=0.3)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_338_iris_1#5$1",focus="m")]
[name="爱丽丝"]唉，也不知道今天是幸运还是倒霉......
[name="爱丽丝"]本来我还有些担心哪里会出状况。
[name="爱丽丝"]没想到今天的工作出奇地顺利，更没想到的是，会在这种小事上出现意外。
[charslot(slot="m",name="avg_338_iris_1#9$1",focus="m")]
[name="爱丽丝"]但愿能尽快修好吧......这样今晚就能返程了。
[charslot(slot="m",name="avg_4182_oblvns_1#6$2",focus="m")]
[name="丰川祥子"]今晚返程......？
[stopmusic(fadetime=2)]
[Dialog]
[charslot]
祥子转身看向身后。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Background(image="31_g3_mini12_farmland",screenadapt="coverall", block=true)]
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[delay(time=0.5)]
就在不远处，母亲正微笑地看着她和她的伙伴们。
她发觉了女儿回眸的视线，于是轻轻地点了点头。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(image="31_g3_mini12_farmland",screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_338_iris_1#10$1",focus="m")]
[name="爱丽丝"]那是......你的母亲？
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]......嗯。
[charslot(slot="m",name="avg_338_iris_1#2$1",focus="m")]
[name="爱丽丝"]你们长得真像，尤其是眼睛和嘴巴，给人一种既温柔又坚定的感觉。
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]......可是我并不坚定。
[charslot(slot="m",name="avg_338_iris_1#1$1",focus="m")]
[name="爱丽丝"]为什么这么说？
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[name="丰川祥子"]因为，我......
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]爱丽丝小姐，你是仙女对吧？
[charslot(slot="m",name="avg_338_iris_1#1$1",focus="m")]
[name="爱丽丝"]嗯......怎么了？
[charslot(slot="m",name="avg_4182_oblvns_1#12$2",focus="m")]
[name="丰川祥子"]仙女会倾听人的愿望，然后将愿望在梦中化为短暂的“现实”......对吧？
[charslot(slot="m",name="avg_338_iris_1#3$1",focus="m")]
[name="爱丽丝"]......是的。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]可是如果，真的有人在梦境中无法自拔，那又该怎么办？
[charslot(slot="m",name="avg_338_iris_1#10$1",focus="m")]
[name="爱丽丝"]真正的仙女，是不会允许这样的事情发生的。
[name="爱丽丝"]待在梦里的时间过长，最后只会让人分辨不清现实和梦境。
[charslot(slot="m",name="avg_4182_oblvns_1#14$2",focus="m")]
[name="丰川祥子"]如果她一直不苏醒呢？
[charslot(slot="m",name="avg_338_iris_1#10$1",focus="m")]
[name="爱丽丝"]祥子，最严重的结果从来不是无法苏醒，而是将梦中的一切当作理所应当后，却在某一刻醒来，发现经历的一切全是泡影。
[name="爱丽丝"]在梦中度过了无比幸福的一生后，却发现自己又回到了现实，一切又回到了原点。
[name="爱丽丝"]年幼的躯体，苍老的灵魂。梦中的一切都无法抓住，从此只能孑然一身地行于世间。
[name="爱丽丝"]这样的梦，真的是好的吗？
[name="爱丽丝"]本该失败的事，就不应靠梦境去逃避；本该错过的人，就应该好好地说声再见。
[Dialog]
[charslot]
祥子再次转身看向身后。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(image="31_g3_mini12_farmland",screenadapt="coverall", block=true)]
[charslot(slot = "m", name = "avg_npc_1941_1#5$1",focus="m")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(image="31_g3_mini12_farmland",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_4182_oblvns_1#10$2",focus="m")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[delay(t

... (全文24134字符)
```

### level_act45side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_deluxeroom",screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[PlaySound(key="$d_avg_policesiren", volume=0.2)]
[delay(time=3)]
从几十层高的天台往下看，地面上的车与人都渺小如尘。
[charslot]
[name="电话里的声音"]若麦小姐，我们已经加强了你住处附近的安保，请你这段时间减少外出。
[charslot]
[name="电话里的声音"]现在绑架犯还没抓到，出于安全考虑，公司建议你暂停这段时间的活动。
[charslot(slot="m",name="avg_4185_amoris_1#3$4", focus="m")]
[name="祐天寺若麦"]暂停活动......？
[charslot]
[name="电话里的声音"]只是一段时间，我们会重新筛选合适的合作方，以确保你的绝对安全。
[charslot(slot="m",name="avg_4185_amoris_1#3$4", focus="m")]
[name="祐天寺若麦"]那喜欢我的粉丝们......
[charslot]
[name="电话里的声音"]若麦小姐，你现在是龙门当红的明星，希望你能意识到自己的人气有多高。
[charslot(slot="m",name="avg_4185_amoris_1#3$4", focus="m")]
[name="祐天寺若麦"]可......！
[charslot]
[name="电话里的声音"]这段时间你可以去休假，或者做一些自己感兴趣的事。
[charslot]
[name="电话里的声音"]——唯独不要乱跑。
[charslot]
[name="电话里的声音"]近卫局又过来联系我们了，我需要去应付一下。
[dialog]
[PlaySound(key="$d_avg_phonestop", volume=0.2)]
[delay(time=4)]
[charslot(slot="m",name="avg_4185_amoris_1#7$3", focus="m")]
[name="祐天寺若麦"]好好待着，不要乱跑......吗？
[charslot]
[dialog]
若麦环顾自己的家——
如果它能被称为“家”的话。
客厅里永远只有一个人看的超大电视。
每天都有人来收拾的床铺，看上去永远都是崭新的。
突然，她的目光被一样东西所吸引。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_4185_amoris_1#7$3", focus="m")]
[name="祐天寺若麦"]找到了......
[Dialog]
[charslot]
也许并不是刻意遗忘，而是她不愿去寻找。
在某个时刻，是她自己选择放弃了它。
那是书柜角落里的一副鼓棒。
[charslot(slot="m",name="avg_4185_amoris_1#7$3", focus="m")]
[name="祐天寺若麦"]（敲击鼓棒）......一，二，三，四。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4185_amoris_1#4$4", focus="m")]
[name="祐天寺若麦"]......打得好烂。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="33_g7_reception",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[charslot]
[name="苍老的声音"]你放走了她。
[charslot]
[name="苍老的声音"]你违抗了我的命令。
[charslot(slot="m",name="avg_4186_tmoris_1#3$3", focus="m")]
[name="八幡海铃"]老爷，这次的交易算我违约，违约金在这。
[Dialog]
[charslot]
海铃从口袋中掏出了一袋金币，将它放在了老爷面前的桌上。
[charslot]
[name="苍老的声音"]......你拒绝了我。
[charslot(slot="m",name="avg_4186_tmoris_1#1$3", focus="m")]
[name="八幡海铃"]我想了很久，我们还是继续保持雇佣关系吧。
[charslot(slot="m",name="avg_4186_tmoris_1#1$3", focus="m")]
[name="八幡海铃"]我还是更适合独来独往，真要有什么作伴的话，我也想选我的贝斯。
[charslot]
[name="苍老的声音"]不，你想回去找弗朗西斯他们。
[charslot(slot="m",name="avg_4186_tmoris_1#1$3", focus="m")]
[name="八幡海铃"]......
[charslot(slot="m",name="avg_4186_tmoris_1#1$3", focus="m")]
[name="八幡海铃"]我对他们的音乐派对感兴趣很久了。对不起，你口中的更大的牌桌，我是没法坐上了。
[charslot]
[name="苍老的声音"]哈哈哈哈哈哈哈......我什么时候说让你上牌桌了？
[charslot]
[name="苍老的声音"]你从来都只是“筹码”。
[charslot(slot="m",name="avg_4186_tmoris_1#9$3", focus="m")]
[name="八幡海铃"]——！
[charslot]
[name="苍老的声音"]不握在自己手里的筹码，一文不值。
[Dialog]
[charslot]
老爷话音刚落，会客室的门立刻就被推开，一群身材健硕的打手将海铃团团围住。
海铃将目光移回老爷身上，一把铳已经明晃晃地对准了她。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="27_g24_cloudy_sea",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_sea", volume=0.6, loop=true, channel="sea")]
[Delay(time=1.5)]
小岛离船越来越远，就要从视野中消失。
[charslot(slot="m",name="avg_4184_dolris_1#12$2", focus="m")]
[name="三角初华"]......
[charslot(slot="m",name="avg_npc_1000_1#1$1",focus="m")]
[name="热心的船夫"]怎么啦，怎么一直回头看？
[charslot(slot="m",name="avg_4184_dolris_1#12$2", focus="m")]
[name="三角初华"]	刚才，我好像听见有谁在叫我......
[charslot(slot="m",name="avg_npc_1000_1#1$1",focus="m")]
[name="热心的船夫"]哈哈，肯定是你听错啦。这海上除了风浪声和羽兽声，还能有什么？
[name="热心的船夫"]（打量）你提这么多行李，是要去大城市打拼？
[charslot(slot="m",name="avg_4184_dolris_1#3$2", focus="m")]
[name="三角初华"]	......我要去找一个人。
[charslot(slot="m",name="avg_npc_1000_1#1$1",focus="m")]
[name="热心的船夫"]巧了，怎么又是一个要找人的......
[charslot(slot="m",name="avg_4184_dolris_1#7$2", focus="m")]
[name="三角初华"]	你说什么......？
[charslot(slot="m",name="avg_npc_1000_1#1$1",focus="m")]
[name="热心的船夫"]（大声）海浪突然变大了......
[charslot]
不知何时，头顶的天空变得昏暗起来。
[charslot(slot="m",name="avg_npc_1000_1#1$1",focus="m")]
[name="热心的船夫"]（更大声）危险......抓紧......护栏......
[Dialog]
[charslot]
可是一切为时已晚。
巨浪重重地砸在了甲板上，汹涌的海水瞬间灌入每一个舱室。
[Dialog]
[stopSound(channel="sea")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="65_g9_warmrabbitnest",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_wdnguitarstrum",volume=1)]
[Delay(time=4)]
[charslot(slot="m",name="avg_4183_mortis_1#6$3",focus="m")]
[name="若叶睦"]不对......不对......不对！
[charslot(slot="m",name="avg_4183_mortis_1#6$3",focus="m")]
[name="若叶睦"]吉他的声音......不对。
可是她心里非常明白，古典吉他永远发不出电吉他的声音。
[dialog]
[charslot]
[delay(time=2)]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[charslot]
[name="睦的父亲"]（小声）小睦，已经很晚了，该睡了哦？
[charslot]
[name="睦的父亲"]（小声）不管怎么说，请你先把房门打开吧......
[charslot]
[name="睦的母亲"]（小声）嗯，就和以前一样，我们陪在你的身边，给你讲睡前故事。
[charslot(slot="m",name="avg_4183_mortis_1#8$3",focus="m")]
[name="若叶睦"]......不要。
[charslot(slot="m",name="avg_4183_mortis_1#8$3",focus="m")]
[name="若叶睦"]除非你们告诉我，祥......她到底去哪了。
[charslot]
[name="睦的母亲"]这，我们也不知道啊......
[charslot]
[name="睦的母亲"]说不定，她也去了其他地方，找到了自己的幸福呢？
[charslot(slot="m",name="avg_4183_mortis_1#8$3",focus="m")]
[name="若叶睦"]......说谎。
[charslot(slot="m",name="avg_4183_mortis_1#8$3",focus="m")]
[name="若叶睦"]祥，不是那样的人。
[dialog]
[charslot]
[delay(time=2)]
门外一片寂静。
[charslot(slot="m",name="avg_4183_mortis_1#4$3",focus="m")]
[name="若叶睦"]祥不会这样轻易改变的，她想要我回到Ave{@nbs}Mujica——
[dialog]
[charslot]
[delay(time=0.3)]
[charslot(slot="m",name="avg_npc_1939_1#1$

... (全文23472字符)
```

### level_act45side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[skipnode(mode="nofirstskip")]
[interlude(channel = 2,clear = true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Dialog]
[Character]
[theater(mode=true)]
[Video(res="video/act45side/SS01.mp4")]
[Dialog]
[theater(mode=false)]
[skipnode(mode="skip")]
[Delay(time=2)]
[charslot]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Image(image="65_i12", screenadapt="coverall")]
[Delay(time=1)]
[Playmusic(key="$m_sys3_avemujica_loop", volume=0.6)]
最后一个音符落定，祥子的手仍停留在键盘上。
空荡荡的城堡里，还萦绕着方才音乐的微弱回响。
[name="？？？"]		......小，祥......？
许久未闻，却又再熟悉不过的声音在她的身旁响起。她缓缓抬起了头。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[name="丰川祥子"]	真的......终于......
[name="三角初华"]	......终于见面了呢，小祥。
[name="三角初华"]	感觉好像做了一个很长很长的梦，差点醒不过来。
[name="三角初华"]	小祥，我们真的兜兜转转了好久，差点又要错过了。
而站在祥子面前的，除了初华，还有其他的乐队成员。
[name="八幡海铃"]就好像被人拉了一把，然后就出现在了这里。
[name="祐天寺若麦"]哎呀~干嘛突然这么认真啦？
[name="若叶睦"]祥，你现在笑得很开心。
头顶的聚光灯闪烁着，晃得祥子有些睁不开眼，也让眼前的一切都显得那么不真实，就像又一场梦一样。
可她知道，她知道的——
她们再一次合奏了属于她们的歌。
Ave{@nbs}Mujica的大家，终于回来了。
[name="丰川祥子"]嗯！当然，我现在很开心......
[name="丰川祥子"]	初华......睦。
[name="丰川祥子"]	若麦......海铃。
[name="丰川祥子"]	我真的......很想你们。
[name="丰川祥子"]各位——欢迎回来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Background(image="65_g2_dreamcastlehall", screenadapt="coverall", block=true)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1937_1#2$1", focus="m")]
[PlaySound(key="$d_avg_yingying_ked_2", volume=1)]
[name="卡尔顿们"]（挣扎的哼唧声）
[dialog]
[PlaySound(key="$d_avg_magicchange", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=false)]
[charslot]
[charslot(slot="r",name="avg_4182_oblvns_1#13$1", focus="all",duration=1)]
[charslot(slot="l",name="avg_4184_dolris_1#7$1", focus="all",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="r",name="avg_4185_amoris_1#4$2", focus="all",duration=1)]
[charslot(slot="l",name="avg_4183_mortis_1#1$1", focus="all",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_4186_tmoris_1#1$1", focus="m",duration=1)]
[delay(time=2)]
[name="八幡海铃"]就是这些家伙让我们昏睡的吧？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1942_1#5$1",focus="m",duration=2)]
[delay(time=2)]
[name="莫菲丝"]	梦境，没有用了......
[charslot(slot="m",name="avg_npc_1942_1#5$1",focus="m")]
[name="莫菲丝"]	不......不行......
[charslot(slot="m",name="avg_npc_1942_1#14$1",focus="m")]
[name="莫菲丝"]	你们不能离开......你们必须......留在这里！
[charslot]
[charslot(slot="m",name="avg_npc_1937_1#2$1", focus="all")]
[name="卡尔顿们"]（尖锐的嘶鸣声）
[charslot]
[charslot(slot="m",name="avg_4182_oblvns_1#4$1", focus="m")]
[name="丰川祥子"]	——大家小心！
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1938_1#3$1", focus="m",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1942_1#5$1",focus="m")]
[name="莫菲丝"]	沃尔夫！！
[charslot(slot="m",name="avg_npc_1938_1#2$1", focus="m")]
[name="沃尔夫"]莫菲丝，别再错下去了！
[charslot(slot="m",name="avg_npc_1942_1#9$1",focus="m")]
[name="莫菲丝"]	别拿你刚从书里学来的话教训我！
[charslot(slot="m",name="avg_npc_1938_1#2$1", focus="m")]
[name="沃尔夫"]祥子，你带着她们——呃！
[dialog]
[charslot]
沃尔夫话音未落，密密麻麻的丝线瞬间刺穿了它的双臂，一缕缕棉花从孔洞中涌了出来。
[charslot(slot="m",name="avg_4185_amoris_1#4$1", focus="m")]
[name="祐天寺若麦"]啊！快看天上——
[dialog]
[charslot]
不计其数的卡尔顿在头顶的天空中纷飞，织出一张巨大的梦网。
梦网一点点朝少女们逼近，而且越来越大。
[charslot(slot="m",name="avg_npc_1938_1#2$1", focus="m")]
[name="沃尔夫"]莫菲丝......别再执迷不悟了！
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$e_skill_skulsrsword",volume=0.5,block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
一把巨大的剪刀从空中落下，梦网瞬间被剪碎成了一根根飘摇的丝线，散落在空中，纷纷扬扬。
[charslot(slot="m",name="avg_npc_1937_1#2$1", focus="m")]
[PlaySound(key="$d_avg_yingying_ked_2", volume=1)]
[name="卡尔顿们"]（慌乱的嘶鸣声）
[charslot(slot="m",name="avg_npc_1942_1#5$1",focus="m")]
[name="莫菲丝"]是谁？！
[dialog]
[charslot]
[PlaySound(key="$d_avg_magic_5")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[charslot]
[name="莫菲丝"]	唔——！
少女在空中抽搐了两下，紧接着从高空落下，速度越来越快——
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot="m",name="avg_npc_1938_1#1$1", posfrom="0,0",posto="300,0",afrom=1,ato=0,focus="m",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="l",name="avg_npc_1938_1#1$1", posfrom="-300,0",posto="150,0",afrom=0,ato=1,focus="all",duration=1)]
[delay(time=0.5)]
[charslot(slot="r",name="avg_npc_1942_1#5$1", posfrom="0,300",posto="0,30",afrom=0,ato=1,focus="all",duration=0.5)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[PlaySound(key="$punch_n1")]
[PlaySound(key="$bodyfalldown2", volume=1)]
[PlaySound(key="$d_avg_clothmovement")]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_4185_amoris_1#4$1", focus="m")]
[name="祐天寺若麦"]我、我们得救了？
[charslot(slot="m",name="avg_4186_tmoris_1#12$1", focus="m")]
[name="八幡海铃"]这到底是怎么回事......
[dialog]
[charslot]
[charslot(slot="l",name="avg_338_iris_1#8$1",focus="all",duration=1)]
[charslot(slot="r",name="avg_369_bena_1#11$1",focus="all",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_338_iris_1#8$1",focus="m")]
[name="爱丽丝"]抱歉，我们来晚了。
[charslot(slot="m",name="avg_4182_oblvns_1#13$1", focus

... (全文21812字符)
```

### level_act45side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="65_g1_rainystreet",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_traffic_amb", volume=1, loop=true, channel="a")]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_sidewalklight_red", volume=1, loop=true, channel="bgs")]
[StopSound(channel="bgs", fadetime=3.5)]
[StopSound(channel="a", fadetime=2)]
[delay(time=2.5)]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4185_amoris_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4185_amoris_1#1$1",focus="m")]
[name="祐天寺若麦"]啊哈，今天的化装舞会也很成功！
[name="祐天寺若麦"]你们注意到安可时大家激烈的欢呼声了吗？！有个孩子，一看就是喵姆亲的大粉丝！
[charslot(slot="m",name="avg_4185_amoris_1#3$1",focus="m")]
[name="祐天寺若麦"]我出场的时候，她的眼睛都变得闪闪发亮了！真是让人开心啊~
[name="祐天寺若麦"]等到下次舞会的时候，要不要再多增加些和粉丝的互动呢~
[Dialog]
[charslot]
[delay(time=0.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4182_oblvns_1#12$1",focus="m")]
[name="丰川祥子"]祐天寺小姐，研究如何增加魅力无所谓，但希望你不要忘记遵守Ave{@nbs}Mujica的世界观。
[charslot(slot="m",name="avg_4185_amoris_1#10$1",focus="m")]
[name="祐天寺若麦"]欸......祥子，这么怕我抢走观众的喜爱呀？
[name="祐天寺若麦"]我的粉丝只是沉浸在了Ave{@nbs}Mujica的化装舞会里罢了。让他们也迷上Mujica，这难道不好吗？
[charslot(slot="m",name="avg_4182_oblvns_1#3$1",focus="m")]
[name="丰川祥子"]哪怕是站姿，也属于表演的一部分。直到最后一秒，我们都不能松懈。
[charslot(slot="m",name="avg_4182_oblvns_1#12$1",focus="m")]
[name="丰川祥子"]我们的使命就是让被邀请来的客人沉醉在这场舞会里。
[name="丰川祥子"]为此，我们得将充满说服力的世界观全面地呈现给大家——
[charslot(slot="m",name="avg_4185_amoris_1#5$1",focus="m")]
[name="祐天寺若麦"]明白啦，明白啦。
[charslot(slot="m",name="avg_4185_amoris_1#8$1",focus="m")]
[name="祐天寺若麦"]不过呢~睦子登场的时候才是欢呼声最大的时候吧？
[name="祐天寺若麦"]“真开心啊~”“希望粉丝更多些~”睦子真的不会有这样的想法吗？
[charslot]
[charslot(slot="r",name="avg_4183_mortis_1#10$1",focus="r")]
[name="若叶睦"]我......没有......
[Dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#9$1",afrom=0,ato=1,duration=0.7,focus="m",isblock=true)]
[Delay(time=1)]
[name="丰川祥子"]请你不要煽动睦。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4184_dolris_1#13$1",focus="m",duration=1)]
[delay(time=1)]
[name="三角初华"]哈哈......大家不要这样......
[charslot(slot="m",name="avg_4185_amoris_1#1$1",focus="m")]
[name="祐天寺若麦"]我只是觉得大家应该都很期待下次的演出啦~
[charslot(slot="m",name="avg_4185_amoris_1#1$1",focus="m")]
[name="祐天寺若麦"]现在喜欢我们的人这么多，我们就应该乘胜追击，用百分之百的努力去回应他们。
[charslot(slot="m",name="avg_4184_dolris_1#13$1",focus="m")]
[name="三角初华"]这几天阁楼上的台灯一直亮到很晚才熄......小祥正在尽最大的努力制作新曲。
[charslot(slot="m",name="avg_4182_oblvns_1#7$1",focus="m")]
[name="丰川祥子"]这段时间以来，Ave{@nbs}Mujica的大家都在努力付出，我怎么能懈怠呢。
[charslot(slot="m",name="avg_4184_dolris_1#9$1",focus="m")]
[name="三角初华"]小祥......
[charslot(slot="m",name="avg_4185_amoris_1#3$2",focus="m")]
[name="祐天寺若麦"]祥子可不能把自己累坏了呀！
[charslot(slot="m",name="avg_4184_dolris_1#1$1",focus="m")]
[name="三角初华"]我们都能感受到小祥你的心意，我也会努力创作出与新曲相配的歌词。
[charslot(slot="m",name="avg_4186_tmoris_1#11$1",focus="m")]
[name="八幡海铃"]刚才演出前丰川同学给我听了样曲，是首不错的曲子。
[charslot(slot="m",name="avg_4184_dolris_1#1$1",focus="m")]
[name="三角初华"]我倒是觉得......节奏可以再慢一点？
[charslot(slot="m",name="avg_4185_amoris_1#4$1",focus="m")]
[CameraShake(duration=0.5, xstrength=8, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="祐天寺若麦"]欸？！你们都已经听过了吗？什么时候？！
[charslot(slot="m",name="avg_4184_dolris_1#1$1",focus="m")]
[name="三角初华"]就在刚才开演前，你好像没在休息室里？
[charslot(slot="m",name="avg_4182_oblvns_1#1$1",focus="m")]
[name="丰川祥子"]本来是想收集全体成员的意见，但因为时间紧迫就先给当时在场的人听了。
[charslot(slot="m",name="avg_4183_mortis_1#6$1",focus="m")]
[name="若叶睦"]若麦拉我去她的直播频道做客......我也没听到。
[charslot(slot="m",name="avg_4185_amoris_1#3$2",focus="m")]
[name="祐天寺若麦"]呃......！
[charslot(slot="m",name="avg_4182_oblvns_1#6$1",focus="m")]
[name="丰川祥子"]什么？！
[charslot(slot="m",name="avg_4182_oblvns_1#4$1",focus="m")]
[name="丰川祥子"]祐天寺，我不是说过不能——
[Dialog]
[charslot]
[PlaySound(key="$d_avg_sidewalklight_green", volume=1, loop=true, channel="bgs1")]
[StopSound(channel="bgs1", fadetime=2)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4185_amoris_1#4$2",focus="m")]
[name="祐天寺若麦"]绿、绿灯要亮起来了！我们赶紧走过去再说吧！
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(duration=0.6)]
[Delay(time=0.8)]
[charslot(slot="m",name="avg_4183_mortis_1#9$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4186_tmoris_1#11$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4182_oblvns_1#2$1",focus="m")]
[name="丰川祥子"]唉，真是头疼......
[charslot(slot="m",name="avg_4184_dolris_1#4$1",focus="m")]
[name="三角初华"]......真好啊。
[charslot(slot="m",name="avg_4182_oblvns_1#12$1",focus="m")]
[name="丰川祥子"]嗯？为什么突然这么说？
[charslot(slot="m",name="avg_4184_dolris_1#1$1",focus="m")]
[name="三角初华"]听了小祥你刚才的那番话，我也深有感触。
[name="三角初华"]经历了这么多，即使有争吵，我们五个人还能在一起组乐队......真好啊。
[name="三角初华"]虽然没有问过，但我相信，大家一定都是这么想的......尤其是我自己。
[charslot(slot="m",name="avg_4184_dolris_1#1$1",focus="m")]
[name="三角初华"]大家都很感激小祥。小睦也过得很开心，海铃和若麦也说她们在Mujica实现了自己的梦。
[charslot(slot="m",name="avg_4182_oblvns_1#14$1",focus="m")]
[name="丰川祥子"]......梦。
[Dialog]
[charslot(duration=0.3)]
[Delay(time=0.5)]
祥子顺着初华的视线望去，几个少女正嬉闹着穿过人行道。
她们无忧无虑，仿佛一切都和童话一样美好。
[charslot(slot="m",name="avg_4184_dolris_1#4$1",focus="m")]
[name="三角初华"]至于我自己，能被小祥你这样信任，真的很开心。
[name="三角初华"]真想把我的人生都奉献给Mujica！
[charslot(slot="m",name="avg_4184_dolris_1#1$1",focus="m")]
[name="三角初华"]一切都和以前一样......感觉就像做梦似的。
[stopmusic(fadetime=1)]
[charslot(slot="m",name="avg_4182_oblvns_1#14$1",focus="m")]
[name="丰川祥子"]欸......
[name="丰川祥子"]......做梦？
[dialog]
[charslot(duration=0.3)]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[focusout(duration=1.5, type="bg", from=0

... (全文25213字符)
```

### training_act45side_01_a

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true)]
[popupdialog(dialogHead="$avatar_vigna")]月色真好......这里能有什么样的危险呢？
[popupdialog(dialogHead="$avatar_huang")]小心点，听说在这座城堡之中，很多造物都会因为这月光“活过来”。
[tutorial(focusWidth=140, focusHeight=140, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_huang", tileY=3, tileX=6)]别看它现在静悄悄地待在角落里，攻击也<@tu.kw>无法对它造成可观的伤害</>......
[battle.pause(pause=false)]
```

### training_act45side_01_b

```
[header(is_tutorial=true)]
[battle.delay(time=0.3)]
[battle.pause]
[inputblocker(blockInput=true, black=0.3)]
[tutorial(focusWidth=140, focusHeight=140, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_huang", tileY=3, tileX=5)]但要是被月光照射一段时间，它就会更快地变成有意识的活物。
[popupdialog(dialogHead="$avatar_huang")]活过来的造物对来客抱有很强的敌意，可不要被它可爱的外表迷惑！
[battle.pause(pause=false)]
```

### training_act45side_01_c

```
[header(is_tutorial=true)]
[battle.pause]
[popupdialog(dialogHead="$avatar_vigna")]唔呃！又从哪里冒出来这么多造物！
[popupdialog(dialogHead="$avatar_huang")]看起来在月光下它们不仅很快有了意识，行动也比在没有光照的地方迅猛得多。
[tutorial(focusWidth=140, focusHeight=140, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_huang", tileY=3, tileX=1)]接下来的作战里我们也许可以利用这一点，挡住这些光线应该能帮我们获得优势。
[battle.pause(pause=false)]
```

### training_act45side_01_d

```
[battle.pause]
[popupdialog(dialogHead="$avatar_huang")]接下来的作战里我们也许可以利用这一点，挡住这些光线应该能帮我们获得优势。
[battle.pause(pause=false)]
```

### training_act45side_01_e

```
[header(is_skippable=true, is_tutorial=true)]
[battle.delay(time=0.3)]
[battle.pause]
[inputblocker(blockInput=true, black=0.3)]
[tutorial(focusWidth=140, focusHeight=140, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_vigna", tileY=5, tileX=4)]这是......钟声？我没有听错吧？那个立在大厅中央的钟表盘，难道也是活物？
[tutorial(focusWidth=140, focusHeight=140, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_huang", tileY=5, tileX=4)]不，它上面转动的光影只是在指示现在城堡内部的时间，依附在上面快要破茧而出的东西才是真正的威胁。
[tutorial(focusWidth=140, focusHeight=140, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_huang", tileY=5, tileX=4)]不过要是钟声响起，就说明月亮的位置快改变了，要注意光线的变化。
[battle.pause(pause=false)]
```

### training_act45side_01_f

```
[header(is_skippable=true, is_tutorial=true)]
[battle.pause]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_vigna")]果然，月亮照过来的方向和刚才不一样了！
[popupdialog(dialogHead="$avatar_huang")]准备好战斗！别忘了，这些造物在月光下会格外凶狠，注意自己的位置！
[battle.pause(pause=false)]
```


## 统计

- 总字符数：280688
- 对话行数：1877


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
