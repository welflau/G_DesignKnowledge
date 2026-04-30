# 明日方舟 · 活动剧情 · act41side（24段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act41side」完整剧情脚本（24个文件，2589行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act41side
- 脚本文件数：24

### act41side_04

```
[header(is_skippable=false, is_tutorial=true)]
[inputblocker(blockInput=true)]
[battle.delay(time=2)]
[battle.pause(pause=true)]
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_kroos", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=4, tileX=4)]在这片奇怪的林地里，偶尔会出现某种精怪留下的<@tu.kw>空壳</>。
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_kroos", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=4, tileX=4)]而且一定是成对出现的。
[tutorial(focusWidth=120, focusHeight=120, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_kroos", tileY=3, tileX=7)]另一个<@tu.kw>空壳</>在这里。
[tutorial(protectTime=1, dialogHead="$avatar_kroos")]只要部署干员到任意一个空壳上，另一个空壳就会生长成和干员<@tu.kw>部署方向相反</>的分身，还能在攻击时造成<@tu.kw>灼燃损伤</>。
[tutorial(protectTime=1, dialogHead="$avatar_kroos")]所以，要是发现了它们，就好好利用起来吧！
[battle.pause(pause=false)]
```

### level_act41side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="crun")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="报童的声音"]号外，号外！
[name="报童的声音"]维多利亚人不战自退！
[name="报童的声音"]塔拉领土全部光复！
[name="报童的声音"]夏末节前，塔拉全境即将恢复和平！
[Dialog]
[stopsound(channel="crun", fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="59_g1_citystreets_d",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(key="$tara_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_wheelscree", channel="wh",loop=true,volume=0.5)]
[delay(time=1)]
[PlaySound(key="$d_avg_carriagebell",volume=1)]
[delay(time=1)]
[name="女性的声音"]停车。
[name="军人的声音"]我接到的命令是护送您直接去见殿下，没有逗留的时间。
[name="女性的声音"]在和她会面之前，我需要先用自己的眼睛看。姐姐的城市，战后的塔拉，那些幸存者和普通人......他们的生活终于开始了吗？
[name="军人的声音"]......如果您执意如此。
[name="军人的声音"]但塔拉人还没有做好面对两条红龙的准备——
[name="女性的声音"]我当然明白。
[Dialog]
[stopsound(channel="wh", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="59_g1_citystreets_d",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_1752_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]你就——你就收下这些吧！
[name="焦急的居民"]这些砍刀、斧头......碗盆，都是铁做的，顶好的原材料。
[name="焦急的居民"]求求你了，库林。哪怕你把它们熔了，给咱们的雕像做只眼睛呢？
[Dialog]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.7, block=true)]
[Subtitle(text="秋天已近末尾，纳斯尔纱的清晨寒凉潮湿。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一双疤痕斑驳的大手摩挲着冰冷干燥的铁器，就像在战时摩挲表彰战功的绶带。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="人们大声呼喊他的名，希望自己手中残破的物件能成为下一个被接纳的原料，熔进英雄所锻铸的雕像。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="英雄，是的，英雄......所有的故事都该有这样一位英雄。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1697_1#6$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1697_1#6$1",focus="m")]
[name="库林"]提奥，提奥！来帮忙，把东西送到工坊去！
[Dialog]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1697_1#1$1",focus="m")]
[name="库林"]提奥，你现在过来，晚上我就腾出手，教你把你的小刀再磨亮些——
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]这孩子只知道偷懒，你真是白宠他了。
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[name="库林"]......
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]不，我是说，不管提奥那小子在不在，你就把这些东西收下吧！
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[name="库林"]不行，这都是吃饭的家伙。更不用说你这条假腿了。
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[multiline(name="焦急的居民")]我——
[PlaySound(key="$d_avg_stickknock",volume=0.4)]
[PlaySound(key="$d_avg_stickknock", volume=0.4, loop=false, channel="knock",delay=0.4)]
[multiline(name="焦急的居民")]我这不是好好站着吗？
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[name="库林"]涅梅丝做的木头假腿只能救急。等城里来了更好的工匠，他们会把你的铁假腿修好的。
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]你在打造的可是纪念整个战争胜利的雕像啊，夏末节的时候会摆在城市中心的广场上的！
[name="焦急的居民"]让这条铁假腿沾沾胜利的光都不行吗？
[charslot(slot="m",name="avg_npc_1697_1#2$1",focus="m")]
[name="库林"]不行就是不行。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]你就收下吧，库林。这些东西都是大家打扫房屋清出来的旧东西，用不上的。
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[name="库林"]碗盆怎么会用不上？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]铁碗没了还有陶的，至于斧头砍刀，大家匀着用就行了。
[name="友善的居民"]刚打完仗，城里什么都缺。我们不来帮你一把，难道眼看着雕像不能完工？
[charslot(slot="m",name="avg_npc_1697_1#2$1",focus="m")]
[name="库林"]......
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[name="库林"]只有旧义肢，我无论如何都不能收。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]你什么都好，我的大英雄，可你就是个死脑筋！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.7,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot="m",name="avg_npc_1694_1#1$1",duration=1)]
[delay(time=2)]
[charslot]
拉芙希妮缓缓走入人群。
不知为何，她觉得自己和这些人中间隔着什么，仿佛在看篝火对面的人。
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]请问大家这是在做什么？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]新面孔？最近可不多见了！瓦伊凡，你从哪儿来？
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]我从很远的地方回到塔拉。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]库林，你看，你早点收下这些东西，也不至于被远道而来的同胞看了笑话。
[charslot(slot="m",name="avg_npc_1697_1#8$1",focus="m")]
[name="库林"]还是那句话，别的算了，假腿不行。
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[name="拉芙希妮"]为什么大家连锅碗瓢盆和......假肢，都拿出来了？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]因为我们要在夏末节的时候在广场上立起一座雕像，庆祝塔拉的新生。
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]你们要过夏末节？
[name="拉芙希妮"]我只在塔拉的传说中见到过这个名字，一个在秋天丰收之后，冬天到来之前庆祝的，连通此岸与彼岸的节日。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]你懂得很多啊，瓦伊凡！
[name="友善的居民"]原本大家只知道秋收之后要庆祝丰收，还是深池的人告诉我们，这是有来历的。
[name="友善的居民"]打扫房屋，设宴待客，最重要的是点起篝火，在生与死交汇的这一天款待所有赴宴的人......能做的事情可太多了！
[name="友善的居民"]加上这是塔拉重获新生以来的第一个夏末节，庆祝就更要隆重。
[name="友善的居民"]多亏这一点，不然库林就算把自己家拆了，也不会愿意收我们的东西的。
[name="友善的居民"]这么说来，你要不要也拿点铁做的东西，让英雄给你熔了锻进雕像里去？
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]我身上只有一枚书签，似乎是铁制的，可以吗？
[charslot(slot="m",name="avg_npc_1697_1#1$1",focus="m")]
[name="库林"]归乡的同胞，她说了不算。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]哈哈......
[charslo

... (全文24042字符)
```

### level_act41side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g3_dragonsquare_d",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$tara_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",posfrom="200,0",posto="0,0",afrom=0,ato=1,duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",posfrom="0,0",posto="-150,0",duration=1)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",afrom=1,ato=0,duration=0.7,isblock=true)]
[Delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]（小声）......抱歉了。
[name="拉芙希妮"]女士，请留步。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",duration=0.5)]
[Delay(time=0.7)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]哦，苇草，是你！你之前突然离席，我还以为是我们的招待有什么不周到的地方呢。
[charslot(slot="m",name="avg_npc_1694_1#9$1",focus="m")]
[name="拉芙希妮"]......不，我很感谢你们的款待，只是当时突然想起还有事。现在我还有一些问题，能请您为我解答吗？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]行，你问吧。
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]你知道自己身上正燃烧着火焰吗？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]火？你是说祝福？真奇怪，你居然能看见其他人身上的祝福？
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[multiline(name="拉芙希妮")]我也是被人提醒，这才意识到的——
[charslot(slot="m",name="avg_npc_1694_1#6$1",focus="m")]
[multiline(name="拉芙希妮")]等等，你是说，你知道，但你们都看不见？这怎么可能呢？
[Dialog]
[charslot]
居民将手伸向自己腰间。
为了驱散沼泽中的黑雾，塔拉人的祖先会在腰间挎上一朵以源石技艺固定住的小小的火焰。
这样的习俗在维多利亚彻底掌控塔拉后被严令禁止。
时移世异，不必再顾及维多利亚禁令的塔拉人，至少是纳斯尔纱人，选择在腰间挎上小巧的源石灯。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]你也知道燃料不够，加上宵禁存在，所以源石灯我们开不起，也不必开。不过......只要像这样......
[Dialog]
[charslot(slot = "m", name = "avg_npc_1688_1#1$1",focus="m")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1688_1#1$1",posfrom = "0,0", posto = "200,0",focus="l")]
[charslot(slot = "m", name = "avg_npc_1688_1#4$1",duration=1.5,focus="all")]
[delay(time=3)]
[charslot(slot="m",name="avg_npc_1694_1#6$1",focus="m")]
[name="拉芙希妮"]是她的火......在这灯上显出了颜色......
[Dialog]
[charslot(slot = "m", name = "avg_npc_1688_1#4$1",focus="m")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=false)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1688_1#4$1",posfrom = "0,0", posto = "200,0",focus="l")]
[charslot(slot = "m", name = "avg_npc_1688_1#1$1",duration=1,focus="all")]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]现在城里人一开灯就是这个颜色，换了别的颜色的元器件也一样。
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[name="拉芙希妮"]你们难道不担心吗？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]你也看到了，现在纳斯尔纱一切向好，所以这只能是红龙的祝福，不会有别的解释了。
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[name="拉芙希妮"]可是——
[Dialog]
[charslot]
可是？
可是一个鲁莽的归乡者，要告诉她这火的存在与不祥勾连？她不会相信的。
也许直接一些的办法反而会奏效，拉芙希妮在心中如此祈祷。
[charslot(slot="m",name="avg_npc_1694_1#9$1",focus="m")]
[name="拉芙希妮"]可是我也想感受一下“红龙的祝福”，所以......我能握一下您的手吗？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]但你都进城了，城市里的人迟早会得到的呀。
[charslot(slot="m",name="avg_npc_1694_1#9$1",focus="m")]
[name="拉芙希妮"]只是个小小的心愿。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]唉，特意回到塔拉来，你也不容易。
[name="友善的居民"]对了，你是做什么的？
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]我......我会一些医疗手段，我的源石技艺可以辅助我，仅此而已。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]原来你是个医生，城里正需要医生呢。
[name="友善的居民"]来吧，让我们握手——
[Dialog]
[charslot(duration=0.5)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1)]
[PlaySound(key="$p_field_magloop",channel="2", volume=0.8,loop=true)]
[stopsound(channel="2",fadetime=2.5)]
[Delay(time=2)]
她握紧女人掌心结着老茧的手，同时让火从自己的手腕处向着对方蔓延。
[charslot(slot="m",name="avg_npc_1694_1#9$1",focus="m")]
[name="拉芙希妮"]谢谢您......
[Dialog]
[charslot]
她闭上眼。
闭上眼，去回忆那些曾被自己抚平痛苦，不再被迫滞留人世的对象——
去温暖这冰冷的火。
[stopmusic(fadetime=1.5)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]呃......
[Dialog]
[charslot]
紫色的火逐渐褪去。在那之下，苍白的、摇曳着友善笑容的面庞慢慢清晰起来。
于是她试图将更多紫色的部分消去，却没能及时看见女人面色陡变的一瞬。
[playMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]天啊，我——
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="友善的居民"]我的手——你对我的手做了什么？我的手没知觉了！
[charslot(slot="m",name="avg_npc_1694_1#6$1",focus="m")]
[name="拉芙希妮"]什么？！
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[multiline(name="友善的居民")]还有我的祝福，也感受不到了！你到底在做什么？
[PlaySound(key="$d_avg_clothmovementsp",volume=0.8)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="友善的居民")]放开我！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(slot="m",name="avg_npc_1692_1#7$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="“守灵人”"]苇草！
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[name="拉芙希妮"]“守灵人”？
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="“守灵人”"]苇草小姐，请先放开这位可怜的女士。
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[name="拉芙希妮"]我——
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[name="“守灵人”"]（摇头）
[Dialog]
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=1.5)]
[charslot(duration=0.5)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1692_1#9$1",focus="m")]
[name="“守灵人”"]抱歉，女士。
[name="“守灵人”"]这位苇草小姐没有恶意，我以我的人格担保。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]可她说她是医生，医生怎么会...

... (全文20676字符)
```

### level_act41side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g1_citystreets_d",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="cr")]
[SoundVolume(volume=0.4, channel="cr",fadetime=2)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1695_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_1696_1#1$1",duration=0.7)]
[Delay(time=1.5)]
[charslot]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1686_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_1689_1#1$1",duration=0.7)]
[Delay(time=1.5)]
[charslot]
[PlaySound(key="$d_avg_footstep_stonestep",volume=1,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot="m",name="avg_npc_240",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]......嗯？
[name="提奥"]好多人......
[name="提奥"]抱歉！呃......请让一让——
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(duration=0.5)]
[name="提奥"]——啊！
[Dialog]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1687_1#1$1",focus="m")]
[name="急切的居民"]——米林顿街我也去过了，早就什么也没有了！虽然店门都开着，但货架全是空的，连个袋子都没剩下！
[name="急切的居民"]克拉马那家伙说这边有库存，我才跑了五条街过来——结果还是连根羽兽毛都看不见！
[name="急切的居民"]我还不如回去拿上弩，翻出岗哨去，到黑林里打点猎，兴许还能在饿死之前见点真正的荤腥......
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]......什么？
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="愤怒的居民"]我看你是真饿糊涂了，去黑林才真的是去送死！
[charslot(slot="m",name="avg_npc_1687_1#1$1",focus="m")]
[name="急切的居民"]你不糊涂！说得像你就知道什么了一样！
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="愤怒的居民"]怎么不知道？拉格兰街的粮店，艾玛开的，你知道吧？
[charslot(slot="m",name="avg_npc_1687_1#1$1",focus="m")]
[name="急切的居民"]那家我还没去呢，怎么了？
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="愤怒的居民"]我先去的那里。虽然也没粮食，但听艾玛的意思，这事和*维多利亚粗口*的维多利亚人脱不开干系！
[charslot(slot="m",name="avg_npc_1687_1#1$1",focus="m")]
[name="急切的居民"]维多利亚的混蛋封锁我们，这又不是第一天了，他们当然该负责。这有什么新鲜的？
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="愤怒的居民"]维多利亚的间谍已经渗透到纳斯尔纱来了！
[charslot(slot="m",name="avg_npc_1687_1#1$1",focus="m")]
[name="急切的居民"]你再说一遍？！
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="愤怒的居民"]艾玛去农业地块的时候亲眼看见了着过火的痕迹，深池还在排查呢！
[charslot(slot="m",name="avg_npc_1687_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="急切的居民"]*维多利亚粗口*！塔拉独立之后我们就该马上打回去！
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="愤怒的居民"]不过有句话你说对了，你确实该回去拿上你的弩，但不是为了打猎，而是为了揪出那些替维多利亚人办事的叛徒！
[name="愤怒的居民"]虽然如果让我抓到他，肯定不是用弩箭穿心这么简单就结束了。
[Dialog]
[charslot]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=1.5)]
[charslot(slot="m",name="avg_npc_240",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]（小声）好像是这些店里的粮食供应断了......
[name="提奥"]（小声）虽然我给库林先生囤了一些土豆，但可能还是不够......
[name="提奥"]（小声）这里人太多了，还是走另一条路吧。
[name="提奥"]（小声）还有好多人都拿着武器......
[name="提奥"]（小声）他们是想围剿维多利亚间谍吗？城里没有粮食......跟维多利亚人也有关系吗？
[name="提奥"]（小声）但我......
[name="提奥"]（小声）我......
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]我没关系的。我是库林先生的学徒。大家都知道这件事。
[name="提奥"]别害怕，提奥。大家不会拿你怎么样的。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(duration=1)]
提奥努力矮下身子，从人群中挤出去，来到街道的拐角处。他灵活地从一条狭窄暗道里穿过，来到石砖墙体的另一面。
嘈杂的人声逐渐从他耳边退去。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopsound(channel="cr", fadetime=1)]
[charslot]
[Background(image="59_g1_citystreets_d",screenadapt="showall")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]......你看，提奥，没人找你的麻烦。
[name="提奥"]库林先生肯定还在忙红龙雕像的事，等他回过神来，其他店里肯定也什么都不剩了。
[name="提奥"]我得帮忙。
[Dialog]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step1",loop=false)]
[stopsound(channel="step1",fadetime=3)]
[charslot(duration=1)]
[Delay(time=1.5)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g10_indoor",screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[name="库林"]你们先把这些东西拿去吃，分给周围的邻居，让他们不要急。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]那你自己怎么办？还有涅梅丝，她会不会没得吃？
[name="友善的居民"]比起把粮食都给我们，你不如跟那些人一起去抓维多利亚间谍。要不然没法从根本上解决问题，是不是？
[charslot(slot="m",name="avg_npc_1697_1#9$1",focus="m")]
[multiline(name="库林")] ......我会去的，也麻烦你这样告诉其他人。
[charslot(slot="m",name="avg_npc_1697_1#10$1",focus="m")]
[multiline(name="库林")]这些东西你们也先拿着。
[name="库林"]涅梅丝在领袖的身边，为你们吃些苦也是应该的。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]那我......那我就不跟你客气了！
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]......库林，你肯定还有别的存粮，是不是？
[name="阴沉的居民"]而且，你怎么知道粮食会断供？是不是涅梅丝提前跟你说了什么——
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]罗里，你说什么呢！
[charslot(slot="m",name="avg_npc_1697_1#8$1",focus="m")]
[name="库林"]你不要就算了。
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]有谁能证明你或者涅梅丝不是间谍？你们合起伙来养大了一个维多利亚人的孩子！
[charslot(slot="m",name="avg_npc_1697_1#8$1",focus="m")]
[name="库林"]......滚。
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]我凭什么滚？你心虚什么？你——
[Dialog]
[charslot]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[charslot(

... (全文16295字符)
```

### level_act41side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_paper2", volume=1)]
[name="拉芙希妮"]每一条有人住的街道都走过了，没有提奥的下落，只看到城里人身上的火......越来越旺盛，就好像忽然起风了一样......
[name="拉芙希妮"]而且每个人都习以为常，祛除火焰只会让他们陷入惊恐，觉得没了火的部分在离自己远去......
[name="拉芙希妮"]难道纳斯尔纱人真的已经......？
[name="拉芙希妮"]......不，先别想那些，孩子要紧。该去碰碰涅梅丝说过的那位游牧民布莉吉了。
[name="拉芙希妮"]但......真有人会因为进不去黑林，就在城门外搭帐篷吗？
[Dialog]
[PlaySound(key="$d_avg_paper1", volume=1)]
[delay(time=1)]
[name="拉芙希妮"]“沿着岗哨右边走出去，蹚过小河”......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_campsite_d",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]啊，好像到了。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4177_brigid_1#11$1",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="l",name="avg_npc_1694_1#1$1",focus="l")]
[name="拉芙希妮"]金色头发的佩洛，高高大大，但很灵巧。
[name="拉芙希妮"]这应该就是涅梅丝说的“布莉吉”——
[Dialog]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot="r",name="avg_4177_brigid_1#11$1",posfrom="200,0",posto="0,0",duration=1)]
[delay(time=1.5)]
[charslot(slot="r",name="avg_4177_brigid_1#11$1",focus="r")]
[name="布莉吉"]你认识我？
[charslot(slot="l",name="avg_npc_1694_1#9$1",focus="l")]
[name="拉芙希妮"]不，我们从前应该没见过，是涅梅丝让我来找你的。我叫苇草。
[charslot(slot="r",name="avg_4177_brigid_1#11$1",focus="r")]
[name="布莉吉"]你......
[Dialog]
[charslot(slot = "r", posfrom="0,0", posto="-100,0", duration=0.7)]
[delay(time=1)]
[PlaySound(key="$d_avg_catsmell", volume=1)]
[Delay(time=1)]
拉芙希妮只看见对方往自己身前凑过来，鼻子翕动了两下，还以为这是什么游牧民的招呼方式。
[Dialog]
[charslot(slot = "r", posfrom="-100,0", posto="0,0", duration=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_npc_1694_1#9$1",focus="r")]
[charslot(slot="r",name="avg_4177_brigid_1#11$1",focus="r")]
[name="布莉吉"]你不是城里那条红龙。
[charslot(slot="l",name="avg_npc_1694_1#11$1",focus="l")]
[name="拉芙希妮"]你在说什么？我不是红龙，我只是——
[charslot(slot="r",name="avg_4177_brigid_1#8$1",focus="r")]
[name="布莉吉"]你不是城里那条红龙，你是另一条红龙。另一条红龙回到城市里......好耳熟的故事。
[charslot(slot="l",name="avg_npc_1694_1#11$1",focus="l")]
[name="拉芙希妮"]你只是闻了闻，就......？
[charslot(slot="r",name="avg_4177_brigid_1#9$1",focus="r")]
[name="布莉吉"]是啊，你身上的火的味道和城里那条红龙一点都不一样。
[name="布莉吉"]不过这都不重要。苇草，你来找我做什么？
[charslot(slot="l",name="avg_npc_1694_1#1$1",focus="l")]
[name="拉芙希妮"]提奥失踪了，听说你回城的时候常找他聊天，所以涅梅丝让我来问问你。
[charslot(slot="r",name="avg_4177_brigid_1#5$1",focus="r")]
[name="布莉吉"]提奥失踪了？！
[charslot(slot="l",name="avg_npc_1694_1#1$1",focus="l")]
[name="拉芙希妮"]提奥今天早上出去就没回家，今天城里又乱作一团。先是涅梅丝，然后是我，我们找遍了整个纳斯尔纱，都找不到他的下落。
[charslot(slot="r",name="avg_4177_brigid_1#11$1",focus="r")]
[name="布莉吉"]可我离开纳斯尔纱之前还去找过他，他那时候还好好的——
[charslot(slot="r",name="avg_4177_brigid_1#8$1",focus="r")]
[name="布莉吉"]不，他那时候的情况也算不上好。
[name="布莉吉"]不管怎么说，我找了提奥之后去了趟堡垒，然后就出了城，在那之后就没见过提奥的影子。
[charslot(slot="r",name="avg_4177_brigid_1#7$1",focus="r")]
[name="布莉吉"]该死，他现在到底在哪儿？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_ltstrongpoint",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4177_brigid_1#4$1",focus="m")]
[name="布莉吉"]提奥——提奥！
[charslot(slot="m",name="avg_4177_brigid_1#7$1",focus="m")]
[name="布莉吉"]该死，我当时就该直接把他打晕，扛在肩上带走的。
[charslot(slot="m",name="avg_4177_brigid_1#4$1",focus="m")]
[name="布莉吉"]提奥，说话！这回你必须跟我走了，提奥！
[charslot(slot="m",name="avg_npc_1694_1#11$1",focus="m")]
[name="拉芙希妮"]布莉吉，这里是......？
[charslot(slot="m",name="avg_4177_brigid_1#10$1",focus="m")]
[name="布莉吉"]战争期间这处地块曾经被拖出去，据说是平定哪里的贵族什么的，拖回来就这样了，挂在纳斯尔纱上，一直也没人修。
[name="布莉吉"]提奥一受了什么委屈就爱往这儿跑。
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]或许提奥真的出城了？
[charslot(slot="m",name="avg_4177_brigid_1#8$1",focus="m")]
[name="布莉吉"]......我只见过一个出城的人，就是拉格兰街的艾玛。当时没看见提奥和她一起离开。
[name="布莉吉"]而且她一个人押着好多东西在黑林外面和人碰了头，那人把东西拉走，她就一个人回来了。
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]她没注意到你？
[charslot(slot="m",name="avg_4177_brigid_1#10$1",focus="m")]
[name="布莉吉"]城里人的眼睛耳朵鼻子都不好使。再说我们离得远着呢。
[charslot(slot="m",name="avg_npc_1694_1#1$1",focus="m")]
[name="拉芙希妮"]好多东西出去，一个人回来......她哪来的东西？
[name="拉芙希妮"]艾玛是做什么的？
[charslot(slot="m",name="avg_4177_brigid_1#10$1",focus="m")]
[name="布莉吉"]她经营一家粮店，我去那里送过信。
[charslot(slot="m",name="avg_npc_1694_1#8$1",focus="m")]
[name="拉芙希妮"]粮店......出城......现在闭门不出......
[charslot(slot="m",name="avg_npc_1694_1#7$1",focus="m")]
[name="拉芙希妮"]现在也只有这么点线索了。我们赶紧过去。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="59_g1_citystreets_d",screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1694_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_4177_brigid_1#11$1",duration=0.7)]
[delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]布莉吉？苇草？
[charslot(slot="m",name="avg_npc_1694_1#9$1",focus="m")]
[name="拉芙希妮"]你好，请问你有没有看见提奥？
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]提奥？涅梅丝把这事交给你了？
[charslot(slot="m",name="avg_npc_1694_1#9$1",focus="m")]
[name="拉芙希妮"]是的。
[charslot(slot="m",name="avg_npc_1688_1#1$1",focus="m")]
[name="友善的居民"]没。天知道那小子又跑哪儿去了，别是跟着烧了农业地块的间谍一起跑了才好。
[charslot(slot="m",name="avg_4177_brigid_1#4$1",focus="m")]
[name="布莉吉"]你！
[charslot(slot="m",name=

... (全文20780字符)
```

### level_act41side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g2_citystreets_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$ghosthunter_intro",key="$ghosthunter_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_insectfly", volume=1)]
[delay(time=1.5)]
一只甲虫低低飞过黑暗弥漫的街巷。
它奋力振翅，却只不过闯进了一片几乎无人踏足的废弃街区。
纯金做的身躯太重，翅膀上的宝石也对飞翔无益。它飞了短短一点距离，就不得不趴在石板中间的缝隙处休息——
[Dialog]
[PlaySound(key="$runsand", volume=1)]
[charslot(slot = "m",name="avg_npc_246",posfrom = "100,0", posto = "0,0",duration =1)]
[delay(time=1.2)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot = "m", posfrom="0,0", posto="-80,0", afrom=1, ato=0, duration=0.7)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[name="“官僚”"]让你再跑！
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[name="“官僚”"]抓住了，抓住了！
[Dialog]
[playsound(key="$d_avg_crowdtalk_fear", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=1, channel="bgs",fadetime=2)]
[delay(time=1.5)]
[name="“酷吏”"]抓住你那破虫子就快去帮我捡水晶！快滚进阴沟里了！
[name="“官僚”"]我这就来——
[name="“官僚”"]不对，我要是帮你捡，你是不是得分我点什么？
[name="“酷吏”"]分，分！你先来帮我捡！水晶滚进阴沟里，你难道不心疼？
[name="“拷问者”"]哈哈，我的好云兽，这下你是我的了！
[name="“监察官”"]剑上的宝石......还好，还好，一个都没碰落......
[name="“拷问者”"]“校官”他们呢？
[name="“官僚”"]管他们干什么？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
官僚把蛀虫藏进怀里，酷吏不厌其烦地看着泪滴一次又一次滑落。
拷问者粗鲁地摆弄云兽的肢体，监察官举起那柄剑，仿佛手执生杀的权力......
[Dialog]
[stopSound(fadetime=2,channel="bgs")] 
[delay(time=1)]
[charslot(slot = "m",name="avg_450_necras_1#13$2",duration =1)]
[delay(time=1.5)]
[charslot(slot = "m",name="avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]......呵，真热闹啊。
[charslot(slot = "m",name="avg_450_necras_1#1$2",focus="m")]
[name="爱布拉娜"]我当然可以把这些财宝赐给你们，我的仆臣们。
[name="爱布拉娜"]你们喜欢这些东西到这种地步，要是不满足你们，不解风情的反倒是我了。
[name="爱布拉娜"]可我把这些给了你们之后，你们又想从我手中拿走什么呢？
[charslot(slot = "m",name="avg_450_necras_1#6$2",focus="m")]
[name="爱布拉娜"]让我猜猜......
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[charslot]
[Image(image="59_i03",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=1)]
[ImageTween(xFrom=-240, yFrom=70, xTo=0, yTo=0, xScaleFrom=1.4, yScaleFrom=1.4, xScaleTo=1, yScaleTo=1, duration=25, block=false)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]
不知为何，原本断了头的小巷中凭空生出一条路来，更多璀璨夺目的东西朝着路的尽头涌去。
人们已经无暇抚弄手里的东西了。
他们把地上的财宝捡起来，塞进口袋，或是背在身上，连腰都来不及直起来，就奔向下一个闪闪发光的地方。
没人关心这条路通往何方。
[name="官僚"]
[name="官僚"]......明天我就去多索雷斯，倒腾了那么多货，我早该给自己买点东西了......
[name="酷吏"]......纳斯尔纱这帮乡巴佬，该再榨一榨他们的油水......
[name="监察官"]......别忘了分我些......
[name="拷问者"]......等城里人真把“维多利亚间谍”送到我这儿来......
[Dialog]
[Delay(time=1)]
[name="爱布拉娜"]哈，听听，你们贪图的何止是财宝啊。
[name="爱布拉娜"]优渥的生活，高贵的地位，横流的物欲，生杀的权柄......你们都想要。
[name="爱布拉娜"]我不讨厌忠于自己欲望的人，你们要的东西，送人也没什么可惜。
[name="爱布拉娜"]可唯一不巧的是，你们是我的仆臣，而你们似乎比我还贪婪得多。
[name="爱布拉娜"]......再见，去你们该去的地方吧。
财宝于无路处凭空铺成一条闪闪发光的路，送彻底癫狂的人群走出巢穴，走上大地......
走向黑暗的来处，那残忍地张开大口的黑林。
[Dialog]
[focusout(duration=2, type="cg", from=0, to=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1.5)]
[focusout(duration=0.1, type="cg", from=1, to=0, block=true)]
[charslot]
[image]
[Background(image="bg_snowconutryinside", screenadapt="coverall", block=true)]
[focusout(duration=0.1, type="bg", from=0, to=1, block=true)]
[Delay(time=2)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[focusout(duration=1.5, type="bg", from=1, to=0, block=true)]
[Delay(time=1)]
[name="神秘的女性"]......这一段，和您之前讲的东西，风格完全不同。
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="m")]
[name="作家"]我早就说过，观察、灵感、写作过程中废掉的文本，我会一股脑抛出来。
[name="作家"]如果我真的能将这个故事完完整整地用统一的风格讲完，那我也不用在这里喝馊掉的啤酒了。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[name="作家"]非要给故事一个结局的人是你，不是我。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="n")]
[name="神秘的女性"]的确如此。
[name="神秘的女性"]不过，如果我非要把这一段当成您的创作，是不是可以说，前面那位布莉吉小姐被黑雾拒绝也算是创作？
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="m")]
[name="作家"]......至少不比你硬塞到故事里的“放逐王”更“创作”。
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="n")]
[name="神秘的女性"]那么，接下来您要讲的，又到底是观察，还是创作呢？
[charslot(slot="m",name="avg_npc_1698_1#5$1",focus="m")]
[name="作家"]如果你愿意，就自己去区分。你到底还想不想让我讲下去？
[Dialog]
[charslot]
[name="神秘的女性"]当然，当然......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g10_indoor",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[focusout(duration=0.1, type="bg", from=0, to=1, block=true)]
[delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[focusout(duration=1.5, type="bg", from=1, to=0, block=true)]
[delay(time=1)]
[CameraEffect(effect="Grayscale", fadetime=1.5, keep=true, initamount=0.7, amount=0, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1694_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_4177_brigid_1#11$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_4177_brigid_1#11$1",focus="r")]
[name="布莉吉"]艾玛她到底怎么了？
[charslot(slot="l",name="avg_npc_1694_1#1$1",focus="l")]
[name="拉芙希妮"]只是轻微的营养不良，外加受了风寒。
[charslot(slot="r",name="avg_4177_brigid_1#11$1",focus="r")]
[name="布莉吉"]她在黑林外边的时候，看起来可没病这么重啊。
[charslot(slot="l",name="avg_npc_1694_1#1$1",focus="l")]
[name="拉芙希妮"]......多半是心病。
[name="拉芙希妮"]打造雕像的铁要挨家挨户收集，人们为

... (全文15388字符)
```

### level_act41side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g3_dragonsquare_d",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_240",posfrom="100,0",posto="0,0",duration=0.7,isblock=false)]
[delay(time=1)]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="-150,0",afrom=1,ato=0,duration=1,isblock=false)]
[delay(time=1.5)]
[charslot]
[PlaySound(key="$d_avg_punchsp3",volume=0.8)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.6)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="m",name="avg_npc_240",duration=0.5)]
[name="提奥"]哎哟！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1686_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]是谁——提奥？你不看路的吗？
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]抱、抱歉！罗里先生，我想去拉格兰街碰碰运气，看能不能买到点土豆——
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阴沉的居民"]滚开！
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="提奥"]抱歉......
[Dialog]
[charslot]
[playsound(key="$d_avg_pcknmgrwl", volume=1)]
[delay(time=1)]
[name="车夫的声音"]小心！驮兽受惊了！快躲开！
[Dialog]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_pcknmrn",volume=0.6)]
[PlaySound(key="$d_avg_carriage_loop", volume=1, loop=true, channel="ca")]
[StopSound(channel="ca", fadetime=4)]
[CameraShake(duration=3.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[PlaySound(key="$d_avg_doorbreak", volume=0.8)]
[PlaySound(key="$bodyfalldown1", volume=1,delay=0.3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot(duration=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]赶车的，你疯了吗，你差点撞死我！给我停下！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_pcknmrn",channel="step1",loop=false, volume=0.4)]
[PlaySound(key="$d_avg_carriagegoaway",channel="step2",loop=false, volume=1,delay=0.2)]
[stopsound(channel="step1",fadetime=4)]
[stopsound(channel="step2",fadetime=4)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]居然就这么跑了？！
[Dialog]
[charslot]
[name="提奥"]罗里先生，我......
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]哈，哈哈，真是恶有恶报，被撞的居然是你？
[name="阴沉的居民"]走，小子，这下你哪也去不了了，跟我去见深池的人，我要把你这个叛徒交给他们，这样我就有土豆可以——
[name="阴沉的居民"]不对，不能走大路！万一这个间谍被其他人抢走......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[CameraShake(duration=1, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
男人一把拎起男孩的领子，不顾男孩痛苦的呻吟，拖着他走向平日无人经过的小巷深处。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="59_g1_citystreets_d",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]也真的是邪门，为什么还是走不出去？难道我记错路了？
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="n")]
[name="遥远的争吵声"]别抢！把土豆还我！你自己去粮店买，你看那里还有剩下的......
[name="遥远的争吵声"]还给我！！
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]还有剩下的？！
[Dialog]
[charslot]
男人看向声音传来的方向，又看了看一条胳膊攥在自己手里，几乎已经没了人样的男孩。
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]快死了......快死了还能从他嘴里撬出来情报吗？深池的老爷们还能愿意给我口吃的吗？
[name="阴沉的居民"]......叛徒，算你运气好。
[Dialog]
[stopmusic(fadetime=1.5)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[CameraShake(duration=0.7, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(duration=1.5)]
[Delay(time=2.5)]
男人甩开孩子那反而抓紧了自己袖口的手，快步跑向声音传来的方向。
[Dialog]
[charslot]
[name="提奥"]好痛......我的腿......
[Dialog]
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
[delay(time=1.5)]
[name="提奥"]不行，站不起来......
[Dialog]
[charslot(slot="m",name="avg_npc_1696_1#1$1",duration=1)]
[delay(time=2)]
[Dialog]
[charslot]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[name="提奥"]艾玛阿姨......
[charslot(slot="m",name="avg_npc_1696_1#1$1",focus="m")]
[name="担忧的居民"]......谁叫我？谁？！
[name="担忧的居民"]我已经照你说的做了，我已经做了！别再来缠着我了——
[Dialog]
[charslot]
[name="提奥"]艾玛......阿姨！
[charslot(slot="m",name="avg_npc_1696_1#1$1",focus="m")]
[name="担忧的居民"]提奥？你怎么了？
[Dialog]
[charslot]
[name="提奥"]我被驮兽车给撞了，然后又被人丢到了这里。
[name="提奥"]我不是维多利亚人的间谍，艾玛阿姨。求你救救我，带我去找库林先生，好吗？
[charslot(slot="m",name="avg_npc_1696_1#1$1",focus="m")]
[name="担忧的居民"]维多利亚人......间谍？
[name="担忧的居民"]原来这么快啊......
[Dialog]
[charslot]
[name="提奥"]艾玛阿姨，我好痛，真的好痛。
[name="提奥"]我知道维多利亚人害了大家，大家都不喜欢我，没人愿意听我说话，更没人愿意碰我。
[name="提奥"]可是能不能......至少把库林先生叫过来，我好痛，而且好冷......
[name="提奥"]艾玛阿姨，等我长大了，我会去找维多利亚人报仇的，我会去替尼亚尔叔叔......报仇的。
[charslot(slot="m",name="avg_npc_1696_1#1$1",focus="m")]
[name="担忧的居民"]（深呼吸）
[name="担忧的居民"]提奥，如果死的只有尼亚尔，也许我会帮你。
[Dialog]
[charslot]
[name="提奥"]艾玛......阿姨？
[charslot(slot="m",name="avg_npc_1696_1#1$1",focus="m")]
[name="担忧的居民"]你只知道尼亚尔死在战争里，可还有更多人，他们没上战场，也死掉了。
[name="担忧的居民"]因为你们维多利亚人封锁了商路，直到现在还在封锁，所有人都在挨饿，包括我，包括......
[name="担忧的居民"]尼亚尔留给我的......我肚子里的孩子。
[name="担忧的居民"]他也饿死了，被你们维多利亚人活活

... (全文15474字符)
```

### level_act41side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g3_dragonsquare_d",screenadapt="coverall", block=true)]
[backgroundTween(xFrom=100, yFrom=0, xTo=-100, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=35, block=false)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15,grad = false,fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15,grad = false,fadetime=0.1)]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[PlaySound(key="$d_avg_woodcracle", volume=0.8, loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
成百上千年前，塔拉人的先祖也曾这样，在秋末冬初的旷野上点起一簇又一簇篝火。
那时他们依偎着红龙睡下，他们炽热的梦被风沙打磨得粗粝，却仍然足以温暖彼此的身躯。
当他们醒来时，篝火不会熄灭，因为红龙不眠。
只是呼吸着那些从篝火里悠悠升上天空的，关于家园、美酒与自由的梦，红龙便能从疲惫与苦痛中得到片刻休憩。
而今天，夏末节又要到了，人们去附近拆下废墟里的木料点起篝火，却全然忘记了那古老、闲适、宛如永恒的时光。
[dialog]
[StopSound(channel="a", fadetime=2)]
[curtain(fadetime=1)]
[delay(time=2)]
[Background(image="59_g3_dragonsquare_d",screenadapt="coverall",fadetime=1.5,block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1695_1#1$1",focus="m")]
[name="狂热的居民"]把手放到火上。
[charslot(slot="m",name="avg_npc_1752_1#4$1",focus="m")]
[name="焦急的居民"]你看我腰上灯的颜色，我是塔拉人，我受过红龙的祝福。
[charslot(slot="m",name="avg_npc_1695_1#1$1",focus="m")]
[name="狂热的居民"]难道间谍想不到要伪造灯的颜色吗？别磨磨蹭蹭的！
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]愿......
[name="焦急的居民"]愿红龙垂怜！
[dialog]
[charslot]
[PlaySound(key="$d_avg_woodcracle", volume=1, loop=true, channel="b")]
[StopSound(channel="b", fadetime=3)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]唔......也......不是很痛。
[charslot(slot="m",name="avg_npc_1695_1#1$1",focus="m")]
[name="狂热的居民"]真的不痛？
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]你看，甚至连烧伤的痕迹都不太明显。
[charslot(slot="m",name="avg_npc_1695_1#1$1",focus="m")]
[name="狂热的居民"]那你就不是维多利亚间谍。你周围还有谁没来这儿试验过？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Background(image="59_g3_dragonsquare_d",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="寡言的居民"]......
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]你，就是你，你去那边烧过手吗？
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="寡言的居民"]......
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]说句话，别摸你那脏兮兮的破绳结了！跟我走！
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[CameraShake(duration=0.5, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="焦急的居民"]我让你跟我走！把绳结放下——
[Dialog]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=0.6)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]你——你打我？！
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[name="寡言的居民"]绳结......你敢......
[charslot(slot="m",name="avg_npc_1752_1#1$1",focus="m")]
[name="焦急的居民"]算了，我不抢你的绳结，跟我去那边，看看你是不是维多利亚间谍！
[Dialog]
[charslot(slot="m",name="avg_npc_1689_1#1$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(duration=1)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Delay(time=2)]
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_crowdtalk_fear", loop=true, channel="bgs",volume=0.8)]
[PlaySound(key="$d_avg_woodcracle", volume=0.6, loop=true, channel="c")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
寡言的居民默默站起身，迈着不大利索的步伐往篝火的方向走去。
广场已经被彻底的混乱占据。
只不过，一半的混乱来自怀疑、仇恨和得不出任何结果的暴怒，另一半却来自绝望的眼神和死一般的寂静......
[Dialog]
[StopSound(channel="bgs", fadetime=3.5)]
[StopSound(channel="c", fadetime=3.5)]
[delay(time=1)]
[PlaySound(key="$d_avg_reddragonstatue",volume=0.3)]
[PlaySound(key="$d_avg_reddragonstatue", volume=0.3, loop=false, channel="red",delay=2)]
[PlaySound(key="$d_avg_reddragonstatue", volume=0.6, loop=false, channel="red1",delay=4)]
[delay(time=2.5)]
直到远处微细的拖拽声传来。
[PlaySound(key="$d_avg_reddragonstatue",volume=1)]
那声音越来越大，越来越大，直到盖过一切嘈杂与混乱。
所有人都听见了巨物被人拖拽，逐渐接近的声音。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.1, block=true)]
[charslot]
[Image(image="59_i04",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=1)]
[ImageTween(xFrom=180, yFrom=-60, xTo=0, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1, yScaleTo=1, duration=20, block=false)]
[playMusic(intro="$ghosthunter_intro",key="$ghosthunter_loop", volume=0.6)]
[PlaySound(key="$d_avg_reddragonstatue",volume=0.6)]
[PlaySound(key="$d_avg_reddragonstatue", volume=0.8, loop=false, channel="reda",delay=3)]
[PlaySound(key="$d_avg_reddragonstatue", volume=1, loop=false, channel="redb",delay=6)]
[PlaySound(key="$d_avg_reddragonstatue", volume=1, loop=false, channel="redc",delay=9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Delay(time=2)]
一瞬间，所有旁的声音都寂灭了，只剩下钢铁颤抖，齿轮颤动。
为潮湿薄雾所掩映的，是冰冷而庞大的雕像轮廓。
由英雄所铸，在所有人印象中都还未完成的红龙先祖雕像，献给塔拉的礼物。它披着将死的猛烈日光到来，却几乎遮蔽了天幕。
[Dialog]
[Delay(time=1)]
[name="焦急的居民"]红龙雕像......活过来了？
[name="狂热的居民"]不，那是——库林？！
[name="焦急的居民"]库林，你也来帮大家揪出维多利亚人了？
[name="狂热的居民"]他得先证明他自己不是！
[name="焦急的居民"]库林，你快来，听我说，只要不是维多利亚人，就算被火烧了也不会很痛——
[name="狂热的居民"]你聋了吗！过来！
[name="焦急的居民"]慢着，他......
[name="焦急的居民"]他就这么，一个人，把那整座雕像拖了过来？！
[Dialog]
[Delay(time=1)]
人们终于看清他如何将铁链挽在手臂上，一圈、两圈、三圈，而雕像的重量全系于那宽阔，却也只属于区区凡人的肩头。
被呼唤名字的英雄不为所动地前进。他的肩膀磨出鲜血，他的肌肉濒临撕裂，他的骨骼发出悲鸣，而他只是走着。


... (全文22408字符)
```

### level_act41side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[stopsound(channel="read2")]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_weaamonologue_2", channel="read2", loop=false)]
[Subtitle(text="<i>高傲的红龙没有朋友，只会偶尔和镜子里的自己聊聊天。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>有一年的夏末节，她要举办一场盛大的宴会，需要镜中人出来帮忙，但她们两个不能同时出现在别人面前，否则镜中人就会消失。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>镜中人不得不遵循红龙的命令，出发去邀请神秘的守灵人。守灵人却无论如何也不愿赴宴，还劝镜中人不要再回去。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>但镜中人仍然只身回到红龙的巢穴。此时宴会已经开始，镜中人连忙躲进篝火外的黑暗。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>不知不觉中，来赴宴的人一个个消失，而红龙硬是把镜中人从黑暗中拉出来，强迫她和自己跳舞。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>她们跳啊跳，跳啊跳，镜中人觉得自己的脚趾都要掉了，她想休息一会儿，红龙却无论如何也不肯停下来。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[SoundVolume(volume=0, fadetime=3,channel="read2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[focusout(duration=0.1, type="char", from=0, to=1, block=true)]
[focusout(duration=0.1, type="bg", from=0, to=1, block=true)]
[delay(time=1)]
[stopsound(channel="read2", fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
给，拉芙希妮。
你要的书，蒸汽骑士冒险故事的续集。
[Dialog]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Background(image="21_G7_decisivebattlealley_d",screenadapt="coverall", fadetime=2.5,block=true)]
[delay(time=1)]
你问我，“为什么”？
这不需要理由，我亲爱的妹妹。
[Dialog]
[charslot(slot = "m", name = "avg_npc_1685_1#1$1", bstart=0.2,bend=0.7, duration=1.5)]
[delay(time=2.5)]
只是，你真的需要读它吗？
读一本要不是迫于同龄人的压力，你其实根本就不感兴趣的书？
[Dialog]
[charslot(duration=0.7)]
[delay(time=1)]
[focusout(duration=0.5, type="char", from=1, to=0)]
[focusout(duration=1, type="bg", from=1, to=0, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1684_1#22$1", focus="m")]
[name="拉芙希妮"]这是我自己想看的。
[charslot(slot = "m", name = "avg_npc_1685_1#1$1",focus="m")]
[name="爱布拉娜"]你不是对父亲说过的吗，你不想被其他人问，为什么会有维多利亚人不喜欢看蒸汽骑士的故事。
[charslot(slot = "m", name = "avg_npc_1684_1#12$1", focus="m")]
[name="拉芙希妮"]这本书......是爸爸让你帮我买的吗？
[charslot(slot = "m", name = "avg_npc_1685_1#8$1",focus="m")]
[name="爱布拉娜"]怎么会呢。
[charslot(slot = "m", name = "avg_npc_1684_1#8$1", focus="m")]
[name="拉芙希妮"]那你......为什么会知道？
[charslot(slot = "m", name = "avg_npc_1685_1#11$1",focus="m")]
[name="爱布拉娜"]你在后退，拉芙希妮。
[name="爱布拉娜"]我不喜欢你像其他人一样畏惧我。
[charslot(slot = "m", name = "avg_npc_1684_1#3$1", focus="m")]
[name="拉芙希妮"]不，我......
[charslot(slot = "m", name = "avg_npc_1685_1#11$1",focus="m")]
[name="爱布拉娜"]如果你这么害怕被我知道这些，不如来跟我跳一支舞，缓解一下紧张，如何？
[charslot(slot = "m", name = "avg_npc_1684_1#13$1", focus="m")]
[name="拉芙希妮"]真的是......跳舞吗？
[charslot(slot = "m", name = "avg_npc_1685_1#8$1",focus="m")]
[name="爱布拉娜"]为什么不可以是呢？
[Dialog]
[charslot]
说着，爱布拉娜甚至优雅地朝妹妹伸出手。
但在拉芙希妮的印象里，即便在父母放起一家人都喜欢的音乐，父亲摇头晃脑，母亲用手指在桌上敲着节拍的时候......
姐姐都只是冷冷地笑着，端坐在原位。
她从未跟着音乐舞动过身体。一次都没有过。
[charslot(slot = "m", name = "avg_npc_1685_1#11$1",focus="m")]
[name="爱布拉娜"]当你能跟上我脚步的时候，你就不必再为一本书、一个请求，或是几个同龄的朋友烦忧了。
[charslot(slot = "m", name = "avg_npc_1684_1#25$1",focus="m")]
[name="拉芙希妮"]......
[Dialog]
[charslot]
[PlaySound(key="$book_close",volume=1)]
还没拆封的骑士小说掉在地上，新书好闻的气味被泥水掩没。
她还太小，她没想过如愿以偿也能如此沉重苦涩，她只记得自己踉跄着转身离开，没有握住那只伸向自己的......
柔软而冰冷的手。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g4_dragonsquare_n",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]拉芙希妮。
[name="爱布拉娜"]人群已经散去，不必再隐藏自己的身份了。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",duration=1)]
[delay(time=2)]
[charslot(slot = "m", name = "avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]现在你仍然觉得他们还活着吗？
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]我只知道，每个塔拉人心中都燃烧着这样的火。从我们的先祖向维多利亚人俯首开始，火就从未熄灭过。
[name="拉芙希妮"]城里的人如此，那些随我回来的人们，他们也是一样，只是他们的火从未染上死亡的颜色。
[charslot(slot = "m", name = "avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]不错的比喻，拉芙希妮。
[charslot(slot = "m", name = "avg_450_necras_1#1$2",focus="m")]
[name="爱布拉娜"]那么，我现在再来问问你吧，你要怎么办呢？
[name="爱布拉娜"]再去把那团火漆成你的颜色？我想你一定已经试过了。
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]......
[charslot(slot = "m", name = "avg_450_necras_1#1$2",focus="m")]
[name="爱布拉娜"]无论是谁，一旦沾染了死亡，你的火焰就只能将其化为灰烬。
[name="爱布拉娜"]所以，拉芙希妮，杀死我。
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]同时杀死城里的所有人？
[charslot(slot = "m", name = "avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]如果你真的这么在意一件事会如何被记述，你也可以说，是我杀了他们，你只是把他们埋葬了。
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]纳斯尔纱的人们还活着。
[charslot(slot = "m", name = "avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]哪怕驱动那具身体的已经只剩死亡，而非生命？
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]如果真的连一点生命的火种都不存在，他们早就变成你那些游荡、无知无识的行尸了。
[charslot(slot = "m", name = "avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]他们早晚会的。
[charslot(slot = "m", name = "avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]不，他们不会。
[name="拉芙希妮"]我宁愿将活人身上的紫火看作一场瘟疫，一场因你

... (全文17312字符)
```

### level_act41side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g8_blackforest_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",duration=1.5)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1020_reed2_1#8$1",focus="m")]
[name="拉芙希妮"]......先前遇上的那个，难道又是捉弄人的幻影？路是错的，我好像又走回来了。
[name="拉芙希妮"]也看不清天色，不知道走了多久......还有多远。
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]但我至少没像布莉吉说的那样，被黑雾和噪声挡在黑林之外，我至少进来了。
[name="拉芙希妮"]还是这些爱捉弄人的精怪，会指给你错路的幻影，故意牵来枝条绊倒人的羽兽......倒是和我带莫兰他们回来时差不多。
[name="拉芙希妮"]也许是这些树木长得太高，也太茂密。它们遮住了天空，让这里面的生命与外界不同。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g9_blackforest_inside",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]......没走错路。这里就是黑林的中心了。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]总感觉......这里的景色也和我来的时候不一样......那些代表秋天的金红色呢，为什么都消失了？
[name="拉芙希妮"]为什么里头变成现在这样了？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=0.05, block=true)]
[bgeffect(name="$eb_blacksmoke_01",fade = true, fadetime = 1.5,layer=2)]
[Blocker(a=0, r=1, g=1, b=1, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_1020_reed2_1#6$1",focus="m")]
[name="拉芙希妮"]是黑雾？！
[charslot(slot="m",name="avg_1020_reed2_1#12$1",focus="m")]
[name="拉芙希妮"]也就是说，黑林到底还是拒绝了我，是吗？
[Dialog]
[charslot]
拉芙希妮紧紧握住手中的武器。假如真的如涅梅丝所说，深池离开城市之后就再也没有回来，被黑雾吞噬的确是他们最可能的下场。
但黑雾并无攻击她的迹象，只是停在原地。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]它是在......拒绝我吗？
[charslot(slot="m",name="avg_1020_reed2_1#12$1",focus="m")]
[name="拉芙希妮"]不，与其说是拒绝，倒不如说是冷漠......失望？
[charslot(slot="m",name="avg_1020_reed2_1#13$1",focus="m")]
[name="拉芙希妮"]为什么？
[Dialog]
[charslot]
除了植物婆娑的晃动之外，没有任何能被认成回答的声响。
拉芙希妮摇摇头，谨慎地经过黑雾身侧，选择了尽头看起来有光亮的一条路，而黑雾仍然对她的通过无动于衷。
那些乐于把人带上歧途的精怪，此刻也不见踪影。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect]
[Background(image="59_g9_blackforest_inside",screenadapt="coverall")]
[Delay(time=2)]
[bgeffect(name="$eb_blacksmoke_01",layer=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_1020_reed2_1#11$1",duration=1.5)]
[Delay(time=2.5)]
[name="拉芙希妮"]不行，又是死路......
[name="拉芙希妮"]没时间在这里逗留了。抱歉，我得烧出一条路来——
[Dialog]
[charslot]
[name="？？？"]那你可真是想太多了。
[charslot(slot="m",name="avg_1020_reed2_1#4$1",focus="m")]
[name="拉芙希妮"]谁？！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1690_1#10$1",duration=1.5)]
[Delay(time=2.5)]
[name="“放逐王”"]你觉得呢？
[charslot(slot="m",name="avg_1020_reed2_1#6$1",focus="m")]
[name="拉芙希妮"]怎么会是......你？
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]在城里的那位......先生。上次我就有问题要问你，但你却——
[charslot(slot="m",name="avg_npc_1690_1#5$1",focus="m")]
[name="“放逐王”"]上次见面确实算得上是不欢而散，不告而别。后面我也跟了你一路，看了你一路，就当是反思了。
[charslot(slot="m",name="avg_npc_1690_1#8$1",focus="m")]
[name="“放逐王”"]总之，我得承认你和我想的不太一样，但现在还不是闲聊的时候。
[name="“放逐王”"]别烧那些树木，只用你的火照亮它们就行了，看看它们到底是什么东西。
[charslot(slot="m",name="avg_1020_reed2_1#8$1",focus="m")]
[name="拉芙希妮"]“是什么东西”......？
[Dialog]
[PlaySound(key="$d_avg_magic_1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[charslot(slot="m",name="avg_1020_reed2_1#6$1",focus="m")]
[name="拉芙希妮"]叶片锋利，荆棘坚硬，枝条上甚至反射出金属的冷光？这究竟是？！
[charslot(slot="m",name="avg_npc_1690_1#8$1",focus="m")]
[name="“放逐王”"]是什么不重要，你的火不可能将其烧穿，这才是重点。
[name="“放逐王”"]跟我来。
[charslot(slot="m",name="avg_npc_1690_1#6$1",focus="m")]
[name="“放逐王”"]在黑雾改了主意之前，跟我来！
[charslot(slot="m",name="avg_npc_1690_1#8$1",focus="m")]
[name="“放逐王”"]我再晚一会儿跟你搭话，那东西一个心情不好，你就被直接吞了，骨头渣子也不剩。
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]可那边不是死路吗？
[charslot(slot="m",name="avg_npc_1690_1#8$1",focus="m")]
[name="“放逐王”"]为什么觉得眼见的东西就一定为实呢？
[name="“放逐王”"]听我的，走！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[bgeffect]
[Background(image="59_g7_blackforest_d",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$runsand")]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="拉芙希妮"]这是......我来纳斯尔纱时走的那条路！
[name="拉芙希妮"]刚刚那些小路居然通向这里？
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]先生，虽然冒昧，但您和林中的精怪......
[charslot(slot="m",name="avg_npc_1690_1#5$1",focus="m")]
[name="“放逐王”"]别傻了，我怎么会和它们扯上关系。
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]倒是这片树林，几百年过去了，除了多了一层黑雾以外，里面居然还是这副样子......
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]呵，煞风景。
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]再往前几步就算是出了黑林，不知道您能否——
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]啧啧啧，这可真是......
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]出什么事了？
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]看你身后。
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$d_avg_crowdrun")]
[Delay(time=3.5)]
[name="莫兰"]苇草！
[name="塔拉流民"]苇草，我们来了！
[Dialog]
[charslot(slot="m",name="avg_npc_728_1#1$1",duration=1.5)]
[PlaySound(key="$runsand")]
[Delay(time=3.5)]
[Dialog]
[charslot]
流民们的身影出现在黑林明亮的边缘。
[

... (全文12506字符)
```

### level_act41side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g12_castlecorridor_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_450_necras_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[name="爱布拉娜"]......
[name="爱布拉娜"]堡垒内的仆役已经全数被我遣退，那么这脚步声......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_723_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="校官"]......殿下。
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]哦，是你呀。来找我有什么事？
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]您不问我为什么还回得来吗？
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]不问。你回来了，仅此而已，我忠心的仆臣。
[name="爱布拉娜"]再说，你能为我带来一位什么样的客人，我心里自然有数。
[Dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=0.05, block=true)]
[bgeffect(name="$eb_blacksmoke_01",layer=1)]
[Blocker(a=0, r=1, g=1, b=1, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_450_necras_1#6$1",focus="m")]
[name="爱布拉娜"]......宵禁开始了吗？
[charslot(slot="m",name="avg_npc_723_1#2$1",focus="m")]
[name="校官"]刚刚开始。
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]那这也不算违背了我的命令。
[Dialog]
[charslot(slot="l",name="avg_npc_652_1#6$1",posfrom="0,90",posto="0,90",afrom=0,ato=0.6,bstart=0.5,bend=0.8,duration=2)]
[charslot(slot="l",action="zoom",poszoom="0.5,0.65",scale=1.7,focus="m")]
[PlaySound(key="$d_avg_dullthunderclap")]
[Delay(time=3)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......失败......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]失败了？
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]纳斯尔纱仍在此处，我也仍在此处，谈何失败？
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......逃离......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_450_necras_1#16$1",focus="m")]
[name="爱布拉娜"]期限是夏末节。就算黑雾以不听人言闻名，这一点想必也还记得住。
[Dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="......不出所料......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......令人失望......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......不可接受......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]说真的，我该如何理解你的只言片语呢？
[name="爱布拉娜"]或者......你也觉得话语的交流，不如法术与毁灭来得直接？
[Dialog]
[charslot]
爱布拉娜话音未落，泛着冷光的枝叶就从黑雾中探出，直指她的咽喉。
[Dialog]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista",volume=0.5)]
[PlaySound(key="$fireburst", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=1)]
与此同时，她的枪也刺进了厚重的雾气深处，紫色的火光在其中隐约可见，只等一个念头就将雾气燃尽。
但枝叶毕竟并未刺进爱布拉娜的咽喉，紫火也并未在黑雾中间燃起。
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]夏末节。
[name="爱布拉娜"]夏末节第二天的朝阳升起之前，我们都会得到那个结果。
[name="爱布拉娜"]至于现在......我们都不过是在虚张声势罢了，不是吗？
[Dialog]
[charslot]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=0.05, block=true)]
[bgeffect]
[Blocker(a=0, r=1, g=1, b=1, fadetime=1, block=true)]
[Delay(time=0.5)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.7, block=true)]
[delay(time=1)]
爱布拉娜维持着刺入黑雾的姿势，但顷刻之后，她咽喉前的枝叶凭空消失，她枪尖的火焰也随之熄灭。
黑雾随即散去。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]殿下......
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]你还在这里啊。
[name="爱布拉娜"]怎么，还有事吗？关于深池？
[name="爱布拉娜"]既然这里只有你我，我最忠心的仆臣，我允许你再度提起这个词。
[charslot(slot="m",name="avg_npc_723_1#6$1",focus="m")]
[name="校官"]感谢您的宽宏，但是，不。
[charslot(slot="m",name="avg_npc_723_1#2$1",focus="m")]
[name="校官"]帮助一个国家建立的鬼魂也仍然是鬼魂，鬼魂不应该被铭刻在历史上。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]但我的确担忧那天和我一样留在原地的几位同僚......他们现在在何处？他们是否会对您不利？
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]无需担心。而且，这应当不是你冒着风险，一直留到现在的原因。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]......在回来的路上，我看见了一片混乱。
[name="校官"]有的人越发狂躁，为了一点东西......甚至不为了什么就大打出手，而另一些人却像木偶般僵在原地......
[name="校官"]仿佛他们都是......当年随我们一同对抗维多利亚人的鬼魂。
[charslot(slot="m",name="avg_npc_723_1#6$1",focus="m")]
[name="校官"]他们也会没入黑暗吗？
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]这里毕竟是纳斯尔纱，红龙的巢穴，塔拉的首府。我怕这里发生的一切都将震动整个塔拉。
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]不会。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]......
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]你看起来仍然不很信服。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]殿下......我......
[charslot(slot="m",name="avg_npc_723_1#2$1",focus="m")]
[name="校官"]归根结底，我只有一个问题。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="校官"]只有这个问题，我恳请您给我一个答复。
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]好，我准许你的僭越。
[charslot(slot="m",name="avg_npc_723_1#2$1",focus="m")]
[name="校官"]（深吸气）
[cha

... (全文18964字符)
```

### level_act41side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g5_remains_outside",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_1020_reed2_1#2$1",duration=1.5)]
[Delay(time=2.5)]
[name="拉芙希妮"]所以，即便去城里不为别的，只为举行一场还火仪式，你们也仍然不愿意？
[charslot(slot="m",name="avg_npc_1691_1#4$1",focus="m")]
[name="严肃的守灵人"]您所述的情况实在太过反常。仅凭您的言语，我们也无法确认城中居民的生与死。
[name="严肃的守灵人"]更不要说还火仪式只是葬礼罢了，请您不要抱不切实际的期望。
[charslot(slot="m",name="avg_1020_reed2_1#13$1",focus="m")]
[name="拉芙希妮"]......那就请回吧，守灵人。无论如何，感谢你们的帮助。
[charslot(slot="m",name="avg_npc_1691_1#4$1",focus="m")]
[name="严肃的守灵人"]即便没有我们，您也要回纳斯尔纱去？
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]莫兰他们如今融入得很好，我没什么可担心的，涅梅丝的托付也已经完成......
[name="拉芙希妮"]我已经没有其他该做的事了。
[charslot(slot="m",name="avg_npc_1691_1#4$1",focus="m")]
[name="严肃的守灵人"]红龙阁下，请保重。
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]我会的。
[Dialog]
[charslot(slot="m",name="avg_npc_1691_1#4$1",focus="m")]
[Delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
红龙迈步，独自向来时的方向继续前进。昨日种种，留到眼中仅余一簇微弱的影。
而那同样也是一簇小小的火。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]“还火”......
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]下定决心回去送死了？
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]不知名的先生？
[name="拉芙希妮"]您来得正好，我们得谈一谈。如果您愿意帮我——
[charslot(slot="m",name="avg_npc_1690_1#11$1",focus="m")]
[name="“放逐王”"]你有没有在你的红龙历史课上，听过一个叫拉布雷德的倒霉鬼的故事？
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]——先生？
[charslot(slot="m",name="avg_npc_1690_1#4$1",focus="m")]
[name="“放逐王”"]哈，看来是没有了。
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]出走多年以后第一次回到王城，还没见到他亲爱的胞弟，就被护卫领走，被利剑穿胸而死......
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]不，我知道这段故事。
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]你也打算学他，做一个彻彻底底的蠢货，是吗？
[charslot(slot="m",name="avg_npc_1690_1#12$1",focus="m")]
[name="“放逐王”"]走吧。你见到了你姐姐，人到现在也都还活着，已经赢了那倒霉鬼太多，是不是？
[charslot(slot="m",name="avg_1020_reed2_1#13$1",focus="m")]
[name="拉芙希妮"]拉布雷德和艾里尔的故事并非我和爱布拉娜的故事。
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]......哼，就当我是偏要把闲事管到底吧。你刚才不是想跟我谈谈吗？要谈什么？
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]城里的还火仪式。
[name="拉芙希妮"]我本来只想多找一个准备仪式的人，但您看起来对塔拉的历史掌故很了解，我想，也许您能为我提供一些帮助......
[charslot(slot="m",name="avg_npc_1690_1#7$1",focus="m")]
[name="“放逐王”"]历史？掌故？
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]那我们不如边走边聊。走这边。
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]可黑林在那边——
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]跟我走，就像在黑林里那次一样，听见了吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="34_g7_galekingruins",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]......王城的遗址？
[name="拉芙希妮"]我曾经来过这里。这里的源石多发环境并不安全——
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]你不是要历史和掌故吗？找遍整个塔拉，还有哪个地方能比得上这座*古老的廷盖语粗口*王城？
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]这座什么样的王城？
[charslot(slot="m",name="avg_npc_1690_1#2$1",focus="m")]
[name="“放逐王”"]嘁，没什么。
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]我始终感激那时您在黑林提供的帮助，可现在我的确也有更要紧的事，没有太多时间——
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]有什么事？送死？
[name="“放逐王”"]你和你姐姐还真是大不相同。那条红龙的火焰受了诅咒，可性格再典型不过，目空一切，再听不见别的声音。你倒好——
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]我和姐姐原本就不同，但她也并不是您说的这样。
[charslot(slot="m",name="avg_npc_1690_1#5$1",focus="m")]
[name="“放逐王”"]可无论你们如何不同，红龙的天性都是斗争，即使你只是被卷入的那个也一样。
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]而斗争从来都只有一种结果，你死，或是她亡。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]......
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]所以说，反正有一个人要死，为什么要着急呢？
[name="“放逐王”"]再多点耐心吧，年轻人。我们就快到了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="34_g8_galekingruins_inside",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1690_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="“放逐王”"]我们今天来这儿就是为了这个祭台。
[charslot(slot="m",name="avg_1020_reed2_1#6$1",focus="m")]
[name="拉芙希妮"]祭台？您是说中间的那个吗？可那不是......熔炉吗？
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]“熔融了所有塔拉战士的武器、颠覆了王朝命运的熔炉”......令死去的战士从中复生的熔炉。
[charslot(slot="m",name="avg_npc_1690_1#4$1",focus="m")]
[name="“放逐王”"]哈，现在你们都这么称呼它？神神道道的，听起来倒是比“祭台”厉害不少。
[charslot(slot="m",name="avg_npc_1690_1#5$1",focus="m")]
[name="“放逐王”"]但很可惜，祭台就是祭台，只不过比其他祭台庞大。王城的核心就围着它建立，盖尔王加冕时的仪式石阵即是它的前身。
[charslot(slot="m",name="avg_npc_1690_1#9$1",focus="m")]
[name="“放逐王”"]而老红龙死去的时候，人们也会在这里为他还火。
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]还火？
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]就跟你在那群木头脑袋那儿看见的东西一样。这么多年了，他们倒真是一直记得清清楚楚。
[name="“放逐王”"]不过，那年头的还火可不是点起篝火就了事的。
[charslot(slot="m",name="avg_npc_1690_1#11$1",focus="m")]
[name="“放逐王”"]梅里亚德那老女人的时候，继承盖尔王之位的红龙的兄弟姐妹，只要把手伸进火里烫几个泡就结了。
[name="“放逐王”"]不过再往上追溯，据说，只是据说，很久很久以前，那些兄弟姐妹都要一起在火里殉葬。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]......
[ch

... (全文20035字符)
```

### level_act41side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g5_remains_outside",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="拉芙希妮"]您送我送得够远，这里已经是守灵人的聚落了。
[charslot(slot="m",name="avg_npc_1690_1#1$1",focus="m")]
[name="“放逐王”"]你姐姐唤醒了我，你如果觉得我聒噪，自然也可以一把火送我回去接着睡。
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_carriagegoaway")]
[Delay(time=2.5)]
[name="？？？"]苇草！
不远处，金发佩洛从驮兽背上一跃而下，向红龙所在的方向疾奔而来。
在她身后，为驮兽所拖曳的，是一辆临时拼凑的板车。上面排布堆叠着长长的木箱。
[charslot(slot="m",name="avg_1020_reed2_1#6$1",focus="m")]
[name="拉芙希妮"]——布莉吉？
[name="拉芙希妮"]你怎么来了这里？你身后拖着的那些是——
[name="拉芙希妮"]......棺材？！
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]......
[Dialog]
[charslot]
[PlaySound(key="$runsand")]
[charslot(slot="m",name="avg_4177_brigid_1#11$1",duration=1.5)]
[Delay(time=2.5)]
[name="布莉吉"]对，棺材。涅梅丝让我带着这些棺材来找守灵人。他们还在遗迹里吗？
[charslot(slot="m",name="avg_4177_brigid_1#8$1",focus="m")]
[name="布莉吉"]红龙，你身边是不是站着什么人？我闻到了熟悉的焦煳味，刚刚好像还听见你和人说话——
[charslot(slot="m",name="avg_npc_1690_1#2$1",focus="m")]
[name="“放逐王”"]哼。
[Dialog]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1020_reed2_1#1$1",focus="m")]
[name="拉芙希妮"]不，只有我一个。
[name="拉芙希妮"]这些是......
[charslot(slot="m",name="avg_4177_brigid_1#11$1",focus="m")]
[name="布莉吉"]死了的人。
[name="布莉吉"]哪怕你拽住他的手，他也拼了命要把肩膀扯脱臼，好用牙去咬他臆想中的仇人的家伙，或是被他们撕成碎片的倒霉蛋。
[charslot(slot="m",name="avg_4177_brigid_1#6$1",focus="m")]
[name="布莉吉"]还有提奥。涅梅丝最终还是找到了他，他......
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]......
[charslot(slot="m",name="avg_4177_brigid_1#6$1",focus="m")]
[name="布莉吉"]就好像事情自然而然地到了这一步，夏末节的夜晚就要到来，篝火马上就要烧到最旺了一样......
[Dialog]
[charslot]
红龙抬头朝纳斯尔纱所在的方向望去。此刻远远地竟也能看见一个渺茫的影，勾勒出属于紫火燃烧的轮廓。
[charslot(slot="m",name="avg_4177_brigid_1#6$1",focus="m")]
[name="布莉吉"]再这样下去，城里可能很快连棺材都不够用了。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g10_indoor",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1692_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[name="涅梅丝"]但愿布莉吉已经到了城外......但愿林中没那么多雾，布莉吉能从小路离开......
[name="涅梅丝"]该死，这些没用上的武器还堆在库林屋里，不能被人看见。
[charslot(slot="m",name="avg_npc_1692_1#5$1",focus="m")]
[name="涅梅丝"]这个......这个是没用光的燃料......爆炸物？也许拉芙希妮殿下回来时能用得上。
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[name="涅梅丝"]不，不用，堡垒中所有的仆役也都染上了紫火，而且那条贪婪的红龙早就把他们遣散了......
[name="涅梅丝"]简直就像......等着拉芙希妮殿下回来和她做个了断一样。
[Dialog]
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1692_1#5$1",focus="m")]
[Delay(time=1)]
[name="涅梅丝"]或者......陷阱？
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1692_1#5$1",focus="none")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="涅梅丝"]谁？！
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1686_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1692_1#5$1",focus="m")]
[name="涅梅丝"]......罗里？你来干什么？
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]你是......涅梅丝。
[charslot(slot="m",name="avg_npc_1692_1#1$1",focus="m")]
[name="涅梅丝"]对，是我。我在整理库林的遗物，如果你没事就先离开——
[Dialog]
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[PlaySound(key="$d_avg_spear", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="-50,0",duration=-0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]叛徒。
[charslot(slot="m",name="avg_npc_1692_1#4$1",focus="m")]
[name="涅梅丝"]你疯了？！
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="涅梅丝"]哦，对，你疯了，我们大家都疯了。
[charslot(slot="m",name="avg_npc_1686_1#1$1",focus="m")]
[name="阴沉的居民"]叛徒——
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.03, block=true)]
[PlaySound(key="$sheildimpact", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.5)]
[PlaySound(key="$bodyfalldown1")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[name="涅梅丝"]我还是......下不去死手，明明大家都已经和死人差不多了。
[name="涅梅丝"]哈，哈哈......
[charslot(slot="m",name="avg_npc_1692_1#8$1",focus="m")]
[name="涅梅丝"]得先把这家伙拖回他自己家，别惹人注意......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g1_citystreets_d",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1692_1#8$1",duration=1.5)]
[Delay(time=2.5)]
[name="涅梅丝"]呼......
[Dialog]
[charslot]
[PlaySound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_1752_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="焦急的居民"]涅梅丝？
[name="焦急的居民"]没、没事的话，我先走了。
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="涅梅丝"]你手里拿着什么？
[charslot(slot="m",name="avg_npc_1752_1#1$1",f

... (全文13428字符)
```

### level_act41side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_wilderness_n",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_226_weed_1#1",duration=1.5)]
[Delay(time=2.5)]
[name="“领袖”"]小丘郡还有多远？
[charslot(slot="m",name="avg_npc_228_1#7",focus="m")]
[name="阿赫茉妮"]远着呢。
[charslot(slot="m",name="avg_226_weed_1#1",focus="m")]
[name="“领袖”"]姐姐她......不会不知道的。
[charslot(slot="m",name="avg_npc_228_1#7",focus="m")]
[name="阿赫茉妮"]说实话，只有“雄辩家”那帮人以为事情天衣无缝。
[charslot(slot="m",name="avg_226_weed_1#6",focus="m")]
[name="“领袖”"]那你还跟着我？
[charslot(slot="m",name="avg_npc_228_1#1",focus="m")]
[name="阿赫茉妮"]如果有得选，我也想美美在之前的营地里睡一觉啊。
[charslot(slot="m",name="avg_226_weed_1#1",focus="m")]
[name="“领袖”"]姐姐为什么不阻止我？
[charslot(slot="m",name="avg_npc_228_1#1",focus="m")]
[name="阿赫茉妮"]不知道。说不定对你寄予厚望吧。
[charslot(slot="m",name="avg_226_weed_1#2",focus="m")]
[name="“领袖”"]不，她从来没对我露出过那样的眼神。在我同意做她的影子之后，她......
[name="“领袖”"]阿赫茉妮，我请求你......我请求你去告诉姐姐，我不想这样。
[charslot(slot="m",name="avg_npc_228_1#7",focus="m")]
[name="阿赫茉妮"]不想去小丘郡？
[charslot(slot="m",name="avg_226_weed_1#2",focus="m")]
[name="“领袖”"]嗯。还有，如果姐姐心情还不错的话，我还想请你告诉她，从今以后，我——
[name="“领袖”"]......
[charslot(slot="m",name="avg_226_weed_1#1",focus="m")]
[name="“领袖”"]不，没有了。
[charslot(slot="m",name="avg_npc_228_1#1",focus="m")]
[name="阿赫茉妮"]好吧，我就勉为其难替你传这个话。“雄辩家”的眼线还挺难躲的呢。
[charslot(slot="m",name="avg_226_weed_1#1",focus="m")]
[name="“领袖”"]嗯，谢谢，请你快些去吧......
[Dialog]
[charslot(slot="m",name="avg_npc_228_1#1",focus="m")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_226_weed_1#2",focus="m")]
[name="“领袖”"]......在姐姐......彻底厌倦之前。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, fadetime=0, keep=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Subtitle(text="直到她到了小丘郡，阿赫茉妮才姗姗来迟。她明白这意味着什么。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="然后，在那个夜晚，炮声轰鸣，晶簇生长，她倒在小丘郡的街道上，血从她的腹部流出来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她没有觉得多害怕，她反倒觉得如释重负。她可以像无数普通人一样死去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="然后她看见，不远处的高楼上，那紫色的火焰来了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她这时才感到害怕。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她怕那火没有看见自己，将自己和街道上的人一同变成傀儡。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她怕那火看见了自己，将受伤的自己带回，让自己继续当她的影子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她和那火对视，试图从中得到什么关于自己未来的暗示，但她能看见的只有厌烦。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她最害怕的事终于发生了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g12_castlecorridor_n",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
死去的红龙躺在地上。
活着的红龙身后，离群的守灵人刚刚明白一切。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g15_castlebalcony_n",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(key="$eblana_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[name="涅梅丝"]......她骗了您。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="高尚的红龙"]不，她没有欺骗任何人。
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="涅梅丝"]她算准了您不愿让整座城市的人为她陪葬，所以才自导自演了这么一出戏！
[charslot(slot="m",name="avg_npc_1692_1#4$1",focus="m")]
[name="涅梅丝"]她引诱您刺穿她的躯壳，而她自己则得以摆脱束缚，让本来还没那么凶猛的紫火能在夏末节前夜把所有人烧光！
[charslot(slot="m",name="avg_1020_reed2_1#13$1",focus="m")]
[name="高尚的红龙"]她为什么要为了一个平时从来不放在眼里的节日......冒这样的风险？
[charslot(slot="m",name="avg_npc_1692_1#10$1",focus="m")]
[name="涅梅丝"]红龙，我也是身染紫火的活人，就连我也感受得到，死火正在我胸口燃烧，比任何时候都冰冷，冷得我马上就要失去知觉！
[charslot(slot="m",name="avg_npc_1692_1#4$1",focus="m")]
[name="涅梅丝"]不管她现在是在图谋整个塔拉，还是她已经疯了，只想拉着一城的人跟她一起死，怎样都好，这些根本就不重要！
[charslot(slot="m",name="avg_1020_reed2_1#12$1",focus="m")]
[name="高尚的红龙"]不，塔拉已经是她的囊中之物，她也绝对没有疯，那她......
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="高尚的红龙"]她——
[name="高尚的红龙"]......
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="高尚的红龙"]涅梅丝，她的尸首还在吗？
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[name="涅梅丝"]我去看看。
[Dialog]
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[Delay(time=1)]
[PlaySound(key="$rungeneral",volume=0.6)]
[charslot(slot="m",afrom=1,ato=0,duration=0.5)]
[charslot(slot="m",posfrom="0,0",posto="200,0",afrom=0,ato=1,duration=2)]
[delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$rungeneral",volume=0.6)]
[charslot(slot="m",name="avg_npc_1692_1#7$1",afrom=0,ato=1,duration=0.5)]
[charslot(slot="m",posfrom="300,0",posto="0,0",afrom=0,ato=1,duration=2)]
[delay(time=2.5)]
离群守灵人的眉毛拧成一团。也许她这辈子还没生出过这么大的恶意，自然也就没下过这么大的决心。
[Dialog]
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="涅梅丝"]她的尸首就在——
[Dialog]
[charslot]
她的回答声被熊熊的燃烧声盖了过去。
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="高尚的红龙"]不管

