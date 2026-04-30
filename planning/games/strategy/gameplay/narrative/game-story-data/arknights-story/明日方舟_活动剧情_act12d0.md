# 明日方舟 · 活动剧情 · act12d0（32段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act12d0」完整剧情脚本（32个文件，2106行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act12d0
- 脚本文件数：32

### level_act12d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Delay(time=1)]
这里有你想要的一切。
你所渴望的片刻安宁、没有战争的大地、母亲的怀抱。
你的意识无限扩张，你挣脱了枷锁，你自由了。
[Dialog]
[delay(time=1)]
[Decision(options="什么是自由？;我自由了！", values="1;2")]
[Predicate(references="1")]
通常意义上，自由是一种相对的状态，它意味着没有束缚，但这么说着的人往往依然被他的肉体所束缚。
但你真正的自由了。
[Predicate(references="2")]
没错，我亲爱的朋友，你永远地、永永远远地自由了。
[Predicate(references="1;2")]
你如同时间长河中的一颗顽石，它将会带走你的责任、宿命、欲望、联系，但唯有你自身，你将永远地存在于这里。
你不拥有任何东西，任何东西也不拥有你。
[Decision(options="没有比这更棒的事了！;责任、宿命、欲望、联系......", values="1;2")]
[Predicate(references="1")]
你理解了一切，现在的你正在与某个未知的存在对话，你应当敬畏，献上你最纯洁的血。
或者，你只是单纯因为冲击而陷入了昏迷状态，在跟臆想中的自己进行一场毫无意义的对话。
[Decision(options="我要在这里建立我的王国！;不，我反悔了，我更喜欢痛苦。", values="3;4")]
[Predicate(references="3")]
绝妙的选择，我的国王，这里比大地更广阔，你可以在这里建立一切你想要的东西。
那么首先，先来建立一个国家吧，国家的名字就叫存在国怎么样？
建立在虚无之上的国家将永远屹立不倒——
哦不，该死，我们的伟业看起来要在此中断了。
如同窗帘间射入的一道光，强烈的酸痛感瞬间占据了你的所有意识。
[Predicate(references="4")]
你喜欢痛苦，你喜欢付出，你喜欢主动投身火焰，你喜欢让自己受伤。
聪明人总是想要一场恰到好处的失败，一些可以及时止损的失去，他们认为这样可以最有效地让自己成长。
不要自大，我的虚无部书记。
那么，首先，先给你来一些你最喜欢的痛苦吧——
从你的全身各处的肌肉上，传来了极度酸痛的感觉。
[Predicate(references="2")]
士兵，你承受了无数痛苦，见证了无数失败，其中让你愉快的事寥寥无几。
而让你走到这一步的就是它们。它们是毒药，它们是枷锁，它们让你不得安宁。
有些事情已经无法挽回，而有的事情无需你来承担。
[Decision(options="你说得对，我该休息了。;不，有人在等我。",values="5;6")]
[Predicate(references="5")]
好的，亲爱的，这就对了。
放轻松，我来为你唱一首摇篮曲，你将永久地睡去，不受一丝侵扰。
哦，但是，就在你要入睡时，一种强烈的感觉突然向你袭来——这是痛楚！
[Predicate(references="6")]
哦，是的，我承认，那是些好孩子。
但你有没有想过，没有你他们也能够前进，你并不对他们负责。
你的责任、你的宿命、你的欲望、你与他们的联系，一切只是你的妄想？
......好吧，我知道你已经决定，那么，给你一个惊喜吧，没错，就是你最喜欢的痛苦！
从你的全身各处的肌肉上，传来了极度酸痛的感觉。
[Predicate(references="3;4;5;6")]
随之而来的，是一个遥远但是熟悉的声音。
[name="？？？"]  ......士，博士！
阿米娅？不，不是，这个声音比阿米娅更加成熟。
[name="？？？"]  躺这么久了还不醒，真麻烦。
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Delay(time=0.55)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.7, xstrength=10, ystrength=12, vibrato=30, randomness=120, fadeout=true, block=true)]
......和暴力。
你感觉到可能是自己脸颊的部位受到了几次冲击，看来对方还有言出必行的优良品质。
[name="？？？"]  怎么办，这都不醒，反正阿米娅不在，把博士抓起来来几圈大风车试试好了。
[name="？？？"]  大风车？好玩吗，我也要玩！
对方似乎要采用过激手段了，而且插进来的这个声音，带着一丝纯真。
纯真这项美好的特质在这种情境下的含义是，她是认真的。
[Decision(options="不，我要回去！;睁开双眼",values="1;2")]
[Predicate(references="1")]
哦，很遗憾，有些旅行不是由你的意志决定的，你已经失去了踏上这次旅行的机会。
不过不要紧张，机会还有很多。现在，让我们睁开双眼......
[Predicate(references="2")]
[Predicate(references="1;2")]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=1, r=0,g=0, b=0, block=true)]
[Background(image="bg_desert_1",x=-100, y=-50,xScale=1.3, yScale=1.3, fadetime=2)]
[Image(image="ac12_1",x=0,y=0,xScale=1, yScale=1)]
[Dialog]
[Blocker(a=0.7, r=0, g=0, b=0,fadetime=0.8, block=true)]
[Blocker(a=1, r=0, g=0, b=0,fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0,fadetime=2,block=false)]
[Delay(time=1)]
[Delay(time=2)]
[name="刻俄柏"]  嘉维尔，大风车应该怎么玩呀？
[name="嘉维尔"]  所谓大风车，就是你要把对方的腿或者手抓起来，然后开始旋转起来。
[name="嘉维尔"]  等到你觉得差不多了就把他丢出去。
[name="刻俄柏"]  听起来好好玩！我可以试试吗！
[name="嘉维尔"]  可以啊，我来接住博士就是了......嗯？
[name="嘉维尔"]  博士，你终于醒了。
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="刻俄柏"]  啊，博士醒了！
[name="嘉维尔"]  小刻，别一下子就跳到博士身上去，博士被你这么一压说不定又要昏过去了。
[name="刻俄柏"]  哦，对不起，博士！
[Dialog]
[character]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.8, crossfade=1, delay=0.5)]
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",fadetime=2,block=true)]
[delay(time=2)]
[Decision(options="你们没事吧？;......;刚刚你是不是扇我了？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  没事，这点高度，小意思。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  我也没事！
[Predicate(references="2")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  喂，不是吧博士，你难道又摔失忆了？
[Decision(options="我失忆了。;姐姐，你是谁？",values="4;5")]
[Predicate(references="4")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，你别忘了，我是医生。
[Predicate(references="5")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  还会开玩笑，看起来没有大事。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  扇了。
[Predicate(references="1;3;4;5")]
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  总之，博士，我来简单说明一下情况吧。
[name="嘉维尔"]  总而言之，我们坠机了。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  从很高的地方摔了下来！咻——！碰！这样。
[Decision(options="详细一点。;......;太简单了吧！",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  啧，好吧，总之，博士你运气不太好，我们被攻击的时候爆炸正好发生在你座位附近，你直接被炸飞撞到墙上就晕倒了。
[name="嘉维尔"]  放心，你的伤口我已经包扎过了，问题不大，而且和你刚到罗德岛的时候比，你的体质可好了不少。不错啊，博士。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  呜呜，博士，对不起，我应该接住你的，但是我被爆炸声吓到了......
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  这也不能怪你，老实说，就算是我也想不到这帮崽子居然还有能对空的武器了。
[Decision(options="也就是说你早就料到会被攻击了？", values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  是啊，我没说过吗，我老家这里的人很好斗的，虽然他们都打不过我。
[Decision(options="其他人呢？", values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  在下坠的时候，为了控制高度，其他人中途就先跳下去了。
[name="嘉维尔"]  为了保护你，我和刻俄柏是最后才跳下来的。
[name="嘉维尔"]  哦对，Lancet-2应该还留在飞行器上。
[Decision(options="飞行器呢？", values="1")]
[Predicate(references="1")]


... (全文9044字符)
```

### level_act12d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Delay(time=0.55)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral")]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.7, xstrength=10, ystrength=12, vibrato=30, randomness=120, fadeout=true, block=true)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  *粗话*，好、好厉害。
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  哎呀，你们还挺厉害的嘛，可惜撞上了我嘉维尔。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  等、等等，你说你叫什么？
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嘉维尔啊。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  嘉维尔？！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  仔细一看，这张脸，这头发，你不是嘉维尔吗！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  我不是说了我是嘉维尔吗！
[Character(name="avg_npc_071")]
[name="阿达克利斯人A"]  噫，是嘉维尔，嘉维尔回来了！弟兄们，走，快去告诉森蚺族长！
[Dialog]
[character]
[PlaySound(key="$rungeneral", volume=0.9)]
[delay(time=0.5)]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嗯？森蚺？喂，给我等等！
[name="嘉维尔"]  啧，跑掉了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="bg_desert_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  太好了，你们再来晚一点，我就要被它们抢走了。
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1#2", focus=2)]
[name="嘉维尔"]  驾驶的家伙呢，叫什么来着，哦对，迪伦，迪伦呢？
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1#2", focus=1)]
[name="Lancet-2"]  迪伦刚才想要反抗这群阿达克利斯人被他们打昏了。
[Character(name="char_187_ccheal_1#2", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  啊，嘉维尔，迪伦在这里！
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  好，把他拖过来吧，我来看看伤势。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  喔。
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  对了，Lancet-2，你应该会修这个飞行器吧？
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=1)]
[name="Lancet-2"]  是的，在出发前，可露希尔为我录入了大量飞行器相关的知识。
[name="Lancet-2"]  原本在成功迫降后，依靠维修工具应该是能完成维修的。
[name="Lancet-2"]  但是......
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  小刻，我让你把他拖过来，不是让你真的用拖的。
[Character(name="char_187_ccheal_1#2", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  喔，对不起。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  ......看起来对面也没下死手，嗯？看不出来，这家伙内裤挺花哨......咳，估计躺半天就自己醒了。
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  然后，Lancet-2，你说什么但是？
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=1)]
[name="Lancet-2"]  但是刚才那群阿达克利斯人，把引擎抢走了。
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  哈？引擎？
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=1)]
[name="Lancet-2"]  是的，在他们发现我之前，我在舱内看到他们首先找到了飞行器的引擎并直接把它拆了下来并带走了。
[name="Lancet-2"]  你们来看这边。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_aircraft_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1#2", focus=2)]
[name="嘉维尔"]  喔，真的有个洞欸。虽然我不太懂这东西，不过应该是飞不起来了？
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1#2", focus=1)]
[name="Lancet-2"]  嗯，飞不起来了呢。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嗯？博士，你的脸色不太好。
[Decision(options="这下麻烦了。;......;要被凯尔希杀了！",values="1;2;3")]
[Predicate(references="1;2;3")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
一段时间以前
[Character(name="char_003_kalts_1",fadetime=1,block=true)]
[delay(time=1)]
[name="凯尔希"]  信？
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  对，从我老家寄来的，家乡那边又要举行“玛维索提亚”了。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=1)]
[name="凯尔希"]  “玛维索提亚”，力量与荣耀？
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  这你都知道？这是我老家选举大酋长的祭典用的名字。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=1)]
[name="凯尔希"]  我已经有相当一段时间没有听人使用这种语言了。
[name="凯尔希"]  不过，我记得你是背井离乡来到罗德岛的。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  是啊，不过还有一个小妹妹和我有联络，这封信就是她寄来的。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=1)]
[name="凯尔希"]  我记得你说过，你是因为被排挤而离开的，那么选举酋长应当与你无关。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  是啊，我也不是回去做大酋长的，只是小姑娘好像很想让我回去的样子，我也有确实有一阵子没有回去了......
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=1)]
[name="凯尔希"]  想家了？
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  有一点吧。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=1)]
[name="凯尔希"]  那么，为什么要带上Dr.{@nickname}，从生物学的角度来说，他没有其实是你同族的可能性。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  博士也努力了这么久，我想着带他去放松一下。
[Character(name="char_003_kalts_1", name2="char_187_ccheal_1", focus=1)]
[name="凯尔希"]  那么飞行器使用申请书又是怎么回事，煌？
[C

... (全文18838字符)
```

### level_act12d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Dialog]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_aerialview",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$leaveshake", volume=0.6)]
[delay(time=2)]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  这片雨林还是老样子啊。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嘉维尔已经很久没来过了吧。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  我一直不喜欢这地方，空气又潮湿，地又松软，一点也没有刚强的感觉。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  不过现在有很多部族都搬进了雨林哦。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  是这样吗？......啊，博士，你醒了，昨晚睡的还好吗？
[Decision(options="还好。;......;我精神超好。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  适应力不错啊，博士，还以为你肯定受不了在这种环境下露宿。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈哈，看你的眼神就知道了。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  嗯，如果你不一直揉额角的话我会相信你的。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  早跟你说了吧，博士，做好心理准备吧，接下来都只有这样的环境了。
[name="嘉维尔"]  给，我用这边能找到的素材做了点醒神的汤，喝了吧。
[name="嘉维尔"]  嘿，说起来，以前不知道，刚才在周围转转才发现，这片雨林的药用植物还挺多的。
[Dialog]
[Character]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  ......嘉维尔居然在照顾人。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嘉、嘉维尔，我也没睡好......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  哈？你这样还能算是阿达克利斯？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  阿达克利斯......呜呜，嘉维尔果然已经忘了我们原本的名字了......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  嗯？哦，我都忘了。是提亚卡乌才对。
[name="嘉维尔"]  自从离开这里后，提亚卡乌这个词好久没用过了。博士，你也记一下，在我们这里，是不按种族区分自己的。
[name="嘉维尔"]  从种族上区分的话，我想想啊，我是阿达克利斯，祖玛玛那家伙是斐迪亚，还有黎博利......嗯，大概有这三种吧。
[name="嘉维尔"]  不过在这里，我们都自称提亚卡乌，在我们的语言中是“骁勇善战的人”的意思。
[name="嘉维尔"]  然后，虽然感觉你应该用不着，不过我们自己称呼这里是叫做阿卡胡拉，在我们的语言中是“茂林丛生之地”的意思。
[name="嘉维尔"]  好了，别哭哭啼啼的，把你的手下也都叫起来，该出发了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#5", focus=2)]
[name="特米米"]  呜呜呜......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#5", focus=2)]
[name="特米米"]  罗德岛，博士。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#5", focus=1)]
[name="嘉维尔"]  哦，对了，公司的意思就是......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  啊，我知道的，因为嘉维尔离开后，我有在了解外面的信息！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  哦？这么说来，你的打扮确实也和以前不一样了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  嗯，这可是外面非常流行的装扮呢！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  我不懂时尚，是这样吗，博士？
[Decision(options="在杂志上看到过。;......;我不知道。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  博士果然也看过吗！
[Predicate(references="2")]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嘉维尔，你的朋友不太懂时尚的样子呢。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  哈哈，博士也有不知道的时候啊。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  对了，特米米，先给博士介绍一下我们这里吧。我离开了这么久，也不知道有没有变化。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=2)]
[name="特米米"]  好的！
[name="特米米"]  唔，让我想想，要给外面的人讲的话......对了，要从部族开始呢。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="ac12_11",xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[dialog]
[Character]
[name="特米米"]  看看这张地图，这里是嘉维尔到达的地方，这里是咱们的过来的路径。
[name="特米米"]  这一大片丛林覆盖的区域就是阿卡胡拉了。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Image(image="ac12_8",xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  生活在阿卡胡拉的所有大大小小部族，根据传统，每隔一段时间，就会通过祭典的方式选出一名大酋长。
[name="特米米"]  啊，祭典的方式就是打斗，谁能战胜所有挑战者并赢得其他人的认可就能获得挑战现任大酋长的权利。
[name="特米米"]  战胜现任大酋长的话，就能成为新的大酋长。
[name="特米米"]  大酋长的权力的话，唔，所有部族都会听他的话！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  这不是基本没什么变化嘛。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  有的哦。
[Character(name="char_411_tomimi_1")]
[name="特米米"]  前任的胡安大酋长因为太喜欢喝酒被老婆追杀到悬崖边跳下去再也没有回来，本来上一次的祭典是要选出继任的大酋长的。
[name="特米米"]  但是，因为嘉维尔的关系，上次没有选出大酋长，而嘉维尔离开后，各个部族都互相不服气。
[name="特米米"]  所以现在各个部族之间陷入了互相斗争的状态。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[delay(time=0.5)]
[Decision(options="上一任大酋长......？", values="1")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  唔？这在我们这里是很常见的。
[name="特米米"]  据我阿爹说，胡安大酋长是当大酋长当的很久的一个了，一般大酋长两三年就会换掉。
[name="特米米"]  只要大酋长没了，就举办祭典选出一个新的。
[Decision(options="因为嘉维尔的关系？", values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  啊？哦，对，这事我确实没跟罗德岛的人说过。
[name="嘉维尔"]  我当时把祭典上所有人都打了一顿然后就走了。
[Decision(options="因为被排挤？;所有人？！", values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  对啊，我当时很气，就把他们都打了一顿。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  算了，这个先不提，现在有什么厉害的部族吗？
[Character(name="char_411_tomimi_1")]
[name="特米米"]  嗯。
[name="特米米"]  现在有几个部族比较厉害。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Im

... (全文11896字符)
```

### level_act12d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_071", name2="char_187_ccheal_1#1", focus=1)]
[name="阿达克利斯人A"]  噫，这、这招死亡大风车......还有这个发夹......你、你难道是嘉维尔！
[Character(name="avg_npc_071", name2="char_187_ccheal_1#3", focus=2)]
[name="嘉维尔"]  正是我！
[Character(name="avg_npc_071")]
[name="阿达克利斯人A"]  可恶，遇到你算我们倒霉。
[name="阿达克利斯人A"]  但是，就算你是嘉维尔，也别想动摇我们对粗尾巴的信仰！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.9)]
[delay(time=1)]
[Character(name="char_187_ccheal_1#4")]
[name="嘉维尔"]  既然这么嚣张就别逃啊！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  博士，我们走吧，下次碰到了再收拾他们。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嘉维尔，你怎么放过他们了。
[name="特米米"]  以前的你，遇到这种事肯定会把他们全追上打晕才解气的。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  是啊，以前的我会这样。
[name="嘉维尔"]  不过，我现在觉得他们还挺可爱的，对吧，博士。
[Decision(options="虽然听不懂，不过确实。;......;暴揍他们的你比较不可爱。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  虽然由我来说可能比较奇怪，不过这里都是些头脑简单的家伙。
[name="嘉维尔"]  哎，在外面动不动就要费脑子，有时候我也会怀念这里。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  喂，博士，你该不会也觉得粗尾巴比较好吧？
[name="嘉维尔"]  我可不同意啊！
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈！虽然我觉得他们可爱，但并不妨碍我揍他们啊。
[name="嘉维尔"]  这叫怎么说来着，对了，一码归一码！
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  嘉维尔......真的和以前不一样了呢。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嗯？等等，特米米，你这丫头。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  诶？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  几年不见，你的尾巴又变粗了啊。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  诶诶诶！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  你该不会也是粗尾巴那一边的吧？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  没有没有，我也不是自己想它才变这么粗的呀！
[name="特米米"]  呜呜，我也想要嘉维尔一样的细尾巴......
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  这样啊，啧啧，真是个可怜的孩子。
[name="嘉维尔"]  不过，刚才战斗的时候看了看，你的源石技艺变得挺厉害了啊。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  真、真的吗？！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  是啊，来我们罗德岛做个干员应该都没问题了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  干......员？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  干员就是呃，反正就是干活的，比如我就是医疗干员。
[name="嘉维尔"]  我记得我走的时候你还在巫医那里学习吧。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=2)]
[name="特米米"]  嗯！为了嘉维尔能够回来，我每天都在磨练自己！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=1)]
[name="嘉维尔"]  为了我？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  啊......唔，我是说，为了嘉维尔回来的时候能够帮上忙！就像刚才那样！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  好吧，那你确实帮上了忙。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=2)]
[name="特米米"]  诶嘿嘿......被嘉维尔夸奖了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=1)]
[name="嘉维尔"]  好了，总而言之，继续前进吧，我记得神庙就在前面不远了吧？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  嗯。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  森蚺绝对是大酋长啊，他们部族这么厉害。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  是啊，而且她自己也很强，以前不都说除了嘉维尔，就是森蚺了，现在嘉维尔不在......
[Character(name="avg_npc_070", name2="avg_npc_072", focus=2)]
[name="阿达克利斯人C"]  喂，看那边！
[Character(name="avg_npc_070", name2="avg_npc_072", focus=1)]
[name="阿达克利斯人B"]  那个难道是，嘉维尔？
[Character(name="avg_npc_071")]
[name="阿达克利斯人A"]  喂，嘉维尔，你终于回来了啊！
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  噢，好久不见啊！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  喂，你腰上这根羽毛这么好看，哪里来的？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  我用武器去跟依娜姆大姐换的。
[Character(name="avg_npc_070", name2="avg_npc_072", focus=2)]
[name="阿达克利斯人C"]  唉，你们部族真好，依娜姆大姐什么都搞得到，我也想去你们部族啊。
[Character(name="avg_npc_070", name2="avg_npc_072", focus=1)]
[name="阿达克利斯人B"]  不行，依娜姆大姐最讨厌人多了，不过你们要是有什么想要的，可以问我！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  好啊！......喂，看那边。
[Character(name="avg_npc_071", name2="avg_npc_072", focus=2)]
[name="阿达克利斯人C"]  那个，难道是嘉维尔！
[Character(name="avg_npc_070", name2="avg_npc_072", focus=1)]
[name="阿达克利斯人B"]  她居然回来了？！
[Character(name="avg_npc_072")]
[name="阿达克利斯人C"]  嘉维尔，你原来没死啊！
[Character(name="char_187_ccheal_1#4")]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="嘉维尔"]  我活得好好

... (全文10437字符)
```

### level_act12d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$bat_Imfxingback_intro", key="$bat_Imfxingback_loop", volume=0.4)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_187_ccheal_1",fadetime=1,block=true)]
[delay(time=0.6)]
[name="嘉维尔"]  博士，我稍微逛了一圈，没有看到其他人的样子。
[name="嘉维尔"]  看来我们可能要在祭典结束后再去雨林里找她们了。
[Character(name="avg_npc_070")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佩塔"]  ——！（胜利的战吼）
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  啊，是佩塔赢了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  这个叫佩塔的家伙挺能干啊，我都想和他打一架了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嗯，他是我的部族的勇士。
[name="特米米"]  但是，他肯定没有嘉维尔厉害。
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  哈哈，那可说不好呢。
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1#3", focus=2)]
[name="特米米"]  嘉维尔可是在小时候就差点夺得了大酋长的位置呢！才不会输给佩塔！
[Decision(options="小时候？",values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=1)]
[name="嘉维尔"]  嗯？哦，是那一次啊。
[name="嘉维尔"]  在我很小的时候，因为很有趣，其实有参加过一次祭典。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#3", focus=2)]
[name="特米米"]  嗯，那个时候的嘉维尔就已经非常厉害了！
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[name="阿达克利斯勇士"]  嘎哈......
[Character(name="avg_npc_070")]
[name="阿达克利斯冠军"]  荒野意志部族最强的家伙也不过如此！
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  好、好厉害......
[Character]
[name="阿达克利斯人A"]  啧，我们部族的勇士竟然被那么轻易地打败了。
[name="阿达克利斯人B"]  我们一起上吧！
[name="阿达克利斯人A"]  不行啊，比人数我们更加比不过......这一次只能放弃了吗......
[Character(name="avg_npc_070")]
[name="阿达克利斯冠军"]  还有谁要来挑战！没有的话，就由我来挑战大酋长！
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  我来！
[Character(name="avg_npc_070")]
[name="阿达克利斯冠军"]  你是......荒野意志部族的孤儿嘉维尔？
[name="阿达克利斯冠军"]  我听说你在小辈里很能打，但是小鬼没有资格参加祭典，滚回家去再喝几年奶吧。
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  哼，等你赢了我再说吧！
[Character(name="avg_npc_070")]
[name="阿达克利斯冠军"]  哈！不愧是孤儿，不怕死的吗！
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  部族的人就是我的亲人！少说废话，打不打！
[Character(name="avg_npc_070")]
[name="阿达克利斯冠军"]  哼，小鬼，找死！
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[delay(time=1)]
[name="阿达克利斯冠军"]  不、不可能......只是两拳就......
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  嘉维尔，好厉害......
[Character(name="char_187_ccheal_1#5")]
[name="嘉维尔"]  哼，也不过就这样嘛！
[name="嘉维尔"]  还有谁来挑战！
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[Decision(options="嘉维尔是孤儿？",values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嘉维尔没有说过吗？
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  我没说过吗？
[name="嘉维尔"]  哦，我好像真的没有说过，毕竟也不是什么特别重要的事。
[name="嘉维尔"]  我不知道我的父母是谁，不过这在这里不是什么很少见的事。
[name="嘉维尔"]  博士，虽然你可能无法想象，在这里，人要死是非常简单的事。
[name="嘉维尔"]  甚至不用天灾——其实这里的人根本不知道天灾是什么——一场感冒，一次恶劣天气说不定就会死不少人。
[name="嘉维尔"]  我想我的父母大概也就是这么随便死掉的吧。
[name="嘉维尔"]  哎，不说这个，反正你只要知道，我从小就是被部族的人一起养大的。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#5", focus=2)]
[name="特米米"]  嘉维尔......
[Decision(options="辛苦你了。;......;至少你现在比谁都健康。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  别这样，博士，搞得我好像很可怜一样。
[name="嘉维尔"]  孤儿也不只是我，在我们这里，几个家庭一起养大几个孤儿是很常见的事。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，别想太多。
[name="嘉维尔"]  我也是离开之后才知道，这种情况是不正常的。
[name="嘉维尔"]  这反而坚定了我学医的想法。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈哈，没错。
[Predicate(references="1;2;3")]
[Decision(options="所以那一次祭典的结果呢？",values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  那一次啊......
[playMusic(intro="$bat_Imfxingback_intro", key="$bat_Imfxingback_loop", volume=0.4)]
[Character]
[name="？？？"]  找到你了，可恶的赏金猎人！
[Character(name="avg_npc_070")]
[name="佩塔"]  什么人？！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嗯？这个声音......
[character]
[Dialog]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="char_2013_cerber_1",fadetime=1,block=true)]
[delay(time=0.6)]
[name="刻俄柏"]  把博士还回来！
[Character(name="avg_npc_070")]
[name="佩塔"]  你在说什么？
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  小刻？！
[name="嘉维尔"]  特米米，不是让你手下绑回部族去了吗？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  诶，是啊？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  这孩子力气不小，估计是直接挣脱了......
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  赏金猎人，把博士交出来！
[name="刻俄柏"]  不然即使是追到大地的尽头我绝对不会放过你的！
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  啧，这傻孩子看样子还没清醒过来。
[character]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佩塔"]  咕哈！
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  佩塔被打飞了！
[character]
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[na

... (全文6611字符)
```

### level_act12d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$bat_Imfxingback_intro", key="$bat_Imfxingback_loop", volume=0.4)]
[Character]
[name="阿达克利斯人A"]  这个怪胎好厉害！已经打退了好几个人了！
[name="阿达克利斯人B"]  虽然听不懂她在说什么，但是好强啊！
[name="阿达克利斯人C"]  让她来做大酋长感觉好像也不坏！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  ......嘉维尔，你的同伴好厉害。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  虽然这种时候只会让人伤脑筋就是了。
[name="嘉维尔"]  不过总算稍微消停了，我上去制住她......
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  什么，整合运动，你们又来了！
[name="刻俄柏"]  原来是你们抢走了博士吗！
[name="刻俄柏"]  别跑！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  糟了，这傻孩子要跑了！
[name="嘉维尔"]  我去追！特米米，你和博士不要乱动，我会回来找你们。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  诶，好的！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=1)]
[delay(time=1)]
[Character(name="char_411_tomimi_1#5")]
[name="特米米"]  ......
[Decision(options="......",values="1")]
[Predicate(references="1")]
[name="特米米"]  啊，上面又有新的人打起来了。
[name="特米米"]  ......博士，可不可以告诉我，嘉维尔在外面是什么样的？
[Decision(options="告诉她嘉维尔在罗德岛的生活。;......;告诉她嘉维尔当医生的样子。",values="1;2;3")]
[Predicate(references="1")]
[name="特米米"]  嘉维尔在外面生活得很好吗。
[name="特米米"]  ......
[Predicate(references="2")]
[name="特米米"]  难道说你和嘉维尔也不是很熟吗？
[name="特米米"]  太好了！......啊，不，我只是以为你和嘉维尔一起回来的，嘉维尔好像很喜欢你的样子，就以为你和嘉维尔关系很好。
[name="特米米"]  没关系的，嘉维尔人很好的，你一定可以和她打好关系的！
[Predicate(references="3")]
[Character(name="char_411_tomimi_1#3")]
[name="特米米"]  太好了，果然即使成为了医生，嘉维尔始终是嘉维尔呢！
[name="特米米"]  是这样啊，嘉维尔没有变呀，太好了......
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  那如果嘉维尔要离开你的话，你会怎么想？
[Decision(options="会很难过吧。;......;祝贺她找到新的道路吧。",values="1;2;3")]
[Predicate(references="1")]
[name="特米米"]  嗯，果然呢，我当时也哭的很伤心呢......
[Predicate(references="2")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  你、你怎么可以这样！嘉维尔那么好，她要离开你你怎么可以觉得无所谓！
[Predicate(references="3")]
[name="特米米"]  你真厉害......我做不到。
[name="特米米"]  我一直希望嘉维尔能够回来。
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  博士，那个，在嘉维尔的事情上，我、我是不会输给你的！
[Decision(options="加油。;（点头）;我也不会输给你的！",values="1;2;3")]
[Predicate(references="1;2;3")]
[Decision(options="所以那一次祭典的结果呢？",values="1")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  那一次......
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  什么嘛，你们这帮大人也不过如此嘛。
[name="嘉维尔"]  还有谁要来挑战我！
[Character]
[name="阿达克利斯人A"]  居然把这么多大人给打倒了......
[name="阿达克利斯人B"]  嘉维尔，了不起啊！
[name="阿达克利斯人C"]  难道说嘉维尔真的能当上大酋长？
[Dialog]
[Character(name="char_416_zumama_1",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  我来！
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  什么啊，怎么是你，祖玛玛。
[name="嘉维尔"]  你不是在造你的机器去了吗？我去找你你都不理我。
[Character(name="char_416_zumama_1")]
[name="祖玛玛"]  ......我想最后试一试。
[Character(name="char_187_ccheal_1",name2="char_416_zumama_1#2",focus=1)]
[name="嘉维尔"]  试什么？
[Character(name="char_187_ccheal_1",name2="char_416_zumama_1#2",focus=2)]
[name="祖玛玛"]  试试我的拳头能不能打败你。
[Character(name="char_187_ccheal_1",name2="char_416_zumama_1#2",focus=1)]
[name="嘉维尔"]  你怎么说得好像要死了一样。
[Character(name="char_187_ccheal_1",name2="char_416_zumama_1#2",focus=2)]
[name="祖玛玛"]  少废话，今天我可不会输给你，嘉维尔。
[Character(name="char_187_ccheal_1#3",name2="char_416_zumama_1#2",focus=1)]
[name="嘉维尔"]  嘿，那要打过才知道了！
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall",block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  她们从中午一直打到了晚上都没有分出胜负。
[name="特米米"]  到最后，她们两个人都没力气了，被其他人给丢了下去。
[name="特米米"]  这就是嘉维尔第一次参加祭典的情况了。
[Decision(options="祖玛玛是个什么样的人？",values="1")]
[Predicate(references="1")]
[name="特米米"]  祖玛玛是当时离得比较近的另一个部族的人。
[name="特米米"]  小时候，她和嘉维尔经常在一起打架，嘉维尔比她厉害，但祖玛玛也不是没有赢过。
[name="特米米"]  但是我听嘉维尔说，她有一天不知道怎么的，就不再喜欢打架了，开始喜欢研究机器。
[name="特米米"]  我记得那天，是祖玛玛最后一次和嘉维尔打架。
[name="特米米"]  在那之后，祖玛玛就再也没和嘉维尔打过，甚至很少出现在大家面前，再之后，她的部族就搬走了，我就在也没见过她了。
[name="特米米"]  就连嘉维尔离开那次的大闹祭典都没有来。
[Decision(options="......",values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  我回来了。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  嘉维尔，你没事吧！
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  我没事。啧，小刻这孩子真能跑，一下子就跑没影了。
[name="嘉维尔"]  不过以她的能力应该不用担心。特米米，祖玛玛来了吗？
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  还没有。
[Character(name="avg_npc_070")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阿达克利斯人"]  还有谁要来挑战！
[Character]
[name="？？？"]  我来。
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  嗯？看来我回来的正是时候。
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act12d0_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$bat_Imfxingback_intro", key="$bat_Imfxingback_loop", volume=0.4)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_416_zumama_1",fadetime=1,block=true)]
[delay(time=2)]
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[name="阿达克利斯人A"]  森蚺，森蚺！
[name="阿达克利斯人B"]  把他们全都解决掉，森蚺！
[name="阿达克利斯人C"]  大酋长，大酋长！
[name="阿达克利斯人D"]  森蚺，娶我！
[Character(name="avg_npc_071")]
[name="阿达克利斯勇士"]  ......森蚺，你果然来了。
[name="阿达克利斯勇士"]  我还以为你缩在自己的雨林里不敢来了。
[Character(name="char_416_zumama_1")]
[name="森蚺"]  雨林很好。
[Character(name="avg_npc_071")]
[name="阿达克利斯勇士"]  哼，缩在雨林里的提亚卡乌都是胆小鬼！
[Character(name="char_416_zumama_1")]
[name="森蚺"]  是不是胆小鬼，你马上就知道了。
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  祖玛玛这家伙，虽然身上多了些奇怪的装备，还是和以前一样啊。
[name="嘉维尔"]  哦，博士，我还没详细给你介绍过吧。
[name="嘉维尔"]  台上那个女孩叫祖玛玛，我们不是一个部族，不过以前离得比较近，年纪又差不多，算是一起长大的。
[name="嘉维尔"]  这家伙虽然不爱说话，但其实也挺厉害。
[name="嘉维尔"]  不过不知道什么时候起，她就变得怪怪的，虽然还是很能打，但是没事的时候会老是自己在捣鼓一些怪东西。
[name="嘉维尔"]  在那之后她部族搬走了，我们就见的比较少。
[name="嘉维尔"]  听说她还是很厉害，但是好像染上了怪病，会和没人的地方说话。
[name="嘉维尔"]  我在罗德岛的时候还特地查过类似的症状，感觉是精神方面的问题，不过她现在看起来还挺正常的。
[name="嘉维尔"]  上次祭典的时候我还以为她会来的，结果她没来，我还挺遗憾的。
[name="嘉维尔"]  没想到现在她开始自称森蚺，既然她来了，上面这个人应该没戏了。
[Dialog]
[character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_071")]
[name="阿达克利斯勇士"]  咕哈！
[character]
[Dialog]
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[Character(name="char_187_ccheal_1#5")]
[name="嘉维尔"]  哈，果然，这家伙也变强了啊，真想和现在的她打一架啊！
[Character(name="char_187_ccheal_1#5", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  果然，祖玛玛很强，但是......
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  嗯？那边的是......
[Character]
[name="阿达克利斯人"]  森蚺，我们来挑战你。
[Character(name="char_416_zumama_1")]
[name="森蚺"]  你们是？
[Character(name="avg_npc_071")]
[name="阿达克利斯人"]  我是猛火部族的族长，乌代！
[Character(name="avg_npc_070")]
[name="阿达克利斯人"]  我是刀疤部族的族长，阿鲁纳！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=0)]
[name="乌代&阿鲁纳"]  小的们，上来！
[Dialog]
[character]
[PlaySound(key="$d_gen_soldiersrun", volume=0.6)]
[delay(time=1)]
[Character(name="char_416_zumama_1")]
[name="森蚺"]  你们要一起上吗？
[Character(name="avg_npc_071")]
[name="乌代"]  嘿，我们之间达成了协......什么来着？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿鲁纳"]  蠢货，那叫协议！
[Character(name="avg_npc_071")]
[name="乌代"]  哦对，协议！
[Character(name="avg_npc_070")]
[name="阿鲁纳"]  可别以为你可以轻易当上大酋长！
[Character(name="char_416_zumama_1")]
[name="森蚺"]  我没有这么想过。不过，我没听说过你们有这么团结。
[Character(name="avg_npc_071")]
[name="乌代"]  这是我们自己的事。
[Character(name="avg_npc_070")]
[name="阿鲁纳"]  嘿，我只是看不惯你这种捣鼓机器的家伙来当大酋长！
[Dialog]
[character]
[delay(time=1)]
[Decision(options="祭典可以上许多人的？;......;难道不是一对一吗？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  诶？嗯，是的。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，看你的表情，你该不会以为祭典是什么擂台赛节目吧。
[Predicate(references="3")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  诶？这样不会花很长时间吗？
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  虽然很多时候为了尊严，大家伙都是一对一的，但本身祭典唯一的规则就是无论用什么手段，谁能赢到最后谁就是大酋长。
[name="嘉维尔"]  带小弟当然是最简单有效的办法了。
[Decision(options="无论什么手段？;......;听起来我也可以当酋长。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，你该不会也想上吧，我建议你放弃。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  啊，博士，你现在肯定在想些坏事吧。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  哈哈哈，博士，很遗憾，你不行的。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  我说的无论用什么手段，可不是博士你想的那些。
[name="嘉维尔"]  我们这里的人很单纯的，不管干啥，也只会想到带很多人一起上。
[name="嘉维尔"]  拐弯抹角的阴险招数在这里可没人会用。
[name="嘉维尔"]  老实说，就算是我在罗德岛呆了好几年，我也不擅长去搞那些小心思。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嗯，而且群殴也是有风险的呢。
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  哈哈，没错，打完之后自己闹内讧的事可不少见。
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  而且另一方面，说是说所有手段都可以用，但是博士你可以真的试一试用你的手段解决其他人。
[name="嘉维尔"]  我保证最后是你会被群殴。
[Decision(options="别把人说得那么坏。;......;民风淳朴啊。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  哈哈哈，我只是实话实说。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  哈哈，能看到博士你翻白眼的样子可真少见。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  是啊，我也是出去了才知道，原来我的家乡这么淳朴。
[name="嘉维尔"]  以前我可是觉得，所有地方的人都是一样的。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  虽然我觉得博士你能做到让所有人都察觉不到是你做的，但是，博士，你知道决定性的差异在哪里吗？
[Decision(options="肌肉？;......;外表？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  没错！你看起来就很弱啊。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  喂，博士，别赌气不听我说话嘛！
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  是可以这么说，毕竟博士你看起来就弱不禁风的样子。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  总之呢，说白了，想要当上大酋长，其实只有一个条件。
[name="嘉维尔"]  那就是——够强，拳头够硬，够能打！
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  对吧，特米米？
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  诶，嗯，嗯！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  不过真是怪了，我记得这两个人可不是什么好朋友，他们居然会联手。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  唔唔，大概是在嘉维尔你离开后关系变好了吧。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name=

... (全文6995字符)
```

### level_act12d0_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$bat_Imfxingback_intro", key="$bat_Imfxingback_loop", volume=0.4)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="阿达克利斯喽喽A"]  嘎哈......
[name="阿达克利斯喽喽B"]  太、太强了......
[Character(name="avg_npc_071")]
[name="乌代"]  算你厉害！
[Character(name="avg_npc_070")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="阿鲁纳"]  森蚺，别得意！
[name="阿鲁纳"]  小的们，上！
[Character]
[Dialog]
[Character(name="char_416_zumama_1#2")]
[name="森蚺"]  ......
[Character(name="char_411_tomimi_1")]
[name="特米米"]  唔，不愧是祖玛玛，果然很厉害。
[name="特米米"]  虽然只有一个人，一般的阿达克利斯也不是她的对手，就像嘉维尔一样。
[name="特米米"]  但是......
[Decision(options="你好像很熟悉她。;......;好帅的女孩子。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  嗯，祖玛玛和嘉维尔从前开始就是我们这一带最厉害的两个人呢。
[name="特米米"]  不过据我所知，祖玛玛从来没有赢过嘉维尔哦！
[Predicate(references="2")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  博士。在外面这么厉害的人一定很少见吧！
[name="特米米"]  但是，嘉维尔更厉害哦！
[Predicate(references="3")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  唔，虽然祖玛玛确实很帅。
[name="特米米"]  但是，嘉维尔更帅！
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  对吧，嘉维尔？
[name="特米米"]  咦，嘉维尔呢？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  喂，你们看，那个人是！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  我刚才在来的路上就看到了，她是——
[Character(name="avg_npc_070", name2="avg_npc_072", focus=2)]
[name="阿达克利斯人C"]  她居然真的回来了！
[Character(name="char_416_zumama_1")]
[name="森蚺"]  你是——
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="所有人"]  嘉维尔！
[Character(name="char_411_tomimi_1")]
[name="特米米"]  哇啊啊啊啊，嘉维尔直接冲上台了！
[Character]
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_187_ccheal_1#3",fadetime=1,block=true)]
[delay(time=1)]
[name="嘉维尔"]  好久不见啊，祖玛玛！
[name="嘉维尔"]  现在应该叫你森蚺头领了对吧。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  你居然回来了，嘉维尔。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#2", focus=1)]
[name="嘉维尔"]  是啊，特米米叫我回来的。
[name="嘉维尔"]  嗯？等等，你居然也会说萨尔贡语？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  ......既然你也会这种语言，看来这种语言确实是外面的语言没错。
[name="森蚺"]  我学习了很久。
[name="森蚺"]  ......我以为你不会再回来了。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#2", focus=1)]
[name="嘉维尔"]  我会回来的，不是现在，未来也会回来的，这里是我的家。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  ......你要当大酋长？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#2", focus=1)]
[name="嘉维尔"]  不，本来我只是找你有点事，打完再找你也没关系的。
[name="嘉维尔"]  但是，你这家伙变得这么厉害了，这让我怎么忍得住啊！
[Dialog]
[Character(name="char_187_ccheal_1#3")]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_416_zumama_1#2")]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  你真的去做医生了？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  是啊。
[name="嘉维尔"]  嘿，我在外面可是很有名的医生！
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  真意外。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  你呢，上次的时候你不是在捣鼓自己的东西没有参加吗？终于捣鼓好了？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1#3", focus=2)]
[name="森蚺"]  ......是。
[name="森蚺"]  你马上就会见到。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_411_tomimi_1#4")]
[name="特米米"]  呜呜呜，嘉维尔不是说她不会出手的吗......
[Decision(options="嘉维尔出乎你的意料了？;......;这才是嘉维尔。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  诶？没、没有的事！只、只是.......
[Predicate(references="2")]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  博士也看入迷了......
[name="特米米"]  呜呜，虽然确实很帅，但是......
[Predicate(references="3")]
[Character(name="char_411_tomimi_1#4")]
[name="特米米"]  呜呜，虽然这么说是没错。
[Predicate(references="1;2;3")]
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$livecrowd", volume=0.7, loop=false, channel="people")]
[Character(name="char_416_zumama_1#2",fadeti

... (全文8967字符)
```

### level_act12d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，我们已经来到雨林深处了。
[name="嘉维尔"]  这里比之前还要潮湿，树木也要更加茂密。
[name="嘉维尔"]  注意你的脚下，小心别被绊倒了。
[name="嘉维尔"]  前面有一个部族，我们可以过去看看。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_075",fadetime=1,block=true)]
[delay(time=1)]
[name="依娜姆"]  呼啊，好无聊，睡个午觉好了......
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  依娜姆！
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  嘉维尔？我听说你在祭典上被祖玛玛打败了，怎么到我这来了？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  消息真灵通啊，依娜姆。
[name="嘉维尔"]  不过，听特米米提到的时候我还不信，没想到你这家伙还真当上部族的头领了。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  我也不想的啊，这帮人擅自要跟着我，我有什么办法。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  你怎么没有来祭典？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  博士，这就是特米米介绍过的依娜姆了。
[Decision(options="你好。;......;嗨！",values="1;2;3")]
[Predicate(references="1")]
[Character(name="avg_npc_075")]
[name="依娜姆"]  哇，是活的外地人。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  嘉维尔，这是你在外面带回来的朋友？怎么这么害羞。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  博士只是不怎么喜欢说话而已。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  哟！嘉维尔，你这个朋友和你一样开朗啊。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1#2", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  嗯？依娜姆，怎么你也会萨尔贡语？
[Character(name="char_187_ccheal_1#2", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  我的官方身份是这一带的信使啊。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  信使？哈？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  你......唉，算了，你这个反应，好歹看得出你已经知道信使是什么了。
[name="依娜姆"]  不像别的家伙，我就算跟他们说信使，他们也不知道是什么东西。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  等等，你什么时候变成信使的？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  我从一开始就是信使......
[name="依娜姆"]  这里好歹也是萨尔贡境内诶，你该不会觉得萨尔贡对这一片区域真的一无所知吧。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  啥，不是吗？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  当然不是，据我所知，这里几百年前，其实是萨尔贡某聚落的一个矿场。
[name="依娜姆"]  但是当时因为天灾的原因，那座移动城市离开了，这片矿场也就废弃了。
[name="依娜姆"]  当时留下的人以及后来回来的人基本形成了现在的人口。
[name="依娜姆"]  原本官方好像也是想过把最近的移动城市开过来重新利用一下的想法。
[name="依娜姆"]  就十几年前，你也知道的那次。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  哦，那一次啊，我和祖玛玛都看到过，那家伙从那天起就变得怪怪的。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  是吗？哎，不过最后我也不知道是因为什么放弃了，大概是勘测了一下发现这片矿区没有那么有价值吧。
[name="依娜姆"]  毕竟如果要把城市停在这片区域，和别的城市的距离就太远了。
[name="依娜姆"]  听说很久以前这片无人区好像还是挺繁荣的，也不知道是多久以前了。
[name="依娜姆"]  算了，不说这个，反正我大概嗯？是几岁来着？算了，反正成为信使后就被派到这里来了。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  哦。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  唉，我难得找到人说这些话题，你就不能假装听得津津有味一点。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  麻烦。不过，既然你是信使，为什么我感觉以前从没见你离开过这里？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  那当然是因为，这里这么封闭，我除了想去城里买点东西，根本没有信要寄啊！
[name="依娜姆"]  从我开始当信使到今天，真正出去了还和这里有联系的人，只有你一个！
[name="依娜姆"]  因为实在没事做，我干脆就没事去最近的城市买点东西回来和大家做做生意。
[name="依娜姆"]  久而久之，就变成大家口中做生意的依娜姆了。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  原来如此，我以前都没发现。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  就你以前那样能发现才怪了......
[name="依娜姆"]  不过，虽然我算是在城市里长大，现在我也更喜欢在这边的生活就是了。
[name="依娜姆"]  简简单单，没什么不好的。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  我也一直都觉得你和雨林里其他黎博利没啥区别。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  我就当你是在夸我了，所以你找我有什么事？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  我先问一问，AUS是怎么回事？不会是你找来的吧？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  AUS？怎么可能，她们可是就算是我这样没什么见识的人都听过名字的乐队，我哪里请得来。
[name="依娜姆"]  倒不如说，我看到她们的时候才是最吃惊的那一个好不好。
[name="依娜姆"]  她们真的只是路过而已，那段时间还是我给她们做的翻译呢。
[name="依娜姆"]  哎呀，说到这个我就来劲了，你来得正好，不懂的人我都不知道该怎么向他吹嘘这件事。
[name="依娜姆"]  我还有她们的亲笔签名唱片呢，你要不要看看？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  算了，我又不是她们的粉丝，只是觉得有点不可思议而已。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  哎，看起来你在外面这么久，品味没有见长啊，嘉维尔。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  小心我揍你啊？比起这个，我和博士正要去找祖玛玛，路过你这里，就想在你这里补给一下。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  好啊。虽然老规矩是以物易物，不过既然你已经知道外面什么样了，你也可以用流通货币跟我交易。
[name="依娜姆"]  ......哦，等等，被你一串问题给问懵了，差点忘了我其实也有事找你。
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  啊？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  你有没有一个叫可颂的朋友？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=1)]
[name="嘉维尔"]  可颂？她和我们一起的，我们正在找她呢，你见到她了？
[Character(name="char_187_ccheal_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  你可以去集市那边看看。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  走

... (全文10002字符)
```

### level_act12d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  所以你怎么会带着这群阿达克利斯来袭击的？
[Character(name="char_187_ccheal_1#2", name2="char_337_utage_1", focus=2)]
[name="宴"]  唔，我只是看到这里有个村庄，就想着打群架应该挺好玩的......
[Character(name="char_337_utage_1", name2="char_201_moeshd#3", focus=2)]
[name="可颂"]  ......该说不愧是你吗，一旦涉及到战斗，就完全变了个人呢。
[Character(name="char_337_utage_1", name2="char_201_moeshd#3", focus=1)]
[name="宴"]  呜呜，对不起啦。
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=1)]
[name="嘉维尔"]  不过，你这家伙到底是怎么做到语言不通还能使唤这群家伙的。
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=2)]
[name="宴"]  关于这个，其实我也不是很清楚。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_337_utage_1")]
[name="宴"]  啊，我的美甲被刮到了，好烦。
[name="宴"]  美甲套装在掉下来的时候也不知道飞哪儿去了，好烦乘二。
[name="宴"]  打架出了好多汗，这里的空气又这么潮，衣服都湿透了，好烦乘三。
[name="宴"]  而且我明明只是在这里走路，为什么不停地有阿达克利斯来和我打架啊，好烦乘四。
[Character(name="char_337_utage_1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="宴"]  而且，说到底，一开始是说这里是个度假的好地方我才来的，但是这里哪里像度假胜地啊！
[Character(name="char_337_utage_1")]
[Delay(time=1)]
[name="宴"]  嗯？有人在悄悄靠近我？那些人是......阿达克利斯？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_337_utage_1")]
[name="宴"]  然后，我就把靠近我的那些人全都打了一顿。
[name="宴"]  后来，又有更多的人来，我就又把他们打了一顿。
[name="宴"]  打到最后，他们不知道为什么就对我毕恭毕敬的了。
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  哦，我懂了，他们可能把你当成新奇的动物了，毕竟我们这里没有长你这样的人。
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="宴"]  哈？！我这样青春可爱的美少女哪里像动物了！
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  呃，老实说，从阿达克利斯的角度来看，你可能确实像个怪胎。
[name="依娜姆"]  而且我看到跟随你的这群人里，有巨木部族的族长，问了他一下，他说，现在你才是巨木部族的族长。
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=1)]
[name="宴"]  诶？
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  也就是说，你把一支部族的族长打败了，他们认为你是新的族长，所以才会跟着你。
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=1)]
[name="宴"]  诶？他们明明听不懂我说话，这也行？！我还以为他们只是好玩才跟着我的......
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=2)]
[name="依娜姆"]  在这里，你只要够强大，就可以。
[Character(name="char_337_utage_1", name2="avg_npc_075", focus=1)]
[name="宴"]  这可怎么办啊，博士......
[Decision(options="你自己解决。;......;不如你就留在这里当族长好了。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_337_utage_1")]
[name="宴"]  呜呜呜，博士好绝情！
[Predicate(references="2")]
[Character(name="char_337_utage_1")]
[name="宴"]  呜呜，博士不要用那种眼神看我嘛。
[name="宴"]  我又不是故意的......
[Predicate(references="3")]
[Character(name="char_337_utage_1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="宴"]  诶，我才不要！我才不要过没电视没空调的生活！
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  算了，至少找到了你和可颂，现在就剩下煌了。
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=2)]
[name="宴"]  煌大姐应该不会有事吧，想象不出她出事的样子诶。
[Character(name="char_201_moeshd")]
[name="可颂"]  是啊。对了，博士，接下来我们要去干什么，去神庙参加嘉维尔说的祭典吗？
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哦，对，忘了你们不知道，博士，你来解释一下吧。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
向宴和可颂解释了一下现状。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_201_moeshd")]
[name="可颂"]  嗯嗯，原来如此，所以我们现在是要去找那个叫祖玛玛的人要回引擎对吗？
[Character(name="char_187_ccheal_1", name2="char_201_moeshd", focus=1)]
[name="嘉维尔"]  没错。
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=2)]
[name="宴"]  诶？祭典就这么结束了吗？
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=1)]
[name="嘉维尔"]  是啊。
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=2)]
[name="宴"]  那我不是白来了吗！
[name="宴"]  算了，反正听起来就是那种我不会很感兴趣的东西。
[name="宴"]  比起这个，嘉维尔，说好的这里适合度假呢！
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=1)]
[name="嘉维尔"]  啊？你不觉得这里环境很好吗？
[Character(name="char_187_ccheal_1", name2="char_337_utage_1", focus=2)]
[name="宴"]  虽然，确实，是这样，没错！
[name="宴"]  但是，这里一点也没有度假的要素啊！
[Character(name="char_187_ccheal_1#2", name2="char_337_utage_1", focus=1)]
[name="嘉维尔"]  度假的要素是什么样的啊？
[Character(name="char_187_ccheal_1#2", name2="char_337_utage_1", focus=2)]
[name="宴"]  当然是，海边，沙滩，阳伞，冰淇淋啊！
[name="宴"]  为了这个，我还特地准备了新的泳装，而且出发前就穿在衣服下面了！
[Character(name="char_337_utage_1", name2="char_201_moeshd", focus=2)]
[name="可颂"]  诶，我倒是单纯地没有什么事做就跟来看看了......
[Character(name="char_187_ccheal_1#2", name2="char_201_moeshd#3", focus=1)]
[name="嘉维尔"]  呃，我一开始就没说过有这种东西吧。
[Character(name="char_187_ccheal_1#2", name2="char_337_utage_1", focus=2)]
[name="宴"]  你不是说可以玩水的吗！
[Character(name="char_187_ccheal_1#3", name2="char_337_utage_1", focus=1)]
[name="嘉维尔"]  那确实有啊，雨林深处有一座大瀑布，我们可以在那里玩水。
[name="嘉维尔"]  而且为了去祖玛玛的部族，我们肯定要经过大瀑布。
[name="嘉维尔"]  别说你，我也带了泳装呢，只不过我没拿出来而已。
[Character(name="char_187_ccheal_1#3", name2="char_337_utage_1", focus=2)]
[name="宴"]  真的吗，好耶！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungle_1",screenadapt="c

... (全文9599字符)
```

### level_act12d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_416_zumama_1#5",fadetime=1,block=true)]
[delay(time=2)]
[name="森蚺"]  大祭司，状态怎么样？
[Character(name="avg_npc_074",fadetime=1,block=true)]
[delay(time=2)]
[name="大祭司"]  噢，我不得不说，开炮的声音吓到我了，我在开炮的时候差点就飞出去了！
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=2)]
[name="森蚺"]  我问的是大丑。
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=1)]
[name="大祭司"]  我只是顺便提一下我的状况。大丑和预想的一样，连续开炮会导致过热。
[name="大祭司"]  但是效果很好，嗯，我不得不说，效果非常好！虽然我确实被吓到了！
[name="大祭司"]  总之回到部族之后，还要好好修一修！
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=2)]
[name="森蚺"]  嗯，这次的祭典太急了，大丑还没有准备好。
[name="森蚺"]  原本我想等大丑准备好再和其他部族商量重新举办祭典的，结果现在就举行了。
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=1)]
[name="大祭司"]  没关系，结果好就行了！
[name="大祭司"]  我还记得那些小家伙们看到大丑时脸上吃惊的表情！哈哈，太有趣了！
[Character(name="avg_npc_074",name2="char_416_zumama_1#5",focus=2)]
[name="森蚺"]  嗯，目的已经达到了。
[Character(name="avg_npc_074",name2="char_416_zumama_1#5",focus=1)]
[name="大祭司"]  接下来，这里将迎来新的秩序，新的时代！噢，机械时代！听起来太棒了。
[name="大祭司"]  你觉得叫“大丑时代”怎么样？哦，我觉得“大祭司时代”也不错，听起来和我一样酷炫。
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=2)]
[name="森蚺"]  就叫机械时代就好了。
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=1)]
[name="大祭司"]  哎，你这孩子什么都好，就是太古板了，既然学习了外面的知识，就应该看到更多的东西！
[name="大祭司"]  你看我，这一身打扮，不觉得很潮流，很有知性吗？
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=2)]
[name="森蚺"]  太矮了根本就看不到，不过潮流是什么？
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=1)]
[name="大祭司"]  噢，算了，对不起，我不该和你聊这个话题，但是没关系，我会亲自为你挑选一套适合大酋长身份的衣服的！
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=2)]
[name="森蚺"]  衣服随便，比起这个，留在部族的人刚才传来消息，他们抢到了一个引擎。
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=1)]
[name="大祭司"]  什么？真的吗？
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=2)]
[name="森蚺"]  嗯，好像是从嘉维尔回来的载具上抢来的。
[Character(name="avg_npc_074",name2="char_416_zumama_1",focus=1)]
[name="大祭司"]  太好了，我迫不及待地想要看到它了！
[name="大祭司"]  哦，这么一说，我直接去看看不就好了，那我先走了！
[Character(name="char_416_zumama_1#5")]
[name="森蚺"]  大祭司还是老样子。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  喂，族长身边那只黎博利是谁啊？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  你是新来的吧？那是大祭司大人！开大丑的！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  什么，我也想开大丑啊！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  算了吧，你是不知道，以前大丑还没完成的时候，天天爆炸，弄伤了好几个弟兄，到后来谁都不敢坐上去了。
[name="阿达克利斯人B"]  然后大祭司大人就来了，别小看他，他每次被炸飞出去都能活着回来！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  啊？这么厉害？！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  是啊，虽然不知道他以前是哪个部族的，但是我们现在都叫他大祭司大人！
[Character(name="avg_npc_071")]
[name="阿达克利斯人A"]   嗯？那边的不是尤吉吗？喂，尤吉。
[Character(name="avg_npc_070")]
[name="尤吉"]  是你们啊。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  你不是和你哥哥在一起吗？你哥哥呢？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]  我正要为这个去找族长。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阿达克利斯人A"]  蠢货，现在要叫大酋长！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="尤吉"]  哦，我正要为这个去找大酋长。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  怎么了？
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  大酋长，我哥哥得了石头病。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  说萨尔贡语。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  啊，是，对不起，我还不怎么熟练。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  ......他怎么得的？
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  哥哥之前为了采到更多的矿，不顾我的反对一个人去了里面的矿区......
[Character(name="avg_npc_070", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  那个蠢货，我不是说过绝对不能深入矿区的吗！
[name="森蚺"]  他现在人呢？
[Character(name="avg_npc_070", name2="char_416_zumama_1#2", focus=1)]
[name="尤吉"]  他现在被嘉维尔带走治疗了。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  嘉维尔？
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  嗯，嘉维尔好像真的成了医生，本来哥哥很难受的样子，她三两下就让哥哥看起来好多了。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  ......原来成为医生不是谎话吗。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  嘉维尔还让我给你带话。
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  她说什么？
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  她说她有事来找你，她好像很生气的样子。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  嘿，肯定是被族长打败不服气！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  没错，族长那一下，轰！实在是太厉害了！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  你忘了叫大酋长！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  你也忘了！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  烦死人了，混账，族长就是族长！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  你才烦死人了！我就是改不过口来！
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.6, xstrength

... (全文11254字符)
```

### level_act12d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[name="？？？"]  怎么只有你们？
[Character(name="avg_npc_071")]
[name="族长A"]  巨木部族的人不见了，我听说好像他们的首领被一个外来者打败了。
[Character(name="avg_npc_070")]
[name="佩塔"]  火石部族还有粗尾部族被一个不知道哪里来的背着很多武器的家伙给全打趴下了。
[Character(name="avg_npc_071")]
[name="族长A"]  还有几个部族选择了加入祖玛玛的部族。
[Character(name="avg_npc_070")]
[name="族长B"]  老实说，祖玛玛搞出来的阵仗真厉害，要不是我是嘉维尔的追随者，说不定也要去加入祖玛玛了。
[Character]
[name="？？？"]  ......没关系。
[name="？？？"]  有你们几个部族的人也足够了。
[Character(name="avg_npc_070")]
[name="族长B"]  喂，我们真的能战胜祖玛玛吗？
[Character]
[name="？？？"]  嗯。
[name="？？？"]  嘉维尔一定能够战胜祖玛玛的巨大机器，到时候，就由我来成为大酋长，让嘉维尔留下来。
[Character(name="avg_npc_070")]
[name="佩塔"]  佩塔觉得，这样不好。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="ac12_6",xScale=1, yScale=1, fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[name="？？？"]  .......
[name="？？？"]  但是，这是唯一能让嘉维尔留下来的方法。
[name="？？？"]  不要忘了，我们是为了什么才成立的“嘉维尔意志”！
[name="？？？"]  “嘉维尔意志”不只是一个部族，是我们所有希望嘉维尔成为大酋长的人的联盟！
[Character(name="avg_npc_070")]
[name="族长B"]  我支持特米米，我只认嘉维尔做大酋长。
[Character(name="avg_npc_071")]
[name="族长A"]  没错，嘉维尔才是应该领导我们的人！
[Character(name="avg_npc_070")]
[name="族长C"]  嘿，要是我不同意，我就不会站在这里了！
[name="佩塔"]  ......佩塔不喜欢，但是佩塔会做。
[Character]
[name="？？？"]  那么你们到了祖玛玛部族外面等我来找你们，明白了吗？
[name="其他族长"]  好。
[name="？？？"]  那么，一切都是为了嘉维尔。
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[name="其他族长"]  一切都是为了嘉维尔！
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image(fadetime=0)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[PlaySound(key="$leaveshake", volume=0.6)]
[Character(name="char_017_homura_summer")]
[name="煌"]  博士，还有其他人也在！太好了，终于找到你们了！
[name="煌"]  唉，博士，你可把我担心坏了。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=1)]
[name="嘉维尔"]  嗯？煌，你怎么就把泳装穿——你的背上怎么还有个人？
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=2)]
[name="煌"]  这小姑娘是我刚才走在路上遇到的，也不知道怎么回事见面就打我。
[name="煌"]  那我肯定打回去啊，就把她和她手下全给打趴下了。
[name="煌"]  不得不说这小姑娘身手还不错，也挺抗打，我就带上了，想着找到你之后让你帮我问问为什么要打我。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=1)]
[name="嘉维尔"]  哦，克玛尔的话，我觉得她大概就是单纯看你挺厉害，就想跟你打一架，这家伙可是个战斗狂。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=2)]
[name="煌"]  哈，能被你这么评价的家伙还真是稀奇啊。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=1)]
[name="嘉维尔"]  我又不是战斗狂，我只是习惯用比较直接的方法解决问题而已啊。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=2)]
[name="煌"]  行行行。
[Dialog]
[Character]
[Character(name="char_415_flint_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="燧石"]  ......这里是......哪里......
[Character(name="char_187_ccheal_1", name2="char_415_flint_1#2", focus=1)]
[name="嘉维尔"]  你醒了，克玛尔。
[Character(name="char_187_ccheal_1", name2="char_415_flint_1", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="燧石"]  嘉维尔？！你怎么在这里？
[Character(name="char_187_ccheal_1", name2="char_415_flint_1", focus=1)]
[name="嘉维尔"]  你遇到了我的同伴，对她出手然后被她打倒了。
[Character(name="char_415_flint_1", name2="char_017_homura_summer", focus=2)]
[name="煌"]  嘿，你终于醒了，小姑娘。
[Character(name="char_415_flint_1#3")]
[name="燧石"]  ......
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="煌"]  喂，嘉维尔，她干什么，怎么刚醒就忽然向我弯腰了？！
[Character(name="char_187_ccheal_1#2", name2="char_415_flint_1", focus=1)]
[name="嘉维尔"]  克玛尔，你要干什么？
[Character(name="char_187_ccheal_1#2", name2="char_415_flint_1", focus=2)]
[name="燧石"]  我在她身上感受到了连我在祖玛玛身上都没感受过的更纯粹的强大。
[name="燧石"]  嘉维尔，我对你失去兴趣了。你好像能和她交流，帮我告诉她，请指导我。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=1)]
[name="嘉维尔"]  哦，她说让你教她。
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=2)]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="煌"]  啥？！
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=1)]
[name="嘉维尔"]  大概意思就是觉得你太强了，想做你小弟，这样的感觉吧。
[Character(name="char_017_homura_summer")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="煌"]  ......博士，怎么办啊，我从没遇到过这种事！
[Decision(options="这要由你来决定。;......;不关我事。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=2)]
[name="煌"]  呃，要不让她先跟着我们？
[Character(name="char_187_ccheal_1", name2="char_017_homura_summer", focus=1)]
[name="嘉维尔"]  也行，喂，克玛尔，你先跟着我们好了。
[Character(name="char_187_ccheal_1", name2="char_415_flint_1", focus=2)]
[name="燧石"]  好。
[name="燧石"]  不过，现在，叫我燧石。
[Character(name="char_017_homura_summer")]
[name="煌"]  说起来，祭典怎么样了？
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，你来给煌讲解一下。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_017_homura_summer")]
[name="煌"]  不惜让手下感染矿石病也要造机器？
[Character(name="char_017_homura_summer")]
[name="煌"]  嘿，这我可不能坐视不管。
[Character(name="char_017_homura_summer")]
[name="煌"]  那还等什么，博士，继续前进吧！
[Character(name="char_337_utage_1")]
[name="宴"]  不过，我们还有另一个地方要去！
[Character(name="char_017_homura_summer")]
[name="煌"]  啊？
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act12d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[name="大祭司"]  哇啊啊啊啊！
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="avg_npc_071")]
[name="阿达克利斯人A"]  啧，又失败了，不过这次飞的弧度不错啊。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  飞哪儿去了？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  不知道，反正待会儿就跑回来了吧，我们继续。
[name="阿达克利斯人A"]  那么，这根管子该接哪里呢——
[name="阿达克利斯人A"]  哈哈，这个接口长的很正点啊，就插你了！
[name="阿达克利斯人A"]  喂，能发动吗？
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  不行啊，你到底会不会啊！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  叫什么叫，这个引擎我从来没见过，让我多试试！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  让我来试试！
[name="阿达克利斯人B"]  照我看，这根管子应该插这里，然后这个按钮是啥？算了，按了就对了。
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  你这家伙才是在乱搞啊！明明应该这样插才对！
[Character(name="avg_npc_072")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阿达克利斯人C"]  你们两个蠢货在干什么，油管都没插上，还是得我来！
[name="阿达克利斯人C"]  油管该插哪儿来着，算了，这个口比较大，就你了！
[name="阿达克利斯人C"]  喂， 谁来启动一下试试！
[Character(name="avg_npc_074")]
[name="大祭司"]  我回来了！
[name="大祭司"]  现在的年轻人真是不懂尊敬老人，我被炸出去了也没有人来找我一下吗！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=1)]
[name="阿达克利斯人A"]  可是大祭司大人你每次都会像现在这样好好地跑回来啊，大家都习惯了！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  哎呀，别废话了，赶紧启动试试！
[Character(name="avg_npc_074")]
[name="大祭司"]  好好好。
[Dialog]
[Character]
[playsound(key="$smallearthquake", volume=0.6)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=false)]
[name="大丑"]  ————！
[Character(name="avg_npc_074")]
[name="大祭司"]  大丑，我的好孩子，该起床了！
[Dialog]
[Character]
[playsound(key="$smallearthquake", volume=0.6)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=false)]
[Dialog]
[Character]
[Character(name="avg_npc_071")]
[name="阿达克利斯人A"]  噢！大酋长，它终于动了！
[Character(name="avg_npc_071", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  这美妙的引擎声！我从来没听过这么动听的声音！
[Character(name="avg_npc_070", name2="avg_npc_072", focus=2)]
[name="阿达克利斯人C"]  哈哈，我就说还是得我来！
[Character(name="avg_npc_072", name2="char_416_zumama_1#6", focus=2)]
[name="森蚺"]  你们是怎么做到的？
[Character(name="avg_npc_071", name2="char_416_zumama_1#6", focus=1)]
[name="阿达克利斯人A"]  就像你看到的一样啊，大酋长，它就是这样动了！
[Character(name="char_416_zumama_1#6", name2="avg_npc_070", focus=2)]
[name="阿达克利斯人B"]  把这根管子插在这里，然后把那根管子插在那里！
[Character(name="avg_npc_072", name2="char_416_zumama_1#6", focus=1)]
[name="阿达克利斯人C"]  就像我们怎么造出的大丑一样！
[Character(name="char_416_zumama_1")]
[name="森蚺"]  很好。
[Character(name="avg_npc_074", name2="char_416_zumama_1", focus=1)]
[name="大祭司"]  啊，曾经是一坨废铁的大丑，今天居然已经变得这么像样了，啊，此情此景，真是让我想高歌一曲！
[Character(name="avg_npc_074", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  但你唱歌很难听。
[Character(name="avg_npc_074", name2="char_416_zumama_1", focus=1)]
[name="大祭司"]  什么？！好吧，我还觉得我挺有歌唱天赋的......真遗憾！
[name="大祭司"]  哦，对，或许是唱法的问题。
[name="大祭司"]  嗯，没错，一定是这样，下次我要试试美声的唱法！
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_073")]
[name="阿达克利斯人"]  大酋长，有人冲进来了！
[Character(name="avg_npc_073", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  是嘉维尔吗？我......
[Character(name="avg_npc_073", name2="char_416_zumama_1#2", focus=1)]
[name="阿达克利斯人"]  不是！是一个带着很多武器的怪胎！
[Character(name="char_416_zumama_1#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="森蚺"]  什么？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  前面应该就是祖玛玛的部族了。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  这家伙，居然把自己的部族都改造成这样了。
[Character(name="char_017_homura_summer")]
[name="煌"]  看起来挺厉害啊！
[Dialog]
[Character]
[PlaySound(key="$fightgeneral", volume=0.3)] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=0.3)] 
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=0.3)] 
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  咦，里面怎么好像很热闹的样子。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嗯？怎么就打起来了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  可恶的整合运动，居然想要抢走小刻的名字，这可是比蜜饼还要珍贵的东西，小刻绝不原谅你们！
[Dialog]
[Character]
[PlaySound(key="$fightgeneral", volume=0.3)] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=0.3)] 
[CameraShake

... (全文7143字符)
```

### level_act12d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  居然有这么强的整合运动，哼，但是小刻不会输的！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  啧，这个傻丫头。
[Dialog]
[Character]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_187_ccheal_1",name2="char_2013_cerber_1")]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  醒醒！
[Dialog]
[Character]
[Character(name="char_2013_cerber_1",fadetime=1,block=true)]
[delay(time=1)]
[name="刻俄柏"]  唔？这里是哪里？
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  啊，是嘉维尔！还有大家！
[Decision(options="早上好。;......;（爆栗）",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  诶嘿嘿，博士早上好。
[Predicate(references="2")]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  唔，博士的脸色有点可怕，是我做错了什么吗？
[name="刻俄柏"]  博士不要生气好不好......
[Predicate(references="3")]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  呜呜呜，头好痛，博士。
[name="刻俄柏"]  为什么突然敲我的头呀......
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  精神看起来至少恢复正常了。
[name="嘉维尔"]  小刻，你还记得你怎么来到这里的吗？
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  ......唔，忘了！
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  好吧。
[name="嘉维尔"]  来，你先躺下，我给你看看身体还有没有出问题，还有下次别乱跑了。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  好~咦，这里是哪里啊？
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  这里是......啧，不知道怎么给你解释，反正躺好就对了！
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  哦——
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[Character(name="char_416_zumama_1#2", fadetime=1,block=true)]
[delay(time=1)]
[name="森蚺"]  嘉维尔，你在搞什么鬼？
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1#2", focus=1)]
[name="嘉维尔"]  啧，给你解释也很麻烦，总之你先等等。
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  ......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
十分钟后
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=1)]
[name="嘉维尔"]  好了，没什么大碍，去博士旁边待着，别乱跑啊，再乱跑不给你蜜饼吃了。
[Character(name="char_187_ccheal_1", name2="char_2013_cerber_1",focus=2)]
[name="刻俄柏"]  哦！蜜饼！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="char_416_zumama_1",fadetime=1,block=true)]
[delay(time=1)]
[name="森蚺"]  可以了吗？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  可以了。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  那么，嘉维尔，你在搞什么鬼？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  唉，说起来有些复杂，总之我是来找你的。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  引擎我是不会还给你的。
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  虽然引擎也是一件事，不过我有别的事要找你。
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  别的事？
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  你是不是让手下去开采铁矿了？
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  是。
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  ......啧。
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  嘉维尔，我没想到你是这么不服输的人。
[name="森蚺"]  被大丑打败让你不服气吗？
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1#2", focus=1)]
[name="嘉维尔"]  不，那个叫大丑的东西确实不赖，我心服口服。
[name="嘉维尔"]  但如果你不惜让手下染上矿石病也要去开采矿石的话，那我作为医生，就必须要阻止你。
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  嗯？矿石病？哦，你在说石头病。
[name="森蚺"]  我没有。
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  啊？
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  我告诉过他们很多次不要靠近矿区深处。
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  可是你的手下明明感染了矿石病！
[Character(name="char_187_ccheal_1#4", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  会有不听话的家伙跑进去，这个我拦不住，你说是吧，尤吉？
[Character(name="avg_npc_070", name2="char_416_zumama_1", focus=1)]
[name="尤吉"]  是，哥哥是想多给大酋长采一些矿才冒险跑进矿区深处的。
[Character(name="char_187_ccheal_1#2", name2="avg_npc_070", focus=1)]
[name="嘉维尔"]  啊？那你早说啊！
[Character(name="char_187_ccheal_1#2", name2="avg_npc_070", focus=2)]
[name="尤吉"]  你又没问。
[stopmusic(fadetime=2)]
[Character(name="char_187_cch

... (全文9959字符)
```

### level_act12d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  这里的楼房跟其他部族明显不一样了......
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  破房子！
[Character(name="char_337_utage_summer_1#2")]
[name="宴"]  唔，这里的建筑和装饰好粗糙。
[Character(name="char_201_moeshd_summer")]
[name="可颂"]  不过奇怪的器械残骸到处都是。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  祖玛玛，你的部族建设得挺特别啊。
[name="嘉维尔"]  看来他们也和你一样喜欢捣鼓机器了嘛。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  这都是我的族人们的杰作。
[name="森蚺"]  嗯。他们也都体会到了机械的魅力，凭借着自己的热情将这个部族建设到了现在这个样子。
[Dialog]
[Character]
[name="阿达克利斯人A"]  快看，是嘉维尔。
[name="阿达克利斯人B"]  大酋长说的是真的，她要用大丑和嘉维尔再进行一次对决。
[name="阿达克利斯人C"]  什么？！这怎么能错过！
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  哇，好多人！
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  这些人里有不少是在祭典后聚集到这里来的其他部族的人，他们也将会加入我们。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  哦，所以你要说些什么？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  嘉维尔，原本如果你就那么离开的话，我不会管你。但是你既然你又站在我的面前，那么我就要在这里打倒你。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  为什么？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  因为你太强了，嘉维尔。
[name="森蚺"]  你还记得那一天吗，嘉维尔？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  那一天？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  在那天之前，我和你一样，坚信自己的拳头就是一切。
[Dialog]
[Character]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="嘉维尔"]  嘿！
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="森蚺"]  哇啊啊！
[Dialog]
[Delay(time=0.6)]
[name="阿达克利斯老人"]  嘉维尔胜！
[name="嘉维尔"]  哈哈，我又赢了。
[name="森蚺"]  哼，再来，下次我一定会赢！
[name="嘉维尔"]  好呀！
[Dialog]
[Character]
[playsound(key="$smallearthquake", volume=0.4)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[delay(time=1)]
[name="森蚺"]  咦，大地怎么在震动？
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="嘉维尔"]  看，是那边！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="ac12_3",xScale=1.2, yScale=1.2,screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=false)]
[ImageTween(xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.05, yScaleTo=1.05,duration=20, block=false)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="森蚺"]  那......那是什么啊？
[name="嘉维尔"]  好大的铁块！
[name="阿达克利斯老人"]  那是萨尔贡的移动城市......
[name="森蚺"]  萨尔贡是什么？
[name="阿达克利斯老人"]  萨尔贡是我们的国家。
[name="森蚺"]  移动城市又是什么？
[name="阿达克利斯老人"]  移动城市就是很大的部族，在上面住着许多人。
[name="阿达克利斯老人"]  我也是年轻时有一次上去看到过。
[name="阿达克利斯老人"]  好了，别害怕，它不会开过来的。
[name="阿达克利斯老人"]  那是和我们一辈子都没关系的东西。
[name="森蚺"]  ......
[Delay(time=1)]
[name="嘉维尔"]  祖玛玛，你怎么了，身体不舒服吗？
[name="森蚺"]  没什么，我先回去了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  哦，我记得啊，萨尔贡的移动城市正好开过了我们这里附近嘛，从那天之后你就变得怪怪的了。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  我反而觉得不可思议，嘉维尔。
[name="森蚺"]  看到那样的东西，难道不会觉得惊讶吗？不会觉得震撼吗？不会觉得自己渺小吗？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  你问我那天的感受，那确实是觉得“哇，好大啊”，可是那和我有什么关系？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  你总是这样，嘉维尔。
[name="森蚺"]  在那天之后，我就对和你打架失去了兴趣。
[name="森蚺"]  我拜托依娜姆帮我寻找和机械有关的书籍，开始学习萨尔贡语和机械知识。
[name="森蚺"]  然后我遇到了大祭司，我们两个人开始一起制造大丑。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  这我知道啊，我不是还去找过你。
[name="嘉维尔"]  嗯？这么说来，那边那只怪家伙就是你的隐形朋友？
[Dialog]
[Character]
[ShowItem(image="item_act13_1", fadetime=0.1)]
[CameraShake(duration=1.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="大祭司"]  没错！
[Character]
[name="宴"]  哇，什么时候到我身边来的！？
[Dialog]
[Character]
[HideItem(fadetime=1,block=true)]
[Character(name="char_201_moeshd_summer",name2="avg_npc_074",focus=1)]
[name="可颂"]  总觉得跟大帝老板一样......
[Character(name="char_201_moeshd_summer",name2="avg_npc_074",focus=2)]
[name="大祭司"]  大帝？你是说那只企鹅吗？
[Character(name="char_201_moeshd_summer",name2="avg_npc_074",focus=1)]
[name="可颂"]  是的，咦，你认识老板吗？
[Character(name="char_201_moeshd_summer",name2="avg_npc_074",focus=2)]
[name="大祭司"]  认识认识，当然认识，虽然我们大概有几十年没见面了，咦，是几十年吗？还是几百年？算了，反正你身上确实有那家伙的气味。
[Character(name="char_337_utage_summer_1#3")]
[name="宴"]  几百年是怎么回事啊......
[Character(name="char_201_moeshd_summer",name2="avg_npc_074",focus=1)]
[name="可颂"]  诶诶诶，没想到老板在这里还有朋友！
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  原来你真的存在啊，我一直以为是祖玛玛脑子出问题了出现了幻觉，在罗德岛的时候我还专门研究过类似的病症咧。
[Character(name="avg_npc_074")]
[name="大祭司"]  噢，你不知道，嘉维尔，小时候你来找祖玛玛的时候，我一直在旁边看着！
[Character]
[name="大祭司"]  就像这样！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  消失了！
[Character]
[Dialog]
[Character(name="avg_npc_074",f

... (全文12282字符)
```

### level_act12d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Character]
[name="大祭司"]  哇啊啊啊啊啊啊！哎，不对，下次我应该换个叫声，有点腻了......
[CameraShake(duration=1.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[CameraShake(duration=1.5, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=2)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  喂，他没事吧。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  不用担心，等一会儿他就会回来了。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  好吧，不过那真的是普通人吗？我没听说有这样的啊。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  不知道，大祭司只说过他在这里生活了很久很久。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  好吧，比起这个......
[name="嘉维尔"]  呼，真是个了不得的大家伙啊。
[Character(name="char_017_homura_summer")]
[name="煌"]  嘉维尔，你头上在流血啊，没事吧。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  没事没事，这点小伤，特米米，把我的医疗包拿过来。
[name="嘉维尔"]  嗯？特米米这丫头人呢？
[Character(name="char_337_utage_summer_1")]
[name="宴"]  给，你的医疗包。至于特米米，刚才快要赢的时候我好像看到她慌慌张张地往其他地方跑去了。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  谢了。她不会被吓破胆了吧，算了，先包扎再说。
[name="嘉维尔"]  对了，你们去看看有没有受伤的家伙，全部带到我这来，我来给他们治疗。
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  噢，交给我吧！
[Character(name="char_017_homura_summer")]
[name="煌"]  哈哈，没问题。
[Character(name="char_337_utage_summer_1#3")]
[name="宴"]  诶，好麻烦啊。
[Character(name="char_201_moeshd_summer")]
[name="可颂"]  别抱怨啦。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士......嗯？
[Character(name="char_416_zumama_1")]
[name="森蚺"]  大丑......
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  祖玛玛，抱歉啊，只能把它拆掉了。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  我知道。
[name="森蚺"]  我检查了一下，你的引擎还能用，我会把它还给你。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  是吗，太好了！
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  嘉维尔，你不打算留下来吗？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  嗯，我和你一样，找到了要做的事。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  是医生吗？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  是啊。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  做医生很开心吗？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  造机器很开心吗？
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1#5", focus=2)]
[name="森蚺"]  开心。
[Character(name="char_187_ccheal_1#5", name2="char_416_zumama_1#5", focus=1)]
[name="嘉维尔"]  那就是了。
[Character(name="char_187_ccheal_1#5", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  但是，大酋长依然需要你来做。
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  哈？
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1#5", focus=2)]
[name="森蚺"]  无论如何，大丑倒下了是事实，你赢了，嘉维尔。
[name="森蚺"]  看，人群重新聚集了起来，大家都在看着你。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  啧，博士，怎么办啊。
[Decision(options="由你决定。;......;大酋长嘉维尔万岁！",values="1;2;3")]
[Predicate(references="1")]
[name="嘉维尔"]  这不是跟没说一样吗！
[Predicate(references="2")]
[name="嘉维尔"]  博士，别装睡了！我可是医生！
[Predicate(references="3")]
[name="嘉维尔"]  啧，博士，我现在真想给你一拳。
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  嘉维尔，你没事吧！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  嗯？没事。你跑哪里去了？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  诶？啊，那个，我刚才忽然想上厕所！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  好吧......嗯？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  怎么了，嘉维尔，你怎么忽然看着我？
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  唔......哈哈，有了！
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  所有人都听着！
[name="嘉维尔"]  我战胜了大丑，所以接下来由我来担任大酋长。
[name="嘉维尔"]  在这里，我要对你们说的是——
[Dialog]
[delay(time=1)]
[name="嘉维尔"]  拳头，就是一切！
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[delay(time=1)]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  诶，嘉维尔，你要留下来做大酋长了吗？
[Character(name="char_187_ccheal_1#3")]
[name="嘉维尔"]  但是！
[name="嘉维尔"]  我有非常重要的事要去做，所以我还是要离开。
[name="嘉维尔"]  不过你们不用担心！我不在的时候，会由特米米来代替我发号施令！
[name="嘉维尔"]  把特米米当成是我就行了！
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  诶、诶诶诶？
[Character]
[Dialog]
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[delay(time=1)]
[Character(name="char_337_utage_summer_1#3")]
[name="宴"]  诶，这样真的行得通吗？这里的人不是力量至上什么的。
[Character(name="char_416_zumama_1")]
[name="森蚺"]  但嘉维尔是大酋长，她已经征服了所有人，所以她说的话当然是令人信服的。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  哈哈，祖玛玛，机器虽然很有意思，但是对我来说，果然还是拳头更好啊。
[Character(name="char_187_ccheal_1#3", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  哼，别忘了，我并没有承认你，我会造出更厉害的机器，然后再来挑战你。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=1)]
[name="嘉维尔"]  好啊，我等着。
[name="嘉维尔"]  哦对了，在那之前，你得跟我走一趟。
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1", focus=2)]
[name="森蚺"]  为什么？
[Character(name="char_187_ccheal_1", name2="char_416_zumama_1",

... (全文6831字符)
```

### level_act12d0_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="char_187_ccheal_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="嘉维尔"]  特米米，你没事吧？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  我不准嘉维尔你离开！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  啊？为什么？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  因为、因为我不想再和你分开了！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  啊？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  本来我就是打算夺得大酋长的位置然后再把你留下来的......
[Character(name="char_416_zumama_1#2")]
[name="森蚺"]  难道说，这次祭典是你举办的？
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  没错，如果不是祖玛玛你忽然杀出来，原本应该是由我来成为大酋长的！
[Character(name="char_416_zumama_1#2")]
[name="森蚺"]  ......原来如此。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  啊？你们在说啥？
[Decision(options="祭典能举办起来很奇怪。",values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  嗯？博士，你在说什么？祭典怎么了？
[Character(name="char_416_zumama_1#2")]
[name="森蚺"]  你很聪明，外乡人。
[name="森蚺"]  稍微想一想就知道了，嘉维尔。
[name="森蚺"]  自从你离开后，大部族分裂成了现在的各个小部族，大家失去了统一的领袖，也就很少再会聚在一起做什么事。
[name="森蚺"]  也就是说，祭典没道理忽然就这么举办了，需要有人把大家组织起来。
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1#2", focus=1)]
[name="嘉维尔"]  嗯？祭典难道不是你举办的吗？
[Character(name="char_187_ccheal_1#2", name2="char_416_zumama_1#2", focus=2)]
[name="森蚺"]  不是啊，大丑一直是缺少引擎的状态，而且还不能算完成，我原本打算再过至少一年才联络其他部族重新举办祭典的，结果它就这么举办了。
[name="森蚺"]  对我来说这也很突然，但是既然举办了，那就举办了，我相信即使还没完成，大丑也能让所有人吃惊。
[name="森蚺"]  只是没想到你回来了。
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  这么说来，把我叫回来的也是特米米。
[name="嘉维尔"]  难道说，这一切都是你计划好的？
[Character(name="char_411_tomimi_1")]
[name="特米米"]  ......嗯。
[name="特米米"]  为了成为大酋长，我在这几年里用书上学来的方法说服了其他部族的人，原本最后会由我来成为大酋长的。
[name="特米米"]  但是现在也还来得及......愿意听我指挥的部族已经就在外面了，大丑也已经倒下，没有人可以阻止我把嘉维尔留下来了！
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  为什么你非要把我留下来不可？
[Character(name="char_411_tomimi_1")]
[name="特米米"]  因为、因为......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="bg_jungle_1",screenadapt="coverall")]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[name="特米米"]  这里、这里是哪里......
[name="特米米"]  呜呜呜，我要回家......
[name="特米米"]  呀啊！
[name="嘉维尔"]  喂，没事吧，特米米。
[name="特米米"]  嘉维尔......
[name="嘉维尔"]  哎，你这家伙真是的，一不注意就跑到这种地方来了，找死我了。
[name="特米米"]  嘉维尔，你在流血！
[name="嘉维尔"]  啊？没事没事，这点小伤不算什么。
[name="嘉维尔"]  走，我们回家。
[Dialog]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="bg_village_2",screenadapt="coverall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  嘉维尔是我的救命恩人，我最喜欢嘉维尔了！
[name="特米米"]  而且、而且嘉维尔是最强的，只要有嘉维尔当大酋长，一定能够带领大家的！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  哎，我还以为过去几年你长大了，这不是和以前没什么两样吗......
[name="嘉维尔"]  我有重要的事要去做，你拦不住我的，特米米。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  ......书上说，“留不住他的心，那就留住他的人”，书上还说，“只要能让他留在我身边，被他讨厌也没有关系”。
[name="特米米"]  所以、所以即使被嘉维尔你讨厌，我也要把你留在这里。
[Character(name="char_337_utage_summer_1#3")]
[name="宴"]  诶，她该不会被什么三流言情小说给毒害了吧......
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  现在，大丑已经倒下，你们也被消耗了许多，你们是不可能战胜我的！
[name="特米米"]  乖乖投降的话，我、我就不会伤害你们！
[Character(name="char_187_ccheal_1#4")]
[name="嘉维尔"]  你是留不住我的，特米米。
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  ......那、那就由不得你了！
[name="特米米"]  所有人一起上吧！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Character]
[Image]
```

### level_act12d0_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="char_187_ccheal_1#4", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  结束了，特米米。
[Character(name="char_187_ccheal_1#4", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  ......还、还没有！
[Character(name="char_411_tomimi_1#2")]
[name="特米米"]  努尔，佩塔！
[Character(name="avg_npc_012")]
[name="迪伦"]  博士！
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  博士——！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  不想让你的同伴受到伤害的话......
[Character(name="char_187_ccheal_1#4", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  别逼我生气啊，特米米！
[Character(name="char_187_ccheal_1#4", name2="char_411_tomimi_1#2", focus=2)]
[name="特米米"]  ......嘉维尔你不留下来的话，我是不会收手的！
[Character(name="avg_npc_012")]
[name="迪伦"]  救我啊，博士！
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  博士，我好怕呜呜呜......
[Decision(options="交给你的任务完成了？;......;不要怕！我这就来救你们！",values="1;2;3")]
[Predicate(references="1")]
[Character(name="avg_npc_012")]
[name="迪伦"]  博士，别这么不上道嘛，小姑娘这么情真意切，配合一下又不会死。
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  唉，这里的人这么淳朴，老实说，欺骗他们让我有些良心不安呢，虽然我没有心。
[Predicate(references="2")]
[Character(name="avg_npc_012")]
[name="迪伦"]  哎呀，博士，你别用那种眼神看着我。
[name="迪伦"]  安心，我怎么也是罗德岛的干员，这点小事都做不好怎么行。
[Predicate(references="3")]
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  博士——！
[Decision(options="Lancet-2！", values="4")]
[Predicate(references="4")]
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  博士——！
[Character(name="avg_npc_012")]
[name="迪伦"]  哇，你们两个演的比我还起劲啊。
[Predicate(references="1;2;4")]
[stopmusic(fadetime=1)]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  诶？
[Character(name="avg_npc_073")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阿达克利斯人"]  什么时候挣脱的！
[Character(name="avg_npc_012")]
[name="迪伦"]  哈哈，抱歉啊，其实从一开始就没绑住。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士，难道你早就料到了特米米会这么做？
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Decision(options="当然。;......;想不发现才难。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1#4")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  你你你、你是怎么发现的？！
[Decision(options="首先，是你在第一次提到祖玛玛时出现的犹豫。", values="1")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1#2")]
[name="嘉维尔"]  啊？犹豫？
[Decision(options="然后，是在祭典时，你对嘉维尔突然行动的惊慌。", values="1")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1#4")]
[name="特米米"]  ......
[Decision(options="最后，迪伦，东西呢？", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_012")]
[name="迪伦"]  哦，我放在Lancet-2身上了。
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  呜呜......要不是为了博士，我可不会轻易让人在我身体里放东西哦。
[Character(name="char_416_zumama_1")]
[name="森蚺"]  ......
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  这是......火箭筒？
[Character(name="avg_npc_012", name2="char_187_ccheal_1", focus=1)]
[name="迪伦"]  对，在特米米的部族里找到的。
[Character(name="avg_npc_012", name2="char_187_ccheal_1", focus=2)]
[name="嘉维尔"]  难道说......
[Character(name="avg_npc_012", name2="char_187_ccheal_1", focus=1)]
[name="迪伦"]  没错，把我们轰下来的罪魁祸首，就是这个小丫头啦。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  特米米。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  呜呜呜，我错了，嘉维尔。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  过来。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  呜呜呜......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  趴到我大腿上。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  嘉维尔，你不要打我，我知道错了......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=1)]
[name="嘉维尔"]  那可不行。
[name="嘉维尔"]  对付不听话的小鬼，当然要打尾巴！
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#4", focus=2)]
[name="特米米"]  呜呜呜......
[Dialog]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="char_2013_cerber_1")]
[name="刻俄柏"]  打尾巴，好像很痛的样子......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#6", focus=1)]
[name="嘉维尔"]  知道错了吗？
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#6", focus=2)]
[name="特米米"]  知道错了，呜呜呜......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1#6", focus=1)]
[name="嘉维尔"]  知道错了就好。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  总之，这下应该算是没事了，博士。
[Decision(options="累了。;......;你刚才居然没有用那招什么大风车。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈哈哈，确实这一连串发生的事还挺多的。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  喂，博士，你该不会站着睡着了吧。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  我当然不伤到特米米这孩子啊。唉，我可是都有点累了。
[Predicate(references="1;2;3")]
[Character(name="char_285_medic2_1")]
[name="Lancet-2"]  这个大家伙......乍一看虽然好像很丑，但是这个棱角，粗犷的设计感，杂乱却有效的线路连接，仔细看看有一种独特的美。
[name="Lancet-2"]  嗯，是适合结婚的类型呢。
[Character(name="char_285_medic2_1", name2="char_187_ccheal_1", focus=2)]


... (全文19307字符)
```

### level_act12d0_ex01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[CameraShake(duration=1, xstrength=0, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=false)]
[playsound(key="$drift", volume=1)]
[delay(time=1)]
[Character(name="npc_2002_Dan_rock",fadetime=2,block=true)]
[delay(time=2)]
[name="Dan"]  烈日，荒野，黄沙，热风！wohoo！新的歌曲在我的心中诞生了！
[Character(name="npc_2003_Frost_rock")]
[name="Frost"]  （solo）
[Character(name="npc_2001_Aya_rock")]
[name="Aya"]  你们两个太吵了。
[Character(name="npc_2004_Alty_rock")]
[name="Alty"]  确实。难得有这么空旷又无人的环境，不用担心被追赶的事，就不能安静地休息一会吗？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  不过，Alty，这里也能闻到海的气息，真的安全吗？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  Aya，你真是一如既往的不解风情。
[name="Alty"]  这片大地上没有安全的地方，但我们总要学会给自己放松一下，不是吗？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  或许你是对的。
[name="Aya"]  所以下一步，我们要用什么拓宽前进的道路？总不能再空手而归了吧。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  至少，这次那个医生已经给了我们答案。 
[Dialog]
[Character]
Alty看了看手中的“钥匙”。
[Character(name="npc_2002_Dan_rock")]
[name="Dan"]  真的吗真的吗？这个东西看上去可不普通，她居然愿意把这个东西给你？你拿啥换的？
[Character(name="npc_2002_Dan_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  知识。
[Character(name="npc_2002_Dan_rock",name2="npc_2004_Alty_rock",focus=1)]
[name="Dan"]  知识与这东西是等价的吗？
[Character(name="npc_2002_Dan_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  我也不清楚，不过我觉得医生她是在催促我们去运用这个知识。
[Character(name="npc_2001_Aya_rock")]
[name="Aya"]  她会不知道这些吗？
[Character(name="npc_2004_Alty_rock")]
[name="Alty"]  我们知道多少，她应该就......
[name="Alty"]  ......仔细想想，真正的交易内容，应该是用我们的好奇心换来了我们的行动。
[Character(name="npc_2002_Dan_rock")]
[name="Dan"]  这，她不是啥都没出吗？
[Character(name="npc_2001_Aya_rock")]
[name="Aya"]  嗯......
[Character(name="npc_2004_Alty_rock")]
[name="Alty"]  嗯......
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  被骗了呢。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  不，应该说是被诱导了。
[Character(name="npc_2002_Dan_rock")]
[name="Dan"]  被指挥了？
[Character(name="npc_2003_Frost_rock")]
[name="Frost"]  被指引了。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  当真有这么重要吗，这个医生？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  不重要。我觉得这个医生正是想告诉我们，她的举动并不重要。
[name="Alty"]  重要的是我们怎么想，怎么做。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  那钥匙呢？我们要去吗？
[Character(name="npc_2002_Dan_rock",name2="npc_2004_Alty_rock",focus=1)]
[name="Dan"]  啊，很麻烦。能不能不去。
[Character(name="npc_2002_Dan_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  我想这就和音乐一样......我们不应该拥有一种可以强制改变别人的力量，我们只是唱自己的歌。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  唱给他们听，如果好听——
[Character(name="npc_2002_Dan_rock")]
[name="Dan"]  那他们也会唱。
[Character(name="npc_2003_Frost_rock")]
[name="Frost"]  （solo）
[Character(name="npc_2004_Alty_rock")]
[name="Alty"]  哈，那就把更多的知识和钥匙都交给准备好了的人吧。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  会是谁呢？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  还不知道。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  说不定还没出生。
[Character(name="npc_2002_Dan_rock")]
[name="Dan"]  那太好了，但愿他还没出生！
[Character(name="npc_2002_Dan_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  别期待这种事情，Dan，我们......嗯？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  怎么了，Alty。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  车没能量了。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  你没有准备吗？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  准备了，但我们之前绕路了。
[name="Alty"]  而且，我必须承认，在这种没有公路也没有道标的荒野上行驶，很容易丧失方向感。
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  也就是说，我们迷路了？
[Character(name="npc_2004_Alty_rock",name2="npc_2001_Aya_rock",focus=1)]
[name="Alty"]  不能完全这么说，在大方向上，我们并没有偏离，只能说我们在开辟新的道路。
[Character(name="npc_2003_Frost_rock")]
[name="Frost"]  迷路了。
[Character(name="npc_2002_Dan_rock")]
[name="Dan"]  迷路！这也是个不错的题材。
[Character(name="npc_2002_Dan_rock",name2="npc_2001_Aya_rock",focus=2)]
[name="Aya"]  不得不说，Dan，我有时候真想学学你的乐观。那怎么办？
[Character(name="npc_2001_Aya_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  那个方向好像有一片雨林，我们去那边看看吧。
[Character(name="npc_2001_Aya_rock",name2="npc_2004_Alty_rock",focus=1)]
[name="Aya"]  那，谁来推车？
[Character(name="npc_2004_Alty_rock")]
[name="Alty"]  或许我们可以轮流来。
[stopmusic(fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character]
[Background(image="bg_jungleentrance",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="npc_2001_Aya_rock")]
[name="Aya"]  Alty。
[Character(name="npc_2001_Aya_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  干什么。
[Character(name="npc_2001_Aya_rock",name2="npc_2004_Alty_rock",focus=1)]
[name="Aya"]  我们周边已经聚集了不少人。
[Character(name="npc_2001_Aya_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  是的。
[Character]
[Dialog]
[Character(name="avg_npc_073", name2="avg_npc_070",fadetime=1,block=true)]
[delay(time=3)]
[Character]
[Dialog]
[Character(name="avg_npc_071", name2="avg_npc_072",fadetime=1,block=true)]
[delay(time=3)]
[Character(name="npc_2001_Aya_rock",name2="npc_2004_Alty_rock",focus=2)]
[name="Alty"]  但我们听不懂他们的语言。
[Character(name="npc_2001_Aya_rock",name

... (全文16779字符)
```

### level_act12d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_187_ccheal_1#2",fadetime=1,block=true)]
[delay(time=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="嘉维尔"]  嘶，啊......有点痛......
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=2)]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特米米"]  嘉维尔，你终于醒了！你没事吧！
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1#2", focus=1)]
[name="嘉维尔"]  没事没事，一点小伤。
[name="嘉维尔"]  比起这个，祖玛玛那个就是她一直以来在捣鼓的机器吗？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嗯，据说叫做“巨大的丑东西”。太可恶了，居然......
[Character(name="char_187_ccheal_1#5", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  也太酷了吧！
[Character(name="char_187_ccheal_1#5", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  居然把......咦，诶？
[name="特米米"]  可是，可是那个大家伙明明把嘉维尔你打倒了......
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  但是它确实很厉害啊，虽然我只瞟到一眼就昏过去了。
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  唔唔，确实......
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  不过，还真是没想到她居然真的造出了这样的东西。
[name="嘉维尔"]  虽然可露希尔也偶尔会造一些古怪的东西出来，不过祖玛玛这台恐怕可露希尔看到也会惊叹吧，哈哈。
[Character(name="char_187_ccheal_1#3", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  诶，在罗德岛那样的东西有很多吗？
[Decision(options="有。;......;没有这么丑的。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  哇哇哇，罗德岛好可怕......
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈哈，罗德岛可是超乎你这小脑瓜想象的地方。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈哈，这么一说倒是真的，那台机器要是可露希尔看到估计要疯了。
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  嗯？神庙怎么倒了？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  被那台怪兽轰倒了。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  哦，那这么说，祭典已经散了吗？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嗯。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  也就是说，祖玛玛成为了大酋长？
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  嗯......
[name="特米米"]  虽然一开始所有人都吓了一跳，但是......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_416_zumama_1")]
[name="森蚺"]  我毁掉神庙的原因，很简单。
[name="森蚺"]  我想告诉大家，这种传统该结束了。
[name="森蚺"]  靠拳头可以打十个人，像嘉维尔那样的，或许可以打一百个，但是，再多呢？
[name="森蚺"]  就算是嘉维尔也解决不了。
[name="森蚺"]  这就是只靠拳头的极限。
[name="森蚺"]  但是，工具不一样，我们部族制造出来的这台“巨大的丑东西”，可以轻易地打败嘉维尔，也可以轻易地让神庙塌掉。
[name="森蚺"]  这就是工具的力量。
[name="森蚺"]  而借助工具，你们也可以变得这么强！
[name="森蚺"]  所以接下来，是机器的时代！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_temple_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  大家都被她说服了，所以......
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  所以她成为了大酋长吗，嗨呀，这下真是输了。
[Decision(options="不甘心吗？;......;可别不服输啊，嘉维尔。",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  嗯？没有，输了就是输了。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  嘿，博士，不用想安慰我的话，我是真的不难过。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哼，当然，我是谁？
[Predicate(references="1;2;3")]
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  哦，不过，特米米，抱歉啊，我这么一搞，你都还没上场就结束了。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=2)]
[name="特米米"]  ......没事的，就算是我先上场，应该也是一样的结果吧。
[Character(name="char_187_ccheal_1", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  好吧，这倒没错。
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  那么，博士，接下来怎么办？
[Decision(options="找引擎和其他人。;......;观光？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哦对，不管怎么说，引擎不找回来，我们可回不去了。
[name="嘉维尔"]  而且这么一说，祭典上还真是一个我们的人都没出现啊，他们该不会是迷路了吧。
[Predicate(references="2")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  博士也没想好吗，没事，慢慢想吧，距离假期结束还有时间呢。
[Predicate(references="3")]
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  哈哈，我就喜欢博士你这种地方，那就一边找引擎和其他人，一边观光吧！
[Predicate(references="1;2;3")]
[Character(name="char_411_tomimi_1")]
[name="特米米"]  那个，这个......
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  嗯？那边那两个人......
[Character(name="avg_npc_070", name2="avg_npc_071", focus=1)]
[name="阿达克利斯人A"]  喂，哥哥，你没事吧！
[Character(name="avg_npc_070", name2="avg_npc_071", focus=2)]
[name="阿达克利斯人B"]  我没事，我只是，有点......
[Character(name="avg_npc_070", name2="avg_npc_071", focus=1)]
[name="阿达克利斯人A"]  哥哥，哥哥！
[name="阿达克利斯人A"]  巫医，这里有巫医吗！
[Character(name="char_187_ccheal_1")]
[name="嘉维尔"]  喂，让我看看。
[Character(name="char_187_ccheal_1", name2="avg_npc_070", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阿达克利斯人A"]  嘉维尔？你没死吗？
[Character(name="char_187_ccheal_1#2", name2="avg_npc_070", focus=1)]
[name="嘉维尔"]  我才没那么容易死。
[name="嘉维尔"]  少废话，把你哥哥放平在地上给我看看。
[Character(name="char_187_ccheal_1#2", name2="char_411_tomimi_1", focus=1)]
[name="嘉维尔"]  特米米，把我的医药箱给我拿过来。
[Character(name="char_18

... (全文14212字符)
```

### level_act12d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_012",fadetime=1,block=true)]
[delay(time=1)]
[name="迪伦"]  Lancet-2，我有个严肃的问题。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  请问。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  你不会没电吗？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  啊，关于这一点请不用担心，在出发前，可露希尔姐姐为我换上了超长续航的新型电池。
[name="Lancet-2"]  理论上我可以在一个星期内不用补充任何能源。
[name="Lancet-2"]  而且飞行器上也还有备用的电池，所以请不用担心我。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  好吧。
[name="迪伦"]  不知道小刻那孩子怎么样了，我们回来的路上她忽然窜起来就跑了。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  确实，刻俄柏小姐现在的状况让人有些担忧呢，不过考虑到她旺盛的生命力，应该不用太过担心呢。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  也对。
[name="迪伦"]  啊，好无聊。
[name="迪伦"]  飞行器检修完毕，嘉维尔送过来的病人的病情也稳定了下来，暂时没有什么别的事可以做了呢。
[name="迪伦"]  而且和这里的人语言又不通，早知道就跟博士去看那什么祭典了。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  飞行器是很重要的罗德岛财产，必须要好好保护才行呢。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  说说而已，我是驾驶员，这点我当然是知道的。
[name="迪伦"]  你就好啦，Lancet-2，无聊的时候可以切休眠模式，我昨天睡了12个小时，现在根本睡不着。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  唔，确切地说，对我来说，并没有“无聊”的概念呢。
[name="Lancet-2"]  虽然我可以理解迪伦先生你现在的感情，可露希尔姐姐也经常会发出这样的感慨，以及通常这样的情况下她就会去做些奇怪的事。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  ......我不是第一次这么想了，Lancet-2，你和其他小车里面真的不是装了个人吗？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  不是呢，我的里面是精密的电路结构，你要看吗？
[name="Lancet-2"]  虽然由于我的性格预设是女性，所以对于向异性展现身体这件事，我可能会做出一些我自己都无法预想的额外行动。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  呃，算了。
[name="迪伦"]  就算要看，这种时候我肯定也是想看泳装啊。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  泳装？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  是啊，现在可是夏天，大家穿上泳装玩水还挺正常吧。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  这样的话，我来为你播放一段海浪的音频吧。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  别啊，这样不就显得我更惨了。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  ......难道说，迪伦先生想看我的泳装吗？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  才不要啊！
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  是呢，对不起，毕竟我只是机器。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  呃，抱歉，我不是那个意思。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  请不用介意。说起来，迪伦先生见过海吗？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  呃，算是见过吧，大概是去年夏天，银灰老爷因为行程有变借用了罗德岛的飞行器，当时是我作为驾驶员送他去的。
[name="迪伦"]  到了地方后我才发现好像是个度假的地方，然后被银灰老爷邀请体验了一把VIP的生活。
[name="迪伦"]  啧啧，我在那时才知道，原来是贫穷限制了我对有钱人的想象。
[name="迪伦"]  你看，我还有那时候的照片呢。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  迪伦先生向往那样的生活吗？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  嗯？向往啊......虽然那几天确实很爽，不过真要我一直过那样的生活，我肯定是过不惯的。
[name="迪伦"]  还是在驾驶舱里吃泡面，每天日夜颠倒的生活适合我。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  这样可不行，迪伦先生，我来为你设计一套比较科学健康的作息表吧。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  那还是免了吧！
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  真遗憾。可露希尔姐姐虽然为我设计了这个功能，但是无论是她还是博士，都从来没有用到过这个功能。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  哈哈，那两位确实。
[name="迪伦"]  哎，不过，话又说回来，这里的部族的生活比我想象的其实也好不少，该有的都有。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  是呢，虽然这里比起外界的生活在便利和舒适程度上差了许多，但是也并没有什么特别不便的地方。
[name="Lancet-2"]  根据我的记录，这两天，迪伦先生的身体健康水平也有所回升。
[name="迪伦"]  真的假的？
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  是真的。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  这就是所谓的回归自然吧？嘿，也是，毕竟说白了，所有人还不都是从这样的生活过来的。
[name="迪伦"]  对了，我记得嘉维尔说过，在那边的雨林中有一座巨大的瀑布，等博士回来后，去那边玩应该不错。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  他们说不定已经过去了也说不定呢。
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=2)]
[name="迪伦"]  博士做事一向公平，我相信他们一定不会抛下我们去玩水的！
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=1)]
[name="Lancet-2"]  是呢，在那之前，就先耐心等待吧。
[stopmusic(fadetime=2)]
[Character(name="char_285_medic2_1", name2="avg_npc_012", focus=-1)]
[name="？？？"]  这里有叫迪伦的人吗？
[Character(name="avg_npc_012")]
[name="迪伦"]  我！
[name="迪伦"]  嗯？你会说萨尔贡语？
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_075",fadetime=1,block=true)]
[delay(time=1)]
[name="依娜姆"]  会。和一台机器在一起的人，嗯，应该是你没错了。
[name="依娜姆"]  叫博士的家伙让我给你带了一封信。
[Character(name="avg_npc_075", name2="avg_npc_012", focus=2)]
[name="迪伦"]  嗯？让我看看。
[delay(time=1)]
[Character(name="avg_npc_012")]
[name="迪伦"]  ......Lancet-2，看来我们有事做了。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Character]
[delay(time=1)]
[largebg(imagegroup="bg_falls_1/bg_falls_2", solidwidth="920/920", solidheight=720,x=-180)]
[largebgtween(xFrom=-180,xTo=-720,  duration=7, ease="6", block=false)]
[Blocker(a=0, fadetime=2, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[delay(time=5)]
[Character(name="char_337_utage_summer_1#2")]
[name="宴"]  哇，远远地就听到水声了，没想到这座瀑布有这么大！
[Character(name="char_187_ccheal_summer_1", name2="char_337_utage_summer_1#2", focus=1)]
[name="嘉维尔"]  哈，

... (全文13657字符)
```

### training_act12d0_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0教学关_a

[PopupDialog(dialogHead="$avatar_ccheal")] 以前我就在想了，这些巨蕈真的不能想想办法吗？
[PopupDialog(dialogHead="$avatar_tomimi")] 那个，嘉维尔，我有办法！让我的手下们去吧！


```

### training_act12d0_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0教学关_b

[Tutorial(focusX=220, focusY=200, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_tomimi", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
大家现在对于处理这种巨蕈很有经验的！


```

### training_act12d0_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0教学关_c

[Tutorial(focusX=220, focusY=120, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_tomimi", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
清理掉巨蕈后，擅长远程攻击的人就可以站上木桩了。

[PopupDialog(dialogHead="$avatar_ccheal")] 等等，这些不是你的手下吗？怎么穿着罗德岛的衣服？
[PopupDialog(dialogHead="$avatar_tomimi")] 唔，因为博士在进入雨林前询问我能不能雇佣一些我的手下。


```

### training_act12d0_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0教学关_d

[PopupDialog(dialogHead="$avatar_ccheal")] 不愧是博士，连这都已经考虑到了吗。
[PopupDialog(dialogHead="$avatar_ccheal")] 那现在这些人应该算是罗德岛的临时雇员了。
[PopupDialog(dialogHead="$avatar_ccheal")] 借助这些临时雇员的力量继续前进吧。


```

### training_act12d0_09_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0演出关_a
[PopupDialog(dialogHead="$avatar_tomimi")] 我、我还没有输！
[PopupDialog(dialogHead="$avatar_tomimi")] 所有人一起上吧！
```

### training_act12d0_09_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0演出关_b
[PopupDialog(dialogHead="$avatar_huang")] 这些人斗志昂扬啊。
[PopupDialog(dialogHead="$avatar_huang")] 嘉维尔，要不然你留下来算了。
```

### training_act12d0_09_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0演出关_c
[PopupDialog(dialogHead="$avatar_tomimi")] 好厉害……
[PopupDialog(dialogHead="$avatar_tomimi")] 但是，这一切都是为了嘉维尔，大家上呀！
```

### training_act12d0_09_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0教学关_a
[PopupDialog(dialogHead="$avatar_moeshd")] 怎么感觉我们像是抢走嘉维尔的坏人一样……
[PopupDialog(dialogHead="$avatar_utage")] 啊哈，虽然这么说不太好，不过不知道为什么，让人有点想从她那里抢走些什么呢！
[PopupDialog(dialogHead="$avatar_moeshd")] 你这么说不就显得我们更像坏人了吗！
```

### training_act12d0_09_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动12d0演出关_e
[PopupDialog(dialogHead="$avatar_cerber")] 唔，他们不是坏人，博士，我不想伤害他们……
```


> 本章节共32个脚本文件，此处展示前30个。

## 统计

- 总字符数：221533
- 对话行数：2106


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
