# 明日方舟 · 活动剧情 · act15d0（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act15d0」完整剧情脚本（23个文件，2230行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act15d0
- 脚本文件数：23

### level_act15d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",fadetime=1,block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[PlaySound(key="$d_gen_walk_n", volume=1, Delay=0.3)]
[Delay(time=3)]
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]地点......应该是这里没错吧？
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=1)]
[name="赫默"]嗯，地址没有错。
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]唔，但是，赫默，那个人真的把你约在这里吗？
[name="梅尔"]这里应该是一间酒吧，看上去也没有废弃的样子......
[name="梅尔"]但是这里一个人都没有诶。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]确实，酒摆放得很整齐，环境也很整洁。
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]真奇怪，要不然我们回去吧？已经快要到出发的时候了吧？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]不，对方知道安东尼越狱的事情，也知道他在我们这边，而且......
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]而且？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[musicvolume(volume=0, fadetime=1)]
[Delay(time=2)]
[Background(image="bg_hotel",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Character(name="char_108_silent_1#5")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="赫默"]晚上就该出发了。
[name="赫默"]我再检查一下其他东西吧。
[dialog]
[PlaySound(key="$phone", volume=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=true)]
[Delay(time=2)]
[name="赫默"]嗯？通信？
[name="赫默"]我不记得这座城市里的其他人有我的联络方式......
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_108_silent_1#3")]
[name="赫默"]等等，这是......内部频段？！
[name="赫默"]......
[dialog]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[Delay(time=1)]
[name="？？？"]赫默小姐。
[name="赫默"]你是谁？
[name="？？？"]我是谁并不重要，重要的是，我知道安东尼在你的手上，而你，是他越狱的协助者。
[name="赫默"]......我不知道你在说什么。
[name="？？？"]不用紧张，虽然我没有任何证据可以向你证明，不过我确实没有恶意，否则也不会大费周章用内部线路来和你建立联络。
[name="赫默"]你想做什么。
[name="？？？"]我只是想请你和梅尔工程师过来和我聊一聊。
[name="赫默"]......
[name="？？？"]我就当你同意了，那么，地址是......
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="char_108_silent_1#5")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[name="赫默"]而且听起来好像是个性格恶劣的人。
[Character]
[name="？？？"]一上来就被人说性格恶劣还真是让我有些伤心呢。
[Character(name="char_242_mayer#3")]
[name="梅尔"]谁？
[dialog]
[Character]
[Delay(time=1)]
[Character(name="char_249_muesys_1#5", fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=2)]
[name="？？？"]嗨~
[name="？？？"]我把这家酒吧包了下来，现在这里只有我们三个人。
[name="？？？"]虽然我也想在普通的酒吧里和你们聊天，不过毕竟不是一些能被别人听到的事情呢。
[Character(name="char_249_muesys_1#1")]
[name="？？？"]所以抱歉啦~
[Character(name="char_242_mayer#2")]
[name="梅尔"]你是......
[Character(name="char_249_muesys_1#5")]
[name="？？？"]那么，互相自我介绍一下吧。
[name="？？？"]我是生态科的主任，缪尔赛思。
[Character(name="char_249_muesys_1#5", name2="char_108_silent_1#4", focus=2)]
[name="赫默"]我记得你。
[Character(name="char_249_muesys_1#6", name2="char_108_silent_1#4", focus=1)] 
[name="缪尔赛思"]哎呀，你知道我吗？真是荣幸。
[Character(name="char_249_muesys_1#6", name2="char_108_silent_1#4", focus=2)]
[name="赫默"]老师对我提起过你。
[Character(name="char_249_muesys_1#5", name2="char_108_silent_1#4", focus=1)]
[name="缪尔赛思"]那么，轮到你们了。
[Character(name="char_249_muesys_1#5", name2="char_108_silent_1#2", focus=2)]
[name="赫默"]明知故问。
[Character(name="char_249_muesys_1#1", name2="char_108_silent_1#2", focus=1)]
[name="缪尔赛思"]哎呀，生活总是需要一些仪式感的嘛。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac15_1", fadetime=0)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=15, block=false)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="赫默"]......结构科，赫默。
[name="梅尔"]工程科，鲁特拉工作室，梅尔。
[name="缪尔赛思"]我听说你们二位现在都在一个叫做罗德岛的组织。
[name="缪尔赛思"]为什么你们会掺和这样一件事？
[name="赫默"]......与你无关。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(name="char_108_silent_1#4",name2="char_242_mayer#3")]
[Image]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="char_108_silent_1#4",name2="char_242_mayer#3",focus=2)]
[name="梅尔"]难道说你就是这次的幕后黑手......
[Character(name="char_249_muesys_1#6")]
[name="缪尔赛思"]呵呵，你猜呢？
[Character(name="char_108_silent_1#3")]
[name="赫默"]不，应该不是。
[Character(name="char_249_muesys_1#3")]
[name="缪尔赛思"]哦？何以见得？
[Character(name="char_108_silent_1#4")]
[name="赫默"]既然你能找到我们，就应该知道，安东尼已经离开哥伦比亚境内了。
[name="赫默"]如果你是幕后黑手，现在来找我们已经没有任何意义了。
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]嗯嗯，没错。
[name="缪尔赛思"]如果我是幕后黑手，那么我现在应该在为了安东尼的去向焦头烂额呢。
[Character(name="char_249_muesys_1#6")]
[name="缪尔赛思"]不过我不觉得他们会就此善罢甘休哦？你们的护卫不知道实力如何呢？
[Character(name="char_108_silent_1#4")]
[name="赫默"]......不劳费心。
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]这样啊，那我就放心了。
[Character(name="char_108_silent_1#4",name2="char_242_mayer#3",focus=2)]
[name="梅尔"]诶，但是，赫默，她不是幕后黑手的话，那她......
[Character(name="char_108_silent_1#3",name2="char_242_mayer#3",focus=1)]
[name="赫默"]我也还没有头绪。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]但是，你一定是和这件事有关联而且想从我们这里获得什么的人。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]不愧是结构科的帕尔维斯主任的得意门生，真是聪明呢，我喜欢和你这样的人聊天哦。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1

... (全文20686字符)
```

### level_act15d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_undergroundF",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_133")]
[name="B区囚犯A"]给我倒！
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_132")]
[name="A区囚犯"]咕，可恶......
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(fadetime=1)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[Dialog]
[Delay(time=2)]
[Character(name="char_empty", name2="avg_npc_133",focus=2)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(xstrength=2, ystrength=2, vibrato=10, randomness=50)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=1,block=false)]
[Character(name="char_214_kafka_1#2", name2="avg_npc_133",fadetime=0.6,focus=1)]
[Delay(time=1)]
[name="卡夫卡"]哇啊，喂，怎么回事啊，怎么忽然就打起来了的。
[PlaySound(key="$fightgeneral", volume=0.5)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(xstrength=2, ystrength=2, vibrato=10, randomness=50)]
[Character(name="char_214_kafka_1#4", name2="avg_npc_133",focus=2)]
[name="B区囚犯A"]卡夫卡，不是让你藏好，你怎么跑我这来了。
[Character(name="char_214_kafka_1#4", name2="avg_npc_133",focus=1)]
[name="卡夫卡"]哎呀，我没事，你赶紧给我解释一下。
[PlaySound(key="$fightgeneral", volume=0.5)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=0.5)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(xstrength=2, ystrength=2, vibrato=10, randomness=50)]
[Character(name="char_214_kafka_1#4", name2="avg_npc_133",focus=2)]
[name="B区囚犯A"]嗨，你看不就明白了，感染者和非感染者互相看不顺眼不是很常见的事吗，然后我们就分成两派打起来了呗。
[Character(name="char_214_kafka_1#2", name2="avg_npc_133",focus=1)]
[name="卡夫卡"]虽然确实是很常见的事没错，但是狱警不管吗？！
[Character(name="char_214_kafka_1#2", name2="avg_npc_133",focus=2)]
[name="B区囚犯A"]你仔细看看他们的样子。
[Dialog]
[Character]
[Delay(time=1)]
[CameraShake(stop=true)]
[PlaySound(key="$fightgeneral", volume=0.5)]
[Delay(time=1)]
[PlaySound(key="$fightgeneral", volume=0.5)]
[Character(name="avg_npc_134",name2="avg_npc_134",focus=1)]
[name="狱警A"]啧啧，还是看这群囚犯打架有乐子。
[name="狱警A"]今天轮到咱们值班算是赚到了。
[PlaySound(key="$fightgeneral", volume=0.5)]
[Character(name="avg_npc_134",name2="avg_npc_134",focus=2)]
[name="狱警B"]哈哈，没错。
[name="狱警B"]呆在这鬼地方工作唯一的乐趣也就是这种时候了。
[name="狱警B"]加油啊，A区的，我看好你们！
[PlaySound(key="$fightgeneral", volume=0.5)]
[Dialog]
[Character(fadetime=0.6)]
[Delay(time=1)]
[PlaySound(key="$fightgeneral", volume=0.3)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(xstrength=2, ystrength=2, vibrato=10, randomness=50)]
[Character(name="char_214_kafka_1#2", name2="avg_npc_133",focus=2)]
[name="B区囚犯A"]看到没，他们才是最享受的家伙。
[name="B区囚犯A"]哪边赢了接下来一段时间伙食还会好一点呢。
[Character(name="char_214_kafka_1#2", name2="avg_npc_133",focus=1)]
[name="卡夫卡"]那不是乐子全被他们找去了，不打不行吗？
[PlaySound(key="$fightgeneral", volume=0.3)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(xstrength=2, ystrength=2, vibrato=10, randomness=50)]
[Character(name="char_214_kafka_1#2", name2="avg_npc_133",focus=2)]
[name="B区囚犯A"]不打？卡夫卡，你知道我怎么进监狱的吗？
[name="B区囚犯A"]就是因为揍了看不起我的那些人一拳！
[PlaySound(key="$fightgeneral", volume=0.3)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(xstrength=2, ystrength=2, vibrato=10, randomness=50)]
[Delay(time=1)]
[Character(name="avg_npc_133")]
[name="B区囚犯A"]嘿，卡夫卡，这座监狱可能是这片大地上唯一干爆那群没被感染的杂种们也不会有什么后果的地方了。
[name="B区囚犯A"]打死了也就是关一阵子禁闭的事。
[name="B区囚犯A"]而且真要死了那就死了呗，进监狱了谁怕这个。
[name="B区囚犯A"]啧，不跟你说了，我继续去干架了，你当心点藏好啊！
[Dialog]
[Character(fadetime=1)]
[PlaySound(key="$rungeneral", volume=1,block=false)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[Delay(time=1)]
[Character(name="char_214_kafka_1#4")]
[name="卡夫卡"]嘁，也太看不起我卡夫卡了。
[name="卡夫卡"]不过，感染者和非感染者之间的矛盾果然在这里也存在啊。
[name="卡夫卡"]而且不仅存在，还变成了一种超级扭曲的样子。
[name="卡夫卡"]虽然在外面也见过不少事了，但是这样的场景我也还是第一次见到诶......要是赫默看了肯定会受不了吧。
[name="卡夫卡"]不过我可就不一样了，嘿嘿。
[name="卡夫卡"]场面越混乱我越喜欢。
[name="卡夫卡"]你们打你们的，让我看看有没有油水可以让我蹭一蹭，也好给后面的事情做点准备......
[Dialog]
[PlaySound(key="$rungeneral", volume=1,block=false)]
[Character(fadetime=0.6)]
[Delay(time=1)]
[CameraShake(stop=true)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[musicvolume(volume=0.2,fadetime=0.5)]
[Character]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Delay(time=1)]
[Character(name="char_214_kafka_1#4", name2="char_empty",fadetime=0.6,focus=1)]
[PlaySound(key="$rungeneral", volume=1,block=false)]
[Delay(time=1)]
[name="卡夫卡"]噫，谁把没吃完的饭给偷偷带过来了。
[Dialog]
[Delay(time=1)]
[characteraction(name="left", type="move", xpos=400, ypos=0,fadetime=1, block=false)]
[PlaySound(key="$rungeneral", volume=1)]
[Delay(time=1.5)]
[name="卡夫卡"]

... (全文13678字符)
```

