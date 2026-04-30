# 明日方舟 · 活动剧情 · act9mini（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act9mini」完整剧情脚本（7个文件，1626行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act9mini
- 脚本文件数：7

### level_act9mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-3
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[playMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]	
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="竞技解说"]  十五位骑士，十五次获得头奖的机会！！
[name="竞技解说"]  今夜，你在哪一位骑士身上下注！今夜，又有谁，能踏着血泊抱走金锭，能在暴力之中赢取赞美！？
[name="竞技解说"]  离比赛正式开始还有十分钟！！别放弃这一夜暴富的机会！谁会放弃呢！让我们见证新星的诞生！！
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_122", fadetime=1.5)]
[delay(time=2)]
[name="索娜"]  ......你叫什么名字？
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......有什么事吗？
[character(name="avg_npc_122")]
[name="索娜"]  别这么警惕嘛，札拉克骑士在这个地方可不多见，只是来打个招呼而已啦。
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......
[character(name="avg_npc_122#5")]
[name="索娜"]  在紧张吗？
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  你......也是感染者吗？
[character(name="avg_npc_122")]
[name="索娜"]  站在这里的，有几个不是呢。只有感染者会来打这种比赛......这可是玩命的。
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......
[character(name="avg_npc_122#6")]
[name="索娜"]  盯着我干嘛？怪吓人的。
[character(name="avg_npc_123#4")]
[name="冷漠的骑士"]  不......你有点......眼熟。
[character(name="avg_npc_122")]
[name="索娜"]  嗯？这算是套近乎吗？
[character(name="avg_npc_123#4")]
[name="冷漠的骑士"]  不。也许就像你说的一样，札拉克骑士......不太常见。
[character(name="avg_npc_122")]
[name="索娜"]  那既然这么有缘，我们联手怎么样？
[character(name="avg_npc_123#5")]
[name="冷漠的骑士"]  ......哈？
[name="冷漠的骑士"]  别开玩笑了，我站在这里是为了——
[character(name="avg_npc_122")]
[name="索娜"]  为了给骑士贵族们一点颜色瞧瞧？
[character(name="avg_npc_123#4")]
[name="冷漠的骑士"]  ......你怎么......
[character(name="avg_npc_122")]
[name="索娜"]  从眼神就能看出来。
[name="索娜"]  太明显了，不屑，愤怒，但其实你盯着他们的时间稍微有点久了——观众席上那几位骑士老爷，已经开始注意你了喔？
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......这种感性在这里是多余的。
[character(name="avg_npc_122")]
[name="索娜"]  别这么急着定论嘛......环顾一下，这里的感染者骑士有几类？
[name="索娜"]  有一些被大老板们掏钱买下，当做赌博的消遣，打赢了可以分一杯羹，输了，可就不好说了。
[name="索娜"]  当然，也有一些人，籍籍无名，他们甚至渴望被某位真正的骑士老爷或者商人相中，渴望成为......工具。
[name="索娜"]  他们是无可奈何的，感染者总是无可奈何的。
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......你想说什么？
[character(name="avg_npc_122")]
[name="索娜"]  嘿，我们联手吧？
[name="索娜"]  混战嘛，私下拉帮结派，获胜率会高一些哦？
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......那你又是为什么想要获胜？为了那笔不菲的奖金吗？
[character(name="avg_npc_122")]
[name="索娜"]  不，因为我不敢让其他人赢。
[character(name="avg_npc_123#5")]
[name="冷漠的骑士"]  ——什么话。
[character(name="avg_npc_122#2")]
[name="索娜"]  这场比赛是有黑幕的。有几个感染者......我还不确定，但恐怕他们已经“说好了”。
[name="索娜"]  为了自己能更好地活下去，他们决定踩着其他人往上爬。
[character(name="avg_npc_122#5")]
[name="索娜"]  正确的选择，对吧？正确到可能这里挺多人都是这么想的。
[name="索娜"]  ——所以我不敢让他们赢。有人赢，就有人输，这没什么。但有人活下去，就会......有人死。
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......空泛的正义感是很难博取别人信任的。
[name="冷漠的骑士"]  但是，好吧，现在正是取得骑士协会认可的关键时刻......
[name="冷漠的骑士"]  我同意。札拉克与札拉克，总比和那些来历不明的家伙们联手要好些。
[character(name="avg_npc_122#5")]
[name="索娜"]  欸？真的答应啦？
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  ......你要只是来开个玩笑，一会我真的先从你下手。
[character(name="avg_npc_122#6")]
[name="索娜"]  别别别，那接下来的混战，就麻烦你啦，小灰。
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  格蕾纳蒂·卡利斯卡。
[character(name="avg_npc_122#7")]
[name="索娜"]  ......卡利斯卡......？
[character(name="avg_npc_123")]
[name="冷漠的骑士"]  是个可笑的姓氏，就算你听说过，也当做不知道吧。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="竞技解说"]  接下来！有请——
[character(name="avg_npc_122")]
[name="索娜"]  你可以叫我索娜，小灰。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_123#2",fadetime=1)]
[delay(time=1.5)]
[name="格蕾纳蒂"]  ......索娜。
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=2)]
[name="索娜"]  嗯？怎么啦？
[Character(name="avg_npc_123", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  那个时候，你在最后，突然抢走了我的分数，对吧？
[Character(name="avg_npc_123", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  ......啊哈哈......小灰啊......那件事呢......
[name="索娜"]  你不会还在记仇吧？
[Character(name="avg_npc_123", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  我其实挺记仇的，你还不清楚吗？
[Character(name="avg_npc_123", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  唔......
[Character(name="avg_npc_123#3", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  但我想的不是被你抢了一个冠军这件事。
[Character(name="avg_npc_123#3", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  呃......
[Character(name="avg_npc_123#2", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  那时候你说过，“不敢让其他人赢”......我也一样。
[Character(name="avg_npc_123#2", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  呃！
[Character(name="avg_npc_123#4", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  反应那么大做什么，那会咱们刚认识，不信任才是正常的表现。
[Character(name="avg_npc_123#4", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  不是......呃......其实也是......
[Character(name="avg_npc_123#4", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  ......好了，不是还要去感染者的聚集区看看情况吗？赶紧出发吧。
[Character(name="avg_npc_123#4", name2="avg_npc_122#3", focus=2)]
[name="索娜"]   为了挽回骑士团内部的信赖关系！请容许我找个借口——！
[Character(name="avg_npc_123#1", name2="avg_npc_122#3", focus=1)]
[name="格蕾纳蒂"]  我们什么时候是一个骑士团的了！？
[Character(name="avg_npc_123#1", name2="avg_npc_122#3", focus=2)]
[name="索娜"]  ......嘿。
[Character(name="avg_npc_123#1", name2="avg_npc_122", focus=2)]
[name="索娜"]  迟早的事，小灰。
[Character(name="avg_npc_123", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  ......你说的那个，感染者骑士团？
[Character(name="avg_npc_123", name2="avg_npc_122", focus=2)]
[name="索娜"]  红松。
[name="索娜"]  我的家乡其实靠近维多利亚，那边早年间还有不少那样的松树来着。不过这几年已经见不到了。
[Character(name="avg_npc_123#5", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  ......红松......？
[name="格蕾纳蒂"]  你是......被那场天灾影响的札拉克！？那你也是当时被骑士们抛下——被卡利斯卡家舍弃的......
[Character(name="avg_npc_123#5", name2="avg_npc_122", focus=2)]
[name="索娜"]  别这样小灰，都是过去的事了。
[Character(name="avg_npc_123#5", name2="avg

... (全文24939字符)
```

### level_act9mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-灰松鼠
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_county_1",screenadapt="coverall")]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playsound(key="$d_gen_walk_n")]
[name="年幼的女孩"]  奶奶，我们要去哪里？
[name="威严的祖母"]  还没到你提问的时候。
[name="威严的祖母"]  拿稳小炮，跟紧了。
[name="年幼的女孩"]  是的奶奶。
[name="威严的祖母"]  快到了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_county_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="年幼的女孩"]  那边是？
[name="威严的祖母"]  竞技场，从大骑士领来的家伙们建的。
[name="威严的祖母"]  哼。
[name="年幼的女孩"]  我们是要去看比赛吗？
[name="威严的祖母"]  比赛？不。
[name="威严的祖母"]  我要带你去参加训练。
[dialog]
[delay(time=1)]
[name="威严的祖母"]  还记得我教你的东西吗？
[name="年幼的女孩"]  是的，奶奶，我记得很清楚！
[name="年幼的女孩"]  架盾、起炮、轰击！
[name="年幼的女孩"]  盯紧敌人、注意弹药、炮不离手！
[name="年幼的女孩"]  还有，嗯......
[name="年幼的女孩"]  炮声轰鸣，胜利已在眼前！
[name="威严的祖母"]  很好。
[name="威严的祖母"]  你比你的父亲要可靠得多。
[name="威严的祖母"]  至少在我闭上眼前，还有人能够记得这些。
[name="年幼的女孩"]  奶奶，请别说这样的丧气话......
[name="威严的祖母"]  呵，古木哪有不烂的道理。
[name="威严的祖母"]  与其就这么腐朽掉，不如做新芽的肥料。
[name="威严的祖母"]  咳咳......
[name="年幼的女孩"]  奶奶！
[name="威严的祖母"]  不必，只是咳嗽一下，没什么好担心的。
[name="威严的祖母"]  你父亲那一辈，甚至我的几位兄弟，早都忘了卡利斯卡是怎么繁荣的了。
[name="威严的祖母"]  林业？那片林子是我们靠功勋、靠火炮换回来的！
[name="威严的祖母"]  “炮声轰鸣，胜利已在眼前”......那帮见钱眼开的家伙连格言都记不住了！
[name="年幼的女孩"]  奶奶，请您别生气了......
[name="威严的祖母"]  哼......
[name="威严的祖母"]  格蕾纳蒂，你是棵好苗。
[name="威严的祖母"]  可别长歪了。
[name="年幼的女孩"]  是，我不会让您失望的！
[playsound(key="$d_gen_walk_n")]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Background(image="bg_outcounty",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[name="？？？"]  沸血骑士团——竞技场屠夫——养好伤后再度归来——一如既往的残暴！！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="？？？"]  而另一边——另一边是——
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="威严的祖母"]  咳，咳咳......
[name="？？？"]  曾经的南方林业巨子——卡利斯卡集团的一员——
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="？？？"]  如今则是一位感染者——隶属于红松骑士团——
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[playsound(key="$d_gen_walk_n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="？？？"]  让我们欢迎——
[name="年幼的女孩"]  奶奶？
[name="年幼的女孩"]  （呼......放轻松，奶奶已经教会我了，我可以的。）
[name="年幼的女孩"]  （我准备好了！）
[name="？？？"]  灰毫骑士，格蕾纳蒂·卡利斯卡！
[Dialog]
[Character]
[Blocker(a=1, r=255, g=255, b=255, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[playMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.4)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.7, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=2.5, block=false)]
[Character(name="avg_npc_123#3",fadetime=0.5)]
[delay(time=3)]
[Character(name="avg_npc_122")]
[name="索娜"]  哎呀，小灰终于进场了。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  格蕾纳蒂进场总是慢悠悠的，也不和观众表示一下，一点都不痛快。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  这就是卖点嘛，有人可喜欢这一套了，你看那儿。
[dialog]
[Character]
[name="激动的粉丝"]  格蕾纳蒂！格蕾纳蒂看我一眼呀！！！
[Character(name="avg_npc_122", name2="avg_496_wdmane_1#7", focus=2)]
[name="艾沃娜"]  嗯......行吧。
[name="艾沃娜"]  欢呼声作不了假。
[name="艾沃娜"]  而且那个持炮的姿势，还挺有贵族范的。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  当然我最期待的还是她开炮轰人的时候啦。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  那是肯定有的啦，听到轰隆隆的响声观众可兴奋了。
[Character(name="avg_npc_122", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  要是有更过瘾的就好了。
[Character(name="avg_npc_122#7", name2="avg_496_wdmane_1", focus=1)]
[name="索娜"]  怎么，你还想看她用炮筒砸？
[Character(name="avg_npc_122#7", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  哈哈，有机会还真想见识一下。
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  巨斧对坚盾！究竟谁才是最后的赢家，让我们拭目以待！
[name="大嘴莫布"]  点开您的终端，做出您的选择，支持您的选手！
[name="大嘴莫布"]  当然更重要的是，给自己一个填满钱包的机会！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=80, fadeout=true, block=false)]
[name="大嘴莫布"]  比赛——开始——！
[Dialog]
[Character]
[Character(name="avg_npc_104",fadetime=1,block=true)]
[delay(time=1)]
[name="锈铜骑士"]  你手上那块塑料最好能多撑一会。
[name="锈铜骑士"]  矿石病垃圾。
[Dialog]
[character(fadetime=1)]
[Character(name="char_empty", name2="avg_npc_123")]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=300, fadetime=1, block=true)]
[Character(name="avg_npc_104", name2="avg_npc_123",fadetime=0.7)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[PlaySound(key="$sheildimpact",volume=1)] 
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Camera

... (全文30079字符)
```

### level_act9mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-野鬃
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]	
[name="电视里的声音"]  从地下竞技场杀出重围，预选赛两轮晋级......又一个有着不凡身手的挑战者，感染者骑士，“野鬃”骑士艾沃娜·克鲁科夫斯卡......
[dialog]
[character(name="avg_npc_122#7",fadetime=1)]
[delay(time=1.5)]
[name="索娜"]  ......“野鬃”？
[Character(name="avg_npc_123", name2="avg_npc_122#7", focus=1)]
[name="格蕾纳蒂"]  怎么了，索娜。
[Character(name="avg_npc_123", name2="avg_npc_122#7", focus=-1)]
[name="电视里的声音"]  ......但是，在休息区与其他参赛骑士产生不正当的争执，并以暴力相向......
[name="电视里的声音"]  ......或许面临“停赛”处分......
[Character(name="avg_npc_123", name2="avg_npc_122#7", focus=1)]
[name="格蕾纳蒂"]  ......又来了，感染者骑士的负面报道。
[name="格蕾纳蒂"]  “不正当的争执”，呵，还能是什么？在那种乱七八糟的场所，无非是落败者对胜利者的叫嚣。
[name="格蕾纳蒂"]  对参赛的感染者骑士，他们总是骂得要多难听有多难听。
[Character(name="avg_npc_123", name2="avg_npc_122#6", focus=2)]
[name="索娜"]  你看到刚才的比赛录像片段了吗，小灰。这位库兰塔的身手......还挺厉害。
[Character(name="avg_npc_123#2", name2="avg_npc_122#6", focus=1)]
[name="格蕾纳蒂"]  招式和那些花拳绣腿的贵族的确不太一样，但离最强的骑士水准还有一段距离。
[Character(name="avg_npc_123#2", name2="avg_npc_122#7", focus=2)]
[name="索娜"]  嗯......
[Character(name="avg_npc_123#5", name2="avg_npc_122#7", focus=1)]
[name="格蕾纳蒂"]  ......你想招揽她？
[Character(name="avg_npc_123#5", name2="avg_npc_122#5", focus=2)]
[name="索娜"]  我听说过她的事......骑士团里有人认识她。
[name="索娜"]  在我们需要的人里，“行动组组长必须身手矫健，有过人的武力”，这可是小灰你说的。
[name="索娜"]  ......我想去碰碰运气。目前参赛的独立骑士都有代理人进行招揽，以感染者为主的骑士团的邀约应该能提起她的兴趣。
[name="索娜"]  我有预感，她会是我们要寻找的人。
[Character(name="avg_npc_123#2", name2="avg_npc_122#5", focus=1)]
[name="格蕾纳蒂"]  你是对她的身手感兴趣，还是觉得她和我们志同道合？
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=2)]
[name="索娜"]  这种事，去聊一聊你就知道了。
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=1)]
[name="格蕾纳蒂"]  首先得有见面和商谈的机会才行。你也听到了，新闻里说，商业联合会考虑对她施行“停赛”处分，这可不是什么能轻松解决的事。
[name="格蕾纳蒂"]  预选赛才刚开始，她是感染者，又是刚刚打上来的独立骑士，不会有谁能帮到她的忙。
[Character(name="avg_npc_123#2", name2="avg_npc_122#2", focus=2)]
[name="索娜"]  ......如果这次，刚好我们能帮到忙的话？
[Character(name="avg_npc_123#2", name2="avg_npc_122#2", focus=1)]
[name="格蕾纳蒂"]  你可要想好了，索娜。这是一次有风险的赌注，如果她已经决心为自己走到底，我们势必会是对手。
[name="格蕾纳蒂"]  不过......如果你一定要和她聊聊，这件事值得我们尽全力去尝试。对现在的红松骑士团来说，每一个能够增加新同伴的机会都非常重要。
[Character(name="avg_npc_123#2", name2="avg_npc_122", focus=2)]
[name="索娜"]  我们还是应该试试看。如果能够顺利沟通......当前的情况下，我觉得，她一定会想为感染者做点什么的。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
几日后
[dialog]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[delay(time=1.5)]
[PlaySound(key="$dooropenquite", volume=0.6)]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_496_wdmane_1#8",fadetime=0.7)]
[delay(time=2)]
[name="艾沃娜"]  ......啧，这群联合会的人，没有一个要听实话的。既然一开始就不想要公平裁决，何必一副道貌岸然的样子和我讲那么多？
[name="艾沃娜"]  嘶......疼死了，警棍的力度都比那个三流的贵族烂货的力度大。我看，还不如让那几个警卫上赛场打两场，观众老爷应该还更爱看呢......
[dialog]
[Character]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[name="？？？"]  出来了，她出来了！
[character(name="avg_496_wdmane_1#6")]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=80, fadeout=true, block=false)]
[name="艾沃娜"]  啊？
[character(name="avg_496_wdmane_1#6",focus=-1)]
[name="新闻记者"]  野鬃骑士，你从商业联合会的大门离开是否意味着官方已经做出裁决？
[name="新闻记者"]  你怎么看待自己与其他骑士在休息室的纠纷？这是否为一种挑衅行为？
[name="新闻记者"]  身为感染者骑士，与其他竞技骑士使用同一休息室，在规则上是否对其他骑士不太公平？
[character(name="avg_496_wdmane_1#8")]
[name="艾沃娜"]  ......烦死了！你们谁啊！
[character(name="avg_496_wdmane_1#8",focus=-1)]
[name="新闻记者"]  野鬃骑士，请正面回复这些问题！还有，您到底使用了怎样的说辞能使商业联合会网开一面......
[character(name="avg_496_wdmane_1#8")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾沃娜"]  ......啊啊，这都是什么人啊！
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="middle", type="move", xpos=300, fadetime=1.5,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_123#5",fadetime=1)]
[delay(time=1.5)]
[name="格蕾纳蒂"]  哦，出来了。
[character(name="avg_496_wdmane_1#5")]
[name="艾沃娜"]  哈、哈......嗯？
[name="艾沃娜"]  你......是在这等我的？
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#5", focus=1)]
[name="格蕾纳蒂"]  前门热闹的场面完全能够预料，这里是你为数不多的选择。除非......你想硬冲出一条路。
[name="格蕾纳蒂"]  幸好，你还算明白，现在的自己必须离镜头越远越好。自我介绍一下......
[Character(name="avg_npc_123", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  不用了，我知道你，拿大炮的，还有另一个用剑的。你们两个札拉克是搭档，身手还算不错。
[Character(name="avg_npc_123#4", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  ......感谢夸奖。
[Character(name="avg_npc_123#4", name2="avg_496_wdmane_1", focus=2)]
[name="艾沃娜"]  灰毫，对吧？你来这里干嘛，找我打架，还是看我的笑话？
[Character(name="avg_npc_123", name2="avg_496_wdmane_1", focus=1)]
[name="格蕾纳蒂"]  我们能料到你会面临的麻烦处境，有必要的话，可以为你提供一些帮助。
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#2", focus=2)]
[name="艾沃娜"]  哦，比如说？
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#2", focus=1)]
[name="格蕾纳蒂"]  你不想面对的那些记者，还有......一些别有用心的代理人的邀请，我们可以帮你回绝掉。
[Character(name="avg_npc_123", name2="avg_496_wdmane_1#2", focus=2)]
[name="艾沃娜"]  你们是谁？
[dialog]
[Character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_122",fadetime=1.5)]
[delay(time=2)]
[name="索娜"]  这个还是让我来解释吧。
[name="索娜"]  野鬃骑士，如果你已经了解过我们，事情就方便多了。
[name="索娜"]  我们在关注每一个感染者骑士的动向，因此，在电视上看到你遇到了麻烦的时候，我们也想了一些办法......
[Character(name="avg_496_wdmane_1#7")]
[name="艾沃娜"]  别绕那么大的弯子，我不想听什么复杂的言论，也听不懂。你们两个，来找我做什么？
[character(name="avg_npc_122")]
[name="索娜"]  ......直白地说，我们是红松骑士团的负责

... (全文27083字符)
```

### level_act9mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-7
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]	
[Subtitle(text="查丝汀娜，你又爬到草垛上去了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你总往那边看，又是在看大骑士领吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我知道，我当然知道大骑士领，那是很厉害的骑士老爷们会一起参加比赛的地方，对吧？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你都说过多少回了，我当然早就记住了！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(timr=1.)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="哎，查丝汀娜，你真的要上那儿去吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我知道你不干农活的时候都在练习。嗯，村子里没人不知道你一直想当骑士，你能打跑来闹事的强盗，那些坏家伙都不是你的对手。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但是查丝汀娜，大骑士领有多远啊......你去了，还会回来吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你会回来？真的？当上骑士就回来？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......那就这么说定了。我们都等着你荣归故里，到时我们就到处去宣传，这里可是骑士查丝汀娜的故乡！", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_23_G05",screenadapt="coverall")]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_216",name2="avg_npc_216", fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_216",name2="avg_npc_216", focus=1)]
[name="无胄盟杀手"]  没有脚印，没有人通过的痕迹......
[name="无胄盟杀手"]  他们没有从这方向走。
[character(name="avg_npc_216",name2="avg_npc_216", focus=2)]
[name="无胄盟领队"]  医院的小队弄丢了目标，这些人想逃脱必然要经过这周边。
[name="无胄盟领队"]  保持警惕，随时汇报情况。
[character(name="avg_npc_216",name2="avg_npc_216", focus=1)]
[name="无胄盟杀手"]  明白。
[Dialog]
[character(name="avg_npc_216",name2="avg_npc_216")]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[character(name="avg_npc_216",name2="char_empty", fadetime=1)]
[delay(time=2)]
[name="无胄盟杀手"]  ......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="无胄盟杀手"]  嗯？
[dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=0.6, xstrength=15, ystrength=15, vibrato=30, randomness=90, block=true)]
[name="无胄盟杀手"]  呃、 啊......
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=30, randomness=90, block=true)]
[dialog]
[PlaySound(key="$bodyfalldown2", volume=1)]
[character(fadetime=1.5)]
[delay(time=1.5)]
[character(name="avg_430_fartth_1",blackstart=0.2, blackend=0.7, fadetime=1.5)]
[delay(time=2)]
[name="？？？"]  ......
[dialog]
[character]
[character(name="avg_430_fartth_1",fadetime=1)]
[delay(time=1)]
[name="查丝汀娜"]  ......走。
[name="查丝汀娜"]  他们很快就会发现这里的异常，趁现在，快跟我走。
[Character(name="avg_npc_103", name2="avg_430_fartth_1", focus=1)]
[name="塑料骑士"]  还轮不到你来指挥我，感染者。
[name="塑料骑士"]  能从那个距离如此轻松地解决掉这群下贱的东西，我是得承认你有些实力。
[name="塑料骑士"]  但是别搞错了，这不代表我就要听从你的安排。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#3", focus=2)]
[name="查丝汀娜"]  ......
[name="查丝汀娜"]  这一带，都被无胄盟的人包围，你一个人很难逃出去。
[name="查丝汀娜"]  他们会一直追着你。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#3", focus=1)]
[name="塑料骑士"]  那又如何？
[name="塑料骑士"]  我会叫他们为自己的愚蠢后悔。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#3", focus=2)]
[name="查丝汀娜"]  ......很难。
[name="查丝汀娜"]  你的伤还没好，现在想要躲过他们的耳目会很难。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#3", focus=1)]
[name="塑料骑士"]  哼......该死的无胄盟。
[name="塑料骑士"]  我答应和你们合作，但是记住，这只是因为我们有同一个对手。我要让那些下贱的凶手为他们的行为付出代价！
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=2)]
[name="查丝汀娜"]  这些之后再谈，我们现在还没完全脱困。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=1)]
[name="塑料骑士"]  我不觉得我和你们还有什么更多好谈的。
[name="塑料骑士"]  小姑娘，感谢那个提出荒唐要求的冠军吧，若非如此，你不会有穿上这身甲胄在这里和我说话的一天。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#2", focus=2)]
[name="查丝汀娜"]  ......
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=2)]
[name="查丝汀娜"]  你说的对。
[name="查丝汀娜"]  我曾经，非常感谢血骑士。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=1)]
[name="塑料骑士"]  嗯？
[Character(name="avg_npc_103", name2="avg_430_fartth_1#2", focus=2)]
[name="查丝汀娜"]  ......
[Character(name="avg_npc_103", name2="avg_430_fartth_1#2", focus=1)]
[name="塑料骑士"]  怎么，这就说不出话来了？
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=2)]
[name="查丝汀娜"]  ......比赛。
[name="查丝汀娜"]  我看过你和玛莉娅·临光的对决——“塑料”瑟奇亚克。
[name="查丝汀娜"]  我不喜欢你。
[name="查丝汀娜"]  你在赛场上，比现在要稍微不那么讨厌一点。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=1)]
[name="塑料骑士"]  你的心情无关紧要，但注意你的态度。既然是这样，你就不该将我从医院带出来。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=2)]
[name="查丝汀娜"]  索娜觉得有必要这么做。况且——
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=1)]
[name="塑料骑士"]  况且什么。索娜，这就是你们头领的名字？哼，听起来又是个小姑娘......
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=2)]
[name="查丝汀娜"]  ......索娜是伙伴。
[name="查丝汀娜"]  我们现在回据点，索娜和其他伙伴都在等我们。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=1)]
[name="塑料骑士"]  ......别因为我暂时同意联手，就把我和你们混为一谈，感染者骑士。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#2", focus=2)]
[name="查丝汀娜"]  不......我不会弄混，你和我们都不同。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=2)]
[name="查丝汀娜"]  但是，“塑料”瑟奇亚克，你自己应该也清楚，你没办法独自对抗无胄盟。
[Character(name="avg_npc_103", name2="avg_430_fartth_1#7", focus=1)]
[name="塑料骑士"]  ......
[name="塑料骑士"]  呵......没错，你说得不错。
[name="塑料骑士"]  真是可笑，现在的这个卡西

... (全文23144字符)
```

### level_act9mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-5
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]	
[Subtitle(text="你想照亮些什么？你能照亮些什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="尽我所能。这是骑士应有的荣耀。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="荣耀。荣耀没有背弃卡西米尔。是人们自身放弃了荣耀的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这不代表荣耀没有价值。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="荣耀这个词过于言之无物，玛嘉烈，常将其挂在嘴边的人，大都愚昧。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那么，就该让骑士用行动去证明。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="倘若你为之献身的对象都对你的一切嗤之以鼻......你的所作所为还有什么意义？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$swordtsing1", volume=0.9)]
[Blocker(a=0, fadetime=0.1, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[character(name="avg_npc_108",fadetime=0.5)]
[delay(time=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$swordtsing6")]
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=25, randomness=80, fadeout=true, block=true)]
[name="玛恩纳"]  ——！
[dialog]
[delay(time=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=15, randomness=70, fadeout=true, block=true)]
[name="玛恩纳"]  唔......！
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[character(name="char_148_nearl_1#4")]
[name="玛嘉烈"]  叔叔！
[character(name="avg_npc_108#2")]
[name="玛恩纳"]  决斗中不要随意和对手交流。我没教过你吗？
[character(name="char_148_nearl_1#3")]
[name="玛嘉烈"]  那么，为什么您不用法术？
[character(name="avg_npc_108")]
[name="玛恩纳"]  我倒是想先问问你，看你法术又有长进，那想必你已经意识到那个真相了？
[character(name="char_148_nearl_1")]
[name="玛嘉烈"]  ......关于这件事，是的。
[character(name="char_148_nearl_1#8")]
[name="玛嘉烈"]  但是！玛恩纳叔叔，我并不希望您在这种时候——
[character(name="avg_npc_108#2")]
[name="玛恩纳"]  无需多言。
[name="玛恩纳"]  我的剑被你打落，那就是你赢了，玛嘉烈。
[character(name="char_148_nearl_1#4")]
[name="玛嘉烈"]  ......即使......您从头到尾都没有使用法术吗？
[character(name="avg_npc_108")]
[name="玛恩纳"]  胜负就只是胜负，一切外因都是借口，我什么时候把你教育得这么优柔寡断了？
[character(name="char_148_nearl_1#7")]
[name="玛嘉烈"]  ......
[character(name="avg_npc_108#2")]
[name="玛恩纳"]  既然你已经意识到当年你的祖父为你的天真付出了什么，你就更应该明白你回到这里的意义。
[name="玛恩纳"]  玛嘉烈，你在践踏父亲的意志。
[character(name="char_148_nearl_1#3")]
[name="玛嘉烈"]  难道祖父的意志，就是教我们做一个懦夫吗？
[character(name="avg_npc_108#3")]
[name="玛恩纳"]  ......
[character(name="char_148_nearl_1#8")]
[name="玛嘉烈"]  “不畏苦暗”。
[character(name="avg_npc_108#3")]
[name="玛恩纳"]  是啊，不畏苦暗......你赢下了决斗，你赢得了一个执迷不悟的机会。
[character(name="avg_npc_108")]
[name="玛恩纳"]  记得祈祷你的一意孤行，不会把太多的人卷进来。
[character(name="char_148_nearl_1#2")]
[name="玛嘉烈"]  ......叔叔。
[character(name="char_148_nearl_1")]
[name="玛嘉烈"]  您还是觉得，我们已经回不到那个时代了吗？
[character(name="avg_npc_108")]
[name="玛恩纳"]  ......
[dialog]
[delay(time=1)]
[PlaySound(key="$phonevibration",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[character(name="avg_npc_108")]
[name="玛恩纳"]  玛嘉烈，你居然还能问出这样的问题。
[name="玛恩纳"]  稍后我有一场电话会议。特锦赛让人们都很繁忙，至于你的夺冠游戏......最好不要让我分心。
[name="玛恩纳"]  正视现实吧，正视他人的生活。看看别人的柴米油盐，别再因为你自己的荣耀就对他人抱有幻想。
[name="玛恩纳"]  你会失望的。迟早会的。
[character(name="char_148_nearl_1#3")]
[name="玛嘉烈"]  如果我没有和您一样呢？
[character(name="avg_npc_108#3")]
[name="玛恩纳"]  ......一样？你吗？
[character(name="avg_npc_108")]
[name="玛恩纳"]  ......
[name="玛恩纳"]  那看来流放的日子里，你还是被你的那些萨卡兹朋友照顾得太好了。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[Character(name="char_empty", name2="char_148_nearl_1#6")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=350, fadetime=0.8, block=false)]
[Character(name="avg_npc_061#3", name2="char_148_nearl_1#6",fadetime=0.5)]
[delay(time=1.5)]
[name="玛莉娅"]  姐姐！
[Character(name="avg_npc_061#3", name2="char_148_nearl_1#6",focus=1)]
[name="玛莉娅"]  姐姐，你没事吧......！
[Character(name="avg_npc_061#3", name2="char_148_nearl_1#6",focus=2)]
[name="玛嘉烈"]  嗯......我没事。
[character]
[dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_064_weapon_1",fadetime=1.5)]
[delay(time=2)]
[name="佐菲娅"]  好啦玛莉娅，别抱这么紧。这家伙的手臂应该已经麻了。
[Character(name="avg_npc_061#3", name2="char_148_nearl_1#6",focus=1)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=80, fadeou

... (全文28764字符)
```

### level_act9mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-4
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G04",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]	
[character(name="avg_npc_223",fadetime=1)]
[delay(time=1.5)]
[name="工作人员"]  马克维茨先生！
[name="工作人员"]  这里，请过来这边，马克维茨先生！
[character]
[dialog]
[Character(name="avg_npc_223", name2="char_empty",focus=-1)]
[name="马克维茨"]  啊，原来是在这里。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_223", name2="avg_npc_211_1",fadetime=1)]
[delay(time=2)]
[Character(name="avg_npc_223", name2="avg_npc_211_1", focus=2)]
[name="马克维茨"]  抱歉，我对这里的路不太熟悉，耽搁了一点时间，让您久等了。
[name="马克维茨"]  谢谢您愿意来接我......
[Character(name="avg_npc_223", name2="avg_npc_211_1", focus=1)]
[name="工作人员"]  不......哪儿的话，这是我该做的。
[name="工作人员"]  请这边走，会场在对面的另一区域。
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=2)]
[name="马克维茨"]  好、好的。
[name="马克维茨"]  ......
[name="马克维茨"]  请问，您......
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=1)]
[name="工作人员"]  什么？
[Character(name="avg_npc_223", name2="avg_npc_211_1", focus=2)]
[name="马克维茨"]  不，算了，没什么。
[name="马克维茨"]  今天是特锦赛正赛前的座谈会......没错吧？
[Character(name="avg_npc_223", name2="avg_npc_211_1", focus=1)]
[name="工作人员"]  是的。这次聚会由商业联合会主办，虽说是座谈会，但形式比较轻松，各位发言人还有企业代表都会出席。
[Character(name="avg_npc_223", name2="avg_npc_211_1#5", focus=2)]
[name="马克维茨"]  嗯......
[Character(name="avg_npc_223", name2="avg_npc_211_1#5", focus=1)]
[name="工作人员"]  入场专用的邀请函应该已经提前发送给各位了，到时只需出示就可以。
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=2)]
[name="马克维茨"]  当然，当然......我带着呢......
[name="马克维茨"]  ......
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=1)]
[name="工作人员"]  请问......
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=2)]
[name="马克维茨"]  是、是的，我在，请、请说！
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=1)]
[name="工作人员"]  ......无意冒犯，请问您是否有什么需要帮助的地方？
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=2)]
[name="马克维茨"]  呃......什么？
[Character(name="avg_npc_223", name2="avg_npc_211_1#3", focus=1)]
[name="工作人员"]  非常抱歉，因为看见您一直在整理上衣......
[name="工作人员"]  如果您遇上了什么麻烦，有任何我可以帮忙的地方，都请尽管说。
[Character(name="avg_npc_223", name2="avg_npc_211_1#6", focus=2)]
[name="马克维茨"]  啊......衣服没有问题，我是说，不，不是什么大问题，只是......
[name="马克维茨"]  只是我还不太习惯......抱歉，这是我个人的问题，请不要在意。
[Character(name="avg_npc_223", name2="avg_npc_211_1#6", focus=1)]
[name="工作人员"]  是这样......
[name="工作人员"]  ......您看起来似乎有些紧张？
[Character(name="avg_npc_223", name2="avg_npc_211_1#6", focus=2)]
[name="马克维茨"]  是、是有一点，很抱歉。
[name="马克维茨"]  我还是第一次这么正式地参加这样的座谈会，稍微有些......不适应。
[Character(name="avg_npc_223", name2="avg_npc_211_1#6", focus=1)]
[name="工作人员"]  ......
[name="工作人员"]  您完全可以不用这样紧张，发言人马克维茨先生。
[name="工作人员"]  今天这场座谈会是由商业联合会发起的聚会，在到场的各位先生女士中，代表商业联合会的诸位发言人才是真正的大人物......
[name="工作人员"]  您大可以更放松一些。
[Character(name="avg_npc_223", name2="avg_npc_211_1#5", focus=2)]
[name="马克维茨"]  可是......我根本算不上什么大人物。我只是......只是机缘巧合......
[name="马克维茨"]  一定是有哪里搞错了，我不应该这样......
[Character(name="avg_npc_223", name2="avg_npc_211_1#5", focus=1)]
[name="工作人员"]  您......太谦虚了。
[Character(name="avg_npc_223", name2="avg_npc_211_1#5", focus=2)]
[name="马克维茨"]  我——
[dialog] 
[PlaySound(key="$phonevibration",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_223", name2="avg_npc_211_1#7", focus=2)]
[name="马克维茨"]  抱歉，电话......
[Character(name="avg_npc_223", name2="avg_npc_211_1#7", focus=1)]
[name="工作人员"]  您请。
[dialog]
[Character(name="avg_npc_223", name2="avg_npc_211_1#7")]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[character(name="avg_npc_223",name2="char_empty", fadetime=1)]
[delay(time=2)]
[character]
[character(name="avg_npc_211_1#3",fadetime=1)]
[delay(time=1.5)]
[name="马克维茨"]  您好，我是马克维茨......您请说。
[name="马克维茨"]  是、是的，没问题......
[name="马克维茨"]  都很合适，没有什么其他要添加的了，非常感谢您。
[name="马克维茨"]  啊，不用这么说，感谢您专程让人来接我。
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="马克维茨"]  不、不会！那位先生非常亲切，没有什么冒犯我的地方，都是我耽误了时间才迟了这么久，请、请您不要为难他......
[name="马克维茨"]  玩笑？......是、是的，当然只是个玩笑......
[name="马克维茨"]  是的，我很快就到。
[name="马克维茨"]  好的，一会见......
[dialog]
[PlaySound(key="$transmission",volume=0.6)]
[delay(time=1)]
[character(fadetime=1)]
[delay(time=1.5)]
[Dialog]
[Character(name="avg_npc_223", name2="char_empty")]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_223", name2="avg_npc_211_1",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_223", name2="avg_npc_211_1#4",focus=2)]
[name="马克维茨"]  抱歉，让您久等了。
[Character(name="avg_npc_223", name2="avg_npc_211_1#4", focus=1)]
[name="工作人员"]  ......哪里，您客气了。
[Character(name="avg_npc_223", name2="avg_npc_211_1#4",focus=2)]
[name="马克维茨"]  刚刚的话题——
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=80, fadeout=true, block=false)]
[name="马克维茨"]  ——啊！
[delay(time=0.8)]
[Character(name="avg_npc_223", name2="avg_npc_211_1#4", focus=1)]
[name="工作人员"]  请小心脚下的阶梯，马克维茨先生！
[name="工作人员"]  我们会从四号通道上楼，请您跟紧我。
[Character(name="avg_npc_223", name2="avg_npc_211_1#7",focus=2)]
[name="马克维茨"]  啊，好、好的，抱歉。
[name="马克维茨"]  ......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G03",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_223", name2="avg_npc_211_1",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_223", name2="avg_npc_211_1",focus=2)]
[name="马克维茨"]  ......
[Character(name="avg_npc_223", name2="avg_npc_211_1", focus=1)]
[name="工作人员"]  ......
[name="工作人员"]  前面就是座谈会会场了，您一直向前走，将邀请函交给门口服务生就好。
[Character(name="avg_npc_223", name2="avg_npc_211_1",focus=2)]
[name="马克维茨"]  好的，好的......谢谢。
[Character(name="avg_npc_223", name2="avg_

... (全文20003字符)
```

### level_act9mini_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔1.5-7
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]	
[playsound(key="$d_gen_walk_n")]
[character(name="char_204na_platnm_1",fadetime=1.5)]
[delay(time=2)]
在顺利结束了学生时代后。
我，欣特莱雅，正在选择自己的人生道路。
在卡西米尔，学生们结束学业后的人生选择多种多样。
参加大公司每年一度的全国性校招，和全卡西米尔的优秀人才竞争，获得一份劳累且堪堪糊口的工作。
又或是加入军队，经过一年的地狱式训练后在边境上祈祷战争不要开始。
[character(name="char_204na_platnm_1#7"  )]
啊，当然，为监正会工作也很有前景的，但那样的工作内容，我可是一点都不感兴趣。
所以......
[Dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_223",fadetime=1.5)]
[delay(time=2)]
[name="骑探"]  欣特莱雅小姐，请问您有兴趣来参加我司的骑士海选吗？
[character(name="char_204na_platnm_1#4")]
所以当这位玫瑰报业联合的员工递上名片时，我带着略为惊讶的表情，一边和对方寒暄一边收下了它。
骑士。
[character(name="char_204na_platnm_1#3")]
在卡西米尔，谁不想成为骑士呢？
谁不想，在成百上千人的拥簇下，坐享粉丝赞美和大笔收益呢？
虽然，一些关于骑士的丑闻时有发生，有些骑士甚至会在一夜间变得默默无闻，但这和我又有什么关系？
我能使一手好弓，外貌也不算差，最重要的，是我愿遵从公司的安排。
[character(name="char_204na_platnm_1#8")]
只要能成为骑士，就算打不过对方，最后像群月骑士团那样，唱唱歌跳跳舞，趁着年轻多赚一些然后早早退休，或许也是个不错的选择。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_23_G09",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="char_204_platnm_1",fadetime=1)]
[delay(time=1.5)]
最终，我拿下了玫瑰报业集团当年的骑士海选亚军，顺利获得了一份梦寐以求的合同。
[character(name="char_204_platnm_1#3")]
至于冠军，那个一头金色碎发，全身散发着太阳味的男人......
怎么说呢，他实在是......太过符合卡西米尔人对于库兰塔的想象了，出身也不错，估计玫瑰早已经内定他作为冠军了。
即使没有内定，想要在一场大型海选上击败他，也还是挺困难的。
至少在观众投票上就绝对赢不了。
[character(name="char_204_platnm_1#8")]
算啦，也没什么好抱怨的。
今后的路还长着，说不定，我会比他先拿到骑士封号。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_222",fadetime=1.5)]
[delay(time=2)]
[name="经纪人"]  您可以放心，欣特莱雅小姐，这次真的可以获得骑士封号了。
[name="经纪人"]  我已经向总部确认过，您现在是处理优先级最高的签约独立骑士。
[name="经纪人"]  近期比赛场数可能会削减，但会大量安排您在媒体上出镜。
[name="经纪人"]  只要再等几个月，获得了封号，您就是玫瑰新一批次中力推的封号骑士了！
[character(name="char_204_platnm_1")]
[name="欣特莱雅"]  嗯，好，谢谢。
我已经不是第一次听到这种许诺了。
什么远大未来，星光闪耀，玫瑰报业的全力支持。
他自己似乎都已经沉浸在了这种幻象里，比他负责的独立骑士还要相信这些许诺。
[character(name="char_204_platnm_1#5")]
唉，这位经纪人性格很好，很刻苦，总是在尽心尽力为我奔波。
但是，说实话。
我已经对成为骑士这件事有些厌倦了。
[character(name="char_204_platnm_1#7")]
尽管还没获得骑士封号，但一位正式骑士生涯中会遇到的问题，我却早就碰了个遍。
指名要在比赛中放水这种已经是最基础的了，除了要打得不像假赛这一点比较累人，其他倒还好。
至少还没被人识破，因此失去骑士资格。
至于应付毫无根据的花边绯闻，还有被迫接受随意变动的赛事安排这种事，实在太累人了。
[character(name="char_204_platnm_1#5")]
只因为我是这一期独立骑士中的种子选手，所以就得这样被呼来喊去吗？
骑士到底是什么？
商品吗？商品至少能买定离手后尘埃落定。
那我呢？
......
[character(name="char_204_platnm_1#3")]
如果说最近还有什么好消息的话，就是我的骑士封号申请已经被监正院公示了。
呵啊......漫长的独立骑士生涯，终于要临近尾声了。
很快，我就能获得自己的骑士封号，获得自己的徽记，然后出现在大街小巷的广告牌上了吧。
之前从来没有人在这个环节被筛下去的，也就是说......
打完眼前这场比赛后，我就可以等着获得封号，成为正式骑士了吧。
虽然这一场，“独立骑士欣特莱雅”的胜负早已被决定了——
是落败哦。
唉......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_hotel",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="char_204_platnm_1#6",fadetime=1)]
[delay(time=1.5)]
今天那一场的库兰塔，怎么回事？
我都已经装作体力不支落败了，也向裁判示意了，他怎么还在攻击我？
这就是他作为胜者的权利吗？在明知自己胜券在握的情况下把我像宠物羽兽一样撵着全赛场乱跑，肆意羞辱我，让我出丑？
要不是......要不是装作受伤这件事不能被观众发现，我一定——
[character(name="char_204_platnm_1#7")]
......
或许父亲说的对，作为骑士，就是去赛场上受辱的。
因为不甘受辱的人，要么用战锤把这规则下的敌人全部砸碎，要么就——
在一篇新闻报道后消失得无影无踪。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="char_204_platnm_1",fadetime=1)]
[delay(time=1.5)]
[stopmusic(fadetime=1)]
今天是玫瑰报业集团签约的独立骑士们上综艺节目的日子。
集团租用了一整座竞技场来拍摄节目，甚至还请来了几位近日大火的封号骑士。
但是在排练开始前，来了队不速之客。
[character]
[dialog]
[playsound(key="$d_gen_soldiersrun")]
[character(name="avg_npc_216",fadetime=1.5)]
[delay(time=2)]
他们把所有骑士带到角落里，挨个询问搜查。
在他们的厉声喝斥下，骑士们就像枯萎的花草那样缩在地上，生怕被无胄盟的人盯上。
即使是几位脾气不好的骑士，也没像平时那样飞扬跋扈，而是低眉顺眼，全力配合无胄盟的调查。
这就是......骑士杀手。
在看着几位骑士精神崩溃，听到几则情急之下脱口而出的惊爆猛料后，无胄盟带走了一位骑士。
而今天的活动，则在延迟四小时后重新开始录制。
[dialog]
[character(fadetime=1.5)]
[delay(time=2)]
至于那位被带走的骑士？我不知道，我再也没听说过和他有关的任何信息。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_hotel",screenadapt="coverall")]
[character(name="char_204_platnm_1")]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
就在那场意外发生后没多久，我接到了一通电话。
[dialog]
[delay(time=1.5)]
嘀嘀，嘀嘀
[PlaySound(key="$phonevibration",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[name="欣特莱雅"]  呼......你好。
[character(name="char_204_platnm_1",focus=-1)]
[name="？？？"]  你好，独立骑士欣特莱雅，恭喜你即将成为封号骑士。
[character(name="char_204_platnm_1#2")]
[name="欣特莱雅"]  我不知道你是怎么获得这个终端号码的，但如果是商业合作，请找我的经纪人去谈，谢谢。
[character(name="char_204_platnm_1#2",focus=-1)]
[name="？？？"]  看来你并不热爱现在这份的工作，你的语气里充满了疲惫。
[name="？？？"]  我能提供更适合你的工作。
[name="？？？"]  只要通过一个简单的测试，你就能获得它。
[character(name="char_204_platnm_1")]
在我仍处于困惑和犹豫的时候，终端那头的男人继续说到。
[character(name="char_204_platnm_1",focus=-1)]
[name="？？？"]  竞技场太过狭窄了，不是吗？
[name="？？？"]  箭在你手上只要稍稍一拨，就能从赛场的这头到那头。
[name="？？？"]  而我提供的这份工作，不仅薪资能和骑士们媲美，自由度也更高。
[name="？？？"]  只要你想，欣特莱雅小姐，你的箭能够洞穿大骑士领的夜幕。
[name="？？？"]  期待你的回应。
[character(name="char_204_platnm_1")]
挂断之后，他发送了一个地址到我的终端上。
我并不知道那里究竟有什么，试炼又需要我去做什么，但......
“只要你想，欣特莱雅小姐，你的箭能够洞穿大骑士领的夜幕。”
[character(name="char_204_platnm_1#8")]
哼，听上去可比拍广告要有意思多了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="char_204_platnm_1",fadetime=1.5)]
[delay(time=2)]
我到达了他发送的地址，那是一家花店，老板见到我之后，就从店里捧出了一束鲜花。
花束上的留言写着一个地址，一些信息，还有一个名字。
上一

... (全文17698字符)
```


## 统计

- 总字符数：171710
- 对话行数：1626


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
