# 明日方舟 · 活动剧情 · act30side（28段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act30side」完整剧情脚本（28个文件，5160行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act30side
- 脚本文件数：28

### level_act30side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g12_mountpath",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6, loop=true, channel="wind")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$e_skill_skulsrsword",volume=0.8)]
[PlaySound(key="$swordtsing4", volume=0.9,delay=0.2)]
[CameraShake(duration=0.8, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_slash_cross",x=-50,layer = 1)]
[Effect(name="$e_spark_02_large",layer = 2)]
[Effect(name="$e_spark_01_mid",roy=-90,layer = 3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_spear",volume=0.8)]
[PlaySound(key="$swordtsing5", volume=0.9,delay=0.2)]
[CameraShake(duration=0.8, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[Effect(name="$e_spark_01_large",layer = 2)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[StopSound(channel="wind", fadetime=2.5)]
[charslot(slot="l",name="avg_npc_275",duration=1)]
[charslot(slot="r",name="avg_npc_275",duration=1)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_npc_275",focus="l")]
[name="身手矫健的山雪鬼"]嗬！哈！
[charslot(slot="r",name="avg_npc_275",focus="r")]
[name="气喘吁吁的山雪鬼"]呼......呼......
[Dialog]
[charslot]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_275",focus="m")]
[name="精疲力尽的山雪鬼"]哈......！嚯啊！
[Dialog]
[PlaySound(key="$d_avg_snowrun", volume=1, loop=false, channel="b")]
[StopSound(channel="b", fadetime=1.5)]
[charslot(duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_275",focus="m")]
[name="斗志昂扬的山雪鬼"]吃我一招！
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot="l",name="avg_npc_275",focus="all")]
[charslot(slot="r",name="avg_npc_275",focus="all")]
[Delay(time=0.2)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="众山雪鬼"]哈啊——！冲啊——！
[Dialog]
[PlaySound(key="$d_avg_snowcrwdmarch", volume=1)]
[charslot(duration=0.7)]
[Delay(time=1.5)]
[Dialog]
[PlaySound(key="$d_avg_janttck_01", volume=1)]
[charslot(slot="l",name="avg_npc_275",focus="all")]
[charslot(slot="r",name="avg_npc_275",focus="all")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_metallicclick", volume=0.9)]
[CameraShake(duration=0.5, xstrength=40,ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.3, block=true)]
[Delay(time=0.2)]
[PlaySound(key="$bodyfalldown2")]
[PlaySound(key="$d_avg_kneelsnow_s", volume=1,delay=0.3)]
[charslot(slot="l",name="avg_npc_275",posfrom="0,0",posto="0,-50",duration=1,isblock=false)]
[charslot(slot="l",name="avg_npc_275",afrom=1,ato=0,duration=0.5)]
[charslot(slot="r",name="avg_npc_275",posfrom="0,0",posto="0,-30",duration=1,isblock=false)]
[charslot(slot="r",name="avg_npc_275",afrom=1,ato=0,duration=0.7)]
[Delay(time=1)]
[name="？？？"]你们都没吃饭？
[name="？？？"]再来。
[name="精疲力尽的山雪鬼"]老大，不、不行了，真的不行了......
[Dialog]
[PlaySound(key="$d_avg_snowfootstep", volume=1, loop=true, channel="j")]
[StopSound(channel="j", fadetime=3)]
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]站起来。
[name="锏"]我是怎么教你们的？
[charslot(slot="m",name="avg_4116_blkkgt_1#11$1",focus="m")]
[name="锏"]站起来，抓紧你们手里的武器！
[Dialog]
[charslot]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_snowfall", volume=0.6)]
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot="l",name="avg_npc_275",posfrom="0,-50",posto="0,0",afrom=0,ato=1,duration=0.7)]
[charslot(slot="r",name="avg_npc_275",posfrom="0,-30",posto="0,0",afrom=0,ato=1,duration=0.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_275",focus="r")]
[charslot(slot="r",name="avg_npc_275",focus="r")]
[name="斗志昂扬的山雪鬼"]是！
[charslot(slot="l",name="avg_npc_275",focus="l")]
[name="气喘吁吁的山雪鬼"]呼......呼......嗬啊！
[Dialog]
[charslot(slot="l",name="avg_npc_275",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_janttck_02", volume=1)]
[CameraShake(duration=0.5, xstrength=40,ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.3, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_snowbodyfall", volume=0.6)]
[charslot(duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4116_blkkgt_1#11$1",focus="m")]
[name="锏"]速度太慢。力道不足。法术太仓促。战术太死板。
[name="锏"]也就有些默契罢了。
[name="锏"]总体还是太弱。
[Dialog]
[charslot]
[name="身手矫健的山雪鬼"]那哪能和老大比......
[name="精疲力尽的山雪鬼"]哈......呼......
[name="精疲力尽的山雪鬼"]能让老大夸一句，这段时间的训练也算值得了。
[name="斗志昂扬的山雪鬼"]还不够！迟早有一天，我也要像老大那样，能单手切碎山石！
[name="气喘吁吁的山雪鬼"]就凭你......
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]......
[name="锏"]看来你们休息够了。
[name="锏"]那就再来。
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="众山雪鬼"]啊——？！
[stopmusic(fadetime=2)]
[Dialog]
[PlaySound(key="$d_avg_snowrun", volume=1, loop=false, channel="c")]
[StopSound(channel="c", fadetime=1.5)]
[charslot(slot="m",name="avg_npc_275",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_275",focus="m")]
[name="慌张的山雪鬼"]老大！不好了！
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]不要慌。
[charslot(slot="m",name="avg_npc_275",focus="m")]
[na

... (全文19078字符)
```

### level_act30side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
我的记忆中有一片茫茫白雪。
我记得小的时候，我躺在木头做的小床上，屋内壁炉里的柴火噼啪作响，窗外漫天大雪彻夜不停。
风声在耳畔呼呼作响，一只大手抚着我的头，有人低声哄我入睡。
我就在暖暖的安心感中沉入梦乡。
我曾一度以为，那是乌萨斯。
妈妈却告诉我，不是的，罗莎琳，那不是乌萨斯。
那是谢拉格的风。
那是谢拉格的雪。
那是......我出生的地方。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g3_traincarriage", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_4114_harold_1#16$1")]
[charslot(slot="r",name="avg_194_leto_1#8$1")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4114_harold_1#16$1",focus="l")]
[name="哈洛德"]所以......罗莎琳你是一直到上高等学校，才知道自己其实是在谢拉格出生的？
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]对啊，我妈之前完全没提过还有这回事，最开始我还以为她在开玩笑呢！
[name="烈夏"]小时候的事我都忘得差不多了，就记得到处都是雪......乌萨斯不也到处都是雪嘛！
[name="烈夏"]这谁分得清。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]唔，这么说的话确实是有几分相似。
[name="哈洛德"]不过在我的记忆里，乌萨斯比谢拉格要更冷点。
[charslot(slot="r",name="avg_194_leto_1#13$1",focus="r")]
[name="烈夏"]啊......这倒是没错，确实还是乌萨斯更冷。
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]大叔你也去过乌萨斯？
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]哈哈，都是好多年前的事了。
[name="哈洛德"]那时候没什么机会好好逛逛，可惜了！
[charslot(slot="r",name="avg_194_leto_1#1$1",focus="r")]
[name="烈夏"]那你下回再来，我给你当向导。
[name="烈夏"]乌萨斯别的不说，圣骏堡的景色还是一等一的。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]那太好了，呃，看来我得多准备两件厚外套。
[name="哈洛德"]在有机会去乌萨斯赴约之前，还是先让我为罗莎琳小姐做向导吧。
[name="哈洛德"]那么，就先说说这趟车的目的地——新建的那座耶拉冈德像。
[name="哈洛德"]它就建在银心湖的湖心岛上，十分显眼，一出车站立刻就能看到。
[name="哈洛德"]当然，对罗莎琳你来说，耶拉冈德像还不是重点......
[name="哈洛德"]你的这趟谢拉格之旅，有比观光更重要的事。
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]对。没错。
[name="烈夏"]我要先替我妈看一眼耶拉冈德像，这是她......她走之前强调过的。
[name="烈夏"]然后我就转道去银心湖旁边的那座山。
[name="烈夏"]我得把这个盒子里的东西，送到那座山的山顶。
[charslot(slot="l",name="avg_4114_harold_1#16$1",focus="l")]
[name="哈洛德"]这里面是？
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]我也不知道，我妈没和我说。
[name="烈夏"]她只让我把这个丢到那座山上，这样她就能心满意足了。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]孤身一人回到陌生的故乡，只为完成母亲的愿望......
[charslot(slot="l",name="avg_4114_harold_1#14$1",focus="l")]
[name="哈洛德"]多么孝顺，多么好的孩子，真是令人感动！
[charslot(slot="r",name="avg_194_leto_1#10$1",focus="r")]
[name="烈夏"]呃，也没有你说的这么夸张啦。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]那么，在那之后罗莎琳你的计划是？
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]把东西送上山之后？没什么具体的计划，可能四处逛逛。
[charslot(slot="r",name="avg_194_leto_1#9$1",focus="r")]
[name="烈夏"]......
[charslot(slot="r",name="avg_194_leto_1#7$1",focus="r")]
[name="烈夏"]也有可能......会去找我爹。
[charslot(slot="l",name="avg_4114_harold_1#16$1",focus="l")]
[name="哈洛德"]你的父亲还在谢拉格？
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]若是寻人，或许我能帮得上忙？
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]真的吗？可是我不知道他的名字，也记不得他长啥样了。
[name="烈夏"]不过我妈和我说过，我爹长得很好看。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]啊哈，一位美男子。
[charslot(slot="r",name="avg_194_leto_1#1$1",focus="r")]
[name="烈夏"]没错！据说是当时谢拉格有名有姓的美男子，好像还挺有名气的嘞。
[name="烈夏"]对了，我妈还说过，我的眼睛最像我爹。
[charslot(slot="l",name="avg_4114_harold_1#11$1",focus="l")]
[name="哈洛德"]谢拉格的有名人？美男子？唔......
[charslot(slot="r",name="avg_194_leto_1#6$1",focus="r")]
[name="烈夏"]有人选？
[charslot(slot="l",name="avg_4114_harold_1#11$1",focus="l")]
[name="哈洛德"]嗯......
[name="哈洛德"]如果那位先生能生出罗莎琳你这个年纪的女儿，那么只能是在维多利亚留学期间......唔......
[name="哈洛德"]不，不不不。再怎么说也......
[charslot(slot="l",name="avg_4114_harold_1#16$1",focus="l")]
[name="哈洛德"]当时，乌萨斯，难道说......
[charslot(slot="r",name="avg_194_leto_1#6$1",focus="r")]
[name="烈夏"]到底怎么说？
[charslot(slot="l",name="avg_4114_harold_1#4$1",focus="l")]
[name="哈洛德"]呃，哈哈，我得再寻思寻思。
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]要是能找到他那最好。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]来一场令人感动的父女相认？
[charslot(slot="r",name="avg_194_leto_1#13$1",focus="r")]
[name="烈夏"]啧。
[name="烈夏"]不太一样。
[charslot(slot="r",name="avg_194_leto_1#4$1",focus="r")]
[name="烈夏"]我只是要看看，这个十多年没出现的混账东西到底是个什么样的人。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g2_trainwalkway", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_276_1#1$1",focus="m")]
[name="列车员"]欢迎各位乘坐最新的“圣女号”列车，我们的列车正处于正常行驶中，您可以透过两侧的车窗观赏谢拉格美丽的自然风光。
[name="列车员"]在列车行驶过程中，我们还将在车内特别开展谢拉格当地特产的售卖活动！
[name="列车员"]谢拉格特色奶酪零食及人气驮兽盲盒均有贩卖，更有喀兰贸易公司推出的精装版高山雪水限量发售，产地直销，圣女严选，品质有保障！
[name="列车员"]有需要的乘客可以自由选购......
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="怪帽子外国佬"]不好意思，请问一下。
[charslot(slot="m",name="avg_npc_276_1#1$1",focus="m")]
[name="列车员"]啊，这位乘客，请问您想来点什么？
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="怪帽子外国佬"]我不是要看商品......
[charslot(slot="m",name="avg_npc_276_1#1$1",focus="m")]
[name="列车员"]您不要看普通商品？那这款精装版高山雪水要看一下吗？
[name="列车员"]这款产品是三族议会的指定用水，圣女大人也非常喜爱呢，我们这趟车到货不多，非常难得，现在购买仅需四弗朗！
[charslot(slot="m",name="avg_npc_280_1#1$1",focus="m")]
[name="看热闹的乘客"]嘶......四弗朗？这都够我下馆子请客吃一顿了！
[charslot(slot="m",name="avg_npc_276_1#1$1",focus="m")]
[name="列车员"]虽然是贵了一点，但您看这包装，这纯净的感觉，特别符合先生您的气质！
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="怪帽子外国佬"]......不必了。
[name="怪帽子外国佬"]就要......这个盲盒吧，谢谢。
[Dialog]
[PlaySound(key="$d_avg_coin", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_276_

... (全文18562字符)
```

### level_act30side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g3_traincarriage",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_trainlp", volume=0.6, loop=true, channel="bgs")]
[Delay(time=1)]
[playMusic(key="$comedy_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[StopSound(channel="bgs", fadetime=1.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_4114_harold_1#11$1",duration=0.7)]
[charslot(slot="r",name="avg_194_leto_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="r",name="avg_194_leto_1#1$1",focus="r")]
[name="烈夏"]......就是说那个蜂蜜饮料啊，喝起来甜滋滋的，没想到后劲大得很！
[name="烈夏"]不过对我来说也就一般般啦，我朋友还说我醉蜜，结果呢，我精神得很，她倒是先倒下了。
[charslot(slot="l",name="avg_4114_harold_1#11$1",focus="l")]
[name="哈洛德"]......
[charslot(slot="r",name="avg_194_leto_1#13$1",focus="r")]
[name="烈夏"]嗯？喂喂，大叔？
[name="烈夏"]喂——你在听吗——
[charslot(slot="l",name="avg_4114_harold_1#11$1",focus="l")]
[multiline(name="哈洛德")]嗯......
[charslot(slot="l",name="avg_4114_harold_1#16$1",focus="l")]
[multiline(name="哈洛德")]啊？
[name="哈洛德"]恕我失礼，罗莎琳，你刚刚说什么？
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]我说我朋友醉蜜！
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]哦，是的是的，没错，醉蜜。
[charslot(slot="r",name="avg_194_leto_1#9$1",focus="r")]
[name="烈夏"]......啧，真麻烦......
[name="烈夏"]大叔你要是有什么在意的事，就先去解决一下呗。
[name="烈夏"]现在这副魂不守舍的样子，根本没法聊。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]不不，现在可没有什么比罗莎琳你的故事更值得我在意的。
[name="哈洛德"]继续说说醉蜜的事吧，罗莎琳，我记得列车上应该也有卖含蜂蜜的特产饮料。
[charslot(slot="r",name="avg_194_leto_1#13$1",focus="r")]
[name="烈夏"]行了，少骗人。
[name="烈夏"]我这双眼睛利着呢，从刚刚那个戴帽子的家伙来开始，大叔你就不太对劲了。
[charslot(slot="r",name="avg_194_leto_1#7$1",focus="r")]
[name="烈夏"]你们是朋友......不对，我看不像。
[charslot(slot="r",name="avg_194_leto_1#9$1",focus="r")]
[name="烈夏"]那就是仇人？
[charslot(slot="l",name="avg_4114_harold_1#12$1",focus="l")]
[name="哈洛德"]......这倒也称不上。
[name="哈洛德"]或许用“同僚”勉强能概括我与那位先生的关系，尽管我们在“公司”内并非隶属同一部门。
[charslot(slot="r",name="avg_194_leto_1#8$1",focus="r")]
[name="烈夏"]哦，那就是休假时撞见关系不怎么样的同事。
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]我喜欢这个说法。
[name="哈洛德"]好吧，罗莎琳，我承认我有点担心我的同僚能否顺利完成他的工作，所以，原谅我要失陪一会。
[name="哈洛德"]作为补偿，我会给你带蜂蜜饮料，主要原料是谢拉格特产高地蜂蜜，每一滴都是耶拉冈德的恩赐，天然纯净......
[charslot(slot="r",name="avg_194_leto_1#6$1",focus="r")]
[name="烈夏"]真的？但我已经要对这套耶拉冈德广告词无感了......
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[name="哈洛德"]千真万确。
[name="哈洛德"]不过你的朋友说你会醉蜜，我想我们需要做个约定——每天最多一瓶，以防你在旅行期间真的喝醉。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g2_trainwalkway", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_npc_867_1#1$1")]
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[PlaySound(key="$d_avg_trainlp", volume=0.6, loop=true, channel="bgs1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[StopSound(channel="bgs1", fadetime=1.5)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]我们之间没有如此剑拔弩张的必要，锏女士。
[name="“灰礼帽”"]公爵阁下心系喀兰贸易，同时也关注谢拉格的发展，为其留意谢拉格的方方面面，是我的工作。
[name="“灰礼帽”"]这次自然也不例外，您不必如此防范。
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]你的工作，包括参观列车的包厢？
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]这里的变化惊人，不是吗？
[name="“灰礼帽”"]据我所知，这条从圣山脚下到银心湖的线路上，投入使用的列车都是自维多利亚引进的车型。
[name="“灰礼帽”"]不过这一系列与当初引进时相比，已经有了很大的变化。
[name="“灰礼帽”"]只用短短三年时间就能够做到这一步，喀兰贸易在技术上的发展，令最早在此事上牵线的公爵阁下也颇为赞叹。
[charslot(slot="r",name="avg_4116_blkkgt_1#11$1",focus="r")]
[name="锏"]诺希斯如果做不到，那为他力排众议的恩希欧迪斯就该头疼了。
[name="锏"]你打算和我聊聊技术？
[name="锏"]那你找错人了，直接去找诺希斯聊，搞不好他还会有点兴趣。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]......我很好奇，女士。
[name="“灰礼帽”"]我没想到会在这里遇见您，还是在这样的情况下。
[name="“灰礼帽”"]是什么人值得您亲自出手？是多么棘手的状况，能让您急迫到......没有时间更换一双沾满血污的手套？
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]......
[charslot(slot="r",name="avg_4116_blkkgt_1#11$1",focus="r")]
[name="锏"]解决了一点小麻烦。
[name="锏"]劝你收起不合时宜的好奇心，“灰礼帽”。
[name="锏"]我只是来找人的，暂时还不想再弄脏一双手套。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]无意冒犯。
[name="“灰礼帽”"]我绝无干涉锏女士行动的意思。
[name="“灰礼帽”"]只是，想必在车上的一定是位重要人物......
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]是又如何？
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]如果您不介意透露些许，或许我能为您效劳。
[name="“灰礼帽”"]毕竟“寻人”......这也算是我们的日常工作之一。
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]你好像搞错了什么。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]什么？
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]恩希欧迪斯默许你们在他身边探头探脑，那是他的事，我不会管。
[name="锏"]但我没那么好的耐心。
[name="锏"]你知道谢拉格比卡西米尔好在哪吗？
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]......
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]这里冷是冷了点，相对的，虫子就少一些。
[name="锏"]那些让人心烦的飞虫，总是让人有伸手碾死的冲动。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]......
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]收敛点，否则，我不介意替恩希欧迪斯动手。
[charslot(slot="l",name="avg_npc_867_1#1$1",focus="l")]
[name="“灰礼帽”"]......多谢忠告。
[charslot(slot="r",name="avg_4116_blkkgt_1#6$1",focus="r")]
[name="锏"]是警告。
[charslot(slot="r",name="avg_4116_blkkgt_1#11$1",focus="r")]
[name="锏"]好了，废话够多了。你拖够时间了？
[Dialog]
[Delay(time=1)]
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]很巧，我要找的就是刚刚在车厢门后面偷听的那位。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)] 
[charslot]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_4114_harold_1#8$1")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4114_harold_1#8$1",focus="m")]
[name="哈洛德"]呃。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]


