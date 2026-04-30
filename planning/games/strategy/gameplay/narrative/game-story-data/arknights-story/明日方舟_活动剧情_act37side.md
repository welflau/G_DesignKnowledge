# 明日方舟 · 活动剧情 · act37side（24段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act37side」完整剧情脚本（24个文件，3105行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act37side
- 脚本文件数：24

### level_act37side_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="27_g7_subway",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_cavewaterdrop", volume=0.3, loop=true, channel="a")]
[playMusic(intro="$darkness02_intro", key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>伦蒂尼姆废弃工厂</><p=2>1098年12月8日 4:43 P.M. </>
[delay(time=3)]
[animtextclean]
[SoundVolume(channel="a", volume=0.7, fadetime=2)]
[delay(time=1)]
[PlaySound(key="$d_avg_openftstprun", volume=1, loop=true, channel="b")]
[StopSound(channel="b", fadetime=2)]
[charslot(slot="m",name="avg_npc_243",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="镇定的女士"]G12区......看上去废弃了段时间，连编号都看不清......是这吗？
[name="镇定的女士"]呼——千万别再撞上那些该死绝的魔族佬——
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_399_1#1$1", duration=0.5)]
[charslot(slot = "r", name = "avg_npc_399_1#1$1", duration=0.5)]
[delay(time=0.7)]
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="谨慎的佣兵"]女士，我想你迷路了。
[name="谨慎的佣兵"]（喂，新来的，把她送走。顺便“温柔地”问问她怎么找到这的。）
[name="谨慎的佣兵"]（记住，这次把尾巴打扫干净。别让老大再发火。）
[charslot(slot="r",name="avg_npc_399_1#1$1",focus="r")]
[name="疲惫的佣兵"]唉，你也听到了。跟我来，女士——
[dialog]
[PlaySound(key="$d_avg_runstop", volume=1)]
[charslot(slot="r", afrom=1,ato=0,duration=0.7)]
[delay(time=1)]
[charslot]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[delay(time=1)]
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_243",focus="m")]
[PlaySound(key="$d_avg_slap", volume=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="镇定的女士"]放开我的手！
[name="镇定的女士"]你们连对女士的基本尊重都没有吗？
[name="镇定的女士"]米基·罗宾森，典范军的英雄......呃，“之一”，也就是我的先生，委托我来取药。
[name="镇定的女士"]缓、缓解那些可怕黑石子病的药。我先生快走不了路了......
[dialog]
[charslot]
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_399_1#1$1",focus="r")]
[name="疲惫的佣兵"]呵，又一个倒霉蛋——
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="谨慎的佣兵"]闭嘴。
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="谨慎的佣兵"]听好了，我没听说过什么米基。
[name="谨慎的佣兵"]这鬼地方你只能找到流浪者的过期致幻剂和死掉魔族佬的骨头棒子。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="镇定的女士"]可——
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="谨慎的佣兵"]还有，想要治矿石病的药，去新建的疗养院里找，这事还是那位新任的议长大人承诺的。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="镇定的女士"]——等等，我们确实没有其他办法了，那里的药根本不够分。
[name="镇定的女士"]我知道这儿能拿到药，我丈夫他......
[name="镇定的女士"]听着，我存了些值钱玩意儿在一个很安全的地方，都是那个坎伯兰公爵府上的好东西，以前公爵阁下赏我们的。只要能拿到药——
[dialog]
[charslot]
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[charslot(slot="r",name="avg_npc_399_1#1$1",focus="l")]
[name="谨慎的佣兵"]别引起外面巡逻的城防军注意。
[charslot(slot="r",name="avg_npc_399_1#1$1",focus="r")]
[name="疲惫的佣兵"]走吧，“女士”。
[dialog]
[charslot(slot="r",name="avg_npc_399_1#1$1",focus="n")]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[delay(time=1)]
[name="终端里的声音"]把单子给她签字，让她明天来拿药。
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="谨慎的佣兵"]是，老大！可万一她没钱......
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="n")]
[name="终端里的声音"]那就老办法。
[dialog]
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="n")]
[PlaySound(key="$transmission")]
[delay(time=2)]
[charslot(slot="r",name="avg_npc_399_1#1$1",focus="r")]
[name="疲惫的佣兵"]奇了怪了，老大好像从来没直接管过这档子事呀。呃，那我现在......？
[charslot(slot="l",name="avg_npc_399_1#1$1",focus="l")]
[name="谨慎的佣兵"]哼，给她合同。
[dialog]
[charslot]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="镇定的女士"]谢谢，谢——这上面的条款，他从来没提过有这么苛刻的条件！要是签了这东西，那我们......
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="谨慎的佣兵"]会活得很好，至少在我们讨债之前。
[name="谨慎的佣兵"]看来你那位英雄丈夫对自己的妻子不太坦诚。
[name="谨慎的佣兵"]来，笔拿稳，别抖。要实在不行，我们可以代签。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[charslot(slot = "m", action="shake",random=true, power=5, times=20,duration=0.3)]
[name="镇定的女士"]——
[dialog]
[charslot]
佣兵死死握住了她拿笔的手，她抖得厉害，方才的镇定再也装不下去了。
她闭上了眼，咬紧牙，任凭佣兵引导她的手。
[dialog]
[PlaySound(key="$d_avg_writerub",volume=1,channel="wr",loop=false)]
[stopsound(channel="wr",fadetime=1.5)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="谨慎的佣兵"]享受活着的每一天吧，*维多利亚粗口*的战争结束了。
[name="谨慎的佣兵"]找“铣痕”求助会是您和您先生最明智的决定，女士。
[Dialog]
[stopmusic(fadetime=2)]
[stopsound(channel="a",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="55_g8_siegeoffice", screenadapt="coverall", block=true)]
[delay(time=1)]
[playMusic(intro="$loneliness_intro",key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_oldtvelectricity", volume=0, loop=true, channel="o")]
[SoundVolume(volume=1, channel="o", fadetime=2)]
[name="广播声"]伦蒂尼姆临时公共卫生行政官兼临时物资筹备主任梅杰女士今晨被发现于新奥克特里格区的公共办公室中去世。
[name="广播声"]亚历山德莉娜议长阁下在今日代表议会，对梅杰女士的感染者帮扶工作表达认可，并哀悼她的离去。
[name="广播声"]梅杰女士逝世前的最后一项日程是前往诺曼底公爵领商谈药物采买，以缓解城内药物短缺的困境。
[name="广播声"]但据可靠的消息来源称，梅杰女士死于矿石病急性发作。
[name="广播声"]她不仅隐瞒了自己感染矿石病的实情，还在近期内被频繁目击到与议长发生争执。
[name="广播声"]在城内上报的感染者数字呈指数增长的敏感时期，失去世袭爵位的梅杰女士离世背后显然还有更多值得挖掘的内幕消息。
[name="广播声"]萨卡兹撤军两个月后的现在，萨卡兹相关恶性事件为何仍然频频发生？
[name="广播声"]而典范军，这支传奇队伍的安置方案是否已有定论？
[name="广播声"]所有人的目光都聚焦在那位得到绝大多数公爵支持的新任议长身上。
[name="广播声"]我们特意联系了与议长关系匪浅的凯特·莫瑞根女士，进一步挖掘了——
[Dialog]
[PlaySound(key="$d_avg_button", volume=1)]
[StopSound(channel="o", fadetime=1)]
[delay(time=1)]
议长办公室内的广播声戛然而止。
[Dialog]
[charslot(slot="m",name="avg_npc_405_1#11$1",focus="m")]
[PlaySound(key="$gavel2", volume=1)]
[CameraShake(duration=1, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="摩根"]这些人真是胡说八道！
[name="摩根"]他们明明就蹲守在疗养院的食堂，故意等我吃饭的时候凑上来套话......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_1019_siege2_1#1$1

... (全文24084字符)
```

### level_act37side_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g2_westlobbyhall",screenadapt="coverall", block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.5, fadetime=0)]
[Delay(time=1)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣王会西部大堂</><p=2>1098年10月8日 7:28 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
战事刚刚平定之时
[dialog]
[charslot(slot="m",name="avg_npc_1518_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1518_1#1$1",focus="m")]
[name="“小公爵”"]二十六年前，这里还是一个辉煌的地方。
[name="“小公爵”"]那会儿我们头顶上的穹顶擦得锃亮，双月的辉光和迷人的黯淡星空是通宵舞会上最美的景色。
[charslot(slot="m",name="avg_npc_1518_1#4$1",focus="m")]
[name="“小公爵”"]我还曾在这里亲吻过那位陛下的手背呢。“向阿利斯泰尔陛下致敬”，这可是一件难得的殊荣。
[dialog]
[charslot]
[PlaySound(key="$d_avg_walk_stage", volume=1,loop="false", channel="ww")]
[stopsound(fadetime=2, channel="ww")]
[charslot(slot="m",name="avg_1019_siege2_1#2$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]维多利亚已经没有国王了，阁下——
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]或者我应该叫你马奇伯爵？
[dialog]
[charslot]
[charslot(slot="l",name="avg_1019_siege2_1#1$1",focus="r")]
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]直接叫我艾莉诺就好。
[name="“小公爵”"]我找诺曼底公爵阁下要来马奇郡作为封地可不是为了什么伯爵的名号，只是图些生意上的方便而已，殿下。
[name="“小公爵”"]如果不是当年那场绞死国王的闹剧，我们的关系本可以更亲密些，维娜。
[dialog]
她顺手翻出一张紫色的烫金名片，上面只印着一束金色的千屈菜。
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]收下吧。既然你更习惯公事公办，这样或许你能舒服些。
[charslot(slot="l",name="avg_1019_siege2_1#10$1",focus="l")]
[name="维娜"]......我和你不熟。阁下，你们就在这地方决定伦蒂尼姆的未来？
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]会议的地点不由我决定。何况，想想在这里发生过的一切，难道还有比这里更合适的地方吗？
[dialog]
[charslot]
[delay(time=1)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.11,grad = true, fadetime=1.5)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.11, grad = true,fadetime=1.5)]
[delay(time=2)]
[backgroundTween(xFrom=0, xTo=30,yFrom=0, yTo=-30,xScaleFrom=1, yScaleFrom=1, xScaleTo=1.2, yScaleTo=1.2, duration=10, block=false)]
[delay(time=3)]
艾莉诺看着大厅尽头褪色的雕像和尘封的大门，似乎能捕捉到来自过去的时光。
那扇门后坐落着维多利亚国王的王座。国王曾身居其中，影响着整个帝国的兴衰。
可如今，那扇门后还剩下些什么呢？
[dialog]
[curtain(fadetime=1)]
[delay(time=2)]
[Background(image="55_g2_westlobbyhall",screenadapt="coverall", fadetime=1.5,block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_1019_siege2_1#10$1",focus="r")]
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]我提前来这，既是为了故地重游，也是想先见见你。我们有许多事情该聊聊。
[charslot(slot="r",name="avg_npc_1518_1#4$1",focus="r")]
[name="“小公爵”"]你不也想见我吗？
[charslot(slot="l",name="avg_1019_siege2_1#6$1",focus="l")]
[name="维娜"]......你知道我手里有——
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]维娜，你在罗德岛的朋友想必已经向你透露了其他公爵的想法。
[charslot(slot="l",name="avg_1019_siege2_1#6$1",focus="l")]
[name="维娜"]其他公爵？我不认为你和你背后的诺曼底公爵和他们有什么不同。
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]不要把我与诺曼底公爵阁下混为一谈。他是位值得尊敬的人，但处置伦蒂尼姆这种小事还犯不上麻烦公爵阁下。
[name="“小公爵”"]至于其他几位，我可不敢和他们相提并论。
[name="“小公爵”"]萨卡兹撤军并不意味着伦蒂尼姆的灾难就此结束，虽然没人愿意现在去统计感染者人数的变化，但结果显而易见。
[name="“小公爵”"]维多利亚的药物生产线不足，也不会有人愿意为了那些感染者去改组自己宝贵的生产线，你知道我的意思。
[charslot(slot="l",name="avg_1019_siege2_1#1$1",focus="l")]
[name="维娜"]你想说什么？
[charslot(slot="r",name="avg_npc_1518_1#2$1",focus="r")]
[name="“小公爵”"]我和哥伦比亚的军方有长期稳定的合作，他们也给我引荐了不少医药企业。
[name="“小公爵”"]没有堵不上的缺口，只要价钱合适。
[charslot(slot="l",name="avg_1019_siege2_1#6$1",focus="l")]
[name="维娜"]......这是威胁吗？
[charslot(slot="r",name="avg_npc_1518_1#2$1",focus="r")]
[name="“小公爵”"]看你怎么想。别急着回答我，等你理清了自己手里到底有什么筹码后再来找我，维娜。
[name="“小公爵”"]我们未来的亲密合作，可以从这起一个好头。
[charslot(slot="r",name="avg_npc_1518_1#1$1",focus="r")]
[name="“小公爵”"]还有，看看这个地方，你的家族曾在这座古老的建筑里指引着整个维多利亚的航向。
[name="“小公爵”"]亚历山德莉娜殿下，伦蒂尼姆对你来说，太小了——
[dialog]
[charslot]
[PlaySound(key="$d_gen_dooropen", volume=0.7)]
[delay(time=1)]
[name="？？？"]我倒觉得这座城市太大了。说来惭愧，城里遍地哭嚎的声音实在让我胆颤心惊，一时心慌居然走错了路。
[name="？？？"]呼，城里的惨象实在是......
[dialog]
[charslot(slot="m",name="avg_npc_1068_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1068_1#1$1",focus="m")]
[name="高多汀公爵"]小艾莉诺，你可真是大变样了。我还记得你趴在我脖子上，握着我角的模样呢。
[charslot(slot="m",name="avg_npc_1518_1#1$1",focus="m")]
[name="“小公爵”"]我依旧感激您的大度。诺曼底公爵阁下还特意提醒我，他准备去更干净的地方休养，您要是愿意，可一起前往。
[charslot(slot="m",name="avg_npc_1068_1#8$1",focus="m")]
[name="高多汀公爵"]哈，在我酒窖的好酒喝完之前，我可舍不得离开我的庄园半步。
[dialog]
[charslot]
[name="？？？"]我本以为老诺曼底会更重视这次小聚一些。
[dialog]
[charslot(slot="m",name="avg_npc_726_1#7$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="m")]
[name="开斯特公爵"]不过无妨，你才是我们今日相聚的原因，亚历山德莉娜。
[charslot(slot="m",name="avg_npc_1068_1#1$1",focus="m")]
[name="高多汀公爵"]咳，何必这么着急就切入主题呢，阁下。
[name="高多汀公爵"]那位老将军迟迟未至......他还是拒绝了您的邀请吗？
[charslot(slot="m",name="avg_npc_726_1#7$1",focus="m")]
[name="开斯特公爵"]他的目光早已不在伦蒂尼姆。我想您的探子会把我与他会面的所有细节放在您明早的餐盘里。
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[name="开斯特公爵"]不过，如今他的风采比之当年吞下高卢时也不遑多让。
[charslot(slot="m",name="avg_npc_1068_1#1$1",focus="m")]
[name="高多汀公爵"]这对维多利亚可算不得好事。
[charslot(slot="m",name="avg_npc_1068_1#7$1",focus="m")]
[name="高多汀公爵"]塔拉和“深池”......虽然他还没有明确宣布脱离维多利亚，但实际情况明眼人都能看出来。
[name="高多汀公爵"]亚伯科恩和法夫损失惨重，“主动放弃”了参与更大决策的机会。而阿什沃思背后的人也做出了远离动荡的决定。
[charslot(slot="m",name="avg_npc_1068_1#1$1",focus="m")]
[name="高多汀公爵"]至于诺曼底公爵......他的态度已经很明确了。
[dialog]
[charslot]
高多汀公爵微笑地看着“小公爵”，艾莉诺也只是淡淡地躬身示意。
[charslot(slot="m",name="avg_npc_1068_1#1$1",focus="m")]
[name="高多汀公爵"]喔，世事真是无常。
[name="高多汀公爵"]当年我们还能在此举办议会的酒宴，而阿利斯泰尔陛下哪怕坐在王座厅内，也没有人会轻视他的声音。
[charslot(slot="m",name="avg_npc_726_1#1$1",focus="m")]
[name="开斯特公爵"]呵。
[dialog]
[charslot]
站在阴暗蒙尘的大厅之中，高多汀公爵用脚轻盈地敲击着刻进骨子里的节拍，一如往日。
烟雾缭绕，舞乐不停，阳光会透过穹顶落在他的身上。那时他意气风发，权贵和夫人们在酒宴上争相为他伴舞，连陛下都要为他鼓掌。
然后，他也联手其他公爵将陛下送上了绞刑架。
[charslot(slot="m",name="avg_npc_1518_1#1$1",focus=

... (全文25068字符)
```

### level_act37side_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g3_westlobbythroneroom",screenadapt="coverall", block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.5, fadetime=0)]
[backgroundTween(xFrom=100, yFrom=0, xTo=-100, yTo=0, xScaleFrom=1.3, yScaleFrom=1.3, xScaleTo=1.3, yScaleTo=1.3, duration=35, block=false)]
[curtain(direction = 0,fillfrom = 0.01,fillto = 0.15,grad = true,fadetime=0.1)]
[curtain(direction = 4,fillfrom = 0.01,fillto = 0.15,grad = true,fadetime=0.1)]
[Delay(time=1)]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", multi = true, text="愿广阔的大地保佑吾王♪", x=300,y=200, alignment="center", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n\n保佑他的人民和他的福祉♪",block = true)]
[Sticker(id="st1", multi = true, text="\n\n赐予我们无限的恩典♪",block = true)]
[Sticker(id="st1", multi = true, text="\n\n让我们欢乐地歌唱♪",block = true)]
[Sticker(id="st1", multi = true, text="\n\n维多利亚，我的故乡！♪",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[dialog]
[curtain(fadetime=1)]
[delay(time=2)]
[Background(image="55_g3_westlobbythroneroom",screenadapt="coverall",fadetime=1.5,block=true)]
[delay(time=1)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣王会西部大堂王座厅</><p=2>1098年10月8日 9:45 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[Decision(options="你在进了王座厅之后，一直在哼这首歌。;你喜欢这首歌？", values="1;2")]
[Predicate(references="1;2")]
[dialog]
[charslot(slot="m",name="avg_1019_siege2_1#8$2",duration=0.5)]
[delay(time=0.7)]
[charslot(slot="m",name="avg_1019_siege2_1#8$2",focus="m")]
[name="维娜"]只是对它印象深刻而已，谈不上喜欢。
[name="维娜"]小时候我睡不着的时候，我的养父母喜欢在我床边为我哼这首歌。
[name="维娜"]我一度把它当做某种摇篮曲，直到他们去世后很久，我才反应过来对他们而言......“我是谁”。
[name="维娜"]那天我才突然发现，我对这首歌很陌生。但没办法，估计我一辈子没法忘掉这首歌的旋律了。
[dialog]
[charslot(slot="m",name="avg_1019_siege2_1#8$2",focus="n")]
[Decision(options="那你还记得他吗？那位......",values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_1019_siege2_1#7$2",focus="m")]
[name="维娜"]那位国王？我对他并不熟悉。至于那个和我血缘上极为亲近的家人......
[charslot(slot="m",name="avg_1019_siege2_1#8$2",focus="m")]
[name="维娜"]博士，我没必要对你撒谎，我也曾试图补全记忆中那个已经支离破碎的父亲形象。
[name="维娜"]但我再次亲眼见到他时，从他身上却找不到一点亲近的感觉。
[name="维娜"]他是国王，我是混街头的。除了都姓“维多利亚”之外，我们没有任何共同点了。
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="m")]
[name="维娜"]比起他，眼下有更重要的事需要我动脑子。
[name="维娜"]博士，刚才那些公爵们的话你听到了，伦蒂尼姆......我的家乡随时可能被他们视作弃子。
[name="维娜"]当初凯尔希医生把你从切尔诺伯格救回来，找我定下了回到维多利亚的计划时，我也没想到会变成现在这样。
[name="维娜"]但我已经做不到撒手不管了。
[dialog]
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="n")]
[Decision(options="“责任”是一个很奇妙的东西。;对罗德岛的大家，我也做不到轻易放手。;我们都一样。", values="1;2;3")]
[Predicate(references="1;2;3")]
[Decision(options="那些公爵也正是吃准了你放不下那些需要你的人。",values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_1019_siege2_1#8$2",focus="m")]
[name="维娜"]我不也吃准了那些公爵想要维持自己势力的心思吗？
[name="维娜"]只要他们还需要“维多利亚”这个名字来点缀自己的门面，我就还能为这座城市的恢复争取一些时间。
[name="维娜"]这不过是一场双方都心知肚明，有着必然结果的交易罢了。
[name="维娜"]真正能给我底气的，是那些一直在背后撑着我的人。
[charslot(slot="m",name="avg_1019_siege2_1#9$2",focus="m")]
[name="维娜"]我们都回到了家，战争也结束了，现在该我去听听他们的声音了。
[dialog]
[charslot(slot="m",name="avg_1019_siege2_1#9$2",focus="n")]
[Decision(options="维娜......",values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_1019_siege2_1#8$2",focus="m")]
[name="维娜"]怎么了，博士？
[dialog]
[charslot(slot="m",name="avg_1019_siege2_1#8$2",focus="n")]
[Decision(options="未来，你做出的某些决定，或许罗德岛不会认同。;或许罗德岛未来做出的某些决定，你并不会认可。", values="1;2")]
[Predicate(references="1;2")]
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="m")]
[name="维娜"]......我知道。
[name="维娜"]就像你们坚持协助维什戴尔领着剩下的萨卡兹撤离，我们中的很多人都并不接受。
[charslot(slot="m",name="avg_1019_siege2_1#5$2",focus="m")]
[name="维娜"]但我很清楚，这场仗不能继续下去了。我......我们失去的人，已经够多了。
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="m")]
[name="维娜"]况且，萨卡兹的警告我们都收到了。
[name="维娜"]所有公爵舰队愿意在他们撤军时按兵不动，不就是因为收到加急消息——
[name="维娜"]几乎同一时间，大部分核心圈国家的首都上空都短暂聚起了骇人的天灾云。
[charslot(slot="m",name="avg_1019_siege2_1#2$2",focus="m")]
[name="维娜"]呵，直截了当的威胁，正大光明地走回卡兹戴尔。
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="m")]
[name="维娜"]博士，你和凯尔希医生应该很清楚，他们拿着那枚源石还能做到什么。
[dialog]
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="n")]
[Decision(options="不被逼到无计可施的地步，他们不会滥用那项技术。",values="1")]
[Predicate(references="1")]
[charslot(slot="m",name="avg_1019_siege2_1#1$2",focus="m")]
[name="维娜"]只为自保？或许他们现在的确是这么想的。
[name="维娜"]但拥有远非自身所能掌控的力量，谁也没法保证会发生什么。
[name="维娜"]我见过很多新兴帮派靠着那些贵族老爷的力量迅速崛起，又很快从内部崩溃瓦解。
[dialog]
[charslot]
[Decision(options="所以阿米娅会一起回到卡兹戴尔。;阿米娅会确保那枚源石在我们的监视之下。", values="1;2")]
[Predicate(references="1;2")]
[dialog]
[musicvolume(volume=0, fadetime=1)]
[delay(time=1)]
[Blocker(a=0.4, r=0, g=0, b=0, fadetime=1, block=true)]
[Sticker(id="st1", text="但你们也无法左右萨卡兹必然走向的未来。此战之后，双方均被烙上难以愈合的伤痕。", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st1", duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st2", text="如那位年轻的萨卡兹摄政王所愿，萨卡兹终于再一次被具体的仇恨团结起来，他们也获得了属于他们的源石......", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st2", duration=1,block = false)]
[delay(time=1)]
[Sticker(id="st3", text="而仇恨，终归只有一个终点。等到了那时，你又会站在何处？", x=300, y=370, alignment="center", size=24, delay=0, duration=1, width=700)]
[Sticker(id="st3", duration=1,block = false)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[PlaySound(key="$d_avg_deeplion", volume=1, channel="slide", loop=false)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_656_1#1$1", duration=2)]
[delay(time=2.5)]
[soundvolume(channel="slide",volume=0,fadetime=1)]
[musicvolume(volume=0.6, fadetime=2)]
王座之后，金色的狮子踱步而出，伏身于黯淡的王座之侧。
高文，仿佛他本就应该存在于此，与周遭如永恒存在的浮雕一同，眨眼间就已见证了帝国兴衰的漫长时光。
而此刻，他黑色的眼眸中映下了你的影子。
[dialog]
[charslot(slot="

... (全文31335字符)
```

### level_act37side_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g6_dusklentiavenue",screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[charslot(slot="l",name="avg_npc_329_1#1$1",duration=0.7)]
[charslot(slot="r",name="avg_npc_240",duration=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_240",focus="r")]
[name="紧张的孩子"]就，就这么过去吗？
[charslot(slot="l",name="avg_npc_329_1#1$1",focus="l")]
[name="不怀好意的市民"]对，你就直接过去问问他价格就行。
[charslot(slot="r",name="avg_npc_240",focus="r")]
[name="紧张的孩子"]好，好的。
[Dialog]
[PlaySound(key="$d_avg_footstep_stonestep",volume=0.6,channel="step",loop=false)]
[stopsound(channel="step",fadetime=2)]
[charslot(slot = "r", posfrom="0,0", posto="100,0", afrom=1, ato=0, duration=1)]
[delay(time=1.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)] 
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)] 
[charslot]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=1.5, block=true)]
孩子走到商人的移动摊位前，怯生生地低头查看着摊位上的产品。
[Dialog]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="和蔼的商人"]买烟花？
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="紧张的孩子"]嗯，嗯......
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="和蔼的商人"]庆生还是送人？可以试试这款，很多人都喜欢买这款庆祝呢！
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="紧张的孩子"]可，可......上面很多灰——
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[name="和蔼的商人"]只是刚好这两天从仓库里搬出来，落点灰正常。这样吧，孩子，可以买一送一——
[Dialog]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="n")]
[playsound(key="$d_avg_fireleadwire", volume=0.7)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_416_1#1$1",focus="m")]
[multiline(name="和蔼的商人")]什么味道——
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="和蔼的商人")]我的货！你点了我的货！
[charslot(slot="m",name="avg_npc_329_1#1$1",focus="m")]
[name="不怀好意的市民"]哈！
[Dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_240",focus="m")]
[name="紧张的孩子"]......
[Dialog]
[charslot]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="不怀好意的市民"]跑啊！愣着干嘛！
[Dialog]
[charslot]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[playsound(key="$d_avg_firerockfall", volume=0.7)]
[PlaySound(key="$firestorm", volume=0.9,delay=0.2)]
[CameraShake(duration=1.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0.6, r=0.92, g=0.3, b=0.3, fadetime=0.05, block=true)]
[Blocker(a=0.2, r=0.92, g=0.3, b=0.3, fadetime=0.3, block=false)]
[PlaySound(key="$d_avg_churchfire", loop=true, channel="bse",volume=0)]
[SoundVolume(volume=0.6, fadetime=3,channel="bse")]
[delay(time=2)]
商人尽力扑灭着摊位上的火焰，却于事无补，连身形都逐渐被火焰吞噬。
烟火炸裂，吸引了越来越多的人。
而“恶作剧”的人已经拉着茫然的孩子逃离了现场。
“我们不是捉弄他吗，为、为什么......”
“敢娶魔族佬当老婆的人不就该落得这么个下场？活该！”
[Dialog]
[charslot(slot = "m", name = "avg_222_bpipe_1#1", bstart=0.5, bend=0.9, duration=1)]
[delay(time=1.5)]
[charslot(slot = "m", name = "avg_222_bpipe_1#1", bstart=0.5, bend=0.9,focus="m")]
[name="？？？"]火势越来越大了，赶紧疏散人群，我去救人！
[charslot(slot = "m", name = "avg_npc_248", focus="m")]
[name="城防军巡逻队"]遵命，队长！
[Dialog]
[charslot(slot = "m", name = "avg_222_bpipe_1#1", bstart=0.5, bend=0.9,focus="m")]
[delay(time=0.2)]
[PlaySound(key="$rungeneral", volume=0.9)]
[charslot(duration=1)]
[delay(time=2)]
[Dialog]
[PlaySound(key="$gunlance",channel="bipe1",volume=1)]
[PlaySound(key="$d_avg_spear",channel="bipe2",volume=1,delay=0.3)]
[CameraShake(duration=1.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
破城矛连发，撕碎火焰，爆裂声与烟火声交相演奏乐章。
瓦伊凡一手持矛，一手提溜着商人冲出了火焰。她把商人放在安全位置后，才大咧咧地坐在商人旁边，抹了抹被熏黑的脸蛋。
[Dialog]
[stopmusic(fadetime=2)]
[SoundVolume(volume=0.2, fadetime=3,channel="bse")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="55_g6_dusklentiavenue",screenadapt="coverall", block=true)]
[delay(time=1)]
[PlayMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_222_bpipe_1#5", duration=0.5)]
[charslot(slot = "r", name = "avg_npc_416_1#1$1", duration=0.5)]
[delay(time=0.7)]
[charslot(slot = "l", name = "avg_222_bpipe_1#5",focus="l")]
[name="风笛"]呃，抱歉，好像我连你的摊子也一起给......
[charslot(slot = "r", name = "avg_npc_416_1#1$1", focus="r")]
[name="和蔼的商人"]不是大事，不是大事。
[charslot(slot = "l", name = "avg_222_bpipe_1#4",focus="l")]
[name="风笛"]这......还不是大事？
[Dialog]
[charslot]
她指了指还在熊熊燃烧的现场，以及不断窜出的烟花。
围观的群众越来越多，甚至还有一无所知的醉鬼硬拉着身边的人跳起了舞。
辱骂酒鬼的声音，起哄跳舞的声音，还有烟花四处乱窜的声音，夕阳下，一切都乱糟糟的。
自从萨卡兹接管城市以来，这条街道已经很久没有这么热闹过了。
现场一片混乱，商人却在冷静下来之后笑了起来。
[charslot(slot = "l", name = "avg_222_bpipe_1#4",focus="l")]
[charslot(slot = "r", name = "avg_npc_416_1#1$1", focus="l")]
[name="风笛"]......？
[charslot(slot = "r", name = "avg_npc_416_1#1$1", focus="r")]
[name="和蔼的商人"]好久都没见过大伙这么轻松的样子了，真是怀念啊......
[charslot(slot = "l", name = "avg_222_bpipe_1#5",focus="l")]
[name="风笛"]......可被烧的不是你的摊子吗？
[charslot(slot = "r", name = "avg_npc_416_1#1$1", focus="r")]
[name="和蔼的商人"]我今天开心，就当放烟花给大伙庆祝了！
[name="和蔼的商人"]长官，悄悄告诉你，我老婆今晚终于可以出城了。
[charslot(slot = "l", name = "avg_222_bpipe_1#7",focus="l")]
[name="风笛"]......？
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_248", focus="m")]
[name="城防军巡逻队"]队长，没人受伤，要去把那个闹事的家伙给抓回来吗？
[charslot(slot = "m", name = "avg_npc_416_1#1$1", focus="m")]
[name="和蔼的商人"]......反正都没人受伤——
[charslot(slot = "m", name = "avg_222_bpipe_1#7",focus="m")]
[name="风笛"]他犯了事，我们就必须得处理，这是我们的职责。
[charslot(slot = "m", name = "avg_npc_416_1#1$1", focus="m")]
[name="和蔼的商人"]不管怎么样，谢谢你。对了，你会跳

... (全文24696字符)
```

### level_act37side_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Image(image="55_i17_2", screenadapt="coverall",fadetime=0)]
[Delay(time=1)]
[PlayMusic(key="$ouat_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>当我决定为阿勒黛撰写一个单独的篇章时，一直没法弄出个满意的开头，因为我突然发现，自己对这个非常熟悉的名字简直一无所知。</i>", x=300,y=240,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>坎伯兰家的最后一个人，背叛了我们，却又甘愿为了救我们而牺牲的人，也是喜欢夸耀自己做的奶油炖菜汤美味的人。</i>",block = true)]
[Sticker(id="st1")]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>“铣痕”......开斯特的手下......“永远高洁的坎伯兰”......到底哪一个才是真正的她？</i>", x=300,y=270,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[Background(image="bg_cherunder_2", screenadapt="coverall", block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=0.5, block=true)]
[delay(time=2.5)]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>伦蒂尼姆地下隧道</><p=2>1098年9月28日 4:53 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
距离典范军突破城内封锁还有34分钟
[dialog]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]老大，坐标确认，那个匿名讯息警告的地点就在前面。信息来源刚刚也查清楚了，是——
[charslot(slot="m",name="avg_npc_1342_1#2$1",focus="m")]
[name="“铣痕”"]罗德岛。
[charslot(slot="m",name="avg_npc_1342_1#1$1",focus="m")]
[name="“铣痕”"]没什么好惊讶的，对我来说这不难猜。走吧。
[charslot(slot="m",name="avg_npc_1342_1#1$1",focus="n")]
佣兵犹豫地站在原地。
[charslot(slot="m",name="avg_npc_1342_1#10$1",focus="m")]
[name="“铣痕”"]......说。
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]弟兄们一直很信你。没有你，我们这些人不是烂在小巷里，就是被魔族佬——
[name="担忧的佣兵"]反正都是死过一次的人，我不介意为了你拼拼命。但这事没道理，罗德岛我们根本不认识，凭什么信他们。
[name="担忧的佣兵"]现在那支典范军就快突进城里了，眼看外面就该彻底乱起来了。我们趁着这机会明明能捞很多好处......
[name="担忧的佣兵"]或者......至少你不该亲自来冒这个险。
[charslot(slot="m",name="avg_npc_1342_1#1$1",focus="m")]
[name="“铣痕”"]不止你这么想吧？
[dialog]
[charslot]
佣兵沉默，他不敢直视“铣痕”的眼睛，他害怕她发怒。
但等了一会儿，什么也没发生。
[charslot(slot="m",name="avg_npc_1342_1#7$1",focus="m")]
[name="“铣痕”"]这场仗打完之后，你们想过伦蒂尼姆会怎么样吗？
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]呃......和之前一样......吗？
[charslot(slot="m",name="avg_npc_1342_1#1$1",focus="m")]
[name="“铣痕”"]不，没有什么会再和以前一样。无论这场仗结果如何，谁都回不去了。
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]等等，老大，你想扔下我们？！
[charslot(slot="m",name="avg_npc_1342_1#1$1",focus="m")]
[name="“铣痕”"]不，我需要你们。很快，伦蒂尼姆会变成一座亟需被缝补的城市。
[name="“铣痕”"]过去的秩序已经被暴力和死亡摧毁，而留下的那些缺口，足够喂饱我们了。
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]可——
[charslot(slot="m",name="avg_npc_1342_1#1$1",focus="m")]
[name="“铣痕”"]我现在没在问你的意见。
[name="“铣痕”"]听好了，我不打算继续过以往那种生活，那就得早为将来做打算。当然，我不会忘了你们。
[name="“铣痕”"]但想保住这口肉，就得让人知道我们能做到什么，敢做什么。
[name="“铣痕”"]别说你们没得选。现在，你是继续走，还是回头？
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]......
[name="担忧的佣兵"]他妈的，我走前面，老大。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="27_g7_subway", screenadapt="coverall", block=true)]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[delay(time=1)]
[PlaySound(key="$d_avg_cavewaterdrop", volume=0, loop=true, channel="a")]
[SoundVolume(channel="a", volume=0.7, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]我没看错吧......这些是什么东西......
[name="担忧的佣兵"]钢架缝隙还有炉子里的那些血红色石头，这些都是魔族佬藏在这的？！他们到底想干嘛......
[charslot(slot="m",name="avg_npc_1342_1#6$1",focus="m")]
[name="“铣痕”"]......血魔的东西。
[Dialog]
[charslot]
空气中弥漫着淡淡的血腥气味，她想起了那些如噩梦般涌来的蠕动的怪物。
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]老大！这边，我找到点东西！
[charslot(slot="m",name="avg_npc_1342_1#4$1",focus="m")]
[name="“铣痕”"]这是......公爵联军的士兵？
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]不对劲，刚死不久。这里还有铭牌......联军第八纵队第五步兵团......校官？！
[charslot(slot="m",name="avg_npc_1342_1#10$1",focus="m")]
[name="“铣痕”"]马奇伯爵的部队，诺曼底公爵的人？身上没有伤口。不是被人谋害，但也绝对不是自然死亡。
[name="“铣痕”"]据我所知，这支部队现在明明还在城墙外围城，一个校官为什么会出现在这——
[stopmusic(fadetime=1)]
[stopsound(channel="a", fadetime=1)]
[Dialog]
[charslot]
[name="？？？"]哪来的？直接动手速战速决，不要耽误执行命令。
[name="？？？"]还有其他祭坛需要启动，剩下的时间不多。
[Dialog]
[PlayMusic(intro="$escape_intro", key="$escape_loop", volume=0.6)]
[PlaySound(key="$d_avg_armour", volume=1)]
[charslot(slot="l",name="avg_npc_1341_1#1$1",duration=1)]
[charslot(slot="r",name="avg_npc_1341_1#1$1",duration=1)]
[Delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]这些该死的魔族佬把我们包围了。怎么撤——
[Dialog]
[charslot]
[charslot(slot = "l", name = "avg_npc_1342_1#8$1",posfrom = "0,0", posto = "200,0",focus="all")]
[Delay(time=0.5)]
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[PlaySound(key="$e_atk_stmwpn_d2",volume=0.7,delay=0.3)]
[charslot(slot = "m", name = "avg_npc_1342_1#8$2",duration=1,focus="all")]
[delay(time=2)]
[charslot(slot = "m", name = "avg_npc_1342_1#8$2",focus="m")]
[name="“铣痕”"]为什么要撤？
[charslot]
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]......
[Dialog]
[charslot]
“疯子”。
没人知道她手中那柄属于蒸汽骑士的锋刃从何而来，更遑论“铣痕”的出身。
佣兵的腿在抖，他很后悔。几分钟前，他本有机会活着转身就走。
......只要那柄紫色的锋刃不会从背后捅了他。
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="担忧的佣兵"]妈的。
[Dialog]
[charslot]
[PlaySound(key="$d_avg_walk_stage", vo

... (全文21868字符)
```

### level_act37side_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g4_victoriaconferencehall",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0, loop=true, channel="c")]
[SoundVolume(volume=0.5, channel="c",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>西涅塞德大堂议会厅</><p=2>1098年12月15日 4:02 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_229_1#1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_229_1#1",focus="m")]
[name="号角"]各位向城防军申请调阅的卷宗我都带过来了。
[name="号角"]议长阁下，从城防军巡逻队组建以来，我们已经收到了不下两百起牵涉“铣痕”及其手下的求助案例。
[name="号角"]“铣痕”他们涉嫌违反议会新修法律条款的罪行均有实证。
[charslot(slot="m",name="avg_npc_659_1#1$1",focus="m")]
[name="粗犷的议员"]那还等什么？！这些人已经干扰到我们上工了，您直接给命令，把他们全掀了完事！
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]我知道你们的情况，费斯特和洛洛已经找过我。
[name="维娜"]我也不想城区重建的进度被耽搁，但议会不是这么运作的。
[dialog]
[Delay(time=0.5)]
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]......艾瑞莎子爵，您说。
[charslot(slot="m",name="avg_npc_175",focus="m")]
[name="矜持的议员"]“铣痕”他们的行为的确有待裁定，但他们提供的药物的确暂时稳定了许多无药可用之人的情绪——
[charslot(slot="m",name="avg_npc_1157_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="愤怒的议员"]放屁！
[name="愤怒的议员"]他们放出来的是药，收回去的是命！
[charslot(slot="m",name="avg_npc_229_1#7",focus="m")]
[name="号角"]亚伦议员，坐回你的位置上，这里是议会！
[charslot(slot="m",name="avg_npc_229_1#1",focus="m")]
[name="号角"]艾瑞莎子爵，他们长期借助战时遗留的地下工事躲避搜捕。
[name="号角"]除去他们刻意将据点分散之外，也有证据表明议会中一直有人在协助他们躲开追查。
[name="号角"]这件事是否也需要一个解释？
[charslot(slot="m",name="avg_npc_175",focus="m")]
[name="矜持的议员"]斯卡曼德罗斯中尉是希望代表伦蒂尼姆城防军向我们申请协助调查吗？
[name="矜持的议员"]我们当然非常支持尽快为市民们扫清“铣痕”带来的威胁。我可以联络开斯特公爵阁下，抽调人手赶到伦蒂尼姆——
[charslot(slot="m",name="avg_1019_siege2_1#6$1",focus="m")]
[name="维娜"]艾瑞莎子爵，既然开斯特终于愿意对议会施以援手，不妨也问问其他几位公爵阁下是否也愿意提供帮助？
[name="维娜"]海克特男爵，吉地恩子爵，海曼医生，还有埃文学士，也劳烦各位“顺便”联系一下其他几位公爵，如何？
[dialog]
[charslot]
[stopsound(channel="c", fadetime=1)]
[Delay(time=1.5)]
人群中几位低调的议员微微错愕之后，只能微笑着起身向维娜鞠躬。
没有肯定，也没有否定。但议会厅中的争执却消失了，就好像刚才的争吵从来没有发生过。
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]“铣痕”的问题，议会将挑选议员组成特别临时法庭即刻处理。当然，我们承认“铣痕”为自己辩护的权利。
[dialog]
[charslot]
席位间窃窃私语，但无人反对。
[name="席位上的声音"]说是审判......她怎么会愿意公然出现在这里？
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]如果她不出现，则将被视作放弃辩护的机会。临时法庭会做出公正的裁定。
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]另外，号角小姐，麻烦通知城防军巡逻队全城搜捕“铣痕”，带她来议会厅。
[multiline(name="维娜")]在议会今天的工作时间内......
[charslot(slot="m",name="avg_1019_siege2_1#7$1",focus="m")]
[multiline(name="维娜")]她还剩下两个小时，我会在这里等她。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="55_g4_victoriaconferencehall",fadetime=0,screenadapt="coverall")]
[charslot(slot="l",name="avg_1019_siege2_1#2$1")]
[charslot(slot="r",name="avg_4110_delphn_1#11$1")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=0.5)]
[charslot(slot="r",name="avg_4110_delphn_1#11$1",focus="r")]
[name="戴菲恩"]维娜，你可以先回办公室休息一会儿，你的状态看上去并不好。
[name="戴菲恩"]她如果来了，我会通知——
[charslot(slot="l",name="avg_1019_siege2_1#6$1",focus="l")]
[name="维娜"]我说了我会在这等！
[charslot(slot="r",name="avg_4110_delphn_1#5$1",focus="r")]
[name="戴菲恩"]......好。
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[name="维娜"]抱歉，我只是......我只是，有点——
[charslot(slot="r",name="avg_4110_delphn_1#5$1",focus="r")]
[name="戴菲恩"]我知道。
[charslot(slot="l",name="avg_1019_siege2_1#7$1",focus="l")]
[name="维娜"]我真不明白，明明我们有更要紧的事情需要去做——需要治疗的感染者，缺少的物资，城市的重建，秩序的恢复......
[name="维娜"]每天都有数不清的重要事项涌到我的办公桌上需要确认。
[charslot(slot="l",name="avg_1019_siege2_1#7$1",focus="l")]
[multiline(name="维娜")]但他们却更愿意花上一整天来争吵一件没有异议的事——
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[multiline(name="维娜")]唉......
[name="维娜"]是我做得还不够好。
[charslot(slot="r",name="avg_4110_delphn_1#11$1",focus="r")]
[name="戴菲恩"]维娜，我记得我向你承诺过，只要让我的人还有城防军全力搜捕她，她没有任何逃脱的机会。但当时你拒绝了。
[charslot(slot="l",name="avg_1019_siege2_1#10$1",focus="l")]
[name="维娜"]我们的人手并不充裕。用这种方式去解决问题，就必须无视掉城内其他更需要解决的问题——
[charslot(slot="r",name="avg_4110_delphn_1#9$1",focus="r")]
[name="戴菲恩"]那为什么你现在又反倒会觉得自己做得还不够好？
[name="戴菲恩"]不要试图把一整座移动城市背在背上移动，它靠的是下面的履带。
[name="戴菲恩"]你也没有义务去成为那些人口中最完美的领袖，那个理所应当该解决一切问题的人。
[charslot(slot="r",name="avg_4110_delphn_1#1$1",focus="r")]
[name="戴菲恩"]况且......“铣痕”、示威、药物短缺，最近的种种事背后，都不乏公爵的影子。
[charslot(slot="l",name="avg_1019_siege2_1#7$1",focus="l")]
[name="维娜"]我知道“铣痕”这件事一定有开斯特的推动，但总归需要有个结果。“铣痕”......已经越线了。
[charslot(slot="r",name="avg_4110_delphn_1#1$1",focus="r")]
[name="戴菲恩"]不过我们的确很难抓到她，按因陀罗和达格达的说法，她还和一个奇怪的血魔有牵连。
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[name="维娜"]戴菲恩......如果她没来——
[charslot(slot="r",name="avg_4110_delphn_1#11$1",focus="r")]
[name="戴菲恩"]你希望她来吗，维娜？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="27_g7_subway",fadetime=0,screenadapt="coverall")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>“铣痕”的藏身处</><p=2>1098年12月15日 5:17 P.M. </>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_243",bstart=0.2,bend=0.7,focus="m")]
[name="慌张的女士"]为什么还要蒙上我的眼睛......我丈夫的账我已经还清了不是吗？
[charslot(slot="m",name="avg_npc_399_1#1$1",focus="m")]
[name="平静的佣兵"]的确，女士，您是讲信用的人。
[name="平静的佣兵"]米基·罗宾森的账您的确还清了。对了，老大让我向您表达她的遗憾。您丈夫生前的确为这座城市做出了无可替代的贡献。
[charslot(slot="m",name="avg_npc_243",bstart=0.2,bend=0.7,focus="m")]
[name="慌张的女士"]......那我，可以走了吗？
[charslot(

... (全文20552字符)
```

### level_act37side_04_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g5_victoriaspeakeasy",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>“一镑十杯”酒馆</><p=2>1098年12月21日 5:05 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="醉醺醺的士兵"]啧，议长阁下做得好！
[name="醉醺醺的士兵"]我们就该把伦蒂尼姆的每一块地板掀起来，把还藏着的魔族佬渣滓统统扫出去......咳、咳咳......
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="潦倒的市民"]而且我听说，很快会有一大批矿石病药物送进来。
[name="潦倒的市民"]我发小就在物资筹备办公室，说不定他能帮我先搞到药，到时候给你也弄点，哈哈......碰个杯庆祝——嗝——
[name="潦倒的市民"]嘿，你当初刚进公爵直属部队时可神气得不行，后来又加入了典范军，结果仗打完，兜兜转转我们又一样了。
[name="潦倒的市民"]两个啥也不剩的感染者——
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="醉醺醺的士兵"]什么感染者？！
[dialog]
[PlaySound(key="$bottlebroken")]
[CameraShake(duration=0.7, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_414_1#1$1",focus="m")]
[name="醉醺醺的士兵"]我能打仗！不是你们这样的病号......我也不怕死！呕——
[dialog]
[charslot]
在场的许多人都抬起了头，盯着那名摇摇欲坠的士兵。
[dialog]
[PlaySound(key="$d_avg_coin")]
[Delay(time=1)]
一枚硬币划过他的眼前，被抛到了吧台之上。一位面色憔悴的人扶住了他的身体。
[dialog]
[charslot(slot="m",name="avg_npc_1520_1#1$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1520_1#1$1",focus="m")]
[name="希勒少尉"]......他昏头了。送他回家吧，账我付了。
[name="希勒少尉"]希望您不要把他们的话放在心上，女士。
[dialog]
[charslot]
[charslot(slot="m",name="avg_4162_cathy_1#9$1",duration=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_4162_cathy_1#9$1",focus="m")]
[name="凯瑟琳"]他只是陈述了事实，少尉。
[dialog]
[charslot]
[charslot(slot="l",name="avg_4162_cathy_1#9$1",focus="r")]
[charslot(slot="r",name="avg_npc_1520_1#1$1",focus="r")]
[name="希勒少尉"]......我也退役了，女士。不过随您吧。
[charslot(slot="l",name="avg_4162_cathy_1#9$1",focus="l")]
[name="凯瑟琳"]好。至于你刚刚问的......我搭上的关系是那位被通缉的人，或是整合运动，还是别的什么人，都不重要。
[name="凯瑟琳"]工人们想要为家乡再尽一份力，但我不能放任他们面对感染恶化的风险不管。
[charslot(slot="l",name="avg_4162_cathy_1#2$1",focus="l")]
[name="凯瑟琳"]特殊时期，特殊办法。我们一直都是这么过来的。
[charslot(slot="r",name="avg_npc_1520_1#1$1",focus="r")]
[name="希勒少尉"]......
[name="希勒少尉"]只是善意的提醒。我目睹过一些来路不明的药物导致的负面效果，前两天有一名士兵在喝酒时突然倒地不省人事。
[name="希勒少尉"]或许是某种巧合，战时我给他动过急救手术。
[charslot(slot="r",name="avg_npc_1520_1#2$1",focus="r")]
[name="希勒少尉"]那时他活了下来，但前两天......我只能给他做一次人生最后的检查。
[charslot(slot="l",name="avg_4162_cathy_1#10$1",focus="l")]
[name="凯瑟琳"]你很仁慈。
[name="凯瑟琳"]我们厂区的药贩子跟我说过，他根本不记得打仗的时候，多少人来找他弄毒药。
[charslot(slot="r",name="avg_npc_1520_1#1$1",focus="r")]
[name="希勒少尉"]不，我当然也不可能在急救中特意记住每一个伤员。
[name="希勒少尉"]身为职业军医，我处理过许多更糟糕的情况。但至少，我总是能再见到那些从医疗帐篷里活着走出去的人。
[name="希勒少尉"]如果您也常来喝酒，也总是能逐渐从人群中分辨出自己见过的人，哪怕只是一面之缘。
[charslot(slot="l",name="avg_4162_cathy_1#10$1",focus="l")]
[name="凯瑟琳"]我认识一些医生，罗德岛过来的。也许你需要他们的帮助。
[charslot(slot="r",name="avg_npc_1520_1#1$1",focus="r")]
[name="希勒少尉"]您忘了，我自己就是医生......您对“典范军”怎么看？
[charslot(slot="l",name="avg_4162_cathy_1#5$1",focus="l")]
[name="凯瑟琳"]别难为一个老工人去回忆过去的事。
[name="凯瑟琳"]那段历史就算对我来说也够久远的了。我只记得几十年前孩子们互相吹嘘的时候，最独特的名号不是哪个公爵的军队，而是典范军。
[charslot(slot="l",name="avg_4162_cathy_1#9$1",focus="l")]
[name="凯瑟琳"]一支了不起的队伍，牺牲了很多人。
[charslot(slot="r",name="avg_npc_1520_1#6$1",focus="r")]
[name="希勒少尉"]不，我是说——
[charslot(slot="l",name="avg_4162_cathy_1#5$1",focus="l")]
[name="凯瑟琳"]我知道你想听到的答案是什么，但抱歉，我的确没有更多的看法了。
[charslot(slot="r",name="avg_npc_1520_1#1$1",focus="r")]
[name="希勒少尉"]......现在这支所谓的“典范军”，大部分人并没有军人的资质，不应该与历史上的军队相提并论。
[charslot(slot="l",name="avg_4162_cathy_1#9$1",focus="l")]
[name="凯瑟琳"]我只知道，大公爵们打赢萨卡兹的时候，我们这些困在城内的人可没开始庆祝。
[name="凯瑟琳"]城墙起了火，手无寸铁的市民跟萨卡兹士兵被关在一起。
[name="凯瑟琳"]没人敢说大公爵们会不会先谈判两个月再进来，谁也说不准事情最后会变成什么样。
[charslot(slot="l",name="avg_4162_cathy_1#10$1",focus="l")]
[name="凯瑟琳"]还好，最后越过了城墙的是典范军。至少在伦蒂尼姆，没人敢抹去你们的贡献。
[dialog]
[charslot(slot="l",name="avg_4162_cathy_1#9$1",focus="l")]
[Delay(time=1)]
[charslot(slot="l",name="avg_4162_cathy_1#9$1",focus="n")]
凯瑟琳停顿了一会儿，因为她余光注意到军官的手颤抖起来。
他在腰袋中摸索了很长一段时间，最后叹了口气，抓起杯子喝了一大口酒。
[dialog]
[charslot(slot="r",name="avg_npc_1520_1#2$1",focus="r")]
[PlaySound(key="$d_avg_drinkswllw", volume=0.7)]
[Delay(time=1)]
[charslot(slot="r",name="avg_npc_1520_1#1$1",focus="r")]
[name="希勒少尉"]不过，目前我们中的大多数人都只不过是各间酒馆的常客。
[name="希勒少尉"]感谢这里的酒馆老板心地善良，并不会将醉鬼赶回家。
[name="希勒少尉"]毕竟，大部分为了回家而不得不打仗的人，现在都无家可归了。
[charslot(slot="r",name="avg_npc_1520_1#5$1",focus="r")]
[name="希勒少尉"]......敬来之不易的胜利。
[dialog]
[charslot]
希勒举起杯子，向凯瑟琳示意碰杯，但后者没有回应。
[charslot(slot="m",name="avg_4162_cathy_1#5$1",focus="m")]
[name="凯瑟琳"]恐怕你找了个不称职的酒友，我得扫你的兴了。我和人约好的时间到了，该办正事了。
[name="凯瑟琳"]你已经醉了，军医。把酒留给你以后的日子。
[charslot(slot="m",name="avg_4162_cathy_1#9$1",focus="m")]
[name="凯瑟琳"]我大概知道些关于典范军的流言，为什么不直接找那位议长阁下聊聊呢？
[dialog]
[PlaySound(key="$d_avg_chairrub", volume=1)]
[charslot(duration=1)]
[Delay(time=2)]
凯瑟琳起身绕过拥挤的客人们，向吧台后的老板点了点头，消失在角落里一扇被杂物挡起来的门后。
[dialog]
[musicvolume(volume=0.3, fadetime=1)]
[Delay(time=1)]
[focusout(duration=1, type="bg", from=0, to=1, block=true)]
[Background(image="55_g5_victoriaspeakeasy",screenadapt="coverall",xScale=1.3, yScale=1.3,fadetime=2,block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_1520_1#2$1",action="zoom",poszoom="0.5,0.5",afrom=0,ato=0,scale=1.3,duration=0,isblock=true)]
[charslot(slot = "m", posfrom = "0,0", posto = "0,-200",afrom=0,ato=1,duration =0,focus="m")]
[name="希勒少尉"]......您怎么知道我没有找过她呢？
[dialog]
[charslot]
他看着凯瑟琳消失的地方，那里通向的是这座城市被遗忘的地方。
城防军巡逻队进去搜查过很多次，但每次除了惹一身灰尘，其他什么都找不到。
[charslot(slot="m",name="avg_npc_1520_1#5$1",action="zoom",poszoom="0.5,0.5",afrom=0,ato=0,scale=1.3,duration=0,isblock=true)]
[charslot(slot = "m", posfrom = "0,0", posto = "0,-200",afrom=0,ato=1,duration =0,focus="m")]
[name="希勒少尉"]呵......与我无关。
[dialog]
[charslot(duration=1)]
[Delay(time=1.5)]
[musicvolu

... (全文24567字符)
```

### level_act37side_04_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g1_battlefieldoutside",screenadapt="coverall", block=true)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.5, fadetime=0)]
[focusout(duration=0.5, type="bg", from=0, to=1, block=true)]
[Delay(time=1)]
[PlayMusic(intro="$loading_intro", key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
[name="？？？"]......少尉......
[name="？？？"]希勒......少尉......快......起......
[name="希勒少尉"]——？
他看到了一双手伸向了自己。
[name="希勒少尉"]戴......戴菲恩小姐？
[Dialog]
[focusout(duration=1.5, type="bg", from=1, to=0, block=true)]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1.5)]
[PlaySound(key="$d_avg_openftstpwalk", volume=1, loop=true, channel="walk1")]
[Delay(time=2)]
[stopSound(channel="walk1", fadetime=2)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_4110_delphn_1#1$1",duration=0.7)]
[delay(time=1)]
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]别动，我背着你，得赶紧撤回我们攻下来的安全驻地。
[name="戴菲恩"]可能还会有更多萨卡兹部队搜查过来，用巫术炸弹拦截我们。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[name="希勒少尉"]我——谢谢您——救我——
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]不必谢我，救你的是一位英勇的士兵，也是一位尽责的护士，莎拉女士。
[charslot(slot="m",name="avg_4110_delphn_1#8$1",focus="m")]
[name="戴菲恩"]她强行催动还不熟练的源石技艺阻挡巫术炸弹的爆炸，保护了还在转运的伤员们，当然，还有你。
[charslot(slot="m",name="avg_4110_delphn_1#8$1",focus="n")]
[name="希勒少尉"]是她......等等，难道她——
[charslot(slot="m",name="avg_4110_delphn_1#9$1",focus="m")]
[name="戴菲恩"]放心，她只是昏过去了。我们已经把她接回了接驳口的临时驻地。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]不过你们都暴露在极高浓度的源石粉尘环境中过长时间......
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[name="希勒少尉"]我很清楚风险。
[name="希勒少尉"]戴菲恩小姐，所以，你们成功了？抵达了接驳口？
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]是的。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[name="希勒少尉"]我看到，城墙上的火......熄灭了。
[name="希勒少尉"]城墙之战......已经结束了？
[charslot(slot="m",name="avg_4110_delphn_1#7$1",focus="m")]
[name="戴菲恩"]......
[name="戴菲恩"]不，这场仗才刚刚开始。
[name="戴菲恩"]食腐者正依仗着城防炮和他最精锐的部队和公爵联军保持着僵持。
[charslot(slot="m",name="avg_4110_delphn_1#7$1",focus="n")]
[name="希勒少尉"]那我们......能做点什么吗？
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]突破接驳口，为联军撕开一道城墙的口子，让萨卡兹露出破绽。
[name="戴菲恩"]就像联军帮我们一样......虽然这并非他们的本意。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[CameraShake(duration=0.5, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="希勒少尉"]我知道了——咳咳——
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]希勒少尉，接下来的任务你不用参加。这是命令。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[name="希勒少尉"]——！
[name="希勒少尉"]这是推进之王的命令——
[charslot(slot="m",name="avg_4110_delphn_1#2$1",focus="m")]
[name="戴菲恩"]我的命令。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]少尉，留在接驳口的驻地，你现在需要的是休息。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[name="希勒少尉"]......
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="27_g15_customs", screenadapt="coverall",block=true)]
[delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>城墙接驳口，典范军临时驻地</><p=2>1098年9月25日 8:21 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="开朗的士兵"]让我们欢乐地歌唱♪
[charslot(slot="m",name="avg_npc_729_1#1$1",focus="m")]
[name="悲伤的士兵"]......
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="积极的士兵"]愿广阔的大地保佑吾王♪
[charslot(slot="m",name="avg_npc_241",focus="m")]
[name="冷静的士兵"]......保佑他的人民和他的福祉♪
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="开朗的士兵"]赐予我们无限的恩典♪
[name="开朗的士兵"]你咋不唱呢？
[charslot(slot="m",name="avg_npc_729_1#1$1",focus="m")]
[name="悲伤的士兵"]......
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="开朗的士兵"]别愁眉苦脸了！大伙儿不都有伤吗？但我们已经到家门口了，小子！
[name="开朗的士兵"]让我们欢乐地歌唱♪
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="积极的士兵"]维多利亚，我的故乡！♪
[charslot(slot="m",name="avg_npc_729_1#1$1",focus="m")]
[name="悲伤的士兵"]维，维多利亚......我的故乡！♪
[charslot(slot="m",name="avg_npc_242",focus="m")]
[name="开朗的士兵"]小子，我这份口粮吃不完，分你点。
[name="开朗的士兵"]这可是我们回家后的第一顿早餐，得吃得饱饱的。
[charslot(slot="m",name="avg_npc_423_1#1$1",focus="m")]
[name="积极的士兵"]等我们的大部队都进了城，就让那些魔族佬们瞧瞧，谁才是伦蒂尼姆真正的主人！
[charslot(slot="m",name="avgnew_112_siege_1#3$1",focus="m")]
[name="维娜"]......
[charslot(slot="m",name="avg_npc_405_1#5$1",focus="m")]
[multiline(name="摩根")]啧，我不喜欢这首歌......
[charslot(slot="m",name="avg_npc_405_1#2$1",focus="m")]
[multiline(name="摩根")]维娜，你说呢？
[charslot(slot="m",name="avg_155_tiger_1#1$1",focus="m")]
[name="因陀罗"]别问她了，她自己有时候睡觉都忍不住哼哼两句呢。
[charslot(slot="m",name="avgnew_112_siege_1#11$1",focus="m")]
[name="维娜"]汉娜！
[charslot(slot="m",name="avg_npc_396_1#8$1",focus="m")]
[name="达格达"]因陀罗，有这功夫，你不如多吃两口饭。
[name="达格达"]或者分给我，一会儿突击的任务我来打头阵。毕竟你在突进赦罪师密道时受了伤。
[charslot(slot="m",name="avg_155_tiger_1#1$1",focus="m")]
[name="因陀罗"]想得美，只是一些小伤罢了。
[name="因陀罗"]你看，我揍起人来可不会被这种伤拖累。达格达，这次可不许你在我前头。
[charslot(slot="m",name="avg_npc_396_1#6$1",focus="m")]
[name="达格达"]哼。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="m")]
[name="戴菲恩"]我吃完了，再带人去巡逻一圈，确认一下情况，保证行动万无一失。
[name="戴菲恩"]既然军事委员会选择在这个修筑城墙的工人们才知道的备用接驳口布防，说明他们对城内的掌控情况远超我们的估计。
[charslot(slot="m",name="avg_4110_delphn_1#1$1",focus="n")]
[name="？？？"]戴菲恩小姐，巡逻的工作我已经完成了。
[charslot(slot="m",name="avg_4110_delphn_1#4$1",focus="m")]
[name="戴菲恩"]——？！
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_1070_1#5$1",duration=1)]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1070_1#5$1",focus="m")]
[name="希勒少尉"]抱歉，能给我也分一些口粮吗？我还没有吃早饭呢。
[charslot(slot="m",name="avg_npc_405_1#9$1",

... (全文18557字符)
```

### level_act37side_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="32_g4_ordnancefactory",screenadapt="showall")]
[Delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>新奥克特里格区，小型载具厂</><p=2>1098年12月21日 6:13 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[playsound(key="$rungeneral")]
[charslot(slot="m",name="avg_npc_660_1#1$1",duration = 1.5)]
[delay(time=2.5)]
[name="热情的工人"]你们终于来了，队长！帮我看看这张蓝图，奥克和我争论，说设计全新的电能驱动分配阀简直多此一举。
[name="热情的工人"]可照我们所预想的，将来肯定会有越来越多的大家伙从我们工厂运到伦蒂尼姆的每一个地块！
[name="热情的工人"]要我说，就该提前做准备。
[name="热情的工人"]不然到时候，未来真正用上这些载具的家伙们发现载重和牵引力完全不够时，一定会转过头来骂我们这些老东西保守——
[name="热情的工人"]“都是些没远见的家伙！”我可不想挨这种骂！
[charslot(slot="m",name="avg_4072_ironmn_1#8$1",focus="m")]
[name="费斯特"]别叫我队长了，虽然我们关系好，但大家已经不是自救军了。何况我们也都各自回到了自己的工厂。
[name="费斯特"]况且，你觉得奥克真想不到这些？无非也是觉得能省就省。
[charslot(slot="m",name="avg_npc_660_1#1$1",focus="m")]
[name="热情的工人"]......我当然知道，但怎么也不该给后辈添堵吧。
[charslot(slot="m",name="avg_4040_rockr_1#12$1",focus="m")]
[name="洛洛"]马丁叔，我当然理解你的心情。
[name="洛洛"]不过我们总得慢慢来嘛。可露希尔和我们分享了很多她捣鼓出来的无人机技术，我也想把这些新技术统统塞到我们新研发的四足载具里。
[name="洛洛"]可电力供应，如何自动化，这些都是我们现在头疼的问题。蓝图虽然好，但还是得先立足当下慢慢来呀。
[charslot(slot="m",name="avg_4072_ironmn_1#4$1",focus="m")]
[name="费斯特"]马丁叔，先按奥克的说法，弄一个基础版解决燃眉之急。
[name="费斯特"]你的蓝图照旧提交给“伦蒂尼姆工业振兴协会”留档吧，别遗失了。
[charslot(slot="m",name="avg_4072_ironmn_1#2$1",focus="m")]
[name="费斯特"]有议会的支持，工业振兴协会本就以战后恢复维多利亚技术在国际上的领先地位为目的，每一个新的想法都应该被尊重。
[charslot(slot="m",name="avg_npc_660_1#1$1",focus="m")]
[name="热情的工人"]反正你是协会的顾问，你说了算。
[charslot(slot="m",name="avg_4072_ironmn_1#4$1",focus="m")]
[name="费斯特"]唔，最近是不是大伙提的新点子太多了......感觉快审不过来了。
[charslot(slot="m",name="avg_4040_rockr_1#12$1",focus="m")]
[name="洛洛"]毕竟大伙都难得能切实感受到自己的家能因为自己的想法发生前所未有的改变，所以热情都很高。
[charslot(slot="m",name="avg_4072_ironmn_1#4$1",focus="m")]
[name="费斯特"]是啊，工厂的流水线，串联所有街道的快速轨道系统，以及保护整座伦蒂尼姆的城墙和城防炮。
[charslot(slot="m",name="avg_4072_ironmn_1#2$1",focus="m")]
[name="费斯特"]我们可以靠自己的双手，把它们打造成我们想象中的样子。
[charslot(slot="m",name="avg_npc_660_1#1$1",focus="m")]
[name="热情的工人"]哎，你们说别的我都认同，但别是你想象中的样子吧，费斯特。我真怕街道被你改造成大游乐园，所有人都绑在滑索上滑来滑去。
[charslot(slot="m",name="avg_4072_ironmn_1#2$1",focus="m")]
[name="费斯特"]呃，那只是被否决的提案中让大家笑得比较开心的一个嘛，又不能代表我所有的点子。
[charslot(slot="m",name="avg_4072_ironmn_1#11$1",focus="m")]
[name="费斯特"]说到这个，你们厂真的决定把奥克留在核心车间吗？毕竟我听说他以前在的厂和你们不是很对付。
[name="费斯特"]每个工厂都有自己的技术机密，以前也有因为抢订单而互相看不顺眼的情况，对吧......
[charslot(slot="m",name="avg_npc_660_1#1$1",focus="m")]
[name="热情的工人"]哈，这倒是。我们厂也不是所有工人都加入了自救军。
[name="热情的工人"]不过凯瑟琳既然能说服其他工厂一起加入协会互相分享技术，那我们也没什么好保留的——
[Dialog]
[charslot]
[stopmusic(fadetime=1.5)]
[playsound(key="$rungeneral")]
[delay(time=2.5)]
[name="焦急的工人"]来人！来人帮忙！
[name="焦急的工人"]马修先生被人打了！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="55_g6_dusklentiavenue",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)] 
[charslot(slot="l",name="avgnew_112_siege_1#1$1",focus="l")]
[name="维娜"]......我们曾经见过吗，先生？
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r",name="avg_npc_659_1#1$1",posfrom="200,0",posto="0,0",duration=2)]
[charslot(slot="r",afrom=0,ato=1,duration=1.5)]
[delay(time=3)]
[playMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.6)]
[charslot(slot="r",name="avg_npc_659_1#1$1",focus="r")]
[name="忧伤的人"]不，算不上，议长阁下。
[name="忧伤的人"]我叫马修，只是一个有间小工厂的商人，但眼下的日子让我不得不向您抱怨。
[charslot(slot="l",name="avgnew_112_siege_1#12$1",focus="l")]
[name="维娜"]你可以写信给议会，或者直接向工业振兴协会求助。我现在......有别的事情需要好好想想。
[charslot(slot="r",name="avg_npc_659_1#1$1",focus="r")]
[name="忧伤的人"]阁下，我联合停工的十余座工厂写给议会的信，恐怕已经被您搁置大半个月了。
[charslot(slot="l",name="avgnew_112_siege_1#1$1",focus="l")]
[name="维娜"]部分工厂停工是议会已经表决通过的事情。你不该比我更清楚伦蒂尼姆的物流港口现在是什么情况吗？
[charslot(slot="r",name="avg_npc_659_1#1$1",focus="r")]
[name="忧伤的人"]但一座工厂的债务崩溃能压死萨迪恩区或者海布里区的几百个家庭。
[name="忧伤的人"]我们只是想为自己争取一点小小的倾斜——哪怕是以私下的形式。
[name="忧伤的人"]我们这些停工的工厂，工人们想从地下渠道买药都买不起。流水线上那些经验丰富的老工人，可比十台机器还值钱。
[name="忧伤的人"]我相信我的工人们，他们能为这座城市做的事，还有很多。
[name="忧伤的人"]与此同时，疗养院里大量珍贵的矿石病抑制剂被分配给了那些半死不活的伤兵。
[charslot(slot="l",name="avgnew_112_siege_1#10$1",focus="l")]
[name="维娜"]......你想说什么！
[charslot(slot="r",name="avg_npc_659_1#1$1",focus="r")]
[name="忧伤的人"]我想帮您算一笔“经济账”——
[charslot(slot="l",name="avgnew_112_siege_1#10$1",focus="l")]
[name="维娜"]*维多利亚粗口*！
[Dialog]
[PlaySound(key="$d_avg_punchsp4", volume=1)]
[charslot(slot="l",posfrom="0,0",posto="50,0",duration=1)]
[charslot(slot="l",afrom=1,ato=0,duration=0.5)]
[charslot(slot="r",afrom=1,ato=0,duration=0.5)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.5, r=0.5, g=0, b=0, fadetime=0.5, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1.5, block=true)]
维娜反应过来的时候，拳头已经砸在了对方的鼻梁上。
那个叫马修的男人一只手捂着流血的鼻子，另一只手狼狈地在口袋里寻找手帕。
可止不住的鲜血依旧从他的指缝间渗出来，染红了他的衣服。
周围越来越多的人围了上来，所有人都直勾勾地看着维娜。
他们并没有敌意或愤怒，只是每一道目光，都在提醒着维娜，她的无力，她的不合时宜。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[charslot(slot="l",name="avgnew_112_siege_1#10$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_659_1#1$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="l",name="avgnew_112_siege_1#9$1",focus="l")]
[name="维娜"]我——
[charslot(slot="r",name="avg_npc_659_1#1$1",focus="r")]
[name="忧伤的人"]我知道你为什么愤怒，阁下。我知道......但有些话，总得有人说。
[name="忧伤的人"]说出这些话，对我来说，也并不好受。
[name="忧伤的人"]我也曾是自救军的一员，一直留在城里，而你是跟着那个卡特斯女孩一起来的伙伴。后来，你们离开了。
[name="忧伤的人"]等到典范军进城以后，我从凯瑟琳女士那里得知了你是他们的领袖，我没有任何犹豫就同意升起蒸汽欢迎你们。
[name="忧伤的人"]但我第一次看到穿着国王的衣服站在街头，代表议会向大家承诺美好生活的那个人时，却没认出来是你。
[name="忧伤的人"]你明明知道，有些许诺根本兑现不了。你在救下一些人的时候，也在牺牲一些人，不是吗？
[Dialog]
[charslot(slot="l",name="avgnew_112_siege_1#7$1",focus="l")]
[delay(time=0.5)]
[PlaySound(key="$d_avg_clo

... (全文17648字符)
```

### level_act37side_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="34_g5_noblehall",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_176",duration=1.5)]
[delay(time=2)]
[name="夸夸其谈的男人"]我还是很难想象，海蒂小姐。我们好不容易回到了这座伟大的城市，你却又要离开。
[name="夸夸其谈的男人"]不过，也许你是该回到你父亲的身边了。
[charslot(slot="m",name="avg_npc_400_1#1$1",focus="m")]
[name="海蒂"]回到多伦郡吗？......嗯，说不定我会走得更远一些。毕竟，我生命中的领路人，可不止我父亲一位呀。
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[name="海蒂"]当然，您的建议也总能启发我。例如您讲述的，与那位马奇伯爵的使者共进晚宴的经历，就让我学到不少知识。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="夸夸其谈的男人"]哈哈，您这样一位远离政治的小说家想要写一些历史情节，我当然愿意提供一手资料。
[charslot(slot="m",name="avg_npc_400_1#1$1",focus="m")]
[name="海蒂"]又例如您刚才说的，将我最熟悉的故乡多伦郡，与伦蒂尼姆这骇人听闻的战争一并写进故事里。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="夸夸其谈的男人"]没错。要坦诚地回忆那段不甚体面的时光当然不容易，但我们为这座城市所做的英雄之举总该被人记住。
[charslot(slot="m",name="avg_npc_400_1#9$1",focus="m")]
[name="海蒂"]英雄......您说得对，或许我们都算是英雄。
[charslot(slot="m",name="avg_npc_400_1#7$1",focus="m")]
[name="海蒂"]对了，这样的爱情故事一定很迷人。远在维多利亚边境的少女与来此度假的青年一见钟情，但青年死在了伦蒂尼姆的战场上。
[name="海蒂"]当然，少女最终发现自己听到的消息是假的，爱人成为了英雄，回到了她的身边。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="夸夸其谈的男人"]这想法很好，海蒂小姐，失而复得的爱人，正如这座被外人践踏又被我们拯救的城市。
[name="夸夸其谈的男人"]......他们开始奏乐了。听啊，虽然宴会上没有红酒与甜点，灯火也不如过去那么明亮，但铜管中流淌出的音乐不会变得沙哑。
[charslot(slot="m",name="avg_npc_400_1#11$1",focus="m")]
[name="海蒂"]请您移步舞池吧，将您提供的灵感和我都留在这窗台边就好。
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="夸夸其谈的男人"]那请问您的这两位朋友——
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",name="avg_npc_1519_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_487_bobb_1#11$1",duration=1.5)]
[delay(time=2)]
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="r")]
[name="埃利西奥"]呃......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#1$1",focus="m")]
[name="海蒂"]这位来自异国他乡的使者恐怕还不熟悉维多利亚的礼仪，您就放过他吧？
[charslot(slot="m",name="avg_npc_176",focus="m")]
[name="夸夸其谈的男人"]哈哈，当然。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_400_1#7$1",focus="m")]
[name="海蒂"]......
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]......海蒂小姐。这是您的名字，是吗？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#1$1",focus="m")]
[name="海蒂"]——啊。我可以带你们四处走走。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]不，不用再麻烦您了，刚才多谢您替我们解围。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[name="海蒂"]事实上，这里从不拒绝任何客人，如果两位有兴趣，下次可以从客厅的大门走进来，而不是窗台。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="r")]
[name="埃利西奥"]谢谢您的好意。但......其实我对贵族们的宴会没有那么大的兴趣。
[name="埃利西奥"]维多利亚的贵族政治是我最先调查的内容，我很清楚你们的礼仪、对感染者的态度，甚至那种舞步我都学过......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#7$1",focus="m")]
[name="海蒂"]唔，先不说我这样一个三流小说家是否敢自诩贵族......您问过身边这位士兵，她为什么把您带到这里来吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#4$1",focus="r")]
[name="埃利西奥"]——不，不是她带我来的，是我自作主张！
[charslot(slot="l",name="avg_npc_1519_1#2$1",focus="l")]
[name="黛安"]唉。海蒂小姐，对不起。他说想留在伦蒂尼姆，更深入地了解我们的感染者问题，所以我想带他到处看看......偶尔用些不太正当的办法。
[name="黛安"]您想笑话他的话可以直接笑，他就是这样不会说谎也藏不住心事的人。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[name="海蒂"]呵呵，很像他的身份......“赤心”。
[name="海蒂"]埃利西奥先生，您是赤心医疗的代表，对吗？
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="r")]
[name="埃利西奥"]我不记得我们机构有这么大的名气......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#1$1",focus="m")]
[name="海蒂"]对感染者问题有兴趣的人，总是很好认的。
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[name="海蒂"]不过，辨认贵族们默契的谎言，恐怕就没那么容易了。
[name="海蒂"]——比如说，正挽着手进入舞池的人，大半都是感染者。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#4$1",focus="r")]
[name="埃利西奥"]......
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]这从理论上是可预期的，萨卡兹散布的源石粉尘伤害了所有伦蒂尼姆市民，不论身份高低。可是......
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#7$1",focus="m")]
[name="海蒂"]没有人会说破的。没有人会去探究站在自己身边的人是不是感染者，这是他们为自己保留的体面，也是......一种梦想。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#4$1",focus="r")]
[name="埃利西奥"]......
[Dialog]
[charslot]
埃利西奥望向大厅。墙柱上残留着金饰被剥去后留下的坑洼，证明战争的暴徒曾踏足此地，但乐手们倾情的演奏几乎掩盖了眼前的萧条。
自称小说家的女士旋开钢笔的笔帽，在笔记本上潦草地写下了什么。
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[name="海蒂"]当然，您可以认为在温饱都成问题的时候，这些只是毫无意义的自我安慰。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]......不，当然不会。
[name="埃利西奥"]只是一种生活与另一种生活。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[PlaySound(key="$d_avg_paper2", volume=1)]
[delay(time=2.5)]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#4$1",focus="r")]
[name="埃利西奥"]——这是？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_400_1#10$1",focus="m")]
[name="海蒂"]刚刚随手记下的，一个不值一读的故事梗概......和一点额外的信息，请您收下。
[charslot(slot="m",name="avg_npc_400_1#11$1",focus="m")]
[name="海蒂"]我有一种预感，埃利西奥先生，我们会再见面的。
[Dialog]
[charslot]
[charslot(slot="l",name="avg_npc_1519_1#1$1",focus="r")]
[charslot(slot="r",name="avg_487_bobb_1#1$1",focus="r")]
[name="埃利西奥"]......谢谢。
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]不过，请容许我额外过问一句——您似乎有什么痛苦，并不能被眼前的幻想安慰。
[Dialog]
[charslot

... (全文19152字符)
```

### level_act37side_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_courtyard",screenadapt="showall")]
[Delay(time=1)]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>塔楼骑士瞭望塔后院</><p=2>1098年12月22日 5:32 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[charslot(slot="l",name="avg_1019_siege2_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_396_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_1019_siege2_1#1$1",focus="l")]
[name="维娜"]我还以为你会在塔楼上帮忙指挥大伙复原里面的陈设。
[charslot(slot="r",name="avg_npc_396_1#1$1",focus="r")]
[name="达格达"]我也以为你在准备议长广播，维娜。再说，我不会插手设计师们的工作。
[charslot(slot="r",name="avg_npc_396_1#8$1",focus="r")]
[name="达格达"]他们比我更懂如何打造一间博物馆，我同样期待他们打造的“塔楼骑士博物馆”会给我什么惊喜。
[name="达格达"]但雕刻纪念碑的工作，必须我亲手来做。
[name="达格达"]你来看看，怎么样？
[charslot(slot="l",name="avg_1019_siege2_1#8$1",focus="l")]
[name="维娜"]原来你还会这一手。
[charslot(slot="r",name="avg_npc_396_1#8$1",focus="r")]
[name="达格达"]很小的时候，马歇尔老师教我的，不过他老是醉酒忘事，总是记不得把真正的拿手绝活教我。
[name="达格达"]来，给你介绍一下。这是芬恩导师，最后一位警戒长，我最亲近的长辈。
[name="达格达"]这是老弗格森，教会了我喝酒。这是蓓丽老师，费尽心思才教会我化妆。
[name="达格达"]这是马歇尔老师——这可不是我雕的，是他喝醉后自己为自己刻的。
[name="达格达"]这是卡尔，爱哭鬼。这是马丁，每周都会偷偷逃跑，然后被家人送回来。这是凯伦......
[charslot(slot="r",name="avg_npc_396_1#8$1",focus="r")]
[name="达格达"]还有......还有......
[charslot(slot="r",name="avg_npc_396_1#2$1",focus="r")]
[name="达格达"]......
[Dialog]
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[delay(time=2.5)]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[charslot(slot="l",posfrom="0,0",posto="50,0",duration=3.5)]
[delay(time=4)]
维娜轻轻地抱住了达格达，安慰着她。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[charslot(slot="l",posfrom="50,0",posto="0,0",duration=3.5)]
[delay(time=4)]
[charslot(slot="r",name="avg_npc_396_1#2$1",focus="r")]
[name="达格达"]谢谢你，维娜，我没事。
[name="达格达"]只是每次回到这里，以前那些都快模糊的记忆又变得很鲜明。
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[name="维娜"]你还刻上了自己的名字，“伊莎贝尔·孟塔古”......
[charslot(slot="r",name="avg_npc_396_1#2$1",focus="r")]
[name="达格达"]塔楼骑士从不缺席。我们都在这里了，芬恩导师会很开心的。
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[name="维娜"]......其实议会还可以为你们保留塔楼骑士的制度，哪怕你——
[charslot(slot="r",name="avg_npc_396_1#8$1",focus="r")]
[name="达格达"]塔楼骑士的使命已经完成了，不是吗？
[name="达格达"]维多利亚不再需要国王，自然也不再需要塔楼骑士。让过去被博物馆铭记，已经是最好的结局。
[name="达格达"]既然塔楼的灯火不必再为了王宫而亮，我的使命也就彻底结束了。
[name="达格达"]今后伦蒂尼姆不再有塔楼骑士伊莎贝尔，只有达格达。格拉斯哥帮的达格达。
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[name="维娜"]......
[stopmusic(fadetime=1.5)]
[charslot(slot="r",name="avg_npc_396_1#8$1",focus="r")]
[name="达格达"]但维娜，如果你需要塔楼骑士留下来，我依旧不会有任何的迟疑。只要你想。
[charslot(slot="l",name="avg_1019_siege2_1#5$1",focus="l")]
[name="维娜"]不用打趣我，达格达......你也听到了那些流言？
[charslot(slot="r",name="avg_npc_396_1#1$1",focus="r")]
[name="达格达"]戴菲恩和我们都在查是谁在传播流言。但显然很多人完全相信，甚至真心实意地支持——
[name="达格达"]“维娜·维多利亚会加冕为王。”
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="32_g3_school_indoor",screenadapt="showall")]
[Delay(time=2)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, fadetime=2.5, block=true)]
[Delay(time=2)]
[dialog]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣马尔索学校</><p=2>1098年12月22日 5:37 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="r",name="avg_487_bobb_1#7$1",posfrom="-200,0",posto="0,0",duration=2)]
[charslot(slot="r",afrom=0,ato=1,duration=0.5)]
[delay(time=3.5)]
[playsound(key="$rungeneral")]
[charslot(slot="l",name="avg_npc_661_1#1$1",posfrom="-200,0",posto="0,0",duration=1)]
[charslot(slot="l",afrom=0,ato=1,duration=0.5)]
[delay(time=3)]
[charslot(slot="l",name="avg_npc_661_1#1$1",focus="l")]
[name="生闷气的孩子"]埃利西奥先生！埃利西奥先生！请等等！
[charslot(slot="r",name="avg_487_bobb_1#4$1",focus="r")]
[name="埃利西奥"]咦，小杰娜，是还有其他问题想问我吗？
[charslot(slot="l",name="avg_npc_661_1#1$1",focus="l")]
[name="生闷气的孩子"]是老师想要邀请您留下看看我们新戏剧的彩排——
[name="生闷气的孩子"]还有，埃利西奥先生，您能去替我证明吗？
[charslot(slot="r",name="avg_487_bobb_1#1$1",focus="r")]
[name="埃利西奥"]哦？
[charslot(slot="l",name="avg_npc_661_1#1$1",focus="l")]
[name="生闷气的孩子"]杰米和我打赌，就算我能和祖母一起搬家到哥伦比亚，也不会比现在过得更好。
[name="生闷气的孩子"]他的爸爸告诉他，在哥伦比亚，像我们一样的孩子根本没法上学，那里也根本没有会教我们排练戏剧的老师......
[name="生闷气的孩子"]杰米说，您在课上说的，都是谎话——
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="r")]
[name="埃利西奥"]......
[Dialog]
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="none")]
[name="？？？"]杰娜，彩排该你上场了，不要缠着埃利西奥先生了。
[charslot(slot="l",name="avg_npc_661_1#1$1",focus="l")]
[name="生闷气的孩子"]呀，老，老师！
[name="生闷气的孩子"]我只是想邀请埃利西奥先生留下观看我们彩排......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_657_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="茉莉"]交给我吧。杰米还在台上等你，他都快哭了。
[name="茉莉"]你不在，杰米可一句台词都说不出来。快去吧。
[charslot(slot="m",name="avg_npc_661_1#1$1",focus="m")]
[name="生闷气的孩子"]唔，杰米真讨厌......好吧，我这就去......
[name="生闷气的孩子"]埃利西奥先生，请一定要留下来看我们的演出哦！
[Dialog]
[playsound(key="$rungeneral")]
[charslot(duration=1)]
[delay(time=3)]
[charslot(slot="l",name="avg_npc_657_1#1$1",focus="l")]
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="l")]
[name="茉莉"]唉，请原谅孩子们的童言无忌，埃利西奥先生。
[name="茉莉"]不过我并不了解哥伦比亚，也的确不清楚，感染后的孩子在那里会被如何——
[charslot(slot="r",name="avg_487_bobb_1#4$1",focus="r")]
[name="埃利西奥"]他们会被照顾得很好！
[charslot(slot="r",name="avg_487_bobb_1#11$1",focus="r")]
[name="埃利西奥"]......只要他们的监护人能够交上医疗保险。
[charslot(slot="l",name="avg_npc_657_1#8$1",focus="l")]
[name="茉莉"]......
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]......
[charslot(slot="l",name="avg_npc_657_1#1$1",focus="l")]
[name="茉莉"]我知道了。
[name="茉莉"]其实孩子们都很喜欢您，我也很感谢您能为他们讲解感染后应该如何照顾自己的知识，这对孩子们很重要。
[name="茉莉"]辛苦您了。
[charslot(slot="r",name="avg_487_bobb_1#5$1",focus="r")]
[name="埃利西奥"]我在老家也常常为孩子们讲解

