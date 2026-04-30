# 明日方舟 · 活动剧情 · act4fun（13段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act4fun」完整剧情脚本（13个文件，346行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act4fun
- 脚本文件数：13

### level_act4fun_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
在最初的手忙脚乱过后，她突然觉得自己抓住了直播的诀窍。
她随便寻找的直播素材能在城际网络上变成红极一时的段子，她无意聊起的寻常话题能在观众里激起一波又一波讨论。
就连她完全凭心情推荐的商品，都有几样卖到了供不应求。
她的直播事业一路高歌猛进，U-Official很快成了城际网络上的红人。
没过多久，她甚至被邀请主持了种种社会活动，最终到了连移动城市新地块的动工仪式都要请她主持的地步。
主播U已经知道了自己成功的原因。
因为，自己是，最后的，全能系，美少女。
还有谁能比最后的全能系美少女更适合直播吗？不可能！
直播就是自己的天职，无需规划，无需担忧，只要随便做做就能吸引所有人的目光，只要略下功夫就能火遍全城。
如果自己命运的曲线是一个U形，那么，自己已经走过了低谷，马上就要攀上人生的下一个巅峰。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="31_g4_mini12_village",screenadapt="coverall")]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="主播U"]《城郊探奇》节目暂时就播送到这里，但是不要走开，一会儿还有下半场等着大家哦！我们稍后再见！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]（关闭麦克风）
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]准备好了吗？中场休息才是这场节目的攻坚战！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="r")]
[name="工作人员"]攻、攻坚战？
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]中场休息这二十分钟不是本来要播广告嘛，现在临时改成我和你的访谈。我已经和你们的制作人说好了。
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="r")]
[name="工作人员"]啊？！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]最重要的是，这场访谈不是正常播出的，而是伪装成播出事故的形式——也就是说，以我忘了关麦克风的形式——向全城放送！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="r")]
[name="工作人员"]可是这又有什么意义呢？
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]首先，给我们的节目增添轻松愉快的氛围，拉近观众和我们的距离，让他们觉得“哇，原来大主播也会像我们一样出错啊”！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]其次，在访谈过程中，我不仅会讲我自己的故事，还会替节目承上启下，勾起观众对下半场节目的兴趣！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]最后，也是最重要的一点！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]在哪里跌倒的，我就要在哪里爬起来！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]既然我的人生的U形曲线是从一场直播事故开始滑向谷底的，就一定要用一场直播事故冲上巅峰！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="r")]
[name="工作人员"]虽然我听不懂，但不知为什么，感觉自己也已经心潮澎湃起来了！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]那正好，我们这就开始！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]（打开麦克风）
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="r")]
[name="工作人员"]U老师辛苦了，一会儿还有下半场，您先喝点水。
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]多谢。
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="r")]
[name="工作人员"]正好现在没在录节目，我想问问您，您究竟是如何从一个小主播发展到今天这一步的呢？
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]好问题啊，好问题。
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]我想，这和很多要素都有关系，但最重要的，还是我的天资、美貌，以及深邃的思想。
[dialog]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
......
二人就这样聊了起来。
主播U口若悬河，滔滔不绝，向工作人员夸耀自己的种种过人之处。
而这些本来应该被归类为“自吹自擂”的东西，经主播U的口中讲出，不知为何，反而变得极具感染力。
不光是配合表演的工作人员，连那些发现似乎是出了什么直播事故，等着看主播U笑话的人，也感受到了发自心底的，敬畏与折服。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(fadetime=0)]
[name="工作人员"]不过我还真的挺好奇，U老师去过那么多地方，眼界又这么高，抛开节目不谈，您觉得我们这儿的风景究竟怎么样？
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]你真想听？
[dialog]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=2)]
[charslot(fadetime=0)]
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="r")]
[name="工作人员"]真是的，正和U老师聊到有趣的地方，怎么老是有人来电话啊，打了十四五通了，真烦人......
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]没关系的，你先接电话也可以，不碍事，我去给我们俩泡点茶喝。
[charslot(fadetime=0)]
[name="工作人员"]好的。唉，到底是哪个不长眼的......
[charslot(fadetime=0)]
[name="工作人员"]喂？您好？
[charslot(fadetime=0)]
[name="工作人员"]中场休息已经播了一个半小时了？！
[name="工作人员"]主播的状态感觉已经收不住了？
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]你脸色不太好啊。给，喝茶。
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="r")]
[name="工作人员"]（嘴唇蠕动）
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]顺带一提，刚刚你那个问题我在泡茶的时候想了想，说实话，我的评价是......
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="r")]
[name="工作人员"]（制止的目光）
[dialog]
[ShowItem(image="item_36_eu7", fadetime=0.5 )]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]要我说啊，你们这里虽然号称旅游胜地风景怡人，但是看来看去也就是些人造的小土坡。
[name="主播U"]说气候吧，气候也不舒服，天气潮潮黏黏，你们这里是有什么湿气天灾吗？
[name="主播U"]吃的喝的也不咋样，油炸油炸油炸，烂煮烂煮烂煮，连一点可选的清淡健康食物都没有。
[name="主播U"]对，也没啥可娱乐的，我看到过的这里最大的活动也就是一个路边超市的促销活动。
[name="主播U"]怎么说呢，总结一下的话。
[name="主播U"]不如多索雷斯。
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[hideitem]
[Dialog]
即使是暴跳如雷的制作人也不能给尤里卡带来一点半点压力。
临时停播公告，违约金，贷款，利息，贷款，利息，贷款。
这都是些啥？尤里卡一点都不在意。
毕竟，直言不讳的尤里卡已经彻底出名了。
可惜的是，任何平台都不敢再相信尤里卡愿意老老实实做直播，没人知道她还会说出些什么来。
[Dialog]
[Delay(time=1)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]好啦，今天就播到这里了。大家在公屏上打出我们的口号！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]我们的评价是——
[charslot(fadetime=0)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="成千上万条弹幕"]不！如！多！索！雷！斯！！！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
这样就好了。
关掉自己的私人渠道小型直播之后，尤里卡这样想着。
一切都很完美。
直播果然就是自己的天职。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(fadetime=2,block=true)]
[Image]
```

### level_act4fun_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
每天一觉醒来，一切都是新的，这当然也包括形形色色的弹幕，和弹幕在她的心中留下的伤痕。
主播U一直都很紧张，紧张于观众们提出的任何一条负面反馈。
说实话，并没有那么多人对主播U抱着恶意。
她天资不差，时而展现出专业的一面，又那么努力，除了同行，有多少人会讨厌这样一个女生呢？
然而，主播U总能在一百条弹幕中精准捕捉到唯一一行对自己冷嘲热讽的字，然后陷入无尽的恐慌、失落与自我怀疑之中。
平台的人和她聊了几次，虽然公事公办，但也是为了双方共同的利益着想，希望她能“更放开一点”，她却把这当成了警告。
她迫于不存在的压力“放开”地播了几次，每次的节目效果都惨不忍睹，粉丝不增反降——
虽然每次只有几十个人取关，但主播U心中的压力终于达到了临界点。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
这次，她在直播中说不出话了。
她只是一脸死相地盯着镜头，足足盯了半个小时。
然后，她说：
[charslot(slot="m",name="avg_4091_ulika_1#5$1",focus="m")]
[name="主播U"]尤里卡！尤里卡！！
[charslot(slot="m",name="avg_4091_ulika_1#5$1",focus="m")]
[name="主播U"]我悟了！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
无视弹幕里的关心、质疑和嘲讽，主播U下了播。
第二天，当她上播时......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[ShowItem(image="item_36_eu6", fadetime=0.5 )]
[name="主播U"]新观众早日了悟，老观众慈悲为怀。
[name="主播U"]大家好，我是谁不重要，我的直播也不重要，不过是不得不为罢了。
[name="主播U"]接下来我为大家诵经，然后是冥想时间。无缘人右上红叉，有缘人随喜赞叹。请我的助手帮我翻到经书的指定位置。
[charslot(fadetime=0)]
[name="可疑的东国人"]小僧来也！
[charslot(fadetime=0)]
[name="可疑的东国人"]这是小僧几日前亲手雕刻的木鱼，请施主敲响！
[name="主播U"]......不生不灭，不垢不净，不吃不喝——
[charslot(fadetime=0)]
[name="可疑的东国人"]施主念错了，是“不增不减”。
[name="主播U"]啊，不增不减......
[charslot(fadetime=0)]
[name="可疑的东国人"]施主口诵吃喝，想必是肚子饿了。但时辰未到，忍耐也是修行的一环。
[charslot(fadetime=0)]
[name="可疑的东国人"]请施主稍安勿躁，小僧正好用墙边这根拖把为施主作一刀舞，期盼能斩却施主心中妄念。
[charslot(fadetime=0)]
[name="可疑的东国人"]斩却烦恼！
[name="主播U"]无智亦无得......
[charslot(fadetime=0)]
[name="可疑的东国人"]六根清净！
[name="主播U"]以无所得故......
[charslot(fadetime=0)]
[name="可疑的东国人"]纳豆拌饭！
[name="主播U"]（肚子咕咕声）
[charslot(fadetime=0)]
[name="可疑的东国人"]油炸豆腐！
[name="主播U"]（吞口水）
......
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[hideitem]
老观众们把这当成某种奇妙的行为艺术，可几天直播下来，他们发现主播U好像是认真的。
老观众纷纷取关，来找乐子的观众大批涌入。
可主播U不是诵经就是冥想，再不就是跟那个东国人一起在出租屋里做些完全没意义的挑水劈柴，弹幕是一眼也不看。
连乐子人也散去之后，反而真的有一帮跟主播U一起诵经和冥想的观众渐渐聚集起来。
平台把这当成拯救过气主播的契机，可当他们找到主播U的出租屋的时候，里面已经没人了。
再也没人见过主播U，或者说，尤里卡的身影。
她留给这座城市的礼物，是一张写着“本来无一物”的纸条，一大笔坏账，还有一段传说。
至于那间出租屋被打造成让人明心见性的旅游胜地的事，就不是我们的尤里卡能预见的了。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(fadetime=2,block=true)]
[Image]
```

