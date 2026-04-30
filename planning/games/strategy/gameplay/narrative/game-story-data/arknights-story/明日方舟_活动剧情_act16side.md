# 明日方舟 · 活动剧情 · act16side（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act16side」完整剧情脚本（23个文件，2845行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act16side
- 脚本文件数：23

### level_act16side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g3_laterano_cathedralballroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#2$1",fadetime=1,block=true)]
[delay(time=1)]
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#2$1",focus=2)]
[name="休露丝"]尤卡坦......你不觉得，拉特兰的饮食有点问题吗......？
[character(name="avg_npc_263_1#7$1",name2="avg_npc_262_1#2$1",focus=1)]
[name="尤卡坦"]相比谢拉格，这里的口味确实有些偏甜了。
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#2$1",focus=1)]
[name="尤卡坦"]但是，露丝你不是喜欢甜食吗？
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#8$1",focus=2)]
[name="休露丝"]那也不能所有的食物都是甜的吧！
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#9$1",focus=2)]
[name="休露丝"]唉，我开始怀念谢拉格了。
[name="休露丝"]都怪菈塔托丝那个臭女人，说什么要抓住一切机会重新提高家族的地位......结果她自己又不来，把我丢到这么远的地方。
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#9$1",focus=1)]
[name="尤卡坦"]这也是大夫人愿意信任你的表现吧。毕竟在那件事之后的绝境里，是靠着你和大夫人的共同努力，才确保了如今布朗陶家的地位。
[character(name="avg_npc_263_1#1$1",name2="avg_npc_262_1#10$1",focus=2)]
[name="休露丝"]又把自己撇出去，尤卡坦，你该不会其实很享受隐居幕后的感觉吧？
[character(name="avg_npc_263_1#8$1",name2="avg_npc_262_1#10$1",focus=1)]
[name="尤卡坦"]对我来说，能看到露丝散发光芒就已经很满足了。
[character(name="avg_npc_263_1#8$1",name2="avg_npc_262_1#4$1",focus=2)]
[name="休露丝"]......唔唔，你什么时候学得这么油嘴滑舌了！
[character(name="avg_npc_263_1#8$1",name2="avg_npc_262_1#4$1",focus=1)]
[name="尤卡坦"]但是，夫人，这场会议或许确实比我们预想的更加有价值。
[name="尤卡坦"]来之前，我们甚至以为不会有多少国家回应邀请。现在看来，可能还是低估了拉特兰的影响力。
[character(name="avg_npc_263_1#8$1",name2="avg_npc_262_1#3$1",focus=2)]
[name="休露丝"]虽然你说得有道理......但是别想转移话题！
[dialog]
[character(name="avg_npc_262_1#3$1",name2="avg_npc_175")]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-80, fadetime=1,block=false)]
[delay(time=1)]
[characteraction(name="right", type="move", xpos=-100, fadetime=0.3,block=false)]
[PlaySound(key="$bodyfalldown1",volume=0.4)] 
[stopmusic(fadetime=1)]
[characteraction(name="right", type="move", xpos=50, fadetime=0.5,block=false)]
[characteraction(name="left", type="move", xpos=-50, fadetime=0.5,block=false)]
[CameraShake(duration=0.9, ystrength=20, vibrato=30, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2",volume=0.8)] 
[Delay(time=1.3)]
[Dialog]
[Character]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[character(name="avg_npc_175")]
[name="刻薄的莱塔尼亚人"]（莱塔尼亚语）哎呀，你长没长眼睛！
[character(name="avg_npc_262_1#4$1",name2="avg_npc_175",focus=1)]
[name="休露丝"]（莱塔尼亚语）是你撞上我的吧。
[character(name="avg_npc_262_1#4$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]多么蹩脚的莱塔尼亚语，哪里来的乡下人？
[character(name="avg_npc_262_1#7$1",name2="avg_npc_175",focus=1)]
[name="休露丝"]我来自谢拉格，谢拉格可不是什么乡下。
[character(name="avg_npc_262_1#7$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]谢拉格？
[name="刻薄的莱塔尼亚人"]谢拉格是什么地方？
[character(name="avg_npc_175",name2="avg_npc_360_1#1$1",focus=2)]
[name="开朗的万国信使"]莎伦夫人，谢拉格是位于维多利亚、哥伦比亚、卡西米尔缓冲地带的雪域国家。
[character(name="avg_npc_175")]
[name="刻薄的莱塔尼亚人"]那片雪山中还有国家？哈，那不就是乡下吗！
[name="刻薄的莱塔尼亚人"]区区边鄙小国的使者，也敢在本公爵夫人面前嘴硬？
[character(name="avg_npc_262_1#7$1",name2="avg_npc_175",focus=1)]
[name="休露丝"]......这位夫人，第一，我要再次强调，谢拉格并非你口中的“乡下”。您不了解这个国家，可能是出于您的孤陋寡闻。
[name="休露丝"]第二，撞上我的人是您，请您向我道歉。
[character(name="avg_npc_262_1#7$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]你......！
[character(name="avg_npc_175",name2="avg_npc_360_1#1$1",focus=2)]
[name="开朗的万国信使"]莎伦夫人，这里是大教堂......
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_355_1#9$1",fadetime=1,block=true)]
[delay(time=1)]
[name="奥伦"]莎伦夫人，请容我提醒，您现在身在拉特兰，而不是在您的莱塔尼亚领地。
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]你又是谁？
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=1)]
[name="奥伦"]拉特兰的万国信使。
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]万国信使，你是什么意思？说什么这里是大教堂，怎么，身为东道主，你想说拉特兰会站在那个乡下人一边吗？
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=1)]
[name="奥伦"]拉特兰站在规则一边。所以，莎伦夫人，您应该向休露丝夫人道歉。
[character(name="avg_npc_262_1#4$1",name2="avg_npc_355_1#9$1",focus=1)]
[name="休露丝"]你知道我的名字？
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]知道各国来使的名字是理所当然的事，不是吗？
[character(name="avg_npc_355_1#1$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]哦？这么说，你很清楚我是谁。
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=1)]
[name="奥伦"]当然，莱塔尼亚的弗朗西斯公爵夫人。
[name="奥伦"]但请容许我再次提醒您，这里是拉特兰，夫人。
[name="奥伦"]在拉特兰，请尊重戒律与规则。无论您在莱塔尼亚享有怎样的特权，在拉特兰，它们并不存在。
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=2)]
[name="刻薄的莱塔尼亚人"]这就是拉特兰的待客之道？
[character(name="avg_npc_355_1#9$1",name2="avg_npc_175",focus=1)]
[name="奥伦"]如果您愿意做“拉特兰的客人”，拉特兰自然会竭诚以待。
[Dialog]
[Character]
[Delay(time=0.51)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_361_1#1$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_361_1#3$1")]
[name="薇尔丽芙"]——奥伦，你什么时候开始代表拉特兰了？
[character(name="avg_npc_355_1#3$1",name2="avg_npc_361_1#3$1",focus=1)]
[name="奥伦"]作为拉特兰的使者，我没有这个资格吗？
[character(name="avg_npc_355_1#3$1",name2="avg_npc_361_1#1$1",focus=2)]
[name="薇尔丽芙"]在大教堂，你没有。
[character(name="avg_npc_361_1#5$1")]
[name="薇尔丽芙"]莎伦夫人，请息怒。
[character(name="avg_npc_175")]
[name="刻薄的莱塔尼亚人"]哼，枢机，现在想息事宁人，是不是有些晚了？
[character(name="avg_npc_361_1#5$1")]
[name="薇尔丽芙"]公爵夫人，我真诚地请求您的谅解。顶撞您的万国信使会受到相应的处罚。晚些时候，您可以在下榻的宾馆亲眼确认教皇厅的诚意。
[name="薇尔丽芙"]休露丝夫人，也请求您的原谅，这一小小误会是我们工作不周所致。如果您愿意宽宏地接受我的歉意，我希望能邀请您稍后往偏厅一叙。
[Dialog]
[character(name="avg_npc_262_1#7$1",name2="avg_npc_263_1#1$1")]
[Delay(time=0.51)]
休露丝看向尤卡坦，尤卡坦轻微地点了点头。
[Dialog]
[Character]
[character(name="avg_npc_175")]
[name="刻薄的莱塔尼亚人"]呵，拉特兰人。罢了。
[character(name="avg_npc_361_1#6$1")]
[name="薇尔丽芙"]阿莱索，玛蒂娜，请替我招待好三位贵宾。
[character(name="avg_npc_355_1#3$1",name2="avg_npc_361_1#1$1",focus=2)]
[name="薇尔丽芙"]奥伦，随我来。
[character(name="avg_npc_355_1#10$1",name2="avg_npc_361_1#1$

... (全文16044字符)
```

### level_act16side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g7_laterano_ward",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[character(name="avg_300_phenxi_1#9$1")]
[name="菲亚梅塔"]所以你现在已经可以离开轮椅行动了吗？
[character(name="avg_npc_353_1#9$2")]
[name="蕾缪安"]嗯，复健得还不错。
[name="蕾缪安"]去年这里办了个轮椅竞速射击赛，我拿了冠军哦......然后就被医生禁赛了。
[character(name="avg_300_phenxi_1#10$1")]
[name="菲亚梅塔"]要说能在射击技巧上比过你的人，恐怕要去铳骑里才能找到了。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]哎呀，这话我爱听。
[name="蕾缪安"]要是某个人也能学学可爱的菲亚梅塔，对我这个病人说几句好听的话，我就更开心了。
[character(name="avg_300_phenxi_1#9$1")]
[name="菲亚梅塔"]莫斯提马，你又打算站在那里装窗帘吗？
[character(name="avg_213_mostma_1#2$1")]
[name="莫斯提马"]你知道我不是那样的性格，蕾缪安。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]什么样的性格？你两三年才回来一次，我记性不太好呢。
[character(name="avg_213_mostma_1#11$1")]
[name="莫斯提马"]好吧，蕾缪安的射击技巧，是我所知道的人里最出色的。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]嗯嗯，这就对了。
[character(name="avg_npc_353_1#6$2")]
[name="蕾缪安"]小乐在龙门过得好吗？
[character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"]前段时间见过她一次，她过得很好。
[name="莫斯提马"]与其替她操心，不如替你自己操心比较好。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]这句话呢，我也原封不动地还给你。
[character(name="avg_npc_353_1#4$2")]
[name="蕾缪安"]你们这次回来会待多久？
[character(name="avg_213_mostma_1#9$1")]
[name="莫斯提马"]不知道欸。不过，至少会待到会议结束，我记得是下下周三？
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]周二。
[character(name="avg_213_mostma_1#7$1")]
[name="莫斯提马"]哦，周二。其他就看那个老家伙的心情吧，谁知道会不会又给我派奇奇怪怪的任务。
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]你是不是把教宗阁下叫成了......
[character(name="avg_213_mostma_1#5$1")]
[name="莫斯提马"]他本人都不会介意啦，菲亚梅塔。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]你们要是想多留一阵子，我也可以帮忙。
[character(name="avg_213_mostma_1#7$1")]
[name="莫斯提马"]是嘛。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]你已经猜到了吧？
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]什么意思？你们在说什么？
[character(name="avg_213_mostma_1#7$1")]
[name="莫斯提马"]你真的没发现吗，菲亚梅塔？
[character(name="avg_213_mostma_1#5$1")]
[name="莫斯提马"]最近半年，我和你的报告交到了谁手里。
[character(name="avg_npc_353_1#4$2")]
[name="蕾缪安"]有那么明显吗？
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]什、什么？......所以，蕾缪安你......开始在教皇厅工作了？可是你还在复健......？
[character(name="avg_npc_353_1#9$2")]
[name="蕾缪安"]别担心，菲亚梅塔，只是一些文书工作而已。
[character(name="avg_213_mostma_1#1$1")]
[name="莫斯提马"]你会顺着这条路走下去吗？
[character(name="avg_npc_353_1#8$2")]
[name="蕾缪安"]还不知道。
[character(name="avg_300_phenxi_1#4$1")]
[name="菲亚梅塔"]你还会回戍卫队吗？
[character(name="avg_npc_353_1#2$2")]
[name="蕾缪安"]那大概是回不去了。
[character(name="avg_300_phenxi_1#5$1")]
[name="菲亚梅塔"]......你的射击技术，就这样埋没......太浪费了。
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]菲亚梅塔对我的评价真高啊，明明那时我搞砸了呢。
[character(name="avg_300_phenxi_1#5$1")]
[name="菲亚梅塔"]......
[name="菲亚梅塔"]那不是你的责任，蕾缪安。
[character(name="avg_npc_353_1#6$2")]
[name="蕾缪安"]那也不是你的责任啊，菲亚梅塔。
[character(name="avg_npc_353_1#9$2")]
[name="蕾缪安"]别把自己绷得太紧。
[character(name="avg_300_phenxi_1#6$1")]
[name="菲亚梅塔"]......总有一天，我要找他算清这笔账。
[character(name="avg_npc_353_1#8$2")]
[name="蕾缪安"]......哎，莫斯提马......
[character(name="avg_npc_353_1#10$2")]
[name="蕾缪安"]我能不能摸一摸你的角？
[character(name="avg_213_mostma_1#5$1")]
[name="莫斯提马"]不能。
[character(name="avg_npc_353_1#5$2")]
[name="蕾缪安"]小器。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background]
[Image(image="26_i03", fadetime=2,xScale=1, yScale=1,x=150, y=-80)]
[ImageTween(xScaleTo=0.8, yScaleTo=0.8, duration=40,xTo=0, yTo=0,block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
蕾缪安望向窗外，莫斯提马靠在窗边，玩弄手中的花朵。
菲亚梅塔恍然回到当年。
拉特兰的早春，阳光总是明媚，空气中带着一丝寒意。
透过窗户，望见远处大小教堂的屋顶。偶有羽兽划过天际。
蕾缪安平时很安静，偶尔说出一两句话，空气都变得柔和。
装酷的莫斯提马不自觉地放松，露出自己未能察觉的笑容。
......
一如既往。
仿佛一切未曾发生。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
然而这只是错觉。
她为此夜不能寐。
[dialog]
[Character]
[Image]
[delay(time=2)]
[Background(image="26_g7_laterano_ward",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[character(name="avg_300_phenxi_1#5$1")]
[name="菲亚梅塔"]蕾缪安......
[character(name="avg_213_mostma_1#1$1")]
[name="莫斯提马"]我在思考一件事情，蕾缪安。
[character(name="avg_213_mostma_1#9$1")]
[name="莫斯提马"]这家医院的志愿者很多吗？
[character(name="avg_npc_353_1#1$2")]
[name="蕾缪安"]嗯？一般吧。
[Dialog]
[Character]
[playsound(key="$doorknockquite")]
[Delay(time=1)]
[character(name="avg_npc_353_1#1$2")]
[name="蕾缪安"]请进。
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_366_1#1$1",fadetime=1.5)]
[delay(time=2)]
[name="认真的医生"]蕾缪安小姐，我想给你看一份......
[name="认真的医生"]啊，有客人在吗？
[character(name="avg_npc_353_1#9$2")]
[name="蕾缪安"]没关系，她们都是我过去的战友。
[character(name="avg_npc_366_1#1$1")]
[name="认真的医生"]战友......难道说！
[character(name="avg_npc_353_1#9$2")]
[name="蕾缪安"]是的。
[character(name="avg_npc_366_1#1$1")]
[name="认真的医生"]既然如此，或许三位都可以看一看这份检查结果......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_361_1#1$1",name2="avg_npc_355_1#1$1",focus=1)]
[name="薇尔丽芙"]奥伦，你知道自己在做什么吗？
[character(name="avg_npc_361_1#1$1",name2="avg_npc_355_1#4$1",focus=2)]
[name="奥伦"]也许可以请你告诉我？
[character(name="avg_npc_361_1#3$1",name2="avg_npc_355_1#4$1",focus=1)]
[name="薇尔丽芙"]她不会认为你的做法是“个人行为”。
[character(name="avg_npc_361_1#3$1",name2="avg_npc_355_1#1$1",focus=2)]
[name="奥伦"]她会认为我们是在刻意展现“拉特兰的姿态”。
[character(name="avg_npc_361_1#3$1",name2="avg_npc_355_1#1$1",focus=1)]
[name="薇尔丽芙"]一不小心，这就会演变成外交问题。
[character(name="avg_npc_361_1#3$1",name2="avg_npc_355_1#4$1",focus=2)]
[name="奥伦"]这难道不正是你期待的事情？
[character(name="avg_npc_361_1#3$1",name2="avg_npc_355_1#8$1",foc

... (全文18620字符)
```

### level_act16side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g10_laterano_roof",screenadapt="coverall")]
[character(name="char_empty",name2="avg_300_phenxi_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[playsound(key="$d_gen_transmissionget")]
[CharacterCutin(widgetID="1", name="avg_213_mostma_1#10$2", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[character(name="char_empty",name2="avg_300_phenxi_1#1$1",focus=1)]
[name="莫斯提马"]所以你就走了？
[character(name="char_empty",name2="avg_300_phenxi_1#1$1",focus=2)]
[name="菲亚梅塔"]和她纠缠没有意义，我甚至怀疑她就是来拖住我的。如果那个女孩已经不在医院，首先要确认的是女孩的去向。
[name="菲亚梅塔"]你那边呢？
[character(name="char_empty",name2="avg_300_phenxi_1#1$1",focus=1)]
[name="莫斯提马"]我走了近道。马上到大教堂。
[character(name="char_empty",name2="avg_300_phenxi_1#1$1",focus=2)]
[name="菲亚梅塔"]如果情况允许，帮我从教皇厅给公证所下配合令。
[name="菲亚梅塔"]我问过医院的人，送那个女孩来医院的是一个见习执行者，说是捡到了走失儿童，找不到父母。
[name="菲亚梅塔"]按流程，他应该把女孩带回公证所。
[name="菲亚梅塔"]即使他不回公证所，我也可以从公证所系统查到他的定位。
[character(name="char_empty",name2="avg_300_phenxi_1#1$1",focus=1)]
[name="莫斯提马"]总觉得菲亚梅塔太厉害了对我不是什么好事......
[character(name="char_empty",name2="avg_300_phenxi_1#8$1",focus=2)]
[name="菲亚梅塔"]对了，你报告之后，先别离开大教堂。
[character(name="char_empty",name2="avg_300_phenxi_1#8$1",focus=1)]
[name="莫斯提马"]嗯？你那边不需要我帮忙吗？
[character(name="char_empty",name2="avg_300_phenxi_1#7$1",focus=2)]
[name="菲亚梅塔"]......不。我觉得，有事情要发生了。
[character(name="char_empty",name2="avg_300_phenxi_1#7$1",focus=1)]
[name="莫斯提马"]不是已经发生了？
[character(name="char_empty",name2="avg_300_phenxi_1#6$1",focus=2)]
[name="菲亚梅塔"]你知道我说的是谁。
[character(name="char_empty",name2="avg_300_phenxi_1#6$1",focus=2)]
[name="菲亚梅塔"]总之，你留在大教堂，说不定对我更有用。
[character(name="char_empty",name2="avg_300_phenxi_1#6$1",focus=1)]
[name="莫斯提马"]你在担心我？
[character(name="char_empty",name2="avg_300_phenxi_1#7$1",focus=2)]
[name="菲亚梅塔"]我只是希望你不要到处乱跑，方便我......以逸待劳！
[character(name="char_empty",name2="avg_300_phenxi_1#7$1",focus=1)]
[name="莫斯提马"]没问题，微光守夜人。
[character(name="char_empty",name2="avg_300_phenxi_1#2$1",focus=2)]
[CameraShake(duration=0.6, xstrength=10, ystrength=30, vibrato=20, randomness=10, fadeout=true, block=false)]
[name="菲亚梅塔"]......给我叫本名！！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g9_laterano_street",screenadapt="showall")]
[CharacterCutin(widgetID="1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$rungeneral")]
[Delay(time=2)]	
[playsound(key="$d_avg_crwddiscuss_outside",channel="bgs",fadetime=1)]
[delay(time=1)]
[StopSound(channel="bgs", fadetime=3)]
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]呼......
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=2)]
[name="塞茜莉亚"]这里，好多人......
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]所以我们不容易被发现。
[name="艾泽尔"]这里是安布罗修区，来过这儿吗，塞茜莉亚？
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=2)]
[name="塞茜莉亚"]......妈妈以前说，她会去安布罗修区买东西。她会在这里吗？
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]你刚才说，妈妈被人带走了，是怎么一回事？
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=2)]
[name="塞茜莉亚"]妈妈生病了......早上，我在陪妈妈说话。然后有人来......公证所的人，穿着白衣服。
[name="塞茜莉亚"]他走之后，穿着袍子的人进来，带走了妈妈。
[character(name="avg_4036_forcer_1#7$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]（公证所......这真的会是绑架事件吗......感觉不太对劲。）
[name="艾泽尔"]你当时在哪里，塞茜莉亚？他们看见你了吗？你爸爸去哪儿了？
[character(name="avg_4036_forcer_1#7$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]......这些和妈妈在哪里有关系吗？
[character(name="avg_4036_forcer_1#9$1",name2="avg_npc_352_1#9$1",focus=1)]
[name="艾泽尔"]呃，不一定有......只是，如果你多告诉我一些事情，也许我能发现什么线索。
[character(name="avg_4036_forcer_1#9$1",name2="avg_npc_352_1#2$1",focus=2)]
[name="塞茜莉亚"]......
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="病重的母亲"]塞茜莉亚，我的塞茜莉亚，躲起来，不要被发现......
......
[name="艾泽尔"]......那么，请告诉我她的父母姓名、家庭住址、身份识别码，以及你和她的血缘或法理关系。
[name="艾泽尔"]如果你有带走塞茜莉亚的正当理由，可以告诉我，我会酌情判断。
[dialog]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_npc_352_1#9$1")]
[delay(time=1.5)]
[character(name="avg_npc_352_1#2$1")]
[delay(time=1.5)]
[character(name="avg_npc_352_1#1$1")]
[delay(time=0.51)]
[name="塞茜莉亚"]艾泽......
[dialog]
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]稍等，塞茜莉亚。
[dialog]
[playsound(key="$d_gen_transmissionget")]
[delay(time=1)]
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]喂，是我。
[name="艾泽尔"]是的，我现在在安布罗修区。
[name="艾泽尔"]嗯，我在帮这个孩子寻找母亲。
[name="艾泽尔"]回公证所？嗯，我正打算过来......大概半小时？
[name="艾泽尔"]好的，明白。
[dialog]
[character]
[playsound(key="$transmission")]
[delay(time=1.5)]
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#12$1",focus=2)]
[name="塞茜莉亚"]艾泽尔......哥哥，你要带我去公证所吗？
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]嗯，有什么问......
[dialog]
[character]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[name="帕蒂亚"]给你一句忠告！如果你真的关心塞茜莉亚，就不要把她交给公证所或者教皇厅！不然，你会后悔的！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_4036_forcer_1#7$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]......塞茜莉亚，你是不是不想去公证所？
[character(name="avg_4036_forcer_1#7$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]......妈妈说，不可以去......
[character(name="avg_4036_forcer_1#7$1",name2="avg_npc_352_1#4$1",focus=2)]
[name="塞茜莉亚"]不过！如果能知道妈妈在哪儿，我愿意......我可以去！
[name="塞茜莉亚"]妈妈在生病......我很担心......
[character(name="avg_4036_forcer_1#7$1",name2="avg_npc_352_1#4$1",focus=1)]
[name="艾泽尔"]......塞茜莉亚，再问你一个问题，刚才的黎博利，你见过她吗？
[character(name="avg_4036_f

... (全文25533字符)
```

### level_act16side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g11_laterano_alley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Character(name="avg_4036_forcer_1#8$1",name2="avg_npc_352_1#1$1",focus=1)]
[name="艾泽尔"]快到了......塞茜莉亚，认得出附近的路了吗？
[Character(name="avg_4036_forcer_1#8$1",name2="avg_npc_352_1#12$1",focus=2)]
[name="塞茜莉亚"]嗯......这些房子我见过......可是，一样的房子好多......
[Character(name="avg_4036_forcer_1#8$1",name2="avg_npc_352_1#12$1",focus=1)]
[name="艾泽尔"]塞茜莉亚，你是刚搬到这附近吗？
[Character(name="avg_4036_forcer_1#8$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]搬家？我不记得搬过家......
[Character(name="avg_4036_forcer_1#3$1",name2="avg_npc_352_1#9$1",focus=1)]
[name="艾泽尔"]哎？
[Character(name="avg_4036_forcer_1#3$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]对不起，艾泽尔哥哥，妈妈带我出门都是晚上，街上不太一样......
[Character(name="avg_4036_forcer_1#3$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]不过平时，我会偷偷从窗户看家外面的样子......我能认出来的！我会努力的......
[Character(name="avg_4036_forcer_1#5$1",name2="avg_npc_352_1#10$1",focus=1)]
[name="艾泽尔"]......
[Character(name="avg_4036_forcer_1#8$1",name2="avg_npc_352_1#10$1",focus=1)]
[name="艾泽尔"]没关系，塞茜莉亚，会找到的，还没到遇见你的地方呢。
[dialog]
[Character(name="avg_npc_352_1#10$1",name2="avg_npc_367_1#1$1")]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=100, fadetime=0.3,block=false)]
[PlaySound(key="$bodyfalldown1",volume=0.4)] 
[characteraction(name="left", type="move", xpos=-50, fadetime=0.5,block=false)]
[characteraction(name="right", type="move", xpos=50, fadetime=0.5,block=false)]
[CameraShake(duration=0.9, ystrength=20, vibrato=30, randomness=50, fadeout=true, block=false)]
[Delay(time=1)]
[Character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]呀！
[Character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]对不起......我在看两边的房子，没有看到您。
[Character(name="avg_npc_367_1#1$1")]
[name="热心的拉特兰市民"]嗯？你不是早上昏倒被送医院的小姑娘吗？没事了吗？
[Character(name="avg_4036_forcer_1#3$1",name2="avg_npc_367_1#1$1",focus=1)]
[name="艾泽尔"]是您啊！嗯，她......她没事。
[name="艾泽尔"]对了，之后有大人来找她吗？
[Character(name="avg_4036_forcer_1#3$1",name2="avg_npc_367_1#1$1",focus=2)]
[name="热心的拉特兰市民"]我一直盯到中午呢！就是没人出现，真奇怪，父母在干什么呢......
[Character(name="avg_4036_forcer_1#1$1",name2="avg_npc_367_1#1$1",focus=1)]
[name="艾泽尔"]塞茜莉亚说，她就住在这附近，您真的没见过她吗？
[Character(name="avg_4036_forcer_1#1$1",name2="avg_npc_367_1#1$1",focus=2)]
[name="热心的拉特兰市民"]这么可爱的小姑娘，要是见过，肯定会有印象啦！我也不用在旁边干着急了不是。
[name="热心的拉特兰市民"]这样吧，之前那个人说得有道理，我带你们去找社区办事处的人吧。如果是刚搬来的住户，在办事处肯定有登记的。
[dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_367_1#1$1")]
[name="热心的拉特兰市民"]嚯，巧了，那不是葆菈姐吗！
[name="热心的拉特兰市民"]葆菈姐！这边这边！
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]嗯，怎么了？我赶着回办公室呢，边走边说吧。
[Character(name="avg_npc_367_1#1$1")]
[name="热心的拉特兰市民"]咱们这片最近有新搬来的住户吗？
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]有当然是有......不过你说的最近是多近啊？
[Character(name="avg_npc_367_1#1$1")]
[name="热心的拉特兰市民"]小姑娘，你大概什么时候搬过来的？
[Character(name="avg_npc_352_1#9$1")]
[name="塞茜莉亚"]......不是刚搬过来的......住在这里很久了......
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]哎？小姑娘，你叫什么名字？
[Character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]我是塞茜莉亚......
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]嗯......没道理呀，我在这里工作十多年了，你要是住了很久......
[name="知性的拉特兰市民"]塞茜莉亚，你知道你的爸爸妈妈叫什么名字吗？
[Character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]妈妈的名字是......费莉亚。
[stopmusic(fadetime=3)]
[Character(name="avg_4036_forcer_1#2$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="艾泽尔"]！！！！！
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]什么什么什么？！费莉亚，是瑟法斯街的费莉亚吗？费莉亚不是单身吗？怎么突然冒出个这么大的孩子？
[name="知性的拉特兰市民"]不过仔细看看......你确实和费莉亚长得很像呢。
[name="知性的拉特兰市民"]太奇怪了......难道是私生子？塞茜莉亚，你刚才说住了很久，是说你妈妈住在这里很久的意思吗？
[Character(name="avg_npc_352_1#9$1")]
[name="塞茜莉亚"]对......
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]你是来找妈妈的吗？
[Character(name="avg_npc_352_1#4$1")]
[name="塞茜莉亚"]......是的，我想找妈妈......
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]哎呀，这位小哥，那你是，费莉亚的亲戚之类的？这个孩子是寄养在乡下吗？你带她来看妈妈？
[name="知性的拉特兰市民"]真没想到，难怪之前我给费莉亚介绍对象她都推辞了......原来孩子都这么大了。
[name="知性的拉特兰市民"]小哥，你怎么不说话了？嗯？你还好吗？
[Character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]说着说着快走到了，那边就是费莉亚家了，我帮你们去敲个门？
[Character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......瑟法斯街7-265号。
[Character(name="avg_npc_368_1#1$1")]
[name="知性的拉特兰市民"]哎？原来你知道地址啊。
[Character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......嗯，我知道。
[Character(name="avg_4036_forcer_1#5$1",name2="avg_npc_352_1#5$1",focus=2)]
[name="塞茜莉亚"]艾泽尔哥哥，你怎么了？你的脸色好难看......
[Character(name="avg_4036_forcer_1#5$1",name2="avg_npc_352_1#5$1",focus=1)]
[name="艾泽尔"]我没事，塞茜莉亚......我们、你，先回家。
[Character(name="avg_4036_forcer_1#5$1",name2="avg_npc_352_1#5$1",focus=1)]
[name="艾泽尔"]走，回家吧，塞茜莉亚。
[Dialog]
[Character(fadetime=1)]
[delay(time=1)]
[stopmusic(fadetime=3)]
名字。
从见到塞茜莉亚就意外不断，我甚至忘记了“我忘记问塞茜莉亚妈妈的名字”这件事。
名字......
生病的母亲，白衣服的执行者，穿袍子的人......
......
我该怎么告诉塞茜莉亚？
我该带她去哪里找妈妈？
......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g10_laterano_roof",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_300_phenxi_1#7$1")]
[PlaySound(key="$grenade_launcher_shot", volume=1)]
[delay(time=0.51)]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[delay(time=1)]
[Character(name="avg_300_phenxi_1#2$

... (全文16837字符)
```

### level_act16side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g8_laterano_dwelling",screenadapt="coverall")]
[character(name="avg_npc_355_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]是菲亚梅塔啊......嗯？你好像有点狼狈？
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]与你无关。
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]别这么大火气，要不要坐下来喝杯茶？
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]别打哈哈，你为什么会在这里？莫斯提马没有提过你会支援。
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]因为薇尔丽芙也没有给我正式下令嘛。
[character(name="avg_npc_355_1#4$1")]
[name="奥伦"]不过我个人可是很愿意帮忙的哦？
[name="奥伦"]莫斯提马说，还有一拨人在追这个小女孩，而且已经和你打过照面了，对吧？
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]......是这样没错。
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]我听公证所报告说艾泽尔切断定位讯号之后，就猜到你可能会被截了。如果被对方抓到时间差，这女孩不就搞丢了吗？
[name="奥伦"]我是不知道为什么莫斯提马不来帮你的忙，但既然她动不了，我就顺手卖她个人情呗。
[character(name="avg_npc_355_1#4$1")]
[name="奥伦"]让你和莫斯提马欠人情的机会可不多。
[character(name="avg_300_phenxi_1#8$1")]
[name="菲亚梅塔"]......几个不成气候的散兵游勇，还拦不住我。
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]“小心驶得万年船”啊，菲亚梅塔。你这样很容易在薇尔丽芙那里落下把柄的。
[character(name="avg_npc_355_1#4$1")]
[name="奥伦"]噢，我说的是一句炎国谚语，就是做事要小心谨慎的意思。
[character(name="avg_300_phenxi_1#6$1")]
[name="菲亚梅塔"]别卖弄了，奥伦，你就是喜欢这样说话才惹人讨厌。
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]不说笑了。既然你来了，那我的人情也送到了，后面就交给你吧。
[character(name="avg_npc_355_1#4$1")]
[name="奥伦"]或者，你需要我护送一程吗，可爱的菲亚梅塔？
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]不用了，再见，奥伦。
[Dialog]
[character(name="avg_npc_355_1#1$1")]
[delay(time=0.8)]
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)] 
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]执行者艾泽尔，把这个女孩交给我。
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]你最好不要拒绝。
[character(name="avg_4036_forcer_1#6$1")]
[name="艾泽尔"]......
[name="艾泽尔"]您是叫做菲亚梅塔，是吗？菲亚梅塔女士，我有一个请求。
[dialog]
[character]
[playsound(key="$d_avg_gunload")]
[delay(time=1)]
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]好了，说吧，你的请求。
[name="菲亚梅塔"]别乱动，我不保证我的手一定很稳。
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......我知道我之前违背里凯莱前辈命令、关掉终端的做法很可疑，但......
[character(name="avg_4036_forcer_1#6$1")]
[name="艾泽尔"]请相信，我并没有背叛拉特兰。
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]我没有完全遵从公证所的命令，是因为不希望塞茜莉亚遭遇不测......而且，我答应了她一件事。
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]这和我有什么关系？
[character(name="avg_4036_forcer_1#8$1")]
[name="艾泽尔"]......我的请求是，让我随同您，一起和塞茜莉亚前往大教堂。如果教皇厅需要了解这件事相关的信息，我在也比较方便，不是吗？
[character(name="avg_300_phenxi_1#8$1")]
[name="菲亚梅塔"]话说在前头，如果你指望的是，只要你跟着去，就能影响上面对这件事的处理结果——我建议你不要抱这种幻想。
[name="菲亚梅塔"]更进一步......如果你想的是什么，要是教皇厅对这个女孩的安排不合你心意，你就把人劫走......
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]就更别做梦了。
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]不敢。大教堂有铳骑驻守，我很清楚。
[character(name="avg_4036_forcer_1#7$1")]
[name="艾泽尔"]而且，我毕竟是拉特兰的执行者。之前我有所担忧，是因为不了解塞茜莉亚究竟是什么情况，也不能确定追着塞茜莉亚的究竟有哪些人......
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]现在我已经明白了，我会服从您的安排。
[character(name="avg_300_phenxi_1#8$1")]
[name="菲亚梅塔"]可以。
[dialog]
[playsound(key="$d_avg_clothmovement")]
[delay(time=1.5)]
[character(name="avg_300_phenxi_1#9$1")]
[name="菲亚梅塔"]嗯......你是叫塞茜莉亚是吗？还走得动吗？
[character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]......艾泽尔哥哥......
[character(name="avg_4036_forcer_1#8$1")]
[name="艾泽尔"]......塞茜莉亚，要是太累了，我背你吧......
[character(name="avg_300_phenxi_1#8$1")]
[name="菲亚梅塔"]我来抱她吧，你太慢了。
[character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]（小声）艾泽尔哥哥......
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......没事的，不会有事的，塞茜莉亚。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_361_1#1$1")]
[name="薇尔丽芙"]执行者艾泽尔·帕斯托莱，今天上午前往司提望区瑟法斯街7-265号执行遗体身份验证、遗嘱确认和守护铳回收任务。
[name="薇尔丽芙"]近午，艾泽尔出现于司提望区中心医院，送诊一名八岁萨科塔女童，后以非常规方式离开。
[name="薇尔丽芙"]司提望区瑟法斯街7-265号户主费莉亚·拉珀尔塔，今天上午病逝于家中，遗体已收容至安魂教堂。
[name="薇尔丽芙"]瑟法斯街7-265号户籍登记人口为一人，社区记录的居住人口也是一人。
[name="薇尔丽芙"]调查瑟法斯街7-265号的近二十年的房屋维护记录，发现七年前曾增筑地下室，承包商留下的单据显示建筑用途是储物。
[name="薇尔丽芙"]这里是费莉亚·拉珀尔塔的资料照片和艾泽尔送诊女童的监控影像。
[name="薇尔丽芙"]女童的来历，想必诸位已有结论。
[name="薇尔丽芙"]另外，根据艾泽尔午前发来的回报，费莉亚·拉珀尔塔未留遗嘱，未作遗嘱预登记，理由也相当明确了：她希望尽量避免与公证所往来。
[name="薇尔丽芙"]合理推断，费莉亚·拉珀尔塔自知时日无多，必定会为自己的女儿准备后路。
[name="薇尔丽芙"]目前无法确定艾泽尔是否就是费莉亚·拉珀尔塔的委托对象，但根据艾泽尔的背调结果，几率较小。
[name="薇尔丽芙"]结合菲亚梅塔发回的信息，更有可能的受托对象应当是......
[character(name="avg_npc_361_1#3$1")]
[name="薇尔丽芙"]迷途者。
[dialog]
[playsound(key="$book_close")]
[delay(time=1)]
[character(name="avg_npc_361_1#6$1")]
[name="薇尔丽芙"]莫斯提马，这就是你留在大教堂的原因吗？
[character(name="avg_213_mostma_1#7$2")]
[name="莫斯提马"]只是暂时。
[character(name="avg_npc_356_1#10$1")]
[name="教宗"]别那么紧张，薇尔。吃泡芙吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="26_g10_laterano_roof",screenadapt="showall")]
[character(name="char_empty",name2="avg_npc_355_1#8$1",focus=2)]
[Delay(time=1)]
[playMusic(intro="$plot_intro", key="$plot_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[playsound(key="$d_gen_transmissionget")]
[CharacterCutin(widgetID="1", name="avg_npc_357_1#6$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[delay(time=1)]
[character(name="char_empty",name2="avg_npc_355_1#1$1",focus=2)]
[name="奥伦"]唉，幸好选了比较温和的方法。
[character(name="char_empty",name2="avg_npc_355_1#4$1",focus=2)]
[name="奥伦"]要是菲亚梅塔来的时候，正好看到我干掉公证所的人，那就糟糕了。
[character(name="char_empty",name2="avg_npc_355_1#8$1",focus=1)]
[name="帕蒂亚"]别找借口了。你不和那个执行者啰嗦那么多

... (全文18708字符)
```

### level_act16side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g9_laterano_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]呼......呼......
[name="艾泽尔"]他们想跑！
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]没这么简单！
[dialog]
[character]
[delay(time=0.51)]
[character(name="avg_npc_362_1#1$1",name2="avg_npc_364_1#1$1")]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[character]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_362_1#1$1",name2="avg_npc_364_1#1$1",focus=2)]
[name="愉快的小贩"]......！！
[character(name="avg_npc_362_1#1$1",name2="avg_npc_364_1#1$1",focus=1)]
[name="安静的小贩"]唔呃......我掩护你，快逃！！
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=1.5)] 
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]这个佩洛竟然帮萨卡兹挡下攻击......两个，都别想跑。
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]艾泽尔，你待在这儿，不许......
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]不许轻举妄动。我明白，菲亚梅塔小姐。终端我打开了。
[name="艾泽尔"]请相信我，我想确保的只有塞茜莉亚的安全。
[character(name="avg_300_phenxi_1#6$1")]
[name="菲亚梅塔"]......我改主意了。你不能留在这里。现在，立刻送塞茜莉亚前往大教堂。
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]你们就这么留在大街上......更危险。
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=1.5)] 
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]......
[name="艾泽尔"]走吧，塞茜莉亚。
[character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]嗯......？我们刚才不是向着圣像走的吗，圣像在那边，艾泽尔哥哥。
[character(name="avg_4036_forcer_1#7$1")]
[name="艾泽尔"]......我们绕一下路。
[character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]绕路？
[character(name="avg_4036_forcer_1#6$1")]
[name="艾泽尔"]你现在要去的地方应该是......
[name="艾泽尔"]安魂教堂。
[stopmusic(fadetime=2)]
[Dialog]
[character]
[delay(time=2)]
[Background(image="bg_black",screenadapt="coverall",fadetime=1.5)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Delay(time=2)]
[Subtitle(text="萨卡兹。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="我原本打算到大教堂之后，请菲亚梅塔小姐帮忙求情......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="要让高阶执行者监察也好、要让戍卫队随行也好......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="只要能确认塞茜莉亚对拉特兰是安全的......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="能不能，让塞茜莉亚，在费莉亚下葬之前，去见母亲最后一面。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="可是，萨卡兹。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="如果塞茜莉亚的父亲是萨卡兹......那塞茜莉亚就应该是萨卡兹。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="她却获得了光环......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="......我到底是不是在做梦。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="如果塞茜莉亚只是普通的“例外”......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="但她是萨卡兹......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="获得了光环的萨卡兹，怎么可能从大教堂走出来......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="就算，就算，她不会被......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="她怎么可能还能离开大教堂......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="......即使会被公证所开除，我也要试一试。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="带塞茜莉亚去安魂教堂。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="至少让她说声再见。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="26_g11_laterano_alley",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]你们跑不掉的。
[character(name="avg_npc_362_1#1$1",name2="avg_npc_364_1#1$1",focus=2)]
[name="愉快的小贩"]她追得好快......
[character(name="avg_npc_362_1#1$1",name2="avg_npc_364_1#1$1",focus=1)]
[name="安静的小贩"]怎么办怎么办，根本甩不掉......
[dialog]
[Character(name="avg_300_phenxi_1#7$1")]
[CameraShake(duration=0.4, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$grenade_launcher_shot", volume=1)]
[delay(time=0.51)]
[character]
[delay(time=0.51)]
[PlaySound(key="$grenade_explosion", volume=1)]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[character]
[delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[dialog]
[character(name="avg_npc_364_1#1$1")]
[delay(time=0.51)]
[character]
[PlaySound(key="$d_avg_singleblunt", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.2, block=true)]
[character(name="avg_300_phenxi_1#7$1")]
[characteraction(name="middle", type="move", xpos=-100, fadetime=0.5,block=false)]
[delay(time=0.8)]
[characteraction(name="middle", type="move", xpos=100, fa

... (全文17733字符)
```

### level_act16side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[character(name="avg_300_phenxi_1#6$1",name2="avg_213_mostma_1#1$2",focus=1)]
[name="菲亚梅塔"]......
[character(name="avg_300_phenxi_1#6$1",name2="avg_213_mostma_1#1$2",focus=2)]
[name="莫斯提马"]脸色这么差，通宵了？
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#1$2",focus=1)]
[name="菲亚梅塔"]他回来了，我看到了，绝不会认错......那种光，安多恩的源石技艺！
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#6$2",focus=2)]
[name="莫斯提马"]啊......所以这就是你昨天下午突然没了消息的原因。
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#9$2",focus=2)]
[name="莫斯提马"]不过，他竟然直接找上你了？
[character(name="avg_300_phenxi_1#7$1",name2="avg_213_mostma_1#9$2",focus=1)]
[name="菲亚梅塔"]......他不是来找我的。
[name="菲亚梅塔"]昨天带那个混血女孩回大教堂的路上......我遇到了萨卡兹。
[character(name="avg_300_phenxi_1#7$1",name2="avg_213_mostma_1#4$2",focus=2)]
[name="莫斯提马"]这种时候？萨卡兹？在拉特兰大街上？
[character(name="avg_300_phenxi_1#7$1",name2="avg_213_mostma_1#4$2",focus=1)]
[name="菲亚梅塔"]......没错。我去追萨卡兹，让艾泽尔带那个女孩回大教堂。
[character(name="avg_300_phenxi_1#6$1",name2="avg_213_mostma_1#4$2",focus=1)]
[name="菲亚梅塔"]我追到法柏尔区边缘......萨卡兹，被安多恩的源石技艺掩护，逃走了。
[name="菲亚梅塔"]至于艾泽尔，我以为他昨天就到大教堂了。
[name="菲亚梅塔"]但他没来。这是他的终端。贴在一辆使节礼宾车的车底。
[character(name="avg_300_phenxi_1#6$1",name2="avg_213_mostma_1#4$2",focus=2)]
[name="莫斯提马"]啧，那个见习小鬼演技有那么好？把你骗过了？
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#4$2",focus=1)]
[name="菲亚梅塔"]......我不认为那是演技。但我确实不明白他为什么......难道，安多恩把他也掳走了......
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#1$2",focus=2)]
[name="莫斯提马"]菲亚梅塔，我觉得你需要冷静点。
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#1$2",focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="菲亚梅塔"]我很冷静，我比这八年中的任何一分钟都要冷静！
[character(name="avg_300_phenxi_1#7$1",name2="avg_213_mostma_1#1$2",focus=1)]
[name="菲亚梅塔"]你们始终不肯告诉我，那天我离开之后的事情。
[character(name="avg_300_phenxi_1#5$1",name2="avg_213_mostma_1#1$2",focus=1)]
[name="菲亚梅塔"]明明只是个清剿任务......明明比预想中还要顺利......
[name="菲亚梅塔"]我只是接了一个临时支援......离开了四个小时......
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#1$2",focus=1)]
[name="菲亚梅塔"]回到那个废墟的时候，什么都迟了。
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#6$2",focus=2)]
[name="莫斯提马"]我能和你讲的都讲过了。
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#6$2",focus=1)]
[name="菲亚梅塔"]锁与匙到底给了他什么？能让他疯到对蕾缪安动手？
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#11$2",focus=2)]
[name="莫斯提马"]这个，还真不是我不想告诉你......我也得知道啊。
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#11$2",focus=1)]
[name="菲亚梅塔"]......
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#1$2",focus=2)]
[name="莫斯提马"]菲亚梅塔，我们现在在拉特兰，在拉特兰大教堂，这里不是什么卡兹戴尔的野外废墟。
[character(name="avg_300_phenxi_1#8$1",name2="avg_213_mostma_1#7$2",focus=2)]
[name="莫斯提马"]你该休息一下，菲亚梅塔。要不，我去帮你把年假请了？公证所的年假不用会过期的。
[character(name="avg_300_phenxi_1#3$1",name2="avg_213_mostma_1#7$2",focus=1)]
[name="菲亚梅塔"]......你在开什么玩笑？！
[dialog]
[character(name="avg_300_phenxi_1#3$1",name2="avg_213_mostma_1#11$2")]
[delay(time=1)]
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#11$2",focus=1)]
[name="菲亚梅塔"]后天就是会议开幕，安多恩带着萨卡兹出现在拉特兰城，掳走了一个混血萨科塔女孩，甚至可能对执行者动了手......
[name="菲亚梅塔"]......是我大意了，看那个萨卡兹对法柏尔区的熟悉程度，他们在拉特兰应该已经潜伏很久了......这个疯子到底又打算干什么！
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#6$2",focus=2)]
[name="莫斯提马"]我说真的，冷静点，菲亚梅塔。
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#9$2",focus=2)]
[name="莫斯提马"]老家伙已经知道迷途者的消息了，薇尔丽芙也知道。我昨天在大教堂也是工作了的——虽然我不是很喜欢把开会叫做工作。
[character(name="avg_300_phenxi_1#2$1",name2="avg_213_mostma_1#7$2",focus=2)]
[name="莫斯提马"]总而言之，拉特兰没你想得那么危险。安多恩也只是个萨科塔而已，没有六只眼睛四条胳膊。你要真想对付他，现在去休息两个小时。
[name="莫斯提马"]然后，我们去找蕾缪安。
[character(name="avg_300_phenxi_1#4$1",name2="avg_213_mostma_1#7$2",focus=1)]
[name="菲亚梅塔"]......
[character(name="avg_300_phenxi_1#4$1",name2="avg_213_mostma_1#2$2",focus=2)]
[name="莫斯提马"]看来你还没有完全失去理智。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="26_g6_laterano_chapelin",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_351_1#8$1",name2="avg_4036_forcer_1#8$1",focus=1)]
[name="修士"]昨晚休息得怎么样？
[character(name="avg_npc_351_1#8$1",name2="avg_4036_forcer_1#8$1",focus=2)]
[name="艾泽尔"]我休息得很好。谢谢你收留我们，先生。
[character(name="avg_npc_351_1#7$1",name2="avg_4036_forcer_1#8$1",focus=1)]
[name="修士"]安魂教堂的门永远敞开，只要你不嫌弃这里太过压抑。
[name="修士"]毕竟，生者和死者都会到访这里。
[character(name="avg_npc_351_1#7$1",name2="avg_4036_forcer_1#8$1",focus=2)]
[name="艾泽尔"]......此时能有一处容身之所已经很难得了。说起来，塞茜莉亚......
[character(name="avg_npc_351_1#8$1",name2="avg_4036_forcer_1#8$1",focus=1)]
[name="修士"]你带来的女孩，对吗？姐妹们告诉我，她昨晚睡得很沉，大概是累了吧。
[name="修士"]也许她度过了太漫长的一天。
[dialog]
[character]
[playsound(key="$dooropenquite")]
[delay(time=1)]
[character(name="avg_npc_352_1#10$1")]
[name="塞茜莉亚"]艾泽尔哥哥，修士先生，早上好。
[character(name="avg_npc_351_1#8$1",name2="avg_4036_forcer_1#4$1",focus=2)]
[name="艾泽尔"]早上好，塞茜莉亚，你好像精神不错。
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"] 嗯......毕竟，今天还有事情要做。
[character(name="avg_npc_351_1#8$1",name2="avg_4036_forcer_1#3$1",focus=2)]
[name="艾泽尔"]嗯......？
[character(name="avg_npc_352_1#4$1")]
[name="塞茜莉亚"]......我向修士先生拜托了一件事。
[name="塞茜莉亚"]修士先生告诉我，来到这里的......去世的人，会有和亲人告别的仪式。
[name="塞茜莉亚"]我也想和妈妈......好好道个别......
[character(name="avg_npc_351_1#2$1",name2="avg_4036_forcer_1#3$1",focus=1)]
[name="修士"]为费莉亚女士办一场葬礼。
[character(name="avg_npc_351_1#2$1",name2="avg_4036_forcer_1#5$1",focus=2)]
[name="艾泽尔"]......是吗，葬礼......
[character(name

... (全文13627字符)
```

### level_act16side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g6_laterano_chapelin",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#6$1",focus=2)]
[name="塞茜莉亚"]再多和我讲些！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#6$1",focus=1)]
[name="罗塞菈"]呀，小心手上的蜡烛，别烫着！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]啊！不能捏坏形状......不然就不好看了。
[name="塞茜莉亚"]为了妈妈......我要做得完美一点。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=1)]
[name="罗塞菈"]好啦，我讲得已经够多的了。无非是无聊的冒险，寻常的生活。至于传说中的卡兹戴尔......
[name="罗塞菈"]说来惭愧，我们都没有去过。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]萨卡兹的卡兹戴尔......一定就像萨科塔的拉特兰一样吧！是萨卡兹们的家乡......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#6$1",focus=2)]
[name="塞茜莉亚"]每个人都开开心心的，也会有棉花糖车吧？还有点心店......大街上会有好多高高兴兴的萨卡兹，大家互相打招呼！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#6$1",focus=1)]
[name="罗塞菈"]......也许是吧。
[name="罗塞菈"]终有一天。
[name="罗塞菈"]该说说你了，塞茜莉亚。你的爸爸妈妈是什么样的人？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]......其实，我也不太清楚......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]我见到爸爸的次数很少......每次要见爸爸的时候，妈妈就会准备很久，带着我在晚上出门，走很远很远......走到树林里。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#11$1",focus=2)]
[name="塞茜莉亚"]我们在森林里见面，爸爸总是穿着厚厚的斗篷，似乎刚从遥远的地方赶过来......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#11$1",focus=2)]
[name="塞茜莉亚"]我其实不太记得爸爸的长相，但我记得爸爸的角！漆黑又笔直，在月亮下闪闪发光。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#11$1",focus=2)]
[name="塞茜莉亚"]他会牵着我的手在树林的边缘散步，告诉我每一棵树的种类和年龄......城外的晚上好安静，连羽兽的叫声都没有，但我一点也不怕。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#11$1",focus=2)]
[name="塞茜莉亚"]爸爸老是紧紧牵着我的手，其实会有一点点疼......但我不想告诉他。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]每次见到爸爸，我觉得爸爸比我还要高兴......！好像也有点......紧张？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]我走累了，妈妈就会背着我回家。我回头，就会看到爸爸站在高高的树下面，一直看着我们，走了很远很远，他还站在那里......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=1)]
[name="罗塞菈"]你的爸爸妈妈都是了不起的人。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#6$1",focus=2)]
[name="塞茜莉亚"]我觉得妈妈可厉害了！她什么都会！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]对了，你看，这是妈妈的守护铳，艾泽尔哥哥放在我这里了。
[name="塞茜莉亚"]妈妈说，爸爸根本打不过她......她都是让着爸爸呢！不过我想爸爸也应该很厉害，嗯！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=1)]
[name="罗塞菈"]哈哈塞茜莉亚，我说的“了不起”和你说的“厉害”，可能不是同一回事。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#6$1",focus=2)]
[name="塞茜莉亚"]是吗？那爸爸妈妈一定又了不起又厉害！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]不过，妈妈从来不和我讲她和爸爸认识的故事，我每次想问，稀里糊涂地就被妈妈绕去说别的了......为什么妈妈不告诉我呢？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=1)]
[name="罗塞菈"]......当我们还小的时候啊，更重要的事情还有很多。你喜欢看泡茶吗，我小时候可喜欢看泡茶啦，茶水的颜色一层一层地变化......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#2$1",focus=2)]
[name="塞茜莉亚"]......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]......罗塞菈姐姐，你现在绕开话题的样子，和妈妈就很像哦......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#2$1",focus=2)]
[name="塞茜莉亚"]......其实我也不是什么都不知道。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]昨天我在城里跑了好多地方，除了你，一个萨卡兹都没见到......萨卡兹，不能来拉特兰，是不是？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#12$1",focus=2)]
[name="塞茜莉亚"]所以爸爸和妈妈也不应该在一起......不对，我是想说，是不是有人不让爸爸妈妈在一起？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#12$1",focus=1)]
[name="罗塞菈"]不，没有什么不应该在一起......这些一定会改变的。不会很久......总有一天。
[name="罗塞菈"]相爱没有罪过。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#2$1",focus=2)]
[name="塞茜莉亚"]......是吗。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#2$1",focus=1)]
[name="罗塞菈"]我们就是为此来到这里的。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#5$1",focus=2)]
[name="塞茜莉亚"]到了那一天，我也可以在拉特兰的大街上随便乱逛了？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#5$1",focus=1)]
[name="罗塞菈"]当然。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#12$1",focus=2)]
[name="塞茜莉亚"]再也不用偷偷藏在房间里？那拉特兰每一家糖果店我都可以去一次吗？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#12$1",focus=1)]
[name="罗塞菈"]一次哪里够呀，塞茜莉亚喜欢去多少次就去多少次。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=2)]
[name="塞茜莉亚"]呜......真希望那一天快点来......好想快点长大！
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#10$1",focus=1)]
[name="罗塞菈"]是啊，如果你快快长大，也许......
[name="罗塞菈"]不，塞茜莉亚，我们不用那么着急。我小时候，总觉得等长大了，什么烦恼都可以解决掉。可是，等到真的长大了......
[name="罗塞菈"]长大是一件非常非常非常辛苦的事，塞茜莉亚，对你来说更是这样，你肩负着......不，算了。你还小，别去想这些。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#12$1",focus=2)]
[name="塞茜莉亚"]可每个人都会长大呀？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#12$1",focus=1)]
[name="罗塞菈"]......是啊，我们没有选择。
[Dialog]
[character]
[stopmusic(fadetime=1)]
[delay(time=1.5)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
一直微笑着的罗塞菈露出了有些落寞的神情。
她看向小教堂的窗外，外面是开满鲜花的墓园，再远处，隐约可见高踞于拉特兰城中心的圣像。
她轻轻哼起了歌。忧伤，又依稀带着希望。
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#5$1",focus=2)]
[name="塞茜莉亚"]啊，是这首歌！昨天碰到罗塞菈姐姐的时候......
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=2)]
[name="塞茜莉亚"]妈妈教我这首歌的时候说，歌词她记不清楚了，就用啦啦啦代替了。可是曲调真的好好听......本来的歌词，是讲什么的呢？
[character(name="avg_npc_363_1#1$1",name2="avg_npc_352_1#9$1",focus=1)]
[name="罗塞菈"]这是萨卡兹的歌，歌词讲的是一个英雄，他要出发去做了不起的事情啦，人们就唱歌和他告别，送他启程，愿他平安归来。
[name="罗塞菈"]歌里面唱啊，英雄就要出发啦，沿着通往远方的路，去实现他的梦想......
[name="罗塞菈"]也许路途遥远，但一定，一定......
[Dialog]
[character]
[delay(time=1)]
[playsound(key="$dooropenquite")]
[character(name="avg_npc_351_1#1$1",name2="avg_4036_forcer_1#1$1",fadetime=1.5)]
[delay(time=3)]
[character(name="avg_npc_352_1#6$1")]

... (全文13467字符)
```

### level_act16side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g5_laterano_chapelout",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[character(name="avg_npc_001")]
[name="凹眼眶的掘墓人"] 嗯，多深了？
[character(name="avg_npc_006",name2="avg_npc_001",focus=1)]
[name="没精神的掘墓人"] 再多挖一点儿？
[name="没精神的掘墓人"] 早晚都是一片废墟，坟墓又不能装上轮子躲天灾。
[name="没精神的掘墓人"] 人总想给自己的一辈子留下点儿痕迹......可惜都是痴心妄想。还不如化成灰抛进荒野哩。
[character(name="avg_npc_006",name2="avg_npc_001",focus=2)]
[name="凹眼眶的掘墓人"] 那样我们就没活儿干了。
[character(name="avg_npc_006",name2="avg_npc_001",focus=1)]
[name="没精神的掘墓人"] 说得也是。
[character(name="avg_npc_006",name2="avg_npc_001",focus=2)]
[name="凹眼眶的掘墓人"] 不过，我看啊，坟墓也不是给死人用的。是那些活着的人需要这些东西......这些仪式，还有一块立在这儿的石头。
[name="凹眼眶的掘墓人"] 人得对着这些东西告别，然后重新开始——
[character(name="avg_npc_006",name2="avg_npc_001",focus=1)]
[name="没精神的掘墓人"] 哈，直到走到自己的坟头。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Background(image="26_g5_laterano_chapelout",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]仪式的准备差不多了。
[character(name="avg_npc_352_1#9$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]......嗯。
[character(name="avg_npc_352_1#9$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]我......我不知道。
[character(name="avg_npc_352_1#2$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]今天......感觉不太好......
[character(name="avg_npc_352_1#4$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]妈妈......
[name="塞茜莉亚"]修士先生，昨天我很高兴......
[name="塞茜莉亚"]罗塞菈姐姐和我说了好多有意思的事情......我们一起为葬礼做准备，我觉得......好像我能为妈妈做一些事了。
[name="塞茜莉亚"]可是......应该做的事情做完了......之后呢？
[name="塞茜莉亚"]我觉得......我为妈妈努力了......
[name="塞茜莉亚"]可是妈妈，真的能看见吗？
[name="塞茜莉亚"]我做的这些......真的有用吗？
[character(name="avg_npc_352_1#12$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]修士先生，您是不是经历过很多次了......
[name="塞茜莉亚"]在这种时候，在......葬礼上。我......该怎么做......才对呢？
[character(name="avg_npc_352_1#9$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]......等葬礼结束了，我又该怎么办......
[character(name="avg_npc_352_1#9$1",name2="avg_npc_351_1#7$1",focus=2)]
[name="安多恩"]唔。是啊，葬礼......
[name="安多恩"]你年纪还小，但我不愿意搪塞你。
[character(name="avg_npc_352_1#9$1",name2="avg_npc_351_1#1$1",focus=2)]
[name="安多恩"]我们为了别人做的许多事，其实仍是为了我们自己。
[name="安多恩"]塞茜莉亚，这不是自私，而是指每个人活着所做的一切，归根到底，只是在为“自我”塑形。
[name="安多恩"]葬礼，告别，是因为有人离去，也是给自己的歇息。
[name="安多恩"]为已经走过的路划一个标记。
[name="安多恩"]许多大人......以此让自己安宁。但是否能获得安宁，或者是否能获得任何东西，都不在于葬礼本身。
[name="安多恩"]而在于经历这一切之后的我们自己。
[name="安多恩"]回望与歇息之后，我们只能继续前进。
[character(name="avg_npc_352_1#12$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]前进去哪里呢......？
[character(name="avg_npc_352_1#12$1",name2="avg_npc_351_1#8$1",focus=2)]
[name="安多恩"]这需要问你自己，塞茜莉亚。
[name="安多恩"]这是只有自己才能回答的问题，是你和我、每一个人，一生都要回答的问题。
[character(name="avg_npc_352_1#2$1",name2="avg_npc_351_1#8$1",focus=1)]
[name="塞茜莉亚"]......自己。
[character(name="avg_npc_352_1#2$1",name2="avg_npc_351_1#1$1",focus=2)]
[name="安多恩"]路途只有自己能够寻找，也只能凭自己的双足行过。
[character(name="avg_npc_352_1#5$1",name2="avg_npc_351_1#1$1",focus=1)]
[name="塞茜莉亚"]修士先生，您呢？您知道这么多，您的路......是怎么样的？
[character(name="avg_npc_352_1#5$1",name2="avg_npc_351_1#1$1",focus=2)]
[name="安多恩"]塞茜莉亚，我无法回答你。我甚至不敢说自己找到了。
[name="安多恩"]这种探索是如此艰辛，如此的无望，简直要让人怀疑，道路是否真的存在......
[name="安多恩"]但我还没有放弃。所以我和兄弟姐妹们称呼自己为......
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]......“寻路者”。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[delay(time=1)]
[Background(image="26_g6_laterano_chapelin",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_4036_forcer_1#9$1",fadetime=1,block=true)]
[delay(time=1)]
[dialog]
[characteraction(name="middle", type="move", xpos=-100, ypos=0,fadetime=2, block=true)]
[delay(time=2)]
[characteraction(name="middle", type="move", xpos=240, ypos=0,fadetime=2, block=true)]
[delay(time=1.5)]
[name="艾泽尔"]烛台，烛台在哪里......
[name="艾泽尔"]（......有人？是医院那个黎博利，是叫帕蒂亚？......还有那个叫奥伦的万国信使......）
[dialog]
[character]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_355_1#10$1",name2="avg_npc_357_1#1$1",fadetime=1,block=true)]
[delay(time=2)]
[character(name="avg_npc_355_1#2$1",name2="avg_npc_357_1#1$1",focus=1)]
[name="奥伦"]我真的搞不懂，那男人在搞什么名堂。
[character(name="avg_npc_355_1#2$1",name2="avg_npc_357_1#6$1",focus=2)]
[name="帕蒂亚"]注意你的措辞，奥伦。
[character(name="avg_npc_355_1#10$1",name2="avg_npc_357_1#6$1",focus=1)]
[name="奥伦"]现在是最好的时机。比起浪费时间办什么葬礼，现在要做的事情还有很多吧。
[character(name="avg_npc_355_1#10$1",name2="avg_npc_357_1#6$1",focus=2)]
[name="帕蒂亚"]我听说你和这孩子的母亲是熟人来着，真冷漠。
[character(name="avg_npc_355_1#4$1",name2="avg_npc_357_1#6$1",focus=1)]
[name="奥伦"]我带着小塞茜莉亚的消息来见安多恩时，就已经做出选择了。
[character(name="avg_npc_355_1#1$1",name2="avg_npc_357_1#6$1",focus=1)]
[name="奥伦"]她足以让这座城市坠下神坛。
[character(name="avg_npc_355_1#8$1",name2="avg_npc_357_1#6$1",focus=1)]
[name="奥伦"]因此，也足以动摇那位总躲在金色与红色帷幕下的圣人......以及更多的人。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]（他在说什么......？）
[character(name="avg_npc_355_1#8$1",name2="avg_npc_357_1#1$1",focus=2)]
[name="帕蒂亚"]一个萨科塔想毁灭他的圣城，凭借一个混血女孩？真是肮脏。
[character(name="avg_npc_355_1#8$1",name2="avg_npc_357_1#1$1",focus=1)]
[name="奥伦"]别把我说得像个破坏狂。我只是说，“足以”。不等于我要去做。
[name="奥伦"]不如说，这件事不被付诸实践，它作为筹码的面额才最大。
[name="奥伦"]我需要确保的只是小塞茜莉亚不落在教皇厅手里......在这一点上，安多恩姑且与我同路。
[character(name="avg_npc_355_1#8$1",name2="avg_npc_357_1#6$1",focus=2)]
[name="帕蒂亚"]奥伦，我奉劝你一句。
[name="帕蒂亚"]不论你想拿塞茜莉亚耍什么把戏，别忘了你曾经给先导的承诺。
[character(name="avg_npc_355_1#4$1",name2="avg_npc_357_1#6$1",focus=1)]
[name="奥伦"]......多谢忠告，我还不介意和你们再同行一段。
[name="奥伦"]恕不奉陪了。若是想消磨时间，比起葬礼，我有更好的去处。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]......
[name="艾泽尔"]（......看来这帮人内部也不是铁板一块。）
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]（我最担心的事情......没想到竟然有万国信使牵涉其中......）
[name

... (全文9604字符)
```

### level_act16side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g5_laterano_chapelout",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[playsound(key="$bullet_loading")]
[delay(time=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[dialog]
[delay(time=1)]
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]塞茜莉亚，小心！
[character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]艾泽尔哥哥！
[dialog]
[Character(name="avg_npc_357_1#3$1")]
[name="帕蒂亚"]先导......我们不能退让了！
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]你！别想把塞茜莉亚当成筹码！
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]......艾泽尔！带塞茜莉亚过来！
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]喂，艾泽尔！你到底怎么回事！难道你真和这帮......
[dialog]
[character]
[Character(name="avg_300_phenxi_1#3$1",name2="avg_npc_357_1#3$1")]
[CameraShake(duration=0.4, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[characteraction(name="right", type="move", xpos=-100, power=0, times=1, fadetime=0.2, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="move", xpos=-20, power=0, times=1, fadetime=0.4, block=true)]
[characteraction(name="right", type="move", xpos=40, power=0, times=1, fadetime=0.4, block=true)]
[delay(time=1)]
[Character(name="avg_npc_357_1#3$1")]
[name="帕蒂亚"]异端分子还是恐怖组织？教廷也只能想出这种无聊的罪名了！
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]帕蒂亚，滚开！
[Character(name="avg_npc_357_1#6$1")]
[name="帕蒂亚"]菲亚梅塔......你说得对，没有谁的想法能够轻易改变。
[name="帕蒂亚"]你我都一样。
[dialog]
[character]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.2, block=true)]
[PlaySound(key="$swordtsing2", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Delay(time=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[dialog]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]你似乎过得不错。
[character(name="avg_213_mostma_1#5$2")]
[name="莫斯提马"]托你的福。你倒是老了不少......“队长”。
[character(name="avg_npc_351_1#7$1")]
[name="安多恩"]也是托你的福。那处铳伤很久才好。
[character(name="avg_213_mostma_1#7$2")]
[name="莫斯提马"]哈哈哈，不错。总好过挨她的子弹吧。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]是啊。
[character(name="avg_213_mostma_1#1$2")]
[name="莫斯提马"]蕾缪安差点就死了。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]我知道。
[character(name="avg_npc_351_1#7$1")]
[name="安多恩"]总好过挨她的子弹。
[character(name="avg_213_mostma_1#8$2")]
[name="莫斯提马"]......看来你的疯病并没好多少。
[character(name="avg_213_mostma_1#9$2")]
[name="莫斯提马"]喂，那边的小子，你就是那个艾泽尔？
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]（又一个万国信使吗......现在究竟应该......）
[dialog]
[character]
[character(name="avg_213_mostma_1#9$2")]
[delay(time=1)]
[playsound(key="$d_avg_cloakmovement")]
[character]
[character(name="avg_213_mostma_1#9$1",fadetime=1,block=true)]
[delay(time=2)]
[character(name="avg_npc_352_1#3$1")]
[name="塞茜莉亚"]！
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]......堕天使？！菲亚梅塔小姐，这是怎么......
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"]......啊，是啊，堕天。理所当然，你用铳对我射击。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]你感受不到了。
[character(name="avg_213_mostma_1#1$1")]
[name="莫斯提马"]所以，现在，我会用眼睛观察，用心判断。
[character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"]那边的小姑娘，是叫塞茜莉亚对吧？
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]姐姐，你有角，也有光环......你是萨科塔吗？
[character(name="avg_213_mostma_1#5$1")]
[name="莫斯提马"]啊，可能算是？不过我也不太确定呢。
[character(name="avg_213_mostma_1#1$1")]
[name="莫斯提马"]听着，艾泽尔，带塞茜莉亚过来。她不会有事。
[character(name="avg_4036_forcer_1#6$1")]
[name="艾泽尔"]......一个堕天使的承诺......
[character(name="avg_213_mostma_1#7$1")]
[name="莫斯提马"]总比那个凶巴巴的黎博利更可信吧。
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]喂！你说的是对面那个对吧！
[Character(name="avg_npc_357_1#5$1")]
[name="帕蒂亚"]......
[dialog]
[character]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.3, xstrength=5, ystrength=8, vibrato=30, randomness=90, blo

... (全文22063字符)
```

### level_act16side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g9_laterano_street",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[character(name="avg_npc_366_1#1$1")]
[name="笑呵呵的邻居"]呀，艾泽尔，早上好！去上班？
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]早上好，今天......不上班，我休假了。
[character(name="avg_npc_366_1#1$1")]
[name="笑呵呵的邻居"]休假起这么早？还愁眉苦脸的，有什么烦心事？是不是在公证所被欺负了？
[name="笑呵呵的邻居"]我以前就跟你说，在那里上班看起来很体面，实际上很惨的啦！
[character(name="avg_4036_forcer_1#8$1")]
[name="艾泽尔"]哈哈哈......
[character(name="avg_npc_366_1#1$1")]
[name="笑呵呵的邻居"]来，艾泽尔，我刚买的杯子蛋糕，你拿去吃吧，别想那么多了！
[name="笑呵呵的邻居"]公证所的事再怎么麻烦，也只是份工作而已，下班了就别想啦！你不是还在实训吗，天塌下来有高个子顶着，别为难自己啦！
[name="笑呵呵的邻居"]开心点，别这么无精打采的，不值得不值得！
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]不值得吗......
[character(name="avg_npc_366_1#1$1")]
[name="笑呵呵的邻居"]还在想呢......哈哈，那我先走啦。
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]谢谢你的蛋糕。
[character]
一个再普通不过的清晨，大街上行人还稀少。
不过，再有一会儿，就会变成平常的样子了吧，热热闹闹，吵吵嚷嚷。
拉特兰人的生活......不就是这样。
[dialog]
[delay(time=1)]
[name="？？？"]要不要来个可丽饼？
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]谢谢，不用了......蛋糕还......
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]是你？！
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_351_1#7$1",fadetime=1,block=true)]
[delay(time=1)]
[name="安多恩"]那边街角的可丽饼店，招牌口味每天限量两百份，要早起才能买到。
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]好在开门时间这么多年都没变。
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]......你在这里干什么？
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]散步。
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]在一座通缉你的城市？
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]没关系。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]......安魂教堂那些人怎么样了？
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]他们都在安全的地方，等到事情了结，他们会和我一起离开拉特兰。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]去哪里？
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"]谁知道呢。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]......你们会带塞茜莉亚一起走吗？
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]不，她离开了。
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]......？！
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]你，怎么会......？
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]她有自己的事要做。也许现在还只是一件小事......
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]但她找到了自己的路，就会一直走下去，穿过我们无法跨越的荆棘，走出我们不敢踏入的困境，走到我们想象不到的远方。
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]......这是什么意思？
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"]放心吧，艾泽尔兄弟，她比我们都了不起。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]但她也许需要你。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]......我只是个普通人。
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]说起来挺丢脸的。虽然我之前一直在塞茜莉亚面前逞英雄，说什么答应了就一定会做到，丢了工作也无所谓......
[name="艾泽尔"]但昨天回家之后，我后怕了一夜。
[name="艾泽尔"]混血萨科塔、堕天使、万国信使、大教堂的会议、萨卡兹、奇怪的异端组织......
[name="艾泽尔"]我怎么会和这些事情扯上关系的？
[character(name="avg_4036_forcer_1#7$1")]
[name="艾泽尔"]我原本只是想要一份体面的工作，最好能分到文职岗，按时上班，到点下班，安安稳稳度过一生......不是很好吗？
[character(name="avg_4036_forcer_1#7$1")]
[name="艾泽尔"]这几天的一切只不过是个插曲，能及时抽身难道不算我运气好？几十年之后再拿出来和朋友吹嘘......
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]这样不就行了吗？
[character(name="avg_4036_forcer_1#6$1")]
[name="艾泽尔"]......也许我现在也不该和你说话，我该转身就走的。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]不走吗？
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]何必骗自己。
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]......我该怎么知道，什么才是我真正想要的？
[character(name="avg_npc_351_1#3$1")]
[name="安多恩"]你和塞茜莉亚问了一样的问题。
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]......她也这么问了吗？
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]措辞不同而已。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]那你是怎么回答的？
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]我给她讲了个故事。
[character(name="avg_4036_forcer_1#6$1")]
[name="艾泽尔"]......突然不是很想听。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]为什么？
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]......总觉得你太会影响人了。我又怎么知道是不是被你蛊惑了......
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]只要你不想，就不会的。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]听起来不太对劲......
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]其实我只是来带个口信。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]之后如何，全凭你自己。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]塞茜莉亚去了老钟楼。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]......她去那里做什么？
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]道别。
[dialog]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Background(image="26_g11_laterano_alley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]......
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]您有什么事吗？
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_355_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="奥伦"]啊呀，塞茜莉亚，大清早一个人走在街上，不害怕吗？
[character(name="avg_npc_355_1#4$1")]
[name="奥伦"]你的那些哥哥姐姐们呢？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="26_g10_laterano_roof",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_transmissionget")]
[delay(time=1)]
[Character(name="avg_npc_357_1#6$1")]
[name="帕蒂亚"]先导，是奥伦。
[character]
[dialog]
[name="安多恩"]没关系，看看他的打算。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g11_laterano_alley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]我有自己要做的事。
[character(name="avg_npc_355_1#1$

... (全文15554字符)
```

### level_act16side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$d_avg_footstep_stonestep", volume=1)]
[Subtitle(text="钟楼的过道很狭窄，脚下的石阶又湿又滑。石头墙壁很粗糙，摸上去凉凉的......就像那片森林里的树。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="脚步声回荡在走廊里，前面会有什么？", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="我是萨科塔和萨卡兹的孩子，他们说，我身上寄托着......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="我不知道，那是我没有听过的音节。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="但我记得罗塞菈姐姐的表情。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="她双眼低垂，带着一点笑容，两手交叠在一起，仿佛掌中有什么宝物。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="他们......大家，希望我做什么呢？到现在，我也没明白。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="但是，我已经明白了，最应该去做的事情，是自己想要做的事。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="萨科塔也好，萨卡兹也好。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="我是塞茜莉亚。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="只是塞茜莉亚。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="再见，妈妈......你会看着我吗？", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g11_laterano_alley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[delay(time=2)]
[character(name="char_279_excu_4")]
[name="费德里科"]艾泽尔，左前方。
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]唔！
[dialog]
[character]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=3, block=false)]
[delay(time=1)]
[character(name="avg_4036_forcer_1#2$1",fadetime=1,block=true)]
[delay(time=1)]
[name="艾泽尔"]好险！
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]我说，咱们也打不出个结果，要不然算了吧？
[dialog]
[character]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="char_279_excu_4",name2="avg_npc_355_1#1$1",enter="left",fadetime=0.7,block=true)]
[CameraShake(duration=0.4, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[characteraction(name="left", type="move", xpos=100, power=0, times=1, fadetime=0.1, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="move", xpos=-30, power=0, times=1, fadetime=1, block=false)]
[characteraction(name="right", type="move", xpos=80, power=0, times=1, fadetime=1, block=true)]
[CameraShake(duration=0.4, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[delay(time=1)]
[character(name="avg_npc_355_1#5$1")]
[name="奥伦"]......真是完全不听人说话啊。
[character(name="avg_npc_355_1#4$1")]
[name="奥伦"]艾泽尔，你不是最担心塞茜莉亚的安危吗？其实说不定塞茜莉亚在我手里会更安全哦？
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]你以为我会相信吗？
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]我从来不说假话的。
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]就算你说的是真的，塞茜莉亚自己不愿意，那就不行！
[character(name="avg_npc_355_1#5$1")]
[name="奥伦"]......有时候我真觉得，安多恩给我添了很多麻烦。
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]！！
[character(name="char_279_excu_4")]
[name="费德里科"]不要分神，艾泽尔。
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]不......费德里科前辈！
[character(name="avg_4036_forcer_1#2$1")]
[name="艾泽尔"]你有没有感觉到......
[character(name="avg_npc_355_1#3$1")]
[name="奥伦"]这是......
[stopmusic(fadetime=2)]
[character]
[dialog]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="空气在颤动。", x=300, y=370, alignment="middle", size=24, delay=0.04, width=700)]
[Subtitle(text="仿佛有某种东西正从虚无中析出。", x=300, y=370, alignment="middle", size=24, delay=0.04, width=700)]
[Subtitle(text="那是一股强大而纯净的力量，却不像是任何已知的源石技艺。", x=300, y=370, alignment="middle", size=24, delay=0.04, width=700)]
[Subtitle(text="某种古老的结构正被唤醒。", x=300, y=370, alignment="middle", size=24, delay=0.04, width=700)]
[Subtitle(text="某种遗忘的声音将要鸣响。", x=300, y=370, alignment="middle", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="char_279_excu_4")]
[name="费德里科"]艾泽尔，行动变更，你去钟楼确认情况。
[character(name="char_279_excu_4")]
[name="费德里科"]这个反叛信使交给我。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_361_1#4$1")]
[name="薇尔丽芙"]教宗阁下，这是！
[Character(name="avg_npc_356_1#1$1")]
[name="教宗"]嘘——
[Characte

... (全文18451字符)
```

### level_act16side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[Dialog]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g11_laterano_alley",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_355_1#1$1")]
[delay(time=1)]
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=1)]
[Character(name="char_279_excu_4")]
[delay(time=1)]
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="26_g9_laterano_street",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_366_1#1$1")]
[name="喜悦的拉特兰市民"]感觉城里好热闹啊，是因为会议要开幕了吗？
[Character(name="avg_npc_368_1#1$1")]
[name="悠哉的拉特兰市民"]可能是吧，好多地方都在爆炸，看来大家都很兴奋嘛。
[dialog]
[Character(name="avg_npc_355_1#1$1")]
[CameraShake(duration=0.9, ystrength=20, vibrato=30, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown2",volume=0.8)] 
[Delay(time=1)]
[Character(name="avg_npc_366_1#1$1")]
[name="喜悦的拉特兰市民"]谁啊！
[Character(name="char_279_excu_4")]
[name="费德里科"]......
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=2)]
[Character(name="avg_npc_368_1#1$1")]
[name="悠哉的拉特兰市民"]那是......一个执行者，一个万国信使？！
[Character(name="avg_npc_366_1#1$1")]
[name="喜悦的拉特兰市民"]这是在干啥，跑酷比赛？
[Character(name="avg_npc_368_1#1$1")]
[name="悠哉的拉特兰市民"]这么热闹？你玩不玩？
[Character(name="avg_npc_366_1#1$1")]
[name="喜悦的拉特兰市民"]走呗！看看追不追得上！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g10_laterano_roof",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]到这里应该......
[dialog]
[character]
[PlaySound(key="$grenade_launcher_shot", volume=1)]
[CameraShake(duration=0.4, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[delay(time=0.51)]
[Character(name="avg_npc_355_1#6$1")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=0.4, xstrength=0, ystrength=0, vibrato=0, randomness=0, fadeout=true, block=true)]
[dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[delay(time=2)]
[Character(name="char_279_excu_4",fadetime=1)]
[delay(time=2)]
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]唉，真是难缠啊，费德里科。
[Character(name="char_279_excu_4")]
[name="费德里科"]你也很难缠。
[Character(name="avg_npc_355_1#2$1")]
[name="奥伦"]我调查过，你现在应该没有任务在身......你根本就休假了啊？！
[Character(name="avg_npc_355_1#2$1")]
[name="奥伦"]我真是搞不懂了，你咬着我不放做什么？我什么时候得罪你了吗？
[Character(name="char_279_excu_4")]
[name="费德里科"]我的上一项任务，是前往叙拉古将一位当地萨科塔的遗物送回拉特兰。
[Character(name="char_279_excu_4")]
[name="费德里科"]他的遗物中有一本笔记，记载了他曾经目睹一名女性萨科塔与萨卡兹接触。
[Character(name="avg_npc_355_1#7$1")]
[name="奥伦"]行吧，那你要查也正常。但是关我什么事？我是男的哦？
[Character(name="char_279_excu_4")]
[name="费德里科"]我追溯各种线索，最终找到这名女性的住址是拉特兰城司提望区瑟法斯街7-265号。
[Character(name="avg_npc_355_1#2$1")]
[name="奥伦"]......
[Character(name="avg_npc_355_1#2$1")]
[name="奥伦"]你到达那里时，发现她已经去世了。
[Character(name="char_279_excu_4")]
[name="费德里科"]不错。
[Character(name="avg_npc_355_1#2$1")]
[name="奥伦"]......你只好继续调查她的行踪记录，然后发现她有一些可疑的出行，而每一次这种可疑的出行之前，她都和我这个万国信使有过联络......
[Character(name="avg_npc_355_1#4$1")]
[name="奥伦"]哈哈哈哈哈！有意思，太有意思了！
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]我还想是我在维多利亚露了马脚？或者哪一次和安多恩联络留了痕迹？没想到竟然是因为好心帮费莉亚的这一点小忙......
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]也可谓是命运的一种了。
[Character(name="char_279_excu_4")]
[name="费德里科"]感慨完了吗？
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]唉，费德里科，如果我没猜错，你现在应该无法感知我的情绪吧？
[Character(name="char_279_excu_4")]
[name="费德里科"]不能，我也不在乎。
[Character(name="char_279_excu_4")]
[name="费德里科"]缉捕对象的情绪与我无关。
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]不是你缉捕对象的人，他们的情绪你就在乎吗？
[Character(name="char_279_excu_4")]
[name="费德里科"]......不。
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]你和我一样，我们都多少拒绝了共感......依我看，我们大可以交个朋友啊。
[name="奥伦"]其实我觉得，拉特兰是应该多一点你这样的人。
[name="奥伦"]不要那么同情心泛滥，单纯以法规为准则行动。
[Character(name="char_279_excu_4")]
[name="费德里科"]我不反对这个观点。或许等你的审判结束后，我可以到监狱里和你交流。
[character]
[name="？？？"]所以，这就是你的理由，奥伦？
[Character(name="avg_npc_355_1#6$1")]
[name="奥伦"]......最麻烦的家伙出现了。我这样日行一善的人为什么会倒霉成这样......
[Character(name="char_279_excu_4")]
[name="费德里科"]枢机薇尔丽芙，你好。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_361_1#5$1",fadetime=1,block=true)]
[delay(time=1)]
[name="薇尔丽芙"]你好，执行者费德里科。
[Character(name="avg_npc_361_1#1$1")]
[name="薇尔丽芙"]叛徒奥伦的处置接下来移交第七厅，公证所方面可以转项结案了，你关于此事的报告麻烦抄送第七厅、第一厅。
[Character(name="avg_npc_361_1#1$1")]
[name="薇尔丽芙"]这是我的认证码。
[Character(name="char_279_excu_4")]
[name="费德里科"]确认完毕，程序合规。
[Character(name="avg_npc_361_1#1$1")]
[name="薇尔丽芙"]然后，你想继续休假还是临时参与迷途者缉捕行动？随你高兴。
[dialog]
[Character(name="char_279_excu_4")]
[delay(time=0.51)]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=2)]
[Character(name="avg_npc_355_1#2$1")]
[name="奥伦"]薇尔，你说，有人听过费德里科说再见吗？
[Character(name="avg_npc_361_1#3$1")]
[name="薇尔丽芙"]别套近乎。
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]你不是来帮我的吗？
[Character(name="avg_npc_355_1#1$1")]
[name="奥伦"]如果你想把我绳之以法，只要等费德里科干完他的活儿就行了，不是吗？
[Character(name="avg

... (全文11342字符)
```

### level_act16side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g11_laterano_alley",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_sp_ballista",volume=1.0)]
[CameraShake(duration=2,xstrength=5,ystrength=3,vibrato=30,randomness=90,fadeout=true,block=false)]
[Blocker(a=1, r=100, g=100, b=100, fadetime=0.1,block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=false)]
[delay(time=3)]
[Character(name="avg_npc_357_1#6$1")]
[name="帕蒂亚"]唔呃......
[Character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]......
[Character(name="avg_300_phenxi_1#8$1")]
[name="菲亚梅塔"]够了，帕蒂亚。
[Character(name="avg_npc_357_1#6$1")]
[name="帕蒂亚"]还......没......
[Character(name="avg_213_mostma_1#10$2")]
[name="莫斯提马"]你叫帕蒂亚，对吗？
[Character(name="avg_213_mostma_1#10$2")]
[name="莫斯提马"]大部分铳骑都已经调到使节区了。你的任务已经完成了。
[Character(name="avg_npc_357_1#2$1")]
[name="帕蒂亚"]......
[dialog]
[playsound(key="$bodyfalldown2",volume=0.4)]
[character(fadetime=1,block=true)]
[delay(time=2)]
[stopmusic(fadetime=2)]
[Character(name="avg_213_mostma_1#1$2")]
[name="莫斯提马"]其实我是不明白啦，安多恩又不是不知道大教堂里最强的究竟是谁......耍这些花招有什么意义？
[Character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]......他只是要确保能见到阁下吧。
[Character(name="avg_213_mostma_1#4$2")]
[name="莫斯提马"]嗯？蕾缪安说的那些，你真听进去了？
[Character(name="avg_300_phenxi_1#8$1")]
[name="菲亚梅塔"]两码事。
[name="菲亚梅塔"]他可以去结清他的账。
[name="菲亚梅塔"]不等于我就会放过他。
[Character(name="avg_213_mostma_1#10$2")]
[name="莫斯提马"]没问题。那走？
[Character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]......先把帕蒂亚安置好。
[Character(name="avg_213_mostma_1#7$2")]
[name="莫斯提马"]哟。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g2_laterano_cathedralhall",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=2)]	
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Character(name="avg_npc_356_1#2$1")]
[name="教宗"]我们该如何面对启示？那些神秘莫测、不可言说的时刻；那些模棱两可、亟待阐释的冲动；那些无法归因、晦涩难言的直觉......
[name="教宗"]它要把我们引向何方？它想让我们做何选择？抑或，这不过是生存的疲乏带来的幻觉？
[name="教宗"]但启示被称为启示。只因为我们愿意相信，或被告知要相信。
[name="教宗"]甚至，就算我们明知其中并无任何超脱常理之处，即使我们已能够将其分解为冰冷的逻辑或客观的自然......
[name="教宗"]可叹的世人们啊，依旧会为“启示”覆上一层属灵的光。
[character]
[name="？？？"]如此，当面对现实的残酷，怯懦者可以责怪启示的暧昧，虔信者可以愧悔领悟的偏差，无论如何，至少可以笃定一切并非自己所致。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_351_1#1$1",fadetime=1,block=true)]
[delay(time=2)]
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]安多恩，你来了。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]你似乎并不意外。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]我不会将这称为某种指引的结果。生活给我的最大教训就是，人们总会相遇，无论本意为何。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]但终归各怀目的。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]至高律法的看守者、监督者、践行者。
[name="安多恩"]承袭了拥有牺牲与团结美德的伊万杰利斯塔之名的第十一世圣徒，立于拉特兰圣迹顶点的教宗阁下。
[Character(name="avg_npc_356_1#1$1")]
[name="伊万杰利斯塔十一世"]何必背诵你不相信的礼辞？
[Character(name="avg_npc_356_1#1$1")]
[name="伊万杰利斯塔十一世"]那个女孩没有留在你们之中。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]她还小，还有许多事要经历。
[Character(name="avg_npc_356_1#2$1")]
[name="伊万杰利斯塔十一世"]我们却已经老了，老到娴熟于阴谋、权术、挑拨和倾轧。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]你打算怎么办，好好对她使用一番这些岁月的礼物吗？
[Character(name="avg_npc_356_1#2$1")]
[name="伊万杰利斯塔十一世"]我还没有糊涂到去挡一个小女孩的路。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]就算她引发了某种“奇迹”？
[Character(name="avg_npc_356_1#1$1")]
[name="伊万杰利斯塔十一世"]不，奇迹属于拉特兰，奇迹只属于拉特兰。恩典降临了，仅此而已。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="26_g3_laterano_cathedralballroom",screenadapt="showall")]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_356_1#10$1")]
[name="伊万杰利斯塔十一世"]你喜欢读历史吗？我相当喜欢。历史要成为历史，通常需要一个原点，混杂一些变量，再激起阵阵涟漪——那些涟漪就是历史。
[name="伊万杰利斯塔十一世"]至于最初投进水中的是什么，也许历史并不在乎。
[name="伊万杰利斯塔十一世"]我也不在乎。
[name="伊万杰利斯塔十一世"]名叫塞茜莉亚的女孩会去到她想去的地方，做她想做的事，将来的某天，塞茜莉亚这个名字可能会大放异彩——也可能默默无闻。
[name="伊万杰利斯塔十一世"]但这些，与你我无关了。
[Character(name="avg_npc_356_1#1$1")]
[name="伊万杰利斯塔十一世"]与你我无关，这是我们的共识，对吗？
[character(name="avg_npc_351_1#5$1")]
[name="安多恩"]......你把自己描述得像是送孙女出门的温柔爷爷。
[name="安多恩"]算了吧，这只是各取所需。你掌握了奇迹的解释权，以此为代价，塞茜莉亚换得离开这里的自由。
[character(name="avg_npc_351_1#5$1")]
[name="安多恩"]这甚至不能算是一场交易，她根本没得选。
[Character(name="avg_npc_356_1#1$1")]
[name="伊万杰利斯塔十一世"]不，我从没打算对她做些什么。矗立数千年的拉特兰不应、不会，也不可能因一个混血儿动摇。
[character(name="avg_npc_351_1#5$1")]
[name="安多恩"]愿你的前任和继任们也都这么想，愿那些被抹去的名字不是白白消亡。
[Character(name="avg_npc_356_1#1$1")]
[name="伊万杰利斯塔十一世"]我们无法奢求得太多，安多恩。罪孽永远都是罪孽。只是时间会将它冲刷得淡漠。
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]淡漠到所有人都忘了这曾是罪孽。
[Character(name="avg_npc_356_1#2$1")]
[name="伊万杰利斯塔十一世"]我无法责怪前人的谨慎。不过，我也不会为了掩盖而把罪孽化为成规。
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]前提是你口中的那个“共识”，对吧？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="showall")]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_356_1#9$1")]
[name="伊万杰利斯塔十一世"]嘿，所以说，变老是一件很无聊的事。经历过的事情让我们畏首畏尾，瞻前顾后。
[Character(name="avg_npc_356_1#9$1")]
[name="伊万杰利斯塔十一世"]老人没有可能性，安多恩。我们只能沿着已有的道路往前走。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]已有的道路......
[Character(name="avg_npc_356_1#10$1")]
[name="伊万杰利斯塔十一世"]你也是一样，安多恩。我知晓你的跋涉。
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]跋涉啊......
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"]是啊，我曾跋涉......聆听最纯洁的祈祷，也听闻最恶毒的诅咒。
[name="安多恩"]我踏入豪奢的宫殿，也将靴子从血污中拔出。
[name="安多恩"]我见无耻的罪人痛哭请求宽恕，也为无辜的孩子合上简陋的棺材。
[name="安多恩"]总是如此。他们的呐喊归于沉寂，他们的泪水一再干涸。而我，我总是站在他们身旁，一再试图安慰。
[name="安多恩"]我说得救终会来临，只要我

... (全文18360字符)
```

### level_act16side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Delay(time=1)]
[Subtitle(text="那是一个伊比利亚的小镇，无论在地图抑或史书，如今你找不到它的名字。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="在还有人生活的时候，那里叫做潮石镇。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="潮石镇的主教抚养了一名年幼的萨科塔。一个萨科塔......在这里成长，在这里学习，度过一生中最美好的岁月。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="这里朴素而贫瘠，但虔诚的生活原本不需要太多。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="只是在大静谧后的伊比利亚，人付出再多努力，生活永远易碎。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="一次瘟疫，一次饥荒，一次早有预谋的渗透，就足以击垮一切。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="为了拯救不是故乡的故乡，萨科塔来到圣城拉特兰，请求一些微不足道的支援。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="他得到的回答很简单：你是我们的一员，他们不是。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="待萨科塔回归伊比利亚，那个“故乡”已然无存。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="甚至一切都被抹去，抚平，仿佛从未存在过。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="像一粒沙消失在沙漠里，一滴水消融于浪潮中。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="萨科塔经历漫长的旅程，又回到拉特兰，形销骨立，宛若游魂。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="他往一座礼拜堂求访获封圣贤的主教，寻求解惑与引导。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="纵是圣贤，面对这许多质疑，也只能沉默。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="他坐在长椅上，坐在那里，从清晨到黄昏。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="菲亚梅塔，那就是我第一次见到安多恩。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[stopmusic(fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]	
[playMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Character(name="avg_npc_356_1#2$1",fadetime=1)]
[delay(time=1)]
[name="教宗"]唉。
[Character(name="avg_npc_356_1#6$1")]
[name="教宗"]算了，自掏腰包吧，这里的维修费用很贵的。
[Character(name="avg_npc_356_1#6$1")]
[name="教宗"]下午茶的甜点往后只能减半了。
[dialog]
[character]
[playsound(key="$rungeneral")]
[character(name="avg_npc_358_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="教宗骑士"]教宗阁下！我听到大教堂方向传来战斗声，您没事吧！
[character(name="avg_npc_358_1#1$1")]
[name="教宗骑士"]这是......？！是异端袭击了您吗？......这是我的失职！
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]别这么紧张，保拉里奥，还记得上次大教堂掰腕比赛的冠军是谁吗？
[character(name="avg_npc_358_1#1$1")]
[name="教宗骑士"]......是您。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]我只是稍微活动了一下手腕，不小心搞出了一点小意外而已。
[Character(name="avg_npc_356_1#1$1")]
[name="教宗"]城内的骚乱已经平息了。
[character(name="avg_npc_358_1#1$1")]
[name="教宗骑士"]是的，他们撤退了。我都还没来得及炸爽——
[dialog]
[character]
[playsound(key="$doorknockquite")]
[delay(time=1)]
[name="？？？"]请问可以进来吗？
[character(name="avg_npc_358_1#1$1")]
[name="教宗骑士"]咳咳，抱歉，教宗阁下，我失态了。
[name="教宗骑士"]我是说，您要找的人已经到了。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]请进吧，孩子们。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_4036_forcer_1#1$1",name2="avg_npc_352_1#1$1",fadetime=1,block=true)]
[delay(time=2)]
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]教宗阁下，向您致敬......
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]教宗阁下，您好，我是塞茜莉亚。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]啊，欢迎，这里有点乱。
[Character(name="avg_npc_356_1#1$1")]
[name="教宗"]你们......
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]喝茶一般配什么甜点？
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[delay(time=1)]
[dialog]
[Background(image="26_g4_laterano_cathedralliving",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[character(name="avg_npc_352_1#2$1")]
[name="塞茜莉亚"]您......需要我做什么？
[Character(name="avg_npc_356_1#8$1")]
[name="教宗"]嗯，让我想想......
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]往自己的茶杯里加块方糖？
[Character(name="avg_npc_356_1#9$1")]
[name="教宗"]艾泽尔，你得多加几块，糖分能舒缓紧张。
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]啊！好、好的......
[character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]教宗阁下，如果我......想要离开拉特兰，您会同意吗？
[Character(name="avg_npc_356_1#9$1")]
[name="教宗"]如果我不允许，你会服从吗？
[character(name="avg_npc_352_1#9$1")]
[name="塞茜莉亚"]可能不会。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]那就去吧。
[character(name="avg_4036_forcer_1#3$1")]
[name="艾泽尔"]......教宗阁下？
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]我只是个可怜的老头子，最大的愿望就是窝在软乎乎的摇椅里安度晚年，哪有工夫去管小女孩的旅行计划呢？
[character(name="avg_4036_forcer_1#9$1")]
[name="艾泽尔"]可塞茜莉亚是......
[Character(name="avg_npc_356_1#1$1")]
[name="教宗"]是什么？难不成她还能是天使和魔鬼的混血，让启示降临的圣徒？
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]塞茜莉亚只是个想要出门看看的小姑娘，对不对？
[character(name="avg_4036_forcer_1#5$1")]
[name="艾泽尔"]......
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]你还带着你妈妈的守护铳，是吗？
[character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]啊，对不起！我是不是应该交给艾泽尔哥哥......
[character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]只是......
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]没关系，孩子。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]获得守护铳是一件庄严的事，原本得举行隆重的仪式，需要监护人出席，导师的首肯，还有一大堆麻烦的文书工作......
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]不过，你也没到可以获得守护铳的年纪。所以，悄悄地把它带走吧。
[character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]真的可以吗？
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]我不敢说这是给你的礼物。每一把铳都是拉特兰的宝贵财富。
[Character(name="avg_npc_356_1#10$1")]
[name="教宗"]不过，若只是孩子思念母亲的寄托，我相

