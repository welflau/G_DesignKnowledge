# 明日方舟 · 活动剧情 · act16d5（21段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act16d5」完整剧情脚本（21个文件，2184行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act16d5
- 脚本文件数：21

### level_act16d5_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[StopSound(channel="bgs")]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(key="$midautumn", volume=0.4)]
[PlaySound(key="$gavel2", volume=1)]
[dialog]
[delay(time=2)]
[Subtitle(text="书接上回，说那跛脚书生败兴而归，自此之后，郁郁不得志。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[delay(time=1)]
[Character(name="avg_npc_138#4",fadetime=1)]
[delay(time=1.5)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="哪件事？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="自然是画。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="什么画？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是那书生痛失故友，心如死灰，一蹶不振十数载后，再一次地灵犀一动——他打定心思，殚心竭虑，发誓要完成那幅毕生力作。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="要画什么？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="要画未见之物。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Subtitle(text="要如何画？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="得作未想之想。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=2)]
[Subtitle(text="诶，话说到这儿，就有点儿意思了。各位都知道，人所想象之极限，一定是所见所知的经验。要靠想象勾勒出未曾知晓的事物，骗别人简单，骗自己，难如登天。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="毕竟这天底下，哪有能想出自己没见过的东西的能人呢？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="那书生对着白纸苦思十来天，瘦了足足三十多斤。本就跛脚，形貌越发恐怖。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[PlaySound(key="$blizzard",channel="bgs", volume=1, loop=true, block=false)]
[Subtitle(text="时入深冬，书生家早已断粮。邻里害怕他那副模样，皆不敢近。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="直到某天，跛脚书生几度朦胧醒来，四肢无力，却头脑清明。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Background(image="bg_white",screenadapt="coverall",fadetime=3)]
[Subtitle(text="他深知自己大限将至。环顾四周，家徒四壁，恍惚间，只感觉四下无物，真真正正变成了孑然一身。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[delay(time=0.6)]
[Subtitle(text="书生逐渐看不见眼前被大雪打湿又冻上的地面，再听不见门窗漏出的风雪动静。睁眼眨眼，落入混沌，感到墙壁正在远游离去，书案消散，笔墨纸砚皆如过眼云烟。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="某个时刻，他忽然得知了窗外鹅毛大雪的具体数目，得知了月光的角度与云层的真理。他伸手摸索夜幕，又不小心摔倒在地，地面却不再是双脚的阻碍，他坠向地底，而又飞向深空。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="他睁眼却不能看，凝神却不能听，周遭黑暗一片——他却反而忽地狂喜起来，好像只有在这绝无外物干扰的境地，他才能寻到真正的创作，而非对其他已有事物的临摹与亵渎。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[soundvolume(channel="bgs",volume=0,fadetime=5)]
[Subtitle(text="他继续等，等到寂灭一片，连自己干枯的肉身也感受不到，他才开始思考——只有在这万事万物都不复存在，唯有他的意识独自清明时，他短暂地成为了他精神的主宰。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Background(image="bg_light",screenadapt="coverall", fadetime=2,block=true)]
[Subtitle(text="他的想象再也不受拘束，创造着存在也不存在的事物——在他思维的疆土上，各种怪诞平地而起，盖过了现实。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="那天深夜，隔壁起夜的老夫子，看见跛脚书生的茅屋里流光溢彩，光怪陆离，发出各种平生未闻的声响，难以名状。老夫子起胆，就隔着墙偷瞄了一眼。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="只那一眼，便再不敢深究。他匆匆忙忙回到屋里，久久不得入眠。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="隔天，邻里纷纷来到茅屋前，夺门而入，发现了书生的遗体，再无别物。大家都以为他是冻死的，村长上前一看，书生面前摊着一张白纸，落满了霜，啥也没画。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="事后，人们便感慨书生走不出过往，痴死在画卷前。也有说是书生早就染了怪病，控制不住自己的法术，才整出这些怪事。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="唯一窥见真相的老夫子，却从不对别人说起这件事。只是在他临终前，他对自己的儿子说，那被人唾弃，连名字都被忘记的跛脚书生，是真正的千古大家。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[soundvolume(channel="bgs",volume=1,fadetime=4)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=3, block=true)]
[Background(image="bg_landscape",screenadapt="coverall",fadetime=0,block=true)]
[StopSound(channel="bgs", fadetime=1)]
[stopmusic(fadetime=2)]
[delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[delay(time=2.5)]
[Character]
[delay(time=0.6)]
[Character(name="avg_npc_140#2")]
[name="村民"]为啥子？
[dialog]
[delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=2)]
[name="说书人"]因为那个跛脚书生在那晚切实完成了诺言，切实画出了“世间从未有过之物”。
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=1)]
[name="村民"]咋感觉和书上写的内容不大一样？
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=2)]
[name="说书人"]老夫子来不及说出为什么，或者压根就说不出为什么就咽了气。
[name="说书人"]于是坊间流传的说辞，就只有跛脚书生从春风得意到失魂落魄的这么一段。
[name="说书人"]至于真相如何，恐怕无人知道了。
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=1)]
[name="村民"]可是画没见过的东西，那有啥难的嘛，我回去乱涂一幅，你们不也没见过。
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=2)]
[name="说书人"]欸，话不能这么说。你从没见过大湖，但见过雨后积水，我便告诉你，湖是很多的积水。说到底，你还是见过的。
[name="说书人"]这跛脚书生，厉害就厉害在这儿了。
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=1)]
[name="村民"]那照你这么说，他到底画了啥？
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=2)]
[name="说书人"]谁知道呢。
[Character(name="avg_npc_140#2",name2="avg_npc_138#4",focus=1)]
[name="村民"]嗨，能不能别老讲这么复杂的，咱不爱听啊，啥时候讲讲其他的？
[Character(name="avg_npc_138#4",name2="avg_npc_142#2",focus=2)]
[name="孩子"]我要听上次那“形单影只向天去，雌雄双剑分天下”的大结局！
[Character(name="avg_npc_138#4",name2="avg_npc_142#2",focus=1)]
[name="说书人"]会讲的，都会讲的。天下讲不完的事，我用寥寥百年的阳寿去讲，要是还奢求面面俱到，就有点贪得无厌了。
[name="说书人"]既然你们想听，那下一回，咱们就讲点别的。
[Character(name="avg_npc_138#4",name2="avg_npc_142#2",focus=2)]
[characteraction(name="ri

... (全文19229字符)
```

### level_act16d5_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_plankroad",screenadapt="coverall")]
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4")]
[PlayMusic(intro="$longmenbat_intro", key="$longmenbat_loop", volume=0.4)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]这些东西......是什么？感染生物吗？
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=1)]
[name="克洛丝"]没有发现感染的迹象喔......而且说是生物，射穿它们的时候，它们就变成黑色的水渍消失了欸。
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]......某种法术？
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=1)]
[name="克洛丝"]有可能。
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]这样下去不行，数量太多了......得找出源头。
[name="炎熔"]它们是从哪个方向进入城镇的？
[Character(name="avg_npc_144#4",name2="char_1011_purgatory_1#4",focus=1)]
[name="克洛丝"]视野越来越暗了哦，小炎熔。
[Character(name="avg_npc_144#4",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]......我知道。
[Character(name="avg_npc_144#1",name2="char_1011_purgatory_1#4",focus=1)]
[name="克洛丝"]还要追吗？
[name="克洛丝"]我们是怎么来到这里的还不清楚......情况有点诡异，我不太建议现在过于深入。
[name="克洛丝"]虽然这可能是个线索啦，但也不用这么着急。
[Character(name="avg_npc_144#1",name2="char_1011_purgatory_1#1",focus=2)]
[name="炎熔"]......
[Dialog]
[Character]
[Delay(time=0.6)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="char_455_nothing_1#3", fadetime=1)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="乌有"]二位恩、恩人！
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#3",focus=1)]
[name="炎熔"]呃，你怎么跟来了......
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#4",focus=2)]
[name="乌有"]什么话！怎么能抛下恩人自个儿跑路呢！
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#4",focus=1)]
[name="炎熔"]你知道那些东西是什么吗？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]我、我也没见过啊......你看我腿都在打颤......
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#3",focus=1)]
[name="炎熔"]不是某种......炎国特产对吧？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]哪能呢！这些奇形怪状的东西要是满地跑，早就变成轰动全国的大新闻咯！
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]......克洛丝，乌有，听我说。
[name="炎熔"]我“完全记不得”推开那茅屋木门之后发生的事情，等到回过神来，就已经在那园林里听那个......
[Character(name="char_455_nothing_1#6")]
[name="乌有"]煮伞居士。
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]对，听那个煮伞居士说故事了。我对自己是怎么来到这里的一点印象都没有。以及，我也不知道这里是哪里。
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#6",focus=1)]
[name="克洛丝"]大家都一样。
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#6",focus=2)]
[name="乌有"]恩人，有件事儿我倒是能确定，这里不是泥翁镇......
[name="乌有"]虽然我也有几年没去过泥翁镇，但这儿的风土人情未免复古了些，刚才我一路跑过来，连个电缆都没有！
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]那更麻烦了......
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#6",focus=1)]
[name="克洛丝"]就像做梦一样呢。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#6",focus=1)]
[name="克洛丝"]......我知道你在想什么，但是现在，我们没有其他办法，只能信任彼此。
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]呃？恩人！你可别不信我啊！我绝不是那忘恩负义之徒！再说我也没那么大能耐啊！
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]我不是这个意思......
[name="炎熔"]......只是考虑到目前的情况，这一切都太诡异了。
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#3",focus=1)]
[name="克洛丝"]没有不相信小乌有你哦，只是必须冷静下来想想各种各样的可能性。
[name="克洛丝"]大概还是某种陷阱吧，那么眼前这一切是不是真的......都很难说了嘛。
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]恩人呐，别看我长得年轻，风流倜傥，但我年纪多半还是比你大的......
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]源石技艺......也有可能。但难度太大了。是连通到了某个地方？还是干脆给我们施展了幻象......
[Character(name="char_455_nothing_1#3")]
[name="乌有"]二位恩人果然是奇人呐，一般人遇到这种情况，哪能瞬间考虑到这个方向......
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]“一般人”呢。
[name="炎熔"]虽然不知道这里是哪里，但这里的地理情况太过反常......
[name="炎熔"]日月的位置相对固定，住房大都建在靠着黑夜的这一侧，农田和集市则在那边......但本地人似乎完全习以为常，还有刚才那些东西......
[name="炎熔"]我们需要情报。越快越好。
[Dialog]
[stopmusic(fadetime=1.5)]
[delay(time=1)]
[PlaySound(key="$bigbell", volume=1)]
[PlaySound(key="$bigbell", volume=1,delay=1.5)]
[delay(time=3)]
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]钟又响了......？
[Character(name="avg_npc_144#5",name2="char_1011_purgatory_1#4",focus=1)]
[name="克洛丝"]只有在大炎和东国才能听到这种撞钟的声响呢。
[Dialog]
[Character(name="avg_npc_144#1",name2="char_1011_purgatory_1#4")]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_landscape",screenadapt="coverall")]
[Character(name="avg_npc_140#2")]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="粗犷的村民"]钟响了，响了！大家伙儿，没事了！都没事了！
[Dialog]
[Character(name="avg_npc_140#2",name2="avg_npc_140#2")]
[delay(time=1)]
[Character(name="avg_npc_140#2",name2="avg_npc_140#2",focus=2)]
[characteraction(name="right", type="move", xpos=30, fadetime=0.5,block=true)]
[name="警惕的村民"]这么快？
[Character(name="avg_npc_140#2",name2="avg_npc_140#2",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="粗犷的村民"]没见到那些玩意的踪迹啦！我看到那几个外人帮我们赶走了那些怪物！
[Character(name="avg_npc_140#2",name2="avg_npc_140#2",focus=2)]
[characteraction(name="right", type="move", xpos=-30, fadetime=0.5,block=true)]
[name="警惕的村民"]他们竟然不怕那些玩意？
[Character(name="avg_npc_140#2",name2="avg_npc_140#2",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="粗犷的村民"]依我看，我们就该一鼓作气，打到那山里去，斩草除根！动不动就来上一遭，

... (全文7924字符)
```

### level_act16d5_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Character(name="avg_npc_138#4")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Delay(time=1)]
[name="说书人"]原来如此，是替朋友寻找亲人，为此不远万里来到大炎，实在令人钦佩。
[name="说书人"]不过，灰齐山，勾吴城？我可从来没有听说过附近有这样的城市......不过这里离天岳倒是不远。兴许是某座不知名的小山头，也有可能。
[Dialog]
[Character]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#6",focus=2)]
[name="乌有"]呃？天岳......？
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#6",focus=1)]
[name="克洛丝"]麻烦了呀。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......抱歉，请问我们现在在大炎的哪里？
[Character(name="avg_npc_138#4")]
[name="说书人"]此地在婆山地界，名为婆山镇。
[Character(name="char_455_nothing_1#6",name2="char_1011_purgatory_1#1",focus=1)]
[characteraction(name="right", type="move", xpos=30, fadetime=0.5,block=true)]
[name="炎熔"]......？
[Dialog]
[Delay(time=0.51)]
[Character(name="char_455_nothing_1#3",name2="char_1011_purgatory_1#1",focus=1)]
[characteraction(name="left", type="jump", power=20, fadetime=0.5,block=false)]
[name="乌有"]（没听过，绝对没听过！）
[character]
[Dialog]
[Delay(time=1)]
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=1)]
[name="炎熔"]那、那今年的年份是......？
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=2)]
[name="说书人"]今年是景祚七年，如今已过立春，恰逢除夕。
[Character(name="char_455_nothing_1#3",name2="char_1011_purgatory_1#1",focus=1)]
[name="乌有"]......啊？
[Character(name="char_455_nothing_1#3",name2="char_1011_purgatory_1#1",focus=2)]
[characteraction(name="right", type="move", xpos=-30, fadetime=0.5,block=true)]
[name="炎熔"]（小声）景祚？
[Character(name="char_455_nothing_1#3",name2="char_1011_purgatory_1#1",focus=1)]
[characteraction(name="left", type="move", xpos=30, fadetime=0.5,block=true)]
[name="乌有"]（小声）恩人呐，不瞒你说，我历史学得不好，但景祚......起码近几百年，都未曾听过这么个年号啊......
[Character(name="char_455_nothing_1#3",name2="char_1011_purgatory_1#1",focus=2)]
[name="炎熔"]......
[Character(name="char_455_nothing_1#3",name2="char_1011_purgatory_1#1",focus=1)]
[name="乌有"]（小声）咋、咋回事儿啊恩人？难不成咱们这是一推门回到一千年前了？
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#3",focus=1)]
[name="克洛丝"]（小声）一千年前会有这种园林建筑吗？
[Character(name="avg_npc_144#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]（小声）那显然不能！莫非是这位煮伞居士信口开河？可我看他文质彬彬的，不至于吧？
[Dialog]
[Character]
[Delay(time=0.6)]
[Character(name="avg_npc_138#4")]
[name="说书人"]三位英雄，你们帮了忙，就是我的贵客，有什么问题直问便是，大可不用客气。
[Dialog]
[Character]
[Delay(time=1)]
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......能劳烦您给我们讲述一下这里的风土人情吗？实不相瞒，这里并不是我们一开始的目的地，看来是迷了路，有些茫然。
[name="炎熔"]比如......比如就说说这座城镇？
[Character(name="avg_npc_138#4")]
[name="说书人"]啊......婆山镇的来历可就大有说法了。相传七十年前，某个富商家起了一场大火，殃及无数。
[name="说书人"]富商受了惊，打算离开那里，另寻一块风水宝地作为自己颐养天年的地方。
[name="说书人"]在那之后，同镇的人们却在满地灰烬中，找到了一幅古怪的画。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......画？
[Character(name="avg_npc_138#4")]
[name="说书人"]没错。房屋都烧得一干二净，那幅画却安然无恙，掸去灰烬后，完好如初。
[name="说书人"]富商听说了这幅画的事，掏了大价钱重新买了回来，图个辟火消灾的吉利。
[name="说书人"]富商在新居里，越看这画中风水，越觉得中意。便发动上百家仆，去寻找这画卷中描绘的山水宝地——
[name="说书人"]——于是就到了这里，有了这座镇，有了这园林。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......是您的祖辈？
[Character(name="avg_npc_138#4")]
[name="说书人"]非也非也，世事无常。几十年前，富商死后，几个儿子都不学无术，散尽家财。
[name="说书人"]正巧我爹因为某些机缘巧合，有一笔闲钱，这才买下了这座园子，定居于此。
[name="说书人"]之后，因为这附近少有天灾，山川秀美，吸引了不少风流雅士，久而久之，婆山镇就有了今天这般规模。
[Character(name="avg_npc_144#1",name2="char_1011_purgatory_1#1",focus=1)]
[name="克洛丝"]（听上去真奇妙呢。）
[Character(name="avg_npc_144#1",name2="char_1011_purgatory_1#1",focus=2)]
[name="炎熔"]（好像没有什么问题......）
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]那，这天色......？
[Character(name="avg_npc_138#4")]
[name="说书人"]天色？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]呃，就是，白天和黑夜好像混在一起了......
[Character(name="avg_npc_138#4")]
[name="说书人"]我们素来日出而作，日落而息，几位有何疑虑？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]从钟声响起到现在，两个小时......差不多有一个时辰了。太阳的位置从来没有变化过，这是什么原因？
[Character(name="avg_npc_138#1")]
[name="说书人"]太阳？变化？
[name="说书人"]日月悬空，日在东，月在西，千古不易，变换什么位置？
[name="说书人"]嗯？各位怎么露出这副脸色？我说了什么不妥当的话吗？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]欸，恩人，打断一下，打断一下啊。
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=1)]
[name="乌有"]敢问先生明天是不是也会在这里说书？
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=2)]
[name="说书人"]那自然。
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=1)]
[name="乌有"]既然明天如此，那想必昨天也是这一把折扇，一块醒木？
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=2)]
[name="说书人"]赋闲在家，只有收集怪书这一个癖好，只靠说书打发时间。故而每日申时，雷打不动。
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=1)]
[name="乌有"]欸，那这日月恒定不落，“今天明天昨天”，这“一天”，要怎么定义？
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=2)]
[name="说书人"]乌兄真有意思，十二个时辰为一天，这还用问吗？
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=1)]
[name="乌有"]呃......十二时辰，二十四小时，指的不是一昼夜的时间吗？
[Character(name="char_455_nothing_1#6",name2="avg_npc_138#4",focus=2)]
[name="说书人"]噫，奇了怪哉，几位究竟是从何处而来的？十二时辰，指的是从极东日出之地，到极西月出之山之间所需的时间呀？
[name="说书人"]当然，也指这段路途的路段划分，婆山镇自东到西，便是由巳到亥。
[name="说书人"]我听说山外有山，难道鸿洞山外，东升河下，其他的地方不是如此？
[Character(name="char_455_nothing_1#3",name2="avg_npc_138#4",focus=1)]
[name="乌有"]这......光是一个婆山镇就占了这么大地盘，其他地方要是有镇子，不得永无天日啊？
[Character(name="avg_npc_144#1")]
[name="克洛丝"]或者永远是白天，睡觉都睡不好呢，真糟糕。
[Character(name="avg_npc_138#1")]
[name="说书人"]这......这我还真不清楚。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]你从没有离开过镇子吗？这里没有其他游客？
[Character(name="avg_npc_138#4")]
[name="说书人"]从来没有。很少有人来这里，而离开这里的年轻人，也很少回来。
[name="说书人"]不瞒几位，我们如今所知道的“大炎”，也不过是从富商留下的一些藏书中获悉的罢了。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......这里没有遭遇过天灾？
[Character(name="avg_npc_138#4")]
[name="说书人"]同样极少。除了典籍记载，至少我们这三代人，从未见过。
[n

... (全文13506字符)
```

### level_act16d5_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_138#4", fadetime=1)]
[Delay(time=1.2)]
[name="说书人"]——点睛之笔，最是难得。徐夫人苦思冥想，始终缺那最后一笔。
[name="说书人"]徐夫人不敢妄动，却又始终找不到最心仪的念想，心烦意乱，只好上街散心。正巧听见一位屠户吆喝，身旁笼子里，关着一只肥美羽兽。
[name="说书人"]徐夫人盯着那只羽兽看了许久。兴许是意识到了死期将至，这头畜生木然地注视着往来的行人，反而不怎么闹腾。
[name="说书人"]看着看着，徐夫人不由开始想象起来，若自己是那只羽兽，心里，会想着什么。
[name="说书人"]来往的都是无法理解的异类，远离青草与河畔，在这处不属于自己的文明的荒野，孑然一身。
[name="说书人"]命运早已不再是可以被谈论的范畴，只能谋求一场盛大的解脱。
[name="说书人"]单单用无助和麻木是无法形容那种感觉的——徐夫人不由得靠近了几步，羽兽似乎是被这种异想天开的眼神所吸引，也朝徐夫人看了去。
[name="说书人"]就这一刹那，根本不需要什么强烈的技法、稀少的色彩，也根本不需要担忧那位买画贵人的心情。
[name="说书人"]成与败，得与失，徐夫人在这只待宰的羽兽眼里，都找到了答案。
[name="说书人"]她掏钱买下了那只羽兽，在自家院子的小池里养了起来，便立刻提笔点睛，水到渠成，再无半点阻塞。
[name="说书人"]第二天，徐夫人顺利完成了那幅仕女图，得到达官贵人们的盛赞。
[name="说书人"]带着满贯金银回家的路上，徐夫人却始终觉得点睛之笔外，还缺了点什么，怅然若失。
[name="说书人"]直到她推开家门，看见那只在池子里扑水的羽兽，才恍然惊觉。
[name="说书人"]她本以为自己功成名就，跳出案板久矣，殊不知只是换了处水塘，再无自由罢了。
[name="说书人"]如今的徐夫人早已不是那意气风发的年轻女子。
[name="说书人"]提笔数十载，名利双收，但丈夫英年早逝，如今又要处处看他人脸色，又有谁来为她点睛，把她放回她的田野上呢？
[name="说书人"]当晚回到徐府的，只有一车车金银财宝。
[name="说书人"]据说之后有人在姜齐地界见过徐夫人，但无论如何，自此之后，这位被誉为“风华所在”的女画家，就再也没有出现过。
[name="说书人"]直到二十年后，夕城权贵间流传起了一幅据说是徐夫人绝笔的画。
[name="说书人"]世人多以为假，与徐夫人早年作品格格不入，不明所以。画多留白，画中只有一只羽兽，形貌若死。
[name="说书人"]许多品鉴者以为，同样画兽，当时有不少大家画的飞禽走兽，栩栩如生，灵动非凡，仿佛随时能走出画卷。
[name="说书人"]而这只羽兽，生硬异常，毫无生机，故而被认作假画。
[name="说书人"]徐夫人的仰慕者中，有一位名叫归余的人，归余年轻时经商有道，如今又家道中落，散尽家财，前途未卜，最是失意时。
[name="说书人"]归余看见这幅画，看见那羽兽的眼，如遭雷击。梦游似地回到家中，久久不能释然，寝食难安十数日后，下定决心，重整旗鼓。
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=1)]
[name="炎熔"]......
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=2)]
[name="说书人"]......世事无常。
[name="说书人"]兴许只有同为失意人的归余，才能看清徐夫人埋藏在那只面若死灰的羽兽双眼里，生生不息的渴望，以及那“兽囚于画中”的意味吧。
[name="说书人"]生活，生活莫过于此。
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=1)]
[name="炎熔"]......先生果然搜集了许多奇闻轶事，让人大开眼界。
[name="炎熔"]不过，好像大都是关于炎国画家的传说？
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=2)]
[name="说书人"]是了，我的书房里藏书颇丰，也不乏各路野史笔札、志怪小说，但其中大部分确实都与历史上那些赫赫有名的大画家有关。
[name="说书人"]当然了，也有记载一些因为各种原因籍籍无名，被埋没在大炎宏史中的小角色。
[name="说书人"]虽然最终未能崭露头角，却也有对这片大地的惊鸿一瞥，不知被谁记录下来，也不知真假。
[name="说书人"]说起来......炎熔小姐替朋友寻找的那位，也是个画家，对吧？
[name="说书人"]若是师出名门，或是在某地小有名气，指不定能找到些线索。
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_138#4",focus=1)]
[name="炎熔"]嗯......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=2)]
[Background(image="bg_plankroad",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_empty",name2="char_362_Saga#1",fadetime=1)]
[Delay(time=1)]
[name="嵯峨"]施主你看，这里就是小镇的出口啦。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",fadetime=1)]
[Delay(time=0.6)]
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=1)]
[name="乌有"]哦哦！这样的天色，不提灯笼真的是什么都看不见！
[name="乌有"]敢问大师，你去过镇外吗？
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]唔？你们不是从外面来的吗？
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=1)]
[name="乌有"]啊哈哈，我......我当时大醉一场，一觉醒来，就已经跟着伙伴们躺在客栈里嘞。
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]是这样啊。镇西边呢，有座鸿洞山，从这里出去，走个几里山路，就到啦！
[name="嵯峨"]不过鸿洞山常年有奇异鬼物出没，小僧还是不建议你擅自靠近呀！
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=1)]
[name="乌有"]......鬼、鬼物，就是那些怪物吧，大师可知道那些东西的真面貌？
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]能猜到点线索罢了，不敢妄言。小僧一般把那些东西叫做“墨魉”。
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=1)]
[name="乌有"]墨？啊，是因为它们都会变成一滩污水消失吗？果然贴切，真不愧是大师啊！
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]过奖过奖，只是小僧儿时，常听住持爷爷说起“魍魉”的鬼故事，记忆深刻罢了。
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=1)]
[name="乌有"]谦虚谦虚。
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]本地人将墨魉来袭的日子称为“除夕”，得彻夜不眠，躲去求太阳庇护。这倒是和小僧听闻的大炎“除夕夜”有不少差距......
[name="嵯峨"]莫非，这是因为大炎地大物博，各地方风俗各异？
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=1)]
[name="乌有"]没有没有，我那儿也没听说过这么个除夕，那些墨魉我更是前所未见。
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]小僧云游四方，见到墨魉的次数也寥寥无几。来到婆山镇后也是这样......
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=1)]
[name="乌有"]唉！那我们可不是倒了大霉......刚来到这个地方，就遇上了墨魉袭击城镇......幸好没持续多久，不然我可就要交待在这儿了。
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]小僧还以为施主掐指一算便事事皆知了。
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=1)]
[name="乌有"]哪儿能呢，我要有那个能耐，也不至于——
[name="乌有"]——慢着，你说的那些墨魉，平时可会离开鸿洞山？是否会有落单的墨魉偶然靠近？
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]小僧闲来无事便会在镇上溜达，从未见过墨魉靠近，除了上次，那可真是成群结队啊。
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=1)]
[name="乌有"]那是不是意味着，如果看见一只，就意味着有一群？
[Character(name="char_455_nothing_1#6",name2="char_362_Saga#1",focus=2)]
[name="嵯峨"]小僧以为，多半如此。
[stopmusic(fadetime=0.5)]
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#1",focus=1)]
[name="乌有"]那、那咱们最好赶紧跑路......
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#2",focus=2)]
[name="嵯峨"]唔？施主什么意思——啊。
[CameraShake(duration=-1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=false, block=false)]
[Dialog]
[Character(name="char_455_nothing_1#3",name2="char_362_Saga#2")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character(name="avg_npc_144#1",name2="avg_npc_142#2")]
[CameraShake(stop=true)]
[Delay(time=2)]
[Background(image="bg_town",screenadapt="coverall")]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[D

... (全文14390字符)
```

### level_act16d5_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_plankroad",xscale=1,ysclae=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$longmenbat_intro", key="$longmenbat_loop", volume=0.4)]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="avg_npc_140#1",fadetime=0.7)]
[delay(time=1)]
[name="村民"]还有人没离开这儿吗！赶紧去先生那儿躲着！
[name="村民"]往东边走，快！
[Dialog]
[PlaySound(key="$rungeneral", volume=1)] 
[character(fadetime=1)]
[Delay(time=2)]
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]......自从留意到天色之后就意识到，这里真的是越往西边走越靠近黑夜呢......
[Character(name="char_455_nothing_1#6")]
[name="乌有"]这么说的话，我们现在是“从正午走向黄昏”？还挺有诗意诶。
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]......还是不对，这“白天到黑夜”的距离也太短了，我们才走了几步路？
[Character(name="char_362_Saga#1")]
[name="嵯峨"]画卷长短时有变化，各处景象光怪陆离，画中人为自己的天地寻了一份规矩，但说到底，也是假的。这也是在所难免的事情嘛。
[Character(name="char_1011_purgatory_1#5")]
[name="炎熔"]所以我说——等等，什么？
[Character(name="char_362_Saga#2")]
[name="嵯峨"]呃？
[Character(name="char_1011_purgatory_1#5")]
[name="炎熔"]你刚才说——
[Dialog]
[character]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]唔啊啊啊——！
[Character(name="char_1011_purgatory_1#5",name2="char_362_Saga#2",focus=1)]
[name="炎熔"]——！还有人没离开这儿吗！？
[Character(name="char_1011_purgatory_1#5",name2="char_362_Saga#6",focus=2)]
[name="嵯峨"]在这里！
[Dialog]
[character(fadetime=0.5)]
[Character(name="avg_npc_143#2",name2="avg_npc_141#1")]
[delay(time=1)]
[characteraction(name="left", type="jump",power=60, fadetime=0.7,times=3,block=true)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="村民"]救、救命！
[Dialog]
[characteraction(name="left", type="move", xpos=100,fadetime=0.5,block=true)]
[Delay(time=1)]
[character]
[Character(name="char_362_Saga#6")]
[name="嵯峨"]莫怕，小僧来也！
[PlaySound(key="$rungeneral", volume=1)]
[Dialog]
[characteraction(name="middle", type="move",xpos=-200,fadetime=1,block=true)]
[character]
[delay(time=1)]
[Character(name="avg_npc_143#2",name2="avg_npc_141#1")]
[Delay(time=1)]
[characteraction(name="right", type="move",xpos=800,block=true,fadetime=1.5)]
[Character(name="avg_npc_143#2",name2="char_empty")]
[delay(time=1.5)]
[characteraction(name="right", type="move", xpos=-950, fadetime=0.2, block=false)]
[Character(name="avg_npc_143#2", name2="char_362_Saga#6",fadetime=0.2)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.51)]
[name="墨魉"]嘎——
[Dialog]
[characteraction(name="right", type="move",xpos=150, fadetime=1, block=false)]
[Character(name="avg_npc_143#2",name2="char_362_Saga#5")]
[characteraction(name="left", type="move", xpos=-100,ypos=50, fadetime=1, block=true)]
[Character(name="char_empty", name2="char_362_Saga#5",fadetime=0.5)]
[delay(time=2)]
[character]
[Character(name="char_362_Saga#2",fadetime=1,block=true)]
[delay(time=1)]
[name="嵯峨"]唔，果不其然，被斩之后便化作墨渍，怪哉怪哉。
[Dialog]
[character]
[Character(name="char_362_Saga#2", name2="char_455_nothing_1#6",fadetime=1,block=true)]
[PlaySound(key="$rungeneral", volume=1)]
[delay(time=1)]
[Character(name="char_362_Saga#2", name2="char_455_nothing_1#6",focus=2)]
[name="乌有"]大师，好身手哇！
[Dialog]
[Character(name="avg_npc_141#1", name2="char_362_Saga#5",focus=2)]
[name="嵯峨"]莫要掉以轻心，姑娘，你赶紧往东边去！
[Character(name="avg_npc_141#1", name2="char_362_Saga#5",focus=1)]
[name="村民"]好，好！你们也要小心啊！
[Character(name="avg_npc_141#1", name2="char_362_Saga#5")]
[Dialog]
[characteraction(name="left", type="exit", direction="right",block=true,fadetime=1.5)]
[delay(time=1.51)]
[character]
[Character(name="char_362_Saga#5", name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]......似乎还有不少来不及逃走的村民。
[Character(name="char_362_Saga#5", name2="char_1011_purgatory_1#4",focus=1)]
[name="嵯峨"]可能是太过突然，反应不及——
[Dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_143#2",name2="avg_npc_142#1")]
[delay(time=1)]
[characteraction(name="left", type="jump",power=60, fadetime=0.7,times=3,block=true)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="小女孩"]爸爸？妈妈？
[Dialog]
[delay(time=1)]
[Character(name="char_362_Saga#5", name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]那、那边有个孩子！
[Character(name="char_362_Saga#6", name2="char_455_nothing_1#3",focus=1)]
[characteraction(name="left", type="move",xpos=-200, fadetime=0.6,times=3,block=true)]
[name="嵯峨"]不好——快趴下！
[delay(time=0.51)]
[Character(name="char_362_Saga#6", name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]来不及了！
[Dialog]
[character]
[Character(name="avg_npc_143#2",name2="avg_npc_142#1")]
[name="小女孩"]呜呜......呜啊啊......
[Dialog]
[characteraction(name="left", type="move", xpos=100,fadetime=0.7,block=true)]
[Delay(time=0.7)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.04, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.7)]
[characteraction(name="left", type="move", xpos=-400,fadetime=1,block=true)]
[Character(name="char_empty",name2="avg_npc_142#1",fadetime=0.5)]
[delay(time=1)]
[name="小女孩"]啊！
[Dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_142#1",name2="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",enter2="right",fadetime=1)]
[delay(time=1)]
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]唔哦，千钧一发！
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#4",focus=2

... (全文21486字符)
```

### level_act16d5_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_town",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[PlaySound(key="$d_gen_walk_n",delai=0.5, volume=0.5)]
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",fadetime=1)]
[delay(time=1)]
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",focus=1)]
[name="小女孩"]呜呜，呜呜呜......
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#4",focus=2)]
[name="乌有"]小姑娘呀，你看这天色都亮起来了，咱们也走了挺远的了，就快到了，别哭了啊。
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#4",focus=1)]
[name="小女孩"]呜呜......
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#4",focus=2)]
[name="乌有"]哎呀，有哥哥陪着你，可安全了。
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]唉......别哭啦别哭啦，都能看到园子了，马上就到啦。
[Dialog]
[Character]
[delay(time=1)]
[PlayMusic(intro="$corrosion_intro", key="$corrosion_loop", volume=0.4)]
[Character(name="avg_npc_143#2",enter="left",name2="char_empty",fadetime=1)]
[delay(time=1)]
[Character(name="avg_npc_143#2", name2="avg_npc_143#2",enter2="left",fadetime=1.5)]
[delay(time=1.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="墨魉"]嘎啊！
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",focus=1)]
[characteraction(name="left", type="move", xpos=100, fadetime=1.2,block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="小女孩"]咿呀呀——！
[delay(time=1.2)]
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",focus=2)]
[characteraction(name="right", type="move", xpos=100, fadetime=1.2,block=true)]
[name="乌有"]怎、怎么这边也有！不是说它们怕太阳的吗！？
[delay(time=1.2)]
[name="乌有"]来，你......你骑我头上，抓稳了！
[Dialog]
[characteraction(name="right", type="move", xpos=-150, fadetime=0.6,block=true)]
[delay(time=0.6)]
[characteraction(name="right", type="move", ypos=-40, fadetime=0.6,block=true)]
[delay(time=0.6)]
[characteraction(name="left", type="move", xpos=100, fadetime=0.6,block=true)]
[delay(time=0.7)]
[characteraction(name="left", type="jump", ypos=185,power=50,times=1, fadetime=0.6,block=true)]
[delay(time=0.8)]
[characteraction(name="right", type="move", ypos=50, fadetime=0.6,block=false)]
[characteraction(name="left", type="jump", ypos=30,power=30,times=1, fadetime=0.6,block=false)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=1000,fadetime=1.2,block=false)]
[characteraction(name="right",  type="move", xpos=1000,fadetime=1.2,block=false)]
[delay(time=1.7)]
[Dialog]
[Character(name="avg_npc_143#2",enter="left")]
[delay(time=0.7)]
[characteraction(name="middle", type="jump",power=60, fadetime=0.7,times=3,block=true)]
[name="墨魉"]嘎啊！
[Dialog]
[characteraction(name="middle", type="exit",direction="right",fadetime=0.7,block=false)]
[delay(time=1)]
[Character(name="avg_npc_143#2",enter="left",name2="char_empty")]
[characteraction(name="left", type="exit",direction="right",fadetime=0.7,block=false)]
[delay(time=0.51)]
[Character(name="avg_npc_143#2",enter="left",name2="char_empty")]
[characteraction(name="left", type="exit",direction="right",fadetime=0.7,block=false)]
[delay(time=1)]
[Character]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="小女孩"]叔叔！叔叔你跑快点啊！
[Dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="乌有"]别，别揪我头发！眼镜要掉了，要掉了！
[Dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="墨魉"]嘎啊！嘎啊！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="avg_npc_144#3",name2="avg_npc_141#2")]
[Delay(time=1.2)]
[Background(image="bg_town",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.2)]
[Character(name="avg_npc_144#3",name2="avg_npc_141#2",focus=1)]
[name="克洛丝"]......乌有这家伙，跑得倒是真挺快。
[Character(name="avg_npc_144#3",name2="avg_npc_141#2",focus=2)]
[name="村民"]英雄，您在说什么？
[Character(name="avg_npc_144#1",name2="avg_npc_141#2",focus=1)]
[name="克洛丝"]嗯？啊，没什么，你们快去院子里躲着，外面的警戒交给我就好啦。
[Dialog]
[characteraction(name="right", type="exit",direction="right",fadetime=1,block=false)]
[characteraction(name="left", type="move", xpos=200, fadetime=1,block=false)]
[delay(time=1)]
[name="克洛丝"]唔......
[name="克洛丝"]那个体型的小墨魉，似乎比寻常的源石虫要迅速一些......不过好像有点被绕晕了？
[name="克洛丝"]竟然真的跑不过乌有哎......？还有这种事？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="avg_npc_142#1",name2="char_455_nothing_1#3",focus=2)]
[characteraction(name="right", type="move", xpos=-150, fadetime=0.5,block=true)]
[characteraction(name="left", type="move", xpos=100,ypos=215, fadetime=0.5,block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=-1010,fadetime=0.5,block=false)]
[characteraction(name="right",  type="move", xpos=-1010,fadetime=0.5,block=false)]
[delay(time=1)]
[Dialog]
[Background(image="bg_town",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[name="墨魉"]嘎......嘎啊......嘎啊......
[Dialog]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=1000,fadetime=1.5,block=false)]
[characteraction(name="right",  type="move", xpos=1000,fadetime=1.5,block=false)]
[delay(time=1.5)]
[name="乌有"]看招！嘿！喝！呀！
[characteraction(name="left",type="jump",xpos=100,power=40,times=1,fadetime=0.5,block=false)]
[characteraction(name="right",type="jump",xpos=100,power=30,times=1,fadetime=0.5,block=false)]
[Pla

... (全文16598字符)
```

### level_act16d5_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_white",screenadapt="coverall")]
[Character(name="char_362_Saga#4")]
[PlayMusic(key="$midautumn", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Blocker(a=0.7, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="小僧自幼在东国一座寺庙长大，话虽如此，小僧也只是被住持爷爷收养，并非真正的僧侣。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="嵯峨这个名，也只是决意下山入世之际，向住持爷爷求来的名字。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="小僧离开东国后，立志要云游四方。见炎国大好山河，流连忘返，突然忆起年幼时，误闯住持爷爷的阁楼的那一日。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="那里堆着不少杂物，灰尘蒙蒙，不过有一些少见的玩意，惹得小僧心生童趣。其中，以一大幅绘卷，最是让小僧在意，只记得装那绘卷的箱子，比当时的小僧还高。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="之后才偶然得知，那是住持爷爷还似小僧如今这般云游时，一路旅途的见证。而那幅绘卷，长近百米，却并非什么名家大作。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="小僧当时求了住持爷爷半天，才勉为其难地为我摊开了那画卷。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="时隔多少年了呢，直至今日，小僧仍旧忘不了那日落叶随风而下，当时还健朗的住持爷爷在寺庙大院儿里摊开画卷——小僧，小僧从未见过那般壮丽的山河。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="更让小僧至今不明的是，那绘卷绝非什么细腻如真，栩栩如生的寻常“名作”，却真能让人一瞬间身临其境，在深秋时节，感受那盛夏飞瀑的勃勃生机——", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="欸，小僧这“身临其境”，可不是什么形容词。那一瞬间，仿佛真真切切身处画中，如羽兽掠林而去。山峦叠起，卵石盈池，树影婆娑，飞瀑直下，恢弘可闻！", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="不过恍惚间回过神来，小僧又似乎只是被画卷吸引，痴痴望着那绘卷罢了。印象里，小僧甚至还打了些个寒颤，从盛夏山川回到那深秋小院的印象，就更加深刻了。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="住持爷爷告诉小僧，这幅画，是因他在大炎苦潭江上的一场偶遇而来。当时的住持爷爷比小僧如今还要年轻些许，只是个小沙弥，正逢节度使南巡，官道不通，只好泛舟渡江。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="行到江中，千帆竞发，却能远远眺望到一叶孤舟，沿江而下，仿佛不属于这生机勃勃的景象。住持爷爷一时好奇，就跟了上去。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="那叶孤舟不紧不慢，不急不缓。住持爷爷只隔船见了她一眼，好似登天岳前望天顶，云缭雾绕。一时间竟是惊慌失措，险些落水，一呼一吸间，却又被那人救起。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="那位女子风华绝代，一言不发，带着住持爷爷一路沿江而下，直到吠山渡下船，往灰齐山方向走。住持爷爷为报答救命之恩，一路为她生柴做饭，背行囊，砍荆棘，披星戴月。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="女子似乎从不需要睡眠，而住持爷爷每晚睡去，都会梦见一段从未见过的往事。醒来之后，却又沉沉忘记，若有若无。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="如此反复数次，住持爷爷也陷入了长久的思考，两个明明并肩而行的旅人，却像各行陌路一般，深陷在自己的孤独中反思自己。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="直到某天，二人来到一处山川秀丽之地，女子有感而发，驻足眺望，一望就是几个时辰。住持爷爷问她在做什么，她说，在画。在画一幅拙山尽起图。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle(text="住持爷爷忍不住打了个盹，等到赫然惊醒，却发现自己仍在苦潭江上的扁舟之内。根本没有什么吠山渡，也没有那位山上神仙似的女子。唯独眼前多出了一幅绘卷，便是这幅画。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[Subtitle]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Background(image="bg_pawnshop",screenadapt="coverall",fadetime=1)]
[delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]......那位女性叫什么？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]不知。
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]没问过？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]也不敢呐。
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]......
[Character(name="char_362_Saga")]
[name="嵯峨"]再说那如梦似幻，如真似假，兴许是一年半载，又或是弹指一瞬，恍神之间，这上哪儿问去？
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]......
[Character(name="char_362_Saga")]
[name="嵯峨"]小僧游历炎国，有意无意回想起这个故事，细细想来，兴许只是住持爷爷敷衍我而胡乱编的故事罢了。
[name="嵯峨"]不过小僧在炎国四处打听，这幅《拙山尽起图》竟然还小有名气。
[name="嵯峨"]相传是一位约百年前的无名画家所留，曾有皇亲国戚重金求而不得，因此闻名。
[name="嵯峨"]正巧到了灰齐山附近，小僧便突发奇想，想借机去看看是否能找到那画中的奇景......
[name="嵯峨"]哈哈，在山中寻到一处山清水秀之地，反应过来时，就已经身在此处啦。
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]灰齐山上的那栋茅屋，这倒是和我们如出一辙......
[name="炎熔"]......这里会是一场梦吗？
[Character(name="char_362_Saga")]
[name="嵯峨"]如是一场大梦，那对施主来说，小僧便是梦中幻象，那小僧说的话，也就不可信了。
[name="嵯峨"]若是不可信了，炎熔施主又如何判断眼前的景色，是梦非梦？
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]慢点......你要把我绕晕了......
[name="炎熔"]那你知道怎么离开这里吗？
[Character(name="char_362_Saga")]
[name="嵯峨"]小僧云游至今，仍未明白如何主动离开此地。
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]......至今？你在这里呆了多久？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]很久很久啦，细细数来......
[Dialog]
[Character]
[delay(time=1)]
[Character(name="avg_npc_139#5", fadetime=0.5)]
[delay(time=0.7)]
[name="黎"]二位的茶就要凉了，别光顾着说话，品一品茶吧。
[Character(name="char_1011_purgatory_1")]
[name="炎熔"]啊......谢谢。
[name="炎熔"]（呼......）
[Character(name="avg_npc_139#5",name2="char_1011_purgatory_1",focus=2)]
[name="炎熔"]......嗯？说起来，黎小姐，难道也是......？
[Character(name="avg_npc_139#1",name2="char_1011_purgatory_1",focus=1)]
[name="黎"]只是本地的当铺掌柜罢了。
[Character(name="avg_npc_139#4",name2="char_1011_purgatory_1",focus=1)]
[name="黎"]炎熔小姐......我很欣赏你的善良，也很钦佩你从墨魉手下保护镇民的意愿，但有时候，请多考虑一下自己的安危。
[Character(name="avg_npc_139#4",name2="char_1011_purgatory_1",focus=2)]
[name="炎熔"]那些怪物对罗德岛的精锐构不成威胁。
[Character(name="char_362_Saga")]
[name="嵯峨"]此话不假，炎熔施主一身好本领，无需担心！
[Character(name="avg_npc_139#5",name2="char_1011_purgatory_1",focus=1)]
[name="黎"]......若真是如此，也好。
[name="黎"]炎熔小姐，我有一个问题，不知当不当问。
[Character(name="avg_npc_139#5",name2="char_1011_purgatory_1",focus=2)]
[name="炎熔"]问吧，其实不用对我们这么拘谨的......
[Character(name="avg_npc_139#2",name2="char_1011_purgatory_1",focus=1)]
[name="黎"]炎熔小姐，你可端详过水中的月亮？
[name="黎"]无论水中月色会被粼粼波光扯碎成什么模样，待到风平浪静时，它还会是那轮圆月。
[name="黎"]若是因为怜悯那一时闪烁的水中月色，因此湿了鞋，着了凉，是大没有必要的。
[name="黎"]炎熔小姐，你可会为了捞那一轮水中月......费尽心思？
[Character(name="avg_npc_139#5",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]不......应该不会？做这种事儿没什么意义吧？
[name="炎熔"]怎么突然说这个？
[Character(name="avg_npc_139#5",name2="char_1011_purgatory_1#4",focus=1)]
[name="黎"]......我不知炎熔小姐的那轮明月是何模样，也就无法提醒炎熔小姐到底差在何处。不过水中月，终归是水中月罢了。
[n

... (全文13422字符)
```

### level_act16d5_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_white",screenadapt="coverall")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(key="$midautumn", volume=0.4)]
[Subtitle(text="烟雾是城市的血。", x=200, y=370, alignment="center", size=24, delay=0.1, width=900)]
[delay(time=1)]
[Subtitle]
[delay(time=1)]
[Subtitle(text="我曾见过月面的轮廓模糊不见，只留下宛如雕刻似的斑迹工整地留在天上，月色顺着被刺破的边界流入天空，晕染一片。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="我曾见我热爱的家园陷于火海。我被迫翻山越岭，从这头走到那头。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="我见过饥饿的灾民互相蚕食。当鲜血淋漓的厮杀发生时，就在擦肩而过的距离，人可以像无事发生过那样，看着前方，行走。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="我见过那条漫漫长路，我曾疑惑为何所有人都会选择同一条道路，死亡是注定的，我们只是在麻木中殊途同归。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="我见过荒漠与青山绿水，见过因一个踉跄就再也没有爬起来过的朋友，见过父母那只是短短一瞬的想要抛下自己的眼神。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.51)]
[character(name="avg_npc_139#5",fadetime=1.5)]
[delay(time=1.5)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.51)]
[Subtitle(text="——我见过你。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="我认得你。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="你的眼睛。你高高在上的，冰冷的，孤独的眼睛。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="比遭遇天灾袭击，被父母遗弃，在饥饿与垂死边缘挣扎的我还要悲哀，莫大的悲哀。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="你在看我，还是在看你自己？", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="我记得，我这么问过你。", x=200, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_town",screenadapt="coverall")]
[character]
[PlayMusic(intro="$longmenbat_intro", key="$longmenbat_loop", volume=0.4)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_143#1",name2="avg_npc_140#1",focus=2)]
[name="村民"]别过来！别过来！
[Dialog]
[Character(name="avg_npc_143#1",name2="avg_npc_140#1",focus=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="left", type="jump", ypos=50,xpos=200,power=50,times=1, fadetime=0.3,block=true)]
[delay(time=0.51)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="村民"]它、它吃掉了我的手，哈、哈哈，我怎么一点感觉不到疼，我——
[Dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_143#2",name2="avg_npc_141#1",focus=1)]
[name="墨魉"]嘎啊！
[Character(name="avg_npc_143#2",name2="avg_npc_141#1",focus=2)]
[name="村民"]噫——别过来！
[Dialog]
[Character(name="avg_npc_143#2",name2="avg_npc_141#1")]
[delay(time=0.6)]
[PlaySound(key="$e_skill_skulsrshot", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Character(name="char_empty",name2="avg_npc_143#1", fadetime=1,block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=2)]
[character]
[Character(name="avg_npc_141#1",name2="char_empty",fadetime=1,block=true)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="avg_npc_141#1",name2="char_1011_purgatory_1#1",fadetime=0.5)]
[delay(time=1)]
[Character(name="avg_npc_141#1",name2="char_1011_purgatory_1#2",focus=2)]
[name="炎熔"]你没事吧！
[Character(name="avg_npc_141#1",name2="char_1011_purgatory_1#4",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="村民"]你为什么才来！！为什么没有人敲钟！那个守岁的僧人去哪儿了！？
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=30, randomness=60, fadeout=true, block=false)]
[name="村民"]明明是信任你们，才按你们说的去做的，为什么！为什么我丈夫会死！你们要怎么赔，要怎么赔！！
[Character(name="avg_npc_141#1",name2="char_1011_purgatory_1#4",focus=2)]
[name="炎熔"]......先离开这里再说。
[Dialog]
[Character(name="avg_npc_141#1",name2="char_1011_purgatory_1")]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.6)]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_142#1")]
[name="小女孩"]唔啊啊——妈妈，妈妈，你还我妈妈！
[Character(name="avg_npc_143#2")]
[name="墨魉"]嘎啊！
[Dialog]
[musicvolume(volume=0,fadetime=0)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Character(name="avg_npc_143#2",name2="char_455_nothing_1#5")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[Character(name="avg_npc_143#2",name2="char_455_nothing_1#5")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.51)]
[CameraShake(duration=0.3, xstrength=15, ystrength=15,

... (全文23549字符)
```

### level_act16d5_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_indoor",screenadapt="coverall")]
[character(name="char_1011_purgatory_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="炎熔"]唔......
[name="炎熔"]......我睡着了？
[Dialog]
[Delay(time=0.6)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[name="炎熔"]啊，我想起来了......昨天帮忙清点损失，太晚了，回来就睡了......
[name="炎熔"]日出日落真的恢复正常了......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.6)]
[Background(image="bg_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="char_1011_purgatory_1#5",name2="char_empty")]
[Delay(time=0.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="炎熔"]......克洛丝，醒醒！
[Character(name="char_1011_purgatory_1#1",name2="char_empty",focus=2)]
[name="克洛丝"]......呼......
[Character(name="char_1011_purgatory_1#2",name2="char_empty",focus=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="炎熔"]克——洛——丝——！
[Character(name="char_1011_purgatory_1#1",name2="char_empty",focus=2)]
[name="克洛丝"]呼......唔......
[Dialog]
[Delay(time=1)]
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#5",fadetime=1)]
[Delay(time=0.6)]
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#5",focus=2)]
[name="克洛丝"]呼啊......早啊，小炎熔......
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#5",focus=1)]
[name="炎熔"]我每次都想问，你抱着弩怎么还能睡这么舒服？
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#5",focus=2)]
[name="克洛丝"]睡眠......是最重要的嘛......嗯~
[name="克洛丝"]呼——
[name="克洛丝"]好啦，洗把脸去吧。
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#5",focus=1)]
[name="炎熔"]你要是在罗德岛的时候，也能起床这么干脆就好了。
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#1",focus=2)]
[name="克洛丝"]不可能的~休假和工作可不一样哦。
[name="克洛丝"]今天还要帮各位重建......
[Dialog]
[Delay(time=0.7)]
[musicvolume(volume=0,fadetime=1)]
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#3",focus=2)]
[name="克洛丝"]......小炎熔，是不是我睡迷糊了，窗外那是谁？
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#3",focus=1)]
[name="炎熔"]唔？
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#3")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.6)]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolune(volume=0.4,fadetime=1)]
[Delay(time=1.5)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="char_empty",name2="avg_npc_142#2",fadetime=1)]
[Delay(time=2)]
[name="小女孩"]妈妈，妈妈，快过来，要赶不上听书啦！
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_141#2",name2="avg_npc_142#2",fadetime=1)]
[Delay(time=1.2)]
[Character(name="avg_npc_141#2",name2="avg_npc_142#2",focus=1)]
[name="村民"]好，好，你别跑，小心绊着。
[Character(name="avg_npc_141#2",name2="avg_npc_142#2",focus=2)]
[name="小女孩"]没事的！咱们快点！
[Character(name="avg_npc_141#2",name2="avg_npc_142#2")]
[Dialog]
[PlaySound(key="$rungeneral", volume=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[character(fadetime=1)]
[Delay(time=1.5)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#3")]
[Delay(time=0.6)]
[Background(image="bg_indoor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#3",focus=1)]
[name="炎熔"]......
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#3",focus=2)]
[name="克洛丝"]......
[Character(name="char_1011_purgatory_1#5", name2="avg_npc_144#3",focus=1)]
[name="炎熔"]那、那是她妈妈......？她妈妈没事儿？
[Character(name="char_1011_purgatory_1#5", name2="avg_npc_144#4",focus=2)]
[name="克洛丝"]不像吧。
[name="克洛丝"]你看那边的房檐，昨天明明被法术的余波毁掉了。
[Character(name="char_1011_purgatory_1#5", name2="avg_npc_144#4",focus=1)]
[name="炎熔"]......不会吧？
[Dialog]
[Character(name="char_1011_purgatory_1#5", name2="avg_npc_144#4")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.6)]
[musicvolume(volume=0.4,fadetime=1)]
[Background(image="bg_town",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="avg_npc_140#2", name2="char_empty",fadetime=1)]
[Delay(time=1)]
[name="村民甲"]欸，新出锅的米糕啊，芝麻馅儿，倍儿香！
[Character(name="avg_npc_140#2", name2="avg_npc_140#2",fadetime=1)]
[Character(name="avg_npc_140#2", name2="avg_npc_140#2",focus=2)]
[name="村民乙"]卖酒酿——卖桂花酒酿——酒酿来咯——！
[Dialog]
[Delay(time=1)]
[character]
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#3",focus=1)]
[name="炎熔"]......什么情况？
[Character(name="char_1011_purgatory_1#4", name2="avg_npc_144#3",focus=2)]
[name="克洛丝"]嗯......变回去了呢。
[Dialog]
[character]
[playsound(key="$rungeneral",volume=1)]
[Character(name="char_455_nothing_1#3",fadetime=1)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="乌有"]恩、恩人！？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]恩人，你们还记得我吧？对吧？我不是在做噩梦吧？
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]慢点，你在说什么——
[Character(name="char_455_nothing_1#6")]
[name="乌有"]哎呀，您二位还记得我真是太好啦！我和您二位说，我一觉睡醒，这昨天的事情就跟完全没发生过一样，所有东西就都变回去了！
[name="乌有"]什么墨魉袭击，家破人亡，都是假的！我和您说，连小阿然她娘都变出来啦！我的天哪，我差点以为大白天见鬼了——
[name="乌有"]——对了！那个云游僧......嵯峨呢？嵯峨在哪儿？她还好吗？
[Character(name="avg_npc_144#3")]
[name="克洛丝"]没见过她呢——啊，是小阿然。
[Character(name="char_455_nothing_1#4")]
[name="乌有"]欸，小阿然~！
[Character(name="avg_npc_142#2")]
[name="小女孩"]嗯？叔叔是谁呀，怎么知道我的名字？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]恩人！恩人呐！你听听，你听听！
[Character(name="avg_npc_144#1")]
[name="克洛丝"]......小阿然，我们呀是来听煮伞先生说书的，不过怎么这么快就结束啦？
[Character(name="avg_npc_142#2")]
[name="小女孩"]哦，原来

... (全文13042字符)
```

### level_act16d5_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_plankroad",screenadapt="coverall")]
[Character(name="avg_npc_143#2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="墨魉"]嘎啊——！
[Dialog]
[PlaySound(key="$fightgeneral", volume=1)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[PlaySound(key="$fightgeneral", volume=0.6,delay=0.4)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[delay(time=1)]
[Character(fadetime=1)]
[Delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#5", fadetime=1)]
[Delay(time=0.6)]
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#5", focus=1)]
[name="炎熔"]......怎么感觉墨魉变少了？
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#5", focus=2)]
[name="克洛丝"]的确是变少了吧。而且好像也没那么可怕了。
[Character(name="char_455_nothing_1#6")]
[name="乌有"]恩人呐，你说它们会不会也不记得了？
[name="乌有"]日复一日，年复一年，就这么徒劳地袭击村庄......可恨又可悲！
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]这谁知道，它们又不会说人话——
[Character(name="char_455_nothing_1#3")]
[name="乌有"]它们——还真不一定，不会说人话。
[Character(name="char_362_Saga#2")]
[name="嵯峨"]什么？住持爷爷常说当以慈悲为怀，若真是如此，可真是难办......
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]如果这里真的只不过是一幅画......
[name="炎熔"]......那我们也许，已经找对了地方。
[name="炎熔"]早该想到的，年那个家伙，是故意不和我们说这些事情的吧......
[Character(name="avg_npc_144#5")]
[name="克洛丝"]怕我们露出破绽，直接让夕小姐溜走了？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]这么神通广大的一个人，会溜吗？说真的，我都有些怕她了......
[name="炎熔"]先不说具体原理，能在自己创造的小天地里容纳下我们这些活生生的人，这意味着什么？
[name="炎熔"]画中吃喝都和真的一样，不仅如此，画中人还能和我们对答如流，这又意味着什么？
[name="炎熔"]如果靠法术就能做到这一切，那年的这个妹妹——
[Character(name="avg_npc_144#5")]
[name="克洛丝"]......也是啦。虽然见过那么多光怪陆离的源石技艺，但眼前这些东西，还是稍微有些超乎常识了。
[Character(name="char_455_nothing_1#6")]
[name="乌有"]二位恩人要找的人......原来这么厉害？真，真出乎预料啊......
[Character(name="char_362_Saga#1")]
[name="嵯峨"]是吗？可小僧以为，这婆山镇，只能算是小僧游历过的山河中，最朴实无华的一处啦。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......你还去过哪些地方？
[Character(name="char_362_Saga#3")]
[name="嵯峨"]这可大有说头。
[name="嵯峨"]小僧先前，曾见过有人能以酒为剑，破空而去。见过奇人斗法，飞瀑逆流而上。
[name="嵯峨"]见过有人八步成诗，却被迫拖棺面圣，被歹人所害，又如此反复——
[name="嵯峨"]见过那北悬巨石，相传是某位先帝登基时，突然由地面升起的一块滚圆巨石，悬浮半空。
[name="嵯峨"]起初被人当作祥瑞，又因为“如有重负”的说法，被不少人当作噩兆。
[name="嵯峨"]还见过那高山仰止，天灾留下的源石晶簇中，有一棵参天巨松，傲然而立，足以分开云海，眺望天边。
[name="嵯峨"]小僧见过青锋刺棋盘，见过铁锅炖字帖，小僧还见过某位大炎奇人，以一人铸一城，但不知何故，其面目模糊，只可远观，不得近看——
[name="嵯峨"]还有，某位大炎皇帝的异乡知己，向真龙诉说了他一路西去，所见千百座不知存在与否的城市人情。
[name="嵯峨"]那人每每开口，小僧便能看见真切幻影，美不胜收！
[name="嵯峨"]——总之，奇人奇事，数不胜数呀！
[Character(name="char_455_nothing_1#6")]
[name="乌有"]呃，北悬巨石我还真听过，不是很多年前被天灾毁弃的那处风景名胜吗？
[Character(name="char_362_Saga#1")]
[name="嵯峨"]是呀，小僧是亲眼见着它浮起来的——
[Character(name="char_455_nothing_1#3")]
[name="乌有"]那得多少年前的事儿！？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="char_362_Saga#1")]
[Delay(time=1)]
[Background(image="bg_town",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[name="嵯峨"]小僧想先确认一下，各位施主认识的，是那位的姐姐？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]是啊。
[Character(name="char_362_Saga#1")]
[name="嵯峨"]她俩关系......如何？
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#5", focus=1)]
[name="炎熔"]......
[Character(name="char_1011_purgatory_1#1", name2="avg_npc_144#1", focus=2)]
[name="克洛丝"]哦~我觉得你问到点子上了。
[Character(name="char_455_nothing_1#6")]
[name="乌有"]莫非是姐妹不和？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......记得我给你看的那个东西吗？那是年给我的东西，开始我还以为，那是用来让夕相信我们身份的信物......
[Character(name="char_362_Saga#3")]
[name="嵯峨"]哦哦，是那个奇妙物件？那究竟是用来做什么的？
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]不知道......
[Dialog]
[delay(time=1)]
[ShowItem(image="item_act16_1", fadestyle="horiz_expand_center", fadetime=0.5, offsetx=0, width=200)]
[delay(time=1)]
[hideitem]
[delay(time=1)]
[Character(name="char_455_nothing_1#6")]
[name="乌有"]我瞅瞅？啊，这东西是不是也给那说书先生看过？
[Character(name="char_362_Saga#1")]
[name="嵯峨"]哦？煮伞先生也见过这东西？他......他当时如何说的？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]他也说未曾见过。
[Character(name="char_362_Saga#1")]
[name="嵯峨"]......小僧觉得，还是得去找他问问看。
[Character(name="char_455_nothing_1#3")]
[name="乌有"]......呃，我也有一事不明啊......
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]怎么？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]那个，就是，你看，恩人呐，我刚才不是稍微露了两手吗？
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]哦......你是说你和一只墨魉拉开架势，大战了三百回合？
[Character(name="char_455_nothing_1#6")]
[name="乌有"]正是！
[Character(name="char_362_Saga#1")]
[name="嵯峨"]小僧也见到了，为何突然提及此事？
[Character(name="char_455_nothing_1#6")]
[name="乌有"]就......哎，我原本只是个手无缚羽之力的门外汉，突然耍得一手好把式，各位就......不奇怪？
[Character(name="avg_npc_144#5")]
[name="克洛丝"]好把式......？也没有多好吧？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]——咳，咳咳！那个，其实是因为我还藏了两手——啊，但肯定不是因为不想出力，这其中有更深的缘由——
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......所以呢？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]......所以恩人，不怀疑我？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]有什么好奇怪的，你骗得了别人，骗不了我。这点眼力都没有，只会在任务途中给自己惹麻烦。
[Character(name="char_362_Saga#3")]
[name="嵯峨"]小僧也正疑惑！看乌有施主扛着那小娃跑步的样子，疾如闪电，大气不喘，分明就不输小僧寺庙里的那些师兄！
[Character(name="char_455_nothing_1#6")]
[name="乌有"]哈，哈哈，几位别摆出那副表情嘛，我这不是也尽力而为，尽力而为了嘛。
[name="乌有"]对了！天色不早了，我们赶紧去找煮伞先生那个说书人吧！之前不是说他病了吗？得赶紧去瞧瞧情况呀！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Character(name="avg_npc_138#2")]
[Delay(time=2)]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[D

... (全文12055字符)
```

### level_act16d5_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_pawnshop",screenadapt="coverall")]
[Character(name="avg_npc_139",name2="avg_npc_143#2")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.4)]
[delay(time=1)]
[Character(name="avg_npc_139#4",name2="avg_npc_143#2",focus=2)]
[name="墨魉"]......嘎啊。
[Character(name="avg_npc_139#4",name2="avg_npc_143#2",focus=1)]
[name="黎"]墨魉，墨，魉，多好的名字。
[name="黎"]嵯峨那个孩子，是个天生慧根的好苗子。
[name="黎"]一次又一次保护着根本不会受损的器物，那是不是总会有一次，他们放弃了心中的那份正义，对这种徒劳的道德感到麻木呢？
[name="黎"]也许会吧。如果瓷器能够轻松恢复原状，砸碎它就不会感到心疼。
[name="黎"]不，你甚至会爱上砸碎它的感觉。
[Character(name="avg_npc_139#4",name2="avg_npc_143#2",focus=2)]
[name="墨魉"]......嘎？
[Character(name="avg_npc_139",name2="avg_npc_143#2",focus=1)]
[name="黎"]可是，又何必做这么绝呢......人性是经不起考验的。
[Character(name="avg_npc_139",name2="avg_npc_143#2",focus=2)]
[name="墨魉"]......嘎唔......
[Character(name="avg_npc_139#4")]
[name="黎"]你看着这里吗？夕？
[name="黎"]你这么坏心眼......可要原谅我接下来的小心思哦？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Character(name="avg_npc_143#2")]
[Delay(time=2)]
[Background(image="bg_plankroad",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Dialog]
[PlaySound(key="$fightgeneral", volume=1)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[PlaySound(key="$fightgeneral", volume=0.6,delay=0.4)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[PlaySound(key="$e_skill_skulsrsword",volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[delay(time=1)]
[Character(fadetime=1)]
[Delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_1011_purgatory_1#5")]
[name="炎熔"]——呼！
[Character(name="char_455_nothing_1#3")]
[name="乌有"]二位恩人，总算解决啦......！
[name="乌有"]可真不是我泼冷水，继续陪着这些怪物耗下去，咱们何日才能找到离开这里的线索？
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]嵯峨说，她会想办法的。
[Character(name="char_455_nothing_1#3")]
[name="乌有"]那咱们就在这儿日复一日地对付墨魉？这也不是什么好事儿吧......
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......没关系，不费劲。
[name="炎熔"]就当钻研自己的法术了。
[Character(name="avg_npc_144#5")]
[name="克洛丝"]——小炎熔。
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_144#5",focus=1)]
[name="炎熔"]嗯？怎么了？
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_144#4",focus=2)]
[name="克洛丝"]......
[Character(name="char_1011_purgatory_1#4",name2="avg_npc_144#4",focus=1)]
[name="炎熔"]说呀？
[musicvolume(volume=0,fadetime=1)]
[Character(name="char_1011_purgatory_1#4",name2="avg_npc_144#4",focus=2)]
[name="克洛丝"]......你刚才使用的源石技艺，稍微有点危险了。
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_144#4",focus=1)]
[name="炎熔"]......我......？啊......
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_144#4",focus=2)]
[name="克洛丝"]看到了？你烧毁了不少铺子。
[Character(name="avg_npc_144#4",name2="char_455_nothing_1#3",focus=1)]
[name="克洛丝"]还有你啊，小乌有。
[name="克洛丝"]你刚才是不是有刻意对那只冲向镇子的小墨魉视而不见？
[Character(name="avg_npc_144#4",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]我那不是相信恩人一定会处理好的嘛......
[Character(name="avg_npc_144#4",name2="char_455_nothing_1#3",focus=1)]
[name="克洛丝"]不，你想的是，“万一出了什么差错，第二天也会变回原样的”。
[Character(name="avg_npc_144#4",name2="char_455_nothing_1#3",focus=2)]
[name="乌有"]......
[name="乌有"]不......我不会否认......就算我心里有数，但......
[Character(name="avg_npc_144#2")]
[name="克洛丝"]今天是第七天。
[name="克洛丝"]我不是强人所难，守卫没有意义的目标，日复一日，迟早是会变成这样的。
[name="克洛丝"]别忘了在雷姆必拓的那个月......那是场血淋淋的教训。
[name="克洛丝"]战斗是会折磨人心的，我们该时刻警醒一点。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]克洛丝......
[Character(name="char_1011_purgatory_1#1",name2="avg_npc_144#5",focus=2)]
[name="克洛丝"]抱歉......小炎熔，你知道的，我一直......
[Character(name="char_1011_purgatory_1#4",name2="avg_npc_144#5",focus=1)]
[name="炎熔"]好了，我知道。
[name="炎熔"]我们不会有事的，我们会安安稳稳离开这里，安安稳稳回到罗德岛。
[Character(name="char_1011_purgatory_1#4",name2="avg_npc_144#1",focus=2)]
[name="克洛丝"]......
[name="克洛丝"]好~回去之后请我喝哥伦比亚咖啡哦。
[Character(name="char_1011_purgatory_1#3",name2="avg_npc_144#1",focus=1)]
[name="炎熔"]嗯。
[Dialog]
[Character]
[delay(time=2)]
[musicvolume(volume=0.4,fadetime=1)]
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]嵯峨还在房间里？
[Character(name="char_455_nothing_1#2")]
[name="乌有"]我今儿出门前去看过一眼，大师已经枯坐整七天啦......恩人呐，你说要真不吃不喝死在这画里......会真死了吗？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]不知道。当时嵯峨只说“交给我吧”，然后二话不说就关门不出了......
[name="炎熔"]最了解现在情况的人就是嵯峨，我们也别无选择，或者你想像她一样，去其他画卷游览一番？
[Character(name="char_455_nothing_1#2")]
[name="乌有"]不不不不，免了免了。我可不如大师那么坚定，一个不留神，就彻底出不来了。
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......在嵯峨那边有什么结果前，我们也没什么能为她做的。
[Dialog]
[Character]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_139#4",fadetime=1,block=true)]
[delay(time=2)]
[name="黎"]原来你们在这里。
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]黎小姐？你来做什么？
[Character(name="avg_npc_139#1")]
[name="黎"]来提醒你们，莫要偏离本心。
[name="黎"]“假作真时真亦假，无为有处有还无”，我过去这么劝过嵯峨。
[Character(name="avg_npc_139#3")]
[name="黎"]对了，她人呢？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]嵯峨已经在房间里冥想许多日了。
[Character(name="avg_npc_139#3")]
[name="黎"]......啊，她想醒去。
[name="黎"]很少有人能主动从画卷中醒去，不，是从来没有人能够做到。
[name="黎"]不过......说不定呢。
[name="黎"]炎熔小姐，你听说过，“爆竹”这种东西吗？
[name="黎"]在大炎，这是一种古老的民俗，当然，起源于——
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]——驱逐古老的怪物？
[Character(name="avg_npc_139#4")]
[name="黎"]哎呀......炎熔小姐是异乡出身的萨卡兹吧？竟然还会对大炎传统有研究？
[Character(name="char_1011_purgatory_1#1")]
[name="炎熔"]......不是，是我那个朋友......
[Character(name="avg_npc_144#3")]
[name="克洛丝"]啊。我想起来了。
[Character(name="char_1011_pur

... (全文10627字符)
```

### level_act16d5_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Character(name="char_362_Saga#4")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.4)]
[delay(time=1.5)]
[name="嵯峨"]......
[name="嵯峨"]...........
[name="嵯峨"]................
[Dialog]
[Delay(time=1)]
[Subtitle(text="心如止水。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="以你的年纪而言，很少见。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="白光湮没，心思寂灭。万事万物正远离你的躯体。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="最后，平稳的心湖开始重新泛起情感——", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——你感到悲哀？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=2, block=true)]
[Background(image="bg_cottage",screenadapt="coverall")]
[character]
[delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_362_Saga#2",fadetime=1)]
[delay(time=2)]
[name="嵯峨"]先生！莫怪小僧叨扰！
[Character(name="avg_npc_138#3")]
[name="说书人"]大梦终醒......过了多久？
[Character(name="char_362_Saga#1")]
[name="嵯峨"]小僧只见得梅花开了十回，又谢过十次。
[Character(name="avg_npc_138#3")]
[name="说书人"]我若不去提笔，画中天地，亘古不变，何时有花开花谢了？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]实不相瞒，小僧从进入那天岳画卷之后，就始终心算时日，大抵真有这么个岁月。
[Character(name="avg_npc_138#3")]
[name="说书人"]......十年？
[name="说书人"]你在我的画里，待了十年？
[Character(name="char_362_Saga#1")]
[name="嵯峨"]差不离。
[Character(name="avg_npc_138#3")]
[name="说书人"]你一介云游僧，在我这里浪费十年光阴，求个什么，何苦来哉？
[Character(name="char_362_Saga#3")]
[name="嵯峨"]哎呀呀，大梦一场，有吃有喝，还不用为凡俗所扰，更不用躲避天灾，惧怕感染，小僧其实觉得颇为惬意呀。
[Character(name="avg_npc_138#3")]
[name="说书人"]......就算如此，你也一梦......十年。
[name="说书人"]很少有人能在这么漫长的日子里保持初心。有些人，就干脆忘记了自己是谁，永远留在那画卷之上。
[Character(name="char_362_Saga#2")]
[name="嵯峨"]唔哦，当真可怕。
[Character(name="avg_npc_138#3")]
[name="说书人"]可你倒是一点也不害怕。
[Character(name="char_362_Saga#1")]
[name="嵯峨"]先生是个好心肠，一定会在那些人意识弥留之际，点醒他们的吧。
[Character(name="avg_npc_138#3")]
[name="说书人"]哦？何出此言？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]天岳山巅钓鱼翁，不归河畔织布妪，无界原上持戟将，龙门客栈老板娘......再到婆山镇中说书人，先生已经提醒小僧多次了。
[Character(name="char_362_Saga#1")]
[name="嵯峨"]是小僧流连忘返，几次将醒未醒，都将就着蒙混了过去。如此说来，小僧该道歉才是，在画中多养一个活人，想必要耗费不少精力吧？
[Character(name="avg_npc_138#3")]
[name="说书人"]放心，你入山时秋风萧瑟，如今不过入冬而已。发梦一场，片刻罢了。
[Character(name="char_362_Saga#3")]
[name="嵯峨"]哦哦！本来小僧确实担心，会不会在这里懈怠久了挨故人责骂，原来这现世不过短暂时光，心里踏实了许多啊。
[Character(name="avg_npc_138#3")]
[name="说书人"]你在天岳时就意识到了自身处境，明知一切皆为画像，又何必浪费时间？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]因为小僧见夕娥奔月之真相，久久不能释怀......真有狂人靠一己之力，想从天空那里夺回挚爱，如此痴癫，却反倒不让人惋惜......
[Character(name="avg_npc_138#3")]
[name="说书人"]嚯......若是我说，就算夕娥那份神意，也是我刻意而为画上的——也是假的呢？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]各国传说、名著、典籍、神话，有多少是假，多少是与朴素生活无缘之物，那难道我们就要因为一个“假”字，否了它们的意义？
[name="嵯峨"]小僧以为，如此谬矣。
[Character(name="avg_npc_138#3")]
[name="说书人"]真是怪人。
[Character(name="char_362_Saga#1")]
[name="嵯峨"]妙人怪人，一线之差，先生过奖。
[Character(name="avg_npc_138#3")]
[name="说书人"]......呵。
[name="说书人"]和你师傅一个模样，年纪不大，倒是一片赤子之心，心思澄澈。
[name="说书人"]既陪我打发了些许光阴......念在你那师傅的面子上，也好，便允你见我一面吧。
[Character(name="char_362_Saga#2")]
[name="嵯峨"]呃，见面？
[Character(name="avg_npc_138#3")]
[name="说书人"]哈哈，你真以为自己推门而入，便是醒来？
[Character(name="char_362_Saga#2")]
[name="嵯峨"]......！莫非小僧此刻仍在画中？
[Character(name="avg_npc_138#3")]
[name="说书人"]无须惭愧，本该如此。
[name="说书人"]要是真被你随随便便闯破了去，倒是有些不给我面子了。
[name="说书人"]好了。
[name="说书人"]醒去——
[playSound(key="$tactfulboost", volume=1)]
[stopmusic(fadetime=0)]
[Dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[delay(time=2)]
[Subtitle(text="星藏点雪。月隐晦明。", x=500, y=370, alignment="center", size=24, delay=0.1, width=400)]
[delay(time=0.6)]
[subtitle]
[PlayMusic(key="$midautumn", volume=0.4)]
[image(image="avg_ac16_2")]
[imageTween( yFrom=-20, yTo=0, duration=5, ease="InOutSine", block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="夕"]醒了？
[name="嵯峨"]啊......
[name="夕"]起来吧，躺在地上，不像个样子。
[name="嵯峨"]啊......！小僧得令......
[dialog]
[delay(time=1)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(name="char_362_Saga#2")]
[image]
[Background(image="bg_cottage",screenadapt="coverall")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[name="嵯峨"]......
[character]
[dialog]
[Character(name="char_2015_dusk_1#5",fadetime=1,block=true)]
[delay(time=2)]
[name="夕"]怎么了？
[Character(name="char_362_Saga#2")]
[name="嵯峨"]不......小僧......从未想过，原来先生本尊，竟是如此模样......
[Character(name="char_2015_dusk_1#5")]
[name="夕"]呵。
[name="夕"]问吧。
[Character(name="char_362_Saga#2")]
[name="嵯峨"]小僧......小僧......
[Character(name="char_362_Saga#4")]
[name="嵯峨"]小僧本以为走过百余幅画卷，至少得见先生大半阅历，未曾想......不过是先生画海之一隅，不值一提......
[Character(name="char_2015_dusk_1#4")]
[name="夕"]不是没有痴人执迷不悟，最终心甘情愿，死在这里。
[Character(name="char_362_Saga#2")]
[name="嵯峨"]倒是可以理解......
[Character(name="char_2015_dusk_1#5")]
[name="夕"]你想问的不是这个。
[Character(name="char_362_Saga#1")]
[name="嵯峨"]哦，对，小僧一时震惊，把这事儿忘了，见谅见谅。
[name="嵯峨"]先生，小僧曾在住持爷爷的阁楼，见过那副《拙山尽起图》，当时只觉得此中有真意，却答不上个所以然。
[name="嵯峨"]问及住持爷爷，师傅他老人家也只让小僧自己下山去找答案。小僧下了山，云游四方，有了些想法，却又因这世道更加迷茫。
[name="嵯峨"]既然有幸能见到先生本尊，小僧便想——
[Character(name="char_2015_dusk_1#4")]
[name="夕"]你有了些想法，何必再问？
[Character(name="char_362_Saga#1")]
[name="嵯峨"]取长补短，查漏补缺......说实话，小僧还是不解那画中真意，为何点到末尾瀑布时，一笔飞去，留下数寸空白？
[Character(name="char_2015_dusk_1#5")]
[name="夕"]你以为？
[Character(name="char_362_Saga#4")]
[name="嵯峨"]——拙山尽起，便是卷中天地，无限延展之意。末尾一笔飞瀑，直冲天际，只余留白，是以此来描摹那画卷描摹不下的大好河山......
[Character(name="char_2015_dusk_1#4")]
[name="夕"]......
[Character(name="char_362_Saga#1")]
[name="嵯峨"]呃，小僧只是自己瞎琢磨的，先生就别卖关子啦，搞得小僧怪不好意思的。
[Character(name="char_2015_dusk_1#4")]
[name="夕"]如何理解，是看客自己的意思。
[name="夕"]不过，只为了这件事......你就费尽如此

... (全文12298字符)
```

### level_act16d5_10_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[delay(time=1)]
[Subtitle(text="星藏点雪。 月隐晦明。", x=500, y=370, alignment="center", size=24, delay=0.1, width=200)]
[delay(time=0.6)]
[Subtitle]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Background(image="bg_lmstreet_1",fadetime=2, screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="char_455_nothing_1#5",fadetime=1)]
[delay(time=1)]
[name="乌有"]......
[name="乌有"]（这里就是......龙门。）
[name="乌有"]（得赶紧——）
[Dialog]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.6)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="char_455_nothing_1#1")]
[name="乌有"]老伯老伯，留步，留步啊。
[Character(name="avg_npc_034#4")]
[name="？？？"]唔。
[Character(name="char_455_nothing_1#1")]
[name="乌有"]欸，老伯，向您打听个事儿。
[name="乌有"]这附近有没有个叫做董氏鳞丸的摊子？
[Character(name="avg_npc_034#4")]
[name="？？？"]你......不是龙门人吧？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_455_nothing_1#3")]
[name="乌有"]......
[Character(name="avg_npc_034#4")]
[name="？？？"]慕名而来？
[Character(name="char_455_nothing_1#4")]
[name="乌有"]诶，当然是慕名而来的，慕名而来嘛，哈哈哈——
[Character(name="avg_npc_034#4")]
[name="？？？"]现在都几点了，早就收摊啦。
[name="？？？"]你要是真想吃上一口，明天一早八点就得来排队。
[Character(name="char_455_nothing_1#4")]
[name="乌有"]收摊了？那您知道那位董师父住在哪儿吗？
[Character(name="avg_npc_034#4")]
[name="？？？"]唔......
[Character(name="char_455_nothing_1#1")]
[name="乌有"]老伯？
[Character(name="avg_npc_034#4")]
[name="？？？"]只是吃个鳞丸，犯不着知道他姓甚名谁，家住哪儿吧。
[Character(name="char_455_nothing_1#3")]
[name="乌有"]呃......哈哈哈，说的也是，哈哈......那我还是等明儿再说吧——
[stopmusic(fadetime=0)]
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]年轻人。
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]唔——
[name="乌有"]——老、老伯，您这是什么意思？请把手杖挪开——
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]你找姓董的什么事？
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]我、我——
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]我劝你规矩点，年轻人，老实交代吧。
[name="？？？"]你这一晚上问了那么多人，从退休的老家伙到灰尾的堂主你全都要找，最后还要来拜访一个卖鳞鱼丸的......
[name="？？？"]没人会大半夜的来这种地方找他。而且......你拿的东西，我认得。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]——您、您是！？唔！
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]别乱动，年轻人，先答，你还要找谁？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]就这么些人！董阿伯是万不得已才要去拜访的人——！
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]你姓廉？
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]不！不不！您听我说——
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]别动。
[name="？？？"]我可不会看走眼，你是个练家子的......那把廉家阴晴扇，廉子虚是你什么人？
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]——是我师父！
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]她怎么了？
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]师父她......
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="？？？"]怎么了！？
[CameraShake(duration=0.3, xstrength=50, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_455_nothing_1#1",name2="avg_npc_034#4",focus=1)]
[name="乌有"]死了！
[dialog]
[delay(time=1)]
[Character(name="char_455_nothing_1#1",name2="avg_npc_034#4",focus=2)]
[name="？？？"]......怎么死的？
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_455_nothing_1#1",name2="avg_npc_034#4",focus=1)]
[name="乌有"]为了......为了我这个废物徒弟，被人活活害死的！
[Character(name="char_455_nothing_1#1",name2="avg_npc_034#4",focus=2)]
[name="？？？"]......
[name="？？？"]......可惜了。
[dialog]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_455_nothing_1#1",name2="char_empty",fadetime=1)]
[delay(time=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="乌有"]林先生——！
[Character(name="avg_npc_034#4")]
[name="林"]嚯......你知道这个名字，你怎么知道的？
[Character(name="char_455_nothing_1#3")]
[name="乌有"]我、我听师父提起过您......求您了，我还不能被他们抓住！
[Character(name="avg_npc_034#4")]
[name="林"]你躲到龙门来，苟且偷生。
[Character(name="char_455_nothing_1#3")]
[name="乌有"]香火不能断！
[Character(name="avg_npc_034#4")]
[name="林"]你该去近卫局。
[Character(name="char_455_nothing_1#3")]
[name="乌有"]当官的管不了！
[Character(name="avg_npc_034#4")]
[name="林"]......
[name="林"]好......念在姓董的和你师父有旧情，我给你这个机会。
[dialog]
[delay(time=1)]
[PlayMusic(intro="$kingmouse_intro", key="$kingmouse_loop", volume=0.4)]
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="林"]让你三招，断了我这根手杖，你就跟我走。
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]——不，不行！
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="林"]动手。
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=1)]
[name="乌有"]师父说过，龙门的林对姓董的有恩，就是对她有恩，无论什么情况，都不能对他不敬——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_455_nothing_1#3",name2="avg_npc_034#4",focus=2)]
[name="林"

... (全文32801字符)
```

### level_act16d5_10_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=2)]
[PlaySound(key="$tactfulboost", volume=0.6)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0, block=true)]
[Background(image="bg_town",screenadapt="coverall")]
[Delay(time=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[PlayMusic(intro="$mudrock_intro", key="$mudrock_loop", volume=0.4)]
[Delay(time=0.6)]
[PlaySound(key="$tactfulboost", volume=0.7)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0, block=true)]
[Background(image="bg_motorway",screenadapt="coverall")]
[Delay(time=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=0.6)]
[PlaySound(key="$tactfulboost", volume=0.8)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0, block=true)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[Delay(time=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[Delay(time=0.6)]
[PlaySound(key="$tactfulboost", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0, block=true)]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_2014_nian_1#4")]
[name="年"]就因为你这脾气，又不搭理人，又突然生气，总摆着个脸色，也只有你的好姐姐我肯来照顾你咯。
[Character(name="char_2015_dusk_1#3")]
[name="夕"]......
[Character(name="char_2014_nian_1#3")]
[name="年"]你和那写字儿的关系不好，是因为你俩都不肯承认字画同源，和我关系不好，是因为你不肯接受微辣的火锅——
[name="年"]欸，要是你再搬出磐蟹冰淇淋锅这种东西，指不定我就真投降了。
[Character(name="char_2015_dusk_1#2")]
[name="夕"]......嘴倔。
[name="夕"]不是因为你已经没力气了，才说胡话拖延时间的吗？
[Character(name="char_2014_nian_1")]
[name="年"]......哎呀，你这么多年......是真的从来没闭过眼？
[Character(name="char_2015_dusk_1#3")]
[name="夕"]......
[Character(name="char_2014_nian_1#3")]
[name="年"]熬夜工作也许会比小睡一两个小时更清醒，但积攒的疲劳迟早会让你垮掉哦。
[name="年"]啊，我知道了，你是在害怕。
[Character(name="char_2015_dusk_1#2")]
[name="夕"]你......
[Character(name="char_2014_nian_1#4")]
[name="年"]你比谁都清楚自己是什么，你知道自己也不过是个画中人，你怕自己一梦醒来，就不复存在——
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_2015_dusk_1#2")]
[name="夕"]住口！
[Character(name="char_2014_nian_1#4")]
[name="年"]欸，别这么着急。
[name="年"]我们都得正视它，我们谁都逃离不了自我的真相。
[Character(name="char_2015_dusk_1#3")]
[name="夕"]嘁。
[Dialog]
[Character]
[PlaySound(key="$tactfulboost", volume=0.6)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Delay(time=0.6)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[Delay(time=0.6)]
[Character(name="char_2015_dusk_1#2")]
[name="夕"]......你居然会这么感性，是不是睡傻了？
[Character(name="char_2014_nian_1")]
[name="年"]当“我们”苏醒，再次俯视大地的时候，现在的你我都将消失。消失得一干二净。
[name="年"]不仅如此，“我们”会掀起滔天的怒火。在“我们”的关系断绝前，我始终能感觉到屈辱和愤懑......
[name="年"]而我呢，不是特别甘心。
[Character(name="char_2015_dusk_1#2")]
[name="夕"]......你要......反抗它？
[name="夕"]痴人说梦。身体的部分如何反抗整个躯体？
[Character(name="char_2014_nian_1")]
[name="年"]欸，这个例子我好像也用过。
[Character(name="char_2015_dusk_1#2")]
[name="夕"]别油嘴滑舌，已经没时间了——
[Character(name="char_2014_nian_1")]
[name="年"]我知道。所以不止我一个人这么想，在“我们”——不，已经与我们断绝了关系的疯物已经不能称作“我们”了——
[name="年"]——在“它”醒来之前，我们必须做好万全的准备，无论借用什么力量，我们都得这么做。
[name="年"]不为了任何东西，只为了我们自己，以及我们喜欢的事物。
[name="年"]还有，我们兄弟姐妹间......你也感觉到了。有人和我们站在一边的，有人不在乎，但也有人，疯的很彻底。
[Character(name="char_2015_dusk_1#3")]
[name="夕"]......不可能。
[Character(name="char_2014_nian_1#4")]
[name="年"]是吗？你其实心底里有几个怀疑人选吧？
[Character(name="char_2015_dusk_1#3")]
[name="夕"]他们都在真龙身边，又有什么机会......不......也不对......
[Character(name="char_2014_nian_1")]
[name="年"]你总不能比我还糊涂吧，想想看这漫长的历史，他们的影子出现了几次？
[name="年"]时至今日，那些权倾朝野的大官宦，也会派遣信使来往那座小小寺庙的侧殿......我可不瞎。大家都不瞎。
[name="年"]枷锁管得住你吗？那又凭什么管得住别人？
[Character(name="char_2015_dusk_1#3")]
[name="夕"]......
[Character(name="char_2014_nian_1")]
[name="年"]时间确实不多了，不管是谁把我们逼到了这个地步，都不多了。
[name="年"]你还记得，你最后一次安然入眠，是什么时候吗？
[Dialog]
[PlaySound(key="$tactfulboost", volume=0.6)]
[Delay(time=1)]
[CameraShake(duration=2, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n", volume=1)]
[PlaySound(key="$d_gen_explo_n", volume=1,delay=0.05)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Background(image="bg_desert_2",screenadapt="coverall")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_2014_nian_1#4")]
[name="年"]哦哦，好险好险，你也太不爱惜你的作品了吧。这可是你自己的画哎，你哪儿有脸教训我？
[Character(name="char_2015_dusk_1#3")]
[name="夕"]满口胡话......
[Character(name="char_2014_nian_1#4")]
[name="年"]你不承认？
[Character(name="char_2015_dusk_1#5")]
[name="夕"]......倒也未必。你说的话，的确值得我稍作思忖。
[name="夕"]可这些，和你身边的“罗德岛”有什么关联？和你要做的事情有什么关联？
[Character(name="char_2014_nian_1#3")]
[name="年"]去了你就知道了，那可真是个好地方。
[Character(name="char_2015_dusk_1#5")]
[name="夕"]......不少人，已经默默接受了这个既定的命运。
[name="夕"]我们会消失，它会醒来，我们重新成为我，然后死在大炎都城的崩毁声中，鱼死网破。
[name="夕"]这又有什么意义......
[Character(name="char_2014_nian_1#4")]
[name="年"]这么多年，你就想出这么个答案？婆婆妈妈的，那个清高不可一世的夕去哪儿了？
[Character(name="char_2015_dusk_1#3")]
[name="夕"]......
[Character(name="char_2014_nian_1#4")]
[name="年"]罢了罢了，咱们这样打下去，再拆掉几幅画都是停不下来的，嘿咻——
[Character(name="char_2015_dusk_1#2")]
[name="夕"]慢着，你不会又要——
[Character(name="char_2014_nian_1#3")]
[name="年"]啊，这可是最新产品。高八尺宽三尺半，采用泰拉大地前所未有的物质引爆——我心爱的二踢脚！
[Dialog]
[Character]
[Delay(time=1)]
[musicvolume(volume=0,fadetime=0)]
[PlaySound(key="$fireworks", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[delay(time=2)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[CameraShake(duration=3, xstrength=50, ystrength=50, vibrato=60, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_gen_explo_n", volume=1)]
[PlaySound(key="$d_gen_

... (全文17562字符)
```

### level_act16d5_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Character(name="char_455_nothing_1#6")]
[PlayMusic(key="$midautumn", volume=0.4)]
[Subtitle(text="自古以来，道高一尺，魔高一丈，天灾人祸，苦尽苍生。", x=250, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="但，正所谓人定胜天，邪不干正。", x=250, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle(text="豪侠义士，行走四方，路见不平，拔刀相助，试看书林隐处，几多俊逸儒流。", x=250, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Character(name="char_455_nothing_1#4")]
[Subtitle(text="呵！正所谓“美食美酒美景，美人美善美谈”，望自古英雄豪杰，皆一身浩然正气。", x=250, y=370, alignment="center", size=24, delay=0.04, width=900)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="？？？"]嗯，看二位恩人根骨精奇，一身正气，又有一颗行侠仗义的难得心肠，必定是哪处的隐士高人吧？
[name="？？？"]呜呜呜，一定是苍天怜我，命不该绝......一想到那些凶恶畜生，我就气不打一处来！不过是误打误撞冲闯了它们的巢穴，何至于此！
[name="？？？"]幸好有二位贵人相救，我才得以顺利脱身。俗话说得好，大恩不言谢，不如让我为二位恩人算上一卦......聊表敬意，您看如何？
[Dialog]
[Character]
[delay(time=1)]
[stopmusic(fadetime=1)]
[Character(name="char_1011_purgatory_1#4",fadetime=1)]
[delay(time=2)]
[name="炎熔"]......唉。
[Dialog]
[delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4, crossfade=1)]
[name="炎熔"]要不你直接把那本占卜杂志借我看看，正好打发时间......
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]咳哼！啊哈哈，炎熔小姐，这就是您的不对了啊，所谓揭人不揭短，打人不打脸——
[Character(name="char_1011_purgatory_1#5",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]有话直说。
[Character(name="char_1011_purgatory_1#5",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]欸，还是炎熔小姐您慧眼如炬啊！这不是俗话说撑船撑到岸，帮人帮到底嘛。虽然您二位帮我赶走了那些玩意，但不瞒二位说......
[name="？？？"]其实我的行李全丢了。嗯，不光是干粮和盘缠，地图啊、帐篷啊、证件啊、换洗衣服和我心爱的小茶壶......嗯，全丢了。
[name="？？？"]毕竟我的车都沉进湖里了嘛，啊哈哈哈。
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]......你这钓竿扇子不是还在吗，你真的是信使？
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]哈哈，哈，诶，其实其中有些隐情啦......反正骗不过您，那麻烦您就当我是吧。
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]所以你是希望和我们一起走？
[Character(name="char_1011_purgatory_1#4",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]没错！
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]唔......
[Dialog]
[characteraction(name="right", type="move", xpos=50, fadetime=1,block=true)]
[delay(time=1)]
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[characteraction(name="right", type="jump", power=30,times=3, xpos=-100,ypos=-80, fadetime=1,block=true)]
[name="？？？"]呜呜呜，我哪会不知二位有私事在身呢，我也实在是不好意思继续给恩人添麻烦......
[delay(time=0.6)]
[characteraction(name="right", type="move", xpos=100,ypos=80 , fadetime=1,block=true)]
[name="？？？"]只是前路三百里有处村庄，名叫泥翁镇，盛产美玉。那儿有一处驿站，只要坐上那糙椅，喝碗粗茶，打点一番，我就能重整旗鼓，再不麻烦别人！
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]一起走段路倒是没什么啦......不过现在那些钳兽受了不小的刺激，攻击性很强，真要一起走，也得等到它们安静下来再说。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[characteraction(name="right", type="move", xpos=50 , fadetime=1,block=true)]
[name="？？？"]哎呀哎呀，给各位添了麻烦，实在不好意思。
[name="？？？"]不过那位叫克洛丝的恩人怎么还没回来？那些野兽数量不少，真不需要咱俩搭把手？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]你要是真能帮上忙，之前为什么被钳兽撵着跑了这么远？老老实实等着吧。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]可二位救我于水火已是大恩难报，再任由那位恩人独身犯险，我实在于心不忍。
[name="？？？"]不如这样！我这里还有一本健身......不，是独门秘籍，价值不菲，可有效改善身材，就当是给二位的报答！
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]能消停会不？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]得嘞。
[characteraction(name="right", type="move", xpos=-50 , fadetime=1,block=true)]
[name="？？？"]......
[characteraction(name="right", type="move", xpos=50 , fadetime=1,block=true)]
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]......
[characteraction(name="right", type="move", xpos=-50 , fadetime=1,block=true)]
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]......
[characteraction(name="right", type="jump", times=1,power=30 , fadetime=0.6,block=true)]
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]......算了，别这样打量我，你还是想问就问吧。
[characteraction(name="right", type="move", xpos=50 , fadetime=1,block=true)]
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]哎，二位恩人，看打扮，不像是附近村里的人吧？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]不是。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]干脆不是炎国人？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]嗯。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]那是来自哪里？东国？乌萨斯？莫不是更远些的，游历四方的骑士？我听说异邦人总有这种奇怪的传统，真的假的？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]我不是......我......唉。
[name="炎熔"]非要说的话，我是维多利亚人。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]哦......维多利亚呀，嗨，那儿啊，我熟。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]你压根不知道维多利亚在哪儿吧。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=2)]
[name="？？？"]啊哈哈，异国异事，也只有城里的老爷们才会上心嘛，我们这种乡野村夫，想那么多作甚。
[name="？？？"]只是难得看见异乡来客，恩人您一口炎国话说得又挺像那么回事，我这才好奇嘛。
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#6",focus=1)]
[name="炎熔"]（其实大炎话是临阵磨枪的......算了。）
[name="炎熔"]唔，克洛丝回来了。
[Character(name="char_455_nothing_1#4")]
[characteraction(name="right", type="jump",ypos=-20, times=1,power=30 , fadetime=1.2,block=true)]
[name="？？？"]哎哟，克洛丝小姐，克洛丝阁下，辛苦，辛苦了啊，伤着了没

