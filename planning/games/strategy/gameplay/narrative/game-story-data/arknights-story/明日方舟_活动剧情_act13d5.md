# 明日方舟 · 活动剧情 · act13d5（22段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act13d5」完整剧情脚本（22个文件，2797行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act13d5
- 脚本文件数：22

### level_act13d5_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 1上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Character(name="avg_npc_101")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  玛莉娅！怎么样了！
[Dialog]
[Character]
[Character(name="avg_npc_061#2",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  稍等——马上就好！就差一个螺丝！
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  拧紧点！
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=1)]
[name="玛莉娅"]  好的！啊，等等！我好像知道底部电池槽接触不良的原因了——
[Character(name="avg_npc_061#2", name2="avg_npc_101#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  快！这个点唱机老沉了，我要抬不动了——！
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_107",fadetime=1,block=true)]
[delay(time=1)]
[name="光头马丁"]  你的芝士片，老弗。
[Character(name="avg_npc_107", name2="avg_npc_120", focus=2)]
[name="老骑士"]  ......喂，这次不会爆炸了吧？
[Character(name="avg_npc_107", name2="avg_npc_120", focus=1)]
[name="光头马丁"]  修个点唱机也能爆炸是不是夸张了点？
[Character(name="avg_npc_107", name2="avg_npc_120#3", focus=2)]
[name="老骑士"]  不好说，和源石有关系的东西，老科瓦尔都能搞砸。
[Character(name="avg_npc_101#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  谁在说我坏话！
[Character(name="avg_npc_061#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  科瓦尔师傅！小、小心点！别乱晃！
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  喔哦哦——抱歉，玛莉娅。
[Character(name="avg_npc_101#2")]
[name="老工匠"]  老弗！等我空出手来你就完了！
[Character(name="avg_npc_120#2")]
[name="老骑士"]  好，我等着——！
[Character(name="avg_npc_107", name2="avg_npc_120", focus=1)]
[name="光头马丁"]  我这酒吧全靠你俩炒热气氛了，但是别打起来，砸了杯子要赔的。
[Character(name="avg_npc_107", name2="avg_npc_120", focus=2)]
[name="老骑士"]  他都叨叨几十年了，你哪次见他动手赢得过我？
[Character(name="avg_npc_107", name2="avg_npc_120", focus=1)]
[name="光头马丁"]  上次。
[Character(name="avg_npc_107", name2="avg_npc_120", focus=2)]
[name="老骑士"]  呃......上次我喝醉了，还犯关节炎......那不算数。
[name="老骑士"]  咕嘟咕嘟——哈，当年他陪着我赶赴边疆的时候可不敢这么和我说话......
[Character(name="avg_npc_101#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  老弗！你是不是又在说什么大话！
[Character(name="avg_npc_120#2")]
[name="老骑士"]  当年你是不是我的扈从！你就说是不是！
[Character(name="avg_npc_101#2")]
[name="老工匠"]  这都几几年了，扈从都已经穿上西装变成你们的主子了——
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[PlaySound(key="$char_emp", volume=0.9)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_064_weapon_1#2",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]  玛莉娅！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  噫！
[Dialog]
[Character(name="avg_npc_101")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  啊——！痛！丫头，你别突然放手啊！
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  抱、抱歉......先让我躲一下.....
[Character(name="avg_npc_107")]
[name="光头马丁"]  佐菲娅，轻点，这个月已经换了几次大门了。
[name="光头马丁"]  唉，这就是我不愿意花钱换自动门的原因啊。
[Character(name="avg_npc_101")]
[name="老骑士"]  发生什么了，干嘛这么气势汹汹的？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_064_weapon_1#5")]
[name="佐菲娅"]  ......
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_npc_064_weapon_1#4")]
[name="佐菲娅"]  在那儿是吧？
[CameraShake(duration=1, xstrength=12, ystrength=24, vibrato=60, randomness=90, fadeout=true, block=false)]
[name="佐菲娅"]  玛、莉、娅！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  噫——！
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Character(name="avg_npc_061#6", name2="avg_npc_101", focus=2)]
[name="老工匠"]  喂，丫头，她走过来了，你好像没藏住。
[Character(name="avg_npc_061#6", name2="avg_npc_101", focus=1)]
[name="玛莉娅"]  呜......这个点唱机为什么这么小啦......
[name="玛莉娅"]  她现在什么表情？
[Character(name="avg_npc_061#6", name2="avg_npc_101", focus=2)]
[name="老工匠"]  不妙哦，自上次她把那个喝醉的小鬼骑士扔出去之后我还没看过她那么生气。
[name="老工匠"]  ——啊，她微笑着走过来了。
[Character(name="avg_npc_061#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  那更不妙了啊！
[Character(name="avg_npc_064_weapon_1#4")]
[name="佐菲娅"]  科瓦尔？
[Character(name="avg_npc_101")]
[name="老工匠"]  咳——老弗！来喝酒！你刚才是不是说我坏话了！我今天必把你喝趴下！
[Character(name="avg_npc_120", name2="avg_npc_101", focus=1)]
[name="老骑士"]  啧，临阵脱逃的胆小鬼。
[Character(name="avg_npc_107", name2="avg_npc_120", focus=1)]
[name="光头马丁"]  那你怎么不去帮玛莉娅说说话？
[Character(name="avg_npc_107", name2="avg_npc_120", focus=2)]
[name="老骑士"]  我、我又不知道出什么事儿了！不要乱说话比较好！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_064_weapon_1#4")]
[name="佐菲娅"]  玛、莉、娅，你躲什么呢？
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  ......呃......
[Character(name="avg_npc_064_weapon_1#4")]
[name="佐菲娅"]  你是不是......有什么事瞒着我呀？虽然我已经全部知道了喔？
[Character(name="avg_npc_061#

... (全文14843字符)
```

### level_act13d5_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 1下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_nearllivingroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  （装备，穿戴完毕。剑......是姐姐以前的训练剑，应该还能用吧？）
[name="玛莉娅"]  （就这样出发......）
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.4)]
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_108",fadetime=1,block=true)]
[delay(time=2)]
[name="？？？"]  ......
[Character(name="avg_npc_108", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  啊......玛恩纳叔叔.....
[Character(name="avg_npc_108#2", name2="avg_npc_061#2", focus=1)]
[name="玛恩纳"]  怎么，还嫌临光家不够丢人吗？
[Character(name="avg_npc_108#2", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  不是的——！
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=1)]
[name="玛恩纳"]  骑士竞技......部门的同事已经告诉我这件事了。
[name="玛恩纳"]  你不配站上骑士竞技的赛场，而骑士竞技也配不上临光之名。
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=1)]
[name="玛恩纳"]  是佐菲娅怂恿的吗？
[Character(name="avg_npc_108", name2="avg_npc_061#5", focus=2)]
[name="玛莉娅"]  不是的！是我自愿——
[Character(name="avg_npc_108", name2="avg_npc_061#5", focus=1)]
[name="玛恩纳"]  我想也是。佐菲娅虽然只是临光家的陪侍，但好歹也在那种商业闹剧里占有一席之地......她现在也是“骑士阶级”了，呵。
[name="玛恩纳"]  可，你呢？
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  我......我只是想保护......
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=1)]
[name="玛恩纳"]  就算被剥夺了贵族身份，我们的信条也不会有一丝动摇，没有什么需要被保护。
[Character(name="avg_npc_108", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  就算这么说......
[Character(name="avg_npc_108#2", name2="avg_npc_061#7", focus=1)]
[name="玛恩纳"]  更没有什么需要你保护，玛莉娅。
[name="玛恩纳"]  别和玛嘉烈一样，只因为年轻气盛就轻易打破了那份矜持——
[Dialog]
[Character(name="avg_npc_108")]
[PlaySound(key="$phonevibration",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[Character(name="avg_npc_108#3")]
[name="玛恩纳"]  ——部长？
[name="玛恩纳"]  晚上好，嗯，是的，是我没错......
[name="玛恩纳"]  请阁下务必放心，如果您对先前的会议有任何疑问都可以来找我......什么？不，不，请您再考虑一下......求您了，是的......
[Dialog]
[Character(name="avg_npc_108")]
玛恩纳瞥了一眼玛莉娅，他冷漠地走上楼去。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_108#3")]
[name="玛恩纳"]  不，的确是我的工作失误，与阁下无关，稍后我会将修订过的文档邮寄给您......明天，对，明天一定......非常抱歉。
[name="玛恩纳"]  不，恳求您务必再考虑一下。嗯，一定，是的，我不会再犯这种失误，请原谅......
[Character(name="avg_npc_108#2")]
[delay(time=0.6)]
[name="玛恩纳"]  ——玛莉娅，下次再说回你的事情，希望你自己有点分寸。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.4)]
[Character(fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="avg_npc_061#7")]
[name="玛莉娅"]  叔叔......
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  不......现在动摇有什么用，快要赶不上和佐菲娅约定的时间了。
[Character(name="avg_npc_061#7")]
[name="玛莉娅"]  ......
[stopmusic(fadetime=2)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.4)]
[Character(name="avg_npc_064_weapon_1#6")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[Character(name="avg_npc_061#3", name2="avg_npc_064_weapon_1#5", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  唔——！
[Character(name="avg_npc_061#3", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  站稳了，注意节奏。
[Dialog]
[Character(name="avg_npc_064_weapon_1#6")]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  呼——
[name="佐菲娅"]  十分钟，一次反击都没有。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  呃......说是单手对付我，你的那把剑不就是单手用的吗！
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  全力以赴的话另一只手也不会闲着的，想试试莱塔尼亚人的作战方法吗？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  我是听

... (全文23302字符)
```

### level_act13d5_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 2上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_103",fadetime=1,block=true)]
[delay(time=1)]
[name="塑料骑士"]  ......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_121", name2="avg_npc_103", focus=1)]
[name="大嘴莫布"]  怎么了怎么了？这不是呼啸守卫家的新星选手嘛？来得可真早啊。
[name="大嘴莫布"]  观众都还没入场，还有两个小时才是本日第一场比赛，是来做提前准备的吗？
[Character(name="avg_npc_121", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  很久没有在这种地方打过比赛了......真让人怀念。
[Character(name="avg_npc_121", name2="avg_npc_103", focus=1)]
[name="大嘴莫布"]  是啊是啊，我也很好奇，虽说骑士称号是“塑料”，但这也算是你的卖点之一......
[name="大嘴莫布"]  上个月的赛程结束后，你的积分在骑士团内已经名列前茅了吧。有必要这么努力吗？
[Character(name="avg_npc_121", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......老东家的要求，我也没办法，害得我假期都取消了。
[Character(name="avg_npc_121", name2="avg_npc_103", focus=1)]
[name="大嘴莫布"]  啊，目的果然是那个？
[Character(name="avg_npc_121", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  明知故问。
[Character(name="avg_npc_121", name2="avg_npc_103", focus=1)]
[name="大嘴莫布"]  哎，果然如此？那今天可不就有好戏看了......
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=1)]
[name="？？？"]  的确有好戏在等待......不过在那之前，请允许我和“塑料”瑟奇亚克先生单独谈谈。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  你是......？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="？？？"]  我是特锦赛海选的工作人员，这是我的名片，瑟奇亚克先生。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......“工作人员”，有什么事吗？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="？？？"]  我只是来通知您一些事情的。
[name="？？？"]  呼啸守卫公司要求您在与玛莉娅·临光的一对一综合竞赛，也就是俗称的“决斗赛”中，装备最新的Jack2护甲型号，并尽力拖延战斗时间。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  什么？但新护甲的材质根本不是为了骑士竞技准备的——
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="？？？"]  无妨。“临光的复出”引来了无数媒体，这是个大好机会。
[name="？？？"]  为了拿下那份长期贸易合同的竞标，他们已经付出了太多代价。他们正需要一次合理的博弈机会，即是测试，也是宣传。
[name="？？？"]  至于呼啸守卫宣传执行部门承诺为你准备的定金......是你去年税后总收入的三倍。
[name="？？？"]  只这一场比赛，足够在你的家乡买下一座村庄了，瑟奇亚克先生。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......需要做到这个地步吗？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="？？？"]  曝光率和带货宣传只是其次，话题热度和特锦赛收益能让呼啸守卫在商业联合会上有着更多的......嗯......发言权。
[name="？？？"]  发言权是很重要的，不是吗？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  既然是老东家的要求......又有钱拿，何乐而不为？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="？？？"]  感谢配合，我们也清楚瑟奇亚克先生有一些特别的需求......
[name="？？？"]  对了，你见过临光家的小女儿吗？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  我看过她的出道战，不算太差，但和耀骑士比起来，太让人失望了。
[name="塑料骑士"]  ......你是在担心我会输？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="？？？"]  不......我并不在意，失礼了。关于新型护甲的注意事项，我们已经和全套装备一并送到了您的住所，请您......
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Character(name="avg_npc_107", name2="avg_npc_101", fadetime=1,block=true,focus=0)]
[delay(time=3)]
[Character(name="avg_npc_120")]
[name="老骑士"]  ......你们有必要现在就凑在一起吗？
[Character(name="avg_npc_120", name2="avg_npc_101", focus=2)]
[name="老工匠"]  什么话！还有一个半小时丫头就要出场了！这可是认真训练过后的首战！当然要捧个场！
[Character(name="avg_npc_107", name2="avg_npc_101", focus=1)]
[name="光头马丁"]  哈哈哈，说得对，所以今天我请客。
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  唉，吵吵闹闹的......
[name="老骑士"]  ......
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  给，“荆棘泪珠”，你很少喝这么烈的酒，在担心吗？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  从佐菲娅第一次问我请教剑术到初赛，她花了整整四年时间......但玛莉娅只花了四个星期。
[name="老骑士"]  我们都该盯着点，该收手就要收手，不能让她们胡来。
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  哈哈哈......一腔热血的年轻骑士，真是让人想起了玛嘉烈说要参赛的那个时候。
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  但她们是不一样的。
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  总之，给她一点信任。
[name="光头马丁"]  只要用聪明点的方式累计积分，获得特锦赛资格也不是什么难事。
[Character(name="avg_npc_120#3", name2="avg_npc_107", focus=1)]
[name="老骑士"]  对于普通的选手，也许可以，但是对于玛莉娅......我不知道。
[name="老骑士"]  总觉得......麻烦会找上门来的。
[Character(name="avg_npc_120#3", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  怎么回事，老弗？你怎么尽泼冷水？是不是嫉妒了？要不要老脸？
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老骑士"]  你说什么！？
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  女——士们先生们！欢迎——光临！
[name="大嘴莫布"]  不得不提前祝贺你们，在今天这个日子来到由呼啸守卫公司全资赞助的呼啸竞技场！“呼啸守卫，狂风也将臣服于你”！
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  不知各位是否找到了值得掏空腰包的独立骑士，如果没有，那么今天，容我再次介绍一遍——
[name="大嘴莫布"]  自上一次的昙花一现已经间隔一月之久，出道战就成为话题中心，不知经历了怎样的磨炼再度归来！
[name="大嘴莫布"]  让我们热烈地欢迎，呼啸竞技场最美丽的脸蛋，传奇的姊妹，临光家最年轻的竞技骑士！
[Character(name="avg_npc_121#3")]
[name="大嘴莫布"]  玛——莉——娅，临光——！！
[Dialog]
[Character]
[Character(name="avg_npc_061#2",fadetime=1,block=true)]
[delay(time=2)]
[PlaySound(key="$livecrowd", volume=0.5, loop=false, channel="people")]
[delay(time=1)]
[Character]
[name="游客"]  我把全部家当都压在你身上啦！临光！
[name="游客"] 

... (全文11950字符)
```

### level_act13d5_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 2下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$livecrowd", volume=0.5, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  各位！各位！各位！
[name="大嘴莫布"]  在竞赛开始之前，谁能预料到这个结果——声名远扬的临光家族与塑料骑士的对决，谁能想到会是这个结果！
[name="大嘴莫布"]  玛莉娅·临光！这个继承了临光之名的小女孩，竟然——！
[name="大嘴莫布"]  被瑟奇亚克完全压制！毫——无——还——手——之——力——！
[name="大嘴莫布"]  这样可不行啊！临光！为了这个名字，你知道在座的观众押了多少钱吗！？
[Character(name="avg_npc_121#2")]
[name="大嘴莫布"]  啊，什么？看赔率其实并不高？喂，你们倒是对临光抱点信任啊！这张脸不值钱吗！？
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.3, loop=false, channel="people")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="玛莉娅"]  呃——！
[Character(name="avg_npc_103")]
[name="塑料骑士"]  又是佐菲娅又是耀骑士的，结果你就这点本事吗......？
[name="塑料骑士"]  让人失望。
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_103")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[Character(name="avg_npc_061#3")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_103")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  不愧是呼啸骑士团的老将，利用人造地形和速度优势，我们可怜的小马驹无处可逃！
[name="大嘴莫布"]  再度停步！再度射击！再度转移！这就是“塑料节奏”！
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  （根、根本看不见他的动作！为什么？明明还没有佐菲娅的动作快——）
[Character(name="avg_npc_061#5")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  （他停下了，得格挡——！）
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[Character(name="avg_npc_061#5")]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[Character(name="avg_npc_103")]
[name="塑料骑士"]  太慢！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.4, block=false)]
[Character]
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.4, block=false)]
[Character(name="avg_npc_061#5")]
[CameraShake(duration=0.4, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_064_weapon_1#2")]
[name="佐菲娅"]  ——玛莉娅！左边！
[Dialog]
[Character]
[Character(name="avg_npc_061#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  什——呜！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  瑟奇亚克，踩着墙壁做出的完美的连续射击！哎呀，如果发生了当场击毙的意外，可就要掐掉直播了啊，好险好险！
[name="大嘴莫布"]  没想到这身自开赛至今被命中数次却完全没有损耗的坚固护甲，竟然还能允许人做出如此轻便的动作！真令人惊讶！
[name="大嘴莫布"]  看到了吗！这就是呼啸守卫的最新产品！Jack2特殊高性能塑化凝胶！
[name="大嘴莫布"]  这种抢手货谁人不爱！？但也不要担心，现在竞技场前台正在派发九五折优惠券！机不可失时不再来！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_122", name2="avg_npc_123", focus=1)]
[name="？？？"]  那就是......临光？
[Character(name="avg_npc_122", name2="avg_npc_123", focus=2)]
[name="？？？"]  等等，她真的是那个耀骑士的妹妹吗？
[Character(name="avg_npc_122", name2="avg_npc_123", focus=1)]
[name="？？？"]  ......怎么，失望了？
[Character(name="avg_npc_122", name2="avg_npc_123", focus=2)]
[name="？？？"]  不......我怎么会因为这种事情失望。倒是你呢？
[Character(name="avg_npc_122", name2="avg_npc_123", focus=1)]
[name="？？？"]  我？哎呀...

... (全文22705字符)
```

### level_act13d5_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 3上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[PlaySound(key="$livecrowd", volume=0.2, loop=false, channel="people")]
[name="众人"]  干杯——！
[Delay(time=1)]
[Character(name="avg_npc_101")]
[name="老工匠"]  恭喜丫头获胜，真是精彩的表现，比现在的老弗强多了！
[Character(name="avg_npc_120#2", name2="avg_npc_101", focus=1)]
[name="老骑士"]  那是比我强多了——但轮不到你说这个话！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  啊啊！？
[Dialog]
[PlaySound(key="$fightgeneral")] 
[Character(name="avg_npc_101")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[Character(name="avg_npc_120")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_064_weapon_1#6")]
[name="佐菲娅"]  怎么又动起手来了......喂，别吵到旁边的客人。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  啊哈哈......都开始扳手腕了......
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  打得不错，孩子，这杯敬你。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  啊.....谢谢！
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  在那种场合还能找出瑟奇亚克的弱点，而且一击制胜，你做得很好。
[name="光头马丁"]  战斗持续了接近二十分钟，一直处于劣势的玛莉娅能在关键的一击中找出反败为胜的方法——
[name="光头马丁"]  ——很了不起。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  没、没有的事啦......如果不是他穿着那种缺陷型号的护甲，可能还真的无从下手......
[name="玛莉娅"]  Jack2型号是我从来没有听说过的产品......冷却系统会导致装甲极短的瘫痪，那根本就是试验品。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  ——但瑟奇亚克是个经验老道的竞赛骑士，这种事情并不罕见，他把宣传品的缺点掩饰得很好。
[name="光头马丁"]  也不用太谦虚了，虽然很粗暴，但骑士竞技向来都是结果论的。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  好、好的......
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#2", focus=2)]
[name="佐菲娅"]  ......玛莉娅！
[Character(name="avg_npc_061#3", name2="avg_npc_064_weapon_1#2", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  在！
[Character(name="avg_npc_061#3", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  不要高兴得太早！
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  是！
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  你要刻意地去控制心态——不是保持平常心就好了的，你要去主动反省，主动平复心情......
[name="佐菲娅"]  ......自负自满这种东西啊，你越是觉得自己没有，越危险，胜利带来的影响是你自己都意识不到的......
[name="佐菲娅"]  而这份大意......会......麻痹你！
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  明、明白！
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[Delay(time=0.6)]
[name="玛莉娅"]  ......姑母？你喝醉了？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#2", focus=2)]
[name="佐菲娅"]  我没有！别叫我姑母！
[Dialog]
[Character]
[delay(time=1)]
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  ——我赢了！！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  该死，科瓦尔，你为什么比半年前还结实了！？
[Character(name="avg_npc_120#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  修水管修的，不服啊？
[Character(name="avg_npc_120", name2="avg_npc_101", focus=1)]
[name="老骑士"]  嘁......
[Character(name="avg_npc_120", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  科瓦尔叔叔，弗格瓦尔德叔叔，佐菲娅姐姐是不是？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  玛莉娅......别喊姑母......
[Character(name="avg_npc_101", name2="avg_npc_064_weapon_1", focus=1)]
[name="老工匠"]  哦.....真的喝醉了，真难得。
[Character(name="avg_npc_101", name2="avg_npc_064_weapon_1#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佐菲娅"]  我......我才没！
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  得了吧！玛莉娅，把你姑母抬到后面的沙发上睡会。
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=1)]
[name="玛莉娅"]  欸......好，好的，姑母......麻烦你抬一下脚......
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佐菲娅"]  别喊姑母！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_120", name2="avg_npc_101", focus=2)]
[name="老工匠"]  “鞭刃”佐菲娅在这里还有一个绰号叫做“千杯”佐菲娅来着......虽然比不过我就是了。
[Character(name="avg_npc_120", name2="avg_npc_101", focus=1)]
[name="老骑士"]  是是是，“万两”弗伦丁，和炎国人喝过一顿以后你就这么嘚瑟？和年轻姑娘比喝酒，老脸不红？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  她的压力很大......第一次以教练的身份盯着赛场，听着那个大嘴莫布絮絮叨叨。
[name="光头马丁"]  真让人怀念......唉，玛莉娅获胜之后我总是这么感叹，我是不是也老了呢？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  想什么呢？我们不是平辈吗？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  那看来是真的老了。
[Character(name="avg_npc_120#2", name2="avg_npc_107", focus=1)]
[name="老骑士"]  喂。
[Character(name="avg_npc_120#2", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  ......是啊，离我第一次看着佐菲娅上阵，过去多久了？十二年？十五年？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  你老了我是没意见，日子都记不清了，但佐菲娅可没那么老啊......
[name="老骑士"]  九年前的事情吧。血骑士，耀骑士，黑骑士......三届之前了。
[Character(name="avg_npc_120", name2="avg_npc_107#2", focus=2)]
[name="光头马丁"]  黑骑士......那个卡普里尼啊，感觉已经是上个时代的名字了呢。
[Character(name="avg_npc_120", name2="avg_npc_107#2", focus=1)]
[name="老骑士"]  毕竟再往前三届也全都是她。媒体们也经常把她当做“时代的标杆”。
[Character(name="avg_npc_120", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  啊，是那个前所未有的三连冠？
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  是啊，一般的骑士封号可不会用那么宽泛的字眼，不然肯定会重复的，叫起来多麻烦。
[name="老工匠"]  但那个莱塔尼亚女人，的确值得夺走“黑”这个字。她根本就是个怪物。
[name="老工匠"]  听说现在跟着某

... (全文20958字符)
```

### level_act13d5_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 3下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
玛莉娅。
玛莉娅，你有一双天马的眼睛。
玛莉娅，站起来，来，过来。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  ——！
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  呃！？
[Dialog]
[Character]
[Character(name="avg_npc_104",fadetime=1,block=true)]
[delay(time=1)]
[name="锈铜骑士"]  哈......哈......！居然躲开了！
[name="锈铜骑士"]  那好吧，就让你的右手在你的身上多呆一会......反正就一小会。
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  （——不是眼泪，黏糊糊的，是血？）
[name="玛莉娅"]  （......好多血......）
[name="玛莉娅"]  （心跳好快......我......）
[CameraShake(duration=0.6, xstrength=8, ystrength=16, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_104")]
[name="锈铜骑士"]  滑稽，真滑稽，你挥舞武器的样子就像大骑士团门前的那些弄臣......
[name="锈铜骑士"]  除了外貌，你有哪点像那个耀骑士了？
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="玛莉娅"]  我......我是不会输的！
[Character(name="avg_npc_104")]
[name="锈铜骑士"]  好啊，这样我更乐意撕碎你那张脸了，不识好歹的贵族妞！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_104")]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_061#6")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[Character(name="avg_npc_061#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  英格拉！风暴般的追击！
[name="大嘴莫布"]  这是本次赛事以来，呼啸竞技场最夸张的一次损毁——！赛场屠夫英格拉！“锈铜”英格拉！
[name="大嘴莫布"]  就在一个月前，“锈铜”英格拉在本赛季的首秀就将“焚风”骑士殴打致四肢粉碎性骨折才肯罢休！
[name="大嘴莫布"]  没错，是殴打！这绝非手持武器的骑士行径！
[name="大嘴莫布"]  今天，在呼啸竞技场备受瞩目的玛莉娅·临光，是否也难逃“锈铜”残暴的利斧？观众们，告诉我你们的态度！
[PlaySound(key="$livecrowd", volume=0.5, loop=false, channel="people")]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121#3")]
[name="大嘴莫布"]  就是这样！“锈铜”英格拉！让你的对手血溅当场吧！
[stopmusic(fadetime=1)]
[PlaySound(key="$livecrowd", volume=0.1, loop=false, channel="people")]
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  呼啊......哈啊......
[name="玛莉娅"]  （好重——）
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$livecrowd", volume=0.1, loop=false, channel="people")]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_064_weapon_1#2")]
[name="佐菲娅"]  玛莉娅！投降吧！
[name="佐菲娅"]  只是输掉一场比赛而已！积分还是有机会的——！
[Character(name="avg_npc_064_weapon_1#6")]
[name="佐菲娅"]  玛莉娅——！！
[Dialog]
[Character]
佐菲娅姑母......在说什么？
听不清......头好晕......盾也好重......
我......在做什么......骑士竞技......我在赛场上......
快......睁开眼！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_061#6",fadetime=1,block=true)]
[delay(time=2)]
[name="玛莉娅"]  呼啊......呼啊......
[Character(name="avg_npc_104")]
[name="锈铜骑士"]  哈！不错的反击——这才有撕裂你的意义！
[name="锈铜骑士"]  那么快就完蛋可没意思了，我要用你的血，涂满你那张让人火大的脸......耀骑士！
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  你明明......也快到极限了吧？
[Character(name="avg_npc_104")]
[name="锈铜骑士"]  哈，这点血也能叫伤！？
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(fadetime=0.6,block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_064_weapon_1#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="佐菲娅"]  玛莉娅！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.6, block=true)]
[Character(name="avg_npc_122", name2="avg_npc_123", focus=1)]
[name="？？？"]  嗯......

... (全文14932字符)
```

### level_act13d5_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 4上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
3:49 P.M.  天气/晴   卡西米尔四城联合，某私人露天阁楼
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=2)]
[name="？？？"]  ......您来了，莫布先生。
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  呃，是您啊，之前在竞技场见到您的时候，您说——
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="？？？"]  不，那些都无所谓，别这么紧张，请坐。
[name="？？？"]  请容我重新自我介绍一下——请叫我恰尔内，本次骑士协会赛区轮换负责人之一。
[name="发言人恰尔内"]  同时也是梅什科集团骑士竞技与宣发部门执行人，被有幸选中成为商业联合会驻赛区发言人。
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  商、商业联合会？请一定要原谅我先前的无礼，恰尔内先生......
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  别这么说，我并不讨厌您的......语言风格，“大嘴莫布”，或者说，我该称呼您的本名？
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  不、不用......
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  哈哈，开个玩笑而已......看看外面，多壮丽的景色。
[Character(name="avg_npc_121#2", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  有些老人家讨厌这样钢筋水泥的丛林，讨厌这白昼黑夜不分的都市，但要我说，这才是文明进步的象征。
[name="发言人恰尔内"]  广袤的森林和草原当然是卡西米尔的一部分，但是强韧的卡西米尔人在林间的空地上建立起了高楼广厦，这是一件值得自豪的事情。
[name="发言人恰尔内"]  只有这样我们才能躲避天灾侵袭，才能形成足以抗拒外敌的坚固阵线。卡西米尔如今一片繁荣，进步迅速......
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  您说对吗？莫布先生。
[Character(name="avg_npc_121", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  当然！您说的对！
[Character(name="avg_npc_121", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  但卡西米尔的进步尚未抵达尽头，我们还有很长的路要走。
[name="发言人恰尔内"]  比如......莫布先生，您知道在您的故乡，被称为“林萌与匠人之都”的奥格尼斯科。
[name="发言人恰尔内"]  在其方圆千里之内，有多少贫穷的村庄，有多少不受城邦庇护的险地？
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  您、您知道得可真清楚，我离开那儿已经有二十多年啦。不过您为什么要和我说这些？说实话，我现在惴惴不安的......
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  坦诚也是我中意您的一点。我是来告诉您一件事，莫布先生，为了我们共同的进步，您被挖角了。
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  ......我？但我刚拿了呼啸守卫的定金......
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  请放心，这份秘密合同上有帕维尔先生的印章，而您从今天开始的雇主就是......
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  我、我现在是梅什科公司的人啦！？
[Character(name="avg_npc_121#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  可以这么说......但也有点小小的不同。
[Character(name="avg_npc_121", name2="avg_npc_106", focus=1)]
[name="大嘴莫布"]  呃？
[Character(name="avg_npc_121", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  现在起，你是我的人了，主持人先生。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_061#5")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  喝啊——！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  ......今天就到这里为止吧。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=1)]
[name="玛莉娅"]  欸？但我还可以......
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#2", focus=2)]
[name="佐菲娅"]  过犹不及！你才刚痊愈没多久，库兰塔身体再结实也没你这么折腾的！
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#2", focus=1)]
[name="玛莉娅"]  好吧......
[name="玛莉娅"]  ——那姑母，上次和你提过的源石技艺打法能不能再陪我琢磨一下？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  ......昨天不是和你说过了吗？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="玛莉娅"]  我昨晚看了莱塔尼亚骑士的战斗录像，我觉得其实有可以借鉴的地方——
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#4", focus=2)]
[name="佐菲娅"]  昨晚？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#4", focus=1)]
[name="玛莉娅"]  啊......
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佐菲娅"]  你又熬夜了！我说过要好好休息的吧！
[Dialog]
[Character]
[Character(name="avg_npc_107",fadetime=1,block=true)]
[delay(time=2)]
[name="光头马丁"]  看来恢复得不错，这下那两个老家伙总算可以放心了。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  啊，马丁叔？你怎么来了？
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  你说为什么......因为这个啊。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  这、这是？
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  找上门来的赞助商，整整十三家，其中倒是有一些排得上名号的大企业......
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  呜啊，这个辉煌盾是那个军火厂商吧......这种企业原来还会培养竞技骑士的？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  都是些骑士团邀请，虽然数字让人心动，但结果而言都只是成为傀儡而已。
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_061#5", name2="avg_npc_064_weapon_1#2", focus=2)]
[name="佐菲娅"]  玛莉娅！你可千万别被这种资本家迷惑了啊？！这种程度姐姐也可以负担得起的！
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#2", focus=1)]
[name="玛莉娅"]  欸......我是没被骗到啦，不过姑母你就这么给我花钱也怪不好意思的......
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  

... (全文10863字符)
```

### level_act13d5_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 4下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$e_atk_arrow_h")]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.25, block=true)]
[CameraShake(duration=0.6, xstrength=5, ystrength=8, vibrato=30, randomness=90, block=true)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  还剩——八名——
[name="大嘴莫布"]  不，是该说“还剩”八名，还是该说竟然已经有近半数骑士负伤退场！
[Character(name="avg_npc_121#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="大嘴莫布"]  等等——说话间，“灰发”骑士就在“泉水”骑士身上夺走了一个积分——啊！！“穿岩”多尔克偷袭了二人！卓有成效！！
[Character(name="avg_npc_121#3")]
[name="大嘴莫布"]  处处都是尔虞我诈——这就是炎刃混战赛的魅力，纯粹的暴力！！
[Dialog]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_061#5")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  光——！
[Dialog]
[Character]
[name="“树枝”骑士"]  就这点能耐，你是怎么打赢英格拉的！？
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  你的剑术......也完全比不上姑母！
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.2, block=false)]
[Character(name="avg_npc_061#5")]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[name="“树枝”骑士"]  嘁，我一定会把你从那个积分榜上拽下来的，“临光”，看招！
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  啊——背后！
[Character]
[name="“树枝”骑士"]  啊——！？
[Dialog]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_122",fadetime=1,block=true)]
[delay(time=2)]
[name="路过的粉丝"]  唔？
[name="路过的粉丝"]  又见面了，小临光，这次你可没地方可去了。
[Dialog]
[Character(name="avg_npc_061#2")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Character]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  “树枝”之后是“焰尾”吗！！喂喂喂，这是比赛开始后第几次针对小临光的袭击了？这可不是你的个人秀啊，玛莉娅！
[Character(name="avg_npc_122")]
[name="路过的粉丝"]  那个家伙真吵啊。
[name="路过的粉丝"]  不过剩下的家伙越来越少了，这下咱们总算可以比试一下了吧？
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  ——比试的话，我乐意奉陪。
[Character(name="avg_npc_122")]
[name="路过的粉丝"]  哦哦，不错嘛，比起你和“塑料”打的时候，眼神好多了。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  ......
[Character(name="avg_npc_122")]
[name="路过的粉丝"]  嘿——
[Dialog]
[Character]
眨眼，一睁，一闭。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  （下面！？）
[Character(name="avg_npc_061#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  呃——！？
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[Character]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_122",fadetime=1,block=true)]
[delay(time=2)]
[name="路过的粉丝"]  唔哦？这都躲开了？
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  （刚才她是什么动作......与其说快，不如说灵巧得过分......）
[Character(name="avg_npc_122")]
[name="路过的粉丝"]  哎，这下我明白为什么你能从英格拉和瑟奇亚克手下坚持那么久啦......比想象中要扎实嘛。
[name="路过的粉丝"]  都是“鞭刃”教你的。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  ......
[Character(name="avg_npc_122")]
[name="路过的粉丝"]  嗯，警惕性也不错，学习速度也挺快的。
[name="路过的粉丝"]  但是——
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[

... (全文16019字符)
```

### level_act13d5_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 5上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人恰尔内"]  您的是这杯。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  谢谢，谢谢。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  呼啸守卫向会员提供的酒水非常丰富，真羡慕那些会员，他们能站在这里，看着骑士们的精彩表现。
[name="发言人恰尔内"]  您说，您是个好人，对吧？
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  呃......
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  您犯过法吗？
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  ......没有。
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  您做过什么坏事吗？
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  不，当然，也没有......
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  换言之，您勤勤恳恳地工作，为自己和家人赚取酬薪，您难道不是个好人吗？
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  是、是这样，这么说，我的确是个好人，卡西米尔有很多这样的好人......
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  是啊，很多的好人，来，为好人们干杯。
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  啊，干杯。
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  您说，如果有人要剥夺好人的工作，剥夺好人生活的办法，这种人，还能是好人吗？
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=1)]
[name="企业员工"]  您是说......？
[Character(name="avg_npc_109", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  连乡野农夫在农活结束之后，都会以收看附近城邦的骑士竞技转播为乐。
[name="发言人恰尔内"]  数十万......甚至是上百万产业相关的卡西米尔人都靠着骑士竞技而活，他们大都是些好人啊，先生。
[Character(name="avg_npc_109#2", name2="avg_npc_106#3", focus=1)]
[name="企业员工"]  您说的是......
[Character(name="avg_npc_109#2", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  假如有一天，骑士竞技消失了......企业一夜之间消失了。
[name="发言人恰尔内"]  谁来为征战骑士们提供年年增长的军费，谁为卡西米尔争取经济地位以遏制外敌的侵略？
[name="发言人恰尔内"]  先生，您说，那些反对者，是坏人吗？
[Character(name="avg_npc_109#3", name2="avg_npc_106#3", focus=1)]
[name="企业员工"]  ......
[Character(name="avg_npc_109#3", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  您是个好人，他们要剥夺您的生活，为他们古老的“荣誉”加冕。
[name="发言人恰尔内"]  同样是靠他人铺设道路，至少我们给了大部分人——甚至是感染者——活下去的机会......
[name="发言人恰尔内"]  那些“坏人们”，则为了他们微不足道的自我安慰，将国家和国民的利益置之不顾。
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  先生，您是个好人，对吧？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Character]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=false)]
[name="游客"]  这就是临光最常光顾的酒吧吗，哇塞，真有卡西米尔的风格！
[name="游客"]  喂，老板！今天玛莉娅·临光会来这里吗？
[Character(name="avg_npc_107")]
[name="光头马丁"]  这就要看你们的运气了。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="avg_npc_120",fadetime=1,block=true)]
[delay(time=1)]
[name="老骑士"]  最近生意兴隆啊？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  托玛莉娅的福。
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  上一次这么多人得是什么时候了？佐菲娅那时候吗？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  这就是“骑士”啊，这其中的大部分人都是慕名而来的，真不知道是哪家媒体报道的......
[Character(name="avg_npc_120", name2="avg_npc_107", focus=1)]
[name="老骑士"]  有钱赚你还不乐意？
[Character(name="avg_npc_120", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  这不是想让她俩有个安安静静放松的地方嘛。
[Character(name="avg_npc_107", name2="avg_npc_101", focus=2)]
[name="老工匠"]  喂，马丁，在这张座位上刻个字，“科瓦尔专属”，我可不想下次过来还要等位子。
[Character(name="avg_npc_107", name2="avg_npc_101", focus=1)]
[name="光头马丁"]  付一笔冠名费，我就同意。
[Character(name="avg_npc_107", name2="avg_npc_101", focus=2)]
[name="老工匠"]  呿。
[Dialog]
[Character]
[name="游客"]  喂，喂，临光真的来了！本人哦！
[name="游客"]  快，别放过这个机会，去要张合影！
[Character(name="avg_npc_061#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=false)]
[name="玛莉娅"]  呃，谢谢、谢谢......合影？我吗？抱歉，我现在......
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  好了好了，都让一让——
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=false)]
[Character]
[name="游客"]  等等......你是佐菲娅！是“鞭刃”佐菲娅！！
[name="游客"]  喂，传言是真的！“鞭刃”佐菲娅真的是小临光的教练！
[name="游客"]  佐菲娅小姐！我看过你的比赛，我深受感动！！
[Dialog]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  （啊，好，完蛋。）
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=false)]
[name="玛莉娅"]  （姑、姑母！快想想办法！）
[Character]
[name="游客"]  玛莉娅，我爱你啊！
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=false)]
[name="游客"]  你说什么！？
[Character(name="avg_npc_120", name2="avg_npc_101", focus=1)]
[name="老骑士"]  喂，要打架出去打。
[Character(name="avg_npc_120", name2="avg_npc_101", focus=2)]
[name="老工匠"]  就是，在这里打架是老东西的特权。
[Character(name="avg_npc_061#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=false)]
[name="玛莉娅"]  ——科瓦尔师傅！弗格瓦尔德师傅！
[Dialog]
[Character(name="avg_npc_107")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=60, fadeout=true, block=false)]
[name="光头马丁"]  请各位客人注意了，为了庆祝本店两位老顾客的优秀表现，今天的消费一律八折起！
[name="光头马丁"]  请各位立刻回到座位上点单！每种酒水小食限量销售，售罄为止！
[Character]
[name="游客"]  打折？还有这种好事？
[name="游客"]  等等......等等......那个光头大叔，难道是......
[Character(name="avg_npc_107")]
[name="光头马丁"]  只是老马丁而已，好了，要点什么？
[Character]
[name="游客"]  马丁......？真的是“颤铁”马丁......呜呜呜......今天真的太值了......给我一杯“马丁特调”......
[Dialog]
[Charact

... (全文14423字符)
```

### level_act13d5_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 5下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人恰尔内"]  骑士竞赛，到底是什么？
[name="发言人恰尔内"]  瑟奇亚克先生，您认为呢？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......别胡闹了，恰尔内，我很忙。
[name="塑料骑士"]  直接说，你要做什么？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  很遗憾......呼啸骑士团决定换下您的特锦赛首发阵容。那位新加入的援护骑士同样名列前茅，团体赛中，他的法术可以派上用场。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......
[name="塑料骑士"]  你......这和说好的不一样......
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  当然，允诺的定金还是会交付的。不过骑士团替补的税金是不一样的，你明白，对吧？
[name="发言人恰尔内"]  哎呀......别冲动，你的孩子马上就要过十岁生日，你没必要因为攻击一个微不足道的我而丢了工作......
[name="发言人恰尔内"]  呼啸骑士团付给你的钱依旧很多，至少今年，你无需再努力。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  我需要的是正赛名额！我......
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  这就看你自己的表现了，瑟奇亚克，总有办法活下去的，不是吗？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......
[name="塑料骑士"]  ......你说得对。
[name="塑料骑士"]  这种事情随便找个员工联系我就好，为什么要亲自来这里找我？发言人都这么闲的吗？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  啊......别误会，我也不是专程来找您的，我只是来确认一些赛事安排。
[name="发言人恰尔内"]  我们似乎有些太松懈了，各个赛区都出现了一些小小的问题，也给一些不法分子可乘之机。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  ......你是在威胁我？威胁“塑料”骑士瑟奇亚克帮你做脏活？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  哪里的话。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  你想要做什么？
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  我有两位在意的骑士需要迅速准备到时刻可以出场的状态......但遗憾的是，他们的积分明显还未够格。
[Character(name="avg_npc_106", name2="avg_npc_103", focus=2)]
[name="塑料骑士"]  呸......你们真想让骑士出线，有的是手段......
[Character(name="avg_npc_106", name2="avg_npc_103", focus=1)]
[name="发言人恰尔内"]  别这么说，偶尔也需要遵守规则，隐秘一些行事——
[name="发言人恰尔内"]  ——利用律法和违反律法完全是两回事，而其本质差异在于，当事人是否拥有这个本事。
[name="发言人恰尔内"]  只要您点头同意，积分转让的额外赛事和手续全部由我们安排。当然，这样一来您在呼啸骑士团内部的问题我也会稍加处理......
[name="发言人恰尔内"]  您意下如何？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  ——失效！踏步骑士的鞋底加速装置失去了作用！！骤然的减速让他猛然摔在了终点线前——！
[name="大嘴莫布"]  冲线——！！冠军是来自辉落骑士团的藤萝骑士！！而玛莉娅·临光紧随其后——斩获压线！
[name="大嘴莫布"]  而失去了鞋底加速的踏步骑士直接从第二位落后到了第七——！！真可惜啊踏步骑士！
[name="大嘴莫布"]  骑士装备的重要性不言而喻！
[name="大嘴莫布"]  而艾伦精选公司为各位提供全面的保养、维修、升级与设备安排管理，贴心的会员制度，为骑士们准备了无微不至的套餐！！
[Dialog]
[Character]
[Character(name="avg_npc_061#5",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  呼......亚军吗。
[name="玛莉娅"]  （这样......离特锦赛就更进一步了......）
[name="玛莉娅"]  （佐菲娅姑母......）
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_107#2")]
[name="光头马丁"]  噢，意料之外的客人。
[name="光头马丁"]  请找个位置随便坐。
[Dialog]
[Character]
[Character(name="avg_npc_103",fadetime=1,block=true)]
[delay(time=1)]
[name="塑料骑士"]  马丁......真的是你，过去大红大紫的骑士如今只开着这一家小酒吧？
[Character(name="avg_npc_103", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  老马丁早已经被剥夺了骑士身份，如今靠着积蓄混口饭吃，如此罢了。
[name="光头马丁"]  “塑料”瑟奇亚克是怎么找到这儿来的？不瞒你说，我这家酒吧很少迎接现役骑士。
[Character(name="avg_npc_103", name2="avg_npc_107", focus=1)]
[name="塑料骑士"]  现在的玛莉娅可是大红人，你的酒吧早就刊登在昨晚的娱乐新闻上了。
[name="塑料骑士"]  哼......大红人，一杯“红色雪绒花”。
[Character(name="avg_npc_103", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  这杯我请。
[Character(name="avg_npc_103", name2="avg_npc_107", focus=1)]
[name="塑料骑士"]  荣幸。
[Character(name="avg_npc_103", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  呼啸守卫的训练基地离这里可不算近，不会让你白跑一趟的。
[name="光头马丁"]  那么，来到之前对手的大本营，是为了来刺探军情，好在特锦赛上报一箭之仇的吗？
[Character(name="avg_npc_103", name2="avg_npc_107", focus=1)]
[name="塑料骑士"]  ......我不会在特锦赛登场。
[Character(name="avg_npc_103", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  嚯......呼啸守卫的决定？我以为你和赞助商的私人关系还不错。
[Character(name="avg_npc_103", name2="avg_npc_107", focus=1)]
[name="塑料骑士"]  哈，私人关系，和企业谈关系，就像和天灾谈恋爱。
[name="塑料骑士"]  当然，做决定的是更上面一层......
[Character(name="avg_npc_103", name2="avg_npc_107", focus=2)]
[name="光头马丁"]  骑士协会？
[Character(name="avg_npc_103", name2="avg_npc_107", focus=1)]
[name="塑料骑士"]  不止......比如，商业联合会。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=2)]
[name="光头马丁"]  唔。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=1)]
[name="塑料骑士"]  我知道你想说什么，老马丁，你在想“一个区区塑料骑士怎么会把事情变这么大条的”。
[name="塑料骑士"]  我还是有自知之明的，没有人会为了一个懂得听从安排的骑士做到这个地步，所以问题出在别的地方。
[name="塑料骑士"]  坊间流传着始终一个说法，耀骑士并不是感染者，她被逐出卡西米尔这件事，也没有那么简单......
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=2)]
[name="光头马丁"]  我毫不知情。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=1)]
[name="塑料骑士"]  别这么警惕......我没有在打探你的意思，老马丁。
[name="塑料骑士"]  我只是想让恰尔内知道，戏弄贵族是要付出代价的......而我想玛莉娅·临光应该也在他的视野之内，不是吗？
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=2)]
[name="光头马丁"]  ......骑士联手起来向协会抗议？这种事情总没有好下场。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=1)]
[name="塑料骑士"]  我只是不想任人宰割。
[name="塑料骑士"]  谢谢你的酒......老马丁，多嘴一句......我年轻时候，是看了你的比赛才决定成为骑士的。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=2)]
[name="光头马丁"]  看来你选错路了。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=1)]
[name="塑料骑士"]  没有，这不是刚准备自己踩出一条路来吗？
[name="塑料骑士"]  下次再见，老马丁。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=2)]
[name="光头马丁"]  瑟奇亚克，最后劝你一句......小心些。
[Character(name="avg_npc_103", name2="avg_npc_107#2", focus=1)]
[name="塑料骑士"]  ......哼，骑士从不需要在那些商贩面前低头，呼啸骑士团会同意我的看

... (全文12251字符)
```

### level_act13d5_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 6上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.4)]
[Character(name="avg_npc_061#7",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  光劝别人酒，你自己呢，这才第几杯！？
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  老东西别嚷嚷，我凭本事转移的火力——
[delay(time=0.6)]
[Character(name="avg_npc_061#7", name2="avg_npc_101", focus=2)]
[name="老工匠"]  ——丫头？
[name="老工匠"]  脸色怎么这么差，还没和佐菲娅和好呐？
[Character(name="avg_npc_061#7", name2="avg_npc_101", focus=1)]
[name="玛莉娅"]  没事的......姑母她有来过吗？
[Character(name="avg_npc_107", name2="avg_npc_061#7", focus=1)]
[name="光头马丁"]  直到刚才她都在门口打转，不过现在已经回去了，她很担心你。
[name="光头马丁"]  你应该去找她。
[Character(name="avg_npc_107", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  ......
[name="玛莉娅"]  下一场比赛的对手已经决定好了。
[name="玛莉娅"]  如果我能赢的话，姑母......大家是不是就能理解我了？
[Character(name="avg_npc_061#2", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  丫头......
[Character(name="avg_npc_120#3", name2="avg_npc_061#2", focus=1)]
[name="老骑士"]  .....没有那么简单，玛莉娅。
[Character(name="avg_npc_120#3", name2="avg_npc_101#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  喂！老糊涂，你胡扯什么呢！？
[Character(name="avg_npc_120#3", name2="avg_npc_061#7", focus=1)]
[name="老骑士"]  佐菲娅不是因为觉得你一定会输或者一定会受伤才不愿意你继续向特锦赛挺进的......
[name="老骑士"]  骑士竞技没有一丝一毫称得上公平公正的地方，一旦踏足更高的领域，你要面对的就不只是对手......
[name="老骑士"]  而是企业，企业和企业的博弈，家族和家族的斗争。
[name="老骑士"]  就算是监正会也完全插不上手，骑士协会、大骑士长和董事们三方的权利归属比想象中混乱得多。
[Character(name="avg_npc_120#3", name2="avg_npc_061#7", focus=2)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_120#3", name2="avg_npc_061#7", focus=1)]
[name="老骑士"]  当然，我不是劝你放弃，玛莉娅。
[name="老骑士"]  “看清苦难再向前冲锋”，认识到这一切，然后打倒它们给我们这些老家伙看看。
[Character(name="avg_npc_120#3", name2="avg_npc_061#5", focus=2)]
[name="玛莉娅"]  ......嗯！
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=0.6)]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_107")]
[name="光头马丁"]  有新的客人——
[Character(name="avg_npc_107#2")]
[name="光头马丁"]  ——
[name="光头马丁"]  ——这里不欢迎你，请离开。
[Dialog]
[Character]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=2)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[name="发言人恰尔内"]  别这么说，老朋友，颤铁骑士。
[name="发言人恰尔内"]  您的牺牲为我们带来了旷日持久的热度，我很尊敬您在赛场上的气质。
[Character(name="avg_npc_120#3")]
[name="老骑士"]  你是什么人？
[Character(name="avg_npc_106")]
[name="发言人恰尔内"]  ......二阶骑士弗格瓦尔德......退役的二阶骑士。或者该称呼你巴特巴雅尔？我不知道是不是这样发音......
[Character(name="avg_npc_101#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老工匠"]  喂——
[Character(name="avg_npc_106#2")]
[name="发言人恰尔内"]  哦，别，别这么剑拔弩张，我可不是骑士，只是个勤勤恳恳的文职人员......
[Character(name="avg_npc_120#3", name2="avg_npc_107#3", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="光头马丁"]  冷静点！弗格瓦尔德！
[Character(name="avg_npc_120#3", name2="avg_npc_106", focus=1)]
[name="老骑士"]  ......如果我的弓在手边，你绝对不敢这么和我说话。
[Character(name="avg_npc_120#3", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  看来是我失言了，如果冒犯到您，我深感抱歉。
[Character(name="avg_npc_107#2", name2="avg_npc_106#3", focus=1)]
[name="光头马丁"]  别整那套阳奉阴违的态度，你来这里是做什么的？
[Character(name="avg_npc_107#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  ......我只是一介员工，自然是来向玛莉娅·临光小姐传达骑士协会的安排。
[Character(name="avg_npc_106")]
[name="发言人恰尔内"]  玛莉娅小姐？
[Dialog]
[Character]
[Character(name="avg_npc_061#5",fadetime=1,block=true)]
[delay(time=0.6)]
[name="玛莉娅"]  啊.....呃，我在......
[Character(name="avg_npc_061#5", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  您的下一场比赛已经安排好了。
[Character(name="avg_npc_107#2", name2="avg_npc_106", focus=1)]
[name="光头马丁"]  ......这根本不需要你亲自来。
[Character(name="avg_npc_107#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  没错，但是我比较喜欢亲身躬行，这样才能确切理解到工作环节上的种种问题......当然，也有一些私心。
[name="发言人恰尔内"]  对于耀骑士玛嘉烈·临光的妹妹，如今风头正兴的年轻骑士，我也难捺好奇心啊。
[name="发言人恰尔内"]  许多有望进入特锦赛的种子选手如今的人气都不如玛莉娅小姐您。这也是您身为竞技骑士实力的一部分，这是您的优势。
[name="发言人恰尔内"]  希望您合理利用您的优势，当然，我这里也有许多......优质的商业合同。
[name="发言人恰尔内"]  比起那些私下找到您的赞助商，我保证这里全部都是一些超过你想象的骑士团加盟和大企业......
[Character(name="avg_npc_107#2", name2="avg_npc_106", focus=1)]
[name="光头马丁"]  ......我们已经听厌了你们的推销，玛莉娅有她自己的想法。
[Character(name="avg_npc_120#2", name2="avg_npc_106", focus=1)]
[name="老骑士"]  没错！你们这种践踏荣耀的行为简直就是对骑士的亵渎！
[Character(name="avg_npc_106")]
[name="发言人恰尔内"]  荣耀？啊......对，荣耀。
[name="发言人恰尔内"]  征战骑士们在边疆要塞戍守黎明，各个身价的竞技者也在为卡西米尔创造利益——
[name="发言人恰尔内"]  荣耀，荣耀在哪里？它消失了吗？
[Character(name="avg_npc_106#3")]
[name="发言人恰尔内"]  不。
[name="发言人恰尔内"]  没有谁能把荣耀驱逐出卡西米尔，就算卡西米尔大小千百家企业联合起来也做不到。
[name="发言人恰尔内"]  那是骑士们沦为战争的工具，被利益蒙蔽了双眼？是骑士们自己放弃了荣耀，忘记了过往？
[name="发言人恰尔内"]  也不对，那样也太小看骑士们了，连董事们都不敢妄言骑士已经沦为傀儡，我们又凭什么为欣欣向荣的骑士竞技感到悲哀？
[Character(name="avg_npc_120#2", name2="avg_npc_106", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老骑士"]  呸！你这种人根本不配谈论荣耀！
[name="老骑士"]  现在的卡西米尔根本不明白过去的——
[Character(name="avg_npc_120#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  ——过去的荣耀，骑士精神，啊——形而上的伟大灵魂！历史虚空中的太阳！
[name="发言人恰尔内"]  我说的对吗？可是观众和游客们并不需要精神，而我们也从来不需要把精神展现给他们。
[Character(name="avg_npc_120#3", name2="avg_npc_106", focus=1)]
[name="老骑士"]  油嘴滑舌......我现在就能撕烂你的脸。
[Character(name="avg_npc_120#3", name2="avg_npc_106#2", focus=2)]
[name="发言人恰尔内"]  哦，别这么急躁。荣耀，对，它很好，它无懈可击，它依旧存在于每一个骑士家族的徽记之上——
[Character(name="avg_npc_120#3", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  ——但可惜的是，卡西米尔人不再需要它了。
[name="发言人恰尔内"]  没有被抛弃，没有被淹没，它们一直都在，只是现代人......不需要了。
[name="发言人恰尔内"]  连抛弃都算不上，朋友。当你买了全新的城际网络数字电视，把一台老旧的收音机收进橱柜，这算“抛弃”吗？
[Character(name="avg_npc_120#3", name2="avg_npc_106",

... (全文12380字符)
```

### level_act13d5_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 6下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人恰尔内"]  前一任白金大位对目标暗生情愫，为了保护他的意中人而死在了其他无胄盟成员的手上。
[name="发言人恰尔内"]  结果而言，如今的这位小姑娘被匆匆推上了这个位置，“最年轻的白金”。
[name="发言人恰尔内"]  ......虽然的确是天才般的射手，真要论实力倒也不至于才不配位......不过其他方面远不如其他大位成熟。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  是、是这样......您为什么要和我说这些？无胄盟的存在应该是个机密......您该不会......
[Character(name="avg_npc_109#2", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  哦，别这么想，只是我最近时常在回想这件事。如果我没有努力到今天这个位置，我连思考这件事的权力都没有。
[name="发言人恰尔内"]  你知道吗？最后推举如今的白金成为白金的，正是濒死前的上一任白金。
[name="发言人恰尔内"]  这就很耐人寻味了......且不说为什么无胄盟要听一个叛徒的话，何况推举这个小姑娘也改变不了他的死局，他为什么要这么做？
[name="发言人恰尔内"]  在他被同僚的弓箭贯穿胸膛之前，他是不是想过要嘶吼什么呢？对谁？说什么？他想做到什么？只是那么简单吗？
[Character(name="avg_npc_109#3", name2="avg_npc_106#3", focus=1)]
[name="企业员工"]  ......
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  我记得您是斯沃玛公司的员工，对吧？
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  是、是的......赛事期间，我负责和其他各大公司以及骑士协会交接任务......
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  跑腿活，很辛苦。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  没有的事，能为企业做出贡献，是我应该做的——
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  不不不，你的工作是为你的薪水准备的，别说这么卑微的话。
[name="发言人恰尔内"]  你曾经似乎有过创业的记录，为什么没有坚持到底呢？
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=1)]
[name="企业员工"]  啊......那是因为我能力不足......
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  决定成败的也许不只是能力。你可能选错了路，否则你也许会和我平起平坐。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  就、就我这种人......
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  在卡西米尔，皆有可能。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_064_weapon_1#6",fadetime=1,block=true)]
[delay(time=1)]
[name="佐菲娅"]  ......
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="光头马丁"]  佐菲娅......很久没看见过你了。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  马丁叔......
[name="佐菲娅"]  ......玛莉娅她来过吗？
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="光头马丁"]  出了点事情，我们让她回家里去了。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  是这样——
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ——有血的味道，等等，这些绷带是怎么回事？
[name="佐菲娅"]  玛利亚受伤了？她的对手是谁？发生了什么！？
[name="佐菲娅"]  我都让她不要急着继续参赛，这个丫头怎么就——
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  冷静点，受伤的是另一个孩子。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......怎么回事？
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  灰毫骑士和焰尾骑士遭到了某些人的袭击......灰毫负了伤，她们恰好躲避到了这里。
[name="光头马丁"]  今天早上，她们说着不想再给临光添麻烦之类的话就离开了。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......会有这么巧的事情吗？
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  她们的处境很危险，但我们爱莫能助。
[name="光头马丁"]  看了今早上的新闻了吗？
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......
[name="佐菲娅"]  玛莉娅现在在做什么？
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  比赛。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  什么比赛？对手是谁？
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  和英格拉一样的无保护一对一，单挑赛。
[name="光头马丁"]  对手是“左手”泰特斯·白杨。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#2", focus=2)]
[name="佐菲娅"]  等等——谁？
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#2", focus=1)]
[name="光头马丁"]  锋盔骑士团主将，贵族骑士，高级商业骑士，曾到十六强止步的竞技骑士，泰特斯·白杨。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  可.....可是玛莉娅这个积分段无论如何也不会和他匹配到一起啊，他的身价甚至......
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  有人来找过玛莉娅，不是什么善茬。
[name="光头马丁"]  现在的她就像是过去的玛嘉烈一样，一门心思往前冲，她可不懂怎么和企业家们打交道。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  她......她和玛嘉烈一样吗？
[name="佐菲娅"]  玛嘉烈知道自己在做什么，她只是一厢情愿地笃定了自己的理想才变成那样的。
[name="佐菲娅"]  玛莉娅她都不清楚自己面对的是什么，也不知道该怎么做。再这样往上爬，实在是太危险了！
[name="佐菲娅"]  至少玛莉娅本来可以过上更轻松的生活......她不用变成你我这样的竞技骑士，不是吗？
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="光头马丁"]  也许你说的对，但是她是不是有自己的觉悟，你不该妄下判断。
[name="光头马丁"]  她还很年轻，也很不安，她那副轻松的态度也许都只是为了让你安心。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  ......
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="光头马丁"]  虽然玛莉娅经常表现出不成熟的样子，但是哪一个没有斗志的人能够战胜塑料骑士，能和锈铜打成平手，还能在混战赛上夺得第三？
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  也许她应该输一场，清醒一下。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  如果你真的这么想的话。
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  ......
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......哪座竞技场？
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
[PlaySound(key="$livecrowd",

... (全文12962字符)
```

### level_act13d5_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 7上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="avg_npc_064_weapon_1#6")]
[name="佐菲娅"]  ......比赛已经开始了。
[name="佐菲娅"]  必须......嗯？
[name="佐菲娅"]  喂，我的剑为什么会在这里？
[Character]
[name="仆人"]  啊，是玛莉娅小姐之前送过来的。
[name="仆人"]  玛莉娅小姐还说，已经帮您调整好了武器的状态，保证焕然一新。
[Character(name="avg_npc_064_weapon_1#5")]
[name="佐菲娅"]  ......
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=30, fadeout=true, block=false)]
[name="仆人"]  呀——！
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  喔......这么轻盈，真怀念这个手感。
[Character]
[name="仆人"]  请、请小心一点！哎呀，您又把栏杆弄坏了！去年才让石雕匠改建的维多利亚石柱风格......
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  那就索性让人把宅子全部翻新一遍好了，你来负责吧。
[Character]
[name="仆人"]  欸、又这么随意？
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  能住人就行......
[Character(name="avg_npc_064_weapon_1#6")]
[name="佐菲娅"]  ......
[Character]
[name="仆人"]  小姐？
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  ......啊，没事，我只是......突然感到有些怀念。
[name="佐菲娅"]  这把剑......是玛莉娅的爷爷送给我的。
[Character]
[name="仆人"]  玛莉娅小姐喊您姑母呢。
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  真要论辈分的话可混乱了。我还记得玛嘉烈是怎么说的——“这是你的......你的......你就喊姑母吧。”
[name="佐菲娅"]  我明明和她们两差不多大吧？居然喊姑母？
[Character]
[name="仆人"]  您还很年轻，而且这么年轻就有这份家业，我们也为您自豪，佐菲娅小姐。
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  一口气买下这么大的宅邸，那时候我是不是也想着证明自己，证明自己配得上那个“临光”的名号，配得上耀骑士呢......
[name="佐菲娅"]  不......现在不是怀念过去的时候。
[Character]
[name="仆人"]  车已经为您备好了，还是说，您觉得自己跑过去更快？
[Character(name="avg_npc_064_weapon_1")]
[name="佐菲娅"]  那当然是——
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[name="大嘴莫布"]  如同戏耍猎物的猎手，左手骑士一次次给予对手重整旗鼓的机会，再一次次击垮玛莉娅·临光！
[Character(name="avg_npc_107#2")]
[name="光头马丁"]  ......
[Dialog]
[PlaySound(key="$rungeneral", volume=0.6)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=50, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_107#2", name2="avg_npc_120#2", focus=2)]
[name="老骑士"]  马丁！我们回来了，现在是什么情况！？
[Character(name="avg_npc_107#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  为什么玛莉娅会和那种级别的对手交战啊？骑士协会都疯了吗！？
[Character(name="avg_npc_107#2", name2="avg_npc_101#2", focus=1)]
[name="光头马丁"]  这说来话长......那几个孩子安全了吗？
[Character(name="avg_npc_107#2", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  暂时安全了，只能这么说，现在他们已经被剥夺合法骑士身份了，呸。
[Character(name="avg_npc_120#3", name2="avg_npc_101#4", focus=1)]
[name="老骑士"]  我从来没想过事情会夸张成这样......
[name="老骑士"]  灰毫，焰尾，还有另外两个没有封号的感染者骑士，以及他们花所有资产从竞技场里买回来的感染者......
[Character(name="avg_npc_120#2", name2="avg_npc_101#4", focus=1)]
[name="老骑士"]  那些斗士，那些供人取乐的感染者都是些孩子！最大的不过二十来岁，最小的才——！
[Character(name="avg_npc_107#2", name2="avg_npc_120#2", focus=1)]
[name="光头马丁"]  ......
[Character(name="avg_npc_107#2", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  就算躲藏在那些管道之间，只要一天不离开这座城邦，就谈不上什么安全，而且人数很多。
[Character(name="avg_npc_120#3", name2="avg_npc_101#4", focus=1)]
[name="老骑士"]  我的老朋友会照顾他们的，但他们毕竟是感染者，事情不会这么简单。
[Character(name="avg_npc_120#3", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  ......这下我们可不光在和企业叫板了。
[Character(name="avg_npc_120", name2="avg_npc_101#4", focus=1)]
[name="老骑士"]  怕了？
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  怕！？乌萨斯人把长枪塞我嘴里的时候我都没怕过！毕竟我也是乌萨斯！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  放屁，工匠团什么时候离开过城头？
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  啊啊！？大铁匠铺被投石机炸烂的时候，我们不冲上去难道要在屋里等死吗？
[Character(name="avg_npc_107#3")]
[name="光头马丁"]  ......
[name="光头马丁"]  ......玛莉娅不能赢。
[Character(name="avg_npc_107#3", name2="avg_npc_120#3", focus=2)]
[name="老骑士"]  唉，现在的玛莉娅遇到这样的对手，的确赢不了啊。
[Character(name="avg_npc_107#3", name2="avg_npc_120", focus=1)]
[name="光头马丁"]  不对，不是赢不了，是不能赢。
[Character(name="avg_npc_107#2", name2="avg_npc_120", focus=1)]
[name="光头马丁"]  骑士协会太过大张旗鼓了，加上之前冒出来的那个恰尔内，事情不会那么简单。
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$batmeeting_intro", key="$batmeeting_loop", volume=0.4)]
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  唔......！
[name="玛莉娅"]  （胳、胳膊快要脱臼了......他的枪，完全没法近身——）
[name="玛莉娅"]  （——不，就算近身了也赢不了......怎么办......）
[Character(name="avg_npc_105")]
[name="左手骑士"]  ......起来。
[name="左手骑士"]  继续。
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  （咬牙起身）唔......
[Character(name="avg_npc_105")]
[name="左手骑士"]  这就摇摇欲坠了吗？真是像极了你那苟延残喘的“骑士家族”。
[name="左手骑士"]  起来，继续。消灭一个骑士最好的办法，就是消灭他们的尊严。
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  挑衅！三番五次的挑衅！以胜利者的睥睨敌手！“左手”泰特斯，真是令人生畏！
[name="大嘴莫布"]  现在奖池已经完全一边倒了，惊人的比例和数字！这个金额，恐怕相当于此时此刻全卡西米尔的竞技场金额之和！
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[name="男游客"]  喂！加把劲啊临光！万一你爆冷了，我赢的钱就够买下一座城堡了啊！
[name="女游客"]  你疯了吧？你给她下了多少钱？？
[name="男游客"]  ——我投给左手的钱更多！不过这样完全赚不到啊，还是对冲投资了一点！
[Dialog]
[Character(name="avg_npc_105")]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, b

... (全文12478字符)
```

### level_act13d5_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 7下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$exciting_intro", key="$exciting_loop", volume=0.4)]
4:12 P.M.  天气/阴  卡西米尔炎刃竞技场
独立骑士玛莉娅·临光与“左手”泰特斯·白杨的比赛开始一小时二十七分钟后
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  这可真是......赛场上难得一见的场面——！
[name="大嘴莫布"]  一次次被击倒却又一次次爬起来，各位观众眼中的那点光芒从未消散！简直就像扎根在竞技场沾满污血的泥土上一样！
[Character(name="avg_npc_121#3")]
[name="大嘴莫布"]  真的就是那么一点光芒——！就像晚上点亮的蜡烛！在泰特斯渐猛的攻势下，在最擅长瓦解斗志的泰特斯的攻势下——
[Character(name="avg_npc_121#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="大嘴莫布"]  ——至今没有熄灭！！
[Dialog]
[Character]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character(name="avg_npc_061#6",fadetime=1,block=true)]
[delay(time=2)]
[name="玛莉娅"]  哈啊......哈啊......
[Character(name="avg_npc_105")]
[name="左手骑士"]  你......又站起来了。你......
[name="左手骑士"]  是这样，用最微小的法术治愈伤口，避免消耗，观察弱点——
[name="左手骑士"]  ——长时间让肉体情况保持在崩溃边缘的感觉，好受吗？
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  哈......哈......不，还好吧......
[Character(name="avg_npc_105")]
[name="左手骑士"]  嘴硬。
[Dialog]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[delay(time=1)]
[name="左手骑士"]  只是些小聪明罢了。
[Character]
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[Character(name="avg_npc_121#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="大嘴莫布"]  挡——挡下了！从目前为止第一次！玛莉娅挡住了泰特斯的攻击！
[Character(name="avg_npc_105")]
[name="左手骑士"]  什......我刺偏了......？
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  不，正中红心.....只是力道，弱了不少。
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  你.....你原来也会累啊，泰特斯......
[Character(name="avg_npc_105")]
[name="左手骑士"]  我？
[name="左手骑士"]  ......
[delay(time=1)]
[Character(name="avg_npc_105")]
[name="左手骑士"]  的确......我为你浪费了太多时间。
[name="左手骑士"]  该结束了。
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.3, block=false)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[Character(name="avg_npc_061#3")]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=0.6)]
[Character(name="avg_npc_105")]
[Character]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character]
[name="游客"]  又是一击——！
[name="游客"]  气势完全不一样啊......再怎么这也......
[Character(name="avg_npc_061#6")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  咕哈......
[Character(name="avg_npc_105")]
[name="左手骑士"]  哼，既然知道了你的小动作，没理由继续给你机会了。
[Character(name="avg_npc_061#6")]
[name="玛莉娅"]  （来不及——）
[Dialog]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=0.6)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_121")]
[name="大嘴莫布"]  连！续！追！击！
[name="大嘴莫布"]  不再给小临光任何喘息机会的追击！！那点精疲力竭的光芒是否会就此熄灭！？
[Dialog]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Character]
[name="游客A"]  那个女孩......还能撑得住？这种比赛好没意思，我已经看腻了啊......
[name="游客B"]  ......那个人，是玛莉娅·临光吧......是上上届冠军的妹妹？
[name="游客A"]  是吗，我前两年来卡西米尔看过特锦赛，完全不是一个水平啊。
[name="游客B"]  但你不觉得绝地翻盘才有看头吗？
[name="游客A"]  可是......
[Character(name="avg_npc_064_weapon_1#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="佐菲娅"]  玛莉娅！
[name="佐菲娅"]  玛莉娅！站起来！
[Character]
[Dialog]
[stopmusic(fadetime=3)]
[Character(name="avg_npc_061#6",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  ......
[Character]
[Dialog]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
视线很模糊。
不能眨眼，玛莉娅。
闭上眼就睁不开了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
玛莉娅，你有一双天马的眼睛。
玛莉娅，站起来，来，过来。
[Dialog]
[Character(name="avg_npc_061#7",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  爷爷......
[Dialog]
[Character]
别哭，孩子。
临光家的家训是什么？
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  “不畏苦暗”......
[Dialog]
[Character]
我不为过去而后悔，我也很高兴玛嘉烈选择了另一条道路。
[Character(name="avg_npc_061#4")]
[name="玛莉娅"]  姐姐......？
[Dialog]
[Character]
如何直面痛苦和黑暗，代代族人都做出了自己的选择。
玛嘉烈她选择了最不现实的道路。
她.....你的姐姐有和你说过她对骑士的看法吗？
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  “所谓骑士，是照亮整片大地的崇高者”......
[Dialog]
[Character]
呵呵，她年纪轻轻......
就想成为光。
就想驱散苦暗。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(imag

... (全文25706字符)
```

### level_act13d5_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 8上
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_sportsbar",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  小队战？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  是二对二，很少见的赛制，原本为了凸显骑士团的分工，至少也该是三对三或者四对四的。
[name="佐菲娅"]  不过无论几对几，你是没有骑士团的，这就需要找个帮手了。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  欸......对手是谁？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  赛程表上写的是雪踵骑士团。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  ......有几个耍弓的好手，还有一个使流星锤的，不知道会遇上谁。
[name="光头马丁"]  玛莉娅的对手终于到了只要听名字就能知道是谁的地步了啊。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  欸哈哈......
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  也不知道是好事还是坏事......
[Character(name="avg_npc_107#2", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  玛莉娅，赢了泰特斯是一件值得高兴的事情，但也意味着更多的目光聚焦到了你的身上。
[name="光头马丁"]  有焰尾和灰毫的前车之鉴，切忌锋芒毕露。
[name="光头马丁"]  必要的时候委身于一些企业作妥协是很重要的，时代不比过去了，纯粹的胜利是带不回荣耀的。
[Character(name="avg_npc_107#2", name2="avg_npc_061#5", focus=2)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_107#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......上次你怎么不帮我劝她？
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  你摔门走了之后我可是好好和玛莉娅谈过心的——对了，上次你把我门砸坏了。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  呃。我会赔的......
[name="佐菲娅"]  老弗和科瓦尔呢？
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  今天是那个日子，还没回来。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  啊......扫墓日啊，糟，还想问问他能不能帮忙修补一下玛莉娅的装备......
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="光头马丁"]  借用一下他的工坊就是了。
[name="光头马丁"]  去年有天他喝醉了可是亲口说过，如果玛莉娅你有这个想法，他随时都愿意把他的工坊继承给你。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="玛莉娅"]  欸！？我怎么没听说过？
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  反正他已经发誓不再碰铁砧了。
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=2)]
[name="佐菲娅"]  唉......都这么多年了......
[Character(name="avg_npc_107", name2="avg_npc_064_weapon_1#6", focus=1)]
[name="光头马丁"]  谁都会对过去难以释怀，只不过我们这些老家伙只剩下过去了。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  那先别管他俩好了，玛莉娅，你得靠自己完成整备。
[name="佐菲娅"]  然后，关于队友的事情......你有人选吗？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  我？唔......
[name="玛莉娅"]  ......
[name="玛莉娅"]  我、我是不是其实没有什么骑士朋友？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  所以我有人选，从认识的人里找，总比到时候协会随便塞一个人给你要安全得多。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  呃，是谁？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  远牙骑士，是个弓弩高手。
[name="佐菲娅"]  和你一样，她从独立骑士打拼起，不愿意接受企业赞助，听说最近还打算建立一支完全自力更生的骑士团。
[name="佐菲娅"]  我想也许你们合得来，战术方面也能互相补缺，小队多人赛和混战赛或是单挑完全不同，到时候你就明白了。
[name="佐菲娅"]  本来有时间的话，你们应该在训练场上互相熟悉一下，不过时间紧迫，也许只能靠临时发挥了。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  ......好、好的。
[Character(name="avg_npc_107", name2="avg_npc_061#2", focus=1)]
[name="光头马丁"]  这就是独立骑士的劣势啊......临时搭伙对抗久经战阵的队伍，一定会处于劣势。
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  会是个什么样的人啊......稍微有点紧张呢......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_106",fadetime=1,block=true)]
[delay(time=1)]
[name="发言人恰尔内"]  这是我们今天第三次路过这片街道了。
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  啊，是的恰尔内先生......
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  你很习惯这样的工作，在各个竞技场间跑来跑去，参与无数的电话会议。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  啊、没有......我这样的人没有什么擅长不擅长的......
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  你的打扮的确邋遢了一点，仪表也是交涉的筹码，不是吗？
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  抱、抱歉......其实前不久我还是失业状态......所以......
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  哦......那有什么关系呢？
[name="发言人恰尔内"]  我并不讨厌你这样的员工，只有跌入谷底的人才会知道我们面临的一切有多么残酷，认识到之后，才能做出让人满意的决断。
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=1)]
[name="企业员工"]  ......
[Character(name="avg_npc_109#3", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  记住我说的每一句话，做的每一件事。
[Character(name="avg_npc_109", name2="avg_npc_106", focus=1)]
[name="企业员工"]  欸？啊，是要做和雪踵骑士团的会议记录吗，没问题，我准备——
[Character(name="avg_npc_109", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  不不不，他们的赞助商是我的老朋友了，不会有什么麻烦事的。
[name="发言人恰尔内"]  只是为了我个人微不足道的......工作方式。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  ......玛莉娅。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  嗯？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  其实从一开始，我就不是非常同意你参加骑士竞技。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=1)]
[name="玛莉娅"]  欸，嗯，怎么突然？这个我还是感觉得到啦。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1#5", focus=2)]
[name="佐菲娅"]  但是你证明了自己。
[Character(name="avg_npc_061#2", name2="avg_npc_064_

... (全文30066字符)
```

### level_act13d5_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 8下
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
观众席上有一位老人。
这位老人对骑士竞技半点不感兴趣，但为了讨孙子的欢心，他还是托人买了两张票，来看这场在报纸和电视里被大肆宣传的比赛。
他皱眉，他感叹，他不知为何，这种萨卡兹人对年轻库兰塔的当众处刑能够受到欢迎。
他并没有觉得哪里是错的，因为他也是一名骑士，没有贵族地位的征战骑士。他只是在唾弃这场比赛，或者是萨卡兹人。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
但是场上突然亮起了光芒，老人想起了，这个骑士是临光家的小女儿。
真可惜啊，他这样感慨道，然后注视着那道光。在他注视着光芒的同时，观众席上极少数的卡西米尔人，同时想起了一个故事。
故事发生在林河湖畔之外，要塞与城墙组成的卫戍之地。
每逢黑夜降临，炬火连成一片，征战骑士的盔甲在月光下熠熠生辉，银枪的锋刃指向黑暗中蠢蠢欲动的敌人。
那些无情的侵略者，使得天空变色的莱塔尼亚人遮蔽了月光，乌萨斯骇人的军队碾过了城墙。
数座城邦被屈辱地带往乌萨斯的国境，防线一退再退，“银枪”成了那些战争贩子嘲弄骑士的一个笑话。
直到退无可退的城邦外围，直到荒芜疆土上最后的防线——
——在卡西米尔最后的阵地，出现了一位金发的老天马。
乌萨斯人在战争中首次败退的那个黎明，卡西米尔遥远的地平线上，升起了两个太阳。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
光。
光没有消散，光雾弥漫，将恐惧驱逐。
此时此刻，太阳也已颔首，迎接这位归乡的骑士。
......
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
......
......玛莉娅。
站起来，玛莉娅。
[dialog]
[Character(name="avg_npc_061#6",fadetime=1,block=true)]
[delay(time=2)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_061#5")]
[name="玛莉娅"]  ......姐姐？
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_light",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
玛莉娅。
你长大了，你做得很好。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_106#2")]
[name="发言人恰尔内"]  不......那不是玛莉娅的法术......
[name="发言人恰尔内"]  发生了什么？
[Character(name="avg_npc_109#2", name2="avg_npc_106#2", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="企业员工"]  恰尔内先生！刚才我们接到了——无胄盟守卫的通知！有一道光从竞技场西北方向一公里处撞进了竞技场！
[name="企业员工"]  速度很、很快！而且根本看不清那到底是什么！
[Character(name="avg_npc_109#2", name2="avg_npc_106#2", focus=2)]
[name="发言人恰尔内"]  ......恐怖袭击？
[Character(name="avg_npc_109#2", name2="avg_npc_106#2", focus=1)]
[name="企业员工"]  不、不像是武器，是一个人，是一个库兰塔，但是这种速度，只可能是最顶级的骑士——
[Character(name="avg_npc_109#2", name2="avg_npc_106#2", focus=2)]
[name="发言人恰尔内"]  ......
[name="发言人恰尔内"]  ......不。
[delay(time=1)]
[Character(name="avg_npc_106#2")]
[name="发言人恰尔内"]  这不可能......光芒......难道......
[stopmusic(fadetime=1)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_bat_game02_intro", key="$m_bat_game02_loop", volume=0.4)]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[Character]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[Blocker(a=0, fadetime=1.5, block=false)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[Blocker(a=0, fadetime=1.5, block=false)]
[Character(name="avg_npc_102", name2="avg_npc_102_2", focus=2)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="腐败骑士"]  嘎.......敌人在哪儿？光太亮，看不清......！
[Character(name="avg_npc_102", name2="avg_npc_102_2", focus=1)]
[name="凋零骑士"]  任务，就要执行到底。不管是谁——先杀了目标！
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_102", name2="avg_npc_102_2", focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="腐败骑士"]  嘎啊......！
[name="腐败骑士"]  竟然.....用拳头就能让我双脚离地......？什么人？
[Dialog]
[Character]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="char_148_nearl_1#3",fadetime=1,block=true)]
[delay(time=2)]
[name="玛嘉烈"]  肮脏的法术......备受折磨的萨卡兹感染者，“骑士”怎该是这副模样？
[Character(name="avg_npc_102_2",fadetime=1,block=true)]
[delay(time=2)]
[name="腐败骑士"]  嘎......
[Character(name="avg_npc_061#2")]
[delay(time=1)]
[name="玛莉娅"]  姐姐......？
[Character(name="avg_npc_061#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="玛莉娅"]  等等......真的是姐姐？我没有昏过去看到幻觉吗......？
[Character(name="avg_npc_061#2", name2="char_148_nearl_1#6", focus=2)]
[name="玛嘉烈"]  嗯。
[Character(name="avg_npc_061#2", name2="char_148_nearl_1#6", focus=1)]
[delay(time=1)]
[name="玛莉娅"]  ......
[Character(name="avg_npc_061#2", name2="char_148_nearl_1#6", focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="玛莉娅"]  真、真的......？
[Character(name="avg_npc_061#2", name2="char_148_nearl_1#6", focus=2)]
[name="玛嘉烈"]  嗯。
[Characte

... (全文41413字符)
```

### level_act13d5_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 纯1
[stopmusic]
[Dialog]
[Delay(time=1)]
[playMusic(intro="$relax_intro", key="$relax_loop", volume=0.4)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
4:12 P.M.  天气/晴     
卡西米尔中部，四城联合，“大骑士领”卡瓦莱利亚基
某处不堪入目的车祸现场
[Dialog]
[Character(name="avg_npc_120",fadetime=1,block=true)]
[delay(time=1)]
[name="老骑士"]  啊......我们还赶得上晚上的酒会不？
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  赶不上也是你的错，老弗。
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  我的错？哈！我的错？
[name="老骑士"]  你非要带着你的破箱子，足足三十公斤！你是嫌自己不够胖吗？
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  这是帮马丁修东西的工具！好，所以这就是你撞在树上的借口？
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  不要质疑我的方向感！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  我说的是你老眼昏花......
[Character(name="avg_npc_120#3", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  你忘了上星期我是怎么夺得酒吧飞镖冠军的吗？你瞎了我都不会眼花的。
[Character(name="avg_npc_120#3", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  我瞎不了，所以我清清楚楚提醒过你，“前面那有棵树”。
[Character(name="avg_npc_120#3", name2="avg_npc_101#4", focus=1)]
[name="老骑士"]  我怎么不记得？
[Character(name="avg_npc_120#3", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  因为音响的声音太大了！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  那是谁把塞壬的新碟放进去的？
[Character(name="avg_npc_120#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  ......别嚷嚷，让丫头专心检查！
[Dialog]
[Character]
[Character(name="avg_npc_061#2",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  唔啊......这撞得也太彻底了吧......
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  都怪老弗。
[Character(name="avg_npc_120", name2="avg_npc_061#2", focus=1)]
[name="老骑士"]  我......你......玛莉娅，少听他胡扯，这事儿真不能赖我。
[Character(name="avg_npc_120", name2="avg_npc_061#2", focus=2)]
[name="玛莉娅"]  行啦行啦，等我再检查一下，嘿咻——！
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  听见没？吵着丫头了，少说几句吧。
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  你！！
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  线路，OK，但发动机还没是有反应，唔，这是上上代的产品了吧，是这样驱动的吗......
[name="玛莉娅"]  引擎没有反应，那干脆手动法术点火试试......
[Character]
[Dialog]
[PlaySound(key="$b_char_defboost", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_061#2")]
[name="玛莉娅"]  ......是这样吧？
[Character(name="avg_npc_120", name2="avg_npc_101", focus=2)]
[name="老工匠"]  啧啧，每次看丫头捏着光的样子，都会让人想起她爷爷。
[Character(name="avg_npc_120#4", name2="avg_npc_101", focus=1)]
[name="老骑士"]  就是！瞅瞅人家玛莉娅！你怎么就屁点源石技艺不懂呢。
[Character(name="avg_npc_120#4", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  谁说我不会修源石装置的！？
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  我说的是——
[Character(name="avg_npc_061#2", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  玛莉娅！让让！今天我要让这个老家伙开开眼！
[Character(name="avg_npc_061#2", name2="avg_npc_101#4", focus=1)]
[name="玛莉娅"]  啊哈哈......二老就别闹了......
[Character(name="avg_npc_061#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玛莉娅"]  啊！有反应了！
[name="玛莉娅"]  这样......再这样......
[PlaySound(key="$b_char_defboost", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$motorbikestart", volume=0.6)]
[delay(time=1)]
[Character(name="avg_npc_120#4", name2="avg_npc_061#2", focus=1)]
[name="老骑士"]  哦哦！引擎声！我亲爱的引擎声！
[name="老骑士"]  玛莉娅是真的一天比一天厉害了，依我看，某个老头差不多也该正式退休了吧？
[Character(name="avg_npc_120#4", name2="avg_npc_061", focus=2)]
[name="玛莉娅"]  嘿嘿，没有的事啦，还不是科瓦尔师傅教得好嘛。
[Character(name="avg_npc_120#4", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  听见没！听见没！听——见——没！
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  嘁，别啰嗦，上车。
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=2)]
[name="老工匠"]  丫头，你接下来去哪儿？要不捎你一程？
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=1)]
[name="玛莉娅"]  我？
[Character(name="avg_npc_061#2", name2="avg_npc_101", focus=1)]
[name="玛莉娅"]  我......我接下来有别的事情啦。
[Character(name="avg_npc_120", name2="avg_npc_101", focus=1)]
[name="老骑士"]  那好吧。抓稳了，科瓦尔，今夜的第一杯酒必须得进我肚子！
[PlaySound(key="$motorbikestart", volume=0.6)]
[Character(name="avg_npc_120", name2="avg_npc_101#4", focus=2)]
[name="老工匠"]  那还用说——慢着，引擎的声音是不是有点——
[Character(name="avg_npc_120")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="老骑士"]  出发！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[PlaySound(key="$drift", volume=0.6)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$drift", volume=0.6)]
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  你干嘛还开那么快！？
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  我年轻时候的冲刺可比这还快！而且其实我没踩油门！
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  呃？等等，七十迈了，慢——慢点啊，喂，八十迈了！超速了！超速了！
[Character(name="avg_npc_120#2", name2="avg_npc_101", focus=1)]
[name="老骑士"]  慢不下来！我说了我没踩油门！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  那就——！刹车，刹车啊！
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$drift", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$d_sp_ballista")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_ballista")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[CameraShake

... (全文9007字符)
```

### level_act13d5_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 纯2
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  恰尔内先生，来质问的部门通讯一个接一个，我们完全顾不过来......！
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=2)]
[name="发言人恰尔内"]  想办法应付一下，至少让还能听得进话的人明白，“胜利”和“价值”不是同等的。
[Character(name="avg_npc_109#2", name2="avg_npc_106", focus=1)]
[name="企业员工"]  好、好的！
[Character(name="avg_npc_109#2", name2="avg_npc_106#3", focus=2)]
[name="发言人恰尔内"]  唉......
[Character(name="avg_npc_106#3", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  ......“左手”阁下，您真的不需要进一步的医疗检查？
[Character(name="avg_npc_106#3", name2="avg_npc_105", focus=2)]
[name="左手骑士"]  不必，能趁我施放法术前让我失去意识已是她的极限，想确实给我留下重伤，她还嫩了点。
[Character(name="avg_npc_106", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  恕我直言，这场比赛结果的确出乎了许多人的预料。
[Character(name="avg_npc_106", name2="avg_npc_105", focus=2)]
[name="左手骑士"]  哼......
[name="左手骑士"]  有没有这场无关紧要的胜利，我都会带着锋盔骑士团全员进入特锦赛。不劳发言人费心。
[Character(name="avg_npc_106", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  您很有自信，这就好。
[name="发言人恰尔内"]  如果您全力以赴，玛莉娅·临光不会有任何胜算，希望您能应付这次意外的失败带来的各种问题......
[Character(name="avg_npc_106", name2="avg_npc_105", focus=2)]
[name="左手骑士"]  我当然不会给自己找借口。
[Character(name="avg_npc_106", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  您会与很多巨额赞助无缘，也许您的骑士团那边——
[Character(name="avg_npc_106", name2="avg_npc_105", focus=2)]
[name="左手骑士"]  ——如果那些人还只能看见最表面的胜负而不懂得操作利益，那就是他们不配与我合作。
[Character(name="avg_npc_106#3", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  您说得对。
[name="发言人恰尔内"]  热度能转化成效益，客户们在意的本来就只是他们能看到的那部分，换言之，他们其实只在意一些感官刺激......而且从无自觉。
[name="发言人恰尔内"]  不过我没想到，泰特斯·白杨阁下居然也会将自己的“失败”明码标价......
[Character(name="avg_npc_106#3", name2="avg_npc_105", focus=2)]
[name="左手骑士"]  发言人，不要挑衅我的底线。
[Character(name="avg_npc_106#2", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  好、好、我很抱歉......等我们的小伙计处理完那些麻烦事，我们立刻就离开。
[Character(name="avg_npc_106", name2="avg_npc_105", focus=1)]
[name="发言人恰尔内"]  让我们在特锦赛上相见吧，“左手”阁下。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_courtyard",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_061#2",fadetime=1,block=true)]
[delay(time=1)]
[name="玛莉娅"]  是这样......原来索娜她们在做这种事......
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  感染者的斗士竞技场，我听说过这个赛制......不，这都算不上“赛制”。
[name="佐菲娅"]  无论是否是骑士家族出身，任何人都可以成为竞技骑士，并靠自己的本事赢得骑士协会的认可，从而跻身贵族行列......
[name="佐菲娅"]  但是感染者......
[Character(name="avg_npc_120", name2="avg_npc_064_weapon_1", focus=1)]
[name="老骑士"]  他们允许感染者参赛，但没有任何一个国家会坐视感染者成为社会的中流砥柱，所以他们区分了一个额外赛制。
[name="老骑士"]  感染者能赚到钱，能活命，但这辈子就会变成单纯的角斗士供人取乐......嘁，这种施舍根本没有意义。
[name="老骑士"]  哦，我没别的意思。
[Character(name="avg_npc_120", name2="avg_npc_101", focus=2)]
[name="老工匠"]  你这老东西，讲话就不能委婉一点吗？
[Character(name="avg_npc_120", name2="avg_npc_101", focus=1)]
[name="老骑士"]  现在委婉给谁看啊，他们都要杀到鼻子上来了！
[Character(name="avg_npc_120", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  虽然感染者的事情的确让人放不下心......不过现在不是担心她们的时候。
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=1)]
[name="玛莉娅"]  ......嗯。
[name="玛莉娅"]  她们靠着自己的实力改变了自己作为感染者的地位......但她们救下了很多的人。
[name="玛莉娅"]  如果我们要改变什么，我们就需要继续前进。
[Character(name="avg_npc_120", name2="avg_npc_061#2", focus=1)]
[name="老骑士"]  ......玛莉娅，已经变成能说出这种话的骑士小姐了......玛嘉烈要是看到了，一定会很欣慰的吧......
[Character(name="avg_npc_120", name2="avg_npc_101#2", focus=2)]
[name="老工匠"]  别把耀骑士说得像是死了一样，你这老家伙！
[Character(name="avg_npc_120#2", name2="avg_npc_101#2", focus=1)]
[name="老骑士"]  是你在曲解我的意思，科瓦尔！
[Character(name="avg_npc_061#7")]
[name="玛莉娅"]  ......
[delay(time=1)]
[Character(name="avg_npc_061#7", name2="avg_npc_064_weapon_1", focus=2)]
[name="佐菲娅"]  玛莉娅？怎么了？
[Character(name="avg_npc_061#2", name2="avg_npc_064_weapon_1", focus=1)]
[name="玛莉娅"]  没、没什么.....
[Dialog]
[Blocker(a=1, fadetime=1, block=true)]
[Character]
[Background]
[Image(image="ac13_1",x=-10,y=-10,xScale=1.1, yScale=1.1)]
[ImageTween(image="ac13_1",x=-10,y=-10,xScale=1.1, yScale=1.1,xTo=10,duration=40)]
[Blocker(a=0, fadetime=2, block=true)]
[delay(time=1)]
[name="白金"]  冠军墙啊......真是个一点都不适合聊天的地方。
[name="白金"]  ......历代冠军像啊，这个黑骑士姐姐占了整整三幅呢。
[name="白金"]  明明统治了特锦赛那么多年，一点看不出来变老......欸，不会吧，看着看着总觉得比我还年轻......
[name="发言人恰尔内"]  小姐说笑了。
[name="白金"]  这就是血统的优势吗，真好啊，真羡慕。
[name="发言人恰尔内"]  黑骑士在骑士竞技历史上留下了浓墨重彩的一笔，起初谁也没想到一个完全不懂得法术的莱塔尼亚人能变成今天的“黑骑士”。
[name="发言人恰尔内"]  不过她的时代早已过去......她也离开了卡西米尔。
[name="白金"]  你们居然会轻易放手这棵摇钱树哎。
[name="发言人恰尔内"]  ......具有统治力的冠军的确会引来不少崇拜者，但是过于膨胀的个人秀从长远看不利于整个竞技业的发展......
[name="发言人恰尔内"]  简单来说，虽然新的挑战者挑战黑骑士的确是卖点，但是连着三次都没能撼动她的胜利......就稍显无聊了。
[name="发言人恰尔内"]  黑骑士的末路不算太好，台面上暗地里想要排除她的人能挤满一座竞技场。
[name="发言人恰尔内"]  不过她运气不错，就在她穷途末路的时候，她遇到了谢拉格的一位大人物。
[name="发言人恰尔内"]  对方提出了一个还算不错的价格......让所有人接受了。
[name="发言人恰尔内"]  能合理地更新换代，也是竞技产业进步的体现。
[name="白金"]  ......然后就是这边，一个空位。
[name="白金"]  耀骑士吗。
[name="发言人恰尔内"]  是的，不用多说了吧。
[name="白金"]  这个人我知道，上一届的，血骑士。
[name="发言人恰尔内"]  血骑士的恐怖和强大是赛场上前所未见的，不过他倒是懂得审时度势，没有给我们添太多麻烦。
[name="白金"]  你们偶尔也该劝劝他，不要用药过度。骑士不是最贵重的商品吗？
[name="发言人恰尔内"]  谨记在心，小姐。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[name="白金"]  ......于是呢？商业联合会发言人邀请我来，总不能是聊历史的吧？
[name="发言人恰尔内"]  请原谅我选在这个地方，冠军墙将在特锦赛期间向客人们开放，我得提前视察一下现场。
[name="发言人恰尔内"]  当然，这也是少数能不被打扰和小姐谈话的地方。
[name="白金"]  唔......行啦，又是工作对吧，反正也跑不掉，我会听的。
[name="发言人恰尔内"]  也不止是工作......不知小姐可否知晓，青金大位的两人如今在做什么？
[name="白金"]  你没有那个权限哦。虽然我也没有。
[name="发言人恰尔内"]  我听说了一些有趣的小道消息......
[name="发言人恰尔内"]  不知道什么天大的事情，需要两位青金大位同时带队行动呢？
[name="白金"]  ——啊啊，我不想听，我什么都没听见。
[name="发言人恰尔内"]  小姐。
[name="白金"]  ......
[name="发言人恰尔内"]  我确认过其他几位负责人的全部申请，没有一件“大事”需要用得上青金大位的，何况还是两位。
[name="白金"]  这你就不用担心了，我只能保证这依旧是商业联合会的命令。
[name="发言人恰尔内"]  原来如此......那我就放心了。
[name="白金"]  ......对我真是毫无信任啊。
[name="发言人恰尔内"]  何出此言呐，小姐。
[name="白金"]  你明知道找我问上位者的事情是没有意义的，不就是想警告我这个“不成熟的白金大位”嘛，好啦好啦，我知道。
[name

... (全文12253字符)
```

### level_act13d5_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 卡西米尔 纯3
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_kxstreet",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Character(name="char_204_platnm_1",fadetime=1,block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget", volume=0.6)]
[name="白金"]  是我。发言人的事情已经结束了——
[name="？？？"]  ......白金大位。
[name="白金"]  .....您是谁？我联络的是董事......
[name="？？？"]  无妨，该终端的授权码你应该已经收到了。
[name="白金"]  既然知道这个频道，您也不是那两个青金大位，那么......
[name="？？？"]  你心里有数就行，不需要这么谨慎试探。
[name="？？？"]  接下来要说的是“无胄盟”之间的对话，和“董事们”没有关系。
[name="白金"]  ......好的。
[name="？？？"]  有一批征战骑士秘密越过了昏林边界，这件事绕过了商业联合会的眼，想必和耀骑士有关。
[name="白金"]  银枪的......？
[name="？？？"]  青金大位将会全权负责此事，你无须过问。
[name="白金"]  哈啊，他们最近这么认真工作的吗？
[name="？？？"]  你的任务是接替他们，监视耀骑士。
[name="白金"]  耀骑士吗......这也是个大麻烦啊。
[name="白金"]  ——所以其实那边的事态更麻烦？
[name="？？？"]  还不清楚。一石激起千层浪，耀骑士的回归给我们带来了很多麻烦......而且，我们都太把注意力放在她身上了。
[name="？？？"]  还有。
[name="？？？"]  无论如何，不要对耀骑士身边的萨卡兹出手。
[name="白金"]  关于那两位萨卡兹......您似乎知道很多。
[name="？？？"]  赦罪师和耀骑士，他们还同属于另一家“公司”。这件事会这么简单吗......我不确定。
[name="白金"]  ......
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[name="？？？"]  做好你自己的事情，别像之前一样搞砸了。
[name="？？？"]  会忙起来的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_arena_1",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$phonevibration",volume=0.6)]
[CameraShake(duration=1, xstrength=5, ystrength=3, vibrato=30, randomness=90, fadeout=true, block=true)]
[Character(name="avg_npc_109#3",fadetime=1,block=true)]
[delay(time=1)]
[name="企业员工"]  啊......又是电话......是找恰尔内先生的吗......
[name="企业员工"]  可是恰尔内先生......已经离开好久了。
[Character(name="avg_npc_109#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="企业员工"]  ......
[PlaySound(key="$d_gen_transmissionget", volume=0.6)]
[Character(name="avg_npc_109#3")]
[name="企业员工"]  ......喂？
[name="浑厚的男声"]  发言人吗。
[Character(name="avg_npc_109#3")]
[name="企业员工"]  啊，不，抱歉，恰尔内先生现在——
[Character(name="avg_npc_109#2")]
[name="企业员工"]  什、什么？
[name="浑厚的男声"]  我拨打的是发言人的号码，而你接起了电话。
[name="浑厚的男声"]  所以你就是发言人。
[Character(name="avg_npc_109#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="企业员工"]  呃？什、什么？我不懂——
[name="浑厚的男声"]  姓名。
[name="企业员工"]  我......？
[name="浑厚的男声"]  姓名。
[Character(name="avg_npc_109#4")]
[delay(time=1)]
[name="企业员工"]  呃，请叫我马克维茨，我之前为斯沃玛食品公司服务，直到恰尔内先生邀请我合作......
[name="浑厚的男声"]  ......
[Character(name="avg_npc_109#3")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="企业员工"]  先、先生？请问恰尔内先生他？
[name="豪迈的女声"]  您好，马克维茨先生。
[name="企业员工"]  啊，抱歉女士，我以为——
[name="豪迈的女声"]  我是斯沃玛食品公司董事长兼首席执行官，您应该听得出我的声音，发言人马克维茨先生，您被正式解雇了。
[Character(name="avg_npc_109#3")]
[delay(time=1)]
[name="企业员工"]  呃？
[name="豪迈的女声"]  从现在起，您既不属于斯沃玛食品公司，也不属于梅什科集团——请时刻记住，您代表商业联合会。
[name="豪迈的女声"]  等到赛事结束，您可以自由选择去留，根据您的表现，您会有丰厚的回报。
[name="豪迈的女声"]  现在，您有三个待办事项，而且没有提问的权利。
[name="豪迈的女声"]  第一，保证赛事继续顺利进行，这是重中之重。
[name="豪迈的女声"]  第二，对耀骑士及相关事件进行舆论引导，我们不需要任何“止损”，我们要求的是在那之上的“收益”。
[name="豪迈的女声"]  第三，无胄盟的接洽人员三分钟后就会抵达你所处的地点，监督他们做好各自的事情，任何异样皆直接向商业联合会暨董事会议汇报。
[Character(name="avg_npc_109#2")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="企业员工"]  等等......！我并不想变成......！
[name="豪迈的女声"]  您还有什么要说的吗？发言人马克维茨先生？
[Character(name="avg_npc_109#3")]
[name="企业员工"]  我......我觉得......
[name="企业员工"]  ......
[Character(name="avg_npc_109#4")]
[name="企业员工"]  不，我、我明白了......
[name="豪迈的女声"]  很好，祝您一切顺利。
[PlaySound(key="$transmission", volume=0.4)]
[Character(name="avg_npc_109",fadetime=1,block=true)]
[delay(time=2)]
[name="发言人马克维茨"]  ......
[name="发言人马克维茨"]  哈......梦......这是梦吧......
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=0.4)]
[Character(name="char_204_platnm_1",fadetime=1,block=true)]
[delay(time=1)]
[name="白金"]  事情我已经听说了......恰尔内的权限现在全部转移给你，是叫......发言人马克维茨，对吧？
[name="白金"]  接下来怎么做？或者你想冷静一下，给我放个假也行的喔。
[Character(name="avg_npc_109#3", name2="char_204_platnm_1", focus=1)]
[name="发言人马克维茨"]  我、我不懂......为什么是我......
[name="发言人马克维茨"]  等等，你也一样，白金大位，你为什么要被推上这个位置？我该怎么办......？
[Character(name="avg_npc_109#3", name2="char_204_platnm_1", focus=2)]
[name="白金"]  谁知道呢，也许他们只是想看着下一个人变得和他们一样糟糕。
[name="白金"]  在卡西米尔，别想太多就对了。
[Character(name="avg_npc_109#2", name2="char_204_platnm_1", focus=1)]
[name="发言人马克维茨"]  但......你看我......甚至买不起一套像样的西装，我......
[name="发言人马克维茨"]  对了......恰尔内先生一定给你安排过任务，你应该知道无胄盟在做什么——
[Character(name="avg_npc_109#2", name2="char_204_platnm_1", focus=2)]
[name="白金"]  不知道。
[Character(name="avg_npc_109#3", name2="char_204_platnm_1", focus=1)]
[name="发言人马克维茨"]  呃......？
[Character(name="avg_npc_109#3", name2="char_204_platnm_1", focus=2)]
[name="白金"]  我只知道我在做什么。
[Character(name="avg_npc_109", name2="char_204_platnm_1", focus=1)]
[name="发言人马克维茨"]  那，那你在做什么？
[Character(name="avg_npc_109", name2="char_204_platnm_1", focus=2)]
[name="白金"]  欸......一般来说就算我这么回答了也不会追问的吧......你啊......
[name="白金"]  算了，毕竟前段时间，我的确搞砸了一件事，现在我需要把精力放在上面。
[name="白金"]  五位骑士杀手在追踪目标的时候被发现，然后全部失踪了。
[Character(name="avg_npc_109#2", name2="char_204_platnm_1", focus=1)]
[name="发言人马克维茨"]  无胄盟失、失踪？
[Character(name="avg_npc_109#2", name2="char_204_platnm_1", focus=2)]
[name="白金"]  ......你真的做好了知道详情的打算吗？
[Character(name="avg_npc_109#4", name2="char_204_platnm_1", focus=1)]
[name="发言人马克维茨"]  我......我别无选择。
[Character(name="avg_npc_109#4", name2="char_204_platnm_1", focus=2)]
[name="白金"]  是么。
[name="白金"]  那就多留意一下“红松骑士团”，他们可不是单纯的竞技骑士这么简单，他们在公开和无胄盟......对抗。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_storehouse",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fade

... (全文15992字符)
```

### training_act13d5_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_a

[PopupDialog(dialogHead="$avatar_sophia")] 好，今天由我暂替杜宾训练各位，这会是一次“有趣的”作战训练。准备好了吗？
[PopupDialog(dialogHead="$avatar_scave")] 模拟卡西米尔的骑士竞技吗……在人造地形中以少搏多，的确像那么回事。
[PopupDialog(dialogHead="$avatar_scave")] ……但这些人真的是骑士吗？
[PopupDialog(dialogHead="$avatar_wyvern")] 只是来客串一下的骑士竞技爱好者啦。你看，这只钳兽看上去也——
[PopupDialog(dialogHead="$avatar_sophia")] 这可是货真价实的钳兽哦。虽然在罗德岛不用遭到那么残酷的饲养方式……但也能轻松劈开护甲。
[PopupDialog(dialogHead="$avatar_wyvern")] 唉!?呜哇哇…!
[PopupDialog(dialogHead="$avatar_frostl")] 真是拿你没办法，我来对付它！

```

### training_act13d5_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_b

[Tutorial(focusX=-480, focusY=170, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_scave", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
无人机？但是好像没有配备武器装置……？
[Tutorial(focusX=-480,focusY=170, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sophia", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是由观众为场上选手赞助的<@tu.kw>特殊补给箱</>，每架无人机的<@tu.kw>补给各有不同</>，打爆它就可以<@tu.kw>获得补给</>哦。
[Tutorial(focusX=-480,focusY=170, focusWidth=100, focusHeight=100, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sophia", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
另外，因为是额外的补给箱，即使飞走了，也<@tu.kw>不会对目标生命值有什么影响</>，自由取舍吧。
[PopupDialog(dialogHead="$avatar_mm")] 那太好了，我来帮忙对付它~里面一定装满了非法货物~！
[PopupDialog(dialogHead="$avatar_flower")] 我来负责治疗，各位，请务必小心钳兽的利爪！



```

### training_act13d5_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13d5教学关_c

[PopupDialog(dialogHead="$avatar_mm")] 欸？教官，那个充满了可疑气息的桩子是怎么回事？
[Tutorial(focusX=0, focusY=20, focusWidth=120, focusHeight=120,\
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sophia", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这是梅什科线圈。<@tu.kw>单个线圈并不会有效果</>。在生效范围内有其他线圈时，相连的线圈之间会<@tu.kw>激活</>。并在线圈之间产生电流攻击敌人。
[Tutorial(focusX=-15, focusY=15, focusWidth=220, focusHeight=220, anchor="BottomRight",\
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sophia", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
尝试部署新的梅什科线圈来扩大地形优势，这也是战术的意义。
[PopupDialog(dialogHead="$avatar_scave")] 那，博士，就靠你了。


```


## 统计

- 总字符数：337095
- 对话行数：2797


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
