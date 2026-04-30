# 明日方舟 · 活动剧情 · act7mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act7mini」完整剧情脚本（6个文件，1869行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act7mini
- 脚本文件数：6

### level_act7mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_1002_nsabr_2",fadetime=1,block=true)]
[Delay(time=1)]
[name="加勒斯"]  小心点，慢点走。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  没事......不用扶我。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  节省体力，我们还得翻过这个山头才行。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  我们离开乌萨斯......多远了？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  没多远，我们还不算深入荒地......还不够深入。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  让我稍微歇一下......
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  没事，我等你。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  ......呼......
[name="依拉"]  东北那座山，翻过去是哪里？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  从那边过去，应该是卡西米尔人的土地。
[name="加勒斯"]  不过我们不去那边。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  ......这是我第一次离开乌萨斯。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  你会习惯的。
[name="加勒斯"]  乌萨斯已经没什么值得留恋的了。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_wild_a",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  呼......这个地方看起来还行。
[name="加勒斯"]  天快黑了，就在这里扎营吧。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  嗯......我们还剩下多少干粮？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  从仓库里带出来的已经吃掉了一大半，算上流民聚落那里换来的，大概还有四天左右的分量......不算多。
[name="加勒斯"]  你看着行李，我去找找柴火。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  这个地方......真是安静。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  安静不是坏事，其他行人反而值得警惕。
[name="加勒斯"]  别看我们一路上都没遇到什么麻烦，这单纯只是运气好。
[name="加勒斯"]  强盗团体和土匪，成群的野兽......
[name="加勒斯"]  荒地对大部分人来说都是个危险致命的地方。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  我们真的能找到那个叫“锈锤”的组织么？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  流民聚落的人没必要骗我们，欺骗我们也没什么意义。
[name="加勒斯"]  锈锤的人在附近有活动，很多人都知道这事。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  ......他们会接纳我们么？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  不确定，但是得试试。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  以前在村子里的时候......当兵的都说“锈锤”是一群残暴野蛮，以杀戮为乐的荒地暴徒。
[name="依拉"]  人们都这么说，后来在队伍里也有人讲过他们......
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  流言不一定是真的，你忘记了那些贵族老爷是怎么说我们的？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  “贪婪，残忍的整合运动强盗。”
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  对于乌萨斯的老爷们来说，只要随便杜撰几句谣言，就足以让他们不喜欢的东西在普通人眼里变成吃人的妖魔。
[name="加勒斯"]  这都是惯用伎俩了，至少我看到的情况肯定不是这样。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  你以前见过他们？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  见过，那还是我当兵时候的事情。
[name="加勒斯"]  那年，就是传说边境守军进入卡西米尔境内劫掠村庄那次。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  啊......我听村子里的人说过这件事。
[name="依拉"]  老队长也说过这件事，好像后来他们都死了？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  老队长还给你讲了这些？
[name="加勒斯"]  他们可是乌萨斯正规军。一支全副武装的正规军小队，带着全套战斗设备穿过边境，这事不可能完全掩人耳目。
[name="加勒斯"]  劫掠只是高级军官推卸责任的说辞，说不定那些士兵是真的想挑起一场战争。
[name="加勒斯"]  但是很遗憾，事情没能如他们所愿。我不知在卡西米尔的山林里发生了什么......但是他们没有一个人回来，大概是全军覆没了。
[name="加勒斯"]  至于他们越过边境的真相......人都死了，谁还在乎。
[name="加勒斯"]  但是他们会死，不完全是因为卡西米尔人......我很清楚。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  所以发生了什么？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  就在那些士兵越过边境的第四天......有哨兵报告说，一大群荒地人进入了乌萨斯的边境。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  荒地人？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  那个时候，我正在边境守备区的补给站驻扎，当哨兵报告了入侵情况后，军营里没人把这件事当回事。
[name="加勒斯"]  一大群走投无路的荒地流民虽然不常见，但也不新鲜，尤其是在乌萨斯边境上。
[name="加勒斯"]  他们派出一支小队，准备拦截这群倒霉蛋，给辖区里的劳工矿场再增加一点劳动力，和他们往常做的事情没什么区别。
[name="加勒斯"]  ......然而......
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  我猜猜，那支小队没有回来？
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  第二天早上，一个满脸是血的卫兵跑到了我们的营区，不止是小队全军覆没，隔壁的三个哨卡也全部失守，只有他活着跑了回来。
[name="加勒斯"]  那时的驻地军官还没有现在这么蠢，他判断是卡西米尔军人伪装成荒地流民袭击了哨卡，于是立刻向上级汇报要求增援。
[name="加勒斯"]  直到这个时候我们才发现，源石通讯器的覆盖范围内已经没有能收到求援信号的友军了，我们孤立无援。然后，就在那天晚上......
[name="加勒斯"]  太阳落山之后，周围的山谷里传来了金属敲打的声音，刺耳可怖，像是原始的战鼓。
[name="加勒斯"]  然后就是人，很多人......上百人......或许是上千人，他们拿着粗制滥造的武器，呼喊着我们根本听不懂的口号，疯狂地冲击我们的营地。
[name="加勒斯"]  他们看起来是人，但是你感受不到他们作为“人”的部分，我以为他们疯了，因为就算是身边的同伴被炮弹炸飞，他们冲锋的脚步也没有停下来半分。
[name="加勒斯"]  那应该是我经历过的最恐怖的冲突，哪怕是后来在整合运动的无数次战斗，都比不上那个疯狂的夜晚。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  ......
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=1)]
[name="加勒斯"]  直到山谷里出现了第一缕阳光，他们才撤退了。
[name="加勒斯"]  无数尸体堆积在营地周围，到处都是血迹和源石法术轰炸的痕迹......整整一天，空气里都弥漫着令人作呕的铁锈味。
[Character(name="char_1002_nsabr_2", name2="char_1011_wizard_1", focus=2)]
[name="依拉"]  ......这也太离谱了。
[name="依拉"]  为什么呢？
[name="依拉"]  如此不计代价地袭击乌萨斯军队？目的是什么？
[Character(name="char_1002_n

... (全文29473字符)
```

### level_act7mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
此处已经不再是你的容身之所。
逃吧，逃吧。战士啊，你那可悲的命运已经定下结局。将不会再留有和你相符的生的职位。
是的，你的生，对我们来说已经毫无意义。
......于是，从不因敌人的鼓声有一次颤抖，从不会因残忍的对手的嘶吼而退却的战士，她逃离此处。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
阿克罗蒂，米诺斯近萨尔贡周边村落地区
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
连日的阴雨使身体健壮的年轻战士也无可避免地病倒。
更何况，这是一位万念俱灰的可怜人。
什么样的经历会使她年纪轻轻便被迫离开家乡？
什么样的过往会使她回头看到自己熟悉的家乡便痛彻心扉？
她不想他人知晓。
逃吧，逃向陌生之地。
然而——
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_482_pallas_1",blackstart=0.3,blackend=0.5,fadetime=1,block=true)]
[Delay(time=2)]
[name="？？？"]  情况如何？
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]  已经在那里挣扎了两个小时了，刚刚安静下来。和我们发现的时候比又向前挪动了十米。
[name="萨卡兹佣兵"]  她若是个称职的间谍，应该保存体力直接装死，而不是一直试图吸引我们的注意。
[name="萨卡兹佣兵"]  也可能是个可怖的诱饵，引诱米诺斯人的善良与同情产生作用，做出一些不顾危险的善意之举。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=2)]
[name="？？？"]  是的，如果是米诺斯人，很难忍受这般良心的煎熬。异乡的战士啊，你对她的举动作何感想？
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=1)]
[name="萨卡兹佣兵"]  哼，诡计。
[name="萨卡兹佣兵"]  要我说，还是诱饵可能性更大。你不是不知道，就是因为萨尔贡人的阴险、狡诈，这些村子这么久以来才......
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=2)]
[name="？？？"]  这是另一码事。我要你看着她，比起揣测和怀疑，更是希望能证明她本人的无辜。
[name="？？？"]  我很感谢你对村民们性命的担忧......
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=1)]
[name="萨卡兹佣兵"]  （冷笑）
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=2)]
[name="？？？"]  ......不管是否出于一份善意。你只需告诉我，萨卡兹的战士啊，来者现在状况到底如何？
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=1)]
[name="萨卡兹佣兵"]  简单来说，生命垂危。
[name="萨卡兹佣兵"]  从装备和武器看，她是一名战士，从萨尔贡那边过来的。现在躺在米诺斯的土地上，像一条离水的鱼进行无谓的挣扎。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=2)]
[name="？？？"]  只有她一人？
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=1)]
[name="萨卡兹佣兵"]  至少目前如此......之后，那可就难说了。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",blackstart2=0.3,blackend2=0.5,focus=2)]
[name="？？？"]  嗯，如果是这样的话......
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]  喂，祭司，“帕拉斯”。
[Dialog]
[Character]
[Character(name="avg_482_pallas_1",fadetime=1,block=true)]
[Delay(time=2)]
[name="帕拉斯"]  怎么了？
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]  出谋划策并不是我的职责，但是米诺斯人把我雇来，又让你来指挥调度我们，所以姑且提醒你一句——
[name="萨卡兹佣兵"]  你可不是普通护士，也并非一个单纯、善良，只知道同情和原谅的傻祭司。
[name="萨卡兹佣兵"]  你是米诺斯人的指挥官，是培养这里的民族战士的指引者，是米诺斯这些村子信仰的什么个“女神”角色。
[name="萨卡兹佣兵"]  你若接纳了她，代表人们都要善待她，为她洗风尘，以像对待你一般的待遇尊重她。毕竟，她是你发现的。
[name="萨卡兹佣兵"]  而现在，这个小战士明明白白的，八九不离十是个萨尔贡人——
[name="萨卡兹佣兵"]  在成功和萨尔贡签订停战协议之前，她都是米诺斯人必须警惕和对抗的敌人。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  ......
[name="帕拉斯"]  战士，你的话蕴含了自己的态度，展现了自己的智慧。出于尊重和职责，我是应当听取的。
[name="帕拉斯"]  但是正如你所想的，我们的判断或许会产生差别。这是令人悲伤，却又必须面对的现实。
[name="帕拉斯"]  我的确在考虑接纳她，至少为她治疗。
[name="帕拉斯"]  她是个年轻的生命，现在命悬一线，不论如何，应该相信她本人对我们无害。
[name="帕拉斯"]  至于她的身后是否潜伏着千百个萨尔贡士兵，这是你应当确认的事情。
[name="帕拉斯"]  既然现在没有危险，我们不能以正在进行的战争为借口放弃救助生命。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  （多管闲事。）
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  或许会有人认为我在多管闲事。这也是我让其他人回去做自己的事，而让你看着她的原因。
[name="帕拉斯"]  萨卡兹人啊，可怜的萨卡兹人。以冷酷无情著称，以此为自己的生存之道，换而言之，你们之中的许多人将冷漠视作自己的骄傲。
[name="帕拉斯"]  让擅长的人去做擅长的事，我遵照着这份准则下达命令。
[name="帕拉斯"]  你只需确保自己的使命达成，其余担忧......自有可以化解的办法。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  既然你只是听了听我的话，又不想改变想法，换谁来看着她不是一样？
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  你在这里做了三个月的雇佣兵了，清楚这里是怎么回事。
[name="帕拉斯"]  如果是米诺斯人，别说两小时，不过十分钟，他们的愧疚便会蛀蚀那纯洁的心，迫使他们无从违抗自己的良心，不顾危险地伸出援助之手......
[name="帕拉斯"]  如果是在这样的场景下，那些背叛真的发生了，村民们那颗赤忱的心该会多么动摇啊。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  哈，说到底，你也承认这些村民就是婆婆妈妈的好心肠，把可能是敌人的命也看得那么重。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  我能够理解你，萨卡兹人。村中的人有些已经认同了你，老人家也将你视如己出，这是善意的接纳。
[name="帕拉斯"]  但是你的需求并不在此。对于爱，至少是我们这些非同族人的爱，和你得到的金钱报酬相比，你并不认为那些有多么无价。 
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  对这些我们没什么好聊的。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  你们有自己的生存之道，这些我无从过问。
[name="帕拉斯"]  但是我能感受到，刚才我所讲述的萨卡兹人的样貌——那或许是你起初的状态。在我们第一次见面时，你的确怀着这般既不纯粹的善，也不彻底邪恶的心。
[name="帕拉斯"]  可现在已经不一样啦。和米诺斯士兵们、村民们的相处，将你改变成了善于思考，根据自己的意识挥动武器的智慧的战士。
[name="帕拉斯"]  你的警惕不无道理。只不过，这一次是我判断，萨尔贡的敌人没有在此时袭击的理由，也没有必要用如此拙劣的手段放出这样一枚“诱饵”。
[name="帕拉斯"]  比起利用善良人心制造出的陷阱，萨尔贡人或许更宁愿就这样大大咧咧地走进来，把烧杀掠夺的残忍企图大声宣告。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  行，行，就当你说的是对的。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  现在，还是把目光转回这位从萨尔贡方向走来的年轻战士身上吧。
[name="帕拉斯"]  正如你所说，我虽然想要救治她......
[name="帕拉斯"]  像你所警告的，贸然将她带回村子不是一件明智的事。
[name="帕拉斯"]  她并没有明显的外伤，至少不是什么必须手术治疗的大病。
[name="帕拉斯"]  我会尝试医治她，至于后果，由我自己承担。
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  你的意思是，让我去给你搬个帐篷来，然后你就在距离边境线不到两公里，甚至比驻军营更远的地方待到把她治好为止？
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=2)]
[name="帕拉斯"]  唔嗯，和在驻军营的区别也不是很大......
[Character(name="avg_npc_053",name2="avg_482_pallas_1",focus=1)]
[name="萨卡兹佣兵"]  你可别忘了自己现在的身份。你是村民们仰赖的对象，带给他们挣脱萨尔贡人束缚的希望。
[name="萨卡兹佣兵"]  他们喜欢你，喜欢叫你“胜利女神”，而你现在却想要这么

... (全文26523字符)
```

### level_act7mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
罗德岛本舰
公共休息区廊道
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_151", fadetime=1,block=true)]
[Delay(time=1)]
[name="贝娜"]  嗯......安妮又跑哪里去玩了......
[Character(name="avg_npc_151#4")]
[name="贝娜"]  都不带我一起玩，哼。
[name="贝娜"]  一会看我怎么收拾她。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_151")]
[name="贝娜"]  唔，走到岔路口了。
[name="贝娜"]  往这里走？还是那里？
[name="贝娜"]  算了，还是用老办法。
[name="贝娜"]  （拿出一枚维多利亚钱币）
[name="贝娜"]  贝娜贝娜迷路啦♪想去哪里就听♪它♪
[name="贝娜"]  巴克莱伊爵士♪指个路吧♪
[Character(name="avg_npc_151#2")]
[name="贝娜"]  嘿！
[name="贝娜"]  （抛出钱币）
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Character(name="avg_npc_151")]
[name="贝娜"]  （捡起钱币）
[name="贝娜"]  往这边走，走到底，嗯嗯，原来如此。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_151", fadetime=1,block=true)]
[Delay(time=1)]
[name="贝娜"]  唉——还有这样的好地方啊，爱丽丝都没和我提过。
[name="贝娜"]  她也没自己说的那么了解罗德岛嘛。
[dialog]
[Character(name="avg_npc_152", fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="贝娜"]  啊，找到了！
[name="贝娜"]  安妮你这个——
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=2)]
[name="安妮"]  （示意贝娜小声）
[Character(name="avg_npc_151#3", name2="avg_npc_152", focus=1)]
[name="贝娜"]  嗯？
[Character(name="avg_npc_151#3", name2="avg_npc_152", focus=2)]
[name="安妮"]  （指了指电视机前的人）
[dialog]
[Character(name="avg_478_kirara_1")]
[Delay(time=1.5)]
[Character(name="avg_npc_151#3", name2="avg_npc_152", focus=1)]
[name="贝娜"]  ？
[name="贝娜"]  （小声）唉，她在干什么？
[Character(name="avg_npc_151#3", name2="avg_npc_152", focus=2)]
[name="安妮"]  玩游戏。
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=1)]
[name="贝娜"]  游戏？游戏不应该是下棋荡秋千堆沙子城堡之类的吗？这个，也是游戏？
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=2)]
[name="安妮"]  嗯。
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=1)]
[name="贝娜"]  唔——
[dialog]
[Character(name="avg_478_kirara_1")]
[Delay(time=3)]
[Character(name="avg_npc_151#5", name2="avg_npc_152", focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="贝娜"]  哇，屏幕上是不是有个黑影子把人拖到小巷里去了？！
[Character(name="avg_npc_151#5", name2="avg_npc_152", focus=2)]
[name="安妮"]  嗯。
[Character(name="avg_npc_151#5", name2="avg_npc_152", focus=1)]
[name="贝娜"]  哎呀要是奶奶知道我们在看这种东西一定会生气的！
[Character(name="avg_npc_151#5", name2="avg_npc_152", focus=2)]
[name="安妮"]  嗯。
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=1)]
[name="贝娜"]  唔唔......
[name="贝娜"]  有点想玩。
[Character(name="avg_npc_151#4", name2="avg_npc_152", focus=2)]
[name="安妮"]  嗯。
[Character(name="avg_npc_151", name2="avg_npc_152", focus=1)]
[name="贝娜"]  啊，我就知道！
[name="贝娜"]  怪不得找不到你。
[name="贝娜"]  那为什么不和这个姐姐谈谈呢？
[Character(name="avg_npc_151", name2="avg_npc_152", focus=2)]
[name="安妮"]  会吓到她的。
[Character(name="avg_npc_151#3", name2="avg_npc_152", focus=1)]
[name="贝娜"]  会吗？
[Character(name="avg_npc_151#3", name2="avg_npc_152", focus=2)]
[name="安妮"]  会的。
[Character(name="avg_npc_151#2", name2="avg_npc_152", focus=1)]
[name="贝娜"]  那就交给我吧。
[name="贝娜"]  毕竟，我玩了就是你玩了嘛。
[Character(name="avg_npc_151#2", name2="avg_npc_152", focus=2)]
[name="安妮"]  嗯。
[name="安妮"]  加油。
[Character(name="avg_npc_151", name2="avg_npc_152", focus=1)]
[name="贝娜"]  唉，安妮，你觉得我这里需要“表演”吗？
[Character(name="avg_npc_151", name2="avg_npc_152", focus=2)]
[name="安妮"]  要。
[Character(name="avg_npc_151", name2="avg_npc_152", focus=1)]
[name="贝娜"]  好，听你的。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Character(name="avg_478_kirara_1", fadetime=1,block=true)]
[Delay(time=2)]
[name="绮良"]  （快到最终篇了，也不知道能不能打出真结局。）
[name="绮良"]  （收集品和分支都按照给出的线索集齐了。）
[Character(name="avg_478_kirara_1#2")]
[name="绮良"]  （最后一步，打过之前的必败战。）
[name="绮良"]  （之前收集结局奖牌的时候试了一下，完全打不过。）
[name="绮良"]  （听说还会转阶段，也不知道能不能行......）
[Character(name="avg_478_kirara_1#4")]
[name="绮良"]  嗯？
[Character(name="avg_npc_151")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="贝娜"]  ~#￥%
[Character(name="avg_478_kirara_1#4")]
[name="绮良"]  （摘下耳机）
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="绮良"]  你，你好，有什么事吗？
[name="绮良"]  （呜哇，我不会应付小孩子啊，怎么办？）
[Character(name="avg_npc_151", name2="avg_478_kirara_1#4", focus=1)]
[name="贝娜"]  大姐姐，你在做什么呀？
[Character(name="avg_npc_151", name2="avg_478_kirara_1#3", focus=2)]
[name="绮良"]  玩......游戏。
[Character(name="avg_npc_151#2", name2="avg_478_kirara_1#3", focus=1)]
[name="贝娜"]  游戏？我也很喜欢玩游戏的！
[name="贝娜"]  我可以一起玩吗？
[Character(name="avg_npc_151#2", name2="avg_478_kirara_1#4", focus=2)]
[name="绮良"]  （现在的小孩子都这么主动吗？！完了，怎么办？）
[name="绮良"]  （她真的会玩吗？就算会玩，现在游戏进度已经很末期了，每个怪都不好打，万一她玩了体验不好手柄一丢走了我会不会很难堪？）
[name="绮良"]  啊，唔，呃，这个......
[Character(name="avg_npc_151#3", name2="avg_478_kirara_1#4", focus=1)]
[name="贝娜"]  姐姐是不方便和别人一起玩吗......
[Character(name="avg_npc_151#3", name2="avg_478_kirara_1#4", focus=2)]
[name="绮良"]  （她，她她她她是不是要哭了？）
[Character(name="avg_npc_151#3", name2

... (全文40583字符)
```

### level_act7mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
2:18 P.M. 天气/晴
伊比利亚以北，临海荒镇
[PlaySound(key="$d_gen_transmissionget", volume=0.6)]
我们已经抵达计划坐标。
目标建筑外观与先行调查报告中的描述一致。
下面小队会进入建筑，做初步查探。稍后可能通讯中断，如有特殊情况，注意信号弹。
蓝毒，通讯完毕。
[PlaySound(key="$transmission", volume=0.6)]
[delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_barracks",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_129_bluep_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="蓝毒"]  这里有个入口。唔，看起来并不是最初的建造者留下的。
[name="蓝毒"]  边缘痕迹很粗糙，像是用利斧硬劈开的。或许是赏金猎人干的？听说他们中的一部分很喜欢来这一带“寻宝”。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  大概因为他们大多不是伊比利亚人......
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  是啊。毕竟，对那些好不容易逃出去的人来说，这种遗迹称得上“毒性”不浅。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  那些留下的人......教会，审判庭。他们也没办法过来。
[name="格劳克斯"]  他们要应付的已经太多了。而且他们也不愿意看到这些。
[name="格劳克斯"]  ......就像我小时候也不想看自己的腿一样。再怎么用力蹬着，它们也没法跑起来——现在的伊比利亚，并不想关注这些“坏掉的部件”。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  小格劳用自己作比喻，我都快要忍不住同情那地方了呢。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  唔，这回我听出来你是在开玩笑了。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Background(image="bg_barracks",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  电磁脉冲力场释放完成。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  那么，往上走，还是往下？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  我听你的。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  我想往上走。不知道为什么，我觉得就该往上。这里就像......一座塔。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  塔？你觉得它有多高？露在地面上的部分最多只有三层。这能派上什么用场？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  这么说的话，我们还是应该往下走。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  嗯？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  你提醒了我。我们还不知道下面有多深。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  那就往下吧。我会跟着你，守住你的背。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  哎呀，小格劳这么说，我放心多了。不过，还是好希望今天能不用打架啊。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_cherunder_2",screenadapt="coverall")]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_129_bluep_1")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="蓝毒"]  唔，好黑。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  照明系统完全坏了。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  连你都修不好吗？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  这是几十年前伊比利亚的技术。和雷神工业的管线设计在思路上就有很大区别。如果给我几天时间的话......
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  那算啦。能不能修好，还是让可露希尔小姐和后面的工程队来考虑吧。我们两个没必要在这地下墓穴憋这么久。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  墓穴？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  一个比喻，又或者不是。这建筑里面弥漫着死气沉沉的味道。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  荒废了几十年，又给海水泡了，在土里埋着......
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  嘘。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  嗯？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  你说，如果我们不说话，会不会听见幽灵的惨叫？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  幽、幽灵......
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  哎呀，骗你的啦。抓我衣服的力道请稍稍轻一些哦，我对这批新衣料还是挺满意的。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  ......啊。还是把便携源石灯打开吧。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  这样就亮多了。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  唔......
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  你对这些技术遗迹真着迷啊。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  这是过去的海边城市才有的科技。现在的伊比利亚，没多少人见过这些了。
[name="格劳克斯"]  它们......是用来做什么的？
[name="格劳克斯"]  瞭望？信号中转？能源产业？或者说......只是观光旅游用的？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  说不定是关押人的地方。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  ......也有可能。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  有些人看往日的伊比利亚，看到的只有遗落的技术，蒙尘的黄金。
[name="蓝毒"]  然而，就在那最辉煌的时代，黄金之城下面，可埋着不少枯骨。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  抱歉......
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  小格劳为什么要道歉？把我的祖先抓到伊比利亚的阿戈尔人，早就给海浪腐蚀得骨头都不剩下了吧。
[name="蓝毒"]  我并不讨厌伊比利亚，也不讨厌阿戈尔人。而且，现在我也没那么讨厌我自己了。除了博士，还有小格劳的功劳啊。
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=1)]
[name="格劳克斯"]  这些技术......会不会让你想起不好的回忆？
[Character(name="avg_326_glacus_1", name2="avg_129_bluep_1", focus=2)]
[name="蓝毒"]  我只关心这地方能不能为罗德岛所用。
[name="蓝毒"

... (全文33041字符)
```

### level_act7mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_068")]
[name="贵族侍从"]  请您在此稍作等待，相关合约稍后将有专人送上。
[name="贵族侍从"]  关于这次合作的相关细节都整理在这里了，还请您带回，令伯爵大人过目。
[name="贵族侍从"]  如果您还有任何问题，随时可以向在下提出......卡涅利安小姐？您在听吗？
[dialog]
[Character(name="avg_426_carnli_1#2", fadetime=1,block=true)]
[Delay(time=1)]
[name="卡涅利安"]  嗯？
[Character(name="avg_426_carnli_1")]
[name="卡涅利安"]  啊......抱歉，一时有点走神。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  ......
[name="贵族侍从"]  那么关于这次的合作，请问，您还有任何疑问吗？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  暂时没什么问题，我会带给霍恩洛厄大人，一切都将由伯爵本人定夺。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  这太好了。相信伯爵大人会做出令我们双方受益的决断。
[name="贵族侍从"]  您接下来便要回程了？若没有什么其他安排，费尔巴哈大人命我送您......
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  送就不必了，还请替我向爵士转达感激之情，感谢他的慷慨。
[name="卡涅利安"]  难得来一趟，之后我还会在城里逛逛，参观一下。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  啊，那么需要为您派一位向导吗？我这就吩咐下去。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  不劳您费心。我自己随意转转就好。
[name="卡涅利安"]  ......说起来，前一次合作时也是由我代表伯爵前来拜访，那还是上一回女皇们宫廷设宴之前吧？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  正是。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  记得那时这里还摆满了异族的犄角作为装饰，现在是换了另一种风格？
[name="卡涅利安"]  唔，比如这件台座摆饰，像这样的质地和光泽可不是常见的货色，我猜猜，莫非这些都是固化源石结晶的精制品？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  您猜的不错。
[name="贵族侍从"]  卡涅利安小姐，不得不说，您比之前要更有眼光了。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  ......过奖了。
[name="卡涅利安"]  据我所知，这一类稳定的结晶，基本只在源石矿脉深处才能挖掘出，而且多半被包裹在源石内部，可以说是有价无市。
[name="卡涅利安"]  而且这种结晶，比岩石还要坚硬得多，一般的雕刻工艺可奈何不了它。
[name="卡涅利安"]  算上加工的难度，想要拿出这么多工艺如此精美的装饰品，费尔巴哈爵士一定也费了不少功夫吧？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  没有您说的那样困难。费尔巴哈大人前阵子勤勉地巡视治下的土地，无意中发现了这些脱胎自源石深处的珍藏。
[name="贵族侍从"]  大人认为，这种黑色的光泽富有意趣且别有一些隐意，十分适合观赏，因此便下令将之装饰在这里，好让前来拜访的客人也能一同赏玩。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  这样看来，我们很该为爵士的慷慨举杯。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  卡涅利安小姐，您好像对此很有了解。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  了解称不上，只是......唔，我曾见过一次这东西的出产过程，个人确实对此有些感慨。
[name="卡涅利安"]  您看，这么一小块固化结晶，想要采掘往往得深入地下百米、千米，一不小心便会失足落下，尸骨无存。
[name="卡涅利安"]  听闻，近期贵领矿区也出了不少事故？这东西啊，就这么一小块，上面凝结的鲜血，说不定就能填满爵士的浴池呢。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  ......
[name="贵族侍从"]  卡涅利安小姐，我想您或许还不太明白......
[Character(name="avg_426_carnli_1#2", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  哦？
[Character(name="avg_426_carnli_1#2", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  在他人看来，这些东西也许确实难得，但于费尔巴哈大人，不过就只是一季的装饰罢了。
[name="贵族侍从"]  费尔巴哈大人不必考虑您说的那些。
[name="贵族侍从"]  大人想要什么，只是一句吩咐的事。我们这些人，便是为此才站在这里。
[Character(name="avg_426_carnli_1#2", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  嚯......
[Character(name="avg_426_carnli_1#2", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  怎么，卡涅利安小姐有不同见解？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  阁下恐怕不会想听我的见解。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  ......恕我直言。您蒙受了伯爵大人天大的恩情，卡涅利安小姐。
[Character(name="avg_426_carnli_1#6", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  唔。
[Character(name="avg_426_carnli_1#6", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  两年前，当得知尚未成年的霍恩洛厄伯爵大人身边，突然多出一个身世未知的外乡人时，大家都对此感到吃惊，这可是从来没有过的事情。
[name="贵族侍从"]  您本应当多顾及伯爵大人的立场及颜面，更加谨慎地行事才是。
[Character(name="avg_426_carnli_1#5", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  您的口气听起来像是对我很不满意。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  请别急着否认，实际上，我见识过不少对我怀有敌意的人，将伯爵也视作贵族中的异类的也大有人在。
[name="卡涅利安"]  如何，我说对了吗？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  ......要整个莱塔尼亚接纳一个外族人，并不是一件容易的事。
[name="贵族侍从"]  但您并不在意那些流言，不是吗。您有相应的才能，也有胆气，我的言语只会是对您的赞誉。
[Character(name="avg_426_carnli_1#7", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  呵呵，狡猾的回答。不过，我姑且就当做夸奖收下了。
[Character(name="avg_426_carnli_1#7", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  至于您方才提到的，矿区的事故......这也无需担忧，卫队和术师团已经有所行动。
[name="贵族侍从"]  您说的不错，现在这样的情况下，我们确实需要更加小心。这件事会被妥善处理，不会成为任何人攻击侯爵大人的把柄。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  原来阁下认为我是在为此担忧？
[name="卡涅利安"]  好吧，就当做是这样。不过，按照我的了解，你们的处理方式或许不怎么和平。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  只是掸去绒毯上的灰尘罢了。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  啊，您想说解决掉所有与此相关的人，也算是解决问题的一种方法？
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  ......
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  好吧，看来我已经说得太多了。是时候告辞了。
[name="卡涅利安"]  容我提醒您，爵士大可以不在意他那些染病的领民，但女皇们可不是什么温和的小羊羔，轻视她们不会有什么好下场。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  啊，不，不不，这您就错了，卡涅利安小姐。我们从没有轻视过女皇们。
[name="贵族侍从"]  女皇们需要权柄，需要更强、更有力的统治，她们要的不仅仅是追随，而是服从。她们已经腾出空来，将目光转向了我们。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  很明白。任何统治者，或许都无可避免会走向这个方向。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  这不令人惊讶，我们互相悉知彼此的想法。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=1)]
[name="卡涅利安"]  阁下看起来很有把握。
[Character(name="avg_426_carnli_1", name2="avg_npc_068", focus=2)]
[name="贵族侍从"]  您会这样惶恐，是因为您没有经历过莱塔尼亚的曾经，卡涅利安小姐。
[name="贵族侍从"]  女皇们，不管是金色的，还是更令人畏惧的黑色的那一位，都难与曾笼罩在莱塔尼亚上方的阴影并论。
[name="贵族侍从"]  尽管那阴影已被她们亲手推翻。
[Character(name="avg_426_carnli_1", name

... (全文31377字符)
```

### level_act7mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
06:50 A.M.  天气/晴
罗德岛本舰，干员宿舍
[PlaySound(key="$rungeneral", volume=0.6)]
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_room_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_173_slchan_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="崖心"]  早上好！
[name="崖心"]  咦，门没锁......那我就打扰啦。
[name="崖心"]  讯使哥！角峰叔！你们在哪呀——
[Character(name="avg_173_slchan_1#2")]
[name="崖心"]  唔，没人在吗？
[Character(name="avg_173_slchan_1")]
[name="崖心"]  按照角峰叔他们的习惯，这个点确实是该起床了才对......不在房间的话，难道是已经出去了？
[name="崖心"]  不行，我得去看看！
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_173_slchan_1",fadetime=0.7)]
[delay(time=2)]
[Character(name="char_198_blackd_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="讯使"]  嗯？恩希亚小姐，这么一大早什么事......等等，别在走廊里这样跑，太危险了！
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Character(name="avg_173_slchan_1")]
[name="崖心"]  啊！发现讯使哥了！
[name="崖心"]  放心，不会有事的啦——呜哇！
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#2",focus=1)]
[name="讯使"]  哎，小心！
[dialog]
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#2",focus=2)]
[characteraction(name="right", type="jump", power=20, fadetime=0.5,block=false)]
[delay(time=1)]
[delay(time=1)]
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#2",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="崖心"]  呼......好险，好险，这里怎么会有一个包裹啊？
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#5",focus=2)]
[name="崖心"]  谢谢啦，讯使哥。
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#5",focus=1)]
[name="讯使"]  真是的，都说了要小心了，万一真的摔倒了该怎么办？
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=2)]
[name="崖心"]  嘿嘿，我就知道讯使哥你一定能接住我嘛。
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=1)]
[name="讯使"]  唉。恩希亚小姐都成为干员了，怎么还是冒冒失失的......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_199_yak_1#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="角峰"]  怎么了，讯使，发生了什么事？
[Character(name="char_198_blackd_1",name2="char_199_yak_1#3",focus=1)]
[name="讯使"]  角峰大哥。
[Character(name="avg_173_slchan_1",name2="char_199_yak_1#3",focus=1)]
[name="崖心"]  早啊，角峰叔！
[Character(name="avg_173_slchan_1",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]  是二小姐啊，早上好。
[name="角峰"]  最近在罗德岛的生活还习惯吗？难得二小姐会这么早起......是准备出任务吗？
[Character(name="char_198_blackd_1",name2="char_199_yak_1#5",focus=1)]
[name="讯使"]  也有可能单纯是不习惯这里的床？毕竟恩希亚小姐对睡眠环境的质量要求很高啊。
[name="讯使"]  老宅里恩希亚小姐的床，还是很小的时候角峰大哥帮着挑的吧？那之后小姐一直不肯更换......还非要抱着自己的小毯子才肯睡呢。
[Character(name="char_198_blackd_1",name2="char_199_yak_1#4",focus=2)]
[name="角峰"]  唔，这倒也是......
[Character(name="avg_173_slchan_1#2",name2="char_199_yak_1#4",focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="崖心"]  等、等下，讯使哥不要乱说， 我才没有那么娇气啦！
[Character(name="avg_173_slchan_1#4",name2="char_199_yak_1#4",focus=1)]
[name="崖心"]  不要小看冒险家哦？早睡早起而已，我还是做得到的！在山上要是因为睡不着而没法补充体力，可没法成为优秀的登山者！
[name="崖心"]  就算是再冷、再空气稀薄的环境，我也是能睡着的！
[Character(name="avg_173_slchan_1#4",name2="char_199_yak_1#5",focus=2)]
[name="角峰"]  恩希亚小姐......真的长大了啊。
[Character(name="avg_173_slchan_1",name2="char_199_yak_1#5",focus=1)]
[name="崖心"]  （小声）而且，我的毯子也好好地带过来了，才不会睡不着呢。
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=1)]
[name="讯使"]  啊，结果还是带来了啊。
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#2",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="崖心"]  有什么关系嘛！
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=2)]
[name="崖心"]  好了好了，不说这个了！
[name="崖心"]  讯使哥和角峰叔这么早就出门，还带着包裹，接下来是要出任务？
[name="崖心"]  唔，看这个行李的量，应该不是短程的......是不是还要回老家那边？
[Character(name="avg_173_slchan_1",name2="char_199_yak_1",focus=2)]
[name="角峰"]  是啊，一会就要准备出发了。
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=1)]
[name="讯使"]  是哦，有些东西要送回去一趟。银灰老爷那里也有不少事情要处理，我和角峰大哥都得回去帮忙。
[name="讯使"]  恩希亚小姐是有什么东西要交给我们带给银灰老爷吗？我和角峰大哥很乐意效劳哦。
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=2)]
[name="崖心"]  嗯，虽然也确实有东西想给老哥啦，但是......但这次不止是这个！
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1",focus=1)]
[name="讯使"]  不止......？
[Character(name="char_198_blackd_1",name2="avg_173_slchan_1#3",focus=2)]
[name="崖心"]  就是，呃。
[name="崖心"]  啊呀，讯使哥，你来一下......！
[Character(name="avg_173_slchan_1",name2="char_199_yak_1#3",focus=1)]
[name="崖心"]  角峰叔我们一会食堂集合，我和讯使哥先走一步！之后替我向老哥和灵知哥问个好！
[delay(time=0.5)]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="left", type="move", xpos=-300, fadetime=1,block=false)]
[Character(name="char_empty", name2="char_199_yak_1#3", focus=1)]
[dialog]
[delay(time=2)]
[Character(fadetime=0.6)]
[Character(name="char_198_blackd_1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="讯使"]  哎，等等，恩希亚小姐，轻点，衣服要被拉下来了......！
[Character(name="char_198_blackd_1")]
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=0.6)]
[characteraction(name="middle", type="move", xpos

... (全文27346字符)
```


## 统计

- 总字符数：188343
- 对话行数：1869


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
