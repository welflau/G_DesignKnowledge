# 明日方舟 · 活动剧情 · act26side（31段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act26side」完整剧情脚本（31个文件，3592行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act26side
- 脚本文件数：31

### level_act26side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="39_g9_monasteryroom",screenadapt="coverall")]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_avg_paper2")]
[Subtitle(text="那时恰好是秋天，我与几名逃离家乡的伊比利亚人同行，行走在荒无人烟的荒野上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="就在我们以为我们将会困死在此处时，面前出现了那座修道院。它就好像是某种奇迹，某种不可能存在于现实中的救赎。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="托雷格罗萨主教阁下接纳了那些无处可去的人。他是一位值得尊敬的老人，是最虔诚的信教者。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在主教阁下的管理下，这座被困于荒野的修道院恍若被从世间割离，成为某种异境。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在这里，本不可能有交集的人们和谐共处，互相依靠。尽管生活清贫，但人们不分彼此，都在为了生活而努力。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot = "m", name = "avg_npc_925_1#6$1",duration=1)]
[Delay(time=1.5)]
[name="蕾缪安"]......
[name="蕾缪安"]这个字迹，果然是......
[dialog]
[charslot(duration=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_avg_paper1")]
[Subtitle(text="当我提出自己的请求时，主教阁下沉默许久后对我说，他不愿拒绝任何需要帮助的人，可我提出的地方太过遥远，他无能为力。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="或许是因为本就不怀太多期望，因此，在被拒绝时我也并不失望。拒绝我的无理请求，主教阁下看起来比我更愧疚难堪。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我为得见这样一处善人的乐园而深感欣慰，可与此同时，我也难以抑制地想到这样的问题：", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这样一处不适应土壤的奇迹，是否真的能长存于这片大地之上？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......或许我在这里停留得是有些久了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我该再度启程，去往拉特兰。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$book_close")]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_925_1#2$1")]
[name="蕾缪安"]“本不可能有交集的人们”“不分彼此”......
[charslot(slot = "m", name = "avg_npc_925_1#6$1")]
[name="蕾缪安"]确实，在最初看到那样的景象时，我也有些怀疑自己的眼睛。
[name="蕾缪安"]如果只是作为我个人来说的话，真希望这样难得的和平能一直一直持续下去。
[dialog]
[charslot(slot = "m", focus = "n")]
[playsound(key="$doorknockquite")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_925_1#1$1")]
[name="蕾缪安"]请进。
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "m", name = "avg_npc_934_1#1$1",duration=1,bstart=0.2,bend=0.7)]
[delay(time=1.5)]
[name="修道院居民"]蕾缪安小姐，你在忙吗？
[name="修道院居民"]之前你提过的那种正在流行的图案，我和其他人尝试着绣了一些在被褥上，你看这样对吗？
[charslot(slot = "m", name = "avg_npc_925_1#1$1")]
[name="蕾缪安"]让我看看......嗯嗯，你们的手艺很好呢，这个就算摆在商店里卖，我也不会感到奇怪的。
[charslot(slot = "m", name = "avg_npc_934_1#1$1",bstart=0.2,bend=0.7)]
[name="修道院居民"]没你夸的这么厉害......
[name="修道院居民"]现在天气凉了，蕾缪安小姐这里的被褥可能不大保暖，大家就凑了点布料送过来。
[charslot(slot = "m", name = "avg_npc_925_1#1$1")]
[name="蕾缪安"]谢谢关心~
[name="蕾缪安"]不过给我的话，你们那里会不会不够用？还是优先分给大家吧。
[charslot(slot = "m", name = "avg_npc_925_1#10$1")]
[name="蕾缪安"]别看我这样，其实我很强壮，不会轻易生病的哦。
[charslot(slot = "m", name = "avg_npc_934_1#1$1",bstart=0.2,bend=0.7)]
[name="修道院居民"]哈哈，我们没关系的，大伙匀一匀多少还是没问题的。
[name="修道院居民"]倒是蕾缪安小姐，看着也不像是很强壮的样子啊，拉特兰也真是的，怎么派蕾缪安小姐出这么远的门？
[charslot(slot = "m", name = "avg_npc_925_1#9$1")]
[name="蕾缪安"]嗯，这个嘛......
[name="蕾缪安"]这个问题，我也很想问一问我的上级呢。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="39_g7_chapel",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_927_1#1$1",duration=1)]
[delay(time=2)]
[name="福尔图娜"]......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot = "l", name = "avg_npc_936_1#1$1")]
[charslot(slot = "r", name = "avg_npc_927_1#1$1")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_927_1#5$1",focus="r")]
[name="福尔图娜"]为什么我们不回去？
[charslot(slot = "l", name = "avg_npc_936_1#1$1",focus="l")]
[name="德尔菲娜"]因为莱蒙德他们不能和我们一起！这个理由还不足够？
[charslot(slot = "l", name = "avg_npc_936_1#6$1",focus="l")]
[name="德尔菲娜"]难道你要抛下他们？我做不到！
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[charslot(slot = "m", name = "avg_npc_927_1#4$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[name="福尔图娜"]（笨蛋菲娜，难道我看起来是这么冷血的人吗？要把从小一起长大的朋友丢下，这我当然也做不到啊。）
[name="福尔图娜"]（可是继续像现在这样僵持下去也不是办法，最近大家脾气都开始变坏了......）
[name="福尔图娜"]（真的就没有什么更好的解决方法了吗？）
[charslot(slot = "m", name = "avg_npc_927_1#5$1")]
[name="福尔图娜"]唉......
[charslot(slot = "m", focus = "n")]
[name="？？？"]怎么了，怎么又唉声叹气？
[charslot]
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[charslot(slot = "m", name = "avg_npc_931_1#11$2",duration=1)]
[delay(time=2)]
[name="莱蒙德"]真稀奇，怎么就你一个人，德尔菲娜竟然没和你在一起？
[dialog]
[charslot]
[PlaySound(key="$rungeneral", volume=0.7)]
[charslot(slot = "r", name = "avg_npc_927_1#8$1",posfrom = "200,0", posto = "0,0",duration = 1)]
[charslot(slot = "l", name = "avg_npc_931_1#11$2",duration =0.3)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_931_1#11$2",focus="r")]
[charslot(slot = "r", name = "avg_npc_927_1#8$1",focus="r")]
[name="福尔图娜"]莱蒙德！
[charslot(slot = "r", name = "avg_npc_927_1#4$1",focus="r")]
[name="福尔图娜"]你这话什么意思，我和菲娜也不是时时刻刻都在一起吧？
[charslot(slot = "l", name = "avg_npc_931_1#9$2",focus="l")]
[name="莱蒙德"]差不多吧，你们不是关系好得就差睡一张床了吗。
[charslot(slot = "r", name = "avg_npc_927_1#7$1",focus="r")]
[name="福尔图娜"]我们有时候是会一起睡......呃，不对，重点不是这个！
[charslot(slot = "r", 

... (全文17900字符)
```

### level_act26side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="39_g10_monasterycorridor_d",screenadapt="coverall")]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "m", name = "avg_npc_927_1#1$1",duration=1)]
[delay(time=2)]
[name="福尔图娜"]（莱蒙德那家伙，神神秘秘的......）
[name="福尔图娜"]（有什么事情不能现在说，还非要等到晚上啊？）
[charslot(slot = "m", name = "avg_npc_927_1#7$1")]
[name="福尔图娜"]（搞不懂，算了，先不管他了。）
[charslot(slot = "m", name = "avg_npc_927_1#5$1")]
[name="福尔图娜"]（今天这么晚才送吃的过去，蕾缪安小姐大概要饿坏了吧......唉，而且还只有这么一点。）
[PlaySound(key="$d_avg_hungry")]
[charslot(slot = "m", name = "avg_npc_927_1#3$1")]
[name="福尔图娜"]（......）
[charslot(slot = "m", name = "avg_npc_927_1#6$1")]
[name="福尔图娜"]（争气一点，我的肚子！别叫了别叫了，不是刚刚吃过东西吗！）
[charslot(slot = "m", name = "avg_npc_927_1#5$1")]
[name="福尔图娜"]（唉......）
[name="福尔图娜"]（真想有一天，能什么都不管地大吃一顿......）
[dialog]
[charslot]
[PlaySound(key="$d_avg_cloakmovement")]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_927_1#6$1")]
[name="福尔图娜"]......！
[name="福尔图娜"]是、是谁？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="福尔图娜"]谁在那边？我已经发现你了......！
[name="福尔图娜"]......
[name="福尔图娜"]到底是谁躲在那边？
[name="福尔图娜"]就算不出声我也知道有人在，我、我看到了！你不是修道院的人！
[dialog]
[PlaySound(key="$bullet_loading",volume=0.8)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="福尔图娜"]快点出来！再、再不出来，我就要喊人......不对，我就要扣下扳机了！
[charslot]
[name="？？？"]好好，我出来。
[name="？？？"]唉，失策了......
[dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "m", name = "avg_4015_spuria_1#1$1",duration=1)]
[delay(time=1.5)]
[name="斯普莉雅"]你眼睛可真尖，是我的光翼不小心露出来了吗？我就说我们萨科塔这人人不同款的光环和光翼真的很容易暴露身形......
[name="斯普莉雅"]真是的，我还以为在这里行动不需要那么谨慎呢。
[charslot(slot = "m", name = "avg_npc_927_1#6$1")]
[name="福尔图娜"]......我之前没见过你，你是谁？
[charslot(slot = "m", name = "avg_4015_spuria_1#1$1")]
[name="斯普莉雅"]你好啊，女士。先把铳放下吧，这可不是好女孩该用来指着同族的东西。
[name="斯普莉雅"]既然你也是萨科塔，那你应该能明白吧，我对你完全没有恶意。
[charslot(slot = "m", name = "avg_4015_spuria_1#10$1")]
[name="斯普莉雅"]我是，呃，这次可以算得上是正义使者？差不多吧，毕竟算是来救人的......
[charslot(slot = "m", name = "avg_npc_927_1#6$1")]
[name="福尔图娜"]......你不愿意说就算了。我现在就喊人来——
[charslot]
[dialog]
[PlaySound(key="$d_avg_clothmovementsp")]
[charslot(slot = "r",name = "avg_npc_927_1#6$1",posfrom = "0,0", posto = "0,0",duration = 0)]
[charslot(slot = "l",name = "avg_4015_spuria_1#1$1",posfrom = "50,0", posto = "200,0",duration = 0.5)]
[delay(time=0.5)]
[charslot(slot ="r", action="shake", power=10, times=50, duration=0.5)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_927_1#6$1",focus="l")]
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]哎哎，你别急啊。
[charslot(slot ="r", action="shake", power=10, times=50, duration=0.5)]
[charslot(slot = "r", name = "avg_npc_927_1#6$1",focus="r")]
[name="福尔图娜"]唔唔唔！
[name="福尔图娜"]（放开我！）
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]没问题，不过你可别真的大叫哦。
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[charslot(slot = "l",posfrom = "200,0", posto = "0,0",duration = 1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_npc_927_1#5$1",focus="r")]
[name="福尔图娜"]呼——哈......
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]抱歉，有点没控制住力道。你还好吗？
[charslot(slot = "r", name = "avg_npc_927_1#6$1",focus="r")]
[name="福尔图娜"]咳......咳咳，你到底是什么人，想干什么？！
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]告诉你也没什么，我是来找人的。
[name="斯普莉雅"]来找一个和我们一样的萨科塔，粉色头发，现在应该还坐着轮椅吧，人看起来特别和善，不过其实性格没那么好的......
[charslot(slot = "r", name = "avg_npc_927_1#3$1",focus="r")]
[name="福尔图娜"]（是蕾缪安小姐？！）
[charslot(slot = "l", name = "avg_4015_spuria_1#7$1",focus="l")]
[name="斯普莉雅"]哦？看你的表情......你们认识？我的运气还是挺不错的嘛。
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]你刚刚端着饭菜，是要给谁送去吗？我随便猜猜，难道是送去给蕾缪安的？
[charslot(slot = "r", name = "avg_npc_927_1#4$1",focus="r")]
[name="福尔图娜"]（嗯？！）
[name="福尔图娜"]（她是怎么知道的？？）
[charslot(slot = "l", name = "avg_4015_spuria_1#7$1",focus="l")]
[name="斯普莉雅"]哈哈，我又猜对啦？你的表情也太明显了！
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]那能不能请你告诉我，这位蕾缪安小姐这段时间过得还好吗？
[charslot(slot = "r", name = "avg_npc_927_1#6$1",focus="r")]
[name="福尔图娜"]......
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]不想说？还是不能说？你在犹豫，还有点害怕......
[charslot(slot = "r", name = "avg_npc_927_1#6$1",focus="r")]
[name="福尔图娜"]你、你别乱说！
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]我是不是乱说，你自己最清楚。
[name="斯普莉雅"]你好像有很多烦恼的样子，真奇怪，我本来以为住在这种与世隔绝的地方，不会有很多烦心事的。
[name="斯普莉雅"]是因为什么？因为这里没有多少同族，所以和其他人起了争执吗？
[charslot(slot = "r", name = "avg_npc_927_1#4$1",focus="r")]
[name="福尔图娜"]......和你没关系。
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]不是吗？那是因为你手里那把守护铳看上去好久没保养，有点生锈了？
[name="斯普莉雅"]如果是因为这个的话，我倒是可以帮你哦，我还挺擅长维修铳的呢。只要你告诉我蕾缪安到底在哪里就行了，是不是很划算？
[name="斯普莉雅"]告诉我吧，你其实也能猜到我是什么身份，对吧？你看起来挺聪明的。
[charslot(slot = "r", name = "avg_npc_927_1#6$1",focus="r")]
[name="福尔图娜"]......
[charslot(slot = "r", name = "avg_npc_927_1#4$1",focus="r")]
[name="福尔图娜"]你和蕾缪安小姐一样，是拉特兰派来的人？
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]答对了。
[charslot(slot = "l", name = "avg_4015_spuria_1#12$1",focus="l")]
[name="斯普莉雅"]好啦，闲聊就到此为止。我还赶时间......
[name="斯普莉雅"]真的不告诉我蕾缪安在哪吗？
[charslot(slot = "r", name = "avg_npc_927_1#4$1",focus="r")]
[name="福尔图娜"]......
[charslot(slot = "l", name = "avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]唔，既然你不愿意说，那就算了。
[name="斯普莉雅"]对了。
[dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "150,0",duration = 0.5)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_glassclink", volume=0.6)]
[delay(time=1)]
[charslot(slot = "l",posfrom = "150,0", posto = "0,0",duration = 0.8)]
[delay(time=1.2)]
[charslot(slot = 

... (全文17439字符)
```

### level_act26side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="39_g2_abandonsancturay",screenadapt="coverall")]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_npc_490_1#1$1",duration=1)]
[Delay(time=2)]
[name="阿尔图罗"]在一个很远很远的地方，有一个小村庄，那里生活着一群幸福的村民。
[name="阿尔图罗"]他们中的一些人为大家建起遮风避雨的小屋，并开垦出农田。
[name="阿尔图罗"]另一些人则外出打猎，寻找矿石，顺便还打跑那些想要将村子占为己有的坏蛋。
[name="阿尔图罗"]这些村民不分你我，谁都离不开谁，他们共同生活在小小的村庄中，都认为这里是自己的家园。
[charslot(slot = "m", name = "avg_npc_490_1#10$1")]
[name="阿尔图罗"]但是好景不长，农田里的作物逐渐减产，打猎也越来越艰难，可以吃的食物越来越少，大家都饿得肚子咕咕叫。
[name="阿尔图罗"]天气也变得越来越冷，可是能用来取暖的燃料却怎么也不够分......
[charslot(slot = "m", name = "avg_npc_490_1#3$1")]
[name="阿尔图罗"]这可怎么办才好呀！大家都说，“这一定是主给予我们的磨练，我们必须祈求宽恕！”
[charslot(slot = "m", name = "avg_npc_490_1#1$1")]
[name="阿尔图罗"]就在这时候，一群好心人来到这里，见到村庄中的情况，就同领头的村民说......
[charslot(slot = "m", name = "avg_npc_490_1#2$1")]
[name="阿尔图罗"]“来吧，你们可以来我们的城市生活。”
[charslot(slot = "m", name = "avg_npc_490_1#1$1")]
[name="阿尔图罗"]“但是，我们只能带走你们之中和我们更相似的那一部分人。”
[name="阿尔图罗"]“来吧，来过更好的生活，只要抛下你们之中的一小部分人就可以了......”
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#1$1",focus="n")]
[charslot(slot = "right", name = "avg_npc_928_1#5$1",focus="r")]
[name="活泼的孩子"]阿尔图罗姐姐，不要讲这个故事！
[charslot]
[charslot(slot = "m", name = "avg_npc_490_1#3$1")]
[name="阿尔图罗"]嗯？你们不喜欢这个故事吗？
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#1$1",focus="n")]
[charslot(slot = "right", name = "avg_npc_928_1#2$1",focus="r")]
[name="活泼的孩子"]不喜欢！饿肚子，会很难受......！
[charslot(slot = "left", name = "avg_npc_929_1#2$1",focus="l")]
[name="害羞的孩子"]嗯，很难受。而且，不可以丢下其他人......
[charslot]
[charslot(slot = "m", name = "avg_npc_490_1#1$1")]
[name="阿尔图罗"]这确实是很“正确”的集体主义观念，或许还带有英雄主义......甚至浪漫主义的色彩。
[name="阿尔图罗"]浪漫的故事自然有其动人之处，只是，浪漫与傲慢有时也会迷惑他人，以及我们自身。
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#7$1",focus="l")]
[charslot(slot = "right", name = "avg_npc_928_1#2$1",focus="l")]
[name="害羞的孩子"]唔，好难，听不懂......
[charslot(slot = "right", name = "avg_npc_928_1#5$1",focus="r")]
[name="活泼的孩子"]阿尔图罗姐姐又说奇怪的话了！
[charslot]
[charslot(slot = "m", name = "avg_npc_490_1#9$1")]
[name="阿尔图罗"]哎呀，对不起，是姐姐不好。
[charslot(slot = "m", name = "avg_npc_490_1#1$1")]
[name="阿尔图罗"]我们换一个故事。你们想听什么？
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#7$1",focus="n")]
[charslot(slot = "right", name = "avg_npc_928_1#1$1",focus="r")]
[name="活泼的孩子"]想听......英雄的故事！
[charslot]
[charslot(slot = "m", name = "avg_npc_490_1#1$1")]
[name="阿尔图罗"]你们想当大英雄吗？
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#8$1")]
[charslot(slot = "right", name = "avg_npc_928_1#3$1")]
[name="害羞的孩子&活泼的孩子"]当大英雄！和妈妈一样！
[charslot]
[charslot(slot = "m", name = "avg_npc_490_1#8$1")]
[name="阿尔图罗"]好厉害，你们的妈妈真了不起！
[dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_941_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot = "m", name = "avg_npc_490_1#7$1")]
[name="阿尔图罗"]......
[charslot(slot = "m", name = "avg_npc_490_1#1$1")]
[name="阿尔图罗"]好孩子们，稍微等我一下。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_490_1#6$1")]
[charslot(slot = "right", name = "avg_npc_941_1#1$1")]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "right", name = "avg_npc_941_1#1$1",focus="r")]
[name="温和的教士"]我好像来得不是时候。打扰到你了吗，阿尔图罗？
[charslot(slot = "left", name = "avg_npc_490_1#6$1",focus="l")]
[name="阿尔图罗"]明知故问，奥卢斯阁下。
[charslot(slot = "right", name = "avg_npc_941_1#2$1",focus="r")]
[name="奥卢斯"]请你原谅。无意惹你不快，我是来向你辞行的。
[name="奥卢斯"]因为多了一位计划外的旅伴，我准备尽快启程，护送我的同胞回到家乡。
[charslot(slot = "left", name = "avg_npc_490_1#7$1",focus="l")]
[name="阿尔图罗"]我会为这位可悲的人稍作祈祷。
[charslot(slot = "right", name = "avg_npc_941_1#2$1",focus="r")]
[name="奥卢斯"]我无意在这里与你争执......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#1$1")]
[charslot(slot = "right", name = "avg_npc_928_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "left", name = "avg_npc_490_1#7$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_941_1#2$1",focus="r")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "left", name = "avg_npc_490_1#7$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_941_1#2$1",focus="r")]
[name="奥卢斯"]......尤其是在这两个孩子面前。
[name="奥卢斯"]不过，任何与生命相关的决心都不应用“可悲”来形容。
[charslot(slot = "left", name = "avg_npc_490_1#6$1",focus="l")]
[name="阿尔图罗"]决心......决心。
[name="阿尔图罗"]我们对自己的控制，往往并没有我们自己想的那样完美无缺，在事情真正发生之前，谁也无法断言。
[name="阿尔图罗"]想着绝不能做的事，有时回过神来，就已经那么去做了。
[charslot(slot = "left", name = "avg_npc_490_1#10$1",focus="l")]
[name="阿尔图罗"]责怪行动偏离内心吗？可又有谁能断言，我们自以为的决心，不是自己用来说服自己的某种谎言？
[charslot(slot = "left", name = "avg_npc_490_1#6$1",focus="l")]
[name="阿尔图罗"]这样的时候，我们最真实的情感与意图究竟藏在何处......
[name="阿尔图罗"]人们的思想、情感、行动，什么时候才会有真正统一的一天？
[name="阿尔图罗"]这不正是你的疑问吗，阁下？
[charslot(slot = "right", name = "avg_npc_941_1#2$1",focus="r")]
[name="奥卢斯"]......
[charslot(slot = "left", name = "avg_npc_490_1#7$1",focus="l")]
[name="阿尔图罗"]今天似乎是会发生很多事情的一天，我听到外面很吵闹，像是有我认识的客人上门。
[charslot(slot = "left", name = "avg_npc_490_1#6$1",focus="l")]
[name="阿尔图罗"]如果我是你，奥卢斯阁下，在如今这样的时刻就不会急着离开。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$calm_loop", volume=0.6)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_490_1#1$1",duration=1)]
[delay(time=1.5)]
[name="阿尔图罗"]久等了。
[charslot]
[charslot(slot = "left", name = "avg_npc_929_1#1$1",focus="n")]
[charslot(slot = "right", name = "avg_npc_928_1#5$1",focus="r")]
[name="活泼的孩子"]姐姐好慢！
[charslot(slot = "left", name = "avg_npc_929_1#2$1",

... (全文30385字符)
```

### level_act26side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="39_g8_outsidepath",screenadapt="coverall")]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "left", name = "avg_npc_924_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_926_1#1$1",duration = 1)]
[Delay(time=2)]
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]......
[name="克莱芒"]杰拉尔德，你是打算和我一起去敲钟吗？
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]很奇怪吗？
[charslot(slot = "left", name = "avg_npc_924_1#8$1",focus="l")]
[name="克莱芒"]奇怪。之前有一回我托你帮忙敲钟，你不乐意，最后还是使唤莱蒙德那小伙子。
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]好像是有这么回事。
[charslot(slot = "left", name = "avg_npc_924_1#10$1",focus="l")]
[name="克莱芒"]我记得你不喜欢钟声。
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]谈不上喜欢不喜欢，都这么多年了。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]这么多年了，你还是没能习惯它。
[charslot(slot = "right", name = "avg_npc_926_1#6$1",focus="r")]
[name="杰拉尔德"]原谅我，钟声没给我留下过什么好的记忆。
[Dialog]
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="all")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[Delay(time=3)]
[PlaySound(key="$d_avg_runstop")]
[Delay(time=1)]
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="r")]
[charslot(slot = "right", name = "avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]......克莱芒，你还记得爱琳吗？
[charslot(slot = "left", name = "avg_npc_924_1#7$1",focus="l")]
[name="克莱芒"]爱琳......
[charslot(slot = "left", name = "avg_npc_924_1#4$1",focus="l")]
[name="克莱芒"]我怎么会忘？当初如果不是你和爱琳救了我，我早就被那群强盗丢进峡谷了。
[charslot(slot = "right", name = "avg_npc_926_1#7$1",focus="r")]
[name="杰拉尔德"]哈哈，是她要救你，我本打算多一事不如少一事。
[charslot(slot = "left", name = "avg_npc_924_1#4$1",focus="l")]
[name="克莱芒"]这话你别当我的面说啊......
[charslot(slot = "right", name = "avg_npc_926_1#7$1",focus="r")]
[name="杰拉尔德"]哈哈，抱歉抱歉。
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]......
[name="杰拉尔德"]昨晚我们在外头扎营，收获不算很多，但处理起来也不轻松。
[name="杰拉尔德"]莱蒙德给他的猎物放血，我把火生起来。看着那点火苗逐渐向上蹿，也不知道怎么了，我忽然想起爱琳。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]杰拉尔德......
[charslot(slot = "right", name = "avg_npc_926_1#6$1",focus="r")]
[name="杰拉尔德"]我其实很久没有想到过她了。但直到我想起，我才意识到......
[charslot(slot = "right", name = "avg_npc_926_1#2$1",focus="r")]
[name="杰拉尔德"]我甚至记不清她的脸。
[charslot(slot = "right", name = "avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]她这个人，在我们这群人中间算是个怪胎。当初她和我说，看见修道院遍地的鲜花，听见这里的钟响，能让她心情平静。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]......现在没有那么多花可以看了。
[charslot(slot = "right", name = "avg_npc_926_1#6$1",focus="r")]
[name="杰拉尔德"]是啊，可惜了。
[name="杰拉尔德"]爱琳是真的喜欢这里的钟声。一直到她走的那天，还坚持等到钟声响起，才合眼。
[charslot(slot = "left", name = "avg_npc_924_1#10$1",focus="l")]
[name="克莱芒"]所以你不喜欢钟声。
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]......或许只是害怕。我怕它再带来坏消息。
[charslot(slot = "left", name = "avg_npc_924_1#7$1",focus="l")]
[name="克莱芒"]如果那时候我们有足够的药，或许她受的伤就不会恶化，也不会就这么......
[charslot(slot = "right", name = "avg_npc_926_1#2$1",focus="r")]
[name="杰拉尔德"]没有如果。
[charslot(slot = "left", name = "avg_npc_924_1#2$1",focus="l")]
[name="克莱芒"]......愿她能获得救赎。
[charslot(slot = "right", name = "avg_npc_926_1#4$1",focus="r")]
[name="杰拉尔德"]是啊，但愿。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]......
[charslot(slot = "left", name = "avg_npc_924_1#10$1",focus="l")]
[name="克莱芒"]杰拉尔德，你们真的决定要走？
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]是真的。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]我没想到会这么急......
[charslot(slot = "right", name = "avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]本来该提前和你说一声，只是一直没找到机会开口。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]莱蒙德和福尔图娜他们恐怕要难受一阵子了，他们几个孩子一向关系好，这次一定很不好受......
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]莱蒙德还太年轻。他来到这儿时还太小，记不住太多事。他还没能理解身为萨卡兹究竟是怎么一回事。
[name="杰拉尔德"]但他总会了解，总要习惯。
[name="杰拉尔德"]或许这就是萨卡兹的宿命。
[charslot(slot = "left", name = "avg_npc_924_1#1$1",focus="l")]
[name="克莱芒"]宿命不是什么好词。
[charslot(slot = "right", name = "avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]啊，你说得有道理，但我找不到别的词来形容。
[charslot(slot = "right", name = "avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]......好了，我该去看看爱琳了。
[name="杰拉尔德"]接下来我们就不是一路了，不如就在这分开吧。
[dialog]
[charslot(slot = "m", focus = "all")]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "r",posfrom = "0,0", posto = "200,0",afrom = 1, ato = 0,duration = 1.5)]
[delay(time=2)]
[charslot(slot = "l",posfrom = "0,0", posto = "200,0",duration = 1)]
[delay(time=1)]
[charslot(slot = "left", name = "avg_npc_924_1#3$1",focus="l")]
[name="克莱芒"]......等等，杰拉尔德！
[name="克莱芒"]我、我可以和你一起走，稍微绕一点路而已，不费什么事！
[name="克莱芒"]对了，你看，最近正好是花期，我们可以一起去摘点花送给爱琳......！
[charslot(slot = "left", name = "avg_npc_924_1#5$1",focus="l")]
[name="克莱芒"]我可以和你们一起......
[charslot]
[charslot(slot="m",name="avg_npc_926_1#1$1")]
[name="杰拉尔德"]不对，克莱芒。你糊涂了。
[charslot(slot="m",name="avg_npc_924_1#5$1")]
[name="克莱芒"]我......！
[charslot(slot="m",name="avg_npc_926_1#1$1")]
[name="杰拉尔德"]你不该从这走。你该走上那边的台阶，往上走，那边的风景会很美。
[charslot(slot="m",name="avg_npc_924_1#10$1")]
[name="克莱芒"]......你们还能看到这么好的风景吗？
[charslot(slot="m",name="avg_npc_926_1#1$1")]
[name="杰拉尔德"]......
[name="杰拉尔德"]去敲钟吧，克莱芒。别耽误了时候。那里才是你要去的方向。
[charslot(slot="m",name="avg_npc_926_1#10$1")]
[name="杰拉尔德"]以后要多保重，兄弟。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_927_1#1$1")]
[charslot(slot = "l", name = "avg_npc_936_1#1$1")]
[Background(image="39_g9_monasteryroom",screenadapt="coverall")]
[playMusic(intro="$drift_intr

... (全文29021字符)
```

### level_act26side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(key="$monastery_sad_loop", volume=0.6)]
这是一种难以形容的感觉。
额头上传来古怪的痒意，头顶的光环不稳定地明灭。
眼前的一切都逐渐开始变得黯淡。
福尔图娜能看到老迈的主教难以置信的双眼，她能听到周围嘈杂的人声。
但当她像之前每一次那样，试图感受面前的老人的想法，对方的心情却无法再流入她的心灵，一丝一毫也不能——
她感受不到其他萨科塔了。
她已不再是他们之中的一员。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[Background(image="39_g7_chapel",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]堕天......？
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]这是什么意思......福尔图娜她会怎么样？她、她是病了吗？
[charslot(slot="m",name="avg_npc_372_1#6$1",focus="m")]
[name="里凯莱"]这个回头再解释，先处理眼下最要紧的问题——
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]斯特凡诺爷爷......！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]救救菲娜！求您了，快、快救救她......！
[charslot(slot="m",name="avg_npc_923_1#3$1",focus="m")]
[name="修道院主教"]孩子，不要慌，好好说......到底是怎么了？
[charslot(slot="m",name="avg_npc_927_1#3$2",focus="m")]
[name="福尔图娜"]菲娜、菲娜流了好多血，我怎么也止不住......我找不到人帮忙......
[charslot(slot="m",name="avg_npc_927_1#3$2",focus="m")]
[name="福尔图娜"]我们只是、只是吵了一架，菲娜要我的守护铳，我该给她的，我为什么不给她？
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]都是我不好......！
[charslot(slot="m",name="avg_npc_923_1#5$1",focus="m")]
[name="修道院主教"]别怕，别怕，孩子，别害怕。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]从现有的情况判断，我认为这是一场不包含主观加害意图的意外伤害事件。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_923_1#6$1",focus="m")]
[name="修道院主教"]住口！执行者！
[charslot(slot="m",name="avg_npc_923_1#6$1",focus="m")]
[name="修道院主教"]你在指控这个孩子......伤害了她的同胞？！
[charslot(slot="m",name="avg_npc_923_1#6$1",focus="m")]
[name="修道院主教"]你竟敢做出这种指控——？！
[charslot(slot="m",name="avg_1032_excu2_1#3$1",focus="m")]
[name="费德里科"]......这是最合理的推测。
[charslot(slot="m",name="avg_1032_excu2_1#3$1",focus="m")]
[name="费德里科"]戒律带来的排斥并非无法克服，无意走火的状况更是时有发生。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_923_1#6$1",focus="m")]
[name="修道院主教"]......一派胡言！
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]不......他说得对......是我，是我扣了扳机！
[charslot(slot="m",name="avg_npc_923_1#5$1",focus="m")]
[name="修道院主教"]福尔图娜！可你......
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]......斯特凡诺爷爷，是我的错，要怎么惩罚我都可以！
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]可是菲娜还在......她受伤了！求您救救菲娜！
[charslot(slot="m",name="avg_npc_923_1#5$1",focus="m")]
[name="修道院主教"]好，好，我现在就去——
[charslot(slot="m",name="avg_4015_spuria_1#8$1",focus="m")]
[name="斯普莉雅"]我去吧。
[charslot(slot="m",name="avg_4015_spuria_1#8$1",focus="m")]
[name="斯普莉雅"]急救我擅长，告诉我在什么地方。
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]就在、就在我的房间......
[charslot(slot="m",name="avg_npc_924_1#6$1",focus="m")]
[name="克莱芒"]我可以带路！
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]拜托你了，克莱芒。
[charslot(slot="m",name="avg_4015_spuria_1#8$1",focus="m")]
[name="斯普莉雅"]少说废话，快点。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Background(image="39_g10_monasterycorridor_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[PlaySound(key="$d_avg_crowdrun",volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_924_1#6$1",focus="m",duration=0.5)]
[delay(time=1)]
[name="克莱芒"]在这边，请跟我来！
[charslot(slot="m",name="avg_npc_924_1#6$1",focus="m")]
[name="克莱芒"]到了，就是这里！
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]门没有关上......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[charslot]
[Background(image="39_g9_monasteryroom",screenadapt="coverall")]
[PlaySound(key="$dooropenquite")] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[delay(time=1)]
[name="克莱芒"]好多血......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]德尔菲娜！
[charslot(slot="m",name="avg_4015_spuria_1#8$1",focus="m")]
[name="斯普莉雅"]小点声！你想让所有人都知道这里出事了吗！
[charslot(slot="m",name="avg_4015_spuria_1#8$1",focus="m")]
[name="斯普莉雅"]让开，让我看看！
[dialog]
[Delay(time=0.5)]
[playsound(key="$d_avg_cloakmovement")]
[characteraction(name="middle", type="move",ypos=-50,isblock=true,fadetime=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4015_spuria_1#6$1",focus="m")]
[name="斯普莉雅"]......不行。伤势太严重，血止不住。
[charslot(slot="m",name="avg_4015_spuria_1#6$1",focus="m")]
[name="斯普莉雅"]而且她的伤......
[Dialog]
[characteraction(name="middle", type="move",ypos=50,isblock=true,fadetime=1)]
[charslot(slot="m",name="avg_4015_spuria_1#6$1",focus="m")]
[name="斯普莉雅"]......
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]现在该怎么办？
[charslot(slot="m",name="avg_npc_924_1#11$1",focus="m")]
[name="克莱芒"]花......对了！我记得主教阁下说过圣堂的花也能当药用！对，对，一定能......
[charslot(slot="m",name="avg_npc_924_1#11$1",focus="m")]
[name="克莱芒"]我这就去摘！
[charslot]
[charslot(slot="l",name="avg_npc_924_1#11$1",focus="r")]
[charslot(slot="r",name="avg_4015_spuria_1#6$1",focus="r")]
[name="斯普莉雅"]别去了。
[charslot(slot="l",name="avg_npc_924_1#6$1",focus="l")]
[name="克莱芒"]别拦着我！立刻、立刻去的话，也许还来得及——
[charslot(slot="r",name="avg_4015_spuria_1#9$1",focus="r")]
[name="斯普莉雅"]去了也没用！就算止住血，也来不及了！
[charslot(slot="l",name="avg_npc_924_1#3$1",focus="l")]
[name="克莱芒"]什么意思？怎么会没用......
[charslot(slot

... (全文22633字符)
```

### level_act26side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="39_g9_monasteryroom",screenadapt="coverall")]
[PlaySound(key="$d_avg_gunsingle", volume=0.9)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_925_1#6$1",focus="m")]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_925_1#9$1",focus="m")]
[name="蕾缪安"]我们一般不会用铳招待客人，特殊情况除外。
[charslot(slot="m",name="avg_npc_925_1#9$1",focus="m")]
[name="蕾缪安"]如果有哪里招待不周，还请谅解一下。
[Dialog]
[charslot(slot="m",name="avg_npc_930_1#1$1",focus="m")]
[playsound(key="$d_avg_fseamonsterroar")]
[delay(time=0.5)]
[name="扭曲的怪物"]（无意义的吼叫）
[charslot(slot="m",name="avg_npc_925_1#7$1",focus="m")]
[name="蕾缪安"]（对我说的话没有任何反应，完全无法沟通吗？）
[charslot(slot="m",name="avg_npc_925_1#8$1",focus="m")]
[name="蕾缪安"]（身体看起来已经不剩多少人类的特征了，覆盖在身上的那些是鳞？）
[charslot(slot="m",name="avg_npc_925_1#8$1",focus="m")]
[name="蕾缪安"]（......这种异变，我记得伊比利亚那边的资料里曾经提过......）
[charslot(slot="m",name="avg_npc_925_1#7$1",focus="m")]
[name="蕾缪安"]......
[charslot(slot="m",name="avg_npc_925_1#7$1",focus="m")]
[name="蕾缪安"]你难道真的是......
[dialog]
[charslot(slot="m",name="avg_npc_930_1#1$1",focus="m")]
[delay(time=0.3)]
[charslot(slot="m",action="zoom",poszoom="0.5,0.5",scale=1.1,duration=0.1,isblock=false)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_wolflordclaw",volume=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_925_1#3$1",focus="m")]
[delay(time=0.1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=0.3, block=false)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$b_char_defboost")]
[Delay(time=1)]
[name="蕾缪安"]嘶......
[charslot(slot="m",name="avg_npc_925_1#7$1",focus="m")]
[name="蕾缪安"]轮椅还是太不方便了。
[charslot(slot="m",name="avg_npc_925_1#7$1",focus="m")]
[name="蕾缪安"]（......奇怪，有哪里不对劲。）
[charslot(slot="m",name="avg_npc_925_1#11$1",focus="m")]
[name="蕾缪安"]（它的攻击目标......好像不是我？）
[charslot(slot="m",name="avg_npc_925_1#11$1",focus="m")]
[name="蕾缪安"]（它在瞄准哪里？它的目标是——）
[dialog]
[charslot(slot="m",name="avg_npc_930_1#1$1",focus="m")]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_wolflordclaw",volume=0.7)]
[Delay(time=0.1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_wolflordclaw",volume=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_925_1#3$1",focus="m")]
[name="蕾缪安"]好险......！
[charslot(slot="m",name="avg_npc_925_1#7$1",focus="m")]
[name="蕾缪安"]（......算了，现在管不了这么多了！）
[dialog]
[playsound(key="$d_avg_gunload")]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_925_1#3$1",focus="m")]
[name="蕾缪安"]不能看我是不方便移动的伤员就想欺负人哦，这位客人！
[dialog]
[PlaySound(key="$d_avg_gunsingle", volume=0.9)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1,r=1, g=1, b=1, fadetime=0.01, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=false)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_930_1#1$1",focus="m")]
[playsound(key="$d_avg_fseamonsterroar")]
[name="扭曲的怪物"]（尖锐的嘶吼）
[dialog]
[delay(time=0.2)]
[PlaySound(key="$runsand", volume=0.6)]
[charslot(slot="m",name="avg_npc_930_1#1$1",focus="m",afrom=1,ato=0,posfrom = "0,0", posto = "350,0",duration=1)]
[delay(time=1)]
[charslot]
[charslot(slot="m",name="avg_npc_925_1#3$1",focus="m")]
[name="蕾缪安"]站住——！
[charslot(slot="m",name="avg_npc_925_1#3$1",focus="m")]
[name="蕾缪安"]这可不行，不能就这么让你逃走！
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[playMusic(key="$monastery_sad_loop", volume=0.6)]
老人们在闲聊时总会提起拉特兰。
他们说那里明亮，富足，人人安居，没有争吵。
他们说那里是真正的人间乐园。
其实大家都知道，修道院已经在外漂泊好几十年，真正见过拉特兰的人已经很少了。或许还有那么两三位，或许只剩下主教斯特凡诺。
人们提起拉特兰，不过是怀念一个早该醒来的梦。
梦里阳光明媚，鲜花满地。
就像许多年前，修道院曾展现过的模样。
[charslot]
[dialog]
[Background(image="39_g2_abandonsancturay",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_924_1#10$1",focus="m")]
[name="克莱芒"]......它们快要谢了。
[charslot(slot="m",name="avg_npc_924_1#10$1",focus="m")]
[name="克莱芒"]今年花开得比往年要早，我猜到谢得应该也会早一些，只是没想到会这么快......
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]刚刚被摘下的那几朵开得很好，还没到凋谢的时候。
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]真漂亮。是准备送给什么人？
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]......来不及了，已经送不出去了。
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]它们救不了任何人......
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]悲伤。痛苦。绝望。
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]嗯......很复杂的弦音，还有其他的情感藏在你的体内......
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]你在愤怒？
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]不敢......阿尔图罗小姐是主教阁下的客人。
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]只是不敢。很坦诚的回答。
[charslot(slot="m",name="avg_npc_924_1#7$1",focus="m")]
[name="克莱芒"]......
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]我的直觉一向非常准确，花匠先生，你似乎有点讨厌我。
[charslot(slot="m",name="avg_npc_924_1#1$1",focus="m")]
[name="克莱芒"]没这回事，您想多了。
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]如果你有任何烦恼，我想我可以帮你。
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]......帮我？呃，我不明白您的意思，阿尔图罗小姐。
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]帮我什么？
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]这取决于你的想法，而不是由我决定。
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]当然，你也可能并不需要什么帮助。你可以指责我多管闲事，也可以说我

... (全文23203字符)
```

### level_act26side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="39_g11_monasterycorridor_n", screenadapt="coverall", block=true)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_941_1#2$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]我有一点惊讶。
[charslot(slot="m",name="avg_npc_923_1#7$1",focus="m")]
[name="修道院主教"]因为我终究背叛了信仰吗？
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]是因为你的逃避，斯特凡诺。
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]我不知道你是否是受到了什么外物的影响，如果......
[charslot(slot="m",name="avg_npc_923_1#2$1",focus="m")]
[name="修道院主教"]没有如果，奥卢斯。
[charslot(slot="m",name="avg_npc_923_1#2$1",focus="m")]
[name="修道院主教"]我还不至于受源石技艺影响。
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]有时转变我们想法的并不一定是源石技艺。有太多东西足以影响我们，斯特凡诺。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......你在劝我重新考虑。为什么，异教的教士。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]如今我的决定，难道不是你想要看到的？
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]我不能否认。
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]但我也得承认，在这座了不起的建筑尚在伊比利亚时，我曾有幸在此学习，那段时光对于那时的我来说弥足珍贵。
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]斯特凡诺，在这方面我同你一样。我对这里同样怀有感情。
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]我还记得那位和你一起从拉特兰来的修士。
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]我记得许多人。
[charslot(slot="m",name="avg_npc_923_1#2$1",focus="m")]
[name="修道院主教"]......
[charslot(slot="m",name="avg_npc_923_1#2$1",focus="m")]
[name="修道院主教"]你记得的那个人，在六十年前带上他的铳，决定和当时的国教会共进退，而我......
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]而我选择留下，保护剩下的人。
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]你以此为信念，坚持至今。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]既然你清楚，你仍要我继续等待，继续忍耐？
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]难道你现在要否认你一直宣扬的那些，转而要我斟酌，劝我坚定？
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]当然不。斯特凡诺，当然不。
[charslot(slot="m",name="avg_npc_941_1#1$1",focus="m")]
[name="奥卢斯"]只是，正因我行走在我认为正确的路上，便希望你也如此。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]明天早上，如果你仍然坚持，那么我便认为这就是你的选择。
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]我会准备好你需要的东西。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]如果你还没有想好，我会劝你继续考虑。
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]不论如何......我希望你的决定发自真心。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......奥卢斯，你弄错了一件事。
[charslot(slot="m",name="avg_npc_941_1#3$1",focus="m")]
[name="奥卢斯"]什么？
[charslot(slot="m",name="avg_npc_923_1#2$1",focus="m")]
[name="修道院主教"]我已别无选择。
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]......
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]好吧，如果真是如此......
[charslot(slot="m",name="avg_npc_941_1#2$1",focus="m")]
[name="奥卢斯"]那么我会欢迎你，斯特凡诺，我新的同胞。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="39_g9_monasteryroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[playMusic(key="$monastery_sad_loop", volume=0.6)]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[charslot]
[name="斯普莉雅"]介意我进来吗？
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]......请进。
[charslot]
[dialog]
[PlaySound(key="$dooropenquite", volume=0.6)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[charslot(slot="m",name="avg_4015_spuria_1#12$1",focus="m",afrom=0,ato=1,duration=1)]
[delay(time=1.5)]
[name="斯普莉雅"]打扰了。
[charslot(slot="m",name="avg_npc_927_1#5$2",focus="m")]
[name="福尔图娜"]......
[charslot]
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="r")]
[charslot(slot="r",name="avg_4015_spuria_1#12$1",focus="r")]
[name="斯普莉雅"]你看起来不太好。
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]......
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]......我可以问一个问题吗？
[charslot(slot="r",name="avg_4015_spuria_1#1$1",focus="r")]
[name="斯普莉雅"]当然可以。
[charslot(slot="l",name="avg_npc_927_1#4$2",focus="l")]
[name="福尔图娜"]......菲娜她，是不是已经......
[charslot(slot="l",name="avg_npc_927_1#1$2",focus="l")]
[name="福尔图娜"]已经不在了？
[charslot(slot="r",name="avg_4015_spuria_1#2$1",focus="r")]
[name="斯普莉雅"]......如果可以的话，我比较希望你能换一个问题。
[charslot(slot="r",name="avg_4015_spuria_1#2$1",focus="r")]
[name="斯普莉雅"]我不太想骗你。
[charslot(slot="l",name="avg_npc_927_1#4$2",focus="l")]
[name="福尔图娜"]......
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]我知道了。
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]其实我最开始就有这样的感觉......
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]那个时候，我忽然就、就感受不到菲娜......明明她那时那么生气，又那么难过......
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]她就在我面前啊......？我却哪里都找不到她......
[charslot(slot="r",name="avg_4015_spuria_1#2$1",focus="r")]
[name="斯普莉雅"]......
[charslot(slot="r",name="avg_4015_spuria_1#2$1",focus="r")]
[name="斯普莉雅"]如果当时，我没帮你修那把铳......
[charslot(slot="l",name="avg_npc_927_1#6$2",focus="l")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="福尔图娜"]别说了！
[charslot(slot="r",name="avg_4015_spuria_1#6$1",focus="r")]
[name="斯普莉雅"]——！
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]......别说了，求你......
[charslot(slot="r",name="avg_4015_spuria_1#2$1",focus="r")]
[name="斯普莉雅"]......好。
[charslo

... (全文17787字符)
```

### level_act26side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[PlaySound(key="$d_avg_churchfire", volume=0.4, loop=true, channel="bse")]
[Delay(time=2)]
火焰是会吞噬一切的魔鬼。
再珍贵的物品，再受珍视的东西，只要一把火，一切都会就此消失。
[dialog]
[dialog]
[Image(image="39_i03",fadetime=0,screenadapt="coverall")]
[Delay(time=2)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=10,block=false)]
[SoundVolume(volume=0.8, fadetime=2,channel="bse")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
杰拉尔德曾和我说，他们萨卡兹没有故乡，只有如影随形的战火。但他希望他们能有一个故乡，因此他们愿意跟随一位了不起的大人物。
只是后来他失望了，所以选择离开。
那时我不敢问他为什么失望。
刚来到这里时，我们曾经满怀希望。
这些年生活虽然辛苦，大家却仍感到幸福。
但是现在......现在。
现在他们要离开了。我忍不住会想，是不是因为这里的生活也同样已经令他失望？
我呢？我又如何？
现在我正......我正看着那些我珍视的东西，在我眼前燃烧。
燃烧。
消失殆尽。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[Background(image="39_g2_abandonsancturay",screenadapt="coverall")]
[Blocker(a=0.2, r=0.92, g=0.4, b=0.3, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]......
[charslot(slot="m",name="avg_npc_924_1#3$1",focus="m")]
[name="克莱芒"]全都......没了......
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]好烫......！好大的火！
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]烧起来了！圣堂......圣堂烧起来了！快！快打水来救火！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[StopSound(channel="bse")]
[Background(image="39_g8_outsidepath",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_931_1#6$1",focus="m")]
[name="莱蒙德"]怎么回事？我看到有火光，发生什么事了？
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]莱蒙德！你怎么在这？你们不是，不是已经......
[charslot(slot="m",name="avg_npc_931_1#6$1",focus="m")]
[name="莱蒙德"]......现在不是说这个的时候！
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]呃！对，对，你说得没错......！
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]你来得正好！圣堂着火了，快来帮忙！
[charslot(slot="m",name="avg_npc_931_1#6$1",focus="m")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="莱蒙德"]圣堂？！
[charslot(slot="m",name="avg_npc_931_1#6$1",focus="m")]
[name="莱蒙德"]圣堂怎么会......怎么会忽然着火？
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]我也想知道啊！往年这个季节也不是没有过火灾，但没一次烧得这么厉害，怎么偏偏就在这时候出岔子？
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]唉，总之得先把火灭了！幸好烧起来的不是大伙住的地方......
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]......
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]先救火。等着，我去喊人。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="39_g2_abandonsancturay",screenadapt="coverall")]
[PlaySound(key="$d_avg_churchfire", volume=0.8, loop=true, channel="bse")]
[PlaySound(key="$d_avg_labber")]
[PlaySound(key="$d_avg_labber", volume=1, loop=false, channel="water1",delay=1.1)]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.2, r=0.92, g=0.4, b=0.3,  fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]水呢！咳......咳咳，还有没有水，再打点水来！
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]不行，这火势压不住。
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]你小心点，别吸这烟......我们得把大门关上，或许这样火就不会烧到外头来......
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]不行！你说什么混账话！
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]这可是圣堂！圣像还在里头！门关上，咳，门关上难道火就能熄了？！
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]我不是这个意思！但现在太危险了！
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]正确的判断。
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]啊？你懂什么......你是什么人？
[charslot]
[charslot(slot="l",name="avg_npc_929_1#2$1")]
[charslot(slot="r",name="avg_npc_928_1#2$1")]
[name="艾丝塔拉&艾伦戴尔"]......
[charslot]
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]这两个孩子是......不对，你、你怎么能让孩子留在这么危险的地方？！
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]快离远点！这里不安全！
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]你说得对，这里并不安全。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]你已经吸入不少烟尘，如不立即采取相应防护措施，推测将很快出现头晕、重影等生理反应。
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]那又怎么样？说了这么多，有没有点实际的？
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]我之前没见过你，你、你是萨科塔，你是拉特兰来的人吧！想点办法啊，那可是拉特兰的圣像！
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]圣像并非我的任务中需要顾及的目标对象。
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]你在说什么......什么任务不任务的！现在是说这些的时候吗！
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]你就不能用个什么，那种什么法术，把这该死的火给灭了？你要是根本什么都干不了，就站到一边去，别碍着我救火！
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]......抱歉，我无法使用那样的源石技艺。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]想要尽量减少损失，需要更多人参与灭火。
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]我这就去喊人来帮忙！
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]不用。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]有人来了。
[charslot]
[dialog]
[PlaySound(key="$d_avg_crowdrun",volume=0.8)] 
[charslot(slot="r",name="avg_npc_933_1#1$1",duration=1)]
[charslot(slot="l",name="avg_npc_932_1#1$1",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot = "m", name = "avg_npc_188",focus="m")]
[name="焦急的居民"]你们......
[charslot]
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="l")]
[charslot(slot="l",name="avg_npc_932_1#1$1",focus="l")]
[name="谨慎的萨卡兹居民"]来帮忙。莱蒙德通知了我们。
[charslot(slot="r",name="avg_npc_933_1#1$1",focus="r")]
[name="暴躁的萨卡兹居民"]少说废话，快点接一下水桶！我再去搬两桶来！
[cha

... (全文22455字符)
```

### level_act26side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="39_g3_abandonsancturay_ex",screenadapt="showall")]
[charslot(slot="m",name="avg_npc_931_1#7$1")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]......你什么意思？
[name="莱蒙德"]怀疑我？
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]我不是这个意思......
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]你们呢？你们也和他一样怀疑我？
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]......
[charslot(slot="m",name="avg_npc_188",focus="m")]
[name="焦急的居民"]别说得那么难听，莱蒙德，什么怀疑不怀疑的......
[charslot(slot="m",name="avg_npc_931_1#11$1",focus="m")]
[name="莱蒙德"]我没在这放什么火。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]那你怎么会这个点在这里？
[name="惊慌的居民"]你们平常根本不和我们一起祈祷，更不会到圣堂来，你们、你们根本没有信仰......！
[charslot(slot="m",name="avg_npc_931_1#11$1",focus="m")]
[name="莱蒙德"]我们是没什么信仰，但这和放火是两回事。
[charslot(slot="m",name="avg_npc_931_1#8$1",focus="m")]
[name="莱蒙德"]随便你们信不信，我只是......有点私事，碰巧路过。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]什么私事？
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]无可奉告！
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]你......！
[charslot(slot="m",name="avg_npc_933_1#1$1",focus="m")]
[name="费尔南"]行了，怎么，我们就不能在这附近出现了？你们叽叽歪歪这么多，不就是想说是我们的人放的火吗！
[name="费尔南"]呸！莱蒙德，我看刚刚咱们就不该来救什么火，给他们全都烧光才好呢！
[charslot(slot="m",name="avg_npc_188",focus="m")]
[name="焦急的居民"]你说什么？！
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]......这个时节失火之前也不是没有过，或许这就是个巧合。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]可这也太巧了！哎，那边那个萨科塔小哥，你不是说这是有人放的火吗？你看这......
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]是的。我依然认为这是一场人为导致的火灾。
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]你也和这些人一样，觉得是我干的？
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]不，我并不这么认为。
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]你在说谎。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]谎言没有任何用处。
[name="费德里科"]在使用助燃物的前提下，从点火到火势扩散所需的时间非常短，可以推断纵火者当时并没有离开圣堂附近。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]所以说，莱蒙德他......！
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]请不要误解。我的意思是，在起火时有可能出现在现场的人都无法洗脱嫌疑。
[name="费德里科"]包括最先出现的各位，以及我本人。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]你、你在说什么啊......！
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]你觉得我们都有可能放火？我们......像我这样的萨科塔，会亲手烧掉我们的圣堂？
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]种族如何并不能成为脱罪的证据。如果有摧毁圣堂的必要，我不会有所犹豫。
[charslot(slot="m",name="avg_npc_937_1#1$1",focus="m")]
[name="冷静的居民"]......
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]至于针对这位萨卡兹的指控，我没有在现场发现相关证据。
[charslot(slot="m",name="avg_npc_933_1#1$1",focus="m")]
[name="费尔南"]哼，你这家伙倒是说得有点道理！
[charslot(slot="m",name="avg_npc_924_1#1$1",focus="m")]
[name="克莱芒"]费德里科先生说得没错......我们不能没有证据就怀疑他人。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]难道就这么算了？！那可是圣堂！还有那些花，那都是你的心血......
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]请不要再说了......！
[name="克莱芒"]我......不怀疑我们之中的任何人。
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="惊慌的居民"]克莱芒......
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]争论到此为止。
[name="费德里科"]萨科塔未必不会摧毁自己的圣堂。我会继续负责调查事件始末，直到找出真正的犯人。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g3_abandonsancturay_ex", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]喂，长翅膀的，刚刚的事，呃......
[charslot(slot="m",name="avg_1032_excu2_1#9$1",focus="m")]
[name="费德里科"]嗯？
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]刚刚的话题本身就是你挑起来的，要不是你说什么助燃物什么纵火的，大家也不会想歪了！
[name="莱蒙德"]还有，你根本就还没完全相信我吧！
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]嗯。
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]你这家伙就不能多给点反应吗？！
[charslot(slot="m",name="avg_npc_931_1#11$1",focus="m")]
[name="莱蒙德"]咳，算了。总之，我的意思是......
[name="莱蒙德"]......别指望我谢你。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]不用。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_929_1#7$1",focus="r")]
[charslot(slot="r",name="avg_npc_928_1#7$1",focus="r")]
[name="艾伦戴尔"]（这个哥哥不会说谢谢呢，萨拉。）
[charslot(slot="l",name="avg_npc_929_1#6$1",focus="l")]
[name="艾丝塔拉"]（好可怜......）
[charslot(slot="r",name="avg_npc_928_1#3$1",focus="r")]
[name="艾伦戴尔"]（好可怜！不过我们可以教这个哥哥呀，谢谢不难学的！）
[charslot(slot="l",name="avg_npc_929_1#2$1",focus="l")]
[name="艾丝塔拉"]（嗯，但是这个哥哥有点可怕......）
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_931_1#11$1",focus="m")]
[name="莱蒙德"]......胡说！谁不会说谢谢？！
[charslot(slot="m",name="avg_npc_931_1#7$1",focus="m")]
[name="莱蒙德"]喂长翅膀的，这两个到底是哪来的臭崽子？！我从来没见过他们！
[Dialog]
[charslot]
[charslot(slot="r",name="avg_npc_928_1#7$1",focus="all")]
[charslot(slot="l",name="avg_npc_929_1#7$1",focus="all")]
[charslot(slot = "l", action="shake",random=true, power=5, times=60,duration=0.3)]
[charslot(slot = "r", action="shake",random=true, power=5, times=60,duration=0.3)]
[name="艾丝塔拉&艾伦戴尔"]呀！
[Dialog]
[charslot(slot="l",name="avg_npc_929_1#7$1",focus="all")]
[charslot(slot="r",name="avg_npc_928_1#7$1",focus="all")]
[Delay(time=0.2)]
[PlaySound(key="$runsand", volume=0.5)]
[PlaySound(key="$runsand", volume=0.5, loop=false, channel="raw",delay=0.2)]
[charslot(slot="l",name="avg_npc_929_1#7$1"

... (全文35280字符)
```

### level_act26side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Subtitle(text="在拉特兰时，我是很少祷告的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="当然，这并不是说那个时期我的信仰有瑕，或是说相较现在我更自大懒惰，我也没法证明现在的我更加笃信，更谦逊勤勉。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="只不过是尚在拉特兰时，受到当时环境的影响，我认为许多事是没有必要的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在拉特兰，所有为人所追寻的东西就在那里，圣城的赐福就在那里。", x=300, y=370, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="无处不在，无处不有。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="萨科塔清楚这一点。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Image(image="39_i13",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
“主啊，请您原谅......”
“我曾发过誓言，要善待所有求助者，无论是谁，需一视同仁，尽我所能地提供帮助。”
“但我食言了。”
“我已无法回应渴求救助之人，我无法让他们留下，只因我们的物资不足，无法负担。”
“在一群人与另一群人之间，我必须做出选择......”
“......选择。是的，我早已做过不止一次选择......”
“可选择是错误的。而今，我已无法忍受更多错误。”
“我已不能再背弃我的信仰，为救人而舍弃，为多数而抛下少数！”
“拉特兰......我久未重逢的故乡......”
“为何仅有拉特兰才是乐园？”
“若通向我所信的前提，乃是背弃我脑中高悬的指引；若只有借助异教，才可真正消除障碍......”
“......再过不久，一切都将得出答案。”
“倘若我们的主真的存在，就请您宽恕我的罪过......”
[stopmusic(fadetime=1)]
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=0.7)]
[Delay(time=2)]
“——！”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[charslot]
[Delay(time=0.5)]
[Background(image="39_g12_anbandonspace", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_923_1#6$1")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_923_1#6$1",focus="m")]
[name="修道院主教"]什么人！
[Dialog]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step1",loop=false)]
[stopsound(channel="step1",fadetime=1.5)]
[charslot(slot="m",name="avg_npc_923_1#6$1",posfrom="0,0",posto="150,0",afrom=1,ato=1,duration=1.5)]
[Delay(time=2)]
[name="修道院主教"]......
[Dialog]
[PlaySound(key="$d_avg_walkfast",volume=0.4,channel="step2",loop=false)]
[stopsound(channel="step2",fadetime=1)]
[charslot(slot="m",name="avg_npc_923_1#6$1",posfrom="150,0",posto="-150,0",afrom=1,ato=1,duration=1)]
[Delay(time=1.1)]
[PlaySound(key="$d_avg_clothmovementsp",volume=1)]
[CameraShake(duration=0.8, xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="m",name="avg_npc_923_1#6$1",posfrom="-150,0",posto="60,0",afrom=1,ato=1,duration=0.6)]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="l",name="avg_npc_372_1#1$1",bstart=0.2,bend=0.7,posfrom="-60,0",posto="0,0",duration=0.5)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_372_1#1$1",bstart=0.2,bend=0.7,focus="l")]
[name="？？？"]哎，别动手，别动手，有话好好说。
[name="？？？"]我找了您好一会呢，主教阁下。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_snowconutryinside", screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",duration=0.5)]
[charslot(slot="r",name="avg_npc_926_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]最近食物缺得厉害，只有这点东西能招待客人，你不介意吧？
[name="杰拉尔德"]介意也没别的了，味道可能不太好，不过只求填饱肚子的话勉强还可以。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]暂时没有进食的必要。
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]吃吧。都拿出来了，别浪费。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]......
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]萨卡兹领袖杰拉尔德，你认识那两名黎博利孩童。
[charslot(slot="r",name="avg_npc_926_1#7$1",focus="r")]
[name="杰拉尔德"]......你总是这么直接吗？
[name="杰拉尔德"]别喊我领袖，我见过真正的萨卡兹的王，我一介猎户配不上这称呼。
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]为什么自称猎户？
[charslot(slot="r",name="avg_npc_926_1#7$1",focus="r")]
[name="杰拉尔德"]因为我确实是个猎户。我靠打猎养活自己和其他人。
[name="杰拉尔德"]虽然是今天刚到，但我猜你应该已经了解这里的情况了吧。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]不完全。
[name="费德里科"]你带着萨卡兹在这里生活，你们是后来者，但曾经融入得很好。
[charslot(slot="r",name="avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]是啊，曾经是不错。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]现在你们与其他人产生冲突，根据目前的局势判断，这种冲突很大可能会继续升级。
[charslot(slot="r",name="avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]你的判断没错。所以我们就要走了。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]正常情况下，在与其他居民的冲突中，你们会占据上风。
[name="费德里科"]这里的原住民中少见擅长战斗的人员，他们缺乏战斗力也是你们被接受的原因之一。
[name="费德里科"]但如今拉特兰的介入让你们失去了在武力上的优势。离开是稳妥的选择。
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]你很擅长得出合理的解释，执行者阁下。
[name="杰拉尔德"]但从很久之前我就明白，到现在也仍在时刻被提醒——
[charslot(slot="r",name="avg_npc_926_1#4$1",focus="r")]
[name="杰拉尔德"]我们的生活从不合理。
[Dialog]
[charslot(slot="r",name="avg_npc_926_1#4$1",focus="none")]
烛光跳动。
年长的萨卡兹的视线落在墙壁上，那里映出模糊的虚影，一切差异在此时都不再清晰。
[Dialog]
[charslot(slot="r",name="avg_npc_926_1#4$1",focus="r")]
[name="杰拉尔德"]我们不会因无法生存而选择离开。
[name="杰拉尔德"]在来到这里之前，老实说，我从未想过能够有这样的生活。
[name="杰拉尔德"]有种种风险，有许多摩擦，但我们被认可、被接纳，我们亲手搭建住所，靠劳动获得粮食......
[name="杰拉尔德"]或许这在你看来很寻常，但对我们来说，这是曾经不敢想象的日子。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]你们选择离开的真正理由是？
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]很简单。
[name="杰拉尔德"]就如你所说，我们都能预见将会有的冲突，

... (全文18879字符)
```

### level_act26side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_snowconutryinside",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_926_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]都检查过了，屋内没有打斗的迹象，两个孩子没被吵醒，都还在睡。
[name="杰拉尔德"]赫曼不可能会伤害孩子们，这点你可以放心。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]只是暂时还没有。
[name="费德里科"]我并不确定她的理智能够保持多长时间。
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]......多谢你。
[name="杰拉尔德"]等孩子们醒了，你打算怎么告诉他们赫曼的事？
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]他们有权知情。
[charslot(slot="r",name="avg_npc_926_1#4$1",focus="r")]
[name="杰拉尔德"]有的事不知道或许更好。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]是否可以理解为，你在向我提出建议？
[charslot(slot="r",name="avg_npc_926_1#4$1",focus="r")]
[multiline(name="杰拉尔德")]不，费德里科......
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[multiline(name="杰拉尔德")]对了，你不介意我这么喊吧？
[name="杰拉尔德"]放过赫曼的是你，得到孩子们信赖的也是你，所以决定权在你。
[charslot(slot="l",name="avg_1032_excu2_1#5$1",focus="l")]
[name="费德里科"]......
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]感觉有点沉重？
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]我没有佩戴负重装备。
[charslot(slot="r",name="avg_npc_926_1#7$1",focus="r")]
[name="杰拉尔德"]我就当这是你的幽默感了。
[Dialog]
[delay(time=0.6)]
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]你在看什么？
[charslot(slot="l",name="avg_1032_excu2_1#6$1",focus="l")]
[name="费德里科"]你认识这个吗？
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]这是......被褥的碎布？不少居民都用这种布做冬天的被褥，不过这种花纹倒是头一次见到。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]这是拉特兰常见的花纹。
[Dialog]
[charslot]
破碎的布料下方，双胞胎的鼻息绵长安稳。
执行者近乎凝视地看了一会，才将视线转向一旁简陋的木桌上。
那里摆着一只陶土小瓶。
插在瓶内，尚未完全枯萎的浅色花束，是室内除了孩子们之外唯一的色彩。
[Dialog]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]这是......花？不太新鲜了，应该是这两天都没有更换。
[charslot(slot="l",name="avg_1032_excu2_1#9$1",focus="l")]
[name="费德里科"]这是赫曼本人的兴趣？
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]我......不确定。
[name="杰拉尔德"]我原以为我对这些跟着我的人足够了解。但我甚至不能确定......
[charslot(slot="l",name="avg_1032_excu2_1#6$1",focus="l")]
[name="费德里科"]......
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]我需要立刻回一趟圣堂。
[name="费德里科"]至于萨卡兹相关的问题，已知的情报已经足够做出判断。
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]那么，你的判断是？
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]首先我需要了解一件事——你是否与奥伦·亚吉奥拉斯有所交流？
[charslot(slot="r",name="avg_npc_926_1#9$1",focus="r")]
[name="杰拉尔德"]那位奥伦特使？
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]是他。
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]没有多少交流。他来这没多久就失踪了。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]了解了。
[name="费德里科"]你自称杰拉尔德，但这不是你的真名。
[charslot(slot="r",name="avg_npc_926_1#1$1",focus="r")]
[name="杰拉尔德"]......一个被使用了十年的名字，谁能说它不是真的？
[name="杰拉尔德"]我们在这里过日子，从用那些破木板在这里搭起第一间屋子开始，我就只是荒野猎户杰拉尔德。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]你的自我认知与我无关。你可以是杰拉尔德。
[charslot(slot="r",name="avg_npc_926_1#10$1",focus="r")]
[name="杰拉尔德"]那么——
[Dialog]
[stopmusic(fadetime=1.5)]
[charslot(slot="r",name="avg_npc_926_1#10$1",focus="none")]
古怪的急迫感驱使着语言自口腔滑落。
费德里科没有给对方说话的空间。
他张口说出了那个已经十年没有再被正式提起过的名字。
[Dialog]
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]卡兹戴尔内战中崭露头角的雇佣兵，中庭公证所通缉的在逃人员之一，共有三十二项被记录的罪名，曾灭杀教皇厅旗下三支执行小队。
[name="费德里科"]霍斯特·蒂芬达尔。
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[charslot(slot="r",name="avg_npc_926_1#3$1",focus="r")]
[name="杰拉尔德"]——！
[name="杰拉尔德"]你已经知道......
[charslot(slot="l",name="avg_1032_excu2_1#4$1",focus="l")]
[name="费德里科"]是的，我知道。而我可以查到的信息，其他人也一样可以。
[name="费德里科"]这会是最后一次警告——
[name="费德里科"]杰拉尔德，你的身份已经不是秘密。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_wild_a", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_366_1#1$1 ")]
[charslot(slot="r",name="avg_npc_371_1#1$1")]
[delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_366_1#1$1 ",focus="l")]
[charslot(slot="r",name="avg_npc_371_1#1$1",focus="l")]
[name="老练的拉特兰特勤队成员"]确认前方建筑，是目标地点无误。
[name="老练的拉特兰特勤队成员"]真的会有萨卡兹愿意住在我们的修道院里吗？真难想象。
[charslot(slot="r",name="avg_npc_371_1#1$1 ",focus="r")]
[name="年轻的拉特兰特勤队成员"]要准备行动了吗？
[charslot(slot="l",name="avg_npc_366_1#1$1 ",focus="l")]
[name="老练的拉特兰特勤队成员"]不着急。等长官们的指令。
[name="老练的拉特兰特勤队成员"]继续观察吧。总归我们的人已经把这一带都围上了。
[name="老练的拉特兰特勤队成员"]就像之前抓到的那个萨卡兹小队一样......
[name="老练的拉特兰特勤队成员"]只要是萨卡兹，就一个都别想跑。
[charslot(slot="r",name="avg_npc_371_1#1$1 ",focus="r")]
[name="年轻的拉特兰特勤队成员"]是！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g9_monasteryroom", screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4015_spuria_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_927_1#5$2",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]我拿了吃的回来。能找到的东西不多，稍微吃一点？
[charslot(slot="r",name="avg_npc_927_1#5$2",focus="r")]
[name="福尔图娜"]对不起，斯普莉雅......我没有胃口......
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]没事，