... (全文15842字符)
```

### level_act16side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="26_g10_laterano_roof",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"]执念，是吗。
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]这是你的执念......
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]就是执念，有什么不可以？
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]没有道理也好，于事无补也好，徒劳无功也好，我打定了主意要做，我就会去做！
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]你以为我们是为了什么战斗？
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]你以为你念的那些经，那些让人发昏的长篇大论，把你自己都绕得云里雾里的胡话——不是你的执念吗？
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]你，我，每个人，谁不是为了执念站在这里？
[dialog]
[character]
[playsound(key="$p_atk_rifle_s")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.3, block=true)]
[Character]
[Image(image="26_i14",xScale=1, yScale=1)]
[ImageTween(xScaleTo=0.8, yScaleTo=0.8, duration=20, block=false)]
[PlaySound(key="$swordtsing1", volume=1)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[dialog]
铳响破空而来。
只是瞄准的对象并非安多恩。
猝不及防，他感到手中的铳脱手而去。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image]
[Blocker(a=0, fadetime=1, block=true)]
他突然觉得这样很好。
他的铳会留在拉特兰。
或许他永远不会说，但是——谁能不喜爱拉特兰？
那些安宁的日子、喜悦的时光、快乐的瞬间......
为了这份“喜爱”，他曾愧悔，负疚，羞耻，怀疑。
或许他永远没办法做一个天生的拉特兰人。
但在这一刻，当想到他的铳将会留在这里，在这个念头冒出来的一刻。
在面前的人怒视他的这一瞬。
那种安宁又如气泡一般浮出水面，小小地炸开一朵几不可见的水花。
他曾经在信与疑的道路上跋涉万里。
离开这一条路，再离开下一条路。
他以为他行于荒野，失去自己的根系。
但也许并非如此。
在许多事情上，都并非如此。
他轻轻道了一声感谢。
过往未来，时间与空间的所有历史中，没有人会听到这声感谢。
但已经足够。
[dialog]
[Delay(time=1)]
[character(name="avg_213_mostma_1#7$1")]
[name="莫斯提马"]终于来了吗，我还以为你睡着了。
[dialog]
[character]
[playsound(key="$d_gen_transmissionget")]
[delay(time=1)]
[name="蕾缪安"]体谅体谅我吧，合适的狙击位置很难找的。
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]行了，安多恩，束手......
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"] （低声）为了执念......站在这里......
[character(name="avg_213_mostma_1#3$1")]
[name="莫斯提马"]小心！
[character]
[dialog]
[character(name="avg_npc_351_1#6$1")]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_originiumcast", volume=1)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=3, block=false)]
[delay(time=1)]
[character]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[dialog]
[Delay(time=1)]
[character(name="avg_213_mostma_1#3$1")]
[name="莫斯提马"]他怎么还有余力释放源石技艺！
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]......一个人，如何可能得救。
[name="安多恩"]不，不是得救，而是人如何可能尊严地生存......
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]你因心中的公义站在我面前，我因心中的公义跋涉至此地。
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]归结于迷思，归结于执着，归结于最终无望的泅渡......这条路，其实早已在我脚下延伸......
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]为何寄希望于得救呢？我们所做的一切，不是为了得救......
[character(name="avg_npc_351_1#8$1")]
[name="安多恩"]而是为了有资格成为自己的拯救者。
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]清醒了，安多恩？那就抬起头直面我——刚才的战斗简直是在向一截木桩挥拳。
[character(name="avg_npc_351_1#2$1")]
[name="安多恩"]我将行我的道。不论这是不是它赋予我的使命......
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]我也要谢谢你，菲亚梅塔。
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]不客气，在你的葬礼上，我会把你的大彻大悟转告给你那些朋友们的。
[character(name="avg_300_phenxi_1#7$1")]
[name="菲亚梅塔"]至于现在，你还是——
[character]
[name="？？？"]可惜可惜，现在还不是时候，这家伙对我还有用呢。
[dialog]
[PlaySound(key="$grenade_launcher_shot")]
[delay(time=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$grenade_explosion")]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=0.51)]
[CameraShake(duration=2, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_rockfall")]
[Delay(time=1)]
[character(name="avg_213_mostma_1#4$1")]
[name="莫斯提马"]这里的承重梁被炸塌了，菲亚梅塔，走！
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]谁......！
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_355_1#4$1",fadetime=1,block=true)]
[delay(time=1)]
[name="奥伦"]这次爆炸是合规的，我刚刚亲自提交的申请，亲手盖的章。
[character(name="avg_300_phenxi_1#2$1")]
[name="菲亚梅塔"]奥伦，你！
[dialog]
[character]
[character(name="avg_npc_361_1#5$1",fadetime=1,block=true)]
[delay(time=1)]
[name="薇尔丽芙"]奥伦，在干什么呢？你为我效力，就是来干这个的吗？
[character(name="avg_npc_355_1#1$1")]
[name="奥伦"]......发现得也太快了......
[character(name="avg_npc_355_1#3$1")]
[name="奥伦"]（安多恩，你先走吧，我之后找你。）
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]......
[character(name="avg_npc_351_1#1$1")]
[name="安多恩"]菲亚梅塔，莫斯提马，我们或许还会再见面......
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]无论在哪里相会，希望我们都依然紧攥住那一点执念。
[character(name="avg_npc_351_1#6$1")]
[name="安多恩"]正如你说的，我们因这些执念而存在。
[dialog]
[character]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=255, g=255,

... (全文11586字符)
```

