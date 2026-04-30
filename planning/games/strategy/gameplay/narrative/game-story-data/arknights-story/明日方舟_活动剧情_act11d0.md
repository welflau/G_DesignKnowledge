# 明日方舟 · 活动剧情 · act11d0（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act11d0」完整剧情脚本（23个文件，2541行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act11d0
- 脚本文件数：23

### act11d0_04

```
[HEADER(is_skippable=true, is_autoable=false)] 活动11d0_04
[PopupDialog(dialogHead="$avatar_folnic")] 暴徒们比想象中多，他们占领了城镇。我答应过阿米娅，不让你卷入过于激烈的战斗......
[PopupDialog(dialogHead="$avatar_lisa")]——不，我会保护好我自己的，我也要保护亚叶姐姐。
[PopupDialog(dialogHead="$avatar_folnic")] ......我？
[PopupDialog(dialogHead="$avatar_lisa")] 因为亚叶姐姐现在的表情......让人很不安。
[PopupDialog(dialogHead="$avatar_folnic")] 好吧......表情......？真有那么糟吗......抱歉。
```

### level_act11d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 1上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
2:10 P.M.    天气/晴
莱塔尼亚移动城镇沃伦姆德，这座昔日繁华的商业都市如今人迹罕见
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
城镇议事厅
[dialog]
[delay(time=1)]
[Character(name="avg_npc_068")]
[name="镇民代表"]  塞弗林·霍索恩长官，你刚才去哪儿了？
[name="镇民代表"]  决策会的时候你不在场，让我们怎么做决定？
[Character]
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_066#5",fadetime=1,block=true)]
[delay(time=1)]
[name="塞弗林"]  ......那在你们决定我儿子命运的时候，我在场吗？
[Character(name="avg_npc_068")]
[name="镇民代表"]  呃......那件事，塔佳娜应该已经......
[Character(name="avg_npc_066#5")]
[name="塞弗林"]  是，告诉我了。让塔佳娜来告诉我的。我只是提醒你们一下你们所做的事。
[name="塞弗林"]  现在情况怎么样？
[Character(name="avg_npc_068",name2="avg_npc_066#5",focus=1)]
[name="镇民代表"]  ......感染者们仍旧在抗议，他们甚至开始排斥新加入社区的感染者。
[Character(name="avg_npc_068",name2="avg_npc_066#5",focus=2)]
[name="塞弗林"]  他们想要什么？
[Character(name="avg_npc_068",name2="avg_npc_066#5",focus=1)]
[name="镇民代表"]  他们......他们认为那场火灾是有人“别有用心”安排的，他们要为安托医生和死去的感染者求个说法。
[Character(name="avg_npc_068",name2="avg_npc_066#5",focus=2)]
[name="塞弗林"]  ......别有用心，求个说法，很好，有人在煽动他们。
[name="塞弗林"]  就算是感染者，他们中的大部分也曾是沃伦姆德的居民，他们不会做出这么低劣的栽赃。
[name="塞弗林"]  他们有和那些武装可疑分子接触吗？
[Character(name="avg_npc_068",name2="avg_npc_066",focus=1)]
[name="镇民代表"]  ......暂时没有。
[name="镇民代表"]  但是，但是那些可疑分子一直在村庄周围徘徊，我担心他们会影响到那些抗议者。
[dialog]
[Character]
[playsound(key="$d_gen_transmissionget", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_068")]
[name="镇民代表"]  等等，是岗哨的联络——
[Character(name="avg_npc_068",name2="avg_npc_066#5",focus=2)]
[name="塞弗林"]  自便。
[Character(name="avg_npc_068")]
[name="镇民代表"]  ......两个人？是感染者吗？
[name="镇民代表"]  自称罗德岛？我记得这个名字——
[Character(name="avg_npc_068",name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  ......是安托医生所属的公司，唉，该来的迟早要来。
[Character(name="avg_npc_068",name2="avg_npc_066#2",focus=1)]
[name="镇民代表"]  那、那该怎么办？
[Character(name="avg_npc_066#2")]
[name="塞弗林"]  安托医生是一位值得尊敬的感染者。他们也许是来调查安托医生的踪迹的，他们有权利知道真相。
[name="塞弗林"]  放他们进来吧。
[Character(name="avg_npc_068")]
[playsound(key="$d_gen_transmissionget", volume=0.6)]
[name="镇民代表"]  ......你也听到了，按长官说的做。
[name="镇民代表"]  呼，可是这样真的没问题吗？如果他们和那些武装人员有关的话？
[Character(name="avg_npc_066")]
[name="塞弗林"]  大裂谷，火灾，感染者。我们还有疑神疑鬼的余裕吗？
[Character(name="avg_npc_068")]
[name="镇民代表"]  可他们知道所有事情后会怎么样？罗德岛如果向我们索赔追责，只会让沃伦姆德雪上加霜！
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......所以呢？
[name="塞弗林"]  把他们拒之门外？还是欺骗他们？告诉他们安托医生带着矿石病患者们远足去了？
[Character(name="avg_npc_068")]
[name="镇民代表"]  我知道瞒不住，但这件事也不是你说了算的，不怕一万就怕万一。
[Character(name="avg_npc_066#3")]
[name="塞弗林"]  真相不被任何人决定，不过......算了，随你们吧。
[name="塞弗林"]  我先走了。
[Character(name="avg_npc_068",name2="avg_npc_066#3",focus=1)]
[name="镇民代表"]  走？你又要去哪儿？
[Character(name="avg_npc_068",name2="avg_npc_066#3",focus=2)]
[name="塞弗林"]  ......去解决问题。
[name="塞弗林"]  我只负责保证这座城镇回到正轨，决策过程嘛......你们过家家，我不感兴趣。
[Character(name="avg_npc_068",name2="avg_npc_066#3",focus=1)]
[name="镇民代表"]  等等！喂！
[name="镇民代表"]  我知道你现在很难过，我也知道我们做了很多不太好的事情，但这没办法！
[Character(name="avg_npc_068",name2="avg_npc_066#3",focus=2)]
[name="塞弗林"]  我知道没办法，这就是我现在还在心平气和地同你说话的理由。
[name="塞弗林"]  罗德岛的事情交给你们了，你们比较擅长这种事。我去看看其他街道的情况。
[name="塞弗林"]  就这样。
[Character(name="avg_npc_068")]
[name="镇民代表"]  塞弗林！塞弗林·霍索恩！你现在才是这里的长官，不要随便乱跑——
[name="镇民代表"]  啧——他这个人总是——
[name="镇民代表"]  ——唉。
[name="镇民代表"]  算了，都是可怜人。塔佳娜，塞弗林，托尔，都是。
[name="镇民代表"]  赶紧把这里收拾一下，罗德岛的人马上就要到了。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Character]
[Background]
[Image(image="ac11_2",xScale=1.2, yScale=1.2,x=0, y=20)]
[ImageTween(xFrom=0, yFrom=20, xTo=0, yTo=-10, xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=0.9, yScaleTo=0.9, duration=30, block=false)]
[Blocker(a=0, fadetime=3, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_358_lisa_1",fadetime=1,block=true)]
[delay(time=1)]
[name="铃兰"]  沃伦姆德，意为第八个月亮，与周围的七座城镇共同组合成了莱塔尼亚北部璀璨的商业聚落——
[name="铃兰"]  书上是这么写的。
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  不过眼前的景象和“商业聚落”根本搭不上边啊。
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  是因为“大裂谷”的事情？
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  嗯。那样规模的天灾并不常见，活性源石裸露在岩壁上，深度也许有上千米，唔啊，回想起来真是触目惊心。
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  可是亚叶姐姐......你当时明明在好奇扔一发炮弹下去会怎么样......
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  不，那是对于活性源石的研究精神，说真的，搞不好真能把整片高地一分为二？
[name="亚叶"]  虽然我们是勉强绕路抵达了，但这座城镇估计现在寸步难行吧。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[Character]
[dialog]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[Character]
[name="镇民"]  这种时候还会有游客？好奇怪的装束，不会是什么危险分子吧？
[name="镇民"]  看看那个尾巴，啊，还有她肩膀上的结晶，是感染者？
[name="镇民"]  可是那个装束，我好像在哪里见到过......是......吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  ......亚、亚叶姐姐，就这么坦荡荡地走在街上真的没关系吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  莱塔尼亚的源石技艺普及带来了两点明显有别于他处的特色，音乐艺术的繁荣，以及，对感染者的宽容态度。
[name="亚叶"]  虽然会被限制人身自由，但至少当你想要活下去的时候，你可以付出代价赢回生活的权利。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  ......代价？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  至少是付得起的代价。
[name="亚叶"]  就算远离了中心，也有冲突和纠纷，但沃伦姆德依旧提供了感染者居住的街道......至少她是这么和我说的——
[Character(name="char_358_lisa_1#3")]
[name="亚叶"]  ——啊，有人来了。
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......嗯？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  （唔？那个叔叔的装束......）
[Char

... (全文11214字符)
```

### level_act11d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 1下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[name="叛乱的镇民"]  那、那些外人为什么要搅和我们的事情！
[name="叛乱的镇民"]  还有你！塞弗林！你的儿子都死在那场火灾里了，你竟然还帮着那些饭桶！
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......把刀放下，告诉我，是谁教唆你们的，是谁给你的武器。
[name="塞弗林"]  最后一次警告。
[Character]
[name="叛乱的镇民"]  呃——！
[Dialog]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral")]
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......都持刀伤人了，躲回家里又有什么用？没关系，宪兵队会挨个敲门问责。
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  只是问责？
[Character(name="avg_npc_066", name2="char_345_folnic_1#4",focus=1)]
[name="塞弗林"]  “问责”的具体过程没必要告诉游客。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  那你没有什么要对“游客”说的吗？“长官”？
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  ......嗯，你们很强，原来医生还能这么能打，真是长见识。
[name="塞弗林"]  以及......非常感谢刚才的帮助。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  一般来说，我们被称为“干员”的情况更多。
[name="亚叶"]  现在可以告诉我安托在哪里了吗？
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  ......这里不安全，我们回去再说。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
[stopmusic(fadetime=3)]
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  ......
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  辛苦了，亚叶姐姐。
[name="铃兰"]  对不起，没能在战斗里帮上太多忙......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#2",focus=2)]
[name="亚叶"]  没关系，你已经很努力了。不如说如果早知道现在沃伦姆德是这个状态，我就不会把你带来了。
[name="亚叶"]  就算只是解决一些纠纷，我也不想你太早卷入——
[Character(name="char_358_lisa_1#2", name2="char_345_folnic_1#2",focus=1)]
[name="铃兰"]  亚叶姐姐！
[Character(name="char_358_lisa_1#2", name2="char_345_folnic_1#2",focus=2)]
[name="亚叶"]  ——唉，好好，小丽萨长大了。没受伤吧？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#2",focus=1)]
[name="铃兰"]  嗯，没事的！
[name="铃兰"]  不过亚叶姐姐刚才一直心不在焉的，怎么了吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......这附近是隔离区。闹事的感染者被赶走后，这里就变回了安安静静的样子。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  嗯......好像和其他地方没有太大区别呀？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  没有太大区别，对，商店，咖啡厅，甚至还有音乐馆和艺术沙龙的广告......
[name="亚叶"]  他们不用被卫兵追捕，不会被流放到冻土上，不仅有着正常的生活空间......怎么讲呢，好像还过得挺好。
[name="亚叶"]  感染者的待遇还真是多种多样啊。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  如果大家都能对感染者这么温柔的话......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  那我们就要失业了。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  欸！？虽然真的因为这种原因失业的话，我也会很高兴的！但、但我才刚当上干员......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#2",focus=2)]
[name="亚叶"]  只是个玩笑啦......感染者能上街随便走动这件事只说明沃伦姆德现在处境特殊。
[name="亚叶"]  ......他们有什么瞒着我们。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#2",focus=1)]
[name="铃兰"]  欸？怎么突然就——
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  嘘！小声点！就是等那个宪兵走远了才说的！
[name="亚叶"]  这些感染者的反抗态度很奇怪。他们说过“火灾”和“医生”之类的话，不是吗？
[name="亚叶"]  还有那个宪兵明明知道我们的身份，我问了几次安托的事情，只是回答一句她在哪里很难吗？
[name="亚叶"]  而且这里......这座城镇现在的气氛有点过于诡异了。
[name="亚叶"]  就算是莱塔尼亚也不至于让感染者满大街乱走，卫兵呢？为什么没有人制止？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  是有点奇怪......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  我有不好的预感。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  也、也许只是因为城镇的情况不太好，大家情绪比较激动？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......只是这样就好了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_069#2",fadetime=1,block=true)]
[delay(time=1)]
[name="塔佳娜"]  二位辛苦了，真是抱歉，一来就被卷入了这样的事情里，我很惭愧......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1",focus=2)]
[name="亚叶"]  啊......没关系。
[name="亚叶"]  你是这里宪兵队的一员吗？
[Character(name="avg_npc_069", name2="char_345_folnic_1",focus=1)]
[name="塔佳娜"]  不算是。不过沃伦姆德的大家都接受过正规军事训练，特殊情况来临的时候，我们都有拿起武器的责任......
[name="塔佳娜"]  啊，不过伯父......塞弗林长官确实是本镇最高长官。
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......一个偷懒抽烟的中年男？不负责任和玩忽职守并不能给人高深莫测的感觉，很遗憾。
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  长官现在这样这是有理由的——
[name="塔佳娜"]  不......没什么......
[name="塔佳娜"]  对了，怎么称呼二位？
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......干员亚叶，这位是干员铃兰。
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  亚叶，铃兰......这是你们的代号？
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  在我们那儿没有多少人会用真名工作，就和“安托”一样。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  安托医生......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  看你的反应，你们认识。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  嗯......抱歉，我知道您心中疑惑，但塞弗林长官会解答你们的。这不是......不是我擅自做主的范畴。
[name="塔佳娜"]  总之，请跟我来。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......我明白了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b

... (全文14653字符)
```

### level_act11d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 2上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
3:59 P.M.    天气/多云
移动城镇沃伦姆德，感染者居住区，十二音街道
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  亚叶姐姐......你在生气吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  他们的态度意味着什么，我太清楚了......
[name="亚叶"]  但是，但是安托不会有事的，她比我们任何人都熟悉莱塔尼亚！
[Character(name="char_358_lisa_1#2", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  嗯！安托姐姐一定没事的。
[name="铃兰"]  但愿......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.3)]
[Character(name="avg_npc_065")]
[name="镇民"]  ......
[Character]
[Dialog]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.3)]
[Character(name="avg_npc_068")]
[name="镇民"]  ......
[Character]
[Dialog]
[delay(time=1)]
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  总觉得这附近有点安静得可怕......？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  嗯，跟紧点。
[name="亚叶"]  看上去不光有普通的居民，还有很多感染者，不过这不是重点。
[name="亚叶"]  刚才阻止那些暴徒的时候我就在想了，这个街道的规模，怎么看都只是普通的街区吧？
[name="亚叶"]  只是把感染者们集中起来生活，并没有什么明面上的差别对待。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  嗯......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  但实际上，感染者依旧被约束了人身自由，而且除了那些能够“物尽其用”的感染者，大部分人这辈子和坐牢没什么区别......
[name="亚叶"]  只不过牢狱变成了一条街道，多了几十倍的狱友罢了。
[name="亚叶"]  看这儿，这家面包店多久没有开过门了？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  啊......我好像看到源石虫爬过去了......好不卫生啊。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  店门口的灰尘和落叶都没人打扫，这个社区没有在正常运作。
[name="亚叶"]  虽说是在特殊时期，但街上见不到一个买卖面包的人？公共交通也停摆了，这也太不自然了......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  因为，因为之前的事情？店主被吓走了之类的？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  但至少他们还有活着的权利，他们——
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  亚叶姐姐......！声音小点！嘘！
[Dialog]
[Character]
[name="镇民"]  ......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......我没有在指责他们，我只是说......关于“武装感染者”的话题。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  他们会是......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  那个宪兵提到了“萨卡兹”，这是首先要确定的事情。
[name="亚叶"]  如果真的和我们所知道的“感染者武装组织”有关，我们必须警觉起来。这里的情况也许比那个宪兵说的还要复杂。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  是这样吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  如果感染者的情况够好，那只是因为处境还不够绝望。
[name="亚叶"]  他们肯定还有事情瞒着我们。
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  亚叶姐姐？
[name="铃兰"]  不用那么紧张喔，安托姐姐可是很聪明的。
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  我......
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  从刚才开始，亚叶姐姐就一直是很可怕的状态嘛。没关系的。
[name="铃兰"]  只要我们好好努力，就能出色地解决这件事，就像各位干员前辈那样！
[name="铃兰"]  所以稍微放轻松一点吧？
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#2",focus=2)]
[name="亚叶"]  ......哈，我又被小丽萨安慰了？这是怎么了？
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#2",focus=1)]
[name="铃兰"]  嘿嘿，烦恼不分大小啦。
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  二位，请稍等——！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  是你？
[name="亚叶"]  我记得我说过我们不需要帮助，只需要权限就......
[Character(name="avg_npc_069#4", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  抱歉，虽然亚叶小姐那么说了，但是毕竟情况特殊，二位人生地不熟的，如果出了什么意外，我们无法承担。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  ......亚叶姐姐。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  好吧......如果有本地人在身边，也许这里的居民也不会这么害怕我们了吧。
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  没错！咳咳！十二音街道原本是沃伦姆德最大的感染者聚集区......
[Character(name="avg_npc_069", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  不过现在因为某些原因，这里也是抗议者最多的地方。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  所以亚叶小姐，现在打算怎么做？
[name="塔佳娜"]  其实我并不是很建议深入这里......不过如果您想了解沃伦姆德的现状，这的确是个好选择。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......先四处逛逛吧，没必要操之过急。
[name="亚叶"]  如果你愿意说点关于安托医生的事情，我会很高兴的。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  亚叶小姐......真的很关心安托医生呢。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  她是我的同学，是我为数不多的好友，更是罗德岛不可或缺的成员。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  ......是吗。
[name="塔佳娜"]  啊，请往这边走，这里是通往秋千广场的路。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  安托在这里做了什么？
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  啊......医治这里的感染者，帮助那些被感染的人做心理辅导。
[name="塔佳娜"]  因为天灾信使的失误，沃伦姆德镇没能在大裂谷出现前及时避开，遭到了不小的损失。
[name="塔佳娜"]  安托医生有机会离开这里，但是她选择了留下。沃伦姆德停泊在现在的位置之

... (全文8571字符)
```

### level_act11d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 2下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_066#5",fadetime=1,block=true)]
[delay(time=1)]
[name="塞弗林"]  ——他们是什么时候潜上来的？
[Character(name="avg_npc_068")]
[name="镇民代表"]  不清楚，但是“留声机”没有启动......
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  我早说过那种实验性的自律施术单元装置不靠谱。
[name="塞弗林"]  只要那些感染者队伍里有其他受过高等教育的莱塔尼亚人，篡夺它们，很简单。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民代表"]  现在说这个也来不及了，感染者居住区到处都有他们的踪迹，呃，他们在煽动感染者。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  ......沃伦姆德的居民都不会那么轻易被煽动起来。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  可，可的确有越来越多人开始抗议，他们聚集在一起——
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  什么诉求？
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  他们要求恢复十二音街道的物资供应......还要求我们撤销对十二音街道的所有隔离措施。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  ......简直胡闹。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  当然，最关键的......还是他们要求对火灾一事给出正式回应......
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  他们根本不关心火灾......看着吧，很快所有人都会忘记这个初衷。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  怎么办？罗德岛的人也已经抵达了，暴露只是时间问题。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  其实我们都清楚，不然我为什么要让塔佳娜去？
[name="塞弗林"]  只不过在向罗德岛摊牌之前，我们得确定他们是一个什么样的公司......确定他们是安托那样的感染者，还是“他们”那样的。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  我不确定这么做对不对......让她们发现我们在隐瞒难道不会加剧分歧？
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  哈......随你怎么想吧，会翻脸的人总会翻脸的，现在沃伦姆德什么情况，你我心知肚明。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  这我清楚——
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  ——那就别指望当什么好人了，好人下场都不太好，结果更重要。
[name="塞弗林"]  咳咳，咳咳......那些真正麻烦的家伙们呢？比如魔族之类的？
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  他们还没有和我们正式接触......
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  一群趁火打劫的劫匪，煽动镇民，创造空隙，很常见的伎俩。
[name="塞弗林"]  他们很谨慎，在试探虚实，如果让他们确信现在的沃伦姆德没有宪兵队驻扎的话......
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  这里每一个人都做好了战斗的准备，我们还有L-44“留声机”防御系统。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  但你们毕竟不是真正的宪兵......唉，我只想少出点人命，咳咳——咳咳咳——
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  请保重身体，沃伦姆德还不能失去你。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  是吗，我倒觉得无所谓......
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  还有谁能在其实一个宪兵都没有的情况下，保证沃伦姆德的治安环境不至于崩溃？
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=1)]
[name="塞弗林"]  只是倔强的血统作祟罢了，高贵的莱塔尼亚人放不下身段行龌龊之事，只要再推他们一把，这里就会变成人间地狱。
[name="塞弗林"]  再不想出办法，我们很快就会玩完的。
[name="塞弗林"]  至少在入冬之前，我们得回到正常的航线，而不是继续停留在这片废土上，饥荒和暴动会毁了这座城镇。
[Character(name="avg_npc_066#5",name2="avg_npc_068",focus=2)]
[name="镇民"]  也许，嗯......你说得对。
[Character(name="avg_npc_066#3")]
[name="塞弗林"]  天已经转凉了，咳——
[name="塞弗林"]  ......但愿沃伦姆德还有其他的选择。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  嘁，你们两个是哪里来的！？
[name="叛乱的镇民"]  你们也要帮着这些蠢货吗，把我们关在这里等死！？
[Character(name="avg_npc_069#3")]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="塔佳娜"]  安分点！
[name="塔佳娜"]  刚才你们在听谁说话？你们告诉了他什么？
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  哈，怕了吗？这就对了！你们当然会怕！
[name="叛乱的镇民"]  就因为你们这些吃官饭的那么无能，沃伦姆德才会沦落到今天的样子！
[name="叛乱的镇民"]  既然如此，不如让我们亲自来掌控一切！
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  这不是任何人的错！
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  把责任怪给天灾就完事儿了吗！？本来就是因为你们的失误，我们才没来得及跑掉！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......你这是无理取闹，感染者。
[name="亚叶"]  你去过其他城市吗？你见过其他感染者生活的处境吗？
[name="亚叶"]  即使是我也能看出沃伦姆德的窘境，其他人和感染者过着一样的日子，这不正是需要携手并进的紧要关头吗？
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  哈？你又是什么人？
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  罗德岛干员，感染者医生，我们会帮助感染者们渡过难关，前提是，不要惹是生非。
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  你、你好，可以的话，请放弃抵抗......
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  嘁！还不是在仗势欺人，要不是我打不过你——！
[name="叛乱的镇民"]  携手并进，帮助？说得好听，是谁先开始反目成仇的，你问问那个女人吧！
[Character(name="avg_npc_069#2")]
[name="塔佳娜"]  这......
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  ......喂，你，你也是感染者吧？
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  嗯。
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  有着九条尾巴的沃尔珀可不常见，你迟早也会沦落到我这样。
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  没有的事......大家都对我很好......
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  就算不是在现在，就算不是在这里，也迟早会的。
[name="叛乱的镇民"]  如果安托医生还在的话——
[Character(name="char_345_folnic_1#5")]
[PlaySound(key="$fightgeneral", volume=0.3)] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_065",name2="char_345_folnic_1#5",focus=1)]
[name="叛乱的镇民"]  呃——！你干什么，松手！
[Character(name="avg_npc_065",name2="char_345_folnic_1#5",focus=2)]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="亚叶"]  你刚才说什么？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#5",focus=1)]
[name="铃兰"]  亚叶姐姐，冷静一点！
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  你刚才说，你刚才说安托医生？
[name="亚叶"]  她现在在哪儿？她怎么样了？
[Character(name="avg_npc_065")]
[name="叛乱的镇民"]  什么她在哪儿，那场火灾夺走了一切！
[name="叛乱的镇民"]  大裂谷出现之后他们就开始排挤我们，他们在恐惧！
[name="叛乱的镇民"]  那些逃难来的感染者也被他们聚集在一起！为什么，为了控制住我们，为了让他们虚伪的人道精神满足，他们把我们豢养

... (全文11248字符)
```

### level_act11d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 3上
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  这......这是......
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  是罗德岛的物资箱没错，有编号，有日期。
[name="亚叶"]  ......是上一次定期联络的时候，是我亲自......
[name="亚叶"]  ......
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  亚叶姐姐......
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  火灾是怎么发生的？
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  事故——本来是这样定性的，但是......
[name="塔佳娜"]  但是这里有明显的施术痕迹，安托医生是个很认真的人，当然不会留下太危险的易燃物。
[name="塔佳娜"]  我们确认不了明显的起火点，帐篷的金属支架都被融化了，而且尸体......
[name="塔佳娜"]  啊......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ......没事的，继续吧。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  根据遗体情况判断，受害者们几乎没能离开帐篷，更不存在挣扎，一瞬间就面目全非。
[name="塔佳娜"]  我不认为普通的火灾能让安托医生和患者们这么简单就被......
[name="塔佳娜"]  除非，是源石技艺，而且不像是普通的火焰，是依赖某种手段达成的瞬间高温......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ——这之中有几个感染者？
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  欸？啊......镇上的感染者有三人，凯文、毕德曼、埃克哈德，他们在这里接受治疗，以及......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  以及......托尔，托尔瓦尔德。
[name="塔佳娜"]  他是长官的独子，是我的老朋友......他不是感染者，他只是去帮忙的，出于好心。
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  ......塔佳娜小姐，如果你感到难过的话，说出来比较好喔。
[Character(name="char_358_lisa_1#3", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  欸？
[Character(name="char_358_lisa_1#3", name2="avg_npc_069#4",focus=1)]
[name="铃兰"]  我能感觉到，这里充斥着悲伤。
[name="铃兰"]  这里......这里有很多不甘心，很多快乐，很多痛苦，但是现在都不存在了。
[Character(name="char_358_lisa_1#3", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  这是......也是某种源石技艺吗？
[Character(name="char_358_lisa_1#3", name2="avg_npc_069#2",focus=1)]
[name="铃兰"]  不——只是看多了这样的事情，大家都喜欢把自己的想法藏起来，但这样不好喔。
[name="铃兰"]  可能只是我多想了，不过，如果总是勉强自己的话，会让身边的人担心吧？
[name="铃兰"]  可以哭一场的，不会有人说什么的啦。
[Character(name="char_358_lisa_1#3", name2="avg_npc_069",focus=2)]
[name="塔佳娜"]  嗯，谢谢，其实我也清楚，但是现在我还不能......不能松懈。
[Character(name="char_358_lisa_1#3", name2="avg_npc_069",focus=1)]
[name="铃兰"]  嗯——
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......别、别看着我，我知道啦，丽萨你就不用担心了。
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  嗯！
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  唉......那什么，抱歉！
[Character(name="avg_npc_069#4", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  欸？怎么突然......？
[Character(name="avg_npc_069#4", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......我在离开罗德岛本舰的时候已经做好心理准备了，安托她是个很认真的人，所以她向来守时。
[name="亚叶"]  我怎么会真的不清楚干员失联意味着什么，罗德岛经历过多少次这样的生死离别，我只是不愿意相信罢了。
[name="亚叶"]  呼......就是，那个，刚才太激动了，我很抱歉。
[name="亚叶"]  这场谋杀之中遭受损失的，不止是罗德岛。
[Character(name="avg_npc_069#2")]
[name="塔佳娜"]  ......八具遗体都被塞弗林长官带走了。
[name="塔佳娜"]  因为镇上没有感染者处理专家，所以我们只能草草埋葬他们......
[name="塔佳娜"]  他们不能跟着沃伦姆德一起前进，他们会被埋葬在城镇之外的废土上，等沃伦姆德离开这里，他们就永远失去了家乡。
[name="塔佳娜"]  本来......按照我们的传统......至少可以不用这样的......
[Character(name="avg_npc_069#2", name2="char_358_lisa_1#3",focus=2)]
[name="铃兰"]  这种事情......很常见。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  八具遗体？
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  八具遗体，除了刚才说的五个人，此外的应该是来这里接受治疗的游荡者......
[name="塔佳娜"]  大裂谷崩裂时，沃伦姆德并没能全身而退，当然也有很多周边的商人、旅行者被卷入了天灾。
[name="塔佳娜"]  尽管在那之后，沃伦姆德的处境越发糟糕，但除了追逐着这座仍旧勉强前进在废土上的城镇之外，他们也没有别的办法。
[name="塔佳娜"]  这期间，难民们的队伍也在变化......不过安托医生一视同仁，她也会负责救助一些愿意被救助的感染者。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  所以，一位非感染者，七位感染者......
[name="亚叶"]  感染者的遗体呢？在生命体征停止的数分钟到数小时内，视体内源石融合率，可能会出现二次扩散，如果不进行专门处理的话很危险。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  啊，那个，塞弗林长官判断因为感染程度较轻，而且高温迅速摧毁了身体组织，所以不存在太大风险......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......不是说没有专业人士吗？
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  诶，塞弗林长官说自己只是按照经验判断，他也没十足的把握......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  经验......什么样的工作才会有处理感染者尸体的经验......
[name="亚叶"]  不过，也是，如果失去了亲生骨肉还能保持冷静，也许他并没有表面上那么轻浮。
[name="亚叶"]  我想回去检查一下各位感染者的遗体......我想见安托一眼。
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=1)]
[name="塔佳娜"]  当然可以，我会向长官解释的，不过大部分遗体炭化严重，我们分辨不出来.......
[Character(name="avg_npc_069#2", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  没关系——
[Character(name="char_358_lisa_1#4")]
[name="铃兰"]  啊——！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="ac11_3",x=0, y=0, xScale=0.9, yScale=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="亚叶"]  丽萨？
[name="铃兰"]  这个牌子......
[name="亚叶"]  啊......安托的工作牌，竟然没有烧毁......
[name="亚叶"]  ......对了。
[name="亚叶"]  她工作的时候，总是会抱怨工作牌碍事。很奇怪吧？明明大家都会挂在胸前，也不知道哪里碍事了......
[name="亚叶"]  我们走吧，我想见她......我想见见她。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=1, block=true)]
[Image]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraShake(duration=2, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista", volume=0.1)]
[delay(time=1)]
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  轰鸣——？
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Character(name="avg_npc_069#4")]
[name="塔

... (全文6631字符)
```

### level_act11d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 3下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.3, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  这里能看见议事厅塔楼！谢天谢地，那里好像平安无事——！
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  丽萨，动作快！
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  嗯！
[Dialog]
[Character]
[name="镇民"]  怎、怎么了？哪里着火了？
[name="镇民"]  我的儿子们还没回来，有谁看到他们了吗——！
[name="镇民"]  宪兵呢，塞弗林呢！？他不是英雄吗，这种时候怎么不在！？
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  街道已经一团乱了！
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  但居民区根本没有遭到攻击，应当有人引导他们！
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  所有人的神经都已经绷紧太久了，出现爆炸，理所当然会引起骚动——
[name="塔佳娜"]  这边！我们得保证议事厅不被攻陷！
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  看见了！人数很多！快点！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.25, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.25, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_067")]
[name="武装的感染者"]  呃！？
[name="武装的感染者"]  你这个老东西，身手还不错，不用忍受矿石病折磨的感觉挺好的吧？
[Dialog]
[Character]
[Character(name="avg_npc_066#5",fadetime=1,block=true)]
[delay(time=1)]
[name="塞弗林"]  嗯......如果我早点戒烟的话，你们这会儿已经在监狱里学唱儿歌了。
[name="塞弗林"]  离开这里，念在你们也曾是城镇一员的份上，我不会——
[Character(name="avg_npc_067")]
[name="武装的感染者"]  哈，还敢嘴硬！沃伦姆德现在只有你一个正规军人，你以为我们不知道吗？
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  你们......
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  塞弗林！你的装腔作势结束了，让出议事厅，从现在开始，由我们来掌握这座城镇——
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  那你们打算做什么？
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  哈！？
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  别那么警惕，休战，让我抽根烟缓缓......告诉我，你们打算做什么？怎么做？
[name="塞弗林"]  说不定沃伦姆德可以考虑你们的诉求。
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  ......你在说什么？
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  看，我把武器放下了，我并不觉得我们有什么不可调和的矛盾，你们为什么要这么做？
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  ......哈。现在轮到你们讲大道理了？
[name="武装的感染者"]  我要你们交出凶手，我要你们抛弃成见。
[name="武装的感染者"]  ......我要回家，我要工作，简单吗？
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  ......只要你填好报告，注意定期体检，很简单。
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  现在呢！？我们只是被关起来等死！
[name="武装的感染者"]  那条街道只剩下地震留下的裂缝，都是随时会爆炸的源石丛，非感染者撤离了街道，物资一天比一天贫乏，有人帮我们吗？
[name="武装的感染者"]  哦，差点忘了，因为你们的无能，整座沃伦姆德都在驶向死亡，我们只是率先被抛弃的那一批人而已。
[name="武装的感染者"]  为了所谓的秩序而隐瞒真相，你还自以为很高明吗？
[Character(name="avg_npc_066#5", name2="avg_npc_067")]
[name="塞弗林"]  ......唉。
[name="塞弗林"]  火柴好像受潮了，既然点不着，就继续吧。
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadetime=0.4, block=true)]
[PlaySound(key="$fightgeneral")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral")] 
[Blocker(a=0, fadetime=1.5, block=false)]
[delay(time=0.6)]
[Character(name="avg_npc_066", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  呃——！？赤手空拳——？
[Character(name="avg_npc_066", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  嗯，哪怕只闻到点烟草味，我也能有点力气。
[Dialog]
[Character(name="avg_npc_066", name2="avg_npc_067",focus=2)]
[PlaySound(key="$fightgeneral", volume=0.2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[delay(time=1)]
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=1)]
[name="塞弗林"]  不过，抱歉，可能要“发生点意外”了。
[Character(name="avg_npc_066#5", name2="avg_npc_067",focus=2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=false)]
[name="武装的感染者"]  该死、放手！你要——你要杀了我吗——呃！
[Character(name="avg_npc_066#5")]
[name="塞弗林"]  不，只是“失手”——
[Dialog]
[Character(name="avg_npc_067")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[PlaySound(key="$fightgeneral", volume=0.2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=

... (全文11734字符)
```

### level_act11d0_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 4上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_367_swllow_1#4",fadetime=1,block=true)]
[delay(time=1)]
[name="灰喉"]  ......怎么会......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="ac11_4",x=0, y=0, xScale=0.9, yScale=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="卡达"]  ......这真是......惨不忍睹......
[name="断崖"]  火灾，现场已经处理过了，时间也过了很久。但是......
[name="断崖"]  这里，罗德岛的物资箱，编号，日期，一应俱全......
[name="卡达"]  这里的灰尘很规则，曾经有个某个方形的物体放在箱子上吧？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[Background(image="bg_ltruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_367_swllow_1#3")]
[name="灰喉"]  ......也许是安托的工作牌，她不喜欢挂在身上。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  卡达干员，断崖干员，现在情况有变。
[Character(name="char_328_cammou")]
[name="卡达"]  这、这我也明白的啦！
[name="卡达"]  既然灰喉姐和艾尔斯把我从山上救下来了，我一定会好好帮忙的！
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  不要叫我艾尔斯......唉，莱恩哈特到底和你们说了些什么......
[name="断崖"]  天灾造成的后果很严重，沃伦姆德现在不会好过，那里的天灾信使在做什么？
[name="断崖"]  如果是莱恩哈特或者地灵小姐在的话，至少情况不会这么糟糕......
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=1)]
[name="灰喉"]  假设是无意义的......我们应该做好最坏的打算。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  驻扎在城镇外，你们俩会有困难吗？
[Character(name="char_328_cammou")]
[name="卡达"]  完全没有！
[Character(name="char_294_ayer")]
[name="断崖"]  ......我毕竟是天灾信使的专职护卫，而这一位干员是为了拍摄视频素材深入冬灵山脉然后迅速遇难的“天才儿童”。
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=false)]
[Character(name="char_294_ayer", name2="char_328_cammou",focus=2)]
[name="卡达"]  都这个时候了你也要损我的吗！？
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  只是开开玩笑，不然......灰喉不会希望我们现在就冲进镇上砸开议事厅的大门，对吧？
[Character(name="char_367_swllow_1")]
[name="灰喉"]  ......抱歉，忍耐一下，我去确认一下安托的情况。
[name="灰喉"]  去去就回。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......饥荒？
[Character(name="avg_npc_066")]
[name="塞弗林"]  饥荒。饥荒会毁了所有人。
[name="塞弗林"]  我知道你想问什么，沃伦姆德这样规模的城镇，当然有自给自足的能力——
[name="塞弗林"]  前提是大裂谷出现的那天，没有那么多源石从地下刺穿构造区，割裂地块，炸毁农田和供给设施。
[Character(name="avg_npc_068")]
[name="镇民代表"]  事实上，没有在商业区和城镇中心发生爆炸，已经是万幸了，但即使如此我们依旧损失惨重......
[Character(name="avg_npc_066")]
[name="塞弗林"]  季节也很糟糕，已经入秋，我们的航线正在向冬灵山脉进发，今年的冬天会来得很早。
[Character(name="avg_npc_068")]
[name="镇民代表"]  我们没有把这一事实告诉所有人，是不希望引发不必要的恐慌。
[Character(name="avg_npc_066")]
[name="塞弗林"]  然后，我们被不知情的自己人捅了刀子。
[Character(name="avg_npc_068",name2="avg_npc_066",focus=1)]
[name="镇民代表"]  那些叛徒......怎么办？
[Character(name="avg_npc_068",name2="avg_npc_066",focus=2)]
[name="塞弗林"]  塔佳娜带着年轻人去排查了，如果没有人带路，没人能够碰到动力炉。
[name="塞弗林"]  各个街道应该有自己的备用拖拉设备，情况如何？
[Character(name="avg_npc_068",name2="avg_npc_066",focus=1)]
[name="镇民代表"]  ......这样行进速度太慢了，顶多只有其他城镇的八分之一，我们无法在冬天之前离开山脉。
[Character(name="avg_npc_068",name2="avg_npc_066",focus=2)]
[name="塞弗林"]  粮仓不能出任何问题，加派人手。
[Character(name="avg_npc_068",name2="avg_npc_066",focus=1)]
[name="镇民代表"]  人手......哪怕是老人和孩子，只要还愿意拿起武器的，都已经......
[name="镇民代表"]  对粮仓出手，等同于杀死沃伦姆德所有的人！他们，他们再怎么也不至于......
[Character(name="avg_npc_068",name2="avg_npc_066",focus=2)]
[name="塞弗林"]  别把他们想得太好。
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  那个......
[Character(name="avg_npc_066", name2="char_358_lisa_1#3",focus=1)]
[name="塞弗林"]  ——请说。
[Character(name="avg_npc_066", name2="char_358_lisa_1#3",focus=2)]
[name="铃兰"]  十二音街道，也就是隔离区，之所以那么萧条，也是因为......？
[Character(name="avg_npc_066", name2="char_358_lisa_1#3",focus=1)]
[name="塞弗林"]  ......如果我说，单纯是因为感染者的人数问题导致配给缩水，你们信吗？
[name="塞弗林"]  不，你们信不信根本不重要，他们信吗？
[name="塞弗林"]  他们要拆掉仓库的门，仔细检查每一颗谷穗，才会相信我们说的话。
[name="塞弗林"]  那么，难道我们就要让他们拆吗？
[Character(name="avg_npc_066", name2="char_358_lisa_1#3",focus=2)]
[name="铃兰"]  ......
[Character(name="avg_npc_066", name2="char_358_lisa_1#3",focus=1)]
[name="塞弗林"]  如果真的只是检查检查，我倒也乐意开诚布公，但不是每个人都打算看看就算了的。
[name="塞弗林"]  即使官方没有公告，聪明人也能从路线和时令推算出沃伦姆德将在冬天遭遇的大饥荒。
[name="塞弗林"]  他们煽动，他们掠夺，今天的所作所为，只是为了部分人自己活下去，而让另一部分人饿死，说白了，就是在找借口抢劫。
[name="塞弗林"]  罗德岛是感染者问题对策专家，我当然信，安托医生的专业和你们的战斗足以说明一切。
[name="塞弗林"]  但是——
[name="塞弗林"]  ——这片大地上的难题，就只有矿石病而已吗？
[Character(name="char_345_folnic_1#3", name2="avg_npc_066",focus=1)]
[name="亚叶"]  ......
[name="亚叶"]  ......即使在这个场合，我也必须为安托发问。
[name="亚叶"]  那是一场谋杀。
[Character(name="avg_npc_068")]
[CameraShake(duration=0.3, xstrength=10, ystrength=5, vibrato=20, randomness=30, fadeout=false)]
[name="镇民代表"]  ——无关人士都出去！长官和罗德岛的二位有要事想谈！
[name="镇民代表"]  塞弗林。
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......我明白。
[Character(name="avg_npc_068")]
[name="镇民代表"]  那么，交给你了。
[Character]
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_345_folnic_1#3", name2="avg_npc_066",focus=1)]
[name="亚叶"]  ......看来，这不是个可以放在台面上进行的话题。
[Character(name="char_345_folnic_1#3", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  哪种有关谋杀的话题可以放在台面上进行？
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=1)]
[name="亚叶"]  你们的隐瞒会招致恶果——不那么正式的用词，我现在就看你们很不爽。
[name="亚叶"]  罗德岛干员安托在沃伦姆德卷入一起谋杀事件殉职，我需要得到一个答复。
[name="亚叶"]  ......还有，根据那位清醒过来的感染者居民的证词，他们也在寻找“凶手”。
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  也许凶手就在他们之中，常见的挑拨伎俩，贼喊捉贼。
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=1)]
[name="亚叶"]  ......也许吧。
[name="亚叶"]  但在我们讨论凶手之前，我想——
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ——打住，你没必要说出来。
[name="塞弗林"]  即使是我也有良心不安的时候，如果你提出请求，会让我感觉很难受。
[name="塞弗林"]  

... (全文11624字符)
```

### level_act11d0_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 4下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
妈妈？妈妈，你要去哪里？
去高地？满是鲜花的高地？
......害了爸爸的坏人就在那里？那妈妈会惩罚他吗？
那惩罚他能让爸爸回来吗？
......不能？
那......那我不要妈妈去了。
不去不行？可我不想妈妈回去乌萨斯......那里的面包太硬了，冬天很冷......
妈妈？
妈妈......
......
......
......妈妈再也没有回来。
我用妈妈留下的钱，继续在乌萨斯读书，生活。
一个人。
一个人等待了好几年。一个人生活了好几年。
直到凯尔希医生出现在我的面前，她说，她是研究所的所长，她来接我了。
那时凯尔希医生很疲惫，比现在还要疲惫，后来我才知道，她刚从某个遥远的地方回到这里，找到了我。
然后，我加入了罗德岛。
我问过凯尔希医生，妈妈去哪儿了。凯尔希医生没有说太多，她只告诉我，妈妈和爸爸一同，被埋葬在乌萨斯的深处。
她是我最尊敬的老师，最憧憬的领袖，她指导我，教育我，不仅在语言上，更靠着无数干员的所作所为感染着我。
但凯尔希医生她......她唯独没有回答我那个最简单的问题——
我该向什么复仇？
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$rungeneral", volume=0.6)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......小丽萨，你其实可以不用跟过来的。
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  我不放心。
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  这没什么......只是去那附近搜查一下，也许会有那支武装感染者队伍的痕迹。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  亚叶姐姐......你觉得他们会是元凶吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  不确定——出于理性，“不确定”是当然的回答，毕竟我们没有证据。
[name="亚叶"]  但考虑到城镇现在的情况，他们是最值得怀疑的对象，不是吗？
[name="亚叶"]  还有冬灵，塞弗林怎么也不肯多说，虽然不知道这意味着什么......但既然串通感染者队伍，那就是一路货色。
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  这附近的山脉叫做冬灵山脉，常年被冰雪覆盖的荒芜山脉......有什么联系吗？
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......我不知道这些，我只知道，我要揪出凶手，然后从他那里得到一个答案。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  亚叶姐姐，你从昨天开始就一直......很吓人。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  丽萨......对不起。
[name="亚叶"]  .......不是每个人都能那么简单释然的。
[name="亚叶"]  这种不辞而别已经是第二次了......至少这次，我不愿意再后悔了。
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_011#2")]
[name="泥岩"]  ......唔。
[name="泥岩"]  出来吧，我没有敌意。
[PlaySound(key="$leaveshake", volume=0.6)]
[Dialog]
[Character]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="char_328_cammou",fadetime=1,block=true)]
[delay(time=1)]
[name="卡达"]  我还觉得自己潜伏的技术很不错......你是怎么发现我们的？
[Character(name="avg_npc_011#2")]
[name="泥岩"]  嗯......直觉？大概吧......
[name="泥岩"]  你们，是谁？
[Character(name="char_294_ayer", name2="char_328_cammou",focus=2)]
[name="卡达"]  （呜啊，总感觉这家伙很难对付啊。）
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  （那你就少说两句。）
[Character(name="char_294_ayer")]
[name="断崖"]  我翻阅过罗德岛的一些战斗记录，你不是普通的感染者。
[Character(name="avg_npc_011#2")]
[name="泥岩"]  ......罗德岛？是这样，你们是......罗德岛的干员。
[Character(name="char_294_ayer", name2="char_328_cammou",focus=2)]
[name="卡达"]  怎么办？要动手吗？
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  现在灰喉不在......但至少我们得拖住他的脚步！
[Dialog]
[Character]
[Character(name="avg_npc_011#2")]
[playsound(key="$smallearthquake", volume=0.2)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[delay(time=2)]
[Character(name="char_328_cammou")]
[name="卡达"]  ——！
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  ——别紧张，别攻击他！卡达！
[name="断崖"]  不要轻举妄动！
[Character(name="char_294_ayer", name2="char_328_cammou",focus=2)]
[name="卡达"]  呃——！抱、抱歉！
[Character(name="avg_npc_011#2")]
[name="泥岩"]  唔......？一瞬间，你的瞳孔变得鲜红，这是某种应激反应吗？
[name="泥岩"]  ......是我吓到你了吗？抱歉，我只是想让你们知道......战斗是徒劳的。
[name="泥岩"]  如果你们是沃伦姆德的居民......你们最好离开这里，很危险。愤怒的冬灵人或是感染者遇到你们......你们凶多吉少。
[Character(name="char_294_ayer")]
[name="断崖"]  ......多谢忠告。
[name="断崖"]  那么你为什么出现在这里？
[Character(name="avg_npc_011#2")]
[name="泥岩"]  我只是来献一束花，之后我自会离开。
[Character(name="char_294_ayer")]
[name="断崖"]  ......你手里捧着的，只是普通的野花？
[Character(name="avg_npc_011#2")]
[name="泥岩"]  这里的秋天很冷，我时常做梦的......梦见这些花，这些花就像是那座雪山的孩子......冰凉凉的。
[name="泥岩"]  ......愿逝者安息。
[Character(name="char_294_ayer", name2="char_328_cammou",focus=2)]
[name="卡达"]  （他真的只是来祈祷的？该不会是假装献花其实在释放什么源石技艺吧？）
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  （看不清他的表情就判断不出他是不是在说谎，但是......）
[name="断崖"]  （......他好像真的很伤心。）
[Character(name="avg_npc_011#2")]
[name="泥岩"]  ——？
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_367_swllow_1#4",fadetime=1,block=true)]
[delay(time=1)]
[name="灰喉"]  不许动，不要转身，举起手。
[Character(name="char_328_cammou")]
[name="卡达"]  灰喉姐！
[Character(name="avg_npc_011#2")]
[name="泥岩"]  ......什么时候出现的，竟然这么轻巧......
[name="泥岩"]  算了吧，罗德岛的弩手，你的弩箭奈何不了我。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  不要动，我只是有话想问问——
[Character(name="avg_npc_011#2")]
[name="泥岩"]  不展露力量的对话......毫无意义。
[Character(name="char_367_swllow_1#4")]
[name="灰喉"]  ——顽冥不化！
[Dialog]
[Character(name="char_367_swllow_1#4")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=0.5)]
[Character(name="avg_npc_011#2")]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[delay(time=1)]
[name="泥岩"]  看，我捏住了你的箭......你伤不到我分毫。
[Character(name="char_294_ayer", name2="char_328_cammou",focus=1)]
[name="断崖"]  他举起了一块岩石挡住了弩箭！？
[Character(name="char_294_ayer", name2="char_328_cammou",focus=2)]
[name="卡达"]  不、不对！是源石技艺！他确实“捏住了”箭矢，用泥土！
[Characte

... (全文14756字符)
```

### level_act11d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 5上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  ......歌声？
[name="亚叶"]  怎么......
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  啊，整个街道都回荡着歌声......
[Dialog]
[Character]
淡蓝的暮色洒在萧条的街道上，零零星星的灯火之间，有人生活。
二人目光所及的街道上空无一人，朦胧的歌声织成了一张网，夕阳西下。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1, block=true)]
裸露的源石丛，躁动的抗议者，苍白的星空和泥砖一同陷入沉寂。
歌声......只剩下歌声......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_345_folnic_1#4",fadetime=1,block=true)]
[delay(time=1)]
[name="亚叶"]  怎么回事......我看见了什么？这是......源石技艺？
[name="亚叶"]  这是......民谣？还是诗歌？在日落的时候？
[name="亚叶"]  沃伦姆德有这样的习俗吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  呃......亚叶姐姐，你听得懂歌词吗？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  不......但这是莱塔尼亚语吗？现代的莱塔尼亚语可没有这么晦涩的发音......
[Character(name="char_358_lisa_1", name2="char_345_folnic_1#4",focus=1)]
[name="铃兰"]  ......但是，很好听。
[name="铃兰"]  像是第一次在罗德岛舰桥上眺望大地那样，悠扬......古老......
[name="铃兰"]  这是......这的确是法术......和东国的某些古老技艺一样！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[stopmusic(fadetime=3)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_066",fadetime=1,block=true)]
[delay(time=1)]
[name="塞弗林"]  把人找出来。
[Character(name="avg_npc_068")]
[name="镇民"]  明白，但是找出来之后呢？直接逮捕吗？
[Character(name="avg_npc_066")]
[name="塞弗林"]  嗯。
[Character(name="avg_npc_068")]
[name="镇民"]  会被别有用心的人当做煽动的借口。
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......是为了防止他们挑拨感染者与非感染者的关系，始作俑者说不定就是冬灵人。
[Character(name="char_358_lisa_1#3", name2="avg_npc_066",focus=1)]
[name="铃兰"]  塞弗林长官！？这、这是要做什么？
[Character(name="char_358_lisa_1#3", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......这是冬灵的歌谣，只在古老的祭典和葬礼上出现。
[name="塞弗林"]  冬灵人是挑拨感染者和非感染者矛盾，带领那些危险分子破坏城镇动力设施的罪魁祸首。
[name="塞弗林"]  现在不是谈宽容的时候，我认为这是某种信号。
[name="塞弗林"]  他们不会无端暴露自己，肯定有其他人在暗中行动，而且多半都是术师，留个心眼。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ——冬灵人到底指什么？
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  本地的卡普里尼，在几百年前，他们才是这片群山的住民。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  然后呢？
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  ......然后是沃伦姆德和冬灵人的冲突，就这样。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  不。不止如此。
[name="亚叶"]  只是单纯的殖民问题的话，哥伦比亚，雷姆必拓，哪个国家都有过这样的历史。
[name="亚叶"]  能让你们想方设法避开话题的话，会这么简单吗？只是矛盾和冲突？
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  ......我不知道我该不该告诉你们，这的确超过了罗德岛有必要知道的范畴......
[name="塞弗林"]  由一位宪兵把这些事情冠冕堂皇地告诉一家境外企业，这会让某些贵族十分地不高兴。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  贵族......？不高兴？？
[Character(name="avg_npc_066", name2="char_345_folnic_1#5",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=40, fadeout=false)]
[name="亚叶"]  ——安托为了帮你们牺牲了！现在还是讲面子的时候吗！？
[Character(name="char_358_lisa_1#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=false)]
[name="铃兰"]  亚、亚叶姐姐！牺牲......不该变成我们争吵的借口。
[name="铃兰"]  塞弗林长官......！可以先停下这场搜捕吗？这会让大家的情绪更糟，会让事情无法挽回的！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ——
[name="亚叶"]  ......不，唯一的线索近在眼前，我们不能放过。
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  诶......？
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  塞弗林，莱塔尼亚那么多的移动城邦，那些身居高塔之巅的贵族，有谁管过你们的死活？
[name="亚叶"]  就算大裂谷出现，倘若最近的移动城邦倾力支援，当真会出现饥荒这种事情？
[name="亚叶"]  塞弗林，看清楚是谁在帮助你们！
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  我知道......亚叶小姐，我比谁都清楚。
[name="塞弗林"]  但我也清楚，罗德岛帮不了我们一辈子。等到事件解决，沃伦姆德重回它应有的位置时，我不希望收到来自某座高塔的信件。
[name="塞弗林"]  ......请理解。
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  但是亚叶姐姐，我们——
[stopmusic(fadetime=2)]
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Character(name="char_358_lisa_1#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[name="铃兰"]  ——爆炸！？又是袭击？
[Character(name="avg_npc_065")]
[name="镇民"]  长官、长官！救救我们！我们需要帮助！
[Character(name="avg_npc_066")]
[name="塞弗林"]  慢点，怎么了？
[Character(name="avg_npc_065")]
[name="镇民"]  他们、他们激活了那些城防装置！爆炸，火焰，他们——！
[Character(name="avg_npc_066")]
[name="塞弗林"]  冷静点！
[PlaySound(key="$rungeneral", volume=0.6)]
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  长官！感染者们、感染者们抓住了所有在十二音街道巡逻的宪兵！我们失去联络了！
[name="塔佳娜"]  他们利用那些留声机负隅顽抗，现在整个街道已经失去控制——！
[Character(name="avg_npc_069#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  .......他们不该这么井井有条，谁在指挥？
[Character(name="avg_npc_069#4", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  还不清楚——但是很多非感染者也加入了抗议的队伍！沃伦姆德已经被......分割成两半了！
[Character(name="avg_npc_069#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  呿，

... (全文9238字符)
```

### level_act11d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 5下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  快！这边走！
[Character(name="avg_npc_065")]
[name="镇民"]  谢谢、谢谢！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  亚叶姐姐！
[Character(name="char_358_lisa_1#4", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  丽萨！你带着平民先走！
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="char_345_folnic_1#5")]
[CameraShake(duration=0.6, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=false)]
[name="亚叶"]  呃——！
[name="亚叶"]  这群暴徒......他们在无差别攻击街道？
[Character(name="avg_npc_067", name2="avg_npc_067",focus=1)]
[name="武装的感染者A"]  喂！我们好不容易才抢下这玩意，你倒是射准一点啊！
[Character(name="avg_npc_067", name2="avg_npc_067",focus=2)]
[name="武装的感染者B"]  闭嘴！要操纵这玩意儿哪有那么简单！得亏我以前在音乐学院学习过——！
[Character(name="avg_npc_067", name2="avg_npc_067",focus=1)]
[name="武装的感染者A"]  哪门子学院！？喂，宪兵！不要轻举妄动，我们有人质的！
[Character(name="avg_npc_067", name2="avg_npc_067",focus=2)]
[name="武装的感染者B"]  人质在哪儿呢？
[Character(name="avg_npc_067", name2="avg_npc_067",focus=1)]
[name="武装的感染者A"]  *莱塔尼亚粗口*！街上在跑的不都是吗！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  啧！
[Character(name="avg_npc_069#3", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  亚叶小姐！不能让他们继续破坏下去了！
[name="塔佳娜"]  这附近的房屋都是木质结构，这样下去整片街道都会化为火海——！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[name="镇民"]  火！快灭火！其他人赶紧离开这里！
[Character(name="avg_npc_069#3", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  还有很多来不及撤离的平民，我们得帮他们！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  但这不是完全没法靠近吗——！
[Character(name="avg_npc_069#3", name2="char_345_folnic_1#3",focus=1)]
[name="塔佳娜"]  ——呃，这火力！
[name="塔佳娜"]  亚叶小姐！麻烦你照顾伤员！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=false)]
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  喂！？
[Character(name="avg_npc_068")]
[name="顽固的镇民"]  你们这些冬灵人！感染者！蛀虫！
[name="顽固的镇民"]  为什么要烧了我的家！为什么！明明是我们养着你们的——！
[Character(name="avg_npc_069#3")]
[PlaySound(key="$rungeneral", volume=0.6)]
[name="塔佳娜"]  小心头顶！
[Character(name="avg_npc_068")]
[name="顽固的镇民"]  呃？
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=2)]
[Character(name="avg_npc_068")]
[name="顽固的镇民"]  唔......呃，塔佳娜？你、你还好吗！？
[Dialog]
[Character]
[Character(name="avg_npc_069#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="塔佳娜"]  呜......我还好，他们控制不住那些自律施术单元，这里很危险！
[Character(name="avg_npc_068")]
[name="顽固的镇民"]  我们一起反抗！把他们赶出去！
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  现在——还不是时候——！呃——！
[Character(name="avg_npc_068")]
[name="顽固的镇民"]  你的脚——！好、好吧，我听你的！
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  离开这里！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_069#2")]
[name="塔佳娜"]  （脚踝的刺痛......是骨折了吗？真糟糕......）
[name="塔佳娜"]  （得快点和其他人汇合......）
[Character(name="avg_npc_067")]
[name="武装的感染者"]  你这，贵族的爪牙！
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  ——！？
[Dialog]
[Character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_066#5")]
[name="塞弗林"]  ......全部撤离了吗？
[Character(name="avg_npc_065")]
[name="镇民"]  是、是的！
[Dialog]
[Character]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Character(name="char_358_lisa_1#3",fadetime=1,block=true)]
[delay(time=1)]
[name="铃兰"]  塞弗林长官，受伤的人很多，这里人手不够......！
[Character(name="avg_npc_066")]
[name="塞弗林"]  医生们，听这位沃尔珀小姐的话，没受伤的年轻人也都去帮忙。
[Character(name="avg_npc_065")]
[name="镇民"]  知道了！
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  如果亚叶姐姐在的话......！
[Character(name="char_358_lisa_1#3", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  等等......她们没有回来？
[Character(name="avg_npc_066")]
[name="塞弗林"]  喂！亚叶和塔佳娜呢？
[Character(name="avg_npc_068")]
[name="镇民"]  她们、她们好像还在十二音街道......
[Character(name="avg_npc_066")]
[name="塞弗林"]  ——我刚才问的不是“全部撤离”吗！？
[Character(name="avg_npc_068")]
[name="镇民"]  噫！对、对不起！但是，亚叶和塔佳娜应该不会有事的，他们救下了那么多人！
[Character(name="avg_npc_066")]
[name="塞弗林"]  叛乱者抢占了城防设施，没有正规武装力量的她们怎么才能没事——咳咳，咳咳！
[name="塞弗林"]  ——咳，找几个身强力壮的，和我去。
[Character(name="avg_npc_068")]
[name="镇民"]  但是他们有火力优势，说不定已经有了人质，我们不应该再去刺激他们了，我们应该等着谈判的机会！
[Character(name="avg_npc_066")]
[name="塞弗林"]  机会！等着敌人给我们机会！你上过战场吗！？
[Character(name="avg_npc_068")]
[name="镇民"]  对、对不起！
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_367_swllow_1#2",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  但他的担忧不无道理。大裂谷留下的活性源石极有可能残留在沃伦姆德的地基内，任由他们破坏，后果不堪设想。
[Character(name="avg_npc_068")]
[name="镇民"]  你们从哪里进来的！无关人士赶紧离开这里！
[Character(name="avg_npc_066#3")]
[name="塞弗林"]  ......不。
[name="塞弗林"]  没有宪兵队的我们倒更像无关人士......我见过你一面，罗德岛的干员。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  感谢理解

... (全文8929字符)
```

### level_act11d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 6上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="塔佳娜"]  唔......
[name="塔佳娜"]  这里是......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_069#2",fadetime=1,block=true)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="塔佳娜"]  唔——！
[name="塔佳娜"]  （头好晕......！视野......听力......还算正常。）
[name="塔佳娜"]  （脚踝......失去知觉了。）
[name="塔佳娜"]  （......好安静，其他人都离开了吗？）
[name="塔佳娜"]  （......）
[name="塔佳娜"]  （真的好安静......等等，敌人就这么把我放在这儿了？）
[Character(name="char_367_swllow_1#3")]
[name="灰喉"]  ......你醒了。
[Character(name="avg_npc_069#4")]
[CameraShake(duration=0.3, xstrength=8, ystrength=6, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="塔佳娜"]  咿呀——！？
[Character(name="char_367_swllow_1", name2="avg_npc_069#4",focus=1)]
[name="灰喉"]  ......别这么紧张。
[Character(name="char_367_swllow_1", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  啊、抱歉！突然被吓了一跳——
[name="塔佳娜"]  欸？您、您是？我记得，您也是罗德岛的——
[Character(name="char_367_swllow_1", name2="avg_npc_069#4",focus=1)]
[name="灰喉"]  干员，灰喉。
[name="灰喉"]  小声点，这附近的叛乱者都被解决掉了。
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  解决......
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=1)]
[name="灰喉"]  ......即使到了这个时候，你还是不希望把他们视作敌人。
[name="灰喉"]  放心吧，基本都性命无忧，已经交给塞弗林·霍索恩长官了。
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  ......谢谢。
[name="塔佳娜"]  啊——亚叶小姐她——
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=1)]
[name="灰喉"]  她没事，其他干员去帮她了，只是......
[name="灰喉"]  安托她真的......牺牲了吗？
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  ......嗯，很抱歉。
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=1)]
[name="灰喉"]  所以亚叶才会是那副模样......
[Character(name="char_367_swllow_1", name2="avg_npc_069#3",focus=2)]
[name="塔佳娜"]  只靠几名干员不可能收复这片街区，我们应该先撤回城镇中心，重整旗鼓。
[Character(name="char_367_swllow_1", name2="avg_npc_069#3",focus=1)]
[name="灰喉"]  嗯，你能走吗？你的脚踝受伤了。
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  啊......我试试看，疼......
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=1)]
[name="灰喉"]  来，手给我。
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  谢谢......
[Character(name="char_367_swllow_1", name2="avg_npc_069#2",focus=1)]
[stopmusic(fadetime=2)]
[name="灰喉"]  ——还有一个问题，塔佳娜小姐。我陪着安托抵达这里的时候，沃伦姆德还是一片繁荣。
[name="灰喉"]  但为什么现在，沃伦姆德连一个正规宪兵都没有？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$plot_intro", key="$plot_loop", volume=0.4)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  唔！
[Character(name="char_294_ayer")]
[name="断崖"]  放下武器，看看你自己，连套像样的装备都没有，就这样也打算战斗？
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  你们这些外来者，到底懂什么！帮那些贵族爪牙，你们到底有什么好处！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......没有好处，我也对你们的政治不感兴趣，但是......你是冬灵人吗？
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  冬灵人——？哈，我才不是那种土著，但我的确认可他们的抗争！
[name="叛乱的镇民"]  看看你们呢？安托医生是个好家伙，但你们呢？你们只是在帮他们落井下石！
[name="叛乱的镇民"]  沃伦姆德——不，整个莱塔尼亚都是腐朽的！他们今天敢放火害死感染者，明天就会放火烧死所有的穷人！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......
[Character(name="char_294_ayer")]
[name="断崖"]  证据呢？
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  ——沃伦姆德一个宪兵都没有！一个！都没有！
[name="叛乱的镇民"]  你知道为什么吗？
[Character(name="char_294_ayer")]
[name="断崖"]  沃伦姆德和周遭的多个城镇组成了聚落，天灾来临，宪兵数量并不足以照顾到所有的——
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  我呸！要真是这么正常的理由，谁会不满！？
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ——别想拖延时间，说，还是不说？
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  ——哼。
[name="叛乱的镇民"]  因为一场婚礼。
[Character(name="char_294_ayer")]
[name="断崖"]  ......婚礼？
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  因为某个身居高塔之上的大贵族迎娶了另一位贵族的独女，所有的宪兵都被调往了最近的移动城邦！
[name="叛乱的镇民"]  贵族的酒池肉林持续了多久？你猜猜看？
[Character(name="char_294_ayer")]
[name="断崖"]  ......
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  哦，对了，贵族们还争吵着哪一方才该开动移动城市去另一方的领土做客，争执了一个月之久——
[name="叛乱的镇民"]  我们的宪兵队就那么被扣押在贵族的宅邸周围，为了排面和名义上的安保，滑稽吗？可笑吗？
[name="叛乱的镇民"]  ——一点都不可笑。
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  的确一点都不可笑，但我依旧没有听见关于火灾的线索。
[Character(name="avg_npc_067")]
[name="叛乱的镇民"]  哼......
[name="叛乱的镇民"]  ......你觉得，谁会放火烧掉一座医治感染者的医疗营地？感染者自己吗？
[name="叛乱的镇民"]  只有那些见不得感染者的人才会做这种事，你应该信任的人是我们——
[name="叛乱的镇民"]  ——信任“整合运动”！
[stopmusic(fadetime=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Character(name="avg_npc_068")]
[name="镇民"]  长官！叛徒们不愿意投降——！
[Cha

... (全文12383字符)
```

### level_act11d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 6下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_011#2",fadetime=1,block=true)]
[delay(time=1)]
[name="泥岩"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  我们就这么白白被他们利用？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  ......如果他们真的借了“整合运动”这个名号，会怎么样？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......他们一定会这么宣称。
[name="泥岩"]  我们一定会被追捕。
[name="泥岩"]  只是这种规模的城镇，奈何不了我们，可......可如果是一整座移动城邦呢？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  莱塔尼亚诸城高塔耸立，睥睨大地的那些大银行家大音乐家大贵族们，随便拎一个出来就够我们喝一壶。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  傲慢会毁了他们。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  也正是傲慢，才让莱塔尼亚那肮脏的侵略性得以遏制。
[name="萨卡兹战士"]  我们也许不该在沃伦姆德闹下去了，继续这样，我们可无路可走。
[Character(name="avg_npc_011#2")]
[name="泥岩"]  ——我们不应该在战场上相见。这里......这里不是战场，不该是。
[name="泥岩"]  你们的时间不多了。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  ——？你在和谁说话？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  不。
[name="泥岩"]  只是......感慨一下。
[name="泥岩"]  很快，冬天就会来了，我们别无选择。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="卡达"]  哎......这感觉好像不太妙呀......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_066",fadetime=1,block=true)]
[delay(time=1)]
[name="塞弗林"]  ——那么，还有什么问题吗？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  以防万一，我想请问塞弗林长官，八具遗体的身份......是如何确认的？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  体型，性别，大致年龄，以及镇内的失踪名单。
[name="塞弗林"]  ......但现在不是讨论那场火灾的时候，眼下有更紧急的问题。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  我不否认，但是......
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  ......有什么发现吗？
[Character(name="char_345_folnic_1#4", name2="char_367_swllow_1",focus=2)]
[name="灰喉"]  据我们接触的整合运动所说，他们在火灾中丧生的感染者人数是“四名”。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......我们有必要在意敌人的话吗？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  恕我直言，这完全有必要，“在意”和“信任”是两回事，双方存在误会的可能性很大。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  我依旧不觉得这能解决问题，我甚至觉得......就算揭开火灾的真相，也制止不了事情变得更坏。
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=1)]
[name="亚叶"]  对我们而言，有意义。
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......那也恕我直言，从中途开始，亚叶小姐，你的表现都显得有些过于主观了。
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=1)]
[name="亚叶"]  但你必须——
[Character(name="char_345_folnic_1#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  我只会为了沃伦姆德而战，这是我的职责，所以我对各位的正义心......并不感兴趣。
[name="塞弗林"]  我有必要为了真相而对罗德岛负责，并不因你的复仇欲负责。
[Character(name="char_345_folnic_1#3", name2="avg_npc_066",focus=1)]
[name="亚叶"]  你——
[Character(name="char_345_folnic_1#2")]
[name="亚叶"]  ——不，你说得对......
[name="亚叶"]  我去冷静一下......丽萨在照顾伤员，我......我去帮她。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_066")]
[name="塞弗林"]  那么我们已经得出结论了，无论如何，将以收复十二音街区为最优先。
[name="塞弗林"]  全面开战不可避免，罗德岛的各位将着力于自律施术单元的争夺，以及，监视那队有萨卡兹在其中的武装分子。
[name="塞弗林"]  ......正面控制暴徒的任务就交给我们，最困难的事，就交给你们了。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=1)]
[name="断崖"]  ......
[Character(name="char_294_ayer", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  呃，嗯......刚才话是不是说太重了？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  ......不，塞弗林长官。那座街道里的叛乱分子，门外的那些愤怒的镇民，你从他们眼里看到了什么？
[name="灰喉"]  如果连我们也被冲昏了头脑，这座城镇沃伦姆德就已经宣告灭亡了。
[name="灰喉"]  ......而且无论真相如何，“整合运动再度出现并摧毁了莱塔尼亚的一座城镇”，这种事情......
[name="灰喉"]  在那么多的牺牲和分别之后，我不想再看见一次。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  ......断崖，联络一下卡达，汇合时间已经到了。
[name="灰喉"]  我去看看那些感染者战俘的情况。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
[Character(name="avg_npc_069#4",fadetime=1,block=true)]
[delay(time=1)]
[name="塔佳娜"]  长官？我看到亚叶小姐已经离开了，会议结束了吗？
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=1)]
[name="塞弗林"]  嗯，辛苦。
[name="塞弗林"]  ......真大声啊，外面的家伙们。
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_068",name2="avg_npc_065")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="镇民"]  谁能忍受家园被破坏！
[name="镇民"]  他们毁了我的店，还打伤了我的孩子！
[name="镇民"]  那些该死的叛徒！忘恩负义！忘恩负义的叛徒！
[Dialog]
[Character]
[Character(name="avg_npc_065")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="镇民"]  我们要战斗！
[Character(name="avg_npc_068")]
[name="镇民"]  我们要战斗！我们要战斗！我们要战斗！
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
我们要战斗！我们要战斗！我们要战斗！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",

... (全文11488字符)
```

### level_act11d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 7上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_345_folnic_1#3",fadetime=1,block=true)]
[delay(time=1)]
[name="亚叶"]  塞弗林，我需要知道天灾信使毕德曼的所有资料。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  毕德曼......？为什么提起他？
[Character(name="char_358_lisa_1#4", name2="avg_npc_066",focus=1)]
[name="铃兰"]  有一位老爷爷说，他在暴乱中看到了负责指挥的毕德曼，是他们毁了动力炉。
[Character(name="char_358_lisa_1#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......老爷爷？可信度有多高？
[Character(name="char_358_lisa_1#4", name2="avg_npc_066",focus=1)]
[name="铃兰"]  他说，他是最后一个“冬灵人”......
[Character(name="char_358_lisa_1#4", name2="avg_npc_066#3",focus=2)]
[name="塞弗林"]  .......他，他还活着？不，很可能是冒牌货。
[Character(name="char_358_lisa_1#4", name2="avg_npc_066#3",focus=1)]
[name="铃兰"]  那样的人是不会撒谎的......尽管这只是我的直觉，但我认为，他是不会撒谎的。
[name="铃兰"]  这是他的日记，和他的刀。我想会是个信物，所以擅自......
[Character(name="char_358_lisa_1#4", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  但他明明......
[name="塞弗林"]  这真是出乎预料......我以为他和那些家伙都.......投湖自尽了。
[name="塞弗林"]  我会去见他，我......我不知道，我该不该去见他？
[Character(name="char_358_lisa_1#3", name2="avg_npc_066#2",focus=1)]
[name="铃兰"]  老爷爷和我说了很多，他说，冬灵人并不是真正的罪魁祸首。
[name="铃兰"]  老爷爷也没有在恨你。说那些事的时候，他很平静。
[Character(name="char_358_lisa_1#3", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  我不是不能理解......但是那些叛乱分子的确在用“冬灵”作为他们掠夺的借口。
[Character(name="char_358_lisa_1#3", name2="avg_npc_066#2",focus=1)]
[name="铃兰"]  那只是借口——
[Character(name="char_358_lisa_1#3", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  就算只是借口，他们也确实实施了暴行。下一步，他们将会要求我们开放粮仓，把一切席卷而空。
[name="塞弗林"]  何况冬灵的血脉早已与本地的沃伦姆德居民融合，事到如今......咳咳......
[name="塞弗林"]  无论借口是什么，我们都只是不信任对方把握自己的命脉而已。
[Character(name="avg_npc_066", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  一个本该死去的天灾信使，不仅活着，瞒着所有人，煽动了叛乱。
[name="亚叶"]  联系这一切来想，他是幕后黑手的可能性最大。
[Character(name="avg_npc_066", name2="char_345_folnic_1#4",focus=1)]
[name="塞弗林"]  ......对，这下就说得通了，如果毕德曼真的还活着，他的确是那个可以煽动叛乱的人，他也知道沃伦姆德处于饥荒边缘的事实。
[Character(name="avg_npc_066", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  动机呢？
[Character(name="avg_npc_066#2", name2="char_345_folnic_1#4",focus=1)]
[name="塞弗林"]  ......大裂谷。
[name="塞弗林"]  天灾发生之后，很多人都将城镇的损失怪罪于他。
[name="塞弗林"]  在那短短数个月间，我们至少制止了七次针对他的暴力事件......而更多的，我们甚至不知详情。
[name="塞弗林"]  在那之后，他几乎日日闭门不出，开始酗酒且有暴力倾向，直到......安托医生砸开了他家的门。
[Character(name="char_358_lisa_1#3", name2="avg_npc_066#2",focus=1)]
[name="铃兰"]  砸、砸开？
[Character(name="char_358_lisa_1#3", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  安托医生对处于低谷的毕德曼伸出了援手，那之后，毕德曼也时常去帮助安托医生的工作。
[Character(name="char_358_lisa_1#3", name2="avg_npc_066#2",focus=1)]
[name="铃兰"]  可听上去......他们的关系还不错？
[Character(name="char_358_lisa_1#3", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  至少表面如此，这也是我不曾怀疑过他的理由......毕德曼本来就是个很阴郁的家伙，就算陪着安托医生干活，我们也没见他笑过。
[name="塞弗林"]  虽然理智的镇民和我本人都对他的工作表示理解，但......这也足以成为他报复我们的借口了。
[name="塞弗林"]  情感上，他的报复动机毫无疑问是符合逻辑的，当然，这不说明任何事情。
[name="塞弗林"]  几乎每一个人，都有想法和理由去报复另一个人。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ......报复，又是报复。
[name="亚叶"]  而且......你也别说得这么事不关己。你确实说过，毕德曼死了。
[name="亚叶"]  你忽视了确认死者身份的工作，你忽视了这份可能性。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  但现在还不能就这么认定——咳咳——咳咳——
[Character(name="char_358_lisa_1#3", name2="avg_npc_066",focus=1)]
[name="铃兰"]  您没事——
[stopmusic(fadetime=3)]
[Character(name="avg_npc_066")]
[name="塞弗林"]  ——慢着，等等。
[name="塞弗林"]  为什么外面的那些呐喊声停下了？
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  长官！
[name="塔佳娜"]  镇民们擅自行动，他们、他们打算包围十二音街道！
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=1)]
[name="塞弗林"]  胡闹！去制止他们！
[name="塞弗林"]  我们不知道现在躲藏在十二音街道是哪些人，万一那些“整合运动”已经蛰伏进了那里怎么办？
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  但，但他们都很激动，根本听不进话——！
[name="塔佳娜"]  他们不知从哪儿得知了“整合运动”的事情......！
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=1)]
[name="塞弗林"]  嘁......一群光知道煽动的蠢货！
[stopmusic(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_011#2")]
[name="泥岩"]  城镇里的动静很大。
[name="泥岩"]  不仅如此......好像还有什么人找到这里来了。
[name="泥岩"]  既然都有组织民兵出城搜捕的决心......说明他们已经有了开战的打算。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  ......那些镇民找到了这里，他们打算烧死我们。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......烧死？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  他们连车夫都懂得简单的法术，源石技艺是他们的义务教育内容，放把火，不难的事。
[name="萨卡兹战士"]  ......这里要待不下去了，会是罗德岛的人带头吗？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......不会。
[name="泥岩"]  我倒觉得......只是这些愤怒的人，把我们当做罪魁祸首，把我们当做罪大恶极的感染者，来驱赶我们。
[name="泥岩"]  如此而已吧。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  ......泥岩。
[name="萨卡兹战士"]  别忘了，我们的同伴丧生在这座城镇中。
[name="萨卡兹战士"]  我们尊重你的选择，但你还年轻......你还不懂这其中的含义。
[name="萨卡兹战士"]  只是你要知道，我们的脾气也不是那么好的。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......一旦动手，我们就会遭到整座城邦的追捕。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  我们逃跑的话，就会被当作放火杀人，挑拨叛乱，抢劫城镇的元凶。一样的啊。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  按照正常的萨卡兹做派，很简单，我们只要毁了这座城镇就行，全部摧毁，这不难。
[name="萨卡兹战士"]  最麻烦的那些城防设备，自律施术单元，已经因为他们自己的内乱而停摆。
[name="萨卡兹战士"]  只要你下令，月亮将永远停留在冬灵山脉的荒野上，春天......不会来临。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......今年的冬天，会很长。
[Character(name="avg_npc_011#2

... (全文14506字符)
```

### level_act11d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 7下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[PlaySound(key="$rungeneral", volume=0.6)]
[Character(name="char_328_cammou")]
[name="卡达"]  快点，这里！
[Character(name="char_294_ayer")]
[name="断崖"]  这附近的痕迹......更像是单纯的发泄。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  ......塞弗林认为，这是一次有谋划，有规律的变节计划。但事实上呢？这的确就是一次单纯的暴力宣泄。
[Character(name="char_367_swllow_1", name2="char_328_cammou",focus=1)]
[name="灰喉"]  卡达，发现什么了？
[Character(name="char_367_swllow_1", name2="char_328_cammou",focus=2)]
[name="卡达"]  没错，但是、但是......
[name="卡达"]  灰喉姐你快过来吧，我......我也不知道该怎么说......
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1)]
[Character(name="char_367_swllow_1", name2="char_328_cammou",focus=1)]
[name="灰喉"]  ......怎么了？
[Character(name="char_367_swllow_1", name2="char_328_cammou",focus=2)]
[name="卡达"]  房间里......
[Character(name="char_367_swllow_1")]
[name="灰喉"]  你的瞳孔......别怕，控制住自己，断崖，在外面陪着她，警戒周围的暴徒。
[Character(name="char_294_ayer")]
[name="断崖"]  明白。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  ......在这里面？
[Dialog]
[Character]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="灰喉"]  （......一片狼藉，真是惨烈的混战......呃......这是......冻裂的肢体？）
[name="灰喉"]  （等等，这个人是——？）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Character(name="avg_npc_067")]
[name="武装的感染者"]  呃——！这个医生怎么！？
[name="武装的感染者"]  你要是坚持不让开，我连你一起杀！
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  ......刚才撒在你们身上的药剂，具有挥发毒性。
[Character(name="avg_npc_067")]
[name="武装的感染者"]  啊！？你、你对我们做了什么？
[name="武装的感染者"]  赶快说！不然我就让你——让你......让你.......呃......
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  难受吗？
[name="亚叶"]  告诉我毕德曼在哪里，我可以给你们解药，否则接下来的三个小时里，你们会在幻觉和呕吐之间度过。
[Character(name="avg_npc_067")]
[name="武装的感染者"]  你这个恶毒的......我......我不知道......什么毕德曼......我只是......贵族都得......死......唔......
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......那很抱歉，你们都要去监狱里待着了。
[Character(name="avg_npc_067")]
[name="武装的感染者"]  唔......？蘑菇？好大的蘑菇......怎么回事，怎么在动，怎么在咬人——
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  长官......很多人都受伤了......！他们已经占领了转角商业街和梅普乐广场......但是，更多的人都被困在了十二音街道.....
[name="塔佳娜"]  我们没法制止他们！
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=1)]
[name="塞弗林"]  ......从第一个人受伤开始，我们就无法阻止任何事情了。
[name="塞弗林"]  现在我们面对的结果有两种，一，投降。二，组织进攻。
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  我们该怎么做？
[Character(name="avg_npc_066")]
[name="塞弗林"]  投降，把控制权交给整合运动和叛乱分子，然后在冻土上饿死。
[name="塞弗林"]  带领民众发起进攻，两败俱伤，死伤惨重，苟且偷生的人在冻土上饿死。
[name="塞弗林"]  ......或者......
[name="塞弗林"]  ......
[name="塞弗林"]  如果伤亡不可避免，至少少死几个——咳咳，咳咳咳——
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=false)]
[name="塞弗林"]  呃......咳咳咳，咳咳咳——
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  长官——伯父？伯父？
[name="塔佳娜"]  ——！伯父，血，你的嘴角都是血......！
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  抱歉！让一下！塔佳娜小姐！
[Character(name="char_358_lisa_1#2", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  伯父他，他说不出话来——
[Character(name="char_358_lisa_1#2", name2="avg_npc_066",focus=1)]
[name="铃兰"]  您还好吗？调整呼吸，肺部病变导致失声，这种时候......这种时候应该......
[Character(name="char_358_lisa_1#2", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  ——怎么了？
[Character(name="char_358_lisa_1#3", name2="char_345_folnic_1#3",focus=1)]
[name="铃兰"]  塞弗林长官他、他其实——
[Character(name="avg_npc_066", name2="char_345_folnic_1#4",focus=2)]
[name="亚叶"]  ......你应该听医生的，戒烟。你的肺部顽疾不需要检查就能看出来有多糟糕。
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  让我检查一下......先把领口打开——
[name="亚叶"]  喂！别乱动！
[name="亚叶"]  ......
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  你......你是感染者？
[Character(name="avg_npc_069#4")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=false)]
[name="塔佳娜"]  欸！？
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......这是矿石病的症状，源石从他的肺部扩张到了咽喉......你喉下那些黑色的粉末状固体是......体表源石结晶。
[name="亚叶"]  啧，体细胞已经开始与源石融合，这就是你根本不在乎健康的理由吗！
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  难道是在刚才的战斗中？
[Character(name="avg_npc_069#4", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  这不是早期症状或是急性病变，他早就已经被感染了。
[name="亚叶"]  是天灾的时候......不对，那也太快了......感染时间还要更早......
[Character(name="avg_npc_066#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=false)]
[name="塞弗林"]  咳咳——咳咳咳——！
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......黑色的血块，铃兰，取样。
[Character(name="char_358_lisa_1#3")]
[name="铃兰"]  好的——！抱歉，长官，忍耐一下。
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  现在的医院——肯定没在运作了，嘁，先把他抬回议事厅！
[Character(name="avg_npc_066#3")]
[name="塞弗林"]  ——沃伦姆德，不能，没有长官！
[Character(name="avg_npc_066#3", name2="char_345_folnic_1#5",focus=2)]
[name="亚叶"]  你再强撑下去沃伦姆德就真的没有长官了——
[Character(name="avg_npc_066", name2="char_345_folnic_1#5",focus=1)]
[name="塞弗林"]  你——这种时候表现得，还真像个医生。
[name="塞弗林"]  咳咳，咳咳咳——
[name="塞弗林"]  唉，吐了口血好像就可以说话了，还挺方便的......
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  嘴硬。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=1)]
[name="塞弗林"]  亚叶小姐，我有一个请求。
[Character(name="avg_npc_066", name2="char_345_folnic_1#3",focus=2)]
[name="亚叶"]  你说你的，但我还是会把你带回去，丽萨，扶着点他，塔佳娜，我们把他扛回去。
[Character(name="avg_npc_069#4", name2="char_345_folnic_1#3",foc

... (全文14126字符)
```

### level_act11d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 8上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_065")]
[name="镇民A"]  塔佳娜！最后一个“留声机”被破坏了！我们没有手段对付那些巨人！
[Character(name="avg_npc_068")]
[name="镇民B"]  欸！那些暴徒开始烧房子了！该死，他们......火势在蔓延！
[name="镇民B"]  喂，塔佳娜，塞弗林呢！这种关键时候，他在哪里！？
[Character(name="avg_npc_069#2")]
[name="塔佳娜"]  塞弗林长官他......他受了伤，他正在休息......
[Character(name="avg_npc_065")]
[name="镇民A"]  都什么时候了还休息！？我们可是冒着生命危险——
[Character(name="avg_npc_068")]
[name="镇民B"]  闭嘴！现在不是吵架的时候，没看我们处于劣势吗！
[Character(name="avg_npc_065")]
[name="镇民A"]  那你的法术有用吗！？废物！
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  别、别吵了！控制好各自的管辖区域，防御性的源石技艺必须保证——
[Character(name="avg_npc_068")]
[name="镇民B"]  东边！东边的术师倒下了！快换一个顶上！
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_069#3")]
[name="塔佳娜"]  小心——！
[Character(name="avg_npc_065")]
[name="镇民A"]  火——！火烧过来了！
[Character(name="avg_npc_068")]
[name="镇民B"]  救——救命啊啊啊——啊啊——
[Character]
[name="镇民A"]  快、快灭火！有没有可以灭火的术师！！
[name="镇民B"]  救——疼，疼啊——
[name="镇民B"]  塔佳娜——救——我——
[Character(name="avg_npc_069#2")]
[name="塔佳娜"]  啊......啊啊......
[Dialog]
[Character]
[Blocker(a=0.3, r=0, g=0, b=0, fadetime=1, block=true)]
清晰的字句很快被单纯的惨叫遮掩。
皮肤烤焦的味道，比任何恶劣的玩笑都要让人胆寒。
被火焰包裹着的人逐渐失去形貌，只留下黑影似的肉体......
焦黑的皮肤和血，他挣扎着开口——
他很痛苦，他请求我帮助他。
但是——
但是——托尔当时，也是这样痛苦的吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="镇民"]  塔佳娜！！别恍神了，你离太远了！小心！
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  欸？
[Character(name="avg_npc_067")]
[name="武装的感染者"]  好机会！你也一起被烧死吧！贵族的宠物！
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  ——
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstreet2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[playsound(key="$smallearthquake", volume=0.6)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Character(name="avg_npc_011#2",fadetime=1,block=true)]
[delay(time=1)]
[name="泥岩"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  混乱。这座城镇从来都不是上下一心的，就像蛋糕，切成一块一块。
[name="萨卡兹战士"]  现在，那最后的一块也将要变成一盘散沙，他们毫无力量。
[name="萨卡兹战士"]  就算我们收手，就算我们撤退，他们当真能活下来吗？
[name="萨卡兹战士"]  莱塔尼亚必然会弃他们于不顾。
[name="萨卡兹战士"]  离这里最近的两座移动城邦，二十四座高塔，没有一个大人物能俯瞰到冬灵山脉里垂死挣扎的小城镇。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ——悲哀。
[name="泥岩"]  我们曾是厌倦了这种悲哀，而站在这里，不要忘了。
[name="泥岩"]  不要试图自作主张。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  ......当然。诶，你平时怎么不这么讲话呢？我只是抱怨抱怨。
[name="萨卡兹战士"]  抱怨我们等待隐忍了那么久，最后的结果也没什么变化，事情还是变得很糟糕。
[name="萨卡兹战士"]  只是一点不甘心的......牢骚。
[Dialog]
[stopmusic(fadetime=2)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_065")]
[name="镇民"]  他们要冲进来了！
[playMusic(intro="$indust_intro", key="$indust_loop", volume=0.4)]
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  ——唔！！
[CameraShake(duration=3, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="铃兰"]  我，我来帮忙！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=0.4)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[delay(time=0.5)]
[CameraShake(duration=2, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_067", name2="avg_npc_067",focus=1)]
[name="武装的感染者"]  该死！好不容易轰开的缺口！
[name="武装的感染者"]  那个沃尔珀是哪儿来的！？她、她怎么有九条尾巴？
[Character(name="avg_npc_067", name2="avg_npc_067",focus=2)]
[name="武装的感染者"]  不对！你也是感染者！你为什么要站在那里！？
[name="武装的感染者"]  这么小的年纪——你的不幸和痛苦，难道就不该反抗吗！？
[Character(name="char_358_lisa_1#4")]
[name="铃兰"]  ——
[Character(name="avg_npc_067")]
[name="武装的感染者"]  同胞！反抗他们！不要被骗了！
[name="武装的感染者"]  他们才是压榨我们欺压我们的罪人啊！
[Character(name="char_358_lisa_1#4")]
[name="铃兰"]  你——
[Character(name="avg_npc_067")]
[name="武装的感染者"]  呃？
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  你——在说什么啊！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=0.4)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[delay(time=0.5)]
[CameraShake(duration=2, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0,

... (全文14630字符)
```

### level_act11d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 8下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_068")]
[name="负伤的镇民"]  啊——长官，你在这里！
[name="负伤的镇民"]  听说你负伤了，你可以下地了吗？
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......咳，这里伤员很多......再这样下去，真的没地方落脚了......
[name="塞弗林"]  塔佳娜......塔佳娜她怎么了？
[Character(name="avg_npc_068")]
[name="负伤的镇民"]  我、我也不清楚，听说有人在她的面前被烧死，她就......
[Character(name="avg_npc_069#2")]
[name="塔佳娜"]  呜呜......呜......
[Character(name="avg_npc_066#2", name2="avg_npc_069#2",focus=1)]
[name="塞弗林"]  ........哭出来吧，孩子，你没必要强撑着的......
[Character(name="avg_npc_066#2", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  对、对不起......但是我......
[Character(name="avg_npc_066#2", name2="avg_npc_069#2",focus=1)]
[name="塞弗林"]  去哭一场。
[Character(name="avg_npc_066#2", name2="avg_npc_069#3",focus=2)]
[name="塔佳娜"]  可现在外面还是一片混乱！
[Character(name="avg_npc_066", name2="avg_npc_069#3",focus=1)]
[name="塞弗林"]  我去......有我在，还有罗德岛的各位。
[name="塞弗林"]  总有办法的。
[Character(name="avg_npc_066", name2="avg_npc_069#2",focus=2)]
[name="塔佳娜"]  不......您难道是想......
[Character(name="avg_npc_066")]
[name="塞弗林"]  带她去休息，我来指挥战局。
[Character(name="avg_npc_068")]
[name="负伤的镇民"]  没问题......
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=2)]
[name="塔佳娜"]  伯父......！答应我！不要去送死！
[name="塔佳娜"]  那是没有意义的......
[Character(name="avg_npc_066", name2="avg_npc_069#4",focus=1)]
[name="塞弗林"]  ......连你都说出没有意义这种话，那可就真没有意义了。
[name="塞弗林"]  至少怀着点希望吧......也许事情还有转机。
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltstreet2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=0.7, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  给我——让开！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=0.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[playsound(key="$smallearthquake", volume=0.2)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[delay(time=2)]
[Character(name="avg_npc_065")]
[name="镇民"]  成功了！那些巨像，巨像被粉碎了！
[Character(name="avg_npc_011#2")]
[name="泥岩"]  这种执着......真是出乎预料。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  泥岩，不该这么手下留情了，否则我们无法全身而退。
[Character(name="avg_npc_011#2")]
[name="泥岩"]  ......你眼中满是仇恨，和茫然。
[name="泥岩"]  你在为安托医生感到愤怒，可那又如何？
[name="泥岩"]  这里每个人背负的东西，都不少。
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  住嘴。
[name="亚叶"]  不许你......提她的名字。
[Dialog]
[Character]
[PlaySound(key="$rungeneral", volume=0.6)]
[delay(time=1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=1)]
[playsound(key="$e_atk_magic_m", volume=1)]
[Blocker(a=0, fadetime=0.5, block=false)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=false)]
[Character(name="char_345_folnic_1#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=10, randomness=30, fadeout=true, block=false)]
[name="亚叶"]  呃——！
[Character(name="avg_npc_011#2")]
[name="泥岩"]  等到饥荒和寒冬来临，你们还是会战败，这是一场无人生还的闹剧。
[name="泥岩"]  沃伦姆德......会灭亡。
[Character(name="char_345_folnic_1#5")]
[name="亚叶"]  这不用你说！
[Character(name="avg_npc_011#2")]
[name="泥岩"]  你在恨谁......？你又想救谁？
[Character(name="char_345_folnic_1#3")]
[name="亚叶"]  ......呃！又是那个法术——
[Character]
[Dialog]
[playsound(key="$smallearthquake", volume=0.2)]
[CameraShake(duration=2, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=false)]
[name="岩石巨像"]  嘎啊啊啊啊——！
[delay(time=2)]
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  亚叶姐姐——！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[playsound(key="$e_atk_magic_n", volume=0.4)]
[CameraShake(duration=0.3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=2, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[delay(time=1)]
[Character(name="avg_npc_053")]
[name="萨卡兹战士"]  减缓了泥岩的法术生效时间......真是奇异的技巧。
[name="萨卡兹战士"]  不过，你还有余裕分心？
[Character]
[Dialog]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_358_lisa_1#2")]
[name="铃兰"]  唔！放、放开我！
[Character(name="char_358_lisa_1#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  你应该庆幸，如果你再大个几岁，我会毫不犹豫地砍下你持杖的惯用手。
[Character(name="char_345_folnic_1#

... (全文23767字符)
```

### level_act11d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 纯剧情AVG序章
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
3:23 P.M.    天气/晴
莱塔尼亚境内，移动城镇沃伦姆德外，一棵微不足道的老栎树下
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_066#2",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  ......
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_069#2",fadetime=1,block=true)]
[delay(time=1)]
[name="塔佳娜"]  塞弗林长官......这已经是您今天的第三包烟了。
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  长官。
[Character(name="avg_npc_069#4", name2="avg_npc_066#2",focus=1)]
[name="塔佳娜"]  啊，抱歉，伯父......
[Character(name="avg_npc_069#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  我有依赖烟草的必要。当然，烟草和酒精都是坏东西......你说的对，别学我。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  但您的咳嗽越来越严重了。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  没必要这么毕恭毕敬，现在不是工作时间，我和你说过......算了。
[Dialog]
[Character]
他望向远处，烧毁的帐篷，肆意生长的野草，他抖了抖烟灰。
他本想在独处的时候获得一些安宁，即使只是通过一个称谓的变化。
[Dialog]
[delay(time=1)]
[Character(name="avg_npc_066#5")]
[name="塞弗林"]  唉......他们让你跑这一趟，他们竟然让你来！
[name="塞弗林"]  一群老滑头，他们不敢亲自来找我提意见也就罢了，他们还要伤害一个小姑娘——咳咳、咳咳！
[Character(name="avg_npc_069#4", name2="avg_npc_066#5",focus=1)]
[name="塔佳娜"]  伯父，别激动！是我自愿的，是我想着至少要亲自告诉伯父......
[Character(name="avg_npc_069#4", name2="avg_npc_066#5",focus=2)]
[name="塞弗林"]  呼——咳咳，咳咳——
[Character(name="avg_npc_069#2", name2="avg_npc_066#5",focus=1)]
[name="塔佳娜"]  您真的得戒掉烟酒了，您最近的状态很差......
[Character(name="avg_npc_069#2", name2="avg_npc_066#5",focus=2)]
[name="塞弗林"]  结果我大概已经猜得到了——该死。
[Character(name="avg_npc_069#2", name2="avg_npc_066#5",focus=1)]
[name="塔佳娜"]  ......嗯，会上讨论得很激烈。不过年轻人都躲在待客室里，谁也不敢发话。
[name="塔佳娜"]  他们、他们没有人帮我，对不起，只靠我说服不了其他人。
[Character(name="avg_npc_069#2", name2="avg_npc_066#3",focus=2)]
[name="塞弗林"]  ......自从城镇偏离航线之后情况就紧张了起来。现在不是搞社会实践的时候，学生和年轻人就算发表意见也没人会听。
[name="塞弗林"]  然后呢？
[Character(name="avg_npc_069#2", name2="avg_npc_066#3",focus=1)]
[name="塔佳娜"]  镇民代表一致认为，因为无法分辨感染者以及他们的感染情况，为了避免意外......
[Character(name="avg_npc_069#2", name2="avg_npc_066#3",focus=2)]
[name="塞弗林"]  ......
[Character(name="avg_npc_069#2", name2="avg_npc_066#3",focus=1)]
[name="塔佳娜"]  尸体必须埋葬在小镇之外，当然也......不允许举办葬礼。
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  唉......
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=1)]
[name="塔佳娜"]  我......我很抱歉......
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  ......但他们中有人是沃伦姆德的一员，是我们的家人，我们不应该这么简单就抛弃他们。
[name="塞弗林"]  埃克哈德是最好的裁缝，他接过他爹的裁缝店后，镇上几乎每一次婚礼都少不了他。
[name="塞弗林"]  毕德曼是个可怜人，因为大裂谷的事他丢了天灾信使的工作，但他在努力赎罪。他很坚强。
[name="塞弗林"]  凯文不是感染者，他为了他的妻子尽心尽力，他本来是个好丈夫。
[name="塞弗林"]  还有托尔瓦尔德，他——咳咳，咳咳——
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=1)]
[name="塔佳娜"]  您不该再抽烟了，长官。托尔也这么说过。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......你接受吗，孩子？实话实说，别管那些老滑头的想法。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  我......我不知道。
[name="塔佳娜"]  但我只想托尔能入土为安，而不是在死后还要被当做危险品......被小心翼翼地处理，被风吹雨打......
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......好吧。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  为什么我们要这么对待他们？过去，过去不是这样的。
[name="塔佳娜"]  还有那位矿石病医生。她很了不起，没有抛弃沃伦姆德，这四个人都有权利得到体面的下葬，但是——
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  就因为感染者和他们一起——
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  ......该责怪的是这场火灾。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  我明白。
[name="塞弗林"]  但是......但是这件事得延后，现在还不能抛弃他们的遗体。
[name="塞弗林"]  我联系了最近的宪兵队，他们会在救援队里增派专业人士协助调查，在那之前，尸体都得保存在我照顾得到的地方。
[name="塞弗林"]  只要有专门人士在，我们就可以更合理地对待死者。
[Character(name="avg_npc_069#4", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  最近？我们还能得到救援......？
[Character(name="avg_npc_069#4", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  “最近”。他们可能要一个月——视那条裂缝的具体长度，可能要好几个月。
[Character(name="avg_npc_069#2", name2="avg_npc_066",focus=1)]
[name="塔佳娜"]  沃伦姆德在脱离原本航线以后情况一天比一天糟糕，大家都说我们得绕过大裂谷往回走，回到正常的航线。
[name="塔佳娜"]  不过越过大裂谷要绕的路也太远了，拖得时间太久的话......
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  ......总之，先等等。
[name="塞弗林"]  让我和托尔多待一会，我......我有这个权利。
[name="塞弗林"]  如果那些老滑头要把我的孩子扔在沃伦姆德之外的荒郊野岭上，就让他们对着他们的士官长开火。
[name="塞弗林"]  对着我，开火。
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=1)]
[name="塔佳娜"]  不会的！大家都清楚您对城镇的付出，不至于......不至于的！
[Character(name="avg_npc_069#2", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  ......不，忘了吧。
[name="塞弗林"]  在这种情况下，我不能说这种话......士官长不能说这种话。我们应该公事公办。
[Character(name="avg_npc_069#4", name2="avg_npc_066#2",focus=1)]
[name="塔佳娜"]  可托尔毕竟是您的儿子......！
[Character(name="avg_npc_069#4", name2="avg_npc_066#2",focus=2)]
[name="塞弗林"]  塔佳娜，你回去告诉他们吧。就说——
[Character(name="avg_npc_066#2")]
[name="塞弗林"]  就说......
[name="塞弗林"]  就说我同意了、咳、我同意了。
[name="塞弗林"]  咳咳，咳咳咳——
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_011#2",fadeitme=1,block=true)]
[delay(time=1)]
[name="？？？"]  ......
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="武装的感染者"]  队长，他们回来了。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="？？？"]  ......嗯。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="武装的感染者"]  多亏了这些本地人，我们才能混进附近的城镇里补充资源......
[name="武装的感染者"]  猎人小队也快回来了，但愿今天能有所收获。我已经吃了两天沙虫

... (全文12181字符)
```

### level_act11d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 纯剧情关
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.4)]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[Character(name="char_367_swllow_1")]
[name="灰喉"]  请进。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_294_ayer",fadetime=1,block=true)]
[delay(time=1)]
[name="断崖"]  ......各位。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......我大概猜到你们会说什么，不过......你可以先说说看。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=1)]
[name="断崖"]  那我就直说了......
[name="断崖"]  天灾信使毕德曼是元凶的可能性值得怀疑。
[name="断崖"]  在物证人证极端匮乏的情况下，我只能做出如此判断......
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=1)]
[name="灰喉"]  我见过你带来的证物。毕德曼是危机合约的天灾信使。
[name="灰喉"]  罗德岛与他们多有合作，为了对抗天灾，他们的确做出了功不可没的贡献。
[name="灰喉"]  但这不代表......他们有那么“好心”。
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=2)]
[name="断崖"]  ......以我作为天灾信使护卫工作的经验，是的。
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=1)]
[name="灰喉"]  在沃伦姆德遭受天灾侵袭后，毕德曼做出了无论如何沃伦姆德都难逃重创的判断。
[name="灰喉"]  为了让更多人活下来，刺杀一位罗德岛干员从而引起外界的关注......完全可行。
[name="灰喉"]  不过，危机合约真的会坐视这种委托进行？他们不该如此没有底线。
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=2)]
[name="断崖"]  危机合约不过提供了一个“提出悬赏”和“完成目的”的平台......幕后是什么样，没人知道。
[name="断崖"]  但有一小部分天灾信使......他们的极端信念就是混淆天灾与人祸，不客气点，就是一群变态的功利主义者。
[name="断崖"]  只要能消除人们对天灾的恐惧......不，甚至都不是为了帮助他人，只要为了对抗他们亘古以来的名为“天灾”地假想敌——
[name="断崖"]  他们会不择手段。
[name="断崖"]  而现在，他们扎根在正常运作的合约机制背后，而且比我之前预想的还要根深蒂固。
[name="断崖"]  但是......问题就在这里。
[name="断崖"]  这种过激行为的前提是，他坚信罗德岛，坚信亚叶会为了寻找安托来到这里。
[name="断崖"]  虽然不知道那个疯子靠什么手段利用了危机合约，不过有一点我可以确定。
[name="断崖"]  那个疯子不会靠“情感”来判断事物，在他们眼里，我们的举动已经算得上是天方夜谭。
[name="断崖"]  把工作赌在“罗德岛对干员的情感”这点上......很奇怪。
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=1)]
[name="灰喉"]  ......都是推测而已。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  不。
[name="塞弗林"]  ......这并不是无稽之谈。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  为什么——
[name="灰喉"]  ——你手里的是，“留声机”的施术单元？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  这是唯一的物证，火灾的规模，火势，毫无疑问是靠这枚过载的施术单元做到的。
[name="塞弗林"]  ——但毕德曼他......不是莱塔尼亚人。
[name="塞弗林"]  就算他能千方百计找到这枚施术单元......他......也掌握不了令其过载并瞬间蒸发人体程度的源石技艺。
[name="塞弗林"]  他作为天灾信使抵达这里不过短短半年时间，更不要提L-44“留声机”系统本来就是最近才引进的新产品。
[name="塞弗林"]  如果他真能在这么短的时间内学到这个地步，他应该去莱塔尼亚的中央大学，并入主一座高塔。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  所以......
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......是的，所以在这一切过后，我们仍旧不确定凶手是谁。
[name="塞弗林"]  除了飞来横祸把城镇破坏的一塌糊涂，除了让我们接下来的道路更加困苦——
[name="塞弗林"]  ——我们一无所得。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  我们不应当这么快下这么......虚无的判断。都只是一些浅显的推论。
[name="灰喉"]  亚叶和铃兰知道这件事吗？虽然发生了很多事情......但她们才是最关心这件事的......
[Character(name="char_367_swllow_1", name2="char_294_ayer",focus=2)]
[name="断崖"]  ......讲真，我不知道怎么开口。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  亚叶小姐已经试着接受自己复仇落空的那种虚无感，也许很自私，但只有这样才是对大家最好的选择。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  ......又或者，我们可以试着继续找出真相。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  大部分的叛逆分子被捕，另一些则跟着泥岩离开，但仍旧有人在抗议和叫骂......经历过那些之后，没人还有心气闹事。
[name="塞弗林"]  但监狱里的情况并不算好......更别提这次的暴乱同样损毁了不少物资，食物配给会越发紧张......
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  ——我明白。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  呼......那么塔佳娜怎么样了？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  一直绷着的弦断掉了，心理问题比轻度烧伤严重得多。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  是这样......是我没有做好......咳咳——咳咳！
[name="塞弗林"]  如果在这个时候继续追究下去，只会再度引起冲突。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=1)]
[name="断崖"]  ......您早就放弃了真相。
[name="断崖"]  如果您一开始就想到了这些疑点，却依旧顺水推舟，只说明......
[Character(name="char_294_ayer", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  不，你要明确一件事情，从目前所有的情报来看，他依然是最大嫌疑人。
[name="塞弗林"]  不过是关于“行事作风”和“学习能力”的两点推测并不能证明任何东西，一切明确的线索都指向他。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=1)]
[name="断崖"]  ......我无法否认这点。说到底，也许“危机合约”有某些我们不曾知晓的手段也有可能。
[name="断崖"]  真相很遥远。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......在我儿的葬礼被否决的时候，我就已经放弃追寻什么真相了。
[name="塞弗林"]  关键吗？
[name="塞弗林"]  我只是想......活着的人至少，好好的......咳咳，咳咳咳——！
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  如果您真的这么想，您应该回到罗德岛检查。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......你在发抖。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  我不掩饰，我依旧对感染者感到......恐惧。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  恐惧......哈，刚才还在为我们战斗到这个地步的恩人，居然会说自己害怕感染者。
[name="塞弗林"]  ......也许罗德岛的确是值得托付的对象。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  唉，关于您的感染......我想亚叶还会有话要问的。
[name="灰喉"]  什么时候的事了？
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  如果早知道灰喉小姐您对感染者如此芥蒂，也许我不该隐瞒。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=1)]
[name="灰喉"]  该抱歉的是我，我已经......习惯感到恐惧了。
[Character(name="char_367_swllow_1", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  ......在那些冬灵族的老头刺杀贵族和商人的时候，我也在追杀他们。
[name="塞弗林"]  那时，最后一个老头，在湖边生了一簇篝火，他早知道我要来，阴影暴露了我的位置，他用源石刺进了我的左胸。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=1)]
[name="断崖"]  ——他也是感染者。
[Character(name="char_294_ayer", name2="avg_npc_066",focus=2)]
[name="塞弗林"]  没错......他也是感染者，我没能解决他，当时我以为他是打算鱼死网破，他和我的复仇都抵达了终点——
[Character(name="char_294_ayer", name2="avg_npc_066",focus=1)]
[name="断崖"]  ......结果呢？
[Character(name="c

... (全文11876字符)
```

### level_act11d0_sub-1-1_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 支线1
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
2:25 P.M.    天气/阴
莱塔尼亚境内，移动城镇沃伦姆德，议事厅临时客房
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
......该怎么办？
谁能想到比起一座创造了无数经济价值的城镇，他们居然更看重一场婚礼？
大裂谷的损失惨重，尽管避免了人员伤亡，但是沃伦姆德失去了四分之一的面积是板上钉钉的事实......
......我该怎么办？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[name="毕德曼"]  请进。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_066",fadetime=1,block=true)]
[delay(time=1)]
[name="塞弗林"]  ......看起来，你的伤好多了。
[Character]
[name="毕德曼"]  ......
[Character(name="avg_npc_066")]
[name="塞弗林"]  别总是这么一副“我们全要完蛋”的表情，偶尔也该豁达一点。
[name="塞弗林"]  你就安心待在这吧，议事厅的客房总不至于还有人敢来闹事。
[Character]
[name="毕德曼"]  我的家呢？
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......惨不忍睹。你不会想知道的。
[Character]
[name="毕德曼"]  告诉我。
[Character(name="avg_npc_066")]
[name="塞弗林"]  门锁被撬了，里面被砸了个稀巴烂，除了你的保险柜基本没有什么东西是完好的。
[name="塞弗林"]  ......当然，他们你没那么好心放过你的宝贝保险柜，他们只是没有成功，上面有高温加热的痕迹。
[Character]
[name="毕德曼"]  ......随他们去吧。
[Character(name="avg_npc_066")]
[name="塞弗林"]  稀奇，你对你的家很有感情？
[Character]
[name="毕德曼"]  怎么也是住了些年的房子......不过对你们而言，我始终是个外人。
[Character(name="avg_npc_066")]
[name="塞弗林"]  别这么说......作为一座商业城镇，沃伦姆德可不会那么排外。只不过......
[Character]
[name="毕德曼"]  我烟味过敏。
[Character(name="avg_npc_066")]
[name="塞弗林"]  啊，好。
[name="塞弗林"]  但听我一句劝，你暂时就不要随便上街了。这次只是皮外伤，下一次就不好说了。
[name="塞弗林"]  你知道，现在沃伦姆德没有宪兵队驻扎，塔佳娜他们顶多算是民兵团，真出了事没人管得住。
[Character]
[name="毕德曼"]  你也做了件蠢事，塞弗林。
[Character(name="avg_npc_066")]
[name="塞弗林"]  ......我也不知道他们一场婚礼能办这么久啊。
[delay(time=1)]
[name="塞弗林"]  行了，好好休息，我就说这么多。
[name="塞弗林"]  ......责任不在你，我们都知道。
[Character]
[name="毕德曼"]  天灾无法准确预测......
[Character(name="avg_npc_066")]
[name="塞弗林"]  人祸也是。
[name="塞弗林"]  好了，你就安心养伤吧。
[name="塞弗林"]  想想之后的事情。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=2)]
之后的事情。
我已经预见到了之后的事情。
大裂谷完美地封死了东南方向的全部航线，沃伦姆德只能向北方继续行进。
......如果不能及时和其他城镇建立救援协议，冬天来临，势必会出现饥荒。
饥荒......
会死很多人，我......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
不，这不怪我。
......这不怪我。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
七天后
[Dialog]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[name="？？？"]  喂~有人在吗？
[name="？？？"]  我听说沃伦姆德的天灾信使暂住在这里喔？有人吗？
[Dialog]
是没听过的声音，年轻女性。
她知道我是天灾信使。
塞弗林说得对，我应该避免抛头露面才是。
......所以，干脆装作不在好了。
[name="镇民"]  安托医生，毕德曼已经有很多天没有露过面了......
[name="？？？"]  哎，我们讲讲道理啊，那些家伙乱撒气把天灾信使揍了一顿，你让他怎么露面？
[name="镇民"]  话、话是这么说......欸，等等，您要做什么......
[name="？？？"]  ——把门踹开啊？
[name="镇民"]  欸？
[Dialog]
欸？
[delay(time=1)]
[name="？？？"]  别看我样，我也是能徒手干掉源石虫的——！
[name="？？？"]  毕德曼，你在的吧？抱歉我不太清楚房间内的布置，麻烦你离门远一点哦！
[name="？？？"]  躲不开的话，干脆防御吧！防御！双手交叉！
[name="？？？"]  嘿——！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$char_emp", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[Dialog]
......罗德岛干员，安托。
她不由分说地找到我，为了寻求我的帮助。
我......我为什么要帮她？
在一座铁定要玩完的城镇里开设临时诊所救治感染者，这有什么好处？
对了......她是在利用我的愧疚心。不然她没有必要找上我这么一个犯了错的天灾信使。
我......
我没有拒绝的理由，塞弗林暗示我，这是改善我和居民关系的机会。
大概吧，我是这么和自己说的。
所以我去了。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
......不早了。
我干嘛要工作得这么努力......
[Character(name="avg_npc_069#4")]
[name="塔佳娜"]  啊......
[Dialog]
[Character]
......看吧。他们见到我还是一副见到瘟神的表情。
[Character(name="avg_npc_069")]
[name="塔佳娜"]  毕德曼......谢谢你帮了托尔和塞弗林伯父。
[name="塔佳娜"]  不少没能躲开天灾范围的商旅也被困在了沃伦姆德，我们急需了解天灾的你帮助我们......
[name="塔佳娜"]  有些不理智的镇民做了不好的事情，但毕德曼先生您也在这里住了很久了，希望您能理解。
[name="塔佳娜"]  请好好休息。
[Dialog]
[Character]
搞什么......来这套啊。
......算了。
明天还要帮安托搬箱子......今天还是早点休息吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_066")]
[name="塞弗林"]  喔，毕德曼，你很努力，这样我们的辟谣工作也能更加顺利。
[Character]
[name="毕德曼"]  ......我说过我对烟过敏吧。
[Character(name="avg_npc_066")]
[name="塞弗林"]  你的私人空间在楼上，这里是公共区域。
[Character]
[name="毕德曼"]  辟谣？
[Character(name="avg_npc_066")]
[name="塞弗林"]  帮你一把。
[name="塞弗林"]  ......但相对的，我希望你也能帮帮我们。安托医生毕竟是个外人，你才是自己人。
[Character]
[name="毕德曼"]  ——半个自己人。
[Character(name="avg_npc_066")]
[name="塞弗林"]  好好......近期我们将会实施紧急时期物资管制方案，但是......
[name="塞弗林"]  十二音街道的物资会是个大问题。
[name="塞弗林"]  新来了不少感染者难民......大都是商人和旅客，他们没能来得及逃离天灾范围。
[name="塞弗林"]  他们无法翻过满是活性源石结晶的大裂谷，别无选择，都追上了这座城镇。
[Character]
[name="毕德曼"]  沃伦姆德可没有接纳那么多人的余裕......
[Character(name="avg_npc_066")]
[name="塞弗林"]  见死不救也不行，事后没法交代。
[name="塞弗林"]  所以我们暂且把他们都带去十二音街道那边了，住房勉强可以靠临时帐篷解决，但是食物......
[name="塞弗林"]  我们还是得优先沃伦姆德的合法居民，然后，才是人道主义救援。
[Character]
[name="毕德曼"]  很合理。他们会理解的。
[Character(name="avg_npc_066")]
[name="塞弗林"]  会理解吗......但愿吧。
[Character]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="毕德曼"]  ......
[name="毕德曼"]  ......信？谁进了我的房间，是塞弗林那家伙吗......
[name="毕德曼"]  这是——
[name="毕德曼"]  危机合约？
[Dialog]
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=1)]
[name="毕德曼"]  谁？
[name="？？？"]  不要开门，就这样听我说。
[name="毕德曼"]  ......
[name="毕德曼"]  ......事到如今，还要找我做什么？

... (全文9535字符)
```

### level_act11d0_sub-1-2_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 九尾狐活动 支线2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltstrongpoint",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  泥岩，他们在追捕剩下的逃犯。
[name="萨卡兹战士"]  ......但他们本来完全可以让逃犯在这片群山中自生自灭，抓回去，是救了他们的命。
[name="萨卡兹战士"]  让人分不清他们是好心还是残忍。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......没有跟来的人都和我们关系不大，但是......
[name="泥岩"]  尽量避开他们的搜查，我们要在入冬之前离开这里。
[name="泥岩"]  已经很冷了。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  离开这里，去哪儿？
[name="萨卡兹战士"]  我们流浪了这么久，到头来呢？永远不会有好结果的。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......那么，我们回家。
[name="泥岩"]  我们回去，找一片安静的树林，我们在那里生存。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  我们要的斗争呢？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  ......先暂且......活下去。
[name="泥岩"]  活下去，只是为了活下去，我们就在和这片大地抗争。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=1)]
[name="武装的感染者"]  ......我们要去哪儿？回家？什么家？
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  ——卡兹戴尔。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=1)]
[name="武装的感染者"]  啊......
[name="武装的感染者"]  但我们呢？我们不是萨卡兹，那里......
[Character(name="avg_npc_011#2")]
[name="泥岩"]  你们，是萨卡兹的同伴。
[name="泥岩"]  卡兹戴尔之外的地方也许容不下萨卡兹，但卡兹戴尔，容得下你们。
[name="泥岩"]  虽然这并不是因为宽容，而是因为那里早已......一无所有。
[name="泥岩"]  卡兹戴尔......不是一座城的名字，也不能算是国家的名称，严格来说，卡兹戴尔只是一个地区。
[name="泥岩"]  一片不被允许建立家园的流亡者们的土地。
[name="泥岩"]  那里......是所有无家可归之人的归宿。是所有无根之人的归宿。
[name="泥岩"]  是你们的归宿。
[Character(name="avg_npc_067")]
[name="武装的感染者"]  ......谢谢。
[name="武装的感染者"]  也许在那个遍地都是萨卡兹感染者的卡兹戴尔，我们反而能安安稳稳地生活下去吧......
[Character(name="avg_npc_067", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  莱塔尼亚对感染者的温和态度终归只是血统和源石技艺普及的副产物，并不代表他们真的愿意接纳你们。
[name="萨卡兹战士"]  撕下游刃有余的面具之后，第一个遭到排斥的，还是感染者。
[Character(name="avg_npc_067", name2="avg_npc_053",focus=1)]
[name="武装的感染者"]  ......不光是矿石病，这个繁荣的国家已经遗忘了那些真正悲惨的角落。
[name="武装的感染者"]  沃伦姆德这样的悲剧......不过是贵族们怄气的幌子，是银行家和宫廷艺术家们茶余饭后的话题。
[name="武装的感染者"]  我们......不能接受。也不想接受。
[name="武装的感染者"]  离开就离开吧，我们去卡兹戴尔，去你们的故乡看看。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  ......嗯。
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=2)]
[name="萨卡兹战士"]  莱塔尼亚会不会找我们麻烦？
[Character(name="avg_npc_011#2", name2="avg_npc_053",focus=1)]
[name="泥岩"]  也许吧......无论前因后果如何，一批萨卡兹感染者出现在了一座被毁的城镇，我们会成为罪魁祸首。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=1)]
[name="武装的感染者"]  塞弗林知道真相，他难道会栽赃给我们......？
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  他会的。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=1)]
[name="武装的感染者"]  .......
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  ......这只是他的行事方式......根据他知道的情报，做出对城镇损害最小的判断。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=1)]
[name="武装的感染者"]  那我们必须得快点离开这里，不然的话，我们会遭到莱塔尼亚官方的通缉。
[Character(name="avg_npc_067", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  嗯，所以才需要尽早规划路线......啊......
[Character(name="avg_npc_011#2")]
[name="泥岩"]  抱歉，等我一会，我还要去个地方......
[name="泥岩"]  一会就好。
[stopmusic(fadetime=3)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltruins",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Character(name="char_367_swllow_1#3")]
[PlaySound(key="$d_gen_walk_n", volume=0.4)]
[name="灰喉"]  ......
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  你在这里。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  亚叶干员......
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  不，不用起身，我不会靠你太近的。
[name="亚叶"]  ......你在等人，对吧？
[Character(name="char_367_swllow_1")]
[name="灰喉"]  嗯。
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  整合运动事件发生的时候我并不在罗德岛本舰......你似乎，变了不少。
[name="亚叶"]  和传闻中相比，给人的感觉大不一样。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  传闻？
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  听说你和一位精英干员并肩作战，在龙门解决了很多事情。
[Character(name="char_367_swllow_1#3")]
[name="灰喉"]  ......只是一只到处撒血的鲁莽大猫。
[name="灰喉"]  我们也没能......解决任何事情。
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  ......谢谢。
[name="亚叶"]  我要再说一次谢谢，如果没有你和小丽萨在，我不知道事情会变成什么样。
[Character(name="char_367_swllow_1#3")]
[name="灰喉"]  ......
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  罗德岛也好，塞弗林也好，哪怕是那个整合运动也好，明明没有人希望事情变成这一步......
[name="亚叶"]  好像所有人都在阻拦着惨剧发生，但它依旧势不可挡。
[name="亚叶"]  安托她......她......
[Character(name="char_367_swllow_1")]
[name="灰喉"]  不用勉强自己感慨什么，事情已经过去了。
[Character(name="char_367_swllow_1#3")]
[name="灰喉"]  只愿逝者安息。
[Character(name="char_345_folnic_1#4")]
[name="亚叶"]  ......我们没能将凶手绳之于法，不仅如此，我们甚至没能保护好安托保护过的这座城镇。
[name="亚叶"]  安托她会怪我的吧。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  只有你会怪罪你自己，安托小姐是个开朗的人。
[name="灰喉"]  是啊，我想她会拍拍你的肩膀，然后陪你喝到烂醉。
[Character(name="char_345_folnic_1#2")]
[name="亚叶"]  呵呵......也是啦，原来你们很熟？
[Character(name="char_367_swllow_1")]
[name="灰喉"]  我和那个陪她喝到烂醉的“精英干员”很熟。
[Character(name="char_367_swllow_1")]
[name="灰喉"]  ......放弃追究这一切的人，不止我们。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.4)]
[Character(name="avg_npc_011#2",fadetime=1,block=true)]
[delay(time=2)]
[name="泥岩"]  ......
[Character(name="char_367_swllow_1")]
[name="灰喉"]  你果然来了。
[Character(name="char_367_swllow_1", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  这是，新摘的野花......
[Character(name="char_367_swllow_1", name2="avg_npc_011#2",focus=1)]
[name="灰喉"]  你应该清楚眼下的状况，清扫任务已经接近尾声，而罗德岛近期就会离开这里，试着联络资源调度进行援助。
[name="灰喉"]  但到那时候......
[Character(name="char_367_swllow_1", name2="avg_npc_011#2",focus=2)]
[name="泥岩"]  没有人会为我们说话，我知道。
[name="泥岩"]  ......我不会怪塞弗林。他只能这么向贵族们汇报，否则要遭殃的是他们......
[name="泥岩"]  我们会尽快离开这里，很快。只是，这里还有我们死去的同伴......我不想不辞而别。
[Character(name="char_345_folnic_1#4")]
[na

... (全文11816字符)
```

### training_act11d0_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动11d0教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 今天的训练目标是如何应对L-44"留声机"系统，类似的自律发生装置正逐渐在一些国家普及，我们需要掌握相关的指示。
[PopupDialog(dialogHead="$avatar_ansel")] 啊，那个敌人正对"留声机"施法！他在做什么？
[PopupDialog(dialogHead="$avatar_doberm")] 这是敌人夺取<@tu.kw>控制权</>的手段，我们得想办法阻止他，或者，把控制权夺过来。



[Tutorial(focusX=30, focusY=60, focusWidth=220, focusHeight=220, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
敌方的特殊单位会用法术改变"留声机"的协议运作机理，以<@tu.kw>控制</>这座"留声机"。

[PopupDialog(dialogHead="$avatar_snakek")] 那我们应该怎么办？
[Tutorial(focusX=-160, focusY=60, focusWidth=106, focusHeight=110, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
打断敌方的源石技艺，在"留声机"附近的<@tu.kw>协议入口</>部署干员，以<@tu.kw>控制</>这座设施。
[Tutorial(focusX=-58, focusY=-40, focusWidth=106, focusHeight=110, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
每个<@tu.kw>协议入口</>下方的源石线路都将产生共鸣，占领多个<@tu.kw>协议入口</>可以<@tu.kw>加速控制</>"留声机"装置。
[Tutorial(focusX=-52, focusY=18, focusWidth=106, focusHeight=30, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
另外，"留声机"的<@tu.kw>控制权</>由它的<@tu.kw>充能进度</>决定。当进度为<@tu.imp>0%</>时，"留声机"将被<@tu.imp>敌方操纵</>，反之，当进度为<@tu.kw>100%</>时，则我方夺得<@tu.kw>控制权</>。

[PopupDialog(dialogHead="$avatar_doberm")] 现在，去占领那座L-44"留声机"装置，实践才是最好的训练。
[PopupDialog(dialogHead="$avatar_ansel")] 明白！
[PopupDialog(dialogHead="$avatar_snakek")] 下面还有其他敌人，就交给我吧！


```

### training_act11d0_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动11d0教学关_b

[PopupDialog(dialogHead="$avatar_beagle")] 这、这就是<@tu.kw>协议入口</>吗......我该......
[PopupDialog(dialogHead="$avatar_doberm")] 保持冷静，迅速占领，现在又出现了一名企图夺取<@tu.kw>控制权</>的敌人。
[PopupDialog(dialogHead="$avatar_beagle")] 又来一个？杰西卡！帮、帮帮我！
[PopupDialog(dialogHead="$avatar_jesica")] 诶！？
[PopupDialog(dialogHead="$avatar_jesica")] 好、好的！我来了，呜......！
[PopupDialog(dialogHead="$avatar_red")] 红也来帮忙，红有刀，能做到。


```


## 统计

- 总字符数：247740
- 对话行数：2541


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