### level_act15d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]那么，让我们继续吧。
[name="缪尔赛思"]感染者和非感染者的地位在监狱中反而得到了平等，真是有够讽刺的呢。
[Character(name="char_108_silent_1#2",name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......那不能叫做平等。
[Character(name="char_108_silent_1#2",name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]呵呵，确实，如果不被当作人对待才能获得平等，那么这种平等还是不要为好。
[Character(name="char_108_silent_1#3",name2="char_249_muesys_1#1",focus=1)]
[name="赫默"]我们能换个话题吗？
[Character(name="char_108_silent_1#3",name2="char_249_muesys_1#6",focus=2)]
[name="缪尔赛思"]我也没有打算把这个话题继续下去，高高在上地聊这样的话题晚上会睡不好的呢。
[Character(name="char_108_silent_1#5",name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]那么，卡夫卡进入监狱的时间，应该是现在的四个半月前，越狱发生的四个月前，曼斯菲尔德监狱正停靠在圣苏菲城的时候吧。
[Character(name="char_108_silent_1#5",name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]是。
[Character(name="char_108_silent_1#5",name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]果然，更早的话，就要往一年前去了。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac15_3",xScale=1.2, yScale=1.2,y=-50, fadetime=0)]
[imageTween(xFrom=50,xTo=-50,duration=30)]
[Blocker(a=0, fadetime=2, block=true)]
[name="缪尔赛思"]毕竟作为移动监狱，它除了每隔几个月会前往周边都市补充资源和接收囚犯之外，平时基本上是停在荒野上的。
[name="缪尔赛思"]用四个月来策划一起越狱，时间说不上短，不过也不能算很长呢。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#5",name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]嗯？等等，这里我有一个疑问。
[Character(name="char_108_silent_1#4")]
[name="赫默"]你提出的规则，该轮到我提问了。
[Delay(time=0.5)]
[dialog]
[Character]
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#3",focus=2)]
[Delay(time=1.2)]
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#2",focus=2)]
[name="缪尔赛思"]啊哈哈，也是，那么请吧。
[Character(name="char_108_silent_1#5")]
[name="赫默"]......在那之前，梅尔，能麻烦你帮我们做些吃的吗？
[Character(name="char_242_mayer#2")]
[name="梅尔"]诶，可以哦，不过我不知道这里的厨房能不能用。
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]可以哦，考虑到这次的谈话时间可能很长，我其实准备了不少食材。
[name="缪尔赛思"]梅尔小姐会下厨吗？
[Character(name="char_242_mayer#4",name2="char_249_muesys_1#5",focus=1)]
[name="梅尔"]我会哦。毕竟我是一人工作室，不会做饭的话早就饿死啦。
[name="梅尔"]虽然莱茵生命和罗德岛都有食堂，不过有时候走过去会很麻烦。
[name="梅尔"]那你们继续聊，我去给你们做点吃的。
[Character(name="char_242_mayer#2",name2="char_249_muesys_1#6",focus=2)]
[name="缪尔赛思"]做之前记得检查一下食材哦？我可不想被说在食材上动手脚呢。
[Character(name="char_242_mayer#4",name2="char_249_muesys_1#6",focus=1)]
[name="梅尔"]好好~
[Character]
[dialog]
[Character(name="char_242_mayer#2")]
[Delay(time=1)]
[Character(fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=2)]
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#6",focus=1)]
[name="赫默"]你还真是......友善。
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]呵呵，我说了，我是来和你谈话的。
[name="缪尔赛思"]反倒是你，为什么特意把梅尔小姐支开？
[Character(name="char_108_silent_1#5",name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......因为我还没有告诉梅尔，海德兄弟的背后是能量科。
[Character(name="char_108_silent_1#5",name2="char_249_muesys_1#3",focus=2)]
[name="缪尔赛思"]......什么？
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac15_3add",xScale=1.2, yScale=1.2,y=20, fadetime=0)]
[ImageTween(xFrom=30, xTo=-30, duration=25, block=false)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="缪尔赛思"]这件事难道不是你们两个人一起策划的吗？
[name="赫默"]不是，我原本不打算告诉她，她只是陪我来这边采购一些器材的。
[name="缪尔赛思"]原来如此，因为能量科和工程科走得很近，不希望让她有不好的想法吗。
[name="缪尔赛思"]不过，既然她不是共犯，那么告诉她有相当的风险哦？
[name="赫默"]......不用你提醒。
[name="赫默"]比起这个，我想知道的是，在这件事情中，能量科究竟站在什么样的位置上？
[name="缪尔赛思"]海德兄弟的背后是能量科，但这一次的事情本身与能量科无关。
[name="缪尔赛思"]是海德兄弟借用了能量科的资源策划了这起刺杀。
[name="赫默"]果然是这样。
[name="缪尔赛思"]那么，轮到我提问了——
[name="缪尔赛思"]据我所知，在安东尼逃狱的帮手中，除了一位原本是监狱入殓师的杜玛小姐，还有一名叫做罗宾的女性。
[name="缪尔赛思"]而奇怪的是，我的情报显示，她本应该是前往刺杀安东尼的杀手之一。
[name="缪尔赛思"]但根据你刚才的说法，你的助手似乎只有卡夫卡小姐一个人。
[name="缪尔赛思"]难道罗宾并不是你的安排？
[name="赫默"]......看来你确实对越狱的过程一无所知，缪尔赛思主任。
[name="缪尔赛思"]我早就说过了嘛。
[name="赫默"]以及，你搞错了一件事，我并没有情报灵通到了解这场刺杀会发生。
[name="缪尔赛思"]诶？
[name="赫默"]如果我事先对此有所了解，那么我不会只让卡夫卡一个人潜入监狱。
[name="赫默"]这对她太危险了，而且在这种情况下，她一个人能发挥的力量也有限。
[name="缪尔赛思"]难道说，你只是掌握了安东尼这条线索？！
[name="赫默"]没错，我在半年前才发现安东尼并没有和他的家人被关在同一座监狱这件事，然后我就安排了卡夫卡进入监狱。
[name="赫默"]我当时的想法是，如果能见到他并协助他越狱自然最好，如果做不到，那就算了。
[name="缪尔赛思"]......然后正好撞上了这场刺杀吗。
[name="缪尔赛思"]原来如此，这样想来确实合理很多。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#5")]
[Image]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]不过，告诉我这件事真的好吗？
[name="缪尔赛思"]要是让我保持着你是为了阻止这场刺杀而行动的印象的话，会让我觉得你厉害很多哦。
[Character(name="char_108_silent_1#3",name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......我不擅长做这种事，缪尔赛思主任。
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]......原来如此，一开始我以为你是我的同类，现在来看，你其实和梅尔小姐其实才是一类人呢。
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]只不过有什么原因让你在最喜爱的研究之余，不得不关心一些自己原本不在意的事情。
[Character(name="char_108_silent_1#3",name2="char_249_muesys_1#1",focus=1)]
[name="赫默"]......
[Character(name="char_249_muesys_1#5")]
[musicvolume(volume=0,fadetime=0)]
[name="缪尔赛思"]而这个原因，我猜，是“炎魔”，对吧？
[Delay(time=1)]
[Character(name="char_108_silent_1#3",name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......
[Character(name="char_108_silent_1#4",name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]那件事与这次的事情无关，缪尔赛思主任。
[name="赫默"]如果你是为了伊芙利特而来，那么我们的谈话就到此为止吧。
[dialog]
[Character]
[Delay(time=0.5)]
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]抱歉抱歉，是我多嘴了，放心，我对这件事也只是有所耳闻，并不知道究竟发生了什么。
[name="缪尔赛思"]为了表达我的歉意，我就免费赠送你一个问题吧。
[musicvolume(volume=0.4,fadetime=1.5)]
[Character(name="char_10

... (全文7431字符)
```

### level_act15d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]疼疼疼......
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]忍一忍，一下就好了。
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]哇啊啊啊啊啊啊！
[Dialog]
[Delay(time=0.5)]
[Character(name="avg_npc_134")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="狱警"]叫什么叫！吵死了！
[name="狱警"]受了伤就去停尸间看看，别在这鬼叫。
[Character(name="char_451_robin#6")]
[name="罗宾"]对不起对不起，那边现在排队的人很多，我就先给他做一些应急措施，马上就好了。
[Character(name="avg_npc_134")]
[name="狱警"]啐。
[Character(name="char_451_robin#3")]
[name="罗宾"]......他说的应该是医务室吧，为什么会叫停尸间？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]啊，那是因为这里的医务室和停尸间是连着的，而且医生和入殓师是一个人。
[name="A区囚犯A"]那个人给人的感觉比较诡异，别说狱警，其实我们没事都不太愿意靠近那边。
[name="A区囚犯A"]也只有打群架后没有办法才不得不去那里接受治疗。
[name="A区囚犯A"]久而久之就叫那边停尸间了。
[Character]
[Dialog]
[musicvolume(volume=0, fadetime=2)]
[Character(name="char_441_lotus_1#4", fadetime=1.7)]
[PlaySound(key="$enemy_dead_n", volume=0.6)]
[PlaySound(key="$enemy_dead_n", volume=0.2,delay=0.6)]
[PlaySound(key="$enemy_dead_n", volume=0.1,delay=1.2)]
[PlaySound(key="$enemy_dead_n", volume=0.05,delay=1.8)]
[Delay(time=2)]
[name="？？？"]你需要帮忙吗？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]噫！杜玛小姐，你、你怎么来了。
[name="A区囚犯A"]啊，我刚才都是瞎说的，那个......
[Character(name="char_441_lotus_1#4")]
[name="杜玛"]没事，我也不太在乎。
[name="杜玛"]比起这个，要来医务室吗？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]不、不了，有这个小姑娘帮我包扎。
[Character(name="avg_npc_132", name2="char_451_robin#5",focus=2)]
[name="罗宾"]嗯，交给我就好。
[Character(name="char_441_lotus_1#3")]
[name="杜玛"]......你的包扎手法不错，那就交给你了。
[Character(name="avg_npc_132", name2="char_451_robin#5",focus=2)]
[name="罗宾"]好。
[Dialog]
[Character]
[Character(name="char_441_lotus_1#4")]
[Delay(time=1)]
[PlaySound(key="$enemy_dead_n", volume=0.6)]
[PlaySound(key="$enemy_dead_n", volume=0.2,delay=0.6)]
[PlaySound(key="$enemy_dead_n", volume=0.1,delay=1.2)]
[PlaySound(key="$enemy_dead_n", volume=0.05,delay=1.8)]
[Character(fadetime=1.7)]
[Delay(time=3)]
[musicvolume(volume=0.4, fadetime=2)]
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]呼......
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]你很怕她吗？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]害怕......不至于，毕竟杜玛小姐还是救了许多人的，但是她确实挺古怪的，就单纯的有些不想接近吧。
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]这样。
[name="罗宾"]好了，你动一动手臂。
[Dialog]
[Character]
[delay(time=0.7)]
[Character(name="avg_npc_132")]
[delay(time=0.51)]
[CameraShake(duration=1, xstrength=30, vibrato=5, randomness=10, fadeout=true, block=false)]
[Delay(time=2)]
[name="A区囚犯A"]......呼，好多了。
[name="A区囚犯A"]你这法子真灵啊，罗宾，你以前是做什么的？
[Character(name="avg_npc_132", name2="char_451_robin#6",focus=2)]
[name="罗宾"]我以前......是在私人安保公司做事的。
[Character(name="avg_npc_132", name2="char_451_robin#6",focus=1)]
[name="A区囚犯A"]私人安保公司？那不是很赚钱吗？
[name="A区囚犯A"]而且你性格也挺不错，我都想不出你这样的人会犯罪进监狱。
[Character(name="avg_npc_132", name2="char_451_robin#6",focus=2)]
[name="罗宾"]......我的爸爸失业后就一蹶不振，一直酗酒，肝出了很大的问题，医药费要很多钱，所以我就铤而走险......
[Character(name="avg_npc_132", name2="char_451_robin#6",focus=1)]
[name="A区囚犯A"]这样啊，啧啧，看来你也不容易。
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]你呢？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]我？嘿，我是做生意的，老婆勾结情夫想把我干掉吞并我的财产，结果最后关头被我反杀了，就这么简单。
[Character(name="avg_npc_132", name2="char_451_robin#6",focus=2)]
[name="罗宾"]......
[Character]
[Dialog]
[Character(name="avg_npc_132")]
[name="A区囚犯A"]总之，我欠你一次。
[name="A区囚犯A"]我在这边也呆了好几年了，这里的事情多多少少都知道一点，你有什么问题都可以问我。
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]我看到平时会有几个A区或者B区的人会进C区的塔，他们是怎么进去的？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]嗯？啊，他们啊。
[name="A区囚犯A"]他们是被抓去给C区的大佬们打扫房间的。
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]打扫房间？
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]是啊，这里其实除了狱警之外的工作人员是很少的。
[name="A区囚犯A"]虽然是官方监狱，好像待遇也不差，但是毕竟谁都不想在监狱工作，而且还是这种成天在荒野上跑的移动监狱。
[name="A区囚犯A"]一般监狱里想要搞什么东西，都是停靠在城市的时候，就地雇一些人来，趁着停靠的时间搞完。
[name="A区囚犯A"]搞不完的话就只能把他们带上，等到搞完了派人把他们送回去，或者干脆把他们带到下一座城市再送走。
[name="A区囚犯A"]上次停靠圣苏菲城的时候就雇了一群人来搞装修，这会儿都已经离开圣苏菲城半个月了还在搞呢。
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=2)]
[name="罗宾"]啊，原来那些到处走的工作人员不是监狱的人啊。
[Character(name="avg_npc_132", name2="char_451_robin#3",focus=1)]
[name="A区囚犯A"]对，正好，你看那边。
[Character]
[Dialog]
[Delay(time=1)]
[Character(name="char_empty", name2="char_empty",focus=-1)]
[characteraction(name="left", type="move", xpos=-50,fadetime=0.4, block=true)]
[characteraction(name="right", type="move", xpos=50,fadetime=0.4, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=50, times=1, fadetime=0.5, block=false)]
[characteraction(name="right", type="move", xpos=-50, times=1, fadetime=0.5, block=false)]
[Character(name="char_214_kafka_1#4", name2="char_440_Pinecone",focus=-1)]
[delay(time=1)]
[name="卡夫卡"]（窃窃私语）
[name="？？？"]（窃窃私语）
[Dialog]
[PlaySound(key="$rungeneral", volume=1)]
[PlaySound(key="$rungeneral", volume=0.7,delay=0.4)]
[characteraction(name="right", type="exit", direction="left", fadetime=2,block=false)]
[characteraction(name="left", type="exit", direction="right", fadetime=2,block=false)]
[delay(time=2)]
[Character]
[Character(name="char_440_Pinecone", name2="avg_npc_

... (全文12895字符)
```

### level_act15d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]罗宾并不是职业杀手吗？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]不是。
[name="赫默"]这一点就连我都看得出来，她身上并没有那种感觉。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]看来有关她的资料是正确的，她过去确实是做安保工作的，在身手上应当是可以信赖的。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]不过这样的话，感觉稍微有些奇怪呢......
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#4",focus=1)]
[name="赫默"]什么？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]就是她为什么会被雇佣这一点......倒也不是什么大问题，先略过吧。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]比起这个，看来大部分杀手都是和罗宾一样，是被单独雇佣的。
[name="缪尔赛思"]他们并不知道自己有没有竞争对手，也不知道自己的雇主是谁。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......海德兄弟究竟雇佣了多少杀手？
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]我也不清楚。
[name="缪尔赛思"]但是正如我之前所说，他们两个为了除掉安东尼可是下了血本的。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]杀手是怎么进入监狱的？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]我想你事先肯定也调查过——曼斯菲尔德监狱是那个州几座城市的政府共同建立的一座监狱，所有大州独此一份。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]嗯。我看到的说法是，这座监狱建立的初衷是因为那个州作为开拓区，虽然发展很快，但是犯罪率一直居高不下，有许多罪犯。
[name="赫默"]当时，这座监狱只是一个接近荒废的工业平台。
[name="赫默"]而伦道尔，也就是现在的典狱长站了出来，提议各城政府建立了这座监狱，一举解决了这座工业平台的处置问题和囚犯的收容问题。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]这有什么问题？
[dialog]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4, crossfade=1)]
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]答案不是很明显了吗？
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]这也就意味着，这座监狱其实是专门用来关押一些“麻烦”的人的地方，而且是各个城市都不是很想管的那种人。
[name="缪尔赛思"]主动想要进入这样的地方其实并不是很麻烦的事情。
[name="缪尔赛思"]卡夫卡小姐应该没有对你说过她具体是怎么进入监狱的吧？
[Character(name="char_108_silent_1#3")]
[name="赫默"]......
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]当然，这座监狱戒备还是非常森严的，想要逃出来非常的困难。
[name="缪尔赛思"]刚才也说过了，它除了每隔几个月会前往周边都市之外，平时基本上是停在荒野上的。
[name="缪尔赛思"]囚犯就算逃出了监狱，面对的也是一望无际的荒野。
[name="缪尔赛思"]你看，罗宾也提到了，神秘人向她许诺过，一定有办法把他们给捞出来。
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]这样他们如果没有在监狱中做一些蠢事提前把自己弄死，并且成功刺杀安东尼，只需要等着被捞出去就行了。
[Character(name="char_108_silent_1#4")]
[name="赫默"]但是他们送去了许多其他杀手，海德兄弟会把他们每一个都捞出去吗？
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]当然不会。
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]所以我才说每个杀手都互相不知道有对方的存在呀。
[name="缪尔赛思"]而一旦进入监狱后，即使知道了有这么一回事，因为逃不掉，能做的也只有拼死杀掉安东尼。
[name="缪尔赛思"]是一种简单有效的手段呢。
[Character(name="char_108_silent_1#3")]
[name="赫默"]......
[name="赫默"]但我还是不明白，为什么？
[name="赫默"]西蒙公司已经倒闭，核心成员全都在监狱里服刑，海德兄弟没有对他们下手，为什么偏偏要对一个安东尼下手？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#3",focus=2)]
[name="缪尔赛思"]......诶，难道我要从这里开始解释吗？
[delay(time=0.7)]
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#3",focus=1)]
[name="赫默"]什么意思？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]好吧，赫默小姐，现在我是真的相信你过去对这方面毫不敏感了。
[name="缪尔赛思"]不过，或许正是因为你不了解，你才会莽撞地做出这样的事，并且成功了。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#4",focus=1)]
[name="赫默"]......
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]抱歉抱歉，我并没有嘲讽你的意思，倒不如说，你甚至可以认为我在夸奖你。
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]那么关于你的问题，首先，我要反问你一个问题——
[name="缪尔赛思"]赫默小姐，你有没有想过，如果要在监狱里除掉安东尼的话，其实杀手是一种最没有效率的手段？
[Character(name="char_108_silent_1#4")]
[name="赫默"]......没有。
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]因为明显还有更有效率的手段，比如买通狱警，或者贿赂典狱长......
[name="缪尔赛思"]而送杀手扮成囚犯进入监狱刺杀另一个囚犯，这听起来就很蠢，不是吗？
[Character(name="char_108_silent_1#3")]
[name="赫默"]因为他们......做不到？
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]没错，因为他们做不到。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]哎呀，从你刚才对这座监狱的历史的反应来看，我要从头给赫默小姐你解释这方面的东西了。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]什么意思？
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]你还记得卡夫卡的回忆中那个监狱队长巴顿说的话吗？
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.1,fadetime=1)]
[Character(name="avg_npc_135")]
[Background(image="bg_undergroundF",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[delay(time=0.51)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="巴顿"]我们州立曼斯菲尔德监狱，可是首都特批的试点监狱，将来是要作为榜样推广给其他州的。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[delay(time=0.51)]
[musicvolume(volume=0.4,fadetime=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]他说的怎么了？
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]试点，特批，你知道这意味着什么吗？
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#4",focus=1)]
[name="赫默"]什么？
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]意味着生意。
[delay(time=0.7)]
[Character(name="char_108_silent_1#2")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="赫默"]......？！
[Character(name="

... (全文19353字符)
```

### level_act15d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cellroomC",screenadapt="coverall")]
[playMusic(key="$chasing_loop",fadetime=0.5, volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Dialog]
[Character(name="avg_npc_133",fadetime=0.6)]
[characteraction(name="middle", type="jump", xpos=0, power=5, times=5, fadetime=1.5)]
[PlaySound(key="$rungeneral", volume=1)]
[delay(time=1)]
[name="B区囚犯B"]......
[Dialog]
[characteraction(name="middle", type="jump", xpos=-350, times=1, fadetime=0.5, block=false)]
[Character(name="avg_npc_133",name2="avg_npc_132")]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=0, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[delay(time=1)]
[name="B区囚犯B"]哼！
[Dialog]
[characteraction(name="left", type="jump",power=50, xpos=300,times=1,fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-150, power=50, times=1, fadetime=0.5,block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=false)]
[characteraction(name="right", type="exit", direction="right",block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=false)]
[Character(name="avg_npc_133")]
[delay(time=1)]
[name="B区囚犯B"]！
[characteraction(name="middle", type="jump", xpos=350, times=1, fadetime=0.5, block=false)]
[Character(name="avg_npc_132",name2="avg_npc_133")]
[delay(time=1)]
[Dialog]
[characteraction(name="right", type="jump", xpos=-100, power=0, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="right", type="jump", xpos=100, power=0, times=1, fadetime=0.1,block=true)]
[characteraction(name="right", type="jump", xpos=-100, power=0, times=1, fadetime=0.1,block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="right", type="jump", xpos=100, power=0, times=1, fadetime=0.1,block=true)]
[characteraction(name="right", type="jump", xpos=-100, power=0, times=1, fadetime=0.1,block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=false)]
[characteraction(name="right", type="jump", xpos=100, power=50, times=1, fadetime=0.3,block=true)]
[delay(time=1)]
[name="A区囚犯"]呃啊......
[Character(name="char_empty",name2="avg_npc_133",fadetime=0.6)]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[Dialog]
[delay(time=1.5)]
[Character]
[delay(time=1)]
[Character(name="char_451_robin#2")]
[name="罗宾"]（这个囚犯好强！其他囚犯都被他几下就放倒了。）
[Dialog]
[Character]
[delay(time=0.7)]
[Character(name="avg_npc_133",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4)]
[delay(time=1)]
[name="B区囚犯B"]......去死。
[characteraction(name="left", type="jump", xpos=100, power=0, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, times=1, fadetime=1,block=true)]
[dialog]
[Delay(time=1)]
[name="狱警B"]......
[Character(name="char_451_robin#2")]
[name="罗宾"]（这个狱警也很厉害，但是，她为什么好像只是在防守......）
[dialog]
[Character(name="avg_npc_133",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4)]
[delay(time=1)]
[name="B区囚犯B"]喝！
[characteraction(name="left", type="jump", xpos=100, power=0, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, times=1, fadetime=1,block=true)]
[dialog]
[Delay(time=1)]
[name="狱警B"]......唔。
[Character(name="avg_npc_133",name2="char_empty",fadetime=1)]
[dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=true)]
[delay(time=1.5)]
[Character(name="char_451_robin#2")]
[name="罗宾"]（糟了，狱警倒下了.....）
[name="罗宾"]（只剩下我了，但是要是我在这里和他战斗的话，之后要怎么解释。）
[Character(name="avg_npc_133")]
[name="B区囚犯B"]......还有你。
[Character(name="avg_npc_133",name2="char_451_robin#2",focus=2)]
[name="罗宾"]（怎么办，难道只能动手了吗。）
[Character(name="avg_npc_133",name2="char_451_robin#2",focus=1)]
[name="B区囚犯B"]......
[Character]
[name="安东尼"]哼。
[Dialog]
[delay(time=1)]
[Character(name="avg_npc_133",name2="char_451_robin#3")]
[delay(time=1)]
[PlaySound(key="$atkboost", volume=1,block=false)]
[Character(name="avg_npc_133",name2="char_264_Mountain_1#4",fadetime=0.2)]
[delay(time=0.6)]
[Character(name="avg_npc_133",name2="char_empty",fadetime=0.2)]
[delay(t

... (全文22214字符)
```

### level_act15d0_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_108_silent_1#3",name2="char_empty")]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=2)]
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]赫默，你没事吧？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]没事。
[Character(name="char_108_silent_1#1",name2="char_242_mayer#2",focus=1)]
[name="赫默"]你怎么过来了？
[Character(name="char_108_silent_1#1",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]我看你在这边呆了很久，就过来看看。
[Character(name="char_108_silent_1#1",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]咦，你身边的酒瓶......难道你喝酒了？
[Character(name="char_108_silent_1#1",name2="char_242_mayer#1",focus=1)]
[name="赫默"]就一点。
[Character(name="char_108_silent_1#4",name2="char_242_mayer#1",focus=1)]
[name="赫默"]缪尔赛思主任呢？
[Character(name="char_108_silent_1#4",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]她还在那边等我们。
[Character(name="char_108_silent_1#4",name2="char_242_mayer#1",focus=1)]
[name="赫默"]你和她说到哪里了？
[Character(name="char_108_silent_1#4",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]说到安东尼希望卡夫卡帮助他，她还和我说了一些有关总辖和塞雷娅的事。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]是吗。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]要我说给你听吗？
[Character(name="char_108_silent_1#1",name2="char_242_mayer#2",focus=1)]
[name="赫默"]不，暂时不用了。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]你好像很难过的样子，刚才缪尔赛思主任对你说了什么不好的东西吗？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=1)]
[name="赫默"]不是......虽然也是。
[name="赫默"]我......说不清楚。
[name="赫默"]我现在思维有些混乱，我有些后悔，感觉自己或许做了一些自己不擅长的事。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]你是指做这件事吗？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]是的。
[name="赫默"]......我应该向你道歉，梅尔。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]为什么？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]我不该把你卷进来的，是我太胆小了，才忍不住把这件事告诉你，让你和我一起承担。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]诶，我是没什么关系的啦。能被赫默你信任我还蛮开心的。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]而且反正我实际做的事也就是陪你回哥伦比亚转了一圈。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]......其实，有一件事我一直没有告诉你。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]是什么？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]这件事的背后，海德兄弟的背后，是能量科。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#3",focus=2)]
[name="梅尔"]诶？是能量科吗？！
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]因为你们工程科和能量科关系很紧密，所以我一直不知道该怎么告诉你。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]哦......嗯，其实也还好啦，我们科虽然事务上和能量科确实关系相当紧密，不过我其实也没有多喜欢能量科。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]不如说我还挺怕能量科主任那个人的......
[Character(name="char_108_silent_1#4",name2="char_242_mayer#2",focus=1)]
[name="赫默"]能量科的主任，是个什么样的人？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]嗯，虽然我也没见过几次啦，不过他有时候会来我们这边看看，也会旁听我们的会议。
[name="梅尔"]虽然他一说话就能感觉到是个很厉害很聪明的人，不过感觉有些......
[name="梅尔"]我不知道该怎么说，就是他更在乎我们的东西能用来做什么，能换来什么之类的。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=1)]
[name="赫默"]原来如此......
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]而且，塞雷娅引咎辞职后，我们科和能量科感觉联系也更加密切了起来。
[name="梅尔"]有的时候会有一些奇怪的工作安排下来，我都做不了自己的事情了。
[name="梅尔"]所以就找了个机会外派来罗德岛了。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]虽然可露希尔也是个怪人，不过在罗德岛工作还蛮开心的。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]是吗......
[Character(name="char_108_silent_1#3",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]总之你不用太在意啦，赫默。而且，我感觉你做了一件好事，不是吗？
[Character(name="char_108_silent_1#3")]
[name="赫默"]好事......
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[musicvolume(volume=0.2, fadetime=1)]
[Character(name="char_003_kalts_1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[name="凯尔希"]你提供的这些情报和分析非常有价值，让我不得不重视你的意见，赫默干员。
[Character(name="char_108_silent_1#5")]
[name="赫默"]那么......
[Character(name="char_003_kalts_1")]
[name="凯尔希"]但首先，这些情报的来源明显是莱茵生命内部。擅自将内部情报泄露给他人的人，恕我无法信任。
[name="凯尔希"]不过，从你的日常表现来看，我也相信你并非如此不谨慎的人，所以我需要一个解释。
[Character(name="char_108_silent_1#5")]
[name="赫默"]这些是我用个人渠道搜集并分析得出的情报，和莱茵生命没有直接的关系。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]但既然你发现了这样的事，应当交由你们内部处理，罗德岛绝无法成为这件事的仲裁者。
[Character(name="char_108_silent_1#4")]
[name="赫默"]......不，我并不期望罗德岛能成为仲裁者。
[name="赫默"]我只是想要帮助这个人，想要请教你的意见。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]为什么是我？或者说，为什么是罗德岛？
[Character(name="char_108_silent_1#4")]
[name="赫默"]现在的我，比起莱茵生命，更相信罗德岛。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]你怀疑莱茵生命的什么？
[Character(name="char_108_silent_1#3")]
[name="赫默"]我不知道，我甚至不知道我在怀疑什么。
[name="赫默"]但我来到这里工作也有很长一段时间了，我亲眼看到了罗德岛在做的事，我至少知道罗德岛在做什么。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]所见未必即所得，赫默干员。
[name="凯尔希"]而且，或许你没有发现，不过从你的情报来看，这名叫安东尼的菲林很有可能是经他父亲安排才在跨州后立刻被捕的。
[name="凯尔希"]这很可能是他们早就布下的局。
[Character(name="char_108_silent_1#4")]
[name="赫默"]但安东尼直到今天都没有出狱，他已经在那座监狱待了六年，而且可能永远也出不去。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]你为什么要执着于这样一个与你无关的人？
[C

... (全文14798字符)
```

### level_act15d0_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2")]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]所以，和卡夫卡的认识有什么问题吗？
[Character(name="char_108_silent_1#4",name2="char_242_mayer#2",focus=1)]
[name="赫默"]不，不是和卡夫卡的认识有问题。而是......
[name="赫默"]和卡夫卡认识之后，我一直希望她能够过上正常的生活，不要再做以前那些见不得光的事情。
[name="赫默"]我给她介绍了一些我能介绍的工作，甚至想要让她成为莱茵生命的一员，虽然最后失败了。
[name="赫默"]但无论如何，我始终希望卡夫卡能够过上更好的生活，我希望她变好。而这个好，是以我在莱茵生命的生活作为标准的。
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]嗯......我觉得在莱茵生命的生活确实还不赖呀？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]前提是我们不知道自己在做什么。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]可是作为科研工作者，我们不是应该非常清楚自己在做什么吗？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=1)]
[name="赫默"]不，我不是指科研上的目的，而是那背后的东西。
[name="赫默"]我们的研究如果真的成功会带来什么影响；我们的成果会被用来做什么；这是不是现在的我们应该研究的东西。
[name="赫默"]在“炎魔”之后，公司内部发生的一些事情让我开始考虑这个问题。
[name="赫默"]我像你，像大部分同事一样，认为我们的研究是正确的，我们的方向是理想的。
[Character(name="char_108_silent_1#4",name2="char_242_mayer#1",focus=1)]
[name="赫默"]但真的是这样吗？
[name="赫默"]伊芙利特让我对这些事情产生了怀疑。
[name="赫默"]这种怀疑促使我暂时离开了莱茵生命，前往了罗德岛。
[Character(name="char_108_silent_1#4",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]原来赫默你一直在想这样的事情啊......
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]在罗德岛的时间里，我一方面在进行科研工作，另一方面，我开始关注起过去没有在意过的一些数据。
[name="赫默"]这些数据是老师给我的，我以前并不明白他将一些公司和地方的数据交给我是为了什么，我也都丢在了一边。
[name="赫默"]但是随着对这些数据的分析和研究，我才发现了其中存在着各种各样的问题。
[name="赫默"]第一次发现其中问题的那一天，我彻夜未眠。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]你是指和安东尼有关的事情吗？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]不，安东尼，或者说西蒙公司的事只是其中一部分，甚至只是一小部分。
[name="赫默"]还有很多一样的事情在发生着，不只是在莱茵生命，是在哥伦比亚之中发生着。
[name="赫默"]那时我才真正意识到，我对莱茵生命这家公司，对哥伦比亚这个国家都了解得太少了。
[name="赫默"]但我不甘心，我不觉得发生在伊芙利特身上的事，发生在安东尼身上的事应该是正常的。
[name="赫默"]所以我才会想要插手安东尼这件事。
[name="赫默"]但是，我或许步子迈得太大了。
[name="赫默"]我现在的感觉和那一天一样，塞雷娅从试验场地将昏迷的伊芙利特抱出来时，仿佛被人从头浇了一盆冰水。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]那次实验究竟发生了什么？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=1)]
[name="赫默"]我不知道。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]诶？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]我一直以为我知道我在做什么，但我现在才发现，我其实不知道。
[name="赫默"]我只知道，我绝不能让伊芙利特再被那样对待。
[name="赫默"]这可能，是我现在唯一能够坚持的事情了。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#1",focus=2)]
[name="梅尔"]......赫默，你有些醉了，我去给你倒点醒酒茶吧。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]嗯......
[Dialog]
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2")]
[Delay(time=0.8)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=50, fadetime=2, block=false)]
[Character(name="char_108_silent_1#3",name2="char_empty")]
[Delay(time=2)]
[Character(name="char_242_mayer#1")]
[name="梅尔"]对不起，赫默，我不知道怎么安慰你。
[Character(name="char_108_silent_1#1")]
[name="赫默"]这不怪你，梅尔。
[Character(name="char_108_silent_1#3")]
[name="赫默"]我只怪我自己过去太无知了。
[Character(name="char_242_mayer#2")]
[name="梅尔"]我觉得赫默你已经知道得很多了，只是大家都有不擅长的领域。
[Character(name="char_108_silent_1#3")]
[name="赫默"]但是，梅尔，我是真的不甘心。
[name="赫默"]如果我能知道得更多一些，如果我能知道得更早一些，或许事情不会变成现在这样。
[Character(name="char_242_mayer#2")]
[name="梅尔"]但是现在开始知道也来得及呀。
[name="梅尔"]我觉得缪尔赛思主任应该也觉得你挺厉害的。
[name="梅尔"]我说实话哦，赫默。
[Character(name="char_108_silent_1#5")]
[name="赫默"]你说。
[Character(name="char_242_mayer#2")]
[name="梅尔"]我感觉赫默你现在有些像我一些同事。
[name="梅尔"]就是在知道了一些新的知识后，就觉得自己过去学的一点用都没有，然后开始哀叹自己为什么没有早点遇上这门学问。
[name="梅尔"]不是说这样就不对啦，但是我觉得这样就很没意思，难道以前努力过的东西真的就没用了吗？新的东西就一定好吗？
[name="梅尔"]如果它真的好，如果真的觉得它有用，那么用和以前一样的努力去学习它不就好了，没有什么好着急的。
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_108_silent_1#5",name2="char_empty")]
[characteraction(name="right", type="move", xpos=50, fadetime=0.6, block=false)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=-50, fadetime=2, block=false)]
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2")]
[Delay(time=2)]
[Character(name="char_108_silent_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]来，喝了这杯醒酒茶。
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]不是你说的那样，这些事情和学问不一样......
[name="赫默"]但是，但是你说的也有道理，确实......
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]哎呀，算了，我来喂你喝吧，真是的，赫默你酒量不行呀。
[Dialog]
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2")]
[delay(time=1)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=0.5, block=true)]
[characteraction(name="right", type="move", xpos=-80, fadetime=0.6, block=false)]
[Subtitle(text="梅尔将几近趴在桌子上的赫默扶了起来，一点一点把醒酒茶喂进了她的嘴里。", x=200, y=360, alignment="center", size=24, delay=0.04, width=900)]
[delay(time=1)]
[Subtitle]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.7)]
[characteraction(name="right", type="move", xpos=80, fadetime=0.6, block=false)]
[delay(time=1)]
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]怎么样，感觉好点没？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]嘶......呼......
[Character(name="char_108_silent_1#1",name2="char_242_mayer#2",focus=1)]
[name="赫默"]好多了，谢谢你，梅尔。
[Character(name="char_108_silent_1#1",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]要是你感觉不好受的话，要不然我们直接回去吧？
[Character(name="char_108_silent_1#3",name2="char_242_mayer#2",focus=1)]
[name="赫默"]......不，还不到那个时候。
[Character(name="char_108_silent_1#4",name2="char

... (全文6664字符)
```

### level_act15d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#4",fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=2)]
[name="赫默"]我回来了。
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]赫默小姐你没事了吗？
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#1",focus=2)]
[name="赫默"]没事，其实或许我要感谢你。
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#1",focus=1)]
[name="缪尔赛思"]为什么？
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#1",focus=2)]
[name="赫默"]没什么。
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#1",focus=1)]
[name="缪尔赛思"]好吧，那么，我们继续？
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#5",focus=2)]
[name="赫默"]你们刚才说到哪里了？
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]说到安东尼对罗宾抛出橄榄枝。
[name="缪尔赛思"]我正在和梅尔小姐讨论安东尼的手段高超呢。
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#5",focus=2)]
[name="赫默"]......我觉得你可能是单纯的想多了。
[name="赫默"]或许，他当时没有想那么多，只是单纯地想要对罗宾付出善意呢？
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]嗯，我确实无法否认这种可能性啦。
[name="缪尔赛思"]不过如果是单纯善良的人，是没有办法在这片大地上活下去的，赫默小姐。
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#5",focus=2)]
[name="赫默"]......算了，我不该和你讨论这个，梅尔说到哪里了？
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]以及卡夫卡和安东尼讨论过后，安东尼终于决定越狱。
[name="缪尔赛思"]说到罗宾在医务室里醒来，被安东尼邀请加入越狱的队伍的部分。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]不得不说，赫默小姐，我确实有些好奇你究竟是从哪里获得安东尼这条线索的情报的了。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#5",focus=2)]
[name="赫默"]从我的老师那里。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]嗯？难道帕尔维斯主任也插手了这件事？
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#3",focus=2)]
[name="赫默"]......不，我已经很久没有和他直接联络过了。
[name="赫默"]而且他恐怕也不知道这件事。
[name="赫默"]自从离开莱茵生命后，我把过去很多从没在意过的情报重新梳理了一遍。
[name="赫默"]而在那之中，我抓到了西蒙家族这条尾巴。
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]哦？
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#4",focus=2)]
[name="赫默"]这个家族覆灭的时间很短，而且一些数据伪装得很好，所以在很多人看来，这些数据就仿佛没有变化过一样。
[name="赫默"]但是伪装总是会有痕迹的。一些报表，一些统计数据，只要详细对比一下，就能发现其中的问题。
[name="赫默"]我原本只是抱着试试的心态过了一遍那些数据，却没想到让我发现了这样的事。
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]只是偶然发现......不，其实是必然吗。
[name="缪尔赛思"]不过，你为什么会突然去梳理一遍那些数据呢？
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#3",focus=2)]
[name="赫默"]因为我开始不信任莱茵生命，也不信任我的老师。
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#3",focus=1)]
[name="缪尔赛思"]是“炎魔”事件吗？
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#4",focus=2)]
[name="赫默"]不，不只是。
[name="赫默"]“炎魔”导致了塞雷娅的离开，在那之后发生的一些事情想必缪尔赛思主任你比我更了解。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]......原来如此。
[name="缪尔赛思"]哎呀，我只是随口问问，就这么告诉我这些事真的好吗？
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#1",focus=2)]
[name="赫默"]这不就是你想听到的东西吗？
[name="赫默"]我不擅长掩饰什么，缪尔赛思主任，所以我思考过后，决定对你坦诚相待。
[name="赫默"]虽然我并不喜欢我的老师，不过他有一句话我一直记得——
[name="赫默"]“对阴谋家来说，最让他们恐惧的是坦诚。”
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#1",focus=1)]
[name="缪尔赛思"]......
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#1",focus=1)]
[name="缪尔赛思"]看来我被当作坏人了呢。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#5",focus=2)]
[name="赫默"]不，在罗德岛生活的时间教会了我一件事，那就是，不是所有反对你的就应该被当作坏人。
[name="赫默"]我想，你不是坏人......塞雷娅也不是。
[name="赫默"]只能说，我和你，和塞雷娅都无法互相理解。
[Character(name="char_249_muesys_1#6",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]......啊哈，或许吧。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#5",focus=2)]
[name="赫默"]缪尔赛思主任，你还要继续听吗？
[Character(name="char_249_muesys_1#1",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]当然，我正听到精彩的部分呢。
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#5",focus=1)]
[name="缪尔赛思"]哎呀，不过故事应该差不多到这里就接近尾声了吧？
[name="缪尔赛思"]也就是说，在那时，安东尼逃狱的队伍就已经差不多结成了吧？
[name="缪尔赛思"]安东尼本人，入殓师杜玛，卡夫卡，临时工米娜。
[name="缪尔赛思"]再加上罗宾，就可以大家一起齐心协力越狱了吧？
[Character(name="char_249_muesys_1#5",name2="char_108_silent_1#4",focus=2)]
[name="赫默"]不，没有这么简单。
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]诶？
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=2)]
[name="赫默"]罗宾并没有加入安东尼的队伍。
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]诶？
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=2)]
[name="赫默"]虽然确实在这之后，卡夫卡就开始和杜玛还有安东尼一起摸索越狱的方法，而且罗宾也加入了其中。
[name="赫默"]但是事情并没有这么简单。
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]发生了什么吗？
[Character(name="char_249_muesys_1#3",name2="char_108_silent_1#4",focus=2)]
[name="赫默"]还记得你之前提到的海德兄弟找来的帮手吗？
[Character(name="char_249_muesys_1#4",name2="char_108_silent_1#4",focus=1)]
[name="缪尔赛思"]记得，他怎么了？
[Character(name="char_108_silent_1#4")]
[name="赫默"]他找到了罗宾。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Character]
[Image]
```

### level_act15d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Dialog]
[stopmusic]
[Character]
[Background(image="bg_cellroomA",screenadapt="coverall")]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="char_451_robin#6")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[name="罗宾"]我究竟该怎么做......
[Character(name="avg_npc_137#9",blackstart2=0.13,blackend2=0.25)]
[name="狱警"]咳咳。
[Character(name="char_451_robin#3",name2="avg_npc_137#9",blackstart2=0.13,blackend2=0.25,focus=1)]
[name="罗宾"]有什么事吗，长官？
[Character(name="char_451_robin#3",name2="avg_npc_137#5",blackstart2=0.13,blackend2=0.25,focus=2)]
[name="狱警"]啊，罗宾小姐，我一直想见你。
[stopmusic]
[name="狱警"]想必你现在正在犹豫究竟是要继续自己的刺杀，还是协助安东尼的越狱吧？
[Dialog]
[Delay(time=1)]
[playMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Character(name="char_451_robin#2",name2="avg_npc_137#9",blackstart2=0.13,blackend2=0.25,focus=1)]
[name="罗宾"]......你是谁？！
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=2)]
[name="狱警"]我的名字是杰斯顿，罗宾小姐。
[Character(name="char_451_robin#2",name2="avg_npc_137#6",focus=2)]
[name="杰斯顿"]别紧张，我和你一样，是接受委托潜入监狱刺杀安东尼的杀手之一。
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]而我恰好偶然听到了安东尼先生对你发出的越狱邀请......
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]......？！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.2,fadetime=0.5)]
[Character(name="avg_npc_137#9")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="bg_Morgue",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_137#9")]
[name="狱警"]安东尼先生，巴顿队长让我问你受的伤重不重。
[Character(name="char_264_Mountain_1#5")]
[name="安东尼"]......不重，让他再等一会儿，马上就好。
[Character(name="avg_npc_137#9")]
[name="狱警"]好的，好的，没有问题。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="char_451_robin#2")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_cellroomA",screenadapt="coverall")]
[musicvolume(volume=0.4,fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="罗宾"]你是那个时候的狱警？！
[Character(name="char_451_robin#2",name2="avg_npc_137#5",focus=2)]
[name="杰斯顿"]啊，看来你记起我来了，太好了，我自认还是挺容易被记住的。
[name="杰斯顿"]要是被你遗忘的话，我会感到悲伤的。
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]你，你一直在那听？
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]呵呵，毕竟是我把你们这些昏迷过去的囚犯送过来的。
[name="杰斯顿"]虽然安东尼先生即使在他的“安全屋”里也压低了音量，不过对于我这样的有心人来说，还是非常容易听到的。
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]你想要干什么？
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]我是来向你提出交易的，罗宾小姐。
[Character(name="char_451_robin#3",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]交易？
[Character(name="char_451_robin#3",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]没错。
[name="杰斯顿"]不得不说，安东尼先生这一手确实值得称道。
[name="杰斯顿"]表面上是向你伸出橄榄枝，其实无论你接或者不接，对他来说都没有损害。
[name="杰斯顿"]漂亮，即使是我也忍不住想夸赞他一番。
[Character(name="char_451_robin#3",name2="avg_npc_137#6",focus=2)]
[name="杰斯顿"]很可惜，他不了解你的身份。
[name="杰斯顿"]否则，他恐怕是要斟酌一番的。
[Character(name="char_451_robin#3",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]我的身份？
[Character(name="char_451_robin#3",name2="avg_npc_137#5",focus=2)]
[name="杰斯顿"]没错，而你，罗宾小姐，你也没有察觉到你和安东尼先生之间，事实上存在的联系。
[Character(name="char_451_robin#2",name2="avg_npc_137#5",focus=1)]
[name="罗宾"]你究竟在说什么？
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]罗宾小姐，你还记得你父亲过去意气风发之时，曾经任职的公司名称吗？
[Character(name="char_451_robin#3",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]黑云。
[Character(name="char_451_robin#3",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]没错，黑云贸易有限公司。
[name="杰斯顿"]你的父亲是那里的总经理，但就在他事业最巅峰的时候，黑云贸易却突然倒闭。
[name="杰斯顿"]在那之后，他无论怎么努力，事业都没有起色，于是从此一蹶不振，开始酗酒，直到今天，躺在医院的病床上等待手术的医药费。
[Character(name="char_451_robin#6",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]......
[Character(name="char_451_robin#6",name2="avg_npc_137#9",focus=2)]
[name="杰斯顿"]那么你知道是谁让黑云贸易倒闭的吗？
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]难道是......
[Character(name="avg_npc_137#6")]
[name="杰斯顿"]没错，正是西蒙家族，而安东尼先生引以为傲的姓氏，也正是西蒙。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]当然，为了表达我的诚意，我来告诉你全貌。
[Character(name="avg_npc_137#6")]
[name="杰斯顿"]简单来说，在六年前，西蒙家族和海德兄弟在为某一样东西竞争。
[name="杰斯顿"]双方都想吞并对方，并且双方的实力也相近，于是明争暗斗逐渐升级，终于到了见血的时候。
[name="杰斯顿"]而最终，是海德兄弟抢先一步，将西蒙家族整个覆灭。
[name="杰斯顿"]西蒙家族的族长，史密斯·西蒙危难之际，决定将唯一的儿子安东尼·西蒙送到别的城市。
[name="杰斯顿"]然而，在逃到铸铁城后，可怜的小安东尼还是被捕了。
[name="杰斯顿"]幸运的是，在铸铁城所属的州法律中，对逃犯的审判是在本州进行的。
[name="杰斯顿"]也就是说，他没有被移送回堡垒山城，并在审判之后，他按照本州法律，被关进了这座州立曼斯菲尔德监狱。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]不得不说，我甚至认为老史密斯早就算到了这一点，是故意让安东尼在铸铁城被捕的。
[name="杰斯顿"]毕竟实际上，正因安东尼没有回到遍布海德兄弟势力的堡垒山城，他才安全了。
[Character(name="char_451_robin#2",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]这和我爸爸的事又有什么关系？
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]当然有。
[name="杰斯顿"]我刚才说了，西蒙家族当时可是和海德兄弟是竞争关系，即使棋差一招，他们临死前也是有能力反咬一口的。
[name="杰斯顿"]而他们反咬一口的对象之中，就有你父亲的公司——黑云贸易。
[name="杰斯顿"]当时，你的父亲是海德兄弟最得力的手下之一，黑云贸易的业绩也十分出色。
[name="杰斯顿"]但就像西蒙家族一夜之间蒸发一般，黑云贸易在西蒙家族的垂死挣扎之下，也一夜之间消失了。
[Character(name="char_451_robin#6",name2="avg_npc_137#9",focus=1)]
[name="罗宾"]......
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]你的父亲当然想要东山再起，但是他的竞争对手们会给他机会吗？
[name="杰斯顿"]不，不会的。
[Character(name="avg_npc_137#7")]
[name="杰斯顿"]哥伦比亚的商场，有时候比战场还要血腥。
[name="杰斯顿"]于是，你的父亲在那之后，就再也没有站起来过。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]也就是说，我必须要承认，安东尼先生想要越狱出去找海德兄弟寻仇是很正常的事。
[name="杰斯顿"]但是你呢，罗宾小姐？
[name="杰斯顿"]我们确实可以假设，如果没有海德兄弟先消灭西蒙家族，那么西蒙家族就不至于垂危挣扎让你父亲的黑云贸易倒闭。
[name="杰斯顿"]我们也可以假设，如果是西蒙家族先一步解决了海德兄弟，那么以史密斯•西蒙在当年展现出的远高于海德兄弟的胸怀。
[name="杰斯顿"]他也确实很有可能会以更和平的方式处理海德兄弟手下的那些企业。
[Character(name="avg_npc_137#7")]
[name="杰斯顿"]但是一切没有如果。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]现在的结果就是——是西蒙家族导致了你父亲的黑云贸易的覆灭。
[name="杰斯顿"]而你刺杀的对象，安东尼•西蒙，正是这个家族最后的幸存者。
[Character(name="char_451

... (全文9027字符)
```