... (全文22496字符)
```

### level_act37side_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g3_westlobbythroneroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>我不喜欢圣王会西部大堂内部的那个王座厅。空荡荡的，瘆人。</i>", x=300,y=270,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>孤零零的王座就那么摆在那，我没法想象，要是维娜真坐在上面会是什么样。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>一个人，坐在那个冰冷冷的椅子上，望着那些空无一物的台阶——</i>",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="<i>按维娜的脾气，她一分钟都待不住......我敢打赌。</i>", x=300,y=270,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$darkness_03_loop", volume=0.6)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>圣王会西部大堂王座厅</><p=2>1098年12月23日 3:26 A.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[charslot(slot="m",name="avg_1019_siege2_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="维娜"]王冠找到了？现在在哪？
[charslot(slot="m",name="avg_npc_229_1#1",focus="m")]
[name="号角"]不算找到，是有人送到了议长办公室。至于丢失的准确时间，不好查，但大致能确定是在你的演讲开始之后。
[charslot(slot="m",name="avg_npc_405_1#13$1",focus="m")]
[name="摩根"]......之前维娜就把王冠放在那个空王座上。可偷走王冠能有什么好处啊？是那些公爵指示的吗？
[charslot(slot="m",name="avg_1019_siege2_1#7$1",focus="m")]
[name="维娜"]我想不是。
[name="维娜"]公爵从不是铁板一块，他们都有自己的打算。只是王冠丢失和他们拜访伦蒂尼姆这两件事同时发生，实在过于巧合了。
[charslot(slot="m",name="avg_npc_405_1#13$1",focus="m")]
[name="摩根"]可按你的说法，那玩意儿现在不就一个上了点年纪的破铁环吗？
[charslot(slot="m",name="avg_npc_229_1#5",focus="m")]
[name="号角"]......呃，摩根，并非如此。
[name="号角"]王冠在很多人心中，与维多利亚的关系非同寻常，无论它现在的处境如何。
[name="号角"]它被空置的二十多年，许多民众非但没有遗忘它，反倒愈加期待——
[name="号角"]......期待下一位能戴上王冠的贤君，期待新的国王能彻底扫清维多利亚的阴霾。
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]不，更多人只是迫切地需要一个足以说服所有人的奇迹来满足他们自己内心对于王权的渴望和崇拜。
[charslot(slot="m",name="avg_npc_229_1#1",focus="m")]
[name="号角"]我无法否认。而且他们的声音，你并不陌生，维娜。
[name="号角"]你的身份，的确极为特殊。本就是王室后裔，又是当之无愧的战争英雄，可偏偏还是在街头长大，许多人天然会对你产生好感。
[name="号角"]加之议会的顺利建立和公爵们的主动让权，他们会更加坚信，你已经获得了所有人的支持。
[name="号角"]接下来的事，无非就是水到渠成——
[charslot(slot="m",name="avg_npc_405_1#4$1",focus="m")]
[name="摩根"]可那些大公爵的真正想法根本不是这样！
[charslot(slot="m",name="avg_npc_229_1#5",focus="m")]
[name="号角"]可民众只会在乎结果，摩根。
[charslot(slot="m",name="avg_1019_siege2_1#7$1",focus="m")]
[name="维娜"]是啊......从我们回家的那天起，我就很清楚了。可惜，有时候，我很擅长让人失望。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="55_g6_dusklentiavenue",screenadapt="showall")]
[Delay(time=2)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2.5, block=true)]
[Delay(time=2)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>新奥克特里格区街道</><p=2>1098年12月23日 4:59 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_409_1#1$1",focus="m")]
[name="悠闲的市民"]埃利西奥先生，谢谢您分享的能量棒。如果每次都有这么美味的谢礼，我很乐意天天接受您的采样体检，哈哈。
[name="悠闲的市民"]在哥伦比亚，这些真的都是商品吗？为什么你们哥伦比亚人要在日常生活中屯这些，也是为了应对天灾吗？
[charslot(slot="m",name="avg_487_bobb_1#1$1",focus="m")]
[name="埃利西奥"]没有啦，只是我的个人喜好。
[name="埃利西奥"]我时常觉得，吃饭无非是平衡能量和营养的过程，既然能量棒能让这个过程更快些，那为什么要拒绝呢？
[charslot(slot="m",name="avg_487_bobb_1#1$1",focus="m")]
[name="埃利西奥"]呃，不过黛安总是批评我这种想法就是了。
[charslot(slot="m",name="avg_npc_409_1#1$1",focus="m")]
[name="悠闲的市民"]不意外，毕竟在当下的伦蒂尼姆，能解决基本的食物需求已经值得感恩。
[name="悠闲的市民"]这已经是亚历山德莉娜殿下付出了很大努力的结果了。
[charslot(slot="m",name="avg_npc_417_1#1$1",focus="m")]
[name="局促的市民"]干嘛和他说这些......
[name="局促的市民"]埃利西奥先生，谢谢您带来的这些......嗯，“能量棒”。但您该走了。
[charslot(slot="m",name="avg_npc_409_1#1$1",focus="m")]
[name="悠闲的市民"]斯坦利，你总不会在害怕埃利西奥先生会——
[charslot(slot="m",name="avg_npc_417_1#1$1",focus="m")]
[name="局促的市民"]我没有！
[name="局促的市民"]我......我总不能当着别人的面为那些蠢事跟你吵起来吧？
[charslot(slot="m",name="avg_487_bobb_1#4$1",focus="m")]
[name="埃利西奥"]哦？
[charslot(slot="m",name="avg_npc_409_1#1$1",focus="m")]
[name="悠闲的市民"]唉。他不喜欢我尊称亚历山德莉娜为“殿下”，就这。
[name="悠闲的市民"]我和斯坦利在政见上很不一样，我觉得现在有个国王不算坏事，但他呢，坚持认为国王还在时我们活得更差。
[charslot(slot="m",name="avg_npc_417_1#1$1",focus="m")]
[name="局促的市民"]......
[charslot(slot="m",name="avg_npc_409_1#1$1",focus="m")]
[name="悠闲的市民"]但您看，不管是从前还是现在，我们俩的日子不都照样过？
[charslot(slot="m",name="avg_487_bobb_1#11$1",focus="m")]
[name="埃利西奥"]......所以，您是说，有没有国王，对你们的生活都不会有影响？
[charslot(slot="m",name="avg_npc_417_1#1$1",focus="m")]
[name="局促的市民"]不管她怎么想，事实就是，就算那个王座上还要坐人，也轮不到我们去吃国王的加冕宴。
[charslot(slot="m",name="avg_npc_409_1#1$1",focus="m")]
[name="悠闲的市民"]唉，斯坦利，你什么时候才能想出些更让我信服的理由。
[name="悠闲的市民"]埃利西奥先生，抱歉，我又得花点时间开导这位死脑筋了。
[name="悠闲的市民"]对了，至于城里频繁有城防军活动是为什么，我确实听说过一点流言——有人偷走了王冠，巡逻队正在调查相关的人。
[name="悠闲的市民"]走吧，斯坦利。再见，埃利西奥先生。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[delay(time=3.5)]
[charslot(slot="m",name="avg_487_bobb_1#7$1",focus="m")]
[name="埃利西奥"]......不过黛安确实从来没提过哪怕一句国王与王冠的话题。或许回去之后可以问问她的看法。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="43_g7_towngreenhouse",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, fadetime=2.5, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="疗养院患者"]埃利西奥先生，您应该休息一下，您几乎一直在外协助收集病例信息。
[charslot(slot="m",name="avg_487_bobb_1#7$1",focus="m")]
[name="埃利西奥"]城里的感染者病例几乎是在同一时间段内遭遇了急性感染，且大都有非常少见的病理进程，我必须尽可能多地记录下这些珍贵的数据。
[name="埃利西奥"]无论是未来用于研究矿石病，还是针对伦蒂尼姆的市民开发专向的药物，这些数据都意义重大。
[name="埃利西奥"]对了，莎拉女士，黛安今天怎么没有来探望你？
[charslot(slot="m",name="avg_npc_418_1#1$1",focus="m")]
[name="疗养院患者"]黛安？
[name="疗养院患者"]我以为她在帮你忙。今天还有好多老战友来疗养院想问问最近有没有发现什么异样，本来还想拉着黛安和老朋友们一起聚聚呢。
[charslot(slot="m",name="avg_487_bobb_1#11$1",focus="m")]
[name="埃利西奥"]——？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0,g=0,

... (全文18358字符)
```

