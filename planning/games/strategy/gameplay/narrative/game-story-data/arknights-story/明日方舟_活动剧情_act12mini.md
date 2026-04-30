# 明日方舟 · 活动剧情 · act12mini（7段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act12mini」完整剧情脚本（7个文件，1615行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act12mini
- 脚本文件数：7

### level_act12mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[delay(time=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
在过去的某个时刻，骑士击碎浪潮的故事尚未被写成小说，穿过林海的风中还能听见炮火轰鸣，弓弦振响。
那时人们笃信自己困于黑暗，以生死之重掷向大地，以淋漓鲜血作为生存的代价和谏言。
而如今，深秋的日色在原野上缓慢地舒展，农人的铁锤叮叮敲打，赶在下一场风雨之前将房檐修葺。
山脚的墓园中，人们只是挥动铁器，一铲一铲翻开泥土，伴随着啜泣声，将枯萎的作物埋进地里。
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Dialog]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
11月27日 3:20 P.M.
卡西米尔南部乡野
[dialog]
[delay(time=1)]
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  ......所以，先生，您现在也是一个人在四处游荡了？
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  没有侍从，没有追随者，甚至也没有剑与甲胄......但似乎也没有人与您为敌。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  我还记得，当年许多人说，您是在和这个国家排得上名号的家族作对，总会惹上大麻烦的。
[Dialog]
[character]
[Character(name="avg_4064_mlynar_1#11$1",fadetime=1)]
[delay(time=2)]
[name="玛恩纳"]  这么说的那些人，不也接受了可能给他们带来麻烦的救济物资吗？
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  ......
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]  ......我已经离开了权势者如今勾心斗角的场地，不再值得他们分神顾忌。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  是啊，是啊......您应该不觉得意外。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  就像当年我逃来这片异国的土地，以为那位君王的法术会永远在我背后穷追不舍......
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  ......但是现在，您看，我这手无寸铁的教书匠，在一间连风雨都抵御不了的小屋里，已经风平浪静地生活了二十余年啦。
[Character(name="avg_4064_mlynar_1#6$1")]
[name="玛恩纳"]  你自称来自莱塔尼亚......巫王高塔早已倒塌，你为什么还留在这里？
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  我躲藏太久啦，如今已经没有非得回到什么地方生活的心气。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  消息流传到这样偏远的地方花了不少时间，而我发现自己已经习惯了在田野间劳作、只计算自己温饱的日子。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  而且为了伪装，我早已将角斩断，习惯像库兰塔一样生活。就算莱塔尼亚还有我的故人幸存，他们又该怎么认我？
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]  但你始终以莱塔尼亚人自居。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  哎，先生，我只是个忘不掉前半辈子的可怜人。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  热忱者已经早早死去，我这样躲躲藏藏活到最后的，也无所谓自己是什么面目了。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  您是来故地重游的吗？我拿不出什么东西，但您如果愿意接受一杯热茶的招待，我荣幸之至。
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  不必了。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  好，好......先生，我只是一直记得您的恩情。这些年了。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  其他人以卡西米尔的地区方言互相呼唤的时候，您看出了我的窘迫。但您没有揭穿我自称的身份，默许我继续站在流民的队伍里。
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  ......
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  ......看来您不记得了。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  您对我说的事情都没有印象，刚刚被认出来的时候却也不觉得惊讶......那您应该像这样救过许多人吧。
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  ......都过去太久了。
[Character(name="avg_4064_mlynar_1#4$1")]
[name="玛恩纳"]  你在帮人写告示？
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  您说刚才那张？是啊，安全告示。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  有骑士昨天来过我们村子，说是最近有强盗一类的人流窜到这一带来了，连茨沃涅克城内都出现了袭击案。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  但明眼人都知道，只是有强盗的话，我们这样远离移动城市航道的村庄就算真的遭受洗劫，也不会有人在意。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  因此，征战骑士如此郑重的提醒，总让我觉得惴惴不安哪。
[name="年老的村民"]  先生，即使现在没有人向您寻仇，您也还是带上一把武器更合适。
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]  ......这是征战骑士告诉你们的？
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  原来您还没有听说？
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  说来确实奇怪。这几年来，我竟然真的见到征战骑士在关心平民百姓的死活。
[Character(name="avg_npc_005#1")]
[name="年老的村民"]  像是前两年村子里搬来的几户人家，就是骑士从天灾底下抢救出来的、隔壁集镇的幸存者......
[Character(name="avg_4064_mlynar_1#9$1")]
[name="玛恩纳"]  ......我不是奇怪这些事。这是他该做的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="31_g4_mini12_village",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  你可把我们吓坏了，切斯柏。
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  要不是你及时把头盔摘下来，说不好就有村民吓得对你拉弓了。
[Character(name="avg_npc_625_1#10$1")]
[name="托兰"]  万一不小心伤到了您这位尊贵的征战骑士......嗯，虽说挂在我身上的罪名已经不少了，但悬赏令估计还能再加急一些。
[Character(name="avg_npc_627_1#4$1")]
[name="切斯柏"]  “村民”？哈哈......
[Character(name="avg_npc_627_1#2$1")]
[name="切斯柏"]  幸好你们还记得我这张脸。
[Character(name="avg_npc_627_1#4$1")]
[name="切斯柏"]  ......呃，至少大多数人还记得？
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  活着的人里，你的老熟人不多啦，新来的倒是不少。
[Character(name="avg_npc_627_1#12$1")]
[name="切斯柏"]  ......
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  犯不着为我们这些人愁眉苦脸的。有何贵干？都巡逻到荒地上的小村庄了，总不能是因为最近可忙的事情不多吧？
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  毕竟，我听说这一带现在不太安宁，征战骑士在协助维护城外的秩序......
[Character(name="avg_npc_625_1#2$1")]
[name="托兰"]  ——我们几个弟兄还在您手下接受调查。
[Character(name="avg_npc_627_1#1$1")]
[name="切斯柏"]  ......所以我才找来这里，托兰。
[name="切斯柏"]  既然过来的赏金猎人是你在牵头，那话就好说多了。
[Character(name="avg_npc_627_1#1$1")]
[name="切斯柏"]  你知道的，我得先按照纪律办事。
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  难得你这次说的不是“只按照纪律办事”。那我们单独聊聊？
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  上次碰面时“小矿工”就想跟你叙叙旧，可惜当时我们忙着撤退，你忙着按纪律回队报告......他前两年就病死啦。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="bg_indoor_u",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_npc_627_1#1$1")]
[name="切斯柏"]  从这里望下去......正好能看见河谷对面的工业园区。你们的据点可真是选了个好位置。
[Character(name="avg_npc_625_1#4$1")]
[name="托兰"]  喔，看起来是家大企业。怎么了？
[Character(name="avg_npc_627_1#2$1")]
[name="切斯柏"]  那里原本是帕伦尼斯科家族的庄园。
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  ......怀旧了？
[Character(name="avg_npc_627_1#3$1")]
[name="切斯柏"]  多少有点。
[Character(name="avg_npc_627_1#1$1")]
[name="切斯柏"]  ......说回正题吧。我不知道猎人们对我有多大的敌意，但我不希望你在他们面前为难。
[Character(name="avg_npc_625_1#1$1")]
[name="托兰"]  这你倒是可以放心，就算这里有许多人不是咱们的老朋友.