... (全文24990字符)
```

### level_act26side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="39_g11_monasterycorridor_n",screenadapt="coverall")]
[charslot(slot="l",name="avg_npc_927_1#5$2",posfrom = "200,0", posto = "200,0",duration=0)]
[charslot(slot="r",name="avg_npc_931_1#1$1")]
[Delay(time=0.5)]
[playMusic(intro="$escape_intro", key="$escape_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]莱蒙德，等一下......莱蒙德！
[CameraShake(duration=0.3, xstrength=5, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="福尔图娜"]你要干什么？！
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]带你离开这。
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]事情我都听说了，那些人别想就这么抓到你！
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]你别害怕，跟我走就好，我们都会帮你——
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]什么？不......我没有害怕！
[CameraShake(duration=0.3, xstrength=5, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="福尔图娜"]莱蒙德，你先松手......你误会了！
[charslot(slot="r",name="avg_npc_931_1#10$1",focus="r")]
[name="莱蒙德"]——！
[Dialog]
[charslot(slot="r",name="avg_npc_931_1#10$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_clothmovementsp")]
[charslot(slot = "l", action="jump",posfrom="200,0",posto="-200,0",power=5, times=1,duration=0.5)]
[CameraShake(duration=0.5, xstrength=5, ystrength=8, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]抱歉！是我太着急了......很疼吗？
[charslot(slot="l",name="avg_npc_927_1#10$2",focus="l")]
[name="福尔图娜"]没事的。
[name="福尔图娜"]你听我说，莱蒙德！我是、我是自愿跟他们去拉特兰的！
[charslot(slot="r",name="avg_npc_931_1#6$1",focus="r")]
[name="莱蒙德"]什么......？
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]别说胡话了！他们拿什么威胁你了？你去那里会死的！
[charslot(slot="l",name="avg_npc_927_1#10$2",focus="l")]
[name="福尔图娜"]那也是我罪有应得！
[name="福尔图娜"]别管我了，莱蒙德，没有人强迫我也没有人威胁我，是我害了菲娜，我不能就这么逃走！
[charslot(slot="r",name="avg_npc_931_1#3$1",focus="r")]
[name="莱蒙德"]德尔菲娜......那是个意外......
[charslot(slot="l",name="avg_npc_927_1#10$2",focus="l")]
[name="福尔图娜"]不！我不想连你也说什么“那是个意外”！
[name="福尔图娜"]意外......意外！是啊，我怎么可能会故意拿铳对着菲娜，那只是个可悲的意外......但是菲娜真的死了！死了！
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]莱蒙德，菲娜不会再睁开眼睛，不会再和我们说话了！
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]福尔图娜，冷静......别这样抓，别伤到你自己！
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]我想冷静下来的......我也不想这样又哭又叫！
[charslot(slot="l",name="avg_npc_927_1#6$2",focus="l")]
[name="福尔图娜"]但是为什么没有人因此责备我？！为什么所有人都说只是个意外，好像菲娜她的死用一个轻飘飘的“意外”就可以一笔带过一样？！
[name="福尔图娜"]菲娜她、她被我杀死了！是不是意外有区别吗？！
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]......喘气，别憋着。
[charslot(slot="l",name="avg_npc_927_1#2$2",focus="l")]
[name="福尔图娜"]呼......哈......
[charslot(slot="l",name="avg_npc_927_1#10$2",focus="l")]
[name="福尔图娜"]呼......
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]好点了？
[charslot(slot="l",name="avg_npc_927_1#1$2",focus="l")]
[name="福尔图娜"]......
[charslot(slot="l",name="avg_npc_927_1#5$2",focus="l")]
[name="福尔图娜"]对不起，我不该这样......但是莱蒙德，我不知道该怎么办才好......
[name="福尔图娜"]我只知道......我不能走，不能逃，不能当作什么都没有发生，不能真的认可那是个意外。
[name="福尔图娜"]那是我的罪......
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]别说了。
[charslot(slot="l",name="avg_npc_927_1#10$2",focus="l")]
[name="福尔图娜"]你别担心我，莱蒙德，或许也没有那么糟......
[name="福尔图娜"]斯普莉雅，就是今天来的那位拉特兰的使者小姐，她对我很好，我没有吃什么苦头。
[name="福尔图娜"]或许回到拉特兰后他们会把我关起来？
[name="福尔图娜"]我长出了角......我也不知道现在我还算不算是萨科塔，不过，就算不是也没什么......
[name="福尔图娜"]总之，我没事的，莱蒙德，你——
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]不行。
[charslot(slot="l",name="avg_npc_927_1#3$2",focus="l")]
[name="福尔图娜"]欸？
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]果然还是不行。
[name="莱蒙德"]福尔图娜，我不能就这么放着你不管——
[charslot(slot="l",name="avg_npc_927_1#4$2",focus="l")]
[multiline(name="福尔图娜")]莱蒙德？你怎么了......
[charslot(slot="l",name="avg_npc_927_1#3$2",focus="l")]
[multiline(name="福尔图娜")]呀！
[Dialog]
[charslot(slot="l",name="avg_npc_927_1#3$2",focus="all")]
[Delay(time=0.2)]
[charslot(slot="r",posfrom="0,0",posto="-150,0",duration=0.7)]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_clothmovementsp",volume=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="l",posfrom="0,0",posto="60,0",afrom=1,ato=0,duration=0.6)]
[charslot(slot="r",posfrom="-150,0",posto="-50,0",afrom=1,ato=0,duration=0.6)]
[Delay(time=1)]
[charslot]
[name="莱蒙德"]（先别说话！屏住呼吸......！）
[name="福尔图娜"]（......？！）
[name="莱蒙德"]（......有人过来了！）
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="39_g11_monasterycorridor_n", screenadapt="coverall", block=true)]
[delay(time=0.5)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$transmission",volume=0.6)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_355_1#1$1",focus="r")]
[charslot(slot="r",name="avg_4015_spuria_1#12$1",focus="r")]
[name="斯普莉雅"]他挂了。
[name="斯普莉雅"]我怎么不知道，你居然已经把里凯莱策反了？
[charslot(slot="l",name="avg_npc_355_1#1$1",focus="l")]
[name="奥伦"]策反谈不上，他就是那种人，只做对自己有利的事。
[name="奥伦"]在自保这方面，他比我还有本事......
[charslot(slot="l",name="avg_npc_355_1#9$1",focus="l")]
[name="奥伦"]......嗯？
[name="奥伦"]总觉得好像有人在盯着我看......
[charslot(slot="r",name="avg_4015_spuria_1#1$1",focus="r")]
[name="斯普莉雅"]怎么，奥伦你是终于多疑到出现幻觉了吗？
[charslot(slot="l",name="avg_npc_355_1#9$1",focus="l")]
[name="奥伦"]比起幻觉，我更愿意相信是真的有什么人躲在角落里偷听。
[charslot(slot="r",name="avg_4015_spuria_1#8$1",focus="r")]
[name="斯普莉雅"]......
[charslot(slot="l",name="avg_npc_355_1#1$1",focus="l")]
[name="奥伦"]哈哈，别那样看我，开个玩笑而已。
[name="奥伦"]对了，你看着的那个堕天使小

... (全文17546字符)
```