### level_act37side_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Background(image="bg_cherunder_2",screenadapt="showall")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="32_g1_lentiavenue",screenadapt="showall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.5, fadetime=0)]
[Delay(time=1)]
[PlaySound(key="$d_avg_mgcbttlfld",channel="1",loop=true,volume=1)]
[playMusic(intro="$m_bat_walkinthedust_intro", key="$m_bat_walkinthedust_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[playsound(key="$p_atk_blackcannon_d", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[playsound(key="$p_atk_blackcannon_d", volume=1)]
[CameraShake(duration=0.5, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=true)]
[playsound(key="$p_imp_blackcannon_d", volume=1,channel="1")]
[Delay(time=0.2)]
[playsound(key="$d_avg_boomdust", volume=1,channel="2")]
[CameraShake(duration=0.5, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Delay(time=1.5)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>奥克特里格区前线T1阵地</><p=2>1098年10月2日 6:23 A.M. 战争结束日</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[charslot(slot="m",name="avg_npc_1331_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="“灵幛”"]死亡......在尽头......等待......
[name="“灵幛”"]宗长......注视......死亡，注视......你们......
[Dialog]
[charslot(duration=1.5)]
[delay(time=3.5)]
[PlaySound(key="$d_gen_soldiersrun",channel="2",volume=1)]
[charslot(slot="m",name="avg_npc_414_1#1$1",duration=1.5)]
[delay(time=2.5)]
[name="兴奋的士兵"]队长，目标已清除！但后续弹药预估只能维持两分钟！
[name="兴奋的士兵"]需要下一步的指令！
[charslot(slot="m",name="avg_npc_229_1#7",focus="m")]
[name="号角"]小队所有成员，准备好面对白刃战！
[name="号角"]坚持最后两分钟，我会掩护你们撤退！
[Dialog]
[playsound(key="$d_gen_transmissionget", volume=1)]
[interlude(maskid = "group_interclude_vertical_common" ,size = "290,760", style=0 ,switch = true, offset = "250,0", channel = 3,tsfrom = "0,1", tsto="1,1",tsduration = 0.5)]
[interlude(channel = 3, type = 3, slot = "m", switch = false, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#1$1", duration = 1)]
[charslot(slot="m",posfrom="0,0",posto="-200,0",duration=1.5,focus="m")]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_229_1#1",posfrom="200,0",posto="-200,0",focus="m")]
[name="号角"]推进之王，后续火力支援即将告罄！
[charslot(slot="m",name="avg_npc_229_1#7",posfrom="200,0",posto="-200,0",focus="m")]
[name="号角"]火力轰炸区预计会在三分钟后停止火力覆盖！你那边战况如何？
[charslot(slot="m",name="avg_npc_229_1#7",posfrom="200,0",posto="-200,0",focus="none")]
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#3$1", duration = 0)]
[name="维娜"]食腐者的浓雾完全驱散不了！
[name="维娜"]工人们开辟出来的补给线被这些鬼东西完全切断了，战略物资没办法迅速补充到你们的阵地。
[name="维娜"]你们做好撤出T1阵地的准备。
[interlude(channel = 3, type = 3, slot = "m", switch = false, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#3$1", duration = 0)]
[charslot(slot="m",name="avg_npc_414_1#1$1",posfrom="200,0",posto="-200,0",focus="m")]
[name="兴奋的士兵"]不行！一旦让出T1阵地，联军的包围圈岂不是从我们这里被突破了！队长，我不能接受——
[charslot(slot="m",name="avg_npc_229_1#7",posfrom="200,0",posto="-200,0",focus="m")]
[name="号角"]战场不是让你们逞能的地方！遵守命令！
[charslot(slot="m",name="avg_npc_229_1#7",posfrom="200,0",posto="-200,0",focus="none")]
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#3$1", duration = 0)]
[name="维娜"]我们已经向罗德岛其他同僚发送了求援信号，现在必须信任博士他们的安排了。
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#6$1", duration = 0)]
[name="维娜"]士兵，我们已经到家了，先活下来！然后才能把失去的东西夺回来！
[interlude(channel = 3, type = 3, slot = "m", switch = false, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#6$1", duration = 0)]
[charslot(slot="m",name="avg_npc_414_1#1$1",posfrom="200,0",posto="-200,0",focus="m")]
[name="兴奋的士兵"]......
[charslot(slot="m",name="avg_npc_229_1#2",posfrom="200,0",posto="-200,0",focus="m")]
[name="号角"]推进之王，我们会防守阵地最后两分钟，然后后撤回援，协助你们清除浓雾里的怪物！
[name="号角"]风笛，保护好他们！
[Dialog]
[charslot(slot="m",name="avg_npc_229_1#2",posfrom="200,0",posto="-200,0",focus="none")]
[playsound(key="$d_gen_transmissionget", volume=1)]
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_222_bpipe_1#8", duration = 1.5)]
[name="风笛"]收到，队长！
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#6$1", duration = 0)]
[name="维娜"]一旦发现雾气驱散不了，别管我们，赶紧前往I12区域和高多汀的一零六突击炮旅会合，继续战斗。
[interlude(channel = 3, type = 3, slot = "m", switch = false, pfrom = "235,0", pto="235,0", name = "avg_1019_siege2_1#6$1", duration = 0)]
[charslot(slot="m",name="avg_npc_229_1#2",posfrom="200,0",posto="-200,0",focus="m")]
[name="号角"]我知道。
[charslot(slot="m",name="avg_npc_229_1#2",posfrom="200,0",posto="-200,0",focus="none")]
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_222_bpipe_1#1", duration = 0)]
[name="风笛"]那就待会再见了，队长——
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "char_empty", duration = 0)]
[name="通讯中的声音"]（怪异的嚎叫）
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_222_bpipe_1#6", duration = 0)]
[name="风笛"]小心，推进之王！
[playsound(key="$d_gen_transmissionget", volume=1)]
[interlude(channel = 3, type = 3, slot = "m", switch = true, pfrom = "235,0", pto="235,0", name = "avg_4110_delphn_1#3$1", duration = 0)]
[name="戴菲恩"]是赦罪师的那些奇美拉怪物..

... (全文32523字符)
```

### level_act37side_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="32_g1_lentiavenue",screenadapt="showall")]
[cameraEffect(effect="Grayscale", keep=true, amount=0.5, fadetime=0)]
[Delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_writerub", volume=1)]
[Sticker(id="st1", multi = true, text="<i>“胜利”。</i>", x=300,y=270,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>拳台上，它所承载的，是赞美与荣誉。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>但在战场上，它承载的，却是无数沉重的生命。</i>",block = true)]
[Sticker(id="st1")]
[Sticker(id="st1", multi = true, text="<i>食腐者之王的死，给所有目睹那一幕的人，留下了太多的恐惧。我不愿去回忆，也不想把它写进我的书里。</i>", x=300,y=270,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>那个萨卡兹，不需要我去铭记。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>但，我会永远缅怀查尔斯·林奇，最后的蒸汽骑士。</i>",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot(slot="m",name="avg_npc_405_1#5$1",duration=1.5)]
[Delay(time=2.5)]
[name="摩根"]......他，已经多久没有动了？
[charslot(slot="m",name="avg_npc_396_1#1$1",focus="m")]
[name="达格达"]十分钟。
[Dialog]
[charslot]
[playMusic(key="$wasteland_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_651_1#1$1",focus="m",duration=1.5)]
[Delay(time=2.5)]
没有人靠近查尔斯·林奇。
在场的所有人都远远地围在一起，半跪着，向最后的蒸汽骑士致以敬意。
他就那么直直地矗立在圣王会西部大堂之前，蒸汽从他盔甲的每一丝裂缝中向外喷涌。
灼热。不停。
[Dialog]
[bgeffect(name="$eb_steamrelease",layer=2)]
[PlaySound(key="$d_avg_steamrelease")]
[bgeffect(layer=2)]
[Delay(time=2.5)]
宛如心脏跳动的声音。
[charslot(slot="m",name="avg_npc_229_1#1",focus="m")]
[name="号角"]他的身体明明已经在与食腐者的战斗中受到了这么严重的损伤，居然还能维持着站姿......
[charslot(slot="m",name="avg_1019_siege2_1#5$1",focus="m")]
[name="维娜"]支撑他站着的，从来不是他的身体，否则他早该止步在诸王长眠之所里了。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[delay(time=3.5)]
维娜向着蒸汽骑士的方向走去，所有人都看到了她的动作。
[Dialog]
[charslot(slot="m",name="avg_155_tiger_1#9$1",focus="m")]
[name="因陀罗"]维娜，不要靠近他！他已经没有理智了！
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]......不，我必须要确认。
[charslot(slot="m",name="avg_npc_405_1#4$1",focus="m")]
[name="摩根"]之前在地下他差点杀了你，维娜！
[charslot(slot="m",name="avg_npc_396_1#12$1",focus="m")]
[name="达格达"]让推进之王去吧。
[charslot(slot="m",name="avg_npc_396_1#13$1",focus="m")]
[name="达格达"]蒸汽骑士......不，查尔斯·林奇的状态不对劲。她应该也看出来了。
[charslot(slot="m",name="avg_npc_405_1#6$1",focus="m")]
[name="摩根"]可是——
[charslot(slot="m",name="avg_npc_396_1#13$1",focus="m")]
[name="达格达"]相信她。
[charslot(slot="m",name="avg_npc_405_1#6$1",focus="m")]
[name="摩根"]......
[Dialog]
[charslot]
维娜靠近了蒸汽骑士，她能感受到灼人的蒸汽几乎让周围的温度都缓缓升高。
[Dialog]
[charslot(slot="m",name="avg_1019_siege2_1#5$1",duration=1.5)]
[Delay(time=2.5)]
[name="维娜"]我从没见过你这样，哪怕是在诸王长眠之所。
[name="维娜"]战争结束了，你已经守护了你的维多利亚，你的使命已经结束了。
[Dialog]
[charslot(slot="m",name="avg_npc_651_1#1$1",focus="m")]
[PlaySound(key="$d_avg_steamrelease",volume=0.5)]
[CameraShake(duration=1, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[bgeffect(layer=2)]
[Delay(time=1)]
[name="查尔斯·林奇"]（急促的喷气声）
[charslot(slot="m",name="avg_1019_siege2_1#5$1",focus="m")]
[name="维娜"]你还在寻找什么，那把剑吗？抱歉，它遗失在了这片战场上的某个地方。
[Dialog]
[charslot(slot="m",name="avg_npc_651_1#1$1",focus="m")]
[PlaySound(key="$d_avg_steamrelease",volume=0.5)]
[CameraShake(duration=1, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="查尔斯·林奇"]（急促的喷气声）
[charslot(slot="m",name="avg_1019_siege2_1#10$1",focus="m")]
[name="维娜"]或者说，你等的，不是那把剑？
[Dialog]
[charslot]
维娜轻轻地触碰到了蒸汽骑士的甲胄，上面斑驳的痕迹无一不刻录着查尔斯·林奇的经历——
宣誓继承称号那天与同僚的比试。
征战边陲平叛，在漫天巫术中幸存。
诸王长眠之所的背叛。
向“荣光”号冲锋，向源石冲锋......
查尔斯·林奇从未倒下。
查尔斯·林奇永远注视维多利亚。
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]你在注视着圣王会西部大堂......我知道了。
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]不止是你，还有很多人都在注视着那里。
维娜回望着远处围着的维多利亚人，受伤的，沉默的，兴奋的，哭泣的......
人们早已自发围起了一堵绵延不绝的人墙，拦住了外面更加骚动不安的人群。
他们都轻声念着不同的名字。
“推进之王”。“维娜”。“亚历山德莉娜”。“维多利亚”。
[Dialog]
[charslot(slot="m",name="avg_npc_651_1#1$1",focus="m")]
[PlaySound(key="$d_avg_steamrelease",volume=0.5)]
[CameraShake(duration=1, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="查尔斯·林奇"]（急促的喷气声）
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]我从来都不相信你疯了。
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]查尔斯·林奇，这是我们第二次正式见面。
[name="维娜"]我曾希望，如果能走出那片黑暗，你也能找到想要守护的东西。
[charslot(slot="m",name="avg_1019_siege2_1#9$1",focus="m")]
[name="维娜"]而我们都已经走到了这里......那现在，请等着我回来吧。
[Dialog]
[charslot(slot="m",name="avg_npc_651_1#1$1",focus="m")]
[PlaySound(key="$d_avg_steamrelease",volume=0.5)]
[CameraShake(duration=1, xstrength=5, ystrength=5, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="查尔斯·林奇"]（急促的喷气声）
[Dialog]
[charslot]
维娜从蒸汽骑士的身边走过，走上了圣王会西部大堂的台阶，独自走进了大堂的深处。
[Dialog]
[Delay(time=1.5)]
时间在流逝。
起初，人群静悄悄的，而后声音越来越嘈杂，骚动在蔓延。
[name="人群中的声音"]为什么这么久？难道里面还有其他的敌人？
[name="人群中的声音"]我们需不需要去帮忙——
[name="人群中的声音"]安静！相信亚历山德莉娜殿下！
[name="人群中的声音"]没有看到连蒸汽骑士大人也在安静等着吗？
[name="人群中的声音"]听说陛下的王冠就存放在里面。你说，会不会等她出来，我们就有一个新的国王了！
[charslot(slot="m",name="avg_4110_delphn_1#7$1",focus="m")]
[name="戴菲恩"]不对劲，按照之前的情报，军事委员会不该有更多的抵抗力量了。
[name="戴菲恩"]里面应该什么都没有才对。
[charslot(slot="m",name="avg_155_tiger_1#6$1",focus="m")]
[name="因陀罗"]就这么干耗着吗？我们直接打进去看看不就知道了。
[charslot(slot="m",name="avg_npc_405_1#6$1",focus="m")]
[name="摩根"]......
[charslot(slot="m",name="avg_4072_ironmn_1#1$1",focus="m")]
[name="费斯特"]我去吧。
[charslot(slot="m",name="avg_4162_cathy_1#4$1",focus="m")]
[name="凯瑟琳"]其他人比你更合适——
[charslot(slot="m",name="avg_4072_ironmn_1#4$1",focus="m")]
[name="费斯特"]奶奶，可只有我们会驾驶“爬行号”。
[name="费斯特"]有它在，不会有任何危险的。哪怕是对上蒸汽骑士，至少我也有把握自保。
[Dialog]
[PlaySound(key="$rungeneral",volume=1)]
[charslot(duration=1.5)]
[delay(time=3.5)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Bloc

... (全文23082字符)
```

### level_act37side_09_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="21_G1_interrogat_room",screenadapt="showall")]
[Delay(time=1)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>城防军临时监禁室</><p=2>1098年12月25日 8:32 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",name="avg_npc_422_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_1519_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]呼——2区总算是打扫干净了，接下来就只剩下4区了。怎么样，当值的活不算轻松吧，要不要歇会？
[charslot(slot="r",name="avg_npc_1519_1#1$1",focus="r")]
[name="黛安"]我打扫的速度可没比你慢。
[charslot(slot="r",name="avg_npc_1519_1#2$1",focus="r")]
[name="黛安"]倒是你，不必顾着我是感染者就故意让着我。
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]嘿嘿。也不算吧，只是觉得你经历了这么多，总该会有点心累吧。
[charslot(slot="r",name="avg_npc_1519_1#2$1",focus="r")]
[name="黛安"]......我还以为——呵，至于王冠那件事，我想得很明白。
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]一时冲动嘛！加上大伙有这个想法的可不在少数。
[name="勤快的守卫"]不过说起来，好像一夜之间，大伙都没那么害怕感染者了。
[charslot(slot="r",name="avg_npc_1519_1#1$1",focus="r")]
[name="黛安"]那是因为我们在伦蒂尼姆。议会和议长阁下颁布的政策，至少的确让许多人不再把恐惧和厌恶直接摆在脸上。
[name="黛安"]照我一位哥伦比亚来的朋友所说，其他地方还是老样子。
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]......不管怎么说，谢谢你帮忙打扫，不然队长又得罚我了。
[charslot(slot="r",name="avg_npc_1519_1#8$1",focus="r")]
[name="黛安"]我应该感谢你们并不限制我的活动，能做点事情也让我更心安。
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]要我说，你完全不用担心议会的处理结果。不然，伦蒂尼姆这么多可以关你的地方，何必专门选城防军的禁闭室呢。
[name="勤快的守卫"]不就是冲着大伙不是老战友就是老熟人，能帮忙照顾你吗？放心，等过几天风头过了，随便找个借口你就能回家了。
[name="勤快的守卫"]那些还专门去议长办公室抗议的人才是真看不懂局势，维娜老大的为人我们还不清楚吗？
[charslot(slot="r",name="avg_npc_1519_1#6$1",focus="r")]
[name="黛安"]......
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]嗯？不舒服吗？要不要先歇会儿？
[charslot(slot="r",name="avg_npc_1519_1#2$1",focus="r")]
[name="黛安"]你说......议长会放了我？
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]哈，你就安安心心暂时在这避避风头吧。为了你那件事，外面现在可是沸沸扬扬。
[name="勤快的守卫"]队长不让给你收音机和报纸也是担心你知道了会瞎想。
[charslot(slot="r",name="avg_npc_1519_1#2$1",focus="r")]
[name="黛安"]......
[charslot(slot="l",name="avg_npc_422_1#1$1",focus="l")]
[name="勤快的守卫"]对了，要是你实在紧张的话，我那个因为贪酒经常被扔进来关禁闭的好兄弟在这藏了些好货。
[name="勤快的守卫"]等我给你拿点。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",posfrom="0,0",posto="-200,0",duration=1.5)]
[charslot(slot="l",afrom=1,ato=0,duration=1)]
[Delay(time=4.5)]
[charslot]
黛安苦笑着，试图聆听外面的声音。
可除了水流通过管道的声音之外，她只能隐隐约约听到城防军操练的声音。
在她被送进来之后，她与外面的一切联系几乎都被切断了。
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]......不知道埃利西奥先生是否一切还好。
[name="黛安"]真该提前和他说一声。他现在应该很担心我......
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="none")]
[name="？？？"]的确。他几乎找遍了所有自己认识的人为你求情。
[charslot(slot="m",name="avg_npc_1519_1#6$1",focus="m")]
[name="黛安"]议长阁下......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_1019_siege2_1#8$1",duration=1.5)]
[Delay(time=2.5)]
[name="维娜"]很好，他们并没有像对待犯人一样对待你。
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]这也是您的安排吗？
[charslot(slot="m",name="avg_1019_siege2_1#9$1",focus="m")]
[name="维娜"]不。大伙自发的，他们认为你不该得到这样的判决。
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]很多人为了你的事来找过我。你的朋友，我的朋友......还有我们共同的战友，甚至那些根本不认识你的市民。
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_422_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_422_1#1$1",focus="m")]
[name="勤快的守卫"]——黛安，我把那小子藏的好酒偷了一点。
[Dialog]
他狠狠灌了一口酒。
[charslot(slot="m",name="avg_npc_422_1#1$1",focus="m")]
[name="勤快的守卫"]噗！
[Dialog]
[charslot]
士兵尚未走到黛安与维娜的面前，就强行控制身体立定了。而他灌在嘴里的酒，吐也不是，吞也不是。
他只好藏住手里的酒瓶，向维娜行了军礼。
[charslot(slot="m",name="avg_npc_422_1#1$1",focus="m")]
[name="勤快的守卫"]唔——
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]别藏了，帕特尔。
[name="维娜"]我记得，号角小姐说过，军营里是禁酒的。
[charslot(slot="m",name="avg_npc_422_1#1$1",focus="m")]
[name="勤快的守卫"]（吞下）咳——咳——
[name="勤快的守卫"]是，维娜老大！可，这不是......呃......
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]我可以不告诉号角小姐，但你也得替我保密我来见黛安的事。
[name="维娜"]还有，酒放下，你不是给黛安准备的吗？
[charslot(slot="m",name="avg_npc_422_1#1$1",focus="m")]
[name="勤快的守卫"]呃......好吧。维娜老大，你专门来找黛安就是为了之后的安排吧？
[Dialog]
[charslot(slot="m",name="avg_1019_siege2_1#7$1",focus="m")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]是。
[charslot(slot="m",name="avg_npc_422_1#1$1",focus="m")]
[name="勤快的守卫"]我就说你不用担心嘛，黛安！
[name="勤快的守卫"]我就先去打扫4区了。我今天可是老老实实执勤了一天，什么都不知道。
[Dialog]
[stopmusic(fadetime=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[Delay(time=3.5)]
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]帕特尔留下的酒，你想先尝尝吗？闻起来不差。
[Dialog]
[playMusic(key="$wasteland_loop", volume=0.6)]
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[Delay(time=1.5)]
黛安有些低落地摇了摇头。
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]那介意我先来点吗？唉，和那些公爵开会，已经说得我口干舌燥。
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]议长阁下，您把我安排在这里，真的是为了要......
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]我们希望在老朋友身边，你会开心些。况且，你并不希望我那么做不是吗？
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]......是的。
[charslot(slot="m",name="avg_1019_siege2_1#5$1",focus="m")]
[name="维娜"]说实话，我没有你想象中那么坚决，我过去的生活，与你，与大多数的伦蒂尼姆人并无本质区别。
[name="维娜"]黛安，我的确犹豫过。
[charslot(slot="m",name="avg_npc_1519_1#8$1",focus="m")]
[name="黛安"]所以，您这次来，是关于我的处置已经有了定论？
[charslot(slot="m",name="avg_1019_siege2_1#7$1",focus="m")]
[name="维娜"]呼——我想，我必须亲自告诉你议会的决定，以及......
[charslot(slot="m",name="avg_1019_siege2_1#1$1

... (全文12589字符)
```

### level_act37side_09_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="21_G1_interrogat_room",screenadapt="showall")]
[Delay(time=1)]
[playMusic(key="$saferoom_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_1519_1#2$1",duration=1.5)]
[delay(time=2.5)]
[name="黛安"]维娜......我不喜欢这个故事。
[name="黛安"]长眠于王座之上不得安息的君王，还有放下了王冠的英雄......
[name="黛安"]故事结束了，可什么都没有改变，不是吗？
[name="黛安"]阿利斯泰尔陛下，还有你，维娜，你们都想要让维多利亚变得更好，可结果呢......
[Dialog]
[PlaySound(key="$d_avg_drinkswllw", volume=1)]
[Delay(time=2)]
黛安狠狠地灌了一口酒。
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]咳——咳——
烈酒呛得她明明已经红肿的眼睛又挤出些泪光来。
[charslot(slot="m",name="avg_npc_1519_1#2$1",focus="m")]
[name="黛安"]如果国王都做不到，那我们还能怎么做？
[name="黛安"]......我们真的什么都没法改变吗？
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]可故事还没结束呢，黛安。
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]我也以为国王安息之后，就该是落幕......可还是有一个意想不到的人找上了我。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="55_g3_westlobbythroneroom",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_1019_siege2_1#1$1",duration=1.5)]
[Delay(time=2)]
[name="维娜"]......我应该问你为什么会出现在这里吗——
[Dialog]
[charslot]
王座之后，一道白色的身影自阴影中浮现。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=0,g=0, b=0, fadetime=2, block=true)]
[Subtitle(text="“在维多利亚的许多传说中，我们总是能捕捉到那位仙子的身影......”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“权力，阴谋，命运，梦想成真，流传数百年的童话里，她似乎拥有不同的力量，可谁也说不清，哪一个才是真正的她。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
“维娜，你见到了谁？”
[Dialog]
[Delay(time=1)]
[Subtitle(text="“我见到了独角兽。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="？？？"]维娜，你大大出乎了我的意料，你让我看到了新的可能。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="m",name="avg_npc_401_1#1$1",duration=1.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_401_1#8$1",focus="m")]
[name="“独角兽”"]放下你手中的锤吧，我并非你的敌人。
[charslot(slot="m",name="avg_npc_401_1#1$1",focus="m")]
[name="“独角兽”"]我们也曾并肩作战过，不是吗？
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]你到底是谁，独角兽？
[charslot(slot="m",name="avg_npc_401_1#8$1",focus="m")]
[name="“独角兽”"]裁缝的女儿，自救军的领袖，维多利亚的见证者......
[charslot(slot="m",name="avg_npc_401_1#1$1",focus="m")]
[name="“独角兽”"]当然，还有许多可怜的老人哪怕在临死之际，依旧一厢情愿地在他们撰写的史书中称呼我为“护国公”。
[name="“独角兽”"]驻留在维多利亚的数百年里，我已经抹去过太多的身份，但眼下，我就是克洛维希娅——
[charslot(slot="m",name="avg_npc_401_1#10$1",focus="m")]
[name="“独角兽”"]一个衷心为你所取得的成绩感到满意的朋友。这个回答是否能让你满意，维娜？
[charslot(slot="m",name="avg_1019_siege2_1#2$1",focus="m")]
[name="维娜"]呵，又一个长生者？你欺骗了自救军中所有的同伴，欺骗了罗德岛。
[charslot(slot="m",name="avg_npc_401_1#9$1",focus="m")]
[name="“独角兽”"]欺骗？我从未欺骗过任何人。人人皆有所愿，我只是满足他们的心愿罢了。
[name="“独角兽”"]受萨卡兹之祸困扰的普通人想要活着，于是我指挥自救军找出一条生路。
[charslot(slot="m",name="avg_npc_401_1#1$1",focus="m")]
[name="“独角兽”"]深陷权力斗争的古老家族不愿覆灭在帝国的漩涡中，于是我替那位可怜的公爵解决一切可能断绝家族延续的威胁。
[name="“独角兽”"]弗雷德里克三世希冀维多利亚不会因红龙而再度混乱，我同样可以满足他的心愿。
[charslot(slot="m",name="avg_1019_siege2_1#10$1",focus="m")]
[name="维娜"]......所以，现在你找上了我？
[charslot(slot="m",name="avg_npc_401_1#1$1",focus="m")]
[name="“独角兽”"]亚历山德莉娜，阿利斯泰尔的女儿，你怎么会认为我此刻才注意到你。
[charslot(slot="m",name="avg_npc_401_1#10$1",focus="m")]
[name="“独角兽”"]维娜，历史是一艘帆船，而决定方向的人，永远是你们。
[name="“独角兽”"]既然你想要改变维多利亚，我可以帮你。你希望以什么身份去实现你的理想？
[name="“独角兽”"]国王，议长，甚至是典范军的唯一领袖，你都可以选。
[Dialog]
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[Delay(time=2.5)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.5, r=0,g=0, b=0, fadetime=2, block=true)]
“维娜，我不得不说，你讲的故事实在缺少了新意，我在老书店里读过太多这样的故事......”
“结局也总是英雄接受了那位仙子留下的礼物。所以，你最后选了议长......？”
[Dialog]
[Subtitle(text="“不，我什么都没有选，黛安。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“数百年的起起伏伏，让独角兽习惯了由她来选择谁是英雄，而英雄只需要选择想要得到什么奖励。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“但凭什么？”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
“‘凭什么’......？”
[Dialog]
[Delay(time=1)]
[Subtitle(text="“对，凭什么我又非得选择她。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_1019_siege2_1#9$1",focus="m")]
[Delay(time=2.5)]
[charslot(slot="m",name="avg_npc_401_1#5$1",focus="m")]
[name="“独角兽”"]你为什么要笑，维娜？
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]你听到外面的声音了吗？
[name="维娜"]他们在为胜利欢呼，也在为维多利亚欢呼。
[name="维娜"]他们中有很多只关心身边小事的人，这些人没有心思去保护任何人。有时，甚至小气到不愿意分给饿肚子的家伙们一口吃的。
[name="维娜"]但就为了那一毫一分，他们却又愿意豁出了命去拼。他们才是我的维多利亚。
[charslot(slot="m",name="avg_1019_siege2_1#9$1",focus="m")]
[name="维娜"]我喜欢那些混蛋，我也愿意罩着那些傻瓜。
[charslot(slot="m",name="avg_1019_siege2_1#8$1",focus="m")]
[name="维娜"]而你更没资格，让我选我明明早就在做的事，克洛维希娅。
[Dialog]
[PlaySound(key="$a_bat_buildingshaking_1",channel="1",volume=0.5)]
[CameraShake(duration=2, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="维娜"]哈，你恐怕得走了，除非你不怕尴尬。
[charslot(slot="m",name="avg_npc_401_1#5$1",focus="m")]
[name="“独角兽”"]......
[Dialog]
[charslot]
[PlaySound(key="$d_avg_giantmecha",channel="2",volume=1)]
[PlaySound(key="$a_bat_buildingshaking_1",channel="1",volume=1)]
[CameraShake(duration=1.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="？？？"]推进之王！
[charslot(slot="m",name="avg_npc_401_1#10$1",focus="m")]
[name="“独角兽”"]你也是个傻瓜，亚历山德莉娜，就像你父亲一样。
[name="“独角兽”"]替我告诉他们，那个裁缝的女儿死了。
[name="“独角兽”"]他们的愿望，我已经实现了。
[Dialog]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[PlaySound(key="$rungeneral",volume=1)]
[charslot(slot="m",name="avg_4072_ironmn_1#6$1",duration=1.5)]
[dela

... (全文27367字符)
```

### level_act37side_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK",is_video_only=true)] 
[stopmusic]
[Background(image="bg_black",screenadapt="coverall")]
[playMusic(intro="$empty",key="$empty")]
[Video(res="video/act37side/GO01.mp4")]
```

### level_act37side_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Image(image="55_i17_2", screenadapt="coverall",fadetime=0)]
[Delay(time=1)]
[PlayMusic(key="$ouat_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>维多利亚忠诚的塔楼骑士伊莎贝尔·孟塔古曾说过——</i>", x=300,y=240,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>“历史就像一座谷仓。”</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>它在繁忙的宅院中沉默、不起眼，还带着一点令人不悦的陈腐的霉味。人们也只有需要往里面塞点什么的时候才能想起它。</i>",block = true)]
[Sticker(id="st1")]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>包容，沉默地包容就是它唯一的工作。</i>", x=300,y=240,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>而人们或许就是生长在麦田里的一株株麦子，经历过一生的风吹雨打，才能结出一点难能可贵的麦穗。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>你经历的这一切，最后都会变成金灿灿的麦种，存放在这座名为历史的谷仓里。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>应该说，历史就是无数人人生的陈列室。</i>",block = true)]
[playsound(key="$d_avg_paper1",volume=1)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="摩根"]金灿灿？嗯，我想那的确是金灿灿的一生......
[Dialog]
[musicvolume(volume=0.3, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[delay(time=1)]
[Image(image="32_i01_1", screenadapt="coverall",fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0.7, fadetime=0)]
[PlaySound(key="$bigbell",volume=1)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[name="激昂的声音"]维娜，这把剑属于你。
[name="激昂的声音"]这是你的命运。
[name="维娜"]父亲，这是......？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[delay(time=1)]
[Background(image="25_mini02_victoria_street_n", screenadapt="coverall", block=true)]
[PlaySound(key="$bigbell",volume=1)]
[delay(time=2)]
[PlaySound(key="$fightgeneral", volume=0.7)]
[PlaySound(key="$d_avg_punchsp5",volume=1,delay=0.5)]
[PlaySound(key="$d_avg_punch02",volume=1,delay=0.7)]
[CameraShake(duration=2, xstrength=35, ystrength=35, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_405_1#11$1",focus="m")]
[name="摩根"]维娜！你做了什么！
[name="摩根"]快停手！你要打死他了！
[Dialog]
[charslot]
[charslot(slot="m",name="avgnew_112_siege_1#10$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avgnew_112_siege_1#10$1",focus="m")]
[name="维娜"]呼......呼......
[charslot(slot="m",name="avgnew_112_siege_1#5$1",focus="m")]
[name="维娜"]我......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=1)]
[Background(image="50_g2_mainbattlefield", screenadapt="coverall", block=true)]
[PlaySound(key="$bigbell",volume=1)]
[delay(time=2)]
[PlaySound(key="$d_avg_explosion", volume=0.4, loop=false, channel="explo")]
[PlaySound(key="$d_gen_explo_n", volume=0.5, loop=false, channel="explo1",delay=0.9)]
[CameraShake(duration=2, xstrength=35, ystrength=35, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_229_1#7",focus="l")]
[charslot(slot="r",name="avgnew_112_siege_1#7$2",focus="l")]
[name="号角"]维娜！现在正是时候！
[charslot(slot="r",name="avgnew_112_siege_1#7$2",focus="r")]
[name="维娜"]交给我！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[image]
[charslot]
[delay(time=1)]
[Background(image="55_g3_westlobbythroneroom", screenadapt="coverall", block=true)]
[PlaySound(key="$bigbell",volume=1)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_401_1#1$1",focus="m")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[charslot(slot="m",name="avg_npc_401_1#1$1",focus="m")]
[name="克洛维希娅"]维娜，你希望自己是以什么身份离开这座宫殿？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_1019_siege2_1#7$1",duration=1)]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_1019_siege2_1#7$1",focus="m")]
[name="维娜"]......
[charslot(slot="m",name="avg_1019_siege2_1#1$1",focus="m")]
[name="维娜"]我选择——
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[image]
[charslot]
[Image(image="55_i17_2", screenadapt="coverall",fadetime=0)]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[delay(time=1)]
[musicvolume(volume=0.6, fadetime=2.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>或许这就是历史运行的方式，身处其中的人不甘现状，拼尽全力与命运抗争。</i>", x=300,y=240,  alignment="left", size=24, delay=0.04, width=700,block = true)]
[Sticker(id="st1", multi = true, text="\n<i>而现实总是像汹涌的潮水，一次又一次地将你打翻在地。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>你不得不再一次站起，想办法站稳脚跟。你知道战斗还没有结束，你必须做好准备迎接下一轮拳头。</i>",block = true)]
[Sticker(id="st1", multi = true, text="\n<i>直到你兜兜转转，却发现自己又以另一种方式回到了原点——</i>",block = true)]
[Sticker(id="st1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="摩根"]哦，我想起来了，或许达格达原话说的是，“磨盘”。
[name="摩根"]“历史就像一个磨盘”？
[name="摩根"]我忘了她的比喻到底是什么，不过应该是磨坊啊风车啊，这一类能让人联想起夕阳的东西。
[Dialog]
[delay(time=1)]
[name="摩根"]见鬼，我一直都不喜欢她那套文绉绉的腔调。
[Dialog]
[PlaySound(key="$d_avg_writerub", volume=1)]
[delay(time=1.5)]
[Blocker(a=0.5, r=0, g=0, b=0, fadetime=0.7, block=true)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Sticker(id="st1", multi = true, text="<i>总之，我想要在这里记下的

... (全文39803字符)
```

### level_act37side_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="55_g7_repairedlentiavenue",screenadapt="showall")]
[Delay(time=1)]
[playMusic(key="$wasteland_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1)]
[animtext(id = "at1", name = "group_location_stamp", style="avg_both", pos = "-400,-200", block = false)]<p=1>诺伯特区街道</><p=2>1098年12月26日 5:23 P.M.</>
[delay(time=3)]
[animtextclean]
[delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",name="avg_155_tiger_1#8$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_396_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_155_tiger_1#8$1",focus="l")]
[name="因陀罗"]达格达，你那边情况如何？
[charslot(slot="r",name="avg_npc_396_1#2$1",focus="r")]
[name="达格达"]黎恩老大还活着，但瘸了条腿。他最好的兄弟，没挺过来，我问了当初那些老熟人......
[name="达格达"]没人知道他那个兄弟具体什么时候走的，可能是当初逃离诺伯特区时，也可能是联军反攻时被走投无路的萨卡兹......
[charslot(slot="l",name="avg_155_tiger_1#6$1",focus="l")]
[name="因陀罗"]你见到黎恩老大了？
[charslot(slot="r",name="avg_npc_396_1#13$1",focus="r")]
[name="达格达"]见了，他现在在货港干活。他不怎么提起过去的日子了，也绝口不提自己的兄弟。
[charslot(slot="r",name="avg_npc_396_1#12$1",focus="r")]
[name="达格达"]但他觉得，如今得好好活着。
[charslot(slot="l",name="avg_155_tiger_1#9$1",focus="l")]
[name="因陀罗"]......*维多利亚粗口*。
[name="因陀罗"]我也去以前罩着的厂子逛了一圈，多了些毛头小子，甚至都没听说过我们格拉斯哥帮。
[name="因陀罗"]那帮崽子可真是欠揍！
[charslot(slot="r",name="avg_npc_396_1#13$1",focus="r")]
[name="达格达"]......你去那间我们常去的老餐馆了吗？
[charslot(slot="l",name="avg_155_tiger_1#6$1",focus="l")]
[name="因陀罗"]......
[charslot(slot="l",name="avg_155_tiger_1#8$1",focus="l")]
[name="因陀罗"]拆了。议会那边派人来联系了街区许多店铺的原主人，烂得没法修的，原主人也找不到的，都准备拆了重建。
[name="因陀罗"]日落街酒店，保罗的酒吧，那个卡西米尔小崽子开的杂志铺......都没了。
[charslot(slot="r",name="avg_npc_396_1#2$1",focus="r")]
[name="达格达"]汉娜......
[charslot(slot="l",name="avg_155_tiger_1#8$1",focus="l")]
[name="因陀罗"]我还去了他们说的那片公共墓地，我没找到麦克拉伦，也没找到——
[Dialog]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_155_tiger_1#2$1",focus="l")]
[name="因陀罗"]（哽咽）他妈的，为什么那些墓碑都不刻上名字。
[charslot(slot="r",name="avg_npc_396_1#2$1",focus="r")]
[name="达格达"]......
[charslot(slot="l",name="avg_155_tiger_1#9$1",focus="l")]
[name="因陀罗"]妈的，我怎么能在你面前哭。
[charslot(slot="l",name="avg_155_tiger_1#8$1",focus="l")]
[name="因陀罗"]走吧，我们回家。摩根恐怕都等不及了。
[Dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="37_g1_glasgowboxinggym",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_405_1#8$1",focus="m")]
[name="摩根"]我原以为......拳馆的状况会更糟些。
[name="摩根"]谢谢你。
[name="摩根"]看来你一直都有在帮忙看管。
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_862_1#9$1",duration=1.5)]
[Delay(time=2)]
[name="卡铎尔"]我想着，如果你们还活着，迟早有天得回来......不管怎么说，我也算格拉斯哥帮的人。
[charslot(slot="m",name="avg_npc_405_1#6$1",focus="m")]
[name="摩根"]你当初没有和我们一起上温德米尔公爵的军舰——
[charslot(slot="m",name="avg_npc_862_1#3$1",focus="m")]
[name="卡铎尔"]我还没废物到需要那些公爵贵族来救我。
[charslot(slot="m",name="avg_npc_862_1#9$1",focus="m")]
[name="卡铎尔"]不过......我得承认，当时我的确有点傻。后来，我带着一伙兄弟一直在诺伯特区周围干那些魔族佬。
[name="卡铎尔"]我从那些魔族佬嘴里听说了典范军的事。
[charslot(slot="m",name="avg_npc_862_1#2$1",focus="m")]
[name="卡铎尔"]你们做了件我从来都不敢想的事，哈，军队......外面战场翻天覆地的时候，我也和其他人去前线做了点事。
[name="卡铎尔"]但我们能做到的很有限，最后还受了些伤——
[charslot(slot="m",name="avg_npc_405_1#2$1",focus="m")]
[name="摩根"]......你也感染了？
[charslot(slot="m",name="avg_npc_862_1#2$1",focus="m")]
[name="卡铎尔"]是啊......听说因陀罗不也是因为不久前在战场上受了伤才感染的。
[charslot(slot="m",name="avg_npc_862_1#11$1",focus="m")]
[name="卡铎尔"]有你们这些朋友在，她可真走运。
[Dialog]
[charslot(slot="m",name="avg_npc_405_1#6$1",focus="m")]
[Delay(time=1.5)]
摩根愣住了，因为她从没想过这个问题。甚至连因陀罗自己都没想过。
[charslot(slot="m",name="avg_npc_405_1#7$1",focus="m")]
[name="摩根"]不对，不对，怎么听你这么说感觉怪怪的。呃，可我一下也弄不清你哪说得不对。
[charslot(slot="m",name="avg_npc_862_1#1$1",focus="m")]
[name="卡铎尔"]哈，随便吧。反正如果有机会，替我对推进之王说声对不起。
[charslot(slot="m",name="avg_npc_405_1#3$1",focus="m")]
[name="摩根"]你可以留下，自己跟她说。
[charslot(slot="m",name="avg_npc_862_1#10$1",focus="m")]
[name="卡铎尔"]我的格拉斯哥帮已经不在了，既然你们都回来了，我也该走了。
[charslot(slot="m",name="avg_npc_862_1#11$1",focus="m")]
[name="卡铎尔"]戴菲恩没和你们回来？
[charslot(slot="m",name="avg_npc_405_1#13$1",focus="m")]
[name="摩根"]她陪在维娜身边。
[charslot(slot="m",name="avg_npc_862_1#11$1",focus="m")]
[name="卡铎尔"]哈，看来你们也闹了一架。我从广播里听说了戴菲恩她妈妈的事......不管她身份是啥，至少她是个有种的人。
[charslot(slot="m",name="avg_npc_405_1#3$1",focus="m")]
[name="摩根"]你接下来去哪？
[charslot(slot="m",name="avg_npc_862_1#11$1",focus="m")]
[name="卡铎尔"]诺伯特区重建还需要人手，货港每天都有货要从城外运进来，我和我的兄弟们还得看着点。
[charslot(slot="m",name="avg_npc_862_1#9$1",focus="m")]
[name="卡铎尔"]然后......然后再去把中央区来的混账商人们揍一顿——呃——
[charslot(slot="m",name="avg_npc_405_1#2$1",focus="m")]
[name="摩根"]......
[charslot(slot="m",name="avg_npc_862_1#2$1",focus="m")]
[name="卡铎尔"]也许吧。摩根，诺伯特区已经变了。
[name="卡铎尔"]我熟悉的人不在了，常去的店也没了，街区里新冒出来一帮屁都不懂的小崽子妄图争个高下......
[charslot(slot="m",name="avg_npc_862_1#3$1",focus="m")]
[name="卡铎尔"]——反正，拳馆我还给你们了。
[charslot(slot="m",name="avg_npc_862_1#11$1",focus="m")]
[name="卡铎尔"]广播里议会说了很多新鲜事，我和几个兄弟谈好了，等过段时间就去其他公爵领看看。
[charslot(slot="m",name="avg_npc_862_1#4$1",focus="m")]
[name="卡铎尔"]我们会找到新地盘的。
[charslot(slot="m",name="avg_npc_862_1#11$1",focus="m")]
[name="卡铎尔"]新的地盘，新的开始。我得花点时间才能忘记有些事情......
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(duration=1.5)]
[delay(time=2.5)]
[charslot(slot="m",name="avg_npc_405_1#6$1",focus="m")]
[name="摩根"]......
[Dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot="l",name="avg_155_tiger_1#6$1",duration=1.5)]
[charslot(slot="r",name="avg_npc_396_1#1$1",duration=1.5)]
[delay(time=2.5)]
[charslot(slot="l",name="avg_155_tiger_1#6$1",focus="l")]
[name="因陀罗"]摩根，刚刚出去的，是卡铎尔？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_405_1#13$1",focus="m")]
[name="摩根"]是的。
[name="摩根"]他来和我们告别，顺带把它还给我们。
[Dialog]
[charslot]
她掏出了一柄蝴蝶刀，上面有些残缺，但依旧可以清晰看到格拉斯哥帮的标记。
贝尔德的蝴蝶刀——汉娜不会认错，上面的标记，还是当初她打赢贝尔德后非要刻上的。
[charslot(slot="l",name="avg_155_tiger_1#6$1",focus="l")]
[charslot(slot="r",name

... (全文29627字符)
```

### training_act37side_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动37side教学关_a

[Tutorial(protectTime=0.5, dialogHead="$avatar_dagda", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
听维娜说最近街上不太平，有人在打货运轨道车的主意。

[PopupDialog(dialogHead="$avatar_tiger")] 哈，都是些街上的小流氓罢了，不算什么威胁。

[Tutorial(protectTime=0.5, dialogHead="$avatar_dagda", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
但如果他们抢劫了轨道车，拿到了武器装备，必定会给治安造成更大的麻烦。

[Tutorial(tileX=1, tileY=2, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_dagda", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
我们应该抢先一步回收这些装备。

[Tutorial(tileX=1, tileY=2, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_morgan")] \
这些装备能给我们带来一定的增益，<@tu.kw>把干员部署于装备所在的地块</>就可以使用了。

[Tutorial(tileX=1, tileY=3, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_morgan")] \
未装配刀片会提高攻击力。

[Tutorial(tileX=1, tileY=1, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_morgan")] \
防护背心会提高防御力。

[Tutorial(tileX=1, tileY=2, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_morgan")] \
而冲击式施术单元，在干员使用自身技能后可以令敌人短时间<@tu.kw>战栗</>，并对其造成<@tu.kw>法术伤害</>。


[PopupDialog(dialogHead="$avatar_morgan")] 但是那些行窃打劫的暴民也可以使用它们。我们必须尽量防止装备被他们捡走。

[PopupDialog(dialogHead="$avatar_morgan")] 看似无害的敌人，拿上装备之后也不容小觑。

[PopupDialog(dialogHead="$avatar_morgan")] <@tu.kw>战栗</>中的敌人所持的装备会受到更多的伤害，从而更容易被打落，我们可以利用这一点。

[Tutorial(protectTime=0.5, dialogHead="$avatar_tiger", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
嘁，有一些装备来不及回收了，打起精神迎战吧。
```

### training_act37side_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动37side教学关1_b

[PopupDialog(dialogHead="$avatar_dagda")] 这家伙害得我使不上劲了！

[Tutorial(protectTime=0.5, dialogHead="$avatar_morgan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
他装备了冲击式施术单元，集中注意力，只要能让他扔下装备，事情就好办了。
```

### training_act37side_01_c

```
[HEADER(is_skippable=true, is_autoable=false)] 活动37side教学关1_c

[PopupDialog(dialogHead="$avatar_dagda")] 稍微......有点吃力。

[Tutorial(protectTime=0.5, dialogHead="$avatar_tiger", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这个敌人装备了防护背心，从正面很难击倒他。

[Tutorial(tileX=3, tileY=4, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_tiger", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
这个位置不错，还可以利用上面的冲击式施术单元。

[Tutorial(protectTime=0.5, dialogHead="$avatar_tiger", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
我来试试！
```

### training_act37side_01_d

```
[HEADER(is_skippable=true, is_autoable=false)] 活动37side教学关1_d

[Tutorial(protectTime=0.5, dialogHead="$avatar_tiger", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
坏了，光顾着解决这边的敌人，被偷袭了！

[Tutorial(protectTime=0.5, dialogHead="$avatar_tiger")] \
喂，想想办法，摩根！货运轨道车被击破的话，装备就要洒得满街都是了！
```

### training_act37side_01_e

```
[HEADER(is_skippable=false, is_autoable=false)] 活动37side教学关1_e

[Tutorial(tileX=4, tileY=4, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_morgan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
该启动<@tu.kw>军工厂指令平台</>了，这样能改变轨道，让货运轨道车向军工厂指令平台移动，保护它们。

[Tutorial(protectTime=0.5, dialogHead="$avatar_morgan", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
我也该去活动活动了！

[Battle.EnsureMinCost(cost=45)]
```


## 统计

- 总字符数：437303
- 对话行数：3105


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
