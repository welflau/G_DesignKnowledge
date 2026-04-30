# 明日方舟 · 活动剧情 · act11d7（1段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act11d7」完整剧情脚本（1个文件，374行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act11d7
- 脚本文件数：1

### level_act11d7_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 棘刺篇
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Image]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[largebg(imagegroup="bg_beach_1/bg_beach_2", solidwidth="920/920", solidheight=720,x=-180)]
[Blocker(a=0, fadetime=1, block=true)]
[Image]
[Character]
[delay(time=1)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[largebg]
[Background(image="bg_sunnytown_2",x=0, y=0, xScale=1.1, yScale=1.1,block=true)]
[Blocker(a=0, fadetime=2, block=true)]
[delay(time=1)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="极境"]  喂喂，喂喂喂，接一下啊？总不能又不接通讯吧？
[name="极境"]  喂？啊，唉唉！听到了听到了。
[name="极境"]  哎，你总算接了......
[Dialog]
[Character(name="char_293_thorns_1",fadetime=1,block=true)]
[delay(time=2)]
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  你现在应该已经到那边了吧？怎么样，汐斯塔如何？
[name="极境"]  我听博士说，那边热得随时有人会晕倒在大街上，然后被免费的啤酒浇醒，是不是真的？
[name="极境"]  哎对了，这次的音乐节都来了哪些名人？大帝是不是要来？
[name="极境"]  哎，你见到日落即逝的成员了吗，我都用她们的曲子做背景音乐，你听这首——
[Character(name="char_293_thorns_1")]
[name="棘刺"]  有事直说，没事的话我挂了。
[Character(name="char_293_thorns_1",focus=2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="极境"]  等下等下等下，别这样！
[name="极境"]  有事有事，我还有事没说完，别挂兄弟！ 
[Character(name="char_293_thorns_1")]
[name="棘刺"]  （叹气）
[name="棘刺"]  如果你真的这么想来，为什么不来？
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  走不开啊！你以为我不想吗！
[name="极境"]  你们那么一大群人都去了，总得有人留在本舰吧。而且，我这边也还有点内部的任务要处理，你知道这次嘉维尔她——
[Character(name="char_293_thorns_1")]
[name="棘刺"]  停，任务内容不必告诉我。
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  耶，也不是什么要保密的事情啦。不过，那个，有一个事儿就比较......
[Character(name="char_293_thorns_1")]
[name="棘刺"]  说重点，还有什么事，三十字内概括一下。
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  哎，兄弟。
[name="极境"]  有没有人说过你真的很难相处？
[Character(name="char_293_thorns_1")]
[name="棘刺"]  没有。
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  真可怜，都没人敢和你说实话。
[Character(name="char_293_thorns_1")]
[name="棘刺"]  我挂了。
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  慢着，我这就说！
[name="极境"]  （吸气）
[name="极境"]  消息来源不太可靠但这次音乐节上可能会出乱子不过我觉得打起来你也不在乎所以如果遇到日落即逝成员麻烦帮我要张签名谢谢我说完了！
[Character(name="char_293_thorns_1")]
[name="棘刺"]  ......你要说的就是这个？
[Character(name="char_293_thorns_1",focus=2)]
[name="极境"]  嗯？是啊。
[Character(name="char_293_thorns_1")]
[name="棘刺"]  一共六十个字，超额百分之一百。
[name="棘刺"]  以及，如果你是用这个音量在办公室里放音乐，那再过十秒隔壁工程部的人一定会冲进来砸掉你的音响。
[Character]
[name="极境"]  啊？
[name="极境"]  等等？找我有事吗简......扰乱工作？那什么......啊呀我错了别别你听我解释别动手——
[Dialog]
[playsound(key="$transmission", volume=0.4)]
[delay(time=1)]
[Character(name="char_293_thorns_1")]
[name="棘刺"]  啧。
[name="棘刺"]  这家伙，到底有多喜欢那个乐队？
[name="棘刺"]  我都快能倒背歌词了......嗯？
[Dialog]
[Character]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]  虽然风景很好，但是这里果然好热啊！尾巴都能挤出水了欸！
[name="普罗旺斯"]  汐斯塔当地的气温好像比我推测的还要高，这有点怪......哎，天火，你有没有觉得热？
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]  我们穿成这样，不热才奇怪吧。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]  呃，那倒也是。
[name="普罗旺斯"]  大家都穿得太多了，这么下去搞不好真的会中暑，最好是能换一身衣服......听说这回有机会去海边，所以我有特地带泳装来哦。
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=2)]
[name="天火"]  等会，现在还不行！我们不是要去火山脚下吗，总得等到回来之后再说！
[Character(name="char_145_prove_1",name2="char_166_skfire_3#1",focus=1)]
[name="普罗旺斯"]  那就早去早回，我也想好好享受一下沙滩，这种机会可不是经常会有的好吗！
[PlaySound(key="$d_gen_walk_n")]
[Dialog]
[Character]
[delay(time=1)]
[Character(name="char_293_thorns_1")]
[name="棘刺"]  ......
[name="棘刺"]  沙滩，海？
[name="棘刺"]  ......这里闻起来可不像是有海的样子。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_sunnytown_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$livecrowd")]
[Character(name="npc_2004_Alty")]
[name="Alty"]  呼，这是第几曲了？晚上还有演出呀，怎么提前就兴奋起来了。
[Character(name="npc_2001_Aya_1")]
[name="Aya"]  不知道，不过我还挺开心的，Frost也是吧。
[Character(name="npc_2003_Frost_1")]
[name="Frost"]  （拨弦）
[Character(name="npc_2002_Dan_1")]
[name="Dan"]  反正也没什么关系吧，我们又不会累。
[Character(name="npc_2004_Alty")]
[name="Alty"]  哎呀，哈哈，也有道理。
[name="Alty"]  行啦，那么，在夜晚到来之前——
[name="Alty"]  就让我们提前狂欢吧！！
[Dialog]
[Character]
[PlaySound(key="$livecrowd")]
[delay(time=2)]
[Character(name="char_293_thorns_1")]
[name="棘刺"]  （这就是那家伙喜欢的乐队？这个风格，果然很吵。）
[name="棘刺"]  （而且......）
[name="棘刺"]  （很奇怪，有什么东西不对劲。)
[name="棘刺"]  （是因为这首歌？这种熟悉的感觉是......什么？）
[Dialog]
[Character]
[delay(time=2)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Character(name="avg_npc_020")]
[name="保镖A"]  找到大小姐了吗？！
[name="保镖B"]  快点！快追，他们一定没跑远！
[name="保镖A"]  从这边走，一定要把大小姐带回来！
[Character]
[name="歌迷A"]  挤什么挤什么，哎真没素质！
[name="歌迷B"]  靠谁踩了我一脚？
[name="歌迷C"]  别管那些人，她们又开始唱下一首了，啊啊啊这是《海中深色》里收录的第一首曲子！
[PlaySound(key="$livecrowd")]
[Character(name="char_293_thorns_1")]
[name="棘刺"]  嗯？
[name="棘刺"]  （从刚刚开始，这些人到底在找什么？）
[name="棘刺"]  （这样的着装风格，不像是民间的什么组织......）
[Dialog]
[Character]
[name="？？？"]  借过，不好意思，借过一下！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="char_290_vigna",fadetime=1,block=true)]
[Delay(time=1)]
[name="红豆"]  呼，总算出来了......
[Character(name="char_293_thorns_1")]
[name="棘刺"]  你急着去哪？
[Character(name="char_290_vigna")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="红豆"]  哇！什么人！
[name="红豆"]  咦，是棘刺，吓我一跳......既然你也在这，就说明你也是日落既逝的歌迷咯？
[name="红豆"]  也是，我记得你是阿戈尔人，我总觉得你们阿戈尔人没人能拒绝她们，她们唱的海比汐斯塔的波浪还要更美、更带劲！
[Character(name="char_293_thorns_1")]
[name="棘刺"]  ......
[Character(name="char_290_vigna")]
[name="红豆"]  哎呀，不对，现在不是说这个的时候！
[name="红豆"]  博士他们现在好像很需要帮忙，我正要赶过去！既然碰上了，你也别愣着，我们一起——
[Character(name="char_293_thorns_1",name2="char_290_vigna",focus=1)]
[name="棘刺"]  博士那里不必我去。
[Character(name="char_293_thorns_1",name2="char_290_vigna",f

... (全文30987字符)
```


## 统计

- 总字符数：30987
- 对话行数：374


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