... (全文13936字符)
```

### level_act30side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g2_trainwalkway",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$comedy_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_032",duration=0.7)]
[charslot(slot="r",name="avg_npc_033",duration=0.7)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_032",focus="l")]
[name="精神的游客"]快看，外面能看到雪山！
[name="精神的游客"]天啊这也太近了吧，这是不是谢拉格的圣山？不管是不是，这景色都太美了！
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]我、我说啊，能不能先把窗户关上......
[charslot(slot="l",name="avg_npc_032",focus="l")]
[name="精神的游客"]欸？
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]风、风有点大，吹得我说话都、都有点不利索了。
[Dialog]
[charslot(slot="l",name="avg_npc_032",focus="l")]
[PlaySound(key="$d_avg_trnclsdor",volume=0.7,channel="close",loop=false)]
[stopsound(channel="close",fadetime=1)]
[Delay(time=1.5)]
[name="精神的游客"]也不至于这么夸张吧，我觉得也不是不能忍忍......
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]真的假的，你真的不冷吗？我看你甚至没穿裤子——
[Dialog]
[PlaySound(key="$d_avg_slap")]
[charslot(slot = "r", action="shake",random=true, power=5, times=40,duration=0.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_032",focus="l")]
[name="精神的游客"]建议你再组织一下语言，再这么说下去我就要告你耍流氓了。
[name="精神的游客"]我穿的这是保暖裤袜，最厚实的那一种！比你那身暖和多了！
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]哎哟......行行行，你说是，那就是吧......
[charslot(slot="l",name="avg_npc_032",focus="l")]
[name="精神的游客"]哼。快，你再站过来点，我要拍照了！
[Dialog]
[stopmusic(fadetime=2)]
[charslot(slot="l",name="avg_npc_032",focus="n")]
[PlaySound(key="$d_avg_crowdrun",volume=0.3)] 
[delay(time=2)]
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]......嗯？
[name="发抖的游客"]哎，你有没有听到什么声音......
[Dialog]
[charslot]
[delay(time=0.5)]
[PlaySound(key="$d_avg_crrigrunlght",volume=0.7)]
[delay(time=1)]
[PlaySound(key="$d_avg_trnclsdorh",volume=1)]
[delay(time=1)]
[CameraShake(duration=1, xstrength=20,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_4114_harold_1#6$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_4114_harold_1#6$1",focus="m")]
[name="哈洛德"]女士们先生们，日安，日安！
[name="哈洛德"]很抱歉打扰各位的观光休闲！麻烦各位暂时回到坐席稍作避让，我们——
[Dialog]
[charslot]
[delay(time=0.5)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.6)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_runstop")]
[charslot(slot="m",name="avg_194_leto_1#4$1",duration=0.3)]
[delay(time=0.5)]
[charslot(slot="m",name="avg_194_leto_1#4$1",focus="m")]
[name="烈夏"]行了这种时候了就别废话了！
[charslot(slot="m",name="avg_194_leto_1#13$1",focus="m")]
[name="烈夏"]对不住各位，让让，麻烦都让让！
[charslot(slot="m",name="avg_4114_harold_1#6$1",focus="m")]
[name="哈洛德"]罗莎琳！这样有点太失礼了......
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[PlaySound(key="$d_avg_crrigrunlght",volume=0.7,delay=0.4)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=15, randomness=90, fadeout=true, block=false)]
[charslot(duration=0.5)]
[delay(time=0.7)]
[name="哈洛德"]哎，哎，罗莎琳，轻点拉，我的袖子要被你扯下来了！
[Dialog]
[charslot(slot="l",name="avg_npc_032",focus="l")]
[charslot(slot="r",name="avg_npc_033",focus="l")]
[name="精神的游客"]呃，这是什么谢拉格风俗？
[name="精神的游客"]我们也要这样在列车里跑跑看吗......？
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]不可能有这种风俗吧？感觉好傻，我不干。
[charslot(slot="l",name="avg_npc_032",focus="l")]
[name="精神的游客"]不管了，还是先把合照拍了！
[name="精神的游客"]看镜头！三......二......
[name="精神的游客"]一......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_sundries",volume=0.6)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2.5)]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=0.5)]
[delay(time=1)]
[charslot(duration=0.5)]
[delay(time=1)]
[PlaySound(key="$d_avg_crrigrunwght",volume=0.7)]
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]我不讨厌这种追逐游戏。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]我谈不上喜欢。我们不能坐下来好好谈吗？
[charslot(slot="m",name="avg_4116_blkkgt_1#11$1",focus="m")]
[name="锏"]是你们自己做贼心虚，一直在跑啊。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]最好继续跑，别停下。
[Dialog]
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_crrigrunlght",volume=0.7)]
[charslot(duration=0.5)]
[delay(time=1)]
[charslot(slot="l",name="avg_4116_blkkgt_1#8$1",focus="l")]
[charslot(slot="r",name="avg_npc_032",focus="l")]
[name="锏"]哦，顺便一说，再等五分钟才是外面风景最好的路段，合影可以之后再拍。
[name="锏"]玩得开心点。
[Dialog]
[charslot(slot="l",name="avg_4116_blkkgt_1#8$1",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_crrigrunwght",volume=0.7)]
[charslot(slot="l",name="avg_4116_blkkgt_1#8$1",afrom=1,ato=0,duration=0.5)]
[delay(time=1.5)]
[charslot]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_032",focus="l")]
[charslot(slot="r",name="avg_npc_033",focus="l")]
[name="精神的游客"]......
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]......
[Dialog]
[charslot(slot="r",name="avg_npc_033",focus="all")]
[delay(time=0.2)]
[PlaySound(key="$d_avg_takphtrptly",volume=0.7)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.3, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_032",focus="l")]
[charslot(slot="r",name="avg_npc_033",focus="l")]
[name="精神的游客"]刚刚那又是什么人？
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="发抖的游客"]不知道......
[name="发抖的游客"]不过你刚刚说得可能有道理，谢拉格搞不好确实有什么要在列车上疾跑一圈的风俗......
[n

... (全文19078字符)
```