... (全文11508字符)
```

### level_act41side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[stopsound(channel="read3")]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$tara_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_weaamonologue_3",channel="read3")]
[Subtitle(text="<i>从前有一位母亲，她曾是一国的国王，却被仇敌夺去了王冠和亲人。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>万幸她有一位强大的女儿，她的女儿与黑林中的黑雾签下契约，合力赶走了仇敌，女儿为母亲夺回了王国，黑雾则取回了不被打搅的安宁。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>母亲决定为女儿举办一场盛大的加冕仪式，可就在仪式开始前，女儿突然死于非命。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>母亲万分悲伤，继而变得狂怒，一心要为女儿复仇，复仇的狂热最终成为一股几乎将整个王国烧尽的烈焰。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>可烈焰太过旺盛，惊扰了刚刚睡下的黑雾。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>黑雾勒令母亲安分守己，不然就要将她拖入黑暗，而母亲在悲伤中认定黑雾就是夺走女儿生命的东西，决定拼死一搏。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[SoundVolume(volume=0, fadetime=3,channel="read3")]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[stopsound(channel="read3")]
[Background(image="59_g2_citystreets_n",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=2.5)]
[name="布莉吉"]涅梅丝、苇草......
在城门口，游牧民最后一次望向远方的堡垒。
突然浓烈起来的焦煳味让她想拔腿就跑。她明白这意味着什么。
可无论拉芙希妮是否成功，自己都应当像涅梅丝说的，立刻离开城市，去找守灵人，去请他们过来，越快越好。
但涅梅丝说话时尽管强硬，却怎么都不像是相信事情有转机，也不像相信自己能请来守灵人。
刺鼻的焦煳味同样从涅梅丝身上散发出来，让布莉吉想起只有死者才会有的偏执。
[Dialog]
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0,ato=0.5,focus="m",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]还在等谁呢？等死亡摸到你的后脑勺，再和它比比谁跑得快吗？
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]......谁？
[charslot(slot="m",name="avg_npc_1690_1#4$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]哦，我都忘了，你能听见我说话。
[charslot(slot="m",name="avg_npc_1690_1#4$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]我能听见。我甚至能感受到你就在那里......但我看不见你。
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]赶快离开这座城市吧，局外人。
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]听你说话，你好像也是局外人？
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]当然。局外人好心提醒另一个局外人，这不是天经地义的事吗？
[charslot(slot="m",name="avg_npc_1690_1#5$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]布莉吉，活着。活着比什么都重要。最迟到明天的太阳升起之前，这座城市一定会死去。
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]听涅梅丝的话，去找她的同族，然后跑得远远的，再也不要回来。
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]......你说得对，我该走了。
[name="布莉吉"]但我会回来。
[charslot(slot="m",name="avg_npc_1690_1#7$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]回来？！
[charslot(slot="m",name="avg_npc_1690_1#4$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]哈，愚蠢和倔强还真是代代相传！
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]她拼了命把你往城外赶，你却要傻乎乎地自己跑回来？
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]果然，你也觉得涅梅丝只是在找个借口让我活下来，是吗？
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]不然呢？你以为自己能说动那些木头脑袋？你就用手拽吧，看看明年春天会不会有一个木头脑袋发了芽，愿意跟你进黑林！
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]我讨厌你现在说话的腔调，看不见的弟兄。
[charslot(slot="m",name="avg_npc_1690_1#2$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]你管我叫什么？弟兄？
[charslot(slot="m",name="avg_npc_1690_1#2$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]你身上的煳味难闻得要命，煳味之外的部分却又和游牧人有点像，我不知道你到底和我们有没有关系，干脆就这么叫你了。
[charslot(slot="m",name="avg_npc_1690_1#4$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]哈哈......哈哈哈哈哈哈！
[charslot(slot="m",name="avg_npc_1690_1#11$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]来打个赌吧，布莉吉！
[charslot(slot="m",name="avg_npc_1690_1#11$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]打赌？
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]赌你离开之后，不可能在今夜，在纳斯尔纱焚尽之前回来。
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]你要赌的明明就不是这个。
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]哦？那你说我赌的是什么？
[charslot(slot="m",name="avg_npc_1690_1#1$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]你只想证明自己是对的，活下去比什么都重要。你觉得我最终也会这么做。
[name="布莉吉"]但是，我跟你赌。
[charslot(slot="m",name="avg_npc_1690_1#4$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]那你还等什么？
[charslot(slot="m",name="avg_npc_1690_1#4$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]只是觉得不太公平。如果你赢了，我会后悔一辈子。可要是我赢了，你也不过是看戏而已。
[name="布莉吉"]要是我赢了，就回你该回的地方吧，好吗？
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]......
[name="“放逐王”"]你觉得我该回哪里？
[charslot(slot="m",name="avg_npc_1690_1#8$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]我不知道，可你的家肯定不在这里。
[name="布莉吉"]你好像被这座城市里的人狠狠地背叛过，可你又狠不下心去伤害他们。
[name="布莉吉"]你装作乐意看人自食其果的样子，可你刚刚说城市就要烧毁的时候......其实一点都不开心。
[name="布莉吉"]你是我见过最别扭的家伙——
[charslot(slot="m",name="avg_npc_1690_1#6$1",afrom=0.5,ato=0.5,focus="m")]
[name="“放逐王”"]够了！
[charslot(slot="m",name="avg_npc_1690_1#6$1",afrom=0.5,ato=0.5,focus="none")]
[name="布莉吉"]......
[Dialog]
[charslot(duration=1.5)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[charslot]
[Image(image="59_i09",screenadapt="coverall",fadetime=1,block=false)]
[ImageTween(xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1, yScaleTo=1, duration=35, block=fa

... (全文12149字符)
```