... (全文20878字符)
```

### level_act16d5_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_town",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[PlaySound(key="$d_gen_soldiersrun")]
[Character(name="avg_npc_140")]
[name="村民"]来这儿！往这儿来点，对！
[name="村民"]欸，你帮我把那门钉上，拿稳了！
[Character(name="avg_npc_141")]
[name="村民"]有没有人看见咱家老三，有没有人看见咱家老三呐？
[name="村民"]你、你有没有看见咱们家的老三？
[Character(name="char_362_Saga")]
[name="嵯峨"]抱歉，小僧未曾见过......
[Character(name="avg_npc_141")]
[name="村民"]是这样......
[name="村民"]小余，小余，你在哪儿啊......
[Character(name="char_362_Saga#3")]
[name="嵯峨"]......唉。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.6)]
[PlaySound(key="$d_gen_soldiersrun")]
[Background(image="bg_landscape",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="avg_npc_142")]
[name="小女孩"]......
[Character(name="char_455_nothing_1#4")]
[name="乌有"]欸，叔叔给你买糖吃，好不好？
[Character(name="char_455_nothing_1#4",name2="avg_npc_142",focus=2)]
[name="小女孩"]......
[Character(name="char_455_nothing_1#4",name2="avg_npc_142",focus=1)]
[name="乌有"]叔叔带你看烟花？
[Character(name="char_455_nothing_1#4",name2="avg_npc_142",focus=2)]
[name="小女孩"]......
[Character(name="char_455_nothing_1#2",name2="avg_npc_142",focus=1)]
[name="乌有"]......你妈妈要是在，也不会想看到小阿然不吃不喝的，对不对？
[Character(name="char_455_nothing_1#2",name2="avg_npc_142",focus=2)]
[CameraShake(duration=0.6, xstrength=20, ystrength=20, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="小女孩"]......妈......
[name="小女孩"]妈妈......妈妈啊啊啊......
[Character(name="char_455_nothing_1#2")]
[name="乌有"]唉，哭吧，哭出来，总比闷在心里要好。
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_1011_purgatory_1#1",fadetime=1,block=true)]
[delay(time=1)]
[name="炎熔"]乌有，这孩子？
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#2",focus=2)]
[name="乌有"]恩人......这孩子叫阿然，听说她父亲早早离乡寻工，再也没回来。昨天的事，又不见了母亲，一直恍恍惚惚的，到了今天也不吃不喝呀......
[Character(name="char_1011_purgatory_1#1",name2="char_455_nothing_1#2",focus=1)]
[name="炎熔"]......
[Character(name="char_455_nothing_1#6")]
[name="乌有"]恩人！恩人呐，您可别摆出那副脸色，要不是您和克洛丝二位，这镇上，还不得生灵涂炭啊，俗话说得好......
[Character(name="char_455_nothing_1#2")]
[name="乌有"]......唉，俗话哪管用呢。
[name="乌有"]恩人，我们现在该怎么办？
[Character(name="char_1011_purgatory_1#4")]
[name="炎熔"]......找到黎和那个说书的。
[name="炎熔"]他们明显知道些什么。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_pawnshop",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlayMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Delay(time=1.5)]
[Character(name="avg_npc_139#5")]
[name="黎"]嚯......稀客。
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_138#1",fadetime=1,block=true)]
[delay(time=1)]
[name="说书人"]你认得我了？
[Character(name="avg_npc_139#5")]
[name="黎"]婥园之主，煮伞先生，这婆山镇，谁人不知？
[name="黎"]您这位说书先生，继承了那位大商的园子，可不就是婆山镇的老天爷嘛。
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=1)]
[name="说书人"]......
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=2)]
[name="黎"]先生请坐。
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=1)]
[name="说书人"]......免了。
[Character(name="avg_npc_138#4",name2="avg_npc_139#3",focus=2)]
[name="黎"]这就要走？
[Character(name="avg_npc_138#4",name2="avg_npc_139#3",focus=1)]
[name="说书人"]......
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=2)]
[name="黎"]今日先生倒真是沉默......不过，请先留步。
[name="黎"]平时都是您给大家说书解闷，只收些象征性的茶水钱。
[name="黎"]不如今天，让我来给先生说段故事，而且不收茶钱，白送这碗茶水。不知先生意下如何？
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=1)]
[name="说书人"]......
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=2)]
[name="黎"]今天要讲的故事，可比先生搜罗来的那些志怪小说，要简单得多。
[name="黎"]话说数十年前，大炎东南边陲，有一处名叫婆山镇的镇子......
[Character(name="avg_npc_138#2",name2="avg_npc_139#5",focus=1)]
[name="说书人"]你......
[Character(name="avg_npc_138#2",name2="avg_npc_139#4",focus=2)]
[name="黎"]嗯？
[Character(name="avg_npc_138#4",name2="avg_npc_139#4",focus=1)]
[name="说书人"]不，你继续吧。
[Character(name="avg_npc_138#4",name2="avg_npc_139#5",focus=2)]
[name="黎"]嗯，好。
[Character(name="avg_npc_139#5")]
[name="黎"]这座婆山镇，平平无奇。镇上不过百来户人家，靠山吃山，日子过得朴实。偶尔会有商队路过，那个日子，就是孩子们狂欢的日子。
[Character(name="avg_npc_139#2")]
[name="黎"]而就是这样一个小镇，却在某一日，遭遇了天灾。
[Character(name="avg_npc_139")]
[name="黎"]天灾没有彻底毁了这座小镇，但活性源石污染了水源。大人们想向附近的城邦求援，但镇上没有信使，离开镇子的大人，又全部杳无音讯。
[name="黎"]于是，被迫无奈地，人们抛弃了这座城镇，开始了漫无目的的旅途——
[name="黎"]镇上其实没人知道该去哪里，他们甚至对最近的城市都一无所知，就像听天由命一样，他们选了一个方向。
[name="黎"]对于那些孩子而言，温暖的床榻，曲折的篱笆，墙上风趣的水渍，突然就全部变成了伸手不见五指的夜晚，还有一条......很长的路。
[name="黎"]这条路上，饿死了很多人。
[Character(name="avg_npc_138#4")]
[name="说书人"]......
[Character(name="avg_npc_139#5")]
[name="黎"]有个孩子，她年岁不大，家境贫寒。
[name="黎"]她跟着她的父母走着，看着那些亲密无间的邻里变得少言寡语。
[name="黎"]看着那些一起玩耍的哥哥姐姐，为了半块发霉的烧饼，就用尖锐的石子互相殴打。
[name="黎"]她想，也许事情会好起来的。她也努力了，去找浆果，找小动物，去抓河里的鳞兽。
[name="黎"]她还险些因为抓鳞兽而溺死在河里，也几次因为饥饿而失去意识。
[name="黎"]也许只是造化弄人，也许她身边的至亲突然意识到，这个瘦削的小丫头最后的用处，就是为他们省下一些口粮。
[name="黎"]当她捧着不知能不能入口的山果回“家”时，那儿已经空无一人。
[name="黎"]寒夜峭壁间的兽鸣提醒了她，她的生命一文不值。她在恍惚间仿佛天人感应一般，每寸肌肤都在向她描绘死亡的温度，然后——
[name="黎"]她见到了一个人。一个......奇妙的人。
[Character(name="avg_npc_138#4")]
[name="说书人"]......
[Character(name="avg_npc_138#4",name2="avg_npc_139#4",focus=2)]
[name="黎"]那话怎么说来着？哦......欲知后事如何，且听下回分解。
[Character(name="avg_npc_138#4",name2="avg_npc_139#4",focus=1)]
[name="说书人"]......
[Character(name="avg_npc_138#4",name2="avg_npc_139#4",focus=2)]
[name="黎"]总是在这个时候吊人胃口，真是坏心眼，先生难得像普通人一样尝尝这滋味，感觉如何？
[Dialog]
[character]
[Delay(time=1)]
[Dialog]
[character]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="char_362_Saga#1",fadetime=1,block=true)]
[name="嵯峨"]哦，掌柜的，小僧找你好久啦——
[Character(name="char_362_Saga#1")]
[name="嵯峨"]——唔？先生何故在此？方才一场大难，大伙可都在担心你啊。
[Character(name="avg_npc_138#4")]
[name="说书人"]没什么......只是在这里走走。
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_138#4")]
[name="说书人"]嵯峨。
[Characte

... (全文8931字符)
```