### level_act30side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g2_trainwalkway",screenadapt="coverall")]
[Delay(time=1)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="bgs",volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_trnrvlbrdcst", volume=0.7)]
各位乘客，本次列车到达终点站——
银心湖站。
银心湖地处盆地中央，湖面雾霭氤氲，水质清澈，是谢拉格土地上孕育出的众多瑰宝之一。
传说银心湖是耶拉冈德落下的第一滴眼泪，在冬季，您可以于冰封的湖面上漫步，透过冰面，还可以观赏冰层深处的风景。
而最新建起的耶拉冈德像伫立于银心湖的湖心岛之上，耶拉冈德在此，注视着谢拉格与其子民。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_black", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
各位乘客，本次列车......
[Dialog]
[StopSound(channel="bgs", fadetime=4)]
[PlaySound(key="$d_avg_walk_stage")]
[PlaySound(key="$d_avg_higheldshosfts", volume=0.6)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[Delay(time=2.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Image(image="45_i05",screenadapt="coverall",fadetime=0,block=true)]
[Delay(time=1)]
[ImageTween(xFrom=0, yFrom=-100, xTo=0, yTo=0, xScaleFrom=1.5, yScaleFrom=1.5, xScaleTo=1, yScaleTo=1, duration=25, block=false)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]
[name="哈洛德"]......
[name="“灰礼帽”"]......
[name="锏"]......
[name="哈洛德"]......所以，一切都是误会？
[name="哈洛德"]没有隐情，没有追杀，没有什么可能在车上的重要人物，什么都没有？
[name="锏"]如果你指的是让我登上这趟列车的“重要人物”，那就是你。
[name="锏"]短短一个月就在牧民间扬名，擅长医治驮兽的哈洛德·克雷加文子爵。
[name="哈洛德"]咳咳。
[name="哈洛德"]我的荣幸，女士。
[name="“灰礼帽”"]请您原谅，锏女士。
[name="“灰礼帽”"]您手套上的血迹，实在令人难以不多做一些设想。
[name="锏"]血迹？
[name="锏"]你很在意？
[name="锏"]这么在意，告诉你也无妨。
[name="“灰礼帽”"]洗耳恭听。
[name="锏"]莉莉生产时的情况不是很好。
[name="锏"]突然早产，出血量很大，费了我不少功夫。
[name="哈洛德"]什么？！
[name="哈洛德"]早产......出血量还不少？
[name="哈洛德"]这可不是小事，锏女士，莉莉她现在情况如何？
[name="锏"]我替她做了应急处理，但后续的护理还需要专业人士来做。
[name="锏"]老雷昂指名说最信得过你，克雷加文。
[name="锏"]之后就要看你的本事了。
[name="哈洛德"]好！我立刻就赶过去！
[name="“灰礼帽”"]......
[name="锏"]你现在的表情有点遗憾。怎么，不符合你的想象？
[name="锏"]没关系，我不介意让你的想象成真。
[name="“灰礼帽”"]这就不必了，女士。
[name="锏"]说说看，你们都误会了什么？
[name="哈洛德"]这个......哈哈，银心湖真是个不错的地方。
[name="哈洛德"]今天的天气也不错，风和日丽，空气清新......
[name="锏"]......维多利亚人连转移话题都要谈论天气？
[name="锏"]这种套话我听过一万次，腻了。
[name="哈洛德"]请您见谅，在维多利亚，我们会从小学习如何靠我们糟糕的天气来开启话题。
[name="“灰礼帽”"]请您不要随便抹黑维多利亚的形象，子爵阁下。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[image]
[Delay(time=0.5)]
[Background(image="45_g1_kjeragtrainstation", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_194_leto_1#13$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_194_leto_1#13$1",focus="m")]
[name="烈夏"]喂——
[name="烈夏"]你们怎么还在这傻站着聊天？
[name="烈夏"]不就是有点小误会吗，你们说开了没有？
[charslot(slot="m",name="avg_4114_harold_1#1$1",focus="m")]
[name="哈洛德"]当然，当然。
[name="哈洛德"]如果不是某些人危言耸听，也不至于产生这样的误会。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]......
[charslot(slot="m",name="avg_194_leto_1#9$1",focus="m")]
[name="烈夏"]行吧，你们都解决了就行。
[name="烈夏"]虽然在列车上跑跑挺有趣的，但我不想再蹲在桌子底下吃灰了。
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]对了，我刚刚去前面看了看，那边有导游姐姐指路，我还要了两张地图来！
[name="烈夏"]这儿离银心湖就一条街的距离，方便得很。
[name="烈夏"]怎么说，我们现在出发？
[charslot(slot="m",name="avg_4114_harold_1#12$1",focus="m")]
[name="哈洛德"]这......我很抱歉，罗莎琳，我无法兑现之前的承诺了。
[name="哈洛德"]现在有一位更加需要我的女士，我必须尽快赶到她的身边。
[charslot(slot="m",name="avg_194_leto_1#6$1",focus="m")]
[name="烈夏"]......莉莉真的是驮兽吧？不是什么，维多利亚贵族的黑话？
[charslot(slot="m",name="avg_4114_harold_1#10$1",focus="m")]
[name="哈洛德"]我求您！
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]行了，知道了，你还是赶紧去看看那位“莉莉女士”吧，我这没啥，我自己一个人完全没问题。
[charslot(slot="m",name="avg_4114_harold_1#2$1",focus="m")]
[name="哈洛德"]罗莎琳......
[charslot(slot="m",name="avg_194_leto_1#14$1",focus="m")]
[name="烈夏"]你、你怎么了，干嘛这副表情？
[charslot(slot="m",name="avg_4114_harold_1#2$1",focus="m")]
[name="哈洛德"]你真是个善解人意的好姑娘！
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_4114_harold_1#4$1",focus="m")]
[name="哈洛德"]来，让我们先交换一下联络方式。
[Dialog]
[PlaySound(key="$d_avg_devicebeep",volume=0.8)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4114_harold_1#1$1",focus="m")]
[name="哈洛德"]如果遇到困难，随时可以联系我，哈洛德乐意为你效劳。
[name="哈洛德"]还有你的父亲......谢拉格美男子，对吧？我也会帮你留意。
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]那就多谢了，大叔。
[name="烈夏"]你们继续聊吧，我先走了！
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(duration=1)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4114_harold_1#14$1",focus="m")]
[name="哈洛德"]唉，多好的孩子，刚刚失去母亲，却还能如此乐观，如此坚强......
[charslot(slot="m",name="avg_4116_blkkgt_1#10$1",focus="m")]
[name="锏"]......谢拉格美男子？
[charslot(slot="m",name="avg_4114_harold_1#1$1",focus="m")]
[name="哈洛德"]啊，您听到了。
[name="哈洛德"]罗莎琳这孩子这趟来谢拉格，就是想要找到多年未见的父亲。
[name="哈洛德"]真是感人，希望她能一切顺利。
[charslot(slot="m",name="avg_4116_blkkgt_1#7$1",focus="m")]
[name="锏"]父亲......
[charslot(slot="m",name="avg_4116_blkkgt_1#10$1",focus="m")]
[name="锏"]那个女孩是这么说的？
[charslot(slot="m",name="avg_4114_harold_1#14$1",focus="m")]
[name="哈洛德"]既然误会已经解开，那......
[name="哈洛德"]锏女士，我是您忠实的支持者，不知可否赏脸签名——
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]没空。
[name="锏"]先走了，你记得照顾好莉莉。
[stopmusic(fadetime=2)]
[Dialog]
[PlaySound(key="$d_avg_higheldshosfts", volume=0.6)]
[charslot(duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4114_harold_1#8$1",focus="m")]
[name="哈洛德"]哎，且慢，请留步，锏女士！
[name="哈洛德"]哎——
[charslot(slot="m",name="avg_4114_harold_1#12$1",focus="m")]
[name="哈洛德"]......这就走了。
[Dialog]
[charslot]
[name="“灰礼帽”"]我们的黑骑士女士看起来并不喜欢那段辉煌的过往经历。
[name="“灰礼帽”"]这也难怪，她毕竟是以那样的方式被卡西米尔驱逐......
[Dialog]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[charslot(slot="l",name="avg_4114_harold_1#1$1",focus="l")]
[

... (全文20395字符)
```

### level_act30side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
罗莎琳，来，妈妈教你怎么向耶拉冈德祈祷。
闭上眼睛，把手放在胸前，在心里呼喊耶拉冈德的名字......
对啦，我们的小罗莎琳真棒，做得很好。
罗莎琳，你知道吗，你是爸爸妈妈最最重要的宝贝。
不管旁人怎么说，妈妈都不后悔生下你。
愿耶拉冈德保佑......
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g9_underkjerastastue", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_194_leto_1#6$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_194_leto_1#6$1",focus="m")]
[name="烈夏"]这耶拉冈德像，走近了看，感觉更大了。
[name="烈夏"]耶拉冈德，原来就长这样啊。
[charslot(slot="m",name="avg_194_leto_1#7$1",focus="m")]
[name="烈夏"]嗯......
[name="烈夏"]耶拉冈德......祈祷......
[name="烈夏"]妈妈当时好像还说了什么，呃呃呃，还有什么来着？
[charslot(slot="m",name="avg_194_leto_1#3$1",focus="m")]
[name="烈夏"]不行，头疼，想不起来，都是三岁之前的事了，想不起来也很正常吧！
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]总之先祈祷——
[charslot(slot="m",name="avg_194_leto_1#3$1",focus="m")]
[name="烈夏"]要闭眼，然后手......手怎么放来着？
[musicvolume(volume=0.3, fadetime=1)]
[Dialog]
[charslot]
[name="？？？"]将右手平展，置于胸前。
[Dialog]
[PlaySound(key="$d_avg_snowfootstep",volume=0.6)]
[charslot(slot="m",name="avg_npc_1160_1#11$1",duration=1)]
[Delay(time=2)]
[musicvolume(volume=0.6, fadetime=1.5)]
[charslot(slot="m",name="avg_npc_1160_1#11$1",focus="m")]
[name="老修士"]在耶拉冈德面前，闭上我们无能洞真的双眼，垂下我们过于骄傲的头颅。
[name="老修士"]祛除心中杂念，默颂耶拉冈德之名。
[charslot(slot="m",name="avg_npc_1160_1#13$1",focus="m")]
[name="老修士"]孩子，来，跟着我一起。
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]......哦！
[Dialog]
[charslot(duration=0.5)]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.8, loop=true, channel="wind")]
烈夏重新闭上眼睛。
视线被遮蔽，四周陷入黑暗，感知却仿佛在刹那间宽阔延展。
身后的老修士用沙哑的声音唱诵对耶拉冈德的赞美——
耶拉冈德，予我们饱腹的山泉与果树。
耶拉冈德，予我们冰冻天灾的风雪。
善良慈爱的耶拉冈德，保佑我们，保佑谢拉格。
在颂声中，风刮过面颊的触感被放大，耳畔的风雪声呼呼作响。
不知从何而起的熟悉感几乎要将烈夏再度拉入回忆。
[Dialog]
[stopsound(channel="wind",fadetime=3)]
[Delay(time=2)]
[charslot(slot="m",name="avg_194_leto_1#11$1",focus="m")]
[name="烈夏"]（耶拉冈德......）
[name="烈夏"]（我不是你的信徒，我也不需要你的保佑。）
[name="烈夏"]（但如果你真能保佑你的信徒，那你一定要保佑我妈。）
[name="烈夏"]（如果不是我妈的要求，我可不会来。）
[charslot(slot="m",name="avg_194_leto_1#7$1",focus="m")]
[name="烈夏"]......
[name="烈夏"]嗯，不行，这样不够。
[charslot(slot="m",name="avg_npc_1160_1#12$1",focus="m")]
[name="老修士"]什么......？
[charslot(slot="m",name="avg_194_leto_1#3$1",focus="m")]
[CameraShake(duration=1, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="烈夏"]耶拉冈德！
[name="烈夏"]耶拉冈德——！
[name="烈夏"]请你保佑我妈妈！她是你的信徒！！
[name="烈夏"]她和我说谢拉格很好——！我会自己去看看到底有多好——！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="45_g9_underkjerastastue", screenadapt="coverall", block=true)]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_523_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_524_1#1$1",focus="l")]
[name="吃惊的游客"]那是在喊什么？
[charslot(slot="r",name="avg_npc_524_1#1$1",focus="r")]
[name="兴奋的游客"]好像是在祈祷？原来谢拉格的祈祷是这样的？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="45_g9_underkjerastastue", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_194_leto_1#11$1")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_194_leto_1#11$1",focus="m")]
[name="烈夏"]呼......
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]好，这样就没问题了。
[charslot(slot="m",name="avg_npc_1160_1#6$1",focus="m")]
[name="老修士"]小姑娘，你这是做什么？
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]这还用问，当然是祈祷啊！
[name="烈夏"]我觉得吧，在心里祈祷不如直接喊出来，都在心里念完了，万一耶拉冈德听不到咋办？
[charslot(slot="m",name="avg_npc_1160_1#12$1",focus="m")]
[name="老修士"]这......
[charslot(slot="m",name="avg_194_leto_1#1$1",focus="m")]
[name="烈夏"]难得来一次，当然要不留遗憾！
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]对了，刚刚多谢你教我啊，老伯。
[charslot(slot="m",name="avg_npc_1160_1#2$1",focus="m")]
[name="老修士"]唉，罢了，想来耶拉冈德也不会在意这些细枝末节......
[charslot(slot="m",name="avg_npc_1160_1#1$1",focus="m")]
[name="老修士"]小姑娘不必多礼。
[charslot(slot="m",name="avg_194_leto_1#1$1",focus="m")]
[name="烈夏"]哈哈哈，那耶拉冈德还蛮开明的嘛。
[name="烈夏"]老伯你也是。
[Dialog]
[PlaySound(key="$d_avg_snowbootwalk")]
[charslot(duration=1)]
[Delay(time=2)]
将一直放在胸前的手垂下，女孩最后抬头望了一眼面前高大的耶拉冈德像，转身走下台阶。
随着她的转身，年老的修士终于看清女孩的面容。
日光描摹面前的这副眉眼。
脸颊的弧度，鼻梁的耸起，唇瓣的形状......
——难以言说的熟悉感瞬间将老人淹没。
[charslot(slot="m",name="avg_npc_1160_1#6$1",focus="m")]
[name="老修士"]——
[name="老修士"]你、你是......
[name="老修士"]......
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]嗯？怎么了？
[charslot(slot="m",name="avg_npc_1160_1#10$1",focus="m")]
[name="老修士"]不、不，没什么......
[charslot(slot="m",name="avg_npc_1160_1#13$1",focus="m")]
[name="老修士"]老头子见过的游客不算少了，但像小姑娘你这般行事的，还是头一回见。
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]这样吗？我觉得我好像也没干啥。
[charslot(slot="m",name="avg_npc_1160_1#12$1",focus="m")]
[name="老修士"]......小姑娘，你叫什么名字？
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]罗莎琳，我叫罗莎琳。
[charslot(slot="m",name="avg_npc_1160_1#6$1",focus="m")]
[name="老修士"]......罗莎琳......
[charslot(slot="m",name="avg_npc_1160_1#12$1",focus="m")]
[name="老修士"]那你，多大年纪了？
[charslot(slot="m",name="avg_194_leto_1#8$1",focus="m")]
[name="烈夏"]我？我就快二十了。
[charslot(slot="m",name="avg_npc_1160_1#6$1",focus="m")]
[name="老修士"]......
[name="老修士"]你可是谢拉格人？
[charslot(slot="m",name="avg_194_leto_1#1$1",focus="m")]
[name="烈夏"]老

... (全文19765字符)
```

### level_act30side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="45_g5_victoriabarracks_c",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1157_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_408_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1157_1#1$1",focus="l")]
[name="老练的士兵"]葫芦！
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="油滑的士兵"]同花顺！
[charslot(slot="l",name="avg_npc_1157_1#1$1",focus="l")]
[name="老练的士兵"]*维多利亚粗口*，你小子是不是藏牌了？
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="油滑的士兵"]对付你还用得着藏牌？得了，乖乖——
[Dialog]
[charslot]
[playsound(key="$d_avg_stickknock",volume=0.6)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="沉默的士兵"]皇家同花顺。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]*维多利亚俚语*，怎么可能？！
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="沉默的士兵"]杰克，你的袖子。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]啊？我——你怎么发现的？
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]杰克，你这*维多利亚名词*，你骗我！
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]你没发现，那就是你的问题。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]*维多利亚问候语*。
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="沉默的士兵"]洗牌。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]得了，洗牌洗牌。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]啧，老子真是倒了霉，今天跟你一起轮班。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_shufflecards",volume=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]跟谁轮班还不都是打牌，弟兄们有几个打牌不会出千，你数数吧。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]哼。
[name="老练的士兵"]不过，这日子过得倒还真是悠哉。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]你还别说，老大当时说要带我们来观光的时候，我是真不信。
[name="油滑的士兵"]结果来了一个月，我现在信了。
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="沉默的士兵"]吃得也好，喝得也好。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]可不是，我感觉我的胃口都回到刚入伍那时候了。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="n")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="虚弱的士兵"]嘶——啊！！！
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]查理斯，你鬼叫什么呢，吓我一跳！
[Dialog]
[charslot]
[name="虚弱的士兵"]*维多利亚俚语*，我又做噩梦了。
[name="虚弱的士兵"]梦见我被萨卡兹一剑砍成两半。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]嘁，我还以为多大事呢。我前天还梦到自己侦察的时候被源石炸药炸得粉碎呢。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="n")]
[name="虚弱的士兵"]我现在就想找块炸药塞你嘴里。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]你赶紧去。
[name="油滑的士兵"]一个上了战场比*维多利亚粗口*血魔还疯的家伙，下了战场比谁都矫情。
[Dialog]
[charslot]
[name="虚弱的士兵"]我有什么办法，我又不能控制做不做噩梦。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]往好了想，你上次说你是被砍成肉沫，这次只是被砍成两半。
[name="老练的士兵"]说不定是好兆头呢。
[Dialog]
[charslot]
[name="虚弱的士兵"]......*维多利亚粗口*，还挺有道理。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]得了，喝一口起来打牌。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]哦，你醒了正好，来替我打几局。
[Dialog]
[charslot]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[charslot(slot="m",name="avg_npc_414_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="虚弱的士兵"]怎么，有事？
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]......没什么，山下有个农民家里缺干农活的，我去帮个忙。
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="虚弱的士兵"]农民？
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="沉默的士兵"]经常给我们送奶的那一户，老图里尔。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]哦，我记起来了，那户人家的女儿挺漂亮的。
[name="油滑的士兵"]啧啧，看不出来啊，里斯本。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]......只是去帮个忙，别想多了。
[Dialog]
[charslot]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_walk_stage")]
[charslot(slot="m",name="avg_4114_harold_1#15$1",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_4114_harold_1#15$1",focus="m")]
[name="哈洛德"]干什么呢，隔几百米都能听到你们一群老油子嚷嚷。
[name="哈洛德"]挺有本事啊你们几个，军营都要成你们的棋牌室了。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]这不是您老人家一开始就跟我们说是来观光的吗。
[name="油滑的士兵"]我们这叫遵守命令。
[charslot(slot="m",name="avg_4114_harold_1#15$1",focus="m")]
[name="哈洛德"]我还让你们去给当地人做做亲善工作，免得别人觉得我们是一群坏种，你们去了？
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]里斯本这不正要去吗，我看他别说去了，都想在这成家了。
[charslot(slot="m",name="avg_4114_harold_1#12$1",focus="m")]
[name="哈洛德"]哦？
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]头儿，别听他胡扯，就是去帮个忙。
[name="老练的士兵"]毕竟咱们终究是来......
[charslot(slot="m",name="avg_4114_harold_1#15$1",focus="m")]
[name="哈洛德"]别废话。
[name="哈洛德"]滚吧，什么时候轮到你操心了？
[name="哈洛德"]你小子要真能成家，还算你有本事了。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]是！
[Dialog]
[PlaySound(key="$d_avg_walkfast",volume=0.7)]
[charslot(duration=0.5)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]头儿，你身上的味儿可真重。
[name="油滑的士兵"]又去锻炼你那兽医技术了？
[charslot(slot="m",name="avg_4114_harold_1#12$1",focus="m")]
[name="哈洛德"]别提了，老雷昂家的莉莉早产了。
[name="哈洛德"]我没赶上，只能去帮忙做一些产后护理。
[charslot(slot="m",name="avg_4114_harold_1#3$1",focus="m")]
[name="哈洛德"]唉，还遇到个晦气的家伙。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]晦气？
[charslot(slot="m",name="avg_4114_harold_1#12$1",focus="m")]
[name="哈洛德"]老乡。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]老乡？我这一个月见到的来观光的维多利亚人没有一千也有八百了。
[charslot(slot="m",name="avg_4114_harold_1#1$1",focus="m")]
[name="哈洛德"]行了，就你最爱上街溜达。
[name="哈洛德"]发牌发牌。
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="沉默的士兵"]我来。
[Dialog]
[PlaySound(key="$d_

... (全文24737字符)
```

### level_act30side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g10_manorhouse",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[name="魏斯"]老爷，是我。
[charslot(slot="m",name="avg_172_svrash_1#1$1",focus="m")]
[name="恩希欧迪斯"]进来。
[Dialog]
[charslot]
[delay(time=0.2)]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(slot="m",name="avg_198_blackd_1#6$1",duration=1)]
[delay(time=2.5)]
[Dialog]
[charslot]
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[charslot(slot="r",name="avg_198_blackd_1#6$1",focus="l")]
[name="恩希欧迪斯"]发生了什么？
[charslot(slot="r",name="avg_198_blackd_1#6$1",focus="r")]
[name="魏斯"]哈洛德子爵托我给您送一封信。
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]那位子爵？
[charslot(slot="l",name="avg_172_svrash_1#5$1",focus="l")]
[name="恩希欧迪斯"]看来他果然对我安排你去军营盯梢的事一清二楚。
[charslot(slot="r",name="avg_198_blackd_1#6$1",focus="r")]
[name="魏斯"]怪我暴露了行踪，老爷，这会不会有什么影响？
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]无妨，你继续说。
[name="恩希欧迪斯"]他是怎么找上你的？
[charslot(slot="r",name="avg_198_blackd_1#6$1",focus="r")]
[name="魏斯"]是！
[name="魏斯"]今天下午......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[cameraEffect(effect="Grayscale", keep=true, amount=0.7, fadetime=0)]
[Background(image="24_g12_mountpath", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_198_blackd_1#8$1")]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_198_blackd_1#8$1",focus="m")]
[name="魏斯"]现在是下午五时，开始记录今天的情况。
[name="魏斯"]今天的情况和过去没有太大的差别。
[name="魏斯"]感染者营的士兵例行前往附近的山上演习。
[name="魏斯"]说是演习，实际上和散心没什么区别。
[name="魏斯"]非感染者营的士兵则自由行动。
[name="魏斯"]自由行动的内容十分繁杂，不方便一一记录，根据之前的调查，大体上都是在山下吃喝玩乐。
[name="魏斯"]营地依然是四人轮班放哨，其中三人在打牌，一人睡觉。
[name="魏斯"]睡觉的士兵醒来后，其余三人中的一人离开了，走的时候很开心。
[name="魏斯"]根据老图里尔的意思，大概是喜欢上了他的女儿......
[name="魏斯"]......
[Dialog]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_198_blackd_1#6$1",focus="m")]
[name="魏斯"]这群维多利亚人来了快一个月了。
[name="魏斯"]虽然是我主动申请来监视的，但我现在越来越怀疑，监视他们真的有意义吗......
[name="魏斯"]这帮人，简直就像是真的来观光一样......
[name="魏斯"]对了。
[Dialog]
[PlaySound(key="$d_avg_devicebeep", volume=1)]
[Delay(time=0.5)]
[name="魏斯"]期间哈洛德子爵返回了营地与放哨的士兵打牌，但是后来不知所踪......
[charslot(slot="m",name="avg_198_blackd_1#6$1",focus="n")]
[name="哈洛德"]哦，贴心的哈洛德觉得放魏斯先生孤身一人在山上，未免有些太可怜了。
[name="哈洛德"]所以给他带了点酒。
[charslot(slot="m",name="avg_198_blackd_1#5$1",focus="m")]
[name="魏斯"]......？！
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot="m",name="avg_4114_harold_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_4114_harold_1#1$1",focus="m")]
[name="哈洛德"]别紧张，先生。
[name="哈洛德"]每天都要监视我们，确实是辛苦你了。
[name="哈洛德"]不过我也能理解，毕竟一支军队驻扎在这里，不稍微留个心眼，那你们的恩希欧迪斯老爷也未免有些太看不起维多利亚了。
[name="哈洛德"]我带了点酒，喝一杯暖暖身子吧。
[charslot(slot="m",name="avg_198_blackd_1#6$1",focus="m")]
[name="魏斯"]......
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=0.7)]
[PlaySound(key="$d_avg_devicebeep", volume=0.6,delay=0.7)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_198_blackd_1#6$1",focus="m")]
[name="魏斯"]抱歉，我有些酒精过敏。
[charslot(slot="m",name="avg_4114_harold_1#4$1",focus="m")]
[name="哈洛德"]是吗？那太可惜了。我年轻的时候也不喜欢喝酒，觉得自己清醒的时候什么事情都做得到。
[name="哈洛德"]哎呀，现在倒是能理解它的迷人之处啦。
[charslot(slot="m",name="avg_198_blackd_1#6$1",focus="m")]
[name="魏斯"]......子爵阁下，您就直说吧，您找我想做什么？
[charslot(slot="m",name="avg_4114_harold_1#1$1",focus="m")]
[name="哈洛德"]小事一桩，只需要魏斯先生帮一个小小的忙。
[name="哈洛德"]我希望你能帮我给恩希欧迪斯老爷递一封信。
[charslot(slot="m",name="avg_198_blackd_1#8$1",focus="m")]
[name="魏斯"]......我知道了，我会送到。
[charslot(slot="m",name="avg_4114_harold_1#16$1",focus="m")]
[name="哈洛德"]哦？你不问为什么？
[charslot(slot="m",name="avg_198_blackd_1#8$1",focus="m")]
[name="魏斯"]......您已经出现在这里，我的监视并没有逃过你们的视线。
[name="魏斯"]而您主动点破，这本身就意味着某种态度。
[name="魏斯"]连同这封信，我会把您的态度也告知老爷。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="24_g10_manorhouse", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_172_svrash_1#1$1")]
[charslot(slot="r",name="avg_198_blackd_1#6$1")]
[Delay(time=1.5)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_198_blackd_1#6$1",focus="r")]
[name="魏斯"]抱歉，老爷，要是我的侦察技术能再精进一些......
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]无妨，不管怎么说，对方都是维多利亚正规军。
[name="恩希欧迪斯"]我们与他们存在客观上的实力差距。
[name="恩希欧迪斯"]按你的步调行事就好。
[charslot(slot="r",name="avg_198_blackd_1#6$1",focus="r")]
[name="魏斯"]......我明白。
[charslot(slot="l",name="avg_172_svrash_1#2$1",focus="l")]
[name="恩希欧迪斯"]况且，确实如你所说，他想要通过你传递的，是一个态度。
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]你监视他们的营地已经将近一个月了。
[name="恩希欧迪斯"]说说你对他们的看法，魏斯。
[charslot(slot="r",name="avg_198_blackd_1#8$1",focus="r")]
[name="魏斯"]好的。
[Dialog]
[charslot]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_198_blackd_1#8$1",focus="m")]
[name="魏斯"]在维多利亚军队踏入图里卡姆的关口之前，我们做了许多准备。
[name="魏斯"]但这些准备完全没有用上。
[name="魏斯"]他们来势汹汹，仿佛明天就要占领谢拉格。
[name="魏斯"]但是等他们真的来了，却像现在这样，驻扎在山下毫无动静。
[charslot(slot="m",name="avg_198_blackd_1#2$1",focus="m")]
[name="魏斯"]这位子爵......
[charslot(slot="m",name="avg_198_blackd_1#8$1",focus="m")]
[name="魏斯"]他把军营刻意设在了远离各大核心城镇的位置，为的是尽量不对民众造成威慑。
[name="魏斯"]他的军营中特意区分了感染者和非感染者的营地，还插了告示，让来人多加注意。
[name="魏斯"]并且根据我探听到的情报，他还给部下下令，要求他们多帮本地人的忙。
[charslot(slot="m",name="avg_198_blackd_1#2$1",focus="m")]
[multil

... (全文31820字符)
```

### level_act30side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g8_nobleroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)] 
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_254_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[name="阿克托斯"]嘶......
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_254_1#9$1")]
[name="阿克托斯"]怎么回事......？地上怎么这么多空酒瓶子？
[name="阿克托斯"]......怪了，我怎么会睡在会客厅地板上？
[Dialog]
[charslot]
[name="老修士"]罗莎琳......好孩子......
[name="老修士"]......阿克托斯......这个......混账东西......
[name="老修士"]（鼾声）
[charslot(slot="m",name="avg_npc_254_1#6$1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, block=false)]
[name="阿克托斯"]爹？！
[Dialog]
[charslot]
[name="老修士"]嗯？呃......
[Dialog]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_1160_1#9$1",duration=1.5)]
[Delay(time=2.5)]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, block=false)]
[name="老修士"]吵什么！连个安稳觉都不让人睡！
[charslot(slot="m",name="avg_npc_1160_1#10$1")]
[name="老修士"]不对，慢着，我这是......
[charslot(slot="m",name="avg_npc_254_1#6$1")]
[name="阿克托斯"]爹！您什么时候回来的，怎么也不提前让人带话说一声？
[name="阿克托斯"]昨天这是怎么回事，咱们怎么都睡到地上去了？
[charslot(slot="m",name="avg_npc_1160_1#8$1")]
[name="老修士"]......别瞎嚷嚷，吵得我头疼。
[Dialog]
[charslot]
[playsound(key="$d_avg_open_door",channel="1",volume=0.6)]
[Delay(time=0.5)]
[playsound(key="$rungeneral",channel="2")]
[charslot(slot="m",name="avg_npc_260_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="古罗"]老爷，还有大老爷。
[name="古罗"]太好了，你们可算醒了！
[charslot(slot="m",name="avg_npc_254_1#1$1")]
[name="阿克托斯"]古罗！
[name="阿克托斯"]昨天这是怎么回事？
[charslot(slot="m",name="avg_npc_260_1#1$1")]
[name="古罗"]昨天老爷和大老爷都喝醉了，说是要不醉不休，说什么都不愿意回房间睡，我们怎么劝都不成。
[name="古罗"]我没办法，只好往炉子里多添了两把柴，这样至少不会冷着。
[name="古罗"]老爷，昨天的事你不记得了？
[charslot(slot="m",name="avg_npc_254_1#9$1")]
[name="阿克托斯"]我......等会，你让我想想。
[charslot(slot="m",name="avg_npc_254_1#2$1")]
[name="阿克托斯"]昨天，昨天......
[Dialog]
[Delay(time=1)]
[name="阿克托斯"]我记得，昨天我是要给耶拉冈德像落成仪式的前夜晚会做准备。
[Dialog]
[Delay(time=1)]
[name="阿克托斯"]圣女大人让我选出谢拉格最好的酒水，用来招待来客，所以我就挨个尝了尝......
[Dialog]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_254_1#9$1")]
[name="阿克托斯"]然后，然后我就不大记得了。
[charslot(slot="m",name="avg_npc_1160_1#9$1")]
[name="老修士"]哼，你自然是不记得了。
[name="老修士"]你喝得烂醉连人都分不清，还抱着柱子要和人家干杯。
[name="老修士"]都多大年纪了，丢人！
[charslot(slot="m",name="avg_npc_254_1#6$1")]
[name="阿克托斯"]行了，爹，我这不也是为了圣女大人，为了谢拉格吗！
[name="阿克托斯"]古罗还在这呢，你少骂我两句，给我留点面子。
[charslot(slot="m",name="avg_npc_1160_1#8$1")]
[name="老修士"]我从来都教你，面子里子都是自己挣的，光要我给你留有什么用！
[charslot(slot="m",name="avg_npc_1160_1#1$1")]
[name="老修士"]......算了，先不和你计较。
[name="老修士"]古罗，怎么没瞧见罗莎琳？
[charslot(slot="m",name="avg_npc_260_1#1$1")]
[name="古罗"]大老爷，罗莎琳小姐一早就上山去了。
[charslot(slot="m",name="avg_npc_1160_1#6$1")]
[name="老修士"]什么？！
[charslot(slot="m",name="avg_npc_260_1#1$1")]
[name="古罗"]罗莎琳小姐醒得早，老爷和大老爷那会都还没醒，小姐就说，干脆让你们再睡会儿。
[name="古罗"]我想着也是，就没喊。
[charslot(slot="m",name="avg_npc_1160_1#7$1")]
[name="老修士"]......
[name="老修士"]她就这样走了，也好。
[charslot(slot="m",name="avg_npc_1160_1#1$1")]
[name="老修士"]或许，或许这就是耶拉冈德为我佩尔罗契家做出的安排。
[charslot(slot="m",name="avg_npc_1160_1#7$1")]
[name="老修士"]见面不识，这是缘分未够，缘分未够啊......
[charslot(slot="m",name="avg_npc_254_1#4$1")]
[name="阿克托斯"]爹，你这又打什么哑谜呢？！
[charslot(slot="m",name="avg_npc_254_1#9$1")]
[name="阿克托斯"]我隐约记得昨天是来了个小丫头没错，不过我确实是醉得不轻，不大想得起来那丫头的长相了。
[name="阿克托斯"]你们说，那丫头叫罗莎琳？这名字......
[charslot(slot="m",name="avg_npc_1160_1#1$1")]
[name="老修士"]......
[name="老修士"]阿克托斯，你过来。
[Dialog]
[charslot]
[Delay(time=0.7)]
[playsound(key="$d_avg_clothmovement")]
[stopmusic(fadetime=1.5)]
[charslot(slot="r",name="avg_npc_254_1#4$1",duration=1.5)]
[charslot(slot="l",name="avg_npc_1160_1#12$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1160_1#12$1",focus="l")]
[name="老修士"]此事，我不该瞒你。
[name="老修士"]便如当初，亦是你自己做了选择一般。
[name="老修士"]如今该如何做，终究需你自己决断。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_283_1#1$1",bstart=0.2,bend=0.7,duration=1.5)]
[Delay(time=2.5)]
[name="护卫？"]......耶拉冈德在上。
[name="护卫？"]这祖孙三代真的就喝了整整一宿。
[name="护卫？"]还把我和其他护卫一起拉上。
[name="护卫？"]嘶——
[name="护卫？"]好久没有喝过这么多酒了。
[name="护卫？"]而且，真的一点正事都没说......
[Dialog]
[playsound(key="$d_avg_clothmovementsp")]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="“灰礼帽”"]......既然侧面行不通，那么，干脆从正面来吧。
[name="“灰礼帽”"]看这个方向，罗莎琳小姐是往山上去了。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
[Delay(time=4)]
[Background(image="24_g12_mountpath",screenadapt="showall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_snowrun")]
[charslot(slot="m",name="avg_194_leto_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="烈夏"]哦——这就是雪山啊——！
[charslot(slot="m",name="avg_194_leto_1#8$1")]
[name="烈夏"]近看比远看还要更壮观，谢拉格的山还是有点真本事的嘛。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.05, block=true)]
[CameraShake(duration=0.8, xstrength=20, ystrength=20, vibrato=30, randomness=90, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
[charslot(slot="m",name="avg_194_leto_1#2$1")]
[name="烈夏"]呃，有点头晕，昨天真的喝多了。
[charslot(slot="m",name="avg_194_leto_1#8$1")]
[name="烈夏"]不知道那老伯和大叔醒了没有，博士怎么没告诉我，谢拉格人竟然这么热情？
[name="烈夏"]等回头下山，再送点什么过去做谢礼吧......
[Dialog]
[charslot(slot ="m", action="shake", power=10, times=30, duration=0.3)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_194_leto_1#7$1")]
[name="烈夏"]嘶，真冷，这风刮得人身上怪疼的。
[name="烈夏"]我记得......这山好像是得自己爬上去，才是对耶拉冈德信仰虔诚来着？
[n

... (全文23199字符)
```

### level_act30side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="24_g12_mountpath",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)] 
[name="烈夏"]拉住我的手。
[name="烈夏"]嗬——哈！
[name="烈夏"]好！
[Dialog]
[playsound(key="$d_avg_snowbodyfall")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, block=true)]
[Delay(time=1)]
[playMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="“灰礼帽”"]之前在列车上有过一面之缘，没想到在这里还会被您所救。
[name="“灰礼帽”"]多亏了您伸出援手，否则我不知还要在这里被困多久。
[name="“灰礼帽”"]我很感谢，罗莎琳·塔季扬诺夫娜·拉里娜小姐，感谢您的无私帮助。
[charslot(slot="m",name="avg_194_leto_1#9$1")]
[name="烈夏"]......唔，小事，不用谢。
[name="烈夏"]你看起来肯定不是本地人，上山应该也是来旅游的？
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]正是。
[charslot(slot="m",name="avg_194_leto_1#9$1")]
[name="烈夏"]那你怎么不沿着大路走，跑到这种林子里来不说，还掉进人家打猎挖的陷阱里？
[name="烈夏"]万一我没正好路过，你打算怎么办？
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]我只是被山间的景色吸引，没有想到积雪之下会有这样的陷阱。
[name="“灰礼帽”"]如果没有您路过解救......那我正好可以多待一会。冷静一下，再想办法自己爬出去。
[name="“灰礼帽”"]不过现在看来，我还是幸运的。
[charslot(slot="m",name="avg_194_leto_1#7$1")]
[name="烈夏"]唔......
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]罗莎琳小姐，您是要继续上山吗？
[charslot(slot="m",name="avg_194_leto_1#9$1")]
[name="烈夏"]嗯？对，没错。
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]如果您不介意，我们可以同行一段。
[name="“灰礼帽”"]我也想要欣赏一番谢拉格雪山山顶的风光。
[charslot(slot="m",name="avg_194_leto_1#8$1")]
[name="烈夏"]......好啊。
[name="烈夏"]我不介意，那我们走吧。
[name="烈夏"]距离山顶还有好一段路程呢。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]刚刚那是......
[charslot(slot="m",name="avg_npc_277_1#1$1",focus="m")]
[name="谢拉格青年"]莱利老爹！
[name="谢拉格青年"]我检查过了，咱们布置在这附近的陷阱被踩塌了一个，应该是有猎物掉进去过！
[name="谢拉格青年"]但我看的时候里头啥也没有，估计是又给逃了。
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]你看到刚刚过去的那人没有？你看他，像不像图里尔那老小子说要找的那人？
[charslot(slot="m",name="avg_npc_277_1#1$1",focus="m")]
[name="谢拉格青年"]你是说，是锏小姐拜托我们找的那个......
[charslot(slot="m",name="avg_npc_279_1#1$1",focus="m")]
[name="谢拉格老人"]穿得乌漆嘛黑、装模作样的，戴着帽子还遮着脸，错不了！
[name="谢拉格老人"]走！咱们回去，赶紧把这事告诉锏小姐！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_snowbootwalk")]
[charslot(slot="m",name="avg_194_leto_1#9$1",duration=1.5)]
[Delay(time=2.5)]
[name="烈夏"]......
[name="烈夏"]喂，那个谁......对了，我还不知道你叫什么名字。
[name="烈夏"]你们不是都讲究什么，见面要先互相告知姓名吗？
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]这是我疏忽了。
[name="“灰礼帽”"]鄙人名叫约翰·史密斯，随便您怎么称呼都可以。
[charslot(slot="m",name="avg_194_leto_1#13$1")]
[name="烈夏"]约翰......？
[name="烈夏"]你这名字......
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“约翰·史密斯”"]名字如何？
[charslot(slot="m",name="avg_194_leto_1#1$1")]
[name="烈夏"]你这名字......听起来和之前博士看的什么间谍电影的主人公似的！
[name="烈夏"]对，我没记错，就是这个名字！
[name="烈夏"]我记得主人公还有个大美女搭档，约翰你......算了，看你能一个人来这种情侣景点，就知道你肯定没对象。
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“约翰·史密斯”"]......
[name="“约翰·史密斯”"]真是个有趣的巧合。
[charslot(slot="m",name="avg_194_leto_1#8$1")]
[name="烈夏"]对吧！
[name="烈夏"]好了约翰，言归正传，我们估计还要爬一会才能到山顶。
[name="烈夏"]我听人说过，雪山越往上就越冷，而且还会让人越来越喘不上气。
[charslot(slot="m",name="avg_194_leto_1#1$1")]
[name="烈夏"]怎么样，你累不累？要不要休息一下？
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“约翰·史密斯”"]请不必担心我。
[name="“约翰·史密斯”"]罗莎琳小姐需要休息一下吗？
[charslot(slot="m",name="avg_194_leto_1#8$1")]
[name="烈夏"]我就不用了。
[charslot(slot="m",name="avg_194_leto_1#1$1")]
[name="烈夏"]看来你的体力不错，“间谍先生”。
[Dialog]
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[Delay(time=1)]
[name="“约翰·史密斯”"]......哈哈。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="24_g12_mountpath",screenadapt="showall")]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_snowbootwalk")]
[charslot(slot="l",name="avg_4116_blkkgt_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[CharacterCutin(widgetID="1", name="avg_172_svrash_1#1$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=350, width=300, block=true)]
[playsound(key="$d_gen_transmissionget")]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_4116_blkkgt_1#2$1")]
[name="锏"]看来，他确实被你骗到了。
[Dialog]
[charslot(slot="l",name="avg_4116_blkkgt_1#2$1",focus="none")]
[CharacterCutin(widgetID="1", name="avg_172_svrash_1#2$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=350, width=300, block=true)]
[name="恩希欧迪斯"]我并没有编造谎言，锏。
[CharacterCutin(widgetID="1", name="avg_172_svrash_1#1$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=350, width=300, block=true)]
[name="恩希欧迪斯"]“灰礼帽”是为公爵搜集情报的密探，一般的谎言瞒不过他们。
[name="恩希欧迪斯"]但我深知，这种人往往最懂得“猜忌”。
[name="恩希欧迪斯"]“佩尔罗契家的继承人秘密归国”，这是他自己最先发现的事实，所以他一定会相信。
[name="恩希欧迪斯"]对方一定会盯上罗莎琳·塔季扬诺夫娜·拉里娜。
[charslot(slot="l",name="avg_4116_blkkgt_1#7$1")]
[name="锏"]你总能猜对。
[name="锏"]那女孩已经上山，菈塔托丝也联系了阿克托斯。
[charslot(slot="l",name="avg_4116_blkkgt_1#11$1")]
[name="锏"]我接到消息，那个“灰礼帽”也跟上去了。
[charslot(slot="l",name="avg_4116_blkkgt_1#1$1")]
[name="锏"]他在躲着我。
[charslot(slot="l",name="avg_4116_blkkgt_1#1$1",focus="none")]
[CharacterCutin(widgetID="1", name="avg_172_svrash_1#2$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=350, width=300, block=true)]
[name="恩希欧迪斯"]无妨。
[CharacterCutin(widgetID="1", name="avg_172_svrash_1#1$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=350, width=300, block=true)]
[name="恩希欧迪斯"]确认他将注意力放在那女孩身上就够了。
[name="恩希欧迪斯"]你

... (全文14605字符)
```

### level_act30side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_white",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)] 
[Subtitle(text="<color=#000000>罗莎琳是坏孩子！</color>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<color=#000000>她没有爸爸，我们不要和她一起玩，她是个怪胎！</color>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<color=#000000>哈哈哈，罗莎琳是没爸爸的坏孩子！</color>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
我才不是坏孩子！
你们、你们不许乱说......！
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Subtitle(text="<color=#000000>哎哟！她、她动手打人！她就是坏孩子！</color>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<color=#000000>上！我们揍她！</color>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="<color=#000000>揍她！</color>", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
打就打，谁怕谁！
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
我不是坏孩子！
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_punch02",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
我有妈妈就够了，才不需要爸爸！
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_punch",volume=1)] 
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
才不需要......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=3)]
[Background(image="bg_iceforest_1",screenadapt="showall")]
[bgeffect(name="$eb_dim_openeye",layer=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=3)]
[bgeffect]
[playsound(key="$d_avg_crwdkneelsnow",volume=1)]
[charslot(slot="m",name="avg_194_leto_1#2$1",duration=1.5)]
[Delay(time=2)]
[name="烈夏"]哈......
[name="烈夏"]没想到从上头摔下来，竟然误打误撞，让我给找到了。
[charslot(slot="m",name="avg_194_leto_1#7$1")]
[name="烈夏"]双生树......原来是藏在这儿。
[charslot(slot="m",name="avg_194_leto_1#9$1")]
[name="烈夏"]真的是两棵树长在一起，应该没错。
[Dialog]
[charslot]
[playsound(key="$d_avg_snowfootstep",volume=1,channel="1")]
[Delay(time=2.5)]
[stopsound(channel="1")]
[charslot(slot="m",name="avg_194_leto_1#9$1")]
[name="烈夏"]......
[name="烈夏"]好......这样就行了。
[charslot(slot="m",name="avg_194_leto_1#7$1")]
[name="烈夏"]老妈的事算是办完了，现在......
[Dialog]
[charslot(duration=1.5)]
[Delay(time=2)]
[playsound(key="$d_avg_snowbodyfall",volume=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, block=false)]
[Delay(time=2)]
[playsound(key="$d_avg_crwdkneelsnow",volume=1)]
[charslot(slot="m",name="avg_194_leto_1#12$1",duration=1.5)]
[Delay(time=2)]
[name="烈夏"]嘁！
[name="烈夏"]还是不行，爬不上去。
[name="烈夏"]这里的积雪太厚，山壁太陡，徒手爬不上去。
[charslot(slot="m",name="avg_194_leto_1#7$1")]
[name="烈夏"]只剩下这边的断崖......
[charslot(slot="m",name="avg_194_leto_1#7$1",focus="none")]
[name="阿克托斯"]等等，罗莎琳！
[Dialog]
[charslot]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_254_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[name="阿克托斯"]咳、咳咳！
[name="阿克托斯"]别太靠近那边，小心危险！
[charslot(slot="m",name="avg_194_leto_1#14$1")]
[name="烈夏"]行，行，我不过去，你别乱动！
[charslot(slot="m",name="avg_194_leto_1#13$1")]
[name="烈夏"]你的腿还动不了吧？别逞强，先坐着歇会。
[charslot(slot="m",name="avg_npc_254_1#13$1")]
[name="阿克托斯"]没那么严重，我总不能让你摔着。
[charslot(slot="m",name="avg_npc_254_1#8$1")]
[name="阿克托斯"]这帮维多利亚来的混账竟然把主意打到你身上，这事不能就这么完了！
[charslot(slot="m",name="avg_194_leto_1#13$1")]
[name="烈夏"]所以那家伙真是维多利亚的间谍？
[charslot(slot="m",name="avg_194_leto_1#7$1")]
[name="烈夏"]其实......他也没把我怎么样。
[charslot(slot="m",name="avg_npc_254_1#7$1")]
[name="阿克托斯"]等到真出事可就太迟了！
[charslot(slot="m",name="avg_npc_254_1#8$1")]
[name="阿克托斯"]如果不是时机不对，我一定要揍到他再也不敢踏进我佩尔罗契家的领地！
[charslot(slot="m",name="avg_194_leto_1#4$1")]
[name="烈夏"]要不是大叔你突然出现，我本来就打算把那家伙绑起来教训一顿的！
[charslot(slot="m",name="avg_194_leto_1#9$1")]
[name="烈夏"]算了，不提这个。
[name="烈夏"]你刚刚，那个......
[charslot(slot="m",name="avg_194_leto_1#4$1")]
[name="烈夏"]啧，我最烦拖拖拉拉磨磨蹭蹭的，我就直接问了！
[name="烈夏"]那啥，刚刚摔下来的时候，你为什么要给我垫背？
[name="烈夏"]还有那个维多利亚来的，他说的什么身份，你知道是什么意思吗？
[charslot(slot="m",name="avg_npc_254_1#14$1")]
[name="阿克托斯"]......
[name="阿克托斯"]罗莎琳。
[charslot(slot="m",name="avg_npc_254_1#12$1")]
[name="阿克托斯"]我知道现在说这些，你可能不好接受，但是......
[name="阿克托斯"]我和塔季扬娜——
[charslot(slot="m",name="avg_npc_254_1#14$1")]
[name="阿克托斯"]......我和你母亲，就是在这座山的山顶认识的。
[charslot(slot="m",name="avg_194_leto_1#14$1")]
[name="烈夏"]和老妈......你的意思是，你是......
[charslot(slot="m",name="avg_npc_254_1#14$1")]
[name="阿克托斯"]就是你想的那样。
[name="阿克托斯"]罗莎琳，你是我的女儿。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="45_g11_karlanheadquarters",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadeti

... (全文21475字符)
```

### level_act30side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_iceforest_1",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[bgeffect(name="$eb_snow",layer=1)]
[PlaySound(key="$blizzard",channel="bgs", volume=0.3, loop=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)] 
那是二十多年前的事了。
我记得那年的冬天比往年都要冷，雪下个没完，风也大，像是能把人刮走一样。
那种天气，没人愿意出门。
人们都窝在自家，不分白天夜里，不熄火炉，炉子上放着热茶，这样就随时能喝上一口热乎的。
驮兽棚子也都在入冬前特地加厚了，驮兽都缩在一起打盹，整日睡不清醒。
那年的谢拉格，好像时间都变慢了。就觉着好不容易挨过一天，第二天却还是那个风雪满天的冬天。
我那时候还年轻，受不了这样过日子。那天我偷偷带了几个人，打算上山去打猎。
可雪实在太大了，一路上找不到猎物，我和其他人在中途失散，只能拼着一口气继续往山上走......
然后，就是在这......
......我在这遇见了塔季扬娜。
[Dialog]
[Delay(time=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=2, block=true)]
[stopsound(fadetime=1.5,channel="bgs")]
[CameraEffect(effect="Grayscale", fadetime=2, amount=0, block=false)]
[Background(image="bg_iceforest_2",screenadapt="coverall",fadetime=1.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[bgeffect(layer=1,fadetime=1.5)]
[Delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2.5, block=true)]
[Delay(time=2.5)]
[playsound(key="$d_avg_snowbootwalk")]
[Delay(time=1.5)]
[name="阿克托斯"]嘁，这破天气！
[name="阿克托斯"]连根肉兽的毛都没捞着，老爹肯定又要说我......
[Dialog]
[playsound(key="$leaveshake")]
[Delay(time=2)]
[name="阿克托斯"]嗯？
[name="阿克托斯"]什么声音......
[Dialog]
[playsound(key="$leaveshake",channel="1")]
[Delay(time=1)]
[StopSound(channel="1")]
[name="阿克托斯"]哈！什么人？！
[multiline(name="阿克托斯")]装神弄鬼！有本事就给小爷出来——
[playsound(key="$d_avg_snowfootstep",channel="1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=30, randomness=90, block=false)]
[StopSound(channel="1")]
[multiline(name="阿克托斯")]哎哟！
[Dialog]
[Dialog]
像是在回应阿克托斯的话，一团雪球自头顶的树枝上落下，砸在他的头上。
一个清亮的女声自上方响起。
[name="？？？"]哈哈哈，砸中啦~
[name="？？？"]嘿，我在这呢。
[name="？？？"]傻大个，你怎么也不知道躲躲？
[name="阿克托斯"]你、你......！
[name="？？？"]我怎么了？
[name="？？？"]你这人真好玩，这种天气上山，还想着能打到猎物？
[name="？？？"]小少爷，看在你长得漂亮的分上，给你一个忠告。
[name="？？？"]赶快回家吧。
[Dialog]
[Background(image="38_g20_skyblue_L2",screenadapt="coverall",fadetime=2.5)]
[Delay(time=3)]
阿克托斯抬起头。
风雪渐止，明亮的日光穿过眼前枝条缠绕的双生树，在他面上落下斑驳的影子。
女性的身姿在一片细雪后若隐若现。
细碎的雪花随着她的动作纷纷扬扬洒落，年轻的塔季扬娜面带笑容，垂首与树下的青年对视。
阿克托斯忽觉眼角干涩。
早已看惯的雪色在这一刻忽然变得刺眼。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot]
那天的日光太明亮了。
[Dialog]
[Delay(time=4)]
[Background(image="45_g9_underkjerastastue",screenadapt="showall")]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_262_1#1$1",duration=1.5,posfrom="-150,0",posto="-150,0")]
[charslot(slot="m",name="avg_174_slbell_1#11$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_250_1#1$1",duration=1.5,posfrom="200,0",posto="200,0")]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_262_1#1$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]圣女大人，您请看！
[charslot(slot="l",name="avg_npc_262_1#10$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]这座耶拉冈德像主体由我布朗陶家负责修建，总高度约三十米，整体由极为坚硬的材料构成，至少未来上百年都不会有损坏的风险。
[name="休露丝"]塑形是由专业匠人配合几百位自愿报名的虔诚信徒共同探讨完成，绝对能够最大限度地还原耶拉冈德的伟岸英姿！
[name="休露丝"]虽然中途大家一度为耶拉冈德到底该不该是人形争吵过......阿克托斯那莽夫还差点和人动手......
[charslot(slot="l",name="avg_npc_262_1#3$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]但我敢保证！这座雕像绝对会是谢拉格今后最惹人注目的奇景！
[charslot(slot="m",name="avg_174_slbell_1#11$1",focus="m")]
[name="恩雅"]嗯，这段时间辛苦各位了。
[Dialog]
[charslot(slot="r",name="avg_npc_250_1#5$1",posfrom="200,0",posto="200,0")]
[Delay(time=1)]
[charslot(slot="m",posfrom="0,0",posto="40,0",duration=0.5)]
[charslot(slot="r",posfrom="200,0",posto="100,0",duration=0.5)]
[Delay(time=0.55)]
[playsound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="r",duration=0.5,action="jump",power=7, times=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_174_slbell_1#12$1",posfrom="40,0",posto="40,0")]
[charslot(slot="r",name="avg_npc_250_1#8$1",posfrom="100,0",posto="100,0")]
[Delay(time=1)]
[charslot(slot="m",name="avg_174_slbell_1#12$1",posfrom="40,0",posto="40,0",focus="m")]
[name="恩雅"]咳......这座耶拉冈德像，是我们谢拉格对外展示的最好的象征之物，能有如今的效果，实在离不开各位的努力。
[charslot(slot="m",name="avg_174_slbell_1#11$1",posfrom="40,0",posto="40,0",focus="m")]
[name="恩雅"]耶拉冈德一定也十分满意。
[Dialog]
[playsound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="r",posfrom="100,0",posto="200,0",duration=2)]
[charslot(slot="m",posfrom="40,0",posto="70,0",duration=2)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_250_1#4$1",posfrom="200,0",posto="200,0")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_174_slbell_1#11$1",posfrom="70,0",posto="70,0",focus="m")]
[name="恩雅"]特别是您和您的姐姐，休露丝夫人。
[name="恩雅"]听闻两位为建造雕像的事务付出良多，一刻不离现场，实在是辛苦了。
[charslot(slot="l",name="avg_npc_262_1#11$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]哼，哼哼......
[charslot(slot="l",name="avg_npc_262_1#11$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]也没什么，分内的事，没什么辛苦的。
[charslot(slot="l",name="avg_npc_262_1#5$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]反正是比被压着读书要轻松多了......
[charslot(slot="m",name="avg_174_slbell_1#5$1",posfrom="70,0",posto="70,0",focus="m")]
[name="恩雅"]读书？
[charslot(slot="l",name="avg_npc_262_1#4$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]没有没有，没什么。
[charslot(slot="l",name="avg_npc_262_1#1$1",posfrom="-150,0",posto="-150,0",focus="l")]
[name="休露丝"]咳嗯，那么圣女大人，我再带您详细参观一下吧。
[name="休露丝"]您请随我来！
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2.5)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_250_1#6$1",duration=1.5)]
[charslot(slot="r",name="avg

... (全文27665字符)
```

### level_act30side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g9_underkjerastastue",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[delay(time=2)] 
[charslot(slot="l",name="avg_npc_262_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_250_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_262_1#1$1",focus="l")]
[name="休露丝"]侍女长，周围的人都已经疏散了，你怎么还留在这里？
[charslot(slot="r",name="avg_npc_250_1#2$1",focus="r")]
[name="雅儿"]休露丝夫人才是，您不是应该已经回避了吗？
[charslot(slot="l",name="avg_npc_262_1#7$1",focus="l")]
[name="休露丝"]哼，你说回避我就要回避吗？
[name="休露丝"]这座雕像可是所有人的心血，要是出了岔子，我要怎么和其他人交代？
[charslot(slot="r",name="avg_npc_250_1#6$1",focus="r")]
[name="雅儿"]是所有人的心血，还是恩希欧迪斯的心血？
[charslot(slot="l",name="avg_npc_262_1#9$1",focus="l")]
[name="休露丝"]......难怪刚才我就看到圣女大人把你按了回去，看来圣女大人对你说过一些什么。
[charslot(slot="r",name="avg_npc_250_1#2$1",focus="r")]
[name="雅儿"]夫人并不惊讶。
[charslot(slot="l",name="avg_npc_262_1#7$1",focus="l")]
[name="休露丝"]我又不是傻子，圣女大人看起来毫不知情，但她怎么可能真的毫不知情？
[name="休露丝"]只是，以她的立场来说，知道，但又不知道，才是她最应该做的事。
[name="休露丝"]而她现在派你来捅破这层窗户纸，说吧，什么事？
[charslot(slot="r",name="avg_npc_250_1#5$1",focus="r")]
[name="雅儿"]正在靠近这里的人，一个是锏，一个是维多利亚的“灰礼帽”。
[charslot(slot="l",name="avg_npc_262_1#4$1",focus="l")]
[multiline(name="休露丝")]“灰礼帽”？！
[charslot(slot="l",name="avg_npc_262_1#9$1",focus="l")]
[multiline(name="休露丝")]啧，他难道......不，应该不至于......
[Dialog]
[Dialog]
[charslot(slot="l",name="avg_npc_262_1#7$1",focus="l")]
[name="休露丝"]圣女大人是特意留你在这里给我提醒的？
[charslot(slot="r",name="avg_npc_250_1#2$1",focus="r")]
[name="雅儿"]您就当作是这么一回事吧。
[charslot(slot="r",name="avg_npc_250_1#6$1",focus="r")]
[name="雅儿"]雕像这边交给我就好。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="45_g10_iceonlake",screenadapt="showall")]
[playMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_janttck_03",volume=1)] 
[Effect(name="$e_spark_02_large",layer = 2)]
[Effect(name="$e_spark_01_large",layer = 2)]
[Effect(name="$e_spark_02_large",layer = 2)]
[Effect(name="$e_spark_01_large",layer = 2)]
[Effect(name="$e_spark_02_large",layer = 2)]
[Effect(name="$e_spark_01_mid",roy=-90,layer = 3)]
[charslot(slot="r",name="avg_npc_867_1#1$1",posfrom="-200,0",posto="0,0",duration=0.6)]
[charslot(slot="r",afrom=0,ato=1,duration=0.4)]
[charslot(slot="l",name="avg_4116_blkkgt_1#1$1",posfrom="200,0",posto="0,0",duration=0.6)]
[charslot(slot="r",afrom=0,ato=1,duration=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Delay(time=0.8)]
[charslot(slot="l",name="avg_4116_blkkgt_1#1$1",focus="l")]
[name="锏"]到此为止了。
[charslot(slot="r",name="avg_npc_867_1#1$1",focus="r")]
[name="“灰礼帽”"]咳......！
[name="“灰礼帽”"]......不愧是黑骑士，个人实力不容小觑。
[name="“灰礼帽”"]不过如果只是这样，您应该清楚，您是对付不了我的。
[charslot(slot="l",name="avg_4116_blkkgt_1#1$1",focus="l")]
[name="锏"]哦？
[name="锏"]我不讨厌有自信的人。
[charslot(slot="l",name="avg_4116_blkkgt_1#6$1",focus="l")]
[name="锏"]不过，我的耐心有限。
[name="锏"]你来回逃窜的样子，已经开始让我觉得有点无聊了。
[charslot(slot="r",name="avg_npc_867_1#1$1",focus="r")]
[name="“灰礼帽”"]我很抱歉，女士。让您感到无聊是我的失职。
[name="“灰礼帽”"]只不过，恕我直言，锏女士，您的招式中没有杀意。
[multiline(name="“灰礼帽”")]曾经在卡西米尔所向披靡，以一把巨剑令对手闻风丧胆的黑骑士，如今却用着这样没有锋刃的武器——
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$d_avg_twohandedblunt",Delay=0.05,volume=1,channel="2")]
[Delay(time=1.5)]
[multiline(name="“灰礼帽”")]嘶！
[Dialog]
[Dialog]
[charslot(slot="l",name="avg_4116_blkkgt_1#11$1",focus="l")]
[name="锏"]这种没有锋刃的武器对付你足够了。
[name="锏"]用莱塔尼亚的巨剑比赛，是那些商人的诉求。
[charslot(slot="l",name="avg_4116_blkkgt_1#6$1",focus="l")]
[name="锏"]呵，“用巨剑的莱塔尼亚武者”“用不了源石技艺的怪胎”......随便怎么说都行，无所谓。
[name="锏"]但好像时间久了，你们都忘了一件事。
[charslot(slot="l",name="avg_4116_blkkgt_1#3$1",focus="l")]
[name="锏"]最开始我选择锏做武器的理由——
[charslot(slot="r",name="avg_npc_867_1#1$1",focus="r")]
[name="“灰礼帽”"]什么......呃！
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[playsound(key="$d_avg_twohandedblunt",Delay=0.05,volume=1,channel="2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Delay(time=1.5)]
[stopsound(channel="2")]
男人的话被袭面而来的风雪堵回口中。
袭向他的是谢拉格刺骨的寒风，是压面而至的无情山雪，是冰冷而重万钧的长锏。
不容任何反抗。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]——？！
[name="“灰礼帽”"]咳哈......
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]这只是一个警告。
[name="锏"]来找恩希欧迪斯麻烦的人很多，如果每一个都能碾死了事，我的麻烦也会少很多。
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",focus="m")]
[name="锏"]可惜，有些人活着比死去更有用处。
[name="锏"]就比如你。
[charslot(slot="m",name="avg_npc_867_1#1$1",focus="m")]
[name="“灰礼帽”"]咳、咳咳......原来如此。
[name="“灰礼帽”"]看来还要多谢，锏女士手下留情。
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",focus="m")]
[name="锏"]锏。
[charslot(slot="m",name="avg_4116_blkkgt_1#2$1",focus="m")]
[name="锏"]我用它的理由很简单。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]它没有刃，用它，留你们这样的人一条命会变得轻松一点。
[name="锏"]就算是这种没有利刃的武器，只要再多用一点力气，大部分人就会变成一摊肉泥。
[charslot(slot="m",name="avg_4116_blkkgt_1#2$1",focus="m")]
[name="锏"]从以前开始，一直如此。
[charslot(slot="m",name="avg_4116_blkkgt_1#11$1",focus="m")]
[name="锏"]有一些人称得上对手，大多数人却会被轻易碾碎。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1",focus="m")]
[name="锏"]不管是莱塔尼亚的术师，还是卡西米尔的骑士，都没什么不同。
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",focus="m")]
[name="锏"]信念也好，理想也好，

... (全文25259字符)
```

### level_act30side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g9_underkjerastastue",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)] 
[charslot(slot="l",name="avg_npc_250_1#6$1",duration=1.5)]
[charslot(slot="r",name="avg_4116_blkkgt_1#2$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_250_1#6$1",focus="l")]
[name="雅儿"]你打算在这里坐到什么时候？
[charslot(slot="r",name="avg_4116_blkkgt_1#2$1",focus="r")]
[name="锏"]他已经发现了这里，迟早会来的。
[charslot(slot="l",name="avg_npc_250_1#6$1",focus="l")]
[name="雅儿"]他来了，你打算怎么做？
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]杀了他。
[charslot(slot="l",name="avg_npc_250_1#2$1",focus="l")]
[name="雅儿"]杀害外国使节可是重罪。
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]到时候再说。
[charslot(slot="l",name="avg_npc_250_1#6$1",focus="l")]
[name="雅儿"]为什么你不是谢拉格人，却愿意为谢拉格做这么多事？
[charslot(slot="r",name="avg_4116_blkkgt_1#2$1",focus="r")]
[name="锏"]恩希欧迪斯的野心，也是“为了谢拉格”？
[charslot(slot="l",name="avg_npc_250_1#2$1",focus="l")]
[name="雅儿"]到了今天，谁还能否认，他即使有自己的野心，这份野心里也包含了“为了谢拉格”的部分呢？
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]这大概是他最不愿意听到的赞美了。
[charslot(slot="l",name="avg_npc_250_1#6$1",focus="l")]
[name="雅儿"]你还没回答我的问题呢。
[charslot(slot="r",name="avg_4116_blkkgt_1#7$1",focus="r")]
[name="锏"]......
[charslot(slot="r",name="avg_4116_blkkgt_1#11$1",focus="r")]
[name="锏"]当恩希欧迪斯和我提到耶拉冈德或许确实存在时，我想过或许有一天，我可以和所谓的神明交手。
[charslot(slot="r",name="avg_4116_blkkgt_1#2$1",focus="r")]
[name="锏"]现在看来是没指望了。
[charslot(slot="l",name="avg_npc_250_1#8$1",focus="l")]
[name="雅儿"]为什么？
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]毕竟，恩希欧迪斯已经没这个打算了。
[charslot(slot="l",name="avg_npc_250_1#8$1",focus="l")]
[name="雅儿"]如果他有这个打算，你真的会对抗可能真实存在的耶拉冈德吗？
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]也许？
[name="锏"]在这里，只有雪崩的时候才能找些刺激，如果真有这样的机会，我可以尝试一下。
[charslot(slot="l",name="avg_npc_250_1#8$1",focus="l")]
[name="雅儿"]你觉得你会赢？
[charslot(slot="r",name="avg_4116_blkkgt_1#2$1",focus="r")]
[name="锏"]不，即使是对抗雪崩，我也从没赢过。
[charslot(slot="l",name="avg_npc_250_1#6$1",focus="l")]
[name="雅儿"]我懂了，你享受的是挑战的过程。
[name="雅儿"]而正发生在这片土地上的事情，你觉得是值得你挑战的。
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]没你想的那么伟大，我是这么长大的，仅此而已。
[charslot(slot="l",name="avg_npc_250_1#1$1",focus="l")]
[name="雅儿"]......这句话真不错。
[name="雅儿"]回去吧，锏小姐。
[name="雅儿"]你的战场不在这里。
[charslot(slot="r",name="avg_4116_blkkgt_1#10$1",focus="r")]
[name="锏"]......
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]如果这是圣女的意思，恕我难以从命。
[name="锏"]我的战场，由我自己选择。
[charslot(slot="l",name="avg_npc_250_1#1$1",focus="l")]
[name="雅儿"]如果说，这是耶拉冈德的意思呢？
[charslot(slot="r",name="avg_4116_blkkgt_1#10$1",focus="r")]
[name="锏"]......那么，为什么由你来传达耶拉冈德的意思？
[charslot(slot="l",name="avg_npc_250_1#1$1",focus="l")]
[name="雅儿"]我是圣女大人的侍女。
[charslot(slot="r",name="avg_4116_blkkgt_1#10$1",focus="r")]
[name="锏"]你是说，圣女的意思，就是耶拉冈德的意思？
[charslot(slot="l",name="avg_npc_250_1#7$1",focus="l")]
[name="雅儿"]或者说，耶拉冈德会支持圣女大人的想法。
[name="雅儿"]我猜的。
[charslot(slot="r",name="avg_4116_blkkgt_1#1$1",focus="r")]
[name="锏"]......哼。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="“灰礼帽”"]......
[name="“灰礼帽”"]如果黑骑士不是个蠢人，那么，比起四处追我，她一定会守在这里。
[name="“灰礼帽”"]她知道我会回来，就像我也知道我会回来。
[name="“灰礼帽”"]唉，但愿我能活着回去。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="“灰礼帽”"]......
[name="“灰礼帽”"]要是我早一些猜到问题的中心在这里——
[name="“灰礼帽”"]不，我猜不到。又有谁能想到，恩希欧迪斯胆子大到敢把一国之信仰当作自己野心的幌子？
[name="“灰礼帽”"]不愧是被公爵阁下投资的人物。
[name="“灰礼帽”"]而那位圣女，她对这一切真的一点都不了解吗？
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_867_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="“灰礼帽”"]......
[name="“灰礼帽”"]锏呢？
[name="“灰礼帽”"]难道，她真的心大到这种地步？
[Dialog]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.5, block=true)]
[playsound(key="$d_avg_magic_1")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_251",duration=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]这是......石头？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_251")]
来者所为何事？
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]......我只是一名虔诚的信徒，为了在近处瞻仰神的面貌而来。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_251")]
祂累了，今天祂想要休息。
明天再来吧。
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]我听说耶拉冈德欢迎外来者的信仰，难道这只是一句戏言？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_251")]
虔诚之人不必自证，不诚之人口舌无用。
祂说，你今日不可再向前一步。
[charslot(slot="m",name="avg_npc_867_1#1$1")]
[name="“灰礼帽”"]若我非要向前呢？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_251")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[playsound(key="$d_avg_magic_2")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5,

... (全文28963字符)
```

### level_act30side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g6_lakescenery_d",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_172_svrash_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="恩希欧迪斯"]人们都说冬季是银心湖最美丽的季节。
[charslot(slot="m",name="avg_172_svrash_1#2$1")]
[name="恩希欧迪斯"]冬季的湖水被坚冰封锁，从远处看，就像是一块巨大的宝石，在阳光照射下会显露出醉人的美丽。
[charslot(slot="m",name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]但若从近处看，或许更能理解这里的美。
[name="恩希欧迪斯"]没有宝石那么无瑕，却更坚硬；冰面之下，水还在流动。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]......你什么时候这么会抒情了？
[name="诺希斯"]按照蔓珠院的说法，我们将要跟随圣女，从这冰面上一直走到耶拉冈德像脚下。
[charslot(slot="m",name="avg_206_gnosis_1#2$1")]
[name="诺希斯"]这是一段不短的路程，这一路上，我们随时可能会出意外。
[charslot(slot="m",name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]怎么，诺希斯，你担心脚下的冰会碎裂吗？
[name="恩希欧迪斯"]这可不像你的性格。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]你知道我说的不是这个。
[charslot(slot="m",name="avg_206_gnosis_1#7$1")]
[name="诺希斯"]来“观礼”的那些客人，里面很多人一直紧盯着我们。
[name="诺希斯"]恩希欧迪斯，你的后手到现在还没有准确的消息，我们的处境并不乐观。
[charslot(slot="m",name="avg_4116_blkkgt_1#2$1")]
[name="锏"]昨天让那个“灰礼帽”接近耶拉冈德像，是我的失误。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1")]
[name="锏"]如果有需要，我可以现在去解决他。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]如果对方已经发现了什么，现在做什么都迟了。
[charslot(slot="m",name="avg_206_gnosis_1#2$1")]
[name="诺希斯"]你动起手来容易忽略四周这毛病......算了，你和恩希欧迪斯都一样，我也不求你们能改变了。
[charslot(slot="m",name="avg_206_gnosis_1#1$1")]
[name="诺希斯"]只是下次，麻烦你们稍微收敛一点，也替每次都要善后的我多着想着想。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1")]
[name="锏"]诺希斯是这么说的。你觉得呢，恩希欧迪斯？
[charslot(slot="m",name="avg_172_svrash_1#2$1")]
[name="恩希欧迪斯"]我可没有随手把几十米高的巨像切割开的实力。
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1")]
[name="锏"]是啊。
[name="锏"]你只是邀请那个博士过来，差点让对方坏了计划而已。
[charslot(slot="m",name="avg_172_svrash_1#2$1")]
[name="恩希欧迪斯"]......
[charslot(slot="m",name="avg_206_gnosis_1#6$1")]
[name="诺希斯"]......唉。
[name="诺希斯"]我不想听你们毫无意义地互相攻击。
[name="诺希斯"]负责维持秩序的山雪鬼......
[charslot(slot="m",name="avg_4116_blkkgt_1#1$1")]
[name="锏"]他们会提前到湖心岛。
[name="锏"]负责招待维多利亚人，还有那些商人。
[charslot(slot="m",name="avg_172_svrash_1#9$1")]
[name="恩希欧迪斯"]诺希斯，你太过紧张了。
[charslot(slot="m",name="avg_172_svrash_1#1$1")]
[name="恩希欧迪斯"]我们已经做好了能做的所有准备，现在剩下的，只有等待。
[name="恩希欧迪斯"]锏，诺希斯，再等等。
[charslot(slot="m",name="avg_172_svrash_1#2$1")]
[name="恩希欧迪斯"]春天就要到了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_254_1#1$1")]
[name="阿克托斯"]我还记得三年前，圣女大人从圣山上走下。
[name="阿克托斯"]当时耶拉冈德降下祝福，就连那恩希欧迪斯，也不免折服......不知道今日是否还能见到那般奇景。
[charslot(slot="m",name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]看来今天的场景勾起了你的许多回忆，我的朋友。
[name="菈塔托丝"]但是阿克托斯，这几年你回忆过去的次数未免太多，你不这么觉得吗？
[charslot(slot="m",name="avg_npc_254_1#9$1")]
[name="阿克托斯"]菈塔托丝，有说这种风凉话的工夫，不如多关心今天的仪式。
[charslot(slot="m",name="avg_npc_254_1#1$1")]
[name="阿克托斯"]我早上一来就觉得奇怪......这座耶拉冈德像，是不是和之前稍微有点不一样了？
[name="阿克托斯"]这里由你布朗陶家负责现场的施工调度，你最好想好了该如何与圣女大人解释！
[charslot(slot="m",name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]呵呵，不劳担心......
[charslot(slot="m",name="avg_npc_253_1#5$1")]
[name="菈塔托丝"]......
[name="菈塔托丝"]我说阿克托斯，你的脸这是怎么了？
[name="菈塔托丝"]难道是“灰礼帽”真的对你动手了？
[charslot(slot="m",name="avg_npc_254_1#2$1")]
[name="阿克托斯"]......我原话送回给你！不劳担心！
[name="阿克托斯"]（嘶......）
[charslot(slot="m",name="avg_npc_254_1#10$1")]
[name="阿克托斯"]（那丫头下手够狠的，这点像塔季扬娜，也像我。）
[charslot(slot="m",name="avg_npc_254_1#11$1")]
[name="阿克托斯"]（不错。）
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_263_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_263_1#1$1")]
[name="尤卡坦"]大夫人，人都到齐了。
[charslot(slot="m",name="avg_npc_253_1#1$1")]
[name="菈塔托丝"]好，你去告诉下面的人，让他们在指定地方等着。
[name="菈塔托丝"]一会圣女大人就要来了，谁敢在这种时候给布朗陶家丢人现眼，我绝不饶他！
[charslot(slot="m",name="avg_npc_263_1#1$1")]
[name="尤卡坦"]是。
[charslot(slot="m",name="avg_npc_253_1#4$1")]
[name="菈塔托丝"]等等，尤卡坦。
[name="菈塔托丝"]怎么就你一个人，你老婆呢？
[name="菈塔托丝"]都这个点了，她怎么还没来？
[charslot(slot="m",name="avg_npc_263_1#1$1")]
[name="尤卡坦"]露丝她早上说有些事要办......
[name="尤卡坦"]她给大夫人您准备了一份惊喜。
[charslot(slot="m",name="avg_npc_253_1#5$1")]
[name="菈塔托丝"]她的惊喜，我可是不敢期待啊。
[charslot(slot="m",name="avg_npc_253_1#7$1")]
[name="菈塔托丝"]什么事能比今天的仪式更重要？她可别在这种时候给我犯浑！
[charslot(slot="m",name="avg_npc_263_1#2$1")]
[name="尤卡坦"]这......我现在就联系露丝。
[charslot(slot="m",name="avg_npc_263_1#1$1")]
[name="尤卡坦"]大夫人也不必太担忧，轻重缓急露丝她心里清楚。
[charslot(slot="m",name="avg_npc_253_1#7$1")]
[name="菈塔托丝"]你倒是会护着你老婆。
[charslot(slot="m",name="avg_npc_253_1#2$1")]
[name="菈塔托丝"]罢了，她也不是小孩子了，那我就等着看她能给我什么“惊喜”。
[charslot(slot="m",name="avg_npc_253_1#4$1")]
[name="菈塔托丝"]不过，她去办事，不带着你？
[charslot(slot="m",name="avg_npc_263_1#1$1")]
[name="尤卡坦"]......
[name="尤卡坦"]露丝她身边有人帮忙......
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_250_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="雅儿"]各位，时间差不多了。
[name="雅儿"]圣女大人到。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_174_slbell_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="恩雅"]各位。
[name="恩雅"]自蔓珠院接受外国人对耶拉冈德的信仰以来，已有三年。
[name="恩雅"]谢拉格能够有如今的发展，离不开在场的各位，以及所有谢拉格人民的努力与奉献。
[charslot(slot="m",name="avg_174_slbell_1#3$1")]
[name="恩雅"]我相信，各位也都将谢拉格这几年的变化看在眼中。
[charslot(slot="m",name="avg_174_slbell_1#1$1")]
[name="恩雅"]耶拉冈德为祂的子民、祂的孩子们降下的挑战，我们已经给出了一个回答。
[name="恩雅"]而这三年，只是一个开始。
[charslot(slot="m",name="avg_174_slbell_1#3$1")]
[name="恩雅"]今后我们会面对比现在还要复杂的局面，谢拉格也将遭遇更多的危机与挑战。
[charslot(slot="m",name="avg_174_slbell_1#1$1")]
[name="恩雅"]但是，我希望各位相信，耶拉冈德不会抛弃谢拉格的土地，耶拉冈德更加不会抛弃在这片土地上生活的、敬爱祂的子民。
[name="恩雅"]这座耶拉冈德像，将会是谢拉格面向外界的第一个标志。
[name="恩雅"]同时，它也将成为所

... (全文37742字符)
```

### level_act30side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g10_iceonlake",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$kazimierz2_1_intro", key="$kazimierz2_1_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[playsound(key="$d_gen_soldiersrun")]
[charslot(slot="l",name="avg_npc_414_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_414_1#1$1",duration=1.5)]
[Delay(time=2)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_twohandedblunt",volume=1,channel="1")] 
[playsound(key="$fightgeneral",Delay=0.3,volume=1,channel="2")]
[charslot(slot="l",posfrom="0,0",posto="-200,-50",afrom=1,ato=0,duration=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[charslot(slot="l",focus="none")]
[name="维多利亚士兵A"]呃......
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_twohandedblunt",volume=1,channel="1")] 
[playsound(key="$fightgeneral",Delay=0.3,volume=1,channel="2")]
[charslot(slot="r",posfrom="0,0",posto="200,-50",afrom=1,ato=0,duration=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[name="维多利亚士兵B"]咳！
[Dialog]
[charslot(slot="m",name="avg_npc_414_1#1$1")]
[name="维多利亚士兵C"]小心——！
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_twohandedblunt",volume=1,channel="1")] 
[playsound(key="$fightgeneral",Delay=0.3,volume=1,channel="2")]
[charslot(slot="m",posfrom="0,0",posto="-100,-50",afrom=1,ato=0,duration=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Delay(time=0.5)]
[charslot]
[Delay(time=0.5)]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",duration=1.5)]
[Delay(time=2)]
[name="锏"]下一个。
[Dialog]
[charslot(slot="m",name="avg_npc_414_1#1$1")]
[name="维多利亚士兵D"]......
[name="维多利亚士兵D"]哈啊——！！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_248",duration=1.5)]
[Delay(time=2)]
[name="维多利亚士兵"]报告长官！
[name="维多利亚士兵"]依靠哈洛德上校的支援，目前受重伤的几人都已经被救回来了！
[name="维多利亚士兵"]但是，按照我们现在的攻势，恐怕暂时无法对对方造成有效打击！
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]突袭！
[name="老练的士兵"]用上你们的武器，对方只有一个人，包围她！
[charslot(slot="m",name="avg_npc_248")]
[name="维多利亚士兵"]可是......
[name="维多利亚士兵"]可是长官，我们难道不该绕开她吗？
[name="维多利亚士兵"]对方只有一个人，只要我们把战线拉长，她怎么也不可能守得过来啊！
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]......蠢货！
[name="老练的士兵"]这点道理，你当我们不懂？
[charslot(slot="m",name="avg_npc_248")]
[name="维多利亚士兵"]那为什么......
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]长了眼睛就自己好好看看！
[name="老练的士兵"]那几个被重伤到差点见耶拉冈德的，哪个不是和你一个想法，去尝试从其他方向突破防线的？
[name="老练的士兵"]你再看看其他人，伤得有他们几个那么重吗？
[charslot(slot="m",name="avg_npc_248")]
[name="维多利亚士兵"]......
[name="维多利亚士兵"]难道，您的意思是......
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]我什么意思也没有——闪开！
[charslot(slot="m",name="avg_npc_248")]
[name="维多利亚士兵"]呃......！
[Dialog]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$d_avg_twohandedblunt",volume=1,channel="1")] 
[charslot(slot="m",posfrom="0,0",posto="-200,0",afrom=1,ato=0,duration=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Delay(time=0.5)]
[charslot]
[Delay(time=0.5)]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1",duration=1.5)]
[Delay(time=2)]
[name="锏"]没收住手。
[name="锏"]悄悄话说完了？
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]你是什么时候到这里的......？！
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1")]
[name="锏"]刚刚。
[name="锏"]如果你指望前面站着几十个人就能挡住我，未免也太天真了。
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]嘁，真是个怪物......
[name="老练的士兵"]几十个人不行，几百个，上千个总能行。
[name="老练的士兵"]你无法凭一己之力与军队抗衡——
[charslot(slot="m",name="avg_4116_blkkgt_1#11$1")]
[name="锏"]咬紧牙关。
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]......什么？
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1")]
[name="锏"]我揍你的时候别张口。
[name="锏"]小心咬到舌头。
[Dialog]
[charslot]
冷冽的劲风随话音而至。
以一人对两千人，明明处于绝对劣势，女人金色的双眼中却没有一丝因此而生的波澜。
她是不可置疑的捕食者，是这片战场的主宰。
在涉及这位锏女士的事情上，哪怕带有任何一点轻视，都是对她的不尊重。
——也是对自己性命的轻视。
[charslot(slot="m",name="avg_npc_1157_1#1$1")]
[name="老练的士兵"]——！！
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[charslot(slot="m",name="avg_4114_harold_1#15$1")]
[PlaySound(key="$d_avg_twohandedblunt",volume=1,channel="1")] 
[playsound(key="$d_avg_janttck_03",Delay=0.05,volume=1,channel="2")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="哈洛德"]手下留情，锏女士！
[name="哈洛德"]如果我的下属说了什么失礼的话，就由我来替他向您道歉。
[charslot(slot="m",name="avg_4116_blkkgt_1#6$1")]
[name="锏"]哦？
[name="锏"]你来代替？
[name="锏"]你又能护他们多久？
[charslot(slot="m",name="avg_4114_harold_1#1$1")]
[name="哈洛德"]这个嘛，哈哈，可能，直到我战死为止？
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, 

... (全文44063字符)
```

### level_act30side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="showall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6, loop=true, channel="wind")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[Subtitle(text="伟大的耶拉冈德，我们追随祂。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="云是祂的羽，风是祂的翼。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="祂赐我们日光与甘霖，赐我们血肉与皮毛。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="仁爱的耶拉冈德，我们敬爱祂。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="群山是骨，百川是尾。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我们走上祂的背脊，我们于祂怀中安睡。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[charslot]
[Background(image="24_g13_mountpath_s", screenadapt="coverall", block=true)]
[Delay(time=1)]
[bgeffect(name="$eb_blizzard",layer=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[SoundVolume(channel="wind", volume=1, fadetime=1.5)]
[Delay(time=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="慈悲的耶拉冈德，我们歌颂祂。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="当我们愁苦时，是祂轻柔抚慰。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="当我们蒙难时，是祂倾力施救。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="耶拉冈德庇佑祂虔诚的子民，庇佑山石与百兽，安乐无灾，永享宁静。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——《耶拉冈德》", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=2)]
[Dialog]
[StopSound(channel="wind", fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[bgeffect(layer=1,fadetime=1)]
[charslot]
[Background(image="24_g1_snowyforest", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
1100年冬，谢拉格佩尔罗契家族领地内，圣山脚下
[Dialog]
[PlaySound(key="$d_avg_soldiersstep",channel="step1",loop=false, volume=0.7)]
[stopsound(channel="step1",fadetime=3)]
[charslot(slot="l",name="avg_npc_1158_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_408_1#1$1",duration=1)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]......
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="l")]
[name="领头的士兵"]加快步伐！
[name="领头的士兵"]别忘了我们是来做什么的，后面的都跟上！
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]是！
[Dialog]
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="all")]
[Delay(time=0.2)]
[charslot(duration=1)]
[PlaySound(key="$d_avg_soldiersstep",channel="step2",loop=false, volume=0.7)]
[stopsound(channel="step2",fadetime=4)]
[Delay(time=3)]
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]立定！靠拢！
[name="领头的士兵"]原地列队！
[Dialog]
[charslot]
[Delay(time=0.2)]
[PlaySound(key="$d_gen_soldiersrun", volume=0.6)]
[charslot(slot="l",name="avg_npc_408_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1157_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[Dialog]
[charslot]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]报告长官！第二小队已整队！
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="l")]
[name="领头的士兵"]嗯，很好。
[name="领头的士兵"]第三小队还没有到？
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]报告长官！还没有！
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="l")]
[name="领头的士兵"]......
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]长官，第三小队那边恐怕情况不妙......
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]我们还等不等他们过来会合？
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="l")]
[name="领头的士兵"]不等了。我早料到可能会有这种情况，谁先抵达，谁就先一步发起进攻！
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]是！
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="l")]
[name="领头的士兵"]关于接下来的作战计划，想必不用我再多说。
[name="领头的士兵"]这是一场远征，是属于我们维多利亚人的战斗！是荣誉的战斗！
[name="领头的士兵"]时刻保持警惕！不要小看任何一个敌人！这一仗......只能成功，不能失败！
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]是！
[charslot(slot="l",name="avg_npc_1158_1#1$1",focus="l")]
[name="领头的士兵"]很好，保持士气！
[name="领头的士兵"]第二小队听令，继续进军！
[name="领头的士兵"]目标——山下牧兽老头的酒馆！
[name="领头的士兵"]绝对不能在酒量上输给那群牧兽佬！这次一定让他们输得心服口服！
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="严肃的士兵"]是！！
[Dialog]
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="all")]
[Delay(time=0.2)]
[charslot(duration=1)]
[PlaySound(key="$d_avg_soldiersstep",channel="step3",loop=false, volume=0.7)]
[stopsound(channel="step3",fadetime=4)]
[Delay(time=3)]
[charslot(slot="l",name="avg_npc_278_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_280_1#1$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_278_1#1$1",focus="l")]
[name="谢拉格平民男性"]......
[name="谢拉格平民男性"]那群维多利亚人又在干啥？
[charslot(slot="r",name="avg_npc_280_1#1$1",focus="r")]
[name="谢拉格平民女性"]拼酒量吧？他们都和莱利大叔他们拼了好几场了，听说这帮人每次都喝到吐。
[name="谢拉格平民女性"]耶拉冈德在上......
[name="谢拉格平民女性"]维多利亚人......平时都这么闲，没有活要干吗？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="24_g8_nobleroom", screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_262_1#5$1",duration=0