### level_act41side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="59_g4_dragonsquare_n",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
涅梅丝将棺椁拖出堡垒。
雕像矗立的广场上空无一人。宵禁已经开始，但她正拖着那条红龙的棺椁，那红龙的火正在她身上燃烧。
她所到之处，黑暗退避。她行过的路，黑暗再去占据。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1692_1#6$1",duration=1.5)]
[Delay(time=2)]
[name="涅梅丝"]哈，库林......我简直要嫉妒你了。
[name="涅梅丝"]那么大的一座雕像被你拖过来，人们就算在睡觉，也会被你吵到睡不着，出门来看热闹的。
[charslot(slot="m",name="avg_npc_1692_1#2$1",focus="m")]
[name="涅梅丝"]可我呢？库林，我呢？
[charslot(slot="m",name="avg_npc_1692_1#6$1",focus="m")]
[name="涅梅丝"]难道我要一路吆喝过去吗？“红龙死了”？
[Dialog]
[charslot]
她抬头和雕像对视。跳动着紫火的眼眸不回答她。
她回想起多年前和守灵人们一起在逝者灵前唱过的那些歌谣。来办葬礼的城里人也会和他们一起唱，尽管许多人唱了几句就开始忘词。
[charslot(slot="m",name="avg_npc_1692_1#2$1",focus="m")]
[name="涅梅丝"]......但愿你们还没把那些古老的歌谣忘干净，塔拉人。
[charslot(slot="m",name="avg_npc_1692_1#7$1",focus="m")]
[name="涅梅丝"]对了，红龙，我该用一首什么样的歌来昭告你的死亡呢？
[name="涅梅丝"]不如来一曲亵渎的，《蒂姆·芬的守灵夜》，人们在你的葬礼上打作一团，连酒都洒在你身上，结果你闻着这酒香复活？
[charslot(slot="m",name="avg_npc_1692_1#2$1",focus="m")]
[name="涅梅丝"]算了吧，没人想让你活过来。
[Dialog]
[charslot]
她随口唱出了另一首闯进她脑海的歌曲。
[charslot(slot="m",name="avg_npc_1692_1#2$1",focus="m")]
[name="涅梅丝"]寒风在高山和丘陵间呼啸，乌云笼罩沼泽与山谷♪
[charslot(slot="m",name="avg_npc_1692_1#1$1",focus="m")]
[name="涅梅丝"]我在黎明时分看见一个旅人，他问我通往金色原野的路♪
[Dialog]
[charslot]
离群的守灵人嘶哑地唱着歌，拖着燃烧的棺椁，走向她烂熟于心的，纳斯尔纱的每一处曾有人居住的场所。
她在每一间房前停留，确保紫色的火映在窗上，守灵人的挽歌传入室内。
她越是歌唱，那火越是亲昵地搂紧她的身躯，越过她迟钝的知觉，让她每走一步都如同折磨......
却同时让她听见从每一扇窗户里传出的，最细碎的声音。
[Dialog]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=1.5, keep=true)]
[Background(image="59_g3_dragonsquare_d",screenadapt="coverall",fadetime=1.5)]
[Delay(time=2)]
[name="好奇的居民"]塔拉语培训班？基兰，这不可能不要钱的吧？
[name="好奇的居民"]要是这个价......也不是不行，大不了少喝几顿酒呗。
[Dialog]
[CameraEffect(effect="Grayscale", amount=0, fadetime=1.5, keep=true)]
[Background(image="59_g4_dragonsquare_n",screenadapt="coverall",fadetime=1.5)]
[Delay(time=2)]
[name="烂醉的居民"]*维多利亚粗口*，基兰，我当年要是多帮帮你，你是不是就不至于被维多利亚人给抓去......
[name="烂醉的居民"]该死的黑雾，要是红龙再不把这东西赶走，那就我来！
[charslot(slot="m",name="avg_npc_1692_1#2$1",focus="m")]
[name="涅梅丝"]寒风在高山和丘陵间呼啸，乌云笼罩沼泽与山谷♪
[name="涅梅丝"]我在黎明时分看见一个旅人，他问我通往金色原野的路♪
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[name="烂醉的居民"]谁？涅梅丝？大半夜的唱什么歌呢？
[name="烂醉的居民"]她身后拖着的东西，烧得正旺的，又是什么......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Background(image="59_g3_dragonsquare_d",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="不舍的居民"]亲爱的，就算你想为塔拉人做些什么，也不用非要去参军吧？
[name="不舍的居民"]......好吧，我会在家一直等你回来的，一直到我们赢得自由那天。
[Dialog]
[CameraEffect(effect="Grayscale", amount=0, fadetime=1.5, keep=true)]
[Background(image="59_g4_dragonsquare_n",screenadapt="coverall",fadetime=1.5)]
[Delay(time=2)]
[name="厌烦的居民"]终于安静了。一直念叨手疼，手疼，手疼，整条胳膊都没了，怎么会疼？喊疼就有药吗？
[name="厌烦的居民"]我宁愿你别回来，宁愿你让我怀念一辈子，也别像现在这样......
[charslot(slot="m",name="avg_npc_1692_1#2$1",focus="m")]
[name="涅梅丝"]我对他说：可敬的人儿，连我也说不清有多远的旅途♪
[name="涅梅丝"]但如果你愿意，我会陪你走一段，通往金色原野的路♪
[Dialog]
[charslot]
[stopmusic(fadetime=2.5)]
[name="厌烦的居民"]这不是悼念死者的歌吗？
[name="厌烦的居民"]那紫色的火......这首歌悼念的是？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Background(image="59_g2_citystreets_n",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="震惊的居民"]什么？！敌人已经摸进黑林，就在纳斯尔纱城外了？
[name="震惊的居民"]涅梅丝，我不能在这儿干坐了。征兵点在哪？我这就带上武器过去！
[Dialog]
[PlaySound(key="$d_gen_soldiersrun")]
[Delay(time=2.5)]
[CameraEffect(effect="Grayscale", amount=0, fadetime=1, keep=true)]
[Delay(time=2)]
窗内既无光亮，也无人声。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1692_1#2$1",duration=1.5)]
[Delay(time=2.5)]
[name="涅梅丝"]你向右转，经过永不倾颓的王城，穿过美酒汇成的河流♪
[name="涅梅丝"]我会陪你在河边喝上一点，接着走通往金色原野的路♪
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="提奥"]涅梅丝小姐，战争结束之后，你要搬过来和库林先生一起住啊？
[name="提奥"]真可惜，我还以为这样就有人代替我帮库林先生做饭了呢......
[Dialog]
[charslot(duration=1.5)]
[CameraEffect(effect="Grayscale", amount=0, fadetime=1.5, keep=true)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1692_1#6$1",duration=1.5)]
[Delay(time=2)]
[name="涅梅丝"]也许拉芙希妮殿下回来之前，我最该做的事......其实是把工坊的门修好。
[name="涅梅丝"]（吸鼻子）
[Dialog]
[charslot(slot="l",name="avg_npc_1692_1#2$1",focus="all",posfrom="200,0",posto="200,0",duration=1.5)]
[Delay(time=2)]
[name="涅梅丝"]愿你找到那片金色原野，愿你在火中找到永不背弃的归宿♪
[name="涅梅丝"]那时你就不会彷徨，你会走完这通往金色原野的路♪
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=4.5)]
[charslot(slot="m",name="avg_npc_1690_1#9$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1690_1#9$1",focus="m")]
[name="“放逐王”"]已经快被死亡蚕食殆尽的守灵人，她唱的歌又能唤醒谁呢？
[name="“放逐王”"]甚至连自己都没能唤醒，不是吗？
[charslot(slot="m",name="avg_npc_1690_1#5$1",focus="m")]
[name="“放逐王”"]......
[charslot(slot="m",name="avg_npc_1690_1#10$1",focus="m")]
[name="“放逐王”"]无论如何，布莉吉，继承了我稀薄血脉的傻孩子......
[name="“放逐王”"]别回来。
[charslot(slot="m",name="avg_npc_1690_1#5$1",focus="m")]
[name="“放逐王”"]这座城市不值得你为它死去。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g4_dragonsquare_n",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, blo

