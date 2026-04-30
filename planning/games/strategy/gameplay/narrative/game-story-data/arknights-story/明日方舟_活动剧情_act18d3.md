# 明日方舟 · 活动剧情 · act18d3（23段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act18d3」完整剧情脚本（23个文件，2814行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act18d3
- 脚本文件数：23

### level_act18d3_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
沉默。怪异。捉摸不定。外乡人。
他们自然会这么说。
阴暗。冷血。见死不救。天生怪物。
所有人在背后都会这么说。
[dialog]
[delay(time=0.5)]
是啊。
人只要失去了故乡，就什么都不是了。
照理来说，来到这里的我，应该能开始一个新的生活。
只是，过往挥之不去。这些东西会顺着影子爬上你的小腿，把你向泥沼深处拽去。
我们谁都摆脱不了过往。
如果有一天，你的故乡找上了你......
[dialog(fadetime=1,block=true)]
[delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_corridor")]
[character(name="char_016_medic",name2="char_263_skadi#3")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
2:33 A.M. 天气/阴
罗德岛本舰，走廊
[Dialog]
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]好啦！等这份报告提交完成，你的外勤任务就算结束了。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]嗯。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]等一下，又是......空白？咳，咳咳......
[name="罗德岛干员"]从头到尾，只有“完成”两个字啊！
[character(name="char_016_medic",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]嗯？
[name="斯卡蒂"]任务确实完成了。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]是、是这样没错......
[name="罗德岛干员"]......你多写两句话也不会有什么问题吧？！
[character(name="char_016_medic",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]嗯？
[character(name="char_016_medic")]
[name="罗德岛干员"]（怎么办......比想象的还难对付？）
[name="罗德岛干员"]（之前没和她说过什么话，这回说是要和她对接，虽然组长提醒过......但果然还是很难办。）
[name="罗德岛干员"]（深呼吸）
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]好、好的，我明白了。
[name="罗德岛干员"]关于任务中的细节，如果博士有疑问，会再找你确认。
[character(name="char_016_medic",name2="char_263_skadi#5",focus=2)]
[name="斯卡蒂"]......博士？
[character(name="char_016_medic",name2="char_263_skadi#5",focus=1)]
[name="罗德岛干员"]是的，凯尔希医生说你也许不会想向她提交报告......她还说阿米娅对你太温柔了，这样下去是不行的......之类。
[name="罗德岛干员"]然后就把这次任务归档到博士那边了。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]这个女人，哼。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]那你想直接向博士面呈报告吗？现在博士好像不在，你可以休息几天，等博士回来。
[name="罗德岛干员"]现在你提交的这份报告，真的很需要再补充！
[character(name="char_016_medic",name2="char_263_skadi#5",focus=2)]
[name="斯卡蒂"]......
[name="斯卡蒂"]很麻烦。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]那么，任务编码F1071，确认提交，后续补充——
[character(name="char_016_medic",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]等等。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]咦？
[character(name="char_016_medic",name2="char_263_skadi#3",focus=2)]
[name="斯卡蒂"]把档案还给我。我想起来，再完善点内容也可以。
[character(name="char_016_medic",name2="char_263_skadi#3",focus=1)]
[name="罗德岛干员"]啊！当然可以！那就麻烦你啦。
[name="罗德岛干员"]（比预想的要顺利一些啊......）
[stopmusic(fadetime=1.5)]
[name="罗德岛干员"]这样的话，我这边没什么事了，还请回去好好休......嗯？
[Dialog]
[delay(time=1)]
[character(name="char_016_medic",name2="char_263_skadi#8",focus=2)]
[name="斯卡蒂"]......
[character(name="char_016_medic",name2="char_263_skadi#8",focus=1)]
[name="罗德岛干员"]你的脸色一下子就变了，发生什么了？
[character(name="char_016_medic",name2="char_263_skadi#8",focus=2)]
[name="斯卡蒂"]可能是。
[character(name="char_016_medic",name2="char_263_skadi#8",focus=1)]
[name="罗德岛干员"]啊？在这里？船上吗？难道是入侵者？！听人说你五感特别敏锐，难道是......
[name="罗德岛干员"]不对啊，如果船上有危险，警报会响起来吧？
[character(name="char_016_medic",name2="char_263_skadi#8",focus=2)]
[name="斯卡蒂"]......歌声。
[character(name="char_016_medic",name2="char_263_skadi#8",focus=1)]
[name="罗德岛干员"]歌？什么歌？呃，很安静啊，我没听见......
[character(name="char_016_medic",name2="char_263_skadi#8",focus=2)]
[name="斯卡蒂"]这里，为什么会有歌声？
[character(name="char_016_medic",name2="char_263_skadi#8",focus=1)]
[name="罗德岛干员"]确实好像有些嗡嗡声，但那也不是歌吧？罗德岛上的各类仪器都还在运转，有可能是，是机械振动？你还没太习惯吗？
[character(name="char_016_medic",name2="char_263_skadi#8",focus=2)]
[name="斯卡蒂"]不，气味。
[name="斯卡蒂"]海水的味道。
[Dialog]
[character]
[delay(time=1)]
[character(name="char_016_medic")]
[name="罗德岛干员"]......斯卡蒂？你有点吓到我了。你在说什......
[Dialog]
[delay(time=1)]
[name="罗德岛干员"]咦？喂！斯卡蒂！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background]
[PlaySound(key="$rungeneral")]
斯卡蒂跑得太急、太快，她跑进楼梯通道，她害怕乘电梯几秒间的焦虑就会让那气味溜走。
[Dialog]
[Subtitle(text="一个猎人走上海岸♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$rungeneral")]
她能听到这歌。这艘船上的大多数人，他们听不见。
这种语言，这种旋律，唤起了她的回忆。她不是个恋旧的人，但她太熟悉了。
但......不该这样。这首歌不该出现在这里。
[Dialog]
[Subtitle(text="他的家乡在后，徒余哀叹♪", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$rungeneral")]
歌声在这艘船的管道里游移。
海水的气味从舱壁里不断渗出来。
[Dialog]
[delay(time=1)]
斯卡蒂也同样记得这味道。潮湿逼近了她，她的皮肤不住地收缩、绷紧。紧张，却也是激动。
[Dialog]
[PlaySound(key="$rungeneral")]
难道她醒了？她不禁加快了脚步。
[Dialog]
[name="斯卡蒂"]幽灵鲨！
[delay(time=0.7)]
[dialog]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[character(name="char_263_skadi#8")]
[Background(image="bg_ri_1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_gen_dooropen")]
[Subtitle(text="她拉开医疗舱的门。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="床铺是空的。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=0.7)]
[name="斯卡蒂"]......
[dialog]
[Blocker(a=0, r=0, g=0, b

... (全文15816字符)
```

### level_act18d3_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_desert_1")]
[character(name="char_263_skadi#3")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[playsound(key="$bodyfalldown3")]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[character(name="avg_npc_181",fadetime=1.5)]
[delay(time=2)]
[name="？？？"]斯卡蒂。
[name="？？？"]你退步了，斯卡蒂。以前的你能轻轻松松地把他们大卸八块。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]何塞先生，我没那么血腥。
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[character(name="avg_npc_181")]
[name="老何塞"]难说。那就是你变了。你居然还给了他们逃的机会。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]可能吧。
[character(name="avg_npc_181")]
[name="老何塞"]是什么风把你又吹到我这来了？他们在这蹲你是不是和我有关系？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]我不知道。
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[character(name="avg_npc_181")]
[name="老何塞"]我听说你不干这行了，后面是加入了什么......一个医药公司吧？好好的正经工作不干，又跑来这荒郊野岭做什么？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]何塞先生，你消息灵通。这次我需要你帮忙。
[character(name="avg_npc_181")]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="老人舔了舔烟纸，从口袋里拿出了些劣质烟草。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="老何塞"]几年过去了，我还以为你收手了。因为你，卡西米尔的赏金猎人换了好几茬。这里离卡西米尔那么远，我都能知道你又干了些什么。
[name="老何塞"]本以为你是个只会搞大动静的人。
[name="老何塞"]......但你现在变得这么安静。
[name="老何塞"]你这一路像拖车一样从米诺斯附近碾过来，就为了找我？你想要什么，说吧。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]我要去盐风城。
[character(name="avg_npc_181")]
[name="老何塞"]盐......风城？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]别告诉我，连你也没听过这地方。
[character(name="avg_npc_181")]
[name="老何塞"]是，我听过。在这一带卖消息的人里，也只有我听过。但你，你怎么会想去那里？
[name="老何塞"]那地方什么都没了。几十年前......就不剩下什么了。
[name="老何塞"]靠近大海的那一大块，你以为还能剩下什么？不过一个空架子，呼口气都漏风。
[name="老何塞"]很多赏金猎人想靠近那些荒弃的城市，就像扑向腐死驮兽骨架的小兽。
[name="老何塞"]他们以为还能抠出一丝能吃的血肉来，却不知道自己吞进肚里的不过是一包毒虫。
[name="老何塞"]伊比利亚。他们觉得这个不出声的伊比利亚也像卡西米尔和高卢一样，到处都是宝藏。
[name="老何塞"]哈，那里什么都没有。什么都没有的地方就越什么都可能有。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]那你会告诉赏金猎人什么？
[character(name="avg_npc_181")]
[name="老何塞"]他们问我买消息，我会卖给他们。对我这样的人来说，这些人回来或者回不来，都是生意。
[name="老何塞"]事实上，他们也确实回不来，一个都回不来。
[name="老何塞"]半个月前，有一队人来找我，“匕首角”的手下。
[name="老何塞"]他的装备比地上这些小子要精良得多。他也很有经验。他带着十几个人一起去了。现在再也没人见过他们。
[name="老何塞"]很多人好奇他们的下落。他们可能是被惩戒军抓走，也可能是国防军干的，但我还听说了别的可能性。
[name="老何塞"]那里有——怪物。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]哦。
[character(name="avg_npc_181")]
[name="老何塞"]要么就是被审判庭抓走了。我不知道哪种下场更惨。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]怪物还是人，对我的剑来说区别不大。只分挡道的，和不挡道的。
[character(name="avg_npc_181")]
[name="老何塞"]好吧，好吧。你去盐风城，总不能是想去度假。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]我要去找人。
[character(name="avg_npc_181")]
[name="老何塞"]又有哪个倒霉蛋惹到你了？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]这回不算。那人是我的......是我以前认识的人。
[character(name="avg_npc_181")]
[name="老何塞"]......比认识我还要早？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]早得多。
[character(name="avg_npc_181")]
[name="老何塞"]我还以为他们都不在这，或者都死了。起码你当年是这么对我说的。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]所以我才要去找。我要弄明白一些事。
[character(name="avg_npc_181")]
[name="老何塞"]......你找了也挺多年了吧？
[name="老何塞"]上回那么大动静，不可能是为了那份骑士宝藏。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]你跟我说过，人该往前。
[character(name="avg_npc_181")]
[name="老何塞"]——
[name="老何塞"]你有没有带藏宝图？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]......什么？
[character(name="avg_npc_181")]
[name="老何塞"]很多人，有些还是老手。他们在荒地里走，走着走着，就忘了自己要去哪，又想找什么。
[name="老何塞"]他们就一直走。不知饥饿，不知疲倦。
[name="老何塞"]......直到荒野将他们杀死。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]他们太弱了。
[character(name="avg_npc_181")]
[name="老何塞"]弱？再强大的猎人，也征服不了没有边际的荒野。很多猎人不明不白地死在路上，到死都不知道自己要找什么——这个结局不适合你。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]为什么要跟我说这些？
[name="斯卡蒂"]我难道没和你说过，他们甚至都不是阿戈尔小机器的对手？
[character(name="avg_npc_181")]
[name="老何塞"]你强，你保住我儿子的命了吗？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]......对不起。
[character(name="avg_npc_181")]
[name="老何塞"]不要说对不起！我不是要刺你。我是要你自己想想，没原谅你自己的是你，不是我。
[name="老何塞"]我后悔的就只有没打断他的腿，不让他走老子的老路。和你无关。
[name="老何塞"]你说自己是海里来的，除了伊比利亚，我没听过其他什么海。你是我不知道的人。
[name="老何塞"]那你呢，你就没有不知道的人？
[name="老何塞"]就是那样的人杀了我儿子。你都不知道的人。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]......我就是害怕那样的事情。
[character(name="avg_npc_181")]
[name="老何塞"]罢了。至少你说的人不会费尽心思杀我。你去盐风城做什么？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]我有一个朋友被人带去了那里。
[character(name="avg_npc_181")]
[name="老何塞"]怪事。
[name="老何塞"]拿好。地图。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]好。我要给你什么？
[character(name="avg_npc_181")]
[name="老何塞"]给我什么？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]你卖情报。一物换一物。你给了我信息，我给你你需要的。
[character(name="avg_npc_181")]
[name="老何塞"]（弹烟灰）
[name="老何塞"]我想想......那年你把胡安那小子的尸体带了回来，你把他交到了我手上，脑袋和胳膊还连在身子上。所以，现在我们就两清了。
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]......何塞先生，非常感谢。
[name="斯卡蒂"]那我走了。保重。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1)]
[delay(time=2)]
[character(name="avg_npc_181")]
[name="老何塞"]停！急急忙忙的，赶着去送死？！
[character(name="char_263_skadi#5")]
[name="斯卡蒂"]嗯？
[character(name="avg_npc_181")]
[name="老何塞"]......嘿。你是不是没怎么听人和你这么说话？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]是。
[character(name="avg_npc_181")]
[name="老何塞"]那你就需要有人这么和你说说。
[name="老何塞"]你穿一身赏金猎人的衣服，就这么大摇大摆地进伊比利亚的城市？
[character(name="char_263_skadi#3")]
[name="斯卡蒂"]对。
[character(name="avg_npc_181")]
[name="老何塞"]还真是老样子啊，斯卡蒂。我费了这么多口水，进你耳朵还不如哗哗的风声。
[name="老何塞

... (全文14852字符)
```

### level_act18d3_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[character(name="char_empty",name2="avg_npc_178")]
[Background(image="bg_ibtownd")]
[Image(image="ac18_02",xScale=1.1,yScale=1.1, fadetime=0)]
[Delay(time=1)]
3:23 P.M. 天气/阴
伊比利亚，盐风城
[dialog]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[ImageTween(yFrom=30, yTo=-30, duration=25, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="一座早已失去生机的城市，半埋在海风味的尘土之下。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="斯卡蒂"]地图上的地方，就是这里。
[name="斯卡蒂"]......空气中的味道，算不上好。
[dialog]
[image(fadetime=1.5,block=true)]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#4",name2="avg_npc_178",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_1012_skadiSP_1#4",name2="avg_npc_178",focus=1)]
[name="斯卡蒂"]你好。
[character(name="avg_1012_skadiSP_1#4",name2="avg_npc_178",focus=2)]
[name="男性居民"]......
[dialog]
[character]
[delay(time=1)]
[character(name2="char_empty",name="avg_npc_178")]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[character(name2="avg_1012_skadiSP_1#4",name="avg_npc_178",fadetime=1.5)]
[delay(time=2)]
[character(name2="avg_1012_skadiSP_1#4",name="avg_npc_178",focus=2)]
[name="斯卡蒂"]请问——
[character(name2="avg_1012_skadiSP_1#4",name="avg_npc_178",focus=1)]
[name="另一个男性居民"]（垂头不语）
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="没有人回应。甚至没有人转过头。他们睁着眼，可是他们一动不动。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="与雕塑的唯一区别是，他们呼吸，缓慢地呼吸。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#7")]
[name="斯卡蒂"]......
[name="斯卡蒂"]......怪物？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="他们都有着人的形貌，除了过于瘦削，衣衫破旧，和这一路上遇见的伊比利亚人并无差别，与老何塞描述中的怪物相去甚远。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]都是人类。
[name="斯卡蒂"]（伊比利亚语）
[name="斯卡蒂"]现在不这么说了么？
[name="斯卡蒂"]（口音稍变的伊比利亚语）
[name="斯卡蒂"]......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="依旧无人应答。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="斯卡蒂下意识握紧了箱子的把手。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="在外面，她有的是让不愿意开口的人开口的办法。可这样做的前提是，对面的人听懂她说的话。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="斯卡蒂"]......况且，我现在是歌手。
[name="斯卡蒂"]歌手不这样做事。何塞先生说的。
[dialog]
[character]
[delay(time=1)]
[musicvolume(volume=0,fadetime=1)]
[name="？？？"]九十九......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="一个小小的影子跑过街道。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1.5)]
[character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]有人在说话。
[dialog]
[musicvolume(volume=0.4,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="她快步追上去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1.5)]
[name="？？？"]九十九。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="char_empty",name2="avg_1012_skadiSP_1#4",fadetime=0.7)]
[delay(time=2)]
[name="斯卡蒂"]一个......孩子？他在念一个数字。
[name="斯卡蒂"]我不会听错。
[dialog]
[character(name="avg_1012_skadiSP_1#7")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="斯卡蒂"]你——
[name="斯卡蒂"]我的项链被......
[character(name="avg_1012_skadiSP_1#6")]
[name="斯卡蒂"]你不能走！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="孩子从她手里滑开了。他一扭头，往更深的巷子里跑去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character]
[delay(time=1)]
[name="幼年居民"]九十九，九十九......
[dialog]
[playsound(key="$rungeneral")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ibbar")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlaySound(key="$rungeneral", volume=1)]
[Character(name="avg_1012_skadiSP_1#7",fadetime=1)]
[delay(time=2)]
[name="斯卡蒂"]你跑不掉。
[character]
[name="幼年居民"]呜......呜呜......
[Character(name="avg_1012_skadiSP_1#7")]
[name="斯卡蒂"]为什么偷我东西？为了把我带到这里？
[name="斯卡蒂"]嗯？
[dialog]
[musicvolume(volume=0,fadetime=0.5)]
[playsound(key="$bodyfalldown1")]
[playsound(key="$dooropenquite")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=3

... (全文10858字符)
```

### level_act18d3_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibbar")]
[Character(name="avg_1012_skadiSP_1#4")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="斯卡蒂看着失去知觉的当地居民，拎起在地上放了一秒的箱子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(fadetime=0.6)]
[delay(time=1)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_180#2",fadetime=0.7)]
[delay(time=2)]
[name="？？？"]......你、你好。
[delay(time=1)]
[Character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]嗯？还有一个。
[Character(name="avg_npc_180#2")]
[name="女性居民"]别，别动手......我和他们不大一样。我知道你是好的。
[Character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]你能明白我的意思。
[Character(name="avg_npc_180#2")]
[name="女性居民"]你只是跟着长凳来这里。
[dialog]
[character]
[name="幼年居民"]呜，呜呜......木框，木框......
[Character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]他跑，我跟着。
[Character(name="avg_npc_180#2")]
[name="女性居民"]你对我们没有恶意。
[Character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]只要他把我的东西还给我。
[Character(name="avg_npc_180#4")]
[name="女性居民"]咦？
[name="女性居民"]长、长凳......你拿了什么？
[dialog]
[character]
[name="幼年居民"]亮亮......亮亮......硬......痛痛......呜呜呜......
[Character(name="avg_npc_180#2")]
[name="女性居民"]这个不能吃呀！快，快从嘴里拿出来！
[name="女性居民"]抱歉，长凳看到没见过的东西就想用手拿。他不懂这东西他不该拿。
[Character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]（接过项链）
[Character(name="avg_npc_180#4")]
[name="女性居民"]呃，全是口水......你的手都弄脏了。
[Character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]拿回来就行。
[dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]这里不常见陌生面孔。你是从外面来的么？
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]我从其他伊比利亚城市来的。
[Character(name="avg_npc_180#1",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]我很少见到别的地方来的人。
[name="女性居民"]你这身衣服......也很奇怪。我从没见过这种料子。外面的人都穿成这样么？
[Character(name="avg_npc_180#1",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]流浪歌手才这么穿。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]流浪......歌手？我听到你对铁皮他们说了，但我不知道那是什么。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]像我这样到处走，偶尔停下来，弹弹琴，唱唱歌。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]这箱子里呢，装的是什么？
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]萨克斯。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]萨克斯是什么？
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]乐器。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]你真的是个流浪歌手？
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]嗯。
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]（小声嘀咕）
[name="女性居民"]那你是来做什么的呢？唱歌吗？
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]我是来找人的。
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]那个人是谁？也是一位流浪歌手么？
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]是的。她是我的伙伴，我们是同僚。
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]她也来了盐风城？
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]对。你见过她么？
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]你还没说她长什么样子呢......算啦！我刚才也说过了，像你这样的人，我以前从来没见过。
[Character(name="avg_npc_180#4",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]我去问其他人。你能带路吗？
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]带路？那个陷阱......是我做的。我以为你知道。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]无所谓。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]你不怪我？我还以为你至少会......也教训我一下。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]走吧。我赶时间。
[Character(name="avg_npc_180#1",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]好......
[Character(name="avg_npc_180#1",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]......
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]啊！
[name="女性居民"]怎、怎么突然停下来......撞在箱子上了，痛。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]忘了说。我箱子里面的东西，对你没用。
[name="斯卡蒂"]除了这个，你想要什么，帮我找到人，我都可以给你。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]呃，我只是好奇......有那么明显吗？
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]和你做的陷阱一样显而易见。
[Character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#4",focus=1)]
[name="女性居民"]哇......歌手，你不光有一双灵巧的手，你还有一双厉害的眼睛啊。
[dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[character(name="avg_npc_187",name2="avg_npc_178")]
[Background(image="bg_ibtownd")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[character(name="avg_npc_187",name2="avg_npc_178",focus=1)]
[name="居民"]九十八......
[character(name="avg_npc_187",name2="avg_npc_178",focus=2)]
[name="居民"]九十九......
[character]
[dialog]
[delay(time=1)]
[Character(name="avg_npc_180#1",name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]......
[n

... (全文28429字符)
```

### level_act18d3_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]看看你，依然在彷徨，仿佛一只迷途的海鱼。
[character(name="avg_474_gladiia_1#5",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]（看他一眼）
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]你想知道我带她去了哪里。你非常在意。我们的集会，你没有资格参与，可你的眼神告诉我，你想知道我们将对她做什么。
[name="主教"]你是找回你们之间的手足之爱了么？你的内心是否在因为你的故交的遭遇而经受撕扯？感到不公？从而愤怒？
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]你在试图找寻你看不见的东西。
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]当然，你当然可以这么回答。
[name="主教"]你以为我想伤害她。你错了，我是想帮她。
[name="主教"]只有弄清楚她的——你们的痛苦根源来自哪里，我才能更好地帮助你们切除症结，不是么？
[name="主教"]就像你。你主动加入我们，你想溶进真正的海洋。等你完成这个任务，你肮脏的本质将得到净化。这是海对你的恩赐。
[name="主教"]而同样的恩赐，最后也会给予你的故交们，只要她们能同你一样，放下过去为敌时的狭见。
[name="主教"]使你们团聚，这是第一步。理解你们，这是第二步。而到最后，你们也会理解我。
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]......
[name="歌蕾蒂娅"]如果你能适当地减少一些废话，我们共事起来还能更融洽。
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]我也可以说一些会使你高兴的。你的故交——清醒的那个，她已经到了。
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]斯卡蒂？
[name="歌蕾蒂娅"]她不在这里。
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]自然不在。没有我的邀请，没人能进入这里。
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]她进城了，你知道。
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]你表现出了意外，这很有趣。这座城市里的声音，我都听见。
[name="主教"]祂赞赏我做的一切，赐予了我力量，令我的生命进一步延展。我的感知，我的心灵，都不再受缚于你所见到的躯壳里。
[name="主教"]我在靠近完美。我将收下你的嫉恨。
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]呵。
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]说回你的故交——她来得比预期的还快。
[name="主教"]“深海猎人血脉相连”。
[name="主教"]她并不知道什么在等着她。只因为你带走了另一个，她就追到了这里，一刻都不曾休息。
[name="主教"]真是令人惊叹的情谊。她知道你如今的样子么？面对叛徒，她会怎么做？是还信任你们的血脉联系、同僚旧情，还是一剑刺入你的身体？
[name="主教"]我很期待。
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]（转身就走）
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]你不需要急着去找她。你做得很好。你将这一个带回到她该待的地方，又将另一个引入了城。
[name="主教"]他会满意的。
[character(name="avg_474_gladiia_1#5",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]他？
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]你不需要知道。
[name="主教"]现在我们只等待。等到那个时候到来，你自然可以找你的故交，去传达我们的邀请。
[character(name="avg_474_gladiia_1#1",blackstart=0.3,blackend=0.5)]
[name="歌蕾蒂娅"]她未必会来。
[character(name="avg_npc_184",blackstart=0.2,blackend=0.35)]
[name="主教"]她会来的。她会自己来找我。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_ibtownd")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$rungeneral")]
[delay(time=1)]
[character(name="avg_npc_180#3",name2="char_empty",fadetime=1)]
[delay(time=2)]
[name="安妮塔"]又回来啦！
[name="安妮塔"]我们住的地方是北边最好的房子，你看，这扇门还能关上。一扇能关上的门，在下雨天能帮你不少。
[dialog]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",fadetime=1)]
[delay(time=1.5)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]附近有人，两个。
[Character(name="avg_npc_180#2", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]他们呀，他们平时就在这里。
[character(name="avg_npc_178")]
[name="男性居民"]一百三十、一百三十一、一百三十二......
[Character(name="avg_npc_180#3")]
[name="安妮塔"]嗨，砖头，今天过得好吗？
[character(name="avg_npc_178")]
[name="男性居民"]......
[name="男性居民"]一，二，三......
[Character(name="avg_npc_180#2")]
[name="安妮塔"]抱歉啦！
[Character(name="avg_npc_180#4", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]可怜的家伙，他又得重新来。他总坐在这里，数街上有几块砖。悄悄告诉你，每天数出来的结果都不大一样。
[name="安妮塔"]还有，那是石柱，他喜欢绕着街上的柱子散步。阴雨天就不出来啦，他年纪不小了，沾了水腿会疼。
[name="安妮塔"]你不用管他们，他们也不会管你，就像他们也不管我一样。
[name="安妮塔"]进来吧，歌手。正式介绍一下，里面就是我家了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playsound(key="$dooropenquite")]
[Background(image="bg_ibbar")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="avg_npc_178",name2="avg_npc_187",focus=1)]
[name="男性居民A"]......
[character(name="avg_npc_178",name2="avg_npc_187",focus=2)]
[name="男性居民B"]......
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]嗨，铁皮。嗨，墙灰。你们醒啦！
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]（摸箱子）
[character(name="avg_npc_178",name2="avg_npc_187",focus=2)]
[name="男性居民B"]痛......
[character(name="avg_npc_178",name2="avg_npc_187",focus=1)]
[name="男性居民A"]喂，木框。你又把这个外面的人带到家里。
[Character(name="avg_npc_180#2")]
[name="安妮塔"]她不是坏人。
[character(name="avg_npc_178",name2="avg_npc_187",focus=1)]
[name="男性居民A"]她是外面来的人。
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]长凳都挺喜欢她的，对不对啊，小长凳？
[character]
[name="幼年居民"]呜......嗷......
[Character(name="avg_npc_180#2", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]别、别咬！歌手的裙子都要被咬坏啦！
[Character(name="avg_npc_180#2", name2="avg_1012_skadiSP_1#5",focus=2)]
[name="斯卡蒂"]咳。
[name="斯卡蒂"]......倒还不会坏。
[Character(name="avg_npc_180#2", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]沾满了口水，就没这么漂亮了。
[character]
[name="幼年居民"]嗷，嗷嗷......
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]这孩子真的很喜欢你，歌手。
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=2)]
[name="斯卡蒂"]......
[Character(name="avg_npc_180#3", name2="avg_1012_skadiSP_1#4",focus=1)]
[name="安妮塔"]你们瞧，长凳也想让她留下来。
[character(name="avg_npc_178",name2="avg_npc_187",focus=1)]
[name="男性居民A"]你在盘算的事。别以为，我不知道。
[Character(name="avg_npc_180#4")]
[name="安妮塔"]呃......


