# 明日方舟 · 活动剧情 · act24side（25段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act24side」完整剧情脚本（25个文件，3326行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act24side
- 脚本文件数：25

### level_act24side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="36_g1_easternvillageD",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#1$1",fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#4$1",focus=2)]
[name="学者猫"]怎么做到的喵？
[name="学者猫"]如同雪鬼兽的皮毛般优秀的防护性能，轻便程度却堪比迅龙的鳞片......
[name="学者猫"]这里衣服的材质竟然都是这样，甚至柔韧性也很出色喵！
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#9$1",focus=2)]
[name="学者猫"]最奇怪的是这里的人都能穿着这种素材做的衣服，裁剪得比最出色的防具加工商的作品还工整......
[name="学者猫"]根本不可能有足量怪物去提供如此大量的标准素材。
[Character(name="avg_npc_751_1#8$1",name2="avg_npc_752_1#9$1",focus=1)]
[playsound(key="$MH_nekohappy01")]
[name="工匠猫"]新素材！喜欢喵！森林里更多的新素材喵！
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#9$1",focus=1)]
[name="工匠猫"]要跟着长角的“猎人”去讨伐火龙喵！
[Dialog]
[characteraction(name="left", type="jump", xpos=-15,times=1,power=5,fadetime=0.5,isblock=true)]
[characteraction(name="left", type="jump", xpos=15,times=1,power=5,fadetime=0.5,isblock=true)]
[characteraction(name="left", type="jump", xpos=-15,times=1,power=5,fadetime=0.5,isblock=true)]
[characteraction(name="left", type="jump", xpos=15,times=1,power=5,fadetime=0.5,isblock=true)]
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#9$1",focus=2)]
[name="学者猫"]小工匠，再好好想想！这个地方和我们要去的新大陆完全是两回事喵。
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#7$1",focus=2)]
[name="学者猫"]不去森林里打猎的村民，也不用怪物素材做防具和武器......
[name="学者猫"]他们用的东西不知道从哪里来的，在村子里还有很多从来没有见过、不知道做什么用的工具。
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#1$1",focus=2)]
[name="学者猫"]虽然听夜刀说，他们中好像也会有和古龙观测所那些家伙一样的人去观测自然现象，也有生态研究的学者......
[name="学者猫"]但还是很不一样喵！各种方面！
[Character(name="avg_npc_751_1#4$1",name2="avg_npc_752_1#1$1",focus=1)]
[name="工匠猫"]不一样喵？
[Character(name="avg_npc_751_1#4$1",name2="avg_npc_752_1#1$1",focus=2)]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]对喵！必须快点想办法回去才行，我的新大陆最强学者计划还有抢救的机会喵！
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#1$1",focus=1)]
[name="工匠猫"]都算新大陆喵......
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#4$1",focus=2)]
[name="学者猫"]小工匠！你是说......这里也是新大陆喵？而且最重要的是，完全没有任何调查团来过。
[name="学者猫"]没有“猎人”和研究员！没有古龙观测所的家伙们！完全不一样的新大陆！只有我们知道的新大陆！
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#8$1",focus=2)]
[name="学者猫"]如果我能够记录下这里的见闻和知识......等我们回去之后，我就会成为万众瞩目的明星学者喵！
[name="学者猫"]到时候，那群书堆里的老龙人们一定会为我的学识目瞪口呆——我真是太聪明了喵！
[Dialog]
[characteraction(name="right", type="jump", xpos=-20,times=1,power=5,fadetime=0.3,isblock=true)]
[characteraction(name="right", type="jump", xpos=20,times=1,power=5,fadetime=0.3,isblock=true)]
[characteraction(name="right", type="jump", xpos=-20,times=1,power=5,fadetime=0.3,isblock=true)]
[characteraction(name="right", type="jump", xpos=20,times=1,power=5,fadetime=0.3,isblock=true)]
[Character(name="avg_npc_751_1#10$1",name2="avg_npc_752_1#8$1",focus=1)]
[name="工匠猫"]喵？
[Character(name="avg_npc_751_1#10$1",name2="avg_npc_752_1#2$1",focus=2)]
[name="学者猫"]不对......不行，我还是要考虑一下。
[Character(name="avg_npc_751_1#10$1",name2="avg_npc_752_1#1$1",focus=2)]
[name="学者猫"]要对付火龙......我们又不是那些整天和“猎人”去狩猎的随从们，更何况已经帮助过他们一次了喵！
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#1$1",focus=1)]
[name="工匠猫"]对付火龙喵！砰砰！
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#1$1",focus=2)]
[name="学者猫"]小工匠，你要去的话我是绝对不会管你的，反正我要待在这里......
[Dialog]
[Character]
[name="好奇的幼童"]哇！你们看！他们是菲林吗？
[name="年长的幼童"]他们这么小，根本不像菲林嘛。而且毛绒绒的......好可爱哦！
[Character(name="avg_npc_752_1#4$1")]
[name="学者猫"]喂！你们想干什么？
[Dialog]
[Character]
[name="好奇的幼童"]哇！他说话了！真的好可爱！
[name="好奇的幼童"]小小的菲林，你可以和我们一起玩游戏吗？
[name="好奇的幼童"]我们可以把你抱在怀里，给你换上漂亮的衣服。
[name="好奇的幼童"]还可以把你扔到天上去！再接住！就像这样！
[Dialog]
[playsound(key="$d_avg_clothmovement")]
[playsound(key="$MH_nekoangry")]
[CameraShake(duration=0.5, xstrength=0, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_752_1#3$1")]
[name="学者猫"]可恶，你们这群尖耳朵的小家伙，我可是原王立古生物书士队的学者，才不是你们的玩具喵！
[Dialog]
[Character]
[name="年长的幼童"]这样可以摸摸他的脑袋呢。
[Character(name="avg_npc_752_1#3$1")]
[multiline(name="学者猫")]喂！不要乱碰我！我警告你喵......
[character(name="avg_npc_752_1#8$1")]
[characteraction(name="middle", type="jump",times=4,power=5,fadetime=0.5,isblock=false)]
[multiline(name="学者猫")]啊，喵......舒服......
[Character(name="avg_npc_752_1#9$1")]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$MH_nekoangry")]
[name="学者猫"]不对喵！
[name="学者猫"]小工匠......你回来......等等我！
[name="学者猫"]我决定了，嗯，决定了喵！
[name="学者猫"]既然他们都诚恳地请求我，希望我渊博的知识能够帮助他们对抗强大的火龙......
[Character(name="avg_npc_752_1#6$1")]
[playsound(key="$MH_nekoangry")]
[name="学者猫"]作为优秀的原王立古生物书士队的学者，我的职业素养是绝对无法允许我拒绝的喵！
[name="学者猫"]出发喵！就是现在！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g10_easternhouse",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_npc_753_1#1$1",name2="avg_502_Yato_1#5$1",fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_753_1#1$1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="露华村村长"]噢，您是说，在我们村庄附近的森林里，出现了一头和一间屋子差不多大的怪物，会飞，还会四处喷火，甚至连爪子都有毒......
[Character(name="avg_npc_753_1#5$1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="露华村村长"]哈哈，森林可真奇妙啊。
[Character(name="avg_npc_753_1#5$1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]我能理解您会难以相信，但确实是我们亲眼所见，还与它交战过。
[name="夜刀"]因为不确定是否还会有新的危机出现......我建议现在应当立刻通知全部村内居民，视作与天灾同等的灾害开始迁移，越快越好。
[Character(name="avg_npc_753_1#1$1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="露华村村长"]二位好不容易远道而来，又遇上了如此的危机，一定十分辛苦吧。
[name="露华村村长"]我的名字是泷居应，虽然是这小小露华村的村长，但村里的安稳并非我一人的功劳，而是靠着村民们的共同努力换来的。
[Character(name="avg_npc_753_1#5$1",name2=

... (全文42266字符)
```

### level_act24side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_cave_2",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$normal02_intro", key="$normal02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1.5)]
[Character(name="char_500_noirc_1")]
[name="黑角"]来了——右侧！
[Dialog]
[Character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]哈！
[name="夜刀"]小心上方！
[Dialog]
[Character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="char_500_noirc_1")]
[name="黑角"]——！
[name="黑角"]好险......
[name="黑角"]感染生物也太多了！它们怎么会出现在这里？
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]这么多年你还是没有改掉问无意义问题的习惯...... 
[name="夜刀"]绝对不能让这些害虫继续前进了，这么多感染生物进入村庄，后果不堪设想。
[Character(name="char_500_noirc_1")]
[name="黑角"]你的右边！又来了！
[Dialog]
[Character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]——这刀！可恶，砍了太多次，越来越钝了。
[Character(name="char_500_noirc_1")]
[name="黑角"]阻挡......俺记得包里还有些上次任务申请的源石炸药，是遥控触发的，威力足够炸开井盖。
[name="黑角"]得想个方法可以不让炸弹连俺们一起炸飞......
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]那个通风井...... 
[name="夜刀"]通风井打通了洞穴的内壁，炸弹可以破开封闭的井罩，给我们打开逃脱的通道。
[name="夜刀"]等我们出来后再迅速引爆下方的炸弹，破坏这一段的洞穴来阻挡它们的去路......这是可行的方案。
[name="夜刀"]但上方爆炸后也会让这一段洞穴的结构变得脆弱，逃脱的时间非常有限，必须抓紧时间。
[name="夜刀"]布置炸弹的时候，必须有一个人挡住感染生物，你可以吗？
[Character(name="char_500_noirc_1")]
[name="黑角"]不用问，你去布置，俺能撑住。 
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]当心。
[Dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1.5)]
[delay(time=2)] 
[Character(name="char_500_noirc_1")]
[name="黑角"]俺在这里！你们一个都！别想过去！
[Dialog]
[Character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_502_Yato_1#7$1",fadetime=1.5)]
[delay(time=2)] 
[name="夜刀"]马上......好！布置完成了！
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]上方炸弹预备引爆！
[Dialog]
[Character]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1.5)]
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]打开了......确认在预期范围内。
[Character(name="char_500_noirc_1")]
[name="黑角"]你先上去！俺把它们挡在这里！
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]不行，那样太危险了，你很有可能会被埋在这里。
[Character(name="char_500_noirc_1")]
[name="黑角"]你听俺的，不然一定会有漏网之鳞的。
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]......好，那你听好我的指令。
[Dialog]
[playsound(key="$d_avg_cloakmovement")]
[characteraction(name="middle",type="move",ypos=100,fadetime=0.7,isblock=false)]
[Character(fadetime=0.4)]
[delay(time=2)] 
[name="夜刀"]我上来了！黑角，迅速撤离！
[Character(name="char_500_noirc_1")]
[multiline(name="黑角")]俺来了，嘿——
[character(name="char_500_noirc_1")]
[CameraShake(duration=0.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="黑角")]啊！
[Dialog]
[Dialog]
[Character]
[name="夜刀"]你怎么了？
[Character(name="char_500_noirc_1")]
[name="黑角"]爬梯断了......
[Character]
[name="夜刀"]怎么会？*东国粗口*！
[Character(name="char_500_noirc_1")]
[name="黑角"]夜刀，你冷静，俺还没事！
[Character]
[name="夜刀"]冷静，冷静，我想想......有了，还有个办法！
[name="夜刀"]直接引爆炸弹，你用盾牌去挡住冲击波，借助冲力上来！
[name="夜刀"]我一定会抓住你的。
[Character(name="char_500_noirc_1")]
[name="黑角"]明白。
[Character]
[name="夜刀"]做好准备！
[name="夜刀"]跳！
[Dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[stopmusic]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Background(image="36_g3_redleafforest",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[delay(time=0.5)]
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]好——我抓住你了！
[name="夜刀"]上——来——
[Dialog]
[Characteraction(name="middle",type="jump",ypos=40,fadetime=0.4,isblock=false)]
[character(fadetime=0.3)]
[CameraSh

... (全文12484字符)
```

### level_act24side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g3_redleafforest",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_502_Yato_1#2$1",fadetime=1.5)]
[Delay(time=2)]	
[playsound(key="$d_gen_transmissionget")]
[Delay(time=1.5)]	
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]第二次语音记录。
[name="夜刀"]时间，上午九时十五分。天气，多云。我们返回了苍暮山地，现在保持前进。
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]在过去的一段时间内，我与干员黑角在执行任务中遭遇了一系列突发情况。
[name="夜刀"]先是与未知的生物......火龙作战，作战以失败告终。
[name="夜刀"]在抵达当地村庄后，我们对矿石病病源的正常调查遭到了当地居民的阻碍。
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]原因尚不明晰，接着我们又在医疗检测中发现当地的源石影响由来已久。
[name="夜刀"]汇总目前收集到的所有线索，我们的判断是：应当继续在森林中追踪火龙，尝试以此探寻矿石病的源头。迄今为止进展差强人意......
[name="夜刀"]呃啊——这片树丛太密集了，黑角，把斧头给我。
[Dialog]
[playsound(key="$d_avg_clothmovement")]
[Delay(time=1.5)]	
[Character(name="avg_502_Yato_1#4$1")]
[name="夜刀"]你拿了什么过来？我是让你拿斧头给我......凹凸不平的......还在蠕动......啊！
[Character(name="avg_502_Yato_1#6$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夜刀"]源石虫！
[Character(name="avg_npc_751_1#4$1")]
[name="工匠猫"]源石虫喵？
[Character(name="avg_502_Yato_1#4$1")]
[name="夜刀"]为什么源石虫会在我手上啊？
[Character(name="avg_npc_751_1#9$1")]
[playsound(key="$MH_nekohappy01")]
[name="工匠猫"]缺少骨头......源石虫的壳坚硬，很好喵！喜欢喵！
[Character(name="avg_502_Yato_1#4$1")]
[name="夜刀"]黑角——你去哪了？
[Character(name="avg_npc_752_1#1$1",name2="char_500_noirc_1",focus=1)]
[name="学者猫"]喵，你看，这个植物的种子戳一下就会爆开喵。
[name="学者猫"]将种子发射到很远的地方播种......和爆裂果实好像喵。
[Character(name="avg_npc_752_1#1$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]这个和火龙行踪的关系是......哦！难道说......
[Character(name="avg_npc_752_1#2$1",name2="char_500_noirc_1",focus=1)]
[name="学者猫"]不，毫无关系喵。
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]（深呼吸）
[Dialog]
[playsound(key="$d_gen_transmissionget")]
[Delay(time=1.5)]	
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]......这些与我们同行的，是来自其他大陆的类菲林种族...... 
[Character(name="avg_npc_751_1#4$1")]
[playsound(key="$MH_nekohappy01")]
[name="工匠猫"]艾露猫喵！
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]他们自称艾露猫，拥有与火龙相关的知识。
[name="夜刀"]有艾露猫的帮助，再加上罗德岛A4行动组丰富的问题处置经验，我相信我们正离解决事件的关键越......
[Character(name="avg_npc_752_1#1$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]夜刀！往这边走！
[Character(name="avg_npc_752_1#1$1",name2="char_500_noirc_1",focus=1)]
[name="学者猫"]不对喵！是这边！火龙往这边去了喵！
[Character(name="avg_npc_752_1#1$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]可刚才你明明说往这边走...... 
[Character(name="avg_npc_752_1#6$1",name2="char_500_noirc_1",focus=1)]
[name="学者猫"]那是上个痕迹，火龙又在这里蹭到了树干！
[Character(name="avg_npc_752_1#3$1",name2="char_500_noirc_1",focus=1)]
[characteraction(name="left", type="jump",times=2,power=30,fadetime=0.5,isblock=false)]
[name="学者猫"]喵！反正就是往这边！黑角真的和冠突龙一样傻！
[Character(name="avg_npc_752_1#3$1",name2="char_500_noirc_1",focus=2)]
[multiline(name="黑角")]你说什么？冠突龙是什么——
[Character(name="avg_npc_752_1#3$1",name2="char_500_noirc_1",focus=2)]
[playsound(key="$d_avg_punch")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="right", type="jump",times=1,power=30,xpos=-40,fadetime=0.5,isblock=false)]
[multiline(name="黑角")]哎哟！谁把这棵树砍倒的？
[Character(name="avg_npc_752_1#6$1",name2="char_500_noirc_1",focus=1)]
[name="学者猫"]就是会横冲直撞地撞上树的迟钝怪物喵！
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]......越来越近，记录完毕。
[name="夜刀"]黑角，两位艾露猫。
[name="夜刀"]听着，我们已经走了两个小时，现在连火龙的影子都没看见。
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]如果你们还在这里争吵不休，浪费时间，我就把你们送回洞穴陪源石虫聊天。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="36_g3_redleafforest",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#1$1",focus=2)]
[playsound(key="$MH_nekolow")]
[name="学者猫"]小工匠，嘘，小声点喵。
[Character(name="avg_npc_751_1#4$1",name2="avg_npc_752_1#1$1",focus=1)]
[name="工匠猫"]喵？
[Character(name="avg_npc_751_1#4$1",name2="avg_npc_752_1#1$1",focus=2)]
[name="学者猫"]看那里喵，花上。
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#1$1",focus=1)]
[name="工匠猫"]草丛喵。
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#6$1",focus=2)]
[name="学者猫"]没错喵，在那里潜藏着的是——蠢蠢欲动的小型生物喵！
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#6$1",focus=1)]
[name="工匠猫"]近了喵——
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#6$1",focus=2)]
[name="学者猫"]在不被注意的暗影里，危险悄然逼近，而飞虫却一无所知......
[name="学者猫"]潜伏的捕食者在等待一个时机，一个近在咫尺的机会！就是现在喵！
[name="学者猫"]它喷出了一股烟雾，飞虫晃晃悠悠，要落下来了喵！
[Character(name="avg_npc_751_1#5$1",name2="avg_npc_752_1#6$1",focus=1)]
[name="工匠猫"]啊......头晕喵......
[Character(name="avg_npc_751_1#5$1",name2="avg_npc_752_1#6$1",focus=1)]
[playsound(key="$MH_nekoinjured")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="工匠猫"]啊、啊嚏——
[Character(name="avg_npc_751_1#5$1",name2="avg_npc_752_1#4$1",focus=2)]
[playsound(key="$MH_nekoangry")]
[name="学者猫"]小工匠啊！瞧你做的好事！都被你吓跑了喵！
[Character(name="avg_npc_751_1#5$1",name2="avg_npc_752_1#4$1",focus=1)]
[name="工匠猫"]突然好困......好多素材在天上转来转去喵......
[Character(name="avg_npc_751_1#5$1",name2="avg_npc_752_1#6$1",focus=2)]
[name="学者猫"]飞虫碰到了烟雾也掉下来了，是那股烟雾的作用吗？ 
[name="学者猫"]记录一下......让人昏睡的小型生物，或许可以在狩猎中派上用场喵。
[name="学者猫"]小型生物和飞虫，飞虫和花蕊，“猎人”与猎物......实在是太像了喵。
[Character(name="avg_npc_751_1#5$1",name2="avg_npc_752_1#6$1",focus=1)]
[name="工匠猫"]喵呜......像......
[Dialog]
[characteraction(name="lfte", type="jump",times=2,power=30,xpos=-200,fadetime=1.5,isblock=false)]
[Character(name="char_empty",name2="avg_npc_752_1#6$1",fadetime=1)]
[name="学者猫"]是的，小工匠，有一件事我一直很在意......泰拉明明是完全不一样的世界，却和我们那里有太多相似之处了喵。
[name="学者猫"]村庄里的人也好，观察到的生物也好，仔细了解后发现共同点是远远大于差别的喵。
[Character(n

... (全文14226字符)
```

### level_act24side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g3_redleafforest",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="char_500_noirc_1",fadetime=0.7)]
[Delay(time=1)]	
[name="黑角"]学者猫，快去树上！角兽群要来了！
[name="黑角"]来不及了！夜刀！
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]我在赶！
[Character(name="avg_npc_751_1#3$1")]
[playsound(key="$MH_nekohappy01")]
[name="工匠猫"]喵！吃我臭臭喵！
[Dialog]
[playsound(key="$MH_nekoangry")]
[characteraction(name="middle", type="jump", times=1,power=50,xpos=-80, fadetime=0.3, isblock=false)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.4)]
[Character]
[Character(name="char_500_noirc_1")]
[name="黑角"]工匠猫，你扔的是什么？
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0.6, r=0.9, g=0.9, b=0.6, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=false)]
[Delay(time=4.5)]	
[Character(name="char_500_noirc_1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="黑角"]臭！臭死了！那些羽兽又来了吗？
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]有效果！兽群改变方向了！
[name="夜刀"]工匠猫，你用的这是？
[Character(name="avg_npc_751_1#8$1")]
[name="工匠猫"]羽兽，臭臭！异臭球喵！
[Character(name="avg_npc_752_1#8$1")]
[name="学者猫"]啊，是这个喵！真不愧是我的小工匠，竟然这么快就拿羽兽的粪便做好了异臭球！
[name="学者猫"]如果把异臭球扔到怪物身上，它们就会无法忍受这个味道跑开了喵，就像我们躲开黑角一样。
[Character(name="char_500_noirc_1")]
[name="黑角"]喂，不要拿俺举例子啊！
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]只是暂时改变了方向，角兽群仍在森林中横冲直撞，这样下去可麻烦了，火龙的踪迹很可能会被它们破坏掉。
[Character(name="char_500_noirc_1")]
[name="黑角"]角兽的狂奔......俺觉得绝对不是正常的现象。它们怎么会无缘无故地发狂呢？
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]原因不重要，我们最好现在就阻止它们的行动。
[Character(name="avg_npc_752_1#1$1")]
[name="学者猫"]以我的知识推测，要使这么大规模的兽群移动，一定会有一个像领头兽一样的家伙带领方向的喵。
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]真的吗？如果是这样的话，只要把它砍了就够了，很简单。
[Character(name="char_500_noirc_1")]
[name="黑角"]等等，什么叫只要把它砍了？
[Character(name="avg_502_Yato_1#2$1")]
[name="夜刀"]字面意思。
[Character(name="char_500_noirc_1")]
[name="黑角"]你打算怎么去把它砍了哇？
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]直接冲进去。
[Character(name="char_500_noirc_1")]
[name="黑角"]这么多角兽，还都是狂奔状态下......你确定吗？发狂的原因也不能确定......
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]没有时间等待我们去确认最终原因了，我必须速战速决，你来掩护我。
[Character(name="char_500_noirc_1")]
[name="黑角"]再等等！工匠猫，你还有那个......异臭球吗？
[Character(name="avg_npc_751_1#8$1")]
[playsound(key="$MH_nekohappy01")]
[name="工匠猫"]臭臭！好多喵！
[Character(name="char_500_noirc_1")]
[name="黑角"]学者猫，俺想确认一下，如果把那个臭味弄在领头兽身上的话，其他的角兽有可能会散开吗？
[Character(name="avg_npc_752_1#2$1")]
[name="学者猫"]根据它们刚刚的反应，理论上来说......会的。
[Character(name="avg_npc_752_1#1$1")]
[name="学者猫"]但是可能时间不会太久喵！异臭球得离得很近才能确保命中角兽。
[Character(name="char_500_noirc_1")]
[name="黑角"]够了，俺有个法子，让俺从树上接近，争取以最近的距离去命中领头兽。
[name="黑角"]夜刀，你抓住其他角兽散开的时机跳下来，一招制服领头兽！
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]我明白了，就这么做。
[Character(name="avg_502_Yato_1#4$1")]
[name="夜刀"]不过这样你就......
[Character(name="char_500_noirc_1")]
[name="黑角"]更臭了而已，没有问题——呕。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="36_g3_redleafforest",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[playsound(key="$rungeneral")]
[Character(name="avg_npc_755_1#1$1",fadetime=1)]
[Delay(time=2)]	
[name="柏生义冈"]......
[name="柏生义冈"]现在......还来得及......
[Dialog]
[Character]
[name="？？？"]它们太快了，太年轻，充满力量，难以掌控。
[name="？？？"]过去被压抑的在膨胀，这片森林的危险从未减弱。
[name="？？？"]脱离掌控，你的身躯已经衰败，你犯了太多错误。
[Character(name="avg_npc_755_1#3$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="柏生义冈"]不！
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]不......这不是理由。
[name="柏生义冈"]追上去，追上去。
[Dialog]
[playsound(key="$rungeneral")]
[Character(fadetime=1)]
[Delay(time=2)]	
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="柏生义冈"]啊，那是......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_752_1#3$1")]
[playsound(key="$MH_nekohappy01")]
[name="学者猫"]在那里！我看到了喵！
[name="学者猫"]在兽群中前方的位置，角大了一圈、还闪着黄色光泽的那头角兽，领头兽应该就是它喵！
[name="学者猫"]往这边来了喵。
[Character(name="char_500_noirc_1")]
[name="黑角"]俺可以做到的，俺可以做到的。
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]集中精神。
[name="夜刀"]马上就到了，做好准备。
[Character(name="char_500_noirc_1")]
[name="黑角"]等等......俺的鼻塞好像掉了。
[Character(name="avg_502_Yato_1#6$1")]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="夜刀"]现在！
[Character(name="char_500_noirc_1")]
[name="黑角"]啊？啊！不管了！
[Dialog]
[CameraShake(duration=0.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.6)]
[Character]
[CameraShake(duration=0.6, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_765_1#1$1")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.1, block=true)]
[Blocker(a=0.6, r=0.9, g=0.86, b=0.6, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=1, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Characteraction(name="middle",type="move",ypos=-60,fadetime=1,isblock=true)]
[Character]
[Character(name="avg_npc_752_1#8$1")]
[name="学者猫"]超大异臭球攻击！成功了喵！ 
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]——哈！
[Dialog]
[Characteraction(name="middle",type="move",xpos=-300,fadetime=0.3,isblock=false)]
[Character(fadetime=0.3)]
[Delay(time=0.6)]
[Character(name="avg_npc_765_1#1$1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]

... (全文11065字符)
```

### level_act24side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g5_redleaflake",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[name="？？？"]你讨厌干涸的血液，会让矛头生锈变钝。
[name="？？？"]今夜也和那夜一样，湖里只有一个月亮。
[name="？？？"]月亮的倒影，孱弱而无能，只顾躲在身后......若是当时能有所不同......
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]啊......太安静了。
[Character]
[name="？？？"]温顺的夜晚最为残忍，把不该遗忘的人拖出回忆。
[name="？？？"]你须记得......我说过，我们常在湖边的营地休憩，围坐在篝火旁，谈论如何对付那些野兽。
[Character(name="avg_npc_755_1#2$1")]
[name="柏生义冈"]火星噼里啪啦，烤肉在旋转，融化的脂肪，我记得。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]我......不能忘记。
[Character]
[name="？？？"]该出发了，不能让那畜生等急了。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]嗯？是火光？
[Character(name="avg_npc_755_1#4$1")]
[name="柏生义冈"]——！废营地的方向......
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]谁在那里？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="36_g7_lakecamp",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[playsound(key="$rungeneral")]
[Character(name="avg_npc_755_1#1$1",fadetime=1)]
[Delay(time=2)]	
[name="柏生义冈"]......有人来过。 
[name="柏生义冈"]这火......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_752_1#1$1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Character(name="avg_npc_752_1#1$1")]
[name="学者猫"]泰拉的星空......虽然看起来和我们那里的差不多，但是星星的位置似乎完全不一样喵。
[name="学者猫"]喵呜，今晚天上有奇怪的云，好多星星都被挡住了。从来没有见过这样的云，得记录一下。
[Character(name="avg_npc_752_1#2$1")]
[name="学者猫"]之前听黑角说，泰拉的气候和我们那里差别不大。
[name="学者猫"]刮风、打雷、下雨、下雪......相似的生态环境会有相似的自然循环，这也是理所应当的喵。
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]黑角还提到了什么......天灾？这是唯一没有听过的现象喵。
[name="学者猫"]要是黑角的描述没错的话，简直是有如岚龙现身那样恐怖的灾害，不过是由他们口中神秘的源石引起的......
[name="学者猫"]不会动的石头怎么会引起灾难呢？根本想象不到是怎样的作用机制。
[Character(name="avg_npc_752_1#6$1")]
[name="学者猫"]喵，我才不会承认没有观测到的现象的，但......泰拉的特殊之处大概是和这个源石有关喵。
[Character(name="avg_npc_752_1#5$1")]
[name="学者猫"]啊......如果有机会能够亲眼观测到天灾就好了喵。
[Character(name="avg_npc_752_1#4$1")]
[name="学者猫"]喵？是黑角他们回来了吗？
[name="学者猫"]咦，那是......
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.6)]
[Image(image="36_i04",fadetime=0)]
[ImageTween(xFrom=0, yFrom=0, xTo=0, yTo=0, xScaleFrom=1, yScaleFrom=1, xScaleTo=0.85, yScaleTo=0.85, duration=40, block=false)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Sticker(id="st1", text="<i>火光点亮了老者的脸颊，</i>", x=220,y=120, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st2", text="<i>那些被过去所侵蚀的沟壑，</i>", x=220,y=200, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st3", text="<i>却似乎比他所经历的一切更加古远。</i>", x=220,y=280, alignment="left", size=24, delay=0.04, width=700)]
[stickerclear]
[Sticker(id="st1", text="<i>已经难以记清是多久以前，</i>", x=780,y=320, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st2", text="<i>身前的篝火正如当时一般炙热，</i>", x=780,y=400, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st3", text="<i>被火焰燃去的时间再一次唤起模糊的声音，</i>", x=780,y=480, alignment="left", size=24, delay=0.04, width=700)]
[Sticker(id="st4", text="<i>他分不清，是他在摇晃，还是大地在摇晃......</i>", x=780,y=560, alignment="left", size=24, delay=0.04, width=700)]
[stickerclear]
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image]
[Background(image="bg_black")]
[delay(time=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[name="柏生义冈"]明......
[Dialog]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Background(image="bg_cave_2",screenadapt="showall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="柏生义冈"]明。
[Character(name="avg_npc_760_1#1$1")]
[name="柏生明"]哈，老头子，你还没死。
[Character]
[name="柏生义冈"]不是现在。
[name="柏生义冈"]和你不一样，这些可怖而低智的畜生永远无法战胜我。
[Character(name="avg_npc_760_1#1$1")]
[name="柏生明"]顽强的生命力，嗯？就和那些被扎透脑袋，仍在向前爬行的野兽一样。
[Character(name="avg_npc_760_1#9$1")]
[name="柏生明"]不赖嘛，你以为自己已经变成这样了。
[Character]
[name="柏生义冈"]听好了，我会一直狩猎下去。
[name="柏生义冈"]哪怕这片森林里还有一百头、一千头，甚至一万头野兽，直到全部杀光之前，我也不会停手。
[name="柏生义冈"]不管我要面对的是什么......我只会亲手杀死它们，一个接一个。
[name="柏生义冈"]我要去追那个大家伙了，没工夫再和你耍嘴皮子。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Background(image="36_g4_redleafcliff",screenadapt="showall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_lightrain_loop",loop=true,channel="bgs",volume=1,fadetime=6,crosstime=2)]
[name="柏生义冈"]咳——爪痕，这可真大。
[name="柏生义冈"]它刚在这里落下不久......它很饥饿，需要捕食。
[Character(name="avg_npc_760_1#1$1")]
[name="柏生明"]今夜你没有机会了。
[Character]
[name="柏生义冈"]不可能。
[Character(name="avg_npc_760_1#7$1")]
[name="柏生明"]你衰老、伤痕累累，刚经历了一场残酷的搏斗，雨仍在下，没有任何人能帮你。
[name="柏生明"]继续前进下去你真的会死，你毕竟不是野兽。
[Character]
[name="柏生义冈"]我可不像你......那么不堪一击。
[Character(name="avg_npc_760_1#7$1")]
[name="柏生明"]你自己明白。
[Character]
[name="柏生义冈"]......落叶，把它们盖在上面，就像被雨水冲刷下来那样。
[name="柏生义冈"]没有任何人会发现它的踪迹，它是独属于我的猎物。
[Character(name="avg_npc_760_1#7$1")]
[name="柏生明"]说真的，老头子，我不明白你做这些有什么意义。
[Character]
[name="柏生义冈"]好哇，现在你又开始指责我了是吗？
[name="柏生义冈"]我只是代替了你的位置，做着你会做的事。
[Character(name="avg_npc_760_1#8$1")]
[name="柏生明"]真的吗？
[Character]
[name="柏生义冈"]没完没了地冲进森林里，追逐那些野兽，去砍，去刺，去剖开被骨骼包裹的心脏，然后遍体鳞伤地回来......
[name="柏生义冈"]整日念叨着狩猎狩猎，这不就是你最爱做的事吗？
[Character(name="avg_npc_760_1#2$1")]
[name="柏生明"]这么久了，你还是无法理解我。
[Character]
[name="柏生义冈"]呵......我理解不了？那你呢？你以为自己做的就是正确的事吗？
[name="柏生义冈"]你从来没有听过我的话，你有试着理解一次我的感受吗？哪怕一次？
[name="柏生义冈"]那天晚上，如果

... (全文10651字符)
```

### level_act24side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g5_redleaflake",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$MH_bat_act24side_01_intro", key="$MH_bat_act24side_01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Effect(name="$e_spark_01_large",layer=2)]
[PlaySound(key="$MH_repel01", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$MH_repel01", volume=1)]
[Effect(name="$e_spark_01_large",layer=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=false)]
[delay(time=0.5)]
[Character(name="avg_1029_Yato2_1#11$1",fadetime=0.5)]
[delay(time=0.5)]
[name="夜刀"]——！
[name="夜刀"]哈？
[dialog]
[Character(name="avg_1030_noirc2_1#9$1")]
[PlaySound(key="$MH_grip2", volume=1)]
[PlaySound(key="$MH_swmvmt1", volume=1)]
[delay(time=0.4)]
[name="黑角"]夜刀，你还好吗？
[Character(name="avg_1029_Yato2_1#11$1")]
[name="夜刀"]很奇怪......这对双剑......应该能对火龙造成伤害，却没法再更进一步。
[name="夜刀"]为什么会这样？是我的使用方法不对吗？
[Character(name="avg_1029_Yato2_1#6$1")]
[name="夜刀"]黑角，掩护我！我再试一次！
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]好！啊，等等，俺的盾收起来了，这个刀该怎么——
[Dialog]
[Character]
[Delay(time=0.1)]
[Character(name="avg_1029_Yato2_1#6$1")]
[Delay(time=0.4)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(fadetime=0.4)]
[Delay(time=0.6)]
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]等——你！唉！俺来了！
[Character(name="avg_1030_noirc2_1#4$1")]
[name="黑角"]学者猫，对策想好没有？
[Character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]等一下，我在想喵！不要催我喵！
[Character(name="avg_npc_752_1#5$1")]
[name="学者猫"]火龙的弱点，火龙的进攻方式，不是这里......我明明记得从“猎人笔记”中抄下来过的，到哪里去了喵？
[Character(name="avg_1030_noirc2_1#4$1")]
[name="黑角"]你能不能行啊？
[Dialog]
[Character]
[charslot(slot="m",name="avg_1029_Yato2_1#6$1",focus="m")]
[delay(time=0.3)]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot="m",name="avg_1029_Yato2_1#6$1",focus="m",posfrom="0,0",posto="250,0",duration=0.3,isblock=false)]
[charslot(slot="m",name="avg_1029_Yato2_1#6$1",focus="m",afrom=1,ato=0,duration=0.5,isblock=false)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",posfrom="0,0",duration=0.3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Effect(name="$e_spark_01_large",layer=2)]
[PlaySound(key="$MH_repel01", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$MH_repel01", volume=1)]
[Effect(name="$e_spark_01_large",layer=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[delay(time=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_spark_01_large",layer=2)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$MH_repel01", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[delay(time=1)]
[playsound(key="$MH_angervoice")]
[CameraShake(duration=2, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[playsound(key="$MH_jump")]
[delay(time=0.3)]
[playsound(key="$MH_flapwing_2")]
[charslot(action="zoom",poszoom="0.5,0.5",scale=1.05,slot="m",name="avg_npc_9998_1#1$1",focus="m",afrom=1,ato=0,duration=0.5,isblock=false)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",focus="m",posfrom="0,0",posto="-50,200",duration=0.8,isblock=false)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",focus="m",afrom=1,ato=0,duration=0.5)]
[delay(time=1)]
[Character(name="avg_1029_Yato2_1#6$1")]
[name="夜刀"]黑角，火龙朝你那边去了！小心！
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]俺举盾——俺盾呢？
[Dialog]
[Character]
[name="？？？"]阁下请往左闪开！
[Dialog]
[Character(name="avg_1030_noirc2_1#4$1")]
[delay(time=0.3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="middle",type="move",xpos=-400,ypos=0,fadetime=0.5,isblock=false)]
[Character(fadetime=0.3)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$MH_fireball", volume=1)]
[PlaySound(key="$MH_fireballhit")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_npc_750_1#1$1")]
[name="？？？"]太刀大开大合，须以气御刃，决胜于收放之间。
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]这声音......是刚刚那个......啊！
[Character(name="avg_npc_750_1#1$1")]
[name="？？？"]......
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]这是什么啊？
[Character(name="avg_npc_752_1#6$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]傻瓜黑角！它也是艾露猫，是随从艾露猫喵！
[Character(name="avg_npc_750_1#1$1")]
[name="随从艾露猫"]长角的异国“猎人”哦，老夫是有多年经验的随从艾露猫......喵。
[dialog]
[character]
[PlaySound(key="$MH_fireballvoice", volume=1)]
[CameraShake(duration=1,xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[Character(name="avg_1030_noirc2_1#4$1")]
[name="黑角"]夜刀，它又要喷火了！ 
[name="黑角"]学者猫，你看它的脑袋！这是艾露猫吗？
[Character(name="avg_npc_750_1#1$1")]
[name="随从艾露猫"]这身装备乃是老夫跟随多年的“猎人”赠予的，凝结了无数过往的狩猎回忆，是勇气与历练的象征......喵。
[Cha

... (全文24908字符)
```

### level_act24side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$escapebattle_intro", key="$escapebattle_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]喵喵喵喵喵喵喵喵！
[name="黑角"]啊啊啊啊啊啊啊啊啊！
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]喵喵喵喵喵喵喵喵！
[name="黑角"]啊啊啊喵喵喵......你把俺带偏了！
[Dialog]
[playsound(key="$MH_flapwing_1")]
[Delay(time=1)]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]喵哇！要掉下去了喵！
[name="黑角"]你说什么——风太大了——哎哟！俺的面罩！
[name="学者猫"]要掉下去了喵！
[name="黑角"]俺抓得紧的，你掉不下去的。
[Dialog]
[playsound(key="$MH_angervoice")]
[playsound(key="$MH_flapwing_1")]
[Delay(time=1)]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]火龙！火龙在掉下去喵！
[name="黑角"]啊，俺的眼睛被面罩挡住了，什么都看不见！
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]黑角，黑角喵！火龙它它它——它直冲过去了！
[name="黑角"]直——直什么？
[name="学者猫"]要撞上了喵！
[name="黑角"]等等——终于，面罩回正了！
[name="黑角"]啊！要撞上了！
[playsound(key="$MH_shootdown")]
[Dialog]
[Delay(time=1.5)]
[playsound(key="$MH_nekoinjured")]
[PlaySound(key="$d_avg_land_impact", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_cave_2",screenadapt="showall")]
[Delay(time=2)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Character(name="avg_npc_752_1#4$1",fadetime=1.5)]
[Delay(time=2)]	
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]喵！我的笔记......我的尾巴......都还在，太好了喵！
[name="学者猫"]这是哪里？好黑喵......
[name="学者猫"]黑角......黑角！你还活着喵黑角？
[name="学者猫"]喵，我只看到半截身子挂在上面了，黑角，你不要死掉喵......
[Dialog]
[Character]
[name="黑角"]俺没事......可以不要拽俺的腿了吗？
[name="黑角"]装备袋里有灯，把它打开。
[name="学者猫"]灯？那是什么？这个吗？
[name="黑角"]对，摁下面的那个开关。
[Dialog]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]哇，好亮喵！竟然一点都不烫......怎么做到的？
[Character]
[name="黑角"]还有一件事，俺的角......插在石头里了，可以上来帮俺一下吗？
[Character(name="avg_npc_752_1#8$1")]
[playsound(key="$MH_nekohappy02")]
[name="学者猫"]......插在石头里了......喵哈哈哈！
[Character]
[name="黑角"]喂！不许笑！
[Character(name="avg_npc_752_1#8$1")]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]喵，我来了。
[Dialog]
[character]
[name="黑角"]从那边上去，哎哎，别从俺身上爬上来！不要抓那个地方！
[name="学者猫"]上来了......卡在这里了喵？我敲！
[Dialog]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[Delay(time=1)]	
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[Character(name="avg_1030_noirc2_1#6$1",fadetime=1)]
[Delay(time=2)]	
[name="黑角"]痛痛痛......俺的屁股。
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]火龙呢？你看到它了吗？
[Character(name="avg_npc_752_1#1$1")]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]火龙往里面去了喵。
[Character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]俺们进来的地方......洞口太高了，凭俺俩爬上去得费点功夫，得想点其他法子给夜刀留信号，但是也不能跟丢了火龙......
[Character(name="avg_1030_noirc2_1#7$1")]
[name="黑角"]等等，这里是什么地方？
[Character(name="avg_npc_752_1#4$1")]
[name="学者猫"]喵？我还想问你呢！
[Character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]向下的洞穴，火龙下去了......说不定这下面就和村庄那处洞穴相连，看来得下去看一下了......
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]学者猫，等等俺！你怎么先走了？
[Character(name="avg_npc_752_1#6$1")]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]喵！快点前进！
[name="学者猫"]有太多谜团了喵！泰拉的自然规律应该和我们那里的差不多，却出现了我完全无法理解的情况！火龙的行为太奇怪了喵！
[Character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]奇怪？那只新出现的艾露猫好像也说了异常之类的词。
[Character(name="avg_npc_752_1#6$1")]
[name="学者猫"]路上再和你解释喵！
[name="学者猫"]火龙钻进了这里面......说不定这里就有导致火龙变奇怪的原因喵！
[name="学者猫"]赌上身为原王立古生物书士队学者的名誉，我一定会把真相弄清楚喵！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_cave_2")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#1$1",fadetime=1.5)]
[Delay(time=2.5)]
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#1$1",focus=1)]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]黑角喵......你过来看这个。
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#5$1",focus=2)]
[name="黑角"]俺来了——味道臭死了......啊？
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#6$1",focus=2)]
[name="黑角"]学者猫，这些难道是......
[Character(name="avg_npc_752_1#2$1",name2="avg_1030_noirc2_1#6$1",focus=1)]
[name="学者猫"]在这里的......全是被火龙撕碎的......生物尸体喵。
[Character(name="avg_npc_752_1#2$1",name2="avg_1030_noirc2_1#6$1",focus=2)]
[name="黑角"]甲兽、角兽、羽兽......竟然有这么多种类，它杀死这些动物是当作食物的吗？是吃剩的残渣吗？
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#6$1",focus=1)]
[name="学者猫"]不，以火龙的咬合力，连骨头都能碾碎喵，不会有这么多大块的残骸剩下。
[name="学者猫"]生物残骸的外观实际上都非常完整喵，只是被干掉，但没有被啃食的痕迹，不应该是被吃过的......
[name="学者猫"]走，我们往前面看看。
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#1$1",focus=2)]
[name="黑角"]哦，好。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[Character(fadetime=1.5)]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_752_1#1$1",name2="avg_1030_noirc2_1#1$1",fadetime=1.5)]
[Delay(time=2.5)]
[Character(name="avg_npc_752_1#4$1",name2="avg_1030_noirc2_1#1$1",focus=1)]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]喵！怎么会这样？
[Character(name="avg_npc_752_1#4$1",name2="avg_1030_noirc2_1#5$1",focus=2)]
[name="黑角"]发现什么了？
[Character(name="avg_npc_752_1#9$1",name2="avg_1030_noirc2_1#5$1",focus=1)]
[name="学者猫"]这一块的生物残骸，已经被彻底烧焦了......明明已经被干掉拖进来了，火龙却仍然对着它们吐出火焰，这下根本没法吃了喵。
[Character(name="avg_npc_752_1#9$1",name2="avg_1030_noirc2_1#9$1",focus=2)]
[name="黑角"]它是......生气了吗？
[Character(name="avg_npc_752_1#9$1",name2="avg_1030_noirc2_1#9$1",focus=1)]
[name="学者猫"]这里，这里

