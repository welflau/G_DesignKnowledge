# 明日方舟 · 活动剧情 · act16mini（6段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act16mini」完整剧情脚本（6个文件，1840行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act16mini
- 脚本文件数：6

### level_act16mini_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_metalpipe")]
[PlaySound(key="$d_avg_ptbolng", volume=0.4, loop=true, channel="people")]
[Subtitle(text="热腾腾的锅子里，菜汤咕嘟咕嘟冒泡的声音，很好听。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="爸爸收音机里的雪花声，磨刀爷爷的吆喝声，身边这个动力炉的机械运转声......虽然它们也很好听，但是我听不到了，或者......很快就要听不到了。", x=300, y=330, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="火苗燃烧着，是在提醒我，要开心一点，再开心一点......就像爸爸期待的那样。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="好像火候不太够呀，加一点火力吧，呼——", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopsound(channel="people", fadetime=1)]
[PlaySound(key="$d_avg_axehitscrape", volume=0.2)]
[PlaySound(key="$d_avg_axehitscrape",channel="hb",loop=false, volume=0.2,delay=0.2)]
[PlaySound(key="$d_avg_axehitscrape",channel="hb",loop=false, volume=0.2,delay=0.4)]
[delay(time=1)]
[Subtitle(text="嗯？这个声音是......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[musicvolume(volume=0.3, fadetime=1)]
[Dialog]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="46_g2_rmbttransporter",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[musicvolume(volume=0.6, fadetime=1)]
[PlaySound(key="$d_avg_axehitscrape", volume=0.4)]
[PlaySound(key="$d_avg_axehitscrape",channel="hb",loop=false, volume=0.4,delay=0.2)]
[Dialog]
[charslot(slot = "left", name = "avg_npc_1183_1#1$1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "right", name = "avg_4081_warmy_1#1$1",posfrom = "200,0", posto = "0,0",duration = 1,isblock=false)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_4081_warmy_1#5$1", focus="r")]
[name="小锅盖"]兰娜姐！你怎么又在敲碗？
[name="小锅盖"]之前不是说过了嘛，不要敲碗呀！吵到别人可怎么办？
[charslot(slot = "l", name = "avg_npc_1183_1#2$1", focus="l")]
[name="阿兰娜"]敲就敲了，在我的车上我还不能做主了？车站里本来就闹哄哄的，能吵到人才怪哩！
[charslot(slot = "r", name = "avg_4081_warmy_1#9$1", focus="r")]
[name="小锅盖"]借口。
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]我无聊嘛......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]你今天莫名其妙做了这么多菜，害得我等这么老半天，肚子都要饿扁了！
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]为了防止这些菜一下子冷掉，我当然得发出点动静来提醒它们——慢点变凉，慢点变凉，还要等着小锅盖一起吃呢。
[charslot(slot = "r", name = "avg_4081_warmy_1#12$1", focus="r")]
[name="小锅盖"]还是借口......真是的，兰娜姐总是不把事情放在心上，像个任性的小孩子。
[charslot(slot = "r", name = "avg_4081_warmy_1#11$1", focus="r")]
[name="小锅盖"]要是真觉得无聊，你还不如来厨房帮帮我呢！
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]哎呀，毕竟你才是“六星级大厨”嘛。小锅盖真的很厉害！
[charslot(slot = "r", name = "avg_4081_warmy_1#7$1", focus="r")]
[name="小锅盖"]能不能不要叫我小锅盖啦——
[charslot(slot = "l", name = "avg_npc_1183_1#4$1", focus="l")]
[name="阿兰娜"]——这个红红的是什么？
[charslot(slot = "r", name = "avg_4081_warmy_1#1$1", focus="r")]
[name="小锅盖"]哦，这个是番茄烩瘤兽肉！
[charslot(slot = "r", name = "avg_4081_warmy_1#4$1", focus="r")]
[name="小锅盖"]刚刚出锅，肯定超好吃的！
[charslot(slot = "l", name = "avg_npc_1183_1#2$1", focus="l")]
[name="阿兰娜"]番茄烩瘤兽肉？怎么是这个颜色的？汤汁不应该更黄一点嘛——
话音未落，阿兰娜的勺子已经伸进了热腾腾的菜碗里，把一大块瘤兽肉塞进嘴中。
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[CameraShake(duration=0.2, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
虽然舌头被烫得打转，但阿兰娜还是伸出了大拇指。
[charslot(slot = "l", name = "avg_npc_1183_1#2$1", focus="l")]
[name="阿兰娜"]......唔......嘶......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]真好吃啊！不愧是我们运载车上的“六星级大厨”。
[charslot(slot = "r", name = "avg_4081_warmy_1#1$1", focus="r")]
[name="小锅盖"]哼哼~
[charslot(slot = "r", name = "avg_4081_warmy_1#4$1", focus="r")]
[name="小锅盖"]不过，这次兰娜姐带回来的肉格外新鲜，所以不用太多调料也香香的！
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]是吗？看来菜场老板知道我们要走，特意给了新到的食材，不枉我们当了他两年熟客。
[charslot(slot = "r", name = "avg_4081_warmy_1#10$1", focus="r")]
[name="小锅盖"]不对哦，兰娜姐，听你的描述，我觉得老板从一开始就很关照我们。
[charslot(slot = "r", name = "avg_4081_warmy_1#10$1", focus="r")]
[name="小锅盖"]我想象中，他一定矮矮的，脾气很好，围裙脏脏的，像胖铁头叔叔一样。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]啊，不，他是那种，每天拿着菜刀站在门口，就能让菜场里再也不会被顺走哪怕一根萝卜的家伙。
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]......哈哈，等你长大了，我就允许你自己上街转转。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]说起来，上次吃这个，番茄烩瘤兽肉？是什么时候来着？
[charslot(slot = "r", name = "avg_4081_warmy_1#10$1", focus="r")]
[name="小锅盖"]上一次？
[charslot(slot = "r", name = "avg_4081_warmy_1#10$1", focus="r")]
[name="小锅盖"]应该是兰娜姐和我一起吃的第一顿饭哦。
[charslot(slot = "r", name = "avg_4081_warmy_1#1$1", focus="r")]
[name="小锅盖"]还是兰娜姐亲自下厨呢！ 
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]噢，那好像确实是很久远的事情了。你还记得啊。
[charslot(slot = "r", name = "avg_4081_warmy_1#1$1", focus="r")]
[name="小锅盖"]那当然啦！
[charslot(slot = "r", name = "avg_4081_warmy_1#11$1", focus="r")]
[name="小锅盖"]你说“做饭只是一件拿手的小事”，结果却做了一锅超——级酸的番茄烩瘤兽肉。
[charslot(slot = "l", name = "avg_npc_1183_1#5$1", focus="l")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="阿兰娜"]咳咳，我哪知道那个品种的番茄那么酸啊。本来还觉着汤汁亮黄亮黄的，看上去那么鲜美，肯定很下饭呢。
[charslot(slot = "r", name = "avg_4081_warmy_1#1$1", focus="r")]
[name="小锅盖"]我记得兰娜姐自己尝过以后，也被酸得龇牙咧嘴。
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]反、反正能填饱肚子就行了！口味是次要的！你不是照样都吃精光了嘛！
[charslot(slot = "r", name = "avg_4081_warmy_1#12$1", focus="r")]
[name="小锅盖"]浪费粮食是不对的！而且......
[charslot(slot = "r", name = "avg_4081_warmy_1#12$1", focus=

... (全文45722字符)
```

### level_act16mini_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.2,fadetime=1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.2,fadetime=1)]
[Background(image="46_g4_rmbtwild_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="bgs")]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="沙地上扬起一条狭长的尘带，掩埋了履带压过的痕迹。这样的景象我已经看过无数次。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="他们叫我“荒野上的阿兰娜”，可我很清楚，我并不是无可抵挡的沙暴，我只是一团停停走走的风滚草。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="工人们的赌局是我表现的展台，乘客们的奇遇是我吹嘘的谈资。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可......那些真的是属于我的故事吗？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="孤独的船航行在大地上，底下是灰黄茫漠的沙野，头顶是金灿灿的太阳。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="它并未循着过往的路径，它前行的方向存在着偏移。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="它在寻求什么？它在逃避什么？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="那......我又在寻求什么？我又在逃避什么？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[StopSound(channel="bgs", fadetime=3)]
[curtain(direction = 0,fillfrom = 0.2,fillto = 0,fadetime=3)]
[curtain(direction = 4,fillfrom = 0.2,fillto = 0,fadetime=3)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=3)]
[PlaySound(key="$d_avg_truckengine", volume=0, loop=true, channel="bgs")]
[SoundVolume(channel="bgs", volume=0.7, fadetime=0.5)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[name="阿兰娜"]天气不错，都能看得清远处的源石晶簇。看来我们会顺利抵达目的地。
[name="？？？"]......
[name="阿兰娜"]沉默，又是沉默。你就没有什么话想说吗？
[name="阿兰娜"]当驾驶员这么长时间，我还从未遇见过像你这样无聊的乘客。
[name="？？？"]说什么？
[StopSound(channel="bgs", fadetime=4)]
[PlaySound(key="$d_avg_faucetoff", volume=0.6)]
[name="阿兰娜"]好吧，算了......哎别别别——你怎么又把它举起来了？
[name="？？？"]你在做什么？
[name="阿兰娜"]我就是想把窗户摇下来，通通风！我没想干别的，我保证！
[name="？？？"]行。
[name="阿兰娜"]能不能先把这个大家伙，从我脑袋边移开？我们好商量。
[dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="46_g2_rmbttransporter",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1183_1#6$1", focus="l",duration=0.5)]
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r",duration=0.5)]
[delay(time=0.7)]
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]......
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]继续往咧嘴谷开，我不会伤害你。
[charslot(slot = "l", name = "avg_npc_1183_1#9$1", focus="l")]
[name="阿兰娜"]你劫了我的车，还用这把不知道是弩还是火炮的玩意指着我，却说不会伤害我？这里面装的是什么？
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]是特制的箭，感染生物很怕它。
[charslot(slot = "l", name = "avg_npc_1183_1#6$1", focus="l")]
[name="阿兰娜"]我其实比较希望你的答案是“胡萝卜”或者“糖果”，而不是“箭”。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]不过还好，我不是感染生物，看来暂时还不需要太怕它。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]可你要是一直这样指着我的话——
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]唉。
[charslot(slot = "l", name = "avg_npc_1183_1#2$1", focus="l")]
[name="阿兰娜"]如果你扣下扳机，我是说如果——如果我倒下了，这辆车可怎么办？
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]你倒下了，我也能开。
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]你能开？等你接过操纵杆，它早就失控了。
[charslot(slot = "l", name = "avg_npc_1183_1#6$1", focus="l")]
[name="阿兰娜"]它会直直地冲向悬崖，或者撞进那些巨大的源石晶簇里。
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]轰——
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]......
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]好吧，就算你能开，就算这辆车也不会失控。
[charslot(slot = "l", name = "avg_npc_1183_1#9$1", focus="l")]
[name="阿兰娜"]你杀了我也就算了，可车上其他人呢？他们......
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]他，那个札拉克的安全怎么办？
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]我给你们机会下车了，是你们不走。
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]我只是要你的车。
[charslot(slot = "l", name = "avg_npc_1183_1#9$1", focus="l")]
[name="阿兰娜"]那你就不觉得奇怪吗？别人为什么不下车？
[charslot(slot = "l", name = "avg_npc_1183_1#9$1", focus="l")]
[name="阿兰娜"]我要是你，我就会在心里害怕他。
[charslot(slot = "l", name = "avg_npc_1183_1#9$1", focus="l")]
[name="阿兰娜"]一个肇事逃逸的冒失鬼，一个职场失意的倒霉蛋......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]或者，是一个跟踪你的便衣警察？别看他现在哆哆嗦嗦的，说不定身手了得呢！
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]谁能没有一点秘密呢？你说对不对？
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", focus="r")]
[name="劫车人"]......嗯。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]至于我不下车的原因嘛——作为公司的雇员，我有责任保护公司的财产安全。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]这辆车陪伴了我这么长时间，于情于理，我都不能把它拱手让给不认识的家伙。
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[multiline(name="阿兰娜",delay=0.2)] 这本该是它...
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[multiline(name="阿兰娜")] ...对了，它走向新生的旅程！
[charslot(slot = "l", name = "avg_npc_1183_1#6$1", focus="l")]
[multiline(name="阿兰娜",delay=0.01,end=true)]它本该开向那座每日吞吐亿万矿石的钢铁萝卜城，在乘客们的注目礼下风光地驶入载具厂。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[multiline(name="阿兰娜",delay=0.01,end=true)]在那里，它会被改装成更新更酷的型号，比如装上盾构机模块，这样下次遇到天灾警报，它就能直接钻进地底躲避。
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[multiline(name="阿兰娜",delay=0.01,end=true)]哈，我替我的车感谢你！我们将要在钢铁萝卜城开启的新生活，总算是泡汤了！拜你所赐！
[charslot(slot = "r", name = "

... (全文41198字符)
```

### level_act16mini_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="46_g4_rmbtwild_d",screenadapt="coverall")]
[PlaySound(key="$d_avg_snowstormflp", volume=0.4, loop=true, channel="a")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="生活本身就是一种巨大的恐怖。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你不知道它会把你卷到什么地方。更糟糕的是，有时候甚至没有三十多个兄弟姐妹和一百多个别的亲戚吵吵闹闹地用他们的决定把你卷走——", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你只是被意外袭击了，呃，就像......我现在这样。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="没有智囊团，没有“绝对不会出错的大多数人的看法”，只有一个真的会用弩的劫匪，以及开车时使劲吹进来的沙子。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="——我认命了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[SoundVolume(volume=0.8, channel="a",fadetime=2)]
[charslot(slot = "m", name = "avg_npc_1184_1#1$1", duration = 1, isblock=true)]
[name="杰里"]那个，我......我觉得我们不能从大风滩经过。那一带几乎是天灾的领地，每年有七万辆运载车在经过大风滩时受损甚至彻底毁坏......
[charslot(slot = "m", name = "avg_npc_1184_1#6$1")]
[name="杰里"]不对，我们的车身本来就已经受损了......
[name="杰里"]那、那应该看看这个，除了天灾以外，可能进一步导致载具损坏的常见因素......
[name="杰里"]源石燃料泄漏、传动系统故障导致二次事故、靠近开采场而被炸药波及......所以我们要避开矿石开采场......
[charslot(slot = "m", name = "avg_npc_1184_1#3$1")]
[name="杰里"]呃，有人在听吗？
[dialog]
[charslot]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.6)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1183_1#1$1", duration=1.5, isblock=true)]
[name="阿兰娜"]对，小锅盖，从这里爬上去，就锯那根树枝，锯完再把水泵接到树顶上！
[dialog]
[charslot]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot = "m", name = "avg_4081_warmy_1#1$1", posfrom="0,-50", posto="0,60", duration=1.5, isblock=true)]
[SoundVolume(volume=1, channel="a",fadetime=1)]
[Delay(time=1)]
[PlaySound(key="$d_avg_woodenladder", volume=1)]
[charslot(slot = "m", name = "avg_4081_warmy_1#3$1", afrom=1, ato=1, posfrom="0,60", posto="80,50", duration=1.2, isblock=true)]
[charslot(slot = "m", posfrom="80,50", posto="0,60", duration=0.6, isblock=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_woodenladder", volume=1)]
[charslot(slot = "m", posfrom="0,60", posto="-80,50", duration=1.2, isblock=true)]
[charslot(slot = "m", posfrom="-80,50", posto="0,60", duration=0.6, isblock=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_ftrub", volume=1)]
[charslot(slot = "m", posfrom="0,60", posto="0,0", duration=1, isblock=true)]
[charslot(slot = "m", name = "avg_4081_warmy_1#3$1")]
[name="小锅盖"]电锯......沉沉的......
[name="小锅盖"]没关系......兰娜姐给的脚扣绑得很紧，只要想象自己像大树鼷兽一样，用脚扣牢牢地抓住树干，“咻”地一下跳上去......
[name="小锅盖"]......我一定能把事情做好的，能让大家开开心心的。
[dialog]
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", posfrom="0,0", posto="-100,0", duration=0.8,isblock=true)]
[PlaySound(key="$d_avg_armour", volume=1, loop=true, channel="a")]
[charslot(slot = "r", posfrom="-100,0", posto="-100,-5", duration=0.3,isblock=true)]
[charslot(slot = "r", posfrom="-100,-5", posto="-100,0", duration=0.2,isblock=true)]
[charslot(slot = "r", posfrom="-100,0", posto="-100,-5", duration=0.3,isblock=true)]
[charslot(slot = "r", posfrom="-100,-5", posto="-100,0", duration=0.2)]
[StopSound(channel="a", fadetime=1)]
[PlaySound(key="$d_avg_fastener")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", posfrom="-100,0", posto="-180,0", afrom=1, ato=0, duration=0.6,isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_4081_warmy_1#7$1")]
[name="小锅盖"]......咦？背上突然轻了？
[charslot(slot = "m", name = "avg_npc_1183_1#3$1")]
[name="阿兰娜"]......喂，劫车的，我可没叫你来干活！
[charslot(slot = "m", name = "avg_4117_ray_1#1$1",isCopy=true)]
[name="莱伊"]嗯，你没有让我做任何事情。不过，我有开采瓶树水的经验。
[charslot(slot = "m", name = "avg_npc_1183_1#1$1")]
[name="阿兰娜"]好吧，我承认你有点良心，但还是麻烦你把工具还给小锅盖。
[name="阿兰娜"]毕竟，比起你这个劫车的，我当然更信任我的老搭档。
[charslot(slot = "m", name = "avg_4081_warmy_1#4$1")]
[name="小锅盖"]嘿嘿......
[charslot(slot = "m", name = "avg_npc_1183_1#6$1")]
[name="阿兰娜"]再说，我们又不是真的要当什么瓶树水专用运货车。
[name="阿兰娜"]我们只是需要在进入移动平台之前伪装一下这辆车而已，别让人看出这是一辆偏离了航线的城际公共交通运载车。
[name="阿兰娜"]顺带再贴点装饰——在用修补铁皮钉上之前，可别让人看出来这辆车被打穿了好几个洞。
[charslot(slot = "m", name = "avg_npc_1183_1#1$1")]
[name="阿兰娜"]小锅盖，咱们串通好的口供，你再教劫车的说一遍。
[charslot(slot = "m", name = "avg_4081_warmy_1#4$1")]
[name="小锅盖"]好。
[charslot(slot = "m", name = "avg_4081_warmy_1#1$1")]
[name="小锅盖"]如果有人问，就说我们正在运输这棵瓶树，并且还要把树干里的水装桶送去工厂，车上的树枝装饰是生产队队长的爱好。
[charslot(slot = "m", name = "avg_npc_1183_1#1$1")]
[name="阿兰娜"]没错。我编的这套说法肯定没问题。
[charslot(slot = "m", name = "avg_npc_1183_1#8$1")]
[name="阿兰娜"]哈哈，真没想到，瓶树这玩意不仅在我们躲天灾长时间偏离方向的时候能救命。
[name="阿兰娜"]我真的爱死那些会在偏远荒野上种瓶树的运载车司机了。
[name="阿兰娜"]当然，包括我自己。
[charslot(slot = "m", name = "avg_npc_1183_1#1$1")]
[name="阿兰娜"]好了，我去驾驶室了！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1, isblock=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1184_1#3$1")]
[name="杰里"]......呃，请问有人在听吗？那个，我还想提醒一下......
[name="杰里"]......每年有三十万人在运载工具上遭遇不同原因导致的骨折，其中从运载车搬运的瓶树上掉下来骨折的有一万五千人。
[charslot(slot = "m", name = "avg_4081_warmy_1#7$1")]
[name="小锅盖"]欸......
[charslot(slot = "m", focus="n")]
[name="阿兰娜"]别听他的。我会慢慢启动水泵，保证你不会被震到从树上掉下来。
[charslot(slot = "m", name = "avg_npc_1184_1#1$1")]
[name="杰里"]但事故总是突如其来的......
[charslot(slot = "m", focus="n")]
[name="阿兰娜"]好，我启动了！小锅盖，抓稳！
[dialog]
[CameraShake(duration=3, xstrength=6, ystrength=6, vibrato=90, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_elevator", volume=1, loop=true, channel="a")]
[Delay(time=1)]
[StopSound(channel="a", fadetime=2)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1184_1#1$1")]
[name="杰里"]每年——每年还有一千多人！因为突发的大风天气——导致树干歪斜——而丧——
[charslot(slot = "m", name = "avg_4081_warmy_1#1$1")]
[name="小锅盖"]我成功了欸，兰娜姐！
[charslot(slot = "m", n

... (全文47428字符)
```

### level_act16mini_st04

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot]
[Subtitle(text="通常来说，我们并不能在事情发生的当下，立即得到令人满意的答案。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="就像老妈和吉姆阿姨在深更半夜爆发的，那场足以把所有邻居从睡梦中惊醒的激烈争吵——", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="而她们争论的内容还是“工厂应该如何调整磨谷机和碾米机的开动时间，才能不打扰工人们的休息”。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="就像“围栏事件”中帮助农民和工人们建立共同阵线的那些雷姆必拓年轻商人——", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="虽然他们为摆脱伯爵和维多利亚商会出了力，但到头来，有几人是为了自己的产业利益？又有几人是真心为了雷姆必拓人的未来？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="还有，就像在那时的旅行中，博士和阿米娅......", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="或许有些问题，总会有个答案。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.11, fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.11, fadetime=0.1)]
[Background(image="46_g4_rmbtwild_d", xScale=1.1,yScale=1.1, screenadapt="coverall")]
[PlaySound(key="$d_avg_snowstormflp", volume=0.5, loop=true, channel="a")]
[PlaySound(key="$d_avg_drivestop", volume=1)]
[delay(time=1)]
[CameraShake(duration=-1,xstrength=0.5,ystrength=0.5,vibrato=10,randomness=10, fadeout=false,block=false)]
[PlaySound(key="$d_avg_truckengine", volume=0.15, loop=true, channel="b")]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[charslot(slot = "l", name = "char_002_amiya_1#1", duration=1)]
[charslot(slot = "r", name = "avg_230_savage_1#1$1", duration=1, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_230_savage_1#4$1", focus="r")]
[name="暴行"]啊？没想好要去哪里？
[charslot(slot = "r", name = "avg_230_savage_1#10$1", focus="r")]
[name="暴行"]回到移动平台寻找童年痕迹不是这次旅行的第一站吗？不是应该还有第二站，第三站......
[name="暴行"]我加了满满当当一整箱燃料，甚至还准备了露营用的炊具和帐篷......
[name="暴行"]而且，雷姆必拓矿业冠军杯正在打小组赛......往南也许能撞上环大哈默矿坑驮兽越野拉力赛......
[charslot(slot = "r", name = "avg_230_savage_1#8$1", focus="r")]
[name="暴行"]或者去试试雷姆必拓特色食物？我这几年可记下了非常多很有风味的餐厅，尤其是那些开在挖空了的矿道里的。
[name="暴行"]总之，凯尔希说了，接下来这段时间里，你们都没有任务。去维多利亚的事，之后再想！
[charslot(slot = "l", name = "char_002_amiya_1#6", focus="l")]
[name="阿米娅"]别、别激动，暴行姐姐......我并不是因为担忧之后的事情而没有旅行的心情！
[name="阿米娅"]我的意思是，或许我更希望像过去一样，只是毫无目的地四处漫游。
[charslot(slot = "l", name = "char_002_amiya_1#3", focus="l")]
[name="阿米娅"]......唔，这么说或许不准确。我想那个时候的博士，应该是知道自己想去哪里的。
[dialog]
[charslot(slot = "r", focus="n")]
[Decision(options="......我？", values="1")]
[Predicate(references="1")]
[charslot(slot = "l", name = "char_002_amiya_1#3", focus="l")]
[name="阿米娅"]因为在我的记忆里，每天似乎都在发生不一样的事情，看到不一样的景观。
[name="阿米娅"]如果真的只是在雷姆必拓的荒野上随便走，大部分时间应该只会看到相似的沙土、源石晶簇和矿坑吧。
[charslot(slot = "r", name = "avg_230_savage_1#9$1", focus="r")]
[name="暴行"]那个嘛，我觉得也有可能是你们运气不好，一路给自己招惹了太多麻烦......
[charslot(slot = "r", name = "avg_230_savage_1#8$1", focus="r")]
[name="暴行"]还好，现在阿米娅已经很有能力了，我也不是那个空有一腔热血的愣头青了，就算再遇上什么麻烦，也不会太难解决......
[dialog]
[charslot(slot = "r", name = "avg_230_savage_1#3$1")]
[charslot(slot = "l", name = "char_002_amiya_1#5")]
[stopmusic(fadetime=1)]
[PlaySound(key="$drift", volume=1)]
[StopSound(channel="b", fadetime=1)]
[BackgroundTween(xScaleFrom=1.1,xScaleTo=1.2, yScaleFrom=1.1, yScaleTo=1.2, duration=0.5, block=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=1.05, duration = 0.5)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=1.05, duration = 0.5, isblock=true)]
[delay(time=0.5)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_punchsp1", volume=1)]
[BackgroundTween(xScaleFrom=1.2,xScaleTo=1.05, yScaleFrom=1.2, yScaleTo=1.05, duration=0.2, block=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=0.98, duration = 0.2)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=0.98, duration = 0.2, isblock=true)]
[BackgroundTween(xScaleFrom=1.05,xScaleTo=1.1, yScaleFrom=1.05, yScaleTo=1.1, duration=0.2, block=false)]
[charslot(slot = "r", action="zoom", poszoom = "0.5,0.5", scale=1, duration = 0.2)]
[charslot(slot = "l", action="zoom", poszoom = "0.5,0.5", scale=1, duration = 0.2, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", focus="n")]
[Decision(options="哎哟——;......", values="1;2")]
[Predicate(references="1")]
[charslot(slot = "l", name = "char_002_amiya_1#5", focus="n")]
[charslot(slot = "r", name = "avg_230_savage_1#5$1", focus="r")]
[name="暴行"]对、对不起博士！
[charslot(slot = "l", name = "char_002_amiya_1#5", focus="l")]
[name="阿米娅"]博士！你还好吧？撞到头了？
[dialog]
[Predicate(references="2")]
[charslot(slot = "l", name = "char_002_amiya_1#5", focus="n")]
[charslot(slot = "r", name = "avg_230_savage_1#1$1", focus="r")]
[name="暴行"]刚刚那是什么声音？
[charslot(slot = "l", name = "char_002_amiya_1#4", focus="l")]
[name="阿米娅"]博士......撞到头很痛的话，请不要强撑......
[dialog]
[Predicate(references="1;2")]
[charslot(slot = "r", focus="n")]
[Decision(options="没事......我的头还在。", values="1")]
[Predicate(references="1")]
[charslot(slot = "l", name = "char_002_amiya_1#4", focus="l")]
[name="阿米娅"]暴行姐姐......发生什么事情了？怎么突然急刹车？
[charslot(slot = "r", name = "avg_230_savage_1#6$1", focus="r")]
[name="暴行"]你们看前边——
[name="暴行"]是不是有一辆正在冒烟的运载车？
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)] 
[curtain]
[charslot]
[Background(image="46_g2_rmbttransporter",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_npc_1183_1#3$1")]
[name="阿兰娜"]劫车的，去接瓶树水，越多越好！
[charslot(slot = "m", focus="n")]
[name="莱伊"]好。
[charslot(slot = "m", name = "avg_npc_1183_1#6$1")]
[name="阿兰娜"]毛毯拿一条过来，再帮我扶她一把。
[char

... (全文42284字符)
```

### level_act16mini_st05

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Background(image="bg_windows",screenadapt="coverall")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="棚屋的窗帘比窗户短了一截。在炉子烧起来、机器转起来、城市醒过来之前，清晨的第一束天光就会把人刺醒。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不过，我一直没有把窗帘补上。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="迷迷糊糊，还没清醒过来的时候，这束光会让我短暂地看到一个幻觉，一个巨大的影子。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="晃晃脑袋，想起自己是谁的时候，这束光会提醒我，现在就该收拾东西出门。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="四处做散工过活的人，得赶在开工之前就早早来到矿场，才能接到些像样的活计。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[PlaySound(key="$d_avg_pullcurtain", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "m", name = "avg_4117_ray_1#1$1", duration=1, isblock=true)]
[name="莱伊"]走吧，沙地兽。
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1188_1#8$1", duration=0.5, isblock=true)]
[PlaySound(key="$d_avg_pawfootstep_1", volume=1)]
[charslot(slot = "m", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=1.5, isblock=true)]
[charslot]
[charslot(slot = "m", name = "avg_4117_ray_1#4$1")]
[name="莱伊"]啊，不是那边。你忘了吗？那边的矿场已经雇到专业的安全员了。
[charslot(slot = "m", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]......今天我们去西北边的矿场碰碰运气。
[dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)] 
[charslot]
[Background(image="46_g3_rmbttown",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[PlaySound(key="$d_avg_pawfootstep_2", volume=1)]
[charslot(slot = "m", name = "avg_npc_1188_1#1$1", duration=1, isblock=true)]
[name="沙地兽"]（缓慢地舒展背扇）
[charslot(slot = "m", name = "avg_npc_1185_1#1$1")]
[name="矿队队长"]嚯，这么大一只，应该已经成年了吧？
[charslot(slot = "m", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]嗯。
[charslot(slot = "m", name = "avg_npc_1185_1#1$1")]
[name="矿队队长"]探井用的沙地兽能长到这么大的可不多见，你运气还真不赖。
[charslot(slot = "m", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]也许吧。
[charslot(slot = "m", name = "avg_npc_1185_1#1$1")]
[name="矿队队长"]这种时候开工是需要点运气。今天这井你要是能下，按规矩我得付你两倍的钱。当然，油水你自己捞。
[charslot(slot = "m", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]好，带路吧。
[charslot(slot = "m", name = "avg_npc_1185_1#1$1")]
[name="矿队队长"]哎，等等，你还真就什么都不问？
[name="矿队队长"]看你也不像刚出来干这行的愣头青，听到双倍钱怎么连点反应都没有？
[name="矿队队长"]西边几百公里的地方前些天遭了灾，大地震，连带着我们矿井里的源石结晶也开始增生，现在底下一片糟。这些情况你都清楚？
[charslot(slot = "m", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]嗯，我现在清楚了。
[charslot(slot = "m", name = "avg_npc_1185_1#1$1")]
[name="矿队队长"]看你这轻描淡写的模样，还真是心大。
[name="矿队队长"]还是说你其实是专业的，见惯了这种场面？
[charslot(slot = "m", name = "avg_4117_ray_1#9$1")]
[name="莱伊"]专业？......我应该不是。只是这些年一直在做探井的工作。
[charslot(slot = "m", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]我会注意人身安全的，如果我死了，沙地兽会没人养。
[charslot(slot = "m", name = "avg_npc_1185_1#1$1")]
[name="矿队队长"]嗤，也是，专业的安全员怎么可能到处给人做散工。
[name="矿队队长"]得了，反正该告诉你的我都告诉你了。
[name="矿队队长"]缺指头奥利！别喝了，赶紧过来做准备。安全绳给她系好就可以放下去了。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="46_g6_rmbtmine",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_energywell", volume=0, loop=true, channel="a")]
[SoundVolume(volume=0.2, channel="a",fadetime=2)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="我不知道其他人说起矿井时会联想到什么。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="敲击的脆响，湿气的阴臭，空气的燥热，汗水的苦涩......也许会有这些。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我是探井人，在每天矿队开工之前，我需要独自下井探察情况。这个时候，矿井下只有黑暗。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="罐笼在下降，头顶的声音逐渐变得模糊，所有东西的轮廓都在消退。然后，我的感官变得敏锐。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="我不想待在很黑的地方，不过，黑暗的触感是我最熟悉的东西。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[PlaySound(key="$d_avg_openftstpwalk", volume=1)]
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", duration=1, isblock=true)]
[playsound(key="$d_gen_transmissionget", volume=1)]
[CharacterCutin(widgetID="1", name="avg_npc_1185_1#1$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[charslot(slot = "r", focus="n")]
[name="矿队队长"]探井人，有什么状况吗？
[charslot(slot = "r", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]沙地兽的背扇打开了，但血管的颜色没有明显变化。是正常反应，暂时安全。
[name="莱伊"]平面图更新过吗？
[charslot(slot = "r", focus="n")]
[name="矿队队长"]新增的巷道还没来得及标，但重要硐室都没变。
[charslot(slot = "r", name = "avg_4117_ray_1#1$1")]
[name="莱伊"]好。
[dialog]
[playsound(key="$e_atk_vibe_n", volume=0.4)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_4117_ray_1#5$1")]
[name="莱伊"]——
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "r", posfrom="0,0", posto="200,0", afrom=1, ato=0, duration=0.5, isblock=true)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$d_avg_arrowshot", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=0.5)]
[name="矿队队长"]怎么回事？
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_4117_ray_1#1$1", posfrom="200,0", posto="0,0", duration=1, isblock=true)]
[name="莱伊"]高能源石虫，已经处理掉了。
[name="莱伊"]不过，这不是好迹象。
[charslot(slot = "r", focus="n")]
[name="矿队队长"]我们矿井原来很少见这种满地乱炸的鬼东西。底下的情况可能比我们想的还要糟糕。
[name="矿队队长"]我得提醒你，就你现在这个深度，再往前走一点就没有信号了。
[charslot(slot = "r", name = "avg_4117_ray_1#1$1")]
[name=

... (全文37104字符)
```

### level_act16mini_st06

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[focusout(type="bg", id="bg_corridor_2", from=0, to=1, duration=1, block=false)]
[Background(image="bg_corridor_2",screenadapt="coverall")]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="博士，我已经不怕了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="她们问了我好多问题。我们走了这么久的路，去了哪些地方，玩得开不开心......我都讲给她们听了。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="不过，有的问题我也答不上来。", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="博士在找什么东西吗？为什么她们悄悄说，博士想看到的，都是不可能再看到的？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="......为什么博士会救起我，和我一起旅行呢？", x=300, y=350, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[focusout(type="bg", id="46_g1_transporter", from=0, to=0, duration=0, block=false)]
[Background(image="46_g1_transporter",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$radio")]
[name="广播喇叭"]......竖起长耳朵和短耳朵的司机朋友们，以上是六小时内的发车指导消息。
[name="广播喇叭"]看好天灾预报，注意行车安全，不追野生动物，早早收车回家......
[dialog]
[charslot(slot = "m", name = "avg_npc_1183_1#8$1", duration=1, isblock=true)]
[name="阿兰娜"]看起来还不错嘛，老家伙。
[name="阿兰娜"]你该庆幸你的最后一程是在我手里度过的，换了别人，可能就没这个本事把你修补好了。
[name="阿兰娜"]你就得带着反装甲炮轰出来的洞，在荒野里破破烂烂地躺着，等工程队过来进行切割，把有用的模块拖回厂里重新组装。
[charslot(slot = "m", name = "avg_npc_1183_1#1$1")]
[name="阿兰娜"]而我呢，就会因为该交的车没交上，把事情搞砸了，被人笑话一辈子。
[dialog]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1183_1#7$1")]
[name="阿兰娜"]......我本来也该被人笑话一辈子。要是她被人打死的时候，有人发现我就躲在这辆车底下的话......
[name="阿兰娜"]啧，那种事不会再有了。
[charslot(slot = "m", name = "avg_npc_1183_1#1$1")]
[name="阿兰娜"]好了，现在就剩下一个问题了，钢铁萝卜城这边熟人有点少，我得找个人教我填事故报告书......
[dialog]
[charslot]
[PlaySound(key="$d_avg_transpthrn", volume=1)]
[delay(time=1.5)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="r")]
[StopSound(channel="r", fadetime=1)]
[charslot(slot = "l", name = "avg_npc_1183_1#9$1", duration=1, isblock=true)]
[name="阿兰娜"]哎，别按铃了别按铃了，这辆车不发车，你走错了——
[dialog]
[PlaySound(key="$d_avg_steamburst", volume=1)]
[PlaySound(key="$d_avg_gateopen", volume=1, loop=true, channel="g")]
[StopSound(channel="g", fadetime=2.5)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_1183_1#4$1")]
[name="阿兰娜"]——胆小鬼？
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1184_1#1$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[charslot(slot = "r", name = "avg_npc_1184_1#3$1", focus="r")]
[name="杰里"]呃......嘿嘿。看来我没认错车。
[name="杰里"]虽然没了那些花里胡哨的装饰，还有那种车厢里像打过一仗的感觉，反而有点陌生......
[name="杰里"]总之，看到这辆车没事就好！我觉得，这应该也说明莱伊小姐和温米妹妹没出事吧......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]哈，算是吧。
[charslot(slot = "r", name = "avg_npc_1184_1#1$1", focus="r")]
[name="杰里"]那、那个，那我打听一下......
[name="杰里"]莱伊小姐最后找到她说的那个东西了吗？
[charslot(slot = "l", name = "avg_npc_1183_1#2$1", focus="l")]
[name="阿兰娜"]当然没有。
[charslot(slot = "r", name = "avg_npc_1184_1#4$1", focus="r")]
[name="杰里"]真对不起！我不是故意要提起你们的伤心事的！
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]没事，要伤心也轮不到我伤心。
[name="阿兰娜"]不过，劫车的也确实不怎么伤心就是了。
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]说起来真是见了鬼......她半路上莫名其妙失踪了，又莫名其妙出现在了我们停车避难、等待小型天灾过去的地方。
[name="阿兰娜"]就像天灾里被狂风卷走几千公里，晕头转向的傻羽兽。
[charslot(slot = "r", name = "avg_npc_1184_1#6$1", focus="r")]
[name="杰里"]呃，那她......不会把自己要找的东西忘了吧？我知道有人跟别人比赛原地转圈，结果把自己转晕，摔坏了脑袋......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]比一般的摔坏脑袋还吓人。她说自己已经见过巨兽了。
[charslot(slot = "r", name = "avg_npc_1184_1#6$1", focus="r")]
[name="杰里"]呃......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]还说见到的不是自己要找的那只。
[charslot(slot = "r", name = "avg_npc_1184_1#2$1", focus="r")]
[name="杰里"]啊？
[charslot(slot = "l", name = "avg_npc_1183_1#6$1", focus="l")]
[name="阿兰娜"]最后还说，巨兽已经告诉她了，她要找的东西真的不存在。
[charslot(slot = "r", name = "avg_npc_1184_1#1$1", focus="r")]
[name="杰里"]我......我真替她伤心。
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]是吗？我一般管这个叫“想通了”。
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]不过，后来我们确实继续往咧嘴谷开了。好不容易跑了那么远，怎么可能凭劫车的一句话我就回头？
[name="阿兰娜"]......
[charslot(slot = "r", name = "avg_npc_1184_1#3$1", focus="r")]
[name="杰里"]......然后呢？你们看到什么啦？
[charslot(slot = "l", name = "avg_npc_1183_1#8$1", focus="l")]
[name="阿兰娜"]......特别酷！可惜那里太危险，你这个胆小鬼一辈子都别想看到啦，哈哈！
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]真的，劝你千万不要去。要不是我技术高超，应急能力又强，这辆车根本不可能从那里开出来。
[name="阿兰娜"]往这里来的路上，我们开一两个小时就得停下来休息，等这老家伙散热......工会说它该“规范化”了，确实有点道理。
[dialog]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1183_1#2$1", focus="l")]
[name="阿兰娜"]唉，二十年了。
[charslot(slot = "r", name = "avg_npc_1184_1#6$1", focus="r")]
[name="杰里"]你......开车二十年了？真看不出来......
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]多谢你对我技术的“认可”。
[name="阿兰娜"]不过我说的只是......认识这辆车二十年了。
[charslot(slot = "l", name = "avg_npc_1183_1#6$1", focus="l")]
[name="阿兰娜"]对了，胆小鬼——我的婚礼请柬呢？
[charslot(slot = "r", name = "avg_npc_1184_1#4$1", focus="r")]
[name="杰里"]欸？呃......
[charslot(slot = "r", name = "avg_npc_1184_1#6$1", focus="r")]
[name="杰里"]那个，你们可能已经错过婚礼了......
[name="杰里"]......咳，其实我正在蜜月旅行。
[name="杰里"]......其实本来蜜月旅行已经结束了，就在十分钟之前。
[charslot(slot = "r", name = "avg_npc_1184_1#6$1", focus="r")]
[name="杰里"]本来钢铁萝卜城是我们的终点站，但是进入关口之后，我看到了你的运载车，突然就......想继续旅行一段时间。
[charslot(slot = "l", name = "avg_npc_1183_1#1$1", focus="l")]
[name="阿兰娜"]喔......你们开的是那辆刚停在不远处的小货车？我还以为是哪个冒失司机送货结果停错了层，没进物流通道呢。
[charslot(slot = "l", name = "avg_npc_1183_1#7$1", focus="l")]
[name="阿兰娜"]不过，真奇怪......
[charslot(slot = "r", name = "avg_npc_1184_1#3

... (全文26167字符)
```


## 统计

- 总字符数：239903
- 对话行数：1840


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
