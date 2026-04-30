# 明日方舟 · 活动剧情 · act11mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act11mini」完整剧情脚本（6个文件，1740行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act11mini
- 脚本文件数：6

### level_act11mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g8_nobleroom",screenadapt="coverall")]
[Delay(time=1)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]露丝，你都准备好了吗？
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]维多利亚和谢拉格不一样，这次我们要和对方合作，我们处于弱势，对方一定会趁此机会血口大开。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]我只能给你建议，无法预测对方具体的行动。这次要你自己来判断。
[character(name="avg_npc_262_1#7$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]行了行了，知道了！耳朵都要被你念出茧来了！
[character(name="avg_npc_262_1#7$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]要是这么不相信我，你干嘛不自己去！
[character(name="avg_npc_262_1#7$1",name2="avg_npc_253_1#5$1",focus=2)]
[name="菈塔托丝"]用你那个没开过封的脑瓜自己想。
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#5$1",focus=1)]
[name="休露丝"]你......！
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]好了，我没工夫和你吵架。记住，这次可不是让你免费旅游，你代表的是我们布朗陶家。
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]尤卡坦，看好你老婆，别让她在外头犯蠢给布朗陶家丢人。
[character(name="avg_npc_263_1#8$1")]
[name="尤卡坦"]哈哈......
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]不许点头！尤卡坦，你到底是哪一边的？！
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#2$1",focus=2)]
[name="菈塔托丝"]别岔开话题。
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#7$1",focus=2)]
[name="菈塔托丝"]总之这一次，凡事都多个心眼，多看，多听，少说，别再和之前似的，口无遮拦。
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]你也该出去开开眼界了，去看看谢拉格之外的大地，看看维多利亚到底是个什么样的地方。
[character(name="avg_npc_262_1#9$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]哼......
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]......
[character(name="avg_npc_262_1#2$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]哎，我说......菈塔托丝。
[character(name="avg_npc_262_1#2$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]怎么？
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]你是不是其实很想自己去？
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#10$1",focus=2)]
[name="菈塔托丝"]......
[character(name="avg_npc_262_1#1$1",name2="avg_npc_253_1#11$1",focus=2)]
[name="菈塔托丝"]露丝，你过来。
[character(name="avg_npc_262_1#4$1",name2="avg_npc_253_1#11$1",focus=1)]
[multiline(name="休露丝")]嗯？
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#11$1",focus=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[multiline(name="休露丝")]......干什么，臭女人！松手，我没发烧！
[character(name="avg_npc_262_1#8$1",name2="avg_npc_253_1#1$1",focus=2)]
[name="菈塔托丝"]那你在说什么梦话？
[character(name="avg_npc_262_1#9$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]我、我就随便问问。
[character(name="avg_npc_262_1#6$1",name2="avg_npc_253_1#1$1",focus=1)]
[name="休露丝"]如果当年有这个机会的话......菈塔托丝，你想去维多利亚吗？
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character]
[delay(time=1)]
[Background(image="bg_manorindoor",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[delay(time=1)]
[Character(name="avg_npc_176")]
[name="维多利亚富商"]哎，两位原来在这里！
[Character(name="avg_npc_176")]
[name="维多利亚富商"]刚才客人太多，实在脱不开身，有不周之处还请两位多见谅。
[dialog]
[character]
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]哈里森先生言重了。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]感谢您的招待，我们今天过得非常愉快。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]您太客气了！
[Character(name="avg_npc_176")]
[name="维多利亚富商"]两位远道而来，我理应尽地主之谊。您面前的这些酒水和餐品还请随意享用，若有别的需要，找附近的侍者就可以了。
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]让您费心了。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]对了，需要我为您示范一下如何使用这些餐具吗？
[character(name="avg_npc_262_1#9$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]......不用了。
[character(name="avg_npc_262_1#6$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]哈里森先生，比起这些，我想我们更应该谈谈关于布朗陶家和贵公司的合作事宜。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]唔，休露丝夫人，您很直接......
[Character(name="avg_npc_176")]
[name="维多利亚富商"]不过，关于合作，我认为我们之前已经达成了一定的共识，不是吗？
[character(name="avg_npc_262_1#10$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]确实如此。
[character(name="avg_npc_262_1#5$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]但在一些细节上，我认为我们还需要详细明确一下。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]当然，您大可以放心。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]我的助理应该已经准备好了正式的合同，您有空时可以过目......
[character(name="avg_npc_262_1#1$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]我已经看过那份合同了。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]哦？
[character(name="avg_npc_262_1#6$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]恕我直言，其中的一些条目布朗陶家是不可能接受的。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]嗯......
[Character(name="avg_npc_176")]
[name="维多利亚富商"]那么，您的意思是？
[character(name="avg_npc_262_1#6$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]我们需要重新谈一谈关于人力提供和利润分配这些方面的具体数字。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]唔。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]您说的我会考虑的。
[character(name="avg_npc_262_1#5$1",name2="avg_npc_263_1#1$1",focus=1)]
[name="休露丝"]那么——
[Character(name="avg_npc_176")]
[name="维多利亚富商"]少安毋躁，休露丝夫人。
[Character(name="avg_npc_176")]
[name="维多利亚富商"]关于这次的合作，在订单抽成上，我自认已经给了您很大的优惠了。
[character(name="avg_npc_2

... (全文36872字符)
```

### level_act11mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(key="Sound_Beta_2/Music/act15side/m_sys_bitw_loop", volume=0.4)]
[Background(image="25_g02_yanalley_n",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_294_1#2$1",fadetime=1,block=true)]
[Delay(time=1)]
[name="老船夫"]大清早的，还有点凉。
[Character(name="avg_npc_294_1#1$1")]
[name="老船夫"]尚蜀这天气，现在嫌凉了，到晌午又热得很，难伺候啊。
[character]
[name="？？？"]寒暑需有个度，想来尚蜀百姓早已适应。
[Character(name="avg_npc_294_1#9$1")]
[name="老船夫"]说得是。不过瞧着最近雨水多了，怕是天气要变。
[name="老船夫"]希望不是什么大寒大暑，给人点时间适应适应。
[Dialog]
[Character]
[character(name="avg_npc_301_1#1$1",fadetime=0.5,block=true)]
[Delay(time=1)]
[name="太傅"]季候到了，总有些变节。
[Character(name="avg_npc_294_1#9$1",name2="avg_npc_301_1#4$1",focus=2)]
[name="太傅"]船家，可否载我一程。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#4$1",focus=1)]
[name="老船夫"]您说，去哪儿。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#1$1",focus=2)]
[name="太傅"]渡江。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#1$1",focus=1)]
[name="老船夫"]没问题。您看您这江，是怎么渡？
[name="老船夫"]走哪条道，赶时间不赶？
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#4$1",focus=2)]
[name="太傅"]有什么不同？
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#4$1",focus=1)]
[name="老船夫"]要是行得急，时间紧，我便行快船，费不了多少工夫就能到对岸。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#1$1",focus=2)]
[name="太傅"]若我不急又如何？
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#1$1",focus=1)]
[name="老船夫"]那就得在渡口先整治些酒菜了。
[name="老船夫"]酒在船上温着，船就从上游这渡口，贴着边漂下去。能看到城市，也能瞧见正在种的田，风景好着呢。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#5$1",focus=2)]
[name="太傅"]听着不差。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#5$1",focus=1)]
[name="老船夫"]那就这么定，我先把酒温上。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#4$1",focus=2)]
[name="太傅"]......你倒很会做生意。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#4$1",focus=1)]
[name="老船夫"]做这行的，总归得有些眼力见儿。
[name="老船夫"]您这样的老丈，没几个不爱多看看这尚蜀城的。就算不看城，也爱看人。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#5$1",focus=2)]
[name="太傅"]说的不错。
[name="太傅"]人，确实当看，若不看人，就是白走一遭。
[name="太傅"]梁洵应当与你说过，他今晚便该随我回京。出尚蜀这趟路，便由你指引。
[Character(name="avg_npc_294_1#1$1",name2="avg_npc_301_1#5$1",focus=1)]
[name="老船夫"]......确实说过。
[name="老船夫"]您别怪罪，梁大人这回走得急，我们这些人难免多担忧些。
[name="老船夫"]我们这知府大人......说是了不得的父母官，可到底还年轻着呢，有时候看着就像家里的子侄，让人担心。
[Character(name="avg_npc_294_1#1$1",name2="avg_npc_301_1#1$1",focus=2)]
[name="太傅"]梁洵他有这般才能，也有志气。顶得住，便是功成名就。
[Character(name="avg_npc_294_1#1$1",name2="avg_npc_301_1#1$1",focus=1)]
[name="老船夫"]要是顶不住呢？
[Character(name="avg_npc_294_1#7$1",name2="avg_npc_301_1#1$1",focus=1)]
[name="老船夫"]——唉，算了，不该问。您要看看这尚蜀，只管跟我来便是。
[Character(name="avg_npc_294_1#8$1",name2="avg_npc_301_1#1$1",focus=1)]
[name="老船夫"]就是可惜，鲤小子前头还在找人，我看今天他要见梁大人，是难了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
[Delay(time=0.6)]
[Background(image="25_g09_teahouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_298_1#1$1",fadetime=1,block=true)]
[Delay(time=1)]
[name="宁小姐"]天还有些凉，好在茶是热的，倒也不冷。
[character(name="avg_npc_298_1#10$1")]
[name="宁小姐"]梁大人公务繁忙，今天怎么来得这么早？
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[character(name="avg_npc_295_1#8$1",fadetime=1,block=true)]
[Delay(time=2)]
[name="梁洵"]说好陪你看戏。
[Dialog]
[character(name="avg_npc_298_1#10$1",name2="avg_npc_295_1#8$1")]
[characteraction(name="right", type="move", xpos=-50,fadetime=1, block=true)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[Delay(time=1)]
[characteraction(name="right", type="move", xpos=50,fadetime=0.8, block=true)]
[Delay(time=1)]
[character(name="avg_npc_298_1#10$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]多披些衣物，小心风寒。
[character(name="avg_npc_298_1#4$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]什么时候说好了？之前只说，得空了就一起来。
[character(name="avg_npc_298_1#4$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]今日就得空。
[character(name="avg_npc_298_1#8$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]骗人。太傅交代得那么紧急，工作上的交接就有大堆麻烦......梁大人莫非是昨夜没睡？
[character(name="avg_npc_298_1#8$1",name2="avg_npc_295_1#10$1",focus=2)]
[name="梁洵"]咳，有稍微合眼。
[character(name="avg_npc_298_1#8$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]宁小姐今天也醒得早。
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]我猜不听人劝的梁大人今天一早会来，一直在等着。
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#4$1",focus=2)]
[name="梁洵"]这，我......
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#4$1",focus=1)]
[name="宁小姐"]茶杯空了，杯子递给我。
[Dialog]
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#4$1",focus=1)]
[PlaySound(key="$pourwater")]
[Delay(time=3)]
[PlaySound(key="$d_avg_chess")]
[Delay(time=1)]
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]......多谢。
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]一杯茶而已，你我之间还用说谢？
[character(name="avg_npc_298_1#10$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]能在这山上坐坐，喝茶醒醒神，也不错。
[name="宁小姐"]这儿的茶点味道也挺好......油酥，芝麻糕，还有——
[character(name="avg_npc_298_1#10$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]糖果子。
[name="梁洵"]上回宁小姐夸奖过。
[character(name="avg_npc_298_1#4$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]啊，您就记着了？
[character(name="avg_npc_298_1#4$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]嗯。宁小姐喜欢，就多留意了些。
[character(name="avg_npc_298_1#8$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]尚蜀什么都好，就是口味上有点重，好在糕点大多还是香软甜口的，合我的口味。
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#8$1",focus=1)]
[name="宁小姐"]唉，梁大人府里煮的锅子最初也辣得很，之后倒好了不少。
[name="宁小姐"]最初动不了一筷子就要找水，太狼狈了。
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#8$1",focus=2)]
[name="梁洵"]府里解辣的汤时刻备着。
[name="梁洵"]宁小姐的家乡......
[character(name="avg_npc_298_1#1$1",name2="avg_npc_295_1#8$

... (全文23510字符)
```

### level_act11mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkalley_intro",key="$darkalley_loop", volume=0.4)]
[Background(image="bg_lungmen_m",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[character(name="char_empty",name2="avg_npc_541_1#1$1",fadetime=1)]
[Delay(time=1)]
[name="卡彭"]九点三十五，已经超过预定时间五分钟了。
[name="卡彭"]安全起见，我们该换个地方了。
[Dialog]
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",fadetime=1)]
[Delay(time=1)]
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]我一秒钟都不想在这儿多待，但我更怕和我们接头的人找不到我们。
[name="甘比诺"]说好的他一入城就来找我们接头，现在一个人都没从关口里出来，肯定是在里面什么地方卡住了。接着等吧。
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]出入城关口这种地方这么显眼，你真打算继续在这儿等下去？
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]要不然呢？我们现在是在给那个疯女人做事！
[name="甘比诺"]她抓住我们之后说的第一句话是什么，你记得吧？
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#2$1",focus=2)]
[name="卡彭"]“我改主意了，我希望你们两个活人比两具死尸的用处大一点。”
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]不是那一句，下一句！
[character(name="avg_npc_542_1#5$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]“别把我的事情搞砸。搞砸一次，你们就死定了。”
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]所以说，与其和接头人走散拿不到信，我宁愿引人注目一点。
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]你——算了。
[name="卡彭"]人群出来了。
[character(name="avg_npc_542_1#10$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]要和我们接头的人长什么样子来着......
[character(name="avg_npc_542_1#10$1",name2="avg_npc_541_1#2$1",focus=2)]
[name="卡彭"]别想了，你想不出来的。
[character(name="avg_npc_542_1#10$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]你什么意思？
[character(name="avg_npc_542_1#10$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]唉。
[name="卡彭"]那女人根本就没说过接头人长什么样子，穿什么衣服。是他来找我们，不是我们去找他。
[Dialog]
[Character]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]   
[character(name="avg_npc_032",fadetime=0.5)]
[characteraction(name="middle", type="move", xpos=200, fadetime=2, block=true)]
[Delay(time=1)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[character(name="char_empty",name2="avg_npc_002",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=-100, fadetime=0, block=true)]
[characteraction(name="right", type="move", xpos=300, fadetime=2, block=true)]
[Delay(time=1)]
[character(name="avg_npc_001",name2="char_empty",fadetime=0.5)]
[characteraction(name="left", type="move", xpos=400, fadetime=1.5, block=true)]
[Delay(time=1)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[character(name="avg_npc_242",name2="avg_npc_243",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=-200, fadetime=0, block=true)]
[Delay(time=1)]
[characteraction(name="left", type="move", xpos=300, fadetime=3, block=false)]
[characteraction(name="right", type="move", xpos=300, fadetime=3, block=false)]
[Delay(time=2)]
[Character(fadetime=0.5)]
[Delay(time=2)]
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]甘比诺，接头流程你总记得吧？
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#2$1",focus=2)]
[name="卡彭"]甘比诺？
[character(name="avg_npc_542_1#7$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]......接头人问我们“蛋黄酱铁板通心粉要不要”，我们说“要超值双人份”，然后他把信交给我们。
[character(name="avg_npc_542_1#7$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]多亏你记得住。
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]这么个让人反胃的接头暗号，我不想记也记住了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]九点五十，现在已经连最后一批入城的人都走干净了。
[name="卡彭"]肯定出了什么岔子，我们得动起来了。
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]那要是一会儿人出来了，我们却不在这儿，怎么办？
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#2$1",focus=2)]
[name="卡彭"]哪有这么碰巧的事？现在已经不是优哉游哉在这傻站着的时候了！
[character(name="avg_npc_542_1#10$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]万一是那个人被关口扣住了呢？
[name="甘比诺"]就算不是，我们在这里等他也不能算错，是接头人自己没找到我们，那个疯女人不能拿我们怎么样......
[character(name="avg_npc_542_1#10$1",name2="avg_npc_541_1#2$1",focus=2)]
[name="卡彭"]有什么区别吗？！
[name="卡彭"]那女人疯得要命，她只要结果，她才不管是谁出了问题！再不从这儿把你的屁股挪开，你就已经搞砸了！
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]......好，就算你说得对，那我们该去哪找人？
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]你动动脑子行不行？
[name="卡彭"]除了叙拉古的人，没人会给那个疯女人写信。企鹅物流姑且不论，现在的龙门还有谁能和叙拉古扯上关系？
[character(name="avg_npc_542_1#6$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]你是说我们从叙拉古带来的那帮叛徒？
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]他们不仅背叛了我们，还把人截走了？！
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#2$1",focus=2)]
[name="卡彭"]呵，你终于能听懂人说话了。
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#2$1",focus=1)]
[name="甘比诺"]......
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]我也不敢说人一定是他们截的，但这事和他们一定脱不了干系，至少他们应该知道些什么。
[name="卡彭"]走吧。
[character(name="avg_npc_542_1#5$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]那群该死的背叛者，我一定要——
[character(name="avg_npc_542_1#5$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]打住！
[name="卡彭"]自打踏上龙门的第一天起我就一直在告诉你，龙门有龙门的规矩。
[name="卡彭"]别忘了我们是怎么成了鼠王的手下败将，他又是怎么放我们一条生路的。
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#1$1",focus=1)]
[name="甘比诺"]不用你说！
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#1$1",focus=2)]
[name="卡彭"]但愿如此。
[character(name="avg_npc_542_1#4$1",name2="avg_npc_541_1#5$1",focus=2)]
[name="卡彭"]所以，我们去那群叛徒的窝点，不是去打架的，更不是去给他们教训的，我们只是去打听消息，明白吗？
[character(name="avg_npc_542_1#1$1",name2="avg_npc_541_1#5$1",focus=1)]
[name="甘比诺"]....

... (全文44016字符)
```

### level_act11mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_county_1",screenadapt="coverall")]
[playMusic(intro="$mist_intro",key="$mist_loop", volume=0.4)]
你问我，我加入无胄盟的理由？
奇怪，这是老头你的组织，我加入还需要什么理由啊。
所以这算是面试吗？我听说城里的企业都搞这一套，我们以后再招新人也要这么来吗？那我是不是该喊你老板？
哎，你别嫌烦啊。
按我看，杀手组织和企业也没什么不一样的，反正都是上班，然后加班，还有安排其他人加班。
真要说个跟着干的理由，那肯定还是赚的钱够多吧，比我自己打猎杀羽兽多赚不是一点半点。
反正一样都是瞄准——射击，那当然是赚得多的活更让人有干劲啊。
是吧老板，毕竟大家都是想要过上好日子的嘛。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_axeimp")]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_avg_arrowshot")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_214_1#1$1",fadetime=1)]
[Delay(time=1)]
[name="血骑士"]无胄盟的杀手，你们是怎么查到这里的。
[Character(name="avg_npc_208_1#1")]
[name="莫妮克"]事到如今还问这种问题？
[Character(name="avg_npc_209_1#1")]
[name="罗伊"]血骑士这样的名人，自然一举一动都有人关注了。
[name="罗伊"]虽然阁下已经足够小心，但......这么说吧，能查到这里的人可不止是我们。
[Character(name="avg_npc_214_1#5$1")]
[name="血骑士"]......
[Character(name="avg_npc_209_1#6")]
[name="罗伊"]要找您麻烦的人可不少，我们能赶在第一个找到您，可是费了不少功夫啊。
[name="罗伊"]时间紧迫，还请您相信我们的诚意。
[Character(name="avg_npc_214_1#6$1")]
[name="血骑士"]......相信你们？
[name="血骑士"]笑话，无胄盟也配与我谈信任吗。
[Character(name="avg_npc_209_1#6")]
[name="罗伊"]必要的时候，我们可以不是无胄盟。
[Character(name="avg_npc_208_1#2")]
[name="莫妮克"]......
[Character(name="avg_npc_214_1#5$1")]
[name="血骑士"]......杀手，这就是你们放任自己的手下被我杀死的理由？
[name="血骑士"]你们是想——
[Character(name="avg_npc_209_1#6")]
[name="罗伊"]嘘，看破不说破。
[name="罗伊"]血骑士阁下一直是个聪明人，应该不会不懂这个道理。
[Character(name="avg_npc_214_1#3$1")]
[name="血骑士"]......
[Character(name="avg_npc_209_1#1")]
[name="罗伊"]帮我们一个小小的忙，也给自己一个脱身的机会，这应该是一笔很划算的买卖。
[name="罗伊"]这样对我们双方都好......你说是吧？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
无胄盟的青金大位，怎么样，听起来够厉害的吧？
实际上赚的也确实够多。某种意义上来说，和竞技骑士差不了多少，都是拿命拼来的钱。
想要来钱快，那多少得付出点代价，承担点风险不是？
不过呢，干这行十多年，差不多也做到头了。
急流勇退啊，最简单的道理，何必要逆着这个时代的洪流这么挣扎？有更安稳的生财法子，何苦再这么拼命呢？
看准了时机，该上岸还是得上岸。
给人打工，哪有自己做老板来得舒服？
[Dialog]
[Character(fadetime=0)]
[Background(image="bg_23_G07",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[name="莫妮克"]手术定在两个小时后，记得准点到。
[name="莫妮克"]明天之后你就只有约尔·泰勒这一个身份，公司那边再过两天会让我们露个脸，别出岔子。
[name="莫妮克"]还有......联合会的人看起来还没完全相信我们和血骑士同归于尽。
[name="莫妮克"]啧，那边调查的人还没完全撤走，不过无胄盟倒是已经定好新的青金人选了。
[name="莫妮克"]总之在事情完全解决之前，少在外头露面，省得节外生枝......
[name="莫妮克"]......喂，你听见没有。
[Character(name="avg_npc_543_1#5$1")]
[name="罗伊"]嗯？啊我在听，我在听。
[Character(name="avg_npc_543_1#1$1")]
[name="罗伊"]老板，麻烦给我来个最贵的套餐。
[name="罗伊"]直接吃不用包上，多加辣！
[Character(name="avg_npc_543_1#3$1")]
[name="罗伊"]哎，莫妮克阁下，你刚刚说什么？
[Character]
[name="莫妮克"]......去死吧。
[Character(name="avg_npc_543_1#1$1")]
[name="罗伊"]那可不行，我要是死了，可怜的泰勒太太可就要直接成为寡......
[Dialog]
[PlaySound(key="$transmission")]
[PlaySound(key="Sound_Beta_2/Player/p_imp/p_imp_funnel_end_h",delay=1)]
[Delay(time=2)]
[name="罗伊"]......嗯，挂得真快。
[Character(name="avg_npc_543_1#5$1")]
[name="罗伊"]（看来一切都还算顺利，董事会就算现在有怀疑，也早就迟了。血骑士......他如果够聪明，就不会这个时候跳出来搅局。）
[name="罗伊"]（况且人人自顾不暇，几个“道具”的损失而已，谁都不会太在意。）
[name="罗伊"]（玄铁那应该轮不着我去担心，剩下的就是换张脸，换个身份......）
[name="罗伊"]（......）
[name="罗伊"]（马上就要和这张脸说拜拜了啊。）
[Character(name="avg_npc_543_1#3$1")]
[name="罗伊"]（不知道新面容顺不顺眼，不过不管怎么说，应该都是不可能再像现在这么帅了。）
[Character(name="avg_npc_543_1#1$1")]
[name="罗伊"]（哎。可惜。）
[Character]
曾经的青金大位站在街道上，将自己隐藏在霓虹灯的阴影之下。
他抬手拍了拍自己的脸颊，视线漫无目的地扫过城市光鲜亮丽的街道。
商业楼外侧的大屏幕上正播放着近期最受关注的新闻要点。
整条街道上大大小小的屏幕似乎都播报着相似的内容，噪音与繁杂的屏幕光线让人略微晕眩。
[name="电视"]血骑士在乡村的隐居处遭遇不明人士袭击，现场有激烈打斗痕迹，现已确认现场残留的血迹归属为血骑士本人。
[name="电视"]现场同时发现了大量袭击者遗体。
[name="电视"]专家指出，在这样激烈的战斗之中，血骑士幸存的可能性非常微小，而残存的大量血迹也佐证了这一推断。
[name="电视"]目前最合理的解释是我们的前任冠军在败给归来的耀骑士后，耗尽了最后的力量，与袭击者同归于尽。
[name="电视"]更多有关资讯，敬请关注我们的后续节目！直击血骑士受袭事件真相！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_220")]
[name="感染者骑士"]胡说！全都是在放屁！
[Dialog]
[characteraction(name="middle", type="move", xpos=-50, fadetime=0.3, block=false)]
[Blocker(a=0, fadetime=0.3, block=true)]
[name="感染者骑士"]血骑士怎么可能被区区杀手杀死，这不可能！他一定是受了伤，所以才不愿意出现在那群只会抢新闻吸血的媒体面前......！
[Dialog]
[characteraction(name="middle", type="move", xpos=50, fadetime=0.3, block=false)]
[Blocker(a=0, fadetime=0.3, block=true)]
[name="感染者骑士"]卑鄙无耻的暗杀者！一群阴沟里的臭虫！血骑士绝不会就这么倒下！
[Dialog]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[Character]
[StopMusic(fadetime=1)]
[Character(name="avg_npc_223")]
[characteraction(name="middle", type="move", xpos=100, fadetime=0.5, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Characteraction(name="middle", type="jump", xpos=50, power=30, times=1, fadetime=0.3,block=true)]
[Blocker(a=0, fadetime=0.4, block=true)]
[name="企业员工"]等一下，你说就说，能不能别乱挥手......哎我的脑袋！
[Dialog]
[PlaySound(key="$punch_n1",volume=0.5)]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=15, randomness=90, fadeout=true, block=false)]
[characteraction(name="middle", type="move", ypos=-30, fadetime=0.3, block=true)]
[Delay(time=1)]
[Character]
[playMusic(intro="$wa

... (全文20646字符)
```

### level_act11mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_020",name2="avg_npc_020",fadetime=0.7)]
[delay(time=0.7)]
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]已经十点半了，喝咖啡？你现在还有闲心喝咖啡？
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]把你的屁股从咖啡机旁的椅子上挪到你的办公桌前面来。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]咳......！
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]上回提的意见你改得怎么样了？现在到下午三点的会可没多长时间了。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]方案已经改好了，在这里。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]之前会上给的意见很清楚，基本上当场就给了几个解决思路，改起来很顺利。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]讲稿也准备好了。
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]时间不多了，从今天算起再到周末，三天，方案要定下来，还要给后面部门留实施的时间。
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]多仔细点，市长的意思很清楚，这次和之前不一样。
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]火山不等人，我这句话可不是在开玩笑。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]嗯嗯，明白。
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]让我看看你写的。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]给，是这一份，讲稿是附在下面的。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]......那个......
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]什么？
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]......其实我做这份方案的时候，一直觉得有个问题我们内部无法解决，需要在会上提出来让老大和市长谈才行。
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]什么问题？
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]我不太确定，我先讲一下。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]你看，这次搬迁，我们给出的方案是分区块迁移模式，先去的是各地块的关键技术人员和重要岗位的管理人员。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]这群人的人数在我们的能力范围内，已经全部迁移完成，等他们再完成了核心地区的接管后，我们就可以开始准备迁入剩下的人口。
[character(name="avg_npc_020",name2="avg_npc_020",focus=1)]
[name="工作人员B"]不变的需求是以区块为单位，依次迁入，但，目前给出的几个方案，即便联络外地的物流公司，运力也肯定是不够的。
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]嗯。所以呢？
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]光有想法约等于没有，发现问题了你的对策是什么？
[character(name="avg_npc_020",name2="avg_npc_020",focus=2)]
[name="工作人员A"]总不是想等着会上提出来让行政和运输局那边给你解决吧。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[musicvolume(volume=0.2, fadetime=1)]
[Delay(time=2)]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_544_1#3$1")]
[playsound(key="$d_avg_paper1",volume=0.8)]
[name="赫尔曼"] ......
[Character(name="avg_npc_544_1#1$1")]
[name="赫尔曼"]......单单几家物流公司的运力肯定不够......
[Character(name="avg_npc_544_1#1$1")]
[name="赫尔曼"]现代物流公司专业的运输管理能力......
[dialog]
[PlaySound(key="$d_avg_telephonering", channel="slide", loop=true, volume=1)]
[delay(time=1)]
[stopsound(channel="slide", fadetime=0)]
[PlaySound(key="$d_avg_telephone", volume=1)]
[delay(time=0.6)]
[Character(name="avg_npc_544_1#1$1")]
[name="赫尔曼"]您好？
[Character(name="avg_npc_544_1#1$1")]
[name="赫尔曼"]这里是汐斯塔市政府，我是市长赫尔曼。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[Delay(time=2)]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[musicvolume(volume=0.4, fadetime=1)]
[Delay(time=1)]
[PlaySound(key="$doorknockquite")]
[delay(time=1)]
[PlaySound(key="$dooropenquite")] 
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_222",fadetime=1.5)]
[delay(time=2)]
[name="秘书"]市长先生，打扰一下，我来和您确认一下今天的日程安排。
[Character(name="avg_npc_222")]
[name="秘书"]这是日程表。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]以上是之前已经定好的日程。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]需要您判断的是，我刚刚接到物流合作方来电，他将会在下午一点左右到达汐斯塔。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]您下午原定的日程有三点的与各部门商讨人口迁入的会议，根据各部门排期表来看并不方便延迟，取消会议的可能性不大。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]需要我代您出席会议吗？
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=1)]
[name="赫尔曼"]......你跟着我去见合作方，会议找另一个秘书和他们先开。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=1)]
[name="赫尔曼"]让他做好会议记录，结束后交给我。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]明白。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]与物流合作方商讨这件事需要和各部门同步一下吗？
[character(name="avg_npc_544_1#3$1",name2="avg_npc_222",focus=1)]
[name="赫尔曼"]......可以先说。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=1)]
[name="赫尔曼"]但只说也许能和外国物流公司合作，成功的话会考虑引进新的物流管理模式，要在会中就给出一个新的方案。
[character(name="avg_npc_544_1#1$1",name2="avg_npc_222",focus=2)]
[name="秘书"]好的，我这就去。
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[character(name="avg_npc_222")]
[name="秘书"]......是的，目前是这个状态。
[character(name="avg_npc_222")]
[name

... (全文30603字符)
```

### level_act11mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Sticker(id="st1", text="<i>亲爱的K先生：</i>", x=200,y=170, alignment="left", size=24, delay=0.04, width=700)]
[PlaySound(key="$d_avg_penrustle")]
[Sticker(id="st2", text="<i>祝您一切顺利。我在凌晨的曼斯菲尔德监狱里给您写信。</i>", x=300,y=260, alignment="left", size=24, delay=0.04, width=900)]
[Sticker(id="st3", text="<i>这里的情况同我潜入时相比，没有多大变化。</i>", x=300,y=340, alignment="left", size=24, delay=0.04, width=900)]
[Sticker(id="st2")]
[Sticker(id="st3")]
[Sticker(id="st4", text="<i>狱警们耀武扬威、无所事事，犯人们把过剩的精力发泄在打架斗殴之中。</i>", x=300,y=260, alignment="left", size=24, delay=0.04, width=900)]
[Sticker(id="st5", text="<i>至于我，犯人和狱警们待我很——</i>", x=300,y=340, alignment="left", size=24, delay=0.04, width=900)]
[Sticker(id="st4")]
[Sticker(id="st5")]
[stickerclear]
[character(name="avg_npc_540_1#1$1",fadetime=1.5)]
[delay(time=2)]
杰斯顿对着“很”字沉思了片刻，从枕头套里翻出一封泛黄的信，信封上的寄信人是“K先生”，收信人是他自己。
借着囚室外面的微光，他低声念着上面的话。
[PlaySound(key="$d_avg_paper2")]
[character(name="avg_npc_540_1#1$1")]
[name="杰斯顿"] “请在监狱内安心蛰伏一段时间，切勿惹人关注，不要惹是生非......”
[character(name="avg_npc_540_1#1$1")]
[name="杰斯顿"] “您仍是沙滩伞公司的重要雇员，我们仍为您保留一切职位和待遇......”
[character(name="avg_npc_540_1#1$1")]
[name="杰斯顿"] “只要您在监狱中表现良好，等到时机成熟，我们一定还您自由，并给予您加倍的补偿......”
[character(name="avg_npc_540_1#4$1")]
[name="杰斯顿"] 哼。
[character(name="avg_npc_540_1#10$1")]
[name="杰斯顿"] 公司的那群人反应太慢，都什么时候了，才把这封信寄到我手里。
杰斯顿摇了摇头，小心翼翼地把信纸折好，塞进信封，放回枕头套里。
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[character(name="avg_npc_132")]
[name="A区囚犯A"]*哥伦比亚俚语*，那么刺激的梦，居然被一泡尿给毁了......
[character(name="avg_npc_132")]
[name="A区囚犯A"]哟，这不是杰斯顿吗，你又在熬夜写信了。
[character(name="avg_npc_132")]
[name="A区囚犯A"]上周你就写信，今天你又写信，你到底是写给谁的？
[dialog]
[character]
[name="杰斯顿"] 这和你无关。
[character(name="avg_npc_132")]
[name="A区囚犯A"]有什么好藏着掖着的，就不能给我们看看吗？你到底在写什么呢？向爹妈要钱？威胁老婆不许出轨？
[character(name="avg_npc_132")]
[name="A区囚犯A"]我今天和别人打了赌的，赌注是十根香烟。
[character(name="avg_npc_132")]
[name="A区囚犯A"]告诉我你在写什么吧。要是赢了烟，我分你一半。
[dialog]
[character]
[name="杰斯顿"] 非常抱歉，我要求你尊重我的隐私。
[character(name="avg_npc_132")]
[name="A区囚犯A"]好好好，隐私、隐私。
[character(name="avg_npc_132")]
[name="A区囚犯A"]假扮狱警混进来杀人，人没杀到，自己倒成了囚犯，就这还装什么优雅，要什么隐私？笑死人了。
[dialog]
[playsound(key="$d_gen_walk_n")]
[character(fadetime=1.5)]
[delay(time=2)]
[musicvolume(volume=0.2, fadetime=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=1)]
[Background(image="bg_undergroundF",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.4, fadetime=1)]
[Character(name="avg_npc_134")]
[PlaySound(key="$d_avg_policewhistle",volume=0.8)]
[name="狱警A"] 人都到齐了吗？
[character(name="avg_npc_132")]
[name="A区囚犯A"]杰斯顿还没来！
[Character(name="avg_npc_134")]
[name="狱警A"] 杰斯顿？他又怎么了？
[character(name="avg_npc_132")]
[name="A区囚犯A"]他出门的时候自己不小心，一头撞在铁栅栏上了！
[Dialog]
[Character(name="avg_npc_134", name2="char_empty")]
[PlaySound(key="$rungeneral", volume=0.9)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_134", name2="avg_npc_540_1#1$1",fadetime=0.7)]
[delay(time=2)]
[Character(name="avg_npc_134", name2="avg_npc_540_1#2$1",focus=2)]
[name="杰斯顿"] 非常抱歉，我去医务室了。
[Character(name="avg_npc_134", name2="avg_npc_540_1#2$1",focus=1)]
[name="狱警A"] 医务室？那你摔得不轻啊，“同事”。
[Character(name="avg_npc_134", name2="avg_npc_540_1#2$1",focus=1)]
[name="狱警A"] 说吧，谁绊的你？看在你这段时间老老实实的分上，说出来，我帮你出出气。
[Character(name="avg_npc_134", name2="avg_npc_540_1#10$1",focus=2)]
[name="杰斯顿"] 并没有人绊我，我是自己撞的。
[Character(name="avg_npc_134", name2="avg_npc_540_1#10$1",focus=1)]
[name="狱警A"] 真的？
[Character(name="avg_npc_134", name2="avg_npc_540_1#10$1",focus=2)]
[name="杰斯顿"] 真的。 
[Character(name="avg_npc_134", name2="avg_npc_540_1#10$1",focus=1)]
[name="狱警A"] 那就别三天两头往医务室跑！谁不知道你比铁栅栏还硬，瞎往医务室跑什么？
[Character(name="avg_npc_134", name2="avg_npc_540_1#10$1",focus=1)]
[name="狱警A"] 其他人好好干活！杰斯顿，你过来，我有别的活派给你。
[Character(name="avg_npc_134", name2="avg_npc_540_1#3$1",focus=2)]
[name="杰斯顿"] 不必了，我就和其他犯人一样工作就行——
[Character(name="avg_npc_134", name2="avg_npc_540_1#3$1",focus=1)]
[name="狱警A"] 啰嗦什么，过来！
[Character(name="avg_npc_134", name2="avg_npc_540_1#3$1",focus=1)]
[name="狱警A"] 喏，这是桶，这是清洁剂，拿好了，把整个A区囚室的厕所刷一遍！
[Character(name="avg_npc_134", name2="avg_npc_540_1#1$1",focus=2)]
[name="杰斯顿"] 没问题，如果这是您安排的任务的话。
[Character(name="avg_npc_134", name2="avg_npc_540_1#11$1",focus=2)]
[name="杰斯顿"] 不过，您还没给我刷子。
[Character(name="avg_npc_134", name2="avg_npc_540_1#11$1",focus=1)]
[name="狱警A"] 用什么刷子呀。
[Character(name="avg_npc_134", name2="avg_npc_540_1#11$1",focus=1)]
[name="狱警A"] 你杰斯顿神通广大，用源石技艺变个钢丝球出来还不是轻而易举？去吧！刷完来找我验收，不干净不准吃饭！
[character(name="avg_npc_132")]
[name="A区囚犯B"]哈哈、哈——
[character(name="avg_npc_540_1#4$1")]
[name="杰斯顿"] （深呼吸）
[character(name="avg_npc_540_1#1$1")]
[name="杰斯顿"] 如您所愿，狱警先生，毕竟此时此地，您才是掌握权力的人。
[character(name="avg_npc_132")]
[name="A区囚犯B"]......
[character(name="avg_npc_132")]
[name="A区囚犯B"]呸，被人罚刷厕所，他还装起来了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_prison_corridor",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[Blocker(a=0,

... (全文45652字符)
```


## 统计

- 总字符数：201299
- 对话行数：1740


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