### level_act16side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] st01
[stopmusic]
[Dialog]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Image(image="26_i07", fadetime=2,xScale=1, yScale=1,x=-150,y=-40)]
[ImageTween(xScale=1, yScale=1, duration=60,xTo=130, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[delay(time=2)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="男人踏进房间。轮椅上的女人未发一言。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=2)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="他整理了桌面上散乱的笔记和纸张。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="将花瓶中枯死的花替换为新鲜的花。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=2)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="她在读一本新借的书，仿佛看不见另一个人的身影。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=2)]
[dialog]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="沉默。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="也许是因为该说的话早已说过。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="不该说的话，还未到时候。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="26_i07",xScale=0.8, yScale=0.8)]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="男人忽然开口。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="消瘦的男人"]她快回来了。
[dialog]
[delay(time=1)]
[name="沉静的女人"]万国信使们筹备已久的会议，她当然会回来。
[name="沉静的女人"]你打算待多久？
[dialog]
[delay(time=2)]
[name="消瘦的男人"]等到该做的事情做完。
[name="消瘦的男人"]毕竟我在这里，只能引渡拉特兰人的灵魂。
[dialog]
[delay(time=2)]
[name="消瘦的男人"]......
[name="消瘦的男人"]我该走了。
[name="沉静的女人"]明天开始，别再来了。
[dialog]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="男人默立片刻，转身离开了房间。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Image(fadetime=2)]
[Delay(time=4)]
[Subtitle(text="女人摇着轮椅来到窗边。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="她打开窗户，看向窗外。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="透过这扇窗户，她看过拉特兰城无数的日夜。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="今夜的拉特兰城一如既往地喧闹，拉特兰人从不知安静与疲倦为何物。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="明天之后呢？", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle]
[Dialog]
[stopmusic(fadetime=4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=4, block=true)]
[Character]
[Delay(time=2)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Background(image="26_g8_laterano_dwelling",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]	
[Character(name="avg_npc_352_1#1$1",fadetime=1,block=true)]
[delay(time=1)]
[name="塞茜莉亚"]妈妈，喝热水。
[Character]
[name="病重的母亲"]好孩子，咳咳......妈妈没事。
[Character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]妈妈......我给你读故事书吧。
[Character]
[name="病重的母亲"]......塞茜莉亚，我可爱的塞茜莉亚。
[name="病重的母亲"]妈妈真舍不得离开你。
[Character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]妈妈要离开我吗？
[Character]
[name="病重的母亲"]不，咳咳......妈妈从来没有想过......离开你......
[name="病重的母亲"]妈妈只是不得不......
[Character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]妈妈要去哪儿？我也一起去，可以吗？
[Character]
[name="病重的母亲"]妈妈要去的地方，塞茜莉亚不能去......那里很冷，很寂寞，什么都没有。
[Character(name="avg_npc_352_1#10$1")]
[name="塞茜莉亚"]我和妈妈一起，我陪着妈妈，妈妈就不会寂寞了。
[Character]
[name="病重的母亲"]......塞茜莉亚，对不起。
[name="病重的母亲"]你本应该有更幸福的童年......
[Character(name="avg_npc_352_1#4$1")]
[name="塞茜莉亚"]我和妈妈在一起，非常幸福。
[Character]
[name="病重的母亲"]......塞茜莉亚，塞茜莉亚，听着，听着。
[Character(name="avg_npc_352_1#1$1")]
[name="塞茜莉亚"]妈妈，我在。
[Character]
[name="病重的母亲"]之后，妈妈不能照顾你了......会有人来接你。
[name="病重的母亲"]跟着他，跟着他去找爸爸。
[name="病重的母亲"]爸爸会代替妈妈照顾你，好吗？
[Character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]妈妈不和我一起去见爸爸吗？爸爸一定也想要见妈妈......
[Character]
[name="病重的母亲"]妈妈......要去做重要的事情......所以不能和你一起去。
[name="病重的母亲"]等你见到爸爸，替妈妈告诉他，妈妈也很想他。
[name="病重的母亲"]还有，替我对他说......对不起。好吗？
[Character(name="avg_npc_352_1#12$1")]
[name="塞茜莉亚"]妈妈为什么要道歉？
[Character]
[name="病重的母亲"]答应我，答应妈妈，塞茜莉亚！
[Character(name="avg_npc_352_1#7$1")]
[name="塞茜莉亚"]我知道了，妈妈......妈妈，别哭......
[Character]
[name="病重的母亲"]塞茜莉亚，我可怜的塞茜莉亚......你的出生是我一生中最幸福的事。可是，这会不会成为你一生的不幸......我的孩子，我最心爱的......
[name="病重的母亲"]谁将祝福你？谁能祝福你？
[name="病重的母亲"]塞茜莉亚，我的塞茜莉亚，躲起来，不要被发现......
[name="病重的母亲"]逃走吧......离开拉特兰......
[Dialog]
[Character]
[delay(time=1)]
母亲抓住女儿的手，眸中闪过无数情绪。最终，一切都从眼中无力地流逝。
那双眼睛缓缓阖上。
[Character(name="avg_npc_352_1#5$1")]
[name="塞茜莉亚"]妈妈......？
[Dialog]
[Character]
萨科塔女孩不知道发生了什么。
她发现母亲的手变凉了，于是捧起来捂在胸前，希望母亲能够暖和一些。
[Dialog]
[delay(time=2)]
[playsound(key="$doorknockquite")]
[stopmusic(fadetime=3)]
是敲门声。
[name="？？？"]拉特兰公证所执行者费德里科，执行公务，请开门。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character]
[Background(image="26_g9_laterano_street",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_360_1#1$1")]
[name="开朗的万国信使"]先生，宾馆的入住手续已经全部办妥啦。
[name="开朗的万国信使"]今天接下来的时间您可以自行安排，出门逛逛也很不错。在路上时，看您似乎很有兴致呢。
[Character(name="avg_npc_177")]
[name="哥伦比亚富商"]嗯——
[name="哥伦比亚富商"]拉特兰城的建筑，风格别致。 
[Character(name="avg_npc_360_1#1$1",name2="avg_npc_177",focus=1)]
[name="开朗的万国信使"]您看，来拉特兰一趟不虚此行吧。
[Character(name="avg_npc_360_1#1$1",name2="avg_npc_177",focus=2)]
[name="哥伦比亚富商"]算是吧

... (全文32872字符)
```

### level_act16side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="26_g9_laterano_street",screenadapt="coverall")]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_262_1#2$1",name2="avg_npc_263_1#1$1",fadetime=1)]
[delay(time=1)]
[character(name="avg_npc_262_1#2$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]我都要把这次来拉特兰当成一次度假了......没想到会发生这样的事。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]尤卡坦，谢拉格也是有信仰的小国......为什么拉特兰可以这样？
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=2)]
[name="尤卡坦"]拉特兰的影响力实在广泛得多......万国信使也是拉特兰教宗布局已久的安排。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=2)]
[name="尤卡坦"]谢拉格没有这样的基础。
[character(name="avg_npc_262_1#2$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]哈......影响力，影响力，走出谢拉格才发现，影响力真是个麻烦的东西。
[character(name="avg_npc_262_1#2$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]现在想想，也真亏恩希欧迪斯过去只靠自己在几个邻国间周旋。
[character(name="avg_npc_262_1#2$1",name2="avg_npc_263_1#4$1",focus=2)]
[name="尤卡坦"]如今，圣女大人的影响力也在逐步提升......我们有我们的优势。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_263_1#4$1",focus=1)]
[name="休露丝"]嗯......可你觉得，拉特兰教宗说的那些，真能实现吗？
[character(name="avg_npc_262_1#9$1",name2="avg_npc_263_1#6$1",focus=2)]
[name="尤卡坦"]......我不知道。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_263_1#6$1",focus=2)]
[name="尤卡坦"]我无法想象，各个国家保持更加紧密的联系，这片大地会是什么样子......这听起来像一个梦。也不知道是不是好梦。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_263_1#1$1",focus=2)]
[name="尤卡坦"]但是那天的神迹......还有教宗的演讲，没有人能等闲视之。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_263_1#6$1",focus=2)]
[name="尤卡坦"]拉特兰，果真是被眷顾之城......吗？
[character(name="avg_npc_262_1#1$1")]
[name="休露丝"]艾泽尔小哥，你们萨科塔怎么看这段时间的事？
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]嗯？啊......是，很大的冲击......
[character(name="avg_npc_262_1#2$1")]
[name="休露丝"]我想也是，听人说那口钟几千年没响过了。
[character(name="avg_npc_262_1#1$1")]
[name="休露丝"]拉特兰会怎么样？
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]......也许不会怎么样，以我对拉特兰人的了解......不，也许哪里都是一样。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]即使发生了后世历史中举足轻重的大事......在当时当地，大家也许，都没什么实感。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]但我们总会意识到变化正在发生，承担起属于自己的责任与使命。
[character(name="avg_npc_262_1#3$1")]
[name="休露丝"]......你还蛮有担当的嘛，小哥。
[character(name="avg_npc_262_1#1$1")]
[name="休露丝"]好了，就送到这里吧，接我们的车会开到这里来。
[character(name="avg_npc_263_1#8$1")]
[name="尤卡坦"]辛苦你了。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]没事。薇尔丽芙枢机就在附近的医院，我直接去向她复命，很方便。
[character(name="avg_npc_262_1#1$1")]
[name="休露丝"]啊，说到那位枢机，替我向她道谢。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]“您满意就好”——枢机是这么吩咐的。
[character(name="avg_npc_262_1#1$1")]
[name="休露丝"]真是滴水不漏......
[character(name="avg_npc_262_1#3$1")]
[name="休露丝"]对了，小哥，帮我和我丈夫拍张照吧。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]好的。
[dialog]
[character(name="avg_npc_262_1#11$1",name2="avg_npc_263_1#8$1")]
[delay(time=1)]
[playsound(key="$skill_flash")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]这样就可以了吗？
[character(name="avg_npc_262_1#11$1")]
[name="休露丝"]摄影技术也不错，艾泽尔小哥。
[character(name="avg_npc_263_1#8$1")]
[name="尤卡坦"]谢谢。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]两位不客气。
[Dialog]
[character(name="avg_npc_262_1#11$1",name2="avg_npc_263_1#8$1")]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=2,block=true)]
[Delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_213_mostma_1#9$1")]
[name="莫斯提马"]菲亚梅塔，你有没有觉得自己的脚步特别沉重？
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]为什么？
[character(name="avg_213_mostma_1#9$1")]
[name="莫斯提马"]教宗阁下讲了那样的话，你难道没有感受到肩上的重担？
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]所以？
[character(name="avg_213_mostma_1#11$1")]
[name="莫斯提马"]所以我在认真考虑是不是该换一份工作了，太需要责任感的工作不太适合我。
[character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"]我看你接替我就很合适。
[character(name="avg_300_phenxi_1#6$1")]
[name="菲亚梅塔"]做梦。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]两位，下午好。
[character(name="avg_213_mostma_1#5$1")]
[name="莫斯提马"]艾泽尔小哥，好久不见。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]也就不到两周啦......
[character(name="avg_300_phenxi_1#3$1")]
[name="菲亚梅塔"]你......在执行任务？
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]薇尔丽芙枢机安排了一点事情，我正要去向她复命。
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]这是我在拉特兰城的最后一项任务了。
[character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"]不错嘛，小哥，出去看过了就知道，拉特兰城蛮无聊的。
[character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"]虽然外面没有那么多好吃的甜点，不过，我们生活的意义也不只是享受，对吧？
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]你要去找薇尔丽芙？她现在在哪？
[character(name="avg_4036_forcer_1#1$1")]
[name="艾泽尔"]司提望区中心医院。
[character(name="avg_300_phenxi_1#1$1")]
[name="菲亚梅塔"]......
[character(name="avg_213_mostma_1#5$1")]
[name="莫斯提马"]走吧，艾泽尔小哥，我们同路。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=2)]
[Character]
[Background(image="26_g7_laterano_ward",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_361_1#1$1")]
[name="薇尔丽芙"]你决定了？
[character(name="avg_npc_353_1#1$2")]
[name="蕾缪安"]嗯，我决定了。
[character(name="avg_npc_361_1#1$1")]
[name="薇尔丽芙"]我以为你还要犹豫一段时间。
[character(name="avg_npc_353_1#2$2")]
[name="蕾缪安"]没什么......只是觉得，大家都迈出了下一步，我也不能再原地踏步了。
[character(name="avg_npc_361_1#6$1")]
[name="薇尔丽芙"]那我就不多问了。你能答应，我已经很高兴了。
[character(name="avg_npc_361_1#6$1")]
[name="薇尔丽芙"]现在这种时候，有你这样的人才加入，再好不过。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_4036_forcer_1#1$1",fadet

... (全文22783字符)
```

### training_act16side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16side教学关_a

[Tutorial(focusX=-130, focusY=-135, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这个是我们拉特兰独有的<@tu.kw>“冰淇淋机”</>，能够为周围干员不断回复技力。
[PopupDialog(dialogHead="$avatar_swllow")] 太棒了，站在<@tu.kw>“冰淇淋机”</>周围让我能更快地使用技能了！

```

### training_act16side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16side教学关_b

[PopupDialog(dialogHead="$avatar_swllow")] 当心，这些是寻路者的突击手，他们会优先攻击<@tu.kw>“冰淇淋机”</>，并对<@tu.kw>“冰淇淋机”</>造成额外伤害。
```

### training_act16side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16side教学关_c

[Tutorial(focusX=-105, focusY=235, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
<@tu.kw>“冰淇淋机”</>被敌人击破后，会对周围所有我方干员造成法术伤害并使其眩晕。

[PopupDialog(dialogHead="$avatar_adnach")] 同理，如果我方击败对手的<@tu.kw>“冰淇淋机”</>，也会对周围所有敌人造成法术伤害并使其眩晕。

```

### training_act16side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16side教学关_d

[Tutorial(focusX=-105, focusY=235, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
<@tu.kw>“冰淇淋机”</>经过短暂的中间状态，又会恢复正常。

[PopupDialog(dialogHead="$avatar_swllow")] 但是现在<@tu.kw>“冰淇淋机”</>的颜色有点奇怪？

[PopupDialog(dialogHead="$avatar_adnach")] 没错，被敌人击破后，<@tu.kw>“冰淇淋机”</>就会转而为敌人回复技力!

[PopupDialog(dialogHead="$avatar_swllow")] 敌人获得技力后，他们马上就又可以使用技能了，可恶，我们必须把<@tu.kw>“冰淇淋机”</>重新争夺回来！

[PopupDialog(dialogHead="$avatar_adnach")] 不用担心，我们的援军到了！

```

### training_act16side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16side教学关_e

[Tutorial(focusX=290, focusY=205, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_adnach", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
寻路者的部分手下配备特殊的弹药技能，当拥有特殊弹药时，他们会使用自己的弹药技能。

```


## 统计

- 总字符数：321231
- 对话行数：2845


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