... (全文21656字符)
```

### level_act18d3_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibtownn")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1",fadetime=1)]
[delay(time=1.5)]
[character(name="avg_npc_180#2")]
[name="安妮塔"]啊，你回来啦！我正准备去找你呢。
[name="安妮塔"]你身上怎么沾了些沙子......你到海边去啦？
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]嗯。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#4",focus=2)]
[name="安妮塔"]都叫你不要去啦，可是你偏不听。
[name="安妮塔"]快跟我进屋里去吧，里面暖和些。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#4",focus=1)]
[name="斯卡蒂"]不用。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]好吧，这个给你，我找到吃的了。我把我缝了一半的衣服给了壁炉叔，从他那里拿了这些，他那里还剩下不少吃的，应该不在意。
[name="安妮塔"]还有好久才入冬呢，我再勤快些，总能找到能用的料子的。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=1)]
[name="斯卡蒂"]这些贝肉......
[dialog]
[characteraction(name="left", type="move", xpos=200, fadetime=0.5, block=true)]
[delay(time=0.51)]
[stopmusic(fadetime=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="斯卡蒂"]你们吃的到底是什么？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]哎呀，你抓得我好疼啊......你力气可太大啦！
[PlayMusic(intro="$jealous_intro", key="$jealous_loop", volume=0.4)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]你们吃的到底是什么......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]是、是岸上捡的呀！
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]这里的海没有食物。没有任何收获。这片海已经安静下来了。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]我说过了呀，你今天去，岸上当然不会有吃的。
[name="安妮塔"]要到那个时候......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]什么时候？
[dialog]
[character]
[delay(time=1)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_178",fadetime=0.7)]
[delay(time=1)]
[name="居民"]一百......
[name="居民"]一百！
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]哎呀！我都没注意数字。原来已经到一百了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[playsound(key="$d_gen_walk_n")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="仿佛得到了某个信号，原本分散在街道各处、各自“忙碌”的人们聚集到了一起。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[playsound(key="$d_gen_walk_n")]
[playsound(key="$d_gen_walk_n", delay=0.4)]
[Subtitle(text="他们嘴里念着同样的数字，围在一个罐子周围，一个接着一个，从罐子里摸出一样东西，然后沉默着离开。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]那个罐子。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]你不是问我，这些食物都是从哪来的吗？
[name="安妮塔"]每当潮汐起落一百次，大人们就会像这样，聚在一起，每人从罐子里摸一个贝壳出来。
[name="安妮塔"]罐子里的贝壳大多数都是白色的，只有一个是红色。
[name="安妮塔"]拿到红色贝壳的那个人，等到天黑之后，他就会去海边。
[name="安妮塔"]到了第二天早上，海岸上就会铺满食物。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]那个人呢？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]去海里生活了。就像律法说的那样。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=1)]
[name="斯卡蒂"]你们这也信？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#4",focus=2)]
[name="安妮塔"]不然你想他去哪里？
[dialog]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_178",fadetime=1.5)]
[delay(time=2)]
[name="男性居民A"]......一百，终于到了。
[name="男性居民A"]喂，木框，你那是什么表情？这是个好日子！
[name="男性居民A"]很快，我们之中，又有一个幸运的人被选中。他先我们一步，去过更好的生活了。
[name="男性居民A"]等明天，新鲜的食物，我们都会有。大家都会活下去。无论是去海里的，还是留在岸上的。
[character(name="avg_npc_180#4")]
[name="安妮塔"]我......
[character(name="avg_npc_178")]
[name="男性居民A"]你不用着急。你已经足够大了。你很快也会加入进来，得到这伟大的，机会。
[name="男性居民A"]现在，你可以和过去一样。祝福那位兄弟姐妹。
[character]
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[character(name="avg_npc_187",name2="avg_npc_178",focus=1)]
[name="男性居民B"]铁皮，我，我......
[character(name="avg_npc_187",name2="avg_npc_178",focus=2)]
[name="男性居民A"]你摔倒了。真是没用。刚才，海边的事，弄软了你的腿。
[character(name="avg_npc_187",name2="avg_npc_178",focus=1)]
[name="男性居民B"]我不明白为什么。我，我好饿......我没力气。我病了......我要死了。
[name="男性居民B"]对，贝壳呢？我刚拿出来的......
[character(name="avg_npc_187",name2="avg_npc_178",focus=2)]
[name="男性居民A"]掉地上了。
[character(name="avg_npc_187",name2="avg_npc_178",focus=1)]
[name="男性居民B"]是不是......是不是红色的？
[name="男性居民B"]我，可以去海里生活？
[name="男性居民B"]到了海里，肚子就不饿了。是这样的吧，铁皮？我会过上，好生活。
[name="男性居民B"]你也会......呃， 跟教士说的那样，祝福我的，是吧？
[character(name="avg_npc_187",name2="avg_npc_178",focus=2)]
[name="男性居民A"]......
[name="男性居民A"]你看错了。
[name="男性居民A"]拿好，这是你的贝壳。看看清楚，这是什么颜色。别让盐水迷了你的眼睛。
[character(name="avg_npc_187",name2="avg_npc_178",focus=1)]
[name="男性居民B"]白色的？为什么会是白色......我看错了吗？不会啊。我的眼睛，很好。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1",fadetime=0.2)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]（拨琴）
[delay(time=1)]
[character]
[dialog]
[delay(time=1)]
[character(name="avg_npc_187",name2="avg_npc_178",focus=2)]
[name="男性居民A"]你也在。
[name="男性居民A"]原来，这东西是这么用的。
[character(name="avg_npc_187",name2="avg_npc_178",focus=1)]
[name="男性居民B"]咳，铁皮，你手里的贝壳......你的手，捏得好紧。是不是要流血了？红红的，我看见了......
[character(name

... (全文35586字符)
```