... (全文20237字符)
```

### level_act12mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
11月28日 5:00 P.M.
卡西米尔南部，车辆难以通行的田间小路
[character]
[name="开朗的女声"]  玛恩纳先生，请务必再仔细回忆一下。
[character]
[name="开朗的女声"]  在您与维斯图兰公司的代表争夺盖尔工业工程合同的竞标会上，我们的确是见过的！
[name="玛恩纳"]  不，我不记得。
[character]
[name="开朗的女声"]  那应该是三年前，血骑士赢得骑士特锦赛冠军的那年！竞标会后的酒会上，餐厅正在转播颁奖仪式呢。
[name="玛恩纳"]  我从不关心骑士竞技，没有印象。
[character]
[name="开朗的女声"]  您或许还记得，在酒会上，您向盖尔工业的每一位负责人敬酒，结果喝红酒喝到醉？
[name="开朗的女声"]  我到现在还记得那时的场景，没想到大公司的销售部门，想要拿下一单生意也这么不容易呀。
[name="开朗的女声"]  从结果来看您也算成功啦，当时几位负责人对您印象倒挺深刻的，虽然最后——
[name="玛恩纳"]  不必这样套近乎。
[name="玛恩纳"]  我们只是顺路，你不用将其视作帮助，也不必认为我会向你索要什么回报。
[character]
[name="开朗的女声"]  怎么能这么说呢？如果不是遇见您，我现在还在荒野上迷路呢！
[character]
[name="开朗的女声"]  而且，我不是想套近乎，是真的想向您表示感谢。等回到大骑士领，我一定找机会正式向您道谢！
[name="玛恩纳"]  如果你还想早点到达的话，专心赶路，看好脚下，黛——
[dialog]
[character]
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[character]
[name="不太开朗的女声"]  抱歉，鞋跟太高了，我没踩稳......
[Character(name="avg_4064_mlynar_1#6$1")]
[name="玛恩纳"]  ......黛丝特女士。
[dialog]
[character]
[Character(name="avg_4032_provs_1#5$2",fadetime=1)]
[delay(time=1)]
[name="黛丝特"]  真不好意思，让您看到我如此不专业的一面！......呃，我的润唇膏掉到哪里去了......
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  还好，纸质材料都放在文件夹里，没有弄脏。
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  请您稍等我一下，我很快就能把手提包收拾好。
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  ......先休息一会吧。
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  好、好的！
[Character(name="avg_4032_provs_1#3$2")]
[name="黛丝特"]  实在是不好意思，玛恩纳先生。要不是租来的车坏了，本来是不用麻烦您的。
[Character(name="avg_4032_provs_1#3$2")]
[name="黛丝特"]  昨晚我刚把车从出租公司开到旅馆，今天早上它就点不着火了。出现这么严重的故障，我之后得起诉出租公司才行。
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  如果您之后遇到这种小麻烦的话，我也可以提供帮助哦！这方面我还挺在行的。
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  ......不用。
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  对了玛恩纳先生，我还没有和您说过，我这次准备要去办理的案件吧。
[Character(name="avg_4032_provs_1#10$2")]
[name="黛丝特"]  这座村庄名叫垒石村。原来的主人贵族骑士马雷克，在七年前将这座村庄的土地所有权抵押给盖尔工业。
[Character(name="avg_4032_provs_1#10$2")]
[name="黛丝特"]  但是在那之后，他又将土地售卖给在这里居住的村民。
[Character(name="avg_4032_provs_1#10$2")]
[name="黛丝特"]  村民们以为终于有机会获得自己的土地，就用十年税金的价格买下了自家的耕地。
[Character(name="avg_4032_provs_1#10$2")]
[name="黛丝特"]  直到半年前，老马雷克先生病逝，盖尔工业也终于将垒石村的开发项目提上日程。这才发现这里的土地归属权已经成了一笔烂账。
[Character(name="avg_4032_provs_1#8$2")]
[name="黛丝特"]  许多村民多年前为了买下自己的土地申请的贷款还没有还清，就又被告知他们的土地已经不属于自己了。是不是很过分？
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]  ......我没有说过我想听。
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  我还以为您会对合作企业的黑料感兴趣呢。
[Character(name="avg_4064_mlynar_1#9$1")]
[name="玛恩纳"]  我对匡扶正义的律师故事不感兴趣。
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  匡扶正义吗？我倒也没有这么觉得啦......只是做一些律师的本职工作嘛。
[Character(name="avg_4032_provs_1#2$2")]
[name="黛丝特"]  对了，玛恩纳先生，您又是为什么离开大骑士领？也是出差吗？
[Character(name="avg_4064_mlynar_1#9$1")]
[name="玛恩纳"]  只是休假而已。
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  喔，真羡慕啊......
[Character(name="avg_4032_provs_1#10$2")]
[name="黛丝特"]  我已经记不清上一次休假是什么时候了，好像还是黑骑士夺冠的时候......？
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  因为押中了冠军，想着可一定要好好奖励自己......
[Character(name="avg_4032_provs_1#2$2")]
[name="黛丝特"]  不过赢来的奖券也不值多少钱就是啦。
[dialog]
[character]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=1)]
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  抱、抱歉！我先接个电话！
[dialog]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[delay(time=1)]
[Character(name="avg_4032_provs_1#7$2")]
[name="黛丝特"]  您好，十分抱歉，因为路上出现了一些状况，我还没有抵达预定地点。
[Character(name="avg_4032_provs_1#7$2")]
[name="黛丝特"]  不，不会延误，请您放心，我一定会在今天之内完成洽谈，按时给企业回复的。
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  是是，这当然算我工作上的失误，造成的一切后果由我承——啊，挂了。
[Character(name="avg_4032_provs_1#7$2")]
[name="黛丝特"]  唉，回去又要看所长脸色了......本来被派到这么偏远的地方出差就已经够呛了......
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]  你说自己是来处理村庄土地被收购的官司？
[Character(name="avg_4032_provs_1#10$2")]
[name="黛丝特"]  是呀。
[Character(name="avg_4064_mlynar_1#4$1")]
[name="玛恩纳"]  但你在电话里说的是，“给企业回复”？
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  玛恩纳先生，您好像误会了。
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  我的确负责这次土地收购的官司，不过，我是盖尔工业的代理人哦。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="31_g4_mini12_village",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_4032_provs_1#2$2")]
[name="黛丝特"]  终于......到了！
[Character(name="avg_4064_mlynar_1#6$1")]
[name="玛恩纳"]  ......
[Character(name="avg_4032_provs_1#5$2")]
[name="黛丝特"]  玛恩纳先生，您还好吗？需不需要先找地方休息一下？
[character(name="avg_npc_222")]
[name="西装革履的男人"]  请问，是黛丝特律师吗？
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  是我是我！您就是之前联系过我的哈姆律师吧。
[Character(name="avg_4032_provs_1#7$2")]
[name="黛丝特"]  非常抱歉迟到了这么久，如您所见，路上的确出了一些事故......
[Character(name="avg_npc_222#1")]
[name="哈姆"]  没有关系，这里离大骑士领路途遥远，发生意外也是可以理解的。
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  那，玛恩纳先生，等我处理完案件请您喝一杯？听说这里的村民有酿啤酒的传统。
[Character(name="avg_4064_mlynar_1#3$1")]
[name="玛恩纳"]  不用了。
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  欸，好吧！那一路上谢谢您啦！
[Character(name="avg_npc_222#1")]
[name="哈姆"]  黛丝特小姐，请问我们可以进入工作了吗？
[Character(name="avg_4032_provs_1#2$2")]
[name="黛丝特"]  当、当然！我们现在就开始吧。
[Character(name="avg_npc_222#1")]
[name="哈姆"]  好的，请跟我来。
[Character(name="avg_npc_222#1")]
[name="哈姆"]  （不愧是大型企业雇请的律师，出差时还会配有专门的助理啊......）
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="27_g26_dusk_wild",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Character(name="avg_4032_provs_1#1$2")]
[name="黛丝特"]  接到这个案子的

... (全文24869字符)
```

