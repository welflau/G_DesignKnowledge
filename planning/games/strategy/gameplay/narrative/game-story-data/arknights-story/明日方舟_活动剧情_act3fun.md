# 明日方舟 · 活动剧情 · act3fun（5段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act3fun」完整剧情脚本（5个文件，101行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act3fun
- 脚本文件数：5

### level_act3fun_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_007_closre_1")]
[name="可露希尔"]   结束了，博士。别发呆啊，体验如何？
[Character(name="avg_npc_380_1")]
[name="断罪者"]   此人定是深受震撼，需要冷静。
[dialog]
[character]
[delay(time=1)]
[Decision(options="我的时间就白白花掉了？;......;有点怪，仿佛有点想再来一把。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   我从你的身上感受到一些困惑。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   果然，以你对艺术的感悟力和鉴赏力，还是不能对你抱太高期待。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   有什么疑问，说出来，本大师可以为你解答。
[dialog]
[character]
[Decision(options="怎么看出“艺术永存！正义永存！”的？;说好的“游戏难度适当，平衡性极好”呢？;精美的画面和逼真的人物在哪里？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   你身为罗德岛的作战指挥官，怎会如此愚钝！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   我本人的形象是否出现在了游戏中？
[dialog]
[character]
[Decision(options="......",values="4")]
[Predicate(references="4")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   我——断罪大师——“艺术”与“正义”的继承者、保护者、代言人，在游戏中出现，且必须被保护，不能倒下。这意味着什么？
[Character(name="avg_npc_380_1")]
[name="断罪者"]   这意味着艺术与正义永不倒下！
[Predicate(references="2")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   有什么问题吗？
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]   博士不能因为我局内得分始终在排行榜前列，就怀疑难度曲线有问题哦。
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]   嘿嘿，人家毕竟是研发人员，当然更懂《狂弹要塞》的玩法嘛！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   身为罗德岛的作战指挥官，与其猜疑可露希尔，不如好好反思自己的游戏实力！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   我恨不得立刻将你断罪！
[Predicate(references="3")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   不是说了嘛，我们请了夕小姐来为游戏中的场景给出美术参考。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   但她暂时还没有同意。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   她迟早会同意的，她是个热爱艺术的人，我看得出来。
[Predicate(references="4;2;3")]
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]   博士，《狂弹要塞！罗德大兵集结》目前只是测试版本，我们计划本轮试玩结束后，进行进一步的优化。
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]   所以博士你有什么想法，都可以提。这对我们很重要。
[dialog]
[character]
[Decision(options="我工作没做完，之后补交感想。（亢奋）;我工作没做完，之后补交感想。（冷漠）",values="1;2")]
[Predicate(references="1;2")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   那今天你就先回去，我晚上会去找你的。毕竟现在你也是我的同伴，提升同伴的审美能力，还是很有必要。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   不懂艺术，是一种罪孽啊！
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_134_ifrit_5#4",fadetime=1,block=true)]
[delay(time=1)]
[name="伊芙利特"]   啊......博士！
[name="伊芙利特"]  你也是被可露希尔姐叫来测试新游戏的吗？
[Character(name="char_134_ifrit_5#10")]
[name="伊芙利特"]  博士已经试玩过了吗？这游戏叫什么名字?
[dialog]
[character]
[Decision(options="狂躁大兵......啥来着。;罗德......啥来着......要塞。;......啥大提鞋来着。",values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_134_ifrit_5#9")]
[name="伊芙利特"]   ......
[name="伊芙利特"]   至少，我还是先试试......
[dialog]
[character(fadetime=1,block=true)]
[delay(time=2)]
[name="屋内可露希尔的声音"]   你来了！恭喜你成为《狂弹要塞！罗德大兵集结》的第五十三位玩家，伊芙利特干员。
[name="屋内断罪者的声音"]   在你正式测试游玩之前，作为《狂弹要塞！罗德大兵集结》的首席策划兼艺术顾问，我有必要向你阐述一下本款游戏的设计理念与亮点！
[dialog]
[Decision(options="伊芙利特，加油。",values="1")]
[Predicate(references="1")]
[Dialog]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image]
```

### level_act3fun_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_380_1",blackstart=0.2,blackend=0.7,fadetime=1)]
[delay(time=2)]
[name="断罪者"]   你没有泄密吧？
[dialog]
[character]
[Character(name="char_007_closre_1",blackstart=0.2,blackend=0.7,fadetime=1)]
[delay(time=2)]
[name="可露希尔"]   系统上没有相关事务记录，之前做的时候也回避了其他人......
[Character(name="avg_npc_380_1",blackstart=0.2,blackend=0.7)]
[name="断罪者"]   ID怎么没藏起来！
[Character(name="char_007_closre_1",blackstart=0.2,blackend=0.7)]
[name="可露希尔"]   啊，稍等！重来一次重来一次。
[dialog]
[character]
[dialog]
[playsound(key="$keyboard")]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=1)]
[Character(name="avg_npc_380_1",blackstart=0.2,blackend=0.7,fadetime=1)]
[delay(time=2)]
[name="？？？"]   做得好。
[Character(name="char_007_closre_1",blackstart=0.2,blackend=0.7)]
[name="？？？"]   呜呜呜呜，多少个日夜，终于——
[Character(name="avg_npc_380_1",blackstart=0.2,blackend=0.7)]
[name="？？？"]   不必如此激动。自我答应和你合作开始，成功便是注定的。好好准备接下来的试验吧。
[Character(name="char_007_closre_1",blackstart=0.2,blackend=0.7)]
[name="？？？"]   对对对！接下来的试验，至关重要......把他们都抓过来，如果有谁不愿意......
[Character(name="avg_npc_380_1",blackstart=0.2,blackend=0.7)]
[name="？？？"]   此言差矣！即使是试验，也并非所有人都够格的，被选中，那是他们的荣幸！
[Character(name="char_007_closre_1",blackstart=0.2,blackend=0.7)]
[name="？？？"]   我到时候一定要把他们的表情都拍下来存档！
[Character(name="avg_npc_380_1",blackstart=0.2,blackend=0.7)]
[name="？？？"]   接受恐惧、震撼、惶惑、癫狂、忧思的洗礼吧！这些愚昧的家伙！
[Dialog]
[Delay(time=1)]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character]
[delay(time=1)]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]   ......
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]   总之，恭喜你成为我们的体验者，博士。
[name="可露希尔"]   体验我们的——
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="可露希尔"]   《狂弹要塞！罗德大兵集结》！
[character]
[dialog]
[Decision(options="......我能走吗？;很荣幸，但是这是啥？;这名字是谁取的？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   你为什么是这种反应！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   作为指挥官，身体弱就罢了，怎能毫无对艺术的崇敬向往之心！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   如果不是今天需要你帮忙，我早已将你断罪！
[Predicate(references="2")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   你的态度，我姑且算是满意。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   但也别太得意了。
[Predicate(references="3")]
[Character(name="avg_npc_380_1")]
[name="断罪者"]   那还用问......当然是灵感与思想齐飞的本断罪大师啊！
[Predicate(references="1;2;3")]
[character]
[dialog]
[Decision(options="可露希尔，这就是“需要紧急处理的事务”？",values="1")]
[Predicate(references="1")]
[Character(name="char_007_closre_1")]
[name="可露希尔"]   这就得说到，有不少干员反映，出外勤任务动不动就耗时几个月，持续面对严苛危险的工作环境，会造成巨大的身心压力。
[name="可露希尔"]   不在本舰，很难有效地维持自身的工作状态。
[dialog]
[character]
[Decision(options="第一次见可露希尔说这么正经的话！;你竟然真的在为罗德岛的工作环境考虑！",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_007_closre_1#4")]
[name="可露希尔"]   博士你这是什么反应嘛，我可没有撒谎哦......
[name="可露希尔"]   所以我想到，如果通讯终端能更新一下，将互动功能做一些优化，提高一下现有界面的使用舒适度，再加装一些简单的娱乐程序！
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]   干员们肯定能任务、休息两不误！
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]   这个提案中最关键的部分是......
[dialog]
[character]
[Decision(options="如何升级通讯终端？;如何改变大家的使用习惯？",values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]   到底应该安装一款什么样的游戏。
[character]
[dialog]
[Decision(options="......",values="1")]
[Predicate(references="1")]
[Character(name="char_007_closre_1")]
[name="可露希尔"]   这款游戏的研发，关系到大家日后的行动效率。这还不算“需要紧急处理的事务”吗？
[Character(name="char_007_closre_1")]
[name="可露希尔"]   我特意找到断罪者配合我完成了游戏设计。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   正好近来无罪可断。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   哎呀，不必和此人解释过多。总之，《狂弹要塞！罗德大兵集结》已经初步研发完成，目前进入到激动人心的测试环节。
[character]
[dialog]
[Decision(options="所以我今天是来参与测试的。",values="1")]
[Predicate(references="1")]
[Character(name="char_007_closre_1#4")]
[name="可露希尔"]   是的。考虑到之后正式上线的火爆，我们不得不现在提前进行压力测试。
[name="可露希尔"]   为了让我们收集数据提前应对粉丝的追捧，博士你可以不用藏着掖着，有什么赞美之词就尽管说，我们都做好心理准备了！
[dialog]
[character]
[Decision(options="好像哪里不对，不过还是开始吧。;你说的有点道理，那就开始吧。",values="1;2")]
[Predicate(references="1;2")]
[dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_380_1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="断罪者"]   等一下！别急着开始！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   作为《狂弹要塞！罗德大兵集结》的首席策划兼艺术顾问，我有必要向你阐述一下本作的设计理念与亮点！
[Character(name="avg_npc_380_1")]
[name="断罪者"]   本作的灵感，来自于初代断罪大师的经历......
[Dialog]
[MusicVolume(volume=0, fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Subtitle(text="故事发生在古王国“阿加门”。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一群邪恶艺术家成为了王国的统治者，垄断了高端艺术的创作，并强迫全国人民只能以西红柿为食。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="积年累月，广大的艺术家无法忍受精神的贫瘠与身体的羸弱。终于，他们集体将手中的西红柿砸向邪恶艺术家。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那是某个四月的第一天，成千上万的西红柿划过天空。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[MusicVolume(volume=0.6, fadetime=1)]
[Character(name="char_007_closre_1")]
[name="可露希尔"]   你之前说的故事，好像不是这个版本......
[Character(name="avg_npc_380_1")]
[name="断罪者"]   是吗？
[Character(name="char_007_closre_1")]
[name="可露希尔"]   算了，说重点。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   可露希尔说要做一款游戏，我瞬间想到了那个画面。
[Character(name="avg_npc_380_1")]
[name="断罪者"]   至于细节方面，可露希尔认真研发、仔细打磨，使灌注了美丽与思念的本人的艺术构思得以具象化。这是工

... (全文9009字符)
```

### act3fun_guide_01_a

```
[HEADER(is_tutorial=true)] 愚人节关卡教学
[Battle.Pause]
[PopupDialog(dialogHead="$avatar_peacok_fool")] 现在进行《狂弹要塞！罗德大兵集结》的操作教学。
[PopupDialog(dialogHead="$avatar_closure")] 是的，还没来得及请人配音，现在由我和断罪者亲自讲解。
[PopupDialog(dialogHead="$avatar_peacok_fool")] 你能看见我在皮艇上<@tu.kw>高速移动</>。不要大惊小怪，这里是游戏，打破你的思维定式！
[PopupDialog(dialogHead="$avatar_peacok_fool")] 如果不是游戏，你又怎会有机会与本断罪大师并肩作战。
[Tutorial(dialogHead="$avatar_closure", animStyle="Drag",           startX=-300, startY=-150, endX=-100, endY=-150)] 说正事！博士，你只需要在<@tu.kw>屏幕</>任意区域<@tu.kw>滑动</>，就可以自由操作皮艇。
[Tutorial(dialogHead="$avatar_closure", animStyle="Drag",           startX=-300, startY=-150, endX=-300, endY=0)] 就像这样。
[Tutorial(focusX=-63, focusY=204, focusWidth=124, focusHeight=57,           animStyle="Highlight", focusStyle="HighlightRect", anchor="BottomRight",black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 和你平时的作战方式有所不同，不过出击部署依然<@tu.kw>需要费用</>。
[PopupDialog(dialogHead="$avatar_peacok_fool")] 怎么样？来源于生活，但又高于生活。这就是艺术！
[PopupDialog(dialogHead="$avatar_closure")] 话说，断罪者......真的不用把拳头换成子弹吗？
[Tutorial(focusX=-400, focusY=60, focusWidth=91, focusHeight=85,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 这么看，画面里你一直在不停发射自己的......<@tu.kw>“拳头”</>。
[PopupDialog(dialogHead="$avatar_peacok_fool")] 我还嫌拳头不够明显呢！这可是灌注了美丽与思念的断罪之拳！难道要本大师用铳吗？
[PopupDialog(dialogHead="$avatar_closure")] 好吧
[PopupDialog(dialogHead="$avatar_closure")] 基本的操作要领就是这些。我已经看到博士你在摩拳擦掌了，但还有一条最重要的规则——
[Tutorial(focusX=-463, focusY=53, focusWidth=164, focusHeight=148,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_closure")] 必须<@tu.kw>保护</>好<@tu.kw>断罪者</>，并成功击败关底的BOSS，才能算通关！
[PopupDialog(dialogHead="$avatar_peacok_fool")] 喂，你听清楚了没有！如果游戏中的我有什么闪失，现实中的你必将被断罪！
[PopupDialog(dialogHead="$avatar_closure")] 顺便一提...
[PopupDialog(dialogHead="$avatar_closure")] 你给自己设置的生命值也太多了吧！
[PopupDialog(dialogHead="$avatar_peacok_fool")] 哈哈哈，不要在意这些细节！
[PopupDialog(dialogHead="$avatar_closure")] 好吧，那么，游戏——开始！
[Battle.Pause(pause=false)]
[Battle.Pause(pause=true)]
```

### act3fun_guide_01_b

```
[HEADER(is_tutorial=true)] 愚人节教学流程B
[Battle.Pause]
[PopupDialog(dialogHead="$avatar_peacok_fool")] 因为是第一关，慈悲的我决定给你个提示，大的要来了。
[PopupDialog(dialogHead="$avatar_peacok_fool")] 第一关的BOSS得是个具备无与伦比的速度和破坏力的铁轨杀手。
[PopupDialog(dialogHead="$avatar_closure")] 你是说速度调成两倍，不、三倍的萨卡兹穿刺手吗？
[PopupDialog(dialogHead="$avatar_peacok_fool")] 咳咳....总之<@tu.kw>击败</>出现的<@tu.kw>BOSS</>，关卡就结束了。
[PopupDialog(dialogHead="$avatar_peacok_fool")] 可别磨磨蹭蹭的，不然这家伙真的会跑出屏幕戳你。
```

### act3fun_guide_03

```
[HEADER(is_tutorial=true)] 愚人节BOSS关对话
[Battle.Pause]
[PopupDialog(dialogHead="$avatar_peacok_fool")] 在最后的审判里，仁慈的艺术之神会把罪人们搓成——等等，可露希尔，艺术之神的素材有问题！
[PopupDialog(dialogHead="$avatar_closure")] 没错啊。
[PopupDialog(dialogHead="$avatar_peacok_fool")] 怎么会没错？这是什么玩意！
[PopupDialog(dialogHead="$avatar_closure")] 这是<@tu.kw>大丑</>。
```


## 统计

- 总字符数：15462
- 对话行数：101


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