### level_act16d5_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
......秋天了。
山楂该很甜吧。孩子们最喜欢吃山楂了。
......
......又是一天。
我还剩下多久寿命呢？
一闭眼，就会想起很多过去的事情......
......一夜无眠。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[image(image="avg_ac16_4",screenadapt="coverall",fadetime=2)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[name="黎"]......夕？
[name="黎"]你怎么来了......
[name="夕"]你好像一点都不吃惊。
[name="黎"]活到这把岁数，吃惊的情况，就少多啦......咳咳，不过和你说这个，还是小巫见大巫咯。
[name="黎"]我们......有多少年没见过了？
[name="夕"]记不得了，几十年吧。
[name="黎"]......你可是夕。
[name="黎"]你竟然还记得我。
[name="夕"]你怎么知道你不是在我的画里，度过了你这一生？
[name="黎"]不会的。
[name="夕"]你很自信嘛。
[name="黎"]夕，你救过我，我在你的画里生活过那么长的时间......我分得清。
[CameraShake(duration=1, xstrength=0, ystrength=10, vibrato=15, randomness=90, fadeout=true, block=false)]
[name="黎"]咳咳......
[delay(time=1)]
[name="黎"]这是我和你打的赌，赌我有朝一日一眼就能勘破你的画，你的天地，还有你。
[name="黎"]不过那日分别之后，你再也没来见过我呀......我以为我再也没有机会......和你说上话了。
[name="夕"]......能这么和我说话的人，本就不多。
[name="黎"]......这么长时间，我经常回忆起那段日子。那座凉亭......远离了天灾、饥荒、难民的，普通的凉亭。
[name="黎"]就像做梦一样......咳咳。
[name="夕"]我以为，你会是个不错的画家。你却一生没有执笔。岂不是枉费了我一番教诲？
[name="黎"]画家，画家，画之大家，见过你之后，谁还能自称画家？
[name="夕"]难得还是有一些的。都是些......奇人。
[name="黎"]......那我可让你失望了。
[name="夕"]谁知道呢。
[name="夕"]说不定......你才是让我意外的那个。
[name="黎"]......
[name="夕"]......
[name="黎"]时隔多年再见......好像没什么话说。我人老珠黄，走完一生，你呢，却还是那个你。
[name="夕"]你有什么想说的吗？
[name="黎"]没有......我......很安心。
[name="黎"]你救了我，你给了我活下去的机会......现在在我弥留之际，你也来了。
[name="黎"]我很欣慰，夕，看看你......还是这副模样。
[name="夕"]你的眼睛......
[name="黎"]我很老啦，夕，病魔折磨了我许多年......
[name="黎"]现在我倒想问问你......你看着认识的那些人一个个死去，你会感到寂寞吗？
[name="夕"]说什么胡话呢。
[name="黎"]那你会怎么想？
[name="夕"]......偶尔会惋惜。偶尔也会感慨。
[name="黎"]你啊......总算肯说实话了。
[name="黎"]......还记得我和你说过的，我那被天灾毁尽的家乡吗？
[name="黎"]现在回想起来，已经太远太远啦......那儿是我回忆的影子，那儿已经不在我身后，他们在遥远的前方......
[name="夕"]......
[name="黎"]我......我从未自己执笔。
[name="黎"]因为如果我这辈子要画，我只会画，咳咳，我的家乡。
[name="夕"]你明明什么都记不得了。
[name="黎"]是啊，就算去回想，除了“婆山镇”这个名字，我也什么都不记得咯。
[name="黎"]那儿没什么好回忆，但我却总是梦到它。梦到很多个的......故乡。你说，人这一辈子，到底想回去哪儿呢？
[name="夕"]......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[name="黎"]......夕啊。
[name="夕"]嗯？
[name="黎"]你能帮我，画出那婆山镇吗？
[name="黎"]我只记得，家边上，是座当铺。当铺里的账房先生，穿得都很漂亮，文质彬彬。小时候，我想过，我也想当个账房先生。
[name="黎"]村子没有那些古怪的移动地块，农田和瓦舍肆意生长，建在哪儿算哪儿，像油菜花一样......
[name="黎"]要是不小心走远些了，就会看见远处的山......
[name="黎"]那座山......我常常梦见在那里迷路，那里有可怕的怪物......天灾云，从山头那边浮现......这是我记得的最清楚的风景了。
[name="黎"]......不用我多说，你也能感觉得到吧？
[name="夕"]当然，一点不落。
[name="黎"]多想让岁月停在年轻的时候，我们在山上住，我学着你画，偶尔帮你研墨......
[name="夕"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="黎"]夕啊。
[name="夕"]嗯。
[name="黎"]你见过多少奇人异事，看过多少沧海桑田......
[name="黎"]你帮我瞧瞧看，你说我......咳咳。
[name="黎"]你说我这辈子......幸福吗？
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=4, block=true)]
[image]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[Character(name="char_2015_dusk_1#1",fadetime=1,block=true)]
[delay(time=1)]
[name="夕"]......
[Character(name="char_2014_nian_1")]
[name="年"]哟，醒了？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#1",focus=2)]
[name="夕"]......罗德岛。
[name="夕"]我算是明白，你为什么要把我带到这里来了。
[name="夕"]......都是些什么人。
[Character(name="char_2014_nian_1#3",name2="char_2015_dusk_1#1",focus=1)]
[name="年"]打麻将不？三缺一。
[Character(name="char_2014_nian_1#3",name2="char_2015_dusk_1#2",focus=2)]
[name="夕"]你......赶紧滚出去，我是不会去的。
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#2",focus=1)]
[name="年"]哎，你明明兴致勃勃地看了一晚上电影，这会又装凉薄无情了？
[name="年"]喜欢电影也没事，我这儿可有好些收藏。
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#2",focus=2)]
[name="夕"]......你那都是什么，粗制滥造的剪贴封面，毫无意义的长命名，看了就倒胃口，快拿开！
[Character(name="char_2014_nian_1#4",name2="char_2015_dusk_1#2",focus=1)]
[name="年"]你怎么能这么说！
[Character(name="char_2014_nian_1#4",name2="char_2015_dusk_1#5",focus=2)]
[name="夕"]......我看过不少行动档案，这个博士是什么人？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#5",focus=1)]
[name="年"]哦？你偷偷拿的？没给可露希尔发现吧？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#5",focus=2)]
[name="夕"]你说那个年轻的魔族？她没管我，我直接过去了。
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#5",focus=1)]
[name="年"]欸......凭什么......她是不是针对我？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#5",focus=2)]
[name="夕"]......罗德岛。
[name="夕"]监察司和罗德岛是什么关系？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#5",focus=1)]
[name="年"]那是另一件事，没关系，别紧张。惊蛰也是贬谪之身，而且现在基本不来罗德岛了。
[name="年"]这么在乎她？那边是不是有官差找过你麻烦？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#1",focus=2)]
[name="夕"]呵，不在乎这小小的监察司，倒是在乎这雷法出处......她那师父，还有总盯着我们的那些个老家伙，没一个省事的。
[name="夕"]你说我画地为牢？他可是直接烧穿画卷，焚尽眼前江山，非要来教训我一通。我又不是你，也不晓得碍着谁了，就要挨一顿骂。
[name="夕"]我烦他烦得要死，又拿他没有办法。
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#1",focus=1)]
[name="年"]嚯嚯，还发生过这种事？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#2",focus=2)]
[name="夕"]......你还没告诉我，博士和凯尔希是什么人？你待在这里，和这两人有什么关系？
[name="夕"]还有，他们现在在哪里？
[Character(name="char_2014_nian_1",name2="char_2015_dusk_1#1",focus=1)]
[name="年"]......好啊。我都告诉你。
[name="年"]这样你就知道......我为什么喜欢这个地方了。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### training_act16d5_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16d0教学关_a