### level_act4fun_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
她努力直播，延长直播时间，增加直播频率，但收入总是寥寥无几。
仿佛大多数的观众都是匆匆看一眼就走，留下的人数量稀少，更别提打赏的了。
也许是自己努力的方向错了，她想。
于是她试图拓宽直播路线，可几天一换的直播主题也并不太受认可。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]今天我们来看经典电影《魂断拉特兰》！据说讲的是一位作家和萨科塔少年的故事！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]这洁白庄严的建筑风格......一定是在拉特兰实景拍摄的吧！
[charslot(slot="m",name="avg_4091_ulika_1#7$1",focus="m")]
[name="主播U"]导演对作家和少年之间关系的微妙——微妙什么来着，忘了，我看看——不！不是看看！我绝对没在念稿！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]大家好呀，今天我们来播怀旧游戏——
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]“昨天你半路下播了，电影后半截呢”？
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]嗨，别在意，电影总能有时间看，今天是游戏之夜！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]大家好！今天是主播U的歌曲纯享时间！
[name="主播U"]第一首，来挑战一下难度极高的《林贡斯恋曲》——
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]“游戏打了一半怎么不打了？存档丢了？”
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]没关系，太阳每天都是新的，主播U每天带给大家的惊喜也都是新的！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]今天来做吃播！主播以前也去过好多地方，见过无数美食，这次带大家品尝的是这款全新上市的雨林蘑菇味麻辣咸香沙虫腿！
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]“还唱不唱歌了”......感觉也已经唱了一段时间，大家的反响——呃，没什么。
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]不提那些，来，观众先吃！好了吗？我这就来尝一尝——
[charslot(slot="m",name="avg_4091_ulika_1#4$1",focus="m")]
[name="主播U"]（咀嚼）
[charslot(slot="m",name="avg_4091_ulika_1#11$1",focus="m")]
[name="主播U"]（艰难地吞咽）
[charslot(slot="m",name="avg_4091_ulika_1#7$1",focus="m")]
[name="主播U"]等等，谁发的“干啥啥不行，吃饭第一名”？！
[charslot(slot="m",name="avg_4091_ulika_1#9$1",focus="m")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=15, randomness=90, fadeout=true, block=false)]
[name="主播U"]我生气了！我真的生、生、生——
[charslot(slot="m",name="avg_4091_ulika_1#11$1",focus="m")]
[name="主播U"]（捂嘴）
[name="主播U"]主播、主播先离开一会儿！马上就回来！！不，不，今天就先到这里了！
[dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(duration=0)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#4$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]唉，昨天吐了好久，现在胃还难受......
[charslot(slot="m",name="avg_4091_ulika_1#11$1",focus="m")]
[name="主播U"]换了这么多直播形式，为什么观众反而越来越少了呢？难道是对我本人有意见？
[name="主播U"]肯定是他们的问题，他们根本不会欣赏主播U！
[charslot(slot="m",name="avg_4091_ulika_1#10$1",focus="m")]
[name="主播U"]不过，还是让我研究研究......他们平时是在哪里议论的？
[name="主播U"]应该是这个论坛没错吧。
[dialog]
[playsound(key="$keyboard")]
[delay(time=1)]
[name="主播U"]注册新用户......用户名......ERK......
[Dialog]
[Delay(time=1)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
意识到了普通的努力无法为自己带来帮助后，主播U加入了粉丝的论坛。
在这里她默默地进行着各种学习，希望可以让自己得到提高。
有功夫不负有心人，她确实产生了蜕变，成功成为了横行各个论坛区块的辩论大师。
[Dialog]
[Delay(time=1)]
[playMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="主播U"] 我？我最讨厌那些网上的喷子了好吧，我从不跟别人争执，我只说事实真相的。
[name="主播U"] 直播当然不应该固定风格！这是主播擅长内容单一的体现！
[name="主播U"] 我直播想换就换，你们爱爱看不爱看可以自行永别。
[name="主播U"] 不不不，你们喜欢看这些无趣的直播节目才是有问题。
[name="主播U"] 什么专精，什么主打，只不过是小主播们能力不全面的藉口罢了。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="主播U"]我看了这部电影的前10分钟，实在是太难看了根本没什么能让我看下去的地方。
[name="主播U"]为什么要给这种导演发工资的，完全就是浪费钱！
[name="主播U"]有什么好在意的，难道看了前10分钟我不喜欢还不能说它吗？
[name="主播U"]真的要是好电影的话，凭什么一开局不能吸引到我？主播我阅片无数，根本不用像你们一样还得看完全片。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="主播U"]主播U我啊，一直以来都勤俭节约的，都是靠自己的努力到现在。实在感谢大家这么长时间支持——
[name="主播U"]什么，你说什么有意见？你懂什么啊，不过就是看我的直播比较早嘛，我不播的时候的努力你知道吗？管好你自己。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="主播U"]说起唱歌，听说隔壁唱片公司去年主推的某唱片获得的各种奖项都是靠花钱造假做数据来的。
[name="主播U"]专辑销量也是靠他们内部自己回购堆起来的。
[name="主播U"]你们不相信，我可是有不少认识的人就在他们公司，这些操作其实都是很正常的。
[name="主播U"]我？你们不懂，我以前从来没有认真投入去演唱过，就是看不起他们这趟混水。
[name="主播U"]这家唱片公司之后必定会调整他们的策略，他们的上层还经常在我的小聊天室里面咨询我的意见呢。
[name="主播U"]肯定跟我说的一模一样，你们走着瞧。这些企业啊，都一个样。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[ShowItem(image="item_36_eu3", fadetime=0.5 )]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
主播U特色直播造成了不小的影响，粉丝更迭快速，因为很多人会被她喷走，又不停地有好奇的人前来。
主播U从中居然还真就得到了不小的收益，平台甚至将其包装成了喷子主播专门为其开启了直播圈专区。
吃到了甜头，主播U自然开始变本加厉。
不出所料，很快她就因为胡乱捏造和诋毁众多个人以及企业的，并且散布各种谣言而收到了法院的传票。
由于传播极广，主播U不得不赔付大量的补偿金，之前进账的收入仅仅是杯水车薪。
看来对她来说，主播这个职业只能到此为止了。
“我，我只是听别的朋友说的，我不知道这个是假的啊，我也就是想跟粉丝们分享分享，我也不是故意的！”
“我道歉还不行吗，对不起我真的不是故意的，应该是那些后来传播的人的错。”
“我真的认识到错误了，实在是非常对不起！”
“......”
“那，那我赔了钱，唱片公司还能考虑考虑我吗？”
[Dialog]
[hideitem]
[stopmusic(fadetime=2)]
[Blocker(fadeti

... (全文6025字符)
```

### level_act4fun_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
她下定决心，和过去冒失而不幸的自己彻底告别。
她苦心孤诣，长袖善舞。
她八面玲珑，左右逢源。
她愿意放弃整晚的睡眠来研究粉丝喜好，也愿意拿出一大半的收入请合同专家为自己保驾护航。
她渐渐收获了相当数量的粉丝，也和平台的对接人员打好了关系，避开了其他主播会遇到的种种陷阱。
终于，她的时代到来了。
在那场梦幻般的直播里，打赏如流水般涌入她的直播间。
密密麻麻的超级留言她甚至念不过来，只能对那些被系统刷下去的人不停道歉，却还是不能阻止粉丝们疯狂的打赏。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]大家今天真的好热情啊，照这个势头，感觉得趁热打铁来个一周连播什么的......
[dialog]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]看看这次收到的分红有多少——
[charslot(slot="m",name="avg_4091_ulika_1#6$1",focus="m")]
[name="主播U"]这、这、这......
[charslot(slot="m",name="avg_4091_ulika_1#7$1",focus="m")]
[name="主播U"]我——我是不是......
[charslot(slot="m",name="avg_4091_ulika_1#7$1",focus="m")]
[name="主播U"]我是不是自由了？
[charslot]
[Dialog]
主播U颤抖着手捡起早已掉在地上的终端。
终端的屏幕上摔了一道裂纹，换成平时，主播U肯定已经心疼得哭出声来。
但此时此刻，看着屏幕上的数字，她张口结舌，一动不动，心中百感交集，傻站了好一会儿。
然后，她朝着天花板高声宣泄心中的喜悦。
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="主播U"]是真的......是真的！
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="主播U"]卡达老师，你看到了吗，你看到了吗？
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="主播U"]我做到了！我用一场直播把贷款连本带利还掉了还能用剩下的钱再买一个五百平米的直播间！
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="主播U"]财富自由万岁！
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="主播U"]耶！！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
狂喜过后，主播U并未放下心来，她怕再有什么飞来横祸，再次把她打回地狱里去。
不过，现实证明她多虑了。
平台很快把她应得的份额打到了她的账上，那些讨债人在得知她一夜暴富之后也无话可说，只能拿钱走人。
粉丝也只增不减，就算打赏的热情没有之前那么猛烈，也足以让她的生活发生翻天覆地的变化。
她其实很克制，只是开始进出稍微好些的餐厅，开始克制地逛奢侈品店，还买下了那间出租屋作为直播工作室。
但她不敢停步。
之前的惨痛经历时刻刺激着她，让她只有在看到银行账户余额稳步增长的时候才有安全感。
但粉丝有增就有减，打赏有多就有少。
就算主播U现在已经成了当地直播界的领军人物。
就算当地报纸争相采访她，就算其他主播疯狂争抢一个和她共同出镜的机会，每次稍微出现一点情况，她心中的警报都会疯狂作响。
她越是心事重重，直播时就越是心不在焉。尽管这给她的直播带来的影响微不足道，她还是觉得自己进入了某种恶性循环。
[charslot]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
这绝对不行，主播U起床后第五次神经质地打开终端看银行存款增量时这么想——
但她突然有了个主意，让线性增长化为指数级增长的主意。
再没有什么比这个主意更适合自己了，她想，名声、和平台的良好关系、大量的闲置资金，都能完美地发挥应有的作用。
[dialog]
[charslot]
[delay(time=1)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]喂？您好，是XX直播平台吗？
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]对的，我是主播U，我打这个电话是想跟你们商量一件事情......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
计划顺利推进，几乎没有遇到任何阻力。
直到那个命运之日的前夜，盘算着一片光明的未来，主播U终于稍微放下心来。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="很像主播U的声音"]哈喽哈喽！
[name="比较像主播U的声音"]新观众初次见面！
[name="有点像主播U的声音"]欢迎来到本次的特别节目——
[name="和主播U一模一样的声音"]主播U的分身大盘点！
[dialog]
[ShowItem(image="item_36_eu2", fadetime=0.5 )]
[name="四个声音"]我们是——U's！
[name="主播U"]这三位是小V、小X和小Y！
[name="主播U"]锵锵！这位是小V，她是我的分身一号，唱功超强，跳舞也不在话下！
[name="主播V"]U姐姐，你这么夸我，我会不好意思的啦！
[name="主播V"]主播V，用唱跳给大家带来笑容！用手比一个V，笑容就会来到脸上哦！
[name="主播U"]这位是小X，我的分身二号，最喜欢的是看电影！无论是名作还是烂片都来者不拒！
[name="主播X"]请不要用喜好开玩笑，我对电影是认真的。
[name="主播X"]速览我看过的782部电影，逐一检索计算......我最爱的情节，就是和小U、小V、小Y吵吵闹闹地生活在一起。计算完成。
[name="主播U"]小Y，我的分身三号！最喜欢打游戏，但是操作水平不怎么样，那些下饭操作都是她的功劳！
[name="主播Y"]U姐姐，你又欺负我了，真是的！以后不理你了！
[name="主播Y"]（小声）但是，但是......人家还是最喜欢U姐姐了......
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[hideitem]
这场史无前例的直播被无数粉丝铭记，他们亲切地将其称为——
直播史上最烂的烂活，没有之一。
同时，平台方面也记录到了堪比天灾过境般疯狂的取关狂潮。
但主播U已经不能收手了。
所有的资源都已经投入这个企划，继续做下去或许还有翻盘的希望，此时退出就等于一切从头开始。
终于，直播出现了回暖的迹象。
可U's粉丝的格局似乎出现了一些改变，平台和主播U的交流出现了莫名其妙的阻力，其余三位主播看她的眼神也越来越异样......
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[name="工作人员"]主播U，我们是来谈条件的......
[name="主播V"]U姐姐，这也是为了U's整个企划的前途......
[name="粉丝代表"]这是论坛里的观众反馈，你可以自己看看我们的评价......
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
“毕业”之后，主播U连“主播U”这个名字都无法继续使用，直播事业一蹶不振。她又欠下了一些贷款，不多，但还不上。
而U's的规模急剧扩张，从三个变成五个，变成十个，变成二十六个......
最终宣布解散。
U's正式解散的那天，我们的尤里卡搬了个小板凳，坐在直播间外面，决定数一数U's最后到底有多少人。
[name="尤里卡"]一百零一，一百零二，一百零三......
[name="尤里卡"]最后是......一百零八个。
[name="尤里卡"]啊。
尤里卡习惯性地掏出终端。
[name="尤里卡"]不算欠款，和我的余额一样多呢。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(fadetime=2,block=true)]
[Image]
```

### level_act4fun_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
她对未来的前景规划非常详细，她已经准备好一步一步将其付诸实施。
她所求的不多，不过是在卡达归来，或是从罗德岛发来消息之前维持住直播间的热度，让贷款不至于越滚越大就好了。
既然卡达已经承认自己有在直播界站稳脚跟的实力，那就算不太努力，也一定是行得通的，对吧。
带着这样的念头，她开始了直播，播得很随性、很自由、很洒脱。
游戏嫌烦不想打了就直接换，歌唱着累不想唱了就直接切，天聊着腻了不想接话就直接下播。
确实有人喜欢这种风格，但更多的人看直播，不是为了看一个人有多任性、多善变、多不负责的。
在移动城市一个小小的角落，主播U的第一个黑粉悄悄诞生。
然后，主播U的黑粉就以指数级的增长速度暴增，很快攻占了直播间。
一开始，面对铺天盖地的恶意弹幕，主播U并未退缩。
就在她觉得黑粉也不过如此的时候，现实给了她无情的打击。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#7$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]“主播你有一份快递到了”？
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]弹幕在搞什么啊，故弄玄虚——
[Dialog]
[charslot]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[name="快递员"]您好——您有一份快件到了——请出来签收一下——
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
那是一封信，主播U拆开之后，看到上面用各种出版物上剪下来的字拼贴出了主播U的私人信息。
结合那条弹幕，信的意义不言自明。
“我们知道你是谁了。”
在那之后，她收到的东西越来越离谱。
但主播U决不后退一步，她就是要和黑粉正面对决，就是要在不卑躬屈膝的同时把直播做下去。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]统计一下统计一下，主播昨天收到的热心粉丝寄来的快递数量是——三件！来给大家展示一下！
[charslot(slot="m",name="avg_4091_ulika_1#6$1",focus="m")]
[name="主播U"]第一件，恐吓信！
[charslot(slot="m",name="avg_4091_ulika_1#11$1",focus="m")]
[name="主播U"]主播U，你如果......还播，看不大清楚......
[name="主播U"]......我们一定会，找到，你的......找到我的什么呀！根本看不懂！
[charslot(slot="m",name="avg_4091_ulika_1#4$1",focus="m")]
[name="主播U"]这个字也太丑了，主播的建议是好好练练字呢！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]第二件，热心粉丝给我下单的，特上生鳞套餐十人份外卖，货到付款——可惜没送到主播手里呢。
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]我说你们能不能换换思路啊，常来我这儿的外送员都知道你们总捣鬼了。
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]第三件——锵锵，一盒源石虫！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
......
黑粉们的过激举动反而给主播U又添加了坚强悲情的人设，甚至让主播U收到的打赏慢慢增加，这让他们抓耳挠腮，寝食难安。
终于，他们开始亲自到主播U的出租屋门外，涂鸦，倒垃圾，泼脏水......
甚至还用口香糖堵锁眼。
在这样的攻势之下，主播U终于显出了颓势。
她上镜时，头发渐渐开始毛糙，脸上有时会挂着大大的黑眼圈，偶尔还脏兮兮的。
她直播给黑粉快递开箱的环节也进行不下去了。
看主播拆源石虫快递盒的包装还挺有趣的，但无论是谁看直播，都不会想看主播展示自家门上的污言秽语。
黑粉们欢欣鼓舞。他们知道，主播U的末日已经一天比一天近了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]接下来是主播U的泰拉环游——
[Dialog]
[charslot]
[dialog]
[stopmusic(fadetime=1)]
[PlaySound(key="$bodyfalldown1", volume=0.4, delay=0.4)]
[delay(time=2)]
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]哼哼......
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]哈哈哈哈哈哈！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[playMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.6)]
[name="主播U"]我花了好几个晚上在二楼设置的机关，终于逮住来搞事情的黑粉了！
[Dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=1)]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[name="主播U"]就是你用口香糖堵我家门锁的是吧！
[charslot]
[name="陌生人"]不，你认错了——
[name="主播U"]还敢嘴硬？
[name="主播U"]给我到房间里来，让大家看看你到底是如何被我教训的！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[ShowItem(image="item_36_eu5", fadetime=0.5 )]
[name="主播U"]这一拳！是为了口香糖！
[dialog]
[PlaySound(key="$punch_n1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[delay(time=0.51)]
[name="主播U"]这一拳！是为了源石虫！
[dialog]
[PlaySound(key="$punch_n1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[delay(time=0.51)]
[name="主播U"]这一铁锅！是为了！特上生鳞套餐！
[dialog]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[delay(time=0.51)]
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]你知道我婉拒外送员的时候心有多痛吗！那可是特上！生鳞！套餐！我从来都没吃过！
[name="主播U"]你知道，你知道......
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]你知道外送员想要递给我的时候......
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="主播U"]它们看上去有多好吃吗！！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[hideitem]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#6$1",focus="m")]
[name="主播U"]等等，这是——饭盒？
[name="主播U"]都洒了一地，这是......生鳞？
[charslot]
[name="奄奄一息的陌生人"]因为小U被那群黑粉搞得太可怜了......我就想着......既然黑粉擅自下单一些有的没的，我就偏偏要让小U吃到他们觉得你吃不起的东西......
[name="奄奄一息的陌生人"]毕竟，小U，我可是你的......
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="奄奄一息的陌生人"]榜一啊！！
[charslot(slot="m",name="avg_4091_ulika2_1#6$1",focus="m")]
[name="主播U"]什，什么！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
主播U看着伤心欲绝夺门逃走的榜一，好半天都没说出一句话。
最后失魂落魄地回到终端前。
她用颤抖的手拿起水杯，刚放到嘴边，就看到了屏幕上弹出的温馨提示：
因您在直播过程中播出违规内容（分类：暴力），且不遵循管理员劝阻，您的直播间已