### level_act15d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1")]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#3",focus=2)]
[name="缪尔赛思"]难怪赫默小姐你说罗宾虽然加入了越狱的队伍却没有那么简单。
[name="缪尔赛思"]看来是她被杰斯顿说服了，是作为卧底加入了安东尼一方吧。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1",focus=1)]
[name="赫默"]嗯。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]......原本我以为这个故事到这里应该不会再有什么让我吃惊的事情发生了。
[name="缪尔赛思"]罗宾居然有这样的身世，这可是连我看到的情报上都没提到的事。
[name="缪尔赛思"]而且杰斯顿这个人，虽然有过耳闻，也是意外的棘手呢......
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=1)]
[name="赫默"]你知道他？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]嗯。
[name="缪尔赛思"]他是沙滩伞公司的王牌打手之一，据说只要有钱就能请动，是海德兄弟这次最大的底牌。
[name="缪尔赛思"]虽然有品位高雅的评价，不过更多都是觉得这个人相当的讨厌。
[name="缪尔赛思"]原本以为只是个普通的打手，没想到脑子也很清醒。
[name="缪尔赛思"]我只知道他是海德兄弟的底牌，却没想到他居然在这个时候就果断下场了。
[name="缪尔赛思"]看似给出了选择，其实几乎是没有选择的。
[name="缪尔赛思"]毕竟确实如他所说，他掌握了安东尼没有掌握的有关罗宾身世的信息。
[name="缪尔赛思"]而且他甚至在安东尼不知道的时候已经观察了他很久，那么他确实就占了主动权。
[name="缪尔赛思"]换做是我，面对这样的处境，于情于理，也会选择协助他了
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]。
[name="赫默"]......确实。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1",focus=2)]
[name="缪尔赛思"]哎呀，我还以为赫默小姐你会反驳我呢。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1",focus=1)]
[name="赫默"]......我并不认同他的一些想法，也不喜欢他这个人。
[name="赫默"]但我认为他对罗宾说的话，至少比三番五次试探我的缪尔赛思主任你要来得真诚。
[name="赫默"]你这种认为已经完全了解我的语气就像我的老师一样令人反感，缪尔赛思主任。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#2",focus=2)]
[name="缪尔赛思"]看来说得有些过火了呢，我道歉，对不起。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]老实说，就算是我也觉得，这家伙稍微有些无聊呢。
[name="缪尔赛思"]罗宾这样和安东尼有这一层纠葛的人，不特意去找肯定是找不到。
[name="缪尔赛思"]而且还特意将她引入局......
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=2)]
[name="缪尔赛思"]算了，无论如何，到这里为止，越狱的队伍应该算是结成了吧。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1",focus=1)]
[name="赫默"]......嗯。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=2)]
[name="缪尔赛思"]一个圆滑的情报通，一个身手不错的打手，一个能在监狱里自由走动的临时工，一个在那里待了很久的入殓师，还有一个优秀的首领......
[name="缪尔赛思"]各方面来说都是相当出色的队伍呢。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=1)]
[name="赫默"]嗯，总的来说，越狱的准备在那之后，基本就进入了比较有条不紊的筹备阶段。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]在这期间有发生什么事吗？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......除了刺杀，似乎没有。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=2)]
[name="缪尔赛思"]对哦，差点忘了，刺杀还在继续吧？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=1)]
[name="赫默"]嗯，但是因为狱警们除了仔细排查囚犯也确实想不出什么办法，而且这些杀手只针对安东尼，最后，他们干脆放弃了去解决这件事。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=2)]
[name="缪尔赛思"]啊哈，真有他们的作风。
[Character(name="char_242_mayer#2")]
[name="梅尔"]啊，我想到罗宾提到的一件事。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1",focus=1)]
[name="赫默"]是什么？
[Character(name="char_242_mayer#2")]
[name="梅尔"]就是说服杜玛也和他们一起离开的这件事呀。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#3",focus=2)]
[name="缪尔赛思"]咦，这是怎么回事？杜玛不是队伍中的一员吗？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#3",focus=1)]
[name="赫默"]哦，对了，他们到后来才知道，杜玛虽然说要协助安东尼越狱，但其实自己并没有离开的意思。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#3",focus=2)]
[name="缪尔赛思"]为什么？
[Character(name="char_242_mayer#2")]
[name="梅尔"]因为她从来没有离开过这座监狱。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Character(name="char_441_lotus_1#4", name2="char_451_robin#3")]
[Background(image="bg_Morgue",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_441_lotus_1#4", name2="char_451_robin#3",focus=2)]
[name="罗宾"]诶？
[Character(name="char_441_lotus_1#4", name2="char_451_robin#3",focus=1)]
[name="杜玛"]是的，我其实不打算跟你们离开。
[Character(name="char_441_lotus_1#4", name2="char_451_robin#3",focus=2)]
[name="罗宾"]为什么？难道你喜欢这座监狱吗？
[Character(name="char_441_lotus_1#3", name2="char_451_robin#3",focus=1)]
[name="杜玛"]不，我不喜欢这里，一点也不喜欢。
[name="杜玛"]我是被上一代的入殓师在监狱某一次停靠时捡来的，从我有记忆起，我就在这座监狱里长大。
[name="杜玛"]狱警们的刻薄，囚犯们之间的仇恨、恶意、暴力，还有死亡。除此之外，我再也没见过别的东西。
[name="杜玛"]我也偶尔会在停靠的时候出去走走，但是我能感觉到，我并不属于那里。
[name="杜玛"]我......害怕。
[Character(name="char_441_lotus_1#3", name2="char_451_robin#3",focus=2)]
[name="罗宾"]那你为什么要帮安东尼越狱呢？
[Dialog]
[Character]
[Delay(time=0.5)]
[Character(name="char_441_lotus_1#1")]
[name="杜玛"]因为安东尼是我唯一的朋友。
[Delay(time=1)]
[name="杜玛"]直到安东尼来到这里，我才知道，这片大地上还有他这样的人。
[name="杜玛"]他虽然也会和别人打斗，但他懂得克制。
[name="杜玛"]他虽然也会愤怒，但他的愤怒从不会波及别人。
[name="杜玛"]他总是很有礼貌，对谁都很讲道理。
[name="杜玛"]他会给我推荐有趣的书，告诉我外面是怎么样的。
[name="杜玛"]他刚来到监狱时，也偶尔会向我抱怨命运的不公，我在那时就已经有了帮助他出去的想法。
[name="杜玛"]但是我什么都不懂，帮不上他的忙，所以我什么都没有说。
[name="杜玛"]后来，他变得越来越沉稳，其他人也越来越尊敬他，我就又高兴，又有些悲伤。
[Character(name="char_441_lotus_1#3")]
[name="杜玛"]因为他似乎少了一些什么。
[name="杜玛"]而且，我总是觉得，他是不应该被关在这里的，他应该能过上更好的生活才对。
[Character(name="char_441_lotus_1#4")]
[name="杜玛"]所以这一次卡夫卡为他带来了他想要知道的东西，并且让他变得想要离开这里后，我发自内心地为他感到高兴。
[name="杜玛"]只要能帮助他出去，我就心满意足了。
[name="杜玛"]你不要告诉他，其实我已经做好准备了，一旦哪个环节出了差错，我赌上性命也要把这个错补上。
[Character(name="char_451_robin#6")]
[name="罗宾"]......错误。
[Character(name="char_441_lotus_1#4", name2="char_451_robin#6",focus=1)]
[name="杜玛"]怎么了，罗宾，你好像脸色不太好。
[Character(name="char_441_lotus_1#4", name2="char_451_robin#3",focus=2)]
[name="罗宾"]没什么。
[name="罗宾"]我只是在想，你竟然愿意为他做到这个程度吗。
[Character(name="char_441_lotus_1#4", name2="char_451_robin#3",focus=1)]
[name="杜玛"]嗯。
[Character(name="char_441_lotus_1#4",

... (全文7080字符)
```

### level_act15d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_249_muesys_1#4")]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="缪尔赛思"]一个从没长时间离开过监狱这样的地方的人，确实会对外界产生恐惧呢......
[Character(name="char_249_muesys_1#6")]
[name="缪尔赛思"]啊，幸好我知道结局，她也一起出来了，不然我听到这里可要开始着急了。
[name="缪尔赛思"]真是太好了~
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]于是在那之后应该就是筹备越狱的时间了吧？
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#1",focus=1)]
[name="赫默"]没错。
[name="赫默"]安东尼决定越狱时，大概是卡夫卡进入监狱一个半月左右的时候，而后，他们花了一个多月的时间才最终制定好了可实行的越狱计划。
[Character(name="char_108_silent_1#5", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]也就是说，完成制定计划时距离实际越狱的时间还有一个半月了吗。
[name="缪尔赛思"]四个月的时间说短不短，说长倒也确实不长呢。
[Character(name="char_249_muesys_1#6")]
[name="缪尔赛思"]不过，说了这么久，终于到我最感兴趣的部分了。
[dialog]
[PlaySound(key="$g_card_10cardsrelease", volume=1)]
[Delay(time=1)]
[Character(name="char_108_silent_1#5")]
[name="赫默"]......这张图纸是？
[Character(name="char_242_mayer#2")]
[name="梅尔"]啊，我懂了，是监狱的平面图吧！
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]没错~虽然比较粗糙，不过基本上该有的都有了。
[Character(name="char_249_muesys_1#6")]
[name="缪尔赛思"]我最好奇的部分，当然是逃狱的方法啦。
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]虽然队伍中每个人的故事我也挺感兴趣，但是一说到越狱，果然还是越狱本身最激动人心吧~
[Character(name="char_108_silent_1#5")]
[name="赫默"]难道说你想了解整个过程，真的只是因为你对越狱感兴趣？
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]你可以这么认为哦？
[Character(name="char_108_silent_1#5")]
[name="赫默"]......好吧。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac15_3",xScale=1.2, yScale=1.2,y=-50, fadetime=0)]
[imageTween(xFrom=50,xTo=-50,duration=30)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
[name="赫默"]既然要讲，还是从头讲起吧。
[name="赫默"]首先，这座监狱采用了一些移动城市的设计经验，并没有直接基于底盘在上面搭建监狱。
[name="赫默"]它是先仿造现实地貌制造了一块人造山体，并在那之上完成的监狱设计。
[name="赫默"]虽然这在现在已经是相当常见的技术，不过以当时的眼光来看，是相当超前且成功的做法。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$g_card_10cardsrelease", volume=1)]
[Image(image="avg_ac15_5",xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[name="赫默"]那么，监狱的外观先略过不谈。
[name="赫默"]监狱一共三层，每一层的结构都比较类似。
[name="赫默"]每一层左下角的这一块是A区，也就是非感染者牢房区。
[name="赫默"]而右上角的则是B区，感染者牢房区。
[name="赫默"]左上和右下两个角落都是警卫室，里面还有休息的地方，平时狱警通常都在那里活动。
[name="赫默"]而中间的这个黑色的方形就是关押重犯的C区塔。
[dialog]
[Delay(time=1)]
[PlaySound(key="$g_card_10cardsrelease", volume=1)]
[Image(image="avg_ac15_5_3",xScale=1, yScale=1, fadetime=1)]
[name="赫默"]中间这一块是地下工厂，也就是犯人们共同作业的地方。
[name="赫默"]这边是医务室，也就是杜玛的房间，而隔壁就是停尸间。
[name="赫默"]另一边是安东尼提议建立的图书馆。
[name="赫默"]结构大致就是这样。
[name="赫默"]在经过米娜一段时间的摸索后，他们大致掌握了监狱的结构，并想出了一个越狱的方法。
[name="缪尔赛思"]嗯嗯。
[dialog]
[Delay(time=0.6)]
[PlaySound(key="$g_card_10cardsrelease", volume=1)]
[Image(image="avg_ac15_5_2",xScale=1, yScale=1, fadetime=1)]
[Delay(time=0.6)]
[name="赫默"]你看结构可以发现，C区的塔其实并不只是在地面上。
[name="赫默"]它不仅中间有电梯可以通往地下，塔本身其实也是有下沉结构的。
[name="缪尔赛思"]诶诶诶，还有这样的结构啊。
[name="梅尔"]嗯，这样的建筑结构还挺少见的。这么设计的理由应该是为了方便在紧急情况下能够将重犯关在地下，以免他们闹事。
[name="赫默"]嗯，而控制塔下沉的机关，平时需要两个警备室里的机关共同作用才能生效。
[name="缪尔赛思"]啊，我知道了。
[name="缪尔赛思"]我事后得知的一些边角情报里确实提到了塔下沉了这回事，所以他们是在警卫室启动了机关吧？......咦，不对。
[name="缪尔赛思"]就算他们进入了地下，但是地下并没有能够逃出去的地方啊？
[name="赫默"]......首先，他们并没有去警卫室，虽然这确实是最早的方案。
[name="赫默"]但是，他们得知，警卫室的机关只能控制塔以比较缓慢的速度下沉。
[name="赫默"]......安东尼是在一份放在图书馆里的资料上发现的。
[name="赫默"]那份资料应该是建造监狱时遗留的一些设计图，应该是没人在意，所以在安东尼提议建造图书馆后，就干脆被随手放在那里了。
[name="缪尔赛思"]噗。
[name="缪尔赛思"]大概也是觉得没有人能拿这个干什么吧，而且毕竟这座监狱也建造了有二十多年了我记得。
[name="赫默"]二十五年。
[name="赫默"]总之，等待塔缓慢下沉是不行的，狱警们必然已经反应过来了，所以这个方案最终被否决了。
[name="缪尔赛思"]咦？这样的话，那......
[name="赫默"]幸好他们在那份资料上还发现了一样东西，那就是——
[Dialog]
[Image(image="avg_ac15_5_2",xScale=1.7, yScale=1.7,x=100,y=-125, fadetime=1.5)]
[imageTween(xFrom=100, yFrom=-125, xTo=120,duration=15, block=false)]
[Delay(time=0.7)]
[name="赫默"]中间的这座塔顶，你看，这里还有一层不是监狱的房间。
[name="赫默"]事实上，这里才是这座塔，甚至是这座监狱真正的主控室。
[name="缪尔赛思"]主控室......原来如此，在这里可以让塔快速地下沉，对吧？
[name="赫默"]没错。而且还可以控制监狱中的电路，制造一些短暂的混乱。
[name="赫默"]而这一层平时是没有人的，想要进入这一层，需要特殊的电梯钥匙，一般狱警配备的钥匙卡是无法进入这一层的。
[name="缪尔赛思"]我大致明白了，他们通过主控室快速让塔下沉来到了地下，并通过断电给地面上制造了许多混乱。
[name="缪尔赛思"]但是这样还是有一个问题——
[name="缪尔赛思"]然后呢？
[name="缪尔赛思"]难道地下有逃出去的路？
[name="赫默"]有的。
[dialog]
[Delay(time=0.6)]
[PlaySound(key="$g_card_10cardsrelease", volume=1)]
[Image(image="avg_ac15_5_3",xScale=1.7, yScale=1.7,x=-5,y=75, fadetime=1.5)]
[imageTween(xFrom=-5, yFrom=75, xTo=13,duration=15, block=false)]
[Delay(time=0.6)]
[name="赫默"]这条路是杜玛提供的。
[name="赫默"]据她回忆，上一任的入殓师提到过，这座监狱由于没有经验可以参考，所以在山体下其实留了一些被废弃的结构。
[name="赫默"]这之中有一些是能够通往监狱外的地表的。
[name="赫默"]而其中有一条，就相当靠近停尸间。
[name="梅尔"]虽然说很近，其实中间也隔着至少3米的墙体就是了。
[name="缪尔赛思"]难道说是......挖？
[name="赫默"]是的，挖。
[name="赫默"]虽然房间的墙壁都是用钢筋混凝土制成的，但是外面毕竟是泥土。
[name="赫默"]只要能找到比较脆弱的墙壁，打穿后不需要非常先进的工具也能进行挖掘。
[name="赫默"]在不引起怀疑的前提下，他们会轮流来到医务室挖掘地道。
[dialog]
[Image(image="avg_ac15_5_3",xScale=1, yScale=1, fadetime=1.5)]
[Delay(time=0.6)]
[name="缪尔赛思"]咦，这么说来，既然在停尸间挖，那么直接挖好之后离开不行吗？
[name="赫默"]你忘了吗，在没有停靠城市时，即使来到监狱外的地表也没有什么用。
[name="赫默"]而一旦停靠在城市时，狱警们也都会提高警备，囚犯们的自由时间会被极端压缩。
[name="赫默"]即使是安东尼也几乎没有自由时间。
[name="赫默"]直接像平时那样前往医务室是不行的。
[name="缪尔赛思"]也对，诶嘿，我忘了。
[name="赫默"]对了，因为已经停靠城市了，米娜在越狱之前就跟着施工团队离开了，所以她并没有实际参与这次越狱。
[name="赫默"]她是在监狱外和卡夫卡他们汇合的。
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[Character(name="char_108_silent_1#5")]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="赫默"]总之，在最后的一个半月里，他们首先从狱警队长巴顿那里偷来了能够通往塔顶层的钥匙卡。
[name="赫默"]然后终于在下一次停靠前几天，挖通了地道，并且确认确实是可以通往地面的。
[name="赫默"]一切都已经准备就绪。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### level_act15d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_249_muesys_1#1")]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="缪尔赛思"]啊，这下终于到实行越狱的环节了。
[name="缪尔赛思"]感觉整个流程虽然略过了一些事情，但还是比我想象的要复杂许多呢。
[Character(name="char_249_muesys_1#2")]
[name="缪尔赛思"]呼啊，我都有些困了。
[Character(name="char_242_mayer#2")]
[name="梅尔"]我也有一点。
[Character(name="char_242_mayer#4")]
[name="梅尔"]啊，我去给大家泡一杯咖啡吧~
[Character(name="char_108_silent_1#4")]
[name="赫默"]还差一点就结束了。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#2",focus=2)]
[name="缪尔赛思"]我知道我知道。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#6",focus=2)]
[name="缪尔赛思"]不过接下来发生的事我也差不多猜到啦。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]一切准备就绪，只等实行越狱的那一天到来。
[name="缪尔赛思"]但是在实行的那一天，有一个人却忽然失踪了，对吧？
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#1",focus=1)]
[name="赫默"]是的。
[Character(name="char_108_silent_1#4")]
[name="赫默"]他们最终决定在监狱停靠在纽莱堡市期间的某一次进入C区清扫的机会进行越狱。
[name="赫默"]但是在那一天约定的时间，罗宾却没有出现。
[name="赫默"]因为他们不知道，他们的计划早已被在暗处的杰斯顿完全掌握了。
[name="赫默"]而罗宾，早已经在他们的必经之路上等待着他们——
[Dialog]
[Delay(time=1)]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cellroomC",screenadapt="coverall")]
[Character(name="avg_npc_132",name2="char_264_Mountain_1#5")]
[playMusic(intro="$dontmaketrouble_intro", key="$dontmaketrouble_loop", volume=0.4)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_132",name2="char_264_Mountain_1#6")]
[characteraction(name="right", type="jump", xpos=-200, power=0, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="right", type="jump", xpos=200, power=5, times=1, fadetime=1,block=true)]
[Delay(time=1)]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(name="char_empty",name2="char_264_Mountain_1#5",fadetime=0.7)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[Delay(time=1.2)]
[Character(fadetime=0.6)]
[delay(time=0.7)]
[Character(name="char_214_kafka_1#4",name2="avg_npc_133", focus=2)]
[delay(time=1)]
[characteraction(name="left", type="jump", xpos=250, power=0, times=0.8, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=10, vibrato=30, randomness=20, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$p_imp_sword_n", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Delay(time=0.7)]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(name="char_214_kafka_1#4",name2="char_empty",fadetime=0.7)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[characteraction(name="left", type="move", xpos=-250, fadetime=0.9,block=true)]
[Delay(time=0.51)]
[Character(name="char_214_kafka_1#4",name2="char_empty",focus=1)]
[Delay(time=0.51)]
[Character(fadetime=0.6)]
[delay(time=0.7)]
[Character(name="char_empty", name2="char_empty")]
[characteraction(name="left", type="move", xpos=-50,fadetime=0.4, block=true)]
[characteraction(name="right", type="move", xpos=50,fadetime=0.4, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=50, times=1, fadetime=0.5, block=false)]
[characteraction(name="right", type="move", xpos=-50, times=1, fadetime=0.5, block=false)]
[PlaySound(key="$rungeneral", volume=1)]
[PlaySound(key="$rungeneral", volume=0.7,delay=0.4)]
[Character(name="char_214_kafka_1#4", name2="char_264_Mountain_1#5")]
[delay(time=1)]
[Character(name="char_214_kafka_1#4", name2="char_264_Mountain_1#5",focus=1)]
[name="卡夫卡"]虽然场面有点混乱，但是姑且跟你确认一下我们的计划！
[name="卡夫卡"]我们像现在这样，趁打扫囚房的机会进来配合你放倒囚犯和狱警......
[Dialog]
[Character(name="char_214_kafka_1#4", name2="char_264_Mountain_1#5")]
[characteraction(name="left", type="exit",fadetime=0.5, block=true)]
[characteraction(name="right", type="move", xpos=-200,times=1, fadetime=0.5, block=true)]
[delay(time=0.51)]
[CameraShake(duration=0.5, xstrength=40, ystrength=0, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Character]
[Character(name="char_264_Mountain_1#6",name2="avg_npc_134")]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=0, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Dialog]
[characteraction(name="left", type="jump",power=0, xpos=450,times=1,fadetime=0.8,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[PlaySound(key="$sheildimpact", volume=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=false)]
[characteraction(name="right", type="exit", direction="right",fadetime=0.3,block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=false)]
[characteraction(name="left", type="move", xpos=-50,fadetime=0.8,block=false)]
[delay(time=0.51)]
[Character(name="char_264_Mountain_1#5")]
[characteraction(name="middle", type="move", xpos=500, fadetime=0.94, block=true)]
[Dialog]
[Character(name="char_empty", name2="char_264_Mountain_1#5")]
[characteraction(name="left", type="move", xpos=-50, times=1, 

... (全文15857字符)
```

### level_act15d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Dialog]
[stopmusic]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[Character(name="avg_npc_135#1",name2="char_empty")]
[delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[characteraction(name="left", type="move", xpos=-70, fadetime=0.5, block=true)]
[delay(time=0.55)]
[characteraction(name="left", type="move", xpos=140, fadetime=0.7, block=true)]
[delay(time=0.75)]
[characteraction(name="left", type="move", xpos=-70, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_npc_135#4",name2="char_empty",focus=1)]
[name="巴顿"]啧，见鬼了，钥匙卡到底哪里去了......
[Character(name="avg_npc_135#2",name2="char_empty",focus=1)]
[name="巴顿"]难道是上厕所的时候被我冲掉了？
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="avg_npc_135#2",name2="avg_npc_134",enter2="right",fadetime=1)]
[delay(time=0.51)]
[Character(name="avg_npc_135#4",name2="avg_npc_134")]
[characteraction(name="left", type="jump", xpos=-20, power=70, times=1, fadetime=0.3)]
[Character(name="avg_npc_135#4",name2="avg_npc_134",focus=2)]
[name="狱警A"]巴顿老大，怎么了？
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="move", xpos=150,fadetime=0.3)]
[characteraction(name="right", type="jump", xpos=50, power=80, times=1, fadetime=0.3)]
[Character(name="avg_npc_135#4",name2="avg_npc_134",focus=1)]
[name="巴顿"]少管闲事！
[dialog]
[delay(title_test=0.51)]
[characteraction(name="right", type="move", xpos=70,fadetime=1,block=true)]
[delay(time=1.1)]
[Character(name="avg_npc_135#4",name2="avg_npc_134",focus=2)]
[name="狱警A"]是，是！
[dialog]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_135#4",name2="avg_npc_134")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="right", type="exit", direction="right")]
[delay(time=1)]
[Character]
[delay(time=0.7)]
[Character(name="char_empty",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4)]
[delay(time=0.51)]
[Character(name="avg_npc_134",enter="left",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4,fadetime=1)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_134",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4,focus=1)]
[name="狱警A"]啧，神气什么......
[Character(name="avg_npc_134",name2="avg_npc_136#4",blackstart2=0.14,blackend2=0.4,focus=2)]
[name="狱警B"]或许......又是谁触了他的霉头。
[Character(name="avg_npc_134",name2="avg_npc_136#4",blackstart2=0.14,blackend2=0.4,focus=1)]
[name="狱警A"]嘿，我猜是安东尼。
[name="狱警A"]也不知道是怎么回事，好像有人要对他下手。
[name="狱警A"]巴顿不是天天吹我们监狱多么好多么完善，这下他肯定难受死了。
[Character(name="avg_npc_134",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4,focus=2)]
[name="狱警B"]我们也是狱警。
[Character(name="avg_npc_134",name2="avg_npc_136#1",blackstart2=0.14,blackend2=0.4,focus=1)]
[name="狱警A"]哎，我不是高兴有人刺杀，我就是看到他不爽就挺爽的。
[name="狱警A"]而且说白了，咱们这些年，看伦道尔和巴顿做的龌龊事还少吗？
[name="狱警A"]要我说啊，伦道尔绝对知道这些刺客哪儿来的，他就是收了钱懒得管。
[Character(name="avg_npc_134",name2="avg_npc_136#4",blackstart2=0.14,blackend2=0.4,focus=2)]
[name="狱警B"]......或许吧。
[Dialog]
[Delay(time=1)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_prison_commandroom",screenadapt="coverall")]
[playMusic(intro="$stranger_intro", key="$stranger_loop", volume=0.4)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Dialog]
[Character(name="char_264_Mountain_1#5")]
[delay(time=1)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_451_robin#6")]
[name="罗宾"]咕......
[dialog]
[characteraction(name="middle", type="move", ypos=-40,fadetime=0.6, block=true)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=0.6, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=0.6)]
[Character(name="char_451_robin#6",name2="char_264_Mountain_1#6",focus=2)]
[name="安东尼"]别动，罗宾。
[name="安东尼"]不要逼我杀你。
[Character(name="char_451_robin#6",name2="char_264_Mountain_1#5",focus=1)]
[name="罗宾"]......
[Character(name="char_214_kafka_1#2")]
[name="卡夫卡"]唔，真没想到，我居然没发现罗宾你是内奸。
[name="卡夫卡"]说不定你有干这行的天赋呢。
[Character(name="char_451_robin#6",name2="char_264_Mountain_1#4",focus=2)]
[name="安东尼"]等等，你手里拿的是什么？
[Character(name="char_214_kafka_1#2")]
[name="卡夫卡"]那是炸药的开关？！
[Character(name="char_451_robin#6",name2="char_264_Mountain_1#4",focus=2)]
[name="安东尼"]卡夫卡，快去启动塔下沉的机关！
[dialog]
[Character]
[delay(time=1)]
[Character(name="char_451_robin#3")]
[PlaySound(key="$tokenset", volume=1)]
[delay(time=1)]
[Character]
[CameraShake(duration=1.5, xstrength=40, ystrength=40, vibrato=40, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n", volume=1)]
[PlaySound(key="$d_gen_explo_n", volume=0.6,delay=0.2)]
[PlaySound(key="$d_gen_explo_n", volume=0.2,delay=0.4)]
[delay(time=2)]
[Character(name="char_214_kafka_1#2")]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[name="卡夫卡"]呜哇！烧起来了！
[Character(name="char_264_Mountain_1#4")]
[name="安东尼"]快！
[dialog]
[Character(name="char_214_kafka_1#5")]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-100, fadetime=0.5, block=true)]
[name="卡夫卡"]我都要忘了是哪个了！
[characteraction(name="middle", type="move", xpos=200, fadetime=0.5, block=true)]
[name="卡夫卡"]而且这些感觉都不能用了啊！
[characteraction(name="middle", type="move", xpos=-100, fadetime=0.5, block=true)]
[name="卡夫卡"]啊，我找到了，应该是这个按钮！
[name="卡夫卡"]拜托了，千万要能用啊！
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[name="卡夫卡"]我按！
[d

... (全文16415字符)
```

### level_act15d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_Morgue",screenadapt="coverall")]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_451_robin#2",name2="char_264_Mountain_1#6",fadetime=0.6)]
[PlaySound(key="$rungeneral", volume=1,block=false)]
[PlaySound(key="$rungeneral", volume=0.6,delay=0.6,block=false)]
[delay(time=2.5)]
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]你们真是搞出了不小的动静啊，安东尼先生。
[name="杰斯顿"]要是我事先没有知道你们的计划，恐怕我也拦不住你。
[Character(name="char_264_Mountain_1#6")]
[name="安东尼"]你就是杰斯顿？
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]没错，正是我。
[name="杰斯顿"]虽然在这座监狱中有过数次擦肩而过，不过请容许我重新自我介绍一下。
[name="杰斯顿"]我叫做杰斯顿·威廉姆斯，是你这次越狱行动中最后的阻碍。
[Character(name="char_264_Mountain_1#6")]
[name="安东尼"]杜玛呢？
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]她在这里。
[dialog]
[Character]
[delay(time=0.6)]
[Character(name="char_441_lotus_1#4",name2="avg_npc_133")]
[Delay(time=0.6)]
[Character(name="char_441_lotus_1#4",name2="avg_npc_133",focus=2)]
[name="囚犯A"]......
[Character(name="char_441_lotus_1#4",name2="avg_npc_133",focus=1)]
[name="杜玛"]安东尼，对不起。
[name="杜玛"]我在医务室等你，没想到这个人忽然带着一些囚犯进来了......
[Character(name="char_214_kafka_1#5")]
[name="卡夫卡"]杜玛......
[Character(name="avg_npc_137#5")]
[name="杰斯顿"]如此阴森的地方，怎么能让这样一位美丽的小姐孤单地在这里等待呢？
[name="杰斯顿"]所以我就稍微保护了一下她。
[Character(name="char_451_robin#3")]
[name="罗宾"]杰斯顿先生......
[Character(name="avg_npc_137#6")]
[name="杰斯顿"]啊，罗宾小姐，你似乎失败了，真是令人遗憾。
[name="杰斯顿"]还是说，你根本没有执行刺杀？
[Character(name="char_451_robin#6",name2="char_264_Mountain_1#6",focus=1)]
[name="罗宾"]我......
[Character(name="char_451_robin#6",name2="char_264_Mountain_1#6",focus=2)]
[name="安东尼"]她失败了，你的手下伤不了我。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]但你却留了她一命，我不得不说，你真是一名出色的绅士，安东尼先生。
[Character(name="char_264_Mountain_1#6")]
[name="安东尼"]废话少说。
[Character(name="avg_npc_137#7")]
[name="杰斯顿"]也好，那就让我们直奔主题吧。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]安东尼先生，不想这位小姐死去的话，请过来这边一点。
[dialog]
[Character]
[delay(time=0.6)]
[Character(name="char_214_kafka_1#4",fadetime=0.5,block=true)]
[name="卡夫卡"]......
[Character(name="avg_npc_137#5")]
[name="杰斯顿"]卡夫卡小姐，请你乖乖地站在那里不要动。
[name="杰斯顿"]你似乎十分擅长浑水摸鱼，希望你不要擅自做一些会伤到杜玛小姐的事。
[Character(name="char_214_kafka_1#4")]
[name="卡夫卡"]嘁。
[Character(name="char_264_Mountain_1#1")]
[name="安东尼"]......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="jump", power=5,times=1, fadetime=0.3,block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="jump", power=5,times=1, fadetime=0.3,block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="jump", power=5,times=1, fadetime=0.3,block=true)]
[Delay(time=1)]
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]对，就站在那里就好。
[name="杰斯顿"]你们，围住他。
[dialog]
[Character]
[Delay(time=1)]
[Character(name="avg_npc_133", name2="avg_npc_132",enter="left", enter2="right", fadetime=1, block=false)]
[PlaySound(key="$rungeneral", volume=1,block=false)]
[PlaySound(key="$rungeneral", volume=0.6,delay=0.6,block=false)]
[Delay(time=2)]
[Character]
[delay(time=0.51)]
[Character(name="char_441_lotus_1#4",name2="avg_npc_133",focus=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杜玛"]安东尼，你别听他的！
[Character(name="char_264_Mountain_1#1")]
[name="安东尼"]不要说话，杜玛，我会救你的。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]危急关头还能保持冷静，真是令人敬佩，安东尼先生。
[name="杰斯顿"]你应该知道我想要干什么，你也知道我不可能会忽然动了恻隐之心放过你。
[Character(name="avg_npc_137#5")]
[name="杰斯顿"]我的建议是，你可以考虑抛弃这位小姐，抛弃你一直以来伪装自己的教养，然后来与我厮杀。
[Character(name="char_264_Mountain_1#1")]
[name="安东尼"]废话，少说。
[Character(name="avg_npc_137#7")]
[name="杰斯顿"]你能坚持到什么时候呢？
[Character]
[dialog]
[delay(time=0.7)]
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]然后是你，罗宾小姐。
[Character(name="char_451_robin#3")]
[name="罗宾"]诶？
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]接下来，请你杀了安东尼先生，完成你未竟的任务。
[name="杰斯顿"]我并不在乎你在刚才与安东尼先生达成了怎样的协议，又发生了怎样的心境转变。
[name="杰斯顿"]如果你想获得那笔钱，如果你想救你的父亲，那么，这是你最后，也是最好的机会。
[Character(name="char_451_robin#6")]
[name="罗宾"]......
[name="罗宾"]我......
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]你在犹豫什么？是安东尼对你许诺了什么空头支票？还是事到如今你心软了？
[name="杰斯顿"]这是你唯一的机会了，罗宾小姐。
[Character(name="char_451_robin#6")]
[name="罗宾"]我，我......
[Character(name="avg_npc_137#6")]
[name="杰斯顿"]想想你的父亲，想想你变得一团糟的生活，想想你的未来，想想你的愿望。
[name="杰斯顿"]如果我是你，我不会犹豫。
[Character(name="char_264_Mountain_1#1")]
[name="安东尼"]你究竟想做什么？
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]我想做什么？
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]我想做的还不明显吗？如果我只是想杀害你，在监狱之中我有许多机会。
[name="杰斯顿"]但这些都太没意思了，真的，太没意思了。
[name="杰斯顿"]杀人这件事对我来说并没有特别的乐趣，安东尼先生。
[Character(name="avg_npc_137#7")]
[name="杰斯顿"]对我来说，最有趣的部分，是改变，是人面临抉择时不得不抛弃过去面孔的那一瞬间。
[name="杰斯顿"]所以我把罗宾小姐引来，渴望罗宾小姐的改变，渴望她的堕落。
[name="杰斯顿"]也渴望你的改变，渴望你此时此刻为了你的家人，为了你的目的，而抛弃一直以来的矜持，露出你的獠牙！
[Character(name="avg_npc_137#6")]
[name="杰斯顿"]啊，别装了，安东尼先生，说真的，别装了。
[name="杰斯顿"]想想你的家族，想想你受的无妄之灾，想想你的忍辱负重，想想你越狱的目标。
[name="杰斯顿"]你真的甘心就这样死在这里？
[name="杰斯顿"]你真的甘心为了区区一个认识几年的女性就葬送性命？
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="杰斯顿"]站起来，安东尼先生，推开罗宾小姐，忘掉杜玛小姐，扑向我，然后杀害我！
[Character(name="char_264_Mountain_1#6")]
[name="安东尼"]别把所有人都想得和你一样，杰斯顿。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]别以为你与众不同，安东尼。
[dialog]
[PlayMusic(intro="$stranger_intro", key="$stranger_loop",crossfade=1,volume=0.4)]
[delay(time=0.6)]
[name="杰斯顿"]我给你五秒钟时间，罗宾小姐，时间到的话，我就会亲自动手，而你，恐怕也不得不葬身此地了。
[name="杰斯顿"]五。
[name="杰斯顿"]罗宾小姐，你父亲的手术费还差许多，而安东尼先生现在身无分文。
[Character(name="char_451_robin#6")]
[name="罗宾"]安东尼，我......
[Character(name="avg_npc_137#6")]
[name="杰斯顿"]四。
[name="杰斯顿"]安东尼先生，你的父母因为在监狱中受到排挤，过得非常不好。
[Character(name="char_264_Mountain_1#3")]
[name="安东尼"]......父亲，母亲。
[Character(name="avg_npc_137#9")]
[name="杰斯顿"]三。
[dialog]
[Character(name="char_441_lotus_1#4",name2="avg_npc_133",focus=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrat

... (全文22024字符)
```

### level_act15d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_Morgue",screenadapt="coverall")]
[PlayMusic(intro="$longmenbat_intro", key="$longmenbat_loop", volume=0.4)]
[Character(name="avg_npc_137#4",name2="char_264_Mountain_1#5")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_137#4",name2="char_264_Mountain_1#4")]
[name="安东尼"]混账！
[characteraction(name="right", type="jump", xpos=-100, power=0, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[playsound(key="$sheildimpact",volume=0.8)]
[playsound(key="$p_imp_blunt_h",Delay=0.05,volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="right", type="jump", xpos=100, power=5, times=1, fadetime=1,block=true)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_137#1",name2="char_264_Mountain_1#4",focus=1)]
[name="杰斯顿"]没用的，安东尼老弟。
[dialog]
[delay(time=1)]
[Character(name="char_451_robin#2",name2="avg_npc_137#4")]
[delay(time=1)]
[Character(name="char_451_robin#2",name2="avg_npc_137#1",focus=2)]
[name="杰斯顿"]罗宾小姐，没想到你的战斗能力也相当出色，我越来越喜欢你了。
[name="杰斯顿"]如何，现在帮助我的话，我依然可以原谅你。
[Character(name="char_451_robin#2",name2="avg_npc_137#1",focus=1)]
[name="罗宾"]不必了！
[dialog]
[Character(name="char_451_robin#2",name2="avg_npc_137#4")]
[characteraction(name="left", type="jump", xpos=100, power=0, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="left", type="jump", xpos=-100, power=5, times=1, fadetime=1,block=true)]
[Delay(time=1.5)]
[Character]
[Character(name="char_214_kafka_1#2")]
[name="卡夫卡"]这家伙的手到底是怎么回事，变黑之后变得好硬的样子！
[Character(name="avg_npc_137#4")]
[name="杰斯顿"]稍微为你介绍一下吧，我的源石技艺能力呢，是操控铁元素，而我的身体，接受过一些小小的改造。
[name="杰斯顿"]你刚才的攻击是不是感觉打到了铁板上？
[name="杰斯顿"]那不只是我的源石技艺的能力。
[name="杰斯顿"]我的皮肤下层，有着莱茵生命科技的结晶——一些小小的金属板。
[Character(name="avg_npc_137#1")]
[name="杰斯顿"]好吧，我并不清楚这东西的学名是什么，总之它能够大幅减少你进攻的威力。
[Character(name="char_214_kafka_1#2")]
[name="卡夫卡"]等等，你是莱茵生命的人？！
[Character(name="avg_npc_137#4")]
[name="杰斯顿"]不，很遗憾，我不是。
[Character(name="avg_npc_137#3")]
[name="杰斯顿"]无论如何，即使被抑制器限制，依然如此善战，真是令人吃惊。
[Character(name="avg_npc_137#4")]
[name="杰斯顿"]看来我也得拿出一些真本事了。
[Character(name="char_451_robin#2")]
[name="罗宾"]他的手，变成了刀刃......
[Character(name="avg_npc_137#4")]
[name="杰斯顿"]你知道吗，安东尼先生。
[Character(name="avg_npc_137#2")]
[name="杰斯顿"]从我来到这座监狱后，第一眼看到你的时候开始，我就感到了一种不协调。
[Character(name="avg_npc_137#4")]
[name="杰斯顿"]你尽力在克制着自己，让自己显得无害，让自己显得有礼貌。
[name="杰斯顿"]但是你的存在本身就是力量的彰显。
[name="杰斯顿"]从那时起，我就很期待现在这一幕。
[Character(name="avg_npc_137#3",name2="char_264_Mountain_1#6",focus=1)]
[name="杰斯顿"]你撕开温文尔雅的伪装后，凶性毕露的样貌——
[Character(name="avg_npc_137#3",name2="char_264_Mountain_1#6",focus=2)]
[name="安东尼"]想必我没有令你失望。
[Character(name="avg_npc_137#4",name2="char_264_Mountain_1#6",focus=1)]
[name="杰斯顿"]没错，我大开眼界。
[dialog]
[Character]
[CharacterCutin(widgetID="mountain1", name="char_264_Mountain_1#4", offsetx=0, width=400, fadestyle="horiz_expand_center", fadetime=0.2, block=true)]
[CameraShake(duration=2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="安东尼"]你没有资格判断我的本性！！！吼！！！
[dialog]
[CharacterCutin(widgetID="mountain1")]
[CharacterCutin(widgetID="npc137", name="avg_npc_137#4", offsetx=0, width=400, fadestyle="horiz_expand_center", fadetime=0.2, block=true)]
[name="杰斯顿"]我也无意于这么做。我只是想说，现在的你，看着顺眼多了。
[dialog]
[CharacterCutin(widgetID="npc137")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[CameraShake(duration=2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_137#4",name2="char_264_Mountain_1#4")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="right", type="jump", xpos=-100, power=0, times=1, fadetime=0.1,block=true)]
[characteraction(name="left", type="jump", xpos=100, power=0, times=1, fadetime=0.1,block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=false)]
[PlaySound(key="$sheildimpact", volume=1)]
[CameraShake(duration=100, xstrength=30, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.04, block=true)]
[playsound(key="$p_imp_blunt_h",volume=1)]
[playsound(key="$p_imp_blunt_h",Delay=0.05,volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.04, block=true)]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=100, xstrength=20, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.04, block=true)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.04, block=true)]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=100, xstrength=20, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[playsound(key="$p_imp_blunt_h",volume=1)]
[playsound(key="$p_imp_blunt_h",Delay=0.05,volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[CameraShake(duration=0.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=100, xstrength=20, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(ti

... (全文19175字符)
```

### level_act15d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]然后接下来的话，就到罗宾......
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]打断一下，梅尔小姐。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]嗯？
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]我有一些其他问题想先问问梅尔小姐你。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]是什么？我懂的没有赫默那么多哦。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]没关系，这是你也知道的事情。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]你对“炎魔”事件怎么看？
[name="缪尔赛思"]据我所知，你也参与了那个项目吧？
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]不知道诶。
[name="梅尔"]我们工程科一般只负责提供设备或者在建造设备时提出专业性的意见，实验本身我们很少主动去了解。
[name="梅尔"]我只知道事件的结果，是赫默带着伊芙利特来到当时刚建立合作关系的罗德岛。
[name="梅尔"]还有塞雷娅一个人揽下了所有事情，直接从莱茵生命离开。
[name="梅尔"]你要是想从我这里了解这起事件的话那你找错人了哦。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]不，我并不想了解这起事件，毕竟，这样的事件在莱茵生命内部并不少见。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]嗯，那你问我这个干什么？
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]因为我想知道，从你的角度来看，赫默和塞雷娅分别是什么样的人？
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]唔，我觉得赫默是一个很认真的人，老实说，我一直觉得研究者应该就是她这个样子了。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]确实，她十分聪明，观察力很敏锐，而且过去也有不少项目成功的经验。
[name="缪尔赛思"]据我所知，结构科的那位主任是希望赫默能够接过他的衣钵的。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]哇，那赫默岂不是下一任的结构科主任，好厉害！
[Character(name="char_249_muesys_1#6",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]是啊，连我都忍不住想要巴结她一下了呢~
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]至于塞雷娅，其实我和她不是很熟呢。
[name="梅尔"]毕竟防卫科和其他科室都不太一样，在罗德岛也几乎没有见过，更不要说聊天了。
[name="梅尔"]不过“炎魔”事件给我最大的感觉是她非常的保守。
[name="梅尔"]毕竟她当时直接叫停了整个项目，甚至干脆引咎辞职了，实验失控这种事在我们内部其实还蛮常见的吧。
[name="梅尔"]虽然我们同事之间也有传闻是“炎魔”事件有一些内幕，不过我也不是很了解这种事啦。
[name="梅尔"]反正现在小伊芙利特在罗德岛还是活蹦乱跳的，应该没有什么大问题吧。
[Character(name="char_249_muesys_1#3",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]嗯？那个叫伊芙利特的实验体现在在罗德岛生活得还好吗？
[Character(name="char_249_muesys_1#3",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]嗯，每天都很有活力哦。
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]啊，我还以为已经......看来罗德岛这家公司也确实有相当的实力呢。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]不过，我可以告诉你的是，塞雷娅离开莱茵生命的理由当然不只是因为“炎魔”事件，那只是一连串事情中的其中一件。
[name="缪尔赛思"]虽然或许是决定性的一件。
[name="缪尔赛思"]她会离开的最大原因，其实是因为和总辖的关系不和。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]诶？总辖？
[Character(name="char_249_muesys_1#1")]
[name="缪尔赛思"]没错，塞雷娅和总辖关系其实还不坏哦？
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]但是塞雷娅确实如你所说的保守，她认为所有的科学研究都应该在可控的范围内进行。
[name="缪尔赛思"]而总辖显然并不这么想，否则也不会有莱茵生命这家公司了。
[Character(name="char_249_muesys_1#4")]
[name="缪尔赛思"]怎么说呢，打个比方吧。
[Character(name="char_249_muesys_1#5")]
[name="缪尔赛思"]我们假设有一条线，这条线是塞雷娅认为的线。
[name="缪尔赛思"]而一直以来，莱茵生命做的事都是在线的下方，最多差点触及这条线，所以塞雷娅一直没有做声。
[name="缪尔赛思"]但是包括“炎魔”在内的一系列事件代表着有些人想要越线，甚至已经越过了。
[name="缪尔赛思"]这就是塞雷娅所无法容忍的了。
[Character(name="char_249_muesys_1#4")]
[name="缪尔赛思"]但是总辖并不在乎这件事。
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]为什么？
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]梅尔小姐，你告诉我，你真的在乎我和赫默小姐讨论的安东尼背后牵扯的事情吗？
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]嗯......在听说了他的事情后，我觉得他能逃出来还挺好的，就这样吧。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]你看，你拥有淳朴的善良，但你其实不在乎，你更在乎自己的研究，在乎你的“咪啵”。
[name="缪尔赛思"]不得不说，咪啵确实是不错的设计，能借我摸摸吗？
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]可以呀，去吧。
[Dialog]
[Character]
[PlaySound(key="$tokenset", volume=1)]
[name="咪啵"]——！
[Delay(time=1)]
[Character(name="char_249_muesys_1#6",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]啊哈，真可爱。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]你刚才也一直在旁边画你的企划案吧。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#4",focus=2)]
[name="梅尔"]没错，我有了不少新点子，就等着回到罗德岛实践一下了。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]呵呵，你看，总辖事实上也是这样的人。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]她看得更高，更远，有时候，我会觉得即使是头顶的天空也挡不住她的视线。
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]她注视的地方，恐怕这片大地上所有的人都想象不到，就连我也只能稍微揣摩她的心思。
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]诶，我只在演讲上看过总辖的样子，没想到总辖也是这样的人啊。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]没错，所以很多事情她其实并不在乎，对她来说，只要没有妨碍到她的研究，那么就没有那么一条线存在。
[name="缪尔赛思"]于是她和塞雷娅产生了分歧。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]但是，为什么你要告诉我这些？这不应该是告诉赫默的事情吗？
[name="梅尔"]告诉我我也不知道能拿这些情报来干什么。
[Character(name="char_249_muesys_1#1",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]正是因为你不知道，所以我才会告诉你。
[name="缪尔赛思"]我只是感觉你和总辖应该合得来，所以希望你能够了解总辖是一个什么样的人。
[name="缪尔赛思"]而且我本人也想和你交个朋友。我个人还是很喜欢你这样纯粹的研究者的。
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]我记得你是自愿前往罗德岛的吧？
[Character(name="char_249_muesys_1#4",name2="char_242_mayer#2",focus=2)]
[name="梅尔"]嗯，因为我想换个环境。
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",focus=1)]
[name="缪尔赛思"]可以说说为什么吗？
[Character(name="char_249_muesys_1#5",name2="char_242_mayer#2",fo

... (全文13229字符)
```

### level_act15d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="avg_ac15_3add",y=-80,x=-250, fadetime=0)]
[ImageTween(xScaleFrom=1.7, yScaleFrom=1.7, xScaleTo=1.6, yScaleTo=1.6, duration=3, block=false)]
[PlayMusic(intro="$nightoflongmen_intro", key="$nightoflongmen_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="缪尔赛思"]斐尔迪南......能量科主任。
[name="赫默"]......是的。
[name="缪尔赛思"]不过，比起这个，我更在意的是......
[dialog]
[Delay(time=0.6)]
[ImageTween(xTo=-320,yTo=200,duration=0.6, block=true)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="缪尔赛思"]为什么，塞雷娅，会，出现在，这里！
[name="赫默"]这个问题正是我想问你的，为什么塞雷娅会出现在这里，缪尔赛思主任？
[name="缪尔赛思"]......这个问题是什么意思？
[name="赫默"]塞雷娅是你在这次事件中的帮手，不是吗？确切地说，原本是你的帮手。
[name="缪尔赛思"]哎呀，为什么你会这么想？
[name="赫默"]在谈话开始时，我就一直在想你在这件事情中所处的位置。
[dialog]
[ImageTween(xFrom=-320,xTo=200,yFrom=200,yTo=-150,duration=1,block=true)]
[Delay(time=1)]
[name="赫默"]我相信你与海德兄弟以及能量科无关，但如果你是了解事情经过的旁观者，那你找到我的行为就显得过于热情。
[name="赫默"]所以我的初步判断是，你在这件事情中应当是我的“竞争者”。
[name="赫默"]你也想要安东尼来做些什么。
[name="赫默"]而在这件事情中，最让我感到不可思议的，就是塞雷娅的出现。
[name="赫默"]她已经完全与莱茵生命断绝了关系，现在的她唯一的身份是罗德岛的干员。
[name="赫默"]她应当没有任何理由插手这件事。
[dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#1",focus=2)]
[name="缪尔赛思"]哎呀，这样说的话，我也可以说她是你的王牌呢。
[name="缪尔赛思"]我确实不知道她居然真的在那个时间出现在了那里哦。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="赫默"]我还记得你开始说的话——
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5")]
[musicvolume(volume=0.2, fadetime=1)]
[Delay(time=1)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]我所了解的，只有它的开端——
[name="缪尔赛思"]海德兄弟针对被关押在曼斯菲尔德监狱中，西蒙家族唯一的幸存者，安东尼·西蒙展开了一场蓄谋已久的刺杀。
[name="缪尔赛思"]还有它的结果——
[name="缪尔赛思"]以安东尼为首的几人团伙成功逃出了曼斯菲尔德监狱，并且与你们两个完成了汇合，目前已经离开了哥伦比亚。
[name="缪尔赛思"]中间具体发生了什么事，很遗憾，原本我有了解的机会，不过现在已经没有了。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5")]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[Background(image="bg_bar_1",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]假设你是我的“竞争者”，那么你不应该只了解这一点，你也应该有一个帮手，而这个帮手应该将能够告诉你监狱中发生的事情。
[name="赫默"]但你没有，从种种迹象来看，我相信你是真的不知道这一连串发生的事情。
[name="赫默"]再联想到塞雷娅的突然出现。
[name="赫默"]我只能得出一个结论，那就是——
[dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="avg_ac15_3add",fadetime=0)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1.05, yScaleTo=1.05, duration=5, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="赫默"]她原本是你的合作者，但她却违背了你们的协议。
[name="缪尔赛思"]但是既然如此，你们的出现也应当是个意外，为什么她会将安东尼交给你？
[name="缪尔赛思"]即使你们同样都和罗德岛有关系，但在这件事上如果真如你所说，她的立场应当完全与你对立，不是吗？
[name="赫默"]......不。确实直到刚才，我也一直没有想明白，卡夫卡不可能是她的对手，理论上她应当才是最后的胜利者。
[name="赫默"]而我们......并没有什么联系，她实在没有理由将安东尼交给我。
[name="赫默"]但是现在我明白了。
[dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#6")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#6",focus=2)]
[name="缪尔赛思"]......啊哈，原来如此，是为了骗过我吗。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]没错。
[name="赫默"]接下来只是我的猜测。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]对她来说，在掌握......不，我不是很想用这个词......
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]还是营救吧，在营救完安东尼后，她可以说是最后的赢家。
[name="赫默"]对她来说，安东尼最好的去处，并不是来到你的手上，因为那会助长你的势力，所以她会做的事应该是将安东尼截下，由她自己掌控。
[name="赫默"]我不知道她在干什么，我也不想知道，但是她肯定知道海德兄弟不会就此善罢甘休，而她将要背叛的你也不会。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]所以她利用了在整个事件中直到最后才登场这一点，将自己完全地从这件事情中从台面上隐去。
[name="缪尔赛思"]虽然我觉得她不会怕我和海德兄弟，不过，好吧，多一事不如少一事，是我我也会这么选。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]而且，她在哥伦比亚应该确实还有事......算了，这和这件事应该无关。
[Character(name="char_108_silent_1#3", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]她......算了，总之，我们的出现对她来说应当也是个意外，恐怕是她从卡夫卡那里大致了解了我们这边的情况后做出的判断吧。
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#6",focus=2)]
[name="缪尔赛思"]......真是漂亮的推理，赫默小姐。
[name="缪尔赛思"]你猜的一点都不错，正是我告诉塞雷娅这件事的。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]杰斯顿在那之后应该是被发现并不是真正的狱卒而被收监了，导致我这边也没有收到有关他的情报。
[name="缪尔赛思"]我确实被塞雷娅摆了一道。唉，虽然我一开始就觉得塞雷娅不会乖乖把人交给我就是了。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=1)]
[name="赫默"]......那你为什么还要找她帮忙？
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#4",focus=2)]
[name="缪尔赛思"]那当然是因为——
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#5",focus=2)]
[name="缪尔赛思"]没有办法啊。
[name="缪尔赛思"]公司内部我没有那么信得过又有能力做到这件事的人。
[name="缪尔赛思"]要是我有别的人可以依靠，我才不想麻烦塞雷娅呢。
[Character(name="char_108_silent_1#4", name2="char_249_muesys_1#2",focus=2)]
[name="缪尔赛思"]我虽然是生态科主任，不过其实是很弱小的哦。
[name="缪尔赛思"]你看，我现在不仅人被她抢走了，还要惨兮兮地想办法看能不能把人

... (全文18247字符)
```

### training_act15d0_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_a
[PopupDialog(dialogHead="$avatar_silent")]监狱里的囚犯会因为身上的“禁锢终端”，被限制攻击能力。
[PopupDialog(dialogHead="$avatar_silent")]白光代表禁锢终端正常运作，此时敌人攻击强度被大幅限制。
[PopupDialog(dialogHead="$avatar_silent")]敌人在“禁锢”状态下<@tu.kw>攻击</>时，会消耗终端的能量。
```

### training_act15d0_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_b
[Tutorial(focusX=120, focusY=220, focusWidth=100, focusHeight=100,          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", 		  dialogHead="$avatar_silent", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 禁锢终端橙光闪烁的样式，是终端即将失效的预警：敌人将<@tu.kw>在下一次攻击时进入解放</>。
[Tutorial(dialogHead="$avatar_silent", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 禁锢终端失效后，<@tu.kw>解放</>的敌人<@tu.kw>攻击速度和攻击力</>将大幅提升，有些敌人甚至会解放<@tu.kw>特殊能力</>。
```

### training_act15d0_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_c
[PopupDialog(dialogHead="$avatar_otter")] 有什么方法可以重新激活禁锢终端？
[Tutorial(focusX=110, focusY=80, focusWidth=120, focusHeight=120,          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_silent", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 唯一有效的办法是利用禁锢装置。它能重新启动监测范围内所有失效的禁锢终端，再次禁锢<@tu.kw>已经解放的敌人</>。
```

### training_act15d0_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_d
[Tutorial(focusX=110, focusY=80, focusWidth=120, focusHeight=120,          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_silent", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 禁锢装置会被囚徒们<@tu.kw>优先攻击</>，请注意这一点。
```

### training_act15d0_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_e
[PopupDialog(dialogHead="$avatar_silent")] 将敌人控制在“禁锢”状态下，痛打他们吧。
```


## 统计

- 总字符数：251760
- 对话行数：2230


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