... (全文23954字符)
```

### level_act41side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Background(image="50_g13_warshipcommandroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_450_necras_1#6$1",duration=1.5)]
[Delay(time=3.5)]
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="“校官”"]殿下，“歌唱家”刚刚来告发“雄辩家”等人挟持拉芙希妮前往小丘郡。
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]我知道了。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="“校官”"]他专门挑了人员已经开拔，“领袖”已经启程前往小丘郡的时候告发，这样就既不用得罪“雄辩家”他们，又不能算知情不报......
[name="“校官”"]我们拿他怎么办？
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]深池本来也不需要他去做眼线。没人指望他来干这个。
[charslot(slot="m",name="avg_npc_723_1#2$1",focus="m")]
[name="“校官”"]非常抱歉，这是我的失职，我以为他们只是在按照命令向小丘郡进发，没想到他们竟敢挟持拉芙希妮。
[name="“校官”"]趁他们还没走远，现在出发，我们还追得上......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_228_1#7",duration=1.5)]
[Delay(time=2)]
[name="阿赫茉妮"]殿下，我替您的妹妹带来消息。她希望您能制止“雄辩家”等人的盲动，将她带回这里。
[charslot(slot="m",name="avg_npc_723_1#4$1",focus="m")]
[name="“校官”"]这是她本人的意愿？
[charslot(slot="m",name="avg_npc_228_1#7",focus="m")]
[name="阿赫茉妮"]没错。
[charslot(slot="m",name="avg_npc_723_1#1$1",focus="m")]
[name="“校官”"]我这就去调动部队——
[charslot(slot="m",name="avg_450_necras_1#15$1",focus="m")]
[name="爱布拉娜"]慢着。
[charslot(slot="m",name="avg_npc_723_1#8$1",focus="m")]
[name="“校官”"]殿下，现在制止他们的确是较好的选择。
[charslot(slot="m",name="avg_npc_228_1#7",focus="m")]
[name="阿赫茉妮"]而且，“不想去小丘郡”，这也的确是拉芙希妮自己的意思。
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]既然这真的是她自己的意思，她理当亲手将其付诸实现。
[name="爱布拉娜"]对她的火而言，这并不是什么难事。她不是已经以“领袖”之名执行了许多人的死刑了吗？
[name="爱布拉娜"]去告诉她，如果她想，就自己去做——
[charslot(slot="m",name="avg_450_necras_1#16$1",focus="m")]
[name="爱布拉娜"]不，连这也不必了。
[charslot(slot="m",name="avg_npc_228_1#3",focus="m")]
[name="阿赫茉妮"]殿下，恕我冒昧，她毕竟是您的——
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]妹妹？
[charslot(slot="m",name="avg_npc_228_1#7",focus="m")]
[name="阿赫茉妮"]......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, fadetime=0, keep=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
巨龙扇动着钢铁的翅膀，掀起冰冷的，燃烧着的涡流，而拉芙希妮未曾动摇半分。
她将枪尖狠狠刺入巨龙的眼窝。
[name="巨龙"]还是没法下定决心杀死我吗，拉芙希妮？
巨龙的声音逐渐与爱布拉娜的重合，连身躯都幻化成爱布拉娜的形状。
周围的景物也飞速改变，一如那个跟随拉布雷德在遗迹中度过的夜晚。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g8_blackforest_n",screenadapt="coverall")]
[charslot(slot="m",name="avg_450_necras_1#5$1",focus="m")]
[playMusic(intro="$ncrmcr_intro",key="$ncrmcr_loop", volume=0.6)]
[Delay(time=2)]
[bgeffect(name="$eb_deathburning",layer = 1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_1020_reed2_1#12$1",focus="m")]
[name="拉芙希妮"]我只是......不懂。
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]你究竟要什么？
[name="拉芙希妮"]你欺骗我，欺骗所有人，就为了一座城市为你陪葬？为了什么？为了成为下一个盖尔王传说？
[charslot(slot="m",name="avg_450_necras_1#5$1",focus="m")]
[name="爱布拉娜"]我并没有骗你。
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]事到如今，你觉得我还会相信吗？
[name="拉芙希妮"]纳斯尔纱对你来说究竟是什么？塔拉对你来说究竟是什么？
[charslot(slot="m",name="avg_1020_reed2_1#4$1",focus="m")]
[name="拉芙希妮"]我一直相信，我们要实现的是同一个梦想。为什么此时此刻，我们的梦已经完全两样了呢？
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]难道对你而言，梦想也会在你追逐权力的路上变成令人厌倦的无聊把戏，就像......
[charslot(slot="m",name="avg_1020_reed2_1#2$1",focus="m")]
[name="拉芙希妮"]就像小丘郡那时的......拉芙希妮一样吗？
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]小丘郡？
[name="爱布拉娜"]那时我在你眼中看到的不是回归的渴望，而是解脱，不是吗？
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]......
[charslot(slot="m",name="avg_450_necras_1#6$1",focus="m")]
[name="爱布拉娜"]至于我，是啊，小丘郡那时，我的确已经厌倦了。
[name="爱布拉娜"]我可以用火将一切熔成想要的形状，却唯独只有镜中的影子......
[charslot(slot="m",name="avg_450_necras_1#15$1",focus="m")]
[name="爱布拉娜"]无论我燃起多大的火焰，她都不会有分毫改变。
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]......因为你从未直接用火焰去灼烧她。
[charslot(slot="m",name="avg_450_necras_1#15$1",focus="m")]
[name="爱布拉娜"]因为我从未直接用火焰去灼烧你。
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="爱布拉娜"]我只是在等，一直在等，等你给我一个回答。
[charslot(slot="m",name="avg_1020_reed2_1#11$1",focus="m")]
[name="拉芙希妮"]回答？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[bgeffect]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Image(image="34_i04",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="爱布拉娜"]——你呢，拉芙希妮？你想要什么呢？
[name="爱布拉娜"]你的血脉与教养让你高尚，这是好事，可你要是一无所求，我又该在身边留什么样的位置给你呢？
[name="爱布拉娜"]说吧，这可是雪夜里的愿望......多么大的野心，我都允许。
[name="拉芙希妮"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, fadetime=0, keep=true)]
[Image]
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[Delay(time=1)]
[bgeffect(name="$eb_deathburning",layer = 1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="拉芙希妮"]你的确并未用火焰灼烧我，因为你有更合用的工具，恐惧、责任、愧疚、同情......
[name="拉芙希妮"]你从未直接要求我改变什么，但你已经无数次间接地这么做了。
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="爱布拉娜"]我的影响毫无作用，我的厌倦却得到了回报，很讽刺，不是吗？
[charslot(slot="m",name="avg_1020_reed2_1#7$1",focus="m")]
[name="拉芙希妮"]......
[charslot(slot="m",name="avg_450_necras_1#16$1",focus="m")]
[name="爱布拉娜"]无论如何，你终于愿意回来，愿意拥抱真实的生活，

... (全文20193字符)
```