### level_act18d3_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibtownn")]
[Delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[delay(time=0.6)]
[character(name="avg_npc_183#3",fadetime=1.5)]
[delay(time=3)]
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]......
[character(name="avg_npc_182#5")]
[name="审判官"]长官！
[character(name="avg_npc_183#3")]
[name="大审判官"]退下。你不是她的对手。
[character(name="avg_npc_182#5")]
[name="审判官"]但是我......
[character(name="avg_npc_183#3")]
[name="大审判官"]退下。
[character(name="avg_npc_182#1")]
[name="审判官"]遵命！
[dialog]
[character(fadetime=1)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[character(name="avg_1012_skadiSP_1#1",fadetime=0.7)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="斯卡蒂与面前的人隔着十来米，静静地对视。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="斯卡蒂"]你，强很多。
[character(name="avg_npc_183#3")]
[name="大审判官"]你不该踏入这座城市。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]我已经在了。
[character(name="avg_npc_183#3")]
[name="大审判官"]违背规则，就要付出代价。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]我管不了那么多。
[character(name="avg_npc_183#3")]
[name="大审判官"]你会留在这里。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]......我不想同你打。
[character(name="avg_npc_182#3")]
[name="审判官"]哼。邪恶的阿戈尔人，你一定是害怕了！有长官在，你绝对跑不掉。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]但，如果这是必须的话——
[name="斯卡蒂"]（阿戈尔语）我将打败你。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[character(fadetime=0.6)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="起步，加速，冲击。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_182#5")]
[name="审判官"]好快，竟比刚才和我交手时候还要快许多！
[name="审判官"]如果是这样的速度，我根本就连她的裙摆都打不中......她到底还藏了多少？！
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1#1")]
[Subtitle(text="在撞上大审判官之前，斯卡蒂退开了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她像一条被海浪冲上半空的鱼，高高跃起，又落在残破的屋顶。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[delay(time=1)]
[character(name="avg_npc_183#3")]
[Subtitle(text="大审判官如影随形。两人身形相撞，又退开，再次相撞。本就千疮百孔的城镇难以经受这样的冲击，街道上建筑物的碎片正在迅速增多。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[delay(time=1)]
[character(name="avg_npc_182#5")]
[name="审判官"]攻击和闪避都越来越快，老师也是。我就要跟不上了。
[name="审判官"]原来我......我还差这么多？！
[character(name="avg_npc_182#4")]
[name="审判官"]不，这不行。那可是一个阿戈尔人。我才不能输给阿戈尔人。
[name="审判官"]可是这个阿戈尔人，她好像，还在拿着她的箱子当武器......那箱子是什么做的啊！为什么那么硬？！
[name="审判官"]不过，老师也没有用手炮。要是用上的话......瞬间就能把她拿下吧？连着这条街一起，都会一起被轰成渣。
[name="审判官"]然而......那只是一个阿戈尔人啊？她的模样，和那些怪物并不一样......
[name="审判官"]她用的是......某种法术吗？我感觉不出来。我们的灯......也并没有能压制她的力量。
[character(name="avg_npc_182#4")]
[name="审判官"]——这阿戈尔人身上藏着的秘密太多了。
[dialog]
[stopmusic(fadetime=1)]
[CameraShake(duration=3, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="整条街的震动渐渐停止了。碎屑与烟尘之中，年长的审判官再次现身。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[character(name="avg_npc_183#3",fadetime=1)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="大审判官"]......
[character(name="avg_npc_182#7")]
[name="审判官"]长官！您果然赢了。我就知道，任何人都无法撼动您分毫。
[name="审判官"]咦，那个阿戈尔人呢？
[character(name="avg_npc_183#3")]
[name="大审判官"]逃了。
[character(name="avg_npc_182#5")]
[name="审判官"]什么？这......怎么会？
[character(name="avg_npc_183#3")]
[name="大审判官"]她受伤了，跑不了多远。
[character(name="avg_npc_182#4")]
[name="审判官"]我去找她——
[character(name="avg_npc_183#3")]
[name="大审判官"]你打不过她。
[character(name="avg_npc_182#3")]
[name="审判官"]咳咳......但绝不能让她这样的人在这片海岸恣意行走！
[name="审判官"]看方向，她应该是去居民聚居处了。她可能混入人群，当地居民之中有人在帮她。我会一间一间屋子找过去。
[character(name="avg_npc_183#3")]
[name="大审判官"]如果你认为这是对的，你就去。
[character(name="avg_npc_182#2")]
[name="审判官"]好——
[dialog]
[delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[name="审判官"]......
[name="审判官"]长官，这座城市的异状，是她带来的吗？
[character(name="avg_npc_183#3")]
[name="大审判官"]我让你去看。你看到了什么？
[character(name="avg_npc_182#2")]
[name="审判官"]这座城市里的人，他们的行为很不正常。每天就像没有醒着的时候。他们行动，却不是为了到达。他们进食，甚至不是为了饱腹。
[name="审判官"]他们正在往海里走，而且他们并不认为这是自杀。
[character(name="avg_npc_183#3")]
[name="大审判官"]你制止了他们？
[character(name="avg_npc_182#2")]
[name="审判官"]是。因为这显然是错的。
[character(name="avg_npc_183#3")]
[name="大审判官"]我们关心的，是结果。你认为你的纠正能有对的结果，那就去做。
[character(name="avg_npc_182#1")]
[name="审判官"]对的结果......
[character(name="avg_npc_183#3")]
[name="大审判官"]若不能，那你必须有所选择。
[name="大审判官"]判官——你的双眼，你的剑，需紧盯伊比利亚最大的威胁。
[character(name="avg_npc_182#1")]
[name="审判官"]是，长官！
[name="审判官"]最大的威胁......是那些正在上岸的怪物。
[name="审判官"]难道说，这些正在走向大海的人，他们与这些怪物有什么联系？
[name="审判官"]对......一定有联系。
[name="审判官"]老师说过，异常往往不是单一现象。这些恐怖的异象之间，必有关联。
[character(name="avg_npc_183#3")]
[name="大审判官"]要解决问题——你首先要看清问题所在。
[character(name="avg_npc_182#2")]
[name="审判官"]我、我知道！
[name="审判官"]——是那些躲在暗中谋划一切的阿戈尔

... (全文20680字符)
```

### level_act18d3_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibtownn")]
[character(name="avg_1012_skadiSP_1#1")]
[Delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="街道安静下来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[character(name="avg_1012_skadiSP_1#1")]
[Subtitle(text="厚重的箱子重新合起，回到流浪歌手的背上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="斯卡蒂迈步。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[playsound(key="$d_gen_walk_n")]
[Subtitle(text="一步，两步。地上堆积的残肢和凝滞的体液在她脚下急遽地腐败、风化。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="三步。海风吹起她的裙摆，满地细小结晶跟着扬起、散开。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[character(fadetime=1.5)]
[subtitle]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_ibindoor",fadetime=1,block=true)]
[character(name="avg_npc_182#5",name2="avg_npc_180#2")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[character(name="avg_npc_182#5",name2="avg_npc_180#2",focus=1)]
[name="审判官"]你都、你都看到了吗？刚才？
[character(name="avg_npc_182#5",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]我看到了。
[character(name="avg_npc_182#5",name2="avg_npc_180#2",focus=1)]
[name="审判官"]那种事，她竟然都能办到？
[character(name="avg_npc_182#5",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]那是歌手。歌手......
[name="安妮塔"]审判官，如果是她的话，她从来能办到。
[character(name="avg_npc_182#4",name2="avg_npc_180#2",focus=1)]
[name="审判官"]歌手......歌手。你还在叫她歌手。
[character(name="avg_npc_182#4",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]不然叫啥哩？你是审判官，你告诉我。
[character(name="avg_npc_182#3",name2="avg_npc_180#2",focus=1)]
[name="审判官"]......
[name="审判官"]我要出去。
[character(name="avg_npc_182#3",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]哎，等等！
[character(name="avg_npc_182#4",name2="avg_npc_180#2",focus=1)]
[name="审判官"]干什么？你以为连你都能拉住我？我可是审判官！
[dialog]
[character(name="avg_npc_180#2")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Dialog]
[delay(time=1)]
[character(name="avg_npc_182#5",name2="avg_npc_180#2",focus=1)]
[name="审判官"]这、这滑腻腻的......
[character(name="avg_npc_182#5",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]呼......打、打到了！差一点，审判官，好险。
[name="安妮塔"]幸亏你刚劈碎了这张椅子，我好拿起来当武器，把这东西砸烂呢。要不然它就要爬到你头上去啦！
[character(name="avg_npc_182#4",name2="avg_npc_180#3",focus=1)]
[name="审判官"]你、你这人！你们这里的人真是太奇怪了！
[name="审判官"]看到这些东西，你都不害怕的吗？
[character(name="avg_npc_182#4",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]有一点。不过还好，没有审判官可怕。
[character(name="avg_npc_182#5",name2="avg_npc_180#3",focus=1)]
[name="审判官"]......你居然，把我，和这些怪物相提并论？！
[name="审判官"]算了。我不跟你计较。你没见过这些，不知道它们能做什么，又怎么会觉得害怕？
[character(name="avg_npc_182#5")]
[name="审判官"]等一下，外面还有别的居民出来了。他们......他们在做什么？！
[name="审判官"]......他们也一点都不害怕。
[character(name="avg_npc_182#2")]
[name="审判官"]问题......
[character(name="avg_npc_182#3")]
[name="审判官"]我要看清楚问题所在。
[dialog]
[musicvolume(volume=0.2,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="所谓问题，即是眼前最不正常的那一点。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="审判官看了看面前的女孩，又看了看外面街道上独自站着的阿戈尔人。", x=300, y=370, alignment="center", size=24, delay=0.04, width=720)]
[Subtitle(text="她的视线最后落在跟着上街的其他居民身上。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_ibtownn")]
[character(name="avg_npc_188",name2="avg_npc_189")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.5)]
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]......
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]沙子。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]......盐。很咸。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]刚刚那个，能吃。都没了。可惜。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]可惜。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]盐也能吃。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]能吃。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]多一点，再多一点......唔呃，呕。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]弄脏了。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]咽下去。更多一点......
[dialog]
[character]
[delay(time=1)]
[musicvolume(volume=0.4,fadetime=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_1012_skadiSP_1#1",fadetime=1.5)]
[delay(time=3)]
[character]
[playsound(key="$rungeneral")]
[character(name="avg_npc_182#4",fadetime=1)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="审判官"]站住！
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]......
[character(name="avg_npc_182#4")]
[name="审判官"]我还有话要问你。你跟我说清楚——什么叫来找你的？
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]我流血了。
[character(name="avg_npc_1

... (全文20896字符)
```

### level_act18d3_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibindoor")]
[character(name="avg_npc_180#3")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[delay(time=1)]
[name="？？？"]没有尽头......浓雾弥漫......
[dialog]
[Subtitle(text="发着光的雾从不见底的深处升起，从头至尾，将她包裹。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="视觉、听觉、嗅觉、触觉，刹那间，她失去了对外界的一切知觉。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可她能感到面前有什么。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她的面前有整片大海。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="她用尽全力，对那庞大又近似无形的，挥出一击。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[delay(time=1)]
[Subtitle(text="她所感受到的一切都轰然崩塌。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="冰冷又炙热的液体将她吞没，那是洋流，也是海的血液。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="最后一支舞已经结束。海水安静下来，她也再听不见同僚的歌声。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她拯救了......不，她并不知道拯救了什么。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她同样不知道自己战胜了什么。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="她拼命地划动，双腿，双臂，可海水背叛了她的意志，变得又冷又硬，像是一团正在凝固的铁，从四面八方挤着她，使她的肢体愈来愈重。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="她不再动，将自己交托给大海。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="她在海里下坠。漆黑的影子缠住了她。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="无数声音有了实体，围绕在她四周。其中有哭喊，也有嘶吼，还有......呢喃。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="海在对她说话。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="深海恢复了它冰冷无光的本来面貌，她的双眼也是。她看不清向上的路。她不断不断地下坠，又不断不断地上升。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="在比深海更深处，温暖的海水托举着她，宛如许多血亲的臂膀。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她打开双唇，海水贯穿她的喉咙，她彻底溶解，而后重组。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她重新拥有了歌声。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=2)]
[musicvolume(volume=0,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="安妮塔"]哼哼~哼......♪
[character(name="avg_1012_skadiSP_1#2",fadetime=1,block=true)]
[name="斯卡蒂"]唔......
[character(name="avg_npc_180#3",name2="avg_1012_skadiSP_1#2",focus=1)]
[name="安妮塔"]歌手，你醒啦！早上好啊！
[character(name="avg_npc_180#3",name2="avg_1012_skadiSP_1#2",focus=2)]
[name="斯卡蒂"]谁在唱歌？
[character(name="avg_npc_180#3",name2="avg_1012_skadiSP_1#2",focus=1)]
[name="安妮塔"]这、这是歌吗？我不会唱。你睡着的时候，嘴里总在哼着这几句哩。
[character(name="avg_npc_180#3",name2="avg_1012_skadiSP_1#2",focus=2)]
[name="斯卡蒂"]我......
[dialog]
[CameraShake(duration=0.6, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#2",focus=1)]
[name="安妮塔"]哎哟！歌手你......你抓我抓得太用力啦......
[character(name="avg_npc_180#2",name2="avg_1012_skadiSP_1#2",focus=2)]
[name="斯卡蒂"]你......
[dialog]
[character(fadetime=0.5)]
[musicvolume(volume=0.4,fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="女孩的身影变得模糊。就像在海里。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[character(name="avg_1012_skadiSP_1#2",fadetime=1)]
[Subtitle(text="不，在海里的是她。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那个梦撕扯着她的神经。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="音符跳动着，扭曲成她的亲人们的哭嚎。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="斯卡蒂"]妈妈......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="她们在她眼前死去。她无能为力。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="斯卡蒂"]怪物......
[name="斯卡蒂"]怪物。
[name="斯卡蒂"]怪物！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="她们在喊叫。她身边的人都在喊叫。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她必须握紧她的武器。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[character(name="avg_1012_skadiSP_1#2",name2="avg_npc_180#2")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#2",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]啊！
[name="安妮塔"]咳咳......歌手，你的箱子......压得我胸口好疼......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="她一剑刺穿正在啃食人的怪物的身躯。", x=300, y=370, alignment="center", size=24, delay=0.04, w

... (全文23415字符)
```

### level_act18d3_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black")]
[character(name="avg_npc_180#2")]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Subtitle(text="女孩听话地闭上眼，松开手。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="缠着她小腿的力道很快消失了。她听到很多细小的物件落水的声响。在触到海面之前，她被一股力道拽了起来，然后落到了地面上。", x=300, y=370, alignment="left", size=24, delay=0.04, width=720)]
[Subtitle(text="——脸先着地。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Background(image="bg_ibcoastn")]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]咳咳咳......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]......对象是人的话，力道和角度很难控制。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]没、没事......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]（嗅了嗅自己）
[name="斯卡蒂"]是不流血了啊。
[name="斯卡蒂"]它们为什么还这么兴奋？这里的恐鱼本来就这么多吗？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]是昨天那种怪物吗？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]差不多。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]我以前没见过哩。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]这几天你们不要到这里来了。快回去。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]歌手。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]......不要拽我的裙子。你不是那么小的小孩子了。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]我是想说......我想好我要什么了。我想听你唱歌。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]哦......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]因为......我不知道什么是歌。我听到你在梦里哼了。但我听不懂。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]好。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]歌手，你答应了？这是不是就是约定？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=1)]
[name="斯卡蒂"]算是吧。
[name="斯卡蒂"]（皱眉）
[name="斯卡蒂"]我的琴。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]咦？是啊，歌手，你的琴去哪里了？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]......我回去找。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]好，我帮你一起找。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]这是不是说，你愿意跟我一起回去啦？太、太好了！
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#3",focus=1)]
[name="斯卡蒂"]......
[name="斯卡蒂"]真的......值得这么高兴？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character(name="avg_npc_187",name2="char_empty")]
[Background(image="bg_ibtownn")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="男性居民B"]......
[dialog]
[playsound(key="$d_gen_walk_n")]
[Character(name="avg_npc_187",name2="avg_npc_180#3",fadetime=1.5)]
[delay(time=2)]
[Character(name="avg_npc_187",name2="avg_npc_180#3",focus=2)]
[name="安妮塔"]嗨，墙灰，早上好呀！
[Character(name="avg_npc_187",name2="avg_npc_180#3",focus=1)]
[name="男性居民B"]铁皮......
[Character(name="avg_npc_187",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]对啊，铁皮去哪里了？你们之前一直形影不离啊。
[Character(name="avg_npc_187",name2="avg_npc_180#2",focus=1)]
[name="男性居民B"]铁皮。
[Character(name="avg_npc_187",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]你盯着的方向......是海......吗？
[name="安妮塔"]难道说，昨天抽到红色贝壳的人，是铁皮？
[name="安妮塔"]唉......
[Character(name="avg_npc_187",name2="avg_npc_180#2",focus=1)]
[name="男性居民B"]木框，我的病好像更严重了。
[name="男性居民B"]我的胸口很涨，像是要爆开一样。
[name="男性居民B"]我连东西都不想吃。你不要和我说话了。
[Character(name="avg_npc_187",name2="avg_npc_180#4",focus=2)]
[name="安妮塔"]......唉。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_ibbar")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_1012_skadiSP_1#1",fadetime=1.5)]
[delay(time=3)]
[Character(name="avg_npc_180#3")]
[name="安妮塔"]歌手，欢迎再次来到我们家！
[character(name="avg_npc_179#1")]
[name="老年居民"]呃......啊......
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]你奶奶......
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]佩特拉奶奶还在休息呢。昨天我们一起回到这里，她就一直躺着。
[name="安妮塔"]我想，她也消耗了很大体力，肯定很累了。我没想到她会冲出来，对审判官那样说话。她变得和平时都不一样。
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]你说的对。她很......厉害。她打退了审判官。
[character(name="avg_npc_179#1")]
[name="老年居民"]呵......哈......
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]打退了......审判官？！歌手，你这么说，要是让审判官听见，她一定又要生气了。
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]随便她。
[name="斯卡蒂"]要是她想再动手......
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=2)]
[name="安妮塔"]她不会再来找你麻烦了吧？
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#1",focus=1)]
[name="斯卡蒂"]......找谁的麻烦都一样。
[name="斯卡蒂"]（摸箱子）
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=2)]
[name="安妮塔"]对了，我们出去找琴吧！
[Character(name="avg_1012_skadiSP_1#1",name2="avg_npc_180#2",focus=1)]
[name="斯卡蒂"]等一下。
[Character(name="avg_1012_skadiSP_1#1"

... (全文17531字符)
```

### level_act18d3_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcoastn")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Subtitle(text="海滩上已经铺满了食物。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="人们的请求得到了大海的回应。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_188",name2="char_empty",fadetime=1.5)]
[delay(time=2)]
[name="男性居民C"]......
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_188",name2="avg_npc_189",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]鳞。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]......壳。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]能吃。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]能吃。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]多一点，再多一点......塞满嘴巴。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]漏了。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]捡起来，吞下去。更多一点......
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]带走。带回去。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]带回去。塞满身体。塞到塞不下。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]教士......
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]教士。
[dialog]
[character(name="avg_npc_188",name2="avg_npc_189")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="他们愿意暂时停下来。他们抬起头，望向他们的兄弟。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",fadetime=1.5)]
[delay(time=2)]
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]兄弟姐妹们，尽情享受你们的早餐吧。
[name="主教"]这是对善行的奖赏，只因饥渴与病痛并未击溃我们，而是令我们更加真挚，更加团结，更加友爱。
[character(name="avg_474_gladiia_1#5",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]......
[name="歌蕾蒂娅"]这种长篇大论的表演，从一个城市到另一个城市，你竟不觉得腻。
[character(name="avg_474_gladiia_1#5",name2="avg_npc_184",focus=2)]
[name="主教"]何为表演？将祂的伟岸与仁爱带到陆上，令无知者领受，我本就乐意之至。
[character(name="avg_474_gladiia_1#5",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]他们什么都听不懂。
[character(name="avg_474_gladiia_1#5",name2="avg_npc_184",focus=2)]
[name="主教"]我们的海洋将一视同仁。
[dialog]
[character(name="avg_npc_184")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="主教慈爱地拍了拍正在努力吞咽的男人的胳膊。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="主教"]来吧，兄弟，将你手上这块鳞肉分享给你受苦的兄弟。你要相信，舍下这一小块，他的满足会使得你的心灵愈加满足。
[character(name="avg_npc_188",name2="avg_npc_189",focus=1)]
[name="男性居民C"]......
[character(name="avg_npc_184")]
[name="主教"]而你，你应同你的兄弟道谢，感激他舍下他本可以拥有的。
[name="主教"]你俩站在一起，手握着手，足抵着足，共享彼此的性命，自此你们将更伟大。
[character(name="avg_npc_188",name2="avg_npc_189",focus=2)]
[name="男性居民D"]谢......教士......老爷。
[character(name="avg_npc_184")]
[name="主教"]乖孩子。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]约定并不在你与它之间。而是他们和它，经你的手。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]约定？不，约定是双向的，这些受苦的人还不足以令大海有所求。
[name="主教"]他们请求，大海给予回应。而我帮助他们，令他们的声音能被听见。
[name="主教"]你既然已将自己当作我们的一部分，你自然清楚规则。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]请原谅我的生疏。我可以换上更恰切的措辞——你将他们的血肉筑成通路，从而在教会内部获得你想要的。
[name="歌蕾蒂娅"]无论怎么说，你没必要每次现身。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]你怎知我要什么？
[character(name="avg_474_gladiia_1#5",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]高人一等的快感很容易使人沉溺。
[character(name="avg_npc_184")]
[name="主教"]谬误。
[name="主教"]身为海的最虔心的造物，我的地位并非伪妄。
[name="主教"]我站在这里，只是因我发自真心想救他们。若是没有我，他们早就化成了这陆上的一滩滩肮脏腐肉。
[name="主教"]疾病，饥饿，这些具体的敌人，如果还能对抗，便不是最深的苦难。最深的苦难来自人心灵的深处。
[name="主教"]当人们发现灾难已无法对抗，他们无论做什么都将把自己引向不可避免的衰亡，这才是真正苦难到来之时。
[name="主教"]像这样的城镇，伊比利亚还有多少？
[name="主教"]这片庞大的国土早已支撑不起人们对它的诉求，这里的人与人却依旧困缩在各自逼仄的皮囊内，或彼此隔绝，或互相争斗。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]您对伊比利亚的关心令人赞叹。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]你又错了。我在意人们的苦，而非区区陆上的国境线。
[name="主教"]人都是如此，不是么？
[name="主教"]囿于自身肉体的限制，难以凭自己的力量打开对自我和对族类的执着，一味地选择对抗而非理解。
[name="主教"]这样下去，再强大的个体都免不了被逐个击破，苦难终将吞噬每一个角落。你也曾见证，你也曾动摇。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]对我说这些，真的有必要？
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]或许我说的还不够多。
[name="主教"]真知总是值得传述，无论听者是否愚钝如你。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]......
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]又或者，看在这段时间的共事之情份上，不如将这段话作为消磨等待时间的小小娱乐。
[character(name="avg_474_gladiia_1#1",name2="avg_npc_184",focus=1)]
[name="歌蕾蒂娅"]您的言语技巧的确非同凡响。难怪沉迷的人这么多。
[character(name="avg_npc_184")]
[name="主教"]你仍然无法理解。我比真诚更真诚。我对他们并无诉求，我亦不相信强迫的力量，我只想向他们指出一种新的可能性。
[name="主教"]身体的弱小将永远限制他们的认知。你以为我是在通过言语诱使他们心灵信服，恰恰相反。
[name="主教"]我是在令他们的心灵听从身体最基本的诉求。圣人的训导能带来的不过是一时的盲信，肉身的强大才能令他们有资格亲眼看见更多。
[name="主教"]海里有些生物。它们没有眼睛，身体微小，无法游动，只能随着潮汐漂荡。
[name="主教"]它们见到的大海，与我们见到的有多大区别？没有眼睛的生物又何从领会大海的神圣与深邃？
[name="主教"]你与你的同僚，你们不知从何处谋取了这层卑劣却坚硬的皮囊。你们看不见这些弱小的正如何挣扎。
[name="主教"]试问谁才是真正的傲慢？
[name="主教"]是正在帮助他们的我，还是那些借着危难扩张，利用言语、将真正的绝望替换成虚假的希望，欺瞒、控制悲惨弱者，从而盗取权柄的伪神教徒？
[name="主教"]又或者——是从来不愿意正视海底的愚蠢的你们？
[name="主教"]我将我看见的分享予他们，令他们打开视野，知晓自己仍有真实

... (全文24123字符)
```

### level_act18d3_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibtownn")]
[character(name="avg_npc_180#3")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="安妮塔"]今天拿的够多了吧？除了我、佩特拉奶奶、长凳的份......
[name="安妮塔"]唔，还有歌手，歌手还会回来的吧？也不能让她饿肚子。
[dialog]
[delay(time=1)]
[name="安妮塔"]剩下的......还有多。可以存盒子里。
[name="安妮塔"]呃，壁炉叔，你想要吗？那、那我还是先给你。
[name="安妮塔"]哇哇，你胳膊上缠着的这些好像是海藻哎！给我吧，我要试试做歌手教我的......呃，海藻酒！
[character(name="avg_npc_180#2")]
[name="安妮塔"]咦，长凳呢？一晃眼又跑哪里去了？
[dialog]
[character]
[name="幼年居民"]咿呀......啊......
[dialog]
[delay(time=1)]
[musicvolume(volume=0,fadetime=1)]
[character(name="avg_1012_skadiSP_1#4",fadetime=0.6)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="一道红色的身影出现在他跟前。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character]
[musicvolume(volume=0.4,fadetime=1)]
[name="幼年居民"]啊......歌......啊啊......
[character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]......别抓。
[name="斯卡蒂"]这个给你。
[dialog]
[character]
[name="幼年居民"]呜哇......
[character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]......别啃。不能吃。
[dialog]
[character]
[name="幼年居民"]木框，木框......
[character(name="avg_1012_skadiSP_1#4")]
[name="斯卡蒂"]......别叫她。
[name="斯卡蒂"]嗯，你帮我把琴带给她。
[name="斯卡蒂"]告诉她......不，你没法告诉她。
[name="斯卡蒂"]这还不是再见。
[name="斯卡蒂"]我去问问题。然后，我会自己说。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="斯卡蒂的目光投向高处的教堂。她清楚剩下的路该怎么走。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character(name="avg_npc_182#1")]
[Background(image="bg_ibcoastn")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="审判官艾丽妮"]长官，我们现在就要在山体上安置爆破物吗？
[Character(name="avg_npc_183#3")]
[name="大审判官"]是。
[Character(name="avg_npc_182#1")]
[name="审判官艾丽妮"]另一方面，我看见一个人进了教堂。
[name="审判官艾丽妮"]她看起来和我们之前遇见过的那个外来人......很像。
[Character(name="avg_npc_183#3")]
[name="大审判官"]......
[Character(name="avg_npc_182#2")]
[name="审判官艾丽妮"]那，长官，她到底是什么人？
[Character(name="avg_npc_183#3")]
[name="大审判官"]阿戈尔人。
[Character(name="avg_npc_182#2")]。
[name="审判官艾丽妮"]我听说了，她和恐鱼战斗了。
[name="审判官艾丽妮"]......除了我们之外，竟然还有人知道这些怪物，专门和这些怪物战斗......
[name="审判官艾丽妮"]如果我们炸毁教堂......她会受到波及吗？
[Character(name="avg_npc_183#3")]
[name="大审判官"]不解决首恶，将这里毁灭也无用。
[Character(name="avg_npc_182#2")]
[name="审判官艾丽妮"]这样吗？所以还是得知道，是谁在这里引起了异象......长官也不能确定吗？
[Character(name="avg_npc_183#3")]
[name="大审判官"]你不可问你任务之外的事。
[Character(name="avg_npc_182#1")]
[name="审判官艾丽妮"]......明白了。
[name="审判官艾丽妮"]另外，虽然我知道长官你不在意，但我还是想说说......这个区块的承重结构，承受不住我们设计的爆炸的威力。
[name="审判官艾丽妮"]南半侧的城市随时都可能塌陷，这里的居民却还不知道这个消息。
[Character(name="avg_npc_183#3")]
[name="大审判官"]继续说。
[Character(name="avg_npc_182#1")]
[name="审判官艾丽妮"]呃......
[name="审判官艾丽妮"]......
[Character(name="avg_npc_182#3")]
[name="审判官艾丽妮"]我想去疏散他们。
[name="审判官艾丽妮"]哪怕他们在长官你看来是古怪的，有问题的......
[name="审判官艾丽妮"]......应该被净化的。
[Character(name="avg_npc_183#3")]
[name="大审判官"]判官！
[Character(name="avg_npc_182#5")]
[name="审判官艾丽妮"]呃......！
[Character(name="avg_npc_183#3")]
[name="大审判官"]说出你的职责！
[Character(name="avg_npc_182#4")]
[name="审判官艾丽妮"]是！
[name="审判官艾丽妮"]“我是为了伊比利亚的存续，为了同伊比利亚的敌人而战，为了守卫伊比利亚的洁净与德行，提起了剑与灯！”
[Character(name="avg_npc_183#3")]
[name="大审判官"]那么你必须对他们做出判决！
[Character(name="avg_npc_182#5")]
[name="审判官艾丽妮"]判决？判处他们......死刑吗？
[Character(name="avg_npc_182#2")]
[name="审判官艾丽妮"]长官，你上一次听到过去的歌声，是什么时候？那些唱片，都已经坏了吧？你的机器也落灰很久了吧？
[name="审判官艾丽妮"]我听见那首歌。我听见了这个阿戈尔人给他们唱的歌。
[name="审判官艾丽妮"]那样的歌，是伊比利亚原本该有的歌。
[Character(name="avg_npc_182#3")]
[name="审判官艾丽妮"]在杀死他们以前，我想知道真相。就像长官你想揪出幕后主使者。
[name="审判官艾丽妮"]也许他们还是会变异，到那时候，我一定会亲手净化他们，但现在我想让他们先去避难。
[name="审判官艾丽妮"]长官，如果你同意，我立刻就会去进行疏散！
[Character(name="avg_npc_183#3")]
[name="大审判官"]这就是你的判决？
[Character(name="avg_npc_182#3")]
[name="审判官艾丽妮"]长官，我不知道！
[Character(name="avg_npc_183#3")]
[name="大审判官"]艾丽妮，你不止在对面前的人下判决。你也在对其他人下判决！
[name="大审判官"]你判决怪物生，就是判决人民死！
[Character(name="avg_npc_182#3")]
[name="审判官艾丽妮"]我明白！这样的判决，我已经下过许多次！
[Character(name="avg_npc_183#3")]
[name="大审判官"]你的判决，既可能阻绝灾难，也可能带来噩兆！你可能救一人而杀百人，也可能杀百人而救一人！
[Character(name="avg_npc_182#3")]
[name="审判官艾丽妮"]......我明白，长官！
[name="审判官艾丽妮"]这里面的利害关系，道德和经文的冲突......我都明白！
[Character(name="avg_npc_183#3")]
[name="大审判官"]我问你这个了吗？
[Character(name="avg_npc_182#2")]
[name="审判官艾丽妮"]......
[Character(name="avg_npc_183#3")]
[name="大审判官"]我问你的是，艾丽妮，这种责任是你能承担得了的吗？
[name="大审判官"]如果你会带来痛苦，你就必须也遭受痛苦，而且要比你施加给别人的那些罪恶加起来还要多。
[name="大审判官"]你有这种胆识吗？你的信仰会在你遭受内心折磨时动摇吗？如果你失败了，你造成了恶果，你会因此一蹶不振吗？
[Character(name="avg_npc_182#3")]
[name="审判官艾丽妮"]......我能承担。我不会动摇。
[name="审判官艾丽妮"]在我加入审判庭的时候，我就已经这么做了。我能。如果我做错了，那么就让我遭受责罚。我必须做。
[name="审判官艾丽妮"]长官！我——
[Character(name="avg_npc_183#3")]
[name="大审判官"]可以了。
[Character(name="avg_npc_182#5")]
[name="审判官艾丽妮"]唔......
[Character(name="avg_npc_183#3")]
[name="大审判官"]可以了。现在去履行你的职责，判官。
[Character(name="avg_npc_182#4")]
[name="审判官艾丽妮"]——是，长官！我立刻就去疏散当地居民！
[name="审判官艾丽妮"]还有，长官......经匣里剩下的爆破物应该够炸毁整座盐风城。
[Character(name="avg_npc_183#3")]
[name="大审判官"]是的。
[Character(name="avg_npc_182#2")]
[name="审判官艾丽妮"]所以......
[Character(name="avg_npc_183#3")]
[name="大审判官"]如有必要，你的判决将被我废除。
[Character(name="avg_npc_182#6")]
[name="审判官艾丽妮"]......是。
[Character(name="avg_npc_182#4")]
[name="审判官艾丽妮"]那我去了，老师。
[dialog]
[playsound(key="$rungeneral")]
[character(fadetime=1)]
[delay(time=2)]
[Character(name="avg_npc_183#3")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="艾丽妮风一般地跑开了。", x=300

... (全文7624字符)
```

### level_act18d3_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcave")]
[character(name="avg_npc_184")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="主教"]杂种......你们两个杂种——
[name="主教"]使者！你在做什么？！你为什么留住她们？她们怎么值得你这么做？！
[name="主教"]在她们对我们同胞大肆杀戮的时候，你们就该意识到她们和你绝对不是一种东西！
[name="主教"]你是神圣的生命！她们只是污浊的残渣！
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]（啐）
[name="歌蕾蒂娅"]很会适应，是不是？
[name="歌蕾蒂娅"]我们用冷兵器去砍杀你们，让你们对技术不那么敏感，不让你们进化成其他手段也解决不了的样子。
[name="歌蕾蒂娅"]现在我却高估你了。你太不敏感了......这都适应不了？
[name="歌蕾蒂娅"]看起来你习惯不了阿戈尔材料学造出来的刀刃。是不是？
[dialog]
[character]
[Character(name="avg_npc_186")]
[name="海嗣"]——
[character(name="avg_npc_184")]
[name="主教"]使者，她在侮蔑你！
[character(name="avg_474_gladiia_1#4")]
[name="歌蕾蒂娅"]主教，主教......你还看不出吗？呵呵，是的，我就是有自信杀了你。我从最开始就能杀掉你。
[character(name="avg_npc_186")]
[CameraShake(duration=0.8, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[name="海嗣"]（低鸣）
[name="海嗣"]呜......（咳嗽）
[name="海嗣"]兄弟，你为什么不接受？
[name="海嗣"]她们都是我姐妹。所以她们也是你姐妹。
[name="海嗣"]我能唤起你，唤起Ishar-mla，当然......也唤起Gla-dia。
[name="海嗣"]你因为你兄弟，游向浅海，就不认他，那样只是......不在乎。
[name="海嗣"]我们，族群，都在乎。
[character(name="avg_npc_184")]
[name="主教"]不......妄言......
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]你难道相信过你手中经书的任何字句？允我提醒，你也是在伊比利亚的眼皮底下宣传邪说，主教。
[name="歌蕾蒂娅"]它说什么我都无所谓，可你，深海教会的人，是不是把他的话都用本子记下来会比较好？
[character(name="avg_npc_184")]
[name="主教"]杀了他们......杀了她们！使者！动手！她们犯下了大罪！他们亵渎了你，亵渎了海洋？
[character(name="avg_npc_186")]
[name="海嗣"]你这样要求......我真会这么做。
[character(name="avg_npc_184")]
[name="主教"]你也无所谓，对吗？就像你和我说的一样，我这么要求也没问题！你会杀了她们！
[character(name="avg_npc_186")]
[name="海嗣"]是的。我依然无所谓。
[character(name="avg_npc_184")]
[name="主教"]先去杀了那个......吟游诗人。把那个红衣服的先杀掉！
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]垃圾。是不是我让你去杀掉你身后的人，杀了你身后穿得像条海带的主教，你也会这么做？
[character(name="avg_npc_186")]
[name="海嗣"]是的。
[character(name="avg_npc_184")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="主教"]......！！！
[character(name="avg_npc_186")]
[name="海嗣"]因为他是我同胞，你也是我同胞。他在呼唤我，你也在呼唤我。
[character(name="avg_474_gladiia_1#3")]
[name="歌蕾蒂娅"]人类啊。
[name="歌蕾蒂娅"]阿戈尔人可真是又卑劣又丑陋。承认吧，主教。
[name="歌蕾蒂娅"]我们都是些愚蠢的阿戈尔人，喜欢把自己的想法去套在畜生身上。你根本不懂它。
[character(name="avg_npc_184")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="主教"]杂种！！
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]只不过，如果你想保护我们的生命——为什么不拒绝？
[character(name="avg_npc_186")]
[name="海嗣"]拒绝？
[name="海嗣"]怎么样......拒绝？
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]行了，的确是劣等生物。你只游到这个深度。
[character(name="avg_474_gladiia_1#3")]
[name="歌蕾蒂娅"]但是，垃圾，听好，我不会开口请你去杀你背后那个软蛋。
[name="歌蕾蒂娅"]你只是猎物。谁会恳求自己的猎物？
[name="歌蕾蒂娅"]你想动她？你听从他的建议，想杀斯卡蒂，我的猎人？你不想再要那个答案了？
[character(name="avg_npc_186")]
[name="海嗣"]杀了她也有其他办法。只要还有办法，我就无所谓。
[name="海嗣"]但你说的，拒绝......
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]太早了。咳......
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="歌蕾蒂娅"]（咳血）
[name="歌蕾蒂娅"]呸。我不管你。你想杀她——你得先通得过我。
[character(name="avg_npc_186")]
[name="海嗣"]那么，Gla-dia。
[name="海嗣"]你的生命能不能延续，你肉体以后还能不能活动，你来选能还是不能。
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]用相互猎杀来选。
[character(name="avg_npc_186")]
[name="海嗣"]相互......相互。是的。用相互捕食来选。你捕食我。我捕食你。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### level_act18d3_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcave")]
[character(name="avg_474_gladiia_1#3",name2="avg_npc_186")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[name="歌蕾蒂娅"]嘶——
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="海嗣的身体再一次被歌蕾蒂娅洞穿。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Subtitle(text="海嗣将死。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="海嗣没有把“脸”转向主教。旁人也不可能知道海嗣是否长着眼睛，但斯卡蒂就是能感觉到怪物的视线——至少她自己这么觉得。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="它正“看着”主教。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="无形的洋流正冲刷着主教，袍裙沉重地压在他的身上，几要把他摧垮。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但海嗣正对她们说话。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_474_gladiia_1#3",name2="avg_npc_186",focus=2)]
[name="海嗣"]你们是更像我......还是更像他？
[name="海嗣"]Gla-dia。 你很强壮。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="歌蕾蒂娅冰冷地注视着猎物。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="海嗣"]情绪。会有我们血亲学习的。我们也在传达许多，我们会试着传达给你们。
[name="海嗣"]Ishar-mla。活着吧。活着会很好。下一次会有其他血亲找到你......向你询问。
[name="海嗣"]我们不太会问问题。我们会学会。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[characteraction(name="right", type="move", ypos=-25, fadetime=2,block=false)]
[stopmusic(fadetime=2)]
[character(name="avg_474_gladiia_1#5",name2="char_empty",fadetime=2)]
[delay(time=2.5)]
[Subtitle(text="慢慢地，海嗣低哼着蹲下去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="怪物的躯体不再起伏。它蜷缩起来，像一朵迅速枯败的花。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]——死了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="斯卡蒂如释重负。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不，不能这么说。她并没有从真相中恢复过来。但这个猎物的死让她感受到......", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="它到底也只是个生物。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[character(name="avg_npc_184")]
[name="主教"]你们这些孽种。
[delay(time=1)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="主教提高了音量。零碎的声响在他的喉头，在激烈战斗留下的碎屑中爬行，像是他的声带正不住嘟囔。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="歌蕾蒂娅甚至没去看他。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]是，上前来。现在轮到你。
[name="歌蕾蒂娅"]这只垃圾孑然一身。外面那些恐鱼也不是它这族的。那么，只会是你的了。
[character(name="avg_npc_184")]
[name="主教"]我来把你们撕碎。我来让你们亵渎的行径受罚。
[name="主教"]我自己来。是得在这里把你们这些杂种都解决掉。生命可贵，但留你们的命是浪费资源。
[name="主教"]一个重伤的孽种。一个动弹不得的孽种。我会把你们的残渣抛洒在大地上，让最低贱的陆地生物吃掉你们的一切。
[name="主教"]杀死你们两个，轻而易举——
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]不用再装了。比起海嗣这些垃圾，还是你们这种曾经是人，现在又伪装成人的最让人反胃。
[character(name="avg_npc_184")]
[name="主教"]（嘶吼）
[name="主教"]你们会死在这里！
[dialog]
[stopmusic(fadetime=1)]
[character]
[delay(time=1)]
[name="？？？"]是不是把我忘了？
[delay(time=1)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_474_gladiia_1#4")]
[Subtitle(text="斯卡蒂翻了个白眼。歌蕾蒂娅笑了笑。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[character(name="avg_npc_184")]
[Subtitle(text="主教迟疑了一下，转过头去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### level_act18d3_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcave")]
[character(name="avg_474_gladiia_1#4")]
[Delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="歌蕾蒂娅"]斯卡蒂，动得了吗？
[character(name="avg_1012_skadiSP_1#2")]
[name="斯卡蒂"]我不清楚。克制那种感觉......难。我好难不去想那些东西。
[name="斯卡蒂"]我的手指没法动。我一动，我的指甲就好像都会从我手上游走。
[character(name="avg_474_gladiia_1#4")]
[name="歌蕾蒂娅"]神经细胞在急速新陈代谢，始终记住，你是个猎人，它们动不了你。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]这么想有用？
[character(name="avg_474_gladiia_1#4")]
[name="歌蕾蒂娅"]你不想成为海嗣，你就不会。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]好。
[name="斯卡蒂"]我想......我能拿起武器。
[dialog]
[character]
[character(name="avg_npc_184")]
[name="主教"]没有武器的杂种，重伤的杂种，感染的杂种，你们能做什么？
[dialog]
[delay(time=1)]
[name="主教"]你那表情是什么意思？开始觉得自己高贵了吗？
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]我？
[name="斯卡蒂"]等等，奇怪......你会错意了。
[name="斯卡蒂"]你别以为那个海嗣让我有些难过，你就也配了。砍死你就完事儿了。 ​
[character(name="avg_474_gladiia_1#3")]
[name="歌蕾蒂娅"]——
[name="歌蕾蒂娅"]你真以为箱子里是萨克斯吗？
[name="歌蕾蒂娅"]小美人鱼，你还要睡多久？睁眼。过去的事情困不住你。
[character(name="avg_npc_184")]
[name="主教"]......她也只是个试验品！
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]鲨鱼，你早醒了吧？
[dialog]
[character(name="avg_npc_184")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="主教转过头去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="幽灵鲨抚摸着玻璃缸壁，用既好奇......又温柔的眼神看着主教。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="主教"]什么......这么高浓度的源石液都......
[dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="主教跌跌撞撞地向后退，却想起两位深海猎人还在身后。这让他不自主地僵立原地。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="幽灵鲨摆出几个口型。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="似乎是很凶残的词汇。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1",name2="avg_474_gladiia_1",focus=2)]
[name="歌蕾蒂娅"]看到你的老样子真不错，鲨鱼。
[character(name="avg_1012_skadiSP_1",name2="avg_474_gladiia_1",focus=1)]
[name="斯卡蒂"]呃。我都快忘了她是这个性子。
[dialog]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1#1")]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Subtitle(text="斯卡蒂踢开箱子。里面躺着一把剑，没错，箱子里安放着她的巨剑......以及一把长柄圆锯。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]啊，手还是好麻。
[name="斯卡蒂"]罗德岛混了这么几年，这点准备我还是做得好的。接着。
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$bottlebroken")]
[Subtitle(text="斯卡蒂微侧身子，猛地一挥，将圆锯掷向了玻璃缸。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="主教慌忙躲闪，可旋锯裹挟的狂风还是把他的长袍撕开了长长的口子。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="就在这凶残的武器就要把玻璃缸连人一同撞烂的瞬间，一只苍白的手击碎了玻璃。水流从缸中喷泄而出，那只手不顾飘散半空的锋利玻璃碎渣，自碎片中一把握住了巨锯。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="她手掌与圆锯握柄间的玻璃碎片在她一抓之下，全都化作亮闪闪的粉尘，自她指缝间滑落。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="而幽灵鲨，当然，手上连个划痕都没有。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="猎人苏醒了。幽灵鲨苏醒了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_143_ghost#2",fadetime=1)]
[delay(time=1.5)]
[name="幽灵鲨"]就不能让我再害羞会儿吗？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="幽灵鲨意味深长地笑了笑。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="幽灵鲨"]做了那么长时间乖巧的修道女，我都不知道该怎么面对你俩呢。
[character(name="avg_474_gladiia_1#3")]
[name="歌蕾蒂娅"]出来吧。别玩了。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]这么长时间过去，我也不知道自己是习惯现在的你，还是疯疯癫癫又有点自闭的那个了。
[dialog]
[character]
[character(name="avg_npc_184")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="主教还没回过神，水缸里的掠食者就跌出了她脆弱的牢笼。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Subtitle(text="接下来，就是一锯子锯在这个始作俑者身上的事。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[CameraShake(duration=0.8, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Subtitle(text="惨嚎回荡在溶洞。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]哇，好硬。
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]鲨鱼，回来！他已经是海嗣了！
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1#1")]
[Subtitle(text="恶臭扑鼻而来，斯卡蒂顿时就知道了谁才是怪象的源头。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="斯卡蒂"]二队长，幽灵鲨......先离开这！
[dialog]
[charac

... (全文24677字符)
```

### level_act18d3_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcave")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="残垣断壁里，怪物将死的臃肿肉体填塞了大半个溶洞。它原本不断散发出奇异之美的古怪躯体因它对死亡的畏惧而愈显僵硬。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_474_gladiia_1#5")]
[name="歌蕾蒂娅"]四处都在漏水。了结它，我们得走了。
[character]
[name="主教？"]为什么你们这种瞎了眼睛的庸人能苟活？为什么我这样为事业投入了生命，专注于伟大目标的人......会失败？
[name="主教？"]盲目、停止流动的阿戈尔拴着的宠物......你们对科学和未来......毫无助益！
[name="主教？"]我已......几近真理！为什么我要死在这里？！而你们......却能逃脱你们应得的酷刑？
[name="主教？"]我走了这么远，我的意志和肉体，都快要撕碎人类躯壳的束缚了！为什么？
[name="主教？"]为什么？为什么？！为什么！！
[character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]闭嘴。
[character]
[name="主教？"]......
[name="主教？"]阿戈尔......必定毁灭。你们什么都不剩......什么都......
[character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]蠢材。我活着，我就是阿戈尔，我活着，阿戈尔就活着。
[character]
[name="主教？"]......你......但......
[name="主教？"]讽刺......讽刺。
[name="主教？"]你是不一样的。呼......你注定不同......
[name="主教？"]你很清楚。你的命运已定。
[character(name="avg_474_gladiia_1#2")]
[name="歌蕾蒂娅"]不要再废话连篇了。请你乖乖死掉，对你我只剩下这个请求。我很真诚的。
[character]
[name="主教？"]我诅咒你们......我要诅咒你们......直到陆地被淹没......你们会像盐粒一样，逃出大海......最后还是被大海溶解。
[name="主教？"]在你们的尸骨堆砌的贫瘠荒原上，我们鼓动不歇的潮声会在苍白夜空下浸没大陆！
[dialog]
[character(name="avg_474_gladiia_1#2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="歌蕾蒂娅似乎在克制。她最后一点礼貌来自她白净面容藏不住的厌恶。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="呜咽般的喉声自主教伸向歌蕾蒂娅的触肢里传来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但在触及猎人前，这条触肢就已经僵化，抽搐，蜷缩成一团。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="主教死去了。他的一切都将被遗忘。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="歌蕾蒂娅看着幽灵鲨和斯卡蒂。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Image(image="ac18_12_1",xScale=1.2,yScale=1.2, fadetime=0)]
[ImageTween(xFrom=-30, xTo=30, duration=25, block=false)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[stopmusic(faddetime=2)]
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]总算死了。这事情也算是结束了......我亲手杀了它。没我想象里那样令人高兴。
[name="幽灵鲨"]比起他们对我做的这些，真是太轻了。杀了一个，还有两个。
[name="幽灵鲨"]呃，头又有点晕了。我是怎么过来的？简直就像一直在做梦。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]鲨鱼？
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]毕竟......没法一直醒着。
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]我们抓到了他们的触手，现在顺着摸过去，把他们连根拔起，一定能找到治好你的办法。
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]也没那么大所谓。现在它们控制不了我，我感觉很好。自由的感觉......竟然是在这时候。我快飘起来了。
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]但是，队长，你们说的我都听到了。
[name="幽灵鲨"]它是说我们也会变成海嗣？队长，你会变成特别厉害的那种？还挺强的。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]不会的。
[name="斯卡蒂"]你和它们可太不一样了。
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]希望我没有因为自己的独断专行而害了你们。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]回答我几个问题。
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]我有问必答。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]我们体内流着海嗣的血？
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]对。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]你来这里是为了确认幽灵鲨身体问题的原因。你之所以要吃那一下是为了知道为什么海嗣想找我。
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]是。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]你早就知道这里不止主教一只海嗣？
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]对。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]你知道我们那场自杀一样的决战的最后，我做了什么吗？
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]不知道。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]我们赢了吗？
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]我也不知道。我与阿戈尔失去了联系。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]......我们是不是阿戈尔的弃子？
[dialog]
[character]
[character(name="avg_474_gladiia_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="是？深海猎人就像诱饵。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是？深海猎人就像海底的光亮。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是？深海猎人的力量这样巨大，却只是阿戈尔的万分之一。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="是？深海猎人的特殊，只在于他们的确和海怪有联系。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="怒火在斯卡蒂红色的瞳孔里打转，但那一点点希望......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="多少是真话，多少是谎言......？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[PlayMusic(intro="$newhope01_intro", key="$newhope01_loop", volume=0.4)]
[Image(image="ac18_12_2",xScale=1.2,yScale=1.2, fadetime=1.5)]
[delay(time=2)]
[name="歌蕾蒂娅"]不是。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]行了。走吧。
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]真爽快。
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]没什么好磨蹭的。我到底是个深海猎人。
[name="斯卡蒂"]......难道二队的人不这样？
[character(name="avg_474_gladiia_1#4")]
[name="歌蕾蒂娅"]深海猎人都这样。
[stopmusic(fadetime=1)]
[character(name="avg_1012_skadiSP_1#8")]
[name="斯卡蒂"]这里快塌了，而且......
[dialog]
[character]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="仿佛被主教的尸体所吸引，恐鱼们从溶洞的裂口处钻了进来。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="密密麻麻。", x=300, y=370, alignment="center", size=24, 

... (全文8597字符)
```

### level_act18d3_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibchurch")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_184")]
[name="主教"]快快，请进，请进。我知道你会来这里的。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]你怎么知道？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]该怎么解释呢......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]呵。不用了。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]你到哪里都会背着那个箱子吗，吟游歌手？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]是。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]那你介意我再问个问题吗？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]问。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]这箱子里装的是什么？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]萨克斯。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]啊，真不错，萨克斯......吹奏乐器吗。不错。
[name="主教"]我是否有幸听听它的音色？音乐......这座城市已经许多年没有音乐响起了。
[name="主教"]哦，不，抱歉......我忽然想到，吟游歌手要拿报酬。
[name="主教"]这可难住我了，您看，恐怕我拿不出什么赏钱。
[name="主教"]且看这座老建筑。哼，打理它是件相当困难的事，货币在这里代表不了什么，没人收集，也没人用。
[name="主教"]但我也有提供一顿午餐的余力。吟游歌手，怎么样？你愿不愿意随便演奏点什么？
[name="主教"]请你吃顿饱饭这种事我还算是能做到的，虽然也不是什么美味佳肴......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]......
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]看你沉默不语的样子......啊，会不会是这样：比起音乐，你更喜欢舞蹈？
[name="主教"]你看，你还穿着舞裙......有天赋的人。我们可太久没在这见到你这样光彩照人的朋友了。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]（......肉麻。）
[name="斯卡蒂"]你如果要听什么，当时你就可以让我唱。不用到这。
[name="斯卡蒂"]我来是要问一个问题。你身边站着的这个人可能知道，现在我觉得你也脱不开干系。
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]......
[character(name="avg_npc_184",name2="avg_474_gladiia_1#1",focus=1)]
[name="主教"]我的，这位——熟人，过去和你认识吗？
[character(name="avg_npc_184",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]自然认识。
[character(name="avg_npc_184",name2="avg_474_gladiia_1#1",focus=1)]
[name="主教"]没有问你。
[dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_474_gladiia_1#1")]
[Subtitle(text="歌蕾蒂娅别过头去，不再言语。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]不认识。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]哦......？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]因为我不知道这个人是不是我当初认识的那个了。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]哦，哦......
[name="主教"]这个，也是正常的。人都是会变的。海水拍打陆地，假以时日也能让海岸变成沙子。
[name="主教"]所以你来这里，不是她让你来的？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]——不是你让我来的吗？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]仅仅是我让你来，你是不会来这里的，对吧。我只是个陌生人。
[name="主教"]我只是问，她有没有让你来这里？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]没有。我是自己来的。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]嗯，你没有说谎。我能听出谎言......但你是诚实的。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]问这问那，我却什么都还没说，你怎么能这么讨人厌？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]消气，消气，歌手。我不是故意的。谨慎一点对我们都有好处。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]那我来问。
[name="斯卡蒂"]这座城市里的人很信任你，但是，在海岸上发生的那些事——
[name="斯卡蒂"]绝对不正常。
[name="斯卡蒂"]乞食。恐鱼。海。
[name="斯卡蒂"]你是哪里人？你是不是知道些什么？你和她对我隐瞒了什么？
[dialog]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]啊，哈哈。是的，我知道的比别人确实要多一些。
[name="主教"]确实，我知道有人想见你的。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]见我？因为我是个吟游歌手？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]在乎音乐的是我。
[name="主教"]虽然这听上去有些荒唐，但想见你的其实不是我。
[name="主教"]想见你的是我的一位朋友。应他要求，我才邀请你来到这里。
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=1)]
[name="斯卡蒂"]谁？他想见我？
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]随我来吧。见到他你就知道了。
[name="主教"]毕竟......你也有一位朋友在这。
[dialog]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="“你想见她，不是吗。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Subtitle(text="主教的语气轻描淡写，斯卡蒂却不能安之若素。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="这个猎人暗暗握紧箱子的把手。得益于材料学的进步以及罗德岛切实投入的大量经费，她才没把这个特制“萨克斯箱”的把手捏碎。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_184",focus=2)]
[name="主教"]请走这里。
[dialog]
[character]
[character(name="avg_npc_184",name2="avg_474_gladiia_1#1",focus=1)]
[name="主教"]至于你。
[character(name="avg_npc_184",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]......
[character(name="avg_npc_184",name2="avg_474_gladiia_1#1",focus=1)]
[name="主教"]你也来。赏赐你的时候也到了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_474_gladiia_1#1",focus=1)]
[Subtitle(text="斯卡蒂看了眼歌蕾蒂娅，没多说什么。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[character(name="avg_1012_skadiSP_1#1",name2="avg_npc_1

... (全文40706字符)
```

### level_act18d3_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ibcoastd")]
[character(name="avg_npc_183#3")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="大审判官"]凯尔希医生。请做出解释。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]......我就知道事情没那么容易。
[character(name="char_003_kalts_1")]
[name="凯尔希"]比起伊比利亚人应该知道的那些，审判庭私藏的秘密已经太多了。
[character(name="avg_npc_183#3")]
[name="大审判官"]女士。在伊比利亚严禁传谣。
[character(name="char_003_kalts_1")]
[name="凯尔希"]审判官阁下，因为你知道那些秘密我才这么说的。
[name="凯尔希"]深海教会已经渗透进了伊比利亚，在伊比利亚隐秘地扎根。
[name="凯尔希"]利用你们和海洋曾经的联系，伊比利亚废弃的城市成了深海教会向陆地伸出触手的据点。
[name="凯尔希"]他们阐释你们的经书，歪曲你们的观点，他们藏得很深，你们顾此失彼。
[name="凯尔希"]......求救吧。再纠结国土和信仰间的浅薄纷争，我们就会错过最后的机会。
[Dialog]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_1012_skadiSP_1#1")]
[Subtitle(text="猎人们和审判官与凯尔希奇怪地对峙着。斯卡蒂这时觉得，也许凯尔希真站在他们这里。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_003_kalts_1")]
[name="凯尔希"]大审判官阁下，伊比利亚人是不同的。
[name="凯尔希"]你们每天看见的天际线都与大地上其他人不同。
[name="凯尔希"]你们怎么称呼自己日夜生活的地方？——海边。
[name="凯尔希"]其他人生活在陆上，而伊比利亚人生活在海边。
[name="凯尔希"]绝大多数人，不管他们是活在荒野还是活在城市，他们抬头看见天空，平视却只能看见一望无际的大地，山脉连绵。
[name="凯尔希"]云层上的一切与他们都无关。
[name="凯尔希"]所以，他们所拥有的一切都只有“这片大地”。
[name="凯尔希"]他们把自己生活的地方叫作大地，是因为他们认定这世界除了陆地别无他物。
[name="凯尔希"]封闭的城邦，闭塞的村落，令人轻易丧命的荒野，他们除了自己能看见的，什么都不信。
[name="凯尔希"]再看看她们。她们，深海的猎人。阿戈尔人。
[name="凯尔希"]比这片陆地更广大的海洋。
[name="凯尔希"]伊比利亚与其他国家不同。
[name="凯尔希"]陆地上的他们醉心于自己的航道与权力，忽视了无限的可能，忽视了他们本可以探索，却盲目忽视的边界。
[name="凯尔希"]你们的世界完整得多。你们既了解陆地，又知晓海洋，伊比利亚对自己身处的位置有着最基础的认知。
[name="凯尔希"]这让你们在过去就已经领先了一大步立足于......
[character(name="avg_npc_183#3")]
[name="大审判官"]不必再说。
[name="大审判官"]这些都过去了。城市的光辉散去，伊比利亚已经徒留废墟。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="ac18_14", xScale=1.3,yScale=1.3, fadetime=0)]
[ImageTween(xFrom=30, xTo=-30, duration=25, block=false)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="凯尔希"]您让我有些惊讶，阁下。我以为您会避而不谈。
[name="大审判官"]你在这，你不瞎。自己抬头看。
[name="大审判官"]盐风城这种城市，遍布伊比利亚海岸。
曾经辉煌的伊比利亚，现在有多少这样的遗迹？
凯尔希知道，大审判官自然也知道。只是大审判官面如坚铁，他的眉眼是一丝感情都不会流露出来的。
加上现在，他戴着面具。
如果能够哭泣，伊比利亚人一定会号啕，如果能开心地笑，伊比利亚人一定会放声大笑。
但是，一个情感充沛的伊比利亚人，已经变成了面前这个样子。
没有表情，没有感情。伊比利亚的黄金时代自他们陷入寂静的生命里消失了。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[character(name="char_003_kalts_1",name2="avg_npc_183#3")]
[Image]
[delay(time=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_183#3")]
[name="大审判官"]太多了。
[name="大审判官"]我们支援不了它们。许多城市自身难保。
[name="大审判官"]大静谧后，伊比利亚已然不再。
[character(name="char_003_kalts_1")]
[name="凯尔希"]那么你更需要其他人的支援。
[character(name="avg_npc_183#3")]
[name="大审判官"]没人知道伊比利亚发生何事。也不可以有人知道。
[character(name="char_003_kalts_1")]
[name="凯尔希"]因为伊比利亚曾经濒临毁灭？
[character(name="avg_npc_183#3")]
[name="大审判官"]即使现在，伊比利亚也不能毁灭。
[character(name="char_003_kalts_1")]
[name="凯尔希"]你们还在。伊比利亚的人民依然还在。
[character(name="char_003_kalts_1")]
[name="凯尔希"]我相信，伊比利亚的人民即使一座城市也没剩下......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="凯尔希望向三位深海猎人，其中，斯卡蒂正走向那些因为动静而从建筑中走出的居民，似乎要和他们说些什么。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="凯尔希"]他们也不会轻易死去。
[name="凯尔希"]阁下，听我一言。
[name="凯尔希"]傲慢与偏见已经毁掉了阿戈尔人，这片土地不能重蹈海洋深处居民的覆辙。
[name="凯尔希"]如果伊比利亚也在这一场灾难的余波中倒下，这里将再没有人知道海洋的真实面貌与它威胁的可怕。
[name="凯尔希"]就像冻原上百年一次的狩猎一样，现在的我们也在卫护人类的疆土，而不是一国的荣辱，无论我们面对的是否是海中怪物。
[name="凯尔希"]并且，如果伊比利亚只是像现在这样苟延残喘......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="char_003_kalts_1",name2="avg_npc_183#3")]
[Subtitle(text="凯尔希看着大审判官的眼睛。大审判官的表情没有任何变化，既不像是拒绝，也不像是允许。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但凯尔希还是会把话说完。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_003_kalts_1")]
[name="凯尔希"]那么伊比利亚终归会毁灭。
[name="凯尔希"]现在的你们依然可以重建家园，重建伊比利亚。
[character(name="avg_npc_183#3")]
[name="大审判官"]我不相信。
[character(name="char_003_kalts_1")]
[name="凯尔希"]我的目标，并不是要令你相信些什么，阁下。我只是想让你知道。
[name="凯尔希"]这个回答，这个决定，不必由您给，也不用现在给。
[character(name="avg_npc_183#3")]
[name="大审判官"]——
[name="大审判官"]盐风城之事也得解决。
[dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character(name="avg_npc_183#3")]
[Subtitle(text="大审判官环顾几位猎人。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[name="大审判官"]这些人里，至少有一个得留下。
[character(name="char_143_ghost#2")]
[name="幽灵鲨"]我。
[character(name="avg_1012_skadiSP_1#1")]
[name="斯卡蒂"]不。
[character(name="avg_474_gladiia_1#1")]
[name="歌蕾蒂娅"]你们回去。
[name="歌蕾蒂娅"]凯尔希，就像我们说好的那样。我不在，就由你带领他们。
[character(name="avg_1012_skadiSP_1#1",name2="avg_474_gladiia_1#1",focus=1)]
[name="斯卡蒂"]你......？
[name="斯卡蒂"]这是怎么回事？
[dialog]
[character]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[delay(time=1)]
[character(name="char_003_kalts_1")]
[name="凯尔希"]......
[name="凯尔希"]大审判官，我是否有这个资格？
[name="凯尔希"]我可以代受审问。我可以梳理来龙去脉。你能得到你需要的信息。
[name="凯尔希"]我能忍受伊比利亚的牢狱。
[character(name="avg_npc_183#3")]
[name="大审判官"]——
[name="大审判官"]如果你这么坚持。
[character(name="avg_1012_skadiSP_1#1",name2="avg_474_gladiia_1#1",focus=2)]
[name="歌蕾蒂娅"]凯尔希女士？
[character(name="avg_1012_skadiSP_1#1",name2="avg_474_gladiia_1#1",focus=1)]
[name="斯卡蒂"]......医生？
[character(name="avg_npc_183#3")]
[name="大审判官"]所以你希望我把这几个人驱逐出境？
[character(name="char_003_kalts

... (全文20374字符)
```

### training_act18d3_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d3教学关_a

[PopupDialog(dialogHead="$avatar_doberm")] 今天我们要学习的是如何对应非常规伤害。
[PopupDialog(dialogHead="$avatar_doberm")] 我们邀请到了干员黑角来为我们演示模拟，有劳你，黑角。
[PopupDialog(dialogHead="$avatar_noirc")] 没事，教官。
[PopupDialog(dialogHead="$avatar_noirc")] 看，这些敌人看起来很弱，正常情况下，用我的防护挡住这些敌人可以说是轻而易举的。
[Tutorial(focusX=3300, focusY=-130, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
但是，不能轻敌！这类......不知从哪找来的奇怪生物，会造成额外的特殊<@tu.kw>神经损伤</>！
[PopupDialog(dialogHead="$avatar_noirc")] 没错，虽然<@tu.kw>神经损伤</>不会直接伤害到我，但是会无视装备的防护性能不断<@tu.kw>累积</>，当超过一定阈值时，就会造成严重的负面效果。




```

### training_act18d3_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d5教学关_b

[Tutorial(focusX=320, focusY=-80, focusWidth=150, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
当累积的神经损伤<@tu.kw>超过承受能力</>时，黑角受到了大量无视防御装备的<@tu.kw>真实伤害</>，并长时间<@tu.kw>晕眩</>了！


```

### training_act18d3_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d5教学关_c

[PopupDialog(dialogHead="$avatar_doberm")] 普通的治疗手段不能治愈干员累积的<@tu.kw>神经损伤</>，需要通过特殊的方式进行治疗。
[Tutorial(focusX=190, focusY=210, focusWidth=130, focusHeight=130,  \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
看到那些钟楼一样的建筑了吗，那些是伊比利亚的<@tu.kw>应急救治设施</>，可以释放出持续<@tu.kw>治疗神经损伤</>的喷雾。


```

### training_act18d3_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动18d5教学关_d

[Tutorial(focusX=190, focusY=110, focusWidth=100, focusHeight=100,  \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
应急救治设施需要我们在它的相邻位置<@tu.kw>部署干员来激活</>。
[Tutorial(focusX=190, focusY=110, focusWidth=300, focusHeight=300,  \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
激活后的救治设施可以在大范围内释放出医疗喷雾，<@tu.kw>持续治疗</>我方受到的神经损伤。


```

### training_act18d3_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 活动16d0教学关_d

[PopupDialog(dialogHead="$avatar_doberm")] 又有一波敌人来了，在另个方向！注意，激活救治设施来应对这些生物的神经损伤，剩下的就交给你们来处理了！
[PopupDialog(dialogHead="system_100_mys")] 是！
[PopupDialog(dialogHead="$avatar_doberm")] 啊，干员黑角......等等，模拟也会真的让人昏厥的吗？


```


## 统计

- 总字符数：347340
- 对话行数：2814


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
