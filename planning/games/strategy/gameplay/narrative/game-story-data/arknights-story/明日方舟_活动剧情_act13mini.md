# 明日方舟 · 活动剧情 · act13mini（8段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act13mini」完整剧情脚本（8个文件，1785行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act13mini
- 脚本文件数：8

### act13mini_sub1-1_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13mini_sub1-1_a

[PopupDialog(dialogHead="$avatar_lolxh")] 咦，这小家伙是什么啊？模样好奇怪。
[PopupDialog(dialogHead="$avatar_spsbr")] 嘎！！
[PopupDialog(dialogHead="$avatar_dusk")] 抱歉，方才作画时几笔墨汁不小心落在画卷外，你且先拦住，我片刻就到。
```

### act13mini_sub1-1_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动13mini_sub1-1_b

[PopupDialog(dialogHead="$avatar_lolxh")] 可恶，怎么越来越多了......
[PopupDialog(dialogHead="$avatar_dusk")] 你们这些小家伙闹够了没，还不回来。
```

### level_act13mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_rooftop_2",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]  
白日里下了一整天的雨，到晚上虽然雨停了，但空气仍然有些湿润。
团团阴云聚在天空，像堵无情的墙，莹莹月光洒不下来，盏盏灯光照不上去。
[Dialog]
[PlaySound(key="$d_avg_catfootstep", volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_classicmiaow_2", volume=1)]
[Character(name="avg_npc_596_1#4$1",fadetime=1,block=true)]
[Delay(time=2)]
[multiline(name="小黑")]这天气讨厌死了，
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_596_1#4$1")]
[multiline(name="小黑")]阿嚏——
[name="小黑"]本来想上来打个盹，这下可好，天台上到处都是水。
[Dialog]
[PlaySound(key="$d_avg_catsmell", volume=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_596_1#3$1")]
[name="小黑"]（嗅嗅）嗯？这有个箱子里面还没湿。
[Dialog]
[PlaySound(key="$d_avg_cardboard", volume=1)]
[Character(name="avg_npc_596_1#1$1")]
[name="小黑"]（钻入箱中）
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_596_1#2$1")]
[name="小黑"]啊哈......这天气倒头睡一觉也是不错。
[Dialog]
[Character]
[Delay(time=0.51)]
[name="楼下广告"]今日生鲜大特惠，买一送一别错过，龙门市区最低价，只为回馈广大顾客！
[Dialog]
[Character(name="avg_npc_596_1#5$1")]
[name="小黑"]（向左翻身）嘶——
[Dialog]
[Character]
[Delay(time=0.51)]
[name="楼下邻居"]和你讲过多少次了！吃完饭不要磨蹭，赶紧去写作业！哎呦老天爷，谁家佩洛是你这样的慢性子！
[Dialog]
[Character(name="avg_npc_596_1#5$1")]
[name="小黑"]（向右翻身）啧—— 
[Dialog]
[Character]
[Delay(time=0.51)]
[name="楼下电视"]近期天气潮湿，请市民们关注消防安全，空气湿度大容易导致家庭电气发生火灾事故，大家务必注意安全用电和定期检查家中电器！
[Dialog]
[PlaySound(key="$bodyfalldown3", volume=0.6)]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=0.7)]
[PlaySound(key="$d_avg_classicmiaow_1", volume=1)]
[Character(name="avg_npc_596_1#5$1")]
[name="小黑"]（猛然坐起）吵死了！这个人话说得这么快，谁能听清啊！
[name="小黑"]......
[Dialog]
[Character]
[Delay(time=0.51)]
[PlaySound(key="$d_avg_cardboard", volume=1)]
[Delay(time=1)]
他躺回箱中，头顶是浓云密布的夜空，耳朵里挤攘着各式各样的声音，但其中并没有他期盼听到的内容。
[Dialog]
[Character(name="avg_npc_596_1#4$1")]
[name="小黑"]小白......阿根......你们现在在哪儿呢？
[Dialog]
[Character]
[Delay(time=0.51)]
[name="？？？"]小黑？你在天台上吗？吃晚饭了！今天刚下过雨，在上面待着会着凉的，快下来吧！
[Dialog]
[PlaySound(key="$d_avg_humanchange", volume=1)]
[Delay(time=0.6)]
[Character(name="avg_lolxh_4067_1#1$1",fadetime=1,block=true)]
[Delay(time=1)]
[name="小黑"]（胡乱擦擦眼睛）
[Character(name="avg_lolxh_4067_1#2$1")]
[name="小黑"]知道啦！我马上就下来！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_rhodesroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]   
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_226_hmau_1#1$1")]
[characteraction(name="left", type="move", xpos=-150, fadetime=0, block=false)]
[characteraction(name="left", type="move", xpos=150, fadetime=1.5, block=false)]
[Delay(time=2)]
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_226_hmau_1#1$1",focus=1)]
[name="小黑"]吽哥，我来帮你拿碗筷了，今天几个人来吃饭？
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_226_hmau_1#1$1",focus=2)]
[name="吽"]不用了，碗筷槐琥已经端过去了。
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_226_hmau_1#1$1",focus=1)]
[name="小黑"]那还有什么我可以帮忙的吗？
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_226_hmau_1#5$1",focus=2)]
[name="吽"]嗯......？
[name="吽"]你这孩子身上怎么潮乎乎的！
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_226_hmau_1#6$1",focus=2)]
[name="吽"]小黑，你又上天台了是不是？难怪刚刚一直找不到你。阿，快帮小黑拿条干净毛巾来！这孩子头发都是湿的。
[Character(name="char_225_haak_1#1")]
[name="阿"]喂，小鬼，接着，不用谢了！
[Dialog]
[Character(name="avg_lolxh_4067_1#6$1")]
[Blocker(a=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[characteraction(name="middle", type="move", xpos=-15, fadetime=0.2, block=true)]
[Blocker(a=0, fadetime=0.2, block=true)]
[characteraction(name="middle", type="move", xpos=15, fadetime=0.2, block=true)]
[Delay(time=1)]
[Character(name="avg_lolxh_4067_1#5$1")]
[name="小黑"]哼，我才没有要谢你呢！
[Character(name="avg_226_hmau_1#10$1")]
[name="吽"]好了好了，别吵了，赶紧擦干净头发来吃饭吧，小黑。
[Dialog]
[Character]
[Delay(time=0.51)]
[name="槐琥"]小黑，快过来！这一大块排骨给你搁在饭碗里啦，你这个年纪的小菲林，正是长身体的时候，营养可不能耽误啦。
[Dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=0.51)]
[Character(name="avg_lolxh_4067_1#2$1")]
[name="小黑"]哎，槐琥姐，我去开门，一会儿就来。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[characteraction(name="middle", type="move", xpos=-250, fadetime=2.5, block=true)]
[Delay(time=2)]
[Character(fadetime=0.5)]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=1)]
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="avg_322_lmlee_1#4$1",fadetime=1,block=true)]
[Delay(time=1.5)]
[name="老鲤"]哎呦，是小黑啊。
[Character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"]哈哈，在走廊里我就闻到味道了，今天有粉蒸排骨对不对？
[Character(name="avg_lolxh_4067_1#2$1")]
[name="小黑"]嗯，吽哥今天一早去市场排队了。
[Character(name="avg_243_waaifu_1#4$1")]
[name="槐琥"]哼，鲤叔你鼻子很灵嘛，不巧了，我鼻子也很灵，说，你背后拎的瓶子是什么！
[Character(name="char_225_haak_1#2")]
[name="阿"]没错，老实交代，交瓶不杀。
[Character(name="avg_322_lmlee_1#1$1")]
[name="老鲤"]唉，办完事回来路过孙家的酒铺，那老孙头非得送四两黄酒来答谢我，我又拗不过他，只好收下了不是。
[name="老鲤"]说清楚了，这可不是我自己要买的。
[Character(name="avg_226_hmau_1#10$1")]
[name="吽"]那可真是谢谢孙老板，正好今天做菜我家里料酒用完了，这酒送得可太及时了。小黑，来帮我把这瓶黄酒收到灶台底下的柜子里。
[Character(name="avg_lolxh_4067_1#2$1")]
[name="小黑"]好嘞，吽哥。
[Character(name="avg_322_lmlee_1#5$1")]
[name="老鲤"]嘿，原来你这老实头才是最坏的，我还一口没喝呢！还有你这小毛头，跟着瞎起哄什么？
[Character(name="avg_243_waaifu_1#3$1")]
[name="槐琥"]哈哈哈，小黑干得好！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_rhodesroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]  
[Character(name="avg_322_lmlee_1#10$1")]
[name="老鲤"]嘶，你这孩子看着小小一只，吃起饭来倒是干劲十足，不错，我喜欢，认真吃饭的总没有坏孩子。
[Dialog]
[PlaySound(key="$d_avg_dis

... (全文34852字符)
```

### level_act13mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_indoor",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
月色如霜，倾泻在厅堂正中那方桐木桌上，桌旁坐着一对夫妻。女人不安地搓着双手，似乎是有话想要对撑着脑袋假寐的丈夫说。
她咽了口唾沫，支支吾吾地开了口。
[Dialog]
[Character(name="avg_npc_140",name2="avg_npc_141",fadetime=0.5,block=true)]
[Delay(time=1)]
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]当家的，我今天在厨房里......听见怪声了，哒哒哒的，怪吓人的。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]妇道人家大惊小怪，这有些年头的老房子都这样，到处都嘎吱嘎吱响个不停。你就是刚搬进来没听习惯。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]不是的，听、听起来像是有东西在墙里面。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]你这女人天天正事不干，净胡思乱想，我在外面从天亮忙到天黑，回家了连口热饭都没有。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]我、我不敢，我进了厨房背后总感觉凉飕飕的，像是有什么......在盯着我。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]放屁，我看你这婆娘就是躲懒，一身懒骨头挨顿打就好了。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]当家的，求你饶了我吧，我上次的伤还没好全呢。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]不想挨揍就赶紧去厨房给我温壶酒来，记得还要炸些花生米来配。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]当家的，我是真不敢进去了，那地方处处都透着诡异。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]我看你今天还真是皮痒了！
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]当家的，我错了，饶命啊！
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]看我今天不打死——
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]当家的你听，那声音又来了！
[Dialog]
[Character]
[Delay(time=0.51)]
哒、哒、哒。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]我没骗你，真的有声音。
[Dialog]
[Character]
[Delay(time=0.51)]
哒、哒、哒。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=1)]
[name="夫"]行，妈的老子这会儿就进厨房给你看个明白，要是我去了什么也没有，你就等着吧。
[Character(name="avg_npc_140", name2="avg_npc_141", focus=2)]
[name="妻"]我、我——
[Dialog]
[Character(name="avg_npc_140", name2="avg_npc_141")]
[Delay(time=0.51)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_empty",name2="avg_npc_141",fadetime=1,block=true)]
[delay(time=1.5)]
[Dialog]
[Character(fadetime=0.5)]
[Delay(time=1.5)]
窗外乌云蔽月，骤雨将至。
[Character(name="avg_npc_141")]
[name="妻"]当家的，当家的？
[name="妻"]你有看到什么吗？
[Dialog]
[Character]
[Delay(time=1)]
......
等了好久，妻子也没有听见回复，空气中静默一片，只有些细若游丝的声音从厨房中幽幽荡来。
她屏住呼吸，站起来凝神静听，只听得几声：
哒、哒、哒。
瞬间，妻子脸色剧变，瞳孔放大，豆大的冷汗从额头上沁出，就在她跌跌撞撞要跑去邻居家求助时，丈夫说话了。
[name="夫"]你来吧。
[Character(name="avg_npc_141")]
[name="妻"]当家的，你还好吗？
[Dialog]
[Character]
[Delay(time=0.51)]
[name="夫"]没事了。
妻子拿起蜡烛，缓缓向厨房挪去。厨房的门虚掩着，她推开门，里面漆黑一片，几乎不能视物。
她举起蜡烛照见了靠在墙边的丈夫，不由得松了一口气。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="妻"]你看见什么了吗？
[Character(name="avg_npc_140",blackstart=0.2,blackend=0.7)]
[name="夫"]你来吧，没事了。
[name="妻"]当家的，这话你刚刚就说了，怎么还说呢？
[Character(name="avg_npc_140",blackstart=0.2,blackend=0.7)]
[name="夫"]你来吧，没事了。
昏黄的烛光在丈夫脸上不断跳跃，妻子突然注意到，丈夫的表情从她进门便是一副空洞死寂的模样，口中则一直重复着刚才那句话：
你来吧，没事了。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_thunders_amb", volume=0.5)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.1, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
窗外一道落雷突然砸下，白光瞬时照亮了整个厨房。
妻子发现，丈夫并非靠在墙边，而是整个身体都融进了墙体，只剩一张惨白的脸露在外面。
与此同时，那熟悉的声音再次传来。
哒、哒、哒。
终于妻子再也抑制不住，大声惊叫起来。
[Dialog]
[stopmusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="？？？"]啊啊啊啊啊啊啊——你不要再说啦！
[Dialog]
[Character]
[Background(image="bg_bar_1",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="char_101_sora_1#4",fadetime=0.5,block=true)]
[Delay(time=0.6)]
[name="空"]啊啊啊啊啊！可颂你别说了，我、我不要听了，呜呜。
[Character(name="avg_lolxh_4067_1#1$1", name2="char_201_moeshd#2", focus=2)]
[name="可颂"]嘿嘿，我还没讲完呢，你不想知道那位妻子后来如何了吗？
[Character(name="char_101_sora_1#4")]
[name="空"]（捂耳朵）我不要听，你住口！
[Character(name="avg_lolxh_4067_1#1$1", name2="char_201_moeshd#2", focus=2)]
[name="可颂"]哈哈哈，那你呢，小朋友，你要不要听完啊？
[Character(name="avg_lolxh_4067_1#1$1", name2="char_201_moeshd#2", focus=1)]
[name="小黑"]你讲吧，我听着呢。
[Character(name="avg_lolxh_4067_1#1$1", name2="char_201_moeshd#2", focus=2)]
[name="可颂"]看你这故作镇静的小脸，别装了，你肯定是害怕了。
[Character(name="avg_lolxh_4067_1#1$1", name2="char_201_moeshd#2", focus=1)]
[name="小黑"]可是......确实没有那么可怕啊。
[Character(name="avg_lolxh_4067_1#1$1", name2="char_201_moeshd#2", focus=2)]
[name="可颂"]哼哼，不要逞强了，要是真的害怕，姐姐我就勉为其难地给你一个拥抱好了。
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd#2", focus=1)]
[name="小黑"]谢谢，但是真的不需要了，感觉那个姐姐好像更需要的样子。
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd#2", focus=2)]
[name="可颂"]（回头）
[Dialog]
[Character]
[Delay(time=0.51)]
[Character(name="char_101_sora_1#4")]
[name="空"]（抽泣）
[name="空"]好可怕......呜，可颂你真是太过分了，讲这么恐怖的故事。
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd#2", focus=2)]
[name="可颂"]呃......不好意思啊，哈哈，本来只是想吓吓这位小朋友来着，没承想吓到你这个大人了。
[Character(name="char_101_sora_1#4")]
[name="空"]呜，你是说我比小孩子还不经吓吗？
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd#4", focus=2)]
[name="可颂"]不是的不是的，哎呀，我错了，求你别哭了。
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd", focus=2)]
[name="可颂"]哎，小朋友，你真的一点都没有被吓到吗？
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd", focus=1)]
[name="小黑"]没有。
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd", focus=2)]
[name="可颂"]这也回答得太干脆了吧。
[Character(name="avg_lolxh_4067_1#2$1", name2="char_201_moeshd#3", focus=2)]
[name="可颂"]那你就不想知道最后

... (全文33236字符)
```

### level_act13mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_building_1",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
龙门上城区，上厂街，近卫局大楼
正午时分
近卫局，这个地方很特别，没事的人不会来这里，有事的人不想来这里，但总有人，他们会没事找事。
[Dialog]
[Character(name="char_015_lmg")]
[name="近卫局成员"]（坚守岗位）
[Dialog]
[Character]
[Delay(time=0.51)]
[Character(name="avg_npc_601_1#1$1",fadetime=0.5,block=true)]
[Delay(time=1)]
[name="？？？"]阿sir，你听过十二年前咸祥饭店的一起黑帮火并案吗？
[Character(name="char_015_lmg")]
[name="近卫局成员"]（没有理会）
[Character(name="avg_npc_601_1#1$1")]
[name="？？？"]阿sir，那十年前的雨夜宝华街大佬被劫案呢？
[Character(name="char_015_lmg")]
[name="近卫局成员"]（默不作声）
[Character(name="avg_npc_601_1#1$1")]
[name="？？？"]阿sir，那七年前的双刀案呢？
[Character(name="char_015_lmg")]
[name="近卫局成员"]这位先生，你说的事情我不知道，也从未听别人提起，请你不要干扰我，我还有执勤任务在身。
[Character(name="avg_npc_598_1#1$1")]
[name="阿根"]（扶额叹气）
[name="阿根"]唉，算了。
[Dialog]
[Character(fadetime=0.5)]
[Delay(time=0.6)]
[Character(name="char_empty", name2="char_015_lmg")]
[delay(time=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_598_1#1$1", name2="char_015_lmg",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_598_1#1$1", name2="char_015_lmg",focus=1)]
[name="阿根"]警察叔叔，我要报警！
[Character(name="avg_npc_598_1#9$1", name2="char_015_lmg",focus=1)]
[name="阿根"]你面前这个人，我刚刚看到他在不远处的广场偷窃别人的自行车！
[Character(name="avg_npc_601_1#1$1")]
[name="？？？"]什么？我怎么可能做这个！
[name="？？？"]小鬼头你胡说八道些什么！！
[Character(name="avg_npc_598_1#9$1", name2="char_015_lmg",focus=2)]
[name="近卫局成员"]这位先生，倒不必这么心虚。
[Character(name="avg_npc_598_1#9$1", name2="char_015_lmg",focus=2)]
[name="近卫局成员"]是不是你干的，我们查过监控便有分晓，现在麻烦你进来一趟了。小朋友，请你也跟来做个笔录吧。
[Character(name="avg_npc_601_1#1$1")]
[name="？？？"]呃......好。
[Character(name="avg_npc_598_1#2$1", name2="char_015_lmg",focus=1)]
[name="阿根"]（眨眼）好的，叔叔。
[name="阿根"]（洛洛姐，计划顺利进行中。）
[Dialog]
[Character(name="avg_4040_rockr_1#12$1",fadetime=0.5,block=true)]
[Delay(time=1)]
[name="洛洛"]（收到，洛克二十七，开启隐蔽模式。）
[Dialog]
[StopMusic(fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_lmstreet_2",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)] 
一天前
[Dialog]
[Character(name="avg_npc_598_1#1$1")]
[name="阿根"]如果没找错，应该就在这里了。
[Dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1)] 
[name="阿根"]您好，请问这里是流浪动物救助站吗？
[Dialog]
[Delay(time=1)] 
[PlaySound(key="$doorknockquite", volume=1)]
[Delay(time=1)] 
[name="阿根"]您好？
[Character(name="avg_npc_598_1#1$1",focus=-1)]
[name="？？？"]滚，我没空！
[Character(name="avg_npc_598_1#9$1")]
[name="阿根"]......我只是来打听些事情的，并没有恶意。
[Character(name="avg_npc_598_1#9$1",focus=-1)]
[name="？？？"]以为我不知道你们这群找过来的小屁孩打的什么主意吗？
[name="？？？"]头天兴致来了就上老子这里带一只回家去，第二天兴致没了再随意往街上一扔。
[Character(name="avg_npc_598_1#9$1")]
[name="阿根"]老板，你是不是误会什么了，我此次前来并非为了领养宠物，只是想向您打听一只走失的乌云兽。
[Character(name="avg_npc_598_1#9$1",focus=-1)]
[name="？？？"]我说了，给老子滚！
[name="？？？"]自己不看顾好，出事了就知道一窝蜂地拥到老子这里找。
[name="？？？"]滚，老子不是专门给你们这些没责任心的小崽子擦屁股的。
[name="？？？"]自己的屁股自己撅起来去擦！
[name="？？？"]快给老子滚！
[Character(name="avg_npc_598_1#10$1")]
[name="阿根"]老板，你能好好听我解释吗！
[Character(name="avg_npc_598_1#10$1",focus=-1)]
[CameraShake(duration=0.5, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"]滚啊！！！
[Character(name="avg_npc_598_1#8$1")]
[name="阿根"]喂，你！老板！
[Dialog]
[PlaySound(key="$d_avg_knockdoorfast", volume=0.7)]
[PlaySound(key="$d_avg_knockdoorfast", volume=0.7,delay=0.8)]
[Delay(time=3)] 
[Character(name="avg_npc_598_1#7$1")]
[name="阿根"]......什么啊，什么脾气啊这是。
[Dialog]
[Character]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[Character(name="avg_npc_598_1#7$1", name2="char_empty")]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="avg_npc_598_1#7$1", name2="avg_npc_032",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_598_1#7$1", name2="avg_npc_032",focus=2)]
[name="邻居"]小朋友，别敲了，他不会开门的。
[name="邻居"]这人脾气就这样，臭得很。
[Character(name="avg_npc_598_1#1$1", name2="avg_npc_032",focus=1)]
[name="阿根"]姐姐，你好，你......认识这里边的人吗？
[Character(name="avg_npc_598_1#1$1", name2="avg_npc_032",focus=2)]
[name="邻居"]我就住在隔壁，但和他一年也说不上几句话，这人脾气不好，来历也不干不净，是叙拉古来的黑帮，不长眼的才往他跟前凑呢。
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=1)]
[name="阿根"]他不是做动物救助的工作吗？再坏也不会坏到哪儿去吧？
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=2)]
[name="邻居"]到底是小孩子，别人说什么都信，他这院子大门一关，里面有没有什么腌臜事别人哪能瞧见。
[name="邻居"]人心啊，隔层肚皮就不能信了，更何况隔道门呢。
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=1)]
[name="阿根"]姐姐，你是见到什么了，才这样说的吗？
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=2)]
[name="邻居"]前几日，有近卫局的人找过来了。
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=1)]
[name="阿根"]近卫......局？
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=2)]
[name="邻居"]嗨，你是外来的吧，就是有警官上他这儿来了，说是这家伙非法藏匿扣留警用循兽？
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=1)]
[name="阿根"]警用的啊，这......不是犯法的事吗？
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=2)]
[name="邻居"]可不是，近卫局的循兽他都敢往屋子里领，还有什么他不敢。
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=1)]
[name="阿根"]那他收留这些动物的目的......
[Character(name="avg_npc_598_1#9$1", name2="avg_npc_032",focus=2)]
[name="邻居"]我常看见他带动物回来，但很快就又送出去了，说不定......是卖到黑市的肉贩子那里去了。
[Character(name="avg_npc_598_1#5$1", name2="avg_npc_032

... (全文45025字符)
```

### level_act13mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="31_g2_luo_reception",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_597_1#2$1",fadetime=0.8)]
[Delay(time=2)]
[name="小白"]敏敏姐，早上好。
[Character(name="avg_npc_597_1#2$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]早啊，小白，你今天——
[Dialog]
[Character(name="avg_npc_597_1#2$1",name2="char_016_medic",focus=3)]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[name="传呼频道"]麻烦值班医生来十一号病房，患者今早血液源石结晶密度骤升，肋间的体表源石迅速生长，出现剧烈疼痛，据判断应该是急性发作。
[Character(name="avg_npc_597_1#2$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]准备急救药品与设施，我马上到。
[Dialog]
[PlaySound(key="$transmission")]
[Delay(time=2)]
[Character(name="avg_npc_597_1#5$1",name2="char_016_medic",focus=1)]
[name="小白"]敏敏姐，我有什么可以......？
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="bgs",volume=0.6)]
[Character(name="avg_npc_597_1#5$1",name2="char_016_medic")]
[Character(name="avg_npc_597_1#5$1",name2="char_empty",fadetime=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[StopSound(channel="bgs", fadetime=0.5)]
[Character(name="avg_npc_597_1#5$1",name2="char_empty",focus=3)]
[name="医疗干员"]小白，等我回来再说！
[Character(name="avg_npc_597_1#1$1",name2="char_empty",focus=1)]
[name="小白"]哦，好、好的。
[Dialog]
[Character]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_4040_rockr_1#12$1",fadetime=0.8)]
[Delay(time=2)]
[name="洛洛"]小白，早啊，早饭有吃过吗？
[Character(name="avg_npc_597_1#2$1",name2="avg_4040_rockr_1#12$1",focus=1)]
[name="小白"]洛洛姐，我一早就去食堂了。
[Character(name="avg_npc_012")]
[name="后勤干员"]洛洛姐，你现在有空吗？办事处的污水处理器好像出了故障，方便来看下吗？
[Character(name="avg_npc_597_1#2$1",name2="avg_4040_rockr_1#5$1",focus=2)]
[name="洛洛"]好的，没问题，我正好带着工具包，麻烦你带路了。
[Character(name="avg_npc_597_1#2$1",name2="avg_4040_rockr_1#5$1",focus=1)]
[name="小白"]洛洛姐，我也可以跟你去......
[Character(name="avg_npc_597_1#2$1",name2="avg_4040_rockr_1#12$1",focus=2)]
[name="洛洛"]那就下午再见啦，小白。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[StopSound(channel="bgs", fadetime=1)]
[Character(name="avg_npc_597_1#5$1",name2="char_empty",focus=1,fadetime=0.5)]
[multiline(name="小白")]呃......看看我能帮到你些什么......
[Character(name="avg_npc_597_1#1$1",name2="char_empty",focus=1)]
[multiline(name="小白")]吗？
[Dialog]
[Delay(time=1)]
[Character(name="avg_npc_597_1#9$1",name2="char_empty",focus=1)]
[name="小白"]嗯......看来大家都很忙呢。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="char_358_lisa_1#1",fadetime=0.8)]
[Delay(time=2)]
[name="铃兰"]小白，早上好啊！
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=1)]
[name="小白"]早呀铃兰，你这是打算出门吗？
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=2)]
[name="铃兰"]嗯，这几天有几位病人去世了，留下了些遗物，我带出去做个简单的告别，希望他们的亡魂能得到慰藉。
[Character(name="avg_npc_597_1#1$1",name2="char_358_lisa_1#1",focus=1)]
[name="小白"]办事处......每天都会有人离开吗？
[Character(name="avg_npc_597_1#1$1",name2="char_358_lisa_1#4",focus=2)]
[name="铃兰"]唉，虽然医疗干员们都尽全力抢救了，但是难免会有不遂人愿的情况。
[Character(name="avg_npc_597_1#6$1",name2="char_358_lisa_1#4",focus=1)]
[name="小白"]那葬礼上我能不能帮上你什么忙？我也想为他们做点什么......
[Character(name="avg_npc_597_1#6$1",name2="char_358_lisa_1#1",focus=2)]
[name="铃兰"]葬礼？不是的不是的，只是一个很小的仪式。
[name="铃兰"]所以不用啦，小白，我一个人去就可以。
[name="铃兰"]你留在这里就很好了，我听很多干员说，自从你来到这里，患者们多了很多笑容呢。
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=1)]
[name="小白"]哈哈哈，真的吗？
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=2)]
[name="铃兰"]嗯，矿石病的治疗过程枯燥又漫长，这几天你陪在患者身边聊天解闷，他们心里都是很开心的。
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=1)]
[name="小白"]那就太好了，其他的我也帮不到什么了......
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#4",focus=2)]
[name="铃兰"]对于我们来说，交谈时不带着恐惧的目光，就已经足够我们感激了。小白，你已经做得很好了。
[Character(name="avg_npc_597_1#9$1",name2="char_358_lisa_1#4",focus=1)]
[name="小白"]这难道不是应该做的吗？你越是这样说我越是觉得什么都没做......
[Character(name="avg_npc_597_1#9$1",name2="char_358_lisa_1#1",focus=2)]
[name="铃兰"]呀，时候不早了，我得走了。
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=1)]
[name="小白"]那你快去吧！
[Character(name="avg_npc_597_1#2$1",name2="char_358_lisa_1#1",focus=2)]
[name="铃兰"]那就晚上见啦！
[Character(name="avg_npc_597_1#3$1",name2="char_358_lisa_1#1",focus=1)]
[name="小白"]再见！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_597_1#3$1",name2="char_empty",fadetime=1)]
[Delay(time=2)]
[Character(name="avg_npc_597_1#1$1",name2="char_empty",focus=1)]
[name="小白"]（噘嘴）唔，又是没帮上什么忙的一天......
[Character(name="avg_npc_597_1#7$1",name2="char_empty",focus=1)]
[name="小白"]哥哥也真是，明明说好一起去帮小沅找乌云兽，那天却自己一个人去找线索，让我先回来。
[Character(name="avg_npc_597_1#9$1",name2="char_empty",focus=1)]
[name="小白"]......是我主动答应别人的事，最后却麻烦了哥哥。
[name="小白"]那时候在荒地上也是，没有一件事可以帮到哥哥，还净让他操心。
[Character(name="avg_npc_597_1#1$1",name2="char_empty",focus=1)]
[name="小白"]我还能做些什么事呢？总不能一直依赖着哥哥呀。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_597_1#1$1",name2="avg_npc_598_1#1$1",fadetime=0.5)]
[characteraction(name="right", type="move", xpos=200, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1.7, block=false)]
[Delay(time=2)]
[Character(name="avg_npc_597_1#1$1",name2="avg_npc_598_1#2$1",focus=2)]
[name="阿根"]想什么呢，小白？
[Character(name="avg_npc_597_1#5$1",name2="avg_npc_598_1#2$1",focus=1)]
[name="小白"]哥哥，你什么时候回来的？你找到乌云兽的消息了吗？
[Character(name="avg_npc_597_1#5$1",name2="avg_npc_598_1#6$1",focus=2)]
[name="阿根"]唉，有消息，却是坏消息，那只乌云兽已经......不在了。
[Character(name="avg_npc_597_1#9$1",name2="avg_npc_598_1#6$1",focus=1)]
[name="小白"]怎么会这样......那小沅她知道了吗？
[Character(name="avg_npc_597_1#9$1",name2="avg_npc_598_1#10$1",focus=2)]
[name="阿根"]嗯，我刚刚就是从她的病房过来的。
[Character(name="avg_npc_597_1#9$1",name2="avg_npc_598_1#10$1",focus=1)]
[name="小白"]她一定很难过......怎么办啊，哥哥？
[Ch

... (全文43812字符)
```

### level_act13mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_lungmenbridge",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Subtitle(text="朝霞，是黑夜与白天的一次离别。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="晚霞，是白天与黑夜的一场重逢。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="分离后，再次相遇，然后日月交替，时间流淌，万物开始繁衍，历史逐步推进，文明得以延续，这一切的一切，不过开始于一场相遇和一次离别。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——《傍晚游记》，佚名，乌萨斯。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.4)]
[delay(time=1)]
[Character(name="avg_npc_597_1#5$1",fadetime=0.5)]
[delay(time=1)]
[multiline(name="小白")]小黑......？
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_597_1#3$1")]
[multiline(name="小白")]小黑！
[Character]
[Dialog]
[Image(image="31_luo_i2",x=-100, y=0, xScale=1.2, yScale=1.2,fadetime=1)]
[ImageTween(xFrom=-100, yFrom=0, xTo=0, yTo=-0, duration=30, block=false)]
[name="小黑"]小白！！
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[Delay(time=1)]
[StopSound(channel="bgs", fadetime=0.5)]
[name="小白"]真的是你吗？
[name="小黑"]嗯！是我！
[name="小白"]我还以为再也见不到你了......
[name="阿根"]我们一直在找你。
[name="小黑"]我也是！你们没事吧？
[name="阿根"]（拍拍小黑肩膀）好着呢，别担心。
[name="小白"]那小黑呢？有没有受伤呀？没有饿肚子吧？
[name="小黑"]（摇头）没有，我很强的！每天都有好好吃饭！
[name="小白"]哈哈，那可真是太好啦！
[name="阿根"]只是没想到，我们的重逢是在这种地方啊。
[name="小白"]能再见就好啦！
[name="小黑"]嗯！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Character(name="avg_lolxh_4067_1#3$1",name2="avg_npc_597_1#3$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_lolxh_4067_1#3$1",name2="avg_npc_597_1#2$1",focus=2)]
[name="小白"]所以你现在是在帮那位鲤先生打工吗？
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_597_1#2$1",focus=1)]
[name="小黑"]嗯，没错，他收留了我，我也不好意思在那里白吃白住。
[name="小黑"]那你们呢？你们在那个罗德岛过得怎么样？
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_598_1#2$1",focus=2)]
[name="阿根"]我们还没有去过罗德岛的本舰，目前只是跟着他们的干员来到了这里的办事处。
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_598_1#2$1",focus=1)]
[name="小黑"]这里的办事处又是什么样的？
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_598_1#2$1",focus=2)]
[name="阿根"]和会馆很像，主要是为了帮助一些很特殊的人。
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_598_1#7$1",focus=2)]
[name="阿根"]或许你见过，就是身上会长石头的人。
[Character(name="avg_lolxh_4067_1#7$1",name2="avg_npc_598_1#7$1",focus=1)]
[name="小黑"]我知道......那些人过得都很不好，其他人对他们的态度都很差。
[Character(name="avg_lolxh_4067_1#7$1",name2="avg_npc_598_1#10$1",focus=2)]
[name="阿根"]是啊，所以我挺佩服罗德岛的干员们。
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_598_1#10$1",focus=1)]
[name="小黑"]我之前一直很担心，你们来到这里后会染上那样的病，在那里，你们不会很危险吗？
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_598_1#1$1",focus=2)]
[name="阿根"]办事处里有很完善的防护措施，至于小白，我一直有很小心地保护她。
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_597_1#2$1",focus=2)]
[name="小白"]小黑，你不要担心，在办事处工作的干员里也有很多人没有得病。
[name="小白"]那边的洛洛姐就是！
[name="小白"]她帮助那些病人的时间很长了，也没出什么事。
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_597_1#1$1",focus=1)]
[name="小黑"]（看向洛洛）
[Character(name="avg_4040_rockr_1#1$1",name2="char_358_lisa_1#1",focus=2)]
[name="铃兰"]洛洛姐，那个小菲林在看你。
[Character(name="avg_4040_rockr_1#5$1",name2="char_358_lisa_1#1",focus=1)]
[name="洛洛"]是吗？
[Character(name="avg_4040_rockr_1#12$1",name2="char_358_lisa_1#1",focus=1)]
[name="洛洛"]（朝小黑挥挥手）
[Character(name="avg_lolxh_4067_1#8$1")]
[CameraShake(duration=0.5, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="小黑"]（僵住）唔！
[Character(name="avg_npc_598_1#2$1")]
[name="阿根"]别紧张，她们都是很好的人。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_lolxh_4067_1#8$1",name2="avg_4040_rockr_1#12$1")]
[characteraction(name="right", type="move", xpos=200, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1.5, block=false)]
[Delay(time=2)]
[Character(name="avg_lolxh_4067_1#8$1",name2="avg_4040_rockr_1#12$1",focus=2)]
[name="洛洛"]你就是小黑吧，小白和阿根和我提过你。
[name="洛洛"]果然和我们想的一样可爱。
[Character(name="avg_lolxh_4067_1#4$1",name2="avg_4040_rockr_1#12$1",focus=1)]
[name="小黑"]你、你好，洛洛姐。
[Character(name="avg_lolxh_4067_1#4$1",name2="avg_4040_rockr_1#12$1",focus=2)]
[name="洛洛"]小黑，小沅有些话想和你说。
[name="洛洛"]过来吧，小沅。
[Dialog]
[Character(name="avg_lolxh_4067_1#4$1",name2="char_empty",fadeime=0.3)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_045_nn_1",fadeime=0.5)]
[characteraction(name="right", type="move", xpos=300, fadetime=0, block=false)]
[characteraction(name="right", type="move", xpos=-300, fadetime=2.5, block=false)]
[Delay(time=3)]
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_045_nn_1",focus=2)]
[name="小沅"]嗯，你好......
[Character(name="avg_npc_597_1#2$1")]
[name="小白"]（小黑，你也笑一下啊，小沅她看到你很紧张的。）
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_045_nn_1",focus=1)]
[name="小黑"]唔，好。
[Dialog]
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_045_nn_1",focus=1)]
[delay(time=1)]
[name="小黑"]呃，你好，小沅，你想和我说什么......？
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_045_nn_1",focus=2)]
[name="小沅"]嗯，谢谢......谢谢你帮我找到了六十七。
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_045_nn_1",focus=1)]
[name="小黑"]不用谢，如果不是帮它，我也不会找到小白和阿根。
[Character(name="avg_lolxh_4067_1#2$1",name2="avg_npc_045_nn_1",focus=2)]
[name="小沅"]原来你们也认识，今天真的是个好日子，那些大家心里挂念着的，最终都见到了。
[name="小沅"]六十七，你说是不是？
[Character]
[Character(name="avg_npc_599_1#1$1",fadetime=0.5)]
[name="乌云兽"]（舔爪子）
[name="乌云兽"]嗷......
[Character(name="avg_lolxh_4067_1#8$1",name2="avg_npc_045_nn_1",focus=1)]
[name="小黑"]你叫它六十七？
[Character(name="avg_lolxh_4067_1#8$1

... (全文33306字符)
```

### level_act13mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_canteen",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$warm_intro",key="$warm_loop", volume=0.4)]
[Delay(time=1)]
[Blocker(a=0.8, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="比丢的一天", x=300, y=370, alignment="center",size=24, width=700)]
[Subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlaySound(key="$d_avg_classicbiu_1")]
[Character(name="avg_npc_604_1#2$1")]
[characteraction(name="middle", type="move", xpos=-300,ypos=50, fadetime=0, block=false)]
[characteraction(name="middle", type="move", xpos=800,fadetime=1.5,block=false)]
[Blocker(a=0, fadetime=0.8, block=true)]
[Character(fadetime=0.3)]
[name="比丢"]Biu！
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="食堂阿姨"]我的食材呢？
[name="食堂阿姨"]我刚做好的菜呢？
[name="食堂阿姨"]小刻是不是被放进来了？！
[Character(name="char_196_sunbr_1#1")]
[name="古米"]那个那个那个东西怎么瞬间变了好几个颜色？
[Character(name="char_355_ethan_1")]
[name="伊桑"]哦？他们从哪里找到的这个小玩意儿？和我蛮像的。
[name="伊桑"]医疗部的，你们要对它好点儿啊。
[Dialog]
[Delay(time=1)]
[name="伊桑"]等等，你们不会还要我也去配合检查吧？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_classicbiu_1")]
[Character(name="avg_npc_604_1#2$1")]
[characteraction(name="middle", type="move", xpos=300,ypos=50, fadetime=0, block=false)]
[characteraction(name="middle", type="move", xpos=-800,fadetime=1.5,block=false)]
[Blocker(a=0, fadetime=0.8, block=true)]
[Character(fadetime=0.3)]
[name="比丢"]Biu！
[Character]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="玩耍的孩子"]玩具一下子就不见了？
[name="逃课的孩子"]呜啊！肯定是坚雷教官发现我逃课来抓我了，怎么办！
[name="冷静的孩子"]慌什么，你就说是自己追查离奇消失的玩具一路来到这里，即将发现罗德岛隐藏在最深处的秘密......
[Dialog]
[Character(name="char_349_chiave#4",fadetime=0.5)]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Delay(time=1)]
[name="贾维"]真的吗？
[name="贾维"]还有这种事儿？
[name="贾维"]加我一个。
[Character]
[name="冷静的孩子"]？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Character(name="avg_npc_604_1#2$1")]
[characteraction(name="middle", type="move", ypos=540, fadetime=0, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_npc_604_1#2$1")]
[characteraction(name="middle", type="move", ypos=-60, fadetime=0.6, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_biu_2")]
[characteraction(name="middle", type="move", ypos=-480,fadetime=0.5,block=false)]
[name="比丢"]Biu！
[Character(fadetime=0)]
[Character(name="avg_npc_012")]
[name="工程部干员"]——？
[CameraShake(duration=0.2, xstrength=10, ystrength=10, vibrato=20, randomness=90, fadeout=true, block=false)]
[name="工程部干员"]什么东西？你要干什么？！
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[name="工程部干员"]那是刚做出来的零件，不能吃——！
[Dialog]
[Character(name="char_empty",name2="avg_npc_604_1#1$1")]
[characteraction(name="right", type="move", xpos=-150, fadetime=0, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_biu_1")]
[Character(name="avg_npc_596_1#5$1",name2="avg_npc_604_1#1$1",fadetime=0.2)]
[Characteraction(name="left", type="jump", xpos=150, power=10,times=1, fadetime=0.6, block=true)]
[delay(time=1)]
[Character(name="avg_npc_596_1#5$1",name2="avg_npc_604_1#4$1")]
[characteraction(name="right", type="move", xpos=-150, fadetime=0, block=true)]
[characteraction(name="right", type="move", xpos=300, fadetime=0.8, block=true)]
[characteraction(name="left", type="move", xpos=300, fadetime=0.8, block=true)]
[Blocker(a=0, fadetime=0.5, block=true)]
[Character(fadetime=0.3)]
[delay(time=1)]
[Character(name="avg_npc_012")]
[name="工程部干员"]喔——是Miss.Christine吗？
[name="工程部干员"]呼，帮大忙了，待会儿要去谢谢傀影干员了。看着不好相处，原来是个热心肠的人啊。
[name="工程部干员"]向女士致敬！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(fadetime=0)]
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_604_1#5$1")]
[characteraction(name="left", type="move", xpos=150, fadetime=0, block=true)]
[characteraction(name="right", type="move", xpos=-150, fadetime=0, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_604_1#5$1",focus=2)]
[PlaySound(key="$d_avg_classicbiu_2")]
[name="比丢"]Biu......！
[Character(name="avg_lolxh_4067_1#1$1",name2="avg_npc_604_1#5$1",focus=1)]
[name="小黑"]抓住了！
[Character(fadetime=0)]
[Character(name="avg_npc_597_1#7$1",name2="avg_npc_598_1#1$1",focus=1)]
[name="小白"]比丢，你怎么这么不听话呀？
[name="小白"]再这样乱跑的话，你会受伤的！
[Character(name="avg_npc_597_1#7$1",name2="avg_npc_598_1#9$1",focus=2)]
[name="阿根"]唔，你这是什么颜色啊？
[Character(name="avg_npc_604_1#2$1")]
[name="比丢"]Biu~
[Character(name="avg_npc_597_1#7$1",name2="avg_npc_598_1#10$1",focus=2)]
[name="阿根"]感觉它刚才吃了不少东西啊。
[name="阿根"]小黑，你是在哪里找到比丢的？
[Character(name="avg_lolxh_4067_1#1$1")]
[name="小黑"]就是走廊尽头的那间屋子。
[name="小黑"]它之前还去了玩具屋和餐厅，吃了饭菜还有玩具，但并不是那里的人喂它的，是它自己直接就吃掉了。
[Character(name="avg_npc_597_1#9$1",name2="avg_npc_598_1#10$1",focus=1)]
[name="小白"]啊......我们得去给人家道歉才行呢。
[Character(name="avg_npc_597_1#9$1",name2="avg_npc_598_1#2$1",focus=2)]
[name="阿根"]是呢，接下来可要好好看好比丢呀。
[Character(name="avg_npc_597_1#2$1",name2="avg_npc_598_1#2$1",focus=1)]
[name="小白"]会的！那我们走吧~
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[character(fadetime=0)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_npc_597_1#6$1",name2="avg_npc_598_1#1$

... (全文34543字符)
```


## 统计

- 总字符数：225203
- 对话行数：1785


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