### level_act26side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="39_g7_chapel",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_sweep")]
[charslot(slot="l",name="avg_npc_939_1#1$1",duration=0.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="none")]
[PlaySound(key="$d_avg_open_door", volume=1)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="瘦削的修道院居民"]主教阁下，您来了。
[Dialog]
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_walk_stage")]
[charslot(slot="r",name="avg_npc_923_1#1$1",duration=1)]
[delay(time=2.5)]
[charslot(slot="r",name="avg_npc_923_1#1$1",focus="r")]
[name="修道院主教"]今天轮到你打扫礼拜堂啊，约里。
[name="修道院主教"]辛苦了。
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="约里"]应该的。最近发生了很多事，本来也睡得不安稳。
[name="约里"]我来帮您拿圣餐吧。
[charslot(slot="r",name="avg_npc_923_1#1$1",focus="r")]
[name="修道院主教"]唔，不用了......
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="约里"]啊对，瞧我，手上全是灰尘。
[name="约里"]呃，您有没有闻到什么味道......隐隐约约的......
[charslot(slot="r",name="avg_npc_923_1#10$1",focus="r")]
[name="修道院主教"]奇怪的味道吗？
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="约里"]不，很好闻，很清新，我能从中感受到一种......生命力。
[name="约里"]具体的，我说不上来，像是站在下风口，虽然分辨不出源头，但循着这个味道，往前走......往前走肯定能到一个什么地方。
[charslot(slot="r",name="avg_npc_923_1#7$1",focus="r")]
[name="修道院主教"]......
[charslot(slot="r",name="avg_npc_923_1#10$1",focus="r")]
[name="修道院主教"]应该是花香，约里。
[name="修道院主教"]小麦粉不够了，今天圣餐里无酵饼的原料，有三分之一是可食用花粉。
[name="修道院主教"]地窖里还剩下的那几瓶葡萄酒有些酸了，所以我也撒了些花粉在里面。
[name="修道院主教"]前两年花期还没有结束的时候，克莱芒就提前收割了一些花朵，晒干，制成粉末，存在地窖里......
[name="修道院主教"]他爱护那些美丽的花朵，他也爱护我们。
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="约里"]唔......
[charslot(slot="r",name="avg_npc_923_1#5$1",focus="r")]
[name="修道院主教"]这是修道院离开这里前的最后一次圣餐，但我们的存粮已经见底，只好把每个人的圣餐份额减半，还要掺些......杂粮。
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="约里"]不，您别这样说。况且今天的圣餐，让人有胃口极了......
[charslot(slot="r",name="avg_npc_923_1#1$1",focus="r")]
[name="修道院主教"]既然如此，约里，你赶快回房间洗把脸，晨会之前和其他人一起过来。
[name="修道院主教"]剩下的准备工作，我自己来就好。
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="l")]
[name="约里"]好。
[Dialog]
[charslot(slot="l",name="avg_npc_939_1#1$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="l",name="avg_npc_939_1#1$1",afrom=1,ato=0,duration=1)]
[delay(time=2)]
[charslot(duration=0.2)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_939_1#1$1",duration=0.3)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_939_1#1$1",focus="m")]
[name="约里"]主教阁下，今天之后，我们都会被拯救吗？
[name="约里"]所有人，萨科塔、萨卡兹......这座修道院里的所有人，都会被拯救吗？
[name="约里"]可是明明杰拉尔德已经......
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......
[name="修道院主教"]你先去吧，约里。
[charslot(slot="m",name="avg_npc_939_1#1$1",focus="m")]
[name="约里"]那，待会儿见，主教阁下。
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.4)]
[charslot(slot="m",name="avg_npc_939_1#1$1",afrom=1,ato=0,duration=1)]
[delay(time=2.5)]
[Dialog]
[PlaySound(key="$doorclosequite", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]......
[Dialog]
[charslot]
老人掩上了门。
他缓慢地走到了祷告台上。
年迈的安布罗修修道院主教，斯特凡诺·托雷格罗萨，开始将圣餐中的无酵饼和葡萄酒小心地分成一份一份。
他低着头，时候尚早，还很暧昧的晨光从圣像后的窗户透进来，圣像的表情隐没在黑暗里。他的表情也同样看不分明。
[Dialog]
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]会的。我们都会得到拯救。
[Dialog]
[musicvolume(volume=0.3, fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g3_abandonsancturay_ex", screenadapt="coverall", block=true)]
[delay(time=1)]
[musicvolume(volume=0.6, fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_walk_stage")]
[Delay(time=1)]
她走进倾颓的圣堂，一些徒留形状的植物根茎在她的脚下化作齑粉。
屋顶的拱形承重结构已经在大火中倒塌，圣堂暴露在天光之下。
风早已吹散刺鼻的焦味，但满眼都是断壁残垣，短时间内没有人会来整理。
除非重建，那场大火的痕迹永远不会消失。
她看了一眼躺倒在地板上的半截圣像，突然扭过头去，看向身后空荡荡的地方。
[Dialog]
[charslot(slot="m",name="avg_npc_490_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]......
[Dialog]
[PlaySound(key="$d_avg_cellodoubt")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]人们总是挣扎，翻来覆去地自我拷问、自我开解，就像奏鸣曲来到高潮段落，弦键纷飞，快慢错落，激昂，萦回。
[name="阿尔图罗"]下定决心后的那刻，奏鸣曲则进入平缓悠长的尾声，这是一种脱力后的虚无，但又无比决绝。
[name="阿尔图罗"]情感是复杂的，但情感的变化总是相似，旋律工整得让人没有惊喜。
[name="阿尔图罗"]......我感受到了你的平静，所以你终于做好了选择。
[name="阿尔图罗"]不管怎样，我应该演奏你。最后的时刻，你应该听见自己的心声。
[name="阿尔图罗"]迷途的、丰沛的灵魂啊。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g12_anbandonspace", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_372_1#5$1",duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_372_1#5$1",focus="m")]
[name="里凯莱"]这些坛子，还有案板......烘焙的痕迹，但空气中并没有残留发酵的味道......嗯，无酵饼确实也不需要发酵。
[name="里凯莱"]看来这里就是准备圣餐的场地了。
[name="里凯莱"]某种异物的碎屑，暂时分辨不出来历......摸起来很潮湿，是因为在地下吗......
[name="里凯莱"]不对。
[name="里凯莱"]桌角还残留着一些小麦粉......为什么也会这么黏稠......
[charslot(slot="m",name="avg_npc_372_1#8$1",focus="m")]
[name="里凯莱"]这个味道......
[name="里凯莱"]......
[name="里凯莱"]......那位虔诚的主教，努力到最后，只能选择这样一条路吗？
[name="里凯莱"]费德里科那边还是联系不上......直接把这些信息告诉奥伦？那事情会变得更加麻烦。
[charslot(slot="m",name="avg_npc_372_1#10$1",focus="m")]
[name="里凯莱"]哈哈，不会真的要我来处理吧？伊比利亚那边的东西，我了解得可不多啊。
[Dialog]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_372_1#8$1",focus="m")]
[name="里凯莱"]唉，头疼。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[B

... (全文18005字符)
```

### level_act26side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="39_g7_chapel",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_walk_stage")]
[PlaySound(key="$d_avg_walk_stage",channel="skz1",loop=false,delay=0.6)]
[PlaySound(key="$d_avg_walk_stage",channel="skt1",loop=false,delay=2.6)]
[PlaySound(key="$d_avg_walk_stage",channel="skt2",loop=false,delay=3.2)]
[charslot(slot="l",name="avg_npc_934_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_932_1#1$1",duration=1)]
[Delay(time=2)]
[charslot]
[charslot(slot="l",name="avg_npc_938_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_189",duration=1)]
[Delay(time=3)]
[charslot]
[Delay(time=1)]
[PlaySound(key="$d_avg_runstop", volume=0.8)]
[charslot(slot="m",name="avg_npc_939_1#1$1",duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_939_1#1$1",focus="m")]
[name="约里"]早安，主教阁下。
[charslot(slot="m",name="avg_npc_923_1#8$1",focus="m")]
[name="修道院主教"]早安，又见面了，约里。请招呼一下其他人。
[charslot(slot="m",name="avg_npc_939_1#1$1",focus="m")]
[name="约里"]好的。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="胆怯的萨卡兹居民"]主教阁下，我们......
[charslot(slot="m",name="avg_npc_923_1#8$1",focus="m")]
[name="修道院主教"]最近发生了很多事，苏拉尔，我理解你的愁苦。
[charslot(slot="m",name="avg_npc_934_1#1$1",focus="m")]
[name="胆怯的萨卡兹居民"]我们是不是不该来？拉特兰来的那些人会不会......
[charslot(slot="m",name="avg_npc_923_1#8$1",focus="m")]
[name="修道院主教"]没关系。
[name="修道院主教"]生活在安布罗修修道院的人，都有资格进入礼拜堂，十年来都是如此。
[name="修道院主教"]就坐在第一排吧，苏拉尔，像以前一样，不用紧张。
[name="修道院主教"]拉特兰人不会打扰已经开始的圣餐仪式。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0.1, loop=true, channel="crwd")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.5)]
[name="修道院主教"]各位，请入座。
[name="修道院主教"]接下来是餐前祷告的时间。请各位等待，请各位聆听，请各位感受此刻的宁静。
[Dialog]
[stopsound(channel="crwd", fadetime=3)]
[Delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Image(image="39_i09",screenadapt="coverall", xScale=1.7, yScale=1.7, x=450, y=100,fadetime=0)]
[ImageTween(xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1.7, yScaleTo=1.7, xTo=380, yTo=60, duration=15)]
[delay(time=0.5)]
[PlayMusic( key="$monastery_sad_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[name="修道院主教"]本人斯特凡诺·托雷格罗萨，安布罗修修道院主教，向各位居民致意。
[name="修道院主教"]我习惯用“居民”来称呼大家，而非“信徒”“同胞”或者其他。
[name="修道院主教"]世人，包括我们自己，对萨科塔和萨卡兹的印象从来如此，律法与野蛮、秩序与暴力、和平与战争、天使与恶魔云云......
[name="修道院主教"]光环与角是我们醒目的体貌，是镌刻进生命的符号，我们各自都是行走在这片大地上会引来关注的群体。
[name="修道院主教"]但过去的数千个日子里，我们共同生活，今天又聚集于此，分领圣餐，共享荫护与赐福。
[name="修道院主教"]大家来到修道院的时间有长有短，但最短的也已逾十年。
[name="修道院主教"]在更长的时间里，我们无从确定自己是否已遭离弃，或已被遗忘。我们未知前路，而又身处险地，终于在无人知晓的歧路相逢。
[Dialog]
[Image(image="39_i09", screenadapt="coverall",fadetime=2, xScale=1.7, yScale=1.7, x=-450, y=100)]
[ImageTween(image="39_i09", fadetime=0.5, xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1.7, yScaleTo=1.7, xTo=-380, yTo=60, duration=15)]
[Delay(time=3)]
[name="修道院主教"]我们并非没有矛盾，我们并非没有隐秘，但我们试着彼此接纳。
[name="修道院主教"]此刻，礼拜堂中的所有人，我们知晓对方的名姓，了解彼此的习惯，我们自觉分享食物，愿意为对方抵御风雨。
[name="修道院主教"]我们共同驱赶野兽，对抗匪徒；我们共同烧制砖石，整理路面；我们修补每一扇窗户，耕种每一垄粮食。
[name="修道院主教"]我们亲如手足，我们彼此爱护，我们将对方的安宁视作自己的所求。
[name="修道院主教"]我们的联系如此紧密，共同的体貌或天然的感应不足以证明什么，信仰的差异或理念的分歧不足以阻隔什么。
[name="修道院主教"]但我们苦熬长夜，却禁受不住晨光熹微之时的寒冷。
[Dialog]
[Image(image="39_i09", fadetime=2, xScale=1, yScale=1)]
[ImageTween(image="39_i09", fadetime=0.5, xScaleFrom=1., yScaleFrom=1, xScaleTo=0.85, yScaleTo=0.85,duration=12)]
[Delay(time=3)]
[name="修道院主教"]远道而来的拉特兰特使、执行者，以及......异域的使者，他们各有盘算，带来了新的希望，也带来了令人苦痛的抉择。
[name="修道院主教"]我们本就残破的梁柱在大火中倾塌，我们可敬可靠的手足在矛盾中殒命......
[name="修道院主教"]斯特凡诺·托雷格罗萨想要谋求尽善的结果，哪怕那是一个未经验证的答案，为此我祈求各位的原谅。
[name="修道院主教"]安布罗修修道院并非乐土，但它是我们共同的“家园”。
[name="修道院主教"]我相信我们会做出一样的选择。
[Dialog]
[Delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[image]
[delay(time=0.5)]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[name="修道院主教"]祷告结束，请各位领取并享用圣餐。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g8_outsidepath", screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_925_1#6$1",focus="m")]
[name="蕾缪安"]疼吗？
[charslot(slot="m",name="avg_npc_355_1#9$1",focus="m")]
[name="奥伦"]还好。
[charslot(slot="m",name="avg_4015_spuria_1#1$1",focus="m")]
[name="斯普莉雅"]别嘴硬了，奥伦，我都听见你上下牙打颤的声音了。
[charslot(slot="m",name="avg_npc_355_1#9$1",focus="m")]
[name="奥伦"]力气再怎么大，狙击铳铳管的威力也不会大过它的子弹。
[charslot(slot="m",name="avg_npc_925_1#6$1",focus="m")]
[name="蕾缪安"]我不介意真给你一颗。
[charslot(slot="m",name="avg_npc_355_1#9$1",focus="m")]
[name="奥伦"]我能清晰感受到你的愤怒......真是强烈。
[name="奥伦"]你在为我冒犯了你信仰的纯粹而愤怒。这样的愤怒，说明你正是作为一个拉特兰人在思考问题。
[name="奥伦"]你的任务是将安布罗修修道院带回拉特兰，救助其中意外离散的萨科塔同胞。而我的目标，则是维护拉特兰之所以为拉特兰的合理性。
[name="奥伦"]放下那些感性的念头吧，蕾缪安，我们从来都没有矛盾。
[charslot(slot="m",name="avg_npc_925_1#6$1",focus="m")]
[name="蕾缪安"]你依然在诡辩。
[name="蕾缪安"]这套靠用冠冕堂皇的大道理唬人的说辞，是从维多利亚那些公爵，还是从哥伦比亚那些商人身上学来的，万国信使奥伦？
[name="蕾缪安"]我说过，突然出现的野兽会惊吓到流浪的人，我不会坐视一场屠杀发生。
[charslot(slot="m",name="avg_npc_355_1#7$1",focus="m")]
[name="奥伦"]特勤部队马上就会就位，你阻拦不了我。
[charslot(slot="m",name="avg_npc_925_1#6$1",focus="m")]
[name="蕾缪安"]我大可以制服你，然后再想办法搞定他们。
[charslot(slot="m",name="avg_npc_355_1#7$1",focus="m")]
[name="奥伦"]除非你真正对着我的脑袋给我一颗子弹，不然这样的偷袭不会成功第二次

... (全文10541字符)
```

### level_act26side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="39_g12_anbandonspace",screenadapt="showall")]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.8, block=true)]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_923_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]一切都已经准备好了，众人会在晨会上吃下它......吃下最后一顿餐食。
[charslot(slot="m",name="avg_npc_923_1#4$1",focus="m")]
[name="修道院主教"]你的琴声......会为我感到悲哀吗？还是庆贺？
[name="修道院主教"]我不懂音乐，阿尔图罗。就像我无法理解你。
[name="修道院主教"]你站在这里，我与你共感，但你仿佛一片空白。
[charslot(slot="m",name="avg_npc_490_1#1$1",focus="m")]
[name="阿尔图罗"]我不过是依照我的意愿自由演奏，阁下。我的音乐只是一面镜子。
[charslot(slot="m",name="avg_npc_923_1#7$1",focus="m")]
[name="修道院主教"]镜子......呵。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_dishes")]
年迈的主教端起瓷盘，双手在琴声中颤抖着。
他仿佛在与幽暗中回荡的琴音角力，等待着对方的终结。
多年前修道院里响起乐声时，他还很年轻，年轻到在喷泉里的倒影中看不见一根白发。
荒野的羽兽被吸引到这片移动的沃土上，在管风琴声中振翅，飞过广场。年迈的老主教将修道院交给他，最年轻的修士斯特凡诺。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“你要留众人活在乐园之中。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我要如何留众人活在乐园之中？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
如今历经沧桑的主教托雷格罗萨闭上眼睛。
琴音依然回荡着，回荡着，回荡着。然后——
他松开了手。
[Dialog]
[delay(time=0.5)]
[PlaySound(key="$bottlebroken")]
[CameraShake(duration=0.7, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_490_1#5$1",focus="m")]
[name="阿尔图罗"]......啊。
[name="阿尔图罗"]多痛苦啊，这就是你的选择。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[charslot]
[Background(image="39_g1_monasteryentrance", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, amount=0, block=true)]
[delay(time=2)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]......
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="none")]
礼拜堂紧闭的大门里传来模糊的说话声。
费德里科站在空旷的大厅中听了片刻，然后转身走上了楼梯。
[Dialog]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_walk_stage")]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",afrom=1,ato=0,duration=1)]
[Delay(time=2)]
[name="费德里科"]......装备正常。
[name="费德里科"]截至目前，唯一的损失为一枚通讯器。
[name="费德里科"]当前目标未更改，继续执行任务。
[name="费德里科"]已锁定嫌疑人。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="39_g10_monasterycorridor_d", screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.8,channel="alstep",loop=false)]
[stopsound(channel="alstep",fadetime=3.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_355_1#9$1",duration=0.5)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_355_1#9$1",focus="m")]
[name="奥伦"]里面情况怎么样？
[charslot(slot="m",name="avg_npc_372_1#1$1",focus="m")]
[name="里凯莱"]圣餐仪式应该已经结束了。
[charslot(slot="m",name="avg_npc_355_1#8$1",focus="m")]
[name="奥伦"]......情况和我想的一样吗？
[charslot(slot="m",name="avg_npc_372_1#1$1",focus="m")]
[name="里凯莱"]恐怕是的。
[charslot(slot="m",name="avg_npc_355_1#7$1",focus="m")]
[name="奥伦"]该死，费德里科呢？
[charslot(slot="m",name="avg_npc_372_1#1$1",focus="m")]
[name="里凯莱"]联络不上。
[charslot(slot="m",name="avg_npc_355_1#7$1",focus="m")]
[name="奥伦"]......他知不知道深海教会养出来的怪物有多难对付？
[charslot(slot="m",name="avg_npc_372_1#8$1",focus="m")]
[name="里凯莱"]工作总是需要人来做。蕾缪安和斯普莉雅呢？
[charslot(slot="m",name="avg_npc_355_1#9$1",focus="m")]
[name="奥伦"]收到你的消息之后，她们去地下调查了。
[charslot(slot="m",name="avg_npc_372_1#8$1",focus="m")]
[name="里凯莱"]好吧，那这最麻烦的工作只能我们两个人来干了。
[charslot(slot="m",name="avg_npc_372_1#1$1",focus="m")]
[name="里凯莱"]推门吧。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g7_chapel", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_923_1#1$1")]
[delay(time=1)]
[PlaySound(key="$d_avg_open_door", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]无论身在何处，无论面对何种境遇，我们都应当彼此尊敬，彼此爱护——
[charslot(slot="m",name="avg_npc_923_1#10$1",focus="m")]
[name="修道院主教"]——早安，来自圣城的使者。
[charslot(slot="m",name="avg_npc_355_1#2$1",focus="m")]
[name="奥伦"]......
[charslot(slot="m",name="avg_npc_372_1#5$1",focus="m")]
[name="里凯莱"]......盘子已经空了。
[charslot(slot="m",name="avg_npc_355_1#7$1",focus="m")]
[name="奥伦"]里凯莱，控制住全部居民。我来对付主教。
[charslot(slot="m",name="avg_npc_923_1#1$1",focus="m")]
[name="修道院主教"]你有什么疑问吗，使者？
[charslot(slot="m",name="avg_npc_355_1#7$1",focus="m")]
[name="奥伦"]疑问？倒不如说......阁下为何想不开，非要将这次晨会变成“最后一次”？
[name="奥伦"]蕾缪安应该告知过阁下，回到拉特兰对接之后，阁下有很大机会继续担任这座修道院的主教......
[charslot(slot="m",name="avg_npc_923_1#10$1",focus="m")]
[name="修道院主教"]拉特兰的使者，你们......凭什么来质问我？
[name="修道院主教"]我已做出自己的选择，放弃了所有人都能得救的宏愿。
[name="修道院主教"]修道院已经穷途末路，最后一次晨会上，就让所有人的盘子空着吧。
[name="修道院主教"]我刚刚向众人宣布，安布罗修修道院，同意返回拉特兰。
[charslot(slot="m",name="avg_npc_355_1#3$1",focus="m")]
[name="奥伦"]......返回拉特兰？
[name="奥伦"]阁下该不会认为，我们会放任深海教会......
[charslot(slot="m",name="avg_npc_923_1#2$1",focus="m")]
[name="修道院主教"]......我说过了，我已做出选择。
[charslot(slot="

... (全文15908字符)
```

### level_act26side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=0.5)]
[playMusic(key="$gardener_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Subtitle(text="我们对生活应该是有所憧憬的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这话说起来好奇怪，这难道不是理所当然的吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="如果对生活没有半点期待，那我们又为什么要拥有生命，降生在这世上呢？总不至于就是为了来受苦的吧？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你看，孩子们就不会考虑这样奇怪的问题。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="童年是多么无忧无虑的一段时光啊，只有脱离童年的人，才能明白那时候的好。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这话放在少年、青年时，也都适用。当时总觉得有许多烦恼，可等之后回头再看看，那时候的小烦恼，算得了什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那个时候，我们都有使不完的力气，总想去做点什么，总相信生活能越来越好。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们是如此认真，如此努力地在生活。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="真奇怪，所有事情难道不是都应该越来越好吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="很难说是从什么时候开始，我像是已经丧失了憧憬未来的力气。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="能容纳我的空间越来越窄小，能供我呼吸的空气越来越稀薄。我的生活变得沉重，变得能够看到尽头，变得......不再有希望。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="就像从山上向下滚落的石头。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="谁都知道石头不会停止，只会不断下落。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="直到摔个粉碎。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Dialog]
[musicvolume(volume=0.3, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g3_abandonsancturay_ex", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_924_1#5$1")]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]我的花......都没了啊。
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]别再往前走了。
[name="费德里科"]此处建筑结构遭到多次破坏，具有高度不稳定性......
[Dialog]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[Delay(time=0.2)]
[playsound(key="$smallearthquake", volume=0.6)]
[Delay(time=1)]
[CameraShake(duration=2.5, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=3)]
[name="克莱芒"]呃——！
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]克莱芒，回来。
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]不，费德里科先生......我想......再找找看。
[charslot(slot="m",name="avg_1032_excu2_1#10$1",focus="m")]
[name="费德里科"]你说过的，这里没有你想要的花了。
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]是啊，我就是想确认......所有的花都死了。没有一朵......任何一朵......幸运地得救。
[Dialog]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_doorbreak", volume=0.5)]
[PlaySound(key="$d_avg_rockfall", volume=0.7,delay=0.3)]
[CameraShake(duration=3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]唔......哈......哈......
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]......
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="m")]
[name="费德里科"]无法解析你的行为。
[name="费德里科"]无法......
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]我亲手种出的花......代表友谊和希望。
[name="克莱芒"]可人们早就不再在意这些，没有人再关注花期，他们遗忘了最不该忘记的事。
[name="克莱芒"]难道不可笑吗？竟然有人怀疑莱蒙德会放火，就因为他是萨卡兹？
[name="克莱芒"]我们明明在一起生活了这么久。越是困难的时刻，我们越该相互依偎......这是主教阁下说的话。我很想相信......我本该相信。
[charslot(slot="m",name="avg_npc_924_1#1$1",focus="m")]
[name="克莱芒"]然而事实就摆在我面前，我无法扭过头去。
[name="克莱芒"]为何隔阂始终存在？人与人是不是注定无法彼此理解？
[name="克莱芒"]一点点的混乱，就足以让表面上的秩序走向崩塌，而一旦陷入混乱，人们就会互相伤害......
[charslot(slot="m",name="avg_npc_924_1#6$1",focus="m")]
[name="克莱芒"]够了......我已经忍耐够久了。
[Dialog]
[charslot(slot="m",name="avg_npc_924_1#6$1",afrom=1,ato=0,duration=1)]
[Delay(time=1)]
克莱芒跌跌撞撞地来到了被大火烧毁的圣像面前。
那里没有第二朵幸运的花，只有一个破旧的木盘，里面盛着几片干瘪的面包。
他将那气味有些古怪的面包放入口中咀嚼。
是略有些腥咸，带着海潮一样苦涩的滋味。
[Dialog]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[CameraShake(duration=0.3, xstrength=8, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="克莱芒"]咳、咳咳，难吃......
[charslot(slot="m",name="avg_1032_excu2_1#4$1",focus="m")]
[name="费德里科"]克莱芒，把你手中的东西放下。
[charslot(slot="m",name="avg_npc_924_1#10$1",focus="m")]
[name="克莱芒"]放下？这可不行......
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[CameraShake(duration=0.3, xstrength=8, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="克莱芒"]咳咳......
[name="克莱芒"]昨夜，我本想去告解，结果无意中听到主教阁下的计划......
[name="克莱芒"]我本来想，至少杰拉尔德他们不用参与进来，他们本来就要走了不是吗？
[name="克莱芒"]但为什么......最后会变成这样？
[charslot(slot="m",name="avg_1032_excu2_1#5$1",focus="m")]
[name="费德里科"]......
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]我会吃完这些东西。
[charslot(slot="m",name="avg_1032_excu2_1#5$1",focus="m")]
[name="费德里科"]你并不是为了延续自己的生命。为何还要尝试转化？
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]我只是想求一个答案。
[name="克莱芒"]我想知道，这世上到底有没有能救我们的存在。
[Dialog]
[charslot]
费德里科知道，自己现在必须要阻止眼前的这个人。
但现实是，他站在原地没有动。
几步之外，阿尔图罗奏响了她的乐器，琴声划破寂静的帷幕，其中的情感费德里科不明白，也从不试图明白。
只是头一次，执行者无法掌控自己的行动。
他开始无法理解自己。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="为什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="为什么他没有在见到对方的第一时间就动手？", x=300, y=370, alignment="center"

... (全文17957字符)
```

### level_act26side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[Subtitle(text="人们都说，拉特兰是一座乐园。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这里自由，欢乐，富有秩序，是纷乱的世间为数不多的净土。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="孩子，你可曾对此抱有任何怀疑？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们的圣城，这座城市如何建立，如何维系，如何发展延绵。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="为何拉特兰独一无二，为何拉特兰被颂为世间净土，千年乐园？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="孩子，你可曾想过，倘若大地上的战火重燃，和平一朝崩毁——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="世间可还容许一座乐园独存？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Delay(time=3)]
[theater(mode=true)]
[PlaySound(key="$alarmenter",channel="warn3", volume=0.8,loop=true,block=false)]
[Sticker(id="st1", multi = true, text="危机。", x=180,y=260, alignment="left", size=24, delay=0.04, width=700,block = false)]
[Blocker(a=0.3, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Sticker(id="st1")]
[Blocker(a=0, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="重复警告。", x=180,y=260, alignment="left", size=24, delay=0.04, width=700,block = false)]
[Blocker(a=0.3, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Sticker(id="st1")]
[Blocker(a=0, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Sticker(id="st1", multi = true, text="危机。", x=180,y=260, alignment="left", size=24, delay=0.04, width=700,block = false)]
[Blocker(a=0.3, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Sticker(id="st1")]
[Blocker(a=0, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Dialog]
[Blocker(a=0.3, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[image]
[charslot]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Image(image="39_i14",screenadapt="coverall",fadetime=4,block=false)]
[Blocker(a=0, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Blocker(a=0.2, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Blocker(a=0, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[StopSound(channel="warn3", fadetime=1)]
[Blocker(a=0.1, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Blocker(a=0, r=1,g=0.2,b=0.2, fadetime=0.7, block=true)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", multi = true, text="......危机等级......评估中......", x=180,y=170, alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n最高级......",block = true)]
[Sticker(id="st1", multi = true, text="\n\n自动运行推演程序。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n推演失败。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n启动紧急应对机制。",block = true)]
[Sticker(id="st1", multi = true, text="\n\n现输出适格人员名单......",block = true)]
[Sticker(id="st1", multi = true, text="\n\n......",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[theater(mode=false)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[image]
[charslot]
[Background(image="26_g2_laterano_cathedralhall", screenadapt="coverall", block=true)]
[Delay(time=2)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_358_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_356_1#1$1",duration=0.7)]
[delay(time=1.5)]
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]教宗阁下，人都到齐了。
[charslot(slot="r",name="avg_npc_356_1#1$1",focus="r")]
[name="伊万杰利斯塔十一世"]辛苦你了。
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]您真的决定了吗？除历代教宗会被授封圣徒外，之前从来没有这样的先例，如此决定恐怕会有些太冒险......
[charslot(slot="r",name="avg_npc_356_1#1$1",focus="r")]
[name="伊万杰利斯塔十一世"]如你所说，我翻遍了所有典籍，遍观我们千年来的记录，从没有类似的记载。
[name="伊万杰利斯塔十一世"]但不必担忧，这并非值得忧虑之事。
[name="伊万杰利斯塔十一世"]恐怕值得思虑的，是我得到的那份警示。
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]您所说的警示，具体是什么内容？
[charslot(slot="r",name="avg_npc_356_1#1$1",focus="r")]
[name="伊万杰利斯塔十一世"]我很想坦诚地回答你的问题，但很可惜，我办不到。
[name="伊万杰利斯塔十一世"]闪耀在我们头顶的信仰向我预警，让我们得知危机将至，但究竟是何种危机，它将如何到来，无人知晓。
[charslot(slot="r",name="avg_npc_356_1#8$1",focus="r")]
[name="伊万杰利斯塔十一世"]我只见到一份名单，数个人名......
[charslot(slot="r",name="avg_npc_356_1#1$1",focus="r")]
[name="伊万杰利斯塔十一世"]上面的头一位，就是我们今天的主角。
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]因此您才提出要给那小子圣徒的名号？
[name="教宗骑士"]即便如此，也可以换个头衔，“圣徒”......还是太特殊，太重了。不论如何，这可是最初建立拉特兰城的圣人们才能有的称谓！
[charslot(slot="r",name="avg_npc_356_1#1$1",focus="r")]
[name="伊万杰利斯塔十一世"]啊，我记得我也有此头衔。
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]这、这如何能相提并论！您是教宗！
[name="教宗骑士"]您现在相当于给出一份不小的权力。自此之后，他将有权参与诸多事务，甚至影响决策......这绝非小事！
[charslot(slot="r",name="avg_npc_356_1#9$1",focus="r")]
[name="伊万杰利斯塔十一世"]别这么紧张，吉奥瓦尼，有时我们需要一点小小的冒险。
[name="伊万杰利斯塔十一世"]对了，我刚刚是不是说过，我得到的那份名单上可不止有一个人名。
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]什么？难道您想把那些人全部封为圣徒......？！
[name="教宗骑士"]胡闹......我是说，这不合规矩！
[charslot(slot="r",name="avg_npc_356_1#1$1",focus="r")]
[name="伊万杰利斯塔十一世"]别急于否定，吉奥瓦尼。首先我们得把人都找到才行。
[name="伊万杰利斯塔十一世"]对啦，我在上面看到了不少我们都熟悉的朋友的名字。你可知这份名单上还有谁？
[charslot(slot="l",name="avg_npc_358_1#1$1",focus="l")]
[name="教宗骑士"]毫无头绪。
[charslot(slot="r",name="avg_npc_356_1#9$1",focus="r")]
[name="伊万杰利斯塔十一世"]哦，既然你猜不到，那我就多保持一些神秘感。
[name="伊万杰利斯塔十一世"]吉奥瓦尼。
[name="伊万杰利斯塔十一世"]我想，等这次仪式结束后，我就该动身去拜访这些朋友了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Backgr

... (全文34843字符)
```

### level_act26side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="39_g2_abandonsancturay",screenadapt="coverall")]
[Delay(time=0.5)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.8, block=true)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[name="爱琳"]快来看这个，霍斯特！这边，你看！
[name="爱琳"]居然真在圣像前种上花了，而且总觉得这里的花开得比其他地方更漂亮哦？克莱芒那家伙脾气虽然软了点，但还是有点本领的嘛！
[name="爱琳"]真亏斯特凡诺能同意，又是挖圣堂地板，又是到处找土什么的......连用什么土都这么讲究。
[name="杰拉尔德"]慢点跑，别忘记你身上还有伤。
[name="爱琳"]这点小伤算什么？
[name="杰拉尔德"]小伤也有恶化的风险。
[name="杰拉尔德"]还有，现在别再叫那个名字了，叫我杰拉尔德。
[name="爱琳"]好了好了，知道了！你怎么也开始管东管西了......可别和斯特凡诺学这个啊！
[name="爱琳"]斯特凡诺那老头子就是管得太多，所以才长那么多皱纹。
[name="爱琳"]老人家就得放宽心，少操心少管事，这样才能长寿！
[name="杰拉尔德"]爱琳！说得太过了，斯特凡诺只是一心为修道院的将来打算。
[name="杰拉尔德"]我们能像现在这样住下，也多亏了他。
[name="爱琳"]我知道！我只是说他打算得太多了，我看了都替他觉得累得慌！
[name="爱琳"]就怕他哪天扛不住了，受不了了，那是要吃大苦头的......！
[name="杰拉尔德"]斯特凡诺不会听劝，他在萨科塔里应该也是特别固执的那一类，只要是他认准了的道理，就一定会坚持到底。
[name="杰拉尔德"]不过，我们能在这里定居下来，也多亏了他的这一点。
[name="杰拉尔德"]他说我们萨卡兹和其他人没什么不同......
[name="爱琳"]老头子这话说得没错啊。
[name="爱琳"]算了，要是真有他扛不住了的那天，大不了你我帮忙搭把手，替他撑着......也算是报恩了。
[name="爱琳"]你也别再想之前的事了。我们那时离开卡兹戴尔，已经背弃了特蕾西娅殿下......杰拉尔德，我们回不了头了。
[name="爱琳"]你我都是。
[name="杰拉尔德"]......我知道。
[name="杰拉尔德"]不用这样提醒我，爱琳。
[name="杰拉尔德"]我曾追随殿下，但不知道什么时候起，我不再能看见殿下描绘的图景......在卡兹戴尔的两位殿下身上，我找不到我们萨卡兹的未来。
[name="爱琳"]别难过。
[name="杰拉尔德"]我没事。至少现在，我们已经有了新的生活。
[name="杰拉尔德"]我把愿意离开的人带出卡兹戴尔，就会对他们负起责任。
[name="爱琳"]现在这日子......比从前好多了。
[name="杰拉尔德"]别大意，我们现在和从前不同，没有物资支持，那些强盗里偶尔也有不好对付的。
[name="爱琳"]你是不是也太小心了一点？
[name="爱琳"]搞不好几年、十几年之后，凶名赫赫的雇佣兵都要变成乡下猎户咯。哈哈哈哈！
[name="爱琳"]哈哈哈哈......
[name="爱琳"]......那个，我说，杰拉尔德啊。
[name="杰拉尔德"]嗯？
[name="爱琳"]你想过你真的放下武器，变成乡下猎户会是什么样吗？
[name="爱琳"]到时候我又会变成什么样？
[name="杰拉尔德"]没有。我没想过。
[name="杰拉尔德"]那时候的我会变成什么样......
[name="杰拉尔德"]爱琳，如果你愿意，你可以亲自确认。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[delay(time=0.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
很久以前，在与人拼杀后的深夜，杰拉尔德总会在想要喘口气时放任自己抬头看天。
天空是压抑的黑色，篝火渐熄，火焰逐渐冷却。
战场上浑身染血的雇佣兵擦掉身上脸上的脏污，注视着同样伤痕累累的同伴，短暂地思考过某些对于他们来说有些奢侈的问题。
他们这样的萨卡兹，是否真的能够拥有所谓幸福的一生？
他曾坚信萨卡兹重新拥有家的那天一定会来，只是他感到越来越无力，越来越力不从心。
他们流了太多血。在实现那位殿下的美好愿景前，他们的血就快要流尽了。
杰拉尔德终于决定放下卡兹戴尔的一切，他带上那些快要活不下去的人，逃一样地离开了曾经为之拼命的土地。
他们隐姓埋名，终于找到一处能容他们萨卡兹安身的场所，他们只期盼在这里过上平静的、与常人无异的生活。
这个愿望一度得以实现。
但是到底是从什么时候开始，生活开始变得苦涩，开始无法呼吸？
就好像是放在台子上无人品尝的佳肴。
明明努力维持，没人破坏，却还是变了质。
如果只有鲜血能让这一切结束......
那么我所能做的事，就只剩下这么一件。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_snowconutryinside", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_926_1#10$1")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_926_1#10$1",focus="m")]
[name="杰拉尔德"]克莱芒，你不必再劝我。
[name="杰拉尔德"]我不能走，也走不了。
[name="杰拉尔德"]我从没告诉过你我之前的名字，那不是什么值得回味的过去，不过是个丧家之犬，一个臭名昭著的逃兵。
[name="杰拉尔德"]有我在，他们就有理由对其他人动手。
[charslot(slot="m",name="avg_npc_926_1#8$1",focus="m")]
[name="杰拉尔德"]别这副表情，我只是先一步去见爱琳，这没什么，死亡对我这样曾经刀口舔血的人来说并不算太陌生。
[name="杰拉尔德"]如果用我的脑袋就能交换其他人的生路，也算是值得。
[name="杰拉尔德"]我走之后，你不用担心这里剩下的人，他们会听我的话。
[charslot(slot="m",name="avg_npc_926_1#7$1",focus="m")]
[name="杰拉尔德"]莱蒙德还年轻，恐怕他会有点冲动。到时候......就拜托你多劝劝。
[charslot(slot="m",name="avg_npc_926_1#1$1",focus="m")]
[name="杰拉尔德"]......
[name="杰拉尔德"]最后......
[charslot(slot="m",name="avg_npc_926_1#4$1",focus="m")]
[name="杰拉尔德"]帮我转告斯特凡诺，或许最开始我们在荒野上流浪那会，就不该贸然停下，不该尝试留下来。
[name="杰拉尔德"]只是对我，对我们萨卡兹来说，这里实在太好了......
[name="杰拉尔德"]能一起生活这么多年，一切真像是一场梦，但我清楚我们终究要面对现实。
[name="杰拉尔德"]替我向斯特凡诺说一句——谢谢，我很抱歉。
[name="杰拉尔德"]接下来就拜托你了，克莱芒。
[Dialog]
[charslot(slot="m",name="avg_npc_926_1#4$1",afrom=1,ato=0,duration=1)]
[Delay(time=1.5)]
[name="杰拉尔德"]到了最后，还是以这个身份......
[name="杰拉尔德"]我究竟是个猎户，还是......依然是那个雇佣兵？
[name="杰拉尔德"]抱歉，爱琳，我现在的样子，恐怕你看了也不会感到满意吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[charslot]
[Background(image="39_g3_abandonsancturay_ex", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0, block=true)]
[charslot(slot="m",name="avg_npc_924_1#5$1")]
[delay(time=3)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]......天亮了。
[name="克莱芒"]从昨天到今天，好像发生了很多事。但又好像只是一眨眼，一切就都结束了。
[name="克莱芒"]不管怎么说......这个夜晚确实漫长，不是吗？
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]你在做什么？
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]不是什么值得您过问的事，费德里科先生。
[name="克莱芒"]我只是想找一朵花，杰拉尔德总不能空着手去见爱琳，这不太好。
[name="克莱芒"]不过，我好像......昨晚的那场大火把东西都烧没了，什么都没剩下。
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]如果你只是想要鲜花，不必特地来这里。
[charslot(slot="m",name="avg_npc_924_1#1$1",focus="m")]
[name="克莱芒"]您不清楚，费德里科先生，那不一样。
[name="克莱芒"]这里的花是特别的。它们是这座修道院培育出来的特殊品种......
[charslot(slot="m",name="avg_1032_excu2_1#1$1",focus="m")]
[name="费德里科"]象征友谊与希望。
[charslot(slot="m",name="avg_npc_924_1#11$1",focus="m")]
[name="克莱芒"]是的，友谊与希望。主教阁下曾告诉我，这是拉特兰与伊比利亚携手合作的象征，是修道院最重要的东西之一......
[name="克莱芒"]多好啊......当时的我，立刻就被它们迷住了。
[name="克莱芒"]那个时候修道院里还到处都是成片种植的花卉，每到花期，从钟塔那样的高处往下看，整座修道院就像是被花填满。
[charslot(slot="m",name="avg_npc_924_1#5$1",focus="m")]
[name="克莱芒"]爱琳特别喜欢那种风景，杰拉尔德也喜欢......
[name="克莱芒"]有很多人原本很怕萨卡兹，不敢和他们说话，但在经过一次花期后，彼此之间的关系就变好了很多。
[name="克莱芒"]大家发现，原来就算是传闻中冷酷好斗的萨卡兹，也会在路过花圃时，停下步子看一小会，也会尝试摘一两朵，装饰在家中。
[name="克莱芒"]他们看起来一点也不像是什么凶恶的亡命之徒，他们和我们没什么不同......
[charslot(slot="m",name="avg_1032_excu2_1#5$1",focus="m")]
[name="费德里科"]......
[charslot(slot="m"

... (全文11549字符)
```

### level_act26side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="39_g3_abandonsancturay_ex",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_1032_excu2_1#1$1",duration=0.5)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[charslot(slot="r",name="avg_npc_931_1#11$1",posfrom="200,0",posto="0,0",afrom=0,ato=1,duration=1)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]喂，那边那个长翅膀的。
[name="莱蒙德"]我在喊你......喂！别走！
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]假设长翅膀是对萨科塔的称呼，这里存在多个形象符合的人物。
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]......喊的就是你。我知道你叫费德里科。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]好的。
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]啧，你这家伙真擅长让人发火。
[name="莱蒙德"]我没工夫和你废话。
[multiline(name="莱蒙德")]那个叫奥伦的家伙......
[charslot(slot="r",name="avg_npc_931_1#6$1",focus="r")]
[multiline(name="莱蒙德")]他告诉我杰拉尔德老大他、他为了我们，为了我和福尔图娜......
[name="莱蒙德"]这是真的吗？！杰拉尔德老大他真的——
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]是的，杰拉尔德已经死亡。
[charslot(slot="r",name="avg_npc_931_1#3$1",focus="r")]
[name="莱蒙德"]......
[name="莱蒙德"]我从来没有这么不想听到肯定回答的时候。
[name="莱蒙德"]我搞不懂啊......这怎么可能......
[charslot(slot="l",name="avg_1032_excu2_1#2$1",focus="l")]
[name="费德里科"]......我很抱歉，但这是事实。
[charslot(slot="r",name="avg_npc_931_1#10$1",focus="r")]
[name="莱蒙德"]哈......你有什么可抱歉的？
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]呼......
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]你离我远点，长翅膀的。最好把眼睛闭上，不许看。
[name="莱蒙德"]我只是眼睛有点痛，你们的光环太刺眼了，只是这样，一会就会好。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]......好。
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]杰拉尔德老大把匕首交给你，那是他的选择，我......没权利否定。
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]但是，我不能让你就这么把它带走。
[name="莱蒙德"]别说你不知道，接下一个萨卡兹雇佣兵的武器意味着什么！
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]名号的传承。
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]没错。所以......连同杰拉尔德老大、连同杰拉尔德的名字，还有他的尊严一起，我会全部从你那里夺回来。
[name="莱蒙德"]我要向你挑战。
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]你不会赢。
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]我必须要赢。
[name="莱蒙德"]只要我还活着，我总会找到你，挑战你。
[name="莱蒙德"]你可别太小看我。
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]我拒绝你的挑战。
[charslot(slot="r",name="avg_npc_931_1#6$1",focus="r")]
[name="莱蒙德"]哈？！你竟然拒绝？！
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]我都这样向你挑战了，你这家伙——
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]杰拉尔德只是一名猎户，我这里的匕首不存在任何继承上的意义。
[charslot(slot="r",name="avg_npc_931_1#10$1",focus="r")]
[name="莱蒙德"]......什么意思？
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]字面意思。
[name="费德里科"]如果你想要的是一柄继承萨卡兹雇佣兵名字的匕首，我并未持有这样一件物品，向我挑战只是浪费你的时间。
[name="费德里科"]如果你想要的是猎户杰拉尔德的匕首，那么它确实被存放在我这里。
[charslot(slot="r",name="avg_npc_931_1#7$1",focus="r")]
[name="莱蒙德"]你这家伙......
[charslot(slot="l",name="avg_1032_excu2_1#10$1",focus="l")]
[name="费德里科"]现在就给你？
[charslot(slot="r",name="avg_npc_931_1#11$1",focus="r")]
[name="莱蒙德"]......开什么玩笑。
[name="莱蒙德"]这可是杰拉尔德老大最宝贝的武器，就这么轻易到我手上，杰拉尔德老大一定也不会同意。
[name="莱蒙德"]所以，你给我把它收好。
[charslot(slot="r",name="avg_npc_931_1#1$1",focus="r")]
[name="莱蒙德"]你等着......我会像杰拉尔德老大一样，带着我们的人找到一条新的出路。
[name="莱蒙德"]等到那时候，我才有资格接下它。我会再回来找你。
[charslot(slot="l",name="avg_1032_excu2_1#5$1",focus="l")]
[name="费德里科"]......
[charslot(slot="l",name="avg_1032_excu2_1#1$1",focus="l")]
[name="费德里科"]好的。
[name="费德里科"]在那之前，我会替你保管。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="39_g8_outsidepath", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_4015_spuria_1#12$1")]
[charslot(slot="r",name="avg_npc_927_1#5$2")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_927_1#5$2",focus="r")]
[name="福尔图娜"]莱蒙德......
[charslot(slot="l",name="avg_4015_spuria_1#12$1",focus="l")]
[name="斯普莉雅"]别看了，我觉得他应该能撑得住。
[charslot(slot="l",name="avg_4015_spuria_1#6$1",focus="l")]
[name="斯普莉雅"]倒是你，你之前说已经无法再握铳，但现在却......在祈祷吗？
[charslot(slot="r",name="avg_npc_927_1#5$2",focus="r")]
[name="福尔图娜"]嗯......
[name="福尔图娜"]我总觉得，它还会回应我。
[charslot(slot="r",name="avg_npc_927_1#10$2",focus="r")]
[name="福尔图娜"]——斯普莉雅，我还能继续用这把铳吗？
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]能啊，怎么不能，虽然这把铳看起来有点旧，但你可以相信我的手艺。
[name="斯普莉雅"]我本来是要去研究遗产铳的哦，那可都是些老古董。
[name="斯普莉雅"]不过最近我越来越觉得......还是新鲜的事情更有意思。
[charslot(slot="r",name="avg_npc_927_1#4$2",focus="r")]
[name="福尔图娜"]新鲜的事情......你不觉得害怕吗？
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]害怕也没用嘛，害怕也还是会想去了解。
[name="斯普莉雅"]而且......
[name="斯普莉雅"]技术要为人所用，这是学姐曾经和我说过的话。
[charslot(slot="l",name="avg_4015_spuria_1#7$1",focus="l")]
[name="斯普莉雅"]那时候我其实没太明白，不过现在嘛......
[charslot(slot="r",name="avg_npc_927_1#4$2",focus="r")]
[name="福尔图娜"]现在？
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]多少明白一点了吧。我是个工匠，我得对从我手上出来的武器负责......
[name="斯普莉雅"]好了，不提这个，你呢？
[name="斯普莉雅"]这位准备和萨卡兹一起离开的女士？你的准备工作都做好了吗？
[charslot(slot="r",name="avg_npc_927_1#3$2",focus="r")]
[name="福尔图娜"]呃......！你、你已经猜到我要跟你说什么了？！
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[name="斯普莉雅"]虽然我不能直接感觉到，但你的心思可比一些能共感的萨科塔还容易猜。
[name="斯普莉雅"]这么一想，没有共感也确实没什么大不了的，是不是？
[name="斯普莉雅"]如果你是打算乖乖回拉特兰的话，可不会在这个时间郑重其事地来找我。
[charslot(slot="r",name="avg_npc_927_1#5$2",focus="r")]
[name="福尔图娜"]......抱歉。
[name="福尔图娜"]我之前明明答应过你，我会服从你们的看管，接受我应得的惩罚......现在我却想逃跑。
[name="福尔图娜"]所、所以......
[charslot(slot="l",name="avg_4015_spuria_1#1$1",focus="l")]
[nam

... (全文21213字符)
```

### training_act26side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 拉特兰圣像栈道教学_a

[PopupDialog(dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]\
闯进来的敌人会令<@tu.kw>修道院的居民</>不安，战斗持续时间越长，居民就越恐慌。

```

### training_act26side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)]拉特兰圣像栈道教学_b

[PopupDialog(dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]\
特别是有敌人经过居民身边时，居民会立刻感到恐慌不安。
```

### training_act26side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 拉特兰圣像栈道教学_c

[Tutorial(focusX=-40, focusY=196, focusWidth=250, focusHeight=196, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
不过，在靠近<@tu.kw>圣像</>时，居民的情绪能够得到安抚，也不那么容易继续受到惊吓了。
```

### training_act26side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 拉特兰圣像栈道教学_d

[Tutorial( focusX=0, focusY=163, focusWidth=150, focusHeight=150, \
            animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
恐慌到达一定程度后，居民会进入<@tu.kw>“惶惶不安”</>的状态，在这种情况下，居民会<@tu.kw>快速消耗体力</>并且盲目移动，寻找下一个可以祈祷的<@tu.kw>圣像</>。

```

### training_act26side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 第十二章物资箱教学_e

[Tutorial( focusX=255, focusY=11, focusWidth=150, focusHeight=150, \
            animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_huang")] \
啊，找到<@tu.kw>圣像</>之后他就稍微镇定了一点呢。

[Tutorial( focusX=364, focusY=33, focusWidth=100, focusHeight=100, \
            animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_amiya", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
在<@tu.kw>圣像</>处祈祷，能有效安抚居民的情绪，让居民平静下来。
```

### training_act26side_01_f

```
[HEADER( is_skippable=true, is_autoable=false)]  拉特兰圣像栈道教学_f

[Tutorial( focusX=45, focusY=-115, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5, dialogHead="$avatar_huang")] \
不妙，前头的通道有<@tu.kw>破洞</>，这群<@tu.kw>“惶惶不安”</>的家伙会慌不择路直接摔下去的！








```

### training_act26side_01_g

```
[HEADER( is_tutorial=true, is_skippable=false, is_autoable=false)] 拉特兰圣像栈道教学_g

[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[Battle.UnlockFunction(mask="CHARACTER_INFO")]
[Battle.UnlockFunction(mask="CHARACTER_MENU")]
[Battle.UnlockFunction(mask="CARD_LIST")]

[Tutorial( focusX=-59, focusY=66, focusWidth=100, focusHeight=100, anchor="BottomRight",\
          animStyle="Highlight", focusStyle="HighlightCircle", black=0.5, \
          protectTime=0.5,  dialogHead="$avatar_amiya")] \
别担心，我们可以用<@tu.kw>备用木材</>帮大家把路修好。

[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="put_down",animStyle="Drag", startX=-59, startY=66, endX=54, endY=-136, dialogY=50, startAnchor="BottomRight", endAnchor="Center", dialogHead="$avatar_amiya")]
[InputBlocker(blockInput=true)]

[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]





```

### training_act26side_01_h

```
[HEADER( is_skippable=true, is_autoable=false)]  拉特兰圣像栈道教学_f

[PopupDialog(dialogHead="$avatar_amiya")]这样暂时就没问题了！







```

### training_act26side_02_a

```
[HEADER(is_skippable=true, is_autoable=false)] 拉特兰落石教学_a

[PopupDialog(dialogHead="$avatar_jesica")]不、不好了！那边的<@tu.kw>墙垣垮塌</>，有<@tu.kw>石块</>砸下来了！

[PopupDialog(dialogHead="$avatar_amiya")]大家当心，被这个高度掉下来的石块砸到可不是小事！

```

### training_act26side_02_b

```
[HEADER(is_skippable=true, is_autoable=false)] 拉特兰落石教学_b

[PopupDialog(dialogHead="$avatar_nearl")]专心战斗！我会<@tu.kw>阻拦落石</>掩护你们！


```

### training_act26side_02_c

```
[HEADER(is_skippable=true, is_autoable=false)] 拉特兰落石教学_c

[PopupDialog(dialogHead="$avatar_jesica")]报告，有居民在朝落石砸下来的方向前进......

[PopupDialog(dialogHead="$avatar_jesica")]怎、怎么办？前面的步道刚才被落石砸坏了，现在也来不及修了！

```


> 本章节共31个脚本文件，此处展示前30个。

## 统计

- 总字符数：411196
- 对话行数：3592


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