... (全文15895字符)
```

### level_act24side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g5_redleaflake",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_1029_Yato2_1#4$1",fadetime=1.5)]
[Delay(time=2)]	
[name="夜刀"]黑角干员，收到请回答，黑角。
[name="夜刀"]......联系不上，信号太差了。
[name="夜刀"]柏生先生......
[name="夜刀"]我执行任务的时候不喜欢带着累赘，要是跟不上前进的速度，麻烦您留在原地，或者原路返回营地。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]蠢货，我没想要和你们同行。
[Character(name="avg_1029_Yato2_1#12$1")]
[name="夜刀"]只要您要去找火龙，就请不要擅自离开我的身边，我必须确保您的安全。
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]你——
[Character(name="avg_1029_Yato2_1#3$1")]
[name="夜刀"]随从艾露猫，你继续说。
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#1$1",focus=2)]
[playsound(key="$MH_nekolow")]
[name="随从艾露猫"]喵，是这样的。
[name="随从艾露猫"]老夫追随的“猎人”接到了某位王室成员的委托，似乎是对方心情不好想要火龙的红玉做首饰，这才委托我们去寻找火龙的。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]心情不好......你们那里讨伐火龙的理由都是这么随意的吗？ 
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#5$1",focus=2)]
[name="随从艾露猫"]......那位委托人应该算是个例喵。 
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]言归正传，老夫在靠近火山的森林里发现了这条火龙。
[name="随从艾露猫"]正想要追上去的时候突然被一股奇怪的力量卷了进去，等到反应过来就已经到这里了。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]你记得是什么样的力量吗？
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#8$1",focus=2)]
[playsound(key="$MH_nekolow")]
[name="随从艾露猫"]完全没有印象了......喵。
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#8$1",focus=1)]
[name="夜刀"]能把火龙这样的生物带过来，这种力量也应当视作威胁，不过当下的情况......暂且搁置吧，你继续讲。
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]老夫初来时由于不熟悉环境，便一直尾随火龙，暗中观察着火龙的行为......喵。
[name="随从艾露猫"]据老夫的观察，火龙的异常是从它自己找到一个洞口，下去里面之后开始出现的。
[Character(name="avg_1029_Yato2_1#8$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]洞口？是通往山体内部的吗？
[Character(name="avg_1029_Yato2_1#8$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]是的喵。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]你记得那里有什么特征吗？
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#5$1",focus=2)]
[playsound(key="$MH_nekolow")]
[name="随从艾露猫"]遗憾喵，简单看下去只是普通的洞穴罢了，火龙确实是在进入那里之后开始出现异常的。
[name="随从艾露猫"]老夫也曾进去探查过喵，但下面......
[name="随从艾露猫"]纵横交错的洞窟尤为复杂，几次尝试都没能找到火龙的位置喵。
[name="随从艾露猫"]老夫猜测火龙是在洞窟内占据了一个区域筑巢，应该是一片距离洞口比较近的宽阔空间喵。
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#5$1",focus=1)]
[name="夜刀"]根据露华村后洞穴中的情形来看，那个洞穴很可能和山里的这些洞窟相连。难怪火龙会出现在那里。
[Character(name="avg_1029_Yato2_1#10$1",name2="avg_npc_750_1#5$1",focus=1)]
[name="夜刀"]我还有件事情想要了解......你也见到了，我们之前与火龙的战斗并不轻松，事实上......很艰难。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#5$1",focus=1)]
[name="夜刀"]至今我们尚不能对它造成有效的伤害，我对再次面对火龙很难保持乐观，预计要付出相当大的代价。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]理解喵。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]我想问的是，凭你对火龙的了解，我们下次想要战胜它，有几成的把握？
[name="夜刀"]或者说，有没有什么办法可以提高我们获胜的可能性？
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#7$1",focus=2)]
[playsound(key="$MH_nekolow")]
[name="随从艾露猫"]很难判断喵......和正常的火龙相比，这头过于焦躁了，受到些许刺激就会展现出强烈的攻击欲望。
[name="随从艾露猫"]之前，老夫发现它的感官敏锐度也有了提升，直接导致了攻击方式的改变，这就是老夫说的异常所在......喵。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#6$1",focus=2)]
[name="随从艾露猫"]阁下与老夫的装备里都没有闪光球，也没有麻痹陷阱喵，老夫想不到什么可以困住火龙的办法。
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#6$1",focus=1)]
[name="夜刀"]所以可能性不大......是吗？
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]喵，要提升对火龙的伤害，老夫还是有些想法的，老夫观察到......阁下是否对双剑的使用方法缺少了解？
[Character(name="avg_1029_Yato2_1#2$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]双剑......你是说这对奇怪的武器吗？确实在使用时，我有力不从心的感觉。
[Character(name="avg_1029_Yato2_1#2$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]阁下手中的这对双剑，一定是来自我们那里的武器，且其品质极为优良，可以肯定是出自顶尖的工匠之手......喵。
[Character(name="avg_1029_Yato2_1#8$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]咦......
[Character(name="avg_npc_751_1#4$1")]
[name="工匠猫"]喵？
[Character(name="avg_1029_Yato2_1#8$1",name2="avg_npc_750_1#1$1",focus=2)]
[name="随从艾露猫"]双剑有一套专门的使用法门，老夫会精简地讲与你听。若是能够正确使用它，对火龙的伤害可以显著提升，但......
[Character(name="avg_1029_Yato2_1#8$1",name2="avg_npc_750_1#1$1",focus=1)]
[name="夜刀"]但？
[Character(name="avg_1029_Yato2_1#8$1",name2="avg_npc_750_1#7$1",focus=2)]
[name="随从艾露猫"]一路前行至今，老夫见到了火龙在此地的处境，这让老夫有所思考......真的有必要讨伐火龙吗？
[Character(name="avg_1029_Yato2_1#4$1",name2="avg_npc_750_1#7$1",focus=1)]
[name="夜刀"]你的意思是不应该置火龙于死地吗？
[Character(name="avg_1029_Yato2_1#4$1",name2="avg_npc_750_1#7$1",focus=2)]
[playsound(key="$MH_nekolow")]
[name="随从艾露猫"]老夫认为，拥有强大武力的“猎人”通常是平衡生态的关键存在喵，狩猎行为会影响当地的生态，应当深思熟虑才行。
[name="随从艾露猫"]根据迄今的观察，火龙的活动范围距离村庄较远，它的活动不会危害村庄，况且......此地的生态似乎难称得上健康。
[Character(name="avg_1029_Yato2_1#4$1",name2="avg_npc_750_1#5$1",focus=2)]
[name="随从艾露猫"]草食生物明显繁衍过度，对森林植被的破坏显而易见，火龙能够遏制草食生物的族群扩张，对环境并非无益......喵。
[Character(name="avg_1029_Yato2_1#4$1",name2="avg_npc_750_1#7$1",focus=2)]
[name="随从艾露猫"]如果是在老夫那里，能够取得委托中需求的素材的情况下，老夫不会选择与无害的怪物为敌。
[Character(name="avg_1029_Yato2_1#3$1",name2="avg_npc_750_1#7$1",focus=1)]
[name="夜刀"]我的任务也并不是讨伐火龙，而是处理另一种致命的威胁——矿石病，只是目前与之相关的线索指向了火龙。
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#7$1",focus=1)]
[name="夜刀"]只要能查清矿石病的源头，杜绝其对村庄的威胁，这头怪物的命运就与我的任务无关。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]你们......
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#7$1",focus=1)]
[name="夜刀"]为了弄清楚原因，我们必须......
[Character(name="avg_npc_755_1#3$1")]
[stopmusic]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="柏生义冈"]你们！
[Character(name="avg_1029_Yato2_1#12$1",name2="avg_npc_750_1#3$1",focus=2)]
[name="随从艾露猫"]猎人阁下？
[Character(name="avg_1029_Yato2_1#

... (全文15001字符)
```