### level_act41side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[stopsound(channel="read1")]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_weaamonologue_1", channel="read1", loop=false)]
[Subtitle(text="<i>为了夺回被仇敌侵占的王国，贪婪的红龙找到盘踞在林中的黑雾帮助自己。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>红龙喷吐死亡的火焰，黑雾将仇敌赶入火中。他们合力夺回了王国，让原本荆棘丛生的原野重新焕发了生机。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>可死火在原野上蔓延开来，整片原野和原野上的居民都在不知不觉中衰败下去，新生命连连夭折，死者却无法安寝。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>红龙不能容忍死亡不受控制、自行蔓延，她要让生命归生命，死亡归死亡。为此，她在夏末节前，将被死火侵染的人们聚集到自己的巢穴。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[SoundVolume(volume=0, fadetime=2,channel="read1")]
[Delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall", block=true)]
[delay(time=1.5)]
[stopsound(channel="read1", fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="作家"]......这就是红龙的故事。
[name="？？？"]接下来呢？那些被死火侵染的人怎么样了？
[name="作家"]没有什么接下来，书上就是这么写的。
[name="？？？"]这不合理。
[name="作家"]一切都有个尽头，不管这个尽头看起来是否合理，小姐。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_snowconutryinside",screenadapt="coverall", block=true)]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[name="神秘的女性"]这也不是您选择在作品出版后销声匿迹，在这样一间破败的酒馆里藏身的理由。太荒谬了。
[Dialog]
[charslot(slot="m",name="avg_npc_1698_1#6$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="m")]
[name="作家"]荒谬的事还多着呢。
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="n")]
[name="神秘的女性"]您就这么喜欢吊人胃口吗？冷眼旁观那些急着知道结局的读者，从中获取心灵上的满足？
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="m")]
[name="作家"]之前倒确实有几位尽责得过了头的信使找到了这里，把读者的信给我送了过来。
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="n")]
[name="神秘的女性"]您果然以此为乐。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[name="作家"]以此为乐？我看都不去看，直接把信扔进那边的火炉里。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="n")]
[name="神秘的女性"]真过分。
[name="神秘的女性"]不仅如此，您发表的故事集里就没有一个故事是没被截断的，太过分了。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[name="作家"]很简单，我不知道该写什么。我写不出结局。
[name="作家"]请回吧，小姐。你显然是个受过良好教育的人，这间粗俗的酒馆不适合你，这几个半截子的故事也不至于让你如此费心。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="n")]
[name="神秘的女性"]为什么这么急着下逐客令呢？或许我可以帮您一把。
[Dialog]
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="m")]
[delay(time=1.2)]
[charslot]
作家重新打量起眼前的人。即便有兜帽作为遮挡，自己也能看到她面色苍白，想必十分虚弱。
这个人一来这座荒村就直奔这家酒馆，来之前显然做了不少调查，看来一时半会儿打发不掉。
作家这么想着，从散落着纸牌和筹码的桌子上抓起黏糊糊的杯子，往嘴里灌了一大口发馊的啤酒。
[Dialog]
[PlaySound(key="$d_avg_drinkswllw",volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="m")]
[name="作家"]那好，你打算给这个故事一个什么样的结局？
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="n")]
[name="神秘的女性"]为什么是我来给呢？
[name="神秘的女性"]作者毕竟是您，我只想给您提供一些或许能点燃灵感的素材。
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="m")]
[name="作家"]素材？
[name="作家"]去年秋天，你也从那座城市死里逃生？
[charslot(slot="m",name="avg_npc_1698_1#7$1",focus="n")]
[name="神秘的女性"]毕竟只要是经历过的人都看得出，您的故事正是以那段时日为蓝本。
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[name="作家"]......
[name="作家"]那就请吧。我等着听你的素材。
[Dialog]
[charslot(duration=0.5)]
[delay(time=1)]
[stopmusic(fadetime=3)]
[focusout(duration=2.5, type="bg", from=0, to=1, block=false)]
[delay(time=1)]
[name="神秘的女性"]那么，在早已被天灾摧毁的塔拉王城旧址最深处......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="59_g14_galekingruins_n",screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.7, block=true)]
[delay(time=1)]
[PlayMusic(intro="$ghosthunter_intro", key="$ghosthunter_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[focusout(duration=1.5, type="bg", from=1, to=0, block=true)]
[delay(time=1)]
在早已被天灾摧毁的塔拉王城旧址最深处，金属炉中的火焰在某个短暂而安宁的日子被人熄灭。
这本不是什么要紧事，但红龙仍然来到了这里。
[Dialog]
[CameraEffect(effect="Grayscale", fadetime=1.5, keep=true, initamount=0.7, amount=0, block=true)]
[delay(time=1)]
[Dialog]
[charslot(slot="m",name="avg_450_necras_1#15$1",duration=1)]
[delay(time=1.5)]
[PlaySound(key="$e_skill_ignite_cast", volume=0.6)]
[PlaySound(key="$b_char_fireharm", volume=0.8,delay=0.3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.2, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_450_necras_1#15$1",focus="m")]
[name="红龙"]在抗拒被点燃？
[name="红龙"]还是说，即便是数百年后另一位不祥的异类，也不能重燃被时光腐蚀殆尽的渴求与怨恨？
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="红龙"]或者，我只是太过拘谨了？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_deathfire", volume=1)]
[bgeffect(name="$eb_eblana_attack",layer = 1)]
[delay(time=0.7)]
[PlaySound(key="$d_avg_churchfire", volume=0.3, loop=true, channel="bse")]
[delay(time=1.5)]
紫色的火焰腾地烧到炉外。
而在火焰的映照下，红龙的脸色分明比方才苍白了几分。
[Dialog]
[stopsound(channel="bse", fadetime=2)]
[bgeffect(layer = 1, fadetime = 1.5)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1690_1#5$2",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1690_1#5$2",focus="m")]
[name="？？？"]......
[charslot(slot="m",name="avg_450_necras_1#13$1",focus="m")]
[name="红龙"]睡醒了吗？
[name="红龙"]或者，需不需要我提醒你的身份......
[charslot(slot="m",name="avg_450_necra

... (全文23848字符)
```

### level_act41side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Subtitle(text="你刚刚讲到......是了，夏末节前夜，太阳还挂在天上的时候。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="夏末节的夜晚将连通生命与死亡，这并不是迷信，或者，它早就超出了迷信的范畴。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="塔拉的传说中，无数伟业与惨剧都在这一夜发生，而这些传说往往不会费心在日期上故弄玄虚。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="只要无数传说都重合在这一天，只要塔拉人还隐约记得要在这一天庆祝丰收，点起火焰，它就不只是一个无聊的时节。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="它自身就是神话最好的注脚。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......哦，还有，我替你故事里的角色取些更贴切的名字，想必你也不会在意的，对吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="59_g10_indoor",screenadapt="coverall")]
[Subtitle(text="太阳已经西斜。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们是还没想好该如何见这最后一次面吗？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Delay(time=2)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1684_1#2$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1685_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1685_1#1$1",focus="r")]
[name="冰冷的幼龙"]拉芙希妮，你怎么又在吃饭时躲进自己房间里了？
[charslot(slot="l",name="avg_npc_1684_1#13$1",focus="l")]
[name="温热的幼龙"]爸爸生气了吗？
[charslot(slot="r",name="avg_npc_1685_1#1$1",focus="r")]
[name="冰冷的幼龙"]没有，不过快了。
[charslot(slot="l",name="avg_npc_1684_1#14$1",focus="l")]
[name="温热的幼龙"]我这就去——
[charslot(slot="r",name="avg_npc_1685_1#22$1",focus="r")]
[name="冰冷的幼龙"]你桌上是什么？
[charslot(slot="l",name="avg_npc_1684_1#12$1",focus="l")]
[name="温热的幼龙"]没什么！
[Dialog]
[charslot]
年幼的红龙试图用身体挡住姐姐的视线，但这完全是徒劳。
她桌上放着一个小小的纸盒，里面仔细地用棉花铺好，上面躺着一只已经死去，但尚有余温的小小羽兽。
羽兽的腿似乎在活着的时候断掉了，旁边散落着硬纸做的不成功的夹板，还有几颗麦粒。
[charslot(slot="l",name="avg_npc_1684_1#3$1",focus="l")]
[charslot(slot="r",name="avg_npc_1685_1#22$1",focus="l")]
[name="温热的幼龙"]这是每天早上都来我窗前唱歌的羽兽，不知为什么变成了这个样子......我想救它，可是......
[charslot(slot="r",name="avg_npc_1685_1#14$1",focus="r")]
[name="冰冷的幼龙"]......
[charslot(slot="l",name="avg_npc_1684_1#2$1",focus="l")]
[name="温热的幼龙"]求你了，姐姐，求你去告诉爸爸，我只是不舒服，我明天会按时出现在餐桌前......我今晚就去把它埋到院子里。
[charslot(slot="r",name="avg_npc_1685_1#22$1",focus="r")]
[name="冰冷的幼龙"]你要放弃了吗？
[charslot(slot="l",name="avg_npc_1684_1#2$1",focus="l")]
[name="温热的幼龙"]它已经死了呀，姐姐。
[charslot(slot="r",name="avg_npc_1685_1#1$1",focus="r")]
[name="冰冷的幼龙"]是吗？
[Dialog]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="r",name="avg_npc_1685_1#6$1",focus="r")]
[PlaySound(key="$e_atk_magic_n",volume=0.5)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=1)]
[charslot]
紫色的火焰从羽毛间渗入羽兽已然冰冷的尸体。
在两人的注视之下，羽兽缓缓站了起来，断掉的腿硬邦邦地直抵在棉花上，支撑着僵硬的躯壳。
[charslot(slot="l",name="avg_npc_1684_1#2$1",focus="r")]
[charslot(slot="r",name="avg_npc_1685_1#1$1",focus="r")]
[name="冰冷的幼龙"]好了，你想让它飞起来吗，还是唱首歌给你听？
[charslot(slot="l",name="avg_npc_1684_1#12$1",focus="l")]
[name="温热的幼龙"]不，不——不该是这样的，不是的！
[charslot(slot="r",name="avg_npc_1685_1#16$1",focus="r")]
[name="冰冷的幼龙"]......
[name="冰冷的幼龙"]如果你不想这样，为什么不在它还活着的时候用你的火呢？
[charslot(slot="r",name="avg_npc_1685_1#17$1",focus="r")]
[name="冰冷的幼龙"]你的羽兽原本还可以活上很久。你知道自己本不必拘泥于那些庸人的做法。
[charslot(slot="l",name="avg_npc_1684_1#3$1",focus="l")]
[name="温热的幼龙"]不，妈妈告诉过我，把火焰吞下去，藏起来，不要被人看到......
[charslot(slot="r",name="avg_npc_1685_1#1$1",focus="r")]
[name="冰冷的幼龙"]有谁会看到呢？
[Dialog]
[charslot]
幼龙移开视线，不去看姐姐的眼睛，却正好看到了僵硬地站在棉花小床上的羽兽。
那羽兽眼中燃烧着紫火，就连略略歪着脑袋的样子，都和姐姐一模一样。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Subtitle(text="或者，我们心中都还抱着不切实际的奢望？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[CameraEffect(effect="Grayscale", amount=0.8, fadetime=0, keep=true)]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_226_weed_1#1",duration=1.5)]
[Delay(time=2.5)]
[name="高尚的红龙"]姐姐，你身上有血......你受伤了？！
[charslot(slot="m",name="avg_450_necras_1#6$1",focus="m")]
[name="贪婪的红龙"]我的血不多，那个大公爵派来的探子的血不少。
[charslot(slot="m",name="avg_226_weed_1#1",focus="m")]
[name="高尚的红龙"]我来替你包扎......
[charslot(slot="m",name="avg_450_necras_1#1$1",focus="m")]
[name="贪婪的红龙"]沃里克伯爵呢？
[charslot(slot="m",name="avg_226_weed_1#6",focus="m")]
[name="高尚的红龙"]他去......办事。
[charslot(slot="m",name="avg_450_necras_1#15$1",focus="m")]
[name="贪婪的红龙"]是的，他一向告诉我们自己是去办事，而你则满足于这个字眼。
[charslot(slot="m",name="avg_450_necras_1#14$1",focus="m")]
[name="贪婪的红龙"]他甚至放任那位探子，在自己去“办事”的时候和你探讨诗歌。
[charslot(slot="m",name="avg_226_weed_1#2",focus="m")]
[name="高尚的红龙"]我以为我没有泄漏任何跟我们的身世、跟伯爵的理想相关的消息......
[charslot(slot="m",name="avg_450_necras_1#5$1",focus="m")]
[name="贪婪的红龙"]伯爵府上的每个人都知道你从不说多余的话，沃里克伯爵想确定的从来都不是这个。
[charslot(slot="m",name="avg_226_weed_1#2",focus="m")]
[name="高尚的红龙"]......
[charslot(slot="m",name="avg_450_necras_1#15$1",focus="m")]
[name="贪婪的红龙"]没错，就算你放跑了探子，沃里克伯爵也总有方法将他掐灭在黑暗中，而我们身上又会再多一条细细的枷锁。
[charslot(slot="m",name="avg_226_weed_1#2",focus="m")]
[name="高尚的红龙"]对不起，我......
[charslot(slot="m",na

... (全文14827字符)
```

### level_act41side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[Subtitle(text="<i>在母亲与黑雾拼死一搏前，森林中的守灵人寻来，提醒她还没为自己的女儿好好举办一场葬礼，那才是此刻最紧要的事情。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>可母亲已决定与黑雾以死相搏，直到守灵人唱起古老的歌谣，母亲不禁泪如雨下。最终选择依照传统，先为女儿守灵。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>葬礼上，她对着象征女儿灵魂的紫色篝火哭泣了整整一夜。倾盆的泪水熄灭了城中燃烧的烈焰，甚至葬礼的紫火也快被浇熄。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>当守灵人询问母亲是否仍要前去与黑雾死战时，母亲面上挂着泪珠，望向行将熄灭的篝火，说道：</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>“我仍有一整个王国的人民要护佑，我不能弃他们于不顾。”</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<i>就在母亲说出这句话的同时，微弱的紫色火焰突然变成了明亮盛大的橙黄，复活的女儿从火中缓缓走出，与母亲紧紧相拥。</i>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_snowconutryinside",screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[name="作家"]这就是结局了。真正的、并非断章的......
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="m")]
[name="作家"]......结局。
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="n")]
[name="神秘的女性"]恭喜。您得到了真相。
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="m")]
[name="作家"]皆大欢喜，皆大欢喜！
[name="作家"]这都是拜您所赐！来，干杯，喝完这杯酒，我就去把故事的结尾写下来发表出去......
[charslot(slot="m",name="avg_npc_1698_1#1$1",focus="m")]
[name="作家"]呃......可能不太好发表，但，只要它已经完成了——
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[Delay(time=1)]
[name="神秘的女性"]葬礼，篝火，复活......您的确全都瞧见了。
[name="神秘的女性"]我没想过，您居然有如此的勇气，在逃离之后又回到了纳斯尔纱......
[name="神秘的女性"]“歌唱家”先生。
[charslot(slot="m",name="avg_npc_1698_1#6$1",focus="m")]
[name="“歌唱家”"]至少结局是好的，不是吗？爱布拉娜带着死去的人离开，再也没有回来。
[name="“歌唱家”"]而您，拉芙希妮殿下，我愿意把这个故事献给您。至于是发表，是封存，还是随着我这样的深池余党一同消失，我都心甘情愿。
[Dialog]
[charslot(duration=0.5)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=2)]
[Image(image="59_i12", screenadapt="coverall",fadetime=2, xScale=1.6, yScale=1.6,y=200,fadetime=2,block=false)]
[name="神秘的女性"]真好啊......
[Dialog]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[name="神秘的女性"]早知如此，放任你用“歌唱家”这样的名字自我贬低，倒的确是把你看得小了。
[name="“歌唱家”"]您——
[name="“歌唱家”"]等等？什么？！
[name="“歌唱家”"]你不是拉芙希妮，你是——爱布拉娜？！
[Dialog]
[charslot]
[playsound(key="$d_avg_bowl_smash", volume=1)]
[PlaySound(key="$d_avg_bottlecollide", volume=0.8,delay=0.4)]
[Delay(time=1.5)]
[ImageTween(yFrom=200,yTo=0,duration=20,xScaleFrom=1.6,xScaleTo=1,yScaleFrom=1.6,yScaleTo=1, block=false)]
[Delay(time=3)]
曾经的“歌唱家”狂乱地挥舞手臂，连酒都碰洒在桌上。
[name="“歌唱家”"]你已经死了！你不该还活着，你已经被两次杀死，一次被枪尖，一次被火焰——你不该在这里！
[name="“歌唱家”"]......
[Dialog]
[Delay(time=1)]
[name="“歌唱家”"]难道是我死了？哈哈，哈哈哈，别开玩笑了......死去的红龙，回你该回的地方去！
[name="“歌唱家”"]是的，一定是的，你在撒谎，你根本没有死，你杀了拉芙希妮，一切都是假象，一切都是谎言——
[name="爱布拉娜"]要是果真如此，你的故事又该怎么办？
[name="“歌唱家”"]我的......故事？
[name="“歌唱家”"]......
[name="爱布拉娜"]唉，终于安静下来了。
[name="“歌唱家”"]你不该还活着，不该还活着......
[name="爱布拉娜"]可死亡对我而言从来都不是沉眠。我驱策生命能做到的，驱策死亡亦然。
[Dialog]
[Image(fadetime=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]看在你终于讲完了故事的分上，“作家”，我可以告诉你，重要的唯有火焰。
[charslot(slot="m",name="avg_npc_1698_1#3$1",focus="m")]
[name="“歌唱家”"]......紫火。
[charslot(slot="m",name="avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]紫火，你故事中看似缥缈，却绝非虚构和粉饰的东西。
[name="爱布拉娜"]我的确已在漫长的战争中将太多火焰分给他人，变得虚弱无力。
[charslot(slot="m",name="avg_450_necras_1#15$2",focus="m")]
[name="爱布拉娜"]但火会蔓延，火会吞噬，火会增殖自身。
[name="爱布拉娜"]“加斯特里尔”号上与食腐者一战后，我迫切需要把那些火，那些我分出去，在原野上，在遗迹中，在人的心里增殖的火收归己身。
[charslot(slot="m",name="avg_npc_1698_1#3$1",focus="m")]
[name="“歌唱家”"]哈，简直就像在放高利贷一样......
[charslot(slot="m",name="avg_450_necras_1#14$2",focus="m")]
[name="爱布拉娜"]征收血税，这不是一位君王最基础的权力吗？
[name="爱布拉娜"]所不同的是，凡俗的君王征收血税，充实他们的兵员，争夺最多不过几百年就离他们而去的领土和人民。
[name="爱布拉娜"]而我征收血税，将其与红龙的火焰共同铺就路途，将生命与死亡连通，让困于生死之间的人将我仰望。
[charslot(slot="m",name="avg_npc_1698_1#5$1",focus="m")]
[name="“歌唱家”"]胡言乱语......
[charslot(slot="m",name="avg_450_necras_1#15$2",focus="m")]
[name="爱布拉娜"]对你而言这的确像是胡言乱语，因为你无法理解，将足以焚尽一整个国度的死亡收归它们的主人，究竟会发生什么。
[charslot(slot="m",name="avg_450_necras_1#6$2",focus="m")]
[name="爱布拉娜"]那是延续千年的怨恨、悲伤和愤怒，当它们聚集到我身上，又怎么可能简简单单地放我的意识和身体消散？
[charslot(slot="m",name="avg_npc_1698_1#5$1",focus="m")]
[name="“歌唱家”"]沦为怨恨的奴隶，真是适合你的下场——
[charslot(slot="m",name="avg_450_necras_1#1$2",focus="m")]
[name="爱布拉娜"]忘了你故事里我的台词了吗？
[name="爱布拉娜"]那些自以为能将我塑造成型的，不过是碰巧长成了能让我得心应手地挥舞的样子而已。
[name="爱布拉娜"]假如我真的沦为了那些东西的奴隶，怕是在见你的第一眼，就已经把你烧成灰烬了。
[charslot(slot="m",name="avg_npc_1698_1#4$1",focus="m")]
[name="“歌唱家”"]......疯子！
[name="“歌唱家”"]所以你才让威灵顿在黑林中驻扎，封锁了整个纳斯尔纱，甚至延续了宵禁。你从一开始......就没打算放纳斯尔纱一条生路！
[charslot(slot="m",name="avg_450_necras_1#15$2",focus="m")]
[name="爱布拉娜"]多谢你愿意挑明这个令人不快的谜底。黑雾，威灵顿。
[charslot(slot="m",name="avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]在“加斯特里尔”号上目睹的银石崖一战，是否仍然常常出现在你每个需要酒精帮助才能入眠的梦里？
[name="爱布拉娜"]它阴魂不散，是吗？否则，你不会执着于描绘那乌云一般盘旋在人们头顶的黑雾，却又不敢给它下一个定义。
[name="爱布拉娜"]宵禁一开始并无问题。那时纳斯尔纱城内的确还有几个维多利亚探子没有落网。
[name="爱布拉娜"]拉芙希妮进入纳斯尔纱的时候，威灵顿公爵陡然加紧了对纳斯尔纱的封锁，因为他要杜绝两条红龙的消息走漏的一切可能。
[charslot(slot="m",name="avg_npc_1698_1#4$1",focus="m")]
[name="“歌唱家”"]那些去而复返的粮食......
[name="“歌唱家”"]哦，校官不仅是你最亲近的近侍，也是威灵顿的赤铁近卫队队长，他去讨要粮食，威灵顿还真的给了他这个面子......
[charslot(slot="m",name="avg_450_necras_1#13$2",focus="m")]
[name="爱布拉娜"]到了拉芙希妮离开纳斯尔纱，去找守灵人的时候，威灵顿只是对她失望了，仅此而已。
[name="爱布拉娜"]你确实得感谢拉芙希妮。如果不是失望的威灵顿放松了对纳斯尔纱的封锁，你绝无可能从黑林中逃脱。
[charslot(slot="m",name="avg_450_necras_1#15$2",focus="m")]
[multiline(name="爱布拉娜")]至于你讳莫如深的那场庆功会......
[charslot(slot="m",name="avg

... (全文30385字符)
```

### training_act41side_01_a

```
[header(is_skippable=false, is_tutorial=true)]
[inputblocker(blockInput=true)]
[battle.delay(time=4.5)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_fang")]小心，这里的敌人比想象中难缠。
[popupdialog(dialogHead="$avatar_kroos", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]没关系，我来支援啦～
[battle.pause(pause=false)]
```

### training_act41side_01_b

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true)]
[tutorial(focusWidth=220, focusHeight=220, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_kroos", tileY=1, tileX=5)]咦？原来只是一些小家伙。
[tutorial(focusWidth=220, focusHeight=220, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=1, dialogHead="$avatar_kroos", tileY=1, tileX=5)]看来处在我们<@tu.kw>攻击范围</>之外的时候，它们才会比较危险啊。
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_beagle", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]芬、克洛丝，敌人数量太多了，我们也来支援！
[battle.pause(pause=false)]
```

### training_act41side_01_c

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true)]
[popupdialog(dialogHead="$avatar_lava", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]当心！
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_lava", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=4, tileX=1)]这边也有敌人出没，交给我吧。
[battle.pause(pause=false)]
[battle.delay(time=5)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true, black=0.3)]
[popupdialog(dialogHead="$avatar_lava", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", protectTime=0.5)]不好！我的视野被挡住了，找不到敌人，也<@tu.kw>发动不了攻击</>。
[battle.lockfunction(mask="SYSTEM_MENU_INTERACT")]
[inputblocker(blockInput=true, validWidth=40, validHeight=40, black=0, tileX=3, tileY=4)]
[tutorial(focusWidth=100, focusHeight=100, animStyle="Click", focusStyle="HighlightCircle", protectTime=0.5, dialogHead="$avatar_lava", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", waitForSignal="char_info", tileY=4, tileX=3, charId="char_121_lava")]让我看看......
[inputblocker(blockInput=false)]
[tutorial(focusX=-133, focusY=23, focusWidth=126, focusHeight=275, animStyle="Highlight", focusStyle="HighlightRect", black="0.5", protectTime=0.5, dialogHead="$avatar_lava", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", waitForSignal="any")]啧，我攻击不了处在这个位置的敌人。
[inputblocker(blockInput=true)]
[tutorial(focusX=-79, focusY=21, focusWidth=506, focusHeight=469, animStyle="Highlight", focusStyle="HighlightRect", black="0.5", protectTime=0.5, dialogHead="$avatar_lava", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]原来这些线表示了所有<@tu.kw>我方单位</>的攻击范围总和，这个情报应该有用吧。
[battle.unlockfunction(mask="SYSTEM_MENU_INTERACT")]
[battle.pause(pause=false)]
```

### training_act41side_01_d

```
[header(is_skippable=false, is_tutorial=true)]
[battle.pause(pause=true)]
[inputblocker(blockInput=true)]
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_kroos", tileY=2, tileX=7)]说起来，这些树丛一样的东西，好像从刚刚开始就在不断生长呢。
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=2, tileX=6)]嗯，看起来它们会朝周围不断生长。
[tutorial(black="0.5", protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]我来试试能不能阻止树丛继续生长——
[battle.pause(pause=false)]
[battle.delay(time=4)]
[battle.pause(pause=true)]
[tutorial(focusWidth=150, focusHeight=150, animStyle="Highlight", focusStyle="HighlightCircle", black="0.5", protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y", tileY=2, tileX=6)]能做到，但干员部署在草毯上时，会受到<@tu.kw>持续的法术伤害</>。
[inputblocker(blockInput=true, black=0.3)]
[tutorial(black="0.5", protectTime=0.5, dialogHead="$avatar_melan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]我来吸引这边敌人的火力，大家专心战斗吧！
[battle.pause(pause=false)]
```


## 统计

- 总字符数：359497
- 对话行数：2589


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
