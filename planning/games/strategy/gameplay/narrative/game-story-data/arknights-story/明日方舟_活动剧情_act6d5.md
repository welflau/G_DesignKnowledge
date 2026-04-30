# 明日方舟 · 活动剧情 · act6d5（3段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act6d5」完整剧情脚本（3个文件，1215行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act6d5
- 脚本文件数：3

### level_act6d5_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
第一幕
迎春
[Dialog(fadetime=2,block=true)]
[Delay(time=2)]
[Blocker(a=1, r=0,g=0, b=0, block=true)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=3)]
[Image(image="ac6_1",x=0, y=0, xScale=2, yScale=2, fadetime=0)]
[Blocker(a=0, fadetime=20, block=false)]
[ImageTween(xFrom=700, yFrom=400, xTo=-600, yTo=-230, xScaleFrom=2, yScaleFrom=2, xScaleTo=2, yScaleTo=2, duration=35, block=false)]
以子之矛，攻子之盾。
以子之盾，拒子之矛。
以子之矛，攻子之盾。
以子之盾，拒子......拒子......
拒子......
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
......
............
......搞什么啊，这不是没完没了吗。
这可咋办？得想个办法啊......
[dialog]
[delay(time=2 )]
[Image(image="ac6_1",x=0, y=0, xScale=2, yScale=2, fadetime=0)]
[Blocker(a=0, fadetime=10, block=false)]
[ImageTween(xFrom=-700, yFrom=-400, xTo=0, yTo=0, xScaleFrom=2, yScaleFrom=2, xScaleTo=1.4, yScaleTo=1.4, duration=35, block=false)]
以子之矛，攻子之盾......
以子之盾，拒子之矛......
不行，要有个“然后”。
然后，然后......啊，有了！
然后引发一场大爆炸，不就能全部搞定了？
[dialog]
[stopmusic(fadetime=3)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=3, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.8, crossfade=1.5)]
[Character]
[dialog]
[Background(image="bg_rooftop_2",screenadapt="coverall",fadetime=1,block=true)]
[Delay(time=1)]
11:15 P.M.  天气/晴
除夕夜，龙门，边防指挥中心
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(image="ac6_2",screenadapt="coverall",fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
“14区汇报，没有状况。”
“5区汇报，没有异样，一切正常。”
“1区正常，没有发现任何可疑迹象。”
“一切正常。大家辛苦了。请继续警惕。”
“了解。”
“明白。”
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_015_lmg",fadetime=1,blok=true)]
[Delay(time=1)]
[name="轻浮的近卫局成员"]   哈欠——
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   是你值夜班啊，现在情况如何？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   唉，正按计划进行迁移，移动速度正常，没有发现任何异样。
[name="轻浮的近卫局成员"]   唯一需要汇报的源石反应也就这些，你瞅瞅。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   ......“怀疑由源石炸药引起的爆炸”？什么情况？难不成在公园非法燃放烟花？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   看仔细啊，地点，地点。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   东芳街122号仓库，租借公司企鹅——哦，那没事了。
[name="认真的近卫局成员"]   但愿今年也是平安无事的一年。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   是啊，如果真是这样就好了。早点交班然后回家吃饭。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   正经点，魏长官特地叮嘱过，不要松懈。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   话说回来啊，我在龙门长这么大，每年都紧张兮兮的......
[name="轻浮的近卫局成员"]   从来没有一次真撞见过什么“年关”，那是个啥情况？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   我也没见过啊。另外这个问题去年你已经问过一遍了。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   不瞒你说，现在的新兵蛋子都已经认定那不过是个民间传说了。
[name="轻浮的近卫局成员"]   一个会吐火的百米巨人？真要有这种东西，在它离龙门还有几十公里的时候我们就能发现，然后用护城炮解决问题。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   应该是个特别大只的野兽，虽然一直在警备，但这种东西已经不太可能来袭击城市了吧。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   话是这么说，但大家都还是好好坚守岗位的，毕竟是魏长官亲自下的命令。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   得了，不用帮他们说话。你们在监控室里吃泡面的事情我已经记下了，不怪你们，年夜饭嘛，等着交红包吧。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   ......
[name="轻浮的近卫局成员"]   那魏长官经历过年关吗？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   你在质疑上司？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   怎么会！我就是因为魏长官才加入的近卫局！
[name="轻浮的近卫局成员"]   可是，把几乎全城的人力调来监视一个几十年都没有出现过的巨人？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   唉，魏长官向来谨慎，事事都要讲个周全，你又不是不知道。
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   话是这么说......
[Character]
[dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[PlaySound(key="$dooropenquite")]
[Character(name="char_383_snsant_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="？？？"]   不、不好意思！我来晚了！这是上一个区间的源石监测报告！
[name="？？？"]   欸？那个......魏长官呢？
[Character(name="char_383_snsant_1",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   ......呃，她不在这儿。
[Character(name="char_383_snsant_1",name2="char_015_lmg",focus=1)]
[name="？？？"]   欸、欸？但是陈警官告诉我她在总监控室......
[Character(name="char_383_snsant_1",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   这里是屋顶......
[name="认真的近卫局成员"]   下楼左拐，最大的那间屋子是总监控室。
[Character(name="char_383_snsant_1")]
[name="？？？"]   欸，我明明刚从那里跑过来的，难道我错过了......
[name="？？？"]   不好意思！我得赶紧过去！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="轻浮的近卫局成员"]   什么情况？那是谁？
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="认真的近卫局成员"]   新来的吧，看样子应该是哪个技术部门的。
[Character(name="char_015_lmg")]
[name="轻浮的近卫局成员"]   看她慌慌张张的，肯定第一次迎接年关，真怀念啊，我也有那样的时候——
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_indoor_3",screenadapt="coverall")]
[delay(time=0.1)]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="char_383_snsant_1",fadetime=1,blok=true)]
[Delay(time=1)]
[name="？？？"]   呼，呼，不好意思，请问总监控室在哪儿......
[Character(name="char_010_chen_1#5")]
[name="陈"]   ......雪雉？你怎么还在这里？
[Character(name="char_383_snsant_1",name2="char_010_chen_1#5",focus=1)]
[name="雪雉"]   欸？陈警官都已经到了吗？
[Character(name="char_383_snsant_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   应该是我问你吧。
[Character]
[dialog]
[PlaySound(key="$flashback", volume=1)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.3

... (全文36975字符)
```

### level_act6d5_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第一关（前）
[Dialog]
[Delay(time=1)]
第二幕
贺岁
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.7, crossfade=1.5)]
[Background(image="bg_lmstreet_1",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_1002_nsabr_2",fadetime=2,block=true)]
[delay(time=2)]
[name="无声的整合运动"]   ......
[Character(name="char_015_lmg")]
[name="近卫局成员"]   放下武器，后退。
[Character(name="char_1002_nsabr_2")]
[name="无声的整合运动"]   ......
[Character(name="char_015_lmg")]
[name="近卫局成员"]   啧，还是交涉无效，动手！
[name="近卫局成员"]   这些家伙根本不是人类，不用手下留情！
[name="近卫局成员"]   听得见吗！这里是隐庐小队！已经确认7区全部目标符合判断条件，都是“兵俑”！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=0.1)]
[Background(image="bg_lungmencommand",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[Character(name="char_015_lmg")]
[name="近卫局成员"]   真的是整合运动吗？
[Character(name="char_2006_weiywfmzuki_1")]
[name="魏文月"]   只是障眼法罢了，先确认他们的身份。
[Character]
[Dialog]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="近卫局成员"]   魏长官！事态有变！
[name="近卫局成员"]   他们的数量......在、在增加。几乎所有巡逻的小队都发现了整合运动！
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="bg_5_2_call",screenadapt="coverall",fadetime=0)]
[Blocker(a=0, fadetime=2, block=true)]
[name="近卫局成员A"]   又、又有报告，市区部分地点出现短暂的急剧升温，监测部门在做什么！？
[name="近卫局成员B"]   没有任何反应！可是看其他的数据的确是有在正常运作的......！
[name="近卫局成员A"]   敌人开始袭击靠近的小队，喊话没有回应，无法建立沟通。
[name="近卫局成员B"]   敌军溃散！他们很脆弱，基本没有反抗，但是数量很多！
[name="近卫局成员A"]   真的是整合运动吗？
[name="近卫局成员B"]   热源在转移，想办法追踪它！
[name="近卫局成员A"]   城防没有任何漏洞，他们不可能出现在市区内——
[name="魏文月"]   不要慌张！
[name="魏文月"]   ......
[name="魏文月"]   通知偶数编号编队集合。最坏的情况，要在市区内与敌人交战。优先让群众避难。
[name="魏文月"]   下城区内市民密集，特别是庙街。让该城区内所有警员优先疏散平民。
[name="魏文月"]   联系边城区优先排查防线是否有漏洞，确认敌人的运输手段，按兵不动，不要让对方有可乘之机。
[name="魏文月"]   整合运动应该早已销声匿迹，明确敌人的身份。控制事态是首要任务。龙门并非第一次在年关遭遇特殊情况，不用小题大做。
[name="魏文月"]   团结一致，近卫局无需畏惧。
[name="近卫局成员"]   是！
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Image(fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_2006_weiywfmzuki_1")]
[name="魏文月"]   ......
[name="魏文月"]   抱歉，阿米娅，博士。尽管你们刚抵达龙门，但可能没有时间给你们休息参观了。
[Character(name="char_002_amiya_1#7")]
[name="阿米娅"]   没关系，自罗德岛抵达龙门的那一刻，合约就已经生效了。
[name="阿米娅"]   请交给我们吧，我们会协助近卫局的行动！
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=0.1)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_1002_nsabr_1",fadetime=1,block=true)]
[delay(time=1)]
[name="兵俑"]   ......
[name="兵俑"]   ......
[Character]  
[name="龙门市民A"] 呼啊，那、那些家伙什么情况？
[name="龙门市民A"] 我认得这些人，但他们不是已经被——！？
[name="龙门市民B"] 咿呀！这里也有！
[Character(name="char_1002_nsabr_1")]
[name="兵俑"]   ......
[Dialog]
[stopmusic(fadetime=2)]
[Character]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[Character(name="char_010_chen_1#2")]
[name="陈"]   嘁，闪开点——！
[dialog]
[Character(name="char_1002_nsabr_1")]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_sp_chixiaobadao")]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.02, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
[Delay(time=1)] 
[Character(fadetime=1,block=true)]
[delay(time=1)]
[Character]
[name="龙门市民A"] 谢、谢谢！
[Character(name="char_010_chen_1#4")]
[name="陈"]   普通市民应该听从广播去指定的避难区避难，而不是在这里闲逛！
[name="陈"]   沿着大路向前，和警员们汇合，动作快！
[Character]  
[name="龙门市民B"] 明、明白了！
[Character(name="char_010_chen_1#1")]
[name="陈"]   ......
[name="陈"]   不会说话，也不会流血，就像切开了一团海绵一样，连尸体都会消失不见。
[name="陈"]   “兵俑”，真是合适的代称。
[Character]
[Dialog]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.7, crossfade=1.5)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[name="魏文月"]   称其为“整合运动”会造成不必要的恐慌，陈警官。他们不是有血有肉的敌人。
[Character(name="char_010_chen_1#1")]
[name="陈"]   我明白。已经确保城区安全。
[Character]
[name="魏文月"]   感谢你的努力，但是很遗憾，单纯的杀敌似乎是徒劳的。
[name="魏文月"]   过去数小时，我们仍未能摸透“兵俑”的特性，但他们的兵力却源源不断。
[Character(name="char_010_chen_1#1")]
[name="陈"]   虽然这样的规模匪夷所思，但会不会是某种法术？
[Character]
[name="魏文月"]   这才是最让人头疼的地方，源石反应监测依旧毫无反应。但也正因如此，他们不是真正的整合运动。
[Character(name="char_010_chen_1#1")]
[name="陈"]   ......绝不会是。我很清楚。
[name="陈"]   这是伪装，只是幻象。
[name="陈"]   但是整合运动大摇大摆地走在龙门的街道上......
[name="陈"]   实在是......让人不快。
[Character]
[name="魏文月"]   他们与源石完全绝缘。在这片大地上，这是几乎不可能的事情。
[Character(name="char_010_chen_1#1")]
[name="陈"]   但它的确发生了，敌人是从哪里进入龙门的？
[Character]
[name="魏文月"]   我们的常规手段无法侦测，完全没有关于敌人“怎样出现”的报告。
[name="魏文月"]   好像他们一直就在那里，无声无息地排兵列阵、冲锋、溃散，如此反复。
[Character(name="char_010_chen_1#1")]
[name="陈"]   ......简直就像浪花一样。
[name="陈"]   我会按照预备方案组织封锁线。
[Character]
[name="魏文月"]   小心点。
[name="魏文月"]   近卫局不能失去你。
[Character]
[Dialog]
[stopmusic(fadetime=2)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[delay(time=2)]
[Character(name="char_1002_nsabr_1")]
[name="兵俑"]   ——
[Character(name="char_010_chen_1#5")]
[name="陈"]   不管他们的主人是谁，创造出这种混淆现实的幻影，除了制造些许混乱，还能对龙门造成什么威胁？
[name="陈"]   他们不堪一击。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Delay(time=0.1)]
[Background(image="bg_park",screenadapt="coverall")]
[Blocker(a=0, fadetime=2, block=true)]
[PlayMusic(intro="$normal02_intro", key="$normal02_loop", volume=0.6, crossfade=1.5)]
[Character(name="char_1002_nsabr_1",name2="char_1002_nsabr_1")]
[name="兵俑"]   ......
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="近卫局成员"]   （这些家伙真的渗人......如果我们不冒头，他们是不是就一直那么整齐地杵那儿？）
[name="近卫局成员"]   （但是我们一露面他们就会冲过来。）
[name="近卫局成员"]   （小声点，他们弱得很，找个机会偷袭他们，速战速决。）
[name="近卫局成员"]   （——等等，你要干嘛！？）
[Character(name="char_015_lmg",name2="char_015_lmg",focus=2)]
[name="近卫局成员？"]   ......
[Character(name="char_015_lmg",name2="char_015_lmg",focus=1)]
[name="近卫局成员"]   喂，你们在干嘛！快回来！
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="近卫局成员"]   ——

... (全文38882字符)
```

### level_act6d5_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 第二关（前）
[Dialog]
[Delay(time=1)]
[Character]
第三幕
拜年
[Dialog(fadetime=2,block=true)]
[Delay(time=1)]
以吾之矛，攻吾之盾。
以吾之盾，拒吾之矛。
那么问题在于，左手和右手打架会有结果吗？
显然不会。
就算打赢了又能怎么样？
不能怎样。
嗯......但其实惯用手还是会有优势的？
[Dialog(fadetime=2,block=true)]
[Delay(time=1)]
[Character]
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_wild_m",screenadapt="coverall")]
[Delay(time=0.4)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1.5)]
[Blocker(a=0, fadetime=3, block=true)]
4:21A.M.  天气/阴
龙门郊区
近卫局失去21号城区控制权后第三日
[dialog]
[Character(name="char_002_amiya_1#1",fadetime=1,block=true)]
[delay(time=1)]
[name="阿米娅"]   陈警官，你在这里。
[Character(name="char_002_amiya_1#1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   这里可以眺望到那片沦陷的城区。
[Character(name="char_002_amiya_1#1",name2="char_010_chen_1#1",focus=1)]
[name="阿米娅"]   移动边城区，组成防线拦截年的攻势，魏长官的决策很果断。
[Character(name="char_002_amiya_1#1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   但我没想到有朝一日，城头的另一边竟然也是龙门的土地。
[name="陈"]   ......真是荒唐。
[Character(name="char_002_amiya_1#1",name2="char_010_chen_1#1",focus=1)]
[name="阿米娅"]   年就在那里。
[Character(name="char_002_amiya_1#1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   那片城区，有我常去的商场。
[name="陈"]   还有我几个朋友的家，都在那里。
[Character(name="char_002_amiya_1#1",name2="char_010_chen_1#1",focus=1)]
[name="阿米娅"]   ......很抱歉，陈警官。
[name="阿米娅"]   难以想象，一座城邦与仅仅一名敌人为敌，竟然会处于劣势。
[Character(name="avg_npc_044_1")]
[name="炎熔"]   培养一位训练有素的士兵需要多久，她随手铸造一名战士又需要多久，结果显而易见。
[Character]
[dialog]
[PlaySound(key="$flashback", volume=1)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.3, block=true)]
[Image(fadetime=0)]
[Character(name="avg_6D5_1#4")]
[Background(image="avg_6D5_1", x=20,y=0,xScale=1.1, yScale=1.1)]
[Image(image="avg_6d5_lava",x=40,y=-80,xScale=1.1, yScale=1.1)]
[Blocker(a=0, fadetime=0.3, block=true)]
[BackgroundTween(image="avg_6D5_1",x=20,y=0,xTo=-20,yTo=0,xScale=1.1, yScale=1.1,xScaleTo=1.2, yScaleTo=1.2,duration=20)]
[ImageTween(image="avg_6d5_lava",x=40,y=-80,xScale=1.1, yScale=1.1,xScaleTo=1.3, yScaleTo=1.3,xTo=120,yTo=-120,duration=15)]
炎熔，罗德岛精英干员，法术大师，灾害专家。
她用法术超越了空间的桎梏，而且理所当然。
[delay(time=1)]
[dialog]
[Character]
[PlaySound(key="$flashback2", volume=1)]
[Blocker(a=1, r=1,g=1, b=1, fadetime=0.4, block=true)]
[Image(fadetime=0)]
[Background(image="bg_wild_m",screenadapt="coverall")]
[Blocker(a=0, fadetime=0.4, block=true)]
[Character(name="char_002_amiya_1#2")]
[name="阿米娅"]   炎熔！你来了！
[Character(name="avg_npc_044_1")]
[name="炎熔"]   抱歉，我不该轻易接触她的。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   这话你该对那些现在还爬不起来的干员说，为了接应你，我们付出的代价不小。
[name="陈"]   我们需要的是你的知识和技巧，而不是这些丧士气的话。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=1)]
[name="炎熔"]   “士气”？靠士气这种东西面对无法理解的敌人，只会徒增伤亡，送死罢了。
[name="炎熔"]   想要打败她夺回城市，就必须直面这个亘古至今困扰我们的谜题。
[name="炎熔"]   “她的弱点”。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   我以为这就是你的任务。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=1)]
[name="炎熔"]   出乎意料的好消息是，那个“年”具有一个相当程度上可以交流的人格。
[name="炎熔"]   坏消息是，她的性格太糟糕了。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   我本来对你的期待更高一点，你可别说一无所获。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=1)]
[name="炎熔"]   当然不会。
[name="炎熔"]   从浩如烟海的史学资料里也只能勉强抓住一些苗头，而如何去佐证那些信息，只有靠厮杀和流血。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]   但你也不用独自行动啊，年天性乖戾，如果你有了什么意外......
[Character(name="avg_npc_044_1")]
[name="炎熔"]   我的血就够了。
[stopmusic(time=3)]
[playsound(key="$d_gen_transmissionget", volume=0.4)]
[Character(name="char_015_lmg")]
[name="近卫局成员"]   陈sir，紧急联络。
[name="近卫局成员"]   发现了“年”本人的踪迹。正在向防线靠近。
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.6, crossfade=1.5)]
[Character(name="char_010_chen_1#4")]
[name="陈"]   ......各队避免和她正面接触，也警告那些热心市民不要随便插手，这不是儿戏。
[Character(name="char_015_lmg")]
[name="近卫局成员"]   但是她并没有带多少兵力......
[Character(name="avg_npc_044_1")]
[name="炎熔"]   对她而言，人数没有意义，我们只能拖住她的脚步。
[Character(name="char_010_chen_1#1")]
[name="陈"]   你说过，她有弱点。时间不多了。
[Character(name="avg_npc_044_1")]
[name="炎熔"]   她的弱点是爆竹。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   ......爆竹？
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=1)]
[name="炎熔"]   任何关于“年”的记载都不曾记录下她的完全面目，更妄说弱点。但是炎国之行让我有了一些新的发现。
[name="炎熔"]   任何历史悠久的民俗一般都有其起源和传说。尽管有一部分可能是近代生造的，因此遮掩了真相。
[name="炎熔"]   有些学说认为，爆竹是现代源石炸药技术的起源，起源于某种祈祷意味的民俗。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]   这种事情大家都知道呀，岁岁平安，驱邪除祟......
[Character(name="avg_npc_044_1")]
[name="炎熔"]   那这些古老的传说里，邪祟是什么？
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]   啊......
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   等等，但近卫局能准备十万倍以上的火力，真是这样的话年根本就不成威胁，这说不通。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=1)]
[name="炎熔"]   “畏响动，畏火光。”
[name="炎熔"]   如果年的职能真的是“冶炼”，那爆竹根本就不对她构成威胁。
[name="炎熔"]   她......自称匠人。火光和响声根本就是她的分内之事，至少是某种存在投影在她身上的分内之事。
[Character(name="char_002_amiya_1#1")]
[name="阿米娅"]   某种存在？
[Character(name="avg_npc_044_1")]
[name="炎熔"]   为了解释她那不依赖源石技艺，完全不讲理的能力而做出的假设。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   她会恐惧自己？这也太扯了吧......
[Character(name="avg_npc_044_1")]
[name="炎熔"]   本以为这只是个传说......但似乎有价值尝试一下。
[name="炎熔"]   无论如何，她在巨大的声音和火焰法术面前的确退缩了。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   ......也许吧，毕竟我们根本没空来严谨地质疑你的假设。
[name="陈"]   所有的可能性我们都要尝试，她已经兵临城下了。
[Character(name="avg_npc_044_1")]
[name="炎熔"]   那么容我最后提醒一下。
[name="炎熔"]   首先，她很强。也许有办法摧毁她，但是势必会血流成河。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   ——近卫局会阻止这种事情发生。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=1)]
[name="炎熔"]   所以尽量避免正面冲突，至少她并不喜好杀戮。
[name="炎熔"]   第二，看不出她的能力会产生损耗，和她耗下去，落于被动的只会是我们。
[name="炎熔"]   第三，不知道为什么，她对大部分现代产物都很好奇。
[Character(name="avg_npc_044_1",name2="char_010_chen_1#1",focus=2)]
[name="陈"]   ......这对接下来的战斗有什么帮助吗？
[Character(name="avg_npc_044_

... (全文46977字符)
```


## 统计

- 总字符数：122834
- 对话行数：1215


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