[PopupDialog(dialogHead="$avatar_lava2")] 呃？那是玫兰莎？玫兰莎为什么在这里？她抵挡不住这么多敌人！
[Tutorial(focusX=240, focusY=100, focusWidth=250, focusHeight=250, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
冷静，冷静...你看那些敌人，着了<@tu.kw>黑白</>二色，那便是<@tu.kw>【晦】【明】</>之分。
[PopupDialog(dialogHead="$avatar_lava2")] 年！？你怎么在这里？
[Tutorial(focusX=-255, focusY=230, focusWidth=80, focusHeight=80, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
再注意看这个地块，称作<@tu.kw>【晦明之印】</>，<@tu.kw>【部署】</>在其中的干员也会获得<@tu.kw>【与其相同】</>的【明】或是【晦】属性




```

### training_act16d5_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16d0教学关_b

[Tutorial(focusX=-255, focusY=240, focusWidth=80, focusHeight=80, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
就像这样，部署在<@tu.kw>【明之印】</>上的米格鲁，也获得了<@tu.kw>【明】</>属性。
[PopupDialog(dialogHead="$avatar_lava2")] 呃，我是不是在做梦......
[PopupDialog(dialogHead="$avatar_nian")] 相由心生，梦不梦，不关键，记住我说的话。你看，因为<@tu.kw>【属性相同】</>，敌人对米格鲁的<@tu.kw>【攻击降低】</>。


```

### training_act16d5_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16d0教学关_c

[Tutorial(focusX=-180, focusY=190, focusWidth=100, focusHeight=100,  \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_nian", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
而<@tu.kw>【晦明相克】</>，如同阴阳本质。部署在<@tu.kw>【晦之印】</>的克洛丝，能以<@tu.kw>【更高的攻击】</>击破<@tu.kw>【明】</>属性的敌人，反之亦然。


```

### training_act16d5_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16d0教学关_d

[PopupDialog(dialogHead="$avatar_lava2")] 又有敌人，这次是，【晦】属性吗......？
[PopupDialog(dialogHead="$avatar_nian")] 没错，<@tu.kw>【同属相惜，异属相克】，【对敌我而言都是如此】</>，哪怕清醒之后，你也要记住了。这可是搞定我那麻烦妹妹的关键。
[PopupDialog(dialogHead="$avatar_lava2")] 慢着，你还能在梦里和人对话的吗！？


```


## 统计

- 总字符数：265913
- 对话行数：2184


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
