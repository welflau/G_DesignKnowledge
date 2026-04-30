# 明日方舟 · 活动剧情 · act4d0（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act4d0」完整剧情脚本（7个文件，1446行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act4d0
- 脚本文件数：7

### level_act4d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.8,crossfade=1)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_cher_0",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_9", screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_cher_6", screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_013_riop",fadetime=2,block=true)]
[Delay(time=2)]
[name="近卫干员"]   唔......
[name="近卫干员"]   啊？怎，怎么回事......
[name="近卫干员"]   我怎么会躺在这种地方......发生了什么......
[name="近卫干员"]   对了！我们潜入切尔诺伯格，要救出Dr.{@nickname}——
[name="近卫干员"]   ！
[CameraShake(duration=0.4, xstrength=8, ystrength=8, vibrato=30, randomness=30, fadeout=true, block=true)]
[name="近卫干员"]   头儿！不对，不对，头儿他......
[name="近卫干员"]   ......头儿他......
[Dialog]
[Delay(time=0.5)]
[name="近卫干员"]   嗯？这张纸是怎么回事？
[name="近卫干员"]   等等，这是......这是罗德岛的工程用纸！
[name="近卫干员"]   是谁留在这的，究竟发生了什么事？
[name="近卫干员"]   呃，这密密麻麻的字，写的还有些乱......
[Character]
不知名的干员，隐藏好自己。我没有机会看你的胸牌，不记得你的名字。
时间并不宽裕，我的字有些潦草，请谅解，麻烦你读下去。
不用慌张，你暂时是安全的。
请务必不要走出这块废墟。天色完全暗下来之前，敌人发现你的概率很高。
可以说，你正身处敌人的重重包围之中。
[Character(name="char_013_riop")]
[name="近卫干员"]   不是头儿的笔迹......是罗德岛同事写下的纸条吗？
[name="近卫干员"]   写的真长啊，为什么不直接把我叫醒，跟我说就好——
[Dialog]
[Character]
[name="？？？"]   你来了。
[Dialog]
[Character]
[Character(name="char_013_riop")]
[name="近卫干员"]   （嗯？说话声？是整合运动吗，混账！）
[name="近卫干员"]   （......不，等等，这个声音有些耳熟？好像是那个诊所的——）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_188_helage_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="赫拉格"]   所以，你们真的瘫痪了整座切尔诺伯格。我不知道该不该祝贺你。
[Character(name="avg_npc_025_1#2")]
[name="？？？"]   ——
[Character(name="char_188_helage_1")]
[name="赫拉格"]   我们居然都染上了矿石病。
[Character(name="avg_npc_025_1#2")]
[name="？？？"]   真的是您。
[name="？？？"]   我以为，只是传言。
[Character(name="char_188_helage_1")]
[name="赫拉格"]   许多年没见了，博卓卡斯替。
[name="赫拉格"]   我是不是该称呼现在的你，“爱国者”？
[Dialog]
[Character]
[Character(name="avg_npc_025_1",fadetime=2,block=true)]
[Delay(time=2)]
[name="爱国者"]   ......将军。
[name="爱国者"]   您居然，记得我。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   如果不是你带着盾卫顶着暴风雪冲进堡垒，我，巴克莱，还有谢苗，全部要死在卡西米尔的银枪皮加索斯手里。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   是我的战士们，勇敢。他们，不在乎牺牲。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   怎么？你说话的方式，和几十年前大不相同了。
[name="赫拉格"]   我见过你在士兵面前慷慨陈词，能让秃头屠夫巴克莱都为你拍手叫好，可不是件简单事。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   感染，改变了声带。现在，我很难，连续说话。很可笑。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   ——
[name="赫拉格"]   还有你现在的身份。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   是吗。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   北原的游击队......领队居然是你。我原以为十几个温迪戈里，最不可能的就是你。
[name="赫拉格"]   蓝胡子阿廖沙，那个骑兵师的，他曾经和我打赌说你会作为一个天生的乌萨斯军人做到元帅。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   我只是个大尉，将军。时代不同了。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   ......笑话。你的忠诚，军功，还有在作战会议上的规划......你是乌萨斯最出色的战地指挥官之一。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   您过誉了。而且，我是个萨卡兹，终归。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   如果你都当不上校官，几乎所有的乌萨斯高级将领都该被送进皇家法庭。
[name="赫拉格"]   虽然，他们几乎都已经死了。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   那我，比他们活得长。您的同僚，几乎都死了。
[name="爱国者"]   而且，陛下他说过，军人服务国家，不是服务军衔。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   他却也说过，凝聚乌萨斯人的不是血液，是信仰。现在呢？只能愿陛下他安息。
[name="赫拉格"]   可见当今皇帝，依旧把你们当做怪物，而不是乌萨斯的战士。他们一直在压制你和你的族群。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   那位，宽容的陛下，已经过世，这些，我能理解。
[name="爱国者"]   乌萨斯，无数战争野兽，够淹没大地，我不算什么。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   所以军队不是你出走的原因。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   是的，我不关心。我只想和战士们，并肩。
[Character(name="avg_npc_025_1")]
[name="爱国者"]   ......
[name="爱国者"]   将军，坐。酒，剩了一些，我从北方带的。
[Character(name="char_188_helage_1")]
[name="赫拉格"]   ......我没剩下多少时间。下次再喝酒叙旧吧。
[Character(name="avg_npc_025_1")]
[name="爱国者"]   是吗......没事。
[name="爱国者"]   没关系。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_025_1")]
[name="爱国者"]   去第四街，找幸存者。严禁恐吓他们。尽力减少伤亡。注意收集物资，我们的储量，依然窘迫。
[Character(name="char_1002_nsabr_1")]
[name="整合运动成员"]   明白！
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   我以为您死了。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   隐姓埋名也是种死亡。现在的我与过去没有勾连。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   这里，隐居地？不很理想。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   切尔诺伯格已经不再适合居住，无论它有没有遭受过天灾的袭击。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   听说您要离开。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格"]   诊所遭受了一次毁灭性的洗劫，虽然我们提前进行了转移，但还是有所损失的。
[name="赫拉格"]   我是听到了你的传闻，才决定留下看看。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=2)]
[name="爱国者"]   我，不值得。这样很危险。
[Character(name="char_188_helage_1",name2="avg_npc_025_1",focus=1)]
[name="赫拉格

... (全文29564字符)
```

### level_act4d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Character]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="整合运动术师"]     W，我们遇到了点麻烦。
[name="W"]   嚯......值得你们用这个频道联系我，怎么？发现了什么有趣的事情？
[name="整合运动术师"]     不太有趣，W，在你重整那些萨卡兹雇佣兵的时候，有一支队伍叛逃了。
[name="整合运动术师"]     好像是支负责清扫战场的后勤队伍，所以我们直接发起了追击。
[name="整合运动术师"]     意料之内的，他们变成了一盘散沙，一触即溃，开始向城外撤离。
[name="W"]   可喜可贺。
[name="整合运动术师"]     但，意料之外的情况是......我们派去追击的小队，和我们失去了联系。
[name="整合运动术师"]     作为佣兵们的新领头人，希望你能给出合理的解释。
[name="整合运动术师"]     我们的小队为什么人间蒸发了？
[Dialog]
[Background(image="bg_cher_3", width=1, height=1, fadetime=1, screenadapt="coverall",block=true)]
01:13 P.M.    天气/晴
切尔诺伯格，郊外，荒野
[Dialog]
[Character(name="char_1504_cqbw",fadetime=2,block=true)]
[Delay(time=2)]
[name="W"]   这种描述可不利于我理解喔？
[Character]
[name="整合运动术师"]     事实如此。协同小队没发现埋伏和陷阱，只知道敌人是萨卡兹人。
[Character(name="char_1504_cqbw")]
[name="W"]   那自然是萨卡兹了，我的佣兵还能有什么其他种族呢？不过，挺有趣的。接着说。
[Character]
[name="整合运动术师"]     最先接触的时候，目标被成功压制，出于谨慎，追击小队也有所保留。对方并不是什么强敌。
[name="整合运动术师"]     然而某个时刻，通讯突然中断了。
[Character(name="char_1504_cqbw")]
[name="W"]   ......嗯，比起你们，真正的野兽更善于隐藏自己的尖牙利齿，你们这也太大意了吧。
[Character]
[name="整合运动术师"]     我们该怎么办？
[Character(name="char_1504_cqbw")]
[name="W"]   那些萨卡兹人有什么特点？
[Character]
[name="整合运动术师"]    ......不清楚，目击者大都失去了联络。从远处看，只知道有一名近身陷阵的战士。
[Character(name="char_1504_cqbw")]
[name="W"]   那就不要和他们正面接触。拖住那个人，我们一会见。
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[Dialog]
[Delay(time=1)]
[Character(name="char_1002_nsabr_2")]
[name="整合运动刀兵"]     出了什么事？
[Character(name="char_1504_cqbw#3",name2="char_1002_nsabr_2",focus=1)]
[name="W"]   没什么，只是有一支不够成熟的小队中了诱饵。
[Character(name="char_1504_cqbw#3",name2="char_1002_nsabr_2",focus=2)]
[name="整合运动刀兵"]     我们要去支援他们吗？
[Character(name="char_1504_cqbw",name2="char_1002_nsabr_2",focus=1)]
[name="W"]   唉，明明大家都有自己的工作，为什么不能各自处理好分内的事情呢？
[name="W"]   嗯......不过这次就不深究了吧。毕竟我也非常在意我可怜的前领导带着哪些奇怪的萨卡兹人呢。
[Character(name="char_1504_cqbw",name2="char_1002_nsabr_2",focus=2)]
[name="整合运动刀兵"]     明白了。
[Character(name="char_1002_nsabr_2")]
[name="整合运动刀兵"]     通知全体小队，临战整备，转移到城郊。
[PlaySound(key="$d_gen_soldiersrun",volume=0.5)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=0.4)]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=0, fadetime=3, block=true)]
[character]
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Delay(time=0.5)]
[Character(name="char_1011_wizard_1")]
[name="整合运动术师"]     呃，该死，这家伙的动作又变快了！他还在隐藏实力吗？
[character]
[Dialog]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Character(name="char_131_flameb_5#7")]
[name="？？？"]   ......太弱小了，所谓的整合运动只有这种水平吗？
[Character(name="char_1011_wizard_1")]
[name="整合运动术师"]     你这家伙！竟然小看我们——
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Delay(time=0.4)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_1504_cqbw#3",fadetime=1,block=true)]
[Delay(time=1)]
[name="W"]   呵......
[name="W"]   本来就预想到会遇上几个老熟人，可没想到会是你啊。
[Character(name="char_1011_wizard_1")]
[name="整合运动术师"]     W，我们——
[Character(name="char_1504_cqbw",name2="char_1011_wizard_1",focus=1)]
[name="W"]   归队，除非你想送死。别摆出那副急着报仇的表情，他还没有使出全力。哦，想送死的话，我就不拦着你咯？
[Character(name="char_1504_cqbw",name2="char_1011_wizard_1",focus=2)]
[name="整合运动术师"]     ......收队。
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_131_flameb_5#4",fadetime=2,block=true)]
[Delay(time=3)]
[Character(name="char_1504_cqbw#4")]
[name="W"]   很久不见了，佣兵刀术师。
[Character(name="char_1504_cqbw#4",name2="char_131_flameb_5",focus=2)]
[name="炎客"]     你——
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=1)]
[name="W"]   现在，叫我W。
[name="W"]   你呢？
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=2)]
[name="炎客"]     炎客。你应该明白，于我而言，互报姓名的意义。
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=1)]
[name="W"]   哎呀，可怕可怕，过去你手刃那些家伙的时候，也会互报姓名吗？
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=2)]
[name="炎客"]     委托和厮杀是不一样的。
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=1)]
[name="W"]   作为一个经历过那场战争的萨卡兹人忽然销声匿迹，很令人担心啊。
[name="W"]   佣兵嘛，只不过是换了个领头人就要跑路，让人很心慌喔？
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=2)]
[name="炎客"]     这无关紧要。
[name="炎客"]     不过没想到，你的部下连让我报上名字的价值都没有。
[Character(name="char_1504_cqbw#4",name2="char_131_flameb_5",focus=1)]
[name="W"]   那还真是荣幸......嗯，虽然他们成为我部下也没多长时间。啊，你是在邀请我杀了你？
[Character(name="char_1504_cqbw#4",name2="char_131_flameb_5",focus=2)]
[name="炎客"]     不，我对你仰仗外力的战斗方式毫无兴趣。
[name="炎客"]     但我得承认，战术也是一种技巧。如果你的战术比过去更加精湛，我愿意领教。
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=1)]
[name="W"]   ......奇怪，你过去不是那种“只要杀了目标怎么都好”的类型吗？
[Character(name="char_1002_nsabr_2")]
[name="整合运动刀兵"]     W，小队已经分散到了指定点，已经彻底切断了敌人的退路，他逃不掉的。
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=2)]
[name="炎客"]     我也没想到你能成为这些家伙的领导者，大家都在改变。
[Character(name="char_1504_cqbw#3",name2="char_131_flameb_5",focus=1)]
[name="W"]   这些家伙？啊......你是说整合运动？
[name="W"]   还是说......萨卡兹们？
[Character(name="char_1002_nsabr_2")]
[name="整合运动刀兵"]     喝——！
[Dialog]
[Character(name="char_131_flameb_5#2")]
[Blocke

... (全文18696字符)
```

### level_act4d0_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[name="雷蛇"]      三点钟20M，术师目标A。 
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[name="雷蛇"]     八点钟30M，重装防御人员身后的指挥者。
[name="雷蛇"]     注意十点钟有敌方狙击人员。 
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]   
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]      
[Delay(time=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=0.4)]
[Background(image="bg_corridor",screenadapt="coverall")]
[PlayMusic(intro="$tech_intro", key="$tech_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Blocker(a=0, fadetime=2, block=true)]
05：32 PM   天气/晴
龙门接舷区，罗德岛舰船，底层射击训练室
[Dialog]
[Character(name="char_107_liskam_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="雷蛇"]    这才第五组折返射击而已。
[name="雷蛇"]    最后的目标转换速度明显慢了下来，而且也没有命中有效击杀点。
[name="雷蛇"]    如果是实战的话说不定已经反过来被敌人击中了。
[name="雷蛇"]    怎么了，杰西卡，是不是这些训练对你来说还是太勉强了。
[Character(name="char_259_Jessica_1")]
[name="杰西卡"]    哈，哈哈，呼......并，并不会！
[name="杰西卡"]    请指导我继续练习！
[Character(name="char_107_liskam_1",name2="char_259_Jessica_1",focus=1)]
[name="雷蛇"]    气势还不错，不过强撑可不行。
[name="雷蛇"]    我们稍微休息10分钟，尽快将自己的气息调整好。
[name="雷蛇"]    在这10分钟里，我会再跟你强调一次手持铳械的基础运用准则。
[name="雷蛇"]    即使是在战场，也一刻都不能忘记这些最核心的部分！
[Character(name="char_107_liskam_1",name2="char_259_Jessica_1",focus=2)]
[name="杰西卡"]   是！
[Character(name="char_107_liskam_1")]
[name="雷蛇"]    首先永远保证姿态的稳定和平衡，不管在怎样的地形中移动，身体核心都不能放松！
[name="雷蛇"]    上身保持压低，保证重心。
[name="雷蛇"]    其次，控制铳械运作的源石技艺绝对不能有半点紊乱。
[name="雷蛇"]    从手臂连接到铳械内部，精确地感知弹药的推送情况，然后激活铳芯开火。
[name="雷蛇"]    说起来轻松，但是需要细腻地进行源石技艺的持续触发。
[name="雷蛇"]    一旦出现了技艺紊乱，就很可能造成射击失误甚至铳械的损坏。
[name="雷蛇"]    最后则是对目标的瞄准射击和再次移动。
[name="雷蛇"]    在黑钢的射击理论中，这些仅仅是基础中的基础，杰西卡你也应该了然于胸了。
[name="雷蛇"]    那么，你知道你刚才的射击中最大的问题在哪里吗？
[Character(name="char_107_liskam_1",name2="char_259_Jessica_1",focus=2)]
[name="杰西卡"]   呃......是因为我的练习量不够，所以重心不稳转换的速度不快，然后源石技艺控制不精.....
[name="杰西卡"]   以及......开枪的时候总是要么犹豫要么松懈，总不能命中目标。
[CameraShake(duration=0.3, xstrength=5, ystrength=8, vibrato=30, randomness=30, block=true)]
[name="杰西卡"]   啊啊啊，这么一想我这不是每一个部分都有很大的问题吗！
[Character(name="char_107_liskam_1",name2="char_259_Jessica_1",focus=1)]
[name="雷蛇"]    你说得一半对，一半不对。
[name="雷蛇"]    杰西卡你总是想要兼顾一切，既想要做到速度够快，还要命中率够高。
[name="雷蛇"]    在不知不觉期间，你会在各个环节都畏首畏尾。
[name="雷蛇"]    因为你的急迫，导致你的源石技艺控制最先出现混乱。因此，当你应当开始瞄准敌人时，你却还要去进行铳械内部的控制检验。
[name="雷蛇"]    从这里开始，你的射击就会出现问题。
[Character(name="char_107_liskam_1",name2="char_259_Jessica_1",focus=2)]
[name="杰西卡"]   原、原来是这样的...！？
[Character(name="char_107_liskam_1")]
[name="雷蛇"]    首先你要做的是丢掉那些你太在意的各个方面，先专注于指尖。
[name="雷蛇"]    相信你的搭档，手中的枪不会欺骗你。
[name="雷蛇"]    你如何对待它，它就会如何回应你。
[name="雷蛇"]    源石技艺输送的量和速度不是关键，谨记，精度控制和稳定性才是最重要的部分。
[name="雷蛇"]    来吧，继续。连续移动到三个练习台对前方多个目标进行快速射击。
[name="雷蛇"]    再进行五组！专注于手上的源石技艺！
[Character(name="char_259_Jessica_1")]
[name="杰西卡"]    好的！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[PlaySound(key="$pistol", volume=0.9)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Delay(time=1)]
[Dialog]
[PlaySound(key="$pistol", volume=0.9)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$pistol", volume=0.9)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_106_franka_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="芙兰卡"]      基本训练、基本训练、基本训练，已经是第三个小时了......
[name="芙兰卡"]      我可以离开这个充满汗味的训练室了吗。
[name="芙兰卡"]      只是杰西卡的一个切城废墟的侦查任务而已，至于看重到连休息日都消耗进去吗。
[name="芙兰卡"]      难不成还会刚好偶遇出来闲逛的大恶人不成。
[name="芙兰卡"]      我觉得杰西卡需要训练训练自己的自信心才对。
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=2)]
[name="雷蛇"]     看看这些黑钢的资料，杰西卡的各项数据都属于中等水准。
[name="雷蛇"]     作为特派罗德岛的正式员工之一，杰西卡自然也有不小的压力。
[name="雷蛇"]     虽然是和霜叶陨星她们一起的侦察任务，做好准备总不会有坏处。
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=1)]
[name="芙兰卡"]      累垮了在战场上没力气了怎么办。
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=2)]
[name="雷蛇"]     ......
[name="雷蛇"]     她担心自己成为他人的累赘，想要提高自己的作战能力，所以才来专门找了我。
[name="雷蛇"]     龙门的清扫任务结束后，我们还得回一趟黑钢本部，没有那么多时间可以陪杰西卡做训练了。
[name="雷蛇"]     关于手持铳械的使用，我尽量也想把我更多的经验分享给她，能多一点也好。
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=1)]
[name="芙兰卡"]     为了可爱的晚辈，真不错啊。 
[name="芙兰卡"]     我还以为你已经忘记了我们还得回黑钢一趟。
[name="芙兰卡"]     这一趟回去不仅要上报龙门任务的情况，还得进行例行的检验。
[name="芙兰卡"]     你就完全不准备一下？不怕这次的考核评价降低了？
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=2)]
[name="雷蛇"]     我早就准备好需要上报的资料了，我又不是回到罗德岛以后只在睡觉和闲逛。
[Character(name="char_106_franka_1", name2="char_107_liskam_1", focus=1)]
[name="芙兰卡"]     嘿~你怎么知道我回来只睡觉和闲逛了？
[name="芙兰卡"]     雷蛇前辈真是个关