... (全文32634字符)
```

### level_act30side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g4_luxurywarminterior",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_1157_1#1$1",duration=0.5)]
[charslot(slot="r",name="avg_npc_408_1#1$1",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="油滑的士兵"]我回来了。
[charslot(slot="l",name="avg_npc_1157_1#1$1",focus="l")]
[name="老练的士兵"]......
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="油滑的士兵"]里斯本，你在东张西望什么呢？
[charslot(slot="l",name="avg_npc_1157_1#1$1",focus="l")]
[name="老练的士兵"]没什么。
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="油滑的士兵"]哦，我记起来了，老图里尔的女儿在后厨做饭，你小子在想找什么借口溜过去吧。
[name="油滑的士兵"]假公济私啊，小子。
[charslot(slot="l",name="avg_npc_1157_1#1$1",focus="l")]
[name="老练的士兵"]她原本就在这附近的饭店当厨师，被请来帮忙也很正常啊。
[charslot(slot="r",name="avg_npc_408_1#1$1",focus="r")]
[name="油滑的士兵"]算了，比起这个，怎么菜还没有上？
[name="油滑的士兵"]哎，老丈，我想问问菜为什么还没有上。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_278_1#1$1",focus="m")]
[name="服务员"]抱歉，抱歉。
[name="服务员"]主要是要上的菜有点太多了，厨房虽然已经请来了许多人帮忙，但还是有些忙不过来。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]既然这样的话，就让我来帮忙吧！
[Dialog]
[charslot]
[name="雅儿"]不必了。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]你是......
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]圣女大人身边的侍女长，雅儿，见过几位长官。
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]呃，我们只是一些士兵，不用对我们行礼。
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]利雅。
[charslot(slot="m",name="avg_npc_269",focus="m")]
[name="侍女"]在。
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]把随行的侍女分组，轮班前往后厨帮忙。
[name="雅儿"]务必让宴会能够顺利进行。
[charslot(slot="m",name="avg_npc_269",focus="m")]
[name="侍女"]是。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]这......怎么好意思！
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]长官不必介怀。
[name="雅儿"]虽然这场宴会是子爵阁下主办，但这里毕竟是谢拉格，对圣女大人而言，诸位才是客人。
[name="雅儿"]子爵阁下宴请圣女大人，那么，我们这些做下人的帮助各位也是理所当然。
[charslot(slot="m",name="avg_npc_250_1#8$1",focus="m")]
[name="雅儿"]况且......请不要怪我说得有些难听，各位长官的手拿武器拿惯了，端起盘子，恐怕帮倒忙的可能性更大些。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]唔......
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]行了，里斯本，侍女长小姐说得对，咱们真去帮忙，指不定要摔碎多少盘子呢。
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]......我明白了。
[name="老练的士兵"]不过，要是有什么需要干体力活的地方，侍女长小姐也别客气。
[charslot(slot="m",name="avg_npc_250_1#8$1",focus="m")]
[name="雅儿"]啊，这么说起来，后厨现在似乎还挺缺人搬运食材的，不知长官......
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[name="老练的士兵"]我去，我去！
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="油滑的士兵"]......谢谢了，侍女长小姐。
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]客气。
[name="雅儿"]既然事情已经解决，我也就不在这里打扰长官们享受宴会了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="45_g4_luxurywarminterior", screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crwddiscuss_inside",loop=true, channel="crwd1", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_269",focus="m")]
[name="侍女"]......我回来了。
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]利雅，还有件事要麻烦你，你去看看他们有没有这几种食材，如果有的话，就让厨房加做一道菜。
[charslot(slot="m",name="avg_npc_250_1#6$1",focus="m")]
[name="雅儿"]就做......就做水果奶酪卷饼。
[charslot(slot="m",name="avg_npc_269",focus="m")]
[name="侍女"]做那种家常菜吗？
[name="侍女"]可是，圣女大人平时从来不碰啊？
[charslot(slot="m",name="avg_npc_250_1#7$1",focus="m")]
[name="雅儿"]哎呀好啦，你就听我的。
[Dialog]
[charslot]
[delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1161_1#1$1",duration=0.7)]
[delay(time=1.5)]
[charslot]
[delay(time=0.2)]
[charslot(slot="m",name="avg_npc_1162_1#1$1",duration=0.7)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]喀兰贸易的职员们看来也已经陆续到场了。
[charslot(slot="m",name="avg_npc_269",focus="m")]
[name="侍女"]是的，那位子爵阁下不仅邀请了圣女大人和恩希欧迪斯老爷，也邀请了蔓珠院的长老们，以及喀兰贸易的员工们。
[name="侍女"]不愧是维多利亚的子爵，真是财大气粗。
[name="侍女"]而且那位子爵确实有些本事，他甚至请到了在驮峰酒店当主厨的那位图里尔大厨。
[name="侍女"]那位脾气可糟糕了，可不是有钱就能请动的。
[charslot(slot="m",name="avg_npc_250_1#1$1",focus="m")]
[name="雅儿"]说明他们进入谢拉格的这一个月里和我们的人民确实相处得不差。
[charslot(slot="m",name="avg_npc_250_1#8$1",focus="m")]
[name="雅儿"]嗯？
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[StopSound(channel="crwd1", fadetime=1)]
[charslot]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_414_1#1$1")]
[charslot(slot="r",name="avg_npc_222")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_414_1#1$1",focus="l")]
[name="虚弱的士兵"]喝！干了！
[charslot(slot="r",name="avg_npc_222",focus="r")]
[name="喀兰贸易员工"]嗝——喝，喝！
[Dialog]
[PlaySound(key="$d_avg_drinkswllw",volume=0.6)]
[PlaySound(key="$d_avg_drinkswllw",volume=0.6,loop=false,channel="1",delay=1)]
[PlaySound(key="$d_avg_drinkswllw",volume=0.6,loop=false,channel="2",delay=2)]
[delay(time=2)]
[charslot(slot = "r", action="shake",random=true, power=5, times=40,duration=0.3,focus="r")]
[delay(time=0.5)]
[charslot(slot="r",name="avg_npc_222",focus="r")]
[name="喀兰贸易员工"]咕......
[Dialog]
[PlaySound(key="$bodyfalldown2", volume=0.8)]
[charslot(slot="r",name="avg_npc_222",afrom=1,ato=0,duration=0.5,focus="r")]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_414_1#1$1",focus="l")]
[name="虚弱的士兵"]不错，你们雪山人，真挺能喝......
[name="虚弱的士兵"]不过，还是我能喝，嘿、嘿嘿。
[name="虚弱的士兵"]下一个，谁来！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Backgr

... (全文39313字符)
```