### level_act24side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_cave_2",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_1030_noirc2_1#4$1",fadetime=0.7)]
[Delay(time=1)]
[Character(name="avg_1030_noirc2_1#4$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="黑角"]嗬啊——
[Dialog]
[Character]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[delay(time=0.5)]
[Character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="学者猫"]喵哇！
[Character(name="avg_npc_752_1#3$1")]
[name="学者猫"]黑角！你差点砍到我了喵！
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]啊，抱歉，俺还没掌握好这柄太刀的用法。
[Character(name="avg_npc_752_1#1$1")]
[name="学者猫"]喵！这些家伙的样子比之前洞穴里的还要可怕。
[name="学者猫"]从体表的源石分布情况来看，它们的感染程度严重了不少，动作也非常急迫，简直像是在逃窜一样喵。
[Character(name="avg_npc_752_1#2$1")]
[name="学者猫"]你一定想问我为什么知道了这么多吧，那当然是因为我一直在观察被源石感染的生物喵......
[Character(name="avg_npc_752_1#3$1")]
[playsound(key="$MH_nekoinjured")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="学者猫"]喵！你有没有在听我说话？
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]救人要紧，俺去看看！
[dialog]
[character]
[PlaySound(key="$rungeneral", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]您好？外面没事了，你在哪里哇？
[Dialog]
[Character]
[name="？？？"]这里这里！来这边！
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]呃......是这里吗？
[Dialog]
[Character]
[name="？？？"]嗯嗯，就是这扇门。
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]......没有任何东西挡在门前哦。
[Dialog]
[Character]
[name="？？？"]欸！怎么可能？我用了好多办法都打不开。
[Character(name="avg_1030_noirc2_1#1$1")]
[name="黑角"]要不，你试试把下面的把手提起来？
[Dialog]
[Character]
[name="？？？"]嗯？是这样吗......啊！打开了！
[Dialog]
[Dialog]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_dooropen", volume=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_761_1#5$1",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_761_1#5$1")]
[name="？？？"]竟然是这么打开的吗？难怪我没有找到。哈哈，真是奇妙的设计！
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]你就这么被困了三天吗？
[Character(name="avg_npc_761_1#5$1")]
[multiline(name="？？？")]没错，嘿嘿，或许是做观测的时候有点入神了，毕竟可是见到了了不得的东西......
[Character(name="avg_npc_761_1#3$1")]
[multiline(name="？？？")]咦？脚下怎么软软的？
[Dialog]
[Dialog]
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]呃......因为你踩在源石虫的尸体上了......请问你是？
[Character(name="avg_npc_761_1#2$1")]
[multiline(name="？？？")]对不起哦，源石虫......
[Character(name="avg_npc_761_1#5$1")]
[multiline(name="？？？")]啊，忘记自我介绍了，我叫泷居未来，是一名生态学者。
[Character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]黑角，她头上的角和你的不一样喵！
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]未来......这是你的名字？
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]是呀。
[Character(name="avg_1030_noirc2_1#1$1")]
[name="黑角"]俺们是罗德岛的干员，正在这附近执行任务，俺是黑角，这是......
[Character(name="avg_npc_752_1#8$1")]
[name="学者猫"]喵！你是这里的学者吗？
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]当然，目前正在这片地方进行生态考察哦。
[Character(name="avg_npc_752_1#8$1")]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]喵——我可以看看你的研究笔记喵？
[Character(name="avg_npc_761_1#3$1")]
[name="泷居未来"]欸......啊！会说话的小动物，你要干什么？
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]喵呜！我不是小动物，我是艾露猫，也是研究学者喵！你看，我也有研究笔记。
[Character(name="avg_npc_761_1#3$1")]
[name="泷居未来"]哇，你把嘭草果实的爆炸瞬间画下来了，我超喜欢这个的，你知道它爆炸的原因是果实内液体的压力吗？
[Character(name="avg_npc_752_1#8$1")]
[name="学者猫"]我猜到了喵！是不是这样，随着果实的成熟，内部的黏液逐渐增多——
[Character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]喂！是俺救你出来的，理俺一下行吗？
[Character(name="avg_npc_761_1#3$1")]
[name="泷居未来"]哦，行吧。
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]......为什么你会被困在这个矿洞里？
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]环境调查嘛，我可是学者欸。
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]还有一个问题......
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]你等一下！我先说！我有一个超惊人的消息要告诉你们！你们绝对猜不到我看到了什么！
[Character(name="avg_npc_761_1#4$1")]
[name="泷居未来"]你们知道......在这矿洞里有什么吗？
[name="泷居未来"]一个——超级——大的！飞天怪物！
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]......哦。
[Character(name="avg_npc_761_1#4$1")]
[name="泷居未来"]飞天！怪物！还会喷火！
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]......明白了。
[Character(name="avg_npc_761_1#6$1")]
[name="泷居未来"]明、明白了？你们就一点都不兴奋吗？
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]它叫火龙，俺们被扔到这里之前就趴在它的背上。
[Character(name="avg_npc_761_1#6$1")]
[name="泷居未来"]啊......怎么会这样？
[Character(name="avg_npc_761_1#2$1")]
[name="泷居未来"]唉，太遗憾了，原来是已经被发现的生物，我本来想以最近看过的漫画角色给它命名的......害我白高兴了一场......
[Character(name="avg_npc_761_1#3$1")]
[name="泷居未来"]等等！会说话的小动物，我没见过你这样的生物，难道你是......新物种？
[Character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]你......你要干嘛！别靠这么近喵！！
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]快让我好好看看！
[Character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]停一停，俺们先说正事，你和火龙有接触吗？
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]是啊，观察了好久，还做了它在矿洞中的行动记录，在源石环境中发生的变化，感觉一下子都没用了。
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]行动记录喵？
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]源石环境？变化！
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]你......哦不，请问你可以把这些记录拿给俺们看一下吗？这真的对俺们非常重要！
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]当然可以了，你们先过来等我找找。
[Character(name="avg_npc

... (全文33730字符)
```

### level_act24side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g8_minecavity",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$plot_intro", key="$plot_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[character(name="avg_npc_752_1#1$1",fadetime=1.5)]
[Delay(time=2)]
[playsound(key="$MH_nekogood")]
[name="学者猫"]真没想到，矿井里面会是这个样子，和火山地带好接近喵。
[multiline(name="学者猫")]尾巴感觉热热的喵——
[character(name="avg_npc_752_1#4$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="学者猫")]好烫！
[Dialog]
[Dialog]
[character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="学者猫"]喵！着火了喵！
[character(name="avg_1030_noirc2_1#6$1",name2="avg_npc_761_1#1$1",focus=1)]
[name="黑角"]俺明白你想要关闭矿场的原因了，如果俺们见到了这样的情况确实也会立刻想办法阻止。
[character(name="avg_1030_noirc2_1#9$1",name2="avg_npc_761_1#1$1",focus=1)]
[name="黑角"]这片矿场的开采已经过度了，甚至还建有源石加工车间，却完全没有使用专业化的平台器械......
[name="黑角"]这些已经不是一个村庄可以控制的了。
[character(name="avg_1030_noirc2_1#6$1",name2="avg_npc_761_1#1$1",focus=1)]
[name="黑角"]摸索开采，缺少严格防护的后果就是......活性源石的泄露，天灾的出现会是必然......
[name="黑角"]可是俺不懂......
[character(name="avg_1030_noirc2_1#2$1",name2="avg_npc_761_1#1$1",focus=1)]
[name="黑角"]根据你说的，矿场是七年前开始开采的，带头的人是现在的村长，你的叔叔泷居应。
[name="黑角"]仅仅七年......怎么能够深入到这种程度？难道这些矿道是自己变出来的不成？
[character(name="avg_1030_noirc2_1#2$1",name2="avg_npc_761_1#1$1",focus=2)]
[name="泷居未来"]你说对了一半。
[character(name="avg_1030_noirc2_1#5$1",name2="avg_npc_761_1#1$1",focus=1)]
[name="黑角"]什么？
[character(name="avg_1030_noirc2_1#5$1",name2="avg_npc_761_1#1$1",focus=2)]
[name="泷居未来"]矿道并不是靠人力挖掘出来的，而是在开采之前就已经存在。
[character(name="avg_1030_noirc2_1#5$1",name2="avg_npc_761_1#5$1",focus=2)]
[name="泷居未来"]记得我刚刚说的，七年前的兽潮吗？
[character(name="avg_1030_noirc2_1#6$1",name2="avg_npc_761_1#5$1",focus=1)]
[name="黑角"]记得，你说七年前曾发生了一场严重的兽潮，柏生明......是柏生老爷子的儿子，也是一名猎人，就是在这场兽潮的袭击中牺牲了。
[character(name="avg_1030_noirc2_1#6$1",name2="avg_npc_761_1#1$1",focus=2)]
[name="泷居未来"]那场兽潮的发生，正是源自这片矿场的开采。
[Dialog]
[Character]
[playsound(key="$MH_nekoinjured")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[name="学者猫"]喵！
[character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]学者猫，没事吧？
[Dialog]
[Character]
[multiline(name="学者猫")]没事喵，是被什么绊倒了......
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$MH_nekoinjured")]
[multiline(name="学者猫")]喵！
[Dialog]
[Dialog]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", ypos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", ypos=200, fadetime=1, block=false)]
[Character(name="avg_npc_752_1#4$1",fadetime=0.7)]
[delay(time=1)]
[PlaySound(key="$MH_nekoinjured", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="学者猫"]骨头！
[character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]好多骨头，还有牙齿，这是......爪子？
[Character(name="avg_npc_752_1#9$1")]
[playsound(key="$MH_nekolow")]
[name="学者猫"]死去很久了喵......
[Character(name="avg_npc_752_1#4$1")]
[name="学者猫"]喵，这种生物形态！是大型的肉食生物喵！第一次见！
[name="学者猫"]从残骸来看，这种生物应该身披鳞甲，前肢发达，有长而尖锐的爪子，很有可能......善于掘洞喵！
[character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]犰爪兽。
[name="泷居未来"]是它们的名字。犰爪兽是曾经栖息于这片山地的掠食者，具有社会性，会在山体中挖掘建造巢穴。
[name="泷居未来"]这些矿洞曾经就是它们的巢穴，历经岁月，它们在源石矿脉中穿行，修建起雄伟的宫殿。
[character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]可是无论在这里还是森林中，俺们并没有见到过犰爪兽。
[character(name="avg_npc_761_1#2$1")]
[name="泷居未来"]那是因为七年前......犰爪兽从这片森林里消失了。
[character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]消失？
[Character(name="avg_npc_752_1#4$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]消失喵！
[character(name="avg_npc_761_1#2$1")]
[name="泷居未来"]它们种族在这片森林的最后遗存，只剩下你们眼前的这堆骸骨。
[character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]这种事情......到底是怎么发生的？
[character(name="avg_npc_761_1#2$1")]
[name="泷居未来"]在源石矿被发现的早期，柏生明是开采的反对者。
[name="泷居未来"]他认为破坏犰爪兽的巢穴可能会带来难以预料的负面影响，源石开采也伴有严重的危险。
[name="泷居未来"]而我叔叔与其他村民则认为村子急需源石矿的利润来改变艰难的现状。
[name="泷居未来"]之后他瞒着柏生明，联合其他猎人，采用非常规的方式屠杀了巢穴内的全部犰爪兽，以便能进行开采活动。
[name="泷居未来"]正是因为对犰爪兽的屠杀，剩余无家可归的犰爪兽愤怒地在森林中肆虐，直接导致了当年的兽潮。
[character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]竟然是这样，那么多无辜的生命......只是因为开采矿场而被杀害了。
[character(name="avg_npc_761_1#2$1")]
[name="泷居未来"]你们一定见识过叔叔的态度了吧？
[name="泷居未来"]在他看来，火龙简直是那些被他屠杀的生命归来，他一定会常常梦见柏生明哥哥的死吧。
[name="泷居未来"]他的挚友，他的徒弟，贯彻猎人意志到最后一刻......为他而死。
[name="泷居未来"]而现在柏生明哥哥的话已经应验了......他当然恐惧。
[character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]为他而死？柏生明不是为了保护村子而......
[character(name="avg_npc_761_1#2$1")]
[name="泷居未来"]兽潮进攻的方向并非村庄，柏生明哥哥被发现的地方远离村子，离矿场更近。
[name="泷居未来"]他遭受了近乎疯狂的野兽围攻，其数量之多即使在兽潮中也远非正常。
[character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]啊，我们到了。
[Dialog] 
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
在熔岩沸腾的矿井里，源石簇拥之处。
天空王者抬起了它的头颅。
渺小的鬼低头望去。
他们的眼中倒映着彼此的目光。
[dialog]
[charslot(slot="m",name="avg_npc_9998_1#1$1",duration=1)]
[Delay(time=1)]
[playsound(key="$MH_sleepbreathe1")]
[Delay(time=1)]
[playsound(key="$MH_sleepbreathe2")]
[Delay(time=1)]
[Dialog] 
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]*东国感叹用粗口*。
[character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]它将大量的源石围在了自己身边。
[name="泷居未来"]注意不要离得太近，既然你们选择现在不处理它，那就保持这个状态就好。
[name="泷居未来"]要是不小心激怒了它，我们会有大麻烦的。
[character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]明白。学者猫......你在哪？
[Character(name="avg_npc_752_1#9$1")]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]火龙......是用源石搭建了巢穴喵。
[name="学者猫"]难以想象，难以想象喵。
[character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]它的样子......它很痛苦，是因为源石吗？
[

... (全文34739字符)
```

### level_act24side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g2_easternvillageB",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_npc_757_1#1$1")]
[name="利藤裕"]快点！你们几个！
[character]
[name="蒙住脸的村民"]可是......
[name="蒙住脸的村民"]利藤你也快逃吧！钱可没有命重要......
[Character(name="avg_npc_757_1#1$1")]
[name="利藤裕"]闭嘴！
[Character(name="avg_npc_757_1#1$1")]
[name="利藤裕"]我去拖住那老头子！
[Character(name="avg_npc_757_1#1$1")]
[name="利藤裕"]还愣着干什么！
[Character(name="avg_npc_757_1#1$1")]
[name="利藤裕"]你妹妹的病不想治了吗？
[character]
[name="蒙住脸的村民"]但......明白了......
[Character(name="avg_npc_757_1#1$1")]
[name="利藤裕"]混账东西......
[character]
[dialog]
[delay(time=1)]
[Character(name="avg_npc_762_1#1$1")]
[name="走失的幼童"]呜呜呜......
[Character(name="avg_npc_762_1#1$1")]
[name="走失的幼童"]妈妈，你在哪里，呜呜。
[Character(name="avg_npc_762_1#1$1")]
[name="走失的幼童"]我找不到你了......
[Character(name="avg_npc_762_1#1$1")]
[name="走失的幼童"]妈妈......呜呜，不要丢下我......
[character]
[dialog]
[PlaySound(key="$d_avg_snarl_2", volume=1)]
[PlaySound(key="$d_avg_snarl_1", volume=1)]
[Delay(time=1)]
[Character(name="avg_1029_Yato2_1#6$1")]
[playsound(key="$rungeneral", volume=1)]
[name="夜刀"]（突进连斩！）
[dialog]
[character]
[playsound(key="$MH_dualswords01")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_bladeline_red",x =542.1, y =-206.7,rox =-70.9, roy =71.2, roz =0, layer = 1)]
[Effect(name="$e_bladeline_red",x =360.4, y =-149.5,rox =-34.87, roy =49.2, roz =0, layer = 1)]
[Delay(time=0.1)]
[playsound(key="$MH_dualswords02")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_bladeline_red",x =116.1, y =-168.4,rox =-70.9, roy =71.2, roz =0, layer = 1)]
[Effect(name="$e_bladeline_red",x =130.6, y =-226.1,rox =-34.87, roy =49.2, roz =0, layer = 1)]
[Delay(time=0.1)]
[playsound(key="$MH_dualswords01")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_bladeline_red",x =542.1, y =-206.7,rox =-70.9, roy =71.2, roz =0, layer = 1)]
[Effect(name="$e_bladeline_red",x =360.4, y =-149.5,rox =-34.87, roy =49.2, roz =0, layer = 1)]
[Delay(time=0.1)]
[playsound(key="$MH_dualswords02")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_bladeline_red",x =116.1, y =-168.4,rox =-70.9, roy =71.2, roz =0, layer = 1)]
[Effect(name="$e_bladeline_red",x =130.6, y =-226.1,rox =-34.87, roy =49.2, roz =0, layer = 1)]
[Delay(time=1)]
[Character(name="avg_1030_noirc2_1#1$1")]
[name="黑角"]哈！幸好赶上了！
[Character(name="avg_1029_Yato2_1#12$1")]
[name="夜刀"]黑角，孩子没事吧？
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]俺瞅瞅，四肢健全，没有外伤......你有哪里疼吗？
[Character(name="avg_npc_762_1#1$1")]
[name="走失的幼童"]疼......呜呜，盔甲好扎。
[Character(name="avg_1030_noirc2_1#5$1")]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="黑角"]啊！对不起！
[Character(name="avg_npc_759_1#1$1")]
[name="慌乱的村民"]我的孩子！
[Character(name="avg_npc_762_1#1$1")]
[name="走失的幼童"]妈妈！ 
[Character(name="avg_npc_759_1#1$1")]
[name="慌乱的村民"]谢谢......谢谢你们救了我的孩子！
[Character(name="avg_1029_Yato2_1#12$1")]
[name="夜刀"]现在绝对不要靠近森林，听清楚了吗？野兽已经出现在村子附近了，接下来只会越来越多，这里太危险了。
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]夜刀......他们应该不是故意来这边的。
[Character(name="avg_npc_755_1#4$1")]
[name="柏生义冈"]不对！村子面向山林的一侧是有防护网的，我亲手加固过，现在才过去多久，野兽怎么会出现在这里？
[Character(name="avg_npc_755_1#4$1")]
[name="柏生义冈"]我去看看。
[Character(name="avg_1030_noirc2_1#2$1")]
[name="黑角"]两位先冷静一下，村里的大家还没有开始撤离吗？
[Character(name="avg_npc_759_1#1$1")]
[name="慌乱的村民"]没有......没有撤离，矿场爆炸了，天空在燃烧......什么都没有了。
[Character(name="avg_npc_759_1#1$1")]
[name="慌乱的村民"]大家都在逃跑，听到有人说野兽来了就乱成一团，不知道该去哪里......
[Character(name="avg_npc_761_1#3$1")]
[name="泷居未来"]为什么会这么混乱？发生了什么？
[Character(name="avg_npc_759_1#1$1")]
[name="慌乱的村民"]我牵着直树想往人少的地方跑，但是一群人忽然就冲过来了，等我回过神来的时候，直树就不见了......
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]防护网被人为破坏了，有人蓄意放野兽进村。
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]*东国粗口*，泷居那家伙哪去了？
[Character(name="avg_npc_759_1#1$1")]
[name="慌乱的村民"]泷居村长他......
[character]
[dialog]
[PlaySound(key="$d_avg_snarl_2", volume=1)]
[PlaySound(key="$d_avg_snarl_1", volume=1)]
[Delay(time=1)]
[Character(name="avg_1029_Yato2_1#6$1")]
[name="夜刀"]黑角，野兽又来了！
[Character(name="avg_1030_noirc2_1#4$1")]
[name="黑角"]俺来挡着！俺有盾......啊啊啊，刀也行！
[Character(name="avg_1029_Yato2_1#10$1")]
[name="夜刀"]柏生先生，麻烦你们带这对母子去安全的地方，照顾一下村里的情况，我和黑角先去阻挡兽群。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]用不上你说......未来，我们走，未来？
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]她好像已经冲进去了。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="36_g2_easternvillageB",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]为什么来得这么快？上一次不是说离天灾成形还有一段时间吗？
[Character(name="avg_npc_753_1#6$1")]
[name="泷居应"]野成，伊上，快去把大家召集起来，带去我上次说的那个避难所！在那里相对安全，等大家都到齐了再开始统一撤离！
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]幸好一直在为了这一天做准备......你的话果真又应验了。
[Character(name="avg_npc_758_1#1$1")]
[name="茫然的村民"]烧起来了......
[Character(name="avg_npc_758_1#1$1")]
[name="茫然的村民"]烟云在山顶翻涌，天上......火焰......矿场......没了。
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]你还在这里愣着干什么？快带上必要的东西走啊！
[Character(name="avg_npc_758_1#1$1")]
[name="茫然的村民"]我的工作，我的生活......就这样消失了......
[Character(name="avg_npc_758_1#1$1")]
[name="茫然的村民"]......村长，矿场烧掉了，我们是不是又要回到以前的生活了？
[Character(name="avg_npc_753_1#6$1")]
[name="泷居应"]现在不是想这个的时候！
[Character(name="avg_npc_758_1#1$1")]
[name="茫然的村民"]没了......什么都没了......
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]为什么这样慌乱？天灾还没有到达这里，到底是怎么回事？
[character]
[dialog]
[PlaySound(key="$d_avg_snarl_2", volume=1)]
[PlaySound(key="$d

... (全文14401字符)
```

### level_act24side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g6_redleafforestB",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_npc_755_1#3$1")]
[name="柏生义冈"]噫——啊！
[dialog]
[CameraShake(duration=0.8, xstrength=70, ystrength=70, vibrato=50, randomness=120, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$d_sp_chixiaobadao", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]（剧烈的喘息）
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]老爷子，快趴下！
[Character(name="avg_npc_755_1#3$1")]
[name="柏生义冈"]去死吧！
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]什么？
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]没说你！是这只畜生......
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]快趴下，我的源石技艺马上就要爆炸了！
[Character(name="avg_npc_755_1#4$1")]
[name="柏生义冈"]——！
[dialog]
[character]
[PlaySound(key="$d_gen_explo_n")]
[PlaySound(key="$d_sp_ballista")]
[CameraShake(duration=1, xstrength=10, ystrength=8, vibrato=30, randomness=90, fadeout=false)]
[Blocker(a=0.3, r=0.93, g=0.7, b=0.2, fadetime=0.1, block=true)]
[Blocker(a=0, r=0.93, g=0.75, b=0.32, fadetime=2, block=true)]
[delay(time=2)]
[Character(name="avg_npc_753_1#6$1")]
[name="泷居应"]我来拉您，没事吧？
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]不用。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]你手上的那是什么武器......那几头野兽瞬间被解决掉了......
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]我的独门狩猎绝技——就是用这个施术单元所施放的源石技艺，没人学得来。
[Character(name="avg_npc_755_1#7$1")]
[name="柏生义冈"]呵，小把戏而已。
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]剩下的靠陷阱可以撑一会，后面就交给须本他们，我们可以去那边防御相对薄弱的地方......老爷子，您走慢点。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]不要废话。
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]......
[Character(name="avg_npc_755_1#1$1")]
[name="柏生义冈"]你这是什么表情？
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]没事，只是有点怀念以前猎人们一起并肩作战的日子了。
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]而且，已经七年了，这是您第一次没有让我滚开，也没有骂我叛徒。
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]我......没有想到您竟然真的会拿起......
[Character(name="avg_npc_755_1#5$1")]
[name="柏生义冈"]明的狩猎矛，直说就好，我知道你是明的师父。没想到我会去杀那些野兽吗？
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]毕竟您当时不是猎人，也反对阿明来做猎人，阿明的牺牲......让您改变了很多。
[Character(name="avg_npc_755_1#2$1")]
[name="柏生义冈"]你知道就好。
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]......
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]老爷子，其实有件事......您也许一直有误解，这么多年，我......也不知道该如何向您开口。
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]当时并不是我没有救他......
[Character(name="avg_npc_755_1#7$1")]
[name="柏生义冈"]诱兽粉。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]啊？您知道？
[Character(name="avg_npc_755_1#7$1")]
[name="柏生义冈"]我可是他的父亲。
[Character(name="avg_npc_755_1#5$1")]
[name="柏生义冈"]这臭小子，他......是自己找死，就为了保护你们的矿场。
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]直到现在，我还是常常梦见那天夜里他脸上的表情，他的动作，他的眼睛......
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]......到处是野兽的叫声，他最后想要对我说什么，但声音被淹没在喧嚣里，我还记得他苍白的嘴唇......
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]啊......
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]难道他是在说......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=1)]
[Background(image="36_g3_redleafforest",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=1, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.6)]
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]阿明！
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]*东国粗口*，怎么会有这么多野兽？你要做什么？
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]难道你对自己用了......
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]师父，你们回去，绝对不要跟上来！
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]你回来啊！我们可以在这里挡住它们！
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]不，师父！你比谁都清楚！
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]这等规模的兽潮不是我们可以击退的......很多人会受伤，甚至会有人牺牲。
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]源石矿场会被破坏，你们付出的所有心血都将会毁于一旦，我不能让这种事情发生。
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]明明你是最反对开矿场的不是吗？毁掉就毁掉了啊！
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]给我回来！没有什么比你活着更重要！
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]野兽都聚过来了。
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]时间不多了，师父。
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]我反对矿场的开发，源石是危险的未知之物，一定会带来无法预估的灾难......
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]我也无法接受你们杀死那些无辜的生命。舍弃敬畏，放任贪婪，最终的结果只会是如此。
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]但是，我同样记得那天我们一起去到城市，看到的那些凭借源石而起的楼宇，那些耀眼的霓虹和闪亮的招牌......
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]源石是有价值的，它会帮助村子脱离现在困难的处境，能成为大家生存的依靠......已经走到了这一步，你们要好好地抓住这个机会。
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]阿明！
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]猎人就是要为了族群的存续挺身而出，是你教我的，记得吗？
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]啊！滚开！你们这些畜生！不要再拦着我了！
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]兽潮，生命的愤怒。
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]我亦是为生存而面对它们，这是一场对等的战斗。
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]师父，最后答应我一件事。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]啊......
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]今后，请带领大家......
[character(name="avg_npc_760_1#1$1")]
[name="柏生明"]活下去！
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]阿明！你回来！
[character(name="avg_npc_760_1#1$1")]
[stopmusic(fadetime=2)]
[name="柏生明"]师父，最后一句话，请帮我转达给我的父亲，那个顽固的老头子。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=1)]
[Background(image="36_g6_redleafforestB",screenadapt="coverall")]
[CameraEffect(effec

... (全文12393字符)
```

### level_act24side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g2_easternvillageB",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$MH_bat_act24side_01_intro", key="$MH_bat_act24side_01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[charslot(slot="m",name="avg_npc_9998_1#3$1",duration=1)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$MH_shootdown", volume=1)]
[Delay(time=1)]
[Dialog]
[PlaySound(key="$MH_fireballvoice", volume=1)]
[Delay(time=0.5)]
[PlaySound(key="$MH_angervoice", volume=1)]
[CameraShake(duration=1.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[charslot]
[playsound(key="$d_avg_clothmovement", volume=1)]
[Character(name="avg_npc_755_1#6$1",fadetime=1)]
[Delay(time=1.5)]
他跪在地上，右手仍抓着插在地上的狩猎矛。
身体受伤了，但是他没感觉到痛，也许是痛感从太多处传来，衰老的神经已经迟钝到无法处理了。
似乎没有流血，在高温的作用下水汽瞬间蒸腾，皮肤被炙烤到失去痛觉，只留下一片黑色的血痂。
喉咙深处火辣辣的，散发着浓烈的甜腥味，他忽然感受到一阵来自腹部的痉挛，是什么涌了上来。
[Character(name="avg_npc_755_1#4$1")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="柏生义冈"]呕——哇——
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]呸——呸，*东国粗口*，真恶心。
[Dialog]
[Character]
[charslot(slot="m",name="avg_npc_9998_1#3$1",duration=0)]
[playsound(key="$MH_angervoice", volume=1)]
[CameraShake(duration=2, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Dialog]
[bgeffect(name="$eb_roar",x = 120,layer=1)]
[delay(time=2)]
[bgeffect]
[charslot]
巨大的吼声让他的耳膜隆隆作响，意识从混沌的泥泞中剥离出来。
他抬起头，凝望着眼前正在重新站起的庞然巨物。
凝望着它的眼睛。
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]哦......是你。
[name="柏生义冈"]是了，我想起来了......
[Dialog]
[Characteraction(name="middle",type="move",xpos=200,fadetime=0.5,isblock=false)]
[Character(fadetime=0.4)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$MH_fireball", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[playsound(key="$d_avg_broadswordblood", volume=1)]
[delay(time=1.2)]
数分钟前的画面涌上脑海，在喷吐火焰的间隙中他抓住了稍纵即逝的机会，将矛尖射入了火龙的头颅。
代价是，他没能躲过下一次的冲撞。
[Dialog]
[playsound(key="$MH_angervoice")]
[PlaySound(key="$d_avg_land_impact")]
[CameraShake(duration=1.5, xstrength=80, ystrength=80, vibrato=50, randomness=120, fadeout=true, block=true)]
[delay(time=1)]
[playsound(key="$d_avg_cloakmovement", volume=1)]
[Character(name="avg_npc_755_1#7$1",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_755_1#8$1")]
[name="柏生义冈"]哈哈......哈哈哈！
[Character(name="avg_npc_755_1#3$1")]
[name="柏生义冈"]血！哈哈，你感觉到痛了吗？
[name="柏生义冈"]是我！我让你流血了！受伤的滋味怎么样？
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]我早就看见了......你头颅上那些鳞片不够坚硬，你的脆弱我一览无余！
[name="柏生义冈"]你并不是坚不可摧的......你会受伤，所以你也会倒下！
[Dialog]
[character]
[Dialog]
[character(fadetime=0)]
[charslot(slot="m",name="avg_npc_9998_1#3$1")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",posfrom="0,0",posto="-120,0",afrom=1,ato=0,duration=1,isblock=false)]
[playsound(key="$MH_foot")]
[delay(time=1)]
[playsound(key="$MH_foot")]
[delay(time=2)]
[charslot]
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]等等......喂！
[name="柏生义冈"]你！你要去哪里？
[Character(name="avg_npc_755_1#3$1")]
[name="柏生义冈"]我才刚让你受伤了！你不能逃跑！
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]我还能战斗！我们没有决出胜负！
[Dialog]
[Character]
他拄着狩猎矛，试图将身体支撑起来，但最后膝盖只勉强维持住了一个角度。
矛柄深深地嵌进地面，他身后的影子剧烈地颤抖着。
[Character(name="avg_npc_755_1#6$1")]
[name="柏生义冈"]你不能离开这里！我不会......让你过去......
[name="柏生义冈"]上一次能让你流血，那这一次......
[Character(name="avg_npc_755_1#3$1")]
[name="柏生义冈"]我会将矛尖刺入你的心脏！
狩猎矛被高高举起，或许因为是在最后的时刻，佝偻的身躯爆发出超乎想象的力量。
[dialog]
[playsound(key="$rungeneral", volume=1)]
[Characteraction(name="middle",type="move",xpos=-200,fadetime=0.7,isblock=false)]
[Character(fadetime=0.4)]
他奔跑了起来，再一次地，向着只可仰望的生命发起冲锋。
[name="柏生义冈"]啊啊啊啊啊啊——
[Dialog]
[Delay(time=0.4)]
[playsound(key="$MH_foot", volume=1)]
[Dialog]
[Delay(time=0.5)]
[CameraShake(duration=1, xstrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$MH_angervoice")]
[PlaySound(key="$d_avg_land_impact")]
[CameraShake(duration=1.5, xstrength=80, ystrength=80, vibrato=50, randomness=120, fadeout=true, block=true)]
[delay(time=0.6)]
[playsound(key="$bodyfalldown1", volume=1)]
[delay(time=1.5)]
[name="柏生义冈"]咳......
[name="柏生义冈"]我......还没死......
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="柏生义冈"]*东国粗口*，再来啊！
[Dialog]
[Character]
[charslot]
[Dialog]
[charslot(slot="m",name="avg_npc_9998_1#3$1")]
[playsound(key="$MH_sfireballvoice", volume=1)]
[CameraShake(duration=1, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
[Dialog]
[charslot]
他的右手仍然死死地抓着狩猎矛，指甲嵌进了手掌。
[Dialog]
[playsound(key="$d_avg_punch02", volume=0.5)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[playsound(key="$d_avg_punch02", volume=0.5)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
他拼命地捶打着自己的大腿，但肌肉只是毫无回应地震颤。
这一次，这副身体里的最后一丝气力也不复存在了。
[Dialog]
狩猎矛从手中滑落。
[Dialog]
[name="柏生义冈"]站起来！站起来！
[Dialog]
[playsound(key="$MH_fireballvoice", volume=1)]
[delay(time=1)]
[name="柏生义冈"]......可恶！
[name="柏生义冈"]站起来啊！
[Dialog]
[Stopmusic(fadetime=1)]
[playsound(key="$d_avg_arrowshot", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=2)]
[playsound(key="$MH_angervoice", volume=1)]
[CameraShake(duration=1, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.2)]
[Dialog]
[playsound(key="$rungen

... (全文10017字符)
```

### level_act24side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[character(fadetime=0)]
[Background(image="36_g2_easternvillageB",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$MH_avg_intro", key="$MH_avg_loop", volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Character(name="avg_1030_noirc2_1#7$1",name2="avg_1029_Yato2_1#6$1",fadetime=1)]
[delay(time=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.3, block=false)]
[PlaySound(key="$MH_epvspinout", volume=1)]
[CameraShake(duration=0.3, xstrength=0, ystrength=30, vibrato=20, randomness=20, fadeout=true, block=false)]
[delay(time=1.5)]
[character(fadetime=0)]
[charslot(slot="m",name="avg_npc_9998_1#3$1",afrom=0,ato=1,duration=2)]
[playsound(key="$MH_foot")]
[delay(time=1)]
[playsound(key="$MH_foot")]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_9998_1#3$1",action="zoom", poszoom = "0.5,0.5",scale=1.1,afrom=1,ato=1,duration =0.3)]
[playsound(key="$MH_angervoice")]
[bgeffect(name="$eb_roar",x = 120,layer=1)]
[CameraShake(duration=3, xstrength=70, ystrength=70, vibrato=50, randomness=120, fadeout=true, block=false)]
[delay(time=3)]
[bgeffect]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_751_1#1$1",name2="avg_npc_752_1#6$1",focus=2)]
[name="学者猫"]小工匠，快，把我下面的话记录下来！这有可能会成为唯一一份在泰拉大地上讨伐火龙的资料喵！
[Character(name="avg_npc_751_1#4$1",name2="avg_npc_752_1#6$1",focus=1)]
[playsound(key="$MH_nekoinjured")]
[name="工匠猫"]喵！
[Character(name="avg_npc_751_1#4$1",name2="avg_npc_752_1#6$1",focus=2)]
[name="学者猫"]喵！这里是第一期泰拉大陆调查团！我是团长学者猫喵！
[Character(name="avg_npc_751_1#10$1",name2="avg_npc_752_1#6$1",focus=1)]
[name="工匠猫"]喵喵？
[Character(name="avg_npc_751_1#10$1",name2="avg_npc_752_1#6$1",focus=2)]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]怎么了小工匠？我做团长不是理所应当的事情喵？不满意？喵！那就封你当首席工匠好了！
[name="学者猫"]不管那么多喵！总之我们现在正位于狩猎的最前线......最前线的一块石头后面！
[name="学者猫"]在我们面前惊心动魄的终极对决正在上演喵！
[name="学者猫"]一边是天空王者火龙！一边是初出茅庐的泰拉本地“猎人”！加上一只自称身经百战的随从艾露猫！
[name="学者猫"]虽然听上去像是火龙会胜利喵......但现在的情况是超乎想象的激烈！已经进入了白热化阶段！小工匠，记下来了吗？
[Character(name="avg_npc_751_1#9$1",name2="avg_npc_752_1#6$1",focus=1)]
[playsound(key="$MH_nekoinjured")]
[name="工匠猫"]喵！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(fadetime=0)]
[charslot(slot="m",name="avg_npc_9998_1#3$1",duration=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[charslot(slot="m",posfrom="0,0",posto="60,0",duration=0.8)]
[PlaySound(key="$MH_sfireballvoice")]
[delay(time=1.2)]
[charslot(slot="m",posfrom="60,0",posto="0,0",duration=0.4)]
[PlaySound(key="$MH_fireball")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[delay(time=0.5)]
[charslot(duration=0)]
[Character(name="avg_npc_750_1#3$1")]
[Delay(time=0.2)]
[playsound(key="$MH_nekoinjured")]
[Characteraction(name="middle", type="jump", xpos=-300,ypos=900,times=1,power=200,fadetime=1,isblock=false)]
[Character(fadetime=0.5)]
[delay(time=0.2)]
[PlaySound(key="$MH_fireball")]
[delay(time=0.1)]
[PlaySound(key="$MH_fireballhit")]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1.5, block=false)]
[Delay(time=1.2)]
[name="学者猫"]现在我们看到，随从艾露猫躲避了火龙的攻击......很好！火龙的注意力被吸引走了！
[Dialog]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_1030_noirc2_1#6$1",fadetime=0.5)]
[delay(time=1.2)]
[PlaySound(key="$MH_swmvmt2", volume=1)]
[Character(name="avg_1030_noirc2_1#4$1")]
[delay(time=1)]
[playsound(key="$rungeneral")]
[characteraction(name="middle", type="move", xpos=700, fadetime=0.7, isblock=false)]
[Character(fadetime=0.5)]
[delay(time=0.8)]
[name="学者猫"]抓住这个机会，黑角冲向了火龙的尾巴，他举起了太刀！然后！
[name="工匠猫"]然后喵！
[Dialog]
[charslot(duration=0)]
[charslot(slot="m",name="avg_npc_9998_1#3$1")]
[playsound(key="$MH_angervoice")]
[CameraShake(duration=1.5, xstrength=80, ystrength=80, vibrato=50, randomness=120, fadeout=true, block=true)]
[delay(time=1)]
[charslot(slot="m",posfrom="0,0",posto="-150,0",afrom=1,ato=0,duration=0.5)]
[playsound(key="$MH_bitevoice")]
[playsound(key="$MH_bite")]
[playsound(key="$MH_bitehit")]
[CameraShake(duration=0.3, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[delay(time=0.5)]
[charslot(duration=0)]
[PlaySound(key="$swordtsing1",volume=1)]
[PlaySound(key="$d_avg_land_impact")]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[character(fadetime=0)]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]被抽飞了喵！
[name="工匠猫"]凄惨喵！
[name="学者猫"]黑角......表现得似乎比较笨拙喵，让我们看看另一位的表现，夜刀借助火龙打击黑角的时机，选择从侧面对火龙发起了进攻喵！
[Dialog]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", xpos=300, fadetime=0.3, block=true)]
[delay(time=0.51)]
[PlaySound(key="$MH_fireba

... (全文48896字符)
```

### level_act24side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Dialog]
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Subtitle(text="活下去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle(fadetime=2)]
[delay(time=2)]
[Subtitle(text="怎样都好，活下去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="无论如何，活下去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle(fadetime=2)]
[delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="36_g5_redleaflake",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Delay(time=1)]	
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]	
[name="？？？"]喂，老家伙，醒醒。
[Dialog]
[delay(time=1)]
潮湿，温暖，柔软，土壤在流动。
沉默，轻柔，缓慢，意识在下沉。
[name="年老的猎人"]呃......
[name="？？？"]你还不能在这里倒下。
[name="？？？"]它会逃掉的。
[dialog]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=1.5, block=true)]
滚烫的月光浇在头颅上，身下的土壤几乎要沸腾起来，濒临破灭的意识被这股热流冲上顶端，灼痛感强迫他睁开双眼。
[Dialog]
[Delay(time=0.5)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.2, block=true)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]	
[Character(name="avg_npc_755_1#1$1",fadetime=1.2)]
[playsound(key="$d_avg_cloakmovement")]
[Delay(time=3.5)]
[Character]
[name="？？？"]是的，就是这样，站起来。
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]我......昏迷了多久？
[Character]
[name="？？？"]五分钟。
[Character(name="avg_npc_755_1#6$1")]
[name="年老的猎人"]五分钟，我浪费了太久。
[Character]
[name="？？？"]大多数时候，一秒钟就能决定一名猎人的生死。
[name="？？？"]但这次幸好，你还有时间。
[name="？？？"]去湖边，把你的矛捡回来。
[Dialog]
[Delay(time=1)]
猎矛，猎人赖以存活的倚仗，如今半截淹没在湖光里。
他忘记了自己为什么丢下了矛，就像丢下了自己的性命。
[Dialog]
[playsound(key="$d_avg_jump_water")]
[Delay(time=2)]
矛重新立了起来，矛尖的血腥依旧新鲜。
[name="？？？"]或许你需要洗把脸清醒一下，你已经追了三天三夜了。 
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]不过三天，我还没有老到那种程度。
[name="年老的猎人"]那头野兽逃到哪里去了？
[Character]
[name="？？？"]受伤了，它在森林里走不远，估计现在正在某个阴冷的角落舔舐自己的伤口。
[Character(name="avg_npc_755_1#10$1")]
[name="年老的猎人"]森林......
[Dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(fadetime=0)]
[Background(image="36_g4_redleafcliff",screenadapt="showall")]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="他向森林里望去，他能看到的，是一具躯壳。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="树干是向上伸展的脊骨，肋骨似张开的枝丫，悬挂着密密麻麻的肉片。", x=300, y=370, alignment="left", size=25, delay=0.04, width=700)]
[Subtitle(text="黑色的脂肪在半空中堆积，满盛鲜活的血浆，如下一刻就会倾泻而下。", x=300, y=370, alignment="left", size=25, delay=0.04, width=700)]
[subtitle]
[Delay(time=2.5)]
[name="？？？"]你在恐惧。
[Dialog]
[playsound(key="$leaveshake", volume=0.7)]
[Character(name="avg_npc_755_1#6$1",fadetime=1)]
[delay(time=1)]
[name="年老的猎人"]胡说。
[Character]
[name="？？？"]你在怀疑。
[name="？？？"]怀疑是自己在前进，还是森林在逼近，张牙舞爪地朝你扑来。
[name="？？？"]你几乎都要转身逃跑了。
[Character(name="avg_npc_755_1#7$1")]
[name="年老的猎人"]不可能。
[Character]
[name="？？？"]别试图掩饰，你的一切都逃不过我的眼睛。
[name="？？？"]但是听着，我不会否定你的恐惧。
[name="？？？"]这片森林就是一头怪物，关于它的一切都值得恐惧。
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]一头怪物......
[Character]
[name="？？？"]一头噩梦般的怪物，张开它的血盆大口，将生命啃咬撕碎。这就是森林本来的样貌。
[Character(name="avg_npc_755_1#2$1")]
[name="年老的猎人"]是的，是这样的。
[Character]
[name="？？？"]但它并非不可战胜。
[name="？？？"]我问你，你还记得我最后的模样吗？
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]我记得，我永远不会忘记。
[Character]
[name="？？？"]你愤怒吗？
[Character(name="avg_npc_755_1#6$1")]
[name="年老的猎人"]我愤怒，我愤怒得浑身颤抖，指甲嵌进手掌。
[Character]
[name="？？？"]很好，我要你愤怒，你必须愤怒。
[name="？？？"]你会害怕，会慌乱，会痛苦万分，但愤怒会冲刷掉这一切。
[name="？？？"]在愤怒面前不会有任何阻碍，森林会因为你的怒火而不堪一击。
[Character(name="avg_npc_755_1#6$1")]
[name="年老的猎人"]没错，我会愤怒，我会拔去森林的尖牙，砍下它的利爪。
[name="年老的猎人"]它如何对待你，我就会如何奉还。
[Character]
[name="？？？"]很好，那边有血迹，去看看。
[Dialog]
[delay(time=1)]
[Character(name="avg_npc_755_1#1$1")]
[Delay(time=0.5)]
[playsound(key="$d_avg_cloakmovement")]
[characteraction(name="middle", type="move",ypos=-50,isblock=true,fadetime=1)]
[Delay(time=1.5)]
[name="年老的猎人"]啧......
[name="年老的猎人"]还是温热的，它流的血不少，伤口又开裂了。
[Dialog]
[characteraction(name="middle", type="move",ypos=50,isblock=true,fadetime=1)]
[name="年老的猎人"]血迹在这里之后就消失了。
[Character]
[name="？？？"]看到树上那些抓痕了吗？仔细观察。
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]用不着你说。
[name="年老的猎人"]树干被抓得很深，它一定抓了很多次，刮下了大量树皮。
[name="年老的猎人"]在痕迹的边缘残留有被血浸透的毛发，地上也有。
[Character]
[name="？？？"]这些畜生越来越狡猾了。
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]它知道血会暴露踪迹，于是把木屑蹭在伤口上止血，又在原先的痕迹上抓得更深，以掩盖自己的行踪。
[Character]
[name="？？？"]但野兽毕竟是野兽，再细的墨棒擦过白纸也会留下痕迹。
[Character(name="avg_npc_755_1#1$1")]
[name="年老的猎人"]苍钩草的果实会附在路过野兽的皮毛上，它们总是喜欢搭顺风车。
[name="年老的猎人"]看看那些离开的小家伙们为我们指出了通往何处的道路，哈......
[Character(name="avg_npc_755_1#6$1")]
[name="年老的猎人"]果然，它进了那个洞穴。
[Dialog]
[Character]
[Delay(time=0.3)]
[Stopmusic(fadetime=1)]
[playsound(key="$MH_angervoice", volume=0.4)]
[Delay(time=3)]
[Character(name="avg_npc_755_1#10$1")]
[name="年老的猎人"]什么？那种声音......我从没听过。
[Character]
[name="？？？"]哦，看来我们有新朋友了。
[Character(name="avg_npc_755_1#6$1")]
[name="年老的猎人"]它的声音让我很兴奋，说不定会是它。
[Character]
[name="？？？"]别急，猎人总是专注眼前。
[Dialog]
[Character(name="avg_npc_755_1#6$1")]
[Delay(time=1)]
[playsound(key="$rungeneral")]
[Character(fadetime=1)]
[Delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_cave_2",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Delay(time=1)]	
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_755_1#1$1",fadetime=1.5)]
[Delay(time=2.5)]
[name="年老的猎人"]我知道你在里面。
[Dialog]
[charact

... (全文11683字符)
```

### level_act24side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="36_g4_redleafcliff",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",fadetime=1.5)]
[Delay(time=2.5)]
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]俺又望见那块石头了。
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]多少次了？
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]俺算算，第七次了。
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]我们一直在这里兜圈子，不管往哪个方向前进总是会回到这里。
[name="夜刀"]如果能记录下行动的轨迹......装备里有够长的绳子吗？
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]以后俺会记得申请的......啊对了！
[name="黑角"]工匠猫......你在干嘛？
[Character(name="avg_npc_751_1#1$1")]
[playsound(key="$MH_nekotalk")]
[name="工匠猫"]挖，挖，挖矿喵。
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]俺......记得你身上是不是有很多好东西，让俺摸摸。
[Character]
[Character(name="avg_npc_751_1#9$1")]
[playsound(key="$d_avg_clothmovement")]
[playsound(key="$MH_nekotalk")]
[Characteraction(name="middle",type="jump",times=5,power=10,fadetime=1.2,isblock=false)]
[name="工匠猫"]喵——喵喵！
[Delay(time=1)]
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]嘿，呃，这里......啊哈！这个或许可以？
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]黑色的粉末，的确能够作为沿途的标记。你们在这里等着，我去试试。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="char_empty",name2="char_500_noirc_1",fadetime=1.5)]
[Delay(time=5)]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",fadetime=1.5)]
[Delay(time=2.5)]
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]夜刀......
[name="黑角"]俺看见你了。
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]不用你说，我看见地上的痕迹了。
[name="夜刀"]又回来了......
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]嗯。
[Character(name="avg_502_Yato_1#7$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]先是被莫名其妙的发狂兽群追，又丢了火龙的踪迹，现在被困在走不出去的山崖。
[name="夜刀"]定位设备全部失灵，图像无法显示......这片森林到底有什么毛病？
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]......不行，我再去试试，绝不能就在这里停下。
[Character(name="avg_502_Yato_1#2$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]夜刀......你冷静些。
[name="黑角"]你听俺说，这可能是某种特殊的自然现象，不是什么威胁。
[name="黑角"]再等等好吗？观察一下，说不定有什么被俺们漏下的地方，一定会有破解的办法。
[name="黑角"]而且......你有没有觉得俺们身边又少了什么？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="36_g3_redleafforest",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_npc_752_1#5$1",fadetime=1.5)]
[Delay(time=2.5)]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]夜刀——
[name="学者猫"]黑角——
[name="学者猫"]小工匠——
[name="学者猫"]你们在哪里喵？
[Dialog]
[playsound(key="$d_avg_snowstormflp")]
[Delay(time=2.5)]
[Characteraction(name="middle", type="jump", times=1,power=10,fadetime=0.5,isblock=true)]
[playsound(key="$MH_nekotalk")]
[name="学者猫"]好了，都出来吧，不要再恶作剧了喵。
[name="学者猫"]黑角，你就在那棵树后面对不对喵？
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]小工匠，别以为你藏在那块石头后面我就发现不了你喵。
[name="学者猫"]夜刀，快从树上下来喵。
[Character(name="avg_npc_752_1#5$1")]
[playsound(key="$MH_nekolow")]
[name="学者猫"]没有......不在......
[name="学者猫"]完了，这下完了喵......
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]只是稍微观察了一会儿树上的奇怪纹路，大家一转眼就不见了喵。
[name="学者猫"]结果那些纹路只是没有价值的树皮破损喵......
[Character(name="avg_npc_752_1#5$1")]
[multiline(name="学者猫")]是我的错......
[character(name="avg_npc_752_1#3$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="学者猫")]怎么可能喵？学者认真做观察的时候，跟班们就应该老老实实地在原地等着喵！
[Dialog]
[Dialog]
[character(name="avg_npc_752_1#9$1")]
[playsound(key="$MH_nekolow")]
[name="学者猫"]都怪他们，没有我的话他们才找不到火龙，谁让他们不好好关注我。
[name="学者猫"]现在我不见了，他们知道我有多重要了，肯定在急着到处寻找我的踪迹喵，特别是黑角和小工匠这两个笨家伙。
[name="学者猫"]夜刀......她凶巴巴的，但她和我还有约定喵，不可能扔下我不管！
[name="学者猫"]怕、怕什么？我安安心心地在原地等着他们来找我就好了喵。
[Dialog]
[playsound(key="$d_avg_snarl_1",volume=0.4)]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_752_1#4$1")]
[Characteraction(name="middle", type="jump", times=1,power=10,fadetime=0.5,isblock=true)]
[Character(name="avg_npc_752_1#5$1")]
[playsound(key="$MH_nekoinjured")]
[name="学者猫"]喵！救我喵！
[name="学者猫"]森林......森林里有......
[name="学者猫"]难道我堂堂原书士队的生态学者，未来的泰拉首席专家......我的荣誉猫生就要在这里止步了吗？
[name="学者猫"]不可能喵！我一定可以——
[Dialog]
[playsound(key="$d_avg_snarl_2",volume=1)]
[Delay(time=0.8)]
[Characteraction(name="middle", type="jump", times=1,power=10,fadetime=0.5,isblock=true)]
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]喵......我再也不掉队了喵。
[name="学者猫"]黑角，我一定再也不说你笨了。小工匠，我会偶尔表扬你的......啊，会经常，经常表扬的喵！
[Character(name="avg_npc_752_1#5$1")]
[name="学者猫"]喵呜，有人能来救我吗......
[Dialog]
[Character]
[Delay(time=0.5)]
[stopmusic(fadetime=1)]
[playsound(key="$d_gen_walk_n")]
[Character(name="char_500_noirc_1",name2="avg_npc_751_1#1$1",fadetime=1.5)]
[Delay(time=2.5)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Character(name="char_500_noirc_1",name2="avg_npc_751_1#1$1",focus=1)]
[name="黑角"]学者猫，你在干嘛？
[Character(name="char_500_noirc_1",name2="avg_npc_751_1#1$1",focus=2)]
[name="工匠猫"]喵？
[Character(name="avg_npc_752_1#9$1")]
[name="学者猫"]喵......我......你怎么......
[Character(name="avg_npc_752_1#6$1")]
[playsound(key="$MH_nekoangry")]
[CameraShake(duration=0.3, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="学者猫"]黑角！你这个愚蠢！迟钝！缓慢的长角怪人喵！
[Character(name="char_500

... (全文30760字符)
```

### level_act24side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="27_g26_dusk_wild",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
故事的最后，猎人没能打败怪物。
但是，村民们都已经离开了，只剩下一片废墟在火焰中熊熊燃烧。
怪物失去了目标，也受了很重的伤，龇牙咧嘴了一阵子，独自返回森林去了。
离开之前，它仿佛留下了这么一句话。
“我总是会再回来的。”
猎人面对森林，静静地矗立着，许久才说出他的回应。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character]
[name="调皮的幼童"]欸？猎人竟然没有打败怪物！太没劲了！
[Character]
[name="好奇的幼童"]是啊，那可是村里最厉害的猎人哇，怎么会打不过怪物呢？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]故事就是这样写的哦。
[Character]
[name="好奇的幼童"]但是之前袭击村庄的火龙，好像确实让它飞走了。
[Character]
[name="调皮的幼童"]哼，那是他们都太弱了，等我以后当了猎人，绝对三下两下就把火龙赶跑了。
[Character(name="avg_npc_756_1#1$1")]
[name="和也"]胡说什么？火龙那种怪物根本不是你可以对付的，我可是亲眼见过它的！
[Character(name="avg_npc_756_1#1$1")]
[name="和也"]你们看！这是什么？
[Character]
[name="调皮的幼童"]是用来狩猎火龙的那柄狩猎矛！
[Character(name="avg_npc_756_1#1$1")]
[name="和也"]夜刀姐姐说暂时交给我保管，这说明我有拿起它的资格。以后，我才会是村里最厉害的猎人，你就一边歇着去吧！
[Character]
[name="调皮的幼童"]你再说一遍！吃我一记气刃兜割！
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]好啦，不要闹了。
[Character]
[name="好奇的幼童"]姐姐，猎人最后讲了什么呀？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]这个嘛......
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]哎呀，要开饭啦，孩子们快去吃饭吧，等回来我再把猎人的话讲给大家听哦。
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]去吧，去吧。
[dialog]
[character]
[playsound(key="$runsand")]
[delay(time=2.5)]
[Character(name="avg_npc_753_1#2$1",fadetime=1)]
[delay(time=1)]
[name="泷居应"]未来......明明那件事已经过去半个月了，有时候却感觉它就发生在昨天。
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]你的记忆力好起来了。
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]唉......我可从来都没有忘记阿明的事，柏生老爷子醒了吗？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]还在昏迷，但医生说身上的伤已经恢复了很多了，他的生命可是相当顽强呢。
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]哎，最近真是忙坏我了，规划街道，修建新房......
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]幸好得益于开采源石，我们的积蓄不少，利藤裕那家伙瞒账所得的资产也在大家的愤怒下交了出来。
[name="泷居应"]开头不会是难事，但是之后的产业......
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]未来，你说的关于凉花草异地栽培的事，安置好了后我们可以去试一试吗？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]是假的哦。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]假......假的？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]是啊，你知道的，凉花草对环境的要求超级严苛哦。以现在的科技水平来看，基本没有异地栽培的可能。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]可是你之前明明说......
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]不那么说你们怎么肯撤离？危险来了都吓成傻子了，被利藤裕耍得团团转，我总得让大家去撤离吧。
[Character(name="avg_npc_753_1#6$1")]
[name="泷居应"]将来......村子产业的事可真的麻烦大了，伤脑筋啊。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]哎呀，不慌嘛，我其实还有一个想法。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]认真的？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]超级认真。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]你说，我听听。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]我们可以用上我们在矿场开采的经验呀。
[name="泷居未来"]比如集合村子里的能手，出村去参与成熟的源石工业项目，把安全可控的技术和产业链带回村子。
[Character(name="avg_npc_753_1#3$1")]
[name="泷居应"]未来，你知道你在说什么吗？我们好不容易脱离了源石矿场，现在又要想方设法回到源石身边？
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]而且......不就是你想把矿场给炸了吗？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]那并不是因为矿场本身，而是矿场的开采超出了你们可以控制的范围，大家又不听我劝嘛。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]我们与源石矿直接接触了那么久，摸索出那么多经验，肯定能派上用场啦。
[Character(name="avg_npc_753_1#4$1")]
[name="泷居应"]源石太危险了，天灾、矿石病......这些我们亲身经历，我们还要再回到这种恐惧的笼罩下吗？
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]叔叔，尽管如此，我们脚下的这片大地，想在它身上求生，源石依然是不可或缺的。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]那些霓虹闪耀的城市，它们的光芒都是由源石工业点亮的。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]我们无法背弃它，回归蛮荒，这不现实。
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]可是......总不能......
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]叔叔，重新开始不意味着前功尽弃。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]我们对于源石工业的了解仅仅是冰山一角，我们需要前行，去与成熟的产业体系交流，完善与丰富自己的经验。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]最后，我们将能够安全地、可控地从源石中获益。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]曾经的急功近利带来了灾难，但并不意味着我们必须抛弃源石。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]相反，我们应该更尊重源石，尊重与它伴生的毁灭，才能接受它所带来的机遇。
[Character(name="avg_npc_761_1#1$1")]
[name="泷居未来"]让过去的牺牲白白归于尘土，这不是我们该做的事。况且，现在有罗德岛的朋友愿意帮助我们，不是吗？
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]嗯......
[name="泷居应"]你说的对，我的确应该脚踏实地地考虑村子的未来。
[Character(name="avg_npc_753_1#2$1")]
[name="泷居应"]源石工业......虽然我不确定我们现在的经验能不能完美衔接上，但就像你说的，为了生存下去，我们可以试一试。
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]等到村子变得更好了，你们能给我盖一间最豪华、最漂亮的研究所吗？
[Character(name="avg_npc_753_1#1$1")]
[name="泷居应"]你......要做什么？
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]当然是要研究凉花草的异地栽培啦，以及去做其他各式各样的研究，寻找可以彻底摆脱源石的方法。
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]为了......让我们驶向不必躲在灾难的阴影之下，能抬头挺胸面向光芒的......
[Character(name="avg_npc_761_1#5$1")]
[name="泷居未来"]明日。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character]
[Delay(time=1)]
[Background(image="36_g4_redleafcliff",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$leaveshake", volume=0.6)]
[delay(time=2)]
[Character(name="avg_1030_noirc2_1#9$1")]
[name="黑角"]夜、夜刀，俺还是担心，在任务结束回程的时候擅自改道来到这里，要是被博士知道了......
[Character(name="avg_1029_Yato2_1#10$1")]
[name="夜刀"]那你会说出去吗？
[Character(name="avg_1030_noirc2_1#5$1")]
[name="黑角"]俺肯定不会！
[Character(name="avg_1029_Yato2_1#1$1")]
[name="夜刀"]到了。
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]哇，这里......天灾真的摧毁了一切。
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]整座山都被烧掉了，升腾的灰烬进入云层，直到今天还在飘落......
[Character(name="avg_1029_Yato2_1#3$1")]
[name="夜刀"]黑角，距天灾那天多久了？
[Character(name="avg_1030_noirc2_1#6$1")]
[name="黑角"]半个月了。
[Character(name="avg_1029_Yato2_1#3$1")]
[name="夜刀"]已经半个月了吗？总感觉还是昨天的事。
[Character(name="avg_1029_Yato2_1#1$1")]
[name="夜刀"]听说艾露猫们在罗德岛上有了新的编制？
[Character(name="avg_1030_noirc2_1#8$1")]
[name="黑角"]嗯，他们的正式编制是“艾露猫特别行动小组”，组长是随从艾露猫，但学者猫仍坚持把名字叫作“泰拉大陆调查团”，并自封团长......
[Character(name="avg_1030_noirc2_1#8$1")]
[name="黑角"]他们会负责对付冒出来的特殊生