... (全文9088字符)
```

### level_act4d0_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
♪你是否听闻一声惊雷？
♪雨成帘，不见山
♪我早已忘记是何人何物
♪将我引领入此道
♪远方的红色的云啊
♪带我回到故乡
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.6,crossfade=1)]
[Background(image="bg_towerinside",screenadapt="coverall",fadetime=2,block=true)]
10:37 A.M.    天气/多云
叙拉古天灾低发区，荒野，某林中小屋
[Dialog]
[Character(name="char_190_clour",fadetime=2,block=true)]
[Delay(time=2)]
[name="红云"]     唔......？
[name="红云"]     ......
[Character(name="char_279_excu_4#6")]
[name="？？？"]     我已经听见了歌声，躲藏是不必要的，我没有恶意。
[Character(name="char_190_clour")]
[name="红云"]     ......每个刽子手都是这么说的。但最后，总是见血。
[Character(name="char_279_excu_4#6")]
[name="？？？"]     刽子手？我不明白你的用词。我是拉特兰公证所——
[Character(name="char_190_clour")]
[name="红云"]     闭嘴！你骗不了我！
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Delay(time=1.5)]
[name="红云"]     得手了！
[Dialog]
[Character]
[Character(name="char_279_excu_4#6")]
[name="？？？"]     并没有。
[Character(name="char_190_clour")]
[name="红云"]     咦？！
[Character(name="char_279_excu_4#6")]
[name="？？？"]     失礼了。
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$char_emp", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_279_excu_4",fadetime=1,block=true)]
[Delay(time=3)]
[name="？？？"]     目标翻窗逃走，反应相当迅速。
[name="？？？"]     环境确认。腌制的羽兽肉，鞣制用的架子，处理过的牙兽皮，手工小刀和木质工具。
[name="？？？"]     放下弓。我清楚你的位置，你埋伏在窗后。
[name="？？？"]     重申一遍，我对你没有恶意。
[Character(name="char_190_clour")]
[name="红云"]     ——不行！
[Dialog]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Delay(time=1)]
[Character(name="char_279_excu_4")]
[name="？？？"]     你的警戒心很强。
[Character(name="char_190_clour")]
[name="红云"]     尝尝这一箭！
[Dialog]
[Character(name="char_279_excu_4")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_atk_arrow_h")]
[Delay(time=2)]
[Character(name="char_190_clour")]
[name="红云"]     抓，用手抓住了箭身？
[name="红云"]     怎么会......你究竟是什么人！
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_279_excu_4")]
[name="？？？"]     诚如报告所说，遗嘱继承人暴躁排外，难以交流。
[Dialog]
[Character]
[stopmusic(fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_279_excu_4")]
以上就是本人遗嘱的全部内容。
除此之外，我有一条出于私心的请求。
在叙拉古的森林之中，我遇到了一位独臂的沃尔珀少女。
她沉溺在对过去的复仇之中，拘泥于那片染血的土地。
出于怜悯，我帮助了她，也许这伤害到了她的自尊，但她倔强的求生方式的确感动了我。
后来我意识到，我一时兴起的援助，不过是坚定了她复仇的执念，这让我寝食难安。
所以我想把我的一切赠送给她，尽管我几乎一无所有，只剩那么点可悲的遗物。
——恕我打断一下，您的亲属列表里没有沃尔珀人。这会为我们的工作带来很多麻烦。
所以，这只是一位膝下无子的拉特兰公民，在将死之际向公证所提出的小小请求。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_forest",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_190_clour")]
[name="红云"]     ......
[name="红云"]     （他的身上，有血的气味，而且，有股讨厌的感觉......）
[name="红云"]     （又是来破坏我们家园的人吗，讨厌，好讨厌！）
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=1)]
[Character(name="char_190_clour")]
[name="红云"]     上钩了！
[Character(name="char_279_excu_4")]
[name="？？？"]     原来如此，又是个陷阱。似乎各个方位都有触发机关。
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Dialog]
[Character(name="char_190_clour")]
[name="红云"]     听着！你已经走进了猎人的陷阱，不想死的话，就把你的武器放下，一步也不要动！
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="？？？"]     如果能方便交流，可以。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     你是什么人？
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="？？？"]     拉特兰公证所的执行者，本次的遗嘱执行人。可以称呼我“送葬人”。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     拉特兰......？
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     “红云”，你是被委托的对象。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     你为什么会知道我的名字？
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     你的名字由遗嘱人迪伦马特先生告知。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     我不认识这个人。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     出于某些原因，他曾使用多个化名。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     你要带我去哪里？
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     出于保密要求，我不能说。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     ......嘁，满嘴谎话！你就死在这里吧！
[name="红云"]     我是不会离开这儿的，我的爸爸妈妈，叔叔阿姨，还有朋友，我的族人，都，都......
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     我的任务只是带你离开。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     不要再说胡话了！你知道自己的处境吗！
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     我处在无法进行交涉的情况下。
[Character(name="char_190_clour",name2="char_279_excu_4",focus=1)]
[name="红云"]     哼，走进这片森林的，都只会是我们的猎物。
[name="红云"]     你的脚下的骨头，原本都是些野兽和坏人！
[Character(name="char_190_clour",name2="char_279_excu_4",focus=2)]
[name="送葬人"]     理解。据点周围布满陷阱。
[name="送葬人"]     落穴，绊索，土制地雷，自动飞镖。
[name="送葬人"]     请放心，我已经全部解除了。陷阱很初级，有伤到委托对象你的可能性。
[Character(name="char_190_clour",nam

... (全文15734字符)
```

