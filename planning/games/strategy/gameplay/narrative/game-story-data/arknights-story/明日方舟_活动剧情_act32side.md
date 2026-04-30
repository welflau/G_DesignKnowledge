# 明日方舟 · 活动剧情 · act32side（24段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act32side」完整剧情脚本（24个文件，2956行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act32side
- 脚本文件数：24

### level_act32side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[charslot(slot="l",name="avg_npc_001",duration=1.5)]
[charslot(slot="r",name="avg_npc_1042_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]兄弟，仙人掌干给我来一包，要马可阿姨的。
[charslot(slot="l",name="avg_npc_001",focus="l")]
[name="社区小贩"]马可阿姨里面添加剂不够多，不如马可叔叔好吃！
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]嗐，总之给我来包仙人掌干，我现在饿得要死。
[charslot(slot="l",name="avg_npc_001",focus="l")]
[name="社区小贩"]看你这副死人相，一晚上没睡吧，又在熬夜洗相片？
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]灵感总是在深夜骤然降临，我也很苦恼。
[charslot(slot="l",name="avg_npc_001",focus="l")]
[name="社区小贩"]那我的相片你什么时候弄好？
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]啊......我想起来了，是你说要送人的那份？是那个搞金属乐的姑娘？
[charslot(slot="l",name="avg_npc_001",focus="l")]
[name="社区小贩"]呵呵，那姑娘上个月已经把我甩了......
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]可恶啊，深夜里记忆也总是会莫名消失。
[charslot(slot="l",name="avg_npc_001",focus="l")]
[name="社区小贩"]*粗口*这楼里那么多搞摄影的，我怎么就找上了你这么个拖延症。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1212_1#7$1",duration=1.5)]
[Delay(time=2.5)]
[charslot]
[charslot(slot="l",name="avg_npc_001",focus="l")]
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="l")]
[name="社区小贩"]哟，特克诺，回来了？那座艺术馆好不好玩？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1212_1#7$1",focus="m")]
[name="特克诺"]快滚蛋。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_001",focus="l")]
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="l")]
[name="社区小贩"]怎么，碰壁了？你昨天晚上不是还信誓旦旦地说要去那里涂点什么吗？
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]他那座“宫殿”里面长什么样啊？我听说里面有不少名家真迹，早知道和你一起去了。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1212_1#2$1",focus="m")]
[name="特克诺"]别提了，我轮廓刚画完，就有人追出来了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_001",focus="l")]
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="l")]
[name="社区小贩"]啧啧啧。
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]没事，这种事有一回就有无数回，总有一回他逃不掉，下一回你可以带上我。
[charslot(slot="l",name="avg_npc_001",focus="l")]
[name="社区小贩"]我也可以，嘿嘿。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1212_1#9$1",focus="m")]
[name="特克诺"]差不多够了啊，你们两个......老爹今天出门了吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_001",focus="r")]
[charslot(slot="r",name="avg_npc_1042_1#1$1",focus="r")]
[name="社区居民"]没，老爹今天心情很差，在他房间里一天都没出来。
[name="社区居民"]我猜，他或许正等你的“好消息”呢。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g11_deluxeroom_n",screenadapt="coverall")]
[charslot(slot="l",name="avg_4123_ela_1#1$1")]
[charslot(slot="r",name="avg_npc_1211_1#1$1")]
[Delay(time=2.5)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]所以，雷内尔先生，你不认识列维。
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]当然，我也得再确定一下，你也不认识我叔叔，是吧？高个子，戴眼镜，笑得很阴森。
[charslot(slot="l",name="avg_4123_ela_1#6$1",focus="l")]
[name="艾拉"]你再说下去，我就要怀疑你叔叔就是我们要找的人了，先生。
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]呃，我想这应该只是另外一个令人不快的巧合。
[Dialog]
[playsound(key="$d_avg_winglssice")]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1211_1#9$1",focus="r")]
[name="雷内尔"]既然误会解释清楚了，你们要一起来点吗？
[charslot(slot="l",name="avg_4123_ela_1#3$1",focus="l")]
[name="艾拉"]我想不用了，雷内尔先生，我们得走了。
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]双月，你为什么在颤抖？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4124_iana_1#7$1",focus="m")]
[name="双月"]如果我们没在做梦，没在经历幻觉......
[name="双月"]我们要么在时间上，要么在空间上......被某种不可知的力量“发射”了出去，落在了这里......
[name="双月"]也许是难以想象的时间维度上的地球，也许是一颗遥远的行星......
[charslot(slot="m",name="avg_4124_iana_1#8$1",focus="m")]
[name="双月"]我只是很激动，艾拉。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_1211_1#9$1",focus="l")]
[name="艾拉"]我能明白你，但摆在我们面前的不仅是全然陌生的世界，还有全然陌生的问题。
[name="艾拉"]所以......无论你现在有多么激动，都请冷静下来。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4124_iana_1#10$1",focus="m")]
[name="双月"]......抱歉。
[charslot(slot="m",name="avg_4125_rdoc_1#10$1",focus="m")]
[name="医生"]走吧，朋友们，但愿深夜来临前我们能在这里找到落脚的地方。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1211_1#9$1",focus="r")]
[name="雷内尔"]气氛倒也不必那么惆怅吧，诸位救了我的性命，作为回报，一些帮助我还是能够提供的。
[name="雷内尔"]至少，一个住的地方？
[charslot(slot="l",name="avg_4123_ela_1#7$1",focus="l")]
[name="艾拉"]......
[charslot(slot="r",name="avg_npc_1211_1#5$1",focus="r")]
[name="雷内尔"]不会吧，你们难道真的打算今晚睡在路边的纸板上吗？
[Dialog]
[PlaySound(key="$d_gen_thunders_amb", volume=0.4)]
[Delay(time=1)]
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_1211_1#5$1",focus="l")]
[name="艾拉"]......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4124_iana_1#1$1",focus="m")]
[name="双月"]要下雨了。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4123_ela_1#1$1",focus="m")]
[name="艾拉"]......我们不会白白接受你的帮助，雷内尔先生。
[name="艾拉"]在这期间，我们可以负责你的安保，至少保证不会有人如今天一般，带着武器冲进你的房间。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1213_1#6$1",duration=1.5)]
[Delay(time=2)]
[name="米沃什"]呵，或者带着武器从天花板上掉下来——
[dialog]
[character]
[charslot(slot="l",name="avg_npc_1213_1#6$1",focus="r")]
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]好了，米沃什，我觉得没有问题。
[charslot(slot="l",name="avg_npc_1213_1#10$1",focus="l")]
[name="米沃什"]（小声）可我们对他们的身份一无所知，雷内尔。
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]（小声）那这不就是我们了解的机会

... (全文16473字符)
```

### level_act32side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$dooropenquite")]
[charslot(slot="m",name="avg_4123_ela_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1211_1#1$1")]
[name="雷内尔"]哦，艾拉小姐，你的朋友们没一起来吗？
[charslot(slot="m",name="avg_4123_ela_1#7$1")]
[name="艾拉"]你雇的保安对导火索很“感兴趣”，在底下缠着他问东问西。正好你也想派个人训练他们，我就把他留在那里了。
[charslot(slot="m",name="avg_npc_1211_1#1$1")]
[name="雷内尔"]我记得你们昨天有四个人呢。
[charslot(slot="m",name="avg_4123_ela_1#1$1")]
[name="艾拉"]之前我们应该说好了，一半的人手保护你，其他人会继续进行我们在这里的搜寻任务，只在需要人手的时候加入进来。
[name="艾拉"]今天你又不出席什么公众活动。
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[name="雷内尔"]别绷着脸嘛，不过是好奇问两句。事实上，跟着我的人越少我反而越轻松。
[charslot(slot="m",name="avg_4123_ela_1#3$1")]
[name="艾拉"]我看到了，你今天的行程里有两场会议，保密度极高。
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[name="雷内尔"]会议？什么会议？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g20_skyblue_L1",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4123_ela_1#4$1")]
[name="艾拉"]蹦极？这就是你的“会议”？
[charslot(slot="m",name="avg_npc_1211_1#1$1")]
[name="雷内尔"]当然，之前米沃什根本不允许我来玩，他今天在外面办事，我当然要抓住这个机会来试试。
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]......作为保镖，我建议你放弃这个计划。
[charslot(slot="m",name="avg_npc_1211_1#10$1")]
[name="雷内尔"]那作为雇主，我建议你少提些建议。
[charslot(slot="m",name="avg_npc_1211_1#1$1")]
[name="雷内尔"]我的安全带调整好了吗？
[charslot(slot="m",name="avg_npc_1211_1#1$1",focus="none")]
[name="工作人员"]没问题，先生，您可以往下跳了。
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[name="雷内尔"]那......回见。
[Dialog]
[playsound(key="$d_avg_clothmovementsp")]
[charslot(slot="m",posfrom="0,0",posto="-100,-30",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=1)]
[Delay(time=2.5)]
[name="雷内尔"]哇哦————！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]呃......这家伙真是个混账。
[charslot(slot="m",name="avg_4123_ela_1#6$1",focus="none")]
[name="工作人员"]女士，您不必紧张，我们使用的都是专业设备，不会有什么危险。
[charslot(slot="m",name="avg_4123_ela_1#3$1")]
[name="艾拉"]如果没有危险，你就不会让他去填那份免责声明了。
[charslot(slot="m",name="avg_4123_ela_1#3$1",focus="none")]
[name="工作人员"]那您还跳吗？安全装置我已经为您绑好了。
[Dialog]
[charslot(slot="m",name="avg_4123_ela_1#1$1")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4123_ela_1#8$1")]
[name="艾拉"]哈，为什么不呢，反正是我老板掏钱。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
背对跳台，艾拉站到边缘处，脚跟的悬空让她产生了丝丝麻意，顺着被绑束的地方蔓延上背脊。
对着工作人员，她轻轻扯出一个笑容，随即向后倒去，享受被失重感捏紧心脏的快意。
[Dialog]
[Blocker(a=1, fadetime=1, block=true)]
[charslot]
[playsound(key="$d_avg_wind",loop=true,channel="1")]
[Background]
[Image(image="20_I01",x=0,y=0)]
[ImageTween(xScaleFrom=1.2, yScaleFrom=1.2, xScaleTo=1.5, yScaleTo=1.5, duration=60, block=false)]
[Blocker(a=0, fadetime=2, block=true)]
[delay(time=1)]
在不停降落的过程中，艾拉等待着绳索延展到极致，然后回弹，将她向上牵拉。
[Dialog]
[Delay(time=2.5)]
[stopmusic(fadetime=1)]
[playsound(key="$d_avg_jump_water",volume=0.3)]
[Delay(time= 1.5)]
但在耳旁呼啸的风声里，她先听到了水花绽开的声音。
[name="工作人员"]*粗口*，那个沃尔珀居然自己解开了自己的安全扣？！
[name="艾拉"]Gówno！
[Dialog]
[stopsound(channel="1",fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_jump_water")]
[charslot]
[image]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Delay(time=3.5)]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="广告"]海滨风光无限，莫让阳光灼伤脸颊，“大帽老哥”防晒霜，让你的肌肤远离紫外线的伤害。现在订购还可获赠一套尾巴护理油......
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_4124_iana_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#1$1",focus="r")]
[name="医生"]梅捷，你在看什么东西？
[charslot(slot="l",name="avg_4124_iana_1#10$1",focus="l")]
[name="双月"]那边的......呃，猫耳女郎，在向路人派发这些东西，我就顺手拿了一张。
[charslot(slot="r",name="avg_4125_rdoc_1#9$1",focus="r")]
[name="医生"]确实，这地方紫外线强度的确比较高。
[charslot(slot="l",name="avg_4124_iana_1#1$1",focus="l")]
[name="双月"]不，我是在看这个。
[charslot(slot="r",name="avg_4125_rdoc_1#13$1",focus="r")]
[name="医生"]磨角石？打错了吧，是不是角质——
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_496_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_499_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_496_1#1$1",focus="l")]
[name="兴奋的莱塔尼亚旅客"]想不到战事频发的玻利瓦尔竟然藏了这么一个度假胜地，这次出差我原本都不想来的。
[charslot(slot="r",name="avg_npc_499_1#1$1",focus="r")]
[name="高兴的莱塔尼亚旅客"]是啊，这几天过得很开心，就是角在盐水里泡久了之后变得很粗糙，一会儿回旅馆得好好打磨一下。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_4124_iana_1#10$1")]
[charslot(slot="r",name="avg_4125_rdoc_1#13$1")]
[Delay(time=1.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#13$1",focus="r")]
[name="医生"]......
[name="医生"]传单上还有沃尔珀、鲁珀和菲林专用的毛发柔顺剂。
[charslot(slot="l",name="avg_4124_iana_1#10$1",focus="l")]
[name="双月"]十升大包装？耳朵和尾巴用得到这么多吗？
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_601_1#1$1",afrom=0,ato=1,duration=1)]
[charslot(slot="l",posfrom="-100,0",posto="100,0",duration=1.5)]
[charslot(slot="r",name="avg_npc_1000_1#1$1",afrom=0,ato=1,duration=1)]
[charslot(slot="r",posfrom="100,0",posto="-100,0",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_1000_1#1$1",focus="r")]
[name="鬼祟的叙拉古游客"]现在到了一批好货，明天我们在沙滩浴场见面时细谈。
[charslot(slot="l",name="avg_npc_601_1#1$1",focus="l")]
[name="可疑的叙拉古游客"]哼，希望它们对得起我出的价。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",posfrom="100,0",posto="-100,0",duration=1.5)]
[charslot(slot="l",afrom=1,ato=0,duration=1)]
[charslot(slot

... (全文25309字符)
```