### level_act12mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[delay(time=1)]
玛恩纳·临光启：
久疏问候，或许在大骑士领的生活过于忙碌，令你无暇顾及旧友的往来书信。我尊重你的选择，希望你一切顺利。
骑士团有许多逸事，如有机会再次小聚，我乐意当面讲给你听。我所行仍与我的理想相去甚远，但我并未后悔。
我不想在客套的寒暄上浪费太多笔墨，我会坦白地告诉你，我写这封信给你的原因：
瑟莉娜被逮捕了，送往了大骑士领。
她是我见过最忠诚、高尚的骑士，是我的战友，也是我的挚爱。我无须多言。
你一定记得她，记得她的红发和红色的信号弹，她无论何时都能令人舒展眉头的笑声。
她那么多次为我们从死地中探寻出生路，我决不能接受她先离我们而去。
我以骑士的荣耀起誓，瑟莉娜是无辜的。她的正直刺痛了那些满心阴翳的政客与商人。
像这样一名骑士，绝不该成为政治和商业把戏的牺牲品。
如果是面对外敌，无论是乌萨斯的盾卫或是莱塔尼亚的法术骑士，我都会毫不犹豫地向敌阵发起冲锋。战斗至我的盔甲破碎，长枪折断。
但是面对国民院，面对商业联合会，我却无能为力。
玛恩纳，很抱歉打扰你平静的生活。但是我已经尝试过其他所有方法，现在我只能求助于你。
这些我无法亲自提交的证据，我恳求你替我转交，以证明她的清白。
因为你是我的朋友，因为你是“临光”。
玛恩纳，我并非出于私情才恳求你的帮助。
我只是想请求一位高尚的骑士，去拯救另一名高尚的骑士。
故友切斯柏敬上
信是打开过的，又被原样装回了信封。
和其他许多文件混在一起，收进了杂乱的柜子里。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[name="电视广播声"]  下面插播一条社会新闻。
[name="电视广播声"]  日前发生在新城区的感染者暴动，以及移动城市入口附近感染者恶意伤人、冲撞警卫事件，主要谋划者泽诺·舍尔文已于今日自首。
[name="电视广播声"]  犯罪嫌疑人为盖尔工业实行的“感染者帮扶计划”中招募的工人。本人声称是长时间对生活不满，才策划了近期的暴动......
[name="电视广播声"]  负责新城区主要建设工作的盖尔工业表示，会尽快完成受损房屋的重建以及对居民的安抚工作。
[name="电视广播声"]  并且加强治安管理，以杜绝类似事件再次发生。
[name="电视广播声"]  在此也提醒各位市民，如需出城，请做好安全防护措施。
[name="电视广播声"]  希望大家保持冷静......
[dialog]
[delay(time=0.51)]
[name="围观的路人"]  说什么给感染者提供工作，到头来全是普通人遭殃。
[name="围观的路人"]  要不是盖尔工业提供了工作，这些人已经在城外被钳兽吃了吧？还敢说对生活不满？！
[name="围观的路人"]  要我说就根本不该让他们进城，感染者没有一个好东西。
[name="围观的路人"]  现在他们进来了，就会想着把他们的同伙也带进来。看看最近这些事吧，他们连警卫都不放在眼里了！
[Character(name="avg_npc_122#2")]
[name="焰尾"]  新闻上说，他是自首的......
[Character(name="avg_npc_123#1")]
[name="灰毫"]  ......不会是他干的。
[Character(name="avg_npc_122#7")]
[name="焰尾"]  我也不愿意相信，可到底是为什么......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="bg_23_G10",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
两天前
11月27日 2:00 P.M.
茨沃涅克新城区，建设区域
[dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[delay(time=1)]
[Character(name="avg_npc_122#8")]
[name="焰尾"]  前面是死胡同！
[dialog]
[character]
[PlaySound(key="$d_gen_doorclose", volume=1)]
[delay(time=2)]
[Character(name="avg_npc_123#1")]
[name="灰毫"]  这扇门......还能挡住一些......
[Character(name="avg_npc_123#6")]
[name="灰毫"]  人很多，我没办法支撑太久......
[Character(name="avg_npc_122#7")]
[name="焰尾"]  我还是不明白，他们为什么要攻击我们？我刚刚说错什么话了吗？
[Character(name="avg_npc_123#1")]
[name="灰毫"]  不......你刚刚根本没来得及说话，这些人的行为，看起来更像是无差别袭击......
[Character(name="avg_npc_122#2")]
[name="焰尾"]  我没记错的话，我们接到的任务应该是“接触卡西米尔边境城镇中正在成形的感染者组织”，而不是“平息当地的感染者暴乱”？
[Character(name="avg_npc_123#2")]
[name="灰毫"]  大概是情报的时间差。
[Character(name="avg_npc_122#8")]
[name="焰尾"]  这是我们来到罗德岛后的第一个正式任务吧，罗德岛平时要处理的问题，都是这么困难吗？
[Character(name="avg_npc_123#3")]
[name="灰毫"]  比起在赛场上解决单一的敌人，确实是要复杂一些......
[Character(name="avg_npc_122#7")]
[name="焰尾"]  现在怎么办......迫不得已的话，先打出去？
[Character(name="avg_npc_123#3")]
[name="灰毫"]  罗德岛员工守则中写过，在外勤任务中如遇到与感染者的突发冲突，首先要保持基本的克制......
[Character(name="avg_npc_122#8")]
[name="焰尾"]  现在可不是背诵工作手册的时候吧！
[character]
[dialog]
[name="？？？"]  二位！请跟我来，往这边跑！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[Background(image="bg_indoor_n",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  ......跑到这里应该就差不多了吧，大部分人还是不知道这条还没有建好的通道的。
[Character(name="avg_npc_122#3")]
[name="焰尾"]  呼......谢、谢啦。
[Character(name="avg_npc_123#5")]
[name="灰毫"]  请问，您为什么会......
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  你们就是灰毫骑士和焰尾骑士吧！
[Character(name="avg_npc_122#6")]
[name="焰尾"]  欸？
[Character(name="avg_npc_123#5")]
[name="灰毫"]  啊？
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  灰毫骑士！我可是您的铁杆粉丝！您的每场比赛我都有看的！
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  啊，您手里拿的，就是您打败锈铜骑士时用的那门炮吧！
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  我还记得那场比赛，最后您饶了“锈铜”英格拉一命，然后对天空鸣了一炮，对不对？
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  实在是太帅了！和电视上看到的一模一样，不对，实物看起来还要更大一点。我、我可以摸一下吗？
[Character(name="avg_npc_122#1")]
[name="焰尾"]  哇，小灰，在离大骑士领这么远的地方都能遇见你的粉丝呀！
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  对了！还有焰尾骑士，我也很喜欢您！
[Character(name="avg_npc_122#1")]
[name="焰尾"]  哈哈哈......倒也不用刻意强调我啦，我不会嫉妒的。
[Character(name="avg_npc_123#1")]
[name="灰毫"]  请问，你是......？
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  抱歉抱歉，我太激动了，还没来得及自我介绍。
[Character(name="avg_npc_626_1#1$1")]
[name="热情的感染者"]  我叫泽诺。也是来茨沃涅克打工的感染者。其实准确来说，也算是一个工头吧......
[Character(name="avg_npc_122#1")]
[name="焰尾"]  我们之前听说了茨沃涅克有感染者正在成立互助会，您也是其中一员吗？
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  我不知道该怎么说......其实本来这里的感染者都只能生活在城市外。
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  前段时间，盖尔工业在这里开始建设新城区，需要很多人手，也雇佣了一些感染者进城来干活。
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  一开始，大家都觉得抢到了难得的工作机会。
[name="泽诺"]  但慢慢地，能听到的抱怨声越来越多，很多人都觉得，我们和身旁的普通人待遇差别太大。
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  虽然我们本来就不可能与普通人相比较，但就像血骑士给感染者骑士打出了一条生路那样，有些事情值得试试。
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  所以，那个时候我还很支持大家为此组织起来，向盖尔工业提出抗议。
[name="泽诺"]  可是再后来......事情就像你们看到的一样。
[Character(name="avg_npc_122#6")]
[name="焰尾"]  所以，暴动的、发动袭击的，都是盖尔工业招来的感染者？
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  不，已经不完全是了，我也不知道那里都有谁......
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]  我甚至不知道......他们是怎么想到这么多暴力手段的。
[Character(name="avg_npc_123#2")]
[name="灰毫"]  ......这根本不是办法，只会让感染者的处境越来越糟。
[Character(name="avg_npc_122#8")]
[name="焰尾"]  小灰，你有没有觉得，听起来像是有人在故意煽动......？
[Character(name="avg_npc_123#3")]
[name="灰毫"]  ......
[Character(name="avg_npc_626_1#1$1

... (全文21773字符)
```

### level_act12mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_23_G09",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]  
11月30日 8:00 P.M.
茨沃涅克城区
[name="电视新闻"]......经过本日游览，莱塔尼亚访问团高度称赞我市的繁荣景象，双方迅速达成合作共识。
[name="电视新闻"]依据协议，我市将与莱塔尼亚城市格劳菲尔德搭建稳定的贸易关系，互通有无。
[name="电视新闻"]主打莱塔尼亚特色的商业街已经于新地块动工建设，一期工程将以莱塔尼亚的音乐艺术为主题。
[name="电视新闻"]承建商盖尔工业的负责人向记者表示，在国际一流设计师把控下，建成后的商业街将成为卡西米尔独一无二的风景线。
[name="电视新闻"]该项目预计将大幅拉动我市旅游业收入......
[Dialog]
[Character(name="avg_npc_103nc_1#2",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_103nc_1#3")]
[name="瑟奇亚克"]（唔，这块切得浅了一点......）
[Character(name="avg_npc_103nc_1#3",focus=-1)]
[name="屋里的女性声音"]亲爱的？
[name="屋里的女性声音"]......把你的手工放一放吧，该去接儿子放学了。
[Character(name="avg_npc_103nc_1#1")]
[name="瑟奇亚克"]他不能自己回来吗？
[Character(name="avg_npc_103nc_1#1",focus=-1)]
[name="屋里的女性声音"]哎呀，他不就是嘴上嫌你多管闲事吗？
[Character(name="avg_npc_103nc_1#1")]
[name="瑟奇亚克"]多管闲事？哼，我堂堂贵族骑士亲自去接他......他倒是和那些小市民的孩子玩得很开心。
[Character(name="avg_npc_103nc_1#1",focus=-1)]
[name="屋里的女性声音"]忍忍吧，也就这一段时间。你自己不是说过吗？很快大家就会忘记“塑料”瑟奇亚克，也不会有人加害我们了。
[Character]
[name="电视新闻"]......下面播报一则社会新闻。旧城区再次出现感染者暴动事件，国民院已经介入调查。
[name="电视新闻"]警方承认，此前自首的感染者主谋泽诺·舍尔文已经逃脱，相关负责人已被问责。
[name="电视新闻"]各位市民如有线索......
[Character(name="avg_npc_103nc_1#1",focus=-1)]
[name="屋里的女性声音"]听到新闻了吗？你快去吧，唉。
[name="屋里的女性声音"]真没想到搬到茨沃涅克这样偏远的城市来，混进普通市民的队伍里避风头，结果还是一样不得安宁。
[name="屋里的女性声音"]以前害怕你在赛场上出事，现在害怕儿子走在路上出事......
[Character(name="avg_npc_103nc_1#2")]
[name="瑟奇亚克"]没什么好怕的，那些新闻只是危言耸听罢了。
[Character(name="avg_npc_103nc_1#1")]
[name="瑟奇亚克"]真正有威胁的势力，什么时候轮得到国民院公开调查？
[name="瑟奇亚克"]感染者只不过原本就没有稳定的身份识别码，让无能的警方不知道从何处下手追查。他们能有多大的——
[Character(name="avg_npc_103nc_1#2")]
[name="瑟奇亚克"]......
[Character(name="avg_npc_103nc_1#1")]
[name="瑟奇亚克"]......经过了那样的特锦赛，感染者当然是个好噱头，可以怂恿人们购置防护装备和人身保险。到最后都是商人的谋划罢了。
[Character(name="avg_npc_103nc_1#1",focus=-1)]
[name="屋里的女性声音"]呵呵......既然是危言耸听的话，你又为什么要全副武装地出门呢？
[Character(name="avg_npc_103nc_1#1")]
[name="瑟奇亚克"]......
[Character(name="avg_npc_103nc_1#1",focus=-1)]
[name="屋里的女性声音"]好啦，我不担心出事，我相信你，“骑士”。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_kxstreet",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=1)]
[name="茨沃涅克代表"]......到这座纪念雕塑脚底，就是中心城区的边界了。
[name="茨沃涅克代表"]外缘的地块难免老旧，恐怕没有什么能介绍给您的风景了。
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=2)]
[name="莱塔尼亚贵族"]容我好奇一下，那边是堆积成山的货箱吗？
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=1)]
[name="茨沃涅克代表"]呃，您这么说也没错......那只是一处废弃街区。
[name="茨沃涅克代表"]原本那里有通向地下层的运输通道，后来通道关闭了，也不知怎么，这些从淘汰运输载具上卸下来的旧货箱就慢慢堆起来了。
[name="茨沃涅克代表"]——当、当然啦，茨沃涅克正在大兴土木升级市容，这样的废弃街区很快就会由一流的工程企业改建，下次您就不会看到这种景象了。
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=2)]
[name="莱塔尼亚贵族"]我倒是觉得，那些五颜六色的旧货箱搭建出的城市也很漂亮。
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=1)]
[name="茨沃涅克代表"]啊，是吗？哈哈......莱塔尼亚人在艺术方面果然独具慧眼。
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=2)]
[name="莱塔尼亚贵族"]呵呵，感谢您的谬赞。
[name="莱塔尼亚贵族"]时间也不早了，如果再勉强各位陪同我参观，我心里多少有些过意不去。
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=1)]
[name="茨沃涅克代表"]哪里的话！能向您展示这座城市的夜景是我的荣幸。
[name="茨沃涅克代表"]不过，您明天还要出席剪彩仪式，是应该提早休息。
[name="茨沃涅克代表"]对了，您应该也喜欢音乐吧。我这里正好有本地销量最高的几张音乐唱片，您或许有兴趣带回酒店房间欣赏？
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=2)]
[name="莱塔尼亚贵族"]感谢您的美意，可惜今晚我已经选好了钟情的主题曲，您不觉得冒犯的话......？
[Character(name="avg_npc_223",name2="avg_npc_493_1#1$1",focus=1)]
[name="茨沃涅克代表"]呃，不会不会......
[name="茨沃涅克代表"]那我就先行告退了，请您好好休息。届时我们来接您。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[character(name="char_empty",name2="avg_npc_493_1#1$1",fadetime=0.5)]
[delay(time=1.5)]
[stopmusic(fadetime=1)]
[character(name="avg_npc_491_1#1$1",name2="avg_npc_493_1#1$1",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_npc_491_1#1$1",name2="avg_npc_493_1#1$1",focus=1)]
[name="贵族侍卫"]老爷，我已经跟这里的市民打听过了。
[name="贵族侍卫"]但现在天色这么晚了，您还要去吗？
[character(name="avg_npc_491_1#1$1",name2="avg_npc_493_1#1$1",focus=2)]
[name="莱塔尼亚贵族"]还有人在盯着我们吗？
[character(name="avg_npc_491_1#1$1",name2="avg_npc_493_1#1$1",focus=1)]
[name="贵族侍卫"]依据我的判断，暂时没有。
[character(name="avg_npc_491_1#1$1",name2="avg_npc_493_1#1$1",focus=2)]
[name="莱塔尼亚贵族"]那我们就走吧。我仍然期待这次旅行能更圆满一些。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_23_G10",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[character(name="avg_npc_006",name2="avg_npc_220",fadetime=0.7)]
[delay(time=1)]
[character(name="avg_npc_006",name2="avg_npc_220",focus=1)]
[name="粗犷的偷渡者"]感觉怎么样？
[character(name="avg_npc_006",name2="avg_npc_220",focus=2)]
[name="受伤的感染者骑士"]能怎么样，你看我的腿有好转的迹象吗？
[character(name="avg_npc_006",name2="avg_npc_220",focus=1)]
[name="粗犷的偷渡者"]这药可是我们俩的钱加在一起买来的，还是正规药店货架上拿的，真不管用？
[character(name="avg_npc_006",name2="avg_npc_220",focus=2)]
[name="受伤的感染者骑士"]唉，正规渠道买来的东西不管用也不是一次两次了......
[character(name="avg_npc_006",name2="avg_npc_220",focus=1)]
[name="粗犷的偷渡者"]那，那你要是还不能走路，我们的计划怎么办？
[character(name="avg_npc_006",name2="avg_npc_220",focus=2)]
[name="受伤的感染者骑士"]嘘......
[name="受伤的感染者骑士"]有人来了。
[Dialog]
[character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_626_1#1$1",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_626_1#1$1",focus=1)]
[name="玛恩纳"]......
[character(name="avg_npc_006")]
[name="粗犷的偷渡者"]咳，贵族老爷，您来这里有何贵干？
[name="粗犷的偷渡者"]我们都很老

... (全文35835字符)
```

### level_act12mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="31_g3_mini12_farmland",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]  
父亲的信。还是老样子，让我做些正经事。你们真的想听我念？
“......去庇护贫困者与落难者的确是骑士应行之道，但选择同行的伙伴时则应该更加谨慎。”
“不要让你该保护的人陪你一起经受苦难，也不必长久地执着于感化恶人、集合弱者。”
——听到自己被骂了，满意了吗？
他并不是觉得我们在做的事情有错，只是在他眼里不会有结果罢了。
“你要救活那些作物，只有先尽力翻动他们足下贫瘠的土地。”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="31_g5_mini12_village_n",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]	
11月30日 11:20 P.M.
茨沃涅克城外村庄
[Dialog]
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#1$1",fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]......我们这个平平无奇的小村庄，这两天倒是挺热闹的，不仅骑士团长能巡逻到这里来，贵族老爷竟然也亲自登门拜访。
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#2$1",focus=2)]
[name="托兰"]是吧，玛恩纳阁下？
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#2$1",focus=1)]
[name="玛恩纳"]......先给这个感染者一个安身处。他现在顶着感染者暴动事件主谋的罪名。
[Character(name="avg_npc_626_1#1$1")]
[name="泽诺"]先、先生，这里就是您说的，安全的地方......？您把我交给了赏金猎人？
[Character(name="avg_npc_626_1#1$1",name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]别怕，你又没什么钱，我们不至于打劫你。
[Character(name="avg_npc_626_1#1$1",name2="avg_npc_625_1#1$1",focus=1)]
[name="泽诺"]（不安地摸了摸脖子）
[Character(name="avg_npc_626_1#1$1",name2="avg_npc_625_1#2$1",focus=2)]
[name="托兰"]既然我们的骑士老爷把你带过来，那你应该知道不少消息。
[name="托兰"]你有家人吗？需不需要信使给他们传个话，叫他们逃命？
[Character(name="avg_npc_626_1#1$1",name2="avg_npc_625_1#2$1",focus=1)]
[name="泽诺"]我，呃......
[Dialog]
[Character(name="avg_npc_626_1#1$1",name2="avg_npc_625_1#2$1")]
[characteraction(name="right",type="move",xpos=-200,fadetime=1.5,block=true)]
[Character(name="avg_npc_626_1#1$1",name2="avg_npc_625_1#2$1",focus=2)]
[Delay(time=0.51)]
[name="托兰"]拿着，纸和笔。
[Dialog]
[PlaySound(key="$d_avg_paper1", volume=1)]
[Delay(time=0.7)]
[character(name="char_empty",name2="avg_npc_625_1#2$1",fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[stopmusic(fadetime=1)]
[Delay(time=1.5)]
[character(name="avg_npc_625_1#1$1")]
[name="托兰"]再看看你，玛恩纳——喔，原来你带着剑只是为了让大骑士领那些家伙看到就心烦啊。
[character(name="avg_npc_625_1#2$1")]
[name="托兰"]离开了那座城市，你反而可以连武器都不要了。
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]......
[character(name="avg_npc_625_1#1$1")]
[name="托兰"]想杀了你的人，光是我这儿的就能排一条长队。你已经傲慢到觉得自己随便用一根树枝就能打发所有人啦？
[Character(name="avg_4064_mlynar_1#6$1")]
[name="玛恩纳"]我现在就站在这里，他们怎么不动手？
[Character(name="avg_4064_mlynar_1#1$1")]
[name="玛恩纳"]......剑拿给征战骑士调整了。我是来说正事的，托兰。
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]哎，开个玩笑。我知道你们约定明天取剑。
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#2$1",focus=2)]
[name="托兰"]要是你这会儿还没想起来我们，那大家可就要伤心啦。
[Character(name="avg_4064_mlynar_1#1$1",name2="avg_npc_625_1#5$1",focus=2)]
[name="托兰"]毕竟......你就这么去见他，可能会死在那里。
[Character(name="avg_4064_mlynar_1#6$1",name2="avg_npc_625_1#5$1",focus=1)]
[name="玛恩纳"]......
[Character(name="avg_4064_mlynar_1#6$1",name2="avg_npc_625_1#5$1",focus=2)]
[name="托兰"]别这么皱着眉头看我啊，这个时间突然找过来说正事，你不会是什么都没察觉到。
[Character(name="avg_4064_mlynar_1#6$1",name2="avg_npc_625_1#5$1",focus=1)]
[name="玛恩纳"]......你知道什么？
[Character(name="avg_4064_mlynar_1#6$1",name2="avg_npc_625_1#5$1",focus=2)]
[name="托兰"]只是有些猜测，不过我们俩应该想的差不多。
[Character(name="avg_4064_mlynar_1#6$1",name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]走吧，我们走得远一点，让这个可怜人自己安安静静地给家里写信。
[Character(name="avg_4064_mlynar_1#6$1",name2="avg_npc_625_1#2$1",focus=2)]
[name="托兰"]虽然夜色这么深了，但河谷那边灯火通明的工厂还是能看见的......曾经帕伦尼斯科家族的庄园所在地，还挺值得怀念的，对吧？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_empty", name2="avg_npc_627_1#10$1")]
[Background(image="bg_coldforest",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]	
[Dialog]
[Character(name="char_empty", name2="avg_npc_627_1#10$1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#10$1",fadetime=0.7)]
[delay(time=1)]
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#10$1",focus=1)]
[name="征战骑士"]......抱歉，我看到这边有黑烟，所以赶来看看是否有火情。是不是打扰到您了？
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#2$1",focus=2)]
[name="切斯柏"]没事，只是我扔了几本笔记进去，皮革的封面烧起来味道确实不太好闻。
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#2$1",focus=1)]
[name="征战骑士"]那就好，是我多虑了。
[name="征战骑士"]还有，工匠团刚刚来人问您那把剑的事。
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#10$1",focus=2)]
[name="切斯柏"]......先放着吧。虽然有点遗憾，但那把剑的主人暂时应该不会来取了。
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#10$1",focus=1)]
[name="征战骑士"]是。那么筹备工作已经全部完成了，只待明天剪彩仪式开始。
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#1$1",focus=2)]
[name="切斯柏"]既然你过来了，就在这里坐一会儿吧，正好我也想听听你对这次行动的看法。
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#1$1",focus=1)]
[name="征战骑士"]遵命。
[name="征战骑士"]......但我只是一名普通的年轻骑士，资历尚浅，或许没有什么值得您重视的见解......
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#2$1",focus=2)]
[name="切斯柏"]没关系，我最初被前任骑士团长要求潜入莱塔尼亚的时候，也只是一名普通的年轻骑士。
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#3$1",focus=2)]
[name="切斯柏"]你在这次行动中，亲自执行的任务最多，所见的也最多，还有谁的想法会比你的更有价值呢？
[Character(name="avg_npc_624_1#1$1",name2="avg_npc_627_1#2$1",focus=2)]
[name="切斯柏"]再说，如今你可是马雷克家族的长骑，不该以普通的骑士自谦吧

... (全文23162字符)
```

### level_act12mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
玛恩纳，我不相信他们会就这样杳无音讯。你们临光家的人，不应该毫无作为。
[Dialog]
[Subtitle(text="哈，我也这么想，他们消失得挺蹊跷。", x=200, y=300, alignment="left", size=24, delay=0.04, width=500)]
[Subtitle(text="你们知道的，猎人收集的情报到大概三年前的黄金平原那边就断啦，之后没人再见过像是他们的人。", x=200, y=300, alignment="left", size=24, delay=0.04, width=500)]
[Subtitle(text="可是就算我们都这么想，你还是得回去照顾老西里尔吧？", x=200, y=300, alignment="left", size=24, delay=0.04, width=500)]
[Subtitle(text="......这几年来，我一直有一种想法。有很多人在盯着临光家。", x=680, y=300, alignment="left", size=24, delay=0.04, width=500)]
[Subtitle(text="他们嫉妒我的兄弟立下的功勋，而憎恨我这个四处作乱的游侠。", x=680, y=300, alignment="left", size=24, delay=0.04, width=500)]
[subtitle]
但你的兄长，斯尼茨他可是这一代最杰出的军事将领，我们都亲眼见过......
就算嫉妒，又有谁能否认他的能力？难道他们不想打胜仗了吗？
[Dialog]
[Subtitle(text="因为那些人觉得，已经不再需要战争了。或者说，他们不想再面对战争了。", x=680, y=300, alignment="left", size=24, delay=0.04, width=500)]
[Subtitle(text="所以，他们要雪藏最锋利的剑......顺带逼迫我回到大骑士领。", x=680, y=300, alignment="left", size=24, delay=0.04, width=500)]
[subtitle]
——但你决不能回去！
我说了，你们临光家的人，不应该毫无作为......
[Dialog]
[Subtitle(text="怎么啦，切斯柏，怎么突然这么激动，还皱着眉头？", x=200, y=300, alignment="left", size=24, delay=0.04, width=500)]
[Subtitle(text="最近又睡得不好？在担心昨天我们救走的那些人会被抓回去？", x=200, y=300, alignment="left", size=24, delay=0.04, width=500)]
[subtitle]
不，我只是......
......只是为了筹备一场刺杀，有些思虑过度。
[Dialog]
[Delay(time=1.5)]
......刺杀？
原来我是在梦中啊。
[Dialog]
[Character(name="avg_npc_627_1#10$1",fadetime=1.3)]
[Delay(time=1.7)]
[name="切斯柏"]......
[Character(name="avg_npc_627_1#6$1")]
[name="切斯柏"]动手吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_coldforest",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
12月1日 2:15 A.M.
茨沃涅克城外
[Dialog]
[Character(name="avg_npc_624_1$1",fadetime=1)]
[Delay(time=1.7)]
[name="征战骑士"]可是......
[Character(name="avg_npc_627_1#6$1")]
[name="切斯柏"]传令给潜伏在城中的哨兵，动手。
[name="切斯柏"]全员做好行军准备。
[Character(name="avg_npc_624_1$1")]
[name="征战骑士"]可是大骑士长军令在前，我们不能再擅自行动......
[name="征战骑士"]......卡瓦莱利亚基显然已经掌握了一切。
[Character(name="avg_npc_627_1#6$1")]
[name="切斯柏"]所以呢？
[Character(name="avg_npc_627_1#7$1")]
[name="切斯柏"]这几句话能折断骑士的枪吗？还是将你们搭在弦上的弩箭都化作了齑粉？
[name="切斯柏"]民众在恐慌中看到的保护者是征战骑士，这一事实能被改写吗？还是说莱塔尼亚当真露出獠牙时，监正会敢不集结军力支援？
[Character(name="avg_npc_627_1#6$1")]
[name="切斯柏"]我们该做的事，不会因为监正会的否认而改变。
[name="切斯柏"]立即行动——这是命令。
[Character(name="avg_npc_624_1$1")]
[name="征战骑士"]......抱歉，您已经......无权下令了。
[name="征战骑士"]骑士团的指挥权已经收回至监正会，此事已经同时传达各分队队长、工匠团等。
[name="征战骑士"]我们终究是为了骑士团的地位，为了征战骑士重获其应有的重视而起事......
[name="征战骑士"]大骑士长的确有权否认这一切。
[Character(name="avg_npc_627_1#6$1")]
[name="切斯柏"]......你不愿意听从吗？
[Character(name="avg_npc_627_1#14$1")]
[name="切斯柏"]那么，我亲自来传令。
[Dialog]
[Character(name="avg_npc_624_1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=255, g=0, b=0, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_knife", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=false)]
[delay(time=2)]
[name="征战骑士"]呃......您......
[Dialog]
[Character(fadetime=0.7)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[Delay(time=2)]
[Character(name="avg_npc_627_1#6$1")]
[name="切斯柏"]......给茨沃涅克城内的指令已发出，一切照原定计划行动。
[name="切斯柏"]没有异议的人，就跟我来。
[Dialog]
[Character(fadetime=1)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=1.5)]
骑士团长将染上殷红的佩剑收入鞘中，大步流星地走过驻军的营帐。
通宵待命的数十名高阶征战骑士业已列队，却只是沉默地站在他走过的路旁。
没有人出列，没有人阻拦，也没有人对他行礼。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_kxstreet",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$drift", volume=0.9)]
[Delay(time=1.5)]
[Character(name="avg_npc_222",fadetime=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Delay(time=1)]
[name="职员模样的男人"]您好，二位，由于最近事故多发，零点至早晨六点期间通过升降平台出城的载具需要接受检查，请出示识别码和相关文书。
[Character(name="avg_npc_222",focus=-1)]
[name="贵族侍卫"]给。
[Character(name="avg_npc_222")]
[name="职员模样的男人"]好的，请稍等。
[name="职员模样的男人"]另外，茨沃涅克特产香草牧兽肉干现在有售，是您旅行纪念品的不二之选。
[Character(name="avg_npc_222",focus=-1)]
[name="莱塔尼亚贵族"]不必了，谢谢。
[Dialog]
[Delay(time=1.5)]
[name="莱塔尼亚贵族"]......
[Dialog]
[Delay(time=1.5)]
他焦急地等待着，但检查人员却迟迟没有示意放行。
[name="莱塔尼亚贵族"]......您看到莱塔尼亚的纹章，还需要检查得这么仔细吗？
[Dialog]
[Character]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_arrowshot", volume=1)]
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.4, block=true)]
[PlaySound(key="$swordtsing2", volume=1)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="莱塔尼亚贵族"]——嗯？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_coldforest",screenadapt="showall")]
[Character(name="avg_npc_627_1#1$1")]
[delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[Delay(time=0.51)]
[name="切斯柏"]这个时间，已经不必考虑目击者，更不用说舆论如何。
[name="切斯柏"]如果箭矢被那名高塔术师化解，你们......允许使用投枪。
[name="切斯柏"]......不必那么担心后果，没有哪座城市还记得征战骑士出手的模样。
[Dialog]
[Character]
[Chara

... (全文38063字符)
```

### level_act12mini_st07

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_107", name2="avg_npc_101", fadetime=1)]
[Delay(time=1.2)]
[Character(name="avg_npc_107", name2="avg_npc_101#4",focus=2)]
[name="老工匠"]马丁啊，怎么感觉你这儿最近怪冷清的？
[Character(name="avg_npc_107", name2="avg_npc_101#4",focus=1)]
[name="光头马丁"]是吗？可能是玛莉娅不在，跟你们闲聊的人少了一个吧。
[Character(name="avg_npc_107", name2="avg_npc_101#4",focus=2)]
[name="老工匠"]这么一说，好像还真是。
[name="老工匠"]她也到了该出去看看的年纪啦，就是下次想起来回卡西米尔，不知道是什么时候了。
[Character(name="avg_npc_120#4")]
[name="老骑士"]你这老家伙可得好好准备，等下次她回来，你就该把工坊转让给她了。
[Dialog]
[character]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=0.7)]
[Character(name="avg_npc_107")]
[name="光头马丁"]——哎呀，好久不见的客人。
[Dialog]
[Character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_1014_nearl2_1#6$1",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_1014_nearl2_1#6$1")]
[name="玛嘉烈"]午安，各位。
[Character(name="avg_npc_101",name2="avg_1014_nearl2_1#6$1",focus=1)]
[name="老工匠"]看来我们的耀骑士终于能闲下来一点了？
[Character(name="avg_npc_101",name2="avg_1014_nearl2_1#6$1",focus=2)]
[name="玛嘉烈"]眼下事情逐渐步入正轨，我面对那些文书工作时也稍微得心应手了一些。
[Character(name="avg_npc_120#3",name2="avg_1014_nearl2_1#6$1",focus=1)]
[name="老骑士"]我早就说了，别把什么事都往自己身上揽，佐菲娅和玛莉娅又不在，你哪里应付得过来？
[Character(name="avg_npc_120#3",name2="avg_1014_nearl2_1#6$1",focus=2)]
[name="玛嘉烈"]嗯，多谢关心......的确还有许多我无法兼顾的事情，我只能尽力而为。
[Character(name="avg_npc_120#3",name2="avg_1014_nearl2_1#1$1",focus=2)]
[name="玛嘉烈"]也许是因为我离开卡西米尔太久，或者只是我从过去就对这座城市的规则不屑一顾......
[name="玛嘉烈"]现在要与这种秩序长期共处时，我才感到自己了解得还太少。
[Character(name="avg_npc_120#3",name2="avg_1014_nearl2_1#2$1",focus=2)]
[name="玛嘉烈"]......甚至有时候我会觉得，我在遭到流放之前对卡西米尔的记忆，只是被爷爷牵着手，在那一条安全的道路上看到的风景。
[Character(name="avg_npc_120#3",name2="avg_1014_nearl2_1#1$1",focus=2)]
[name="玛嘉烈"]各位，我想再问一问我离开这几年间发生的事情。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character(name="char_empty", name2="avg_npc_625_1#1$1")]
[Background(image="31_g4_mini12_village",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]	
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-100, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=100, fadetime=1.5, block=false)]
[Character(name="avg_4064_mlynar_1#3$2", name2="avg_npc_625_1#1$1",fadetime=1)]
[delay(time=1.5)]
[Character(name="avg_4064_mlynar_1#3$2", name2="avg_npc_625_1#13$1",focus=2)]
[name="托兰"]哎，真巧，咱们可算又偶遇啦，玛恩纳阁下。
[Character(name="avg_4064_mlynar_1#3$2", name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]把委托交给赏金猎人就不知去向，这样可是要被列入合作方黑名单的。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#1$1",focus=1)]
[name="玛恩纳"]......有什么事吗？
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]我嘛，就是来看看这座村子，毕竟这里的村民可是写了委托信向我们求助的。
[name="托兰"]本来今天应该是工程队到这儿开工的日子，但听说盖尔工业被调查啦，这里的土地交易也随之作废了。
[Character(name="avg_4064_mlynar_1#3$2", name2="avg_npc_625_1#1$1",focus=1)]
[name="玛恩纳"]......我看到报纸了。
[Character(name="avg_4064_mlynar_1#3$2", name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]喔，那你应该也看到......这次调查牵扯出不少企业和旧贵族，甚至让国民院为几年前的另一桩案件翻案，对吧？
[Character(name="avg_4064_mlynar_1#3$2", name2="avg_npc_625_1#2$1",focus=2)]
[name="托兰"]虽说那个时候获罪的人都已经找不到了，也没有多少看客还记得是怎么回事。
[name="托兰"]但你肯定还有印象。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#2$1",focus=1)]
[name="玛恩纳"]既然人都已经不在了，难道我还要为此而高兴吗？
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#13$1",focus=2)]
[name="托兰"]也对，我们高尚的骑士老爷，恐怕不会觉得那些家伙配得上“复仇”一词。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#13$1",focus=2)]
[name="托兰"]至于我们这些小小的赏金猎人，只是帮忙把一些人拿到的证据交给了另外一些人，也没什么值得您在意的。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#5$1",focus=2)]
[name="托兰"]只不过事情全办成了，一切都算是尘埃落定了......看在咱们的交情上，总可以问你几个问题吧？
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#5$1",focus=1)]
[name="玛恩纳"]如果是切斯柏的事情，我没有什么可说的。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#5$1",focus=2)]
[name="托兰"]嗯......我知道我们都需要时间静一静。要是你还什么都没想好，我也不会来找你。
[name="托兰"]但是，你应该猜得出来我是怎么找到你的。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#5$1",focus=1)]
[name="玛恩纳"]......我只是说，没什么可说的。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#5$1",focus=1)]
[name="玛恩纳"]如果你真的那么好奇的话......一个执迷不悟的人，对他不可实现的骑士理想喋喋不休，这就是他最后所做的事。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#5$1",focus=1)]
[name="玛恩纳"]要对此寄托哀思的话，请便。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#13$1",focus=2)]
[name="托兰"]哈，听起来......这最后的话题挺残酷的。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]不过，你都提到了，聊一聊倒也不坏。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#1$1",focus=2)]
[name="托兰"]我记得有一次，我正好撞到我们那个自学成才的医师，捡起武器送走了一个躺在战场上、受了重伤的兄弟。
[name="托兰"]我不知道他们说了什么，只看到那个医师身上溅了不少血，一副很局促的样子，我还以为他太难过啦。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#13$1",focus=2)]
[name="托兰"]但你猜他怎么回答的？
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#13$1",focus=1)]
[name="玛恩纳"]......
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#5$1",focus=2)]
[name="托兰"]他说，血太热了。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#11$1",focus=2)]
[name="托兰"]能死在相信一切充满希望、信念快要被实现的时刻，说不好是件挺幸运的事。
[Character(name="avg_4064_mlynar_1#1$2", name2="avg_npc_625_1#7$1",focus=2)]
[name="托兰"]可惜，到了现在再谈论理想，恐怕不太能让人安心地死去吧。让旁人觉得被灼伤，倒还是有一些可能。
[Character(name="avg_4064_mlynar_1#5$2", name2="avg_npc_625_1#7$1",focus=1)]
[name="玛恩纳"]灼伤？......以他那在懊丧与愤怒之中选择的偏颇的理想，有悲惨的下场也不值得同情。
[name="玛恩纳"]他的质疑，并不比我这些年想过的更多。
[Character(name="avg_4064_mlynar_1#1$2",

... (全文23264字符)
```


## 统计

- 总字符数：187203
- 对话行数：1615


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