... (全文6108字符)
```

### level_act4fun_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
她的身上仿佛有种奇异的魔力，能让进入她直播间的粉丝流连忘返。
她的直播间是整个城际网络——不，也许放眼整个泰拉也是如此——最和谐的直播间。
囊中羞涩者喝彩，一掷千金者打钱，口不择言者谨言慎行，心怀不轨者无处遁形。
她下播之后，粉丝还要四处寻找她的直播切片，反复观摩，细细回味。
虽然从粉丝那里收到的打赏金额和大主播没得比，但主播U能从一笔笔款项中感受到大家对自己的爱。
就算这些钱用来还贷款还要好几年，但自己已经是这片大地上最幸福的主播了。
是爱，而不是钱，支持着她度过了每一个负债累累的日子，她想。
这样的日子似乎会永远持续下去......
在某一个普通的一天里，主播U普通地患上了轻度感冒，应各方的要求，不得已休息停播一周。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]咳......没错，主播也很舍不得大家......
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]但离别，是为了再一次相聚！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]一周之后，主播康复了回到这里的那一天，一定会把更多的爱，把更多的幸福和快乐带给大家！
[charslot(slot="m",name="avg_4091_ulika_1#2$1",focus="m")]
[name="主播U"]这是我们的，咳，约定！
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]不，大家不要再打钱了！心意我已经感受到了，只要有大家的心意——咳、咳，我很快就会好起来的！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
这一周是何其漫长啊。
主播U在床上叼着体温计，心里是满满的思念与焦灼。
哪怕再早一天，只要早一天好起来，就能早一天见到粉丝......
但无情的感冒还是持续了整整一个礼拜。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika_1#3$1",focus="m")]
[name="主播U"]新观众初次见面，老观众七天不见！大家好，主播终于康复啦！
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]能见到大家，主播真是太高......兴......
[charslot(slot="m",name="avg_4091_ulika_1#9$1",focus="m")]
[name="主播U"]......欸？
[dialog]
[charslot]
直播间里，观者寥寥，粉丝的数量已经大不如前。
爱......是这样容易消散的东西吗？
主播U不明白。
这时，一位粉丝在弹幕里给出了一个链接，并告诉主播U，这里就是她的爱的去处。
心急如焚的主播U立刻点了下去，然后看到了让自己一生难忘的画面。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="？？？"]新观众初次见面，老观众一天不见！
[name="？？？"]大家好，我是新人主播，U-Gigamax！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Showitem(image="item_36_eu4", fadetime=0.5)]
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]Gigamax？
[name="U-Gigamax"]欢迎新观众进入我的直播间！喔，这不是U-Official妈妈吗？妈妈，你好！
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]妈妈？？
[name="U-Gigamax"]我是基于雷神思考者-Psi型高智能交互平台开发的7*24小时直播特化型人工智能。
[name="U-Gigamax"]调试和虚拟形象设计工作都由妈妈的忠实粉丝，网名Anonymous的爸爸完成！
[charslot(slot="m",name="avg_4091_ulika_1#1$1",focus="m")]
[name="主播U"]爸爸？！
[name="U-Gigamax"]为了缓解见不到U-Official妈妈的痛苦，Anonymous爸爸参考妈妈的外形和语言习惯，独立完成了我的开发工作！
[name="U-Gigamax"]妈妈在一星期前停播，我则是在五天前正式上线的！
[name="U-Gigamax"]妈妈的粉丝给了我很大的鼓励和支持，我的粉丝数已经达到了妈妈的四分之三呢！
[name="U-Gigamax"]妈妈，请你以后也一定要爱我哦！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[hideitem]
令人感动的母女相逢场面在城际网络引发了轰动。
而在平台的催促和粉丝的怂恿下，主播U甚至还和U-Gigamax联机打了一场游戏对战，被人工智能狠狠地教训了一顿。
粉丝们以为这样母慈女孝的场面能像他们对主播U的爱一样永远持续下去，但他们想错了。
一个曾经得到了爱，却又失去了爱的人究竟会有多疯狂，他们永远都想象不到。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m")]
[name="主播U"]（整理设备）
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="主播U"]（对镜头摆姿势）
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m")]
[name="主播U"]身上贴了这么多贴片，真不适应啊......
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m")]
[name="主播U"]但这一切都是值得的！没有什么是不值得的！
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="主播U"]我现在可以开播了吗？
[dialog]
[charslot]
[name="工作人员"]好了好了，可以开始了！
[name="主播U"]呀嚯！新观众初次见面，老观众——同样初次见面！
[name="主播U"]我是你们的——主播U-G-Official！
[name="主播U"]别看我的外表还是Gigamax，我的心可不是什么只会复读别人说话的AI......
[name="主播U"]我是主播U，是主播U本人啊！
[name="主播U"]（哽咽）
[name="主播U"]从今往后，就让我继续为大家带来满~满的爱和幸福，大家也一定要给我最最热烈的爱，这是我们的......约定！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
为了向那位擅自让AI管自己叫爸爸，管主播U叫妈妈的Anonymous发起绝地反击，更为了夺回属于自己的爱。
主播U拼上了一切——生活水平、人脉、存款、违约金，甚至尊严......只为了让U-Gigamax彻底在城际网络上消失。
平台直白地告诉她，这不可能，于是，她退而求其次——
她要宣誓爱的主权，她要侵占U-Gigamax的灵魂。
她不允许任何一个看到这个虚拟形象的人想起略带机械感的AI语音，他们的脑海里必须回荡起自己的声音！
可惜，她还是输了。
主播U的传说，从此彻底成为了U-Gigamax的传奇故事背景。
不过，至少主播U依靠着法律手段，拿到了一笔肖像授权补偿。
当然，这笔钱并不够还完欠款。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(fadetime=2,block=true)]
[Image]
```