### level_act32side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_1271_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="带队的军官"]报、报告上尉！
[charslot(slot="m",name="avg_npc_1210_1#1$1",focus="m")]
[name="马特奥"]有什么话直接说，不要在那里叽叽歪歪。
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]您让我去探听的事，有些眉目了。
[name="带队的军官"]赌场里有消息说，近来有批矿石病抑制剂正要送进那片社区。社区里面的感染者众多，如果我们能拦下来，说不定可以......
[charslot(slot="m",name="avg_npc_1210_1#10$1",focus="m")]
[name="马特奥"]送药的是谁？
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]是家叫罗德岛的制药企业，在多索雷斯名声不错，和坎黛拉女士也有点交情......听来头似乎有些不好惹？
[charslot(slot="m",name="avg_npc_1210_1#8$1",focus="m")]
[name="马特奥"]不好惹......让我想想......
[charslot(slot="m",name="avg_npc_1210_1#1$1",focus="m")]
[name="马特奥"]对了，前些天出现在雷内尔办公室里的几个人是什么底细，能查出来吗？
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]抱歉，上尉，我们尽力了，但还是没查到......
[charslot(slot="m",name="avg_npc_1210_1#10$1",focus="m")]
[name="马特奥"]我们的老对头呢？他们背后的人呢？
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]那边也没消息。
[charslot(slot="m",name="avg_npc_1210_1#5$1",focus="m")]
[name="马特奥"]难道你想告诉我这几个人是从天上掉下来的？
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]......也许有人根本不想让我们查出他们的底细！
[charslot(slot="m",name="avg_npc_1210_1#8$1",focus="m")]
[name="马特奥"]那这个人到底是谁？
[charslot(slot="m",name="avg_npc_1210_1#10$1",focus="m")]
[name="马特奥"]......
[charslot(slot="m",name="avg_npc_1210_1#1$1",focus="m")]
[name="马特奥"]哦，对，还有这一层......我怎么没想到呢？
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]您想到什么了？
[charslot(slot="m",name="avg_npc_1210_1#1$1",focus="m")]
[name="马特奥"]如果是联合政府自己的人呢？毕竟我在多索雷斯的位子是个肥差，想取而代之的人肯定不少。
[name="马特奥"]就算这个人一直跟在我身边也没什么奇怪的，你说呢？
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]不是，您......您千万别误会！绝对不是您想的那样！我从头到尾只忠于您一个人！真的！
[charslot(slot="m",name="avg_npc_1210_1#8$1",focus="m")]
[name="马特奥"]呵，是啊，就你？得了吧。
[charslot(slot="m",name="avg_npc_1271_1#1$1",focus="m")]
[name="带队的军官"]您说得对，您说得太对了！
[charslot(slot="m",name="avg_npc_1210_1#8$1",focus="m")]
[name="马特奥"]屁股后面的麻烦是顾不上了，还是先想想眼前的事情吧......就没有什么办法能一举两得吗？
[charslot(slot="m",name="avg_npc_1210_1#10$1",focus="m")]
[name="马特奥"]既能好好敲打敲打社区里的帮派，又能给那几个人使些绊子......
[charslot(slot="m",name="avg_npc_1210_1#1$1",focus="m")]
[name="马特奥"]......我问你，那天他们用的战术，你记得多少？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_avg_driveincar",channel="1",loop=true)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.11, fadetime=1.5)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.11, fadetime=1.5)]
[Delay(time=1.5)]
[charslot(slot="l",name="avg_486_espumo_1#1",duration=1.5)]
[charslot(slot="r",name="avg_282_catap_1#10$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_282_catap_1#10$1",focus="r")]
[name="空爆"]我来之前可听说在关口得排好长时间的队。
[charslot(slot="l",name="avg_486_espumo_1#5",focus="l")]
[name="龙舌兰"]嗐，关口负责人是我的朋友，所以行了个方便。这辆车也是他借我的。
[charslot(slot="r",name="avg_282_catap_1#1$1",focus="r")]
[name="空爆"]想不到你在这里居然这么吃得开。
[name="空爆"]赶紧把药送去目标地点吧，等任务完成，我可得找片沙滩好好放松休息下。
[charslot(slot="l",name="avg_486_espumo_1#1",focus="l")]
[name="龙舌兰"]倒也不用那么着急，我们此行的任务地点是个非常有意思的社区，你说不定会很喜欢。
[charslot(slot="r",name="avg_282_catap_1#5$1",focus="r")]
[name="空爆"]啊，怎么说？
[charslot(slot="l",name="avg_486_espumo_1#6",focus="l")]
[name="龙舌兰"]他们中有非常多的人都从事着特殊的精神生产活动，通过独特的语言与手段展示自己对生活，以及周遭一切的感悟。
[charslot(slot="r",name="avg_282_catap_1#8$1",focus="r")]
[name="空爆"]老兄，我感觉有点混乱......有没有通俗点的说法。
[charslot(slot="l",name="avg_486_espumo_1#1",focus="l")]
[name="龙舌兰"]那里有很多搞艺术的人。
[Dialog]
[stopmusic(fadetime=1.5)]
[stopsound(channel="1",fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[curtain]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1271_1#1$1",bstart=0.2,bend=0.9,duration=1.5)]
[Delay(time=2)]
[playsound(key="$d_gen_transmissionget")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1271_1#1$1",bstart=0.2,bend=0.9,focus="m")]
[name="带队的军官"]报告，准备工作都做好了。
[name="带队的军官"]上尉，您就放心吧，衣服也换了，那几个家伙动手时的口令也都让大家记住了。
[name="带队的军官"]模仿他们的说话口音和战术动作可能有点难，但我们这有个从黑钢离职的家伙，我们让他打头阵。
[name="带队的军官"]他还有几把铳，我让弟兄们拿着。我们还有一些源石爆炸物和发射器，也用得上。
[name="带队的军官"]嗯，嗯，药品优先，尽量挑没人的地方动手，还有留活口，我懂。
[name="带队的军官"]上尉，您放一百个心，都包在我身上了！
[Dialog]
[playsound(key="$transmission")]
[Delay(time=1.5)]
[playsound(key="$rungeneral")]
[charslot(slot="m",bstart=0.2,bend=0.9,posfrom="0,0",posto="-200,0",duration=1)]
[charslot(slot="r",name="avg_npc_1272_1#1$1",bstart=0.2,bend=0.9,posfrom="200,0",posto="0,0",duration=1.5)]
[charslot(slot="r",afrom=0,ato=1,duration=1)]
[Delay(time=2.5)]
[charslot(slot="r",focus="r")]
[name="持铳的军人"]头儿，他们的车还有一个路口就到这儿了！
[charslot(slot="m",focus="m")]
[name="带队的军官"]弟兄们，动起来！
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_driveincar",channel="1",loop=true)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.11, fadetime=1.5)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.11, fadetime=1.5)]
[

... (全文24005字符)
```

### level_act32side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[charslot(slot="l",name="avg_npc_1212_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#1$1",focus="r")]
[name="医生"]还有什么我能帮忙的吗？
[charslot(slot="l",name="avg_npc_1212_1#1$1",focus="l")]
[name="特克诺"]不用了，剩下的就交给我的朋友，她这就来。
[Dialog]
[charslot]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_697_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="社区居民"]一接到你的消息我马上就过来了，你这家伙是怎么了？让我看看！
[Dialog]
[charslot(slot="m",name="avg_npc_1212_1#1$1",focus="m")]
[Delay(time=0.3)]
[playsound(key="$d_avg_clothmovement")]
[charslot(slot = "m", action="shake",random=true, power=5, times=10,duration=0.5,isblock=true)]
[name="特克诺"]哎，哎，你别拧我脑袋，这么多人你注意点，别撩我裙子。
[charslot(slot="m",name="avg_npc_697_1#1$1")]
[name="社区居民"]你这不挺好的......活蹦乱跳的。
[charslot(slot="m",name="avg_npc_1212_1#9$1",focus="m")]
[name="特克诺"]多亏了这两位，我发病的时候他们正好在旁边，帮了我一把。
[charslot(slot="m",name="avg_4125_rdoc_1#10$1",focus="m")]
[name="医生"]没事，我是医生，都是该做的。
[charslot(slot="m",name="avg_npc_697_1#1$1")]
[name="社区居民"]唉......这年头像你一样的医生不多了，大多数一听到我们的情况，跑都来不及。
[charslot(slot="m",name="avg_4125_rdoc_1#10$1",focus="m")]
[name="医生"]既然这位小姐有人照顾，那我们就不久留了......
[charslot(slot="m",name="avg_npc_697_1#1$1")]
[name="社区居民"]哎，别走啊。这是小店的名片，你们有空务必光顾，按摩推油一应俱全，你们来都是八折优惠。
[charslot(slot="m",name="avg_4124_iana_1#1$1",focus="m")]
[name="双月"]不用了，女士，我不是很需要。
[charslot(slot="m",name="avg_npc_1212_1#9$1",focus="m")]
[name="特克诺"]你们别客气，那家伙手艺不错，大家有个头疼脑热的都去找她。
[charslot(slot="m",name="avg_4125_rdoc_1#12$1",focus="m")]
[name="医生"]没关系，作为医生，我对自己的身体情况大致有了解，很健康，不需要额外关注。
[charslot(slot="m",name="avg_npc_697_1#1$1")]
[name="社区居民"]先生，试过再说。
[charslot(slot="m",name="avg_4124_iana_1#1$1",focus="m")]
[name="双月"]女士，我们还是保持距离比较好。
[Dialog]
[charslot]
女人听到双月的话，退后几步，从包里掏出一副手套，戴好后捏了捏手指，发出清脆的咔哒声。
[charslot(slot="m",name="avg_npc_697_1#1$1")]
[name="社区居民"]没事，离你远点也能按。
[charslot(slot="m",name="avg_4124_iana_1#4$1",focus="m")]
[name="双月"]这个距离你能碰到我？
[charslot(slot="m",name="avg_4125_rdoc_1#9$1",focus="m")]
[name="医生"]呃，咳咳，我听说过这种隔空进行的气功疗法，很多资料证实这不过是伪科......呃......
[Dialog]
[charslot]
只见她的手指在空中轻轻捏过几下，二人奇异地感受到一股温热的力量在按压自己的肩颈，瞬间，轻松与舒爽将他们温柔地包裹。
[charslot(slot="m",name="avg_4125_rdoc_1#6$1",focus="m")]
[name="医生"]啊......我感觉压力和焦虑......一扫而空......
[charslot(slot="m",name="avg_4124_iana_1#4$1",focus="m")]
[name="双月"]是错觉吗......我现在舒服得头皮发麻......啊......
[charslot(slot="m",name="avg_4125_rdoc_1#13$1",focus="m")]
[name="医生"]啊......谁还管什么科学......
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[Delay(time=2.5)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1214_1#5$1",focus="m")]
[name="迪亚兹"]什么......你说药被抢走了？！
[name="迪亚兹"]这可不是开玩笑的，埃内斯托先生，我们的社区里有很多感染者，他们都需要药物来控制病情。
[charslot(slot="m",name="avg_486_espumo_1#7",focus="m")]
[name="龙舌兰"]很抱歉，是我和阿莱塔小姐没能完成运输任务，造成的损失我们会尽快想办法弥补。
[charslot(slot="m",name="avg_npc_1214_1#7$1",focus="m")]
[name="迪亚兹"]你不会想赔钱了事吧？
[charslot(slot="m",name="avg_486_espumo_1#2",focus="m")]
[name="龙舌兰"]如果找不到，我会想办法按时赔偿你等量的药品。
[charslot(slot="m",name="avg_npc_1214_1#3$1",focus="m")]
[name="迪亚兹"]抱歉，埃内斯托先生......是我太着急了。
[charslot(slot="m",name="avg_npc_1214_1#8$1",focus="m")]
[name="迪亚兹"]那些抢药的人，你们有看到他们的样子吗？社区里人多，说不定能帮忙。
[charslot(slot="m",name="avg_486_espumo_1#7",focus="m")]
[name="龙舌兰"]这也是我们觉得蹊跷的地方，那些人埋伏在半途中突然冲出，似乎是早有准备。罗德岛在这里一向是小心处事，从不与人交恶......
[name="龙舌兰"]我实在想不出有什么人会这样针对我们。
[charslot(slot="m",name="avg_npc_1214_1#8$1",focus="m")]
[name="迪亚兹"]或许他们就是盯上了你们的药，抑制剂在黑市的价格可不低。
[charslot(slot="m",name="avg_486_espumo_1#7",focus="m")]
[name="龙舌兰"]在抢夺过程中他们采用的战术非常专业，动作迅速，干净利落......
[name="龙舌兰"]那些药品真的值得让一群人如此大动干戈吗？对了，我依稀记得在躲避时还听到了铳械的声音。
[charslot(slot="m",name="avg_npc_1214_1#5$1",focus="m")]
[name="迪亚兹"]铳械......又是专业的家伙......呵，雷内尔真瞧得起我们啊。
[charslot(slot="m",name="avg_486_espumo_1#7",focus="m")]
[name="龙舌兰"]迪亚兹先生，你觉得此次行动是有人针对社区吗？
[charslot(slot="m",name="avg_npc_1214_1#5$1",focus="m")]
[name="迪亚兹"]唉，我们与雷内尔也是积怨很久了，只是没想到......他最终会使用如此下作的手段。
[dialog]
[charslot]
[playsound(key="$d_avg_crwddiscuss_outside",loop=true,channel="1",volume=0.5)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_486_espumo_1#4",focus="m")]
[name="龙舌兰"]楼下发生什么了，怎么这么吵？
[charslot(slot="m",name="avg_486_espumo_1#3",focus="m")]
[name="龙舌兰"]......好像是有人在外面病情发作，被好心人送回来了。哟，这里三层外三层的，围的全都是来感谢的人。
[charslot(slot="m",name="avg_npc_1214_1#1$1",focus="m")]
[name="迪亚兹"]对我们好的人，当然是要报答的。让我看看来的是哪里的客......
[charslot(slot="m",name="avg_npc_1214_1#10$1",focus="m")]
[name="迪亚兹"]这几个怎么这么脸熟，感觉在哪里见过？
[Dialog]
[charslot]
从桌上拿起昨天的报纸，男人草草翻过几页找到八卦版，看见标题上赫然写着：《没人能忍受他的恶劣性格——雷内尔再次更换保镖》。
旁边的副标题则是《记者独家暗访：四名保镖两两轮换，究竟何方神圣》。
[stopsound(channel="1",fadetime=1.5)]
[charslot(slot="m",name="avg_486_espumo_1#3",focus="m")]
[name="龙舌兰"]嘶......这几张照片里的人和楼底下出现的人，是不是有些相似得过分了？
[charslot(slot="m",name="avg_npc_1214_1#7$1",focus="m")]
[name="迪亚兹"]呵，这下我们可真得好好报答报答了。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4124_iana_1#4$1",focus="m")]
[name="双月"]好像自己是完全崭新的一个人了......这种感觉很难形容。
[charslot(slot="m",name="avg_4125_rdoc_1#10$1",focus="m")]
[name="医生"]呼......谢谢你，女士，这种按摩方式太神奇了。
[charslot(slot="m",name="avg_npc_697_1#1$1")]
[name="社区居民"]这可是我从谢拉格学的传统按摩术。当年我在暴风雪中登上圣山，当地的圣女看我诚心才决定将这秘术传授给我。

... (全文20296字符)
```

### level_act32side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[charslot(slot="m",name="avg_npc_1271_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="带队的军官"]报告，药已经在地下库房里了。
[name="带队的军官"]和您指示的一样，我们学着那些人安置了炸弹，制造了一点混乱，就抢到手了。
[charslot(slot="m",name="avg_npc_1210_1#1$1")]
[name="马特奥"]不错......
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]可您怎么看着愁眉不展的？
[charslot(slot="m",name="avg_npc_1210_1#8$1")]
[name="马特奥"]我在想这批药该怎么脱手......就算改变包装销往地下市场，也很难不留下踪迹。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]您是怕有人查？
[charslot(slot="m",name="avg_npc_1210_1#3$1")]
[name="马特奥"]......行动开展时我收到一条消息，罗德岛此次前来派送药物的人身份有些特殊。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]确实，我们行动时留意到了，那个男的是个熟面孔......
[name="带队的军官"]可老潘乔现在人在监狱里，手下的人走的走，散的散。他儿子如今回到这里，未必还能像从前那样吃得开。
[charslot(slot="m",name="avg_npc_1210_1#1$1")]
[name="马特奥"]那可不一定，市政府之前有人透给我了些讯息，说坎黛拉在考虑培养自己的接班人，那小子正是几个考察对象之一。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]可老潘乔和坎黛拉不是......
[charslot(slot="m",name="avg_npc_1210_1#8$1")]
[name="马特奥"]哼，坎黛拉用人可一向不避亲仇。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]那我们怎么办......
[charslot(slot="m",name="avg_npc_1210_1#1$1")]
[name="马特奥"]我记得，上次雷内尔的小秘书来时和我们分享了一些资源。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]是......有几家店铺和仓库。
[charslot(slot="m",name="avg_npc_1210_1#1$1")]
[name="马特奥"]其中是不是有一家药企的仓库？
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]没错。
[charslot(slot="m",name="avg_npc_1210_1#8$1")]
[name="马特奥"]药品嘛，多一车少一车，估计他们也不会太在乎......
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]您的意思是，把包袱丢给雷内尔？
[charslot(slot="m",name="avg_npc_1210_1#9$1")]
[name="马特奥"]话可不能这么讲，他们主动找上门合作，我们回些谢礼不也正常？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$bar_intro", key="$bar_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_486_espumo_1#1",focus="r")]
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]久等了，埃内斯托先生。
[charslot(slot="l",name="avg_486_espumo_1#1",focus="l")]
[name="龙舌兰"]没有没有，我也是刚刚才来。
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]女士，麻烦给我一杯......
[charslot(slot="l",name="avg_486_espumo_1#1",focus="l")]
[name="龙舌兰"]我已经为你点好了，布克先生，还是老样子，双倍浓缩，对吗？
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]离开这里这么久，难为你还记得我的习惯。
[charslot(slot="l",name="avg_486_espumo_1#5",focus="l")]
[name="龙舌兰"]这点时间，再久也久不过我们共事的时间嘛。
[charslot(slot="l",name="avg_486_espumo_1#5",focus="none")]
[name="侍者"]两位的咖啡。
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]谢谢，嗯......不错，什么都是刚刚好。
[name="市长保镖"]唉，你走之后，再没人能像你一样做事面面俱到了，现在新来的小年轻啊......
[charslot(slot="l",name="avg_486_espumo_1#6",focus="l")]
[name="龙舌兰"]再等等看吧，放在那个环境里，人变得很快的。
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]哦，对了，坎黛拉女士托我把这份文件带给你。
[charslot(slot="l",name="avg_486_espumo_1#3",focus="l")]
[name="龙舌兰"]文件？坎黛拉女士有事情吩咐我去做？
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]不，是你要的东西。
[charslot(slot="l",name="avg_486_espumo_1#3",focus="l")]
[name="龙舌兰"]这......我今天才来找你，话还没说出口呢......
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]你一到多索雷斯，坎黛拉女士就知道消息了，又听说你们运送的货物遭人抢劫，肯定正着急。
[name="市长保镖"]文件袋里是近些天物流与交通的异常数据，相关的地点与人员都有记录。
[charslot(slot="l",name="avg_486_espumo_1#1",focus="l")]
[name="龙舌兰"]坎黛拉女士这样挂心，我都不知道该如何感激。
[charslot(slot="r",name="avg_npc_207",focus="r")]
[name="市长保镖"]哎，讲什么感激，只要你也能记挂着我们大家就好。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_warehouse",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4123_ela_1#2$1")]
[name="艾拉"]咳咳......
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]这地方灰比货还多。
[charslot(slot="m",name="avg_4124_iana_1#1$1")]
[name="双月"]艾拉，你接到的到底是什么任务？
[charslot(slot="m",name="avg_4123_ela_1#1$1")]
[name="艾拉"]仓库的货物买来之后就滞销了，积压在仓库里足足有半年，只剩一个管理员看守。
[charslot(slot="m",name="avg_4125_rdoc_1#13$1")]
[name="医生"]那不相当于敞开大门放任别人来拿？
[charslot(slot="m",name="avg_4123_ela_1#7$1")]
[name="艾拉"]是的，米沃什说几乎每天都会收到失窃报告。
[charslot(slot="m",name="avg_4124_iana_1#1$1")]
[name="双月"]我们是来追查丢失货物去向的吗？
[charslot(slot="m",name="avg_4123_ela_1#1$1")]
[name="艾拉"]不，这仓库只出不进已经是常态了，但昨天仓库看守人接到一通电话，说有一批药品会运过来，要他做好交接。
[name="艾拉"]米沃什觉得很蹊跷，让我们过来看看。
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]来者不善？
[charslot(slot="m",name="avg_4125_rdoc_1#2$1")]
[name="医生"]难说，这样一间仓库我看不出对方能有什么图谋。
[charslot(slot="m",name="avg_4124_iana_1#7$1")]
[name="双月"]或许米沃什只是想找个借口支开你和舒赫拉特，毕竟他好不容易空下来可以和雷内尔做点什么。
[charslot(slot="m",name="avg_4123_ela_1#3$1")]
[name="艾拉"]他大可以直说，我绝对不会出现在他俩一千米范围内。
[charslot(slot="m",name="avg_4124_iana_1#1$1")]
[name="双月"]看得出你真的对那家伙不太待见。
[charslot(slot="m",name="avg_4123_ela_1#7$1")]
[name="艾拉"]我只是不想天天看那个家伙大门不出在阳台打高尔夫。
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]至少他遵守了对你的承诺——安分。
[charslot(slot="m",name="avg_4123_ela_1#7$1")]
[name="艾拉"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_486_espumo_1#4",duration=1.5)]
[charslot(slot="r",name="avg_282_catap_1#10$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_486_espum

... (全文25672字符)
```

### level_act32side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_4126_fuze_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="导火索"]......呃，头好痛。
[charslot(slot="m",name="avg_npc_1212_1#1$1")]
[name="特克诺"]你醒了，大个子，给，这是冰块，你的额头肿了很大一个包。
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]你、你是攻击我的那个孩子？
[charslot(slot="m",name="avg_npc_1212_1#3$1")]
[name="特克诺"]再叫我一句孩子我就让你后脑勺再肿一个包。
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]......发生什么了？
[charslot(slot="m",name="avg_4124_iana_1#2$1")]
[name="双月"]总之就是，他们丢失的药品找回来了，所以他们和我们之间的误会也解除了......
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]什么药品？什么误会？怎么解决的？
[charslot(slot="m",name="avg_4125_rdoc_1#1$1")]
[name="医生"]通过一位可怜的司机先生，他的嘴很硬，但又没那么硬。
[charslot(slot="m",name="avg_4126_fuze_1#1$1")]
[name="导火索"]不......我觉得更混乱了......我们现在在哪里？
[charslot(slot="m",name="avg_4125_rdoc_1#1$1")]
[name="医生"]走吧，我扶你出去看看。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_4124_iana_1#8$1")]
[charslot(slot="r",name="avg_4123_ela_1#8$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]您的药，请拿好。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_001")]
[name="社区居民"]哦......谢谢......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4124_iana_1#8$1",focus="l")]
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="l")]
[name="双月"]你叫什么？在这里打个钩。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_001")]
[name="社区居民"]迈克......好了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4124_iana_1#8$1",focus="r")]
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]唔，这里还剩两份。
[charslot(slot="l",name="avg_4124_iana_1#7$1",focus="l")]
[name="双月"]我再从头核对一下名单，说不定是有人忘了拿......看看还有谁没来签字。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1212_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[name="特克诺"]......最后两份药是我的。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1212_1#6$1",focus="r")]
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]给你，特克诺小姐。
[charslot(slot="l",name="avg_npc_1212_1#6$1",focus="l")]
[name="特克诺"]咳咳......今天发生的事情我很抱歉，我们不知道抢劫事件另有他人指使......
[charslot(slot="r",name="avg_4123_ela_1#9$1",focus="r")]
[name="艾拉"]没关系，这些药品能物归原主就是最好的结果。
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]古斯塔夫告诉我，这里很多人都患有一种特殊疾病，如果没有这些抑制药剂，后果不堪设想。
[charslot(slot="l",name="avg_npc_1212_1#8$1",focus="l")]
[name="特克诺"]话说，那个上尉不是之前和雷内尔不对付吗？为什么一转脸就要抢我们的药来讨好雷内尔？
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]米沃什告诉我，他是冲雷内尔手里对这片社区的开发权而来。
[charslot(slot="l",name="avg_npc_1212_1#7$1",focus="l")]
[name="特克诺"]哼，有开发权又如何？这两年就算雷内尔自己拿着开发文件不也一样对我们束手无策。
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]那挺好，你们的社区文化很吸引人，就这样被开发成酒店赌场我觉得很可惜。
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[name="特克诺"]你不过是在这里站了半天罢了，说得好像很了解这里一样。
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]不过半天，但几乎每个来领药的人都极力向我推销自己的艺术作品。
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[name="特克诺"]还是要吃饭的嘛......话说你胳膊上那是什么？
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]是串刺绣手链，本来不打算买的，但是看见那孩子满手都是针扎的痕迹......
[charslot(slot="l",name="avg_npc_1212_1#8$1",focus="l")]
[name="特克诺"]（小声）谁家的孩子啊，这么笨手笨脚的......
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]你刚说什么？
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[name="特克诺"]呃......我说......你想去我的工作室坐坐吗？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="34_g6_noblelivingroom",screenadapt="coverall")]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_223")]
[name="拍卖会主持人"]五千万哥伦比亚金券，没有再加价的吗？
[name="拍卖会主持人"]好的，五千万金券落槌！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1211_1#5$1",focus="r")]
[name="雷内尔"]你说什么......一直丢东西的仓库？哪间仓库？
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]就是被你收购半年之后就倒闭的那家药企的仓库。
[charslot(slot="r",name="avg_npc_1211_1#6$1",focus="r")]
[name="雷内尔"]哦，好像是有这么回事......所以有人抢了那片社区的药，栽赃到你们头上，然后又想偷偷把药运到那间仓库去。
[charslot(slot="l",name="avg_4123_ela_1#3$1",focus="l")]
[name="艾拉"]准确来说，是你头上。
[charslot(slot="r",name="avg_npc_1211_1#9$1",focus="r")]
[name="雷内尔"]那我现在该怎么做？谢谢你帮我化解了这场误会？
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]不用谢，雷内尔先生。
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]听米沃什说你们打算离开我提供的住所了。怎么，找到自己的朋友们了吗？
[charslot(slot="l",name="avg_4123_ela_1#7$1",focus="l")]
[name="艾拉"]不，我们只是找到了另外一处落脚的地方。
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]哪里？
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]那片社区。
[charslot(slot="r",name="avg_npc_1211_1#6$1",focus="r")]
[name="雷内尔"]那里？虽然我也没什么异议，但你们为什么要离开？
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]我在那里看到了些很有意思的东西。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=2.5)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",na

... (全文17699字符)
```

### level_act32side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[charslot(slot="l",name="avg_npc_1214_1#7$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1212_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_1214_1#7$1",focus="l")]
[name="迪亚兹"]不可能，只要我还在这里一天，那几个雷内尔的手下就别想参与到我们艺术节中来。
[name="迪亚兹"]艺术节就在眼前了，这个节骨眼上我必须保证万无一失。
[charslot(slot="r",name="avg_npc_1212_1#8$1",focus="r")]
[name="特克诺"]可他们不都把药还回来了，雷内尔不也没反对。
[charslot(slot="l",name="avg_npc_1214_1#7$1",focus="l")]
[name="迪亚兹"]谁知道他们这么做揣的是什么心思？你能保证他们没有恶意吗？
[charslot(slot="r",name="avg_npc_1212_1#8$1",focus="r")]
[name="特克诺"]......
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]特克诺，你为什么不说话？
[charslot(slot="r",name="avg_npc_1212_1#8$1",focus="r")]
[name="特克诺"]老爹，我知道他们是雷内尔的人，报纸上到处都是他们和雷内尔的照片，我没法帮他们辩驳。
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[name="特克诺"]可那天我矿石病发作，倒在地上动弹不得，周围一个人也没有......我想，或许那一刻真的来了。
[name="特克诺"]就在我准备坦然接受一切时，他们来了，救起了我，将我送回到社区。
[name="特克诺"]老爹，很多年前，那场火灾里，我的心情也是一样绝望。但你来了，救了我，将我带出火场。
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]这怎么能一样呢，特克诺？我是个消防员，救你就是救你，本职而已，什么也不图。他们呢？你能保证吗？
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[name="特克诺"]如果你担心，我会找人盯紧他们的。就让他们看看我们在做什么，行吗，老爹？
[charslot(slot="l",name="avg_npc_1214_1#3$1",focus="l")]
[name="迪亚兹"]特克诺，你怎么这么固执？你为他们做担保......如果真的出事大家第一个怪罪的就是你啊。
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[name="特克诺"]求你了，老爹，我不会让他们捣乱的。
[charslot(slot="l",name="avg_npc_1214_1#3$1",focus="l")]
[name="迪亚兹"]唉，又来，每次和我一有争论，你就开始撒娇......
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[name="特克诺"]啊......求你了求你了，老爹......
[Dialog]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_1212_1#2$1",focus="r")]
[Delay(time=0.2)]
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[Delay(time=0.2)]
[charslot(slot="r",name="avg_npc_1212_1#2$1",focus="r")]
[Delay(time=0.2)]
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]行了，别眨巴眼睛了，不管用。
[charslot(slot="r",name="avg_npc_1212_1#6$1",focus="r")]
[name="特克诺"]可是这一套以前明明很管用的......
[charslot(slot="l",name="avg_npc_1214_1#2$1",focus="l")]
[name="迪亚兹"]你说呢？以前你这头发还不是红红绿绿的，你这身上还不是乌漆嘛黑的，你走起路来也不是当啷作响的。
[name="迪亚兹"]你这孩子......唉，以前清清爽爽的不好吗？
[charslot(slot="r",name="avg_npc_1212_1#8$1",focus="r")]
[name="特克诺"]哼......
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]算了，别噘嘴了，让他们领头的女人来找我，我有几句话和她说。
[charslot(slot="r",name="avg_npc_1212_1#1$1",focus="r")]
[name="特克诺"]来这里？
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]不，去那片沙滩。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", fadetime=0, amount=0, block=true)]
[Background(image="bg_beach_1",screenadapt="coverall")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_npc_1214_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4123_ela_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]艾拉小姐，知道我为什么找你吗？
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]应该不是来看风景？
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]你们在雷内尔手下做事，见识到的美景肯定不少，这片普通的沙滩入不了你们的眼吧。
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]不好说，在一条布满垃圾的小巷后面却是一片干净的沙滩，即使是太阳快落山的现在，光照也比社区好很多，我还挺惊喜的。
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]光照没什么办法，社区里建筑又多又高又乱。
[charslot(slot="l",name="avg_npc_1214_1#3$1",focus="l")]
[name="迪亚兹"]至于垃圾......以前堆在这里的垃圾比小巷里的还多，管事后，我亲自带着人清理干净，谁要是敢再丢，都会被我狠狠教训一顿。
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]我想，只要是来到多索雷斯的人，都该有机会享受属于自己的沙滩时光。
[charslot(slot="l",name="avg_npc_1214_1#1$1",focus="l")]
[name="迪亚兹"]我说得对不对，艾拉小姐？
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]迪亚兹先生，我不是来这里丢垃圾的，我只是想和你一样，坐下看看风景。
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]这里没有浮夸喧哗的游客，也没有铺天盖地的赌场广告，只是一片干净的沙滩，我很喜欢。
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]这里安静只是因为总有强风，所以不会有人来开发。
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]看到了，这里的树只有背风一侧长叶子。
[name="艾拉"]......他们很强韧，逆着风也能茁壮生长。
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]它们。
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]......抱歉，我的本地话学得不是很地道。
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]艾拉小姐......你们说要看看，那我们也没什么好藏的，但记住，看的时候管好自己的手，别碰不该碰的东西。
[name="迪亚兹"]特克诺喜欢和你们待在一起，社区里的大家也很欢迎你们，所以就让我来扮这个黑脸。
[charslot(slot="l",name="avg_npc_1214_1#7$1",focus="l")]
[name="迪亚兹"]你们要是敢辜负她的信任，让她伤心，我就算是拼了老命也要让你们付出代价。
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]迪亚兹先生，你对特克诺小姐实在是有些过度关照了，她只是你的属下，不是吗？
[charslot(slot="l",name="avg_npc_1214_1#8$1",focus="l")]
[name="迪亚兹"]我这一辈子没结婚没孩子，把她从火中救出后，在我心里，她就是我的孩子了。
[charslot(slot="l",name="avg_npc_1214_1#7$1",focus="l")]
[name="迪亚兹"]我的话就讲到这里，你们自己掂量着看吧。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",posfrom="0,0",posto="-100,0",duration=2)]
[charslot(slot="l",afrom=1,ato=0,duration=1.5)]
[Delay(time=3.5)]
[charslot(slot="r",name="avg_4123_ela_1#3$1",focus="r")]
[name="艾拉"]......真是个爱操闲心的老父亲。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="33_g8_srcroom",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadeti

... (全文22433字符)
```

### level_act32side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_windows",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[charslot(slot="l",name="avg_4123_ela_1#6$1",duration=1.5)]
[charslot(slot="r",name="avg_4126_fuze_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_4126_fuze_1#1$1",focus="r")]
[name="导火索"]看来特克诺已经穿戴好安全设备了，看她抓耳朵的样子，根本不像是准备好了。
[name="导火索"]现在下去？
[charslot(slot="l",name="avg_4123_ela_1#6$1",focus="l")]
[name="艾拉"]稍等，等她下降到既定位置，我可不想在速降过程中发生冲撞。
[Dialog]
[charslot]
[playsound(key="$d_avg_sldrsldng",channel="1")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[Delay(time=1.5)]
[stopsound(channel="1")]
[name="特克诺"]哎哎哎，慢点慢点，我掉得太快了！！
[Dialog]
[charslot(slot="l",name="avg_4123_ela_1#10$1",focus="l")]
[charslot(slot="r",name="avg_4126_fuze_1#1$1",focus="l")]
[name="艾拉"]这也算快吗？
[charslot(slot="r",name="avg_4126_fuze_1#1$1",focus="r")]
[name="导火索"]她就像片小羽毛，缓缓落下。
[charslot(slot="l",name="avg_4123_ela_1#1$1",focus="l")]
[name="艾拉"]......这会儿可不是笑到肚子痛的好时候。
[charslot(slot="r",name="avg_4126_fuze_1#1$1",focus="r")]
[name="导火索"]她到位置了。
[name="导火索"]一切就绪，你也可以动身了。
[Dialog]
[charslot]
[playsound(key="$d_avg_clothmovement")]
扯扯手中的安全绳，艾拉侧身翻出窗户，将脚尖抵在墙上，努力让悬空的身体在风中保持住平衡。
等了一会儿，风渐渐停下，她松开一只抓住绳子的手，将被风吹歪的帽子戴正，向屋内的导火索露出微笑。
随后，她将另一只手也松开，消失在窗外，只留下一段绳索挂在窗沿快速滑动。
[Dialog]
[playsound(key="$d_avg_sldrsldng")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4126_fuze_1#1$1",focus="m")]
[name="导火索"]唔......不错，看来她们是成功会晤了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="38_g20_skyblue_R1",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1212_1#5$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_sldrsldng")]
[charslot(slot="r",name="avg_4123_ela_1#1$1",posfrom="0,25",posto="0,0",duration=1.5)]
[charslot(slot="r",afrom=0,ato=1,duration=1)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1212_1#4$1",focus="l")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="特克诺"]哇啊啊啊——！你怎么也跳下来了！
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]别吵，专注点，刚才你差点就要剪断一根主操作线了。
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[name="特克诺"]那些跟着你的人呢？
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]甩掉了。
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[name="特克诺"]老爹难道没有警告过你不要到处乱走吗......
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]嗯，说了。
[charslot(slot="l",name="avg_npc_1212_1#6$1",focus="l")]
[name="特克诺"]那你还跟过来干什么？
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]确保你不会搞砸这项工程。
[charslot(slot="l",name="avg_npc_1212_1#6$1",focus="l")]
[name="特克诺"]你这人......你知道该怎么办吗，就这么讲我？
[charslot(slot="r",name="avg_4123_ela_1#8$1",focus="r")]
[name="艾拉"]那你呢？
[charslot(slot="l",name="avg_npc_1212_1#6$1",focus="l")]
[name="特克诺"]呃......
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]下降时我简单检查了一下木偶手臂上的控制元件，是液压驱动的问题，把你的工具给我。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_windows",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$rungeneral")]
[Delay(time=2.5)]
[name="？？？"]他们就在上面，快点！
[name="？？？"]要不是底下那个女人拦着，早就逮住他们了......
[charslot(slot="m",name="avg_4126_fuze_1#1$1",focus="m")]
[name="导火索"]嚯......
[name="导火索"]看起来之后都是我的麻烦了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="作业人员"]领队！好消息，绳索交缠的地方解开了！
[charslot(slot="m",name="avg_npc_1274_1#1$1",focus="m")]
[name="指挥人员"]这么快？那赶紧把特克诺拉上来，我们继续组装木偶的手臂与身体。
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="作业人员"]她说她要继续留在那里。
[charslot(slot="m",name="avg_npc_1274_1#1$1",focus="m")]
[name="指挥人员"]什么？
[Dialog]
[charslot]
[playsound(key="$d_gen_transmissionget")]
[name="特克诺"]我说我要继续待在这里！我会在这里辅助安装！
[charslot(slot="m",name="avg_npc_1274_1#1$1",focus="m")]
[name="指挥人员"]啊，你愿意帮忙当然挺好，可你能保证不会影响到旁边的艾拉女士吗？
[Dialog]
[charslot]
[playsound(key="$d_gen_transmissionget")]
[name="特克诺"]你再说一遍？我一会儿上去要一拳揍歪你的鼻子！
[charslot(slot="m",name="avg_npc_1274_1#1$1",focus="m")]
[name="指挥人员"]咳咳，艾拉小姐，为了我的鼻子着想，你能让她继续留在那里吗？
[Dialog]
[charslot]
[playsound(key="$d_gen_transmissionget")]
[name="艾拉"]当然可以，特克诺小姐是位讲义气的朋友，不愿意让我一个人面对高空作业的危险。除了感激，我还能说什么呢？
[name="特克诺"]咳、咳！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_416_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_242",focus="l")]
[name="惊讶的居民"]看，木偶的手臂重新开始移动了！
[name="惊讶的居民"]在那里吊着的人是特克诺......怎么还有另外一个人？
[charslot(slot="r",name="avg_npc_242",focus="r")]
[name="疑惑的居民"]那是谁？工程师，技师，还是特克诺的助手？
[charslot(slot="l",name="avg_npc_416_1#1$1",focus="l")]
[name="惊讶的居民"]助手，你确定？特克诺一向不喜欢有人参与到她的设计中来。
[charslot(slot="r",name="avg_npc_242",focus="r")]
[name="疑惑的居民"]我再看看......不行，视线被挡住了。哎，朋友，你能认出来吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4124_iana_1#1$1",focus="m")]
[name="双月"]在喊我吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_416_1#1$1",focus="r")]
[charslot(slot="r",name="avg_

... (全文18951字符)
```

