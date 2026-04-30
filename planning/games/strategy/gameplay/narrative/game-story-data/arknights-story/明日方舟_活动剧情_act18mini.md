# 明日方舟 · 活动剧情 · act18mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act18mini」完整剧情脚本（6个文件，1725行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act18mini
- 脚本文件数：6

### level_act18mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Sticker(id="st1", text="一切将归于火。", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st1", duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st2", text="而你，我不驯顺的影子，你原有不投身其中的权利。", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st2", duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st3", text="既然最终你选择一起踏入火中，", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st3", duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st4", text="那便来吧，", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st4", duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st5", text="来参加这连影子也失掉了的盛大的燃烧。", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st5", duration=1,block = false)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot]
[Background(image="34_g9_tent",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_amb_forestnight_loop", volume=0, loop=true, channel="e")]
[SoundVolume(volume=0.3, channel="e",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_416_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="失去土地的农民"]所以说，我们现在已经到伦蒂尼姆外围了？
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="逃离城市的手艺人"]听说是的。
[name="逃离城市的手艺人"]这真是我这辈子走过的最远的路。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="失去土地的农民"]你走得再远，有莫兰他们远吗？
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="逃离城市的手艺人"]他们？他们从石高原野就一直跟着领袖了，我怎么和他们比。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="失去土地的农民"]不管走了多远，反正我们都到这里了。下一步怎么说，打仗吗？
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="逃离城市的手艺人"]打就打呗，反正这一路我们也没少打——乱窜的萨卡兹、荒地上的劫匪、贵族的私兵......
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="被抛弃的伤兵"]......
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="逃离城市的手艺人"]抱歉，不是说你。我说的是专门针对塔拉人的那种，你别在意。
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="被抛弃的伤兵"]我知道。我是想说......
[name="被抛弃的伤兵"]不，没什么。
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="逃离城市的手艺人"]吞吞吐吐的就没意思了。你腿怎么样了，好利索了吗？要不要来跳支舞？
[Dialog]
[charslot(duration=0.7)]
[Delay(time=1)]
[SoundVolume(volume=0.6, channel="e",fadetime=1)]
夏末秋初略显闷热的风自顾自地吹着，空气中尽是原野和沼泽的气息。
脱队的士兵抬头望向伦蒂尼姆的方向。零星的炮声并不怎么刺耳，传闻中的萨卡兹巫术也未见踪影。
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="被抛弃的伤兵"]跳就跳，你别踩我脚就行。
[Dialog]
[StopSound(channel="e", fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="34_g4_swamp_n",screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_728_1#3$1")]
[charslot(slot="r",name="avg_1020_reed2_1#9$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_728_1#3$1",focus="l")]
[name="莫兰"]营地那边有人跳舞？动静太大了，我去劝他们停下。这里离战场已经很近了。
[charslot(slot="r",name="avg_1020_reed2_1#9$1",focus="r")]
[name="苇草"]不用，只要还在营地范围内，我们就还是安全的。
[charslot(slot="l",name="avg_npc_728_1#1$1",focus="l")]
[name="莫兰"]但我们总得继续前进。
[charslot(slot="r",name="avg_1020_reed2_1#3$1",focus="r")]
[name="苇草"]......不。
[charslot(slot="r",name="avg_1020_reed2_1#1$1",focus="r")]
[name="苇草"]接下来，穿过战场的路，我得一个人走。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot="m",name="avg_npc_416_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="失去土地的农民"]苇草、莫兰，来跳舞吧！
[charslot(slot="m",name="avg_1020_reed2_1#9$1",focus="m")]
[name="苇草"]......你们来了啊。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="失去土地的农民"]前面就是战场了，大家会怎么样都说不定......
[name="失去土地的农民"]不过，趁大伙还都好好的，怎么也得好好跳场舞！
[name="失去土地的农民"]苇草，我们都得动动，说不定就不怕了——
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="苇草"]正好......接下来这段时间，请大家在营地里驻扎，不要再前进了。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="失去土地的农民"]欸？我们不去战场吗？
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="苇草"]那对你们来说太危险了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_242",duration=0.7)]
[charslot(slot="r",name="avg_npc_423_1#1$1",duration=0.7)]
[delay(time=1.5)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="逃离城市的手艺人"]你要一个人往前？
[charslot(slot="m",name="avg_1020_reed2_1#12$1",focus="m")]
[name="苇草"]抱歉。
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="被抛弃的伤兵"]要走多久？
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="苇草"]不知道，但我一定会回来。
[charslot(slot="m",name="avg_npc_728_1#1$1",focus="m")]
[name="莫兰"]苇草，所有跟着你的人都知道自己是来打仗的。
[name="莫兰"]大家都明白，要参与面前这场惨烈的战争，我们还不够格。可我们还是想帮你，哪怕挡几发弩箭。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="苇草"]我也一样不够格。
[charslot(slot="m",name="avg_npc_728_1#3$1",focus="m")]
[name="莫兰"]......苇草？
[charslot(slot="m",name="avg_1020_reed2_1#13$1",focus="m")]
[name="苇草"]不论是威灵顿、其他几位大公爵，还是萨卡兹，他们是举足轻重的砝码，而我们......
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="苇草"]无论投到哪边，作为战力，我们在天平上的重量都比不上哪怕一粒灰尘。你们如此，我也一样。
[charslot(slot="m",name="avg_npc_728_1#3$1",focus="m")]
[name="莫兰"]那你？
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="苇草"]我只是去做我本就该做的事情。
[name="苇草"]这件事并不比为了同胞向维多利亚人拔剑高尚分毫。我只是不能不去面对它......
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[nam

... (全文29875字符)
```

### level_act18mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_offce",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_081",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_081",focus="m")]
[name="助理"]主编先生，这是关于切尔诺伯格的全部资料，我给您放在桌子上了。
[name="助理"]希望您能从这些满是灰尘的东西里找到想要的信息。
[Dialog]
[charslot]
[name="主编"]谢谢你的整理，热尼亚。
[Dialog]
[charslot(slot="m",name="avg_npc_081",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[charslot(duration=1)]
[Delay(time=2)]
[PlaySound(key="$d_avg_woodenladder",volume=0.8,channel="w",loop=false)]
[stopsound(channel="w",fadetime=1)]
[playsound(key="$doorclosequite",delay=1.4)]
[Delay(time=1)]
助理离开时习惯性地将门带上，老旧的门蹭过不平的地板，发出的声音堪比惨叫。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[PlaySound(key="$d_avg_lighter", volume=0.7,delay=1.5)]
[Delay(time=2)]
坐直身体，主编点起一根烟，忍住不适开始翻阅眼前堆成山的旧报纸。
[Dialog]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=1)]
[name="主编"]《第三集团军在切尔诺伯格事件中的渎职......》。
[name="主编"]啧......老调重弹的东西，《切尔诺伯格关闭的矿场——对乌萨斯源石工业的打击》。
[name="主编"]......《新切尔诺伯格——在陛下的光辉下，感染者的幸福生活》。
[name="主编"]简直是无稽之谈。
[name="主编"]不，都不是我要找的......这些破烂不过是在最外面兜圈子。
[name="主编"]......没有一篇报道能够接近真相。
[Dialog]
[PlaySound(key="$burningloop1", volume=0.9, loop=true, channel="burn")]
[Delay(time=1)]
主编推高滑下的眼镜，弹了弹烟灰，却不慎将火星溅在纸上。
[Dialog]
[PlaySound(key="$d_avg_chairbump", volume=0.7)]
[StopSound(channel="burn", fadetime=2)]
[Delay(time=1.5)]
他急忙扑灭燃起的火苗，可报纸已被灼烧出一个洞。
透过小洞，主编看到一行小小的文字——“整合运动”。
那是他从未见过的名字。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_warehouse_2",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_043_1#2",duration=0.7)]
[charslot(slot="r",name="char_011_talula_1#3",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="char_011_talula_1#3",focus="r")]
[name="塔露拉"]这几天，陆续有感染者找到我们，表达了自己想要加入整合运动的意愿。
[name="塔露拉"]我告诉他们，一个月后，我们将离开伦蒂尼姆，去往高多汀公爵领。
[charslot(slot="l",name="avg_npc_043_1#2",focus="l")]
[name="九"]即便如此，他们也愿意和我们一同出走吗？
[charslot(slot="r",name="char_011_talula_1#3",focus="r")]
[name="塔露拉"]没有同意，也没有拒绝。他们自己没有答案。
[charslot(slot="l",name="avg_npc_043_1#2",focus="l")]
[name="九"]......我会做好带他们离开的准备，他们已经没有其他地方可去了。
[name="九"]高多汀公爵领。听说那位公爵颁布了许多改善感染者生活条件的命令，的确需要观察一下。
[charslot(slot="r",name="char_011_talula_1#3",focus="r")]
[name="塔露拉"]命令无法代表现实。
[charslot(slot="l",name="avg_npc_043_1#2",focus="l")]
[name="九"]我当然清楚这一点，塔露拉。所以亲自去确认一下才更有价值。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_paper1", volume=1)]
[Delay(time=1)]
角落处，陈将手中的报纸翻过一页，发出轻微的哗啦声。
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]陈，你在旁边听了那么久，打算一直不说话吗？
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]这是你们内部的事情，九。
[name="陈"]这些事轮不上我发表看法，我的注意力都在报纸上。
[charslot(slot="m",name="char_011_talula_1#3",focus="m")]
[name="塔露拉"]你私下与队伍中许多人交流时的表态可并不是这样。
[name="塔露拉"]我们需要你的意见，晖洁。
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]我放任你留在我们身边，并非只是为了向你证明这支队伍有多么不一样，陈。
[name="九"]不必自以为是地认为你对我和塔露拉负有责任。
[name="九"]如今的情况下，任何能帮上这些人的力量我都不会拒绝。你大可说明你的看法。
[charslot(slot="m",name="avg_npc_662_1#7$1",focus="m")]
[name="陈"]......
[Dialog]
[PlaySound(key="$d_avg_scroll", volume=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]你们是想接纳那些无处可去的人吗？
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]为何不？
[name="九"]他们会成为我们新的有生力量。
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]或者是新的矛盾。
[name="陈"]这支被你们以所谓“整合运动”的名号聚拢的队伍，各种身份的人混杂其中。
[name="陈"]九，这就是你当初离开时向我许下的愿景吗？
[charslot(slot="m",name="avg_npc_662_1#7$1",focus="m")]
[name="陈"]还加上她。
[Dialog]
[charslot]
陈看向了淡然的塔露拉。
[charslot(slot="m",name="char_011_talula_1#3",focus="m")]
[name="塔露拉"]......
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]你们迟早会引来更多的目光。
[name="陈"]如果你问我，我建议你们暂时停留在伦蒂尼姆一段时间，稍作休整——
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]然后让更合适的人来处理这件事，对吧？
[charslot(slot="m",name="avg_npc_662_1#1$1",focus="m")]
[name="陈"]我不否认。
[name="陈"]看看你们这支队伍中的人，罪犯、感染者、从战场逃离的军人......你真的知道自己要把他们带到什么地方去吗？
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]至少绝不是停留在原地。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot="m",name="char_1002_nsabr_1",duration=0.5)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]怎么了？这么着急？
[charslot(slot="m",name="char_1002_nsabr_1",focus="m")]
[name="整合运动战士"]......九，雷德刚刚带回来一个紧急的消息。呃——
[Dialog]
[charslot]
他瞥了一眼身边的陈。
自从这个名为“陈”的陌生人来到他们的队伍，周围的同伴就都表现得很奇怪。
她很少离开塔露拉和九的身边，也从不对整合运动的行动发表任何看法。
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]说吧，她是自己人。
[charslot(slot="m",name="char_1002_nsabr_1",focus="m")]
[name="整合运动战士"]......工厂附近有一支公爵联军的部队正在靠近。需要让他们离开吗，九？
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[name="九"]公爵联军？虽然他们应该不会特意针对我们......我亲自去看看。
[name="九"]塔露拉......带着大家隐蔽起来。
[charslot(slot="m",name="char_011_talula_1#3",focus="m")]
[name="塔露拉"]放心。
[Dialog]
[charslot(slot="m",name="avg_npc_043_1#2",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[charslot(duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_662_1#6$1",focus="m")]
[name="陈"]你也认同九的做法？
[charslot(slot="m",name="char_011_talula_1#3",focus="m")]
[name="塔露拉"]......并不完全同意。但这支队伍，和最初那支与我在雪原上同行的队伍很不一样。
[name="塔露拉"]遗憾的是，对待这些被压迫的人，这片大地上的任何地方都没有区别。
[name="塔露拉"]晖洁，没人在乎这些人去哪里，他们只在乎我们最后停在哪里。然后思索，到底该如何驱逐我们。
[charslot(slot="m",name="avg_npc_662_1#6$1",focus="m")]
[name="陈"]......
[charslot(slot="m",na

... (全文31549字符)
```

### level_act18mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="32_g1_lentiavenue",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[playsound(key="$d_avg_crowdtalk_fear", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.8, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_418_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]奥利，跟紧我......！
[name="慌乱的女性"]你不愿让我抱着，就必须得自己牢牢地跟紧了。抓住我的衣服，知道吗？
[name="慌乱的女性"]妈妈没办法牵着你的手......我手上全是汗水，会滑开的！所以，你一定要抓紧我的衣服。
[Dialog]
[charslot]
[name="寡言的孩子"]（点头）
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]柯林，柯林！你在哪儿？咱们到底还能出去吗？
[name="慌乱的女性"]实在不行，我们还是先躲回家里去吧！孩子这样小，要怎么跟着我们逃命呢？
[name="慌乱的女性"]柯林——
[Dialog]
[PlaySound(key="$d_avg_explosion",volume=0.4)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]啊！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_416_1#1$1",duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]快来，我找到一条路！典范军进城后，看守咱们的那些魔族佬也都被引开了，只要不撞上爆炸——
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]“只要不撞上爆炸”！杂货店的施瓦尔背着家当跑出来，只是在发红光的地方摔了一跤......
[name="慌乱的女性"]伤口不过巴掌大，却把身上的血都流干了，你忘啦？
[name="慌乱的女性"]......不，是被“抽”干了......那样的东西真的还是爆炸吗？
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]那都是因为他的伤口一直没愈合！只要咱们小心些，别受伤，也别流血，就不会有问题。
[name="紧张的男性"]无论如何，现在绝不能往回走。
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]刚才炸开的地方离我们这儿不超过两百米，比起莫名其妙死在半路上，我宁可回去。
[name="慌乱的女性"]柯林，你祖母还在城里呢——
[Dialog]
[charslot]
[StopSound(channel="bgs", fadetime=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_1066_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]......往回走只会更危险。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]你是——
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]没人能确定封锁区里的萨卡兹是不是全都被调离了。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]你从外面进来，是典范军？你们是来帮我们的吗？求求你，救救我们！
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]......抱歉，我不是典范军，我和他们没有关系，也不为救人而来。
[name="诺威尔"]我来伦蒂尼姆，只为了找一个人。
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]找谁？你的鞋子都磨破了，可到现在的伦蒂尼姆来，还能找到谁？
[name="慌乱的女性"]你不是典范军，你只是个和我们一样的可怜人。柯林，我们往回走吧......
[charslot(slot="m",name="avg_npc_1066_1#6$1",focus="m")]
[name="诺威尔"]......
[charslot(slot="m",name="avg_npc_1066_1#5$1",focus="m")]
[name="诺威尔"]唉。
[Dialog]
[charslot]
男人重重地叹息，再次谨慎地打量四周。
时隔多年，他再次作为配镜师来到伦蒂尼姆。这座城市如今的样貌，就像在工坊的热气中举起镜片查验，画面模糊而失真。
等到终于看清，映入眼帘的仅剩动荡。要在这样的混乱中准确找到一个行踪诡谲、不知面貌的存在并非易事。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]先生，您想要什么？我把我身上所有值钱的东西都给您，能不能求您带我们出去？
[name="紧张的男性"]您独自进了封锁区却毫发无伤，这代表您一定知道安全的路。我请求您......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_pcket", volume=1)]
[PlaySound(key="$d_avg_cloakmovement", volume=1,delay=0.7)]
[Delay(time=1.5)]
瘦小的男子低头将身上口袋摸遍，又从包裹里掏出几块面包，试图塞到诺威尔手里。一旁的女性也连忙从身上掏出零碎的钱币来。
[charslot(slot="m",name="avg_npc_1066_1#6$1",focus="m")]
[name="诺威尔"]......
[Dialog]
[charslot]
诺威尔没有伸手去接。他摇了摇头，知道眼前三人的未来与路边流干了血的尸体仅有一线之隔。
自己站在那条纤细的隔断之后，从来都如此旁观。
他曾经伸出过双手，可仅靠这一双手，无法挽救所有人。
[charslot(slot="m",name="avg_npc_1066_1#6$1",focus="m")]
[name="诺威尔"]抱歉......
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]先生！
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]柯林，我们走吧，他不会答应的......
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]我们没有其他的办法了！
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]......虽然我不是典范军，但我知道他们驻扎在哪。
[name="诺威尔"]我可以带你们去典范军的据点。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]......！谢谢、谢谢您！
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]仅此而已，我也不能做更多了。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]好、好，已经足够好了，我们都跟您走！
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]柯林，那你祖母呢？
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]等这些事情都结束，我们会回来接她的。魔族佬再怎么残忍，也不至于对疗养院里手无寸铁的老人下手——
[name="紧张的男性"]对吧？
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]......
[name="诺威尔"]我带你们出去，至于之后如何......
[name="诺威尔"]就只能靠你们自己了。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]没关系，这足够了。谢谢您，好心的先生！
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]......不用。牵好孩子，跟在我身后。
[name="诺威尔"]这边走。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="37_g3_fogblockadestreet_d",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_openftstpwalk", volume=1, loop=true, channel="walk1")]
[PlaySound(key="$d_gen_walk_n",loop=true,channel="walk2",volume=0.5,delay=0.3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[stopSound(channel="walk1", fadetime=1)]
[stopSound(channel="walk2", fadetime=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1066_1#1$1",focus="m")]
[name="诺威尔"]就从这里继续往前，一直走到城墙下。
[name="诺威尔"]城墙下有处被轰炸出来的空洞，典范军的一部分人正驻扎在那周围。
[name="诺威尔"]再往外，应该是公爵联军的队伍。你们也可以自己选择去向谁求助。
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="紧张的男性"]我们......
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]那您呢，您去哪儿？听您的意思，是不会继续同我们一起走了。
[name="慌乱的女性"]您在刚才救了我们的命。虽然我不明白是怎样做到的，但至少让我们也为您做些什么吧。
[charslot(slot="m",name="avg_npc_1066_1#9$1",focus="m")]
[name="诺威尔"]不用。伤口已经愈合了。
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="慌乱的女性"]就算——就算您再天赋异禀，那些炮火对您也不会比对我们更加仁慈。要我说，您就应该和我们一起

... (全文36494字符)
```

### level_act18mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_battlefield",screenadapt="showall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_mgcbttlfld",volume=0.3,channel="1",loop=true)]
[PlaySound(key="$d_avg_battlepresent",volume=0.3,channel="2",loop=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="这片异国的土地上已经浸满了萨卡兹的血。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="斑驳，混杂，我能触碰到混沌的情绪纠缠在一起。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="犹豫，愤怒，胆怯，思乡。殿下，这就是您所愿吗？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="睡吧，我的同胞。只要血一直流，你很快就连痛也感觉不到了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......我来得太晚了？也许吧。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="如果战争真的有结局，如果结局真的能论输赢......我们萨卡兹什么时候赢过？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不过，我不爱看钟表，只喜欢按照自己心脏的跳动来计时。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="它现在催促着我来这里，我就来了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[stopsound(channel="1",fadetime=2)]
[stopsound(channel="2",fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cherunder_2",screenadapt="showall")]
[Delay(time=2)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)] 
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_003_kalts_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]自从你们那位亲王独自远走，航船们分崩离析后，玫瑰河畔在我的认知中便已经解散。
[charslot(slot="m",name="avg_003_kalts_1#2$1",focus="m")]
[name="凯尔希"]曾经的航船中，转而为军事委员会效力的人不在少数。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]如今军事委员会刚露出颓势，你就重新恢复我们之间沉寂多年的通讯，我无法保证你能从我这得到你想要的东西。
[Dialog]
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="none")]
[name="神秘的血魔"]一点情分都不讲？你还是老样子，凯尔希。
[name="神秘的血魔"]阿米娅成长得很快。不过现在她也在暗处提防着我，对吧？
[charslot(slot="m",name="avg_003_kalts_1#2$1",focus="m")]
[name="凯尔希"]必要的准备。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="m")]
[name="凯尔希"]Logos已经向我们预警了你的出现。
[name="凯尔希"]我们从坠落的飞空艇撤离后，你是第一个接触到我们安全点的外人。
[charslot(slot="m",name="avg_003_kalts_1#1$1",focus="none")]
[name="神秘的血魔"]......“外人”。
[name="神秘的血魔"]勋爵，或许你跟我一样，伤心的时候最不好说话？
[charslot(slot="m",name="avg_003_kalts_1#2$1",focus="m")]
[name="凯尔希"]隐德来希，这里不是巴别塔的安全点。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_1521_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot]
[charslot(slot="l",name="avg_003_kalts_1#2$1",focus="r")]
[charslot(slot="r",name="avg_npc_1521_1#1$1",focus="r")]
[name="隐德来希"]......
[charslot(slot="r",name="avg_npc_1521_1#3$1",focus="r")]
[name="隐德来希"]这个代号从你的嘴里说出来，真让我怀念那些日子。
[name="隐德来希"]我来时经过伦蒂尼姆城内外的整片战场，救了一些人，也送走了一些人。
[name="隐德来希"]看着同胞们沦陷在这片不属于他们的土地上，那种滋味并不好受，凯尔希。
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]我不记得你是多愁善感的人。
[Dialog]
[charslot(slot="r",name="avg_npc_1521_1#3$1",focus="all")]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_npc_1521_1#3$1",focus="none")]
血魔沉默了，凯尔希看出了她并不愿意对此有任何回应。
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]隐德来希，为什么冒着危险深入维多利亚战场来见我？
[name="凯尔希"]如果你需要得到帮助，特雷西斯会是更好的选择。
[charslot(slot="r",name="avg_npc_1521_1#8$1",focus="r")]
[name="隐德来希"]不必试探我，凯尔希。我对摄政王要做的事情毫无兴趣。或许我们之中有些姐妹认可了摄政王的想法，但你也知道......
[charslot(slot="r",name="avg_npc_1521_1#4$1",focus="r")]
[name="隐德来希"]自特蕾西娅殿下在巴别塔遭遇意外之后，我们姐妹间的联系越来越少，互相之间的约束也在减弱。
[charslot(slot="r",name="avg_npc_1521_1#1$1",focus="r")]
[name="隐德来希"]不过这并不是我来找你的原因，凯尔希。阿斯卡纶那边，我打算帮她一点小忙，让她进城的路容易些。
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]你索求什么？
[charslot(slot="r",name="avg_npc_1521_1#3$1",focus="r")]
[name="隐德来希"]......
[charslot(slot="l",name="avg_003_kalts_1#3$1",focus="l")]
[name="凯尔希"]按照我们收到的即时讯息，城内军事委员会正在加强管控。
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]食腐者的军队与维多利亚公爵的大军正以城墙为前线对峙，情势瞬息万变。
[charslot(slot="r",name="avg_npc_1521_1#8$1",focus="r")]
[name="隐德来希"]我当然清楚，但她那样一个可爱又好学的年轻人，还是值得我去关照的。
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]不，我在意的是在这种局势下，你不该找得到阿斯卡纶的踪迹。我对她的手段很清楚。
[charslot(slot="r",name="avg_npc_1521_1#4$1",focus="r")]
[name="隐德来希"]她受伤了。伤势不轻。
[charslot(slot="l",name="avg_003_kalts_1#2$1",focus="l")]
[name="凯尔希"]......
[name="凯尔希"]她从不容忍自己用受伤这种借口放松警惕。
[charslot(slot="r",name="avg_npc_1521_1#1$1",focus="r")]
[name="隐德来希"]你很信任她。很难说，被你如此看重，我该为她开心还是为她担心。
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]谁在帮你？
[charslot(slot="r",name="avg_npc_1521_1#1$1",focus="r")]
[name="隐德来希"]“小聪明”，我们那位耳目好使的姐妹。作为技术人员，她在伦蒂尼姆追查到了一些我在意的线索。
[charslot(slot="l",name="avg_003_kalts_1#6$1",focus="l")]
[name="凯尔希"]她？我记得你们以前很爱惜她，绝对不会同意她贸然涉足战场中心。而且按照你们航船之间当初的约定，你们任何一个人都不该来。
[charslot(slot="r",name="avg_npc_1521_1#4$1",focus="r")]
[name="隐德来希"]......你果然清楚我们当年的事，她的情报没错，你有亲王的线索。
[charslot(slot="r",name="avg_npc_1521_1#8$1",focus="r")]
[name="隐德来希"]勋爵，那你应该也清楚，我是唯一那个，绝不会，也无法从这条血河上离开的人。
[charslot(slot="r",name="avg_npc_1521_1#9$1",focus="r")]
[name="隐德来希"]我都这样说了，你还怀疑我吗？
[charslot(slot="l",name="avg_003_kalts_1#1$1",focus="l")]
[name="凯尔希"]罗德岛会感谢你的帮助，我们会回报航船的付出，就和在巴别塔时特蕾西娅做的那样。
[name="凯尔希"]我会告诉你我所知道的线索，关于那位亲王。
[charslot(slot="r",name="avg_npc_1521_1#9$1",focus="r")]
[name="隐德来希"]谢谢你，凯尔希。
[charslot(slot="r",name="avg_npc_1521_1#1$1",focus="r")]
[name="隐德来希"]另外，我在这座城市的地下闻到些属于杜卡雷的臭血味，我很愿意顺手替你们解决——
[name="隐德来希"]但我需要你

... (全文34229字符)
```

### level_act18mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="32_g9_kingrest",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="诸王啊，你们能听到维多利亚的哭泣吗？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="火焰燎伤了母亲的肌肤......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我飞过她的头顶，却听不到她求救的声音。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="只有叹息。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可母亲在为谁而叹息——", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4071_peper_1#9$1",duration=1.5)]
[Delay(time=2)]
[name="明椒"]......
[charslot(slot="m",name="avg_4087_ines_1#1$1",focus="m")]
[name="伊内丝"]你没必要替这些蒸汽骑士和佣兵收尸，维多利亚人自己早就建好了这座坟墓留给这些人。
[charslot(slot="m",name="avg_4071_peper_1#9$1",focus="m")]
[name="明椒"]我知道，伊内丝小姐......只是......
[Dialog]
[charslot(slot="m",name="avg_4071_peper_1#9$1",focus="m")]
明椒轻轻捏着被鲜血染红的稿纸，她试图想象眼前这位蒸汽骑士死前写下这些词句时的场景。
[charslot(slot="m",name="avg_4071_peper_1#9$1",focus="m")]
[name="明椒"]这些蒸汽骑士的家就在这里，但这些萨卡兹不应该留在这。
[name="明椒"]如果赫德雷先生真的能用“生命脊椎”把大家带回卡兹戴尔，我们能带着这些同胞一起回家吗？
[charslot(slot="m",name="avg_4087_ines_1#2$1",focus="m")]
[name="伊内丝"]如果你决定了，那就去做。
[charslot(slot="m",name="avg_4087_ines_1#1$1",focus="m")]
[name="伊内丝"]卡兹戴尔可不是你的家，明椒，你想清楚了？
[charslot(slot="m",name="avg_4071_peper_1#4$1",focus="m")]
[name="明椒"]我、我要是想回哥伦比亚也总是有办法的——
[Dialog]
[charslot]
[name="？？？"]跟着大部队一起回去恐怕已经是目前最稳妥的办法了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_4088_hodrer_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4088_hodrer_1#1$1",focus="m")]
[name="赫德雷"]留在维多利亚，或是现在就回哥伦比亚都不安全。
[charslot(slot="m",name="avg_4088_hodrer_1#6$1",focus="m")]
[multiline(name="赫德雷")]按现在的局势来看
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[multiline(name="赫德雷",end=true)]——唔。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="20,-20",duration=1)]
[charslot(slot="l",name="avg_4087_ines_1#1$1",posfrom="-100,0",posto="0,0",duration=1)]
[charslot(slot="l",afrom=0,ato=1,duration=0.5)]
[Delay(time=1.5)]
[charslot(slot="l",focus="l")]
[name="伊内丝"]你最好还是别假装自己没受过伤。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot="l",posfrom="0,0",posto="-150,0",duration=2.5)]
[charslot(slot="m",posfrom="20,-20",posto="0,0",duration=1)]
[Delay(time=3.5)]
[charslot(slot="m",name="avg_4088_hodrer_1#2$1",focus="m")]
[name="赫德雷"]我死不了，也不能死。况且，我们的动作已经够慢了。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4071_peper_1#9$1",focus="m")]
[name="明椒"]赫德雷先生，骸骨恢复的状况怎么样了？
[charslot(slot="m",name="avg_4088_hodrer_1#1$1",focus="m")]
[name="赫德雷"]至少在我们回卡兹戴尔之前不会散架......如果没有其他“意外伤害”的话。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_1035_wisdel_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="维什戴尔"]哦，听上去像是在警告我？
[charslot(slot="m",name="avg_1035_wisdel_1#1$1",focus="m")]
[name="维什戴尔"]你恢复得不错嘛，赫德雷。
[charslot(slot="m",name="avg_4087_ines_1#1$1",focus="m")]
[name="伊内丝"]W，外面的状况如何？
[charslot(slot="m",name="avg_1035_wisdel_1#6$1",focus="m")]
[name="维什戴尔"]......
[name="维什戴尔"]我姑且不会因为名字和你生气，伊内丝。
[charslot(slot="m",name="avg_4087_ines_1#10$1",focus="m")]
[name="伊内丝"]哼，那更好。所以外面的情况如何？
[charslot(slot="m",name="avg_1035_wisdel_1#6$1",focus="m")]
[name="维什戴尔"]城墙上那场大火之后，那些维多利亚人的军队推进得很迅猛，食腐者的阵线溃散得也很快......
[charslot(slot="m",name="avg_4088_hodrer_1#6$1",focus="m")]
[name="赫德雷"]食腐者之王呢？
[charslot(slot="m",name="avg_1035_wisdel_1#10$1",focus="m")]
[name="维什戴尔"]没死，但退守到城内了——
[charslot(slot="m",name="avg_4071_peper_1#9$1",focus="m")]
[name="明椒"]......维什戴尔小姐，还、还有将军他的消息吗？
[charslot(slot="m",name="avg_1035_wisdel_1#11$1",focus="m")]
[name="维什戴尔"]没有，说不定死了哦。
[charslot(slot="m",name="avg_4071_peper_1#9$1",focus="m")]
[name="明椒"]......
[charslot(slot="m",name="avg_4088_hodrer_1#2$1",focus="m")]
[name="赫德雷"]曼弗雷德没那么容易死。
[charslot(slot="m",name="avg_1035_wisdel_1#10$1",focus="m")]
[name="维什戴尔"]但外面的混乱也明显有问题。
[name="维什戴尔"]从我手底下的人收集的情报来看，孽茨雷那老家伙自己的阵地丝毫不乱，即使这场仗军事委员会显然已经输定了。
[name="维什戴尔"]哪怕我恨不得把特雷西斯炸成渣，我也没法否认......
[name="维什戴尔"]以他的能耐和算计，军事委员会没道理会这么快就到了要完全败亡的程度。
[name="维什戴尔"]你的计划必须要提前了，赫德雷。
[charslot(slot="m",name="avg_4088_hodrer_1#1$1",focus="m")]
[name="赫德雷"]“生命脊椎”已经准备好了。
[charslot(slot="m",name="avg_4088_hodrer_1#8$1",focus="m")]
[name="赫德雷"]不管摄政王的计划是什么，我们都得准备带着那些被卷进来的人离开......在对萨卡兹的清洗开始之前。
[charslot(slot="m",name="avg_4087_ines_1#8$1",focus="m")]
[name="伊内丝"]维多利亚人恐怕不会这么轻易放他们离开。
[charslot(slot="m",name="avg_4088_hodrer_1#2$1",focus="m")]
[name="赫德雷"]我知道，但......
[charslot(slot="m",name="avg_1035_wisdel_1#13$1",focus="m")]
[name="维什戴尔"]嘁，什么时候我们办事还要听维多利亚人的想法了？
[name="维什戴尔"]我有个好点子。
[charslot(slot="m",name="avg_1035_wisdel_1#1$1",focus="m")]
[name="维什戴尔"]但那得先拿下军事委员会的指挥中心，嗯，以“巴别塔”的名义。
[name="维什戴尔"]你们就乖乖在这等着我的命令——
[charslot(slot="m",name="avg_4087_ines_1#1$1",focus="m")]
[name="伊内丝"]点子不是计划，W。不过看起来你已经很有把握了。
[name="伊内丝"]走吧，我已经受够待在地下了。
[charslot(slot="m",name="avg_1035_wisdel_1#12$1",focus="m")]
[name="维什戴尔"]呃，赫德雷需要人照顾。
[charslot(slot="m",name="avg_4087_ines_1#1$1",focus="m")]
[name="伊内丝"]他死不了，他自己说的。
[charslot(slot="m",name="avg_4088_hodrer_1#1$1",focus="m")]
[name="赫德雷"]......对。
[charslot(slot="m",name="avg_4088_hodrer_1#7$1",focus="m")]
[name="赫德雷"]不管摄政王和食腐者在圣王会西部大堂谋算什么，剩下人的死活必然不是他们最在乎的问题了。
[name="赫德雷"]我们不能坐视不管。至于你的点子，可以慢慢说给我们听。
[charslot(slot="m",name="avg_1035_wisdel_1#1$1",focus="m")]
[name="维什戴尔"]啧，两个蠢货。
[name="维什戴尔"]你呢，毛线球？
[charslot(slot="m",name="avg_4071_peper_1#11$1",focus="m")]
[name="明椒"]我和你们一起！将军可能也在指挥中心，我还有很多问题想问他！
[charslot(s

... (全文59273字符)
```

### level_act18mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="43_g1_giantmonstercockpit",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>“生命脊椎”</><p=2>1098年10月，萨卡兹大撤军</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="r",name="avg_4087_ines_1#1$1",duration=1.5)]
[charslot(slot="l",name="avg_4088_hodrer_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="r",name="avg_4087_ines_1#1$1",focus="r")]
[name="伊内丝"]赫德雷，接受使用骸骨撤退的我都带上来了。
[charslot(slot="r",name="avg_4087_ines_1#2$1",focus="r")]
[name="伊内丝"]大多都是没法坚持住长途行军的家伙。年长的，年纪小的，还有很多伤员，几乎都在了。
[charslot(slot="r",name="avg_4087_ines_1#8$1",focus="r")]
[name="伊内丝"]W放话“随便他们要不要送死”的伤员也被她小队里其他人抬上来了。
[name="伊内丝"]她活着的手下竟然还不少，够在“生命脊椎”内部维护秩序，也够盯着被关押的厄尔苏拉。
[name="伊内丝"]所以不必担心你在路上突然死了，没人能接手驾驶员的位置。
[charslot(slot="l",name="avg_4088_hodrer_1#1$1",focus="l")]
[name="赫德雷"]......好。
[charslot(slot="r",name="avg_4087_ines_1#1$1",focus="r")]
[name="伊内丝"]你在等什么？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="55_i01_1", screenadapt="coverall", xScale=1.1, yScale=1.1, fadetime=0)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=30, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
“生命脊椎”在战场的废墟上投下一片阴影。
没有萨卡兹抬头，他们或许知道，或许已经习惯，将有一片更大的阴影笼罩这支绵延数里的队伍。
为了翻越高速军舰留下的沟壑，大多数人步履缓慢。
[Dialog]
[charslot(slot="r",name="avg_4087_ines_1#1$1",focus="all")]
[charslot(slot="l",name="avg_4088_hodrer_1#6$1",focus="all")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_4088_hodrer_1#6$1",focus="l")]
[name="赫德雷"]我只是在想......撤军的队伍竟然那么长。
[name="赫德雷"]卡兹戴尔和维多利亚之间的路，我们都走过，都知道要走多久。
[charslot(slot="r",name="avg_4087_ines_1#2$1",focus="r")]
[name="伊内丝"]可要是维多利亚人现在出尔反尔，对着萨卡兹的队伍开炮，你也做不了什么。
[charslot(slot="l",name="avg_4088_hodrer_1#2$1",focus="l")]
[name="赫德雷"]是啊，事情一向如此。
[charslot(slot="l",name="avg_4088_hodrer_1#1$1",focus="l")]
[name="赫德雷"]哪怕不是现在......等我们向全泰拉发出信号的时候，各国必定有所反应。
[charslot(slot="r",name="avg_4087_ines_1#13$1",focus="r")]
[name="伊内丝"]你确定那个办法能奏效吗？
[name="伊内丝"]如此张扬地撤退回卡兹戴尔，恐怕会令很多国家产生恐慌。
[charslot(slot="l",name="avg_4088_hodrer_1#2$1",focus="l")]
[name="赫德雷"]但的确没有更好的办法了。
[charslot(slot="l",name="avg_4088_hodrer_1#1$1",focus="l")]
[name="赫德雷"]这支队伍必须继续向所有势力展现出最强势的一面。一旦失去挥动武器的力气，这些人立马就会被吃得骨头都不剩。
[name="赫德雷"]那位新的“魔王”也一样。
[name="赫德雷"]主动权必须握在我们自己的手里。
[Dialog]
[charslot]
透过骸骨看向外面，飞空艇若隐若现，舰炮的索敌状态也一直没有解除。
而在它的周围，是一片随着撤军队伍移动的巨大天灾云。
[charslot(slot="m",name="avg_4087_ines_1#8$1",focus="m")]
[name="伊内丝"]但还有另一件事，我非常担心。
[charslot(slot="m",name="avg_4087_ines_1#1$1",focus="m")]
[name="伊内丝"]你确定让W看守曼弗雷德是个好主意？
[charslot(slot="m",name="avg_4088_hodrer_1#1$1",focus="m")]
[name="赫德雷"]她的确是最合适的人选。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="29_g2_edgeofbase",screenadapt="showall")]
[Delay(time=2)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_901_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="哥伦比亚军官"]队伍已抵达指定地点。
[name="哥伦比亚军官"]天气晴朗，能见度良好。
[Dialog]
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="none")]
[PlaySound(key="$d_gen_transmissionget",volume=1)]
[delay(time=0.5)]
[name="通讯那头的声音"]持续瞭望东南方向。
[name="通讯那头的声音"]我们已经收到了国防部同步给我们的最新情报，其中还包括了卡兹戴尔的大概坐标。
[name="通讯那头的声音"]请持续关注萨卡兹军队在撤军返乡的旗号掩护下有何实际动作。
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="m")]
[name="哥伦比亚军官"]明白。
[Dialog]
[charslot]
事实上，军官并不明白关注萨卡兹有什么意义。
但出于对合作伙伴的尊重，他坐在侦察车里，聚精会神地盯着无人机传回的数据。
风平浪静。
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="m")]
[name="哥伦比亚军官"]目前没有异常状况，先生。所以，只是随便聊聊......梅兰德很少派您这样身份的代表出面与军方联系。
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="none")]
[name="通讯那头的声音"]呵呵，维多利亚人自以为将伦蒂尼姆的灾难掩饰得很好。
[name="通讯那头的声音"]梅兰德需要调查一些情况，然后跟他们谈谈。
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="m")]
[name="哥伦比亚军官"]明白。
[Dialog]
[PlaySound(key="$d_avg_oldtvelectricity",volume=1)]
[delay(time=3.5)]
[bgeffect]
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="none")]
[name="通讯那头的声音"]......少尉，少尉！
[name="通讯那头的声音"]及时报告情况！
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="m")]
[name="哥伦比亚军官"]是，目前没有新情况......
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="none")]
[name="通讯那头的声音"]什么都没有？！
[charslot(slot="m",name="avg_npc_901_1#1$1",focus="m")]
[name="哥伦比亚军官"]呃，那是......？
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_warning",volume=1)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=2, block=true)]
军官放下了通讯器。车载天灾预警系统正在发出尖锐的警报声。
他望向特区的方向，这个距离下他几乎看不见移动城市的轮廓。
但他看到天灾云投下了一片庞大的阴影，从特区的上空一直蔓延到自己的头顶。
[Dialog]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="44_g6_towerterrace",screenadapt="showall")]
[Delay(time=2)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_498_1#1$1",focus="m")]
[name="恭敬的侍者"]是的，他知道您与叙拉古的那些人相熟，所以希望您这一次有机会施展才能。
[charslot(slot="m",name="avg_npc_493_1#1$1",focus="m")]
[name="莱塔尼亚贵族"]请放心。数量庞大的萨卡兹是灾祸，是无序的军事力量......但也是佣兵。
[name="莱塔尼亚贵族"]现在我们已经知道，我们的邻居维多利亚没能看管好他们。
[name="莱塔尼亚贵族"]但我有信心，不让那些污秽干扰莱塔尼亚的辉煌乐章。
[name="莱塔尼亚贵族"]请您如此传话给您的主人——
[Dialog]
[charslot]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=2, block=true)]


... (全文31044字符)
```


## 统计

- 总字符数：222464
- 对话行数：1725


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