### level_act4d0_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[Dialog]
[Character]
[Background(image="bg_light",screenadapt="coverall",fadetime=2)]
[Delay(time=3)]
一切都是白色的。
头顶的天空与脚下的地面，目所能及之处，全都被安静的白色填满。
纯白、寂静、空无一物。
只有火苗摇曳燃烧。
从某一个时间点起，悄然侵蚀梦境，又于梦醒时融化消弭。
“这里是哪里？”
无人应答。
“我为什么会在这里？”
无人应答。
“我该怎么离开？”
无人应答。
“......”
除了自己之外，谁都不在。
除了自己之外，什么都没有。
那么，
所有的困惑就只剩下一个——
“你......是什么？”
......
............
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, fadetime=1, block=true)]
02:35 P.M.  天气/阴转小雨 
罗德岛舰船，二号舱室，干员生活区 
[Dialog]
[Character(name="char_134_ifrit_5#7",fadetime=2,block=true)]
[Delay(time=2)]
[name="伊芙利特"]  ！！
[name="伊芙利特"]  ......呼。
[Character(name="char_134_ifrit_5#7")]
[name="伊芙利特"]  （又来了。怎么老做那个梦，那到底什么玩意啊。）
[name="伊芙利特"]  （呃，头都睡扁了，好痛。）
[name="伊芙利特"]  （抓头）烦死了，都是博士那家伙害的，这些题也太难写了吧！
[name="伊芙利特"]  这什么怪题目啊，还要求面积？搞什么啊？
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_134_ifrit_5#4")]
[name="伊芙利特"]  哇啊！
[name="伊芙利特"]  停停停停。不是现在，别烧起来啊喂！
[Character(name="char_134_ifrit_5#7")]
[name="伊芙利特"]  唔呃......
[name="伊芙利特"]  还是把桌角烤焦了......算了，还好作业没事。
[name="伊芙利特"]  博士那家伙......
[Dialog]
[Character]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_134_ifrit_5#3")]
[name="伊芙利特"]  喂， 这些一定要都写完吗？真麻烦......
[name="伊芙利特"]  啊？学起来对我有好处？
[Character(name="char_134_ifrit_5#9")]
[name="伊芙利特"]  废话，这我当然知道，要不然谁要跟你学！
[name="伊芙利特"]  但是作业也太多了吧！而且这个词和这个词有什么区别啊......
[name="伊芙利特"]  就因为我讲了你两句，赫默还拿走了我的辣椒干，这都怪你！
[Character(name="char_134_ifrit_5#2")]
[name="伊芙利特"]  喂，你还笑？！
[Decision(options="我知道她藏辣椒干的地方。;......;炭烤沙虫腿，来一根？",values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_134_ifrit_5#7")]
[name="伊芙利特"]  真的？！在哪？！
[name="伊芙利特"]  真要跟你一起拿了，你和我肯定都会挨骂。
[Predicate(references="2")]
[Character(name="char_134_ifrit_5#2")]
[name="伊芙利特"]  别一直笑啊，又不说话，很奇怪呀！
[name="伊芙利特"]  你是不是压根就不想回答我啊？
[Predicate(references="3")]
[Character(name="char_134_ifrit_5#9")]
[name="伊芙利特"]  恶，博士，这是什么？
[name="伊芙利特"]  拿走拿走，我不要！——唔唔唔？
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="char_134_ifrit_5#7")]
[name="伊芙利特"]  唔？
[name="伊芙利特"]  （咀嚼）呃。
[name="伊芙利特"]  （吞咽）咕嘟......啊？
[name="伊芙利特"]  我，我吃了什么？
[name="伊芙利特"]  算了......
[Predicate(references="1;2;3")]
[Character(name="char_134_ifrit_5#5")]
[name="伊芙利特"]  对了，博士，赫默明天是不是要去出任务？
[name="伊芙利特"]  带上我一起，怎么样？我的实力，你知道的对吧？
[name="伊芙利特"]  你去和她说说，让我也去看看吧？
[Decision(options="这次行动是收尾，你更擅长战斗吧？;这个月投诉有点多，先忍忍吧？",values="1;2")]
[Predicate(references="1")]
[Character(name="char_134_ifrit_5#7")]
[name="伊芙利特"]  搞什么，你说的那些我也会啊？
[name="伊芙利特"]  那为什么我们现在没得战斗，让我去啊，我一定要给其他人看看我的实力！
[Predicate(references="2")]
[Character(name="char_134_ifrit_5#2")]
[name="伊芙利特"]  我这能烧干整个战场的火力，他们就是做不到才嫉妒我吧！
[name="伊芙利特"]  我才不管那些人怎么说呢！
[Predicate(references="1;2")]
[Character(name="char_134_ifrit_5#2")]
[name="伊芙利特"]  赫默和你总该相信我吧？
[name="伊芙利特"]  其他人不能理解，我没关系，又不关我的事，
[name="伊芙利特"]  但为什么连你们也这么说！为什么呀！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Decision(options="伊芙利特，冷静！",values="1")]
[Predicate(references="1")]
[Character(name="char_134_ifrit_5#8")]
[name="伊芙利特"]  咳！
[Dialog]
[Character]
[Blocker(a=1, initr=2, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(name="char_134_ifrit_5#7")]
[name="伊芙利特"]  烦死了。
[name="伊芙利特"]  算了，去他的。我看看，这题这题还有这题......都填C。
[name="伊芙利特"]  还有这题......看不太懂，算了随便写写。
[Character(name="char_134_ifrit_5#1")]
[name="伊芙利特"]  这样就成了......！
[Dialog]
[Character]
[CameraShake(duration=0.3, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="医疗干员"]  到做检查的时间了，伊芙利特。
[Character(name="char_134_ifrit_5#9")]
[name="伊芙利特"]  恶。
[name="伊芙利特"]  烦人的家伙来了。
[Character(name="char_016_medic")]
[name="医疗干员"]  怎么一股烧着了的味道......
[name="医疗干员"]  伊芙利特？打扰一下。
[name="医疗干员"]  今天要做一个血液源石结晶密度检查，请你配合......嗯？这桌子是怎么回事，怎么被烧焦了？
[Character(name="char_016_medic",name2="char_134_ifrit_5#9",focus=2)]
[name="伊芙利特"]  没什么。就是个意外。
[Character(name="char_016_medic",name2="char_134_ifrit_5#9",focus=1)]
[name="医疗干员"]  伊芙利特......这样很危险的。
[name="医疗干员"]  罗德岛内部是不允许出现明火的，如果是你的话，更要好好控制。
[name="医疗干员"]  我跟他们说了，不可以用抑制类的药物，但也需要你好好配合......
[Character(name="char_016_medic",name2="char_134_ifrit_5#9",focus=2)]
[name="伊芙利特"]  ......
[name="伊芙利特"]  啰嗦死了。烦不烦啊！
[Character(name="char_016_medic",name2="char_134_ifrit_5#9",focus=1)]
[name="医疗干员"]  ......伊芙利特，我只是个普通的护士，我不太会带孩子，
[name="医疗干员"]  如果可以的话，我们能好好交流......
[Character(name="char_016_medic",name2="char_134_ifrit_5#2",focus=2)]
[name="伊芙利特"]  谁又是孩子了，你好烦啊？！
[name="伊芙利特"]  为什么我要摊上你这种人，就不能让我一个人呆着吗？！
[Character(name="char_016_medic",name2="char_134_ifrit_5#2",focus=1)]
[name="医疗干员"]  伊芙利特......我也有自己的工作的。
[Character(name="char_016_medic",name2="char_134_ifrit_5#2",focus=2)]
[name="伊芙利特"]  那就别管我的事！说过好多次了，那些穿着白大褂的，我看见就难受！
[name="伊芙利特"]  快让开，别挡着我出门。
[Character(name="char_016_medic",name2="char_134_ifrit_5#2",focus=1)]
[name="医疗干员"]  可是，检查......
[Character(name="char_016_medic",name2="char_134_ifrit_5#2",focus=2)]
[name="伊芙利特"]  我让你别挡路！
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_134_ifrit_5#4")]
[name="伊芙利特"]  啊！！
[name="伊芙利特"]  我，我的作业！烧，烧起来了！
[Character(name="char_134_ifrit_5#2")]
[name="伊芙利特"]  你搞什么，搞什么啊？！
[Character(name="char_016_medic",name2="char_134_ifrit_5#2",focus=1)]
[name="医疗干员"]  伊芙利特！快，快灭火！
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="cha

... (全文22791字符)
```

### level_act4d0_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
08:30 A.M 天气/暴雪
北地，因非冰原，莱茵生命420号临时科考观测站
[name="装置"]  系统已解锁。
[name="装置"]  确定年份：未知
[name="装置"]  时间设置出现问题，现在转到手工控制。
[name="装置"]  要进行下一步操作，请进行身份认证。
[Dialog]
[Character(name="char_248_mgllan",fadetime=1,block=true)]
[Delay(time=1)] 
[name="麦哲伦"] 唔，我想想......嗯，莱茵生命科学考察员，麦哲伦。
[Character]
[name="装置"]   认证中——
[name="装置"]   认证完毕，声音样本已确认。
[name="装置"]   哔哔——
[name="装置"]   指纹已确认。
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[name="装置"]   （活泼的女声）嗨，你好呀麦麦，欢迎回来！
[Character(name="char_248_mgllan")]
[name="麦哲伦"]   ......
[name="麦哲伦"]   好怪哦！
[name="麦哲伦"]   唉，早知道就不答应梅尔姐测试这个签到系统了，好奇怪的功能啊......
[name="麦哲伦"]   呼，总而言之，开始干活吧！
[name="麦哲伦"]   今年最后一个勘察点，确认没有新的发现。
[name="麦哲伦"]   至此，本年度预定的勘查目标已经完成，确认其他各项任务完成后，将踏上返程。
[name="麦哲伦"]   呼，搞定。
[name="麦哲伦"]   写报告可真是我最不擅长的东西了，还是来听听录音吧。
[Character]
[name="装置"]   （活泼的女声）你好，麦麦。今天，是你本次外出勘察的第1，8，7天了哦。
[Character(name="char_248_mgllan")]
[name="麦哲伦"]  哇，这一次也已经出来这么久啦，我都没有感觉了。
[Character]
[name="装置"]   （活泼的女声）你已经出去很久了，也该回来了吧？大家都想你了。
[Character(name="char_248_mgllan")]
[name="麦哲伦"]  欸？！之前有这一段吗......难道是梅尔姐偷偷录的然后设置了触发条件？
[name="麦哲伦"]  呜哇，不管怎么样，居然还有这样的小惊喜，好开心啊！
[name="麦哲伦"]  不过，说是说可以回去了，但是......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2, block=true)]
[Background(image="bg_bridge",screenadapt="coverall")]
[PlaySound(key="$blizzard")]
[Blocker(a=0.4, r=1, g=1, b=1, fadetime=2, block=true)]
[Character(name="char_248_mgllan")]
[name="麦哲伦"]  这场暴风雪，恐怕还要持续至少一周呢，唉，幸好物资储备还算充裕。
[name="麦哲伦"]  算啦，还是来确认一遍任务表吧，我记得应该还有几个没有填的。
[name="麦哲伦"]  让我看看，嗯，周边的样本采集，完成。遗迹线索的寻找，没有~也算完成。
[name="麦哲伦"]  和去年比没有什么新发现呢，要是再来一个和大前年一样的发现就好了。
[name="麦哲伦"]  虽然说这才是常态啦，要是科长在肯定要批评我贪心了。
[name="麦哲伦"]  应该没有了吧......嗯？还有一项空着，新材料的低温性质测试......啊。
[name="麦哲伦"]  我完全忘记了这件事！！！不如说这个新材料被我放哪儿去了来着！！！
[name="麦哲伦"]  糟了糟了，这个要是丢了，我可要被杀掉了！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=1, block=true)]
[name="麦哲伦"] 呼，好险好险，居然被塞在外层口袋里......
[name="麦哲伦"] 外层口袋是零下43度，持续时间6小时，依然保持弹性。
[name="麦哲伦"] 接下来测试一下硬度。
[name="麦哲伦"] 嘿！
[name="麦哲伦"] 嗯，也没有问题。好，接下来放进实验瓮就行。
[name="麦哲伦"] 唔，幸亏还是有放在外套里......
[name="麦哲伦"] 好吧，反正现在是暴风雪，干脆把它放到门外去摆一天看看低温疲劳性好了。
[name="麦哲伦"] 现在外面的气温应该很合适吧。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=1)]
[name="麦哲伦"] 听着，麦哲伦，你要深呼吸，在打开门的瞬间，把东西丢出去，然后立刻关门。
[name="麦哲伦"] 要快，准，狠！不然暴风雪灌进来可就糟了。
[name="麦哲伦"] 1，2，3！
[Dialog]
[Character]
[PlaySound(key="$d_gen_dooropen")]
[PlaySound(key="$blizzard")]
[Character(name="char_341_amona_2#2",fadetime=1,block=true)]
[Delay(time=1)] 
[name="？？？"] ......
[Character(name="char_248_mgllan")]
[name="麦哲伦"] ......
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="？？？"] 请问......
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="麦哲伦"] 啊啊啊啊啊啊啊啊啊啊！！！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=1, block=true)]
[Character(name="char_248_mgllan")]
[name="麦哲伦"]  麦哲伦，你刚才好像看到了一个幽灵。
[name="麦哲伦"]  麦哲伦，虽然她很漂亮，但一定是个幽灵。
[name="麦哲伦"]  但是，这里可是北地，怎么可能会有别人？
[name="麦哲伦"]  难、难道说真的是雪中的幽灵？
[name="麦哲伦"]  不行不行，要再开门看看，要用科学的眼光去看待！！
[name="麦哲伦"]  没有幽灵这种东西！我的体温也没有下降到出现幻觉！
[name="麦哲伦"]  万一是新的族群，那就是大发现！加油啊，麦哲伦！
[Dialog]
[Character]
[PlaySound(key="$d_gen_dooropen")]
[Character(name="char_341_amona_2#2")]
[name="？？？"] ......
[Character(name="char_248_mgllan")]
[name="麦哲伦"] ......
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="？？？"] 请问，我能进来吗？
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 呃，呃......你......我......
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="？？？"] 不用害怕。我是活人，不信的话，摸摸我的脸吧？
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 呃？呃？
[name="麦哲伦"] 好，好......
[name="麦哲伦"] 呜啊，好暖和！怎么会，这不是在北地吗，怎么会......
[name="麦哲伦"] ......您是萨米人吗？
[name="麦哲伦"] 咦......欸。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="？？？"] 虽然不知道是哪里让你感到失望，不过我确实是萨米人。你好，小姑娘。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 你，你好。虽然不知道你是怎么到这里来的，不过先进来吧，外面可不是普通人能活下来的温度！
[name="麦哲伦"] 即使是萨米人，对这样的暴风雪也没辙吧？
[Character(name="char_341_amona_2#2")]
[name="？？？"] 谢谢你。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Blocker(a=0.3, r=1, g=1, b=1, fadetime=2, block=true)]
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 给，热茶。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="？？？"] 谢谢。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 姐姐你叫什么？
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="？？？"] 就叫我——
[name="？？？"] 西蒙娜吧，西蒙娜。你的名字呢，小姑娘？
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 代号麦哲伦！莱茵生命科考专员，420号观测站的负责人......
[name="麦哲伦"] 说是这么说，其实现在只有我一个人在用啦。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="西蒙娜"] 是这样啊。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 西蒙娜，你为什么会来这里？还被困在暴风雪里......
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="西蒙娜"] 我是受人所托来找人的。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 找人？这里可是北地哦，别说人了，我一个月连生物都见不到几只呢。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="西蒙娜"] 委托我的人说，她应该就在这一带活动。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 你找她要做什么呢？
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="西蒙娜"] 这场暴风雪将会持续很久很久，她可能会耽搁一些时间。我是来这里接她的。
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=2)]
[name="麦哲伦"] 咦，是这样吗？！你是来接我的吗？
[Character(name="char_341_amona_2#2",name2="char_248_mgllan",focus=1)]
[name="西蒙

... (全文20713字符)
```

### level_act4d0_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
[PlayMusic(intro="$tech_intro", key="$tech_loop", volume=0.8, crossfade=1.5, delay=0.5)]
[Character]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_lungmencommand",screenadapt="coverall")]
[Delay(time=0.4)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=1, block=true)]
11:30 A.M.  天气/多云
野外，罗德岛总工程师办公室
[Dialog]
[Character(name="char_003_kalts_1")]
[name="凯尔希"] 这次又要做什么？
[Character]
[Dialog]
[Character(name="char_007_closre_1#5",fadetime=1,block=true)]
[Delay(time=1)]
[name="可露希尔"] 凯尔希，我等会能去看看博士吗？
[Character(name="char_003_kalts_1")]
[name="凯尔希"] 你是好久没有对{@nickname}恶作剧，又手痒了？
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 欸，不要那么警觉嘛！我可是好心在关心人家呢！
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 上一次你说关心别人的后果，是创造了一间连续三个月都在午夜零点自动播放“可露希尔的午夜录像超商”的舱室。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 可是......
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 还没法调低音量。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 好啦好啦，我承认！我确实是想逗逗博士啦。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 然而，Dr.{@nickname}现在是失忆状态，是否记得你还是个未知数。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 啊？是睡太久了睡傻了吗？好惨哦，之后去给博士送点零食慰问一下好了。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 随你。只是，别再给Dr.{@nickname}留下些坏印象。
[name="凯尔希"] 华法琳已经够糟了，再增加{@nickname}对血魔的误会，卡兹戴尔的事情会被迫继续延后。无限期。
[name="凯尔希"] 这可是你在他人心目中重新建立自己形象的机会，好好把握。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=2)]
[name="可露希尔"] 我以前的形象有那么差吗？
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=1)]
[name="凯尔希"] 在中央空调三十六度事件之后，是的。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 不，那是机房断电。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 我在操作台上找到了你的指纹。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 是机房断电！
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 你黑掉监控删除了录像，但操作台有生物备份系统，我有十三张分布在不同时段的组织切片。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=2)]
[name="可露希尔"] 对不起是我的错那个什么混账使节太嚣张了我想治治他十分对不起。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=1)]
[name="凯尔希"] ......
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 不过，欢迎会呢？Dr.{@nickname}的欢迎会，我们不弄一个吗？
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 免了。现在是非常状态。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 欸，不要这么冷淡嘛，凯尔希。既然博士失忆了，我们不是更应该让博士多感受些同伴的温暖吗？
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 你以前是这么看待Dr.{@nickname}的？
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 可能......我和博士也没那么亲近？不过就像你说的，这不是建立自己的美好形象的最佳时机吗。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 可露希尔，我现在不想聊这个话题。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 哼，你不去我就自己去，我可不管你。
[name="可露希尔"] 话说，按照既定安排，我们是要去龙门没错吧。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 嗯。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 能自由行动吗？
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 龙门已经变得相当危险了。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 欸，龙门有这么危险吗？不是说那边治安还挺好吗？
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 离切尔诺伯格最近的城市就是龙门，剩下的不用我多说。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 那为什么要去？
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 因为离切尔诺伯格最近的城市就是龙门。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 你是不是还隐瞒了什么理由啊......
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 不，上次开会的时候，我全都报告了。只是那个时候，你正戴着眼罩躺在会议椅上睡觉。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 系统实在是维护太累了......不好意思。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 我没有责怪你的意思。没有你的努力，罗德岛连启动都做不到。
[name="凯尔希"] 但我还是要打消你那些奇奇怪怪的想法......你叫我来究竟是为了什么？
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 哎呀，就是叫叫你。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 我回实验室了。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=2)]
[name="可露希尔"] 别走呀！哎其实......三区有两条走廊断电了。
[name="可露希尔"] 一起去看看线路嘛，行不行嘛！
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=1)]
[name="凯尔希"] 叫工程干员去不就行了。又是供能线路出了问题？
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"] 我们亲自去看看也没什么问题呀。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"] 平常我让你检查的时候，你可都是交给其他干员去做的。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#5",focus=2)]
[name="可露希尔"] 身为罗德岛总工程师的责任感在这一刻又一次觉醒了！我们去吧！
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"] 快走吧，路我比你熟......
[Character(name="char_007_closre_1")]
[name="可露希尔"] 唉？
[Dialog]
[Character]
[Character(name="char_304_hvrain",fadetime=1,block=true)]
[Delay(time=1)]
[name="暴雨"] ......
[Character(name="char_007_closre_1")]
[name="可露希尔"] ......
[name="可露希尔"] 唉？！
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"] 这位是暴雨。
[Characte

... (全文14808字符)
```


## 统计

- 总字符数：131394
- 对话行数：1446


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