### level_act30side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="45_g10_iceonlake",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.7, loop=true, channel="wind")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[stopsound(fadetime=1.5, channel="wind")]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.6)]
[name="维多利亚士兵"]唔......
[name="维多利亚士兵"]呃，我这是......
[multiline(name="维多利亚士兵")]都结束了吗？我们的行动成功了没有......
[PlaySound(key="$d_avg_bonrcver")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="维多利亚士兵")]嘶，疼！
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="阴沉的士兵"]知道疼就还行，这条胳膊算是没废。
[name="阴沉的士兵"]没死就赶紧地起来！
[Dialog]
[charslot]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[charslot(slot="m",name="avg_npc_408_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_408_1#1$1",focus="m")]
[name="维多利亚士兵"]嘶！查理斯，你轻点！
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]行了，少折腾，别给哈洛德再增加工作量了。
[name="领头的士兵"]还能走的都先去湖边整队，伤势不重就先自己处理一下。
[name="领头的士兵"]再来几个还有力气的，跟我一起去把爬不起来的人抬回去。
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="阴沉的士兵"]杰弗逊，我跟你去。
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]不想要你那条腿就直说，回头让哈洛德给你也换条假的。
[name="领头的士兵"]都该干嘛干嘛去！*维多利亚常用语*，打到现在居然所有人都还有气，真他*维多利亚常用语*的是个奇迹。
[name="领头的士兵"]难道真是耶拉冈德保佑？
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="阴沉的士兵"]说反了吧，打到现在她竟然还有气，上千人打一个哎......
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]看来真是耶拉冈德保佑。
[Dialog]
[charslot]
[name="恩雅"]并非如此。
[name="恩雅"]耶拉冈德是仁爱的神明，但这一结果，并非祂的力量所致。
[Dialog]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="ew")]
[stopsound(fadetime=1.5, channel="ew")]
[charslot(slot="m",name="avg_174_slbell_1#11$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_174_slbell_1#11$1",focus="m")]
[name="恩雅"]无人在此丢掉性命，这是你我双方共同创造的奇迹。
[name="恩雅"]我如此相信。
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]你是......不对，您是谢拉格的圣女大人？
[name="领头的士兵"]圣女大人这话，我们可担不起。
[name="领头的士兵"]您有什么吩咐？
[charslot(slot="m",name="avg_174_slbell_1#11$1",focus="m")]
[name="恩雅"]称不上吩咐。
[name="恩雅"]只不过是来尽地主之谊，邀请各位参加仪式后的宴会。
[name="恩雅"]各位来谢拉格，不正是为了观礼与庆贺吗？
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]......我以为最好的情况也是被驱逐出境来着。
[name="领头的士兵"]还能参加宴会？
[charslot(slot="m",name="avg_174_slbell_1#11$1",focus="m")]
[name="恩雅"]各位想参加宴会，还是想承认这是场“军事行动”，被关进大牢？
[charslot(slot="m",name="avg_npc_1158_1#1$1",focus="m")]
[name="领头的士兵"]呃。
[charslot(slot="m",name="avg_174_slbell_1#11$1",focus="m")]
[name="恩雅"]请吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g9_underkjerastastue", screenadapt="coverall", block=true)]
[charslot(slot="l",name="avg_174_slbell_1#11$1")]
[charslot(slot="r",name="avg_npc_250_1#1$1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_npc_250_1#1$1",focus="r")]
[name="雅儿"]圣女大人。
[name="雅儿"]都准备好了，宴会随时可以开始。
[charslot(slot="l",name="avg_174_slbell_1#11$1",focus="l")]
[name="恩雅"]嗯，谢谢你，雅儿。
[charslot(slot="r",name="avg_npc_250_1#1$1",focus="r")]
[name="雅儿"]谢我做什么？
[charslot(slot="l",name="avg_174_slbell_1#11$1",focus="l")]
[name="恩雅"]没什么，就是想谢。
[name="恩雅"]雅儿，谢拉格会变得更好。
[charslot(slot="l",name="avg_174_slbell_1#12$1",focus="l")]
[name="恩雅"]迟早有一天，外面的人不会只知道喀兰贸易，不会只看到茫茫白雪和深谷高山。
[name="恩雅"]他们会知道这里的国家叫作谢拉格。
[name="恩雅"]这是一个人民富足，风俗独特，值得尊敬的国家。
[charslot(slot="r",name="avg_npc_250_1#1$1",focus="r")]
[name="雅儿"]听起来真好。
[name="雅儿"]恩雅，这次真的不用我“帮点小忙”？
[name="雅儿"]不用的话，可就没有上一次那样漂亮的彩虹可以看了哦？
[charslot(slot="l",name="avg_174_slbell_1#11$1",focus="l")]
[name="恩雅"]耶拉冈德的赐福正因为珍贵，才更震撼心灵。
[name="恩雅"]若将来无论大小事务，都要耶拉冈德降下神迹，恐怕得来的便不再是信仰，而是依赖了。
[name="恩雅"]也难免会让一些人对此习以为常，失去对耶拉冈德的敬畏之心。
[name="恩雅"]现在这样就很好。
[name="恩雅"]只盼望我这样的想法，不会让耶拉冈德感到不敬，生我的气才好。
[charslot(slot="r",name="avg_npc_250_1#7$1",focus="r")]
[name="雅儿"]......呵呵，放心吧，恩雅。
[name="雅儿"]孩子放开母亲的手开始学步，母亲只会感到欣慰，哪有会生气的呢？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="45_g10_iceonlake", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_172_svrash_1#10$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_1156_1#7$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_1156_1#7$1",focus="r")]
[name="发言人莫布"]希瓦艾什先生，我说完了。
[name="发言人莫布"]露天演说我还是头一次尝试，您确定这样没问题吗......？
[charslot(slot="l",name="avg_172_svrash_1#10$1",focus="l")]
[name="恩希欧迪斯"]非常完美，莫布先生。
[name="恩希欧迪斯"]我相信任谁都挑不出半点问题，您的声音饱含热情。
[name="恩希欧迪斯"]虽然您拒绝了我安排下属使用源石技艺来放大声音，但您使用的那件扩音用的小装置很好地完成了使命，甚至超出预期......
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]恕我冒昧，难道这就是贵企业的新产品？
[charslot(slot="r",name="avg_npc_1156_1#7$1",focus="r")]
[name="发言人莫布"]您说这个扩音器？
[charslot(slot="r",name="avg_npc_1156_1#1$1",focus="r")]
[name="发言人莫布"]不，当然不。虽然效果很好，但扩音器在卡西米尔的市场早已被几家大企业瓜分，没有我们能插足的余地......咳咳，抱歉，我失言了。
[charslot(slot="l",name="avg_172_svrash_1#1$1",focus="l")]
[name="恩希欧迪斯"]我对卡西米尔企业间的竞争有所耳闻，您只是说出了实情。
[name="恩希欧迪斯"]那么，您使用的是......？
[charslot(slot="r",name="avg_npc_1156_1#1$1",focus="r")]
[name="发言人莫布"]这是一位在列车上遇见的朋友赠送给我的。
[name="发言人莫布"]我想，对方大概只以为自己送出了一件小玩具。
[charslot(slot="r",name="avg_npc_1156_1#6$1",focus="r")]
[name="发言人莫布"]谁能想到，希瓦艾什先生会突然提出这样的请求，这东西忽然就派上了大用场呢！
[charslot(slot="l",name="avg_172_svrash_1#9$1",focus="l")]
[name="恩希欧迪斯"]原来如此......
[charslot(slot="l",name="avg_172_svrash_1#10$1",focus="l")]
[name="恩希欧迪斯"]莫布先生，喀兰贸易希望能够与贵企业长久地展开合作，而非仅局限于这一次。
[name="恩希欧迪斯"]接下来的几天，我将安排专人带您参观谢拉格，包括我们的矿区和工厂。
[name="恩希欧迪斯"]这也是我向您展示的诚意。
[name="恩希欧迪斯"]我相信，谢拉格不会令贵企业失望。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]