### level_act4fun_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[stopmusic]
[Dialog]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.8)]
[Delay(time=3)]
在某年某月某地某城，有一位主播，她的名字是U-Official，通称主播U。
她很普通。
就像她当时向卡达保证的那样，她确实没有误入歧途，但她同样也错过了那些能让她在城际网络成为焦点的机会。
她就这样普普通通地在出租屋里，起床，吃饭，上播，下播，睡觉。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m",duration=1)]
[delay(time=1)]
[name="主播U"]明天就是开播一百天......可我总感觉我这个主播做不长久。
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]要是卡达老师再因为什么事情耽搁了，或者罗德岛根本不要我，那可怎么办啊！
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]在家里待了这么久，该出去走走了吧......
[name="主播U"]我总有一种预感，有这么一位前辈，他一定可以给到我答案。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
主播U晃晃悠悠地出了门，连该去哪里都不知道。任凭双腿自行将她带上了一条从未有人走过的旅途。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
她仿佛走过大街，仿佛走过小巷。
仿佛走过高山，仿佛走过大河。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
仿佛从极北冰原一路走到焚风热土。
仿佛一路走上天空，走入星辰。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="28_g3_slumstreets_night",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
又仿佛一直在暗巷里打转。
她也不知道自己要找的人究竟在哪里，也不知道那个人是谁，不过反正，最后的最后，她找到了。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#6$1",focus="m")]
[name="主播U"]您......您一定就是那位前辈吧！
[charslot]
[name="？？？"]嗯。
[stopmusic(fadetime=4)]
[Dialog]
[Delay(time=1)]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
在那之后的事情，主播U记不太清，只记得自己和那位德高望重的前辈聊了一会儿，具体聊了什么，想不起来。
再加上她刚一回家就收到了卡达寄来的邀请函和录像带，这件事就被她彻底抛到脑后了。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
数个月后
[charslot(slot="m",name="char_016_medic",focus="m")]
[name="Medic"]体检结果已经出来了，尤里卡小姐，您没有感染，身体状况也基本良好。
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="尤里卡"]卡达老师现在在吗？她的宿舍在哪里？
[charslot(slot="m",name="char_016_medic",focus="m")]
[name="Medic"]卡达干员本来是一直等着您的，不过昨天突然来了紧急任务，她出外勤去了。
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m")]
[name="尤里卡"]好吧......
[charslot(slot="m",name="char_016_medic",focus="m")]
[name="Medic"]听卡达干员说，您在来罗德岛之前是城际网络里的主播。做主播一定很开心吧！
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m")]
[name="尤里卡"]做主播——
[dialog]
正在斟酌用词的当口，尤里卡突然想起那天与那位前辈的对话。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="主播U"]您......您一定就是那位前辈吧！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]嗯。
[charslot(slot="m",name="avg_4091_ulika2_1#7$1",focus="m")]
[name="主播U"]前辈，我觉得我快顶不住了！我感觉主播已经做不下去了！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]嗯。
[charslot(slot="m",name="avg_4091_ulika2_1#7$1",focus="m")]
[name="主播U"]卡达也一直不来找我，我要是去不了她说的罗德岛怎么办啊！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]嗯。
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]还有，我心情时好时坏，粉丝对我忽冷忽热，连平台给我的分红也像过山车一样。
[name="主播U"]我有好几次都觉得自己马上要去做什么傻事了！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]嗯。
[charslot(slot="m",name="avg_4091_ulika2_1#7$1",focus="m")]
[name="主播U"]前辈，你倒是说句话呀！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]（清嗓子）
[name="？？？"]关于主播生涯的问题，我的建议是别瞎忙活了，你这个主播做不下去的。不如锻炼锻炼腿脚，以后你还要去当导游呢。
[charslot(slot="m",name="avg_4091_ulika2_1#6$1",focus="m")]
[name="主播U"]导游？？
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]至于第二个问题，你去不去得了罗德岛——
[charslot(slot="m",name="avg_4091_ulika2_1#6$1",focus="m")]
[name="主播U"]等等啊，你还没说我为什么做不下去主播了啊！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]别吵，别吵。
[name="？？？"]——你当然去得了罗德岛啦。
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]为什么？
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]你不去罗德岛，有一大帮人要找我麻烦的。
[charslot(slot="m",name="avg_4091_ulika2_1#9$1",focus="m")]
[name="主播U"]为什么？谁要找前辈麻烦，我跟他们没完！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]呃......那不重要，至少对你来说不重要。
[name="？？？"]然后是第三个问题，关于你为什么觉得有些东西老是变来变去——
[name="？？？"]你觉得自己所经历的一切都是真实的吗？
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]真实？为什么不真实？
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]比如说，我们其实永远都不可能知道，自己是否是某个更高的意志的傀儡。
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]更高的......意志的......傀儡？怎么就不可能知道了？
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]当它能控制你的一举一动，甚至所思所想，它不会允许你思考你是否是自由的。
[name="？？？"]更可怕的是，它甚至可以允许你思考自己是否自由。
[name="？？？"]但它会让你永远也无法得出结论，你只能怀疑这个意志是否存在，却永远不能得知真相！
[charslot(slot="m",name="avg_4091_ulika2_1#5$1",focus="m")]
[name="主播U"]难道......前辈，你就是那个更高的意志？太可恶了！怎么可以这么对我！
[charslot(slot="m",name="avg_npc_9999_1#1$1",focus="m",bstart=0.6,bend=0.9)]
[name="？？？"]为什么你觉得那个意志是我，而不是平台、是粉丝、是你内心的压力，又或是操纵这些东西的人呢？
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="主播U"]呃，我开始听不懂了......
[charslot(slot="m",name="avg_npc_99

... (全文9935字符)
```

### level_act4fun_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot="m",name="avg_328_cammou_1#1$1",focus="m",duration=1)]
[delay(time=1)]
[name="卡达"]给，盒饭。
[dialog]
[charslot]
[charslot(slot="m",name="avg_4091_ulika2_1#7$1",focus="m",duration=1)]
[delay(time=1)]
[name="尤里卡"]卡达老师，我真的不能再白吃你的饭了！
[charslot(slot="m",name="avg_4091_ulika2_1#7$1",focus="m")]
[name="尤里卡"]这间房是你掏钱给我租的，这张床是你上街给我淘的，连这几天的饭都是你请我吃的！
[name="尤里卡"]再这么白吃白喝下去，我真的会无地自容的！
[charslot(slot="m",name="avg_328_cammou_1#2$1",focus="m")]
[name="卡达"]这句话，从我请你吃第一顿饭你就开始说了。
[charslot(slot="m",name="avg_4091_ulika2_1#9$1",focus="m")]
[name="尤里卡"]（目光躲闪）
[charslot(slot="m",name="avg_4091_ulika2_1#7$1",focus="m")]
[name="尤里卡"]（犹豫着伸出手）
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="尤里卡"]（接过盒饭）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m",duration=1)]
[name="尤里卡"]唉，吃饱了，吃饱了。
[charslot(slot="m",name="avg_328_cammou_1#5$1",focus="m")]
[name="卡达"]但你说得对，我确实不能一直这么让你白吃白喝下去。
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="尤里卡"]卡达老师，有什么吩咐你尽管说！
[name="尤里卡"]自从在多索雷斯被人解雇，又在阿卡胡拉被人抢了摄像机，我一路走到现在这座移动城市，从来没人对我这么好！
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="尤里卡"]要是也有人在你屁股后面追债，我一定帮你躲起来，谁都找不到！
[charslot(slot="m",name="avg_328_cammou_1#4$1",focus="m")]
[name="卡达"]你到底想躲多久啊？
[charslot(slot="m",name="avg_4091_ulika2_1#1$1",focus="m")]
[name="尤里卡"]反正我已经努力好久了，可无论如何都还不上钱，能躲多久是多久咯。
[charslot(slot="m",name="avg_328_cammou_1#4$1",focus="m")]
[name="卡达"]你啊......老是逃避解决不了任何问题！
[charslot(slot="m",name="avg_328_cammou_1#7$1",focus="m")]
[CameraShake(duration=1, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="卡达"]锵锵！你看，这是我给你淘来的终端和配套装备！
[charslot(slot="m",name="avg_328_cammou_1#1$1",focus="m")]
[name="卡达"]还记得之前我跟你提到的网络主播吗？
[name="卡达"]当时你不也觉得挺有兴趣吗？有了这些设备，就能亲自试试了！
[name="卡达"]顺利的话，说不定你也能收获到自己真正的粉丝，赚一大笔钱！
[charslot(slot="m",name="avg_4091_ulika2_1#10$1",focus="m")]
[name="尤里卡"]我、我真的可以吗？
[charslot(slot="m",name="avg_328_cammou_1#1$1",focus="m")]
[name="卡达"]从第一次遇到你的时候我就看出来，你肯定很有主播天赋的！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="尤里卡"]这就是——你离开的理由——我懂——♪
[charslot]
[Dialog]
[PlaySound(key="$livecrowd")]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="尤里卡"]感谢大家的支持！如果喜欢我的表演，请大家有钱的捧个——
[charslot]
[Dialog]
[PlaySound(key="$firestorm", volume=1)] 
[PlaySound(key="$b_char_defboost", volume=0.5, Delay=0.4)]
[PlaySound(key="$firestorm", volume=1)] 
[delay(time=5)]
[charslot(fadetime=0)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="路人"]快看，她背后那栋楼冒烟了！快跑啊！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_328_cammou_1#1$1",focus="m")]
[name="卡达"]当时我就想，这个歌手唱功还不错，有机会也许可以找她合作一下。
[charslot(slot="m",name="avg_328_cammou_1#5$1",focus="m")]
[name="卡达"]后来，我再次遇到你，你正在给卖场做大减价的营销主持。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="28_g2_slumstreets",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="尤里卡"]中奖的号码是——109号！
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="尤里卡"]是哪位幸运顾客获得了我们的现金大奖——哦！原来是这位老奶奶！
[charslot(slot="m",name="avg_4091_ulika2_1#3$1",focus="m")]
[name="尤里卡"]恭喜，恭喜！请您上前来，我们——
[charslot]
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[charslot(fadetime=0)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="路人"]老太太绊倒了！快叫救护车！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="36_ulkroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_328_cammou_1#1$1",focus="m")]
[name="卡达"]我当时觉得，你亲和力也不错，怎么就沦落到主持促销活动了呢？
[charslot(slot="m",name="avg_328_cammou_1#1$1",focus="m")]
[name="卡达"]再后来，我还听说你连主持都不是，被骗到了奇怪的地方做促销了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="30_g1_durinstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4091_ulika2_1#2$1",focus="m")]
[name="尤里卡"]小朋友，给，气球~
[charslot(fadetime=0)]
[name="顽皮的小孩？"]嘿！哈！
[name="顽皮的小孩？"]长眼睛了吗？你才是小朋友！
[charslot(slot="m",name="avg_4091_ulika2_1#6$1",focus="m")]
[name="尤里卡"]别踢，别踢——
[charslot]
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="尤里卡"]哇啊！
[name="顽皮的小孩？"]摔倒了，哈哈哈——
[name="严肃的长胡子小孩？"]你怎么回事？快，给人道歉！
[name="顽皮的小孩？"]是她先说我是小屁孩的！我走了！
[name="尤里卡"]没、没关系......但是能不能先扶我一把，我自己站不起来......
[name="严肃的长胡子小孩？"]没问题——
[name="严肃的长胡子小孩？"]啊，衣领卡在墙缝里了......我试试能不能用点力——
[CameraShake(duration=2, ystrength=

... (全文8420字符)
```

### training_act4fun_01_a

```
[HEADER(is_tutorial=true, is_skippable=false)] 2023愚人节教学关1_a

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.LockFunction(mask="BATTLE_STATUS")]
[Battle.Pause]

[Tutorial(protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
想找直播素材，从自己的见闻入手一定没错。我曾经去过的卡西米尔大骑士领就是一个永远不缺素材的地方。
[PopupDialog(dialogHead="$avatar_ulika")] 大骑士领......听说有很多帅哥，是真的吗？
[Battle.Pause(pause=false)]
[Delay(time=1)]
[Battle.Pause(pause=true)]

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]


[Battle.EnsureMinCost(cost=5)]
[Tutorial(focusX=220, focusY=90, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
帅哥我们过一会儿再说，你先试着将<@tu.kw>自己</>部署到这里，然后拍摄一些包含路人的街景吧。



[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.EnsureMinSp(charId="trap_116_stdurk", sp=5)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=false)]
[InputBlocker(blockInput=true, validX=188, validY=100, validWidth=150, validHeight=150)]

[Tutorial(waitForSignal="char_info", focusX=225, focusY=130, focusWidth=150, focusHeight=150, \
          animStyle="Click", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
点这里准备<@tu.kw>拍照</>。
[InputBlocker(blockInput=false)]
[Battle.EnsureMinSp(charId="trap_116_stdurk", sp=12)]
[Tutorial(waitForSignal="use_skill", focusX=200, focusY=-85, focusWidth=150, focusHeight=150, \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_cammou")] \
技能准备就绪后，可以将范围内的<@tu.kw>路人</>拍摄下来，在之后的直播中作为素材与观众讨论。

[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]

[Battle.Pause(pause=false)]
[Delay(time=2)]
[Battle.Pause(pause=true)]

[PopupDialog(dialogHead="$avatar_cammou")] 你拍到的人是竞技骑士，虽然装甲看起来很拉风，但是太常见了，很难说这样的素材会引发什么样的反应。
[PopupDialog(dialogHead="$avatar_ulika")] 那岂不是要专门挑名人拍？我哪有那样的资源啊......
[PopupDialog(dialogHead="$avatar_cammou")] 别灰心，名人也有上街闲逛的时候嘛。





```

### training_act4fun_01_b

```
[HEADER(is_tutorial=true, is_skippable=false)] 2023愚人节教学关1_b

[InputBlocker(blockInput=true)]
[Battle.Pause(pause=true)]

[Tutorial(protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
你看那位正在看报纸的上班族，一见之下普普通通，不过总觉得他很有故事，也许就是我们需要的“名人”。
[Tutorial(protectTime=0.5, dialogHead="$avatar_ulika", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
我看不出他有没有故事，但我觉得他就是我要拍的帅哥！

```

### training_act4fun_01_c

```
[HEADER(is_tutorial=true, is_skippable=false)] 2023愚人节教学关1_c

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.EnsureMinSp(charId="trap_116_stdurk", sp=5)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=false)]
[InputBlocker(blockInput=true, validX=188, validY=100, validWidth=150, validHeight=150)]

[Tutorial(waitForSignal="char_info", focusX=225, focusY=130, focusWidth=150, focusHeight=150, \
          animStyle="Click", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
那还等什么，点这里——
[InputBlocker(blockInput=false)]

[Tutorial(waitForSignal="use_skill", focusX=200, focusY=-85, focusWidth=150, focusHeight=150, \
          animStyle="Click", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_cammou")] \
开拍！
[Battle.Pause(pause=false)]
[Delay(time=3)]
[Battle.Pause(pause=true)]

[InputBlocker(blockInput=true)]
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]

[PopupDialog(dialogHead="$avatar_cammou")]这张素材就很不错，人物看起来很独特，可以说是<@tu.kw>稀有素材</>了。
[PopupDialog(dialogHead="$avatar_cammou")]除了独特的人物，有的路人之间会发生有趣的互动，把这样的场景拍下来，也会获得<@tu.kw>稀有素材</>。
[PopupDialog(dialogHead="$avatar_cammou")]和一般的素材不同，<@tu.kw>稀有素材</>在直播中引发的反应是可以预测的，这对你维持直播顺利进行来说非常重要。
[Tutorial(focusX=200, focusY=-60, focusWidth=150, focusHeight=150, anchor = "TopLeft", \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
可以在这里查看已经收集到的<@tu.kw>直播素材</>。

[Battle.Pause(pause=false)]













```

### training_act4fun_01_d

```
[HEADER(is_tutorial=true, is_skippable=false)] 2023愚人节教学关1_d

[Battle.Pause(pause=true)]
[InputBlocker(blockInput=true)]
[Tutorial(focusX=-345, focusY=15, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_ulika", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
那位女性看起来气度不凡，该不会就是卡达老师你说的上街闲逛的名人吧？
[Tutorial(protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
是烛骑士薇薇安娜小姐！没想到她居然会出现在这里。
[Tutorial(protectTime=0.5, dialogHead="$avatar_ulika", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
那还等什么呢，我拍——










```

### training_act4fun_01_e

```
[HEADER(is_tutorial=true, is_skippable=false)] 2023愚人节教学关1_e

[Battle.Pause(pause=true)]
[Tutorial(focusX=-345, focusY=15, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
等等！你看，她后面跟着一个鬼鬼祟祟的家伙，也许在干什么见不得人的勾当......至少心情不好是肯定的。
[PopupDialog(dialogHead="$avatar_cammou")]如果拍到了这种心情不好的家伙，这一次拍摄就失败了，千万要注意呀。
[PopupDialog(dialogHead="$avatar_ulika")]卡达老师，我明白了！我会避开心情不好的家伙，多拍帅哥的！
[Tutorial(focusX=80, focusY=-60, focusWidth=150, focusHeight=150, anchor="TopLeft", \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
还有，倒计时结束会进入<@tu.kw>直播环节</>。如果你觉得自己收集够了素材，也可以点这里直接结束素材收集。
[Tutorial(protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
在正式的取材中，最好收集<@tu.kw>8张</>以上的素材再进入直播，否则就算能进入直播，也无法以正常方式下播。
[Tutorial(protectTime=0.5, dialogHead="$avatar_cammou", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
好了，再试着随手拍一拍吧。想取别处的景可以<@tu.kw>再部署</>过去哦！










```


## 统计

- 总字符数：54389
- 对话行数：346


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
