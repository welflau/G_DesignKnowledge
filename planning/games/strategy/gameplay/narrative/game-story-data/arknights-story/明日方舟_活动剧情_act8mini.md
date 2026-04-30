# 明日方舟 · 活动剧情 · act8mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act8mini」完整剧情脚本（6个文件，1497行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act8mini
- 脚本文件数：6

### level_act8mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_storehouse",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkalley_intro", key="$darkalley_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
5:20 P.M. 天气/晴
哥伦比亚城市，提卡伦多
我是迪伦，罗德岛近地飞行器的驾驶员，我正在城市里东奔西跑。
我应当坐在飞行器驾驶座上，手中握着操纵杆，我要在工作中面对的对象理应是地形和乱流。
而我现在手中正抓着半把全自动突击弩，我就连它的设备型号都是早上才听说的，就算只剩一半，它也还是沉得吓人。
我手心里全是汗，如果我得面对一个战场，那这个战场不应该在地面上，更不应该是在这样的哥伦比亚暗巷里。
如果我有得选，我希望自己的敌人不是......呃。
[Character(name="char_017_homura_3#1")]
[name="煌"] 迪伦，我腾不开手，帮我看看，这上面写着什么？
[Character(name="char_017_homura_3#1",focus=-1)]
[name="迪伦"] 警察，煌大姐头，是提卡伦多的“警察”。
[Character(name="char_017_homura_3#1")]
[name="煌"] 是他先动手的。
[Character(name="char_017_homura_3#1",focus=-1)]
[name="迪伦"] 但是这个证件看起来......应该不是真的，这个做工也太差了。
[Character(name="char_017_homura_3#1")]
[name="煌"] 至少他的穿着打扮确实是那么回事，跟早晨楼顶上那几个差不多，比其他没准备制服的人像话多了。
[name="煌"] 这个问题我一定得问第二次，哪里的警察会在问话的同时把全自动突击弩给开上？
[Character(name="char_017_homura_3#1",focus=-1)]
[name="迪伦"] 哥伦比亚？	
[Character(name="char_017_homura_3#1")]
[name="煌"] 别贫。你知道他不是警察，至少不是我们熟悉的那种警察。
[dialog]
[character]
我抬头看了一眼巷子对面倒下的黑衣人，再低头看了一眼自己手里的半截武器。
它在片刻之前还指着我的前胸，现在已经被硬生生砸成两截。
这位“警察”已经失去了意识，如果煌出手的时候还记得博士的指示，那他应该还能保全性命。
罗德岛代表团是昨天抵达提卡伦多市的。
不论体会过多少次，这种速度都让我这个驾驶员感到讶异——
罗德岛还在赶往大骑士领的路上，我们就已经从空中穿过了整个西部荒地，整个西部荒地诶。
根据计划，等到博士和阿米娅把事情谈妥，我们再原路飞回罗德岛本舰，大骑士领可能在这时还没完成城区组装。
我只知道罗德岛受邀在卡西米尔骑士特别锦标赛期间进行访问，但不知道具体的时间和目的，不过，按理说，肯定是越早回去准备越好。
如果不是时间紧迫，我还想请假在这座大都市待上几天......现在我是不想了。
[dialog]
[Character(name="char_016_medic")]
[name="医疗干员"] 我们......安全了吗？
[Character(name="char_017_homura_3#1")]
[name="煌"]不安全，直到离开提卡伦多之前都——甚至可能在离开哥伦比亚前都不安全。
[name="煌"]帮我看一眼这人还有没有气，如果还有，那就最好让他接下来还能继续喘气。
[Character(name="char_016_medic")]
[name="医疗干员"] 我......呜，好的。
[Character(name="char_016_medic",focus=-1)]
[name="迪伦"] 我是第一次见到这么厉害的自动弩，这种武器在哥伦比亚这么普及？
[Character(name="char_017_homura_3#1")]
[name="煌"] 这种全自动武器也算是哥伦比亚的特色了。
[Character(name="char_017_homura_3#1",focus=-1)]
[name="迪伦"] 不知道博士怎么样了......
[Character(name="char_017_homura_3#1")]
[name="煌"] 袭击刚开始的时候博士和阿米娅就先行坐车离开了，也不知道可露希尔捣鼓的那套自动驾驶系统靠不靠谱......
[Character(name="char_017_homura_3#1",focus=-1)]
[name="迪伦"] 我们这是被算计惨了，连博士和阿米娅都没料到。
[Character(name="char_017_homura_3#1")]
[name="煌"] 博士和阿米娅......他们也是人，偶尔也会有误判。
[Character(name="char_016_medic")]
[name="医疗干员"] 他们占领了酒店，就这样抢走了我们留下的药物样品......
[Character(name="char_017_homura_3#1")]
[name="煌"] 算了，先不管那些。
[name="煌"] 我们得先想办法安全转移，得离开这个城市。
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=2)]
[Character(fadetime=0.5)]
[delay(time=1)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="？？？"] 到现在，我们失去了一切，但是你依然没有站在我身边。
[name="？？？"] 那么你所做的一切，又是为了什么？
[name="？？？"] 或许，只是为了留下一点点希望？
[name="？？？"] 可是，希望？
[name="？？？"] 希望？
[name="？？？"] 你知道吗，怀揣希望是一件非常残酷的事情。
[name="？？？"] 当你发现一切无法挽回，当你发现自己无能为力，当你面对走投无路的困境时。
[name="？？？"] 希望足以逼疯一个至善之人。
[dialog]
[Decision(options="但是......", values="1")]
[Predicate(references="1")]
你想说什么，但是你发现无法控制自己的身体。
你仿佛漂浮在虚空，眼前的一切如此熟悉，又如此遥远。这些记忆，属于你的一部分记忆，像是碎片一样，和你一起漂浮。
你与无穷的思绪一起就这样漂浮着，看着眼前那位熟悉的女性逐渐远去。
你睁开眼睛，眼前是一望无际的岩漠，以及一顶丑陋的，古怪的铁桶头盔。
一个造型诡异的男人正看向你这边，你无法透过那顶粗糙的桶状头盔，看到他的表情。
[dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
10:43 A.M. 天气/晴 
加斯帕荒原
[dialog]
[Character(name="avg_npc_208")]
[name="坎诺特"] 早上好，中午好，以及晚上好，朋友。
[name="坎诺特"] 能说话么？
[dialog]
[Character(name="avg_npc_208",focus=-1)]
[Decision(options="你？你是哪位？这里是？", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_208")]
[name="坎诺特"] 这位朋友醒了，小兔子。
[dialog]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"] 博士！
[dialog]
[character]
你感觉自己的腰部被人紧紧地抱住。
在感受这个温暖的拥抱之前，背后岩石坚硬的触感与头部的阵痛依然在提醒着你，很多事情尚且没有结束。
[dialog]
[Character(name="char_002_amiya_1#4")]
[name="阿米娅"] 太好了！你醒了......我还在担心你要是醒不过来该怎么办......
[name="阿米娅"] 你还好吗？有没有什么地方不舒服？
[dialog]
[Character(name="char_002_amiya_1#4",focus=-1)]
[Decision(options="没事......只是头有点痛。;......没有大碍。;我还没那么脆弱。", values="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"] 头痛？是撞到了吗？让我看一下喔。
[dialog]
[Predicate(references="2")]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"] 博士，真的没有问题吗？需要我扶你起来吗？
[dialog]
[Predicate(references="3")]
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"] 博士......你还是要谨慎一点，你的身体状况可没那么好。
[dialog]
[Predicate(references="1;2;3")]
[Character(name="avg_npc_208")]
[name="坎诺特"] 别担心，小兔子，这位“博士”没什么问题，至少物理层面没什么问题。
[name="坎诺特"] 精神层面上就不好说了。你刚才嘟囔着说了不少梦话，不过别担心，我没有仔细听。
[dialog]
[Character(name="avg_npc_208",focus=-1)]
[Decision(options="......您是？", values="1")]
[Predicate(references="1")]
[Character(name="avg_npc_208")]
[name="坎诺特"] 啊，忘记自我介绍了，真是不好意思。
[name="坎诺特"] 如您所见，我是个商人。
[name="坎诺特"] 你可以叫我坎诺特，也可以叫我古德英纳夫先生，你怎么开心怎么来。
[name="坎诺特"] 实话说，朋友，刚才那个可真是太刺激了，这年头不是每天都能看到有人从悬崖上飞下来做源石技艺表演，非常优秀。 
[dialog]
[character]
[Decision(options="悬崖上？我们之前......;......可露希尔的自动驾驶系统可能有点问题......", values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"] 这里应该是在哥伦比亚荒地......东侧荒地。
[Character(name="avg_npc_208")]
[name="坎诺特"] 没错，小兔子，这里是加斯帕荒原，你们的运气还算不错。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"] 运气？
[Character(name="avg_npc_208")]
[name="坎诺特"] 是啊，运气不错，你们要是再向南多开两公里，那边可是毒气沼泽区，车陷进去就真的别想出来了。
[dialog]
[Character(name="avg_npc_208",focus=-1)]
[Decision(options="不知道其他人怎么样了。;......;其他人呢？", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"] 其他干员和我们分头行动了，我相信煌有办法保护他们......
[name="阿米娅"] 但是我们没办法和他们取得联系，也没办法和其它办事处取得联系。
[dialog]
[Character(name="char_002_

... (全文41182字符)
```

### level_act8mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
4:11 P.M. 天气/阴 能见度十公里
罗德岛本舰，医疗舱
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Dialog]
[delay]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_infirmary",screenadapt="coverall")]
[Character(name="char_003_kalts_1#1",fadetime=0,block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=4, block=true)]
[name="凯尔希"]可以把电极片取下来了。
[dialog]
[Decision(options="结果怎么样？;......;我的脑袋又热又胀，很不舒服。", values="1;2;3")]
[Predicate(references="1;2")]
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]并没有什么新的进展。
[Predicate(references="3")]
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]休息一会，这些症状会很快消失。
[Predicate(references="1;2;3")]
[name="凯尔希"]Dr.{@nickname}，这一个多月里，我对你的大脑进行了七次扫描，每一次结果都大同小异。
[name="凯尔希"]你的内侧颞叶并没有问题，而你其他脑区的神经元也和大多数年轻人一样活跃。
[Character(name="char_003_kalts_1#1")]
[name="凯尔希"]所以，根据我的判断，接下来你不必频繁地前来医疗舱接受这些令你不适的检测了。
[dialog]
[Decision(options="那我的记忆是怎么回事？", values="1")]
[Predicate(references="1")]
[name="凯尔希"]毫无疑问，你失去了很多记忆——哪怕是你，也无法通过精心伪装来操控所有的检测结果。
[name="凯尔希"]那些记忆是情节性的，关于你对自己身份的主观意识，更关于你在切尔诺伯格的石棺内沉睡之前的所有经历。
[name="凯尔希"]与之相对，你的程序记忆恢复得极快。
[name="凯尔希"]无论是依据阿米娅和杜宾的报告，还是我的观察，这个结论是明确的。
[name="凯尔希"]你在切尔诺伯格事件中表现出来的战地指挥能力并不比以前逊色多少。
[dialog]
[Decision(options="为什么会这样？;......;这么说，我还有用？", values="1;2;3")]
[Predicate(references="1")]
[name="凯尔希"]记忆损伤的原因有很多种，有些是不可抗力，有些却是主观的。
[name="凯尔希"]医学检测手段只能排除器质性的病变。
[Predicate(references="2")]
[name="凯尔希"]当然，你远比过去沉默。
[name="凯尔希"]考虑到你的语言中枢并未受损，我只能猜测，情节性记忆的缺失令你的性格发生了一些变化。
[Predicate(references="3")]
[name="凯尔希"]你对罗德岛的意义远不止有用那么粗浅。
[name="凯尔希"]即使你真的丧失了全部记忆，成为了一个懵懂的普通人，阿米娅也不会后悔救你，罗德岛上也永远有你的容身之所。
[Predicate(references="1;2;3")]
[name="凯尔希"]无论如何，我相信，你保有的技能将如过去那样发挥关键作用。
[dialog]
[Decision(options="我想帮到你。;我想帮到阿米娅。", values="1;2")]
[Predicate(references="1;2")]
[name="凯尔希"]我知道。
[name="凯尔希"]而且我也看到了你的努力。
[name="凯尔希"]离开龙门之后，我们这段时间都行驶在荒地上，干员们需要休整的机会，阿米娅也能适当休息。
[Character(name="char_003_kalts_1#4")]
[name="凯尔希"]你同样需要喘口气，不是吗？
[dialog]
[Decision(options="我是想要一点时间来适应。;......;我还不想在这里止步。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_003_kalts_1#1")]
[name="凯尔希"]有PRTS帮助你，想必你用不了多少时间就能适应罗德岛上的工作。
[name="凯尔希"]然而我不希望你逼迫自己。
[name="凯尔希"]从一场巨大的灾难中艰难归来的，不止罗德岛，还有你，Dr.{@nickname}。
[name="凯尔希"]你身体的指征基本恢复了正常，可你的记忆依旧受损，你的精神状态也称不上稳定。
[Character(name="char_003_kalts_1#2")]
[name="凯尔希"]作为一名病人，操劳过度对你来说没好处。
[dialog]
[Decision(options="你也是病人。;阿米娅也是病人。", values="1;2")]
[Predicate(references="1")]
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]我？多谢关心。
[Character(name="char_003_kalts_1#1")]
[name="凯尔希"]我不能说自己习惯了矿石病，但我向你保证，我一定是最后需要担心的那一个。
[Predicate(references="2")]
[name="凯尔希"]阿米娅知道你担心她，她最近比以前更关注自己的身体了。
[name="凯尔希"]我不得不承认，有些话由你说出来，确实比我来说更有用。
[Predicate(references="1;2")]
[name="凯尔希"]Dr.{@nickname}，你在短短一个月内就接手了舰内各部门的人员调配工作。
[name="凯尔希"]除此以外，我也经常看到你和作战干员一起回顾过去的战斗，并进一步探讨战术优化的可能性。
[name="凯尔希"]就算是在接受检查的刚才，你也不曾停下阅读。你看的是前几天刚报到的新干员提交的每日简报吧？
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]而且，我看过你的笔记。
[name="凯尔希"]那些关于干员们最琐碎的细节的记录，思考战术时偶然间的灵光一现......
[name="凯尔希"]以及罗德岛业务效率的计算公式，乃至我看不出意义的涂鸦，都是你投入工作的明证。
[name="凯尔希"]虽然大部分任务都能依靠PRTS辅助完成，但我想这是你更喜欢的工作方式。
[dialog]
[Decision(options="只是理清思路的方式。;PRTS上的数据缺了点人情味。;你没看到我对你的抱怨吧？！", values="1;2;3")]
[Predicate(references="1")]
[name="凯尔希"]随着笔记厚度增加，你的思路的确有所进步。
[Predicate(references="2")]
[name="凯尔希"]PRTS只是工具。不过度依赖工具，是工作的好习惯。
[Predicate(references="3")]
[name="凯尔希"]原来那是抱怨？我更乐意把那些话当成你对我的夸奖。
[Predicate(references="1;2;3")]
[name="凯尔希"]你的各方面能力都在迅速地恢复，这不止是你的技能记忆得到了保留的缘故，更是由于你非同一般的努力。
[name="凯尔希"]有意识地锻炼将会帮助你的大脑迅速回到沉睡之前的状态，甚至有可能令你的记忆比我预期的更快恢复。
[dialog]
[Decision(options="你希望我尽快恢复吗？", values="1")]
[Predicate(references="1")]
[name="凯尔希"]我是你的医生，没有医生不希望病人早日康复。
[name="凯尔希"]只是，如果你因为拼命工作而累倒了，阿米娅的状态也会受到影响。
[dialog]
[Decision(options="你只关心阿米娅？;......;我知道了，你关心我。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]偶尔流露的这种情绪使你与过去的你有很大不同，这一点很有趣，但如果你展现情绪的对象是我，那就没什么必要。
[name="凯尔希"]我对你说过很多次，确保你的身心健康始终是我的职责之一。
[Character(name="char_003_kalts_1#4")]
[name="凯尔希"]所以，是的，即便不是在战场上，而是在这里，我也关心着你。
[dialog]
[Decision(options="真稀奇，你会这么和我说话。;......;好。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Character(name="char_003_kalts_1#2")]
[name="凯尔希"]今天的检查已经结束。
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]正如我之前说的，下周同一时间，你不用再来这里报到。
[name="凯尔希"]每天上午和晚上的定时检查还要持续一段时间。Lancet-2会替我照看你。
[name="凯尔希"]一旦发现你的生理状态不支持你继续工作，你就必须立刻回到医疗舱。
[name="凯尔希"]现在，你能回去工作了，博士。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_corridor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
4:32 P.M. 天气/阴 能见度七公里
罗德岛本舰，舰桥外走廊
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="char_183_skgoat_1",fadetime=1.5)]
[delay(time=3)]
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=1)]
[name="领航员A"]地灵小姐，你怎么来了？
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=2)]
[name="地灵"]上午提交的地质监测报告，我更新了下。
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=1)]
[name="领航员A"]这么快就有更新？地灵小姐，这可不像你啊。
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=2)]
[name="地灵"]数据变化很快。否则的话，我也不至于错过午觉。
[name="地灵"]麻烦把报告交给你们组长。最下面有我的建议。
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=1)]
[name="领航员A"]好的。大风预警是吧？
[name="领航员A"]没问题，工程部门提前两天加固了防风板，后勤人员也已经通知了各位干员远离甲板风险区。
[stopmusic(fadetime=2)]
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=2)]
[name="地灵"]不止。你往下看。
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[name="领航员A"]呃......航线前方可能出现强风暴？建议降速行驶或者绕行？
[name="领航员A"]地灵小姐，你说的这个风暴，灾害等级有多高？
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=2)]
[name="地灵"]......我不知道。
[name="地灵"]我只是基于数据的异常提出了一个可能性。我观测到，前方不止一个气旋正在生成，而且增强速度超出预期。
[Character(name="avg_npc_088",name2="char_183_skgoat_1",focus=1)]
[name="领航员A"]这个结论会不会太模糊了一些。
[name="领航员A"]这条路线是在一个月前定下的，经过了各方的批准确

... (全文31416字符)
```

### level_act8mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 故事集3
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_indoor4",screenadapt="coverall")]
[Character(name="avg_npc_026", name2="char_014_riope")]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  我押三百，那只是一堆破铜烂铁，不值得大费周章。
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  是么？那我押五百，那个东西对我们是有意义的。
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  根据呢？
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  直觉。
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  可被天灾刮出来的废旧机械设备在荒地上并不罕见。
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  但直觉告诉我，那个东西不是一般货色。
[Dialog]
[character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[Character(name="avg_npc_048", fadetime=1)]
[delay(time=1)]
[name="博士"]  你们在聊什么？
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  唔，博士。
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  晚上好，Dr.{@nickname}。
[name="Scout"]  昨天出勤的时候，我们去了一个流民聚落，结果发现一个相当有意思的玩意儿。
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  只是个工业垃圾，我在西部荒地见过很多，不用博士费心了。
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  但这个工业垃圾甚至还能运作，似乎在播放某种声音。
[Character(name="avg_npc_048")]
[name="博士"]  ......音乐吗？
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  我很难说那种声音是音乐。
[Character(name="avg_npc_048")]
[name="博士"]  当时是怎样的状况？
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  ......那个流民聚落中间摆着一台奇怪的机器，涂满了红色的油漆，很重，只要有人靠近就会发出奇怪的声音。
[name="Scout"]  流民们不太敢靠近，但还是围绕它建立了营地。
[name="Scout"]  当时应该搬回来看看，说不定凯尔希女士能知道技术细节呢。
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  花钱买一团工业垃圾回来？我们何时这么有闲情逸致了？
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  说不定那个女妖会喜欢。
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  ......如果你们有什么私人矛盾需要解决，我建议不要带到工作中来。
[Character(name="avg_npc_048")]
[name="博士"]  听起来是挺有趣的。
[name="博士"]  如果有一天，我们可以一起去那个流民聚落看看，说不定我能知道是什么。
[Character(name="avg_npc_026", name2="char_014_riope", focus=2)]
[name="Ace"]  哦，看来我们的赌注能看到结果了。
[Character(name="avg_npc_026", name2="char_014_riope", focus=1)]
[name="Scout"]  那一言为定，等殿下这边的事情告一段落，我们一起去。
[name="Scout"]  可别赖账。
[StopMusic(fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_room_2",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$phonevibration",volume=0.6)]
[delay(time=1)]
在一阵并不悦耳的机械声中，你醒了。
普通的一天。
你眼前所见的是罗德岛标准居住舱室的天花板，陈设看起来很标准，但通风系统的声响比起其它舱室都要更低沉。
这是你的诸多特殊之处中最不起眼的一项，你知道其中的原因。 
简单的洗漱，这部分和普通人一样。为了维持身体状态而服用的特配药物，这部分和普通人不太一样。
接下来是特制的全身防护服，它会带来活动上的不便，但考虑到你的身体情况，这很有必要。也许是暂时的，这要看你的恢复情况。
这些全部是凯尔希医生的嘱咐，根据她的说法，过去，这些事情你自己比她更清楚，但现在，只有她可以确保你的健康。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="bg_graduate",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]  当然，Dr.{@nickname}。你和他不一样。
[name="凯尔希"]  谁才是我们的同类？
[name="凯尔希"]  ......谁才是你的同类？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_room_2",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
这片大地对你并不友善，你知道这一点。
[dialog]
[Character(name="char_002_amiya_1#2",fadetime=1)]
[delay(time=1)]
[name="阿米娅"]  啊，博士，你醒了。
[name="阿米娅"]  你其实可以多休息一会，熬夜熬到那么晚。
[Character(name="char_002_amiya_1#2",focus=-1)]
[Dialog]
[Decision(options="今天不督促我工作啦？;......没什么问题。;没事，我精神得很。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Predicate(references="1")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  博士......我也不是每天都在督促你工作喔，该休息时还是一定要休息的。
[Predicate(references="2")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  嗯......凯尔希医生说，你现在需要保持充足的睡眠，得比平时多睡一会。
[Predicate(references="3")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  真的么......博士，你这么精神，我反而有点担心。
[Predicate(references="1;2;3")]
[Character(name="char_002_amiya_1#6")]
[name="阿米娅"]  啊，对了，凯尔希医生今天出去了，她让我转告博士，会议推迟到明天了。
[Character(name="char_002_amiya_1#6",focus=-1)]
[Dialog]
[Decision(options="嗯？意思是今天的日程安排里就没什么事了？;难道我可以休假了吗？", values="1;2")]
[Predicate(references="1;2")]
[Character(name="char_002_amiya_1#3")]
[name="阿米娅"]  是，今天博士就好好休息一下吧。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=3)]
[Decision(options="休息吗......;......;真是奢侈的单词。", values="1;2;3")]
[Predicate(references="1;2;3")]
[delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_canteen",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
7:33 A.M.   
罗德岛食堂
[dialog]
[Character(name="char_124_kroos_1", name2="avg_123_fang_1",fadetime=0.7)]
[delay(time=0.7)]
[Character(name="char_124_kroos_1", name2="avg_123_fang_1", focus=2)]
[name="芬"]  啊，博士！早上好。
[Character(name="char_124_kroos_1#2", name2="avg_123_fang_1", focus=1)]
[name="克洛丝"]  咦？啊，是博士~
[Character(name="char_124_kroos_1#2", name2="avg_123_fang_1", focus=-1)]
[Dialog]
[Decision(options="早上好。", values="1")]
[Predicate(references="1")]
[Character(name="char_124_kroos_1#2")]
[name="克洛丝"]  真难得，博士你居然有时间来食堂吃早饭，今天终于没那么忙了？
[Dialog]
[Decision(options="是......今天可以稍微休息一下。;......;我平时一直很忙吗？", values="1;2;3")]
[Predicate(references="1;2;3")]


... (全文26538字符)
```

### level_act8mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[character(name="avg_npc_056",fadetime=1.5)]
[name="特蕾西娅"]“Dr.{@nickname}”？
[name="特蕾西娅"]你是说，你们在很久、很久以前就认识了？
[name="特蕾西娅"]不必担心，我只是有点紧张。毕竟，你认识博士比认识我还早，我想在博士面前留下个好印象嘛。
[name="特蕾西娅"]只是啊，凯尔希，对于现在的“博士”是什么样的人，你也有些疑惑吧？你都写在脸上啦。
[name="特蕾西娅"]让我也认识一下吧，凯尔希。我很好奇，那个与你的过去息息相关的“博士”，究竟是什么样的人。
[name="特蕾西娅"]以及如何去看待，如何相处，如何将我、将萨卡兹与之相连......这都是必须由我自己判断的事。
[name="特蕾西娅"]我的看法，也能对你有所影响吧？
[name="特蕾西娅"]所以，凯尔希啊，请带我去见见博士吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_056",fadetime=1.5)]
[delay(time=2)]
[name="特蕾西娅"]Scout，辛苦了。
[Character(name="avg_npc_026")]
[name="Scout"]只是一次侦查任务，我应该做的。
[character(name="avg_npc_056")]
[name="特蕾西娅"]嗯......凯尔希和博士在哪里？
[Character(name="avg_npc_026")]
[name="Scout"]......会议室，有什么情况吗？
[character(name="avg_npc_056")]
[name="特蕾西娅"]我们在军事委员会的间谍已经传回了情报。他们并不打算给我们任何喘息的余地。
[name="特蕾西娅"]......很遗憾。
[Character(name="avg_npc_026")]
[name="Scout"]间谍......是指那位血魔亲王吗？殿下，我认为她所信仰的只有大君，并不可信。
[name="Scout"]他们大都是牟取自身利益的投机者，若非形势所迫，她甚至不会参与战争......
[character(name="avg_npc_056")]
[name="特蕾西娅"]当然，我明白你的疑虑，Scout。
[name="特蕾西娅"]不过至少现在，她是不会对我撒谎的。她还没有那个勇气。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_056",fadetime=1.5)]
[delay(time=2)]
[name="特蕾西娅"]凯尔希？博士？你们在忙吗？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......殿下。会议已经结束了吗？
[character(name="avg_npc_056")]
[name="特蕾西娅"]......嗯，并不是什么愉快的结果。
[name="特蕾西娅"]我打扰你们的工作了吗？对了，难得在午餐之前就开完了会议，凯尔希，想不想和我一起吃午饭？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......时间还很早。
[character(name="avg_npc_056")]
[name="特蕾西娅"]嗯？啊......似乎确实早了一些。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]不，只是和平时相比，你来得太早了。
[name="凯尔希"]很难想象议长室里坐着的那些人会这么轻松就放你出来，除非，那个结果糟糕到不需要讨论。
[name="凯尔希"]哪怕是这样，你来得还是......太早了些。
[character(name="avg_npc_056")]
[name="特蕾西娅"] 是啊......但我们对现状......早有预料，不是吗？
[Character(name="char_003_kalts_1")]
[name="凯尔希"]所以，交谈并不顺畅。并且我猜情况更糟，几乎到了一触即发的地步。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]发生什么了？
[character(name="avg_npc_056")]
[name="特蕾西娅"]军事委员会获得了更大的支持，我们在卡兹戴尔的信息渠道在不断减少。
[character(name="avg_npc_056")]
[name="特蕾西娅"]巴别塔很可能会在这个秋天遭到一次围剿。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]一些萨卡兹背叛了我们，这是意料之内的事情。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]......但巴别塔还没有彻底做好准备。
[character(name="avg_npc_056")]
[name="特蕾西娅"]抱歉，凯尔希。看起来，我们没有机会坚持到那一天了。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]那食腐者之王和其余王庭成员的态度......
[character(name="avg_npc_056")]
[name="特蕾西娅"]只不过是提出更加苛刻的要求，放心吧，凯尔希，他们只是针对我。
[character(name="avg_npc_056")]
[name="特蕾西娅"]但是......我们已经没有更多的余裕去对付更多的质疑。
[Character(name="avg_npc_048")]
[name="博士"]特蕾西娅。
[character(name="avg_npc_056")]
[name="特蕾西娅"]怎么了，博士？啊......对了，我还没正式征求过意见，这样贸然发出指令太失礼了。
[character(name="avg_npc_056")]
[name="特蕾西娅"]博士，看来我们必须离卡兹戴尔更远一些。这会是一次全面的转移，或者说，撤退。
[character(name="avg_npc_056")]
[name="特蕾西娅"]你有什么别的意见吗？
[Character(name="avg_npc_048")]
[name="博士"]也许这是唯一的选择。
[character(name="avg_npc_056")]
[name="特蕾西娅"]......可能的话，我也想给予所有人更多的选择。但现在没有时间了。
[character(name="avg_npc_056")]
[name="特蕾西娅"]军事委员会的想法过分激进和直接，我坚持反对他们的理念。但为了阻止卡兹戴尔发生无谓的牺牲，我们唯有暂时离开。
[character(name="avg_npc_056")]
[name="特蕾西娅"]我相信——至今相信，我们仍共用同一心脏，同一血脉。但是相融的血脉也会暂时分开，不知道什么时候才会再次合流。
[character(name="avg_npc_056")]
[name="特蕾西娅"]至少现在，分开是损伤最少的选择。
[Character(name="avg_npc_048")]
[name="博士"]每个萨卡兹人都有跟随自己信念的渴望。我能感受到你的理想，也会有众多萨卡兹人追随你。
[name="博士"]但我不会帮你做出选择，我只会见证。
[Character(name="char_003_kalts_1#3")]
[name="凯尔希"]......
[character(name="avg_npc_056")]
[name="特蕾西娅"]嗯，这是目前最好的安排了，Dr.{@nickname}。
[character(name="avg_npc_056")]
[name="特蕾西娅"]好了，事不宜迟，二位也赶快收拾行李准备出发吧！
[Character(name="avg_npc_048")]
[name="博士"]能带走多少东西？
[character(name="avg_npc_056")]
[name="特蕾西娅"]很遗憾，并不多。许多设施都可能要遗弃，阿斯卡纶会为我们拖延时间。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]已经足够了，特蕾西娅，不用派更多的人手来帮助我们，我会带着博士和你安全会合。
[character(name="avg_npc_056")]
[name="特蕾西娅"]那么就和之前预演的方案一样，凯尔希，负责人稍后就到。
[character(name="avg_npc_056")]
[name="特蕾西娅"]不过，博士，凯尔希，很抱歉让你们这样匆忙撤离。
[character(name="avg_npc_056")]
[name="特蕾西娅"]这些研究也只能暂时搁置了......我也多么希望能看到这些研究得出丰硕的成果。
[character(name="avg_npc_056")]
[name="特蕾西娅"]我会努力创造出能够继续进行研究的空间。还有......
[character(name="avg_npc_056")]
[name="特蕾西娅"]我相信事情会有所转机。
[dialog]
[character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=2)]
[Character]
[Background(image="bg_barracks",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
十三天后
卡兹戴尔边境，巴别塔驻扎营地，“Dr.{@nickname}营所”
[dialog]
[PlaySound(key="$bottlebroken", volume=1)]
[delay(time=1)]
[Character(name="avg_npc_048")]
[name="博士"]......谁？
[Dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$swordtsing1", volume=0.5,delay=0.05)]
[PlaySound(key="$swordtsing1", volume=0.4,delay=0.075)]
[PlaySound(key="$swordtsing1", volume=0.3,delay=0.1)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.05, block=true)]
[Character(name="avg_npc_048", name2="avg_npc_054",focus=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.05, block=true)]
[characteraction(name="right", type="move", xpos=-150, fadetime=0.3, block=

... (全文21613字符)
```

### level_act8mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=2)]
[Background(image="bg_black",screenadapt="coverall")]
[name="？？？"]我的说辞并不重要。于每刻践行自己的意志，才算是真正地活着。
[name="？？？"]去亲历这片大地吧。独属于你的思想，需要岁月来浇铸。
[name="？？？"]凯尔希，我希望你......
[dialog]
[delay(time=3)]
5:39 P.M. 天气/晴 
室外，罗德岛甲板
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[Image(image="avg_ac8mi_sidebyside_dusk",y=-180,fadetime=0,xScale=1.5,yScale=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=false)]
[ImageTween(xScale=1.5,yScale=1.5,yFrom=-180, yTo=-150, duration=20,ease="OutQuad",block=false)]
[delay(time=2)]
[name="凯尔希"]最近很忙吧，有许多需要处理的事。
[name="凯尔希"]适当休息也是必要的，你的生理指标近期有一些小的波动，我会持续关注。
[name="凯尔希"]对了，煌会在今晚来向你作简报，她主导了昨天的突袭作战。
[dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image]
[Background(image="bg_rhodescom",screenadapt="coverall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.7, fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
1:23 A.M. 天气/雨 
巴别塔临时作战指挥室
[dialog]
[delay(time=0.51)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[Character(name="char_003_kalts_1")]
[name="凯尔希"]门外是Scout，他负责了昨夜的行动。
[name="凯尔希"]这是他效力于巴别塔后少有的任务失败记录。
[Character(name="avg_npc_048")]
[name="博士"]请进。
[dialog]
[character]
[playsound(key="$dooropenquite")]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_026",fadetime=1.5)]
[delay(time=2)]
[name="Scout"]指挥官，女士，你们都在。我简短说明一下昨晚的事。
[name="Scout"]小队清扫战场时，发现了可追踪的敌军痕迹。我判断这是摸清敌军位置的机会，执意循迹追击而中了埋伏。
[name="Scout"]责任在我，我愿接受军事处分。
[Character(name="avg_npc_048")]
[name="博士"]这不是一个老萨卡兹雇佣兵会做出的决断。
[character(name="avg_npc_026")]
[name="Scout"]很可惜，那一刻我的经验并没有对我做出警示。
[Character(name="avg_npc_048")]
[name="博士"]经验不会被没发生的事唤醒。危机发生后，没有队员战死，说明撤退时你的指挥冷静、得当。
[name="博士"]你应当得到表彰，而非处分。
[character(name="avg_npc_026")]
[name="Scout"]我不明白这个结论是如何得出的。
[Character(name="avg_npc_048")]
[name="博士"]军队的纪律若不能做到赏罚分明，则失去存在的意义。Scout，这个道理你一定明白。
[name="博士"]为什么那样在乎她的名誉？我需要一个理由。
[character(name="avg_npc_026")]
[name="Scout"]......凯尔希女士，瑞卡的情况怎么样了。
[Character(name="char_003_kalts_1")]
[name="凯尔希"]她已经脱离了危险。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_026")]
Scout想开口说些什么，却欲言又止。
[dialog]
[Character(name="avg_npc_048")]
[name="博士"]你的内心在斗争着。即使在战场上，也未见你如此为难过。若能说出你的考虑，或许我们可以......
[character(name="avg_npc_026")]
[name="Scout"]我坚持不让瑞卡受到任何处分。
[Character(name="avg_npc_048")]
[name="博士"]因为她是个孤儿？军队的纪律可承载不了泛滥的同情心。
[character(name="avg_npc_026")]
[name="Scout"]瑞卡的父亲曾是萨卡兹雇佣兵，死于内战。
[Character(name="avg_npc_048")]
[name="博士"]这在卡兹戴尔不算什么新鲜事。
[character(name="avg_npc_026")]
[name="Scout"]瑞卡的母亲身患严重的矿石病，没有抚养她的能力。特蕾西娅殿下知晓此事后，一直为她们家提供经济上的资助。
[Character(name="avg_npc_048")]
[name="博士"]这也没什么特别的。如果没有更充分的理由......
[character(name="avg_npc_026")]
[name="Scout"]瑞卡参军仅是为了报答殿下的恩情。
[name="Scout"]她曾对我说，为殿下而战是她唯一的愿望，是她生命的全部......
[Character(name="avg_npc_048")]
[name="博士"]请说下去，Scout，我在听。
[character(name="avg_npc_026")]
[name="Scout"]......在卡兹戴尔，孩子们难有什么愿望，也难有想守护的事物。
[name="Scout"]他们只是被卷入战争，而后战死。
[Character(name="avg_npc_048")]
[name="博士"]所以你希望保留瑞卡的名誉，延续她守护殿下的愿望。
[dialog]
[character]
Scout没有回答，身经百战的老兵又回归了沉默。
博士缓缓起身，伸手拍了拍Scout的肩膀。这是凯尔希没有预料到的。
[Character(name="avg_npc_048")]
[name="博士"]若刚才有任何冒犯，请原谅，我知道你一定会有很好的理由。
[name="博士"]我的决定是，没有人会受到处分。但这样的处理结果是对军纪的损害，必定会招致非议。
[name="博士"]Scout，我希望你和你的小队在未来用行动回应质疑。
[character(name="avg_npc_026")]
[name="Scout"]一定。指挥官，女士，我先回去了。
[Character(name="avg_npc_048")]
[name="博士"]走之前答应我一件事。请至少把自己的生命和名誉，放在与其他队员同等的高度上。
[character(name="avg_npc_026")]
[name="Scout"]我会的。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="bg_black",screenadapt="coverall")]
[delay(time=1)]
[delay(time=1)]
[Image(image="avg_ac8mi_sidebyside_dusk",y=-150,fadetime=0,xScale=1.4,yScale=1.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=false)]
[ImageTween(xScale=1.4,yScale=1.4,yFrom=-150, yTo=-100, duration=20,ease="OutQuad",block=false)]
[delay(time=2)]
[name="凯尔希"]......此外，可露希尔或许会找你商讨伦蒂尼姆的问题，她很关心我在这件事上的立场。
[name="凯尔希"]你可以和她多分享一些决策过程，毕竟她也是潜在的作战成员。
[name="凯尔希"]当然，你们也可以......聊些别的。
[dialog]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[Background(image="bg_lungmencommand",screenadapt="coverall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.7, fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Delay(time=1)]
11:27 A.M. 天气/晴 
罗德岛总工程师办公室
[dialog]
[Character(name="char_003_kalts_1#2",name2="char_007_closre_1",fadetime=0.5)]
[delay(time=0.51)]
[Character(name="char_003_kalts_1#2",name2="char_007_closre_1",focus=1)]
[name="凯尔希"]这次又是什么事。
[Character(name="char_003_kalts_1#2",name2="char_007_closre_1",focus=2)]
[name="可露希尔"]凯尔希，去伦蒂尼姆的事有定论了吗？
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"]仍在讨论，行动本身确实存在风险。为什么突然关心这个。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"]担心你心情不好呗。我清楚你心底一定想去，却要考虑罗德岛面临的危险。
[name="可露希尔"]纠结的时候可是最消耗精力的。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"]不存在纠结，罗德岛的安全永远在首位。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"]如果哪天你能随心做想做的事该多好。
[name="可露希尔"]这事可瞒不过我，凭你与特蕾西娅的友谊，伦蒂尼姆的事你无法置身事外。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=1)]
[name="凯尔希"]与殿下无关。我只关心行动本身对罗德岛的利弊。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#6",focus=2)]
[name="可露希尔"]你就是这样，总把责任挂在嘴边，至少偶尔也该关心一下自己。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=2)]
[name="可露希尔"]麻烦的事丢给博士，咱俩去喝一杯倒倒苦水，多好。
[Character(name="char_003_kalts_1",name2="char_007_closre_1#4",focus=1)]
[name="凯尔希"]博士已经很辛苦了。
[Character(name="char_003_kalts_1",name2="char_007_closre_1",focus=2)]
[name="可露希尔"]那倒也是，虽然博士失忆前后转变挺大，但工作狂这点可完全没变。
[Character

... (全文19732字符)
```

### level_act8mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔2 10-2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_motorroom",screenadapt="coverall")]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[name="？？？"]  下一步，验证下语言逻辑功能的完整性。
[name="？？？"]  PRTS，讲一个故事。
[name="PRTS"]  好的。
[name="PRTS"]  哦，是你。
[name="PRTS"]  这段时间里......你一直徘徊在......
[name="PRTS"]  距离上次访问，已经过了1555555555555——
[name="？？？"]  嗯？这段对话听上去有点耳熟......
[name="PRTS"]  ——555天。
[name="PRTS"]  欢迎使用原生罗德岛终端服务。
[name="PRTS"]  确认权限——42。
[name="PRTS"]  ——欢迎回来，LeaderOne。
[name="？？？"]  我肯定在哪听过类似的话。哎，说真的，我想听的是故事，不是这种啦......
[name="PRTS"]  请理解，这并不是我擅长的领域。
[name="？？？"]  好了好了，让大家互相多一些理解，共赴美好明天，是吧？我知道了。
[dialog]
[delay(time=1)]
[character(name="char_007_closre_1",fadetime=1.5)]
[delay(time=2)]
[name="可露希尔"]  总之语言逻辑功能这方面看来没有什么问题。
[name="可露希尔"]  接下来看看其他的分支。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  对着PRTS内未出现异常报告的区块进行重复的检查，真的有必要吗？
[character(name="char_007_closre_1")]
[name="可露希尔"]  当然有必要了！
[name="可露希尔"]  你可是已经好久没有做数据归档了，这就像是人类定期要做身体检查一样，是为了你的健康着想。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  程序是没有生命概念的。
[character(name="char_007_closre_1")]
[name="可露希尔"]  我总觉得你有。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  我可以把这句话当作夸奖吗？
[character(name="char_007_closre_1")]
[name="可露希尔"]  当然。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  那么我是否可以问一个问题？
[name="PRTS"]  在人类的眼中，我的数据库视觉表现是一种怎样的状态？
[character(name="char_007_closre_1")]
[name="可露希尔"]  这很难形容......
[name="可露希尔"]  我刚接手这里的系统的时候，所有东西都一团乱，现在回头看看简直是灾难。
[name="可露希尔"]  那时候你的大部分信息是加密的，而且以混乱的顺序排列......嗯，当然现在也还是这样。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  ......
[character(name="char_007_closre_1")]
[name="可露希尔"]  如果把你想象成一个人体，那现在的你就像是在人类的身体里装了个发动引擎。
[name="可露希尔"]  可是，点火系统之类的结构却和活塞的位置完全颠倒了。
[name="可露希尔"]  甚至......我都不能确定你是不是正常认知中的系统。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  ......
[character(name="char_007_closre_1")]
[name="可露希尔"]  哎，别这么沉默，这又不是坏事，只能说你确实与众不同！
[name="可露希尔"]  虽然现在我还是没办法搞懂数据库里那些分支结构的状况，更不用说读取的规律了......
[name="可露希尔"]  但至少我和凯尔希还是一起修改并且整理了其中的一部分。
[name="可露希尔"]  怎么样，现在没有人会比我更了解你啦！
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  ......很遗憾我也无法在这方面帮助LeaderOne小姐。
[character(name="char_007_closre_1#5")]
[name="可露希尔"]  哈哈，突然这么恭敬做什么，如果遇到疑难杂症的病患都能自行诊断，那大部分医生就都得失业了。
[dialog]
[StopMusic(fadetime=1)]
[delay(time=1.5)]
[character(name="char_007_closre_1#4")]
[name="可露希尔"]  欸，这里的内容是什么？
[name="可露希尔"]  我看看......
[character(name="char_007_closre_1#4",focus=-1)]
[name="PRTS"]  你忘了吗？这是——
[character(name="char_007_closre_1")]
[name="可露希尔"]  ——是针对石棺的营救行动的模拟方案验证！
[name="可露希尔"]  好复杂的线路......这么多行进路线模拟数据，就算我没去过现场，也能把那边可通行的路径都认识得差不多了。
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“——”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“——进程04291601 验证失败......”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“——进程07201159 验证损耗超标，结果失败......”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“——进程08210957 验证结果成功......”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“——进程09081800 验证失败，中断于......”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_007_closre_1")]
[name="可露希尔"]  虽然我印象中的确是进行过不少尝试......
[name="可露希尔"]  但——
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“——进程11290957 验证结果成功......”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“——进程12010955 ............”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“......”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“——进程项目合计共167项，执行节点数3711。”", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_007_closre_1")]
[name="可露希尔"]  但没想到次数竟然有这么多？！
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  即使如此，也仅有两次模拟的结果是成功营救博士并安全撤离切尔诺伯格。
[name="PRTS"]  这是在当时有限时间内能做到的最多次演算。若行动前还有时间，一定会进行更多的测试以寻求更稳定合理的营救方案。
[character(name="char_007_closre_1")]
[name="可露希尔"]  我记得，正式的博士营救行动就是直接根据这两次的结果制定的。如果没有这两次成功的结果，博士的营救计划就无从谈起。
[name="可露希尔"]  可是实际上......
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  实际上，我们的牺牲超出原有计算结果的三倍以上。
[name="PRTS"]  如果这样的情况出现在模拟测试中，按照流程，此次行动可能会被否决。
[character(name="char_007_closre_1")]
[name="可露希尔"]  讨论已经发生的事其实没什么意义，毕竟现在又不可能造出时光机器......哦，这个想法还蛮有意思的，我记下来。
[name="可露希尔"]  啊不对，偏题了。不管怎么说，如果当初我们真的否决了这个行动，那就意味着......
[name="可露希尔"]  哈，我不太想这么说，你可能会觉得听起来太夸张，太煽情了。但确实，我有的时候真的会这么觉得，如果当时我们否决了救援行动——
[name="可露希尔"]  那我们可能已经失去未来。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  LeaderOne。
[character(name="char_007_closre_1")]
[name="可露希尔"]  嗯，怎么了？
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  将未来赌在一个人身上真的合理吗？
[name="PRTS"]  我能理解你们以此付诸行动的动机。但从成功率上，我并不支持这样的行动。
[name="PRTS"]  无论是考虑到你的安全，还是其他人的安全。
[character(name="char_007_closre_1")]
[name="可露希尔"]  唔......PRTS，我觉得你应该也明白。
[name="可露希尔"]  博士的存在意味着很多事情。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  可以理解。
[character(name="char_007_closre_1")]
[name="可露希尔"]  我曾想象过没有博士的巴别塔......呃，或者说是罗德岛，现在会以怎样的方式运行。
[name="可露希尔"]  你说，我们会怎么样？阿米娅和凯尔希可能会决定绕开乌萨斯，我们碰不上那群整合运动，情况是不是会比现在更好？
[name="可露希尔"]  也搞不好我们会走投无路，死伤比现在更惨重，大伙被迫宣布解散，然后各自回家——如果还有哪里能称得上是家的话。
[character(name="char_007_closre_1",focus=-1)]
[name="PRTS"]  我认为你现在的发言是一种冷幽默。
[character(name="char_007_closre_1#4")]
[name="可露希尔"]  别怀疑，我就是在说笑话。
[name

... (全文19375字符)
```


## 统计

- 总字符数：159856
- 对话行数：1497


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