... (全文7998字符)
```

### level_act24side_tr01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_forest",xScale=0.9,yScale=0.9,x=0,y=-20)]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=2)]
[Character(name="avg_502_Yato_1#5$1",fadetime=1,block=true)]
[Delay(time=1.5)]
[playsound(key="$leaveshake", volume=0.7)]
[Delay(time=1.5)]
[name="夜刀"]往左。
[Dialog]
[characteraction(name="middle", type="jump", xpos=-40, times=1,power=2,fadetime=2, isblock=true)]
[Character(name="avg_502_Yato_1#5$1",focus=-1)]
[name="黑角"]够了吗？
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]往右再回一点。
[Dialog]
[characteraction(name="middle", type="jump", xpos=40, times=1,power=2,fadetime=2, isblock=true)]
[playsound(key="$leaveshake", volume=0.7)]
[Delay(time=1.5)]
[name="夜刀"]还是不行......把脚踮起来。
[Dialog]
[Delay(time=1)]
[name="夜刀"]黑角......踮高一点。
[Dialog]
[Delay(time=0.8)]
[playsound(key="$d_avg_clothmovement")]
[characteraction(name="middle", type="move", ypos=30,fadetime=2.5, isblock=true)]
[name="夜刀"]好，就这样，保持住。
[Character(name="avg_502_Yato_1#5$1",focus=-1)]
[name="黑角"]啊，嗯......
[Dialog]
[Character(name="avg_502_Yato_1#5$1")]
[CameraShake(duration=1, xstrength=1, ystrength=1, vibrato=5, randomness=10, fadeout=false, block=false)]
[Delay(time=0.5)]
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]肩膀不要晃。
[Character(name="avg_502_Yato_1#5$1",focus=-1)]
[name="黑角"]俺在努力......
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]快了，再坚持一下。
[Character(name="avg_502_Yato_1#5$1",focus=-1)]
[name="黑角"]好......
[Dialog]
[Character(name="avg_502_Yato_1#5$1")]
[playsound(key="$d_avg_cloakmovement")]
[Delay(time=2)]
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]完成了，放我下来吧。
[Dialog]
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=20, randomness=30, fadeout=true, block=false)]
[characteraction(name="middle", type="move", ypos=-15,fadetime=1, block=false)]
[Character(fadetime=0.8)]
[playsound(key="$d_avg_clothmovement")]
[Delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Background(image="bg_forest",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#1$1",fadetime=0.7)]
[Delay(time=1)]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#1$1",focus=1)]
[name="黑角"]（喘气）
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#1$1",focus=2)]
[name="夜刀"]这一次采集到的样品质量不错。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#1$1",focus=1)]
[name="黑角"]夜刀，俺有一个建议。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#1$1",focus=2)]
[name="夜刀"]你说。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#1$1",focus=1)]
[name="黑角"]俺觉得......
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]把镊子递给我。
[Dialog]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1")]
[playsound(key="$d_avg_clothmovement")]
[characteraction(name="left", type="move", xpos=20,fadetime=1, isblock=true)]
[delay(time=0.3)]
[characteraction(name="left", type="move", xpos=-25,fadetime=1, isblock=true)]
[Delay(time=0.5)]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]好，是这样的......
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]封口条。
[Dialog]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1")]
[playsound(key="$d_avg_clothmovement")]
[characteraction(name="left", type="move", xpos=20,fadetime=1, isblock=true)]
[delay(time=0.3)]
[characteraction(name="left", type="move", xpos=-25,fadetime=1, isblock=true)]
[Delay(time=0.5)]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]给。那个......
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]不是这个，是那个蓝色的。注意样品分类。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]好......
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#4$1",focus=2)]
[name="夜刀"]对了，你要说什么？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#4$1",focus=1)]
[name="黑角"]俺......俺觉得下次出野外任务之前，俺们是不是可以申请一个梯子？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]否决，过重的装备负担会影响野外行动的机动性，遭遇突发事件将会难以应对。
[name="夜刀"]好了，这份样品也拿去检测一下，希望这次能找到点东西。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]嗯。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#4$1",focus=2)]
[name="夜刀"]所以为什么要申请梯子？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#4$1",focus=1)]
[name="黑角"]......没事，不要往心里去。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.7, block=true)]
[character(fadetime=0)]
[playsound(key="$keyboard")]
[delay(time=1)]
[Background(image="bg_forest",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=0.5)]
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#4$1",focus=1)]
[name="黑角"]样品的初步检测结果，活性源石微粒，未检出，和之前一样。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]竟然还是没有......我们采集了多少份样品？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]空气检测、土壤采样、生物采样、环境表面采样......共十七个采样点，二十三份样品。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]我再确认一遍，二十三份样品都没有检测出任何异常？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]没有。
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]奇怪。
[name="夜刀"]我想想，前两日这片山地附近下了很大的雨，对活性源石微粒的检测或许会有所影响。
[name="夜刀"]一路上你还有注意到其他的异常状况吗？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=1)]
[name="黑角"]俺想想，那几棵折断烧焦的树算吗？
[Character(name="char_500_noirc_1",name2="avg_502_Yato_1#5$1",focus=2)]
[name="夜刀"]那大概是雨中被雷劈断的......要是这能称得上异常的话，森林里得有一头又会喷火又横冲直撞的超大怪物了。
[name="夜刀"]虽然不想承认毫无收获，但依照现有的检测结果，继续在自然采样上花时间显然效

... (全文19361字符)
```

