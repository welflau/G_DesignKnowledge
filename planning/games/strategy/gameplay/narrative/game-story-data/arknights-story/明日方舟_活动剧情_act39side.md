# 明日方舟 · 活动剧情 · act39side（26段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act39side」完整剧情脚本（26个文件，3491行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act39side
- 脚本文件数：26

### level_act39side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Subtitle(text="半个月前", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="53_g16_sunnyday_R2",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=2)]
[PlaySound(key="$transmission")]
[Delay(time=1)]
[name="伊西多"]记录，滑沙板磨损严重，附近找不到适合用来修补的材料。
[name="伊西多"]淡水储备......最多还能再坚持一天。
[name="伊西多"]所幸距离下一个补给点只有半天行程。
[Dialog]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[name="伊西多"]......这么多条留言？
[name="伊西多"]我攒了这么长时间吗？
[Dialog]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[name="通讯器留言"]棘刺干员，好久没收到你的讯息了，有空记得汇报一下你的位置哦。
[Dialog]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[name="通讯器留言"]据我估算，我们的任务路线有所重叠，或许之后能找到机会见一面，我有些多余的物资可以给你。
[Dialog]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[name="通讯器留言"]嘿，棘刺，你那个超级厉害的剑术寻找之旅进行得如何了？有没有什么好消息分享下？
[Dialog]
[PlaySound(key="$d_gen_transmissionget")]
[Delay(time=1)]
[PlaySound(key="$d_avg_button")]
[Delay(time=1)]
[name="伊西多"]算了......等行程结束后慢慢回吧。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_laccolith",screenadapt="coverall")]
[charslot(slot="m",name="avg_293_thorns_1#1$2",focus="m")]
[Delay(time=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_paper1")]
[Delay(time=1)]
[charslot(slot="m",name="avg_293_thorns_1#6$2",focus="m")]
[name="伊西多"]拦在中间的这片区域......地图上除了个名字，什么都没标。
[charslot(slot="m",name="avg_293_thorns_1#3$2",focus="m")]
[name="伊西多"]“苍白海”......海吗？
[charslot(slot="m",name="avg_293_thorns_1#1$2",focus="m")]
[name="伊西多"]但愿它不是真的海。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
荒芜的原野上，风带起沙粒，送来一股咸腥的气味。
阴云的裂隙间，阳光倾泻而下，早已干涸的河道中只有几株灌木。
其中窸窸窣窣的声音，证明这片荒原并非毫无生气。
扯出绳索，青年将几块木板绑紧，然后踩在上面，纵身一跃。
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_ship_sand",channel="a")]
[Delay(time=1.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g1_saltdesert_d",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
陡然，荒原戛然而止，一道高崖截断了大地。
俯瞰崖底，伊西多真的看见一片苍白色的海。
费尽力气，青年攀下陡崖，踏上那片苍白的“海”，他伸手蘸了一抹干燥的“海水”送入口中。
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_293_thorns_1#4$2",duration=1.5)]
[Delay(time=2.5)]
[name="伊西多"]......盐晶？
[Dialog]
[charslot]
没有水，只有苍白的盐地，其间点缀着数不清的骨骸，那都是它所吞噬的生命。
但青年总觉得在看不见的角落，还有什么在流淌，在涌动。
他停下滑沙的木板，摸向腰间的佩剑。
[charslot(slot="m",name="avg_293_thorns_1#7$2",focus="m")]
[name="伊西多"]奇怪......
[name="伊西多"]这个地方不应该有任何生命的。
[Dialog]
[charslot]
[stopmusic(fadetime=2)]
[PlaySound(key="$smallearthquake")]
[CameraShake(duration=3.5, xstrength=35, ystrength=35, vibrato=20, randomness=70, fadeout=true, block=true)]
脚下的地面轻轻震动，围绕着青年，盐层缓缓下陷。
震动愈发剧烈，盐地上，一道凹痕向青年的位置快速蔓延。
[Dialog]
[charslot(slot="m",name="avg_293_thorns_1#4$2",focus="m")]
[name="伊西多"]盐漠里有鳞？！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_gaintplugin")]
[CameraShake(duration=3, xstrength=35, ystrength=35, vibrato=20, randomness=70, fadeout=true, block=true)]
[PlaySound(key="$d_avg_explosion_stone")]
[CameraShake(duration=3.5, xstrength=35, ystrength=35, vibrato=20, randomness=70, fadeout=true, block=true)]
猝不及防，庞然巨物从盐层中跃出，船帆般的背鳍高高扬起，锋锐的头甲如同巨矛。
[Dialog]
[Effect(name="$e_dust_step",x=350,y=0,layer = 1)]
[Effect(name="$e_dust_step",x=150,y=0,layer = 2)]
[Effect(name="$e_dust_step",x=550,y=0,layer = 3)]
[PlaySound(key="$d_avg_explosion_stone")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=1, g=1, b=1, fadetime=0.05, block=true)]
[charslot]
[charslot(slot = "m",posfrom="0,0", posto="-50,0", afrom=1, ato=0, duration=0.5, isblock=false)]
[CameraShake(duration=0.5, xstrength=25, ystrength=25, vibrato=20, randomness=70, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$bodyfalldown1",channel="2")]
[CameraShake(duration=0.5, xstrength=35, ystrength=35, vibrato=20, randomness=70, fadeout=true, block=true)]
强烈撞击下，青年被抛上天空，五脏六腑痛得仿若移位，随即重重摔在地上，不省人事。
意识模糊之际，他看到那条巨鳞迅速钻回盐层中不见踪影。
[name="伊西多"]（......幸好......它不饿......）
[Dialog]
[Dialog]
[charslot]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[name="伊西多"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3.5, block=true)]
[Dialog]
[charslot]
[Background(image="57_g1_saltdesert_d",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[bgeffect(name="$eb_sand02",layer=1,flip = 1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4163_rosesa_1#11$1",duration=1.5)]
[Delay(time=2)]
[name="帕斯卡拉"]咳咳......真是倒霉......
[charslot(slot="m",name="avg_4163_rosesa_1#11$1",focus="m")]
[name="帕斯卡拉"]天杀的执裁官简直阴魂不散，就连这毛都不长一根的破地方他也追得上来。
[charslot(slot="m",name="avg_4163_rosesa_1#14$1",focus="m")]
[name="帕斯卡拉"]咳，糟......刚刚跑得太急，水都洒了。
[charslot(slot="m",name="avg_4163_rosesa_1#11$1",focus="m")]
[name="帕斯卡拉"]......怎么办..

... (全文33836字符)
```

### level_act39side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g17_lighthouse_alley",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$rungeneral")]
[charslot(slot="m",name="avg_4163_rosesa_1#19$1",duration=1.5)]
[Delay(time=2.5)]
[PlaySound(key="$doorknockquite",channel="2")]
[Delay(time=2)]
[charslot(slot="m",name="avg_4163_rosesa_1#19$1",focus="none")]
[name="“平凡”的镇民"]哟，帕斯卡拉，你终于来了。我还以为你死在盐漠里了。
[charslot(slot="m",name="avg_4163_rosesa_1#19$1",focus="m")]
[name="帕斯卡拉"]呼......
[charslot(slot="m",name="avg_4163_rosesa_1#19$1",focus="none")]
[name="“平凡”的镇民"]看你这惨白的小脸，路上遇到什么了？
[charslot(slot="m",name="avg_4163_rosesa_1#19$1",focus="m")]
[name="帕斯卡拉"]闭嘴，蒂奇......快点让我进去。
[charslot(slot="m",name="avg_4163_rosesa_1#19$1",focus="none")]
[name="“平凡”的镇民"]想进来？首领要的东西你拿到了吗？
[charslot(slot="m",name="avg_4163_rosesa_1#17$1",focus="m")]
[name="帕斯卡拉"]当然，不止罗盘，我还有另外一个大发现。
[name="帕斯卡拉"]胡安娜女士一直在找的炼金术师，我也有线索了。
[name="帕斯卡拉"]现在我能进去了吗，蒂奇？
[charslot(slot="m",name="avg_4163_rosesa_1#17$1",focus="none")]
[name="“平凡”的镇民"]当然，神偷帕斯卡拉小姐，您的光临让寒舍蓬荜生辉。
[Dialog]
[PlaySound(key="$dooropenquite")]
[charslot(slot="m",posfrom="0,0", posto="-200,0", afrom=1, ato=0, duration=1)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g14_ibtown_n",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="r",name="avg_npc_187",posfrom="-150,0", posto="-150,0",duration=1.5)]
[Delay(time=2)]
[name="蹒跚的老人"]升起船帆嘿，收起船锚嘿♪
[name="蹒跚的老人"]让狂风撕扯我们的衣衫♪
[name="蹒跚的老人"]让暴雨浇醒我们的酒意♪
[name="蹒跚的老人"]准备！出发！港口的船有千千万万只！♪
[Dialog]
[charslot(slot="l",name="avg_293_thorns_1#1$1",bstart=0.3,bend=0.5,posfrom="0,-50", posto="0,0", afrom=0, ato=1, duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",bstart=0.3,bend=0.5,focus="l")]
[name="？？？"]......
[charslot(slot="r",name="avg_npc_187",posfrom="-150,0", posto="-150,0",focus="r")]
[multiline(name="蹒跚的老人")]天亮我们将第一个冲向大♪......
[CameraShake(duration=0.3, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[charslot(slot="r",posfrom="-150,0", posto="0,0",duration=0.5)]
[multiline(name="蹒跚的老人",end=true)]啊啊——你谁？！为什么会蹲在我家？！
[Dialog]
[charslot(slot="l",name="avg_293_thorns_1#10$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[name="伊西多"]老伯，这条小巷......是你家吗？
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]小伙子，你现在顶的纸板就是我的床......
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[name="伊西多"]对不起，我看它在垃圾桶旁，以为没人要。
[name="伊西多"]我能在你家暂避下雨吗？天亮我就离开。
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]镇上都两个月没见一滴雨了。
[name="蹒跚的老人"]就算要下雨，你能不能先放下我的床？喏，这是我的被子，你拿去吧。
[Dialog]
[charslot(slot="r",name="avg_npc_187",focus="all")]
[PlaySound(key="$d_avg_clothmovement")]
[delay(time=1.5)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]......谢谢，先生。
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]你是来干什么的，阿戈尔人？
[charslot(slot="l",name="avg_293_thorns_1#6$1",focus="l")]
[name="伊西多"]我在找一种本地流传的剑术，传说最早创立这种剑术的......咳咳......
[name="伊西多"]几个月前，我听说了这种“能与风浪相搏”的特异剑术，想来学习。
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]真是胆子大，不知道审判庭的人到今天还戒备着海盗吗？
[charslot(slot="l",name="avg_293_thorns_1#3$1",focus="l")]
[name="伊西多"]我对海盗不感兴趣，只是觉得自己的剑术有欠缺。
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]剑是用来砍人的，不是用来砍水的，更何况，你学了干什么？出海吗？
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]......
[name="伊西多"]你问太多了，老伯。
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]唉......总有人信这种傻事。你要是早来半年，我还能带你去见见那个老家伙。
[name="蹒跚的老人"]他当年跟那群海盗学了一招两式，天天吵吵着自己能劈开巨浪。最后还不是跟我一样，跑回镇子里安安稳稳地等死？
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]他死前有留下什么吗？
[charslot(slot="r",name="avg_npc_187",focus="r")]
[name="蹒跚的老人"]他的日记？都带进坟里啦，自己挖去吧。
[name="蹒跚的老人"]那家伙要是知道有人想学自己的剑术，肯定高兴得要从坟里爬出来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g2_saltdesert_n",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_sandftsingle")]
[Delay(time=1)]
[PlaySound(key="$d_avg_sandftsingle")]
[Delay(time=1)]
[charslot(slot="m",name="avg_293_thorns_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="伊西多"]......
[Dialog]
[charslot]
将锹子竖在一旁，伊西多掀开棺材板，拨开落入其中的盐粒，一具外表晶亮，色泽红润的尸体露了出来。
尸体的衣袋中露出书册的一角。
伊西多小心翼翼捏住，将它取出，尽全力保护因盐分侵蚀而异常脆弱的纸张碎片。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]这就是那位先生说的日记吗？
[name="伊西多"]碎得什么都看不出来。
[Dialog]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_293_thorns_1#10$1",focus="m")]
[name="伊西多"]咳咳咳......噗——呸呸！
[charslot(slot="m",name="avg_293_thorns_1#2$1",focus="m")]
[name="伊西多"]......碎纸片都吹进嘴里了，好咸。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]去别的地方再找找吧。
[Dialog]
[charslot]
[name="？？？"]别的地方？你这十恶不赦的盗墓贼、食人犯，还想去哪里作恶？
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1587_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_293_thorns_1#10$1",focus="m")]
[name="伊西多"]盗墓贼？食人犯？？
[charslot(slot="m",name="avg_npc_1587_1#1$1",focus="m")]
[name="？？？"]一路上看你鬼鬼祟祟地摸到墓地里来，这下让我逮了个正着。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]我可以解释，这位先生。
[charslot(slot="m",name="avg_npc_1587_1#1$1",focus="m")]
[name="？？？"]“这位先生”......？你甚至不认识我！
[charslot(slot="m",name="avg_293_thorns_1#10$1",focus="m")]
[name="伊西多"]您是当地什么很有名的人物吗？
[stopmusic(fadetim

... (全文40916字符)
```

### level_act39side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g11_meetingroom",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1580_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[name="蒂奇"]一个人的时候，您永远都看着大海的方向。
[name="蒂奇"]记得小时候，您抱着我，指着远处说，继续往前，就能看到比天空还要湛蓝的海洋。
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]那已经是五十年前的事了。
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]夫人，您至今也未曾忘记百年前的往事。
[charslot(slot="m",name="avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]哦，小珍珠，若你像我一样曾驾驶着船只在海浪中翻腾，看闪电在云间交会，耳边是不绝的雷声。
[name="胡安娜"]你也只能用一生去怀念。
[charslot(slot="m",name="avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]真好奇啊，长辈们心心念念的海洋到底是什么模样？
[name="蒂奇"]这一辈子我都生活在盐漠里，恐怕想破头也想不出个所以然。
[name="蒂奇"]倒是我家那老爷子，临死前天天念叨的都是出海出海，说他跟着您和科鲁兹船长把船舱塞满财宝，钱币多得快要把船压沉。
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]你父亲是我见过手脚最敏捷的操帆手，在桅杆上攀爬如履平地。
[charslot(slot="m",name="avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]可惜，那些真正见识过海洋的船员没剩多少了。
[name="蒂奇"]这正是我担心的问题，夫人，就算有罗盘的引领，我们也缺乏老练的海员。
[charslot(slot="m",name="avg_npc_1581_1#11$1",focus="m")]
[name="胡安娜"]小珍珠，面对海洋，我们都是鲁莽无知的孩童。
[charslot(slot="m",name="avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]唉......如今我们连面对这片盐漠都开始觉得吃力。
[name="蒂奇"]探子回来报告，雅隆来了一个厉害家伙，几乎掐断了所有商路。
[charslot(slot="m",name="avg_npc_1581_1#5$1",focus="m")]
[name="胡安娜"]他们终于要动真格了？
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]夫人，那人准确找出了我们与商队接触的地点，之前的几十年，镇子里的那些草包可连踪迹都摸不到。
[charslot(slot="m",name="avg_npc_1581_1#2$1",focus="m")]
[name="胡安娜"]唉......重兵把守的罗盘被窃，这对审判庭来说近乎羞辱与挑衅。
[name="胡安娜"]无论如何，他们不会轻易放过我们。
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]时间不多了，那小子又油盐不进......该如何是好，夫人？
[name="蒂奇"]或许他没骗我们，他真的不是炼金术师？
[charslot(slot="m",name="avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]我能肯定他的身份，小珍珠。
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]他身上有枚金币，正反两面分别有代表“盐”与“水”的图样，是一支特殊炼金流派的标志，它们的意思是“向海而生”。
[name="胡安娜"]我认识金币原来的主人，奥卢斯，他是那一派中最有才的炼金术师。
[name="胡安娜"]况且那小家伙还用着和奥卢斯一样的剑术，言谈举止也有些相似。
[charslot(slot="m",name="avg_npc_1580_1#6$1",focus="m")]
[name="蒂奇"]或许他们只是认识，金币就是随手送的礼。
[charslot(slot="m",name="avg_npc_1581_1#9$1",focus="m")]
[name="胡安娜"]不，如果奥卢斯将那枚金币赠予他人，只说明他对那人抱有超乎寻常的期望。
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]按他们流派的规矩，那枚金币只能由老师传给学生。
[charslot(slot="m",name="avg_npc_1580_1#6$1",focus="m")]
[name="蒂奇"]既然如此，那小子为何死不承认？
[charslot(slot="m",name="avg_npc_1581_1#9$1",focus="m")]
[name="胡安娜"]我也觉得困惑，明明已经再三申明，他不必承担任何风险......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
年幼的伊西多狠狠地咬住牙根，却压不住牙床深处泛上来的酸涩。
眼前，昔日同窗的尸体就在恩师脚下。
早已冰冷的四肢上，还残留着令他作呕的淡蓝色黏液。
泪水模糊了他的视线，一个流水般温柔的声音不请自来地探入他内心深处。
[name="奥卢斯"]为什么要抹去自己的眼泪，伊西多？
[name="伊西多"]是你杀了他......
[name="奥卢斯"]海洋与陆地本是一体，融合，不过是抹消彼此间的隔阂。
[name="奥卢斯"]他自愿作出这样的决定，拥抱自己体内流淌的盐与水，与我们共享他存在的全部。
[name="奥卢斯"]再无恐惧、憎恶、嘲笑与痛恨......再无紧闭的门窗，再无封闭的内心，再无污秽的血脉，再无可耻的伤痛。
[name="奥卢斯"]终有一日，所有人都会向所有人敞开身心。
忽然，地板上的尸体像离水的海鳞般弹动起来，发出近乎凄厉的吸气声，随即又瘫倒在地。
伊西多注意到尸体的眼皮缓缓抬起，露出陌生生物的眼睛。
嘴唇开阖，发出似人非人的声音。
“你也......同我......一样......”
[Dialog]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="伊西多"]不——！
[Dialog]
[stopmusic(fadetime=2)]
[CameraEffect(effect="Grayscale", amount=0,fadetime=0.5,keep=true)]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_293_thorns_1#10$1",duration=1.5)]
[Delay(time=2.5)]
[name="伊西多"]我绝不会......绝不会同你一样......
[name="伊西多"]不会......
[name="伊西多"]呼......
[PlayMusic(key="$normal_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧哼哧！
[name="宝宝"]（拱来拱去）
[charslot(slot="m",name="avg_293_thorns_1#7$1",focus="m")]
[name="伊西多"]唔......？
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]（拍打胸鳍）
[charslot(slot="m",name="avg_293_thorns_1#7$1",focus="m")]
[name="伊西多"]你......
[charslot(slot="m",name="avg_npc_1586_1#3$1",focus="m")]
[name="宝宝"]（狠狠啃咬）
[charslot(slot="m",name="avg_293_thorns_1#4$1",focus="m")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="伊西多"]干什么！痛！
[Dialog]
[charslot]
小动物在他脚旁扭动，试图用它那圆滚滚的身躯盖住他的脚。
繁杂的声响从四面八方灌入棚屋。那之中有哭泣，有争论，但更多的是咒骂。
但愿他们咒骂的不是自己，伊西多停下动作，下意识地想。
他探出头，看守竟反常地不在门外。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g9_community_d",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
聚落中，一行队伍垂着头走过，每个人身上的衣服都染着污血。
队伍后面拖行的木板上躺着几个重伤的人，伤口深可见骨，却只用破布草草包扎。
血液将木板浸透，在雪白的盐层上留下长长的拖痕。
只有几声间或的喘息证明他们仍然活着。
[charslot(slot="m",name="avg_npc_1589_1#1$1",focus="m")]
[name="沮丧的女人"]少了几乎一半......
[charslot(slot="m",name="avg_npc_1590_1#2$1",focus="m")]
[name="鲁斯"]唉......
[charslot(slot="m",name="avg_npc_1589_1#1$1",focus="m")]
[name="沮丧的女人"]你们......是遇到什么了？
[charslot(slot="m",name="avg_npc_1590_1#2$1",focus="m")]
[name="鲁斯"]审判庭的经棍一早埋伏在必经之路上。许多伙伴都牺牲了，就剩我们......好不容易逃回来。
[charslot(slot="m",name="avg_npc_1591_1#1$1",focus="m")]
[name="悲伤的男人"]镇子里的家伙没有盐船，是怎么深入盐漠找到你们的？
[charslot(slot="m",name="avg_npc_1590_1#6$1",focus="m")]
[name="鲁斯"]没人知道......
[name="鲁斯"]他们就像恶灵一样，仿佛感受不到痛苦，即使受伤也不会倒下，立刻又会展开攻击。
[Dialog]
[charslot]
[name="伊西多"]（小声）镇子里都是普通的教士，只不过修习过一点武艺......怎么可能做到这种程度？
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1580_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1590_1#1$1",focus="m")]
[name="鲁斯"

... (全文23013字符)
```

### level_act39side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g1_saltdesert_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_avg_sandftsingle")]
[Delay(time=1)]
[PlaySound(key="$d_avg_sandftsingle")]
[Delay(time=1)]
[PlaySound(key="$swordtsing1")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Delay(time=1)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1591_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]......计程仪？
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]你知道这是什么？
[charslot(slot="l",name="avg_293_thorns_1#6$1",focus="l")]
[name="伊西多"]不就是以前水手们用来记录航程的东西。
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]你以前接触过这些东西？
[charslot(slot="l",name="avg_293_thorns_1#6$1",focus="l")]
[name="伊西多"]......嗯，我的老师带着我学过很多。
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]你的老师胆子还真大啊。
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]你要一直站在我背后讲个不停吗？
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]你以为我想吗，小子？是水手长吩咐我要和你寸步不离。
[Dialog]
[charslot(slot="r",posfrom="0,0",posto ="-50,0",duration = 1.5,isblock=false)]
[Delay(time=2)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]我觉得我们的距离有点过近了。
[Dialog]
[charslot(slot="r",posfrom="-50,0",posto ="0,0",duration = 1.5,isblock=false)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]哼......
[Dialog]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="all")]
[PlaySound(key="$d_avg_sandstone",channel="1")]
[Delay(time=2)]
[stopsound(channel="1",fadetime=1)]
[charslot(slot="l",name="avg_293_thorns_1#7$1",focus="l")]
[name="伊西多"]这声音......好熟悉......
[Dialog]
[charslot]
捕捉到盐粒流动的声音，伊西多警觉地环顾四周，看见在船员的身后，熟悉的凹痕出现在盐层表面。
[charslot(slot="l",name="avg_293_thorns_1#5$1",focus="l")]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="l")]
[name="伊西多"]快闪开，有盐鳞！
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="l",posfrom="0,0",posto ="100,0",duration = 1,isblock=false)]
[charslot(slot="r",posfrom="0,0",posto ="50,-20",duration = 1.5,isblock=false)]
[charslot(slot="l",afrom=1,ato =0,duration = 0.5,isblock=false)]
[charslot(slot="r",afrom=1,ato =0,duration = 0.5,isblock=false)]
[Delay(time=1.5)]
[PlaySound(key="$bodyfalldown1",channel="2")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[charslot]
[Delay(time=0.8)]
[PlaySound(key="$d_avg_sandstone",channel="1")]
[charslot(slot="m",name="avg_npc_1585_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="l",name="avg_293_thorns_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1591_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]吃鳞屎了！你这小子！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1585_1#1$1",focus="m")]
[name="盐鳞"]啾叽......啾叽......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]你就为它把我撞开吗？
[name="塞斯克"]你不会以为盐层下面是巨鳞吧？
[charslot(slot="l",name="avg_293_thorns_1#7$1",focus="l")]
[name="伊西多"]闭嘴......
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]那种巨鳞来时地面会有剧烈震动。这种小家伙只会留下一些凹痕。
[name="塞斯克"]而且，它们和宝宝是同一物种，能造成什么破坏？
[name="塞斯克"]真不知道那疯婆娘找你来干嘛！
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧......
[charslot(slot="m",name="avg_npc_1585_1#1$1",focus="m")]
[name="盐鳞"]啾叽......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="l")]
[name="伊西多"]这两个......是一种生物吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1585_1#1$1",focus="m")]
[name="盐鳞"]啾叽......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_sandstone")]
[charslot(slot="l",name="avg_npc_1585_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1584_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot]
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="l")]
[name="伊西多"]这里的盐鳞不止一种吗？
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]是的，大大小小共有几十种。
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[name="伊西多"]我看到你们的船帆使用了皮革材质，那些皮......
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]是盐鳞的皮，我们的帐篷也用它搭。
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[name="伊西多"]那你们帐篷外晒的肉干......
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]是盐鳞做的。
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[name="伊西多"]武器......
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]盐鳞的骨头。
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="l")]
[name="伊西多"]那它们......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧......
[charslot(slot="m",name="avg_npc_1585_1#1$1",focus="m")]
[name="盐鳞"]啾叽......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_293_thorns_1#10$1",focus="r")]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]不一样，除非迫不得已，我们不会伤害它们。
[name="塞斯克"]疯婆娘很喜欢它们，曾经想过捕捉到船上来饲养，但这种盐鳞一旦离群就会迅速失去活力，所以她最终还是放弃了。
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]那它为什么会来到船上？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧哼哧。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1591_1#1$1",focus="r")]
[name="塞斯克"]宝宝是被族群抛弃的孩子，因为身体过于孱弱，无法跟上其他盐鳞的行进，幸好......疯婆娘捡到了它。
[Dial

... (全文27353字符)
```

### level_act39side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g11_meetingroom",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1581_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1579_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_1581_1#1$1",focus="l")]
[name="胡安娜"]小哈，很感激你为我带来晚餐，非常美味，我很喜欢。
[charslot(slot="r",name="avg_npc_1579_1#7$1",focus="r")]
[name="哈维尔"]胡安娜女士......我有些疑问。
[charslot(slot="l",name="avg_npc_1581_1#1$1",focus="l")]
[name="胡安娜"]讲吧，你在我面前不必遮掩。
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]女士，我们的人力不足，但这次围猎却要选择如此巨大的盐鳞作为猎杀目标，实在是有些......冒险。
[name="哈维尔"]去追小规模的盐鳞群，会更保险些吧？
[charslot(slot="l",name="avg_npc_1581_1#10$1",focus="l")]
[name="胡安娜"]我们最近追到的盐鳞群，少得有点太可怜了。之后的炼金会需要大量的材料，我们得提早做准备。
[charslot(slot="r",name="avg_npc_1579_1#1$1",focus="r")]
[name="哈维尔"]我们已经为此准备了很多。
[charslot(slot="l",name="avg_npc_1581_1#10$1",focus="l")]
[name="胡安娜"]远远不够，有了罗盘才只是开始，进入海洋我们需要更多。
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]前任厨子波兹曾和我讲过，您总是会做出一些疯狂的决定，大部分会使人感到热血沸腾，但有些......
[name="哈维尔"]却让人觉得如坠冰窟。
[charslot(slot="l",name="avg_npc_1581_1#1$1",focus="l")]
[name="胡安娜"]......我忠诚的老下属，无论我做出什么样的决定，他总是支持我。就算是那些让他胆寒的事情，他也义无反顾。
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]您希望我也那样做吗，胡安娜女士？
[charslot(slot="l",name="avg_npc_1581_1#11$1",focus="l")]
[name="胡安娜"]当然不，所以他卸任，你成为我的新厨师。
[charslot(slot="r",name="avg_npc_1579_1#10$1",focus="r")]
[name="哈维尔"]......
[charslot(slot="l",name="avg_npc_1581_1#1$1",focus="l")]
[name="胡安娜"]小哈，你真的甘心永远留在这里过这种为眼前日子发愁的生活吗？这是难得的机会，只要抓住它，我们就能一劳永逸解决所有麻烦。
[name="胡安娜"]那片海洋哺育了整个黄金时代的富商与豪门，而我们船队的规模甚至比不上二手贩子的私船队。
[charslot(slot="r",name="avg_npc_1579_1#5$1",focus="r")]
[name="哈维尔"]这片盐漠也哺育了我们整整几十年啊！这么多年，虽然艰辛，但你都带着我们挺过来了。
[charslot(slot="l",name="avg_npc_1581_1#2$1",focus="l")]
[name="胡安娜"]盐漠于我们而言实在过于贫瘠了。
[charslot(slot="r",name="avg_npc_1579_1#1$1",focus="r")]
[name="哈维尔"]但海洋于我们而言实在是过于危险了。
[charslot(slot="l",name="avg_npc_1581_1#9$1",focus="l")]
[name="胡安娜"]小哈，想想镇子里的人，他们恨不得将我们除之后快，如今他们的围剿步步紧逼......
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]可你以前从没有害怕过他们啊，胡安娜女士？！
[charslot(slot="l",name="avg_npc_1581_1#2$1",focus="l")]
[name="胡安娜"]......我害怕的不是他们。
[charslot(slot="l",name="avg_npc_1581_1#9$1",focus="l")]
[name="胡安娜"]我害怕的是盐漠，这里的生态要崩溃了，小哈。
[name="胡安娜"]那次地裂......正是一种预兆，探险队之前报告给我，由于地下暗河枯竭，盐漠地下出现了大量空洞。
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]空洞？
[charslot(slot="l",name="avg_npc_1581_1#8$1",focus="l")]
[name="胡安娜"]暗河濒临干涸，其中的微生物数量在锐减......以微生物群为食的盐鳞数量也在骤减。
[name="胡安娜"]......捕鳞船已经很久没有遇到大型的盐鳞群落了。
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]您为什么不告诉我们呢？
[charslot(slot="l",name="avg_npc_1581_1#2$1",focus="l")]
[name="胡安娜"]我该怎么说？再不离开，我们马上就要完蛋了？这只会在船队中徒增恐慌，小哈。
[charslot(slot="r",name="avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]这是我们唯一的办法了吗，首领？
[charslot(slot="l",name="avg_npc_1581_1#7$1",focus="l")]
[name="胡安娜"]......是的，唯一的办法。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_piratepet_vo01")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_bonrcver")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_293_thorns_1#3$1",duration=1.5)]
[Delay(time=2.5)]
[name="伊西多"]左边点......谢谢。
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_piratepet_vo01")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_bonrcver")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_293_thorns_1#9$1",focus="m")]
[name="伊西多"]嗯......再用点力气踩。
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧——！
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]和鲁斯先生学了一整天，想不到在这里捕捉盐鳞这么艰难......肩膀好痛。
[Dialog]
[PlaySound(key="$d_avg_bonrcver")]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_293_thorns_1#9$1",focus="m")]
[name="伊西多"]嘶......对，就是那个地方，好酸。
[Dialog]
[charslot]
在伊西多不断的倒吸气声中，他背上的宝宝踩得更加奋力。
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]宝宝......
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧哼哧！
[charslot(slot="m",name="avg_293_thorns_1#2$1",focus="m")]
[name="伊西多"]算了，说了你也不懂。
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]......我不是不想帮你们。
[name="伊西多"]小时候，有乞丐教了我两手粗浅戏法，用来糊弄行人骗些吃的。
[name="伊西多"]后来认识了老师，他告诉我那可不是戏法。
[charslot(slot="m",name="avg_293_thorns_1#2$1",focus="m")]
[name="伊西多"]那是炼金术啊......
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m")]
[name="宝宝"]哼哧......哼哧......
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]刚开始学习炼金术时，我对它很是痴迷，过程中不断的成功换来了老师的夸奖、同伴的认可。
[name="伊西多"]更好的是，我感觉到自己不再是一无所有的流浪儿。
[name="伊西多"]我是一个值得些什么的人了。
[charslot(slot="m",name="avg_293_thorns_1#6$1",focus="m")]
[name="伊西多"]直到我得知了那支炼金流派最本质的特征......
[Dialog]
[charslot]
伊西多停顿片刻，宝宝也停下踩踏，疑惑地抬起脑袋。
[Dialog]
[charslot(slot="m",name="avg_293_thorns_1#2$1",focus="m")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[musicvolume(volume=0.2, fadetime=2)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="伊西多......很遗憾，你舍弃不了自己拥有的东西。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你在惶恐，如果赌失败，又会变成那个一无所有、四处流浪的孩子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="但炼金术的本质即是为了达成目的，以最偏执激进的方式将所拥有的事物全都投入进去。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="孤注一掷......只为一个机会。", x=300, y=370, alignment="center", size=24, 

... (全文30247字符)
```

### level_act39side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g4_newdeck_2",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_avg_steamburst_big",channel="2")]
[CameraShake(duration=1.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=true)]
[charslot]
[charslot(slot="m",name="avg_npc_1580_1#2$1",duration=1.5)]
[Delay(time=2.5)]
[name="蒂奇"]小心，别往蒸汽柱上撞。
[charslot(slot="m",name="avg_npc_1579_1#6$1",focus="m")]
[name="哈维尔"]哼，大言不惭说要领着我们往里闯，这就是你的办法吗？把我们所有人弄死在这里。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]抱歉......我下次会注意。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement")]
[CameraShake(duration=0.5, xstrength=5, ystrength=5, vibrato=20, randomness=70, fadeout=true, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_glassbroken",channel="1")]
[Delay(time=0.3)]
[PlaySound(key="$d_avg_steamburst_big",channel="2")]
[CameraShake(duration=1.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=true)]
伊西多投出的试管在空气中炸裂，淡金色的雾气随之散开。
很快，几人便清晰地看见一道微弱的赤色气流冲开雾气。
紧随其后的，是剧烈的蒸汽喷发。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]这样我们就能预知蒸汽喷发了。
[charslot(slot="m",name="avg_293_thorns_1#2$1",focus="m")]
[name="伊西多"]但我手里这种药剂剩的不多了，不够支撑我们行进太远......快点划吧。
[charslot(slot="m",name="avg_npc_1579_1#6$1",focus="m")]
[name="哈维尔"]哼......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_turnrudder")]
[Delay(time=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g4_newdeck_2",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]哈维尔，前面有船只残骸，注意行驶。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]如果需要，我可以用药剂爆破掉它。
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[name="哈维尔"]用不着，我能避开。你多能干我已经知道了，小子。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]哦......好。这沉船......看起来有些年头了。
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]我认识它，胡安娜设计的最初版盐船，她带上大家，以为可以驾驶着它穿过骸礁峡谷，回到海洋。
[charslot(slot="m",name="avg_npc_1579_1#2$1",focus="m")]
[name="哈维尔"]她失败了。
[charslot(slot="m",name="avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]也失去了很多。
[charslot(slot="m",name="avg_npc_1579_1#7$1",focus="m")]
[name="哈维尔"]小子，看到首领的踪迹了吗？
[charslot(slot="m",name="avg_293_thorns_1#6$1",focus="m")]
[name="伊西多"]看得到，离得不远了。
[Dialog]
[charslot]
盐船继续向前行驶，掠过一片高耸的骨刺，几道裂痕贯穿骨刺表面，沾染了大量血液。
[charslot(slot="m",name="avg_npc_1579_1#6$1",focus="m")]
[name="哈维尔"]......
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]别乱想，那是盐鳞血。
[Dialog]
[charslot]
伊西多捡起从崖壁上滚落的碎盐块，扔了出去。
然后，他摊开黏腻的手掌，看到手中满是从盐块上沾来的血迹。
[charslot(slot="m",name="avg_293_thorns_1#7$1",focus="m")]
[name="伊西多"]......
[charslot(slot="m",name="avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]这是怎样的一场搏杀，一路上几乎都是血迹。
[charslot(slot="m",name="avg_npc_1579_1#6$1",focus="m")]
[name="哈维尔"]首领她......还活着吗？
[charslot(slot="m",name="avg_293_thorns_1#7$1",focus="m")]
[name="伊西多"]答案就在前面了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="57_g1_saltdesert_d",screenadapt="coverall")]
[BackgroundTween(xFrom=0, yFrom=150, xTo=0, yTo=150, xScaleFrom=1.4, yScaleFrom=1.4, xScaleTo=1.4, yScaleTo=1.4, duration=0, ease="InOutCubic", block=true)]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
绕过峡谷间的骸骨巨柱，可以看到巨大的盐鳞尸体横在地上，早已没了气息，一把舵轮正插在它的脑袋上。
而舵轮的主人趴在盐鳞的背上，一动不动，血液顺着她的脚慢慢滑下。
[charslot(slot="m",name="avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]夫人......
[charslot(slot="m",name="avg_npc_1579_1#9$1",focus="m")]
[name="哈维尔"]胡安娜......不......
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="m",posfrom="0,0",posto ="-50,0",duration = 1.5,isblock=false)]
[charslot(slot="m",afrom=1,ato=0,duration=1,isblock=false)]
[Delay(time=2)]
[charslot]
所有人走下船，攀上盐鳞的背。哈维尔轻轻触碰女人的胳臂，她的身体尚存温热，却令他更觉悲伤。
[charslot(slot="m",name="avg_npc_1579_1#5$1",focus="m")]
[name="哈维尔"]对不起，是我们来晚了。
[Dialog]
[charslot(slot="m",name="avg_npc_1579_1#5$1",focus="none")]
[name="？？？"]咳......咳咳，你们来得确实太晚。
[charslot(slot="m",name="avg_npc_1579_1#9$1",focus="m")]
[name="哈维尔"]女、女士？！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_npc_1581_1#6$1",posfrom="0,-50",posto ="0,0",duration = 1.5,isblock=false)]
[charslot(slot="m",afrom=0,ato=1,duration=1,isblock=false)]
[Delay(time=1.5)]
[Dialog]
[name="胡安娜"]我还指望你们能早点来搭把手呢。
[charslot(slot="m",name="avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]夫人，你还好吗？我们看到你浑身都是血......
[charslot(slot="m",name="avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]别担心，身上的血不是我的，是这大家伙的。它挣扎了一路，还是没能撑到最后。
[charslot(slot="m",name="avg_npc_1581_1#9$1",focus="m")]
[name="胡安娜"]伊西多，可以把水壶递给我吗？
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]当然。
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Image(image="57_i03",screenadapt="coverall", fadetime=0)]
[PlaySound(key="$d_avg_decap")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
接过水壶，胡安娜缓缓爬下盐鳞的背，然后倚靠着它巨大的身躯坐下。
她扒开塞子，痛饮几口，看看围过来的众人，嘴角噙着一丝笑意。
[name="胡安娜"]咸鳞汁啊......可惜。如果是壶上好的朗姆酒就好了。
[name="胡安娜"]伊西多......你能来扶我一把吗？和这大家伙拼斗这么久，我累得根本站不起来。
[name="伊西多"]我？
[name="哈维尔"]我来吧。
[name="胡安娜"]不，还是让那小家伙来，你们得把这头盐鳞切开来带回去呢。
[name="胡安娜"]小哈，顺便帮我把舵轮从盐鳞身上取下来吧。
[name="哈维尔"]没问题，女士。
[name="胡安娜"]过来，小家伙。
[name="伊西多"]好......好的，我来扶你。
[name="胡安娜"]哦，慢着，等候一位女士可不能太心急，最起码要等她把手头的事情做完。
将壶塞丢到空中抛接几次，胡安娜不紧不慢地喝干壶里的液体，而一旁的伊西多只能耐心等待。
胡安娜的喉头一滚一滚，她吞咽得很缓慢。
或者说，她吞咽得很费劲。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, 

... (全文28015字符)
```

### level_act39side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g13_ibtown_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[playsound(key="$d_avg_crwddiscuss_outside", loop=true, channel="b",volume=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_187",focus="m")]
[name="饥饿的镇民"]谢谢，谢谢......
[charslot(slot="m",name="avg_npc_189",focus="m")]
[name="拘谨的镇民"]驮兽入栏的时候，我不小心激怒了它，导致一名教士被抓伤，给我少盛些吧，就当是赎罪......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1583_1#6$1",duration=1)]
[Delay(time=1.5)]
[name="西尔弗"]多吃些，下次才不会出这种事。
[name="西尔弗"]这条盐鳞够所有人饱餐一顿，大家都多吃些。
[charslot(slot="m",name="avg_npc_189",focus="m")]
[name="拘谨的镇民"]可是，西尔弗大人，吃太饱的话——
[charslot(slot="m",name="avg_npc_1583_1#6$1",focus="m")]
[name="西尔弗"]总比浪费好。现在这个天气，盐鳞肉存不了太久，尽早吃完吧。
[name="西尔弗"]厨师先生，这几份麻烦你给受伤的教士们送去。
[name="西尔弗"]这些日子他们身上新伤叠旧伤的，也该好好补补了。
[Dialog]
[stopsound(channel="b",fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="bg_ibbar",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$doorknockquite")]
[Delay(time=1.5)]
[PlaySound(key="$dooropenquite")]
[charslot(slot="m",name="avg_npc_1583_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="西尔弗"]执裁官阁下，那份计划书您看了吗？
[charslot(slot="m",name="avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]我不明白，您为何会有这样的想法？
[charslot(slot="m",name="avg_npc_1583_1#1$1",focus="m")]
[name="西尔弗"]只要那些强盗交出罗盘和盐船的设计图，我会赦免大多数人，允许他们以我指定的方式生活下去。
[name="西尔弗"]他们中有不少精壮的年轻人，如果我们的镇子要移动起来，那就是最宝贵的劳力。
[name="西尔弗"]况且，掌握着这些不受教条束缚的刀剑，我们以后和谁谈判，都会轻松很多。
[charslot(slot="m",name="avg_npc_1582_1#8$1",focus="m")]
[name="安纳斯塔西奥"]他们会毁了您的镇子。
[charslot(slot="m",name="avg_npc_1583_1#1$1",focus="m")]
[name="西尔弗"]除掉领头的那个阿戈尔人，剩下的强盗不过是一盘散沙。现在地下室铐着的那三个人，各自都打着自己的算盘呢。
[charslot(slot="m",name="avg_npc_1583_1#4$1",focus="m")]
[name="西尔弗"]等到我把他们分裂开来，分别放在互相之间会有利益冲突的位置上......他们哪怕还有歹心，也只会向曾经的同伴举刀。
[charslot(slot="m",name="avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]您曾经拯救了镇上的所有人，教他们克制欲望、保持纯洁......而如今您竟要为利益而赦免杀害过他们亲朋好友的强盗？
[name="安纳斯塔西奥"]哪怕您能接受，您真的认为镇民们都能接受？
[charslot(slot="m",name="avg_npc_1582_1#6$1",focus="m")]
[name="安纳斯塔西奥"]这难道不是背叛？
[charslot(slot="m",name="avg_npc_1583_1#3$1",focus="m")]
[name="西尔弗"]......
[name="西尔弗"]那您认为该怎么做？
[charslot(slot="m",name="avg_npc_1582_1#8$1",focus="m")]
[name="安纳斯塔西奥"]我很快会再带人深入盐漠，彻底剿灭残存的强盗，毁去他们用于作孽的一切手段。
[charslot(slot="m",name="avg_npc_1583_1#3$1",focus="m")]
[name="西尔弗"]您看到受伤的教士们了。他们需要休息。
[name="西尔弗"]我们的人手和资源都不够再进行一次大规模围剿了。
[charslot(slot="m",name="avg_npc_1582_1#8$1",focus="m")]
[name="安纳斯塔西奥"]我会确保他们能够出战。
[charslot(slot="m",name="avg_npc_1583_1#1$1",focus="m")]
[name="西尔弗"]不，恕我直言，这不是您能做的决策，执裁官阁下。
[name="西尔弗"]天色一暗下来，地下室的那三个强盗就会“偷溜”出镇。不出意外的话，他们很快就能把消息带回去。
[name="西尔弗"]您只需要在强盗上门谈判的时候维持秩序。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g6_olddeck_1",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_293_thorns_1#1$1",duration=1)]
[Delay(time=1.5)]
[name="伊西多"]......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1581_1#1$1",duration=1)]
[Delay(time=2)]
[name="胡安娜"]......为什么突然改主意了？
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]只是修复一枚罗盘而已，没有那么多要考虑的。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]......
[Dialog]
[PlaySound(key="$d_avg_sweep",volume=0.5,channel="1")]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_sweep",volume=0.5,channel="3")]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]唉......心里没事的人，手上可不会这么不安分。我该担心你在我的船上面抠出一个洞来吗，小家伙？
[charslot(slot="m",name="avg_293_thorns_1#6$1",focus="m")]
[name="伊西多"]我并没有使那么大力气。
[charslot(slot="m",name="avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]别这样，一本正经的家伙才最让人觉得滑稽。
[name="胡安娜"]换套衣服吧，你身上都是血。
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]......谢谢。
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]跟我来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g12_alchemyworkshop",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_dooropen")]
[bgeffect(name="$eb_dust_01",layer=1)]
[Delay(time=3.5)]
[bgeffect(fadetime=1.5)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_1581_1#1$1",duration=1)]
[Delay(time=2)]
[PlaySound(key="$aluminum")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[Delay(time=1)]
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]咳咳......
[charslot(slot="r",name="avg_npc_1581_1#1$1",focus="r")]
[name="胡安娜"]哦，忘记叫你屏住呼吸了，这间舱房已经封闭了数十年，灰尘很重。
[charslot(slot="l",name="avg_293_thorns_1#2$1",focus="l")]
[name="伊西多"]对不起，我不该在你的船舱里随意乱碰。
[charslot(slot="r",name="avg_npc_1581_1#3$1",focus="r")]
[name="胡安娜"]你把我说得像个小气又记仇的女人。
[charslot(slot="r",name="avg_npc_1581_1#1$1",focus="r")]
[name="胡安娜"]想摸就上手摸摸吧，这些都是最上等的炼金器械，没那么脆弱。你肯定不觉得自己那只小手比风暴和炮火更有破坏力吧？
[name="胡安娜"]怎么样，以后这就是你的工作室了。
[charslot(slot="l",name="avg_293_thorns_1#1$1",focus="l")]
[name="伊西多"]这是一间正规的舰载炼金工坊？
[charslot(slot="r",name="avg_npc_1581_1#1$1",focus="r")]
[name="胡安娜"]嗯。
[charslot(slot="l",name="avg_293_thorns_1#6$1",focus="l")]
[name="伊西多"]......
[charslot(slot="r",name="avg_npc_1581_1#10$1",focus="r")]
[name="胡安娜"]对了......
[name="胡安娜"]这是以前船上炼金术师的衣服，试试吧。你和他身量差不多，应该合适。
[charslot(slo

... (全文38449字符)
```

### level_act39side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g12_alchemyworkshop",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[charslot(slot="l",name="avg_npc_1577_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_450_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_450_1#6$1",focus="r")]
[name="极境"]胳膊和腿都还在，脸也没有破相，就是更黑了点......
[name="极境"]真是太好了！你不知道我听说他们这些强盗冷血无情、杀人如麻的时候，我有多紧张！
[charslot(slot="l",name="avg_npc_1577_1#1$1",focus="l")]
[name="伊西多"]......你这都是从哪里听来的......
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="r")]
[name="极境"]我是付出了多大的勇气才敢跑到这里来救你的啊！温蒂还留在镇子里，我这就给她......
[charslot(slot="l",name="avg_npc_1577_1#7$1",focus="l")]
[name="伊西多"]......
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="r")]
[name="极境"]（小声）等准备好了，我就给她发通讯，然后想办法离开这里！
[charslot(slot="l",name="avg_npc_1577_1#6$1",focus="l")]
[name="伊西多"]我试过了，逃不出去的，而且，短期内我不打算离开。
[charslot(slot="r",name="avg_npc_450_1#5$1",focus="r")] 
[name="极境"]为什么？难道你真如传言一般加入了强盗的船队？
[charslot(slot="r",name="avg_npc_450_1#2$1",focus="r")] 
[name="极境"]（小声）老实告诉我，你真觉得在这穷乡僻壤当强盗很有前途吗？
[charslot(slot="l",name="avg_npc_1577_1#10$1",focus="l")]
[name="伊西多"]......我对当海盗不感兴趣，极境。
[charslot(slot="l",name="avg_npc_1577_1#1$1",focus="l")]
[name="伊西多"]我留下是因为......我想重拾当年自己逃避掉的炼金研究。这可是搭载了心相原质的罗盘......可能就只有这一枚存世了。
[name="伊西多"]而且......我答应了他们要修好罗盘。没有罗盘，他们很难继续活下去。
[charslot(slot="r",name="avg_npc_450_1#2$1",focus="r")] 
[name="极境"]那......你以后也打算一直跟他们走？
[charslot(slot="l",name="avg_npc_1577_1#1$1",focus="l")]
[name="伊西多"]不，等到罗盘修好，这些海盗就会离开盐漠，驶向大海。
[charslot(slot="l",name="avg_npc_1577_1#7$1",focus="l")]
[name="伊西多"]我会留下来，继续在伊比利亚精进自己的剑术与炼金技艺。
[Dialog]
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="all")] 
[PlaySound(key="$d_avg_slapcloth_light")]
[Delay(time=2)]
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="r")] 
极境拍了拍伊西多的肩膀，感觉自己的朋友似乎变了一些。
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="r")] 
[name="极境"]看来这段日子你有很多感触啊......也好。
[name="极境"]对了，外面那个小丫头叫我过来本来是要干什么来着？
[charslot(slot="l",name="avg_npc_1577_1#6$1",focus="l")]
[name="伊西多"]我修复罗盘的过程中，需要有人帮忙做些辅助操作。
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="r")] 
[name="极境"]那简单，就和在罗德岛一样，有什么需要帮忙的就和我说。
[charslot(slot="l",name="avg_npc_1577_1#1$1",focus="l")]
[name="伊西多"]嗯。
[name="伊西多"]我会叫你。
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=2)]
伊西多走到塑金台前站定，他手中施术用的探针在空气中划出锐响，精密的法术能量场沿着探针的轨迹逐渐成型。
他小心翼翼地拆下罗盘的外壳，将它送上塑金台。慢慢地，罗盘内原本凝固的流体物质，也开始随着法术能量流动的方向漾起波澜。
法术能量与心相原质交相辉映，淡金色的光透过工坊的缝隙，照亮了船外的盐地。
船员们没见过这样的景象，一个又一个地被吸引而来。
[name="门外的船员"]他们在搞什么东西？
[name="好奇的船员"]是那个外面来的小子在搞什么炼啥术......这金光还挺有意思的。
[name="探头的船员"]让我看看让我看看......
[charslot(slot="l",name="avg_npc_1577_1#7$1",focus="l")]
[charslot(slot="r",name="avg_npc_450_1#1$1",focus="l")]
[name="伊西多"]......
[charslot(slot="r",name="avg_npc_450_1#6$1",focus="r")]
[name="极境"]当真，还挺酷的。你手里的这是什么？
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Dialog]
[charslot]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Background(image="57_g14_ibtown_n",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_459_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_461_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="r",name="avg_npc_461_1#1$1",focus="r")]
[name="好奇的路人"]看，那孩子手里是什么？
[charslot(slot="l",name="avg_npc_459_1#1$1",focus="l")]
[name="不屑的路人"]还能有什么，又一个小鬼为了讨饭耍的把戏呗。
[charslot(slot="r",name="avg_npc_461_1#1$1",focus="r")]
[name="好奇的路人"]那算了，赶紧走吧，我们可没有多余的口粮。
[charslot(slot="l",name="avg_npc_459_1#1$1",focus="l")]
[name="不屑的路人"]惹人烦的小鬼......
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(fadetime=1.5)]
[Delay(time=2)]
[name="小伊西多"]戏法表演！只要一块饼就能观赏，诸位请不要错——
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_178",duration=1.5)]
[Delay(time=2)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=0.03, block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0.5, block=true)]
[Dialog]
[delay(time=0.51)]
[charslot(slot="m",name="avg_npc_178",focus="none")]
[name="小伊西多"]呜......
[charslot(slot="m",name="avg_npc_178",focus="m")]
[name="冷漠的路人"]别挡在路中间，到一边去。
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2)]
[name="小伊西多"]（小声）呸，混蛋......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[Dialog]
[charslot]
[CameraEffect(effect="Grayscale", amount=0, keep=true)]
[Background(image="57_g12_alchemyworkshop",screenadapt="coverall")]
[charslot(slot="l",name="avg_npc_1577_1#7$1")]
[charslot(slot="r",name="avg_npc_450_1#1$1")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_1577_1#7$1",focus="l")]
[name="伊西多"]......
[charslot(slot="r",name="avg_npc_450_1#2$1",focus="r")]
[name="极境"]呃，外面围了好多人，会打扰你吗？
[name="极境"]我去把他们赶走？
[charslot(slot="l",name="avg_npc_1577_1#6$1",focus="l")]
[name="伊西多"]没事，有你在这叨叨，我感觉像是回到了之前在罗德岛的工作环境。他们打扰不到我的。
[Dialog]
[charslot]
伊西多没有停下手中的动作，他手中的探针仿佛在与能量场中荡漾的心相原质舞蹈。
光芒自他的掌心诞生，在窗外的船员们眼中，像是一场在干渴与饥饿中突然出现的白日梦境。
[name="门外的船员"]你见过这玩意吗？这小子还真会啊。
[name="好奇的船员"]很久之前好像首领讲过差不多的故事，说大的城镇里有变戏法的，看起来就是这样。
[name="探头的船员"]好看......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1577_1#7$1",focus="l")]
[charslot(slot="r",name="avg_npc_450_1#2$1",focus="l")]
[name="伊西多"]他们想看就让他们看吧，只要别突然冲进来要把我绑了送出去换吃的就行。
[charslot(slot="r",name="avg_npc_450_1#2$1",focus="r")]
[name="极境"]......确实是他们能干出来的事

... (全文18066字符)
```

### level_act39side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g12_alchemyworkshop",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_underwateramb", loop=true, channel="bgs",volume=0)]
[SoundVolume(volume=0.6, channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1.5)]
[StopSound(channel="bgs", fadetime=1)]
[delay(time=1)]
[playsound(key="$d_avg_firemagic",volume=0.7)]
[PlaySound(key="$firemagic_explosion",volume=1,delay=1.2)]
[delay(time=1.2)]
[CameraShake(duration=1.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[PlayMusic(key="$m_avg_pirate_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_npc_1577_1#7$1", duration=1)]
[charslot(slot = "r", name = "avg_npc_450_1#8$1", duration=1)]
[delay(time=1.5)]
[charslot(slot = "r", name = "avg_npc_450_1#8$1",focus="r")]
[name="极境"]哇，这可比你在罗德岛搞的实验危险多了。
[name="极境"]以前你一天最多也就炸三四次实验室，现在平均每十五分钟炸一次。
[charslot(slot = "l", name = "avg_npc_1577_1#7$1", focus="l")]
[name="伊西多"]我要的不是这种数据......
[charslot(slot = "r", name = "avg_npc_450_1#1$1",focus="r")]
[name="极境"]放心放心，前面几次实验我都有完整记录下来。小毛毛，过来清理一下桌面。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]好嘞，大人！
[charslot(slot = "m", name = "avg_npc_1577_1#10$1", focus="m")]
[name="伊西多"]为什么她在这里？
[charslot(slot = "m", name = "avg_npc_450_1#6$1",focus="m")]
[name="极境"]作为你的助手，我觉得自己也需要一个助手，放心吧，她人机灵，又勤快，能干很多活。
[Dialog]
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",focus="m")]
[Delay(time=0.5)]
[charslot(slot="l",name="avg_4163_rosesa_1#12$1",action="zoom",poszoom="0.5,0.5",afrom = 0, ato = 0,scale=1.1,duration=0,focus="m",iscopy=true)]
[charslot(slot = "l", posfrom="200,-30",posto="120,-30",afrom = 0, ato = 0.7,duration = 0.7,focus="m", end = true,iscopy=true)]
[name="帕斯卡拉"]（呵，你就把所有事情都塞给我吧......）
[Dialog]
[charslot(slot = "l", posfrom="120,-30",posto="200,-30",afrom = 0.7, ato = 0,duration = 0.7,focus="m", end = true,iscopy=true)]
[charslot(slot="m",name="avg_4163_rosesa_1#7$1",focus="m")]
[Delay(time=1.5)]
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1577_1#7$1", focus="m")]
[name="伊西多"]......
[charslot(slot = "m", name = "avg_npc_450_1#4$1",focus="m")]
[name="极境"]咳咳，小毛毛，去仓库帮我们再拿些鳞油和异铁好吗？
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]没问题，大人！
[Dialog]
[PlaySound(key="$d_avg_walkfast", volume=0.7)]
[charslot(duration=0.7)]
[Delay(time=2)]
[charslot(slot = "l", name = "avg_npc_1577_1#4$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_450_1#1$1",focus="r")]
[name="极境"]她走了......
[charslot(slot = "r", name = "avg_npc_450_1#1$1",focus="r")]
[name="极境"]现在你能告诉我到底遇上什么麻烦了吗？
[charslot(slot = "l", name = "avg_npc_1577_1#4$1", focus="l")]
[name="伊西多"]进展很糟糕......到目前为止造出来的几个实验样本，都不符合标准。
[charslot(slot = "r", name = "avg_npc_450_1#8$1",focus="r")]
[name="极境"]看着挺好的啊，闪闪亮亮的。
[charslot(slot = "l", name = "avg_npc_1577_1#1$1", focus="l")]
[name="伊西多"]不。心相原质存世量如此之少，不是没有原因的。它以高度复杂的结构支撑起了极为夸张的功用。
[name="伊西多"]要么是我手法有误，要么我对心相原质结构的理解从头就是错的。
[charslot(slot = "l", name = "avg_npc_1577_1#4$1", focus="l")]
[name="伊西多"]以我现在这种水平，怎么可能直接去操作真正的心相原质？
[charslot(slot = "r", name = "avg_npc_450_1#1$1",focus="r")]
[name="极境"]你再多造几个实验样本，造到你觉得达标为止？
[charslot(slot = "l", name = "avg_npc_1577_1#1$1", focus="l")]
[name="伊西多"]资源不足，我不能将它们全部用完，万一我失败了......至少还能给他们留下一些。
[charslot(slot = "r", name = "avg_npc_450_1#6$1",focus="r")]
[name="极境"]你又半途就开始考虑失败的事了。拿出点信心来，棘刺。
[multiline(name="极境")]我们合作过那么多次，我相信你会成功的，还有胡安娜女士，还有那个谁......
[charslot(slot = "r", name = "avg_npc_450_1#1$1",focus="r")]
[multiline(name="极境")]呃......谁来着？
[charslot(slot = "r", name = "avg_npc_450_1#6$1",focus="r")]
[name="极境"]啊，总之那个谁......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_dooropen", volume=0.7)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]还有我。
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="m")]
[name="极境"]哟，小毛毛，回来得这么快？
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]我真心希望你们能成功。
[charslot(slot = "m", name = "avg_npc_1577_1#1$1", focus="m")]
[name="伊西多"]你能得到什么好处呢，帕斯卡拉？
[charslot(slot = "m", name = "avg_4163_rosesa_1#3$1",focus="m")]
[name="帕斯卡拉"]可别忘了，这只罗盘可是我带来的，你要是搞砸了，我也没什么好下场。
[charslot(slot = "m", name = "avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]所以，如果你有麻烦，请不要将我支开，我会想办法帮你。
[charslot(slot = "m", name = "avg_npc_1577_1#6$1", focus="m")]
[name="伊西多"]......你没把我再卖一次就算帮我了。
[charslot(slot = "m", name = "avg_4163_rosesa_1#5$1",focus="m")]
[name="帕斯卡拉"]嘁，信不信随你了......
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="m")]
[name="极境"]咳咳，多谢你跑腿，小毛毛，我现在要重新调整塑金台的朝向，辛苦你接着分拣材料了。
[charslot(slot = "m", name = "avg_4163_rosesa_1#1$1",focus="m")]
[name="帕斯卡拉"]知道啦知道啦。
[Dialog]
[charslot(slot="l",name="avg_4163_rosesa_1#12$1",action="zoom",poszoom="0.5,0.5",afrom = 0, ato = 0,scale=1.1,duration=0,focus="m",iscopy=true)]
[charslot(slot = "l", posfrom="200,-30",posto="120,-30",afrom = 0, ato = 0.7,duration = 0.7,focus="m", end = true,iscopy=true)]
[name="帕斯卡拉"]（哼，就知道催！）
[Dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[PlaySound(key="$d_avg_knockdoorfast", volume=0.7)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1577_1#1$1", focus="m")]
[name="伊西多"]请进！
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1580_1#6$1", focus="m")]
[name="蒂奇"]抱歉，打扰你工作了。有件事我需要和你商量下。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="57_g12_alchemyworkshop",screenadapt="showall")]
[charslot(slot = "l", name = "avg_npc_1580_1#6$1")]
[charslot(slot = "r", name = "avg_npc_1577_1#1$1")]
[delay(time=1)]
[PlayMusic(intro="$

... (全文29724字符)
```

### level_act39side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g1_saltdesert_d",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[playsound(key="$d_avg_sandanimaldig")]
[charslot(slot = "m", name = "avg_4163_rosesa_1#9$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_4163_rosesa_1#9$1",focus="m")]
[charslot(slot = "m", action="shake",random=true, power=5, times=60,duration=0.5)]
[name="帕斯卡拉"]唔......唔！
[Dialog]
[charslot]
[playsound(key="$d_avg_sandftsingle")]
[charslot(slot = "m", name = "avg_npc_450_1#12$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_450_1#12$1",focus="m")]
[charslot(slot = "m", action="shake",random=true, power=5, times=60,duration=0.5)]
[name="极境"]唔——！
[charslot(slot = "m", name = "avg_npc_1590_1#1$1",focus="m")]
[name="鲁斯"]好了，你们俩都到这个地步就不要再挣扎了。
[name="鲁斯"]别怪我把你们交给审判庭，说到底我们都不是一路人，各为各的前程而已。
[name="鲁斯"]如果你们愿意安静下来，我就拿开你们嘴里的布团。
[charslot(slot = "m", name = "avg_4163_rosesa_1#8$1",focus="m")]
[name="帕斯卡拉"]（犹豫地点头）
[Dialog]
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_4163_rosesa_1#8$1",focus="m")]
[name="帕斯卡拉"]我不吵......
[charslot(slot = "m", name = "avg_npc_1590_1#5$1",focus="m")]
[name="鲁斯"]你识相最好。
[charslot(slot = "m", name = "avg_4163_rosesa_1#8$1",focus="m")]
[name="帕斯卡拉"]但鲁斯先生，你有没有想过，就算你们把我们和罗盘都交给审判庭，也不一定能有好结果。
[charslot(slot = "m", name = "avg_npc_450_1#11$1",focus="m")]
[name="极境"]对啊......
[name="极境"]你们弟兄的尸体还挂在镇子外面的旗杆上发臭，你真觉得审判庭不会把你们也挂上去吗......？
[charslot(slot = "m", name = "avg_npc_1590_1#2$1",focus="m")]
[name="鲁斯"]......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g11_meetingroom",screenadapt="showall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_chairbump", volume=0.7)]
[PlaySound(key="$d_avg_cardboard", volume=1,delay=0.2)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1579_1#6$2",focus="m")]
[name="哈维尔"]没有......不在这里。
[name="哈维尔"]该死......那枚罗盘到底在哪里？那小子明明每晚炼完之后都会把罗盘送回这里......！
[Dialog]
[charslot]
[PlaySound(key="$d_avg_highheelfts", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_1581_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]你在找这个吗，小哈？
[charslot(slot = "m", name = "avg_npc_1579_1#10$2",focus="m")]
[name="哈维尔"]......
[charslot(slot = "m", name = "avg_npc_1579_1#9$2",focus="m")]
[name="哈维尔"]你不该这个时候回来的，胡安娜。
[charslot(slot = "m", name = "avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]但我怎么觉得，自己回来得刚刚好呢。
[charslot(slot = "m", name = "avg_npc_1579_1#9$2",focus="m")]
[name="哈维尔"]女士，我......没有选择......
[charslot(slot = "m", name = "avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]放下你的刀，小哈，你的刀法都是我教给你的，对上我你没有丝毫胜算。
[charslot(slot = "m", name = "avg_npc_1579_1#6$2",focus="m")]
[name="哈维尔"]或许我该试一试，你身上有伤，说不定打败你也不是那么困难。
[charslot(slot = "m", name = "avg_npc_1581_1#5$1",focus="m")]
[name="胡安娜"]......
[charslot(slot = "m", name = "avg_npc_1581_1#8$1",focus="m")]
[name="胡安娜"]小哈，我不明白，究竟是怎样的不满让你与我走到这一步。
[name="胡安娜"]像今天这般，刀剑相向。
[charslot(slot = "m", name = "avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]我从未对你有过不满，你所做的每个决定我都愿意支持，你的每个想法我都愿意赞同。
[name="哈维尔"]当我的母亲离开我，你牵起我的手，告诉我从此你就是我的家人。
[name="哈维尔"]那时起，我对你就不会有任何不满了，胡安娜。
[charslot(slot = "m", name = "avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]那你又是为了什么呢，小哈？
[charslot(slot = "m", name = "avg_npc_1579_1#5$2",focus="m")]
[name="哈维尔"]为了胡安娜......为了你......
[charslot(slot = "m", name = "avg_npc_1581_1#8$1",focus="m")]
[name="胡安娜"]谎话，我就站在你面前。
[name="胡安娜"]告诉我，你要如何为了我而与我相敌对！
[charslot(slot = "m", name = "avg_npc_1579_1#5$2",focus="m")]
[name="哈维尔"]我知道的胡安娜，不会为了一己私欲让整个船队陷于危难，她是最英勇也最英明的首领，我们可以放心地跟从她。
[name="哈维尔"]你不是我认识的胡安娜，你不过是一个......
[charslot(slot = "m", name = "avg_npc_1581_1#4$1",focus="m")]
[CameraShake(duration=0.3, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="胡安娜"]说出来！
[charslot(slot = "m", name = "avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]不过是一个为找寻往日激情，而忽视摆在面前的真实生活的可怜女人。
[charslot(slot = "m", name = "avg_npc_1581_1#8$1",focus="m")]
[multiline(name="胡安娜")]告诉过你很多次......
[charslot(slot = "m", name = "avg_npc_1581_1#2$1",focus="m")]
[multiline(name="胡安娜")]海洋不是我们的过去，它是我们的未来。
[charslot(slot = "m", name = "avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]那只是你的一厢情愿，船队中已经没人再相信了。我们的父辈已经死去，从他们口中流传出的故事也该一同消失。
[Dialog]
[charslot(slot = "m", name = "avg_npc_1579_1#6$2",focus="m")]
[PlaySound(key="$d_avg_unsheathe",volume=0.7)]
[Delay(time=0.5)]
[name="哈维尔"]把罗盘给我，胡安娜。
[charslot(slot = "m", name = "avg_npc_1581_1#8$1",focus="m")]
[name="胡安娜"]尽管上前来，试试看你能不能拿到。
[charslot(slot = "m", name = "avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]胡安娜......你还不明白吗？
[name="哈维尔"]将罗盘交给审判庭可不是我一意孤行。
[Dialog]
[charslot]
[playsound(key="$whistle_short",volume=0.6)]
[Delay(time=1)]
[PlaySound(key="$d_gen_dooropen", volume=0.7)]
[Delay(time=1)]
[PlaySound(key="$d_avg_crowdrun", volume=1, loop=true, channel="c")]
[StopSound(channel="c", fadetime=2.5)]
[charslot(slot = "l", name = "avg_npc_1591_1#1$1",duration=1)]
[charslot(slot = "r", name = "avg_npc_1592_1#1$1",duration=1)]
[Delay(time=2.5)]
[Dialog]
[charslot]
[playsound(key="$d_avg_swordexsheath")]
[PlaySound(key="$d_avg_exsheath", volume=1,delay=0.1)]
[PlaySound(key="$d_avg_daggerexsheath", volume=1,delay=0.2)]
[PlaySound(key="$d_avg_unsheathe",volume=0.7,delay=0.3)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1581_1#5$1",focus="m")]
[name="胡安娜"]一场哗变......原来等着我的是这个......
[charslot(slot = "m", name = "avg_npc_1581_1#8$1",focus="m")]
[name="胡安娜"]真是惊喜。
[charslot(slot = "m", name = "avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]我只想要罗盘，而他们也只想要一个安稳的未来。
[name="哈维尔"]成全大家，你依然是我们的首领，什么都不会变。
[charslot(slot = "m", n

... (全文24333字符)
```

### level_act39side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g2_saltdesert_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_wind", volume=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_450_1#11$1",duration=0.7)]
[charslot(slot = "r", name = "avg_4163_rosesa_1#8$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_4163_rosesa_1#8$1",focus="r")]
[name="帕斯卡拉"]（小声）难以置信，那女人竟然愿意放我们离开......本来以为修复失败后，我们都会被五花大绑交给审判庭。
[charslot(slot = "l", name = "avg_npc_450_1#11$1",focus="l")]
[name="极境"]（小声）嘘......
[Dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_1581_1#1$1",duration=0.7)]
[charslot(slot = "r", name = "avg_npc_1577_1#4$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1577_1#4$1",focus="r")]
[name="伊西多"]我知道，无论说多少次抱歉，都挽回不了你的损失。
[charslot(slot = "l", name = "avg_npc_1581_1#1$1",focus="l")]
[name="胡安娜"]我想这就是结局了，伊西多。
[name="胡安娜"]安心吧，我不会怪你，这不是你的错。做下选择的时候，我就已经接受了结果。
[charslot(slot = "r", name = "avg_npc_1577_1#4$1",focus="r")]
[name="伊西多"]我知道，是你为我们承受了船员们的愤怒，也是你保下了帕斯卡拉。
[charslot(slot = "r", name = "avg_npc_1577_1#1$1",focus="r")]
[name="伊西多"]......或许你也可以和我们一起走。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_450_1#11$1",focus="m")]
[name="极境"]可以预见，女士，留在这里你会非常危险。
[charslot(slot = "m", name = "avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]快走吧。你们之前不是吵着要跑吗？现在有机会了，怎么还不动身？
[charslot(slot = "m", name = "avg_npc_1577_1#4$1",focus="m")]
[name="伊西多"]......
[charslot(slot = "m", name = "avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]我是船队的首领，我不会抛下我的船员。这是我向科鲁兹立下的誓言，这一辈子我都不会违背它。
[charslot(slot = "m", name = "avg_npc_1577_1#4$1",focus="m")]
[name="伊西多"]胡安娜女士，有样东西......我得还给你。
[charslot(slot = "m", name = "avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]那身衣服和剑你留着吧，就当是给你的酬劳。
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]不是那些......
[charslot(slot = "m", name = "avg_npc_1581_1#5$1",focus="m")]
[name="胡安娜"]那是？
[Dialog]
[charslot]
青年将手伸进衣袋，却突然停住了。他缓缓地吐了口气。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1)]
然后取出了兜里的物件。
[Dialog]
[ShowItem(image="item_act39side_1",fadetime=1)]
[Delay(time=2)]
[HideItem(fadetime=0.5)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1581_1#5$1",focus="m")]
[name="胡安娜"]罗盘？不......
[name="胡安娜"]不......我不明白，如果它还安然无恙，那炼金工坊里那些残骸是......？
[charslot(slot = "m", name = "avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]如果你没在修复罗盘，那这段时间你到底在做什么？！
[charslot(slot = "m", name = "avg_npc_1577_1#6$1",focus="m")]
[name="伊西多"]......
[charslot(slot = "m", name = "avg_npc_1581_1#4$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="胡安娜"]说话啊！
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]实验里毁掉的那个罗盘......是我尝试着复制出来的。真品......我没动。
[charslot(slot = "m", name = "avg_npc_450_1#9$1",focus="m")]
[name="极境"]呼......
[charslot(slot = "m", name = "avg_4163_rosesa_1#15$1",focus="m")]
[CameraShake(duration=0.5, xstrength=15, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="帕斯卡拉"]什么？！我怎么不知道......什么时候的事情？
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]我没告诉任何人......
[charslot(slot = "m", name = "avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]我不明白，你这么做的理由是什么？！
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]罗盘上搭载的心相原质......结构远比我想象的复杂。如果我不能完美地将它复制出来，那说明我很可能仍然没能理解它的本质。
[name="伊西多"]这种情况下贸然去操作真正的心相原质，几乎只可能失败。
[charslot(slot = "m", name = "avg_npc_1577_1#7$1",focus="m")]
[name="伊西多"]但我不能失败。你的期望，整支船队的关注，极境和帕斯卡拉的命运......都在我身上。
[name="伊西多"]后来，我总忍不住去想，如果注定失败，至少我该有办法把损失降到最低。
[name="伊西多"]所以我一直在试图复制心相原质。假如事实证明我没有能力理解心相原质，你们至少还可以带着真品，去找下一位炼金术师。
[name="伊西多"]我还省出了一部分材料，不至于让船队弹尽粮绝。
[charslot(slot = "m", name = "avg_npc_1577_1#4$1",focus="m")]
[name="伊西多"]我、我......
[name="伊西多"]对不起，我确实想尽了办法。
[charslot(slot = "m", name = "avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]伊西多......你觉得这样就算是尽了全力吗？
[charslot(slot = "m", name = "avg_npc_1577_1#4$1",focus="m")]
[name="伊西多"]我算过，失败的概率超过百分之八十七......这是我能想到的最保险的办法。
[charslot(slot = "m", name = "avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]失败并不足以让人畏惧，纵然成功的几率只有万分之一，我也会孤注一掷，倾尽所有去赌一个机会。
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]这是赌博，不是实验。
[charslot(slot = "m", name = "avg_npc_1581_1#11$1",focus="m")]
[name="胡安娜"]哈......比起成功的概率，我们拥有第二次机会的概率才更为渺茫。
[name="胡安娜"]告诉我，我们的人生到底是赌博，还是实验？
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.6)]
[charslot(duration=1)]
[Delay(time=2.5)]
[charslot(slot = "m", name = "avg_npc_1577_1#7$1",focus="m")]
[name="伊西多"]......
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="m")]
[name="极境"]温蒂一会儿会来接我离开，你打算和我们一起走吗？
[charslot(slot = "m", name = "avg_npc_1577_1#7$1",focus="m")]
[name="伊西多"]......我的旅途还没有结束。
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]我会继续下去。
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="m")]
[name="极境"]你呢，帕斯卡拉？和我一起走吗？
[charslot(slot = "m", name = "avg_4163_rosesa_1#11$1",focus="m")]
[name="帕斯卡拉"]我......
[charslot(slot = "m", name = "avg_npc_450_1#11$1",focus="m")]
[name="极境"]走吧，至少我能想办法带你离开这里......
[charslot(slot = "m", name = "avg_4163_rosesa_1#10$1",focus="m")]
[name="帕斯卡拉"]好......伊西多，你保重。
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="m")]
[name="极境"]保重。
[charslot(slot = "m", name = "avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]嗯，你们也是。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="57_g14_ibtown_n",screenadapt="showall")]
[delay(time=1)]
[PlayMusic(intro="$ponder_intro", key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1583_1#2$1",duration=0.7)]
[charslot(slot = "r

... (全文20165字符)
```

### level_act39side_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g9_community_d",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$formal_loop", volume=0.6)]
[PlaySound(key="$burningloop1", volume=1, loop=true, channel="burn")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1577_1#5$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1577_1#5$1",focus="m")]
[name="伊西多"]......
[Dialog]
[charslot(slot="m",name="avg_npc_1577_1#5$1",focus="n")]
[PlaySound(key="$d_avg_slapcloth_light",volume=1)]
[delay(time=0.5)]
[name="？？？"]嘿，小子。
[charslot(slot="m",name="avg_npc_1577_1#10$1",focus="m")]
[name="伊西多"]蒂奇？到底怎么回事？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]哈维尔把审判庭的人引来了，胡安娜夫人被他们关在了船长室。
[charslot(slot="m",name="avg_npc_1577_1#5$1",focus="m")]
[name="伊西多"]......
[charslot(slot = "m", name = "avg_npc_1580_1#6$1",focus="m")]
[name="蒂奇"]你回来干什么？
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]不知道......大概和你的目的一样吧。
[charslot(slot = "m", name = "avg_npc_1580_1#6$1",focus="m")]
[name="蒂奇"]等等......对面甲板上躲着的......是你的朋友吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[StopSound(channel="burn", fadetime=1)]
[charslot]
[Background(image="57_g3_newdeck_1", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_4163_rosesa_1#15$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_4163_rosesa_1#15$1",focus="m")]
[name="帕斯卡拉"]那是伊西多吗？想不到他居然也回来了。
[charslot(slot="m",name="avg_4163_rosesa_1#18$1",focus="m")]
[name="帕斯卡拉"]嘿，我就说嘛，连我都放心不下，更何况他呢。
[charslot(slot="m",name="avg_npc_450_1#4$1",focus="m")]
[name="极境"]我朋友这么好的人，看到这边的火光，当然会回来了！
[charslot(slot="m",name="avgnew_400_weedy_1#5$1",focus="m")]
[name="温蒂"]那我呢？
[name="温蒂"]为什么我也要来？
[charslot(slot="m",name="avg_npc_450_1#8$1",focus="m")]
[name="极境"]呃，来救火？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g11_meetingroom", screenadapt="coverall", block=true)]
[charslot(slot = "l", name = "avg_npc_1587_1#1$1",focus="all")]
[charslot(slot = "r", name = "avg_npc_1587_1#1$1",focus="all")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$fightgeneral", volume=0.6)]
[PlaySound(key="$d_avg_punch", volume=0.9,delay=0.2)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=0.5)]
[Dialog]
[PlaySound(key="$bodyfalldown1", volume=1)]
[PlaySound(key="$bodyfalldown2", volume=1,delay=0.2)]
[charslot(slot="l",afrom=1,ato=0,duration=0.7)]
[charslot(slot="r",afrom=1,ato=0,duration=0.5)]
[Delay(time=0.5)]
[name="习武教士"]唔......
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]醒醒，夫人......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot="m",name="avg_npc_1581_1#6$1",posfrom="0,-50",posto="0,0",afrom=0,ato=1,duration=1)]
[CameraShake(duration=1, xstrength=30, ystrength=15, vibrato=10, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]小珍珠......宝宝呢？你们不该回来的。
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]我把宝宝送回盐漠了，哪怕它身体孱弱，也不是完全没机会挣扎着活下去，至少好过被叛乱的船员宰了。
[name="蒂奇"]我们不能留您一个人在这。
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",focus="m")]
[multiline(name="蒂奇")]您看起来状态不太好......
[charslot(slot = "m", name = "avg_npc_1580_1#2$1",focus="m")]
[multiline(name="蒂奇")]难道他们对您做了什么？！
[charslot(slot="m",name="avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]没有......只是他们给我服了些药剂。
[name="胡安娜"]你们本来可以逃走，可以活下去的。
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]我以为你这样执拗的人不会放弃得那么快。
[charslot(slot="m",name="avg_npc_450_1#11$1",focus="m")]
[name="极境"]既然我们都已经回来了，就别说这些了吧？女士，你是船队里最熟悉盐漠的人，你知道有什么逃跑的好去处吗？
[charslot(slot="m",name="avg_npc_1581_1#8$1",focus="m")]
[name="胡安娜"]我们现在有几个人？
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]二十四个。
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]很好，够我们夺下一艘船离开这里了。
[charslot(slot = "m", name = "avg_npc_1580_1#6$1",focus="m")]
[name="蒂奇"]哪一艘？
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]征服宣告号。
[charslot(slot = "m", name = "avg_npc_1580_1#3$1",focus="m")]
[name="蒂奇"]那艘老船......它的速度可比不上新造的盐船。
[charslot(slot="m",name="avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]但我最熟悉它。
[name="胡安娜"]况且，那艘船很旧，审判庭不会花费太多人力看守，我们夺船的难度不大。
[charslot(slot = "m", name = "avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]好，我带八个人去甲板，巡逻和放哨的我们会解决掉。剩下的人和极境先生从侧舷摸进船舱，搞定其他人。
[charslot(slot="m",name="avg_npc_1577_1#10$1",focus="m")]
[name="伊西多"]我呢？
[charslot(slot = "m", name = "avg_npc_1580_1#4$1",focus="m")]
[name="蒂奇"]胡安娜夫人很虚弱，走不快......这一路，我希望你看着她些。
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]放心，我会的。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="57_g6_olddeck_1", screenadapt="coverall", block=true)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_whlntt", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1591_1#1$1",focus="m")]
[name="警惕的船员"]什么动静？
[Dialog]
[PlaySound(key="$fightgeneral", volume=0.6)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)

... (全文30845字符)
```

### level_act39side_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g14_ibtown_n",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",duration=0.7)]
[charslot(slot = "r", name = "avg_npc_1590_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_npc_1590_1#1$1",focus="r")]
[name="鲁斯"]这个点，不睡觉在外面干什么？你的火把也太晃眼了。
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",focus="l")]
[name="忧虑的海盗"]守夜。
[charslot(slot = "r", name = "avg_npc_1590_1#5$1",focus="r")]
[name="鲁斯"]傻孩子，这是在城镇，不用担心半夜有盐鳞冲进营地，也不会突然刮盐暴把帐篷吹走。
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",focus="l")]
[name="忧虑的海盗"]我知道，我只是不习惯。
[name="忧虑的海盗"]屋子里太热，床也太结实，甚至都不会晃......我睡不着。
[name="忧虑的海盗"]而且，我总觉得不对劲。那个叫西尔弗的证裁官把我们安排在这里？他人呢？怎么不见了？
[charslot(slot = "r", name = "avg_npc_1590_1#1$1",focus="r")]
[name="鲁斯"]碍于身份，不方便与我们直接接触吧。
[name="鲁斯"]镇民们还是对我们抱有戒备，不然也不会特地让我们半夜进镇子，住在镇子里这些空了很久的老房子里。
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",focus="l")]
[name="忧虑的海盗"]我们和他们不一样是人？
[charslot(slot = "r", name = "avg_npc_1590_1#1$1",focus="r")]
[name="鲁斯"]......唉。
[charslot(slot = "r", name = "avg_npc_1590_1#5$1",focus="r")]
[name="鲁斯"]火把给我吧。不放心的话，我在这再盯一会儿。
[name="鲁斯"]你赶紧回去睡。
[name="鲁斯"]镇里的生活，你总要习惯的。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_ibindoor",screenadapt="showall")]
[charslot(slot = "l", name = "avg_npc_1582_1#1$1")]
[charslot(slot = "r", name = "avg_npc_1579_1#5$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1582_1#1$1",focus="l")]
[name="安纳斯塔西奥"]看起来，你们今天吃的还是从船上带来的肉干。
[charslot(slot = "r", name = "avg_npc_1579_1#5$1",focus="r")]
[name="哈维尔"]......
[charslot(slot = "l", name = "avg_npc_1582_1#9$1",focus="l")]
[name="安纳斯塔西奥"]哈维尔先生？
[charslot(slot = "r", name = "avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]啊，是，肉干。
[charslot(slot = "l", name = "avg_npc_1582_1#1$1",focus="l")]
[name="安纳斯塔西奥"]这间厨房虽然已经弃置很久了，但西尔弗特地找人修缮过，里面的厨具应该都能用。
[name="安纳斯塔西奥"]我听闻你一直想当个真正的厨师。为什么有了厨房，反而不做饭？
[charslot(slot = "r", name = "avg_npc_1579_1#1$1",focus="r")]
[name="哈维尔"]我今天做不出来。
[charslot(slot = "l", name = "avg_npc_1582_1#9$1",focus="l")]
[name="安纳斯塔西奥"]这是什么意思？你是觉得，这些还不够？
[charslot(slot = "r", name = "avg_npc_1579_1#1$1",focus="r")]
[name="哈维尔"]够了，够了。我一辈子也没见过这么多厨具。
[charslot(slot = "l", name = "avg_npc_1582_1#9$1",focus="l")]
[name="安纳斯塔西奥"]那究竟是为什么？
[charslot(slot = "r", name = "avg_npc_1579_1#5$1",focus="r")]
[name="哈维尔"]......
[charslot(slot = "l", name = "avg_npc_1582_1#9$1",focus="l")]
[name="安纳斯塔西奥"]我想知道为什么，哈维尔先生。
[charslot(slot = "r", name = "avg_npc_1579_1#5$1",focus="r")]
[name="哈维尔"]做饭的人在做饭的时候，脑子里想的大多不是手里的厨具，而是一会儿要吃饭的人。
[name="哈维尔"]做饭的时候总在想的人不在了，饭也就做不出来了。
[charslot(slot = "l", name = "avg_npc_1582_1#9$1",focus="l")]
[name="安纳斯塔西奥"]你的同伙都在这里了。而如果你说的是先前那场围剿中执意抵抗的人，那我想我们都不必感到惋惜。
[charslot(slot = "r", name = "avg_npc_1579_1#1$1",focus="r")]
[name="哈维尔"]......啧。
[charslot(slot = "l", name = "avg_npc_1582_1#6$1",focus="l")]
[name="安纳斯塔西奥"]你明明得到了许多珍贵之物，这些厨具，这些食材......
[charslot(slot = "r", name = "avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]都是西尔弗准备的，不是你。为什么是你在这说这些鬼话——
[charslot(slot = "l", name = "avg_npc_1582_1#1$1",focus="l")]
[name="安纳斯塔西奥"]他死了。
[charslot(slot = "r", name = "avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]你杀了他......是不是？
[charslot(slot = "l", name = "avg_npc_1582_1#2$1",focus="l")]
[name="安纳斯塔西奥"]我杀了。
[charslot(slot = "r", name = "avg_npc_1579_1#10$1",focus="r")]
[name="哈维尔"]......
[charslot(slot = "l", name = "avg_npc_1582_1#2$1",focus="l")]
[name="安纳斯塔西奥"]......
[charslot(slot = "r", name = "avg_npc_1579_1#9$1",focus="r")]
[name="哈维尔"]那我们呢？你也打算杀了我们吗？
[charslot(slot = "l", name = "avg_npc_1582_1#1$1",focus="l")]
[name="安纳斯塔西奥"]不，我要你们与我走上相同的道路。赎罪的道路。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="57_g13_ibtown_d",screenadapt="showall")]
[delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",duration=0.5)]
[charslot(slot = "r", name = "avg_npc_1590_1#5$1",duration=0.5)]
[delay(time=0.7)]
[charslot(slot = "r", name = "avg_npc_1590_1#5$1",focus="r")]
[name="鲁斯"]睡得好吗？
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",focus="l")]
[name="忧虑的海盗"]不怎么好。屋子太热、床不会晃我努努力都能接受了，可这里墙不漏风！吹不到风我觉得我脸都要僵了。
[charslot(slot = "r", name = "avg_npc_1590_1#5$1",focus="r")]
[name="鲁斯"]知足吧。
[name="鲁斯"]你看看船队里的老家伙，一个两个脸都被风吹歪了。那副面相走在街上，恐怕都要把人吓走。
[name="鲁斯"]你还年轻，还有机会长成个慈眉善目的漂亮姑娘。
[charslot(slot = "l", name = "avg_npc_1589_1#1$1",focus="l")]
[name="忧虑的海盗"]厨房没烟。哈维尔还是不打算做饭吗？
[charslot(slot = "r", name = "avg_npc_1590_1#1$1",focus="r")]
[name="鲁斯"]我会去找他谈。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g13_ibtown_d",screenadapt="showall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]教士们搜遍了你们窝点的每一个角落，并没有发现失窃的罗盘。
[charslot(slot = "m", name = "avg_npc_1579_1#9$1",focus="m")]
[name="哈维尔"]......那么个小玩意，可能已经被烧成灰了吧。
[charslot(slot = "m", name = "avg_npc_1582_1#8$1",focus="m")]
[name="安纳斯塔西奥"]与此事有关的几个重要人物，那个窃取罗盘的女孩，那个盗食镇民遗体的青年，和你们先前的首领......
[charslot(slot = "m", name = "avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]他们带着赃物，藏进了盐漠深处。
[charslot(slot = "m", name = "avg_npc_1579_1#9$1",focus="m")]
[name="哈维尔"]你还要我们去追？
[charslot(slot = "m", name = "avg_npc_1582_1#1$1",focus="m")]
[name="安纳斯塔西奥"]你们比我更了解如何在盐漠中穿行，也更熟悉在逃的几人。
[charslot(slot = "m", name = "avg

... (全文29632字符)
```

### level_act39side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g8_oldcabin",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(key="$m_avg_chasing_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[name="？？？"]伊西多！
[name="伊西多"]......唔......呃！
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="伊西多"]——咳咳咳！！
[Dialog]
[charslot]
[playsound(key="$rungeneral",volume=0.6)]
[charslot(slot="m",name="avg_npc_1581_1#4$2",duration=1)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1581_1#4$2",focus="m")]
[name="胡安娜"]所有人都去甲板上！我来掌舵，帕斯卡拉，你和温蒂看着蒂奇！
[multiline(name="胡安娜")]审判庭的船追上来了，伊西多，快醒来，站起来——
[charslot(slot="m",name="avg_npc_1581_1#6$2",focus="m")]
[multiline(name="胡安娜")]等等，你的胳膊怎么了？
[Dialog]
[charslot]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot="m",name="avg_npc_1577_1#4$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1577_1#4$1",focus="m")]
[name="伊西多"]......我......
[Dialog]
[charslot]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_gunboatscombat", volume=0.6, loop=true, channel="atk1")]
[stopsound(channel="atk1", fadetime=3)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1581_1#8$2",focus="m")]
[name="胡安娜"]——啧，又追上来了，极境，伊西多，还能用剑吗？
[charslot(slot="m",name="avg_npc_450_1#7$1",focus="m")]
[name="极境"]我剑断了，但我用旗子也能打人！
[charslot(slot="m",name="avg_npc_450_1#11$1",focus="m")]
[name="极境"]......唉，谁会在战场上拿旗子当武器啊......
[Dialog]
[charslot(slot = "m", name = "avg_npc_1577_1#4$1",focus="m")]
[charslot(slot ="m", action="shake", power=5, times=40, duration=0.5)]
[Delay(time=1)]
伊西多捂住了自己的右臂，剧痛还没有消退。
[charslot(slot = "m", name = "avg_npc_1577_1#5$1",focus="m")]
[name="伊西多"]一只左手够用了。
[charslot(slot="m",name="avg_npc_1581_1#8$2",focus="m")]
[name="胡安娜"]好——
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g6_olddeck_1", screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_4163_rosesa_1#13$1",focus="m")]
[name="帕斯卡拉"]他们又在装炮弹了！小心！
[Dialog]
[charslot]
风吹来背后盐船上的呐喊。
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
“——开炮！！”
[Dialog]
[playsound(key="$d_avg_shipcannon", volume=1)]
[PlaySound(key="$d_avg_explosion", volume=0.9,delay=0.3)]
[PlaySound(key="$d_avg_bodyfallvalley", volume=1,delay=0.6)]
[CameraShake(duration=3, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[Delay(time=2.5)]
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot="m",name="avg_npc_1581_1#8$2",posfrom="0,-50",posto="0,0",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1581_1#8$2",focus="m")]
[name="胡安娜"]我们还是不够快。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothtrailground", volume=1)]
[charslot(slot = "m", name = "avg_npc_1577_1#5$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_1577_1#5$1",focus="m")]
[name="伊西多"]我们能赶在他们追上之前驶进骸礁峡谷吗？
[charslot(slot="m",name="avg_npc_1581_1#8$2",focus="m")]
[name="胡安娜"]哪怕不能，我也绝不会停船。
[charslot(slot = "m", name = "avgnew_400_weedy_1#6$2",focus="m")]
[name="温蒂"]可是现在船体受损严重......我早上只来得及修补了一部分，刚才那一下几乎打穿了半个船舱！
[charslot(slot = "m", name = "avg_4163_rosesa_1#16$1",focus="m")]
[name="帕斯卡拉"]而且伊西多的炼金装置都炸了，没有罗盘，我们进了骸礁峡谷，还怎么出来？
[Dialog]
[PlaySound(key="$d_avg_hylelive", volume=1)]
[charslot(slot = "m", name = "avg_npc_1577_1#7$1",focus="m")]
伊西多隐约感到手套之下，仍有心相原质在活跃地涌动。
他或许毁了自己的一只手臂，但他没有毁掉所有人的生机与希望。
[charslot(slot = "m", name = "avg_npc_1577_1#6$1",focus="m")]
[name="伊西多"]......总还有办法的。
[Dialog]
[charslot(duration=0.7)]
伊西多望向骸礁峡谷，遍地的骨骸正在他眼中快速放大。
[Dialog]
[MusicVolume(volume=0.3, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g6_olddeck_1",screenadapt="showall")]
[delay(time=1)]
[PlaySound(key="$d_avg_bone_rub", volume=0.9)]
[CameraShake(duration=-1, xstrength=5, ystrength=8, vibrato=30, randomness=90, fadeout=false, block=false)]
[bgeffect(name="$eb_sand02",layer=1,flip = 2)]
[bgeffect(name="$eb_wind",layer=2,flip = 1)]
[MusicVolume(volume=0.6, fadetime=2)]
[playsound(key="$d_avg_sandship_fast", loop=true, channel="bgs2",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_planeshake", volume=0.6)]
[Delay(time=2)]
[PlaySound(key="$d_avg_turnrudder_2", volume=1)]
一千米。
征服宣告号已经无需转向，胡安娜紧握住舵轮，几乎将木柄压出裂缝。
她俯下身子盯着正前方，仿佛那可怖的骸礁峡谷是她的猎物。
[Dialog]
[delay(time=1)]
五百米。
[CameraShake(duration=-1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=false, block=false)]
尖锐的盐粒划过胡安娜的脸颊，留下一道刮痕。
帕斯卡拉在劲风与盐尘中挣扎着挤动眼睛，也只能从缝隙间堪堪瞥见身后迫近的巨帆。
[Dialog]
[delay(time=1)]
一百米！
[CameraShake(duration=-1, xstrength=15, ystrength=15, vibrato=30, randomness=90, fadeout=false, block=false)]
本应是苍白的骨骸被涌动的微生物染成了明亮的赤红。
哪怕在被海水淹没之前，这片土地上也不曾有过如此鲜明的色彩。
[Dialog]
[delay(time=1)]
五十米。
[PlaySound(key="$d_avg_steamburst_big", volume=0.6)]
[PlaySound(key="$d_avg_turnrudder_2",channel="tr1", volume=1,delay=0.1)]
[PlaySound(key="$d_avg_steamburst_big", volume=0.4, channel="1",delay=0.7)]
[PlaySound(key="$d_avg_steamburst_big", volume=1, channel="2",delay=1)]
[CameraShake(duration=-1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=false, block=false)]
蒸汽从骨骸的孔隙中喷涌而出，密集而激烈。
末端，明亮的赤红晕开，像是喷溅在空气中的血雾。
[Dialog]
[m

... (全文41960字符)
```

### level_act39side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g7_olddeck_2",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_steamburst_big", volume=0.6)]
[PlaySound(key="$d_avg_steamburst", volume=0.8,delay=0.4)]
[PlaySound(key="$d_avg_steamburst_big", volume=0.4, channel="1",delay=0.7)]
[PlaySound(key="$d_avg_steamburst_big", volume=1, channel="2",delay=1)]
[PlayMusic(intro="$calamity_intro", key="$calamity_loop", volume=0.6)]
[CameraShake(duration=3.5, xstrength=25, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_450_1#6$1",focus="m")]
[name="极境"]我解决了！我把他们都解决了！......温蒂，你那里需要帮忙吗？
[charslot(slot = "m", name = "avgnew_400_weedy_1#6$2",focus="m")]
[name="温蒂"]不用，我也解决了——只要我刚修好的船别再被撞坏就好！
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="m")]
[name="极境"]好！呼......
[Dialog]
[charslot(slot = "m", name = "avg_npc_450_1#1$1",focus="n")]
[PlaySound(key="$d_avg_sandstormimpact", volume=0.8)]
[PlaySound(key="$d_avg_bone_rub", volume=0.7,delay=0.1)]
[CameraShake(duration=2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_450_1#11$1",focus="m")]
[name="极境"]啧，我这辈子都不会再想去游乐场坐过山车了。
[charslot(slot = "m", name = "avgnew_400_weedy_1#5$2",focus="m")]
[name="温蒂"]等等，极境......你身上刚才还没有这么多血的！......是刚刚的骸骨碎片吗？
[charslot(slot = "m", name = "avg_npc_450_1#11$1",focus="m")]
[multiline(name="极境")]血......？
[charslot(slot = "m", name = "avg_npc_450_1#4$1",focus="m")]
[multiline(name="极境")]没事，为好朋友受点小伤不算什么。棘刺有了想去做的事情，我要全力支持他才行。
[charslot(slot = "m", name = "avgnew_400_weedy_1#5$2",focus="m")]
[name="温蒂"]我先给你包扎一下......棘刺他想做什么？他说过吗？
[charslot(slot = "m", name = "avg_npc_450_1#11$1",focus="m")]
[name="极境"]哎......等时候到了，让他亲口给你说！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g7_olddeck_2", screenadapt="coverall", block=true)]
[charslot(slot = "m", name = "avg_npc_1582_1#7$1",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1582_1#7$1",focus="m")]
[name="安纳斯塔西奥"]啊，伊西多。你想赎自己的罪，想抹消自己对无辜之人产生的影响，将他们送回原本的生活轨迹。
[name="安纳斯塔西奥"]这究竟是你坚定的意志，还是良心的回照？
[name="安纳斯塔西奥"]毕竟，常有罪人在意识到自己已走上绝路时，恸哭着为他被连累的亲友求情......
[charslot(slot = "m", name = "avg_npc_1582_1#2$1",focus="m")]
[name="安纳斯塔西奥"]但这并不代表他真心愧悔。
[charslot(slot = "m", name = "avg_npc_1582_1#7$1",focus="m")]
[name="安纳斯塔西奥"]一个不清楚自己欲望是什么的人，如何能证明，他有能力抑制那欲望，然后去赎那酿成的罪？
[charslot(slot = "m", name = "avg_1039_thorn2_1#5$1",focus="m")]
[name="伊西多"]不。需要抑制欲望的人是你，需要证明自己的人也是你。
[charslot(slot = "m", name = "avg_npc_1582_1#2$1",focus="m")]
[name="安纳斯塔西奥"]......当然，我已说过，欲望无法被杀死。食人的欲望始终活在我的体内，我必须抑制它。
[charslot(slot = "m", name = "avg_npc_1582_1#7$1",focus="m")]
[name="安纳斯塔西奥"]我会亲手剜下自己的血肉，然后将它弃置。
[name="安纳斯塔西奥"]我会证明自己对血肉的渴望能够被抑制，哪怕只是瞬间。
[Dialog]
[charslot]
伊西多清楚地看到，安纳斯塔西奥从领口中露出的那些皮肤，都覆盖着丑陋的疤痕。被剜去又生长出来的血肉，如此难以直视。
[charslot(slot = "m", name = "avg_1039_thorn2_1#5$1",focus="m")]
[name="伊西多"]你说，欲望只会无穷无尽地生长，将越来越多的人拖入深渊。
[charslot(slot = "m", name = "avg_1039_thorn2_1#2$1",focus="m")]
[name="伊西多"]你以此为由，审判过多少人，杀死过多少人？你为什么偏偏相信自己的欲望能被抑制？
[charslot(slot = "m", name = "avg_npc_1582_1#7$1",focus="m")]
[name="安纳斯塔西奥"]因为死亡是一种解脱。
[name="安纳斯塔西奥"]伊西多，在被欲望沾染之前，你还有过正常的生活，行过良善之事。
[name="安纳斯塔西奥"]所以在染上欲望之后，你有资格以死解脱。
[charslot(slot = "m", name = "avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]但我的生命，从最初就是一个错误，从最初就是一种罪孽。
[name="安纳斯塔西奥"]我若是死去，那我这可悲的存在，除了亵渎之外，还能有什么意义？
[charslot(slot = "m", name = "avg_npc_1582_1#6$1",focus="m")]
[name="安纳斯塔西奥"]......所以我必须赎罪。在我的欲望发展到无法抑制的地步之前，我会尽我所能地赎罪。
[Dialog]
[charslot]
安纳斯塔西奥左手的指甲嵌入自己的胸膛，唯有疼痛才能使他感到一丝安定。
[charslot(slot = "m", name = "avg_1039_thorn2_1#5$1",focus="m")]
[name="伊西多"]你甚至在乎自己存在的意义。
[charslot(slot = "m", name = "avg_1039_thorn2_1#2$1",focus="m")]
[name="伊西多"]安纳斯塔西奥，你是真的不配死去，还是太想活着了？
[name="伊西多"]你总在谈论自己“食人的欲望”，可你最根深蒂固的欲望，难道不只是活着？
[name="伊西多"]不论残害自己还是审判别人，你难道不只是为了让所谓“罪孽深重”的自己能安心地活着？
[Dialog]
[charslot(slot = "m", name = "avg_npc_1582_1#9$1",focus="m")]
[Delay(time=0.2)]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(duration=0.3)]
[Delay(time=0.5)]
[Dialog]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[PlaySound(key="$swordtsing1", volume=1,delay=0.2)]
[PlaySound(key="$swordtsing2", volume=1,delay=0.7)]
[PlaySound(key="$swordtsing4", volume=1,delay=0.9)]
[CameraShake(duration=0.5, xstrength=50, ystrength=50, vibrato=60, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Effect(name="$e_slash_cross",y=150,layer = 1)]
[Effect(name="$e_spark_01_mid",y=150,layer = 2)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Effect(name="$e_spark_01_mid",layer = 3)]
[Effect(name="$e_slash_fold_hit",layer = 4)]
[CameraShake(duration=0.2, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.2, block=true)]
[Effect(name="$e_spark_01_mid",y=-180,layer = 5)]
[Effect(name="$e_slash_cross_hit",y=-180,layer = 6)]
[CameraShake(duration=1.2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.7, block=true)]
[delay(time=0.5)]
安纳斯塔西奥为了听取伊西多告解而放缓的攻势，转瞬间便重新凌厉起来。
伊西多每挡下一剑，手臂上的心相原质都会因剧烈的震动而丝丝缕缕地飘浮起来。
[charslot(slot = "m", name = "avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]你不愿告解，那就死。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a

... (全文20387字符)
```

### level_act39side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g8_oldcabin",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_gen_soldiersrun", volume=0.7)]
[charslot(slot = "l", name = "avg_npc_1587_1#1$1",duration=1)]
[charslot(slot = "r", name = "avg_npc_1587_1#1$1",duration=1)]
[delay(time=2)]
[charslot(slot = "l", name = "avg_npc_1587_1#1$1",focus="l")]
[name="习武教士"]找到了！都过来，她们在这里！
[name="习武教士"]举盾，列阵！别让她跑了！
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_4163_rosesa_1#5$1",focus="m")]
[name="帕斯卡拉"]......嘁。
[charslot(slot = "m", name = "avg_4163_rosesa_1#16$1",focus="m")]
[name="帕斯卡拉"]对付我一个人，至于你们这么大的阵仗？而且，谁说我要跑了？
[charslot(slot = "m", name = "avg_4163_rosesa_1#16$1",focus="n")]
这绝不是第一次有审判庭的教士想取帕斯卡拉的性命，但帕斯卡拉打定主意不再转过身逃跑。
[charslot(slot = "m", name = "avg_4163_rosesa_1#13$1",focus="m")]
[name="帕斯卡拉"]——来！
[name="帕斯卡拉"]有本事杀了我！！
[Dialog]
[PlaySound(key="$e_skill_skulsrsword", volume=0.9)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0,r=0.95, g=0.95, b=0.95, fadetime=0, block=true)]
[Blocker(a=1,r=0.95, g=0.95, b=0.95, fadetime=0.05, block=true)]
[charslot(duration=0.4)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.5, block=true)]
[PlaySound(key="$e_skill_skulsrsword", channel="2",volume=0.9)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1,r=0.95, g=0.95, b=0.95, fadetime=0.05, block=true)]
[charslot(slot="l",name="avg_4163_rosesa_1#13$1",posfrom="50,0", posto="50,0",duration=0,isblock=true)]
[charslot(duration=0.4)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.5, block=true)]
[PlaySound(key="$e_skill_skulsrsword",channel="3", volume=0.9)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1,r=0.95, g=0.95, b=0.95, fadetime=0.05, block=true)]
[charslot(slot="r",name="avg_4163_rosesa_1#13$1",posfrom="-50,0", posto="-50,0",duration=0,isblock=true)]
[charslot(duration=0.4)]
[Blocker(a=0, r=0.95, g=0.95, b=0.95, fadetime=0.5, block=true)]
[Delay(time=0.5)]
但她终归不是什么战士，费尽全力也只能在两名习武教士的围攻下勉强躲闪。
可很快，连躲闪的余地也没有了。
[Dialog]
[charslot(slot = "l", name = "avg_npc_1587_1#1$1",posfrom="-70,0", posto="0,0",duration=0.7)]
[charslot(slot = "r", name = "avg_npc_1587_1#1$1",posfrom="70,0", posto="0,0",duration=0.7)]
[PlaySound(key="$d_avg_armour", volume=1)]
[Delay(time=1)]
[PlaySound(key="$d_avg_axeimp", volume=1)]
[CameraShake(duration=1, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
[charslot]
教士们架盾封住了她面前的路，而她身后，是已经站不起来的蒂奇。
[Dialog]
[charslot(slot = "m", name = "avg_4163_rosesa_1#14$1",focus="m")]
[Delay(time=0.2)]
[playsound(key="$sheildimpact",volume=1)]
[CameraShake(duration=2, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[charslot(duration=0.7)]
[Delay(time=1)]
[name="帕斯卡拉"]咳......可惜......
[name="帕斯卡拉"]......我还想着能再见到那几个人贫嘴呢......
[name="帕斯卡拉"]......算了......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="57_g7_olddeck_2",screenadapt="showall")]
[delay(time=1)]
[PlaySound(key="$d_avg_planeshake", volume=0.6)]
[PlaySound(key="$d_avg_steamburst_big", volume=1,delay=0.1)]
[CameraShake(duration=2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_450_1#5$1",focus="m")]
[name="极境"]等等，等等......
[charslot(slot="m",name="avg_npc_450_1#7$1",focus="m")]
[name="极境"]你看见棘刺了吗？他刚刚还在和安纳斯塔西奥打架！
[charslot(slot = "m", name = "avgnew_400_weedy_1#6$2",focus="m")]
[name="温蒂"]......那边只剩下安纳斯塔西奥了。
[Dialog]
[charslot(slot="m",name="avg_npc_450_1#12$1",focus="m")]
[PlaySound(key="$d_avg_originiumcastshort", volume=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avgnew_400_weedy_1#6$2",focus="m")]
[name="温蒂"]极境，停下，你没法在掌舵的同时这样高强度地施放源石技艺！
[name="温蒂"]......极境！
[charslot(slot="m",name="avg_npc_450_1#12$1",focus="m")]
[name="极境"]我得找到他。
[name="极境"]棘刺是在实验室里被炸过多少次都活蹦乱跳，可他终归是肉做的，如果连盐鳞那么结实的东西都要躲着喷发的蒸汽，那他......
[charslot(slot="m",name="avg_npc_450_1#7$1",focus="m")]
[name="极境"]必须尽快找到他！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)] 
[charslot]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1582_1#8$1")]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot = "m", name = "avg_npc_1582_1#8$1",focus="m")]
[name="安纳斯塔西奥"]你结束了他的折磨，拯救了那些可能被他拖入深渊的无辜之人。
[Dialog]
[PlaySound(key="$d_avg_swordy",volume=0.6)]
[delay(time=1)]
像在试探什么似的，安纳斯塔西奥缓缓将剑尖抵上自己的喉咙。
[charslot(slot = "m", name = "avg_npc_1582_1#6$1",focus="m")]
[name="安纳斯塔西奥"]......不，你不配死去。帮助一个到死都认不清自己的欲望的可怜人获得解脱，远不足以让你赎清罪孽。
[name="安纳斯塔西奥"]认清现实，安纳斯塔西奥，你还远远没有根除在这片土地上蔓延的欲望，你当然不配......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_walkfast", volume=1)]
[charslot(slot = "m", name = "avg_npc_1587_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_1587_1#1$1",focus="m")]
[name="习武教士"]......
[name="习武教士"]执裁官阁下！您还好吗？
[charslot(slot = "m", name = "avg_npc_1582_1#9$1",focus="m")]
[name="安纳斯塔西奥"]我无妨。
[name="安纳斯塔西奥"]你们，重新整队，杀掉所有还活着的强盗，夺回两艘船的控制权。
[name="安纳斯塔西奥"]那个胡安娜，我会亲自去杀她。
[charslot(slot = "m", name = "avg_npc_1587_1#1$1",focus="m")]
[name="习武教士"]阁下，那些强盗，您之前不是说要给他们报酬......
[charslot(slot = "m", name = "avg_npc_1582_1#7$1",focus="m")]
[name="安纳斯塔西奥"]他们向我索要报酬时，如同饥饿

... (全文30686字符)
```

### level_act39side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="49_g12_diving",screenadapt="coverall")]
[Delay(time=1)]
[PlaySound(key="$d_avg_jump_water")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[PlaySound(key="$d_avg_underwateramb",volume=0.3,channel="1",loop=true)]
[Subtitle(text="“盐必有其神圣之处，它既存于海中，也存于我等的泪水之中。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
他努力适应水中的昏暗，找寻湖底微弱的金属光泽。
[Dialog]
[PlaySound(key="$d_avg_swiminwater",volume=0.5,channel="2",loop=true)]
划动胳膊，他缓缓向前游动，手指伸入淤泥，只能抓到丝丝水草。
冰冷的湖水在肌肤表面与发间流动，他感到困惑，不知道该如何才能找到那枚金币。
[Dialog]
[Subtitle(text="“不要用眼睛去看，让水流告诉你方向。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
有个声音从岸上传来，隔着湖水，他看不清那人的面容，但温柔亲切的语气让他生出几分相信。
于是他闭上眼，感知水流涌动，水底的图景在他脑海中清晰地绘出——
一枚坚硬的、花纹繁复的金属圆片躺在游弋的水草中。
他抚摸圆片上的花纹，然后攥在手心向水面游去，岸上，那人的面孔愈发清楚。
[Dialog]
[Subtitle(text="“孩子，你找到那枚金币了吗？”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
他摊开掌心，金币上，一个精细的圆形图案被一道横线拦腰分开，恍惚间，他觉得那像是自己未曾谋面的，遥远的海平线。
[Dialog]
[StopSound(channel="1",fadetime=1.5)]
[StopSound(channel="2",fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_piratepet_vo01")]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_clothmovement")]
[Delay(time=1.5)]
[name="伊西多"]唔......
[name="伊西多"]什么味道......又腥又咸......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_towerinside",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$comedy_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_piratepet_vo01")]
[charslot(slot="m",name="avg_npc_1586_1#1$1",focus="m",duration=1.5)]
[Delay(time=2)]
[name="古怪的生物"]哼哧......哼哧......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_clothmovement")]
[charslot(slot="m",name="avg_293_thorns_1#2$1",duration=1.5)]
[Delay(time=2)]
[name="伊西多"]唉......
[charslot(slot="m",name="avg_npc_1586_1#4$1",focus="m")]
[name="古怪的生物"]（吐出舌头）哼......
[charslot(slot="m",name="avg_293_thorns_1#7$1",focus="m")]
[name="伊西多"]不许舔我脸，小家伙，我真的会揍你。
[Dialog]
[PlaySound(key="$d_avg_piratepet_vo02")]
[charslot(slot="m",name="avg_npc_1586_1#4$1",focus="m")]
[charslot(slot = "m", action="jump",power=50,times=1,duration = 0.5,isblock=true)]
[name="古怪的生物"]哼哧......
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]......算了，以后也不会再受你的气。
[Dialog]
[PlaySound(key="$dooropenquite")]
[Delay(time=2)]
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="none")]
[name="粗粝的男声"]小子，你的饭来了，赶紧吃！大姐头等着见你呢！
[Dialog]
[PlaySound(key="$doorclosequite")]
[Delay(time=2)]
[charslot(slot="m",name="avg_293_thorns_1#6$1",focus="m")]
[name="伊西多"]......
[charslot(slot="m",name="avg_293_thorns_1#1$1",focus="m")]
[name="伊西多"]她今天见不到我了。
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[Delay(time=2)]
伊西多扯下房间里的帆布吊床，将盘子中坚硬的面包和小半瓶水包起来。
随即踢开旁边的皮箱，露出底下的洞口。
为了挖掘这条通道，伊西多花费了整整一周。
一旁怪模样的动物凑上来亲昵地叼住伊西多的裤脚，他看着被口水打湿一片的裤脚，叹了口气。
[charslot(slot="m",name="avg_293_thorns_1#3$1",focus="m")]
[name="伊西多"]我绝对不会再回到这里了。
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp")]
[charslot(duration=1.5)]
[Delay(time=2)]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="57_g9_community_d",screenadapt="coverall")]
[Delay(time=2)]
[PlayMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_broadsword_polish",channel="1",volume=1,loop=true)]
[PlaySound(key="$d_avg_crwddiscuss_outside",channel="2",volume=0.3,loop=true)]
[charslot(slot="m",name="avg_npc_1579_1#1$2",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1579_1#1$2",focus="none")]
[name="泼辣的女人"]（口哨）哈维尔，我上个月放在这里的那把刀能取走了吗？
[Dialog]
[charslot(slot="m",name="avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1580_1#2$1",duration=1.5)]
[Delay(time=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="泼辣的女人"]哈维尔！！
[Dialog]
[StopSound(channel="1",duration=1.5)]
[StopSound(channel="2",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1579_1#8$2",focus="m")]
[name="哈维尔"]哦......抱歉，蒂奇，我没听到你在说话。你是来取刀的吗？
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]不然呢？难道来看你被汗打湿的胸膛吗？
[charslot(slot="m",name="avg_npc_1579_1#2$2",focus="m")]
[name="哈维尔"]你们不该总开这样的玩笑，蒂奇。
[charslot(slot="m",name="avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]别这么说嘛，你清晨起来磨刀的身影已经是这里的一道风景了。
[name="蒂奇"]看看这四周围过来的人......他们可不像来请你磨刀的。
[Dialog]
[charslot]
[name="旁观的男人"]（抛媚眼）嗨，哈维尔！
[charslot(slot="m",name="avg_npc_1579_1#9$2",focus="m")]
[name="哈维尔"]真是胡闹......拿着吧，蒂奇，这是你的刀。
[charslot(slot="m",name="avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]我们不剩多少金属能修补武器了，只能想点其他办法，这阵子你先将就用吧。
[charslot(slot="m",name="avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]骨头和贝壳？真是个手巧的家伙。
[charslot(slot="m",name="avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]要试刀吗？
[charslot(slot="m",name="avg_npc_1580_1#1$1",focus="m")]
[name="蒂奇"]你这里有什么坚硬的食材可以试刀吗？
[charslot(slot="m",name="avg_npc_1579_1#7$2",focus="m")]
[name="哈维尔"]本来还有一块干面包......但刚刚送去给棚屋里的小子了。
[charslot(slot="m",name="avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]浪费。
[Dialog]
[charslot]
[PlaySound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_1590_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="？？？"]让一让，让一让，你们大清早没事情做吗？堵在这里干什么！
[charslot(slot="m",name="avg_npc_1579_1#1$2",focus="m")]
[name="哈维尔"]鲁斯？
[charslot(slot="m",name="avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]原来是你，我就说一大早，太阳那么刺眼。
[c

... (全文32664字符)
```

### level_act39side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g8_oldcabin",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$calm_loop", volume=0.6)]
[PlaySound(key="$d_avg_woodenship_cabin", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
太阳落了下去，盐漠的晚上冷到所有人都在颤抖。
大家翻遍了破落的船舱，才勉强找到了一些不知放了多久的鳞肉干和一口破锅。
在仿生海龙的帮助下，锅中终于有了一点热气。
[Dialog]
[PlaySound(key="$d_avg_dishes", volume=1)]
[delay(time=1)]
[PlaySound(key="$d_avg_plateplace", volume=1)]
[delay(time=1)]
[charslot(slot="m",name="avgnew_400_weedy_1#5$1",focus="m")]
[name="温蒂"]太冷了......之前那些碎木头没撑多久，都已经烧完了，我让小叶先来代替一下火盆吧。
[name="温蒂"]只是本来它的加热功能是用来暖手的，如果是烹煮食物的话，只能做到这种程度了......
[charslot(slot="m",name="avg_npc_450_1#6$1",focus="m")]
[name="极境"]能吃到热的已经很伟大了！
[charslot(slot="m",name="avg_npc_1581_1#6$1",focus="m")]
[name="胡安娜"]食物和淡水都不多，就算省着吃，这些也只能撑上两三天。
[name="胡安娜"]要是遇到雨云，把集雨用的布袋放出去，估计还能再收回来一点水......但盐漠里的天气向来难以预料。
[charslot(slot="m",name="avg_npc_1577_1#10$1",focus="m")]
[name="伊西多"]外面喷发的那些蒸汽......不能当作水源吗？
[charslot(slot="m",name="avg_npc_1581_1#2$1",focus="m")]
[name="胡安娜"]那里面混杂着盐漠深处的微生物，人不能直接喝。
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]我可以提纯。
[charslot(slot="m",name="avg_npc_1581_1#10$1",focus="m")]
[name="胡安娜"]你先修复罗盘。
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]......
[charslot(slot = "m", name = "avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]哈哈，我们先熬过今晚再说吧。
[name="蒂奇"]盐漠深处的夜晚可不是闹着玩的，吃的本来就不够，有人还受了伤，不好好保暖的话，小心睡着睡着人就再也醒不过来了。
[charslot(slot="m",name="avg_4163_rosesa_1#3$1",focus="m")]
[name="帕斯卡拉"]......真的......真的会再也醒不过来了吗？
[name="帕斯卡拉"]要是现在再遇上盐鳞，我们可能真的就......
[charslot(slot="m",name="avg_npc_450_1#6$1",focus="m")]
[name="极境"]没事，我可以发挥特长，先给盐鳞传通讯，就说我们来了，让它们准备乖乖受死。
[charslot(slot="m",name="avg_4163_rosesa_1#5$1",focus="m")]
[name="帕斯卡拉"]......我真不懂，你怎么不管什么时候都能这么没心没肺的？
[charslot(slot="m",name="avgnew_400_weedy_1#1$1",focus="m")]
[multiline(name="温蒂")]......忍忍吧，这个时候也就他会贫嘴了......
[charslot(slot="m",name="avgnew_400_weedy_1#4$1",focus="m")]
[multiline(name="温蒂")]啊，小心！
[musicvolume(volume=0.3, fadetime=1)]
[Dialog]
[charslot]
[PlaySound(key="$d_avg_planeshake", volume=0.6)]
[CameraShake(duration=2, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2.5)]
似乎是轧过了一条骸骨，征服宣告号颠簸了起来，破锅与里面的食物一同被震飞。
极境一个激灵冲上前去接锅，却被烫得哀嚎。
伊西多垫步上前，剑尖精准地穿过锅的把手，这才勉强保住晚餐。
一旁，仿生海龙的热气也消散了。
[musicvolume(volume=0.6, fadetime=1)]
[charslot(slot="m",name="avgnew_400_weedy_1#5$1",focus="m")]
[name="温蒂"]加热功能......坏了，等我先修一下......！
[charslot(slot="m",name="avg_4163_rosesa_1#9$1",focus="m")]
[charslot(slot = "m", action="shake",random=true, power=5, times=50,duration=0.4)]
[multiline(name="帕斯卡拉")]嘶......嘶......好冷......
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="帕斯卡拉")]阿嚏！
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]我可以炼些简单的发热物质，应该不会花太久......
[charslot(slot="m",name="avg_npc_1581_1#1$1",focus="m")]
[name="胡安娜"]那些材料，用来修罗盘。取暖的事，我来想办法。
[charslot(slot="m",name="avg_4163_rosesa_1#9$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="帕斯卡拉"]......阿嚏！......阿嚏！
[name="帕斯卡拉"]......姐姐，能不能再分我一点毯子，我人小，冷得快，真的快要冻死了......
[charslot(slot="m",name="avgnew_400_weedy_1#5$1",focus="m")]
[name="温蒂"]我......
[charslot(slot = "m", name = "avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]这种时候就别什么你的我的了，都挤到一块！伊西多，别在那边发愁了，过来吧！
[charslot(slot="m",name="avg_npc_450_1#4$1",focus="m")]
[multiline(name="极境")]能和我这样的大帅哥挤在一起......
[charslot(slot="m",name="avg_npc_450_1#5$1",focus="m")]
[CameraShake(duration=0.3, xstrength=12, ystrength=15, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="极境")]唔！毯子盖住我的头了！
[charslot(slot="m",name="avg_npc_1577_1#9$1",focus="m")]
[name="伊西多"]......
[Dialog]
[charslot(duration=0.3)]
[delay(time=0.5)]
[Background(image="38_g21_skystarry_L2",screenadapt="coverall",fadetime=2,block=true)]
[delay(time=1)]
胡安娜挡在风口，帕斯卡拉被蒂奇裹好，只露出一张被挤成一团的脸。
极境和温蒂努力活动着僵硬的手指，好抓起食物送进嘴里。
伊西多想要转身回到塑金台，但在拿起探针的那一刻，他意识到，自己冻僵的手指毫无用处。
征服宣告号漫无目的地顺风行驶着。
[Dialog]
[stopmusic(fadetime=1.5)]
[Background(image="57_g8_oldcabin",screenadapt="coverall",fadetime=2,block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_4163_rosesa_1#8$1",focus="m")]
[name="帕斯卡拉"]呼......我们现在要往哪里去？
[charslot(slot="m",name="avg_npc_1577_1#1$1",focus="m")]
[name="伊西多"]不知道，往深处开吧。
[playMusic(key="$saferoom_loop", volume=0.6)]
[charslot(slot="m",name="avg_4163_rosesa_1#9$1",focus="m")]
[name="帕斯卡拉"]......
[name="帕斯卡拉"]不知道我们要去哪里......
[name="帕斯卡拉"]不知道那些臭念经的什么时候追上来......
[name="帕斯卡拉"]也不知道这么冷，我会不会就醒不过来了，或者是船又撞上什么东西......
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[charslot(slot="m",posfrom="0,0",posto="0,-30",afrom=1,ato=0,duration=1)]
[delay(time=1.5)]
[name="帕斯卡拉"]......
[charslot(slot="m",name="avg_npc_450_1#11$1",focus="m")]
[name="极境"]......她怎么突然这样了？
[name="极境"]她不该早早抢一个最暖和的位置睡下吗？说不定还会半夜抢我们所有人的毯子。
[charslot(slot = "m", name = "avg_npc_1580_1#5$1",focus="m")]
[name="蒂奇"]她也就是个十岁刚出头的小丫头。
[charslot(slot="m",name="avg_npc_1581_1#2$1",focus="m")]
[name="胡安娜"]唉......
[charslot(slot="m",name="avg_npc_1581_1#12$1",focus="m")]
[name="胡安娜"]她睡着了，还有点发烧，看看她的口袋里有没有什么能用的草药。
[Dialog]
[charslot]
[name="帕斯卡拉"]要是明天我就要死在这里了......我还、我还想回我原先的家再睡一觉......
[name="帕斯卡拉"]大房子还在......我的床、我的被子、我的浴缸......
[name="帕斯卡拉"]穿最好看的衣服，一套又一套......！
[name="帕斯卡拉"]吃不完的食物，花不完的钱，我不用再......被人一脚踢出去......
[name="帕斯卡拉"]被人踢好疼......从街这头滚到街那头，好疼......我只想回一趟家......
[name="帕斯卡拉"]我要过上好日子......！
[name="帕斯卡拉"]我不要死在......死在......
[Dialog]
[delay(time=1)]
[name="帕斯卡拉"]......呼......
[name="帕斯卡拉"]......
[charslot(slot="m",name="avg_npc_450_1#2$1",focus="m")]
[name="极境"]......
[name="极境"]我没想到这次居然会走到这么危险的地步......抱歉，温蒂，我不该轻易地让你过来......
[charslot(slot="m",name="avgnew_400_weedy_1#7$1",focus="m")]
[name="温蒂"]我既然来了，就是来帮你们的。
[charslot(slot="m",name="avg_npc_450_1#1$1",focus="m")]
[nam

... (全文17813字符)
```

### level_act39side_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="57_g13_ibtown_d",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Subtitle(text="半个月后", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_1579_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="哈维尔"]只剩下这一艘完好的盐船，其他的多多少少都有受损，但大部分构件和材料都能拆下来用。
[name="哈维尔"]这本是盐船的设计图纸，上面边边角角地附带点开船技巧。这张是盐漠地图。
[charslot(slot="m",name="avg_npc_1256_1#1$1",focus="m")]
[name="兴奋的商人"]哈哈哈，好，我都要！要是真的能从盐漠里走，商队能省不少时间！
[name="兴奋的商人"]你出个价吧，我们爽快点！
[charslot(slot="m",name="avg_npc_1590_1#1$1",focus="m")]
[name="鲁斯"]这个数，要全用多布隆金币结。
[charslot(slot="m",name="avg_npc_1256_1#1$1",focus="m")]
[name="兴奋的商人"]哈哈，没问题！
[Dialog]
[PlaySound(key="$d_avg_clothmovement")]
[Delay(time=1.5)]
[name="兴奋的商人"]给，你看看，钱是不是对的？
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[name="哈维尔"]嗯......没错。
[charslot(slot="m",name="avg_npc_1256_1#1$1",focus="m")]
[name="兴奋的商人"]好！那我先走了，你们继续忙！
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1590_1#6$1",focus="m")]
[name="鲁斯"]这人怎么这么爽快......哈维尔，我是不是要少了？
[charslot(slot="m",name="avg_npc_1579_1#7$1",focus="m")]
[name="哈维尔"]......
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[name="哈维尔"]嘿，等等！
[Dialog]
[charslot]
[name="兴奋的商人"]呃......怎么了？
[Dialog]
哈维尔追上去两步，顺着绳子爬上了甲板。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[charslot]
[Background(image="57_g3_newdeck_1",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[name="哈维尔"]这个舵轮我留下了！多少钱？我退给你！
[charslot(slot="m",name="avg_npc_1256_1#1$1",focus="m")]
[name="商人"]哦，哦，舵轮啊！这可是一艘船上最重要的东西呢。
[name="商人"]你想要拿回去？那我要——
[name="商人"]这个数。
[charslot(slot="m",name="avg_npc_1579_1#9$1",focus="m")]
[name="哈维尔"]......
[charslot(slot="m",name="avg_npc_1256_1#1$1",focus="m")]
[name="商人"]哎，表情别这么难看啊，老兄！刚刚交易已经达成了，它们现在是我的船了，对吧？
[name="商人"]公平交易嘛，看它在你心里值不值得这个价了！
[charslot(slot="m",name="avg_npc_1579_1#7$1",focus="m")]
[name="哈维尔"]......算了......
[charslot(slot="m",name="avg_npc_1256_1#1$1",focus="m")]
[name="兴奋的商人"]可惜啊，那下次有机会再交易咯。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Dialog]
[charslot]
[Background(image="57_g13_ibtown_d",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_1579_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[name="哈维尔"]——船员们！都过来吧！
[name="哈维尔"]这些就是刚刚卖盐船得来的钱，我们平分，一人一份。
[name="哈维尔"]拿了这笔钱，就去干你们自己想干的事情吧。
[name="哈维尔"]给，鲁斯，你的份。
[charslot(slot="m",name="avg_npc_1590_1#6$1",focus="m")]
[name="鲁斯"]......
[charslot(slot="m",name="avg_npc_1579_1#10$1",focus="m")]
[name="哈维尔"]怎么了？
[charslot(slot="m",name="avg_npc_1590_1#6$1",focus="m")]
[name="鲁斯"]说实在的，我还没有想好我接下来要去做什么。
[charslot(slot="m",name="avg_npc_1579_1#2$1",focus="m")]
[name="哈维尔"]做个决定，很简单的事情。
[charslot(slot="m",name="avg_npc_1590_1#2$1",focus="m")]
[name="鲁斯"]......之前，我想的是离开胡安娜，安稳点。后来我觉得你也是个疯子，跟着你也不会安稳。
[name="鲁斯"]现在我站在这个镇子里，看着镇上这些人，又瘦又干，眼睛里一点光都没有......这里过的真是安稳日子吗？
[name="鲁斯"]如果我不在这里，去别的地方，以我那些海盗本事，能过得上安稳的日子吗？
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[name="哈维尔"]......
[charslot(slot="m",name="avg_npc_1590_1#2$1",focus="m")]
[name="鲁斯"]说出来不怕你笑话，我其实挺佩服蒂奇的。她比我大几岁，一直都很有主见。
[name="鲁斯"]那天，我看到她伤成那样，还是打定主意要跟着胡安娜出海......真犟啊......也真够厉害，我可能就没这个胆子。
[charslot(slot="m",name="avg_npc_1590_1#5$1",focus="m")]
[name="鲁斯"]哈哈......不说我了。你呢，哈维尔？
[charslot(slot="m",name="avg_npc_1579_1#2$1",focus="m")]
[name="哈维尔"]我应该会换个地方开个餐馆吧。
[charslot(slot="m",name="avg_npc_1590_1#5$1",focus="m")]
[name="鲁斯"]唔......就这样吧，抽完这支烟，我也就上路了。
[name="鲁斯"]人嘛......谁又能知道呢？
[Dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2)]
盐船逐渐远去，哈维尔望着那白色的风帆和鲁斯的背影一并消失在视线里。
[Dialog]
[charslot(slot="m",name="avg_npc_1579_1#1$1",focus="m")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1579_1#2$1",focus="m")]
[Delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2)]
他把自己的那份钱收进口袋，向着下一个路口，走远了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Dialog]
[charslot]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4163_rosesa_1#10$1",focus="m")]
[name="帕斯卡拉"]喂，这个多少钱？
[charslot(slot="m",name="avg_npc_006",focus="m")]
[name="车队的商贩"]一个银币。
[charslot(slot="m",name="avg_4163_rosesa_1#10$1",focus="m")]
[name="帕斯卡拉"]这个呢？
[charslot(slot="m",name="avg_npc_006",focus="m")]
[name="车队的商贩"]也是一个银币。
[charslot(slot="m",name="avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]唔，不贵嘛！
[name="帕斯卡拉"]那这个、这个和这个，都给我包起来，放到我后面这辆车上。
[charslot(slot="m",name="avg_npc_006",focus="m")]
[name="车队的商贩"]好嘞！哎呦，您买这么多东西，这是要去哪啊？
[charslot(slot="m",name="avg_4163_rosesa_1#8$1",focus="m")]
[name="帕斯卡拉"]我想要就买了，怎么了？
[charslot(slot="m",name="avg_npc_006",focus="m")]
[name="车队的商贩"]没怎么，您看到什么想要的直接和我说就好！我都包好了送您车上！
[charslot(slot="m",name="avg_4163_rosesa_1#7$1",focus="m")]
[name="帕斯卡拉"]哼哼，这还差不多。
[charslot(slot="m",name="avg_4163_rosesa_1#6$1",focus="m")]
[name="帕斯卡拉"]嗯......买了衣服买了首饰还买了各种小玩意......怎么还是感觉少点什么......
[name="帕斯卡拉"]唔......少点什么呢......
[Dialog]
[charslot(slot="m",name="avg_4163_rosesa_1#6$1",focus="none")]
[name="车队成员A"]（小声）......对啊，你也很震惊吧！
[name="车队成员B"]（小声）但我怎么知道会这样啊？天啊......
[charslot(slot="m",name="avg_4163_rosesa_1#4$1",focus="m")]
[name="帕斯卡拉"]（......嗯？他腰带上的那个卡扣真好看啊......亮闪闪的.....

... (全文18144字符)
```

### training_act39side_01_a

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_a

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_doberm")]那艘盐船越靠越近了，海盗随时可能尝试跳帮，做好迎击准备！
[Battle.Pause(pause=false)]
```

### training_act39side_01_b

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_b

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_fang")]有人直接跳进盐漠追过来了！
[PopupDialog(dialogHead="$avatar_doberm")]在盐漠中徒步行进并不容易，即使是这些在盐漠出生长大的海盗，也无法行动自如。
[Battle.Pause(pause=false)]
```

### training_act39side_01_c

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_c

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[Tutorial(dialogHead="$avatar_doberm",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]除了坚实的板结盐层，盐漠中也有细碎的流盐，如果在盐漠中停留太久，他们也会<@tu.kw>失足陷入其中</>。
[Tutorial(dialogHead="$avatar_doberm",dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]如果不是急于追击又无路可走，恐怕他们也不会轻易踏入盐漠。
[Battle.Pause(pause=false)]
```

### training_act39side_01_d

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_d

[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(tileX=6, tileY=3, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_doberm", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")]注意！那个海盗在尝试架设悬索桥！
[Battle.Pause(pause=false)]
```

### training_act39side_01_e

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_e

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]
[PopupDialog(dialogHead="$avatar_doberm")]果然，架好之后，他们改变了路线，要通过悬索桥进攻了！
[PopupDialog(dialogHead="$avatar_beagle")]我来拦住他们！
[PopupDialog(dialogHead="$avatar_melan")]我去打倒那个架桥的海盗。
[Battle.Pause(pause=false)]
```

### training_act39side_01_f

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_f

[Battle.SwitchToDefaultUIState]
[Battle.Delay(time=0.5)]
[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[Tutorial(tileX=2, tileY=1, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_doberm")]注意！有海盗空降到了阵线后方！
[Tutorial(tileX=6, tileY=1, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_doberm")]那艘盐船上搭载的“盐坨子炮”除了发射炮弹，似乎也能发射<@tu.kw>重量较轻</>的海盗。
[Tutorial(tileX=6, tileY=1, focusWidth=120, focusHeight=120, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=2, dialogHead="$avatar_doberm")]“盐坨子炮”不仅结构坚实，也<@tu.kw>不容易被瞄准</>，我们暂时没有足够的火力摧毁它。

[PopupDialog(dialogHead="$avatar_firwhl")]火力支援就位！

[Battle.Pause(pause=false)]
```

### training_act39side_01_g

```
[HEADER(is_tutorial=true, is_skippable=false)]  活动39side教学关_g

[Battle.Pause]
[InputBlocker(blockInput=true, black=0.3)]

[PopupDialog(dialogHead="$avatar_firwhl")]啊，正面攻击的效果好差。
[PopupDialog(dialogHead="$avatar_utage")]从后面砍掉就好了~

[Battle.Pause(pause=false)]
```


## 统计

- 总字符数：539240
- 对话行数：3491


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
