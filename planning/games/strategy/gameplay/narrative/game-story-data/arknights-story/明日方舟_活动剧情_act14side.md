# 明日方舟 · 活动剧情 · act14side（25段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act14side」完整剧情脚本（25个文件，4151行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act14side
- 脚本文件数：25

### level_act14side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bgs")]
[Image(image="24_i01", fadetime=2, xScale=1.3, yScale=1.3)]
[ImageTween(image="24_i01", tiled=true, xScaleTo=1.0, yScaleTo=1.0, duration=25, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="外力。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一点微小的外力。只要这轻轻一推......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="雪崩就会掩埋整个谢拉格，包括它所隐瞒的阴谋和发生过的一切。", x=300, y=350, alignment="center", size=24, delay=0.04, width=750)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[StopSound(channel="bgs", fadetime=1)]
[delay(time=3)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[stopmusic(fadetime=1)]
[Character]
[theater(mode=true)]
[Background(screenadapt="showall", image="24_g9_manoravenue",x=0, y=-50, xScale=1.3, yScale=1.3)]
[backgroundTween(xFrom=0, yFrom=-50, xTo=0, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=5, block=false)]
[Delay(time=2)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2.5)]
[theater(mode=false)]
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]老板，只是块破木牌而已，为什么卖五十镑这么贵？
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]客人，这您就不懂了，这可不是什么普通的木牌，这是雪境之神耶拉冈德的祝福。
[name="谢拉格商人"]谢拉格能够免受天灾侵袭，扎根于这片土地，都是多亏了祂的庇佑。
[name="谢拉格商人"]而这块护符的原材料，可是取自我们谢拉格第二高的山峰少女峰峰顶的常绿乔木。
[name="谢拉格商人"]少女峰您知道吗？传说啊，那座峰是耶拉冈德流下的眼泪结冰而成的。
[name="谢拉格商人"]受山上雪水浇灌的树木满含着耶拉冈德对这片土地的慈爱与祝福，用这木料制成的护符更是能保佑出入平安，祛灾辟邪。
[name="谢拉格商人"]看您是第一次来谢拉格，想要给在维多利亚的家人带一些纪念品吧？
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]你怎么知道？
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]哎呀，这两年，被恩希欧迪斯老爷的政策吸引来的大公司员工越来越多了，您的口音我一听就听出来了。
[name="谢拉格商人"]像您这样初来乍到的人呢，我是特别推荐您购买这个护符作为纪念品的。
[name="谢拉格商人"]不知您有没有听说过山雪鬼？是我们这儿深山里头的食人怪物，面目狰狞，似人非人，神出鬼没。
[name="谢拉格商人"]但只要您戴着这受了蔓珠院赐福的护符，它们就会在耶拉冈德的威光下畏缩，不能伤你哩。
[name="谢拉格商人"]您想，您带回去和您的家人说，这护符有谢拉格圣山的神力庇佑，也有面子不是？
[name="谢拉格商人"]您大老远跑到谢拉格出差，也不想回去没有什么好东西带给家人吧？
[dialog]
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]......
[name="出差的经理"]......啧，好吧，我买了，给我的老婆孩子各买一块！
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]好嘞，就喜欢您这样豪爽的人！
[dialog]
[character]
[delay(time=1)]
[name="？？？"]我看啊，这木材恐怕是随便找个山头砍来的吧。
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="谢拉格商人"]？！
[dialog]
[character]
[PlaySound(key="$d_avg_snowbootwalk")]
[character(name="avg_173_slchan_1",fadetime=1.5)]
[delay(time=3)]
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]你、你凭什么这么说？！
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]首先，没有佩尔罗契家的许可，根本没有人可以攀爬少女峰。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]其次，我可从没听说过之前有人爬上过少女峰。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]我离开谢拉格的时候，还特意嘱咐过魏斯哥，要是有人爬上去了给我报个信呢。
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]你怎么知道......
[name="谢拉格商人"]等等，这个尾巴......您难道是恩希亚小姐？！
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]恩希亚......你、您是恩希欧迪斯先生的妹妹？！
[character(name="avgnew_173_slchan_1#2$1")]
[name="恩希亚"]嗯哼？
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]喂，老板，你难道真的在骗我？！
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]哎呀，哈哈哈，听说恩希亚小姐自幼热爱登山，对于雪山的了解果然比我们普通人要强。
[name="谢拉格商人"]我店里的这些货其实也是从山上的猎人那里进的，肯定是那些猎人骗了我。
[name="谢拉格商人"]我之后就去找他们算账！
[name="谢拉格商人"]至于这个护符......恩希亚小姐，您看？
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]这个护符有蔓珠院的赐福倒不假，没有谢拉格人胆敢伪造蔓珠院的印信冒犯耶拉冈德。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]想凭它抵挡传闻中的山雪鬼就算了吧。不过当作纪念品带回去的话，我觉得应该还是很合适的。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]所以，卖便宜点就好啦。
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]呼......既然如此，我这就把定价改成十镑！那，这位先生，您还买吗？
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]既然那位恩希欧迪斯先生的妹妹都这么说了，我肯定是相信的。
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=1)]
[name="出差的经理"]老板你做生意也不容易，我买五个吧！
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]好的好的。
[character(name="avg_npc_222",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人"]恩希亚小姐呢，您要买一些什么吗？只要是您喜欢的，您随便拿就是，毕竟我这生意也是受了希瓦艾什家的照顾。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]不用不用，我正常付钱就好。
[character(name="avgnew_173_slchan_1#10$1")]
[name="恩希亚"]对吧，博士？
[dialog]
[Character(name="avgnew_173_slchan_1#10$1",focus=-1)]
[Decision(options="当然。;幸好特意换了不少维多利亚和卡西米尔货币。;既然是自家的领地，不能随便拿吗？", values="1;2;3")]
[Predicate(references="1")]
[Predicate(references="2")]
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]哎呀，反正换了再多，也只能在我们家的领地用。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]而我们家的领地中，最繁荣的就是这座贸易港了，所以博士你就算把钱全都花在这里也没关系的。
[Predicate(references="3")]
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]欸，博士，别人也是要做生意的呀。
[character(name="avgnew_173_slchan_1#10$1")]
[name="恩希亚"]不过，你要是真的想，我们可以去拜托老哥试试看。反正老哥会处理好的！
[Predicate(references="1;2;3")]
[dialog]
[character]
[PlaySound(key="$d_avg_snowbootwalk")]
[Character(name="char_198_blackd_1",fadetime=1)]
[delay(time=1)]
[name="魏斯"]二小姐，我们差不多该去车站等车了。
[character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]啊，现在时间紧，博士，我们出发吧。
[dialog]
[PlaySound(key="$d_avg_snowbootwalk")]
[character(fadetime=1.5)]
[delay(time=

... (全文17251字符)
```

### level_act14side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g3_mainhall",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]啧，真慢。
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#7$1",focus=2)]
[name="菈塔托丝"]休露丝，安静一点，你打断了我的思路。
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#7$1",focus=1)]
[name="休露丝"]还有什么好想的，恩希欧迪斯这次必须把他的地交出来。
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]尤卡坦，你怎么想？
[character(name="avg_npc_263_1#2$1")]
[name="尤卡坦"]......我和露丝意见一致，只不过，恩希欧迪斯老爷不会善罢甘休。
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]你至少没你老婆这么说话不过脑子。
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]你说谁说话不过脑子？！
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]当然是在说你，我的好妹妹。
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]要不是阿克托斯这个莽汉一遇到和圣山有关的事情就坐不住，我可不想这么早就和恩希欧迪斯翻脸。
[name="菈塔托丝"]恩希欧迪斯这种人呢，就算他死，也至少会带走你半条命，更何况......
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#2$1",focus=2)]
[name="菈塔托丝"]我怎么这么不信，他会认命呢。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#2$1",focus=1)]
[name="休露丝"]哼，要我说......
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]我说了安静一点，休露丝。你要是真的非要说点什么，可以出去，然后对着群山说个够。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]当然，我不会允许你再进来。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]啧，知道了，我闭嘴还不行吗。
[name="休露丝"]（低声）自己说得这么开心。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_253_1#11$1",focus=2)]
[name="菈塔托丝"]......
[character(name="avg_npc_268")]
[name="修士"]阿克托斯老爷到。
[dialog]
[character]
[musicvolume(volume=0, fadetime=2)]
[delay(time=2)]
[PlaySound(key="$d_avg_gateopen", volume=0.8)]
[delay(time=1.5)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6)]
[playsound(key="$d_gen_walk_n")]
[delay(time=2)]
[character(name="avg_npc_254_1#1$1",fadetime=1.5)]
[delay(time=2)]
冬日的圣山峰顶，寒风从不断绝，但阿克托斯的眼神，以及他手中巨斧偶尔摩擦到地面的声响却让人产生错觉——仿佛寒风皆是因他而起。
[dialog]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]瞧瞧是谁来了，阿克托斯，我的好朋友。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]恩希欧迪斯呢？
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]你问我，我问谁？
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]我还以为你们会碰上，然后直接在外面把事情解决了，我就不用坐在这里烦心，可以高高兴兴回家了。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]想不到还有能让你菈塔托丝烦心的事。
[character(name="avg_npc_253_1#7$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]当然有，我烦心的事多得很。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]比如说，我领地内越来越多的人想要去恩希欧迪斯那儿打工赚钱。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]又比如说，你手下最得力的将领，古罗，今天怎么没有来？
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#9$1",focus=2)]
[name="阿克托斯"]他感冒了。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#9$1",focus=1)]
[name="菈塔托丝"]谢拉格最强壮的战士会感冒，这可不是个好兆头。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#9$1",focus=1)]
[name="菈塔托丝"]看来，得让恩希欧迪斯手下的那位诺希斯帮他治疗一下了。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]他会自己好起来。
[character(name="avg_npc_253_1#10$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]好吧好吧。当我好心没好报。
[character(name="avg_npc_253_1#10$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]既然你来了，那么，就剩下恩希欧迪斯了。
[dialog]
[character]
[name="？？？"]三点的钟声还未响起。
[name="恩希欧迪斯"]久等了，两位。
[character(name="avg_npc_268")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="修士"]恩、恩希欧迪斯老爷与大长老到！
[character(name="avg_npc_253_1#4$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]嗯？
[name="菈塔托丝"]啧，稀奇了，这两人是怎么会一同......
[dialog]
[character(fadetime=0.5)]
[delay(time=1)]
[character(name="avg_npc_258_1#1$1",name2="avg_172_svrash_1#1$1",fadetime=1.5)]
[playsound(key="$d_gen_walk_n")]
[PlaySound(key="$d_gen_walk_n",delay=0.2,channel="R",volume=1,block=true)]
[SoundVolume(channel="R", volume=0, fadetime=0.2)]
[delay(time=3)]
[character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]恩希欧迪斯，难不成在来开会前，你先去向圣女祈祷了？
[character(name="avg_npc_258_1#1$1",name2="avg_172_svrash_1#10$1",focus=2)]
[name="恩希欧迪斯"]哪里，路上偶遇大长老，就与大长老聊了几句。
[name="恩希欧迪斯"]大长老，您先请。
[character(name="avg_npc_258_1#1$1",name2="avg_172_svrash_1#10$1",focus=1)]
[name="大长老"]有礼了。
[dialog]
[character]
[musicvolume(volume=0, fadetime=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[background]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="24_i03", fadetime=2)]
[ImageTween(image="24_i03", tiled=true, xScaleTo=1.0, yScaleTo=1.0, duration=25, block=false)]
[delay(time=2)]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_gatecloz", volume=1)]
大殿的正门缓缓关上，殿内的空气霎时安静下来。
大长老端坐中央，阿克托斯与菈塔托丝站在一侧，而恩希欧迪斯站在另一侧。
泾渭分明，一目了然。
[name="大长老"]以往的三族议会，历来是大家坐在一起，聊一聊今年的各种行事谁家多出一点力，谁家遭了雪难需要援助。
[name="大长老"]没想到现在会上的议题......唉。
[playMusic(intro="$longmenoffice_intro", key="$longmenoffice_loop", volume=0.4)]
[name="阿克托斯"]这就得好好问问恩希欧迪斯了。
[name="恩希欧迪斯"]不用这么咄咄逼人，阿克托斯。
[name="恩希欧迪斯"]如大长老所说，三族议会不该是我们互相指责谩骂的地方。
[name="菈塔托丝"]好一个恶人先告状啊，恩希欧迪斯。
[name="大长老"]罢了罢了。既然人已到齐，那就开始这一次的三族议会吧。
[name="大长老"]耶拉冈德在上。
[name="所有人"]耶拉冈德在上。
[dialog]
[character]
[image(fadetime=2)]
[background]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=

... (全文38280字符)
```

### level_act14side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g9_manoravenue",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]洛拉，一回家就帮忙干活，真孝顺啊。
[character(name="avg_422_aurora_1#1$1")]
[name="极光"]哪里，是我应该做的，我也想到处走走。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]哎，出去学习过的就是不一样，比我弟弟懂事多了。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]多好的一个姑娘，真可惜。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]搬家之后，不知道还找不找得到你这么好的姑娘了。
[character(name="avg_422_aurora_1#2$1")]
[name="极光"]欸，莎莎姐，你不是在这里住得好好的吗，怎么要搬家啦？
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]还不是我爸。昨天不是三族议会上宣布要让圣女来管三大家吗？
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]我爸这不就来劲了。
[character(name="avg_422_aurora_1#4$1")]
[name="极光"]啊......佐尔叔一直都反对恩希欧迪斯老爷的开放政策呢......
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]可不是嘛，当年我们一家是为了我弟和我的工作从北边搬过来。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]本来呢，这些年磨着磨着，我爸也差不多习惯了。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]结果昨天还政这事一宣布，他可高兴了。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]昨晚吃饭的时候就一直在骂恩希欧迪斯老爷这些年做的事，我都听烦了，还跟他吵了一架。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]但也拗不过老头子，说不定我们家就要搬回佩尔罗契家的领地去了。
[character(name="avg_422_aurora_1#2$1")]
[name="极光"]那你弟弟的工作呢？
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]谁知道呢，这次还政完，不知道图里卡姆能不能还像以前那样做生意呢。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]我听佩尔罗契那边的说法啊，本来上次三族议会上也是圣女大人要恩希欧迪斯老爷交出谷地和矿区呢。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]要是圣女大人来管谢拉格，恩希欧迪斯老爷估计讨不了好吧。
[character(name="avg_422_aurora_1#3$1")]
[name="极光"]......也是。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]不过，这也是好事。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]你这几年在外面可能不知道，一开始三大家族之间还挺配合的，但是最近啊，他们互相是越来越不对付。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]上次议会之后很多人都觉得怕是要打起来了。
[character(name="avg_422_aurora_1#1$1")]
[name="极光"]......是呢，没想到这次恩希欧迪斯老爷居然让步了，而且是让圣女大人来掌权。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]对啊，不过要我说，早该这么办了，虽然我不讨厌恩希欧迪斯老爷的开放政策，毕竟我们家也跟着赚了不少钱。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]但是，有的时候也确实觉得和老人们说的一样，谢拉格变得不再像谢拉格了。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]现在恩希欧迪斯老爷决定让步，事情别闹太大，大家都是赞成的。
[character(name="avg_npc_280_1#1$1")]
[name="邻居"]大概也就你哥那种老顽固反对了。
[character(name="avg_422_aurora_1#4$1")]
[name="极光"]我哥......
[Dialog]
[musicvolume(volume=0.2, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_422_aurora_1#9$1")]
[name="极光"]我回来了。
[character(name="avg_npc_276_1#1$1")]
[name="极光的姐姐"]唉，傻孩子，说了让你回来就好好休息，非要干活。
[name="极光的姐姐"]（轻声）你这个什么石什么病的，你不心疼自己的身体状况，我们还心疼得紧呢。
[character(name="avg_422_aurora_1#9$1")]
[name="极光"]没事，姐，这点活还不碍事。
[character(name="avg_422_aurora_1#2$1")]
[name="极光"]咦，哥哥呢？
[character(name="avg_npc_276_1#1$1")]
[name="极光的姐姐"]他说要去一趟工厂，刚才急匆匆地出门了，还说今天不会回来了。
[character(name="avg_422_aurora_1#2$1")]
[name="极光"]工厂？
[PlaySound(key="$transmission",volume=0.6)]
[delay(time=1)] 
[stopmusic(fadetime=2)]
[character(name="avg_422_aurora_1#2$1")]
[name="极光"]是队长？
[dialog]
[character]
[Character(name="char_empty",name2="avg_422_aurora_1#2$1",focus=2)]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[CharacterCutin(widgetID="1", name="avg_npc_252", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[Character(name="char_empty",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]队长，有什么事吗？
[Character(name="char_empty",name2="avg_422_aurora_1#1$1",focus=-1)]
[name="Sharp"]假期结束了，极光。
[Character(name="char_empty",name2="avg_422_aurora_1#1$1",focus=-1)]
[name="Sharp"]博士昨天在车站被佩尔罗契家的人接走了。
[Character(name="char_empty",name2="avg_422_aurora_1#2$1",focus=2)]
[name="极光"]哎？！
[Character(name="char_empty",name2="avg_422_aurora_1#2$1",focus=-1)]
[name="Sharp"]博士是自愿和他们走的，你应该明白我的意思，他多半有什么计划了。
[Character(name="char_empty",name2="avg_422_aurora_1#2$1",focus=-1)]
[name="Sharp"]我大致看了一下地图，从车站到佩尔罗契家要一段时间。
[Character(name="char_empty",name2="avg_422_aurora_1#2$1",focus=-1)]
[name="Sharp"]现在，博士现在应该已经到佩尔罗契家了，我们也该行动了。
[Character(name="char_empty",name2="avg_422_aurora_1#2$1",focus=-1)]
[name="Sharp"]我现在借口去你家看看状况，然后出来和你会合。
[Character(name="char_empty",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]好的。
[dialog]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[CharacterCutin(widgetID="1",block=true)]
[delay(time=1)]
[character(name="avg_422_aurora_1#4$1")]
[name="极光"]......先去和队长会合吧。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_npc_251")]
[name="耶拉"]原来如此，你就是那个罗德岛的人啊。
[dialog]
[character(name="avg_npc_251",focus=-1)]
[Decision(options="原来你不认识我。;你并不是特意找上我的。", values="1;2")]
[Predicate(references="1;2")]
[character(name="avg_npc_251")]
[name="耶拉"]是啊。
[character(name="avg_npc_251")]
[name="耶拉"]你很独特，但我也不知道你为什么很独特。
[dialog]
[character(name="avg_npc_251",focus=-1)]
[Decision(options="你在市场说的，是什么意思？", values="1")]
[Predicate(references="1")]
[character(name="avg_npc_251")]
[name="耶拉"]嗯？
[character(name="avg_npc_251")]
[name="耶拉"]一点忠告而已。
[character(name="avg_npc_251")]
[name="耶拉"]你看，结果不是得被一群陌生人盯着，连出门逛逛都不自在吗？
[dialog]
[character(name="avg_npc_251",focus=-1)]
[Decision(options="你知道些什么？", values="1")]
[Predicate(references="1")]
[character(name="avg_npc_251")]
[name="耶拉"]在回答你这个问题之前，先告诉我，你来谢拉格是为了什么？
[dialog]
[character(name="avg_npc_251",focus=-1)]
[Decision(options="出于和喀兰贸易的商业合作。;帮崖心修

... (全文21225字符)
```

### level_act14side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g8_nobleroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]居然真敢独自来到我们布朗陶家的领地，胆子不小啊，埃德怀斯家的诺希斯。
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]我行事向来坦荡。
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]哼，因为一些愚蠢的小动作而被逐出喀兰贸易的叛徒，也好意思说自己坦荡。
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]我以为在这里的会是菈塔托丝。
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]凭几句谁都能说的大话，菈塔托丝怎么可能那么轻易就相信你。
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#2$1",focus=2)]
[name="诺希斯"]......
[character(name="avg_npc_262_1#1$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]我应该说过，合作需要双方的诚意。看起来我的话已经传到了她那里，这就足够了。
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]装腔作势。
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]说吧，既然你敢亲自来这里，你上次说的事已至此，究竟是什么意思？
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]哪件事？又是至了哪个此？
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#6$1",focus=2)]
[name="诺希斯"]唉。
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#6$1",focus=2)]
[name="诺希斯"]你认为，恩希欧迪斯为什么会提出还政？
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#6$1",focus=1)]
[name="休露丝"]哼，当然是因为他斗不过佩尔罗契家还有我们布朗陶家，所以选择了妥协。
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#5$1",focus=2)]
[name="诺希斯"]妥协？
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]呵，妥协。
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]再想想，休露丝夫人。我敢说，你的姐姐不是这么想的。
[character(name="avg_npc_262_1#7$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]自从恩希欧迪斯回到谢拉格，他可有哪一步行动不是为了制胜？由他提出的还政当真会是一种妥协？
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#9$1",focus=1)]
[name="休露丝"]......
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]提示是——大典。
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="休露丝"]......？大典又怎么了？他还能当众耍赖，不交出权力不成？
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]大典在即，出入希瓦艾什家领地，运载物资与人员的列车远比平时频繁。
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]猜猜看，恩希欧迪斯为什么会主动提出要交权给圣女，并顺理成章地把日期定在大典？
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]阿克托斯目光短浅，满心以为恩希欧迪斯定会在权力的让渡上做些小动作。
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]先是把人手都调到谷地和矿区，又严加监视恩希欧迪斯请来的那位博士。
[character(name="avg_npc_262_1#9$1",name2="avg_206_gnosis_1#7$1",focus=2)]
[name="诺希斯"]可笑的是他全然不知，这都不过是些无用功！
[character(name="avg_npc_262_1#4$1",name2="avg_206_gnosis_1#7$1",focus=1)]
[name="休露丝"]......！！
[dialog]
[character]
休露丝一瞬间将视线投向房间中的某个方向，那个方向只有一面空无一物的墙板，而这个动作被捕捉到了。
诺希斯径直地看向那面墙板。
[character(name="avg_206_gnosis_1#7$1")]]
[name="诺希斯"]菈塔托丝，你不会蠢到想不到这一层。
[character(name="avg_206_gnosis_1#7$1")]]
[name="诺希斯"]恩希欧迪斯到底在盘算些什么，我会告诉你。
[character(name="avg_206_gnosis_1#7$1")]]
[name="诺希斯"]但是，下一次你最好亲自来见我。
[character(name="avg_206_gnosis_1#7$1")]]
[name="诺希斯"]否则，哪怕要我坐等恩希欧迪斯的奸计得逞，看着你们成为他的阶下囚——
[character(name="avg_206_gnosis_1#4$1")]]
[name="诺希斯"]我也决不会接受第二次这样的戏弄。
[dialog]
[character]
[name="墙板"]......
[character(name="avg_206_gnosis_1#2$1")]]
[name="诺希斯"]告辞。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[PlaySound(key="$doorclosequite")]
[delay(time=1)]
[character(name="avg_npc_262_1#7$1")]]
[name="休露丝"]......菈塔托丝。
[character(name="avg_npc_262_1#8$1")]]
[name="休露丝"]喂，菈塔托丝，我知道你在里面！
[dialog]
[character]
[name="墙板"]......别吵了，休露丝。
随着一阵震动声，墙板缓缓移开，坐在其中的菈塔托丝缓缓站起，走了出来。
[Dialog]
[stopmusic(fadetime=2)]
[Character(name="char_empty", name2="avg_npc_262_1#7$1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#7$1",fadetime=0.7)]
[delay(time=1.5)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#7$1",focus=2)]
[name="休露丝"]你觉得他说的是真的吗？
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#7$1",focus=1)]
[name="菈塔托丝"]倒不如说，你没有想过这种可能性才令我感到吃惊，我的妹妹。
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#8$1",focus=2)]
[name="休露丝"]可如今就连圣女也自己选择站在我们这一边！
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#8$1",focus=2)]
[name="休露丝"]恩希欧迪斯他难道能不择手段到......
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#8$1",focus=1)]
[name="菈塔托丝"]不择手段到？
[Character(name="avg_npc_253_1#7$1", name2="avg_npc_262_1#8$1",focus=1)]
[name="菈塔托丝"]别傻了，休露丝。
[Character(name="avg_npc_253_1#7$1", name2="avg_npc_262_1#8$1",focus=1)]
[name="菈塔托丝"]从恩希欧迪斯蔑视信仰，大肆开挖山道把铁路铺进谢拉格，并与圣女决裂开始......
[Character(name="avg_npc_253_1#7$1", name2="avg_npc_262_1#8$1",focus=1)]
[name="菈塔托丝"]不，从他最初坦然接受让他的妹妹成为圣女，换来回归三族议会的机会开始，他就根本不在乎。
[Character(name="avg_npc_253_1#7$1", name2="avg_npc_262_1#8$1",focus=1)]
[name="菈塔托丝"]早年他们兄妹间的手足之情我们有目共睹，我也曾以为让本就虔诚的恩雅成为蔓珠院的人质会是一着妙手。
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#8$1",focus=1)]
[name="菈塔托丝"]但现在，呵，他就是哪天带人上山把蔓珠院烧了，我都不会觉得奇怪。
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#7$1",focus=2)]
[name="休露丝"]......难道说，恩希欧迪斯真的打算用武力......
[Character(name="avg_npc_253_1#1$1", name2="avg_npc_262_1#7$1",focus=1)]
[name="菈塔托丝"

... (全文21990字符)
```

### level_act14side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",focus=1)]
[name="Sharp"]汇报情况。
[character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]情况不太对，博士猜得没错，这边聚集了很多人。
[character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",focus=1)]
[name="Sharp"]他们是向着工厂那边进发的？
[character(name="avg_npc_252",name2="avg_422_aurora_1#5$1",focus=2)]
[name="极光"]是......我确定。
[character(name="avg_npc_252",name2="avg_422_aurora_1#5$1",focus=1)]
[name="Sharp"]想办法跟上，随时报告。
[character(name="avg_npc_252",name2="avg_422_aurora_1#5$1",focus=2)]
[name="极光"]收到。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g9_manoravenue",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_267_1#1$1")]
[name="切斯特"]那么这所工厂的交接也完成了。
[character(name="avg_npc_267_1#7$1")]
[name="切斯特"]目前为止都进行得很顺利，多亏了博士您的调停。
[character(name="avg_npc_267_1#7$1")]
[name="切斯特"]之前可能有点怠慢了，真是不好意思。
[dialog]
[character(name="avg_npc_267_1#7$1",focus=-1)]
[Decision(options="别在意，我只是个学者。", values="1")]
[Predicate(references="1")]
[character(name="avg_npc_267_1#8$1")]
[name="切斯特"]哎呀，您可别这么谦虚，以后还有很多事情需要请教您。
[character(name="avg_npc_261_1#6$1")]
[name="瓦莱丝"]且慢。
[character(name="avg_npc_267_1#4$1")]
[name="切斯特"]呃，瓦莱丝将军是对此有什么疑问吗？
[stopmusic(fadetime=2)]
[character(name="avg_npc_261_1#6$1")]
[name="瓦莱丝"]有埋伏。
[Dialog]
[PlaySound(key="$d_avg_snowbootwalk")]
[PlaySound(key="$d_avg_snowbootwalk",delay=0.2)]
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1")]
[delay(time=2)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]不愧是瓦莱丝将军。
[character(name="avg_npc_261_1#6$1")]
[name="瓦莱丝"]什么人？
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]来讨说法的人。
[character(name="avg_npc_267_1#5$1")]
[name="切斯特"]诸位，魏斯和博士方才应该已经向领民代表们传达过喀兰贸易的措施了。
[character(name="avg_npc_267_1#5$1")]
[name="切斯特"]我想，其中一定是有什么误会......
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]误会？
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]切斯特先生，你恐怕还不明白。
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]恩希欧迪斯老爷被这个外国人骗了！
[dialog]
[character(name="avg_npc_284_1#1$1",focus=-1)]
[Decision(options="你说什么？", values="1")]
[Predicate(references="1")]
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]我们原先也都被蒙在鼓里，直到有人告诉了我们才明白过来。
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]切斯特先生应该知道，原本这个外国人来谢拉格的名头，是要担任矿石病和感染者处理方式的顾问。
[character(name="avg_npc_261_1#5$1")]
[name="瓦莱丝"]你什么意思？
[character(name="avg_npc_267_1#6$1")]
[name="切斯特"]......
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]线人的情报不会错的。
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]这个外国人已经和阿克托斯达成了合作，而瓦莱丝将军则是负责监视他的人。
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]谁不知道，蔓珠院和阿克托斯早已不满恩希欧迪斯老爷对谢拉格的开拓。
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]这个外国人，会以工厂会传播矿石病为理由，大量提供对老爷不利的证据，永久关闭工厂！
[character(name="avg_npc_261_1#6$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="瓦莱丝"]这是污蔑！佩尔罗契家何曾做过这等见不得光的事！
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]佩尔罗契家与蔓珠院互相勾结，见不得光的事和牺牲的人还少吗？！
[character(name="avg_npc_261_1#2$1")]
[name="瓦莱丝"]......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_npc_261_1#2$1")]
[name="瓦莱丝"]父亲，父亲！你还好吗？
[character(name="avg_npc_258_1#1$1")]
[name="大长老"]来，喝了它吧，喝下去就好了。
[character(name="avg_npc_258_1#1$1")]
[name="大长老"]耶拉冈德的眼泪会洗净山雪鬼留下的邪毒。
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="24_g9_manoravenue",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_261_1#6$1")]
[name="瓦莱丝"]......你有什么证据！
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]我呸，你们自己干的破事，还要来问我？
[character(name="avg_npc_267_1#5$1")]
[name="切斯特"]博士，这......
[dialog]
[character(name="avg_npc_267_1#5$1",focus=-1)]
[Decision(options="不是真的。;......;你觉得呢？", values="1;2;3")]
[Predicate(references="1")]
[character(name="avg_npc_267_1#2$1")]
[name="切斯特"]......我可以相信吗？
[Predicate(references="2")]
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]怎么，说不出话了？
[Predicate(references="3")]
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]少在这里油嘴滑舌的！
[Predicate(references="1;2;3")]
[stopmusic(fadetime=2)]
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]不必多说了，我要你给我们一个交代！
[PlayMusic(intro="$epic_intro", key="$epic_loop", volume=0.4)]
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_261_1#6$1")]
[name="瓦莱丝"]卫兵！保护客人！把他们拿下！
[character(name="avg_npc_284_1#1$1")]
[name="武装的领民"]先抓住那个外国人！
[dialog]
[Dialog]
[PlaySound(key="$d_avg_snowrun", channel="slide",loop=true,volume=0.8)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=100, fadetime=

... (全文16437字符)
```

### level_act14side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g11_snowylane",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=1)]
[name="迟钝的战士"]哎，听说，要咱们监视的这位叫什么博士的贵客，被希瓦艾什家那边的人袭击了？
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=2)]
[name="多事的战士"]你怎么才听说啊，大伙儿都早就传遍啦。
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=1)]
[name="迟钝的战士"]......那你给讲讲，这到底是怎么回事啊，这个博士原本不是恩希欧迪斯请去的客人吗？
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=2)]
[name="多事的战士"]嗨，我这儿听来的版本啊，是说那帮袭击者都觉得阿克托斯老爷在接走这个博士后买通了他。
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=1)]
[name="迟钝的战士"]啊？阿克托斯老爷哪儿会做这种事情！
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=2)]
[name="多事的战士"]笨，这不明摆着是那帮袭击的人在胡说八道嘛！
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=2)]
[name="多事的战士"]要我说啊，搞不好恩希欧迪斯在听到阿克托斯老爷要接走博士时，就直接将计就计准备要诬陷老爷了。
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=2)]
[name="多事的战士"]这帮来袭击的人，弄不好都是恩希欧迪斯安排的。
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=1)]
[name="迟钝的战士"]哎你这么一说，好像是这个道理啊。
[character(name="avg_npc_283_1#1$1",name2="avg_npc_284_1#1$1",focus=1)]
[name="迟钝的战士"]那我们还费这功夫监视这个博士干啥啊，他咋看也不像和恩希欧迪斯一伙的啊。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_261_1#2$1")]
[name="瓦莱丝"]之前不了解博士的为人，我等或许对博士多有得罪，还望包涵。
[character(name="avg_npc_261_1#2$1")]
[name="瓦莱丝"]博士是恩希欧迪斯的贵客，有些话或许我不应当讲......
[character(name="avg_npc_261_1#1$1")]
[name="瓦莱丝"]但此次针对博士的袭击确有一些蹊跷。
[dialog]
[character(name="avg_npc_261_1#1$1",focus=-1)]
[Decision(options="确实很蹊跷。", values="1")]
[Predicate(references="1")]
[Decision(options="有人在利用这些人。;我无法准确推测其用意。;这些人的行动并不合理。", values="4;5;6")]
[Predicate(references="4")]
[character(name="avg_npc_261_1#5$1")]
[name="瓦莱丝"]恩希欧迪斯......
[dialog]
[character(name="avg_npc_261_1#5$1",focus=-1)]
[Decision(options="不，他难以从中获利。", values="4")]
[Predicate(references="4")]
[Decision(options="（我也知道更明确的嫌疑人，但是......）", values="4")]
[Predicate(references="4")]
[Predicate(references="5")]
[character(name="avg_npc_261_1#2$1")]
[name="瓦莱丝"]我以为他们肯定是想打伤博士，好让恩希欧迪斯有借口向佩尔罗契家发难，指责我们没保护好博士。
[dialog]
[character(name="avg_npc_261_1#2$1",focus=-1)]
[Decision(options="这说不通。", values="5")]
[Predicate(references="5")]
[Decision(options="犯罪远比失职更招人唾弃。", values="5")]
[Predicate(references="5")]
[Predicate(references="6")]
[character(name="avg_npc_261_1#3$1")]
[name="瓦莱丝"]我也觉得，他们明明已经得到了魏斯代表恩希欧迪斯传达的信息，却还是表示不信任博士。
[character(name="avg_npc_261_1#8$1")]
[name="瓦莱丝"]这感觉就像......
[dialog]
[character(name="avg_npc_261_1#8$1",focus=-1)]
[Decision(options="有人预先料到恩希欧迪斯的打算。", values="6")]
[Predicate(references="6")]
[Decision(options="并以此为前提对他们进行煽动。", values="6")]
[Predicate(references="6")]
[Predicate(references="4;5;6")]
[character(name="avg_npc_261_1#8$1")]
[name="瓦莱丝"]唔......
[character]
[name="？？？"]哈，说得好。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_254_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="阿克托斯"]瓦莱丝，都说你棋下得好，脑子好使。照我看啊，你还得向这位博士学学。
[character(name="avg_npc_261_1#1$1")]
[name="瓦莱丝"]老爷说得是。
[character(name="avg_npc_254_1#1$1")]
[name="阿克托斯"]啊，对了，瓦莱丝。你替我传下去，告诉他们之后都不用再盯着这个博士了，好好看家就行。
[character(name="avg_npc_254_1#1$1")]
[name="阿克托斯"]至于这位博士带来的护卫，之后也允许他们自由出入这里好了。
[character(name="avg_npc_261_1#1$1")]
[name="瓦莱丝"]是。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_254_1#10$1")]
[name="阿克托斯"]你们刚才聊的，我在走廊上也碰巧听到些。
[character(name="avg_npc_254_1#10$1")]
[name="阿克托斯"]我对你们玩的推理游戏没什么兴趣，线索倒是可以给你们一些。
[character(name="avg_npc_254_1#2$1")]
[name="阿克托斯"]耶拉冈德在上。博士，就当我为佩尔罗契家先前的无礼赔个不是——
[character(name="avg_npc_254_1#7$1")]
[name="阿克托斯"]在这里我以佩尔罗契家主之名向耶拉冈德起誓，这次袭击绝不是我阿克托斯唆使挑起。
[character(name="avg_npc_254_1#7$1")]
[name="阿克托斯"]博士你要是信得过，也大可以认为我佩尔罗契家绝对没有哪个崽子胆敢背着我搞这等下三烂的袭击。
[dialog]
[character(name="avg_npc_254_1#7$1",focus=-1)]
[Decision(options="感谢你的信任，阿克托斯先生。;感谢你的线索，阿克托斯先生。", values="1;2")]
[Predicate(references="1")]
[character(name="avg_npc_254_1#1$1")]
[name="阿克托斯"]哦？我可没说我相信了你啊，博士。
[character(name="avg_npc_254_1#10$1")]
[name="阿克托斯"]不过我倒是能肯定，至少你没有在给我搞鬼。
[Predicate(references="2")]
[character(name="avg_npc_254_1#11$1")]
[name="阿克托斯"]哈哈哈哈，好。
[Predicate(references="1;2")]
[character(name="avg_npc_254_1#1$1")]
[name="阿克托斯"]博士，虽然我只是个粗人，可就连我也看得出来，谢拉格有不寻常的事情在发生。
[character(name="avg_npc_254_1#1$1")]
[name="阿克托斯"]恩希欧迪斯这小子，突然说要还政，又突然把诺希斯赶走，再把你给摆到这个位置上。
[character(name="avg_npc_254_1#1$1")]
[name="阿克托斯"]你又偏偏在处理这个还政时被人袭击了。
[character(name="avg_npc_254_1#2$1")]
[name="阿克托斯"]说老实话，我没法不去怀疑恩希欧迪斯，可他也确实没有露出半点破绽。
[character(name="avg_npc_254_1#2$1")]
[name="阿克托斯"]但这么不明不白地干等着耶拉冈德交予我们的土地和人民遇险，真叫我不甘心......
[dialog]
[character(name="avg_npc_254_1#2$1",focus=-1)]
[Decision(options="那么，阿克托斯先生......", values="1")]
[Predicate(references="1")]
[character(name="avg_npc_254_1#4$1")]
[name="阿克托斯"]怎么了？
[dialog]
[character(name="avg_npc_254_1#4$1",focus=-1)]
[Decision(options="我们的和解也可能意味着......;如果对手能预想到你的反应就说明......", values="1;2")]
[Predicate(references="1;2")]
[Decision(options="对手不再需要拿我充当障眼法了。;对手已经准备完毕，时间不多了。", values="1;2")]
[Predicate(references="1;2")]
[character(name="avg_npc_254_1#7$1")]
[name="阿克托斯"]什么？！
[Dialog]
[character]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",volum

... (全文11234字符)
```

### level_act14side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[delay(time=1)]
[Subtitle(text="恩雅，我希望你能争取成为圣女。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——为什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="喀兰贸易如果想要在谢拉格更进一步，需要一个圣女，这是一个绝佳的机会。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——为什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="当然，事情不会这么简单。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="另两家人会有什么盘算你我都很清楚。但是我相信你若是被雪水滴中，一定能够通过考验，成为圣女。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="恩雅，我知道你可以做到。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——如果我不想呢？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——如果我失败了呢？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="所有的反驳和疑问，我一句都没有说出口。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="因为我知道他会怎么回答，他一定会说。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[delay(time=1)]
[PlaySound(key="$d_avg_tinnitus",volume=1)]
[Subtitle(text="你姓希瓦艾什，恩雅。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g9_manoravenue",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[character(name="avg_172_svrash_1#1$1",fadetime=1.5)]
[playsound(key="$d_gen_walk_n")]
[delay(time=3)]
[Character]
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=1, fadetime=1.5)]
[delay(time=2)]]
[name="谢拉格平民A"]亲爱的，你快出来看，那是恩希欧迪斯老爷吗？
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民B"]怎么可能，明天就是上山圣猎的日子了，老爷这时候不准备给圣女的供奉，一早跑到领地来视察做什么？
[name="谢拉格平民B"]......等等，这还真是恩希欧迪斯老爷！
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格平民A"]我听说，最早人们进圣山是不许骑驮兽的。
[name="谢拉格平民A"]尤其是要去拜见圣女的人们，要从跨出自家门槛的第一步开始，双掌合十，眼不离地，低着头一路祈祷过去。
[name="谢拉格平民A"]你看老爷现在的样子，莫不是他想效仿传统？
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民B"]是啊，是啊。我是听说过这种习俗，可老爷他......毕竟是老爷啊，竟然也要这么低着头一步一步走到圣山上面去。
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格平民A"]你在说什么呢，老爷也是耶拉冈德的子民啊，你难道也和佩尔罗契家的傻子一样，觉得他忘了本？
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民B"]你在胡说什么，我哪有这个意思！
[name="谢拉格平民B"]我只是替老爷担心。你又不是不知道，另外两家贪得无厌，老爷提出了把大权交给圣女，他们竟然还不太乐意。
[name="谢拉格平民B"]那两家嫉妒老爷带来的发展，连我们的铁路都炸了，听说是想把谢拉格封起来，然后两家一起把咱们给包了。
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格平民A"]他们怎么敢？在耶拉冈德的眼前动武，祂可是会动怒的。
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民B"]他们还有什么不敢？
[name="谢拉格平民B"]今天老爷这么手无寸铁地徒步走在街道上，明天又是三家带兵在山中打猎，真不知道他们又能做出什么伤天害理的事情！
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格平民A"]哎呀，可不要说这种不吉利的话！耶拉冈德在上，请保佑老爷一路平安！
[character(name="avg_npc_280_1#1$1",name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民B"]耶拉冈德在上，请保佑老爷一路平安！
[character(name="avg_npc_272_1#1$1")]
[name="谢拉格贵族"]恩希欧迪斯老爷，没想到今日还能见到如您这样虔诚的上山参拜者！
[character(name="avg_npc_272_1#1$1",name2="avg_198_blackd_1#8$1",focus=2)]
[name="魏斯"]抱歉，帕莱老爷，我家主人因行大礼，必须一路虔诚祈祷，无法分心回应您。
[name="魏斯"]在下替老爷向您致以问候。
[character(name="avg_npc_272_1#1$1",name2="avg_198_blackd_1#8$1",focus=1)]
[name="谢拉格贵族"]无妨无妨，是我冒犯了。耶拉冈德在上，还请原谅我。
[name="谢拉格贵族"]只不过从图里卡姆到圣山，路程遥远，我等领民将恩希欧迪斯老爷的举止看在眼里，难免忧心。
[character(name="avg_npc_272_1#1$1",name2="avg_198_blackd_1#1$1",focus=2)]
[name="魏斯"]老爷早下定了决心，请不用为他担忧。
[name="魏斯"]我们这一队护卫也不会让老爷出任何意外。
[character(name="avg_npc_272_1#1$1",name2="avg_198_blackd_1#1$1",focus=1)]
[name="谢拉格贵族"]那就好，愿耶拉冈德赐福于希瓦艾什。
[character(name="avg_npc_272_1#1$1",name2="avg_198_blackd_1#1$1",focus=2)]
[name="魏斯"]也愿耶拉冈德保佑您。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g4_boudoir",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_174_slbell_1#1$1",name2="avg_npc_250_1#1$1",focus=1,fadetime=1.5)]
[Delay(time=2)]
[name="恩雅"]总觉得，围猎还没有开始，野兽却已经在惊慌了。
[character(name="avg_174_slbell_1#1$1",name2="avg_npc_250_1#1$1",focus=2)]
[name="雅儿"]您啊，只是从这窗格向外望，怎么就知道野兽在惊慌了？
[character(name="avg_174_slbell_1#3$1",name2="avg_npc_250_1#1$1",focus=1)]
[name="恩雅"]积雪在发出响动。
[character(name="avg_174_slbell_1#3$1",name2="avg_npc_250_1#1$1",focus=2)]
[name="雅儿"]这么说来，明天圣猎时，您可要小心脚下。
[character(name="avg_174_slbell_1#3$1",name2="avg_npc_250_1#6$1",focus=2)]
[name="雅儿"]......大长老到了。
[character(name="avg_174_slbell_1#10$1",name2="avg_npc_250_1#6$1",focus=1)]
[name="恩雅"]唉，我需要小心的麻烦事多着呢。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g3_mainhall",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_258_1#1$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="大长老"]恩雅，你可做好了准备？
[character(name="avg_npc_258_1#1$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]行装与致辞，我都已准备好了。
[name="恩雅"]请大长老放心，我已经不是第一次参与大典了。
[character(name="avg_npc_258_1#1$1",name2="avg_174_slbell_1#1$1",focus=

... (全文10486字符)
```

### level_act14side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g12_mountpath",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="slide")]
[delay(time=2)]
[stopsound(channel="slide", fadetime=3)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1, loop=true, channel="bse")]
[character(name="avg_172_svrash_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="恩希欧迪斯"]......
[character(name="avg_172_svrash_1#1$1",name2="avg_199_yak_1#6$1",focus=2)]
[name="角峰"]老爷，喝口热水吧。
[name="角峰"]从昨天开始您就滴水未进，走了这一路，之后还要参加狩猎，这......
[character(name="avg_172_svrash_1#1$1",name2="avg_199_yak_1#6$1",focus=1)]
[name="恩希欧迪斯"]不必了。
[character(name="avg_172_svrash_1#1$1",name2="avg_199_yak_1#1$1",focus=2)]
[name="角峰"]可是——
[character(name="avg_172_svrash_1#1$1",name2="avg_199_yak_1#1$1",focus=1)]
[name="恩希欧迪斯"]这是我的决定。
[character(name="avg_172_svrash_1#5$1",name2="avg_199_yak_1#1$1",focus=1)]
[name="恩希欧迪斯"]不要让我说第二次，角峰。
[dialog]
[character]
[character(name="char_empty",name2="avg_199_yak_1#1$1",fadetime=1.5)]
[delay(time=1.5)]
[StopSound(channel="bse", fadetime=1)]
[delay(time=2)]
[character(name="char_empty",name2="avg_199_yak_1#2$1",fadetime=0.7,focus=2)]
[delay(time=0.7)]
[name="角峰"]......
[dialog]
[PlaySound(key="$d_avg_snowbootwalk")]
[character(name="avg_198_blackd_1#6$1",name2="avg_199_yak_1#2$1",fadetime=1.5,focus=1)]
[delay(time=2)]
[name="魏斯"]别再说了，角峰大哥。
[name="魏斯"]老爷的脾气你应该最清楚，明知老爷肯定不会接受，又何必这样？
[character(name="avg_198_blackd_1#6$1",name2="avg_199_yak_1#1$1",focus=2)]
[name="角峰"]......至少我得试试。
[name="角峰"]老爷他......太冒险了。
[character(name="avg_198_blackd_1#8$1",name2="avg_199_yak_1#1$1",focus=1)]
[name="魏斯"]风险与机遇并存，一直不都是这么过来的？
[name="魏斯"]我们只需要听老爷的。
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bse")]
[character(name="avg_198_blackd_1#8$1",name2="avg_199_yak_1#1$1",focus=2)]
[name="角峰"]......
[character(name="avg_198_blackd_1#8$1",name2="avg_199_yak_1#1$1",focus=1)]
[name="魏斯"]呼......
[character(name="avg_198_blackd_1#5$1",name2="avg_199_yak_1#1$1",focus=1)]
[name="魏斯"]真冷。这雪是不是越来越大了？
[StopSound(channel="bse", fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g6_square",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_253_1#7$1",name2="avg_npc_254_1#1$1",focus=1,fadetime=1.5)]
[Delay(time=1)]
[name="菈塔托丝"]真慢。
[name="菈塔托丝"]要我们两家一起等着他，好大的排场。
[character(name="avg_npc_253_1#7$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]他一路步行而来，这倒确实不错。
[character(name="avg_npc_253_1#4$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]真稀奇，你竟也会夸他？听说这一路上，恩希欧迪斯是被交口称赞，受欢迎得很啊。
[character(name="avg_npc_253_1#10$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]阿克托斯，你可要小心点，说不定再过几天，耶拉冈德最虔诚的信徒就要从你阿克托斯变成他恩希欧迪斯了。
[character(name="avg_npc_253_1#10$1",name2="avg_npc_254_1#9$1",focus=2)]
[name="阿克托斯"]风凉话就免了，菈塔托丝。
[character(name="avg_npc_253_1#10$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]我虽不信任恩希欧迪斯，但他若做得对，我便说对。
[name="阿克托斯"]如果你把我喊过来就是为了说这些，那就恕我不奉陪了。
[character(name="avg_npc_253_1#7$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]我也没有那么闲，阿克托斯。
[name="菈塔托丝"]我只是要提醒你。
[character(name="avg_npc_253_1#7$1",name2="avg_npc_254_1#3$1",focus=2)]
[name="阿克托斯"]提醒？有什么事是需要你菈塔托丝来提醒我的。
[character(name="avg_npc_253_1#7$1",name2="avg_npc_254_1#3$1",focus=1)]
[name="菈塔托丝"]你认为没有？
[character(name="avg_npc_253_1#8$1",name2="avg_npc_254_1#3$1",focus=1)]
[name="菈塔托丝"]阿克托斯，逞口舌之快对我们都没有好处。在当下，我们两家之间才是最牢固的盟友关系。
[character(name="avg_npc_253_1#8$1",name2="avg_npc_254_1#2$1",focus=2)]
[name="阿克托斯"]......
[character(name="avg_npc_253_1#8$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]逞口舌之快的恐怕不是我，菈塔托丝。
[name="阿克托斯"]我不喜欢你和恩希欧迪斯的那种弯弯绕绕，我一向只看行动。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="菈塔托丝"]你只看行动，那正好。
[name="菈塔托丝"]那我们就谈谈两天前的那场爆炸。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#3$1",focus=2)]
[name="阿克托斯"]怎么，难道菈塔托丝你要承认那是你布朗陶家所为？哼，我可不信，这事不是你的风格。
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#9$1",focus=2)]
[name="阿克托斯"]还是说，你知道主谋是谁？
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#9$1",focus=1)]
[name="菈塔托丝"]......我要是说我知道呢？
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#5$1",focus=2)]
[name="阿克托斯"]——此话当真？
[character(name="avg_npc_253_1#1$1",name2="avg_npc_254_1#5$1",focus=1)]
[name="菈塔托丝"]绝无虚言。
[name="菈塔托丝"]阿克托斯，你要不要猜猜，我们的这位援兵究竟会是什么人？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_npc_262_1#8$1")]
[name="休露丝"]莫希，莫希！
[character(name="avg_npc_262_1#8$1")]
[name="休露丝"]人呢，跑哪儿去了......？！
[Dialog]
[Character(name="avg_npc_262_1#8$1", name2="char_empty")]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_262_1#8$1", name2="avg_npc_255_1#1$1",fadetime=0.7)]
[delay(time=2)]
[character(name="avg_npc_262_1#8$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]夫人。您找我？
[character(name="avg_npc_262_1#8$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="休露丝"]我找没找你，这还用问吗？！
[character(name="avg_npc_262_1#7$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="休露丝"]平时你不是挺机灵的，怎么偏偏在这种时候瞎跑！我明明说了这次狩猎一定要好好准备......算了，你准备得怎么样了？
[name="休露丝"]我可实话和你说了，莫希，你是我手下最可靠的战士。
[name="休露丝"]这次我能不能给布朗陶家争光，让菈塔托丝那个臭女人没话可说，可全都看你的表现了！
[character(name="avg_npc_262_1#7$1",name2="avg_n

... (全文13743字符)
```

### level_act14side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[delay(time=1)]
[Subtitle(text="人的领袖在耶拉冈德面前跪下，向祂献上最高的敬意。然后询问：", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“这片土地不再是无主之地。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“这片土地上的每一个人都崇拜您，敬仰您，您是我们所有人的领袖。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“所以，请告诉我们，我们的名字是什么？”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="耶拉冈德回答：", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“我已为你们想好名字。从今天起，这片土地就叫作谢拉格。而你们，就是谢拉格人。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text=" ——《耶拉冈德》第二页", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Background(image="24_g12_mountpath",screenadapt="showall")]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]......
[name="阿克托斯"]............
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]阿克托斯大人。
[character(name="avg_npc_254_1#4$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]——！我在，圣女大人有何吩咐？
[character(name="avg_npc_254_1#4$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]不必如此紧张，阿克托斯大人，我并非食人猛兽。
[character(name="avg_npc_254_1#3$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]不管怎么说，这是您第一次亲自参与圣猎。不光是我，您看看这些战士们，在圣女大人您面前大家都绷紧了，想好好表现一番！
[character(name="avg_npc_254_1#3$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]......作为圣女，与耶拉冈德的战士们一同参与圣猎，我认为这是我应当做的。
[character(name="avg_npc_254_1#3$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]您这话说得有理！
[character(name="avg_npc_254_1#3$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]不说我了。我见您从狩猎开始时，就一直像是有什么心事，若是有什么想问的，就请直接问吧。
[character(name="avg_npc_254_1#3$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]......哈哈，瞒不过圣女大人，您见笑了。
[character(name="avg_npc_254_1#3$1",name2="avg_174_slbell_1#11$1",focus=2)]
[name="恩雅"]若您不介意，可以将我当成一个朋友。
[name="恩雅"]那么，我也会将您当成一个朋友。
[character(name="avg_npc_254_1#5$1",name2="avg_174_slbell_1#11$1",focus=1)]
[name="阿克托斯"]圣女大人......
[name="阿克托斯"]我心中，也把圣女大人您当作一个朋友。
[character(name="avg_npc_254_1#5$1",name2="avg_174_slbell_1#11$1",focus=2)]
[name="恩雅"]既然如此，就让我们像朋友似的说话。
[character(name="avg_npc_254_1#2$1",name2="avg_174_slbell_1#11$1",focus=1)]
[name="阿克托斯"]......
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#11$1",focus=1)]
[name="阿克托斯"]我明白了，那么恕我直言。
[name="阿克托斯"]我想知道，圣女大人，究竟是怎么看待还政一事的？
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]......您很爽快。
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]朋友之间，自当如此。
[name="阿克托斯"]我佩尔罗契家的人论战斗，不会输给布朗陶和希瓦艾什，但论阴谋诡计，实在不是这两家的对手。
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]弯弯绕绕，遮遮掩掩绝非我的风格。
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#3$1",focus=2)]
[name="恩雅"]您说得不错......
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]不过，我的朋友，还是得请您原谅我。
[name="恩雅"]在回答您的问题之前，我需要先向您确认一件事。
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]圣女大人请说。
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]阿克托斯大人，您是一位忠勇、虔诚的战士。
[name="恩雅"]我清楚您率直、爽快，同时我也知晓，您绝不是真的毫无考虑。
[name="恩雅"]既然您说朋友之间理应不遮不掩，那么我亦当效仿。
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]——我想知道，一直以来，为什么您会如此坚定地反对恩希欧迪斯的开放政策？
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]......我是个粗人，圣女大人。
[name="阿克托斯"]无论恩希欧迪斯将他的所谓开放吹得有多好，有多吸引人，我要的不是那些夸夸其谈，不是那些漂亮话。
[name="阿克托斯"]我只看他带来了什么。
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]而我看到的是涌进我们家中的毫无信仰的外国人，是打着发展旗号对土地山川的破坏，是在他的领地里工作后日渐失去信仰的谢拉格人。
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]......
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]......他带进来的那些东西是好用，他因此赚了很多钱，造了很多大房子，我当然知道。
[name="阿克托斯"]可是如果人人都学他那样，为了所谓的发展，就把信仰抛在脑后，那么这片土地会变成什么样子？
[character(name="avg_npc_254_1#8$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]耶拉冈德既然令我佩尔罗契家守卫谢拉格，那我阿克托斯就决不能容忍有任何人，以任何方式想要将其破坏！
[character(name="avg_npc_254_1#8$1",name2="avg_174_slbell_1#3$1",focus=2)]
[name="恩雅"]......阿克托斯大人的想法我明白了。
[character(name="avg_npc_254_1#8$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]那么该我回答您的问题了。
[name="恩雅"]恩希欧迪斯大人提出要将核心领地尽数交于我手，此事事出突然，确实在我的意料之外。
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]圣女大人果然也不知情吗？
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]确实，在此之前，我对他竟有这种打算一无所知。
[name="恩雅"]但是——
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#3$1",focus=2)]
[name="恩雅"]......
[character(name="avg_npc_254_1#7$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]不论恩希欧迪斯大人究竟是出于何种考量，才提出还政一事，就结果而言，我并不认为这是一个很坏的发展。
[character(name="avg_npc_254_1#5$1",name2="avg_174_slbell_1#1$1",focus=1)]
[name="阿克托斯"]您的意思是......
[character(name="avg_npc_254_1#5$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]我坐在蔓珠院中，日日夜夜看着人们向耶拉冈德祈祷。
[name="恩雅"]有一点我比恩希欧迪斯大人要清楚，那就是——谢拉格还无法失去信仰。
[name="恩雅"]既做出了这样的决定，接下来的许多事情，我想，就不再是谁个人说了便能算数的了。
[character(name="avg_npc_254_1#5$1",name2="avg_174_slbell_1#1$1",focus=2)]
[name="恩雅"]意外总会发生，不是吗？
[character(name="avg_npc_254_1#5$1",name2="avg_174_slbell_1#8$1",focus=2)]
[name="恩雅"]若恩希欧迪斯大人没有提前料想到这一点，那就是他的不是了。
[character(name="avg_npc_254_1#1$1",name2="avg_174_slbell_1#8$1",focus=1)]
[name="阿克托斯"]......行，其他的我不管，但我信您这句话。
[character(name="avg_npc_254_

... (全文19978字符)
```

### level_act14side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#1$1", fadetime=2)]
[Background(image="bg_towerinside",fadetime=2,block=true)]
[delay(time=1)]
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="诺希斯"]接下来的行动准备好了？
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]......是。
[name="莫希"]......
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#3$1",focus=2)]
[name="莫希"]诺希斯大人......！
[name="莫希"]......我可以问一个问题吗？
[character(name="avg_206_gnosis_1#4$1",name2="avg_npc_255_1#3$1",focus=1)]
[name="诺希斯"]真少见，这是不是你头一次提出问题？
[name="诺希斯"]你说。
[character(name="avg_206_gnosis_1#4$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]......属下僭越。
[name="莫希"]只是，若按照我们的计划行事，事后追查起来，布朗陶家恐怕也将受到牵连。
[character(name="avg_206_gnosis_1#4$1",name2="avg_npc_255_1#8$1",focus=2)]
[name="莫希"]属下......属下只是担心，如今诺希斯大人与布朗陶家结成同盟，若是布朗陶家遭发难，是否会对诺希斯大人的计划不利......
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#8$1",focus=1)]
[name="诺希斯"]你说的问题我也考虑过，不过无妨，布朗陶家如何从来不是重点，这次机会十分难得，我不希望错过。
[name="诺希斯"]但我也希望你能保全自己。
[name="诺希斯"]如果真的出现最坏的情况，不需要考虑布朗陶家的问题。我了解恩希欧迪斯，只要你的证词对他有利，他大概暂时不会动你。
[name="诺希斯"]到时我会安排人手确保你的安全。
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]诺希斯大人！我......
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="诺希斯"]......怎么了？
[name="诺希斯"]如果你有顾虑，计划也可以换人执行。
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#3$1",focus=2)]
[name="莫希"]......不！请让我来！
[character(name="avg_206_gnosis_1#1$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]只要是诺希斯大人的吩咐......
[name="莫希"]莫希在所不辞。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="24_g12_mountpath",screenadapt="showall",fadetime=1.5)]
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_singleblunt", volume=3)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1",focus=1)]
[name="年长的谢拉格战士"]这下总算是把那些野兽全部解决了！
[name="年长的谢拉格战士"]有一两个小子受了点伤，但没什么大碍......多亏了圣女大人！
[Character(name="avg_174_slbell_1#11$1")]
[name="恩雅"]我并没有做什么。是各位出色地证明了自己的勇武，想必耶拉冈德也会为祂的勇士们自豪。
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1",focus=1)]
[name="年长的谢拉格战士"]您、您过奖了......！
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1",focus=2)]
[name="年轻的谢拉格战士"]圣女大人！
[Character(name="avg_174_slbell_1#5$1")]
[name="恩雅"]嗯？你是......刚刚的......
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1",focus=2)]
[name="年轻的谢拉格战士"]是我。多谢圣女大人方才救了我一命。
[character(name="avg_npc_254_1#1$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="阿克托斯"]圣女大人！您刚刚确实是太冒险了！
[name="阿克托斯"]但还是感谢您，感谢您救了这个混小子！
[Character(name="avg_174_slbell_1#11$1")]
[name="恩雅"]耶拉冈德的子民之间本就应当如此，不必言谢。
[character(name="avg_npc_284_1#1$1",name2="avg_npc_283_1#1$1",focus=2)]
[name="年轻的谢拉格战士"]......圣女大人......
[character(name="avg_npc_254_1#1$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]确实是精彩的一箭。我还不曾听闻圣女大人竟还有这样的本领......
[Character(name="avg_174_slbell_1#1$1")]
[name="恩雅"]圣女原本就应有保护雪山民众的能力，这并不是什么值得特别提及的事。
[character(name="avg_npc_254_1#3$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="阿克托斯"]您就是太谦虚了！方才的那一箭，我看完全能与我们谢拉格最善射的战士比个高下！
[Dialog]
[Character]
[PlaySound(key="$d_avg_snowrun", volume=1)]
[character(name="avg_npc_283_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="谢拉格战士"]圣女大人！阿克托斯大人，菈塔托丝大人！
[name="谢拉格战士"]不、不好了！
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#7$1",focus=2)]
[name="菈塔托丝"]乱喊什么？我们好得很。
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]你是希瓦艾什家的人？怎么，又出什么事了，总不会是你们也遭到野兽袭击，他恩希欧迪斯还要来找外援吧？
[Character(name="avg_npc_283_1#1$1")]
[name="谢拉格战士"]不、不是野兽！
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="阿克托斯"]那究竟是怎么回事，不要吞吞吐吐，快说清楚！
[Character(name="avg_npc_283_1#1$1")]
[name="谢拉格战士"]是！是恩希欧迪斯大人遭刺客袭击！
[Character(name="avg_174_slbell_1#6$1")]
[name="恩雅"]——！
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#4$1",focus=2)]
[name="菈塔托丝"]......你说什么？
[name="菈塔托丝"]恩希欧迪斯他被袭击？竟有人敢在圣猎这样的场合对他动手？
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#4$1",focus=1)]
[name="阿克托斯"]......留下一半人手保护圣女，保持警惕。
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#4$1",focus=1)]
[name="阿克托斯"]其余的人，跟着我走！
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#7$1",focus=2)]
[name="菈塔托丝"]等等，阿克托斯！你发什么疯？
[name="菈塔托丝"]你要干什么，难道你真要去救援？且不说恩希欧迪斯他需不需要，就现在的情况......你想清楚了？
[character(name="avg_npc_254_1#7$1",name2="avg_npc_253_1#7$1",focus=1)]
[name="阿克托斯"]......没什么好想的，菈塔托丝，我知道你的意思。
[name="阿克托斯"]但我，我不管他恩希欧迪斯如何，他是真心悔改也好，假意做戏也罢，有人要在圣猎作怪，我阿克托斯绝不允许！
[character(name="avg_npc_254_1#8$1",name2="avg_npc_253_1#7$1",focus=1)]
[name="阿克托斯"]——我族世代立有保护谢拉格的誓言，圣猎仪式的秩序也在此之列！
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=2)]
[characteraction(name="left", type="move", xpos=-300, fadetime=2,block=false)]
[character(name="char_empty",name2="avg_npc_253_1#7$1",fadetime=0.5)]
[delay(time=2)]
[name="菈塔托丝"]真是莽夫......罢了，我倒是要看看，你这好心能换来什么结果。
[dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=2)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="char_empty",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_174_slbell_1#7$1",fadetime=1)]
[delay(time=1)]
[name="恩雅"]......
[name="恩雅"]恩希欧迪斯......
[Dialog]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]


... (全文16362字符)
```

### level_act14side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] level_act14side_06_beg
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="24_g11_snowylane",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_250_1#2$1",fadetime=0.7)]
[Delay(time=0.7)]
[name="雅儿"]不出兵攻打另外两家，只派兵保护蔓珠院......
[Character(name="avg_npc_250_1#5$1")]
[name="雅儿"]真是，好一个保护蔓珠院呢。
[name="雅儿"]这下，他可以名正言顺地控制蔓珠院了。
[Dialog]
[Character(name="avg_npc_250_1#5$1",focus=-1)]
[Decision(options="台面上看，他已经赢了。;历史是由胜利者书写的。", values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_250_1#5$1")]
[name="雅儿"]唉，确实是这么回事。
[name="雅儿"]恩希欧迪斯的做法，现在就算是我也看明白了。
[name="雅儿"]还政就是一个幌子，他从一开始就是想要掀翻整张桌子。
[Dialog]
[Character(name="avg_npc_250_1#5$1",focus=-1)]
[Decision(options="谢拉格的人民无法想象离开神的生活。;恩希欧迪斯知道没有神该怎么生活。;这不是耶拉冈德的问题。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Predicate(references="1")]
[Character(name="avg_npc_250_1#5$1")]
[name="雅儿"]是啊，所有人都以为他绝对无法战胜谢拉格人对耶拉冈德的信仰，觉得他做不到这样的事。
[name="雅儿"]大长老，菈塔托丝，阿克托斯，甚至我，都这么想。
[Predicate(references="2")]
[Character(name="avg_npc_250_1#6$1")]
[name="雅儿"]他确实知道。
[Character(name="avg_npc_250_1#4$1")]
[name="雅儿"]但是，我始终在好奇一件事。
[name="雅儿"]离开神，是不是一定意味着要没有神？
[Predicate(references="3")]
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]哎呀，我只是感慨一下，没有觉得沮丧啦。
[name="雅儿"]信仰逐渐成为了一种阻碍......至少谢拉格人对耶拉冈德的信仰是如此，我早就知道。
[Character(name="avg_npc_250_1#7$1")]
[name="雅儿"]但还是谢谢你。
[Predicate(references="1;2;3")]
[Character(name="avg_npc_250_1#2$1")]
[name="雅儿"]......唉，不过这和我一个小小的侍奉圣女的侍女长也没有关系就是了。
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]说起来，我还以为，你会问我为什么还跟在你身边。
[Dialog]
[Character(name="avg_npc_250_1#1$1",focus=-1)]
[Decision(options="一个人选择旁观可以有无数种理由。", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]就好像你选择插手也可以有无数种理由一样，是吗？
[Character(name="avg_npc_250_1#7$1")]
[name="雅儿"]......谢谢你，博士。
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]我会坚持我的选择，希望你也一样。
[Character]
[Dialog]
[Delay(time=0.51)]
[Character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",fadetime=1.5)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[PlaySound(key="$d_avg_snowbootwalk",delay=0.2,channel="a",volume=1)]
[Delay(time=2)]
[Character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",focus=1)]
[name="Sharp"]博士，工作完成了。
[Dialog]
[Character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",focus=-1)]
[Decision(options="他们人呢？;辛苦了。", values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_252",name2="avg_422_aurora_1#1$1",focus=1)]
[name="Sharp"]我留不住谢拉格的二位家主。菈塔托丝让我替她向你道谢，不过她似乎有自己的打算，返回了自己的领地。
[name="Sharp"]阿克托斯正在赶回本家，他看起来要集结兵力和恩希欧迪斯决一死战。
[Character(name="avg_npc_252",name2="avg_422_aurora_1#4$1",focus=2)]
[name="极光"]博士，让他们回到自己的领地，真的能够避免伤亡吗？
[Dialog]
[Character(name="avg_npc_252",name2="avg_422_aurora_1#4$1",focus=-1)]
[Decision(options="只有他们两个能管住自己家族的人。;目前为止的发展，已经是损失最小的办法了。", values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_252",name2="avg_422_aurora_1#4$1",focus=1)]
[name="Sharp"]博士的意思是，他们两个如果在这里被抓住，那么，很有可能因为群情激愤而直接被处死。
[name="Sharp"]即使没有，也必然会直接遭到审判。
[Character(name="avg_npc_250_1#5$1")]
[name="雅儿"]虽然他们两人此时被打成了叛徒，但两家，尤其是佩尔罗契家，手下的死忠是不会轻易相信的。
[name="雅儿"]到那时候，他们擅自挑起争端也好，起内讧也好，谢拉格必然会陷入一片混乱。
[Character(name="avg_npc_252")]
[name="Sharp"]但对恩希欧迪斯来说，不管怎样，他都已经站住了大义。
[name="Sharp"]对他来说，哪怕会在最初出现混乱，甚至过程中出现相当伤亡，局势最终也是可以收拾的。
[Character(name="avg_422_aurora_1#4$1")]
[name="极光"]......
[Dialog]
[Character(name="avg_422_aurora_1#4$1",focus=-1)]
[Decision(options="我想，他不会完全坐视不管。", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_252")]
[name="Sharp"]是的，恩希欧迪斯苦心营造如今的局面，说明他不是一个完全不在乎民众的人。
[name="Sharp"]我在喀兰贸易“做客”的时候，对他的做派也有所耳闻，员工们对他的评价普遍是有远见。
[name="Sharp"]如今他选择在明面上直接起事，可以猜想，这种风险极大的下策已经是他手里的最佳选项了。
[Character(name="avg_422_aurora_1#4$1")]
[name="极光"]但愿......是这样吧。
[Character(name="avg_npc_252")]
[name="Sharp"]希瓦艾什家过去与布朗陶家交往比较密切，其中必然安插了不少棋子，这些棋子应该能够起到抑制混乱的作用。
[name="Sharp"]重点依然还是佩尔罗契家，他们的装备和军事素养虽然落后，但规模依然不容小觑。
[Character(name="avg_npc_250_1#6$1")]
[name="雅儿"]是呢，希瓦艾什家与他们家关系向来不好。
[name="雅儿"]而且，佩尔罗契家上下的忠诚心都是很强的，即使发生了现在这样的事，他们会背叛佩尔罗契家的可能性也是不好说的......
[Character(name="avg_npc_252")]
[name="Sharp"]所以我并不是不能理解博士协助他们两人的做法。
[name="Sharp"]只有家主在，一个家族才能拧成一股绳，而这样，只要能够影响家主，就足够博士做一些宏观上的规划。
[name="Sharp"]不过，博士，我想应该不用我提醒的是——
[name="Sharp"]谢拉格地势复杂，交通不便，我们的时间，并不多。
[Dialog]
[Character(name="avg_npc_252",focus=-1)]
[Decision(options="先见一见他们吧。", values="1")]
[Predicate(references="1")]
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_270_1$1",fadetime=1.5)]
[playsound(key="$doorclosequite")]
[Delay(time=3)]
[Character(name="avg_npc_270_1$1")]
[name="布朗陶家贵族"]大夫人，久等了。
[Character(name="avg_npc_253_1#10$1")]
[name="菈塔托丝"]难为你在这种时候还愿意帮我。
[Character(name="avg_npc_270_1$1")]
[name="布朗陶家贵族"]哪里，我毕竟是布朗陶家的人，这种时候站在大夫人这边是应该的。
[Character(name="avg_npc_253_1#10$1")]
[name="菈塔托丝"]恩希欧迪斯说的那些，你信吗？
[Character(name="avg_npc_270_1$1")]
[name="布朗陶家贵族"]怎么会，一定是他在诬陷您。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]......
[name="菈塔托丝"]要你准备的东西怎么样了？
[Character(name="avg_npc_270_1$1")]
[name="布朗陶家贵族"]从希瓦艾什家返回布朗陶家路途有些遥远，不过我已经准备好了车，也打点好了关系。
[name="布朗陶家贵族"]等到您和休露丝夫人都准备好，一定能将您二位送回布朗陶家的领地。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]......领地里有什么消息吗？
[Character(name="avg_npc_270_1$1")]
[name="布朗陶家贵族"]在大典上的消息传开后，靠近领地边缘的几个镇子立刻换上了希瓦艾什家的旗帜。
[name="布朗陶家贵族"]靠近中心一些的还没有动作，不过......
[Character(name="avg_npc_253_1#2$1")]
[name="菈塔托丝"]行了，我布朗陶家有多少他恩希欧迪斯安插的人，我心里有数。我怕他们站在一起我都数不过来。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]恩希欧迪斯有什么动静？
[Character(name="avg_npc_270_1$1")]
[name="布朗陶家贵族"]希瓦艾什家的战士已经驻扎在了圣山脚下和山腰。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]哼，他倒是说话算话。

... (全文40735字符)
```

### level_act14side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] level_act14side_06_end
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="我亲爱的妹妹，你羡慕我所拥有的一切，权力、地位、钱财。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你却不知道，我也羡慕着你所拥有的一切，爱人、自由、未来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我时常希望我们能够交换，即使我知道这不可能。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="将布朗陶家交给你，等于这个家族的覆灭。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="正如将你的生活交给我，恐怕也只会是一段失败的人生。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g7_thoroughfare",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_253_1#1$1",fadetime=1)]
[Delay(time=1)]
[name="菈塔托丝"]......
[Dialog]
[Character]
[Character(name="avg_npc_257_1#1$1",name2="avg_172_svrash_1#1$1",fadetime=1.5)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[Delay(time=3)]
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]不愧是你啊，恩希欧迪斯，只带一名护卫，就来赴我的约。
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]我并不是来战斗的，我想，你也应当没有这个打算。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]哼，我倒是想。
[name="菈塔托丝"]我布朗陶家可没有佩尔罗契家那么雄厚的兵力。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]锏也要进来吗？
[Character(name="avg_npc_257_1#4$1")]
[name="锏"]你希望我进去吗？
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]都可以。
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]锏，你在外面等我吧。
[Character(name="avg_npc_257_1#1$1")]
[name="锏"]你确定？我无所谓。
[Character(name="avg_172_svrash_1#10$1")]
[name="恩希欧迪斯"]这是我的——诚意。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]恩希欧迪斯，你确实很擅长包装自己的想法。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]诚意？只是笃定我现在做什么都没有意义罢了。
[Character(name="avg_172_svrash_1#10$1")]
[name="恩希欧迪斯"]你也可以理解为——我在等待你做一些有意义的事。
[Character(name="avg_npc_253_1#11$1")]
[name="菈塔托丝"]你会等到的。请进吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g8_nobleroom",screenadapt="coverall")]
[PlaySound(key="$d_avg_gatecloz", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1.5)]
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]如果我没记错的话，这里过去是埃德怀斯家的领地。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]是啊。这栋楼是不是还不错？
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]位置好，视野广阔，是一栋好宅子。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]埃德怀斯家世代为谢拉格保管卷宗典籍，和三大家族的关系都不差。爷爷过去差人在这里建了这栋楼，作为我们家的别院。
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]听说老卢卡生前最爱建筑设计，从这间屋子的水平来看，恐怕连维多利亚有名的设计师也不得不心服口服。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]哈哈哈，就算被你承认，他老人家大概也高兴不起来吧。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]不过，你要是喜欢，我可以把当初的设计图给你看看。
[Character(name="avg_172_svrash_1#2$1")]
[name="恩希欧迪斯"]我会考虑。
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]菈塔托丝，你知道我们现在这样坐着聊天，让我想起了什么时候吗？
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]什么时候？
[Character(name="avg_172_svrash_1#5$1")]
[name="恩希欧迪斯"]七年前。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]七年前......哦，七年前。
[name="菈塔托丝"]你刚从维多利亚返回谢拉格，带回了许多东西，把你的领地发展了起来。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]然后，你想要为希瓦艾什家争取回三族议会上的地位，也想要彻底打开国门，于是找到了我。
[name="菈塔托丝"]你告诉我，打开国门后，生意大有可做，谢拉格人能吃得更好，穿得更暖。
[name="菈塔托丝"]然后，我和你一起说服了阿克托斯和大长老，谢拉格就此打开了国门，开始跟外面做起了生意。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]那真是一段好时光啊。
[Dialog]
菈塔托丝喝了一口热瘤奶，语气中带着怀念。
那确实是一段好时光，希瓦艾什家与布朗陶家合作，喀兰贸易代表谢拉格开始对外贸易。
资金、技术、人才，源源不断地来到谢拉格，一切似乎都在向着好的方向发展。
[Character(name="avg_172_svrash_1#6$1")]
[name="恩希欧迪斯"]而你主动结束了这样的好时光。
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]菈塔托丝，我曾以为，你会是一个优秀的合作伙伴。
[Character(name="avg_npc_253_1#7$1")]
[name="菈塔托丝"]你也令我失望，恩希欧迪斯。
[name="菈塔托丝"]那是你的好时光，不是我的，也不是阿克托斯的，更不是谢拉格的。
[name="菈塔托丝"]到最后，只有你们喀兰贸易过上了好日子，其他人都没有，这算什么好时光？
[Character(name="avg_npc_253_1#9$1")]
[name="菈塔托丝"]不过，说这些都已经迟了，胜负已定，我是失败者。
[name="菈塔托丝"]败者没有高谈阔论的权力。
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]没有失败者会自称失败者，菈塔托丝。
[Character(name="avg_172_svrash_1#8$1")]
[name="恩希欧迪斯"]说吧，关于我父母的死，你究竟知道什么？
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]恩希欧迪斯，在你看来，你的父母是不是被我爷爷和阿克托斯他父亲联手所害？
[Character(name="avg_172_svrash_1#2$1")]
[name="恩希欧迪斯"]......
[Character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]从当时调查的结果来看，我的父母是死于诺希斯父母故意为之的列车意外事故。
[Character(name="avg_172_svrash_1#8$1")]
[name="恩希欧迪斯"]但我并不相信。而当时，三族议会上，老卢卡和阿克托斯的父亲也如同今天的局面一样，在反对着我父母主导的工业化。
[name="恩希欧迪斯"]我很难相信其中没有联系。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]那么，我可以告诉你真相。
[name="菈塔托丝"]真相是，你的父母确实死于列车意外事故，只是，被我爷爷栽赃给了埃德怀斯一家。
[Character(name="avg_172_svrash_1#8$1")]
[name="恩希欧迪斯"]......
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]别急，我还没说完呢。
[name="菈塔托丝"]爷爷他老人家呢，早就已经打算暗杀你的父母了。
[name="菈塔托丝"]这栋楼，本来是预备等到你的父母来赴约的时候，将他们两个烧死在里面的。
[Character(name="avg_npc_253_1#7$1")]
[name="菈塔托丝"]只是，他们还没到，就在路上遇难了。
[name="菈塔托丝"]于是，这栋过去为他们预留的楼，也就闲置了下来。
[name="菈塔托丝"]对了，爷爷的计划得到了阿克托斯他爹的默许。
[name="菈塔托丝"]而你也知道，在你父母死后几年，阿克托斯他爹就把家主的位置传给了阿克托斯，不知道干什么去了。
[name="菈塔托丝"]现在谁也不知道他死没死。
[Character(name="avg_172_svrash_1#8$1")]
[name="恩希欧迪斯"]你应当不是来向我炫耀的，菈塔托丝。
[stopmusic(fadetime=3)]
[Character(name="avg_npc_253_1#2$1")]
[name="菈塔托丝"]我只是没想到，一直以来，爷爷搞的东西，我碰都不想碰。
[Character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]结果如今，他曾经用来想要谋杀你父母的房子，却被我用来与你同归于尽。
[Character(name="avg_172_svrash_1#8$1")]
[name="恩希欧迪斯"]......这确实是一种绝妙的讽刺。
[Character(name="avg_npc_253_1#11$1")]
[name="菈塔托丝"]两样筹码加起来换你恩希欧迪斯一条命，我想应该并不过分。
[Dialo

... (全文21039字符)
```

### level_act14side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] level_act14side_07_beg
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="24_g3_mainhall",screenadapt="coverall")]
[Character(name="avg_npc_268",name2="avg_npc_268")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Character(name="avg_npc_268",name2="avg_npc_268",focus=1)]
[name="长老A"]唉！
[Character(name="avg_npc_268",name2="avg_npc_268",focus=2)]
[name="长老B"]怎么样？
[Character(name="avg_npc_268",name2="avg_npc_268",focus=1)]
[name="长老A"]那些“山雪鬼”果然不让我们离开。
[name="长老A"]说什么恩希欧迪斯说为了我们的安全着想，要我们待在这里，不要随意走动。
[Character(name="avg_npc_268",name2="avg_npc_268",focus=2)]
[name="长老B"]你看，我就说，他恩希欧迪斯就是要将我们关在这里！
[Character(name="avg_npc_268",name2="avg_npc_268",focus=1)]
[name="长老A"]如今大长老昏迷不醒，圣女又没有戴冠，他嘴上说着另外两家是叛徒，我看他也没安好心。
[Character(name="avg_npc_268",name2="avg_npc_268",focus=2)]
[name="长老B"]嘘......唉，现在说这些又有什么用呢，院内的事务一向由大长老决断，如今大长老这副样子，我们也不知道该怎么办啊。
[Character(name="avg_npc_268")]
[name="长老C"]难道说事情变成这副样子也是耶拉冈德的旨意吗......
[Dialog]
[Character]
[Delay(time=0.51)]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_174_slbell_1#8$1",fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_174_slbell_1#8$1")]
[name="恩雅"]耶拉冈德是否想要如今的境况不好说，但是祂若看到你们这副样子，想必会感到痛心。
[Character(name="avg_npc_268",name2="avg_npc_268",focus=1)]
[name="长老A"]圣、圣女大人！
[Character(name="avg_npc_268",name2="avg_npc_268",focus=2)]
[name="长老B"]我们......我们只是在担忧......
[Character(name="avg_174_slbell_1#1$1")]
[name="恩雅"]有什么值得担心的事？
[Character(name="avg_npc_268")]
[name="长老C"]大长老的情况......还有如今三大家族的状况......
[Character(name="avg_174_slbell_1#8$1")]
[name="恩雅"]刚才我问过医生，大长老的情况确实不容乐观，但他掌管蔓珠院这么多年，想必耶拉冈德也会保佑他。我相信，大长老一定会好起来的。
[name="恩雅"]在这期间，院内无论大小事项一切由我代为决断。
[Character(name="avg_npc_268",name2="avg_npc_268",focus=1)]
[name="长老A"]这......
[Character(name="avg_npc_250_1#5$1")]
[name="雅儿"]圣女大人本就要在戴冠仪式上成为这谢拉格的管理者，大长老也早有让圣女大人接班的意思，现在情况特殊，有何不可？
[name="雅儿"]还是说，各位长老有更好的主意？
[Character(name="avg_npc_268",name2="avg_npc_268",focus=1)]
[name="长老A"]你一个侍女长......
[Character(name="avg_npc_268",name2="avg_npc_268",focus=2)]
[name="长老B"]罢了，雅儿侍女长说得确实不错。
[name="长老B"]我们本就信服圣女大人的能力，现在圣女大人愿意站出来稳定人心，自然没有比这更好的事。
[Character(name="avg_174_slbell_1#3$1")]
[name="恩雅"]另外，各位长老也不必忧心。
[name="恩雅"]大典上发生那样的事，恩希欧迪斯确实有这么做的理由。
[Character(name="avg_174_slbell_1#8$1")]
[name="恩雅"]而即便恩希欧迪斯真的不怀好意，有我在，蔓珠院也不会有事。
[Dialog]
[Character]
若是圣猎中的圣女，其存在只让人觉得耀眼夺目。
如今的圣女，却让人觉得有一股气势，一股无法违抗的气势。
长老们面面相觑，然后纷纷低下头。
“全凭圣女大人安排。”
[Character(name="avg_174_slbell_1#8$1")]
[name="恩雅"]都下去吧。
[Dialog]
[Character(name="avg_npc_268",name2="avg_npc_268",block=true)]
[Delay(time=0.51)]
[playsound(key="$d_gen_walk_n")]
[Character(fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_174_slbell_1#3$1",name2="avg_npc_250_1#1$1",focus=1)]
[name="恩雅"]......
[name="恩雅"]呼......
[Character(name="avg_174_slbell_1#3$1",name2="avg_npc_250_1#7$1",focus=2)]
[name="雅儿"]恩雅，刚才很威风哦。
[Character(name="avg_174_slbell_1#1$1",name2="avg_npc_250_1#7$1",focus=1)]
[name="恩雅"]真的吗？
[Character(name="avg_174_slbell_1#1$1",name2="avg_npc_250_1#1$1",focus=2)]
[name="雅儿"]真的，我还以为你从大典回来后，会很失望呢。
[name="雅儿"]现在看来，是我多心了。
[Character(name="avg_174_slbell_1#7$1",name2="avg_npc_250_1#1$1",focus=1)]
[name="恩雅"]......我确实很失望。
[name="恩雅"]但是，上一次失望的时候，我什么都说不出口。
[name="恩雅"]那时的我，没有办法为自己争取任何东西。
[Character(name="avg_174_slbell_1#8$1",name2="avg_npc_250_1#1$1",focus=1)]
[name="恩雅"]而这一次，我虽然很失望，但我知道，我已经拥有能够改变一些东西的力量了。
[name="恩雅"]既然如此，这一次，我不希望我只能失望了，我应该去做一些事情，让我自己不再失望。
[Character(name="avg_174_slbell_1#8$1",name2="avg_npc_250_1#1$1",focus=2)]
[name="雅儿"]......恩雅，你真是长大了。
[Character(name="avg_174_slbell_1#10$1",name2="avg_npc_250_1#1$1",focus=1)]
[name="恩雅"]如果可以的话，我希望我永远是个孩子，整天去思考这些东西太麻烦了......
[name="恩雅"]......
[Character(name="avg_174_slbell_1#7$1",name2="avg_npc_250_1#1$1",focus=1)]
[name="恩雅"]但你说得对，我长大了。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[musicvolume(volume=0.4, fadetime=1)]
[name="大长老"]信仰......
[name="大长老"]......咳咳。
[Character(name="avg_npc_268")]
[name="修士"]大长老，您终于醒了！
[Dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_258_1#3$1",fadetime=1)]
[Delay(time=1)]
[name="大长老"]不要喧哗。
[Character(name="avg_npc_268")]
[name="修士"]是。
[Character(name="avg_npc_258_1#1$1")]
[name="大长老"]大典......咳咳，怎么样了？老朽......只记得，审问布朗陶家的人的事了，在那之后，就记不得了。
[Character(name="avg_npc_268")]
[name="修士"]您被阿克托斯老爷下毒，然后，诺希斯的出现让局势更加复杂了。
[name="修士"]最后，阿克托斯老爷与菈塔托丝夫人联手想要制服恩希欧迪斯老爷，却被恩希欧迪斯老爷反过来压制......
[Character(name="avg_npc_258_1#1$1")]
[name="大长老"]老朽要听的不是这个。
[name="大长老"]戴冠仪式呢？圣女呢？还政呢？
[Character(name="avg_npc_268")]
[name="修士"]......仪式被中止了，恩希欧迪斯老爷宣布，在收服佩尔罗契家和布朗陶家后，重新举办仪式。
[Character(name="avg_npc_258_1#6$1")]
[name="大长老"]......
[name="大长老"]......恩希欧迪斯，咳咳。
[name="大长老"]圣女呢？
[Character(name="avg_npc_268")]
[name="修士"]圣女大人......此时正在自己的房间里。
[Character(name="avg_npc_258_1#1$1")]
[name="大长老"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
小家伙，第一次旁听三族议会的感觉如何？
......大长老爷爷，我没想到，三族议会竟然是这么无聊的事情。
三位家主只说着和自己家族有关的事，在提到每年行事由哪家出力时也都兴趣缺缺，他们根本不关心耶拉冈德。
呵呵，聪明的孩子，老朽果然没有看错你。
......大长老爷爷，您是故意让我看到这些的吗？
不错。
为什么？
因为总有一天，你会成为大长老。
然后，你会明白，所谓的信仰，究竟意味着什么。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_258_1#1$1")]
[name="大长老"]你......在蔓珠院多久了？
[Character(name="avg_npc_268")]
[name="修士"]啊？二十五年，大长老。
[Character(name="avg_npc_258_1#1$1")]
[name="大长老"]这二十五年，咳咳，你可觉得，这蔓珠院，这谢拉格有什么变化？
[Character(name="avg_npc_268")]
[name="修士"]这......除了希瓦艾什家带来的一些东西，我觉得没有什么变化。
[Character(name="avg_npc_258_1#3$1")]
[name="大长老"]这片土地，千年以来都没有什么变化。
[name="大长老"]未来，也不应当有所变化。
[Character(name="avg_npc_258_1#1$1")]
[name="大长老"]咳咳，扶老朽起来。
[Character(name="avg_npc_268")]
[name="修士"]可是大长老，您的身体......
[Cha

... (全文15611字符)
```

### level_act14side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] level_act14side_07_end
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="24_g10_manorhouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Character(name="avgnew_173_slchan_1#8$1",name2="avg_npc_267_1#1$1",fadetime=1)]
[Delay(time=2)]
[Character(name="avgnew_173_slchan_1#8$1",name2="avg_npc_267_1#1$1",focus=1)]
[name="恩希亚"]......切斯特叔叔，为什么我不能出去？
[Character(name="avgnew_173_slchan_1#8$1",name2="avg_npc_267_1#1$1",focus=2)]
[name="切斯特"]总裁吩咐了，在他回来之前，不允许你四处跑。
[Character(name="avgnew_173_slchan_1#7$1",name2="avg_npc_267_1#1$1",focus=1)]
[name="恩希亚"]那老哥什么时候回来？
[Character(name="avgnew_173_slchan_1#7$1",name2="avg_npc_267_1#1$1",focus=2)]
[name="切斯特"]总裁现在应当正在前往圣山的路上，过两天就能回来了。
[Character(name="avgnew_173_slchan_1#8$1",name2="avg_npc_267_1#1$1",focus=1)]
[name="恩希亚"]我只是想去散步也不行吗？
[Character(name="avgnew_173_slchan_1#8$1",name2="avg_npc_267_1#2$1",focus=2)]
[name="切斯特"]只是在宅子附近的话......我会派人跟着你。
[name="切斯特"]恩希亚，现在谢拉格的形势十分险峻，这也是为了你好。
[Character(name="avgnew_173_slchan_1#7$1",name2="avg_npc_267_1#2$1",focus=1)]
[name="恩希亚"]......唉。
[Dialog]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g8_nobleroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]老哥......你就一定要这么做吗？
[Character(name="avgnew_173_slchan_1#7$1")]
[name="恩希亚"]博士，我该怎么办......
[Dialog]
[Character]
[stopmusic(fadetime=5)]
[Character(name="avg_422_aurora_1#1$1",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avgnew_173_slchan_1#3$1")]
[name="恩希亚"]极光？！
[Character(name="avg_422_aurora_1#1$1")]
[name="极光"]嘘——好严密的守备，我好不容易才进来的。
[Character(name="avgnew_173_slchan_1#3$1")]
[name="恩希亚"]你不是和Sharp队长一起去博士那边了吗？
[Character(name="avg_422_aurora_1#1$1")]
[name="极光"]嗯，我这次来，就是博士有话要我带给你。
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g12_mountpath",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_206_gnosis_1#4$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="诺希斯"]你确定？
[Character(name="avg_206_gnosis_1#4$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]是的，阿克托斯在领地内集结了大量士兵，但是，这支队伍的领导者是那位博士，而不是阿克托斯。
[Character(name="avg_206_gnosis_1#7$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="诺希斯"]阿克托斯人呢？
[Character(name="avg_206_gnosis_1#7$1",name2="avg_npc_255_1#6$1",focus=2)]
[name="莫希"]不清楚......根据眼线的回报，在将这支队伍的指挥权正式交给博士后，他就不知所踪了。
[Character(name="avg_206_gnosis_1#7$1",name2="avg_npc_255_1#6$1",focus=1)]
[name="诺希斯"]......那个博士的队伍是诱饵？不，不会这么简单。
[name="诺希斯"]规模呢？
[Character(name="avg_206_gnosis_1#7$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]佩尔罗契领地响应阿克托斯号召的家族和您想象的差不多，以此估算的话——阿克托斯应该不可能再集结起另外一支同样规模的队伍。
[Character(name="avg_206_gnosis_1#2$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="诺希斯"]但是他不可能待在后方，有另一支队伍的可能性很大。
[Character(name="avg_206_gnosis_1#2$1",name2="avg_npc_255_1#1$1",focus=2)]
[name="莫希"]佩尔罗契家的战士本来就很擅长在山野中行动，这确实不是没有可能。
[Character(name="avg_206_gnosis_1#7$1",name2="avg_npc_255_1#1$1",focus=1)]
[name="诺希斯"]但是，无论是诱饵还是主力，这支队伍都不能放任不理。
[name="诺希斯"]让魏斯传令，命战士们在山下集结，等候命令。
[name="诺希斯"]然后派人去盯着大部队，你主要负责去找出阿克托斯的踪迹。
[Character(name="avg_206_gnosis_1#7$1",name2="avg_npc_255_1#6$1",focus=2)]
[name="莫希"]是。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g8_nobleroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avgnew_173_slchan_1#3$1")]
[name="恩希亚"]博士......希望我能登上圣山，潜入蔓珠院去找姐姐？
[Character(name="avg_422_aurora_1#5$1")]
[name="极光"]是的。
[name="极光"]博士的意思是，如今，佩尔罗契家和希瓦艾什家之间的冲突已经几乎无法避免了。
[name="极光"]但是，如果说还有一个人可以阻止这一切的话，那么，这个人必然是你的姐姐，当代圣女，恩雅·希瓦艾什。
[Character(name="avgnew_173_slchan_1#7$1")]
[name="恩希亚"]但是......
[Character(name="avg_422_aurora_1#4$1")]
[name="极光"]原本，博士是想秉承罗德岛不干政的方针，选择袖手旁观的。
[name="极光"]但是，博士指出一点，既然还政对于恩希欧迪斯先生来说只是一个幌子，那么他也必然不会将对谢拉格的信仰放在眼中。
[name="极光"]而一旦希瓦艾什家的部队真的击败了佩尔罗契家的部队，那么对他来说，阻拦他将谢拉格纳入囊中的，也就只有蔓珠院。
[name="极光"]也就是谢拉格人民的信仰对象，圣女。
[Character(name="avg_422_aurora_1#1$1")]
[name="极光"]博士说，他并不是想要让你去说服圣女做些什么，而是你曾经拜托过他，希望他能够帮忙缓和你们兄妹之间关系。
[name="极光"]他对于自己来到谢拉格后没有帮上忙一直感到有些自责。
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]这怎么能怪博士！我才要对博士和随行的各位道歉，明明应该是一次愉快的旅行，结果却因为老哥而变成了这个样子......
[Character(name="avg_422_aurora_1#1$1")]
[name="极光"]这也不怪你呀，崖心。
[name="极光"]总之，博士的意思是，他可以不在乎很多东西，但一方面他从一开始就被恩希欧迪斯先生卷了进来。
[name="极光"]另一方面，你是恩希欧迪斯先生的妹妹也是不争的事实。
[name="极光"]所以，博士还是打算做一些什么。
[name="极光"]让你上山，是希望你能成为圣女身边的保险。
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]博士希望我在必要的时候去阻止老哥。
[Character(name="avg_422_aurora_1#5$1")]
[name="极光"]或者在必要的时候带着圣女逃跑。
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]......
[Dialog]
[Character]
恩希亚下意识地摸了摸自己手中的绳环。
这是小时候，姐姐亲手为她编织的。
[stopmusic(fadetime=1)]
[Character(name="avgnew_173_slchan_1#2$1")]
[name="恩希亚"]......
[Dialog]
[delay(time=1.5)]
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]我去。
[Character(name="avg_422_aurora_1#1$1")]
[name="极光"]这是一次潜入行动，我和其他的随行干员会一起协助你。
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]......不。
[name="恩希亚"]我有更好的办法。
[Character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]大家只要能帮我到达圣山脚下就好，剩下的，交给我一个人。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g12_mountpath",screenadapt="coverall")]
[playMusic(intro="$darkness

... (全文17133字符)
```

### level_act14side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] level_act14side_08_beg
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="24_g5_guestroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_255_1#6$1")]
[name="莫希"]大人，我沿着佩尔罗契家边缘的林地找了一圈，没有找到行军的痕迹。
[Character(name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]......继续找。
[Character(name="avg_npc_255_1#1$1")]
[name="莫希"]是。
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="avg_198_blackd_1#9$1",fadetime=1)]
[Delay(time=1.5)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_198_blackd_1#9$1")]
[name="魏斯"]诺希斯，有情况。
[name="魏斯"]古罗从博士的队伍里分出来，带着一部分人急行军直接绕过了圣山，突破关口，占领了车站！
[Character(name="avg_206_gnosis_1#7$1")]
[name="诺希斯"]你说什么？！
[Character(name="avg_198_blackd_1#9$1")]
[name="魏斯"]现在，古罗的队伍驱赶了车站里的人，而且，还有一支队伍向着科林斯镇去。
[Character(name="avg_npc_255_1#8$1")]
[name="莫希"]尤卡坦现在被关押在那里......他们的目的是救人？
[Character(name="avg_206_gnosis_1#7$1")]
[name="诺希斯"]不可能。这样的效率太低了，他们必然有别的目的。
[name="诺希斯"]莫希，你认为，你所看到的那个博士的行进路线，是向哪里靠近的？
[Character(name="avg_npc_255_1#8$1")]
[name="莫希"]......他们挑选了一条可以通往圣山，也可以通往关口的路线。
[Character(name="avg_198_blackd_1#6$1")]
[name="魏斯"]嘶——难道说，博士的目的真的是直接绕过圣山，进攻我们的领地......
[Character(name="avg_206_gnosis_1#2$1")]
[name="诺希斯"]我应该警告过你们这种可能性。
[Character(name="avg_206_gnosis_1#8$1")]
[name="诺希斯"]不，我自己也大意了，应该在关口驻扎更多的兵力。
[Character(name="avg_198_blackd_1#7$1")]
[name="魏斯"]博士......
[Character(name="avg_206_gnosis_1#8$1")]
[name="诺希斯"]但是，阿克托斯人还不见踪影，还不能完全断定他们的目的......
[Character(name="avg_206_gnosis_1#7$1")]
[name="诺希斯"]......啧，派瓦莱丝去车站解决古罗，然后让魏斯去科林斯镇。
[name="诺希斯"]把山下的队伍分出一部分，去关口驻扎，防止博士的队伍突破关口进入我们的领地。
[Character(name="avg_198_blackd_1#6$1")]
[name="魏斯"]我明白了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g11_snowylane",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_283_1$1")]
[name="佩尔罗契家战士"]将军，我们已经占领了这个车站，为什么还要在这等着啊？
[name="佩尔罗契家战士"]博士让我们尽量不要伤人，但没说不能把这里砸了吧？这车站可就是希瓦艾什那套东西的象征啊。
[Character(name="avg_npc_260_1#1$1")]
[name="古罗"]别急，下一班列车来了再说——
[name="古罗"]啧，是不是下一班来着，我看看博士给我留的纸条......
[name="古罗"]嗯，应该没错。
[Dialog]
[Character]
[playsound(key="$d_avg_trainwhistle")]
[Delay(time=4)]
[playsound(key="$d_avg_train")]
[Delay(time=4)]
[Character(name="avg_npc_277_1#1$1",name2="avg_npc_278_1#1$1",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_277_1#1$1",name2="avg_npc_278_1#1$1",focus=1)]
[name="谢拉格商人A"]噫，发生了什么事？！
[Character(name="avg_npc_260_1#6$1")]
[name="古罗"]这个车站已经被我佩尔罗契家的古罗占领了，不想死的就给我滚！
[Character(name="avg_npc_277_1#1$1",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人B"]佩尔罗契家的人怎么会出现在这里？！
[Character(name="avg_npc_277_1#1$1",name2="avg_npc_278_1#1$1",focus=1)]
[name="谢拉格商人A"]而且是那个最凶恶的古罗！难道佩尔罗契家打过来了！
[Character(name="avg_npc_277_1#1$1",name2="avg_npc_278_1#1$1",focus=2)]
[name="谢拉格商人B"]噫——我还不想死，快跑！
[Character(name="avg_npc_260_1#1$1")]
[name="古罗"]没错，跑就对了！跑快点！
[Dialog]
[Character]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[PlaySound(key="$d_avg_snowrun", volume=1)]
[delay(time=2)]
[Dialog]
[Character]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[Character(name="avgnew_173_slchan_1#8$1",name2="avg_422_aurora_1#1$1",fadetime=1.5)]
[Delay(time=3)]
[Character(name="avgnew_173_slchan_1#8$1")]
[name="恩希亚"]......
[Character(name="avgnew_173_slchan_1#1$1")]
[name="恩希亚"]呃，古罗将军，那个，谢谢你接应我。
[Character(name="avg_npc_260_1#1$1",name2="avgnew_173_slchan_1#1$1",focus=1)]
[name="古罗"]哼，接应希瓦艾什家的女儿，要不是博士跟我说你是他的帮手，我可不想干这活。
[name="古罗"]你真的和你哥不是一伙的？
[Character(name="avg_npc_260_1#1$1",name2="avgnew_173_slchan_1#8$1",focus=2)]
[name="恩希亚"]我是来阻止老哥的。
[Character(name="avg_npc_260_1#1$1",name2="avgnew_173_slchan_1#8$1",focus=1)]
[name="古罗"]......我不相信你，但我相信博士，那位Sharp跟我说过，让我相信他带来的胜利。
[name="古罗"]行了，你不是还要上山，赶紧的。
[name="古罗"]等你们走了，我还得让这铁路瘫......什么来着，哦，对了，瘫痪，免得希瓦艾什家的援军来得太快。
[Character(name="avgnew_173_slchan_1#10$1")]
[name="恩希亚"]嗯，还是谢谢你，古罗将军！
[Dialog]
[PlaySound(key="$d_avg_snowrun", volume=1)]
[Character(fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_260_1#7$1")]
[name="古罗"]......这一家子，真是闹不明白。
[Character(name="avg_npc_260_1#1$1")]
[name="古罗"]管他的，反正我要做好自己的事。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[delay(time=1)]
[Background(image="24_g7_thoroughfare",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[Character(name="avg_npc_262_1#10$1",fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_262_1#10$1")]
[name="休露丝"]......哼，那个傻大个虽然人挺傻，战斗力确实是不差的。
[name="休露丝"]车站那边交给他应该没问题。
[Character(name="avg_npc_262_1#6$1")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=20, fadeout=true, block=false)]
[name="休露丝"]接下来就是——哎哟，我的屁股......
[Character(name="avg_npc_283_1#1$1",name2="avg_npc_283_1#1$1",focus=1)]
[name="布朗陶家战士A"]休露丝夫人，您下驮兽休息一下吧，接下来交给我们就好。
[Character(name="avg_npc_262_1#2$1")]
[name="休露丝"]哼，现在哪里是休息的时候。
[name="休露丝"]我们的任务可是比古罗的还要艰巨得多。
[Character(name="avg_npc_262_1#7$1")]
[name="休露丝"]除了救出尤卡坦，还要尽可能地占领科林斯镇。
[name="休露丝"]在博士那边成功前，要尽量吸引希瓦艾什家的注意。
[Character(name="avg_npc_283_1#1$1",name2="avg_npc_283_1#1$1",focus=1)]
[name="布朗陶家战士A"]夫人，我们的人数真的撑得住这样闹吗，那个博士会不会是在害我们？
[Character(name="avg_npc_283_1#1$1",name2="avg_npc_283_1#1$1",focus=2)]
[name="布朗陶家战士B"]是啊，大夫人都......
[Character(name="avg_npc_262_1#8$1")]
[name="休露丝"]闭嘴。
[Character(name="avg_npc_262_1#7$1")]
[name="休露丝"]听着，菈塔托丝撑着这个家这么久，她现在累了，所以她把这件事交给了我来做。
[name="休露丝"]现在是我们布朗陶家危急存亡的关头，做好了，我们布朗陶家还有未来，做不好，我们就改姓希瓦艾什。
[name="休露丝"]不管他恩希欧迪斯想做什么，想把这谢拉格变成什么样，但我们布朗陶家从来不是任人宰割的。
[Character(name="avg_npc_262_1#8$1")]
[name="休露丝"]想改姓的话现在就可以走，还对布朗陶这个姓氏有念想的都跟我来！
[Character(name="avg

... (全文23036字符)
```

### level_act14side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[theater(mode=true)]
[Background(screenadapt="showall", image="24_g13_mountpath_s",x=0, y=0, xScale=1, yScale=1,fadetime=0.5)]
[playsound(key="$d_avg_snowstormlp", channel="wind",fadetime=2,loop=true,volume=1)]
[playsound(key="$d_avg_falcon", volume=1)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_drumlp", channel="slide",fadetime=2,loop=true,volume=0.4)]
[PlaySound(key="$d_avg_snowrun")]
[CameraShake(duration=2, xstrength=0, ystrength=15, vibrato=20, randomness=90, fadeout=true, block=false)]
[backgroundTween(xFrom=0, yFrom=0, xTo=0, yTo=0, xScaleFrom=1, yScaleFrom=1, xScaleTo=1.3, yScaleTo=1.3, duration=2.5, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.2)]
[PlaySound(key="$d_avg_bldwhoosh", volume=2)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Character(name="avg_npc_257_1#4$1")]
[PlaySound(key="$swordtsing1", volume=0.9)]
[characteraction(name="middle", type="jump", xpos=-100, power=0, times=1, fadetime=0.4,block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[characteraction(name="middle", type="jump", xpos=200, power=0, times=1, fadetime=0.4,block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[PlaySound(key="$swordtsing2", volume=0.9)]
[characteraction(name="middle", type="jump", xpos=-100, power=0, times=1, fadetime=0.4,block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=20, ystrength=22, vibrato=50, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[theater(mode=false)]
[name="锏"]......你是萨尔贡宫廷的人？
[dialog]
[character]
[delay(time=0.1)]
[Character(name="avg_npc_252")]
[name="Sharp"]......上一份工作。
[name="Sharp"]想不到你能认出萨尔贡的剑术。
[dialog]
[characteraction(name="middle", type="move", xpos=140, fadetime=0.05,block=false)]
[Character(fadetime=0.5)]
[delay(time=0.51)]
[Dialog]
[PlaySound(key="$d_avg_bldwhoosh", volume=2)]
[delay(time=0.51)]
[PlaySound(key="$d_avg_singleblunt", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing1", volume=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing2", volume=0.5)]
[PlaySound(key="$swordtsing2", volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing2", volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=40, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$swordtsing4", volume=0.7)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=40, randomness=90, fadeout=true)]
[delay(time=1)]
[PlaySound(key="$bodyfalldown3", volume=1)]
[Character(name="avg_npc_257_1#6$1",fadetime=0.3)]
[name="锏"]我对法术不感兴趣，但是和兵器有关的东西，想忘都难。
[Character(name="avg_npc_252")]
[name="Sharp"]难怪黑骑士被称作天生的武者。
[Character(name="avg_npc_257_1#4$1")]
[name="锏"]天生？
[Character(name="avg_npc_257_1#8$1")]
[name="锏"]呵。
[name="锏"]你知道，从“不会使用法术的莱塔尼亚残次品”，到“天生的武者”需要花费多长的时间？
[dialog]
[characteraction(name="middle", type="move", xpos=-140, fadetime=0.05,block=false)]
[Character(fadetime=0.5)]
[Dialog]
[Delay(time=0.51)]
[CameraShake(duration=2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[stopsound(channel="slide", fadetime=1)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4,fadetime=4)]
[PlaySound(key="$d_avg_bldwhoosh", volume=1)]
[dialog]
[character]
[delay(time=0.1)]
[Character(name="avg_npc_252",enter="left",name2="avg_npc_257_1#4$1",enter2="right",fadetime=0.7,block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=false)]
[CameraShake(duration=100, xstrength=30, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=

... (全文50396字符)
```

### level_act14side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g3_mainhall",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$longmenoffice_intro", key="$longmenoffice_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]既然此事已定，那么接下来，我们三家需要频繁接洽。
[character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]商讨将部分权力移交给圣女的具体事宜，以及各族需要保留的部分。
[character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]不过，在此之外，我们三人对仪式的准备也同样重要。
[character(name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]我提议，将即将到来的大典，同时也作为圣女大人接管大权的典礼举行。
[character(name="avg_172_svrash_1#4$1")]
[name="恩希欧迪斯"]此事与移交权力并不由同样的人来操办，因此可以同步进行，而仪式又与家主的参与紧密相关，不知道两位有没有意见？
[character(name="avg_npc_254_1#2$1")]
[name="阿克托斯"]既然已经决定这么去做，那也是迟早的事。
[character(name="avg_npc_253_1#4$1")]
[name="菈塔托丝"]哈......
[character(name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]今年的大典，同时也是圣女大人接管大权的典礼吗......倒是很让人期待。
[character(name="avg_npc_258_1#1$1")]
[name="大长老"]既然如此，老朽这就差下面的人起草相关文书，尽快发往谢拉格全境。
[character(name="avg_npc_258_1#7$1")]
[name="大长老"]想必谢拉格民众也一定会为这个消息感到高兴。
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]等等。
[character(name="avg_172_svrash_1#4$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="恩希欧迪斯"]还有什么事？
[character(name="avg_172_svrash_1#4$1",name2="avg_npc_254_1#5$1",focus=2)]
[name="阿克托斯"]别想蒙混过关，恩希欧迪斯。谷地和矿区在未来几日的管理呢？诺希斯过去管这一片，他被你撤了职，谁来监管交接事宜？
[character(name="avg_172_svrash_1#10$1",name2="avg_npc_254_1#5$1",focus=1)]
[name="恩希欧迪斯"]不必为我担忧，阿克托斯。
[character(name="avg_172_svrash_1#10$1",name2="avg_npc_254_1#5$1",focus=1)]
[name="恩希欧迪斯"]我自谢拉格外请来了一位专家。
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#5$1",focus=1)]
[name="恩希欧迪斯"]这位专家将对谷地和矿区展开医疗方面的实地考察，并着手希瓦艾什领地内医疗服务设施的建设。
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#5$1",focus=1)]
[name="恩希欧迪斯"]这两块地区的监管，我也将全权交予此人负责。
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#5$1",focus=1)]
[name="恩希欧迪斯"]算算时间，对方乘坐的列车此时应当快要抵达圣山了，两位若是有意要见一见专家本人，也可以等上片刻。
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#8$1",focus=2)]
[name="阿克托斯"]少说这些有的没的！我不知道你请了什么人，又想要拿医疗做什么文章。但是！
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#7$1",focus=2)]
[name="阿克托斯"]你口中这个所谓的“专家”，必须在我的视线范围内行动。
[character(name="avg_172_svrash_1#8$1",name2="avg_npc_254_1#7$1",focus=1)]
[name="恩希欧迪斯"]......这是我的贵客，阿克托斯。
[character(name="avg_172_svrash_1#8$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]正因为他是你的贵客。
[character(name="avg_172_svrash_1#8$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]你说矿区的过度开采全是诺希斯干的，我其实无所谓是不是。
[character(name="avg_172_svrash_1#8$1",name2="avg_npc_254_1#7$1",focus=2)]
[name="阿克托斯"]在我看来，你的手下，全都是诺希斯，少了一个，还会有下一个。
[character(name="avg_172_svrash_1#8$1",name2="avg_npc_254_1#7$1",focus=2)]
[name="阿克托斯"]你的人要管土地的移交，可以，那么，就让那位专家做给我这个粗人看看。
[character(name="avg_172_svrash_1#8$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]只要这位专家好好做事，那此人不仅是你恩希欧迪斯的贵客，也会是我阿克托斯的客人，我保准好好招待。
[character(name="avg_172_svrash_1#9$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="恩希欧迪斯"]......
[character(name="avg_172_svrash_1#9$1",name2="avg_npc_254_1#7$1",focus=2)]
[name="阿克托斯"]怎么，方才夸夸其谈，这事倒要考虑这样久吗？
[character(name="avg_172_svrash_1#9$1",name2="avg_npc_254_1#8$1",focus=2)]
[name="阿克托斯"]要是坦坦荡荡，你有什么放心不下的。还是说你请来的是另一个诺希斯，你要做一些见不得人的小动作？
[character(name="avg_172_svrash_1#2$1",name2="avg_npc_254_1#8$1",focus=1)]
[name="恩希欧迪斯"]......蔓珠院的护卫一向由佩尔罗契家提供，既然我要将土地交给蔓珠院，那接受佩尔罗契家的“陪同”，哪里有放心不下一说？
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#8$1",focus=1)]
[name="恩希欧迪斯"]不过......
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#8$1",focus=1)]
[name="恩希欧迪斯"]给你一个忠告，阿克托斯——当心，这位客人没有那么好招待。
[character(name="avg_172_svrash_1#1$1",name2="avg_npc_254_1#10$1",focus=2)]
[name="阿克托斯"]哈，放心，没有我佩尔罗契家“招待”不来的客人！
[character(name="avg_npc_254_1#4$1")]
[name="阿克托斯"]——我倒要看看，你的客人是不是和你一样硬骨头。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[Character]
[Background(image="24_g13_mountpath_s",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_253_1#4$1",name2="avg_npc_262_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_253_1#4$1",name2="avg_npc_262_1#1$1",focus=1)]
[name="菈塔托丝"]......休露丝，你去见一见那个人。
[character(name="avg_npc_253_1#4$1",name2="avg_npc_262_1#6$1",focus=2)]
[name="休露丝"]又要我跑腿？
[character(name="avg_npc_253_1#7$1",name2="avg_npc_262_1#6$1",focus=1)]
[name="菈塔托丝"]我现在没有心情跟你开玩笑，休露丝。
[character(name="avg_npc_253_1#7$1",name2="avg_npc_262_1#9$1",focus=2)]
[name="休露丝"]啧。
[character(name="avg_npc_262_1#6$1")]
[name="休露丝"]莫希，莫希！
[character(name="avg_npc_255_1#6$1")]
[name="莫希"]属下在。
[character(name="avg_npc_262_1#1$1")]
[name="休露丝"]去给我备车！
[character(name="avg_npc_255_1#6$1")]
[name="莫希"]是。
[character(name="avg_npc_262_1#10$1")]
[name="休露丝"]尤卡坦，走！
[character(name="avg_npc_263_1#1$1")]
[name="尤卡坦"]夫人，当心脚下。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_npc_261_1#1$1",name2="avg_npc_254_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_261_1#1$1",name2="avg_npc_254_1#1$1",focus=2)]
[name="阿克托斯"]......瓦莱丝，你怎么看？
[character(name="avg_npc_261_1#3$1",name2="avg_npc_254_1#1$1",focus=1)]
[name="瓦莱丝"]......属下无能，无法看出恩希欧迪斯的真实意图。
[character(name="avg_npc_261_1#3$1",name2="avg_npc_254_1#6$1",focus=2)]
[name="阿克托斯"]不怪你，不过菈塔托丝那个奸诈的女人竟然就这样答应了，我有点没想明白。
[character(name="avg_npc_261_1#8$1",name2="avg_npc_254_1#6$1",focus=1)]
[name="瓦莱丝"]以菈塔托丝大人的风格，恐怕早有其他打算了。
[character(name="avg_npc_261_1#8$1",nam

... (全文48930字符)
```

### level_act14side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g1_snowyforest",screenadapt="showall",x=0, y=20, xScale=1.2, yScale=1.2)]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_253_1#1$1", fadetime=1.5)]
[delay(time=2)]]
[name="菈塔托丝"]喂。
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="菈塔托丝"]来这种荒郊野岭是想挖出什么宝贝给我看？
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]当然是打算杀人灭口。
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#9$1",focus=1)]
[name="菈塔托丝"]你就嘴硬吧。你在这里被我杀人灭口，倒是个不错的选择。
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]就快到了。菈塔托丝，你对此地可还有印象？
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="菈塔托丝"]......这一带，我没记错的话，通往谢拉格外的路早就因为桥梁被风雪毁坏而废弃了。
[name="菈塔托丝"]这里本来就暴风雪频发，连加固过的桥梁都难保安稳，人们也就放弃了对这边道路的再开发。
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]你在图里卡姆的关口有多少人，菈塔托丝？
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="菈塔托丝"]足以让我知道恩希欧迪斯每天都在和谁交易什么的程度。
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=2)]
[name="诺希斯"]那你知道，近日有多少武装人员和装备从你的眼皮底下绕过，进入了谢拉格吗？
[character(name="avg_npc_253_1#9$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="菈塔托丝"]......
[character(name="avg_npc_253_1#1$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="菈塔托丝"]你难道要说，恩希欧迪斯绕开图里卡姆，在这种地方也开辟了铁路？
[character(name="avg_npc_253_1#2$1",name2="avg_206_gnosis_1#1$1",focus=1)]
[name="菈塔托丝"]......怎么可能。
[character(name="avg_npc_253_1#2$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]你看，来了。
[character(name="avg_npc_253_1#4$1",name2="avg_206_gnosis_1#9$1",focus=1)]
[name="菈塔托丝"]可那条路前面是片峡谷......
[character(name="avg_npc_253_1#4$1",name2="avg_206_gnosis_1#9$1",focus=2)]
[name="诺希斯"]不再是了。
[dialog]
[delay(time=1)]
[character(fadetime=0.5)]
[PlaySound(key="$d_avg_drawbridge", volume=5)]
[delay(time=2)]
[character(name="avg_npc_253_1#4$1")]
[name="菈塔托丝"]......
[character(name="avg_npc_253_1#7$1")]
[name="菈塔托丝"]............
[character(name="avg_npc_253_1#8$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlayMusic(intro="$m_bat_essenceofevolution_intro", key="$m_bat_essenceofevolution_loop", volume=0.4)]
[name="菈塔托丝"]这不可能！
[character(name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]用装置把桥梁、轨道、承重结构全都收在两边的悬崖山体中。
[name="诺希斯"]为了掩人耳目，只在列车将要通过的时候再从山体中伸出架成桥梁......
[character(name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]多么简单的构思，却要用到多么复杂的设计去实现。真让我有些不舍。
[Dialog]
[Character]
[backgroundTween(xFrom=0, yFrom=20, xTo=0, yTo=-20, xScale=1.2, yScale=1.2, xScaleTo=1.3, yScaleTo=1.3, duration=10, block=false)]
地面上新落的雪令人难以察觉地颤动着，一种细微的声响在渐渐变强。
[Dialog]
[delay(time=1)]
桥梁的轴承间亮起星星点点的火光，一如照亮谢拉格的文明灯火。
[Dialog]
[delay(time=1)]
[PlaySound(key="$d_avg_train", volume=0.4)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_trainwhistle", volume=0.4)]
[PlaySound(key="$d_avg_trainlp", volume=0.6, loop=true, channel="bgs")]
[Delay(time=2)]
[StopSound(channel="bgs", fadetime=1)]
[musicvolume(volume=0, fadetime=2)]
列车头带着身后一节节车厢飞快地碾过桥梁，那些火光或许是感受到载货车厢的重量，也逐渐雀跃起来。
[dialog]
[character(name="avg_206_gnosis_1#2$1",blackstart=0.05,blackend=0.2,fadetime=1)]
[delay(time=1)]
青年转过身来面向众人，打了个响指。
[dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.2, block=true)]
[Blocker(a=0, r=0.95, g=0.5, b=0.3,fadetime=0.25, block=true)]
[character(name="avg_206_gnosis_1#9$1",blackstart=0.05,blackend=0.2,fadetime=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_snapping", volume=1)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=0.85,g=0.3, b=0.3,fadetime=0.1, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=255, g=0.5, b=0.3,fadetime=0.1, block=true)]
[Blocker(a=0, r=1, g=1, b=1, fadetime=0.4, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Image(image="24_i14", fadetime=0.2, xScale=1.7, yScale=1.7, x=0, y=0)]
[ImageTween(xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1.5, yScaleTo=1.5, duration=0.5, ease="InOutBounce", block=true)]
[musicvolume(volume=0,fadetime=0)]
[PlaySound(key="$d_gen_explo_n")]
[CameraShake(duration=2, xstrength=70, ystrength=70, vibrato=60, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0.8, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=-1, xstrength=3, ystrength=5, vibrato=50, randomness=100, fadeout=false, block=false)]
火光突然膨胀起来，变得越来越亮，越来越暖，连同列车中段的数节车厢也一并吞没，胜似节日庆典夜晚的篝火。
终于，这火光不再能够包裹住它吞下的东西，伴随着一声震耳欲聋的声响残忍地撕开了车厢。
[dialog]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[playsound(key="$e_atk_magic_n", volume=1)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$p_atk_lasergun_n",delay=0.2,volume=0.4)] 
[PlaySound(key="$d_gen_explo_n",delay=0.4,volume=0.6)]
[CameraShake(duration=2, xstrength=70, ystrength=70, vibrato=60, r

... (全文14938字符)
```

### level_act14side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g6_square",screenadapt="showall")]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0.6, loop=true, channel="bse")]
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]什么？你说，昨天恩希欧迪斯老爷在山里被人袭击了！
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=2)]
[name="谢拉格平民B"]什么？真的吗？
[Character(name="avg_npc_283_1#1$1")]
[name="谢拉格战士"]当然是真的，阿克托斯老爷让古罗将军带人赶过来给大长老报信。
[name="谢拉格战士"]我三叔的另一个侄子就是跟着古罗将军回来的。
[name="谢拉格战士"]他们刚刚赶到这边，我就是从他那里听来的。
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]好小子，这可是个大消息啊！
[Character(name="avg_npc_283_1#1$1")]
[name="谢拉格战士"]嘿嘿！
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=2)]
[name="谢拉格平民B"]不过，谁这么大的胆子，居然敢袭击恩希欧迪斯老爷？！而且居然是在圣猎途中！
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]难道不是山雪鬼吗？
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民C"]都说是人了，怎么会是山雪鬼。
[name="谢拉格平民C"]要我说，肯定是佩尔罗契家或者布朗陶家的人做的。
[name="谢拉格平民C"]过去佩尔罗契家和布朗陶家那么打压希瓦艾什家，嘴上说是因为恩希欧迪斯老爷做的事践踏了信仰。
[name="谢拉格平民C"]谁知道是不是盯上了希瓦艾什家的土地。
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格战士"]这种话可不能乱说。
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民C"]乱说？你不会不知道，恩希欧迪斯老爷当初离开谢拉格外出留学后，布朗陶家吞了希瓦艾什家多少土地吧？
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=2)]
[name="谢拉格平民B"]......
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民C"]现在恩希欧迪斯老爷改过自新，主动向圣女大人示好，两家没法打压希瓦艾什家了，这下着急了。
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]这......
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格战士"]你、你是哪家的人？！
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民C"]我是布朗陶家的人，怎么着？
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格战士"]你是布朗陶家的？布朗陶家的人怎么会这么说自己家的事！
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民C"]因为我在谷地工作了这么久，我打心眼里为恩希欧迪斯老爷感到不公平！
[name="谢拉格平民C"]恩希欧迪斯老爷为谢拉格带来了这么多好的东西，却一直在三族议会上被打压。
[name="谢拉格平民C"]现在恩希欧迪斯老爷主动提出还政，而且还主动和蔓珠院以及圣女大人修复关系，却还要被这么对待。
[name="谢拉格平民C"]就算你是佩尔罗契家的人，你良心不会痛吗！
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=1)]
[name="谢拉格战士"]你......我......
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]这......倒也是。
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=2)]
[name="谢拉格平民B"]对啊，不管怎么说，袭击恩希欧迪斯老爷这件事做得实在是太不应该了。
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]而且发生在圣猎这么重要的仪式里，这也是对耶拉冈德的大不敬。
[Character(name="avg_npc_283_1#1$1", name2="avg_npc_277_1#1$1",focus=2)]
[name="谢拉格平民C"]没错，这件事不管怎么说，都必须要有个交代才行！
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=2)]
[name="谢拉格平民B"]说得对。
[Character(name="avg_npc_279_1#1$1", name2="avg_npc_280_1#1$1",focus=1)]
[name="谢拉格平民A"]没错，必须要找出凶手！
[StopSound(channel="bse", fadetime=1)]
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]怎么了，昨晚没睡好吗？你的脸色不太好。
[Dialog]
[Character(name="avg_npc_250_1#1$1",focus=-1)]
[Decision(options="恩希欧迪斯果然遇到了麻烦。", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]嗯，这件事已经传开了，大家都在讨论这件事。
[name="雅儿"]我看已经有许多人说，这件事必须要有一个说法。
[name="雅儿"]你这副表情，难道这出乎了你的预料吗？
[Dialog]
[Character(name="avg_npc_250_1#1$1",focus=-1)]
[Decision(options="就是因为这没有出乎我的预料。", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_250_1#3$1")]
[name="雅儿"]嗯？那你在纠结什么呢？
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]诺希斯因为和恩希欧迪斯不合，和他分道扬镳后，一直在图谋着推翻恩希欧迪斯。
[name="雅儿"]而你认为恩希欧迪斯不会没有对策，你也不想插手三大家族的事务，所以选择了在这里优哉游哉地逛大典。
[name="雅儿"]我只说表面情况啊，这么看的话，情况不就是这样吗？
[Dialog]
[Character(name="avg_npc_250_1#1$1",focus=-1)]
[Decision(options="各方势力对情况的把握都有偏差。;未必如此。", values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_250_1#8$1")]
[name="雅儿"]真不知道你整天脑子里都在考虑什么东西。
[Character(name="avg_npc_250_1#2$1")]
[name="雅儿"]不过感觉我也被你传染得开始喜欢思考这些事了，我也来想想看吧。
[Character(name="avg_npc_250_1#6$1")]
[name="雅儿"]嗯——恩希欧迪斯既然过去和诺希斯是好友，而他又是一个老谋深算的人，那么他必然一开始就对诺希斯的背叛有所防备。
[name="雅儿"]但他还是遇袭了，并且这件事被闹得很大......
[Character(name="avg_npc_250_1#3$1")]
[name="雅儿"]也就是说，这个让民众开始同情他的局面，有可能是他故意营造的？
[Character(name="avg_npc_250_1#6$1")]
[name="雅儿"]可是，这又有什么影响呢？
[name="雅儿"]现在，圣猎的队伍应当也在返回的路上了。
[name="雅儿"]马上，大典最后的仪式，同时也是圣女大人的戴冠仪式就要举行了。
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]无非是在仪式上找出凶手，让他恩希欧迪斯更有人望一些......仅此而已吧？
[Dialog]
[Character(name="avg_npc_250_1#8$1",focus=-1)]
[Decision(options="事实上，还有一种可能性。", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_250_1#1$1")]
[name="雅儿"]那是什么？
[Dialog]
[Character]
[Decision(options="还只是可能性而已。;马上就会知道了。", values="1;2")]
[Predicate(references="1;2")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="24_g5_guestroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Character(name="avg_npc_258_1#5$1",fadetime=0.7)]
[Delay(time=1)]	
[name="大长老"]......你说，圣女在圣猎中亲自出手射杀了猎物。
[Character]
[name="长老A"]是的。
[Character(name="avg_npc_258_1#5$1")]
[name="大长老"]并且，恩希欧迪斯遇袭的消息，已经在民众之间传开。
[Character]
[name="长老B"]是的。
[name="长老A"]不仅如此，已经有一部分民众要

... (全文64704字符)
```

### level_act14side_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] level_act14side_st04
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="24_g6_square",screenadapt="coverall")]
[Character(name="avg_174_slbell_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.4)]
[Character(name="avg_174_slbell_1#1$1")]
[name="恩雅"]数千年前，耶拉冈德降生在这片土地，将这里命名为谢拉格，并始终守护着这片土地。
[name="恩雅"]千百年来，祂的教诲无时无刻不在影响着谢拉格的人民。
[name="恩雅"]祂将血肉赐予佩尔罗契家，将皮毛赐予布朗陶家，将骨骼赐予希瓦艾什家。
[name="恩雅"]但我们有一个共同的名字——谢拉格人。
[name="恩雅"]对祂的信仰，是谢拉格的根基，也是今时今日，我们能够站在这里，共同自称谢拉格人的理由。
[name="恩雅"]我们心中共同怀揣着对祂的敬仰，携手在这片土地上生存至今。
[Character(name="avg_174_slbell_1#3$1")]
[name="恩雅"]但是，我们如今已经知道，这片大地上并非只有谢拉格一个国家。
[Character(name="avg_174_slbell_1#1$1")]
[name="恩雅"]在这片雪山之外，还有广阔的天地，那里有着和我们长相不同，语言不同，且并不信仰耶拉冈德的人。
[name="恩雅"]在过去，我们在如何与这样的人接触这一点上，产生了巨大的分歧。
[Character(name="avg_174_slbell_1#8$1")]
[name="恩雅"]但这分歧并不是危机，而是祂对我们的考验，同时也是祂对我们的教导。
[name="恩雅"]祂作为谢拉格全体人民信仰的对象，是我们的母亲，是我们的守护神。
[name="恩雅"]因为母亲，绝不会希望看到自己的孩子停滞不前。
[Character(name="avg_174_slbell_1#3$1")]
[name="恩雅"]所以——
[Character(name="avg_174_slbell_1#8$1")]
[name="恩雅"]不要因为贪恋旧的而不去尝试新的，你是祂的子民，你当充满勇气。
[name="恩雅"]不要因为怀恋家乡而不去探寻新的土地，无论你身在何处，祂都与你同在。
[name="恩雅"]不要因为已经拥有财富而不去冒险，你本可以拥有更庞大的财富。
[Character(name="avg_174_slbell_1#1$1")]
[name="恩雅"]因为，祂是包容的，祂所守护的这片土地理当是包容的，祂的子民，更应是包容的。
[name="恩雅"]以祂赐予我的权柄，我在此郑重宣布：
[Character(name="avg_174_slbell_1#11$1")]
[name="恩雅"]蔓珠院将接受外国人士对耶拉冈德的信仰。
[name="恩雅"]并且，蔓珠院鼓励民众以自己的方式追求更美好的生活。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character]
[Delay(time=3)]
为纪念喀兰圣女、神启者、应被称颂者恩雅·希瓦艾什面向全谢拉格人民的极具感染力的演讲。
这一日，被定为谢拉格的国教日。
[Dialog]
[Background(image="24_g10_manorhouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[Image(image="24_i13", fadetime=2, xScale=1.5, yScale=1.5, x=480, y=252)]
[Background]
[Decision(options="（移动棋子）", values="1")]
[PlaySound(key="$d_avg_chess", volume=1, delay=0.5)]
[Predicate(references="1")]
[name="恩希欧迪斯"]......谷地一事，原本只是一手闲棋。
[name="恩希欧迪斯"]我需要一个人引开佩尔罗契家的注意力，让我得以暗中调遣物资和人员。
[name="恩希欧迪斯"]这个人若不是你，也会是别人。
[name="恩希欧迪斯"]原本，事后我打算就此事向你致歉。
[name="恩希欧迪斯"]不过现在看来，我或许更该为轻视了你能产生的影响而道歉。
[PlaySound(key="$d_avg_chess", volume=1, delay=0.5)]
恩希欧迪斯自顾自地说着，移动了一枚棋子。
[Dialog]
[Decision(options="（移动棋子）", values="1")]
[PlaySound(key="$d_avg_chess", volume=1, delay=0.5)]
[Predicate(references="1")]
[image(fadetime=1)]
[delay(time=1)]
[Image(image="24_i13", fadetime=2, xScale=1.5, yScale=1.5, x=-480, y=252)]
[name="恩希欧迪斯"]诺希斯是我的挚友，同时也是合作者。
[name="恩希欧迪斯"]他的想法和我并非完全一致，他有他的想法和做法。
[name="恩希欧迪斯"]但我了解他。
[name="恩希欧迪斯"]只要目的一致，他就不会背叛我，甚至不必在计划中和他交换情报。
[name="恩希欧迪斯"]我可以放心地任由他动用一切资源，选择他认为高效的方式，绊住布朗陶家的力量。
[name="恩希欧迪斯"]破坏铁轨是一着妙手。诺希斯既取得了菈塔托丝的信任，也封锁了他国的间谍与信使进出的道路。
[Dialog]
[Character]
[PlaySound(key="$d_avg_chess", volume=1, delay=0.5)]
恩希欧迪斯看了你一眼，移动了一枚棋子。
[Dialog]
[Decision(options="（移动棋子）", values="1")]
[PlaySound(key="$d_avg_chess", volume=1, delay=0.5)]
[Predicate(references="1")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="24_i13", fadetime=0.5, xScale=1.7, yScale=1.7, x=-80, y=252)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="恩希欧迪斯"]和棋。
仿佛是预示了结局一般，恩希欧迪斯将手脱离棋子，摊开双手。
示意本局已经结束。
[ImageTween(image="24_i13", xScaleFrom=1.7, yScaleFrom=1.7, xFrom=-80, yFrom=252, xTo=-80, yTo=0, duration=20)]
[name="恩希欧迪斯"]看来，最近我的时运确实不太好。
[name="恩希欧迪斯"]连下棋都开始赢不了了。
[Dialog]
[Decision(options="你并没有输。", values="1")]
[Predicate(references="1")]
[name="恩希欧迪斯"]有的时候，和意味着大胜，而有的时候，和则意味着大败。
[Decision(options="对你来说，这样的结果是大胜，还是大败？", values="1")]
[Predicate(references="1")]
[name="恩希欧迪斯"]......对我来说，向来是若未取得大胜，就等同于大败。
[name="恩希欧迪斯"]不过这一次，确实是例外。
[name="恩希欧迪斯"]我的胜利毋庸置疑。
[name="恩希欧迪斯"]但没想到的是，你为我的胜局开拓了另一种可能性。
[Dialog]
[Decision(options="另一种可能性。;我没有能力说服圣女下山。;我只是想避免伤亡。", values="1;2;3")]
[Predicate(references="1")]
[name="恩希欧迪斯"]是的，另一种。
[name="恩希欧迪斯"]我本以为这样的结果不可能实现，但你竟在一无所知的不利境况下看破并影响了局面。
[name="恩希欧迪斯"]即使这没有改变我胜利的事实。
[name="恩希欧迪斯"]也许是太久没有棋逢对手，旗鼓相当的对局确实令我心潮澎湃。
[Predicate(references="2")]
[name="恩希欧迪斯"]圣女——不需要别人为她做出决定。
[name="恩希欧迪斯"]但是，你在合适的时候推了她一把，为她提示了一个方向。
[name="恩希欧迪斯"]并且，你还为她搭建好了舞台。
[name="恩希欧迪斯"]你想告诉我，这一切都是你的无心之举？
[Predicate(references="3")]
[name="恩希欧迪斯"]而你确实达成了这个目的。
[name="恩希欧迪斯"]主动接触阿克托斯和菈塔托丝，为他们进行战前预估，并提供了更优的避免开战的方案。
[name="恩希欧迪斯"]确实很有你的风格，博士。
[name="恩希欧迪斯"]即便是我，也没有预料到，这一次的事情，能以这样和平的方式收场。
[Predicate(references="1;2;3")]
[name="恩希欧迪斯"]想必你已经知道，我为什么如此急于让谢拉格成为一个整体。
[Dialog]
[Character(name="avg_172_svrash_1#1$1",focus=-1)]
[Decision(options="外忧。", values="1")]
[Predicate(references="1")]
[Image(image="24_i13", fadetime=2, xScale=1.7, yScale=1.7, x=400, y=252)]
[ImageTween(image="24_i13", fadetime=0.5, xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1.5, yScaleTo=1.5,duration=20)]
[name="恩希欧迪斯"]不错。
[name="恩希欧迪斯"]我并没有那么痛恨蔓珠院，或是急于将信仰从这片土地上根除。
[name="恩希欧迪斯"]我也没有那么不满阿克托斯的排外，菈塔托丝的踌躇。
[name="恩希欧迪斯"]他们不知道外面正在发生什么，也就不可能与我有相同的看法。
[name="恩希欧迪斯"]如果时间充足，我不介意花上五年十年甚至更长的时间，去改变他们的想法，去用更温和的方法改变谢拉格。
[name="恩希欧迪斯"]但是——
[name="恩希欧迪斯"]谢拉格没有那么多时间。即便或许称不上富饶，也一定会有邻国盯上这片不受天灾侵扰的土地。
[name="恩希欧迪斯"]我必须加快步伐，而如果有谁不能接受，那我就只能剥夺他们反对的权力。
[name="恩希欧迪斯"]仅此而已。
[Dialog]
[Character(name="avg_172_svrash_1#5$1",focus=-1)]
[Decision(options="你不必说服我。;这些与我无关。", values="1;2")]
[Predicate(references="1;2")]
[Predicate(references="1")]
[name="恩希欧迪斯"]只是与我认为值得分享的人分享一些我的想法罢了。
[Predicate(references="2")]
[name="恩希欧迪斯"]你以一个旁观者的身份洞察了这一切，所以我才能放心与你谈论这些。
[Predicate(references="1;2")]
[Image(image="24_i13", fadetime=2, xScale=1.7, yScale=1.7, x=-480, y=-252)]
[ImageTween(image="24_i13", fadetime=0.5, xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1.5, yScaleTo=1.5,duration=20)]
[name="恩希欧迪斯"]据我所知，阿克托斯会宣布对给大长老下毒负责，并辞去家主之位。
[name="恩希欧迪斯"]他之所以这么大方，是因为他决定主动向圣女宣誓，佩尔罗契家的土地将由圣女参与管理。
[name="恩希欧迪斯"]恐怕是想要巩固圣女的地位吧。
[name="恩希欧迪斯"]布朗陶家与希瓦艾什家的从属协约即将签订。
[name="恩希欧迪斯"]我可以对你多透露一些，我并没有吞并布朗陶家的打算，如果菈塔托丝愿意，她的权力不会比过去少多少。
[name="恩希欧迪斯"]不再有渴望停滞的人、坚守不前的人与权衡利弊的人阻挡喀兰贸易和谢拉格的发展。
[name="恩希欧迪斯"]我可以接受这个结果，博士。
[Dialog]
[Decision(options="你与圣女之间，并没

... (全文22180字符)
```

### training_act14side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动14side教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 在这种严寒环境下作战，无论敌我都会在一定程度上受到影响，即便是谢拉格的战士也不例外。

[Tutorial(focusX=-312, focusY=-54, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
在<@tu.kw>冰面</>上的单位，会周期性地受到<@tu.kw>霜冻</>效果，陷入<@tu.kw>寒冷</>状态，攻击速度<@tu.imp>降低</>。

[PopupDialog(dialogHead="$avatar_doberm")] 首先让我们尝试攻击这些敌人——趁着<@tu.kw>降雪</>还没开始。

```

### training_act14side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动14side教学关_b

[PopupDialog(dialogHead="$avatar_doberm")] 在<@tu.kw>降雪</>持续期间内，所有敌人和我方单位都会周期性地陷入<@tu.kw>寒冷</>状态。
[PopupDialog(dialogHead="$avatar_kroos")] 那里好像有人被冻成了硬邦邦的冰块......
[PopupDialog(dialogHead="$avatar_doberm")] 已经处于<@tu.kw>寒冷</>状态的单位再次受到<@tu.kw>霜冻</>效果时，会陷入<@tu.kw>冻结</>状态。
[PopupDialog(dialogHead="$avatar_doberm")] 处于<@tu.kw>冻结</>状态的单位无法行动，并且法术抗性会降低。
[PopupDialog(dialogHead="$avatar_kroos")] 这样啊~小炎熔在哪里哦~快来帮忙~
[PopupDialog(dialogHead="$avatar_lava")] 别那样叫我！哼，看来这些冰块需要烤烤火了。
```

### training_act14side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动14side教学关_c

[PopupDialog(dialogHead="$avatar_doberm")] 该准备好撤离了，看来一波更持久的风雪即将到来。
[PopupDialog(dialogHead="$avatar_doberm")] 最后，让我们复习一些物理知识，或许会在之后的作战中有所帮助。为此我请来了阿消小姐进行战术演示。
[Tutorial(focusX=253, focusY=245, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sqrrel", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
杜宾教官，我猜您打算让我将那只磐蟹推进深坑对吗？但我想哪怕磐蟹重量很轻，在那个距离应该也是办不到的。
[PopupDialog(dialogHead="$avatar_doberm")] 不必担心，请等待磐蟹陷入<@tu.kw>冻结</>状态后再尝试推动。
[PopupDialog(dialogHead="$avatar_doberm")] 被<@tu.kw>冻结</>的敌人在冰面上受到位移效果影响时，移动的距离会<@tu.kw>大幅提升</>，如果地形合适，可以借此一举消灭棘手的敌人。
```

### training_act14side_02_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动14side教学关2_a

[PopupDialog(dialogHead="$avatar_yak")] 这些特殊的敌人十分危险，我绝不会让他们通过这里。
[PopupDialog(dialogHead="$avatar_yak")] 这种天色，似乎要刮起暴雪了。
[PopupDialog(dialogHead="$avatar_yak")] 伴随着暴雪的<@tu.kw>刺骨寒风</>会向特定方向推动敌人，如果能够结合地形或许会有奇效。
[PopupDialog(dialogHead="$avatar_yak")] 嗯？这个风向......或许能够利用这里的陷阱制胜。
```

### training_act14side_02_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动14side教学关2_b

[Tutorial(focusX=43, focusY=-1, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这种冰面是<@tu.kw>转角冰面</>，它可以改变敌人受到位移影响时移动的方向。
[PopupDialog(dialogHead="$avatar_doberm")] 利用好这种地形，将有助于我们对抗强大的敌人。
```


## 统计

- 总字符数：508343
- 对话行数：4151


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