### level_act32side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G02",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[name="电视里的声音"]昨夜，一对巨大的木偶出现在本市街头艺术社区中，其精美绝伦的程度足以让每个见到它们的人瞠目结舌。
[name="电视里的声音"]社区中的艺术家设计制作了这对木偶，在昨天的彩排表演中，它们在月光下翩翩起舞。
[name="电视里的声音"]我们可以看到拍摄的画面中，在社区居民的精细操控下，它们舞姿灵动曼妙，好像真人一般。
[name="电视里的声音"]众所周知，该社区生活着大量的帮派分子与流浪汉，犯罪率居高不下，从没有人敢靠近。但昨晚的表演吸引了许多人冒险前去观看。
[name="电视里的声音"]接下来让我们把画面给到本台记者，看看现场观众是怎么说的。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1000_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="旅客"]老板，来份冰淇淋。
[charslot(slot="m",name="avg_npc_1002_1#1$1")]
[name="摊贩"]......
[charslot(slot="m",name="avg_npc_1000_1#1$1")]
[name="旅客"]老板？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_bar_1",screenadapt="coverall")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="电视里的声音"]先生，请问这两个木偶出现的时候你正在做什么？
[name="电视里的声音"]我正在跑步，突然看到两栋楼之间出现了一个巨大的人脸，吓得我直接坐到地上。
[name="电视里的声音"]后来我壮着胆子，走上前去观看了整场表演......
[name="电视里的声音"]看完后我的双腿还在不停打颤，不过这次不是被吓到了，而是被震撼到了。
[name="电视里的声音"]好的，先生，谢谢你愿意接受我们的采访。
[name="电视里的声音"]哈哈，从这位先生走路的姿势来看，他说的都是实话。现在让我们把镜头对准那些生活在这里的艺术家。
[name="电视里的声音"]问问他们为何要造出如此巨大的一对木偶，又有怎样的故事要向我们讲述。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_020")]
[name="赌场荷官"]女士们，先生们，终局请下注。
[charslot(slot="m",name="avg_npc_176")]
[name="游客"]嘘......
[charslot(slot="m",name="avg_npc_020")]
[name="赌场荷官"]诸位？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_524_1#1$1")]
[name="记者"]哦，看刚刚走过的女孩，她可是这里的核心人物。小姑娘，请留步！
[charslot(slot="m",name="avg_npc_1212_1#1$1")]
[name="特克诺"]嗯......？
[charslot(slot="m",name="avg_npc_524_1#1$1")]
[name="记者"]听说你就是这场表演的总设计师，这么小的年纪担此大任......
[charslot(slot="m",name="avg_npc_1212_1#7$1")]
[name="特克诺"]够了，要问什么你快点问，我还有急事。
[charslot(slot="m",name="avg_npc_524_1#1$1")]
[name="记者"]我们想知道的事情非常简单，为什么那两个木偶会出现在这里？
[name="记者"]如此大费周章，是为了将大家的目光吸引到这片社区吗？
[charslot(slot="m",name="avg_npc_1212_1#7$1")]
[name="特克诺"]呵，几年前我们有两栋大楼在火灾中焚毁，也没见有几个人把目光投向这里啊。
[charslot(slot="m",name="avg_npc_524_1#1$1")]
[name="记者"]火灾......？
[charslot(slot="m",name="avg_npc_1212_1#8$1")]
[name="特克诺"]（小声）果然没什么人记得。
[charslot(slot="m",name="avg_npc_1212_1#7$1")]
[name="特克诺"]我们的木偶表演就是为了纪念那场火灾，纪念在那天离开我们的朋友。为此我们特意将开幕时间定在了火灾发生的同一天。
[charslot(slot="m",name="avg_npc_524_1#1$1")]
[name="记者"]但广受关注的克里斯达尔艺术馆开幕式也选在了当天进行，这会给你们带来压力吗？
[charslot(slot="m",name="avg_npc_1212_1#2$1")]
[name="特克诺"]彩排前或许有，但现在基本没有......
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="电视里的声音"]......在艺术节正式开幕当天，表演效果只会更加轰动，我并不认为一个艺术展馆的开幕典礼能和我们的表演平分秋色。
[name="电视里的声音"]不论以怎样的噱头粉饰，归根结底，艺术馆的开幕典礼向所有人传达的不过只有一件事——
[name="电视里的声音"]那就是雷内尔先生作为生意人的生意经。
[Dialog]
[PlaySound(key="$d_avg_fastener", volume=0.7)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1213_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1211_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1211_1#1$1",focus="r")]
[name="雷内尔"]为什么要关掉电视，米沃什？我正在看呢。
[charslot(slot="l",name="avg_npc_1213_1#1$1",focus="l")]
[name="米沃什"]你该去睡一会儿了。
[charslot(slot="r",name="avg_npc_1211_1#6$1",focus="r")]
[name="雷内尔"]别啊，我现在一点也不困。
[charslot(slot="l",name="avg_npc_1213_1#2$1",focus="l")]
[name="米沃什"]去睡觉。
[charslot(slot="r",name="avg_npc_1211_1#5$1",focus="r")]
[name="雷内尔"]米沃什......你为什么板着脸，为什么不替我高兴？
[charslot(slot="l",name="avg_npc_1213_1#1$1",focus="l")]
[name="米沃什"]去睡一觉吧，雷内尔。
[charslot(slot="r",name="avg_npc_1211_1#9$1",focus="r")]
[name="雷内尔"]十几年过去了，那份本应属于我的生日礼物终于回到了我的手上，我真的很开心。
[charslot(slot="l",name="avg_npc_1213_1#1$1",focus="l")]
[name="米沃什"]是吗？看你现在乱糟糟的模样，你的话在我听来没有任何说服力。
[charslot(slot="r",name="avg_npc_1211_1#10$1",focus="r")]
[name="雷内尔"]那本应该是送给我的八音盒......过生日前，她说要送我一个。
[name="雷内尔"]但是老混蛋很不开心，她怎么能创作一件不产生任何经济效益的作品呢？
[charslot(slot="r",name="avg_npc_1211_1#10$1",focus="r")]
[name="雷内尔"]她是天才，是明星，她的作品注定是要放在展会上被层层要价，怎么能放在一个男孩的床头柜上寂寂无名呢？
[charslot(slot="l",name="avg_npc_1213_1#5$1",focus="l")]
[name="米沃什"]......但它回到你手中了，时隔多年，它最终还是物归原主。
[charslot(slot="r",name="avg_npc_1211_1#9$1",focus="r")]
[name="雷内尔"]我很喜欢，就算它被改得面目全非我也喜欢。
[name="雷内尔"]米沃什，那她呢？她会喜欢我的回礼吗？
[charslot(slot="l",name="avg_npc_1213_1#2$1",focus="l")]
[name="米沃什"]......你送给她的一切她都爱不释手。
[charslot(slot="r",name="avg_npc_1211_1#8$1",focus="r")]
[name="雷内尔"]......
[charslot(slot="l",name="avg_npc_1213_1#1$1",focus="l")]
[name="米沃什"]为什么不说话？
[charslot(slot="r",name="avg_npc_1211_1#10$1",focus="r")]
[name="雷内尔"]......我确实想睡一会了，米沃什。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1212_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1214_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1214_1#1$1",focus="r")]
[name="迪亚兹"]我看到你在电视里说那些话了，你不该在媒体面前这样锋芒毕露。
[charslot(slot="l",name="avg_npc_1212_1#6$1",focus="l")]
[name="特克诺"]老爹，你既然提议去搞那个巨大的木偶，就不应该担心我们的风头是不是出得太过了。
[charslot(slot="r",name="avg_npc_1214_1#8$1",focus="r")]
[name="迪亚兹"]唉，特克诺，我刚刚收到了一份信函，来自

... (全文15706字符)
```

### level_act32side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_20_G07",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$tech_intro", key="$tech_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_207",duration=1.5)]
[Delay(time=2.5)]
[charslot]
[charslot(slot="l",name="avg_npc_207",focus="r")]
[charslot(slot="r",name="avg_npc_198_1#1",focus="r")]
[name="坎黛拉"]布克，有事吗？
[charslot(slot="l",name="avg_npc_207",focus="l")]
[name="市长保镖"]坎黛拉女士，上尉先生好像是坐不住了。
[charslot(slot="r",name="avg_npc_198_1#2",focus="r")]
[name="坎黛拉"]被雷内尔耍了那么多次，他现在才坐不住吗？
[charslot(slot="l",name="avg_npc_207",focus="l")]
[name="市长保镖"]我们的人递消息过来，说是他打算动用武力来搞定那片社区。
[charslot(slot="r",name="avg_npc_198_1#3",focus="r")]
[name="坎黛拉"]在我的地界上动武，他哪里来的胆子？
[charslot(slot="l",name="avg_npc_207",focus="l")]
[name="市长保镖"]联合政府内有人支持他的行动，现在他有权调遣城内所有联合政府的军事力量。
[charslot(slot="r",name="avg_npc_198_1#1",focus="r")]
[name="坎黛拉"]这些家伙，手伸得越来越长了......
[charslot(slot="l",name="avg_npc_207",focus="l")]
[name="市长保镖"]我们是否要采取行动阻止？
[charslot(slot="r",name="avg_npc_198_1#1",focus="r")]
[name="坎黛拉"]暂且不动吧。社区那帮人随心所欲，经常和市政府唱反调。要是他们真能将那里的事情解决干净，也算是帮了我一个忙。
[name="坎黛拉"]不过你也要时刻盯着，马特奥生性短视又贪婪，手握这么大的权力，我不信他不会动些歪脑筋。
[charslot(slot="l",name="avg_npc_207",focus="l")]
[name="市长保镖"]此外，坎黛拉女士，几天后的克里斯达尔艺术馆的开幕式您打算去吗？
[charslot(slot="r",name="avg_npc_198_1#2",focus="r")]
[name="坎黛拉"]唉，那也是个爱惹是生非的啊......我不去了，派人把贺礼送到就行。
[charslot(slot="l",name="avg_npc_207",focus="l")]
[name="市长保镖"]那我先下去了。
[charslot(slot="r",name="avg_npc_198_1#1",focus="r")]
[name="坎黛拉"]等等，还有一件事我需要埃内斯托去做，你记得告诉他。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g11_deluxeroom_n",screenadapt="coverall")]
[Delay(time=3.5)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[playsound(key="$d_avg_crwddiscuss_outside",loop=true,channel="1",volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_177",focus="m")]
[name="殷勤的投资商"]雷内尔，你还记得我吗？几年前我们见过一面。
[charslot(slot="m",name="avg_npc_1211_1#5$1",focus="m")]
[multiline(name="雷内尔")]您是......等等，别提醒我，我一定能想起来。
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="m")]
[multiline(name="雷内尔",end=true)]诺里斯先生，对吗？三年前我们一起竞拍过一尊来自米诺斯的雕像。
[charslot(slot="m",name="avg_npc_177",focus="m")]
[name="殷勤的投资商"]我对你优秀的记忆力有深刻的印象，那天晚上你一直在谈论那尊雕像，从它的创作者到几个经手的收藏家，你竟然都记得。
[charslot(slot="m",name="avg_npc_1211_1#1$1",focus="m")]
[name="雷内尔"]嗯，不轻易忘记......确实，算是我的优点之一了。
[charslot(slot="m",name="avg_npc_177",focus="m")]
[name="殷勤的投资商"]这么长时间不见，你的变化可真大，褪去了青涩，愈发有你父亲的风范了。
[charslot(slot="m",name="avg_npc_1211_1#1$1",focus="m")]
[name="雷内尔"]只可惜他离开得太早，不能看见我正在做的一切。
[charslot(slot="m",name="avg_npc_177",focus="m")]
[name="殷勤的投资商"]别太伤感，当孩子做出一番超越父辈的伟业，就算父亲无法得见，他也必定会为自己的孩子感到自豪。
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="m")]
[name="雷内尔"]呵......但愿他真的会吧。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="谄媚的收藏家"]科瓦尔斯基先生，我刚刚一直在找您呢。
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="m")]
[name="雷内尔"]嘿，切蒂，最近还好吗？楼底下的展馆里刚刚到了一幅伊比利亚的湿壁画，去年一整年你都在四处奔波，收集这些杰作。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="谄媚的收藏家"]那都是去年的事了，今天我打算尽可能多地买入那些来自炎国的水墨画。
[charslot(slot="m",name="avg_npc_1211_1#1$1",focus="m")]
[name="雷内尔"]想不到你们那里的投资风向转变得这样快。
[charslot(slot="m",name="avg_npc_177",focus="m")]
[name="殷勤的投资商"]这就是雷内尔你不知道了，哪里是投资风向变得快，是我们切蒂先生的心变得快。
[charslot(slot="m",name="avg_npc_1211_1#10$1",focus="m")]
[name="雷内尔"]......这话听来有趣。
[charslot(slot="m",name="avg_npc_177",focus="m")]
[name="殷勤的投资商"]（小声）他今年新换了一位太太，那位女士很喜欢水墨画。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="谄媚的收藏家"]既然你说到这个，有些事我就直白讲了，科瓦尔斯基先生。
[name="谄媚的收藏家"]那些湿壁画我想尽快出手，不知道您有没有路子，玛丽她很讨厌凯瑟琳留下的藏品。
[charslot(slot="m",name="avg_npc_1211_1#10$1",focus="m")]
[name="雷内尔"]应该有些办法，我会尽量试试的。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="谄媚的收藏家"]别谦虚了，您可是斯特凡·科瓦尔斯基的儿子，您父亲当年只用了不到半个月就将我手中所有悉数......
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4123_ela_1#1$1",duration=1.5)]
[Delay(time=3.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",posfrom="0,0",posto="-100,0",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=1)]
[Delay(time=3.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1211_1#10$1",focus="m")]
[Delay(time=0.5)]
[charslot(slot="r",name="avg_4123_ela_1#1$1",posfrom="200,0",posto="0,0",duration=2)]
[charslot(slot="r",afrom=0,ato=1,duration=1.5)]
[Delay(time=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[stopsound(channel="1",fadetime=1.5)]
[charslot(slot="r",posfrom="0,0",posto="100,0",duration=2)]
[Delay(time=2)]
[charslot(slot="r",focus="r")]
[name="艾拉"]啊，不好意思，雷内尔先生，我没注意到您站在这里。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="谄媚的收藏家"]你这女人怎么回事，看不到三个大活人站在这里吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1211_1#1$1",focus="l")]
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="l")]
[name="雷内尔"]诸位，她是我新招来的保镖，我之后会教训她的。
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]请问您现在需要换件衣服吗？
[charslot(slot="l",name="avg_npc_1211_1#1$1",focus="l")]
[name="雷内尔"]当然了，这些酒黏在身上真的很难受，失陪了，诸位。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_npc_1211_1#1$1",focus="l")]
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="l")]
[name="雷内尔"]多亏你那杯酒，再有一个人围过来我就要窒息了。
[charslot(slot="r",name="avg_4123_ela_1#3$1",focus="r")]
[name="艾拉"]不用谢，该做的。
[charslot(slot="l",name="av

... (全文16897字符)
```

### level_act32side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="48_g9_gangsters",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_1215_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="社区守卫"]特克诺，老爹，外面来了好多士兵，架起了一道铁丝网，气势汹汹地堵在楼底下。
[charslot(slot="m",name="avg_npc_1212_1#4$1")]
[name="特克诺"]士兵？他们来干什么？
[charslot(slot="m",name="avg_npc_1215_1#1$1")]
[name="社区守卫"]他们带着授权文件来，说是要彻查这里的消防隐患。
[charslot(slot="m",name="avg_npc_1214_1#6$1")]
[name="迪亚兹"]什么？！
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[charslot(slot="r",name="avg_npc_1214_1#6$1",focus="l")]
[name="特克诺"]啊......这是士兵该管的吗？不应该是那些傻头傻脑的政府机关人员来干这事吗？
[charslot(slot="r",name="avg_npc_1214_1#7$1",focus="r")]
[name="迪亚兹"]特克诺，你带着社区里的老人和孩子离开这里，去罗德岛的办事处找埃内斯托。
[name="迪亚兹"]其他人抄上家伙和我走，今天咱们也别想睡好觉了。
[charslot(slot="l",name="avg_npc_1212_1#3$1",focus="l")]
[name="特克诺"]我、我要留在这里！
[charslot(slot="r",name="avg_npc_1214_1#7$1",focus="r")]
[name="迪亚兹"]你的源石技艺是我们中最好的，把他们交给你我才放心。
[charslot(slot="l",name="avg_npc_1212_1#5$1",focus="l")]
[name="特克诺"]可是......
[charslot(slot="r",name="avg_npc_1214_1#1$1",focus="r")]
[name="迪亚兹"]特克诺，记住我交代给你的任务，保护好那些人，无论发生什么，都以这件事为重。
[charslot(slot="l",name="avg_npc_1212_1#7$1",focus="l")]
[name="特克诺"]......好，老爹。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g8_slums",screenadapt="coverall")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_gen_soldiersrun")]
[charslot(slot="l",name="avg_npc_1272_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1272_1#1$1",duration=1.5)]
[Delay(time=3.5)]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1214_1#7$1",duration=1.5)]
[Delay(time=2.5)]
[name="迪亚兹"]诸位来到这里到底是为了什么？
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]迪亚兹·冈萨雷斯，我记得你，从辛嘉斯的军队退伍后，你来到多索雷斯成为市消防局的一员。
[name="带队的军官"]在消防局待了五年，无数次在火场出入，换来的荣誉数都数不清。
[name="带队的军官"]怎么你现在却沦落到了这个破烂的地方呢？
[charslot(slot="m",name="avg_npc_1214_1#7$1")]
[name="迪亚兹"]我是消防员，不论待在哪里，干的都是防火救灾的活儿，豪华酒店的火是火，街头巷尾的火也是火。
[name="迪亚兹"]只要是火，我都能救，我都会救。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]呵......迪亚兹你是内行人，肯定会积极配合我们的工作，对吧？
[charslot(slot="m",name="avg_npc_1214_1#5$1")]
[name="迪亚兹"]少来这一套，你们打的主意我一清二楚，明面上说是消防检查，实际上只是为了赶人。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]我们也是为了这里的安全着想，你也不想几年前的火灾重演吧。
[charslot(slot="m",name="avg_npc_1214_1#5$1")]
[name="迪亚兹"]滚出去，这里的事情我会操心，轮不到你们来指手画脚。
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]唉，不行啊，迪亚兹，这场艺术节表演已经吸引了全市的目光，这里的事已经不光是你们的事了。
[name="带队的军官"]我们来这里，就是为了确保你们的表演不会给大家的生活造成不好的影响。
[charslot(slot="m",name="avg_npc_1214_1#5$1")]
[name="迪亚兹"]我说了，滚！
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]哎，老兄你还是不明白形势啊，既然要检查，我们怎么能不做准备呢？
[Dialog]
[charslot]
[playsound(key="$d_gen_soldiersrun")]
[charslot(slot="l",name="avg_npc_1272_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1272_1#1$1",duration=1.5)]
[Delay(time=3.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1271_1#1$1")]
[name="带队的军官"]辛苦诸位好好查一查了，每一个危险源头都不要放过。
[name="带队的军官"]如果有人敢阻拦我们的检查，就是危害公共安全，直接动手吧，我们不用客气。
[Dialog]
[charslot]
[playsound(key="$d_avg_oicrwd")]
[name="军官的手下"]是！
[Dialog]
[Delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1212_1#3$1")]
[name="特克诺"]这群混账......这群该死的混账。
[charslot(slot="m",name="avg_npc_240")]
[name="稚嫩的孩子"]特克诺姐姐，我怕......我们到底要去哪里啊？
[charslot(slot="m",name="avg_npc_1212_1#9$1")]
[name="特克诺"]有坏人进到社区里来了，这里不安全，我送你们去埃内斯托先生那里。
[charslot(slot="m",name="avg_npc_093")]
[name="年迈的老人"]那其他人呢......我们就把他们丢在这里吗？
[charslot(slot="m",name="avg_npc_1212_1#8$1")]
[name="特克诺"]......老爹只说让我看顾好你们......其他的......他会留下来安排。
[charslot(slot="m",name="avg_npc_1212_1#7$1")]
[name="特克诺"]他们正在往这边来，我们得赶紧离开了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_ltalley",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_singleblunt",channel="1")]
[Delay(time=0.3)]
[playsound(key="$bottlebroken",channel="1")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_002")]
[name="社区电工"]你们这是干什么？！
[charslot(slot="m",name="avg_npc_1272_1#1$1")]
[name="暴躁的军官"]排查木偶的每条供电线路，只要有隐患，就统统给我拆个干净。
[charslot(slot="m",name="avg_npc_002")]
[name="社区电工"]我好不容易搭设好的电路啊，你们给我停手！
[charslot(slot="m",name="avg_npc_1272_1#1$1")]
[name="暴躁的军官"]滚开吧你，真碍眼。
[Dialog]
[charslot]
[playsound(key="$d_avg_singleblunt",channel="1")]
[Delay(time=0.3)]
[playsound(key="$d_avg_glassbroken",channel="1")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_002")]
[name="社区电工"]这位军老爷，别这样，有话我们好好商量，我半年的心血啊......别拆了，求求你们别拆了......
[charslot(slot="m",name="avg_npc_1272_1#1$1")]
[name="暴躁的军官"]我管你搭了几个月，就你这种故意破坏用电安全与扰乱供电秩序的行为，把你送去监狱都不过分。
[Dialog]
[charslot]
[playsound(key="$d_avg_singleblunt",channel="1")]
[Delay(time=0.3)]
[playsound(key="$d_avg_glassbroken",channel="1")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_002")]
[name="社区电工"]停手啊——！
[Dialog]
[charslot]
[playsound(key="$d_avg_singleblunt",channel="1")]
[Delay(time=0.3)]


... (全文31172字符)
```

### level_act32side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_ltroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4123_ela_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1213_1#4$1")]
[name="米沃什"]艾拉小姐......你怎么来了？
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]雷内尔在哪里？
[charslot(slot="m",name="avg_npc_1213_1#1$1")]
[name="米沃什"]在阳台上打高尔夫......
[Dialog]
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[Delay(time=0.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",posfrom="0,0",posto="100,0",duration=1.5)]
[charslot(slot="m",afrom=1,ato=0,duration=1)]
[Delay(time=1.5)]
[charslot]
[charslot(slot="m",name="avg_npc_1213_1#4$1")]
[name="米沃什"]等等，艾拉小姐！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g10_deluxeroom",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_avg_whshglf")]
[Delay(time=1.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4123_ela_1#6$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1211_1#7$1")]
[name="雷内尔"]抱歉......刚刚那颗球打到你了？你这么生气做什么？
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]......就在昨天，迪亚兹的社区出事了。
[charslot(slot="m",name="avg_npc_1211_1#6$1")]
[name="雷内尔"]出事？什么事？
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]他们的艺术节表演被毁了个彻底，你不知道吗？
[charslot(slot="m",name="avg_npc_1211_1#11$1")]
[name="雷内尔"]......你这是什么兴师问罪的语气？
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]米沃什曾经找到我说，希望我能说服社区里的人推迟他们的艺术节表演，不要和你的开幕式撞了时间。
[charslot(slot="m",name="avg_npc_1211_1#10$1")]
[name="雷内尔"]没错，是我让米沃什去找你谈的。所以你认为......因为你没答应，我便授意别人去做了这事。
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]......在你身边担任保镖时，我有很多次见到米沃什去找那位上尉谈合作，他运送药物的仓库又在你名下。
[name="艾拉"]现在看来，你们的关系并没有表现出来的那么紧张，他甚至在你开幕式的邀请名单上。
[name="艾拉"]有很多疑点我在当时没有细究，但如今出事了，我得来问问你。
[charslot(slot="m",name="avg_npc_1211_1#2$1")]
[name="雷内尔"]告诉我，艾拉小姐，你是心里带着答案来问我的吗？
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]我没有预设答案，我想听你的解释。
[charslot(slot="m",name="avg_npc_1211_1#10$1")]
[name="雷内尔"]不......我主动找上他并不是为了与他合作，只是......想看他笑话。
[name="雷内尔"]那么多人都在那片社区吃过亏，我想，说不定那家伙也能在他们手下吃点苦头。
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]......什么？
[charslot(slot="m",name="avg_npc_1211_1#2$1")]
[name="雷内尔"]事实的确如此，不管你信不信，我没有指使他去做这件事......
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]或许你的本意并非如此......但你有想过这样做可能带来的后果吗，雷内尔？
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]你让一位武装部队的首领直接对上了一群手无寸铁的社区平民。
[charslot(slot="m",name="avg_npc_1211_1#2$1")]
[name="雷内尔"]我没有想到结果会......
[charslot(slot="m",name="avg_4123_ela_1#4$1")]
[name="艾拉"]或者你根本不在乎！
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]为了安放你庞大的自我，你修建了这座华美的艺术馆。这难道不够吗？为什么你还要一次次地招惹那些与你毫无干系的人？
[name="艾拉"]为什么？你需要靠这些来证明你的存在感吗，雷内尔？
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1213_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="米沃什"]够了，艾拉小姐，你该离开了。
[charslot(slot="m",name="avg_4123_ela_1#6$1")]
[name="艾拉"]米沃什先生，我一直很想问，你在这样一个庞然大物身边，有足够的空间喘息吗？
[charslot(slot="m",name="avg_npc_1213_1#6$1")]
[name="米沃什"]......出去。
[charslot(slot="m",name="avg_npc_1211_1#10$1")]
[name="雷内尔"]够了，艾拉小姐，如果你执意要为这出惨剧找个罪魁祸首，那你就当是我做的吧。
[charslot(slot="m",name="avg_npc_1211_1#8$1")]
[name="雷内尔"]你该离开了，艾拉。
[Dialog]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[playsound(key="$d_avg_whshglf")]
[Image(image="48_i02",fadetime=0,screenadapt="coverall")]
[ImageTween(xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1, yScaleTo=1, duration=35, block=false)]
[delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
男人背过身站定，不再理会艾拉，随即重心轻移，肩膀内旋，优雅利落地挥出一杆。
球在空中划出一道曲线，本应落在距离洞口一米开外，可高尔夫球诡异地改变了原先的路线，滑进了球洞。
艾拉从球筐里随手拾起一颗球，举高在阳光下。
[name="艾拉"]以前我就注意到了，无论你打出的球有多么刁钻古怪的抛物线，最终都会落进洞里。
[name="艾拉"]米沃什先生，作为雷内尔最亲近的人，你能告诉我为什么吗？
[name="米沃什"]......
[name="艾拉"]所以，你这辈子有没有试过靠自己的本事挥出一杆，雷内尔？在空中挥出一道真实的曲线。
[name="雷内尔"]尝试过很多次。
[name="艾拉"]结果如何？
[name="雷内尔"]心力交瘁，那片草地根本没有球洞，我只是徒劳。
[name="艾拉"]......那真是太遗憾了。
叹了口气，艾拉将手中的高尔夫球掷出，在草坪上滚过几圈后，那颗球缓缓滚进球洞。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="48_g3_galleriessquare_n",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1210_1#1$1",duration=1.5)]
[Delay(time=4.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="bg_offce",screenadapt="coverall")]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1210_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_gen_transmissionget")]
[Delay(time=0.5)]
[name="马特奥"]如何，事情办妥了吗？
[name="马特奥"]好，连撤退的时机都掌握得很精准，来多索雷斯这么久，我头一次觉得你们把事情办得很漂亮。
[charslot(slot="m",name="avg_npc_1210_1#8$1")]
[name="马特奥"]那四个人？
[charslot(slot="m",name="avg_npc_1210_1#1$1")]
[name="马特奥"]不用担心，那个小个子不是被你们伤得很重吗？
[charslot(slot="m",name="avg_npc_1210_1#3$1")]
[name="马特奥"]整个社区现在估计都热血上头，他们拦不住的。
[name="马特奥"]赶紧回来，还有更大的事情要做。这件事办妥了，你们和我就都稳当了。
[charslot(slot="m",name="avg_npc_1210_1#7$1")]
[name="马特奥"]什么一半人不一半人的，我们这次是全数押上，兴废在此一举，都给我精神一点。
[name="马特奥"]对，所有人都撤回到艺术馆，部署好后随时待命。
[name="马特奥"]越多越好，成本和我们的收益相比根本不值一提。
[charslot(slot="m",name="avg_npc_1210_1#

... (全文18714字符)
```

### level_act32side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g5_galleries",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_1210_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1)]
[charslot(slot = "r", name = "avg_npc_1271_1#1$1", posfrom="200,0", posto="0,0", duration=1, isblock=true)]
[charslot(slot = "r", focus="r")]
[name="带队的军官"]报告上尉，开幕式的观众已经全都被我们控制住，雷内尔也已经被我们绑在阳台上了。
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", focus="l")]
[name="马特奥"]好，接应都就位了吗？
[charslot(slot = "r", focus="r")]
[name="带队的军官"]我们安排的十五辆卡车全都停在艺术馆的围墙外面了。
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", focus="l")]
[name="马特奥"]接下来要干什么，不用我再说了吧。
[charslot(slot = "r", focus="r")]
[name="带队的军官"]是！
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", focus="l")]
[name="马特奥"]记得警告那些大老粗，把艺术品搬上车的时候别弄坏了。
[charslot(slot = "l", name = "avg_npc_1210_1#7$1", focus="l")]
[name="马特奥"]要是谁敢弄坏一件东西，我就断掉他的一根手指。
[charslot(slot = "r", focus="r")]
[name="带队的军官"]明白。
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", focus="l")]
[name="马特奥"]哦，还有，记得收缴那些老爷们的终端。
[charslot(slot = "r", focus="r")]
[name="带队的军官"]那他们身上的财物，我们是不是也......
[charslot(slot = "l", name = "avg_npc_1210_1#9$1", focus="l")]
[name="马特奥"]哼，你倒是很懂啊。
[charslot(slot = "l", name = "avg_npc_1210_1#9$1", focus="l")]
[name="马特奥"]对人怎么样我不管，但对那些艺术品，一定记得轻拿轻放。
[name="马特奥"]走吧，我还得去会会雷内尔先生。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g10_deluxeroom",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1211_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", posfrom="-200,0", posto="0,0", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", focus="l")]
[name="马特奥"]天亮了，日出好看吗？
[charslot(slot = "l", name = "avg_npc_1210_1#9$1", focus="l")]
[name="马特奥"]不对，按照你们这种文化人的调调，我该问你，“美吗”？
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", focus="r")]
[name="雷内尔"]......
[charslot(slot = "l", name = "avg_npc_1210_1#1$1", focus="l")]
[name="马特奥"]打算沉默了？别以为保持沉默就能保你平安。
[name="马特奥"]不过话又说回来，也确实没什么需要你说的。你只要在这里老老实实坐着，扮演好恐怖袭击受害人就够了。
[charslot(slot = "r", name = "avg_npc_1211_1#10$1", focus="r")]
[name="雷内尔"]——你打算让我当恐怖袭击受害人？
[charslot(slot = "l", name = "avg_npc_1210_1#9$1", focus="l")]
[name="马特奥"]你看，这不是开口了嘛。
[charslot(slot = "r", name = "avg_npc_1211_1#2$1", focus="r")]
[name="雷内尔"]抱歉，我的错。我以为你看穿了什么，但我又想了想，不对，只是个利欲熏心的傻瓜炮制的巧合而已。
[charslot(slot = "l", name = "avg_npc_1210_1#9$1", focus="l")]
[name="马特奥"]瞧瞧你，刚刚还装得大义凛然的，现在就开始撒脾气了。
[charslot(slot = "r", name = "avg_npc_1211_1#9$1", focus="r")]
[name="雷内尔"]不，我对这个巧合毫无怨言，因为我发现，它只会为我最终的创作增光添彩——
[name="雷内尔"]当然，因为这是个巧合，而非你有意为之，所以我只会感谢命运，而不是你，上尉。
[charslot(slot = "l", name = "avg_npc_1210_1#10$1", focus="l")]
[name="马特奥"]很好，你还是闭嘴吧。
[dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="run")]
[StopSound(channel="run", fadetime=1)]
[charslot(slot = "m", name = "avg_npc_1271_1#1$1", posfrom="200,0", posto="0,0", duration=1, isblock=true)]
[name="带队的军官"]上尉，上尉！
[charslot(slot = "m", name = "avg_npc_1210_1#7$1")]
[name="马特奥"]怎么了？有人闹起来了？
[charslot(slot = "m", name = "avg_npc_1271_1#1$1")]
[name="带队的军官"]不，其实......
[name="带队的军官"]我们还是到房间里说吧。
[dialog]
[StopSound(channel="a", fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g2_galleriessquare",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot = "m", name = "avg_npc_1212_1#5$1")]
[name="特克诺"]老爹，难道我们记错日期了？
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]不可能。你看广场上的样子，刚才还有很多人在这里。肯定是发生什么事了。
[charslot(slot = "m", name = "avg_npc_1212_1#5$1")]
[name="特克诺"]有人看见了我们，给雷内尔报了信，他就跑回艺术馆里面去了？
[charslot(slot = "m", name = "avg_4123_ela_1#1$1")]
[name="艾拉"]这不是雷内尔的风格。假如他真的知道你们要来，他也许会暴怒，也许会兴奋，但绝对不会像你说的那样一躲了之。
[charslot(slot = "m", name = "avg_npc_1212_1#8$1")]
[name="特克诺"]那这......
[dialog]
[charslot]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_282_catap_1#11$1")]
[name="空爆"]终端？我的？
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1)]
[charslot(slot = "m", posfrom="0,0", posto="200,0", duration=1, isblock=true)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[CharacterCutin(widgetID="1", name="avg_486_espumo_1#7", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[charslot(slot = "m", name = "avg_282_catap_1#11$1")]
[name="空爆"]喂？埃内斯托？
[charslot(slot = "m", focus="n")]
[CharacterCutin(widgetID="1", name="avg_486_espumo_1#7", style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=-300, width=200, block=true)]
[name="龙舌兰"]是我。
[charslot(slot = "m", name = "avg_282_catap_1#10$1")]
[name="空爆"]怎么样，你的私事有进展了吗？
[charslot(slot = "m", focus="n")]
[name="龙舌兰"]阿莱塔，通知街头艺术社区的人，至少在今天，别靠近艺术馆。
[charslot(slot = "m", name = "avg_282_catap_1#5$1")]
[name="空爆"]啊？为什么？
[charslot(slot = "m", focus="n")]
[name="龙舌兰"]艺术馆里面铺设了大量源石爆炸物，随时可能爆炸。
[charslot(slot = "m", name = "avg_282_catap_1#5$1")]
[multiline(name="空爆")]源石爆炸物？
[charslot(slot = "m", name = "avg_282_catap_1#1$1")]
[multiline(name="空爆",end=true)]这......啊哈哈......
[charslot(slot = "m", focus="n")]
[CharacterCutin(widgetID="1", name="avg_486_espumo_1#3", style="cutin", fadestyle= "horiz_expand_center", fadetime=0, offsetx=-300, width=200, blo

... (全文21237字符)
```

### level_act32side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g2_galleriessquare",screenadapt="coverall")]
[playMusic(key="$formal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[charslot(slot = "m", name = "avg_4123_ela_1#1$1", duration=0.5, isblock=true)]
[name="艾拉"]导火索，情况如何？
[charslot(slot = "m", focus="n")]
[name="导火索"]已净空。
[name="导火索"]守军相当懈怠，对我们的突袭毫无防备，我们也没给他们时间向上通报。
[charslot(slot = "m", name = "avg_4123_ela_1#8$1")]
[name="艾拉"]做得好。
[dialog]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_4123_ela_1#1$1")]
[name="艾拉"]是时候开始突袭了。
[name="艾拉"]各位，行动务必要迅速，不要拖泥带水，不要给守军反应的时间。
[charslot(slot = "m", name = "avg_4123_ela_1#7$1")]
[name="艾拉"]我们上。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[PlaySound(key="$d_avg_explosion_stone", volume=0.3)]
[Background(image="48_g5_galleries",screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_npc_1272_1#1$1", posfrom="200,0", posto="0,0", duration=1.5)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1272_1#1$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[charslot(slot = "r", name = "avg_npc_1272_1#1$1", focus="r")]
[name="胆怯的军人"]刚刚外面是不是有什么响动？爆炸？
[charslot(slot = "l", name = "avg_npc_1272_1#1$1", focus="l")]
[name="懈怠的军人"]好像是。
[charslot(slot = "r", name = "avg_npc_1272_1#1$1", focus="r")]
[name="胆怯的军人"]该不会是那群疯子真的要闯进来吧......
[charslot(slot = "l", name = "avg_npc_1272_1#1$1", focus="l")]
[name="懈怠的军人"]闯进来干嘛？营救雷内尔？
[dialog]
[charslot(slot = "l", posfrom="0,0", posto="-20,0", duration=0.2, isblock=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_glass_break", volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1272_1#1$1", focus="l")]
[name="懈怠的军人"]别胡思乱想了，接好，这个好像是炎国的瓷器，一碰就碎，小心点。
[charslot(slot = "r", name = "avg_npc_1272_1#1$1", focus="r")]
[name="胆怯的军人"]你刚刚打破玻璃罩子的时候差点连瓷器一起打碎了，还说我......
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "l", posfrom="-20,0", posto="0,-20", duration=1)]
[charslot(slot = "r", posfrom="0,0", posto="0,-20", duration=1, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "l", posfrom="0,-20", posto="0,0", duration=0.5)]
[charslot(slot = "r", posfrom="0,-20", posto="0,0", duration=0.5, isblock=true)]
[PlaySound(key="$d_avg_axeimp", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_fastener", volume=0.5)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_fastener", volume=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1272_1#1$1", focus="r")]
[name="胆怯的军人"]......说起来，刚刚队长打碎了个瓶子，说是上楼去找上尉报告，怎么到现在还没回来？
[charslot(slot = "l", name = "avg_npc_1272_1#1$1", focus="l")]
[name="懈怠的军人"]大概就和第一次来的时候一样，在爬楼梯吧。
[name="懈怠的军人"]要不就是跟上尉商量给这些东西找下家的事，说不定两个人现在连自己腰包里能装多少钱都聊好了——
[dialog]
[charslot]
[stopmusic(fadetime=1)]
[CameraShake(duration=2, xstrength=20,ystrength=20, vibrato=90, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$glass", volume=1)]
[delay(time=1)]
[name="双月"]手雷已掷出！
[dialog]
[PlaySound(key="$d_avg_explosion_stone", volume=1)]
[delay(time=0.5)]
[PlayMusic(intro="$mutate_intro", key="$mutate_loop", volume=0.6)]
[CameraShake(duration=2.5, xstrength=40,ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Background(image="48_g6_galleries_b",screenadapt="coverall")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=2, block=true)]
[delay(time=1)]
[name="双月"]已确认房间内没有人质！优先压制守军！
[dialog]
[PlaySound(key="$d_gen_soldiersrun", volume=1)]
[delay(time=0.5)]
[PlaySound(key="$pistol", volume=1)]
[delay(time=0.5)]
[PlaySound(key="$pistol", volume=1)]
[charslot(slot = "m", name = "avg_npc_1272_1#1$1")]
[name="懈怠的军人"]见鬼，怎么是你们？
[dialog]
[charslot]
[PlaySound(key="$d_avg_arrow_rain", volume=1)]
[PlaySound(key="$d_avg_frdrgntkln", volume=0.6)]
[delay(time=1)]
[PlaySound(key="$d_avg_frdrgntkln", volume=0.4)]
[charslot(slot = "l", name = "avg_npc_1272_1#1$1")]
[charslot(slot = "r", name = "avg_npc_1272_1#1$1")]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1, loop=true, channel="w")]
[StopSound(channel="w", fadetime=1.5)]
[charslot(slot = "r", posfrom="0,0", posto="150,0", duration=1.5, isblock=true)]
[charslot(slot = "l", name = "avg_npc_1272_1#1$1", focus="l")]
[name="懈怠的军人"]别怕，他们的连发铳威力不行！
[charslot(slot = "r", name = "avg_npc_1272_1#1$1", focus="r")]
[name="胆怯的军人"]我......我不是怕，我是想找个安全的地方呼叫增援——
[dialog]
[charslot]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_frdrgntk", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_ldrdhtgrnd", volume=1)]
[PlaySound(key="$transmission", volume=1)]
[Delay(time=1)]
[charslot]
[PlaySound(key="$d_avg_bulltdrpsnw", volume=1)]
[charslot(slot = "m", name = "avg_4123_ela_1#6$1")]
[name="艾拉"]想都别想。
[charslot(slot = "m", name = "avg_npc_1272_1#1$1")]
[name="懈怠的军人"]啧，准头倒不错。
[dialog]
[PlaySound(key="$d_avg_bowstring", volume=1)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_arrowshot", volume=1)]
[Delay(time=1)]
[name="懈怠的军人"]可惜你们那破弹药威力太弱，中一下还不如被源石虫刺一下——
[dialog]
[PlaySound(key="$d_avg_twohandedblunt", volume=1)]
[Delay(time=0.5)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraS

... (全文32244字符)
```

### level_act32side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g10_deluxeroom",screenadapt="coverall")]
[PlayMusic(intro="$mutate_intro", key="$mutate_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="暴躁的军人"]报告！我们把人押上来了！
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1273_1#1$1", posfrom="200,0", posto="0,0", duration=1.5)]
[charslot(slot = "m", name = "avg_npc_1214_1#1$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot]
[charslot(slot = "m", name = "avg_npc_1210_1#10$1")]
[name="马特奥"]......居然真的是这老家伙。
[charslot(slot = "m", name = "avg_npc_1273_1#1$1")]
[name="暴躁的军人"]他抵抗得很厉害，打伤了一个人，但我们也没客气，让他出了点血。
[charslot(slot = "m", name = "avg_npc_1210_1#1$1")]
[name="马特奥"]好了，你们干得不错。下去接着干活吧。
[dialog]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1210_1#1$1")]
[name="马特奥"]怎么了？
[charslot(slot = "m", name = "avg_npc_1273_1#1$1")]
[name="暴躁的军人"]上尉，这老家伙都已经上到六楼了，说明他们的人一定不少，我们可能......没法......
[charslot(slot = "m", name = "avg_npc_1210_1#5$1")]
[name="马特奥"]没法？没法什么？告诉你们，如果这一票干不成，我们全都要万劫不复！
[charslot(slot = "m", name = "avg_npc_1273_1#1$1")]
[name="暴躁的军人"]还有就是，这个老家伙到底是在做什么，墙里面都是线......
[charslot(slot = "m", name = "avg_npc_1210_1#7$1")]
[name="马特奥"]不要多问，做好你自己的事情。
[charslot(slot = "m", name = "avg_npc_1273_1#1$1")]
[name="暴躁的军人"]是......
[charslot(slot = "m", name = "avg_npc_1210_1#1$1")]
[name="马特奥"]说说吧，迪亚兹，是什么风把你和你的手下吹到艺术馆来的？
[charslot(slot = "m", name = "avg_npc_1214_1#7$1")]
[name="迪亚兹"]别明知故问了，马特奥。
[name="迪亚兹"]人质已经被我们救了出去，你的手下也溃不成军，现在恐怕整个多索雷斯都知道这场恐怖袭击是你自导自演的了。
[name="迪亚兹"]一句话，你已经完了。
[charslot(slot = "m", name = "avg_npc_1210_1#7$1")]
[name="马特奥"]别想骗我。
[charslot(slot = "m", name = "avg_npc_1214_1#9$1")]
[name="迪亚兹"]你该不会觉得自己还能把那些艺术品运出去换钱吧？
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]告诉你，你安排的那些卡车才装了不到一辆，看守和司机就都被我们控制了。你的发财梦该醒了。
[charslot(slot = "m", name = "avg_npc_1210_1#5$1")]
[name="马特奥"]你说什么？！
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]不信可以去问问你刚刚派下楼的那些人。炸弹的事我们也已经知道了，趁爆炸发生之前赶紧收手吧。
[charslot]
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", focus="n")]
[charslot(slot = "l", name = "avg_npc_1210_1#7$1", focus="l")]
[name="马特奥"]炸弹......炸弹......雷内尔，你那个炸弹到底什么时候爆炸？把起爆时间告诉我。
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", focus="r")]
[name="雷内尔"]......
[charslot(slot = "l", name = "avg_npc_1210_1#7$1", focus="l")]
[name="马特奥"]我让你告诉我炸弹起爆的时间，雷内尔。
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", focus="r")]
[name="雷内尔"]......
[charslot(slot = "l", name = "avg_npc_1210_1#5$1", focus="l")]
[name="马特奥"]说话！你是哑巴了吗？！
[dialog]
[charslot(slot = "l", posfrom="0,0", posto="100,0", duration=0.5)]
[delay(time=0.2)]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(slot = "r", posfrom="0,0", posto="-30,10", duration=0.3, isblock=true)]
[charslot(slot = "l", focus="l")]
[name="马特奥"]你要是等不及被炸死，我也可以现在成全你——
[charslot]
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]十点钟。
[name="迪亚兹"]收敛点，马特奥，想想之后该怎么办，起爆时间已经很近了。
[charslot(slot = "m", name = "avg_npc_1210_1#7$1")]
[name="马特奥"]......
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]如果你还保有一点理性，就把我手上的束缚解开。
[name="迪亚兹"]楼里总共有四个炸弹节点，其中三个已经在我们的控制之下，马上就拆除成功，只差雷内尔办公室通风井里的那个了。
[charslot(slot = "m", name = "avg_npc_1210_1#5$1")]
[name="马特奥"]老东西，要是让我知道你在说谎，你就完了！
[dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(duration=1, isblock=true)]
上尉狠狠地骂了一句，抓起终端，大步走到阳台靠近办公室的阴影里去了。
老消防员抬头望向天空，雷内尔则找了个习惯的姿势，舒舒服服地靠在一幅巨大的画作旁边。
阳台上陷入一阵尴尬的沉默。
[dialog]
[charslot(slot = "m", name = "avg_npc_1211_1#10$1", duration=0.5, isblock=true)]
[name="雷内尔"]迪亚兹。
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]原来你还能说话啊。
[charslot(slot = "m", name = "avg_npc_1211_1#10$1")]
[name="雷内尔"]你们怎么会连炸弹的起爆时间都知道？哪个人给你们透露的消息？
[charslot(slot = "m", name = "avg_npc_1214_1#10$1")]
[name="迪亚兹"]怎么？没法用爆炸来让那些投资人的钱变成废纸了，你很沮丧？
[charslot(slot = "m", name = "avg_npc_1211_1#2$1")]
[name="雷内尔"]不过也无所谓，通风井里还有一个起爆节点。
[charslot(slot = "m", name = "avg_npc_1211_1#8$1")]
[name="雷内尔"]虽然不足以毁了楼下的艺术品，但要让艺术馆变成废楼，投资人的钱打水漂，也足够了。
[charslot(slot = "m", name = "avg_npc_1214_1#7$1")]
[name="迪亚兹"]要结果我们这些在阳台上的人的性命也足够了。
[charslot(slot = "m", name = "avg_npc_1211_1#10$1")]
[name="雷内尔"]和我即将达成的目标相比，那很重要吗？
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g7_galleriesstaircase",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="run")]
[StopSound(channel="run", fadetime=1)]
[charslot(slot = "m", name = "avg_4123_ela_1#5$1", duration=0.5, isblock=true)]
[name="艾拉"]迪亚兹！
[dialog]
[charslot]
尽管已经做好了心理准备，面对眼前的景象，艾拉仍然觉得心里一凉。
楼梯间侧面被凿出了一个大洞，从中探出的金属接头有不少都掉在地上，还有的一看就被倒在地上的人压过。
而楼梯间里更醒目的则是地上的血迹。
一条已经开始发黑的血迹从洞口起始，一路朝楼上延伸过去。
[dialog]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse", volume=0.4, loop=true, channel="b")]
[delay(time=1)]
[StopSound(channel="b", fadetime=2)]
[delay(time=1)]
艾拉还来不及拿起终端报告情况，脚下突然传来一阵震动。
[dialog]
[CameraShake(duration=4, xstrength=20, ystrength=20, vibrato=90, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse", volume=0.6, loop=true, channel="b")]
[delay(time=2)]
[StopSound(channel="b", fadetime=2)]
[charslot(slot = "m", name = "avg_4123_ela_1#6$1")]
[name="艾拉"]......该死！
[dialog]
[PlaySound(key="$d_avg_explosion_stone")]
[PlaySound(key="$d_avg_collapse", volume=1)]
[delay(time=0.5)]
[Effect(name="$e_sandfall_01",layer = 2)]
[CameraShake(duration=4, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, b

... (全文27427字符)
```

### level_act32side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="48_g10_deluxeroom",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n", volume=0.4)]
[delay(time=0.1)]
[PlaySound(key="$d_gen_explo_n", volume=0.5)]
[delay(time=0.1)]
[PlaySound(key="$d_gen_explo_n", volume=0.6)]
[delay(time=0.1)]
[PlaySound(key="$d_gen_explo_n", volume=0.8)]
[delay(time=1)]
[PlayMusic(intro="$mutate_intro", key="$mutate_loop", volume=0.6)]
[name="马特奥"]哈哈、哈哈哈哈！
[name="马特奥"]你们干得漂亮，然后呢？又能怎么样？只能一个不剩地死在这儿！
[dialog]
艾拉无视像垂死的野兽一样躺在地上嗥叫个不停的马特奥，快步走到阳台边缘。
[dialog]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "m", name = "avg_4123_ela_1#1$1", duration=1, isblock=true)]
[charslot(slot = "m", name = "avg_4123_ela_1#1$1")]
[name="艾拉"]我们得稍微做一些超出挂绳使用守则的事了。我需要一个人和我各带一个人质速降，破窗进入较低楼层。
[charslot(slot = "m", name = "char_457_blitz_1#4")]
[name="闪击"]糟了，我们从罗德岛出发的时候可没带这个。
[charslot(slot = "m", name = "avg_4123_ela_1#6$1")]
[name="艾拉"]真的？！
[charslot(slot = "m", name = "char_457_blitz_1#5")]
[name="闪击"]别急，开个玩笑，只是有更好的方法。
[charslot(slot = "m", name = "avg_4123_ela_1#5$1")]
[name="艾拉"]更好的？
[charslot(slot = "m", name = "char_457_blitz_1#6")]
[name="闪击"]穿上这个。这是我们拜托罗德岛的可露希尔小姐制作的多功能喷气滑翔背包。
[charslot(slot = "m", name = "avg_4123_ela_1#1$1")]
[name="艾拉"]看起来像飞机上的救生衣。
[charslot(slot = "m", name = "char_457_blitz_1#6")]
[name="闪击"]外形上就是按照那东西做的，至于用途上嘛，感谢可露希尔小姐，既可以展开滑翔翼滑翔，也可以只用喷气功能协助降落。
[charslot(slot = "m", name = "avg_4123_ela_1#10$1")]
[name="艾拉"]你确定这东西可靠？
[charslot(slot = "m", name = "char_457_blitz_1#6")]
[name="闪击"]不然我们是怎么从六楼进入这栋建筑的？
[dialog]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse", volume=0.4, loop=true, channel="b")]
[delay(time=1)]
[StopSound(channel="b", fadetime=2)]
[delay(time=1)]
[charslot(slot = "m", name = "char_457_blitz_1#6")]
[name="闪击"]总之，穿上它，拉一下下面的手柄，别动上面那个，这东西就会把你安全送到地上。这是你的，艾拉。
[charslot(slot = "m", name = "avg_4123_ela_1#8$1")]
[name="艾拉"]帮大忙了。
[dialog]
[PlaySound(key="$d_avg_armour", volume=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "char_457_blitz_1#6")]
[name="闪击"]迪亚兹先生，这是你的。
[charslot(slot = "m", focus="n")]
老消防员利索地把背包套在身上。
[charslot(slot = "m", name = "char_457_blitz_1#4")]
[name="闪击"]至于这位雷内尔先生......
[charslot]
闪击朝艾拉递了个疑问的眼神，艾拉耸了耸肩。
[charslot(slot = "m", name = "avg_4123_ela_1#1$1")]
[name="艾拉"]我答应过别人，如果有机会，会把这家伙救下来。
[charslot(slot = "m", name = "char_457_blitz_1#4")]
[name="闪击"]那么这个是你的。
[charslot]
雷内尔接过背包，却不穿在身上，只是对着背包出神。
[charslot(slot = "m", name = "char_457_blitz_1#4")]
[name="闪击"]先生，我建议你赶紧把它穿好，开玩笑可以，拿自己的生命开玩笑就过头了。
[charslot(slot = "m", name = "avg_npc_1211_1#8$1")]
[name="雷内尔"]正好，我记得不久以前你们的艾拉小姐说过，她不能保护一个拿自己生命开玩笑的人。
[name="雷内尔"]当时我说她误会了，因为我还有事要做。
[name="雷内尔"]现在......我的事总算是尘埃落定，所以......
[charslot(slot = "m", name = "avg_npc_1211_1#9$1")]
[name="雷内尔"]拿命开个玩笑又何妨？
[charslot(slot = "m", name = "avg_4123_ela_1#1$1")]
[name="艾拉"]别傻了，快把它穿好。
[charslot]
[PlaySound(key="$d_avg_armour", volume=1)]
雷内尔耸了耸肩，把背包套在自己身上。
[charslot(slot = "m", name = "char_457_blitz_1#6")]
[name="闪击"]我来打头阵，请没用过的各位看清楚了。
[dialog]
[charslot]
[PlaySound(key="$d_avg_explosion", volume=0.4)]
[CameraShake(duration=4, xstrength=20, ystrength=20, vibrato=90, randomness=50, fadeout=true, block=false)]
[PlaySound(key="$d_avg_collapse", volume=0.6, loop=true, channel="b")]
[delay(time=2)]
[StopSound(channel="b", fadetime=2)]
雷内尔向后退了两步，看着闪击翻过阳台边缘，在空中飘飘摇摇地向下方落去。
然后是迪亚兹。那个口音和导火索有几分类似，但身形更高大一些的男人拍了拍迪亚兹的肩膀，帮他拉下了手柄。
阳台上的人们一个接一个地离开，直到站在阳台上的只剩雷内尔和艾拉。
雷内尔还有些迟疑，艾拉启动了两人的喷气背包，拉着雷内尔向阳台外纵身一跃。
[dialog]
[PlaySound(key="$d_avg_steamburst", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[delay(time=0.5)]
[stopmusic(fadetime=1)]
[PlaySound(key="$d_avg_explosion_stone")]
[PlaySound(key="$d_avg_collapse", volume=1)]
[delay(time=0.5)]
[CameraShake(duration=4, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[name="艾拉"]等等，雷内尔，你做什么？！
[name="雷内尔"]我都说了，用命开个玩笑又何妨？
雷内尔脱下了身上的背包，直直地向下落去。
耳边传来艾拉的怒吼，他的腿似乎有一瞬间被艾拉抓在手里，但重力很快将他扯向地面。
[dialog]
[PlaySound(key="$d_avg_snowstormflp", volume=1, loop=true, channel="s")]
雷内尔不知道自己会落到哪里，地面还是游泳池，但反正这次他身上没有安全绳，也没有背包。
他试图品味此刻的失重感与蹦极究竟有何区别，他是否在战栗，而那些战栗又是否与自己制造的这场盛大的毁灭相衬——
在他得出结论之前，他忽然觉得手里钻进了一枚圆圆的东西，背上被什么东西硌得生疼。
[SoundVolume(volume=0.4, channel="a",fadetime=2)]
顶着强风强行睁开双眼，雷内尔隐约看到源石技艺的闪光，同时感受到一些小而硬的圆球抵在自己身下，竭力对抗重力。
[name="雷内尔"]......高尔夫球？
不知是突然迸发了求生欲，或者只是被高尔夫球硌得难受，总之，雷内尔选择了接受。
他手里的高尔夫球迸发出类似的光芒，引得附近更多的高尔夫球像磁铁一样吸到他的背上，一同延缓他下坠的速度——
[dialog]
[StopSound(channel="s", fadetime=2)]
[PlaySound(key="$d_avg_jump_water", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_underwtr", volume=1, loop=true, channel="c")]
[delay(time=2)]
[charslot]
[Background(image="48_g12_privatebeach",screenadapt="coverall")]
[StopSound(channel="c", fadetime=2)]
[Delay(time=1)]
[PlaySound(key="$d_avg_sea", volume=0.3, loop=true, channel="a")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
落入游泳池的雷内尔短暂地浮沉了几次，最终还是浮在了水面上——
更准确地说，是一张由密密麻麻的高尔夫球组成的漂浮垫浮在了水面上，而雷内尔躺在上面。
他在那张高尔夫球漂浮垫上稳稳当当地站了起来，甚至只跨一步就上了岸。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_npc_1211_1#4$1", posfrom="-100,0", posto="0,0", duration=1, isblock=true)]
[name="雷内尔"]米沃什，米沃什！你在哪里？我知道你在附近！
[dialog]
[PlaySound(key="$rungeneral", volume=1, loop=true, channel="run")]
[StopSound(channel="run", fadetime=1)]
[charslot(slot = "l", name = "avg_4123_ela_1#10$1", posfrom="-200,0", posto="0,0", duration=1, isblock=true)]
[Delay(time=0.5)]
[ch

... (全文19154字符)
```

### level_act32side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_labcorridor",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[playsound(key="$d_avg_sldrsldng",channel="1")]
[charslot(slot="l",name="avg_4124_iana_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4123_ela_1#1$1",duration=1.5)]
[Delay(time=2)]
[stopsound(fadetime=1,channel="1")]
[playsound(key="$d_gen_transmissionget",channel="1")]
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]我们已进入磁山二号，重复一遍，我们已进入磁山二号。
[name="艾拉"]医生，你和导火索那边情况如何？
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="none")]
[name="医生"]已确认外围安全。
[name="医生"]考虑到磁山二号实验室的特殊性，我建议从现在开始会合，一起行动。
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]好。
[name="艾拉"]双月，报告一下无人机侦察结果。
[charslot(slot="l",name="avg_4124_iana_1#1$1",focus="l")]
[name="双月"]和我们上次撤离时几乎没有差别，仪表读数相差无几，设施内部也没有发现其他人活动。
[charslot(slot="l",name="avg_4124_iana_1#7$1",focus="l")]
[name="双月"]看来我们上次离开之后，磁山二号的封锁做得很彻底。
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]也就是说，根本没人。
[name="艾拉"]我们的任务是来寻找失踪的灰烬小队，没人算不上好消息。
[charslot(slot="r",name="avg_4123_ela_1#1$1",focus="r")]
[name="艾拉"]注意警戒，会合后我们直接往列维的主实验室原址前进。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_caveentrance",screenadapt="coverall")]
[charslot]
[Delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_4124_iana_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4123_ela_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_4123_ela_1#7$1",focus="r")]
[name="艾拉"]我们到了。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="l",name="avg_4126_fuze_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_4125_rdoc_1#1$1",focus="r")]
[name="医生"]你确定？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_4123_ela_1#1$1",focus="m")]
[name="艾拉"]没错，按照地图，这里就是列维的主实验室应该在的地方。
[charslot(slot="m",name="avg_4124_iana_1#7$1",focus="m")]
[name="双月"]当时我们只比科恩他们晚了一步，先是感到一阵震动，然后......
[name="双月"]不知道是列维那个疯子干的还是仪器本身出了问题，总之，整个主实验室凭空消失了。
[Dialog]
[charslot(slot="m",name="avg_4125_rdoc_1#13$1",focus="m")]
[name="医生"]确定是“凭空消失”？
[Dialog]
[charslot(slot="m",name="avg_4124_iana_1#1$1",focus="m")]
[name="双月"]结合当时的情况和专家的意见，这是最合理的解释。
[Dialog]
[charslot(slot="m",name="avg_4125_rdoc_1#13$1",focus="m")]
[name="医生"]但这太不现实了。
[charslot(slot="m",name="avg_4126_fuze_1#1$1",focus="m")]
[name="导火索"]没有哪种现实中的爆炸能完全抹除一座实验室的所有痕迹，留下巨大的空洞，外面的人却只觉得震了两下。
[Dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[playsound(key="$smallearthquake")]
[bgeffect(name="$eb_dust_01",layer=1)]
[CameraShake(duration=-1, xstrength=5, ystrength=10, vibrato=15, randomness=70, fadeout=false, block=false)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_4125_rdoc_1#6$1",focus="m")]
[name="医生"]地震？还是你们说的......？
[charslot(slot="m",name="avg_4124_iana_1#3$1",focus="m")]
[name="双月"]不，不是地震！
[charslot(slot="m",name="avg_4123_ela_1#4$1",focus="m")]
[name="艾拉"]震动极有可能与失踪事件相关！
[name="艾拉"]各位，原地寻找掩体，等待震动平息！
[Dialog]
[playsound(key="$a_bat_buildingshaking_2")]
[CameraShake(duration=4, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[bgeffect]
[charslot]
[Blocker(a=1, r=1, g=1, b=1, fadetime=2, block=true)]
[Background(image="48_g7_galleriesstaircase",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$d_gen_soldiersrun")]
[charslot(slot="l",name="avg_npc_1271_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1272_1#1$1",duration=1.5)]
[Delay(time=3.5)]
[charslot(slot="r",focus="r")]
[name="痛苦的军人"]队长，请问艺术馆到底有多少层？我腿都要走折了。
[charslot(slot="l",focus="l")]
[name="带队的军官"]呼......反正往上爬，爬到顶楼就对了，雷内尔就在那儿。
[charslot(slot="r",focus="r")]
[name="痛苦的军人"]我们就不能坐电梯吗？为什么要在这里一圈一圈地爬楼梯？
[charslot(slot="l",focus="l")]
[name="带队的军官"]你以为我不想吗？
[name="带队的军官"]出发前我们摸清了这里的安保布置。
[name="带队的军官"]那家伙狡猾得很，建筑内只有这部楼梯和一部他自己用的电梯可以通到顶楼，每层电梯口都有人把守。
[name="带队的军官"]楼梯是防守最为薄弱的一环，我们只能从这里突破。
[charslot(slot="r",focus="r")]
[name="痛苦的军人"]他不就是个来这儿捞钱的卡西米尔人吗？身后连个撑腰的人都没有，不过是强迫他签份转让协议，我们何苦做得这么谨慎？
[charslot(slot="l",focus="l")]
[name="带队的军官"]呵，这个地方有钱撑腰还不够吗？
[name="带队的军官"]楼下那个，快走两步，别东张西望的了！
[charslot(slot="l",focus="none")]
[name="懈怠的军人"]队长，真走不动了......我宁愿坐电梯去和他的保安拼刀拼弩。
[charslot(slot="l",focus="l")]
[name="带队的军官"]嘘......
[charslot(slot="l",focus="none")]
[name="懈怠的军人"]队长......？
[charslot(slot="l",focus="l")]
[name="带队的军官"]（小声）我们马上就到那家伙办公室了！脚步放轻......
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_ltroom",screenadapt="coverall")]
[charslot]
[Delay(time=2.5)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1211_1#8$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[playsound(key="$doorknockquite")]
[Delay(time=1.5)]
[charslot]
[playsound(key="$dooropenquite")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1213_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_1211_1#10$1",focus="m")]
[name="雷内尔"]信？米沃什，我记得前几天跟你说过了，寄给我的信你直接看就好，不必来问我。
[charslot(slot="m",name="avg_npc_1213_1#1$1",focus="m")]
[name="米沃什"]可这上面写的是“望您亲启”哦，雷内尔。
[charslot(slot="m",name="avg_npc_1211_1#10$1",focus="m")]
[name="雷内尔"]信是从哪寄来的？
[charslot(slot="m",name="avg_npc_1213_1#1$1",focus="m")]
[name="米沃什"]这一封是从卡西米尔......好像是你叔叔的。
[charslot(slot="m",name="avg_npc_1211_1#2$1",focus="m")]
[name="雷内尔"]哦，知道了，是来要遗产的。
[charslot(slot="m",name="avg_npc_1213_1#1$1",focus="m")]
[n

... (全文37908字符)
```

### level_act32side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="48_g3_galleriessquare_n",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$holiday_intro", key="$holiday_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)] 
[charslot(slot="l",name="avg_npc_021",duration=1.5)]
[charslot(slot="r",name="avg_npc_033",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_021",focus="l")]
[name="疲惫的观众"]（打哈欠）
[name="疲惫的观众"]雷内尔可真能折腾人，好好的艺术馆开幕式，非要放在大晚上举办，还说要一直开到天亮。
[charslot(slot="r",name="avg_npc_033",focus="r")]
[name="兴奋的观众"]我相信雷内尔一定能给我们看到不一样的东西，你不也一样吗？要不然干嘛熬这么晚？
[charslot(slot="l",name="avg_npc_021",focus="l")]
[name="疲惫的观众"]算了吧。本来想去看街头艺术社区的艺术狂欢节的，不知道为什么取消了，我只好来这儿了。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_223",focus="l")]
[charslot(slot="r",name="avg_npc_176",focus="l")]
[name="投资界新人"]雷内尔的噱头是真做足了。开幕式的具体安排对我们这样的高级合作伙伴都要保密......
[name="投资界新人"]哼，哗众取宠还是他行。
[charslot(slot="r",name="avg_npc_176",focus="r")]
[name="投资界前辈"]等你搞出的噱头能让全泰拉一大半的艺术投资人都愿意像跑到克里斯达尔艺术馆一样跑到我们堡垒山城的总部，那时候再在我耳边抱怨。
[charslot(slot="l",name="avg_npc_223",focus="l")]
[name="投资界新人"]是......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_492_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_493_1#1$1",focus="l")]
[name="窘迫的贵族"]宣传册上这个卡西米尔人......他的艺术沙龙真能让我的画卖出去吗......
[charslot(slot="r",name="avg_npc_493_1#1$1",focus="r")]
[name="傲慢的掮客"]这里可不是莱塔尼亚，一切全看你讲的故事够不够打动那些投资人。
[charslot(slot="l",name="avg_npc_492_1#1$1",focus="l")]
[name="窘迫的贵族"]......你不是说全交给你吗？
[charslot(slot="r",name="avg_npc_493_1#1$1",focus="r")]
[name="傲慢的掮客"]早跟你说了，染个头发，学点脏话，穿身破衣服，自称腐朽贵族制度的反叛者，好多人都吃这一套，可你又不干，那我能替你讲什么？
[name="傲慢的掮客"]最后再给你个温馨提示，虽然不如叛逆小子，但落魄贵族这套也有人喜欢。至于能不能打动投资人，就看你临场发挥了。
[Dialog]
[charslot]
[name="广播声"]请各位保持安静，我们的开幕式马上就要开始了。
[name="广播声"]重复一遍，请各位保持安静，我们的开幕式，马上就要开始——
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1211_1#10$1",duration=1.5)]
[Delay(time=2.5)]
雷内尔信步走上艺术馆前广场上搭设的演讲台。
他缓缓扫视了几次台下的人群，尤其是坐在靠近演讲台位置的人，确信该来的人全都来了，然后清了清嗓子。
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[name="雷内尔"]各位，早上好，中午好，晚上好——请自行对号入座，这取决于你们惯常的入睡时间。
[Dialog]
[playsound(key="$d_avg_applause")]
[Delay(time=5)]
[name="雷内尔"]感谢鼓掌的各位，也感谢没鼓掌的各位，你们毕竟牺牲了自己宝贵的睡眠时间，陪我一起观赏双日城这场伟大的日出。
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="none")]
[name="投资界新人"]哼。
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[name="雷内尔"]感谢你们的热情与期待。
[name="雷内尔"]感谢你们愿意与我一起创造历史，尽管只是一小段，在更久远的跨度下可能微不足道，但对各位来说，必定铭记终身。
[Dialog]
[playsound(key="$d_avg_applause")]
[Delay(time=5)]
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="none")]
[name="傲慢的掮客"]好大的口气。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="48_g1_dossolesstreet_n",screenadapt="coverall")]
[Delay(time=2)]
[playsound(key="$d_avg_crwddiscuss_outside",loop=true,channel="1",volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="社区居民"]天佑玻利瓦尔，天佑多索雷斯♪
[name="社区居民"]只知道掏钱的游客脑袋空空♪
[name="社区居民"]就像这座城市的未来♪
[name="社区歌手"]老兄，这个词该换了。你帮我伴奏，我给你创作点更应景的词。
[name="社区歌手"]天佑联合政府，天佑科瓦尔斯基♪
[name="社区歌手"]住在垃圾堆的富豪跟军头媾合♪
[name="社区歌手"]在那怪胎着床的夜晚♪
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopsound(channel="1",fadetime=1.5)]
[charslot]
[Image]
[Background(image="48_g3_galleriessquare_n",screenadapt="coverall")]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="雷内尔"]各位，欢迎来到多索雷斯，欢迎来到克里斯达尔艺术馆。
[name="雷内尔"]在进入正题之前，我希望先给各位介绍一个划时代的项目。
[name="雷内尔"]我相信，各位并非全都为了艺术馆或开幕式而来——“卡西米尔富二代硬凑起来的噱头罢了”，想必在座各位也有人是这么想的。
[name="雷内尔"]你们大概更关心一个能生钱的项目，所以我把它放在前面，满足你们的好奇心和贪欲。
[name="雷内尔"]在场的各位，请让我看到你们随身带着的终端，把它高高举起。
[Dialog]
[playsound(key="$d_avg_cheer_street")]
[Delay(time=2.5)]
[name="雷内尔"]看来各位不光自认为具有高雅的审美品味，还都赶上了时代的潮流。
[name="雷内尔"]便携终端，多么伟大的发明，让人摆脱消磨时光的罪恶感，带来城市各个角落的消息，把整座城市连接在一起。
[name="雷内尔"]而我愿意为这座未来的富矿添上一座以艺术为名的钻探平台，让其中涌出的金币和纸钞填满你们的腰包。
[name="雷内尔"]隆重为各位介绍这项突破性的发明，即将在城际网络上掀起浪潮的......
[name="雷内尔"]虚拟艺术藏品项目。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="48_g1_dossolesstreet_n",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="社区小贩"]哥们，我怎么没见过你？
[charslot(slot="m",name="avg_npc_201",focus="m")]
[name="狡猾的陌生人"]你怎么可能没见过我？我就住你家楼上！
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="社区小贩"]哦，你是那个......皮斯托？
[charslot(slot="m",name="avg_npc_201",focus="m")]
[name="狡猾的陌生人"]对对对。
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="社区小贩"]可你不是去治病了吗？
[charslot(slot="m",name="avg_npc_201",focus="m")]
[name="狡猾的陌生人"]我去治病怎么了，去治病雷内尔就有权进我们社区搞破坏吗？
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="社区小贩"]说得好！
[charslot(slot="m",name="avg_npc_201",focus="m")]
[name="狡猾的陌生人"]怎么样，等到了艺术馆，准不准备大干一场？
[charslot(slot="m",name="avg_npc_001",focus="m")]
[name="社区小贩"]当然要大干一场！
[charslot(slot="m",name="avg_npc_201",focus="m")]
[name="狡猾的陌生人"]那就对了！对这种人不能有一点同情心！
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image]
[Background(image="48_g3_galleriessquare_n",screenadapt="coverall")]
[Delay(time=2)]
[playMusic(intro="$tech_intro", key="$tech_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1211_1#9$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="none")]
[name="投资界新人"]虚拟艺术藏品？我们给你投资是要看这种东西吗？
[charslot(slot="m",name="avg_npc_1211_1#9$1",focus="m")]
[name="雷内尔"]啊，想想看，一部分艺术家以后不再和颜料、画笔打交道，他们在终端前为城际网络创造的作品同样能成为你们的投资对象。
[name="雷内尔"]如果我把艺术馆中收藏的某幅画作在城际网络上原样复制，诸位随时可以在终端上看到画作的每一个细节。
[name="雷内尔"]没人可以夺走或复制这幅画，你拥有处置这幅虚拟画作的全部权利，想卖，想毁，全由你自己决定——

... (全文14683字符)
```

### level_act32side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Background(image="bg_cellroomB",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$dooropenquite", volume=1)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", duration=0.5, isblock=true)]
[name="雷内尔"]我记得现在是午休时间，如果需要提审，你可能要晚点来——
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_486_espumo_1#7", duration=1.5, isblock=true)]
[charslot(slot = "l", focus="l")]
[name="龙舌兰"]我不是来提审你的。
[charslot(slot = "r", name = "avg_npc_1211_1#10$1", focus="r")]
[name="雷内尔"]你是......
[name="雷内尔"]哦，怎么，罗德岛也想踩着我的尸体分一杯羹吗？欢迎欢迎。
[charslot(slot = "l", name = "avg_486_espumo_1#7", focus="l")]
[name="龙舌兰"]我只是来替坎黛拉女士告知你多索雷斯对你的最终处理结果。
[name="龙舌兰"]依据多索雷斯市长办公室的判断，多索雷斯将不会审判你的罪行。
[charslot(slot = "r", name = "avg_npc_1211_1#10$1", focus="r")]
[name="雷内尔"]让我猜猜，把我交给联合政府？
[name="雷内尔"]虽然马特奥是个蠢货，但他毕竟是联合政府在多索雷斯的代表。
[charslot(slot = "r", name = "avg_npc_1211_1#9$1", focus="r")]
[name="雷内尔"]嗯......我三番五次地耍他玩，联合政府肯定等不及要把我挫骨扬灰。
[charslot(slot = "l", name = "avg_486_espumo_1#7", focus="l")]
[name="龙舌兰"]你对局势的判断很精准。联合政府确实想把你抓去拉乌尼达公审，就像他们对马特奥做的一样。
[charslot(slot = "r", name = "avg_npc_1211_1#2$1", focus="r")]
[name="雷内尔"]一场公审？很好，我很期待。
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]不，雷内尔先生。
[name="龙舌兰"]你将被送回卡西米尔。
[charslot(slot = "r", name = "avg_npc_1211_1#5$1", focus="r")]
[name="雷内尔"]......你再说一遍？
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]商业联合会向坎黛拉施加了压力，希望将你送回卡西米尔。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[charslot(slot = "r", name = "avg_npc_1211_1#4$1", focus="r")]
[name="雷内尔"]你再说一遍？！
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]你父亲在联合会中留下的人脉发挥了作用，你现在不必留在多索雷斯，也不用去拉乌尼达，你可以回家了。
[charslot(slot = "r", name = "avg_npc_1211_1#7$1", focus="r")]
[name="雷内尔"]不......我不会回去。
[name="雷内尔"]我不会回到那些最卑劣、最下贱、最可悲的东西中去......
[charslot(slot = "l", name = "avg_486_espumo_1#7", focus="l")]
[name="龙舌兰"]事到如今也由不得你了，雷内尔先生，不管你的最终归属是哪里，都是你鲁莽行动造成的结果。
[name="龙舌兰"]是苦是甜，你都得自己咽下。
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", focus="r")]
[name="雷内尔"]呵，老东西......你还真是阴魂不散啊。
[charslot(slot = "l", name = "avg_486_espumo_1#3", focus="l")]
[name="龙舌兰"]对了，还有一件事，你需要决定你财产的归属问题。
[charslot(slot = "r", name = "avg_npc_1211_1#8$1", focus="r")]
[name="雷内尔"]说得好像，我真的能自己决定一样，坎黛拉不是早就想方设法把它们挪去其他地方了吗？
[charslot(slot = "l", name = "avg_486_espumo_1#2", focus="l")]
[name="龙舌兰"]还有一些固定资产......没有人敢接手......
[name="龙舌兰"]你就在这份转让合同上随便写个名字吧。
[dialog]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1211_1#10$1", focus="r")]
[name="雷内尔"]......那就是下一个路过这里的人好了——
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_1214_1#1$1", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_486_espumo_1#3")]
[name="龙舌兰"]迪亚兹先生，你来监区干什么？？
[charslot(slot = "m", name = "avg_npc_1214_1#10$1")]
[name="迪亚兹"]指认假装人质的马特奥手下啊。反倒是你，你喊我干嘛？
[charslot(slot = "m", name = "avg_486_espumo_1#4")]
[name="龙舌兰"]没、没事。
[charslot(slot = "m", name = "avg_npc_1214_1#1$1")]
[name="迪亚兹"]那我走了。
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_npc_1211_1#1$1", focus="n")]
[charslot(slot = "l", name = "avg_486_espumo_1#4", focus="l")]
[name="龙舌兰"]哎......你......反正还没落笔，你随时可以反悔——
[charslot(slot = "r", name = "avg_npc_1211_1#1$1", focus="r")]
[name="雷内尔"]反悔？我从来都不反悔。
[name="雷内尔"]......何况，这么一想也不赖。
[name="雷内尔"]把它留给真正热爱艺术的家伙。
[dialog]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_20_G01",screenadapt="coverall")]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_486_espumo_1#1")]
[charslot(slot = "r", name = "avg_npc_198_1#1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "r", name = "avg_npc_198_1#1", focus="r")]
[name="坎黛拉"]雷内尔最后真的把那位老消防员的名字写上去了？
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]是的。送他出多索雷斯的时候，我最后向他确认了一次，他还是在监区的那套说辞。
[charslot(slot = "r", name = "avg_npc_198_1#1", focus="r")]
[name="坎黛拉"]......他真是连他父亲一丁点的特质都没有继承。
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]说实话，他大概不讨厌这种评价。
[charslot(slot = "r", name = "avg_npc_198_1#1", focus="r")]
[name="坎黛拉"]当然，但这句话可不是在夸他。
[charslot(slot = "l", name = "avg_486_espumo_1#6", focus="l")]
[name="龙舌兰"]哈哈......
[charslot]
[charslot(slot = "m", focus="n")]
[name="市长保镖"]坎黛拉女士，您和埃内斯托先生的咖啡。
[dialog]
[PlaySound(key="$d_avg_plateplace", volume=1)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_198_1#1", focus="n")]
[charslot(slot = "l", name = "avg_486_espumo_1#3", focus="l")]
[name="龙舌兰"]好浓的香气！布克先生，我能请教一下用的是哪种咖啡豆吗？
[charslot(slot = "m", focus="n")]
[name="市长保镖"]是坎黛拉女士最近常喝的三种深烘豆拼配。请二位慢用。
[charslot(slot = "r", name = "avg_npc_198_1#4", focus="r")]
[name="坎黛拉"]现在事情告一段落，要见见你在多索雷斯其他的熟人吗？
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]其实我在进城之前没想过要惊动任何人。
[charslot(slot = "r", name = "avg_npc_198_1#2", focus="r")]
[name="坎黛拉"]的确，假如一切都风平浪静的话，你本可以不惊动任何人，但多索雷斯永远不可能风平浪静，你从来都知道这一点。
[charslot(slot = "l", name = "avg_486_espumo_1#1", focus="l")]
[name="龙舌兰"]......是啊。
[charslot(slot = "r", name = "avg_npc_198_1#1", focus="r")]
[name="坎黛拉"]就像现在，雷内尔的这场闹剧过后，联合政府在多索雷斯的声势遭到了沉重打击。
[name="坎黛拉"]尽管从拉乌尼达寄来的抗议信一封接一封，但雷内尔和他的财产，他们想都别想。多索雷斯不是他们俯首帖耳的附庸。
[name="坎黛拉"]可与之相应，其余两方也已经迫不及待——
[dialog]
[delay(time=1)]
[charslot(slot = "r", name =

... (全文15385字符)
```

### training_act32side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 


[PopupDialog(dialogHead="$avatar_jesica")] 我已到达目标区域。

[Tutorial(focusX=-287, focusY=105, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_jesica", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这里视野良好，可以作为部署地点......
 
[PopupDialog(dialogHead="$avatar_doberm")] 等等！
```

### training_act32side_01_b

```
[Tutorial(focusX=-103, focusY=113, focusWidth=287, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这里的敌人会对处于<@tu.kw>同一直线方向上</>的我方干员发动<@tu.kw>“直击”</>，高台干员很难抵挡这种攻击。
```

### training_act32side_01_c

```
[PopupDialog(dialogHead="$avatar_jesica")] 抱歉......看来我身上的装甲还是不够厚......

[Tutorial(focusX=255, focusY=104, focusWidth=246, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
要避免遭受<@tu.kw>“直击”</>，我们可以站在<@tu.kw>封阻物</>后方。<@tu.kw>封阻物</>会阻隔敌人的视线，他们通常不会对<@tu.kw>封阻物</>背后的我方干员发起<@tu.kw>“直击”</>。

[PopupDialog(dialogHead="$avatar_doberm")] 当然，也可以在敌人视野内部署我方干员，吸引敌人的<@tu.kw>“直击”</>火力。

[PopupDialog(dialogHead="$avatar_snakek")] 吸引火力的工作就交给我啦！
```

### training_act32side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 

[PopupDialog(dialogHead="$avatar_snakek")] 不好，敌人好像发现杰西卡了，他们正在试图隔着<@tu.kw>封阻物</>对她射击

[PopupDialog(dialogHead="$avatar_doberm")] 刚才击坠的无人机带有侦察功能，会在坠毁时使附近的我方<@tu.kw>暴露</>位置

[PopupDialog(dialogHead="$avatar_doberm")] <@tu.kw>暴露</>后，只要处于同一直线方向上，敌人就会朝我方进行<@tu.kw>“直击”</>，且<@tu.kw>暴露</>中的我方受到的伤害还会<@tu.imp>提升</>

[PopupDialog(dialogHead="$avatar_jesica")] 幸好这<@tu.kw>封阻物</>还能遮挡几发子弹，赶紧解决他们吧
```

### training_act32side_01_e

```
[HEADER(is_skippable=true, is_autoable=false)] 

[PopupDialog(dialogHead="$avatar_ela")] 各位，各自寻找<@tu.kw>封阻物</>，进入战斗位置。

[PopupDialog(dialogHead="$avatar_iana")] 我刚刚探查了上方的情况，敌人正在<@tu.kw>封阻物</>附近聚成一团。

[PopupDialog(dialogHead="$avatar_fuze")] 轮到霰射炸药出场了。

[PopupDialog(dialogHead="$avatar_iana")] 小心，下方也有敌人来袭。

[PopupDialog(dialogHead="$avatar_doc")] 别担心，还有我呢。
```


## 统计

- 总字符数：423562
- 对话行数：2956


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