... (全文42746字符)
```

### training_act30side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 


[PopupDialog(dialogHead="$avatar_snakek")] 谢拉格好冷啊，在这样的天气里战斗的话，我们会被<@tu.kw>冻住</>的。
```

### training_act30side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动30side教学关_b


[Tutorial(focusX=93, focusY=209, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_hibisc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
幸好紧急供暖器可以为一定范围内的干员<@tu.kw>提供温暖</>，我们在紧急供暖器周围可以避免被<@tu.kw>“封冻”</>。
```

### training_act30side_01_c

```
[HEADER(is_skippable=true, is_tutorial=true)] 
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[InputBlocker(blockInput=false)]

[Tutorial(waitForSignal="put_down", dialogHead="$avatar_kroos", animStyle="Drag", \
          startX=-62, startY=60, startAnchor="BottomRight", endX=194, endY=130)] \
站在紧急供暖器<@tu.kw>周围</>可以更快地<@tu.kw>激活</>另一个紧急供暖器，让我来示范一下吧。
[Tutorial(waitForSignal="select_direction", dialogHead="$avatar_kroos", animStyle="Drag", \
          startX=250, startY=140, endX=284, endY=-100)] \
只要我能<@tu.kw>击中</>其他紧急供暖器，<@tu.kw>受到攻击</>的紧急供暖器就能被激活。
[InputBlocker(blockInput=true)]

[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause(pause=false)]
```

### training_act30side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 


[PopupDialog(dialogHead="$avatar_snakek")] 成功<@tu.kw>激活</>另外一个紧急供暖器了，在它周围再也不会冷了。
```

### training_act30side_01_e

```
[HEADER(is_skippable=true, is_tutorial=true)] 
[Battle.Pause]





[Tutorial(focusX=306, focusY=-18, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_snakek", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
如果紧急供暖器<@tu.kw>右侧</>的“风门”位置上没有干员看守的话，紧急供暖器会<@tu.kw>逐渐停止工作</>的。




```

### training_act30side_01_f

```
[HEADER(is_skippable=true, is_tutorial=true)] 
[Battle.LockFunction(mask="SYSTEM_MENU_INTERACT")]
[Battle.Pause]

[InputBlocker(blockInput=false)]
[Tutorial(waitForSignal="put_down", dialogHead="$avatar_snakek", animStyle="Drag", \
          startX=-62, startY=60, startAnchor="BottomRight", endX=312, endY=-38)] \
快来<@tu.kw>守住</>这个紧急供暖器的“风门”！
[Battle.UnlockFunction(mask="SYSTEM_MENU_INTERACT")]
```

### training_act30side_05_a

```
[HEADER(is_skippable=true, is_autoable=false)] 
[PopupDialog(dialogHead="$avatar_snakek")] 哇，这里的<@tu.kw>紧急供暖器</>都没有工作，我们得利用它们。咦，这些<@tu.kw>高山驮兽</>都被冻住了吗？
```

### training_act30side_05_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动30side教学关_b
[Tutorial(anchor="BottomRight",focusX=-48, focusY=62, focusWidth=140, focusHeight=140,           animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_hibisc", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 还好我们准备了<@tu.kw>点火石</>，点火石可以直接启动一个未工作的<@tu.kw>紧急供暖器</>
```

### training_act30side_05_c

```
[HEADER(is_skippable=true, is_autoable=false)] 
[PopupDialog(dialogHead="$avatar_snakek")] 点火的时候也要<@tu.kw>小心</>，万一融化了这些<@tu.kw>高山驮兽</>身上的冰块，它们就会<@tu.kw>苏醒</>给我们带来麻烦哦。
```


## 统计

- 总字符数：507929
- 对话行数：5160


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