### level_act24side_tr01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_forest",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$MH_bat_act24side_01_intro", key="$MH_bat_act24side_01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$MH_flapwing_1")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=60, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="char_500_noirc_1")]
[name="黑角"]12点钟方向——不对，4点钟方向！
[Dialog]
[playsound(key="$MH_flapwing_2")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=60, fadeout=true, block=false)]
[delay(time=1)]
[name="黑角"]又去7点钟方向了！又飞过来——
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]快举盾！
[Dialog]
[Character]
[PlaySound(key="$MH_fireballvoice")]
[delay(time=0.3)]
[PlaySound(key="$MH_fireball")]
[delay(time=0.3)]
[PlaySound(key="$MH_fireballhit")]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[delay(time=0.3)]
[PlaySound(key="$MH_fireball")]
[delay(time=0.3)]
[PlaySound(key="$MH_fireballhit")]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[delay(time=0.3)]
[PlaySound(key="$MH_fireball")]
[delay(time=0.3)]
[PlaySound(key="$MH_fireballhit")]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=false)]
[delay(time=2)]
[Character(name="avg_502_Yato_1#7$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]你没事吧？
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]还好。
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]它刚刚那是......喷火吗？
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]显而易见。
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]连石头都被烧焦了，上一次见到这样的威力还是煌的源石技艺。
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=1)]
[name="夜刀"]我敢肯定煌愿意和它打一架。
[Character(name="avg_502_Yato_1#5$1",name2="char_500_noirc_1",focus=2)]
[name="黑角"]快闪开！它又来了！
[Dialog]
[Character]
[playsound(key="$MH_flapwing_1")]
[charslot(slot="m",name="avg_npc_9998_1#1$1",duration=1)]
[playsound(key="$MH_shootdown")]
[Delay(time=2.5)]
[playsound(key="$MH_angervoice")]
[CameraShake(duration=1.5, xstrength=80, ystrength=80, vibrato=50, randomness=120, fadeout=true, block=true)]
[PlaySound(key="$MH_sweeptailvoice", volume=1)]
[PlaySound(key="$MH_sweeptail", volume=1)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",posfrom="0,0",posto="-100,0",duration=1,isblock=false)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",focus="m",afrom=1,ato=0,duration=0.5,isblock=false)]
[CameraShake(duration=0.3, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$MH_sweeptailhit")]
[delay(time=0.4)]
[Dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Character(name="avg_502_Yato_1#7$1")]
[PlaySound(key="$swordtsing4")]
[PlaySound(key="$d_avg_land_impact")]
[CameraShake(duration=1, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Characteraction(name="middle",type="move",xpos=-200,fadetime=0.4,isblock=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.1)]
[name="夜刀"]呃啊！
[Dialog]
[Character]
[charslot(slot="m",name="avg_npc_9998_1#1$1")]
[playsound(key="$MH_angervoice")]
[CameraShake(duration=0.8, xstrength=70, ystrength=70, vibrato=50, randomness=120, fadeout=true, block=false)]
[delay(time=1)]
[Dialog]
[CameraShake(duration=0.8,ystrength=60, vibrato=50, randomness=120, fadeout=true, block=false)]
[playsound(key="$MH_flapwing_2")]
[ImageTween(xFrom=0, yFrom=-40, xTo=100, yTo=600, xScaleTo=1, yScaleTo=1, duration=1, block=false)]
[Image(fadetime=0.4)]
[bgeffect]
[Delay(time=1)]
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]哈——不行。
[name="夜刀"]它的动作幅度太大，我们想要近身反击时它不是甩开我们就是飞起来......
[name="夜刀"]我们只能一直被动防御它的攻击，不能这样下去了，得想办法靠近它。
[Character(name="char_500_noirc_1")]
[name="黑角"]夜刀，快躲开——
[Character(name="avg_502_Yato_1#5$1")]
[name="夜刀"]看着呢，我没事。
[name="夜刀"]想想它的动作......位于地面的时候会左右甩尾，猛然前咬......
[Character(name="char_500_noirc_1")]
[name="黑角"]还会加速冲撞过来，一飞起来就开始喷火！
[Character(name="avg_502_Yato_1#7$1")]
[name="夜刀"]甩尾，前咬，冲锋，喷火......黑角，尾巴来了！
[Dialog]
[Character]
[charslot(slot="m",name="avg_npc_9998_1#1$1",posfrom="-50,0",posto="150,0",duration=0.6,isblock=false)]
[charslot(slot="m",name="avg_npc_9998_1#1$1",focus="m",afrom=1,ato=0,duration=0.5,isblock=false)]
[CameraShake(duration=0.3, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$MH_sweeptailvoice")]
[delay(time=0.3)]
[playsound(key="$MH_sweeptail")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Character(name="char_500_noirc_1")]
[CameraShake(duration=0.8, xstrength=70, ystrength=70, vibrato=50, randomness=120, fa

... (全文51485字符)
```

### training_act24side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动24side教学关_a

[PopupDialog(dialogHead="$avatar_nblade")] 黑角，注意戒备。这里的野兽狂躁不安，似乎受到了什么惊吓。

[PopupDialog(dialogHead="$avatar_noirc")] 俺没发现有什么异常，难道是俺吓到它们了......不应该啊。

[PopupDialog(dialogHead="$avatar_noirc")] 啊，夜刀，有个大家伙朝俺们冲过来了！
```

### training_act24side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动24side教学关_b

[PopupDialog(dialogHead="$avatar_noirc")] 这家伙......头可真硬，竟然拿岩石做外壳包住了脑袋，怎么长成这样的？

[PopupDialog(dialogHead="$avatar_nblade")] 正面进攻效果很差，太浪费时间了。

[PopupDialog(dialogHead="$avatar_nblade")] 帮我拖住它，我从背后进攻。
```

### training_act24side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动24side教学关_c

[PopupDialog(dialogHead="$avatar_noirc")] 解决了，原来它的弱点是背面。

[PopupDialog(dialogHead="$avatar_noirc")] 得把这个情报记下来，下次再遇上就好对付了。

[PopupDialog(dialogHead="$avatar_nblade")] 保持警惕。
```

### training_act24side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动24side教学关_d

[PopupDialog(dialogHead="$avatar_noirc")] 欸，刚才天上是不是突然暗了一下？

[PopupDialog(dialogHead="$avatar_nblade")] 似乎有什么飞了过去......

[PopupDialog(dialogHead="$avatar_nblade")] 周围的野兽再次躁动起来了。黑角，做好战斗准备。

[PopupDialog(dialogHead="$avatar_noirc")] 夜刀！那边！
```

### training_act24side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动24side教学关_e

[PopupDialog(dialogHead="$avatar_noirc")] 小心！它又到天上去了！

[PopupDialog(dialogHead="$avatar_nblade")] 这头生物......就没有什么弱点吗？

[PopupDialog(dialogHead="$avatar_noirc")] 俺还在找，看它的动作......

[PopupDialog(dialogHead="$avatar_noirc")] 啊！危险！
```

### training_act24side_01_f

```
[HEADER(is_skippable=true, is_autoable=false)] 活动24side教学关_f

[PopupDialog(dialogHead="$avatar_noirc")] 俺的脑袋......哎呦，好烫！

[PopupDialog(dialogHead="$avatar_nblade")] 注意！它又要来了！
```


## 统计

- 总字符数：423480
- 对话行数：3326


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
