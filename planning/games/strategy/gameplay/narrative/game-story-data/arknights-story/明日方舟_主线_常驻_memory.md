# 明日方舟 · 主线/常驻 · memory（371段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 主线/常驻, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟主线/常驻「memory」完整剧情脚本（371个文件，6070行对话）

## 正文
## 章节信息

- 分类：主线/常驻
- 目录：obt/memory
- 脚本文件数：371

### story_12fce_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
你不应当跟着我。
在我前去的地方有永不停息的战火。
你只是累赘而已，没必要自寻死路。
[name="？？？"]我......
[name="？？？"]...... 
[Dialog]
[delay(time=2)]
[Background(image="bg_battlefield",screenadapt="coverall")]
[playMusic(intro="$frontline_intro", key="$frontline_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$d_sp_ballista", volume=0.7)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]萨弗拉，你怎么还杵在那，嫌命太长吗！
[Dialog]
[Character]
[Character(name="char_009_12fce_1",fadetime=1,block=true)]
[Delay(time=1)]
[name="？？？"]！
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]*萨卡兹粗口*，快找个掩体蹲下，炮火来了！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$d_sp_ballista", volume=0.7)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[delay(time=1)]
[Character(name="char_009_12fce_1")]
[name="？？？"]咳，咳咳！
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]哟，还活着吗？！
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]还好。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]这里的狙击点暴露了，时间不多，现在马上转移！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$d_sp_ballista", volume=0.7)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[Dialog]
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]那么快又再来？！
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$d_sp_ballista", volume=0.7)]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true)]
[delay(time=1)]
[Character(name="avg_npc_053")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="萨卡兹佣兵"]啊啊啊，该死！我的小腿！
[Character(name="char_009_12fce_1")]
[name="？？？"]（施展法术）
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="？？？"] 这边！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_053")]
[name="萨卡兹佣兵"]咳咳，谢了兄弟。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]只不过是利用一下掩体，举手之劳。
[name="？？？"]腿还好吧。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]小问题，不知道受过多少次这样的小伤了。包扎一下就行。
[name="萨卡兹佣兵"]不说我，兄弟你也不像很能打的样子，竟能撑到现在。
[name="萨卡兹佣兵"]看你用源石技艺挪动掩体来掩护的样子，手法老道啊。
[name="萨卡兹佣兵"]你这是第几次上战场了？
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]虽然做过不少训练，但是这还是第一次。
[name="？？？"]到现在也全凭运气，不是什么大不了的事情。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]你还挺谦虚。
[name="萨卡兹佣兵"]不过说真的，再这么僵持下去可不是个办法。
[name="萨卡兹佣兵"]上头的人倒是轻松，但我们这可吃不消啊。
[name="萨卡兹佣兵"]看来这里就我们俩了，不知道其他人如何。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]我和其他人失散了......原本的突袭任务失败了，敌人冲散了我们。
[name="？？？"]前面一点动静都没了，看来冲到前方的队员都......
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]啧，那可真是巧，我也一样。
[name="萨卡兹佣兵"]我已经不指望他们能回来帮我了。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]就算是任务失败了，我可不准备在这里倒下。
[name="？？？"]我去四周侦察下，一定有逃出包围圈的方法。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]侦察？你？
[name="萨卡兹佣兵"]我不是看不起你，兄弟。
[name="萨卡兹佣兵"]但我敢保证，不管你的源石技艺能帮你制造多少掩体，只要你的白色脑袋晃悠出去，对面的炮火马上就能把你炸得稀烂。
[name="萨卡兹佣兵"]还不如我们先在这里观望观望。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]那可不成......
[name="？？？"]三点钟方向......有敌人来了。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]该死的库兰塔？
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]对面的是轻装库兰塔佣兵。虽然可能还有其他敌人......通常会协同作战。
[name="？？？"]等他们冲过来，就没地方能逃了。
[name="？？？"]可能还配备了术师无人机。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]你，怎么知道得这么清楚？
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"]简单的推断，猜测，经验。
[name="？？？"]可能有猜错的，但是大致如此。
[name="？？？"]虽然现在出去可能比较醒目，但是我们的位置躲不了多久。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]知道得这么清楚，那岂不是你也能轻松干掉他们？
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="？？？"] 凭我的源石技艺可做不到，估计一出手就会被敌人解决掉了。
[name="？？？"] 对我来说，只是逃跑就已经拼尽全力了。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]哈哈哈看来雇你来上战场的雇主也是看走了眼。
[name="萨卡兹佣兵"]打败仗的原因竟然是太抠门只能雇来这样的士兵。
[name="萨卡兹佣兵"]......之前没来得及问。
[name="萨卡兹佣兵"]萨弗拉，你叫什么名字？
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="46A"]我的名字很多，现在叫我46A就行。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]哈，这个是名字么？听上去像是什么家用电器的编号。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="46A"]其中一个代号而已，暂时就这样叫我就行。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]听你这么说，看来是你自己也没想好。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=2)]
[name="46A"]名字也许不重要。
[Character(name="avg_npc_053",name2="char_009_12fce_1",focus=1)]
[name="萨卡兹佣兵"]也对，看来你和我一样，见机行事混口饭吃。
[name="萨卡兹佣兵"]我是不是听到炮弹的声音了？！
[name="萨卡兹佣兵"]走，46A，快走！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[PlaySound(key="$d_sp_ballista", volume=0.7)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[Charact

... (全文11276字符)
```

### story_absin_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_undergroud_u_2",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.8, crossfade=1, delay=0.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
地下废墟
[dialog]
[PlaySound(key="$transmission", volume=0.6)]
[delay(time=1)]
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]......这里是罗德岛干员......
[dialog]
[charslot]
[PlaySound(key="$d_avg_button", volume=0.6)]
[Delay(time=1)]
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]......重复，这里是罗德岛干员苦艾与干员......早露。
[charslot(slot="m",name="avg_405_absin_1#7$1")]
[name="苦艾"]约两个小时三十分钟前，我们于乌萨斯边境天灾疏散任务中与队伍失散，陷入一处塌方形成的地下空洞......
[charslot(slot="m",name="avg_405_absin_1#7$1")]
[name="苦艾"]......目前暂时没有人员伤亡。最后的位置坐标......
[dialog]
[charslot]
[PlaySound(key="$d_avg_button", volume=0.6)]
[Delay(time=1)]
[playsound(key="$transmission",volume=0, loop=true, channel="bgs")]
[SoundVolume(volume=1,channel="bgs", fadetime=0)]
[Delay(time=1)]
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]......
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]收到请回复。
[dialog]
[StopSound(channel="bgs", fadetime=0)]
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]......
[charslot(slot="m",name="avg_405_absin_1#9$1")]
[name="苦艾"]不行，还是联络不上。
[charslot(slot="m",name="avg_405_absin_1#9$1")]
[name="苦艾"]也许我得再换个位置——
[charslot]
[name="？？？"]——你怎么站起来了？
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="char_197_poca_1#2",duration=1.5)]
[delay(time=2)]
[name="早露"]你应该坐下来好好休息，你的腿......
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]娜塔莉娅。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]你离开了三十分钟，有什么发现吗？
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]......很遗憾，没有能帮助我们离开这里的发现呢。
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]不过你说的没错，里面的确是一个自然形成的溶洞，但透光处位于更深处的正上方，而不是直线尽头。
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]无法沿着洞穴离开，头顶的透光处又过高，没有外部援助，我们很难出去。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]看来和这里的情况差不多。我知道了，谢谢你的确认。
[charslot(slot="m",name="char_197_poca_1#1")]
[name="早露"]不用谢！
[charslot(slot="m",name="char_197_poca_1#1")]
[name="早露"]不如说，反而是我应该谢谢你......
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]对了，苦艾小姐，你感觉好些了吗？你的伤口怎么样了？
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]我在后勤部门的时候，学习过有限条件下的急救措施，可以再帮你检查一下止血情况，然后换药。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]不用......
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]不要急着拒绝我。你为了救我受伤，又带着我避开了后续的余震。这都是我应该做的。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[delay(time=2)]
[Background(image="bg_snow_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_snowfootstep", volume=1)]
[delay(time=2)]
[charslot(slot="m",name="char_197_poca_1#1")]
[name="早露"]......东侧已经疏散完毕，确认没有居民了！
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]山脚的最后一户也已经安全转移。时间不够了，我们需要尽快撤离，否则天灾——
[dialog]
[charslot]
[PlaySound(key="$d_avg_rockfall", volume=1)]
[playsound(key="$smallearthquake", volume=1)]
[CameraShake(duration=-1, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=false)]
[delay(time=3)]
[charslot(slot="m",name="avg_405_absin_1#4$1")]
[name="苦艾"]——当心！
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]啊——！
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]苦艾小姐！
[charslot(slot="m",name="avg_405_absin_1#6$1")]
[name="苦艾"]......抓住我！
[dialog]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_avg_rockfall", volume=1)]
[playsound(key="$smallearthquake", volume=1)]
[CameraShake(duration=3, xstrength=4, ystrength=4, vibrato=20, randomness=30, fadeout=true)]
[delay(time=6)]
[charslot]
[name="苦艾"]嘶......啊。
腿部传来的剧痛使苦艾的声音变得扭曲。但她很快将痛呼压低，隐忍不发，强行将注意力转移到周围。
在这陡至的黑暗中，她一无所获。
[Dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[delay(time=1)]
[name="苦艾"]......看不清。
[name="苦艾"]之后肯定还有余震，得快点转移位置。
[name="苦艾"]呃——光棒不在我这里。早......娜塔莉娅！你能听见我说话吗？
[name="苦艾"]娜塔莉娅？
她伸出手去，交握的掌心仍然温热，所幸两人并未因坠落而彻底分散开来。
但此刻另一只手的主人却毫无回音。
[name="早露"]......
[name="苦艾"]......昏迷了？
[name="苦艾"]有血腥味，黏稠......她头上好像也出血了。
[name="苦艾"]头部出血......
[name="苦艾"]得先转移位置，最好有些光线才能看清楚。
[name="苦艾"]（轻敲断壁）
断壁横梁带出一阵空洞的回响，驱散头脑中的混沌。闭眼后再睁眼，她的视野逐渐清晰。
[name="苦艾"]......来吧，来吧。至少给我一个更安全的方向。
苦艾搀扶起昏迷的同伴，向隐约有光的地方挪去。
[Dialog]
[charslot]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[delay(time=3)]
[Background(image="bg_undergroud_u_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_405_absin_1#2$1")]
[name="苦艾"]我只是做了我应该做的。
[charslot(slot="m",name="avg_405_absin_1#2$1")]
[name="苦艾"]换了罗德岛的其他任何人，他们也都会这样做。带着同伴，找到结构更稳定的地下空间，争取救援时间......固定流程而已。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]而且就像你头上的伤一样，我的腿伤也不严重，都是外伤，已经止血，也没有骨头需要掰正，急救派不上用场。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]你不用太在意。
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]......
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]那......通讯器？
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]还是无法联络外界。
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]而且因为里面储存的能源剩得不多，我们不能一直保持开机状态，等待信号被捕捉，只能间隔一段时间再尝试。
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]那我现在还能做些什么吗？
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]目前暂时只能先等等。
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]好......
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]......
[charslot(slot="m",name="avg_405_absin_1#1$1")]
[name="苦艾"]你想问什么，可以直接问。
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]有这么明显吗？
[charslot(slot="m",name="char_197_poca_1#2")]
[name="早露"]其实我是想问我们最后疏散的、住在山脚下的那对母子，他们是不是真的安全撤离了？因为地震来得很突然......
[

... (全文30429字符)
```

### story_acdrop_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="29_g8_alley_n",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness02_intro",key="$darkness02_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_523_1#1$1",fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]你，对，就是你。
[Character(name="char_366_acdrop")]
[name="酸糖"]......这里没别人。
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]我知道。
[name="？？？"]外面主路沿街的墙上，那些涂鸦是你画的？
[Dialog]
[Character(name="char_366_acdrop")]
[Delay(time=1.5)]
[Character(fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]踩着滑板跑了？！
[name="？？？"]别动——不对，你等下，我不是来抓你的！
[Dialog]
[character]
[name="酸糖"]那你想干嘛？
[Dialog]
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]我是想问你，有没有兴趣参加涂鸦比赛？
[Dialog]
[character]
[name="酸糖"]别逗了，哪个城市会举办这种破坏市容的比赛？
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]看看这个。
[Dialog]
[character]
[name="酸糖"]传单？
[Dialog]
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]如果你担心我突然动手，我就把传单放在这里，你自己来拿，好不好？
[Dialog]
[characteraction(name="middle", type="move", ypos=-15, fadetime=0.8, block=true)]
[Blocker(a=0, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_paper1")]
[characteraction(name="middle", type="move", ypos=15, fadetime=0.8, block=true)]
[Delay(time=1)]
[characteraction(name="middle", type="move", xpos=150, fadetime=2, block=false)]
[Character(fadetime=1.5)]
[Delay(time=2)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_366_acdrop",fadetime=1.5)]
[Delay(time=2)]
[name="酸糖"]城市......街头......文化节？涂鸦比赛、滑板竞速、花式跑酷、街舞对战——高额奖金？还要现场直播？
[name="酸糖"]你们市议会的脑子是集体短路了吗？
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]天知道。我只是他们雇来跑腿做宣传的。
[Character(name="char_366_acdrop")]
[name="酸糖"]撒谎。
[name="酸糖"]在小巷子里用“你，对，就是你”这种话招呼人，顺势开始盘问，你可不只是个跑腿的。
[Character(name="avg_npc_523_1#1$1")]
[name="？？？"]职业习惯。
[Character(name="char_366_acdrop")]
[name="酸糖"]你承认自己是警察了？
[Character(name="avg_npc_523_1#1$1")]
[name="警察"]警察已经下班了，我现在只是个发传单赚外快的。
[name="警察"]如果你有兴趣，就拿着这张传单去报名吧。报名时记得让他们把传单的编号记下来，这样你能在比赛全程喝到免费的矿泉水。
[Character(name="char_366_acdrop")]
[name="酸糖"]你也能拿一笔佣金？
[Character(name="avg_npc_523_1#1$1")]
[name="警察"]......听着，姑娘，你不喜欢被人盘问，警察也一样，不管他在执勤还是已经下班了。
[Character(name="char_366_acdrop")]
[name="酸糖"]我——
[Character(name="avg_npc_523_1#1$1")]
[name="警察"]你要是不想参加可以走，别在我身上玩什么探案游戏。要不是急用钱，你以为我不想让你知道破坏公物有多讨人嫌吗？
[Dialog]
[character]
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1",fadetime=1.5)]
[Delay(time=2)]
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1",focus=1)]
[name="酸糖"]（拍拍警察的肩膀）
[Dialog]
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1")]
[characteraction(name="left", type="move", xpos=15, fadetime=1, isblock=true)]
[Blocker(a=0, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_clothmovement")]
[characteraction(name="left", type="move", xpos=-15, fadetime=1, isblock=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1",focus=1)]
[name="酸糖"]抱歉，不该刨根问底的。
[name="酸糖"]去传单上写着的这个地点报名，然后把传单给他们就行了，没错吧？
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1",focus=2)]
[name="警察"]（迟疑地点头）
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1",focus=1)]
[name="酸糖"]现在还开着吗？
[Character(name="char_366_acdrop",name2="avg_npc_523_1#1$1",focus=2)]
[name="警察"]......二十四小时都开。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="29_g7_mainstreet_n",screenadapt="showall")]
[Delay(time=2)]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",fadetime=1.5)]
[Delay(time=2)]
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=1)]
[name="工作人员"]酸糖小姐，我帮您登记好了。您还有别的疑问吗？
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=2)]
[name="酸糖"]是谁想到要举办这种比赛的？
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=1)]
[name="工作人员"]市议会的库珀议员希望让整座城市关注年轻人和风靡年轻群体的街头文化，加深对年轻人的理解......
[name="工作人员"]同时也希望年轻人能更多地参与到城市的建设与维护当中......
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=2)]
[name="酸糖"]我懂了，我懂了，比赛是这位库珀议员办起来的，对吧？
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=1)]
[name="工作人员"]您可以这么理解。
[name="工作人员"]您还有其他事吗？您身后又来了一位报名者，如果可以的话......
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=2)]
[name="酸糖"]呃，最后一件事。
[name="酸糖"]给我传单的那个人说，只要我拿着传单来报名，他就能得到一笔钱。
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=1)]
[name="工作人员"]没错，只要您明天来参加预赛，钱款就会在次日打到他的账上。如果您进入决赛，或是在决赛中获得较好的名次，他还能拿更多。
[name="工作人员"]您也有兴趣为比赛的宣传工作出力吗？
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=2)]
[name="酸糖"]只是好奇。
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=1)]
[name="工作人员"]没关系，您可以看看这里的报酬表......
[Dialog]
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop")]
[characteraction(name="left", type="move", xpos=20, fadetime=1, isblock=true)]
[Blocker(a=0, fadetime=0.2, block=true)]
[PlaySound(key="$d_avg_clothmovement")]
[characteraction(name="left", type="move", xpos=-20, fadetime=1, isblock=true)]
[Blocker(a=0, fadetime=1, block=true)]
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=2)]
[name="酸糖"]光是拉个人来参加比赛都能发这么多钱，这个库珀议员可真有钱啊。
[Character(name="avg_npc_524_1#1$1",name2="char_366_acdrop",focus=1)]
[name="工作人员"]（微笑）
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="29_g6_mainstreet",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[Character(name="avg_npc_524_1#1$1",fadetime=1.5)]
[Delay(time=2)]
[name="工作人员"]时间到！请库珀先生及诸位评委为这一批选手的作品打分！
[name="工作人员"]在打分环节结束之前，选手们

... (全文27805字符)
```

### story_adnach_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="21_G3_victoria_street_d",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.7)]
[PlaySound(key="$d_avg_crwddiscuss_outside",loop=true,channel="bgs",volume=0.5)]
[Delay(time=2)]
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]先生，我们不想惹麻烦。
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]罗德岛，我们治病的地方现在正在改建，我们只是来这个办事处暂时生活一段时间。
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]办事处的人和市政府达成了协议，我们会在未开发地块上生活，不会和郡里的人有交集。
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]我们不会打扰你们。
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]不会打扰？那么这家伙是怎么回事？他可是跑到了我家门口！
[charslot(slot="m",name="avg_npc_974_1#1$1")]
[name="激动的病人"]我以前也是阿什福德郡的人，只是为了治病变卖了家产，离开了这里......
[charslot(slot="m",name="avg_npc_974_1#1$1")]
[name="激动的病人"]难得有一个机会能回来，我只是想看看我以前的家变成了什么样子！
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]原来就是你！
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]我花了大价钱买了这套房子，然后才知道这套房子原来的主人是个倒霉的感染者。
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]从那之后，我的人生就变得倒霉了起来！不仅如此，现在这房子还卖不出去！这一切都是你害的！
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]你也是这个郡的人？从你得了矿石病的那一刻起，你就已经不属于这里了！
[dialog]
[charslot]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="m",name="avg_npc_974_1#1$1")]
[name="激动的病人"]你——
[dialog]
[charslot]
[PlaySound(key="$fightgeneral")] 
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]居然还敢还手......我告诉你，这件事没完！
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]怎么回事？为什么聚集了这么多人？
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]长官，我们——
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]你们不是那群刚来的感染者吗？不好好待在划给你们的地块上，居然偷偷溜进城里来？
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]长官，他们还动手了！
[charslot(slot="m",name="avg_npc_974_1#1$1")]
[name="激动的病人"]我......我只是......
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]啧，我就说，把你们这些感染者放进来准没好事。把这两个人抓起来！
[dialog]
[charslot]
[charslot(slot="r",name="avg_npc_399_1#1$1",duration=1)]
[charslot(slot="l",name="avg_npc_399_1#1$1",duration=1)]
[PlaySound(key="$d_gen_soldiersrun",volume=0.8)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_npc_242")]
[name="亢奋的青年"]没错，就该把他们都赶出去！谁知道他们是真的来借住，还是有别的企图！
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]先生，我们——
[dialog]
[charslot]
[name="安德切尔"]等等。
[dialog]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="char_211_adnach_1#5",duration=2)]
[delay(time=3)]
[charslot(slot="m",name="avg_npc_974_1#1$1")]
[name="激动的病人"]安德切尔先生——
[charslot(slot="m",name="char_211_adnach_1#5")]
[name="安德切尔"]我听到你们的消息就赶过来了，没事吧？
[charslot(slot="m",name="avg_npc_975_1#1$1")]
[name="尝试克制的病人"]我们没事。但是——
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]你又是谁？
[charslot(slot="m",name="char_211_adnach_1#1")]
[name="安德切尔"]我是负责护送这批病人来这里的，罗德岛行动预备组A4小组的队员，安德切尔。
[charslot(slot="m",name="char_211_adnach_1#1")]
[name="安德切尔"]我对病人们的行为负责。
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]负责？怎么负责？你们要是在这里爆炸把我们炸死，谁来赔？
[charslot(slot="m",name="char_211_adnach_1#1")]
[name="安德切尔"]罗德岛正在为了不让这样的事发生而努力。
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]哼，努力有什么用？别以为有大人物同意你们进城，你们就可以为所欲为了。
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]我告诉你，有了今天这件事，明天就能让你们全都滚出去！
[charslot(slot="m",name="char_211_adnach_1#1")]
[name="安德切尔"]......唉。
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]把他们全抓回去！
[Dialog]
[StopSound(channel="bgs",fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cellroomA",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[PlaySound(key="$d_gen_dooropen", volume=0.7)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]精金，你这个办事处负责人现在不该出现在这里。
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]我也不该给你开这个门。
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[name="郡警"]但是，看在你们罗德岛给我弟弟看过病的分上，你可以见他。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]谢谢。
[dialog]
[charslot(slot="m",name="avg_npc_399_1#1$1")]
[delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(duration=2)]
[delay(time=2)]
[PlaySound(key="$d_avg_closedoorheavy", volume=1)]
[delay(time=2)]
[charslot(slot="m",name="char_211_adnach_1#1")]
[name="安德切尔"]罗德里和帕尔梅拉还好吧，有我这个“主犯”在，这里的人应该不会太为难他们。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]是啊，多亏了你，他们还好。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]但是......情况不太好。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]虽然在场的人有些能够证明那场冲突是郡里的那个年轻人挑起来的，但是没有用，事情已经传开了。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]郡里本来就有不少人对于政府同意在未开发地块上安置矿石病人的决定感到不满。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]这场冲突还是落人口实了，我听到一些风声，有几个贵族已经往市政厅去了，他们要重新讨论该不该收容这批患者的问题。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]......唉。
[charslot(slot="m",name="char_211_adnach_1#5")]
[name="安德切尔"]这次在安排改建期间病人的去向上，原本就有让病人们能够尽量离家乡近一点的意图在。
[charslot(slot="m",name="char_211_adnach_1#5")]
[name="安德切尔"]罗德里是这里土生土长的人，为了治病变卖家产，吃了那么多的苦才在罗德岛安顿下来，他想要回自己过去的家看一看是人之常情。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]谁说不是呢。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]但是，我们也是花费了巨大的功夫，动用了办事处建立以来的所有人脉，才让一些大人物点头，把这批患者安置在未开发地块上。
[charslot(slot="m",name="avg_npc_012")]
[name="精金"]而且，如果这批患者现在要被赶走，那麻烦可就大了。
[charslot(slot="m",name="char_211_adnach_1#5")]
[name="安德切尔"]我知道，在这一带有办事处的三个郡里，阿什福德郡已经是在政策上对感染者比较友好的一个郡了。
[charslot(slot="m",name="char

... (全文24837字符)
```

### story_aglina_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 个人剧情 安洁莉娜
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_291_aglina_1",fadetime=1,block=true)]
[delay(time=1)]
[name="安洁莉娜"]  嗯哼哼~让我看一下，信件，特产包裹，加了高额保险金的邮购物品，全部勾上。
[Character(name="char_291_aglina_1#5")]
[name="安洁莉娜"]  太好啦，今天的工作全部完成！
[Character(name="char_291_aglina_1")]
[name="安洁莉娜"]  做些什么好呢？洗个热水澡，或者先喝一杯奶茶？上次买的柑橘奶油千层还剩一些没有吃完......
[Character(name="char_291_aglina_1#4")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="安洁莉娜"]  等等，安洁莉娜！你忘了答应自己要控制重......呃，注意饮食健康的吗？
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_201_moeshd",fadetime=1,block=true)]
[delay(time=1)]
[name="可颂"]  哟安洁莉娜，你也下班啦？要不要一起看看我新进的货？
[Character(name="char_291_aglina_1",name2="char_201_moeshd",focus=1)]
[name="安洁莉娜"]  好啊......（哈欠）
[name="安洁莉娜"]  诶，忍不住打哈欠了呢，抱歉啊可颂，时间好像不早了。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  我说，这次的货里啊，有你上次提过的龙门老街那家饰品店的定制发夹哦。
[name="可颂"]  我费了老大劲才让老板留了十套，里面一定有你喜欢的。
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  啊，可是......
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd#4",focus=2)]
[name="可颂"]  可是“晚睡会长黑眼圈”，对吧？你天天跟我念叨，我可记住啦。
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd",focus=2)]
[name="可颂"]  算了，我会把东西都留着，等你有空的时候再来找我，可颂亲友专属特别服务哦！
[Character(name="char_291_aglina_1#5",name2="char_201_moeshd",focus=1)]
[name="安洁莉娜"]  嗯嗯~可颂最好啦！
[Character(name="char_291_aglina_1#5",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  哈哈，要不是安洁莉娜借我看了最新的时尚杂志，还帮我划了重点加了注释，我也挑不到这么好的货。
[name="可颂"]  这几次的衣服和饰品都特别受船上的大家欢迎呢！
[name="可颂"]  算下来这个月能赚不少。下周休息日，又可以一起去吃好吃的了。
[name="可颂"]  烤肉还是披萨？或者还是去吃炎式火锅？
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  啊，说出来就觉得肚子和嘴巴一起有反应了......可是......
[Character(name="char_291_aglina_1",name2="char_201_moeshd#4",focus=2)]
[name="可颂"]  可是“最近要控制体重”是吧？
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#4",focus=1)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="安洁莉娜"]  ......是要注意饮食健康。
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  确实。对安洁莉娜来说，根本不存在需要担心体重这回事吧。就这么说出来的话，果然挺让人羡慕的。
[name="可颂"]  要不然下回索性出一期小册子呢？《青春美少女减重小秘诀101条》之类......
[Character(name="char_291_aglina_1#2",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  等等，一定卖不出去的吧？
[Character(name="char_291_aglina_1#2",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  幻想一下还是可以的嘛。或许还是有一些不熟悉你的人上当呢？
[name="可颂"]  比如上回新来那位峯驰的小少爷，他和你打赌比赛举重，哈哈，就让我小赚了一笔钱。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  把欺负新人说的这么理直气壮真的好吗？
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  这叫合理利用信息差。无论是做信使，还是做生意，信息都是关键吧？
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  嗯......也是......虽然心里还是觉得怪怪的。下次见到拜松再请他吃一次小蛋糕好了。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  那我先回去啦！
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[delay(time=0.4)]
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  咦，那是什么？
[Character(name="char_291_aglina_1#2",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  啊，在宿舍门口......是包裹？为什么还有一个包裹在这里？
[name="安洁莉娜"]  明明我今天的件都送完了呀。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  粉红色的包装纸，闻起来也香香的。摸上去方方正正的，好像是本书？
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  会是你订的小说或者杂志吗？
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  杂志的话每个月是固定时间送来的，这个月的都拿到了，应该不会有增刊啊。
[name="安洁莉娜"]  而且最近送信工作和后勤工作都不少，每天时间都安排得满满的，我也并没有时间看新的小说。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  那，是不是有人给你的礼物？
[Character(name="char_291_aglina_1#2",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  礼物？不，不会的，怎么会有人送我礼物？
[Character(name="char_291_aglina_1#2",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  用不着这么惊讶吧，安洁莉娜这么可爱的女孩子，有人送礼物也很正常啊？
[Character(name="char_291_aglina_1#2",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  ......不可能的啦。
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  没写收件人的姓名地址，看样子是和其他物品打包在一起，本来应该同时送达的。
[name="安洁莉娜"]  落在这里的话，大概是早上出去时候太匆忙，不小心从包里掉了出去吧。
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  唉，又失误了啊......
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  别急别急，这种小错误，补送一下就好啦！
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  那现在就出发吧。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  诶，现在吗？明天再送也可以吧？你不是说很晚了吗？
[Character(name="char_291_aglina_1#5",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  我曾经听过一句话，“要改正错误的话，永远只有现在是最合适的时机”。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_snowconutry_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_291_aglina_1",fadetime=1,block=true)]
[delay(time=1)]
[name="安洁莉娜"]  已经跑了好几个地方，暂时没能找到包裹的主人呢。
[name="安洁莉娜"]  这个附属包裹上面本身没有任何信息，只能回头去找白天的收件人一个个确认。
[name="安洁莉娜"]  真是麻烦可颂一起跑这么远。
[Character(name="char_291_aglina_1",name2="char_201_moeshd",focus=2)]
[name="可颂"]  是我自己想陪你的。
[name="可颂"]  再说，夜间锻炼嘛，白天更精神。
[name="可颂"]  倒是你跑得这么快，真的不会累吗？
[Character(name="char_291_aglina_1",name2="char_201_moeshd",focus=1)]
[name="安洁莉娜"]  没事......嗯，其实是有一点。不过想到没有收到包裹的人会多失望多着急，这点累根本不算什么。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  所以嘛，我一直觉得安洁莉娜是很出色的信使。
[Charac

... (全文13103字符)
```

### story_aglina_1_2

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 个人剧情 安洁莉娜
[stopmusic]
[Dialog]
[Delay(time=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_snowconutry_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  这是白天我送出最后一个包裹的地方了。
[Character(name="char_291_aglina_1",name2="char_201_moeshd",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="可颂"]  是快餐店哎！我的最爱！
[name="可颂"]  炸兽肉！薯条！椒盐蘑菇！哇，我全都要！
[Character(name="char_291_aglina_1#2")]
[name="安洁莉娜"]  咦，那个女孩子不在这里。
[Character(name="avg_npc_002")]
[name="快餐店店主"]  炸兽肉要几份？两份？二十份？这么多，小姑娘你一个人真吃得完吗？
[name="快餐店店主"]  好嘞，十份番茄酱，十串撒盐。这些给你——还有你呢，你要什么？
[Character(name="char_291_aglina_1#2")]
[name="安洁莉娜"]  唔......嗯......都好香。
[Character(name="char_291_aglina_1#4")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="安洁莉娜"]  不行，现在还不能吃宵夜。我还有正事还没做完。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(name="char_291_aglina_1")]
[delay(time=0.6)]
[Character(name="char_291_aglina_1",name2="avg_npc_002",focus=1)]
[name="安洁莉娜"]  老板，请问傍晚坐在你店里看书的女孩子，她去了哪里？
[Character(name="char_291_aglina_1",name2="avg_npc_002",focus=2)]
[name="快餐店店主"]  哦，你说她啊。她走啦，应该是想办法回隔壁镇上啦。
[Character(name="char_291_aglina_1#2",name2="avg_npc_002",focus=1)]
[name="安洁莉娜"]  连夜走了？
[Character(name="char_291_aglina_1#2",name2="avg_npc_002",focus=2)]
[name="快餐店店主"]  是啊，连夜。如果再不走，可能就见不到她爸最后一面了吧。
[name="快餐店店主"]  诶小姑娘，你看着面熟，是不是傍晚来过一次？你就是那个给艾米丽送来消息的信使吧？
[Character(name="char_291_aglina_1",name2="avg_npc_002",focus=1)]
[name="安洁莉娜"]  我......是我。不过我并不知道是那样的消息。
[Character(name="char_291_aglina_1",name2="avg_npc_002",focus=2)]
[name="快餐店店主"]  哎，艾米丽一个人在这念书，有空的时候会来我摊上搭把手，挣点零花钱。
[name="快餐店店主"]  她爸爸在老家，平时每个月都会给寄信来，没想到上个月和上上个月信都没到。
[name="快餐店店主"]  艾米丽一直很着急，还专门去找你们信使问，是不是把信漏了。
[Character(name="avg_npc_002",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  老板我们很靠谱的，一般不丢件。
[Character(name="avg_npc_002",name2="char_201_moeshd#2",focus=1)]
[name="快餐店店主"]  好好好，我信你们，艾米丽也不是不相信。但等不到家里的消息，心里总是很不安啊。
[Character(name="char_291_aglina_1",name2="avg_npc_002",focus=1)]
[name="安洁莉娜"]  难怪她傍晚看到我的时候，特别高兴。
[Character(name="char_291_aglina_1#4",name2="avg_npc_002",focus=1)]
[name="安洁莉娜"]  只可惜......
[Character(name="char_291_aglina_1#4",name2="avg_npc_002",focus=2)]
[name="快餐店店主"]  欸，那句话怎么说的？天有什么风云？反正啊，是人就总会有生老病死。
[name="快餐店店主"]  再说了，要不是你送来了她爸爸这最后一封信，她也不会知道自己得赶紧回家了。
[Character(name="avg_npc_006",name2="char_291_aglina_1#4",focus=1)]
[name="快餐店店主"]  艾米丽她打心眼里是想谢谢你的吧。
[name="快餐店店主"]  对了，你们来找她是有什么事？
[Character(name="avg_npc_006",name2="char_291_aglina_1",focus=2)]
[name="安洁莉娜"]  这个......现在没事了。
[name="安洁莉娜"]  我想这东西不会是她的。
[Character(name="avg_npc_006",name2="char_291_aglina_1",focus=1)]
[name="快餐店店主"]  好嘞，没事的话，吃的尽管点，我给你们打八折！
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_corridor",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Character(name="char_201_moeshd",fadetime=1,block=true)]
[delay(time=1)]
[name="可颂"]  嗝——
[Character(name="char_201_moeshd#4")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="可颂"]  不知不觉就吃了好多东西，完蛋，这个月钱又花光了！
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  天都快亮了啊。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  可不是，跑了一夜！肚子确实饿了。咦，你可是一点东西都没吃啊！
[name="可颂"]  是不是还想着艾米丽的事？
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  是......
[name="安洁莉娜"]  或许不完全是。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  只是听说她的事情之后，我忍不住在想，会不会也有人一直在等我的消息。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  对哦，安洁莉娜很久没回家了吧？
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  ......如果路过也算的话，倒也不算太久。
[Character(name="char_291_aglina_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  哎，你想好什么时候回去了吗？或者至少联系一下爸爸妈妈啊。
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  我不知道......
[name="安洁莉娜"]  我不知道有没有做好准备。
[Character(name="char_291_aglina_1#4",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  什么准备呀？现在安洁莉娜的病情不是挺稳定的么？当初你说不忍心关心你的人眼睁睁看着你痛苦，宁可让他们以为你失踪......
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  ......以为我是失踪的话，哪怕过去五年、十年，也依然会有我还在某个地方好好活着的希望吧。
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  可心里一定还是很担心啊！
[name="可颂"]  而且有医疗部门的大家在，别说五年十年，未来一定是光明的！
[Character(name="char_291_aglina_1#3",name2="char_201_moeshd#2",focus=1)]
[name="安洁莉娜"]  我......
[Character(name="char_201_moeshd#2")]
[name="可颂"]  咦，那是谁？
[name="可颂"]  我好像看到了一条......不对，一、二、三......好多条毛茸茸的尾巴。
[Dialog]
[Character(name="char_358_lisa_1",fadetime=1,block=true)]
[delay(time=1)]
[name="铃兰"]  啊，安洁莉娜姐姐，可颂姐姐，早、早上好。
[Character(name="char_291_aglina_1#2",name2="char_358_lisa_1",focus=1)]
[name="安洁莉娜"]  是小丽萨啊，早上好。欸，现在时间还很早，还没到丽萨的起床时间吧？
[Character(name="char_291_aglina_1#2",name2="char_358_lisa_1",focus=2)]
[name="铃兰"]  可是......可是我想来看看那样东西......
[Character(name="char_291_aglina_1",name2="char_358_lisa_1",focus=1)]
[name="安洁莉娜"]  什么东西？
[Character(name="char_291_aglina_1",name2="char_358_lisa_1",focus=2)]
[name="铃兰"]  就是，就是那个笔记......
[Character(name="char_291_aglina_1",name2="char_358_lisa_1#3",focus=2)]
[name="铃兰"]  我昨天做完了，就想赶紧拿来给安洁莉娜姐姐看，后来太晚了，我，我不敢让凯尔希医生发现我没有按时睡觉......
[Character(name="char_291_aglina_1",name2="char_358_lisa_1",focus=2)]
[name="铃兰"]  但实在很想让安洁莉娜姐姐马上看到啊！
[Character(name="char_358_lisa_1",name2="char_201_moeshd#2",focus=2)]
[name="可颂"]  所以你就把东西放在了宿舍门口

... (全文13170字符)
```

### story_agoat2_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_wilderness_d",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[name="阿黛尔"]八月二十四日。预警花培育箱内温度：正常；湿度：正常；土壤各项成分数值：正常；分区源石活性：尚未启动活性控制。
[name="阿黛尔"]今天来到了乌纳火山附近的乌纳村，找到新址花费了我不少时间，他们在原址向北好几公里外的地方重新搭建了房屋并住下。
[name="阿黛尔"]在如今的乌纳村里，不论向何处眺望，我都无法看到乌纳火山。只有登上最高处的屋顶，才能望见极远处旧乌纳村的废墟。
[name="阿黛尔"]山路又远又崎岖，还好这次考察我申请了载具，培育箱没有受损，里面预警花花苗的状态也很好，可以立刻开始实验。
[name="阿黛尔"]只是不知道为什么......村民们的态度很是奇怪。
[name="阿黛尔"]在我刚走进村子时，他们以为我是迷路的旅人，十分热情。
[name="阿黛尔"]但在我介绍自己是来做火山考察的之后，他们立刻冷下脸来，再不愿意和我多说一句话。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement", volume=1)]
[Delay(time=1)]
阿黛尔放下手中的笔，放眼望去。比起几年前的报道中村庄被火山灰覆盖的景象，新的乌纳村早已恢复了生机。
居民来来往往，有人拨弄着手中的乐器，房屋中传来阵阵乐声，几个快乐的孩童在阳光下奔跑，用充满好奇的目光望向阿黛尔。
极远处乌纳火山山脚下却有一抹灰黑，似乎是一片毫无生机的废墟，明明很暗，却又很显眼，紧紧地贴在原地。
阿黛尔四处张望，目光最终停留在那里。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_penrustle",volume=1,channel="wr",loop=false)]
[name="阿黛尔"]好在，在一个好心小朋友的帮助下，我终于找到了村长，她愿意把空置的阁楼提供给我暂住......
[Dialog]
[stopsound(channel="wr",fadetime=1)]
[Delay(time=1)]
[Dialog]
[charslot(slot = "m", name = "avg_npc_497_1#1$1", duration=1)]
[Delay(time=1.5)]
[charslot(slot = "m", name = "avg_npc_497_1#1$1",focus="m")]
[name="村长"]打扰了，阿黛尔小姐。作为屋主，我给你泡了些热茶，这些是你的晚餐。
[name="村长"]以及作为村长，我也得向你解释一下之前村民们对你态度冷淡的这件事。
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_1016_agoat2_1#1$2", duration=0.7)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_1016_agoat2_1#1$2",focus="m")]
[name="阿黛尔"]多谢您的饭菜和茶水。
[charslot(slot = "m", name = "avg_npc_497_1#1$1",focus="m")]
[name="村长"]我就直接说了，我们并不喜欢提到任何有关那边那座火山的事情，我们不想再看到它，最好是连“火山”这个词也不要说出口。
[name="村长"]那场灾害让太多人离开了我们，没有人能轻易地再提起它。你还是尽快做完你的事，尽快离开吧，今天有不少村民来找我说这件事了。
[charslot(slot = "m", name = "avg_1016_agoat2_1#9$2",focus="m")]
[name="阿黛尔"]......
[charslot(slot = "m", name = "avg_1016_agoat2_1#11$2",focus="m")]
[name="阿黛尔"]我还是会按照原计划做完我要做的事情，然后再离开的。
[name="阿黛尔"]村长，我现在在做的事情与火山灾害预警相关，我并不觉得这会是冒犯到村民们、让他们对我态度恶劣的原因。
[charslot(slot = "m", name = "avg_npc_497_1#1$1",focus="m")]
[name="村长"]......年轻人，我能明白你想说什么。
[name="村长"]......可我们也有我们自己面对火山的方式，我们也需要时间。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_caveentrance", screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[name="阿黛尔"]九月三日。预警花培育箱内温度：正常；湿度：正常；土壤各项成分数值：正常；分区源石活性：尚未启动活性控制。
[name="阿黛尔"]我在火山上的几处地点采集了土壤样本，找到了一处合适的预警花育苗地点。预警花的存活率很喜人，它们在乌纳火山适应得很好。
[name="阿黛尔"]大约半个月后是它们的花期，要是能够从它们的颜色变化中探寻到与源石活性相关的生物状态，或许防范火山灾害会有新的可能。
[name="阿黛尔"]那样的话，就能避免更多人遭受火山所带来的危害。
[name="阿黛尔"]每日来往山坡花田和住所的路线我也已经熟悉，只要能赶在日落前下山，我就能一个人顺利回到住处。
[name="阿黛尔"]看来需要设置一个最晚工作时间呢，否则天黑之后我就完全看不清山路了。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[name="阿黛尔"]......只是村民们似乎还是很排斥我，很难和他们沟通交流。我并不想评判他们的处理方式，只是......这样一味地逃避，真的好吗......？
[name="阿黛尔"]对了，是时候给这片试验田围上围栏了，下午要记得找一些做围栏的材料。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_caveentrance", screenadapt="coverall", block=true)]
[charslot(slot = "m", name = "avg_1016_agoat2_1#9$2",focus="m")]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=0.5)]
[charslot(slot = "m", name = "avg_1016_agoat2_1#9$2",focus="m")]
[name="阿黛尔"]唔，花苞已经长出来了不少，再过几天就都能开花了......
[name="阿黛尔"]从今天开始缩短记录源石活性的间隔，做出分区开始控制每个实验区的源石活性吧。
[name="阿黛尔"]从这边开始做标记......
[Dialog]
[charslot]
[stopmusic(fadetime=1)]
[name="？？？"]呃啊啊啊——呜哇！
[Dialog]
[PlaySound(key="$bodyfalldown2", volume=1)]
[CameraShake(duration=1,xstrength=50,ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1.5)]
[name="？？？"]好痛！！这里怎么突然有一个围栏挡我！
[charslot(slot = "m", name = "avg_1016_agoat2_1#4$2",focus="m")]
[name="阿黛尔"]......！
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_661_1#1$1", duration=1)]
[Delay(time=1.5)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[charslot(slot = "m", name = "avg_npc_661_1#1$1",focus="m")]
[name="好奇的孩子"]啊，你是那天说要上火山的姐姐......你果然在这里！
[charslot(slot = "m", name = "avg_1016_agoat2_1#4$2",focus="m")]
[name="阿黛尔"]你是那天给我指路的孩子......？有没有受伤？你怎么一个人跑到火山上来了？这里对你来说可不是能乱跑的地方啊！
[charslot(slot = "m", name = "avg_npc_661_1#1$1",focus="m")]
[name="好奇的孩子"]我没事......
[name="好奇的孩子"]哼，爸爸妈妈不让我上火山，也不让我去老村子那边的废墟，我就偏要来！
[name="好奇的孩子"]不就是火山吗？有什么大不了的，我自己一个人也能爬上去......哎哟！
[charslot(slot = "m", name = "avg_1016_agoat2_1#2$2",focus="m")]
[name="阿黛尔"]还是摔到腿了吧......你坐下来，我来给你涂一点药。
[charslot(slot = "m", name = "avg_npc_661_1#1$1",focus="m")]
[name="好奇的孩子"]这点小伤口没事的，姐姐，我就知道你在这里！
[name="好奇的孩子"]你能告诉我，怎么才能爬到火山的山顶上去吗？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_caveentrance", screenadapt="coverall", block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[name="阿黛尔"]九月二十三日。昨天工作结束得迟了一点，又赶上下雨，试着冒雨下山，果然还是摔了一跤。还好被村民们发现，把我送回了住处。
[name="阿黛尔"]他们问我怎么天气这么差还上山，我和他们说了研究火山灾害预警的事情。他们似乎没那么排斥我了，还给了我当地的药膏，很好用。
[Dialog]
[Delay(time=1)]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[name="阿黛尔"]记回工作。源石活性对预警花的颜色有着很明显的影响，基本上源石活性每提升一级，预警花的颜色差别都能够直接用肉眼观察到。
[name="阿黛尔"]这段时间已经提取了足够多的植物样本成分进行分组实验，希望能够找到究竟是植株中的什么物质造成了这一现象。
[name="阿黛尔"]如果能尽快发现，或许能够早日找到应用这种物质来提升火山预警灵敏度和精度的新方向，准确预警火山灾害的那一天或许将不再遥远。
[name="阿黛尔"]以及，我在这里又遇到了那个给我指路的小朋友。从那天她摔倒在花田里，我给她涂了点药之后，她几乎天天都来找我。
[name="阿黛尔"]她总是不听父母的话跑上火山，或是到火山山脚的废墟去，还想让我带她登上乌纳火山的山顶......似乎对火山很感兴趣呢。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Background(image="bg_caveentrance", screenadapt="coverall", block=true)]
[charslot(slot = "l", nam

... (全文32487字符)
```

### story_akafyu_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=2)]
[Background(image="bg_indoor_2",screenadapt="coverall")]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.6)]
大人，这次作战失利责任全在我指挥失当，未能识破敌人奸计，所有罪责由属下一人承担！
属下深知自己罪不容诛，我一人死不足惜，但属下只求一个最后报答大人的机会，我定能——
[dialog]
[Subtitle(text="定能如何？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="若我今日判你身死，或是让你死于战场，是能挽回战败对局势的影响，还是能让那些因你而死的战士复生？你又如何担得起责？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="你究竟，将战争当作何物？", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
大人！我——
[dialog]
[Subtitle(text="赤冬，你没有资格留在这里。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="离开东国。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[stopmusic(fadetime=3)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=1)]
[playMusic(intro="$sjoyasorrow_intro", key="$sjoyasorrow_loop", volume=0.6)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=20, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_spear",volume=0.7)]
[Delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_singleblunt")]
[Delay(time=1.5)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_avg_spear",volume=1)]
[Delay(time=1)]
[name="赤冬"]九百九十八......九百九十九......一千......
[name="赤冬"]呼......
剑士收起长剑，深深吐纳。抽出随身小刀在墙上的计数符号上又刻下一划。
被驱逐出东国的第一百三十七天，停留在这座名为龙门的陌生城市的第三十九天。
离开东国之前，收到了一家名为“罗德岛”的公司的邀请，他们说自己依然有可以作为剑士而战的机会——大抵也是主上的默许。
如今自己要做的就是在这里耐心等待，等待对方接头人带自己去新的安身地点——某个远离东国的地方。
前路未卜。
[dialog]
[charslot(slot="m",name="avg_475_akafyu_1#1$1",duration=1)]
[delay(time=2)]
[name="赤冬"]锻炼从未懈怠，可刀油已经用完了。
[name="赤冬"]如何是好......
[charslot]
人们常说，落单的剑士脆弱如羽兽。曾经握在手中的剑越是锋锐，便越是易折。
离开东国前遇到过数次几乎致命的麻烦，之后的路虽相对安稳，可也不清楚是否还有敌人跟随自己来到此处，万万不能掉以轻心。
按照约定，每十天会有人按时将必需的生活物资留在门口，自己不该随意离开这间屋子。
[dialog]
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[PlaySound(key="$d_avg_open_box",volume=1)]
[PlaySound(key="$d_avg_wind",volume=1,delay=0.5)]
[delay(time=1)]
[name="赤冬"]今天似乎也没有异样......
[charslot]
暂住的居所地处城市外围的一条老旧小巷中，丝毫不引人注目，应该还算安全。
偶有形形色色的路人路过，还有每日都会按时出摊的早餐店主，没有发现可疑的人。
从窗户可以看到这座陌生城市一隅。龙门的模样和家乡大不相同，与传闻中南朝治下的光怪陆离的城市倒有几分相似。
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[name="赤冬"]食物都已经消耗尽了，今天本该是补充物资的时间。
[name="赤冬"]不知周围是否还有追兵潜藏，贸然出行恐怕还是有危险......
[name="赤冬"]啧......何等令人烦躁，堂堂剑士岂有避战畏敌的道理！光严家的剑士何曾有过这般屈辱！
[name="赤冬"]适应环境，是必要的修行......
[Dialog]
[PlaySound(key="$d_avg_hungry",volume=1)]
[delay(time=1.5)]
[name="赤冬"]按时进食也是......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_lungmen_b", screenadapt="coverall", block=true)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
深巷。
剑士谨慎地踏出一步，月余来第一次走出房间，第一次从低处观察这片空间。
小巷两侧低矮的房屋紧紧挤挨着，露出狭窄的一方天空，剑士恍惚想起神社低矮的屋檐。
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[name="赤冬"]看上去是老旧的民居，并无特殊之处。建筑上悬挂的杂物众多，也无合适的狙击位。
[name="赤冬"]进出都只有一个口，就算有跟踪者，应该很难隐藏踪迹。可若遇到伏兵堵截，敌众我寡时，脱身同样麻烦。
[name="赤冬"]此地不宜久——
[dialog]
[charslot(slot = "m", focus = "n")]
[PlaySound(key="$d_avg_firemagic",volume=0.7)]
[Delay(time=1)]
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="赤冬"]——！
[dialog]
[MusicVolume(volume=0.2, fadetime=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[PlaySound(key="$d_sp_ballista",volume=0.7)]
[PlaySound(key="$d_gen_explo_n",volume=0.5,delay=1.5)]
[name="惊慌的声音"]队长！当心弩炮！
[PlaySound(key="$d_gen_explo_n",volume=0.5)]
[name="惊慌的声音"]我们已经中了埋伏，敌人数量太多，继续苦战也是不会有结果的......
[name="赤冬"]振作起来，我们一起杀出去！
[PlaySound(key="$d_gen_explo_n",volume=0.5,delay=1.5)]
[name="惊慌的声音"]请您先撤退吧！我们会给您断后的！
[dialog]
[Delay(time=1)]
[MusicVolume(volume=0.6, fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
再睁开眼，身旁空无一人。
[PlaySound(key="$d_avg_smithy",volume=0.6)]
阳光灿烂，和那个雪天所见的阳光别无二致，涌入鼻腔的却是临街店铺传来的油烟味。
[dialog]
[PlaySound(key="$d_gen_walk_n",volume=0.7)]
[charslot(slot="m",name="avg_npc_032",duration=1)]
[Delay(time=2)]
[name="路过的食客"]老板，今天怎么大清早就开始做炒菜啊？
[charslot(slot="m",name="avg_npc_005")]
[name="早餐店老板"]偶尔试试换个花样，最近年轻人起床越来越晚，早午饭都合一顿了，我也得跟着适应不是？
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[name="赤冬"]冷静些......不能因为过去的失败失态......冷静些。
[charslot(slot="m",name="avg_npc_005")]
[name="早餐店老板"]那位姑娘，还没吃饭吧，吃点什么东西？
[name="早餐店老板"]再怎么匆忙，还是要好好吃饭呀。
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[name="赤冬"]（常见的街边饭店。店主人和客人都是普通人，感受不到危险的气息。）
[name="赤冬"]（或许可以用这里的食物充饥。）
[name="赤冬"]这里，都提供什么食物？
[charslot(slot="m",name="avg_npc_005")]
[name="早餐店老板"]豆浆油条，包子炒面，什么都有。这儿的客人都说我们家的肠粉是一绝，您要不要尝尝？
[charslot(slot="m",name="avg_475_akafyu_1#1$1")]
[name="赤冬"]我......
[name="赤冬"]（面皮包裹着看不清的馅料，还有来路不明的酱汁，这香味的确是容易让人精神动摇......）
[name="赤冬"]（不......不妥，还是得寻找更为安全的食物才行。）
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot = "m",posfrom = "0,0", posto = "300,0",duration = 1)]
[charslot(duration=1)]
[delay(time=2.5)]
[charslot]
[charslot(slot="m",name="avg_npc_032")]
[name="路过的食客"]刚才那个人怎么回事，看上去像是没有带钱？
[charslot(slot="m",name="avg_npc_005")]
[name="早餐店老板"]有些面生，好像不是住这附近的人吧。
[name="早餐店老板"]那姑娘看上去面黄肌瘦的，怕是有阵子都没好好吃饭了。唉，要是口袋里紧张的话，请她一顿也不要紧的呀。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_lungmen_m", screenadapt="coverall", block=true)]
[Delay(time=1)]
[playMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_horn", volume=1)]
码头。
城市的重要出入口，人流量最为庞大的地方之一。如果与自己接头的人来自更远的地方，他有可能会出现在这里。
剑士站在高处凝神眺望，稍远处，大型舰船吞吐着数量庞大的货物和人群，稍作停顿又匆忙驶向远方。
其中是不是也有一条船，可以直接驶向东国......
[c

... (全文14712字符)
```

### story_alanna_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_20_G08",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Delay(time=2)]
[dialog]
[playsound(key="$d_avg_bwlngrlng")]
[delay(time=4)]
[charslot(slot="m",name="avg_npc_006")]
[name="叼牙签的工人"]几比几来着？
[charslot(slot="m",name="avg_npc_005")]
[name="流汗的工人"]你已经超了我十分了。要不......这球免了？
[charslot(slot="m",name="avg_npc_006")]
[name="叼牙签的工人"]免什么免，看我给你再来个帅的——背身盲抛一发全倒！
[dialog]
[charslot]
[Dialog]
[Character]
[Blocker(a=1, r=1, g=1, b=1, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0, fadetime=1.5, block=false)]
[PlaySound(key="$char_emp", volume=0.9)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[name="？？？"]大板牙——大板牙！嗓子冒烟了！
[dialog]
[charslot(slot="l",name="avg_4178_alanna_1#1$1",duration=1.5)]
[charslot(slot="r",name="avg_4081_warmy_1#3$2",duration=1.5)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_4178_alanna_1#7$1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="阿兰娜"]快给我倒一大杯啤酒！
[charslot(slot="m",name="avg_4081_warmy_1#3$2")]
[name="温米"]兰娜姐......
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[name="阿兰娜"]哦对，还要一瓶胡萝卜汽水！
[charslot(slot="m",name="avg_npc_006")]
[name="叼牙签的工人"]阿兰......阿兰娜？！
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[multiline(name="阿兰娜")]喂喂，大板牙你牙签掉地上了——
[charslot(slot="m",name="avg_4178_alanna_1#5$1")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="阿兰娜")]别放回嘴里啊，真恶心！
[charslot(slot="m",name="avg_npc_005")]
[name="流汗的工人"]好、好像真的是她！
[charslot(slot="m",name="avg_4178_alanna_1#8$1")]
[name="阿兰娜"]你们这一副见了鬼的表情是怎么回事？
[dialog]
[charslot]
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]真是好久不见。距离你上次踹坏这扇门，已经有一年多了。
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[name="阿兰娜"]真有那么久吗？把吧台上那杯啤酒给我，我快渴死了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[Delay(time=1)]
[PlaySound(key="$d_avg_drinkswllw")]
[PlaySound(key="$d_avg_drinkswllw",loop=false,channel="d1",delay=1)]
[PlaySound(key="$d_avg_drinkswllw",loop=false,channel="d2",delay=1.6)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[name="阿兰娜"]哈——
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]你刚才说，你这次回来，是因为一张罚单？
[charslot(slot="m",name="avg_4178_alanna_1#4$1")]
[name="阿兰娜"]对，我在罗德岛加班的时候，突然收到一张电子罚单，落款是雷姆必拓比格皮勒自治州住宅管理委员会。
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]住宅管理委员会？什么时候冒出来这个......没事，你继续说。
[charslot(slot="m",name="avg_4178_alanna_1#4$1")]
[name="阿兰娜"]罚单上说，我名下有一处住宅被认定为“违规建筑”，如果不在规定时间内缴纳罚金的话，就会被拆掉！
[charslot]
[charslot(slot="m",name="avg_npc_002")]
[charslot(slot="l",name="avg_npc_005")]
[charslot(slot="r",name="avg_npc_006")]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="异口同声的工人们"]什么？
[charslot]
[charslot(slot="m",name="avg_4178_alanna_1#8$1")]
[name="阿兰娜"]很意外，对吧？我以为我老家那栋房子早就没了，没想到居然还在！
[charslot(slot="m",name="avg_npc_005")]
[name="流汗的工人"]不对，阿兰娜。我们的确很惊讶，但最让我们感到意外的是......
[charslot(slot="m",name="avg_npc_006")]
[name="叼牙签的工人"]你这个吃住都在运载车上，站在平地上反而会晕，打赌自己除了上厕所可以一年不下车的家伙......
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]......居然有一栋房子？什么时候？
[charslot(slot="m",name="avg_4178_alanna_1#3$1")]
[name="阿兰娜"]那是我爸妈的房子——好吧，我继承过来了，所以也算是我的。但我一直以为它早就塌了！就算没塌，天灾过后也住不了人呀。
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]但你现在却收到了那张罚单......
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[name="阿兰娜"]所以我就火急火燎赶回来了，万一是当初组织撤离的人搞错了呢？万一天灾压根儿没来呢？
[charslot(slot="m",name="avg_npc_006")]
[name="叼牙签的工人"]既然真是这么要紧的事情，为什么你第一个来的地方是这里？
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[name="阿兰娜"]难得你脑子开窍一回，大板牙。你想想，这么多年了，先不说我还找不找得到那个地方，起码我得有辆车吧？
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]我听明白了，阿兰娜，你想要的恐怕不只是一辆车。最好再给你配一个司机是不是？
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[name="阿兰娜"]那肯定，我可从不干疲劳驾驶的事——听起来，你还算感兴趣？
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]一直把自由漂泊，来去如风挂在嘴上的“荒野上的阿兰娜”，居然也有自己的秘密老巢？我当然感兴趣！
[charslot(slot="m",name="avg_4178_alanna_1#1$1")]
[multiline(name="阿兰娜")]那就这么说定了！事不宜迟，咱们现在就出发——
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="阿兰娜")]小锅盖！
[charslot(slot="m",name="avg_4081_warmy_1#6$2")]
[name="温米"]怎么啦？
[charslot(slot="m",name="avg_4178_alanna_1#9$1")]
[name="阿兰娜"]让大板牙给你拿几瓶胡萝卜汽水路上喝。不用付钱，他欠我的。记得要冰镇的！
[charslot(slot="m",name="avg_npc_006")]
[name="叼牙签的工人"]嘿嘿，多拿几瓶吧。没事的，小家伙。祝你健康。
[charslot(slot="m",name="avg_4081_warmy_1#11$2")]
[name="温米"]谢、谢谢你......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[PlaySound(key="$d_avg_truckengine", volume=0.8, loop=true, channel="bg")]
[delay(time=4)]
[StopSound(fadetime=2,channel="bg")]
[delay(time=1)]
[Background(image="46_g2_rmbttransporter",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]这张地图上也找不到吗？
[charslot(slot="m",name="avg_4178_alanna_1#5$1")]
[name="阿兰娜"]也许是地图太新了......唉！怎么才过去十几年，那么大一座镇子就直接从地图上消失了？
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]一直在大路上绕圈子也不是个办法。除了遭遇过天灾之外，那个镇子还有别的特点吗？
[charslot(slot="m",name="avg_4178_alanna_1#4$1")]
[name="阿兰娜"]我想想，镇子旁边有个矿场，镇子上住着的都是矿场的职工。
[charslot(slot="m",name="avg_npc_002")]
[name="小查理"]......雷姆必拓百分之九十九的镇子都这样。
[charslot(slot="m",name="avg_4081_warmy_1#10$2")]
[name="温米"]兰娜姐的爸爸妈妈，也是矿工吗？
[charslot(slot="m",name="avg_4178_alanna_1#4$1")]
[name="阿兰娜"]不算吧，他们只是在矿场工作，

... (全文27527字符)
```

### story_almond_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="42_g10_blacksteelarmory",screenadapt="showall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[playMusic(key="$normal_loop", volume=0.6)]
[delay(time=2)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "l", name = "avg_4105_almond_1#2$1",duration=1.5)]
[charslot(slot = "r", name = "avg_npc_524_1#1$1",duration=1.5)]
[Delay(time=2.5)]
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]罗拉？你对巴伦基地应该没有那么陌生吧？
[charslot(slot = "l", name = "avg_4105_almond_1#7$1",focus="l")]
[name="罗拉"]啊......抱歉，我有点出神......
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]看你直直地盯着桌上的模型，我还以为它出了什么问题呢。
[name="黑钢文员"]听前辈们说，这个模型可是巴伦基地改造完成、交付使用时，工程队专门制作的纪念品......
[name="黑钢文员"]它真的没问题吧？
[charslot(slot = "l", name = "avg_4105_almond_1#11$1",focus="l")]
[name="罗拉"]没有。它看上去......就和现在的基地一模一样。
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]你这么说我就放心了。那我们继续？
[charslot(slot = "l", name = "avg_4105_almond_1#11$1",focus="l")]
[name="罗拉"]好哦。
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]准备好了哦，等我看下你的报告......咳咳......
[name="黑钢文员"]罗拉，收到追捕银行劫匪的命令后，你采取了什么行动？
[charslot(slot = "l", name = "avg_4105_almond_1#10$1",focus="l")]
[name="罗拉"]那时候我正带领工程小队再次确认地块连接结构的稳固性，收到消息后......
[charslot(slot = "l", name = "avg_4105_almond_1#2$1",focus="l")]
[name="罗拉"]......我选择继续手头的工作。
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]陈述你如此行动的理由。
[charslot(slot = "l", name = "avg_4105_almond_1#10$1",focus="l")]
[name="罗拉"]我接收到的命令是，除了参与地块对接工作的人员外，其他小队开始追捕银行劫匪。
[name="罗拉"]我判断地块对接工作仍需要人手，而我们工程小队本就需要加入其中，属于相关人员。
[name="罗拉"]我选择听从指令，不改变原先的接驳工作。
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]但根据报告上的内容，在实施银行劫案的劫匪中，有一位是你在达维镇的同伴。你当时清楚这一消息吗？
[charslot(slot = "l", name = "avg_4105_almond_1#2$1",focus="l")]
[name="罗拉"]我......我知道。
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]关于这一消息，你当时的判断是怎样的？
[charslot(slot = "l", name = "avg_4105_almond_1#9$1",focus="l")]
[name="罗拉"]判断......我的判断？
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]“我不会重复第二遍。”
[charslot(slot = "l", name = "avg_4105_almond_1#9$1",focus="l")]
[name="罗拉"]我的判断......我没做什么判断......
[charslot(slot = "l", name = "avg_4105_almond_1#10$1",focus="l")]
[name="罗拉"]......我是黑钢的雇员，奉命行事是......
[name="罗拉"]我的职责。
[Dialog]
[charslot]
[Delay(time=0.2)]
[charslot(slot = "m", name = "avg_npc_1045_1#1$1",focus="m")]
[name="黑钢佣兵"]（皱眉）......
[Dialog]
[playsound(key="$d_avg_penrustle",channel="1")]
[Delay(time=2)]
[stopsound(channel="1")]
[charslot]
[Delay(time=0.2)]
[charslot(slot = "l", name = "avg_4105_almond_1#10$1",focus="r")]
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]“奉命行事，罗拉，你做出了正确的决定。”
[name="黑钢文员"]怎么样？罗拉，我学得还挺像那么回事的吧？
[name="黑钢文员"]还有刚刚那句，“我不会重复第二遍”，简直一模一样是不是？
[charslot(slot = "l", name = "avg_4105_almond_1#10$1",focus="l")]
[name="罗拉"]......
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]欸......罗拉，怎么了？你的脸色好像不太好。不会是......我给你的压迫感太强了吧？
[charslot(slot = "l", name = "avg_4105_almond_1#10$1",focus="l")]
[name="罗拉"]没事的......我只是......
[name="罗拉"]拜托，我们继续吧。
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]刚刚......那就是最后一个问题。
[name="黑钢文员"]罗拉，我必须得告诉你，从达维镇回来以后，你就一直表现得有些心神不宁。
[name="黑钢文员"]我们都知道，那是一场非常特殊的行动，而那时候你恰好就处在漩涡的中心。
[name="黑钢文员"]我真的难以想象你经历了什么，但即便如此，你也不能一直这么紧绷着。
[name="黑钢文员"]罗拉，现在的你需要的是休息。
[charslot(slot = "l", name = "avg_4105_almond_1#2$1",focus="l")]
[name="罗拉"]休息......
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]而且是好好休息。别再想行动报告的事了，你应该申请一个长假。
[charslot(slot = "l", name = "avg_4105_almond_1#2$1",focus="l")]
[name="罗拉"]你说得对......我不能再这么消沉下去了。
[name="罗拉"]阿莉莎，陪我再来一遍，好吗？
[charslot(slot = "r", name = "avg_npc_524_1#1$1",focus="r")]
[name="黑钢文员"]罗拉......你根本就没有听我说话......
[Dialog]
[charslot]
[charslot(slot = "m", name = "avg_npc_1045_1#1$1",focus="m")]
[name="黑钢佣兵"]要我说，罗拉，你最好别去做这个行动报告了。
[name="黑钢佣兵"]已经过去两周了，没人会再说起那件事了。
[name="黑钢佣兵"]这不过是公司历程中的一个小插曲而已，你做得再认真，主管肯定也只是装模作样地听一听。
[name="黑钢佣兵"]这位小姐说得很对，你还不如找主管去批个长假。
[charslot(slot = "m", name = "avg_4105_almond_1#10$1",focus="m")]
[name="罗拉"]不......我得去做这次报告。
[name="罗拉"]我从一开始就到了达维镇，很多事情是我亲眼所见，亲身经历。
[name="罗拉"]在行动中执行命令，行动后做好行动报告，这都是黑钢雇员的职责所在，更何况......
[charslot(slot = "m", name = "avg_4105_almond_1#9$1",focus="m")]
[name="罗拉"]阿莉莎，你看到我在报告上写的东西了吧？那些事情难道不应该被整理汇报上去吗？
[charslot(slot = "m", name = "avg_npc_524_1#1$1",focus="m")]
[name="黑钢文员"]罗拉，我......
[charslot(slot = "m", name = "avg_npc_1045_1#1$1",focus="m")]
[name="黑钢佣兵"]不需要报告，达维镇发生的事情已经再清晰不过。
[name="黑钢佣兵"]在完成政府委托任务的过程中，有一位黑钢员工违规参与了犯罪活动，严重影响了公司的形象与声誉。
[name="黑钢佣兵"]罗拉，我们都清楚，这不是一件值得反复提及的事情，尤其是在......两周之后。
[name="黑钢佣兵"]我们靠工资吃饭，只用奉命行事，保住自己的饭碗就够了。
[name="黑钢佣兵"]没必要让自己那么烦恼。
[charslot(slot = "m", name = "avg_4105_almond_1#10$1",focus="m")]
[name="罗拉"]......
[name="罗拉"]我、我还是要找人问清楚。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="bg_black",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Subtitle(text="......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="痛......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[name="母亲"]哪里痛？
[Dialog]
[Subtitle(text="屁股......痛。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[name="母亲"]屁股痛没事，长教训。
[name="母亲"]你知道错了吗？
[Dialog]
[Subtitle(text="我知道了，妈妈，我不该在床底下折腾......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="可是......妈妈，我真的喜欢那些机械零件。我知道你不喜欢我碰这些东西，所以我只能......", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[name="母亲"]看起来你不知道自己错在哪里了。
[name="母亲"]吃完饭，跟我来。
[Dialog]
[Blocker(a=0, r=0, g

... (全文19249字符)
```

### story_amgoat_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_laccolith",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_180_amgoat",fadetime=1,block=true)]
[delay(time=1)]
[name="艾雅法拉"]  ......可以开始了吗？录音键好像闪了一下，不知道是不是错觉......嗯......摸起来慢慢变热了......大概在工作了？
[name="艾雅法拉"]  咳咳，那个......今天是外勤的第三天，我们成功抵达了目标地块附近。
[name="艾雅法拉"]  现在是上午十点三十......呃，这个数字是一吗？抱歉，我看不太清......
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=70, fadeout=true, block=false)]
[name="艾雅法拉"]  ......变、变成二了！现在是十点三十二分，距离罗德岛抵达汇合点还有......嗯，还有十二小时二十八分钟。
[name="艾雅法拉"]  到目前为止都很顺利，检测符文在来的路上已经准备好啦，采样设备的话，大家正在帮我安装。
[name="艾雅法拉"]  ......欸，什么？似乎听见有人叫我......
[delay(time=0.4)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=70, fadeout=true, block=false)]
[name="艾雅法拉"]  啊啊，录音器差点掉地上。呼......呼，不能着急。
[name="艾雅法拉"]  ......是在对我挥手？看这个手势的意思，是都安装好了吗？数据采集开始......同步分析启动......好，好的！
[Dialog]
[Character(name="avg_npc_012",fadetime=1,block=true)]
[delay(time=1)]
[name="外勤干员"]  艾雅法拉小姐！
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  啊，是......是巴蒂先生吧？助听器......好的，助听器没问题。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="巴蒂"]  哎呀，别着急！走慢些，小心脚下。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  没、没关系的......巴蒂先生，您可以不用扶着我。这里视野很开阔呢，也不用担心我不小心撞到东西。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="巴蒂"]  这样吗？但是风很大，而且到处都是凹凸不平的石块，艾雅法拉小姐的话，还是留在飞行器那边比较好吧？
[name="巴蒂"]  毕竟出来的时候，我可是拿下个月的薪水向凯尔希医生他们保证了哦，一定会确保你的安全。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  呃......
[name="艾雅法拉"]  ......沙拉？和......凯尔希医生一起？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  啊？是说薪水啦，薪水！
[name="干员巴蒂"]  （小声）我可不敢和凯尔希医生一起吃沙拉。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  啊，是、是这样吗......
[name="艾雅法拉"]  呜......我的助听器......可能是刚才风太大了，还是受了一点影响。
[name="艾雅法拉"]  不好意思，您刚刚是在说自己的工作吧？
[name="艾雅法拉"]  巴蒂先生十分可靠呢。这趟出来多亏了巴蒂先生，如果只有我一个人的话，光是安装那些设备，就要花掉一整个下午。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  诶，一个人？这么重的设备，你一个人......还是太困难了吧。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  以前也有过啦。还在学校的时候，有一些研究需要一个人完成。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  咦，同学们呢？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  啊......那个，大家的进度不太一样......那些课题的话，确实还是需要一些经验的。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哎呦，说着说着就忘了，艾雅法拉小姐已经是个很厉害的学者，其他同学恐怕跟不上吧。
[name="干员巴蒂"]  就是这样的话，在学校还是太辛苦咯。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  其实还好啦......没、没关系的，一个人的话，慢慢地总能做好。
[name="艾雅法拉"]  不过哦，来罗德岛以后，无论是在船上还是偶尔出外勤，确实做什么都方便很多。
[name="艾雅法拉"]  新的助听器比之前的都要好用，凯尔希医生和前辈很支持我的研究，可露希尔小姐还帮忙改造了我的宿舍......
[name="艾雅法拉"]  就像巴蒂先生一样，干员们总是在很温柔地照顾着我。嗯......真的很感谢大家。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  这一路上被艾雅法拉小姐感谢了好多次，哎呀，真是越来越不好意思了。
[Dialog]
[Character]
[Character(name="avg_npc_068",fadetime=1,block=true)]
[delay(time=1)]
[name="向导"]  喂！前面也踩好点了，能走，就是路挺窄，你们这大玩意儿啊，过不去。
[Character(name="avg_npc_068",name2="char_180_amgoat",focus=2)]
[name="艾雅法拉"]  呃......最后一个采样点，是说没办法过去吗？
[Character(name="avg_npc_068",name2="char_180_amgoat",focus=1)]
[name="向导"]  人可以走。可——以——走。
[Character(name="avg_npc_068",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  那个，也不用这么大声吧？
[Character(name="avg_npc_068",name2="avg_npc_012",focus=1)]
[name="向导"]  这不是看她呆呆的，老是耳朵不大灵光的样子么。
[Character(name="avg_npc_068",name2="char_180_amgoat",focus=2)]
[name="艾雅法拉"]  抱歉......我现在听到了。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  那么，巴蒂先生，我们现在就过去？
[Character(name="avg_npc_068",name2="char_180_amgoat",focus=1)]
[name="向导"]  喂，等等，你也要过去？我说人可以走，但你这样的，还是算了吧？
[Character(name="avg_npc_068",name2="char_180_amgoat",focus=2)]
[name="艾雅法拉"]  咦？
[Character(name="avg_npc_068",name2="char_180_amgoat",focus=1)]
[name="向导"]  前面那路可不好走。这附近总地震，到处坑坑洼洼，说不好啥时候就一脚踩进坑里。要不是你们给钱多，连我都不乐意到这来。
[name="向导"]  你啊，你这平地走起来都不利索，还非要去凑热闹，这不纯粹添乱么？
[Character(name="avg_npc_068",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  你......你怎么能这么说艾雅法拉小姐？别看她年纪小，她可是最顶尖的火山学家！这次任务我们可都是听她指挥！
[Character(name="avg_npc_068",name2="avg_npc_012",focus=1)]
[name="向导"]  我才不管这个学家那个学家，前头的路就是要靠两条腿过去才行。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  呃说得也......那个，艾雅法拉小姐......他有句话说得没错，如果前面的路真的不好走，你要不然还是......
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  ......这样啊。
[name="艾雅法拉"]  很抱歉，巴蒂先生，向导先生......给你们添麻烦了。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  但是，我必须去。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  如果是担心设备的话，我都可以帮你安装好——
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  嗯，我知道，巴蒂先生说得没错。可前面就是这附近源石反应异常带的中心，必须使用更高精度的检测手段，这需要用上我的源石技艺。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  那，要不然就用附近这些采样点的数据？也不少了吧。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  不行哦巴蒂先生。想要得到最确切的结果，就不能放过每一处细节。如果我在这里偷懒的话，我们这趟任务，可能都会功亏一篑呢。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  艾雅法拉小姐突然变得好严肃......既然这样的话，那就只能出发了吧。
[name="干员巴蒂"]  不过事先说好哦，假如艾雅法拉小姐觉得很难受的话，我们需要随时停下来。就像做研究是艾雅法拉小姐的工作一样，这也是我的工作。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  嗯......我可以的，巴蒂先生不用担心。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  唉。怎么看都是在勉强自己啊！
[Character(name="avg_npc_068",name2="avg_npc_012",focus=1)]
[name="向导"]  啧，大实话你们不爱听。
[name="向导"]  我可说好了，万一出了点什么事，我只管我自己。
[Character(name="avg_npc_068",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哎你这人......
[Character(name="avg_npc_068",

... (全文18773字符)
```

### story_amgoat_2_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
4:32 P. M. 天气/阴
莱塔尼亚北部荒原 火山带7号采样点
......请您放心，本次任务顺利进入尾声，艾雅法拉小姐很疲惫，不过健康状况基本稳定。
本次调查的具体结果尚且不明，从艾雅法拉小姐的反应来看，应该有些小小的、难称突破的进展。
回程路上，我会继续确保她......
[playMusic(intro="$warm_intro", key="$warm_loop", volume=0.4)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_180_amgoat",fadetime=1,block=true)]
[delay(time=1)]
[name="艾雅法拉"]  巴蒂先生？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[delay(time=0.6)]
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="干员巴蒂"]  啊......啊！艾雅法拉小姐，有、有什么事吗？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  那个......左前方最近那个采样点的设备似乎偏移了一点，实时数据的背景噪声突然有些波动......
[name="艾雅法拉"]  您能不能帮忙看下是怎么回事？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  对、对不起！
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  咦？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  是我刚才动了一下！实在很抱歉，我我我不是有意要看数据——
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  唔......原来巴蒂先生是在看数据？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="干员巴蒂"]  咳、咳咳咳......
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  这样啊......那没事啦。我本来还以为是风太大导致的，这么看的话也不用检查其他采样设备了。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  呼......咦？居然一点都没生气？
[name="干员巴蒂"]  艾雅法拉小姐不怪我随便看数据吗？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  ......怪？我、我不是很确定有没有听清楚......巴蒂先生是说我有没有觉得奇怪吗？
[name="艾雅法拉"]  要说奇怪的话，是有一点。没想到巴蒂先生也会对这些研究数据有兴趣呢。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哈哈......确实。像我这样的大老粗......
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  没那回事啦。
[name="艾雅法拉"]  只是火山方面的研究不算热门，大多数时候就是像这样跑到荒地里，坐着观察一整天，然后埋头分析数据......一般人都会觉得枯燥吧？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  要说枯燥的话，这世上绝大多数人的生活都很枯燥啊。
[name="干员巴蒂"]  每天起床，吃东西，白天忙着各种活计，到了晚上就一觉睡过去。
[name="干员巴蒂"]  比起来，像艾雅法拉小姐这样学者，可是在永远都在和新鲜事物打交道。这起码有意义多了！
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  ......
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[CameraShake(duration=0.2, xstrength=10, ystrength=12, vibrato=30, randomness=70, fadeout=true, block=false)]
[name="干员巴蒂"]  ......笑、笑了！是我说的话太傻了吗？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  没有没有。巴蒂先生刚刚说话的语气，听起来有一点点像我过去认识的学校里的人哦。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哈哈，这个嘛，毕竟我过去也是和大学里的人打过交道的。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  诶？巴蒂先生不是一直从事安保方面的工作吗？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哎呀，好久以前的事了。那会我在......承蒙一位年轻教员的关照，才有了起步的工作机会。
[name="干员巴蒂"]  他帮助了我许多，也让我认识到做研究是一件有意义而且......呃，怎么说呢，没那么简单的事。对，没那么简单。
[stopmusic(fadetime=5)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_012",fadetime=1,block=true)]
[delay(time=1)]
......通过上次与凯尔希医生的交谈，知悉巴蒂先生目前在罗德岛就职，还有件事想要拜托......
是关于瑙曼小姐......她目前在罗德岛的代号叫做艾雅法拉。
她是我恩师唯一的孩子......
希望巴蒂先生能尽量关照这个孩子。
不仅仅是身体方面，她的矿石病确实已相当凶险......
还有她的研究工作。
请务必关注她的进展情况，有必要时麻烦与我联系。
[playMusic(intro="$dignified_intro", key="$dignified_loop", volume=0.4)]
[name="干员巴蒂"]  卡恩先生......
[name="干员巴蒂"]  出行之前凯尔希医生把这封信转交给我，但她应该很清楚，哪怕没有您的委托，我也会保护好艾雅法拉小姐。
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  说起来，艾雅法拉小姐第一次火山考察是在好几年前了吧？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  嗯，第一次考察的话......好像有三年多啦。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哎呀，那时候艾雅法拉小姐还是个小孩子啊！
[Character(name="avg_npc_012")]
[name="干员巴蒂"]  （小声）现在的研究机构都这么黑心的吗？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  目前助听器工作很正常，我都听到了哦巴蒂先生。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="干员巴蒂"]  啊，我不是在说罗德岛，千、千万别误会！
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  开个玩笑......其实威廉大学也没有啦，当时学校并不支持我这么早就参与进来。
[name="艾雅法拉"]  只是，爸爸妈妈留下的资料，有些内容只有我能解读。
[name="艾雅法拉"]  我不希望项目中断......我觉得爸爸妈妈也不希望项目中断。是我坚持要代替他们加入下一次实地考察的。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  爸爸妈妈......啊！抱歉抱歉，差点忘了艾雅法拉小姐的父母已经......
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  没关系的巴蒂先生，已经过去很久了。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  就是因为......火山？
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  嗯......火山很危险。妈妈从小就这么跟我说。
[name="艾雅法拉"]  ——光火焰就能轻松吞噬掉一栋房子。火山的话，是肚子里装满了能量的庞然巨物。
[name="艾雅法拉"]  巨物或许没有多余的想法，可是当它张开嘴，随意地呼吸或者咳嗽——它就会改变大地。
[name="艾雅法拉"]  说来有些好笑，我很小的时候，并不能真正理解爸爸妈妈的工作。那时候在我心里，爸爸妈妈是挑战巨物的勇士。
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=2)]
[name="干员巴蒂"]  哎，说是勇士也不为过吧？明知危险，却还是坚持去做。这需要多大的勇气啊！
[Character(name="char_180_amgoat",name2="avg_npc_012",focus=1)]
[name="艾雅法拉"]  ......也会害怕

... (全文13506字符)
```

### story_angel_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 个人剧情 能天使
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[playMusic(intro="$longmenbat_intro", key="$longmenbat_loop", volume=0.4)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.3, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=1, xstrength=8, ystrength=6, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0.7, r=0.95, g=0.95, b=0.95, fadetime=0.02, block=true)]
[PlaySound(key="$d_sp_ballista")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.25, block=true)]
砰砰砰！
啪啪！砰！
哒哒哒哒！砰啪！
[Dialog]
[delay(time=0.6)]
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.8, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.8, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=60, fadeout=true, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=60, fadeout=true, block=true)]
[PlaySound(key="$p_atk_smg_h", volume=0.6)]
[CameraShake(duration=0.1, xstrength=10, ystrength=12, vibrato=30, randomness=60, fadeout=true, block=true)]
[Character(name="char_103_angel_1#2",fadetime=2,block=true)]
[Delay(time=1)]
[name="能天使"]  咻咻咻！砰砰！
[name="能天使"]  最后一个人，最后一颗橡皮弹，无污染无浪费，绝对节能环保，你觉得怎么样？
[name="能天使"]  追了我三条街，你们还真执着欸，都说东西不在我身上了。
[Character(name="avg_npc_002")]
[name="地痞"]  混蛋，什么环保，你是在耍我吗？！
[Character(name="char_103_angel_1#2")]
[name="能天使"]  被你发现啦？没办法，因为要解决掉你们真的简单到无聊嘛。
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[name="能天使"]  好啦，游戏结束。这位先生，如果还有什么想说的，建议你趁现在抓紧时间说哦。
[Character(name="avg_npc_002")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="地痞"]  别过来，你别过来！
[dialog]
[Character]
[Character(name="char_103_angel_1#2",fadetime=2,block=true)]
[Delay(time=1)]
[name="能天使"]  3、2、1，时间到——
[name="能天使"]  啪！你死啦！
[PlaySound(key="$pistol", volume=0.6)]
[dialog]
[Character(name="avg_npc_002")]
[CameraShake(duration=1, xstrength=10, ystrength=12, vibrato=30, randomness=90, fadeout=true, block=true)]
[name="地痞"]  呃，啊。
[Dialog]
[Character(fadetime=1,block=true)]
[PlaySound(key="$bodyfalldown2", volume=0.9)]
[Delay(time=2)]
[Character(name="char_103_angel_1#8")]
[name="能天使"]  ——全中！
[Character(name="char_103_angel_1#5")]
[name="能天使"]  不愧是我，准头真好。嗯，奖励自己今天可以多吃一块苹果派！
[stopmusic(fadetime=1)]
[name="能天使"]  接下来......工作工作。
[Dialog]
[Character]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Background(image="bg_lmstreet_2",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Character(name="char_103_angel_1#3")]
[name="能天使"]  唔，今天最后一个地址，中街12-7号，阿徐饭馆......
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.2)]
[Character(name="char_103_angel_1#7")]
[name="能天使"]  ......哇哦，抱歉，有没有撞到你？
[character]
[name="路人"]  没关系。
[name="路人"]  阿徐饭馆的话就在那边哦，方向反了。
[Character(name="char_103_angel_1#8")]
[name="能天使"]  啊，真的......谢谢你啊，小哥。
[Character]
[name="路人"]  不客气。难得看到同乡。
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[Character(fadetime=1,block=true)]
[Delay(time=1)]
[Character(name="char_103_angel_1#7")]
[name="能天使"]  ......嗯？
[name="能天使"]  （拉特兰人？看起来是信使啊......）
[Character(name="char_103_angel_1#6")]
[name="能天使"]  （信......）
[Character(name="char_103_angel_1#3")]
[name="能天使"]  （......安魂夜前写封信回家好像也不错。）
[name="能天使"]  基地应该有信纸吧，嗯......也买点特产一起送回去好了。
[Character(name="char_103_angel_1#5")]
[PlaySound(key="$d_gen_walk_n", volume=0.6)]
[name="能天使"]  先工作，先工作，阿徐饭馆......
[name="能天使"]  有了，就是这里。
[Character(name="char_103_angel_1#3")]
[name="能天使"]  打扰了，有人在吗？企鹅物流送货上门——
[PlaySound(key="$doorknockquite", volume=0.6)]
[delay(time=0.5)]
[Character(name="avg_npc_033")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="一般龙门市民"]  谁啊......哇啊！这是怎么回事，地上这是......死、死人了？！
[Character(name="avg_npc_033", name2="char_103_angel_1#4", focus=2)]
[name="能天使"]  嘿嘿，没什么，别在意这种小事！
[Character(name="avg_npc_033", name2="char_103_angel_1#3", focus=2)]
[name="能天使"]  企鹅物流加急特送，街区重建出血特惠服务，现在起三天内配送费减半哦！这些都是您订购的货物没错吧？
[Character(name="avg_npc_033", name2="char_103_angel_1#3", focus=1)]
[name="一般龙门市民"]  ......快递？
[name="一般龙门市民"]  等下，这应该是送错了吧？
[Character(name="avg_npc_033", name2="char_103_angel_1#7", focus=2)]
[name="能天使"]  欸？
[Character(name="avg_npc_033", name2="char_103_angel_1#7", focus=1)]
[name="一般龙门市民"]  我是订了东西，可这才刚下单没几个小时，应该没可能送到......
[Character(name="avg_npc_033", name2="char_103_angel_1#5", focus=2)]
[name="能天使"]  这话就不对了，下单都几个小时了，物品送达也很正常吧？
[name="能天使"]  速度可是物流业的生命耶！
[Character(name="avg_npc_033", name2="char_103_angel_1#7", focus=2)]
[name="能天使"]  扩音器材、彩灯、还有花篮。哇哦，是新店开张用的吗？
[Character(name="avg_npc_033", name2="char_103_angel_1#7", focus=1)]
[name="一般龙门市民"]  嗯，嗯......
[Character(name="avg_npc_033", name2="char_103_angel_1#3", focus=2)]
[name="能天使"]  恭喜恭喜。东西都在这儿了，怎么样，没错吧？
[Character(name="avg_npc_033", name2="char_103_angel_1#3", focus=1)]
[name="一般龙门市民"]  确实，这些和我的订单内容一模一样..

... (全文27947字符)
```

### story_angel_2_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_motorway",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[PlaySound(key="$d_gen_transmissionget",volume=0.6)]
[dialog]
[character]
[delay(time=1)]
[CharacterCutin(widgetID="1", name="avg_300_phenxi_1#1$1", style="cutin", fadestyle= "horiz_expand_center", fadetime=0.5, offsetx=-300, width=200, block=true)]
[Character(name="char_empty",name2="avg_213_mostma_1#1$2",focus=-1)]
[name="黎明破坏者"] 我很好奇，我只是上个厕所的工夫，你又跑哪里去了？
[Character(name="char_empty",name2="avg_213_mostma_1#2$2",focus=2)]
[name="莫斯提马"] 如果我告诉你我正处在性命攸关时刻的话，你信不信？
[Character(name="char_empty",name2="avg_213_mostma_1#2$2",focus=-1)]
[name="黎明破坏者"] 龙门应该是一座治安良好的城市。
[Character(name="char_empty",name2="avg_213_mostma_1#5$2",focus=2)]
[name="莫斯提马"] 我也想知道，为什么在这样一座治安良好的城市里，我走在大街上会被擦肩而过的人追杀。
[Character(name="char_empty",name2="avg_213_mostma_1#1$2",focus=2)]
[name="莫斯提马"] 好吧，其实我大概知道为什么。
[Character(name="char_empty",name2="avg_213_mostma_1#5$2",focus=2)]
[name="莫斯提马"] 你找个地方喝奶茶吧，可以帮我也带一杯。挂了。
[Character(name="char_empty",name2="avg_213_mostma_1#5$2",focus=-1)]
[name="黎明破坏者"] 喂，你的信怎——
[Dialog]
[CharacterCutin(widgetID="1",block=true)]
[playsound(key="$transmission", volume=0.4)]
[delay(time=1)]
[Character(name="avg_213_mostma_1#1$2")]
[delay(time=1)]
[PlaySound(key="$d_avg_bldwhoosh", volume=1)]
[characteraction(name="middle", type="jump", xpos=-350, times=1, fadetime=0.5, block=false)]
[Character(name="avg_213_mostma_1#1$2",name2="char_102_texas_1#1")]
[delay(time=1)]
[Dialog]
[Character(name="avg_213_mostma_1#1$2",name2="char_102_texas_1#1",focus=1)]
[name="莫斯提马"] 德克萨斯，理论上我们应该算是同事吧。
[Character(name="avg_213_mostma_1#1$2",name2="char_102_texas_1#1",focus=2)]
[name="德克萨斯"] 算是。
[Character(name="avg_213_mostma_1#5$2",name2="char_102_texas_1#1",focus=1)]
[name="莫斯提马"] 在街上随意对同事出剑不是和同事相处的方式吧。
[Character(name="avg_213_mostma_1#5$2",name2="char_102_texas_1#1",focus=2)]
[name="德克萨斯"] 但是能天使一直在找你。
[Character(name="avg_213_mostma_1#5$2",name2="char_102_texas_1#1",focus=2)]
[name="德克萨斯"] 而且你很难对付，所以把你放倒之后绑去给能天使那家伙会比较方便。
[Character(name="avg_213_mostma_1#10$2",name2="char_102_texas_1#1",focus=1)]
[name="莫斯提马"] 唉，不愧是叙拉古出身的人，做事干净利落啊。
[Character(name="avg_213_mostma_1#10$2",name2="char_102_texas_1#1",focus=1)]
[name="莫斯提马"] 我得承认，刚才那一下，确实只差一点就让你得手了。
[Character(name="avg_213_mostma_1#7$2",name2="char_102_texas_1#1",focus=1)]
[name="莫斯提马"] 但到了现在，你是抓不住我的。
[Character(name="avg_213_mostma_1#7$2",name2="char_102_texas_1#1",focus=2)]
[name="德克萨斯"] 我从大帝那里听过一些你的事，所以，我也没有打算一个人对付你。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_103_angel_1#1$1",fadetime=1.5)]
[delay(time=2)]
[multiline(name="能天使")]喂，德克萨斯，你不是在送货吗，怎么忽然把我喊过来......
[Character(name="avg_103_angel_1#4$1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[multiline(name="能天使")]欸？！
[Character(name="avg_213_mostma_1#7$2")]
[name="莫斯提马"] 哈喽。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]莫斯提马？！
[Character(name="char_102_texas_1#1")]
[name="德克萨斯"] 凑巧遇到的。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]厉害啊，德克萨斯！
[Character(name="char_102_texas_1#1")]
[name="德克萨斯"] 老样子，我正面你包抄。
[Character(name="char_102_texas_1#1")]
[name="德克萨斯"] 把她绑在椅子上，我有许多方法让她说出你想知道的事。
[Character(name="avg_213_mostma_1#10$2")]
[name="莫斯提马"] 叙拉古式的方法？
[Character(name="char_102_texas_1#1")]
[name="德克萨斯"] 德克萨斯式的方法。
[Character(name="avg_213_mostma_1#10$2")]
[name="莫斯提马"] 小乐，你不会也打算动手吧？
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]......
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]为什么不呢？
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]老板经常会说起企业文化，虽然企业文化的关键词总是在变，但我的企业文化关键词一直都是——
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]玩得痛快！
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]来玩吧，莫斯提马。
[Character(name="avg_213_mostma_1#1$2")]
[name="莫斯提马"] ......
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[Character(name="avg_213_mostma_1#1$1",fadetime=0.7)]
[delay(time=1)]
[name="莫斯提马"] 那么，来玩警察抓小偷吧，抓到我，就算你们赢。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]无论用什么方法抓到？
[Character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"] 打倒我也没关系，小乐，你可以用你的铳。
[Character(name="avg_103_angel_1#4$1")]
[name="能天使"]欸？
[Character(name="avg_213_mostma_1#10$1")]
[name="莫斯提马"] 放心，戒律不保护堕天使。
[Character(name="avg_103_angel_1#5$1")]
[multiline(name="能天使")]哦......
[Character(name="avg_103_angel_1#2$1")]
[multiline(name="能天使")]不对，在市区怎么用铳啊！你也不准用你的那个法术！
[Character(name="avg_213_mostma_1#9$1")]
[name="莫斯提马"] 好吧，就当增加一些难度。至于你——
[Character(name="char_102_texas_1#1")]
[name="德克萨斯"] 我可以不用源石技艺。
[Character(name="avg_213_mostma_1#11$1")]
[name="莫斯提马"] 但不打算放下武器，对吧？
[Character(name="char_102_texas_1#1")]
[name="德克萨斯"] 只要你别反抗得太厉害，应该不会受伤。
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]那么，三——（使眼色）
[Character(name="char_102_texas_1#3")]
[name="德克萨斯"] （微微点头）
[Character(name="avg_103_angel_1#6$1")]
[name="能天使"]开始！
[dialog]
[PlaySound(key="$rungeneral", volume=0.9)]
[character(fadetime=0.5)]
[delay(time=0.51)]
[Character(name="char_empty")]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.7, block=true)]
[delay(time=0.7)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.5, block=false)]
[Character(name="avg_213_mostma_1#10$1")]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=-800, fadetime=0.3, block=false)]
[character(fadetime=0.3)]
[delay(time=0.51)]
[Character(name="avg_103_angel_1#4$1")]
[characteraction(name="middle", type="jump", power=5, times=2, fadetime=0.51,block=true)]
[delay(time=0.51)]
[name="能天使"]好快！
[dialog]
[character]
[name="远处的莫斯提马"]小乐，你这招我早就习惯了。
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]果然是莫斯提马啊......
[Character(name="avg_103_angel_1#1$1")]
[name="能天使"]德克萨斯，你吃过饭了吧？
[Character(name="char_102_texas_1#1")]
[nam

... (全文34840字符)
```

### story_ansel_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_corridor",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_002",focus="m")]
[name="罗德岛信使"]就这些吗，安赛尔？
[charslot(slot="m",name="avg_212_ansel_1#2$1",focus="m")]
[name="安赛尔"]嗯，下个月A4预备小队的任务目的地就是铁腕城，所以，不用麻烦你从家乡带什么东西回来了。
[charslot(slot="m",name="avg_npc_002",focus="m")]
[name="罗德岛信使"]我知道，可是......你不给你的家人寄几封信回去吗？
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]......没关系的。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]把这封给我朋友的信带到就可以了，恩加拉会帮我出主意的。
[charslot(slot="m",name="avg_212_ansel_1#2$1",focus="m")]
[name="安赛尔"]啊，对了，只有那个大包裹是给他的，这小盒的消炎药是给你的，在野外被虫兽咬了的话会很有用，不要忘记拿了。
[charslot(slot="m",name="avg_npc_002",focus="m")]
[name="罗德岛信使"]......哈哈，要是撞见你的家人，我会很难办啊。
[charslot(slot="m",name="avg_npc_002",focus="m")]
[name="罗德岛信使"]那我出发了，安赛尔，多谢啦。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]嗯，我也该继续做准备了。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]......呼。
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=1)]
[Background(image="46_g4_rmbtwild_d",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[playMusic(intro="$frontline_intro",key="$frontline_loop", volume=0.6)]
[Delay(time=1)]
[charslot(slot="m",name="char_211_adnach_1#5",focus="m")]
[name="安德切尔"]玫兰莎，我现在看不见你了，提供不了火力掩护！
[charslot(slot="m",name="char_211_adnach_1#5",focus="m")]
[name="安德切尔"]东北方向又有两只小钳兽过来了！卡缇，不能冲！
[charslot(slot="m",name="char_211_adnach_1#5",focus="m")]
[name="安德切尔"]遵照安赛尔规划的医疗支援线路！
[charslot(slot="m",name="char_209_ardign",focus="m")]
[name="卡缇"]没事，我不会让安赛尔为难的！
[charslot(slot="m",name="char_209_ardign",focus="m")]
[name="卡缇"]呼——哼哼，闻到了！气味引诱剂！
[charslot(slot="m",name="char_209_ardign",focus="m")]
[name="卡缇"]玫兰莎，控制这些钳兽的驯兽师绝对就在东北方向，说不好就躲在那个矿场黑乎乎的入口里！
[charslot(slot="m",name="char_208_melan_1#5",focus="m")]
[name="玫兰莎"]了解了。史都华德......往后撤，这边交给我。
[charslot(slot="m",name="char_208_melan_1#5",focus="m")]
[name="玫兰莎"]你可以帮安赛尔照顾一下护送目标吗？
[dialog]
[charslot]
[charslot(slot="l",name="avg_212_ansel_1#5$1",focus="all",duration=1)]
[charslot(slot="r",name="avg_npc_243",focus="all",duration=1)]
[delay(time=2)]
[charslot]
[charslot(slot="m",name="avg_212_ansel_1#5$1",focus="m")]
[name="安赛尔"]请躺下，女士。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="惊慌的商人"]躺下？开什么玩笑？医生，带我们回载具！
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="惊慌的商人"]你是眼瞎了看不到那些虫子和钳兽，还是听不到榴弹爆炸的声音？！
[charslot(slot="m",name="avg_212_ansel_1#5$1",focus="m")]
[name="安赛尔"]请相信我的队友。
[charslot(slot="m",name="avg_212_ansel_1#5$1",focus="m")]
[name="安赛尔"]这个位置下，我能够及时支援他们，他们也会比载具的铁皮更好地保护我们。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="惊慌的商人"]你、你确定？
[dialog]
[charslot]
[PlaySound(key="$grenade_explosion", volume=1)]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2)]
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="惊慌的商人"]——噫！
[charslot(slot="m",name="avg_212_ansel_1#5$1",focus="m")]
[name="安赛尔"]刺伤您的钳兽有毒性，请保持镇静，躺下减缓血液流速，并尽快接受处理。这样也能避免您的中枢神经受到不可逆转的损害。
[charslot(slot="m",name="avg_212_ansel_1#5$1",focus="m")]
[name="安赛尔"]不用太担心，我有携带对应的解毒血清。
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="惊慌的商人"]这、这......
[charslot(slot="m",name="avg_npc_243",focus="m")]
[name="惊慌的商人"]......好吧，我听你的，医生。
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=1)]
[charslot(duration=1)]
[delay(time=2)]
[name="惊慌的商人"]......你真的没弄错？万一你认错了钳兽的种类，你、你要怎么赔我？
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]不会的，我很熟悉雷姆必拓的自然生物。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]好了，请放松......
[charslot]
[name="惊慌的商人"]等等，医、医生，过来了，那边——
[name="史都华德"]安赛尔，低头！
[dialog]
[PlaySound(key="$grenade_explosion", volume=1)]
[PlaySound(key="$d_sp_ballista", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[CameraShake(duration=1.7, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=3)]
[charslot]
[name="史都华德"]靠近的威胁我已经处理掉了，那边还有一名伤员，我背到安全的位置了！
[charslot(slot="m",name="avg_212_ansel_1#5$1",focus="m")]
[name="安赛尔"]好，稍微等我一下！
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]女士，注射完成了，您可以再休息一下。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]接下来我会去治疗您队伍中的其他伤员。医疗处理全部完成之后，我们会按任务需求继续护送各位的。
[charslot]
[name="惊慌的商人"]呼，呼......
[name="惊慌的商人"]谢谢......
[name="惊慌的商人"]......医生，有没有人说过，以你的年纪，你冷静得有些......吓人？
[charslot(slot="m",name="avg_212_ansel_1#3$1",focus="m")]
[name="安赛尔"]欸？
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]不，我只是尽力专注于自己能做到的事情而已。
[charslot]
[name="惊慌的商人"]但你很了不起。你一定救过很多人吧。
[charslot(slot="m",name="avg_212_ansel_1#6$1",focus="m")]
[name="安赛尔"]我......
[charslot]
[Dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(slot="m",name="char_210_stward_1#3",focus="m",duration=1)]
[delay(time=1.5)]
[name="史都华德"]安赛尔，情况如何？
[charslot(slot="m",name="char_210_stward_1#2",focus="m")]
[name="史都华德"]......怎么突然这么低落？
[charslot(slot="m",name="avg_212_ansel_1#3$1",focus="m")]
[name="安赛尔"]——啊。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]能量补充营养剂在挎包里。我马上给你处理伤口。
[charslot(slot="m",name="avg_212_ansel_1#1$1",focus="m")]
[name="安赛尔"]抱歉，我竟然一下子走神了。
[charslot(slot="m",name="char_210_stward_1#6",focus="m")]
[name="史都华德"]哈哈，这说明你的队友们值得你信任。
[charslot(slot="

... (全文24498字符)
```

### story_aosta_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_corridor",screenadapt="coverall")]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4,fadetime=3)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[Character(name="char_016_medic",name2="char_empty",fadetime=1)]
[StopSound(channel="bgs", fadetime=1)]
[Delay(time=1)]
[Character(name="char_016_medic",name2="char_empty",focus=1)]
[name="医疗干员"]在这里！我看到他啦。
[Dialog]
[playsound(key="$rungeneral", loop=true, channel="bgs")]
[Character(name="char_016_medic",name2="avg_npc_088",fadetime=1)]
[StopSound(channel="bgs", fadetime=1)]
[Delay(time=1)]
[Character(name="char_016_medic",name2="avg_npc_088",focus=2)]
[name="术师干员"]嗯来了来了。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="avg_346_aosta_1#1$1",fadetime=1)]
[Delay(time=2)]
[name="奥斯塔"]唔，你们好。
[Dialog]
[PlaySound(key="$d_avg_cloakmovement")]
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic")]
[Delay(time=1)]
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=1)]
[name="奥斯塔"]已经做好了，看一看符合心意吗？
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]喔喔——
[Character(name="avg_npc_088")]
[name="术师干员"]嗬，真的是你做的？
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]我没想到这么快就做好了！好、好可爱！
[Character(name="avg_346_aosta_1#7$1",name2="char_016_medic",focus=1)]
[name="奥斯塔"]做的时候有了一些灵感，所以时间比想象中用得少，还有想修改的地方吗？
[Character(name="avg_346_aosta_1#7$1",name2="char_016_medic",focus=2)]
[Characteraction(name="right", type="jump", power=30, times=1, fadetime=0.4,block=true)]
[name="医疗干员"]我完全没有意见，这就是我想要的样子！
[Character(name="avg_346_aosta_1#7$1",name2="char_016_medic")]
[Dialog]
[characteraction(name="right", type="move", xpos=-80, fadetime=1.5, block=true)]
[PlaySound(key="$d_avg_glassclink", volume=1,delay=1)]
[Delay(time=2)]
[Character(name="avg_346_aosta_1#7$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]喏，这是当时定好的报酬~顺便，我们前几天在厨房烤了些饼干，也请收下尝尝吧！
[Dialog]
[characteraction(name="right", type="move", xpos=80, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_346_aosta_1#2$1",name2="char_016_medic",focus=1)]
[name="奥斯塔"]饼干吗？唔，谢谢了。
[Character(name="avg_346_aosta_1#2$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]嘿嘿，我越看越喜欢，你领子内衬用的材料也好好哦！摸上去软软的。
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=1)]
[name="奥斯塔"]对，我试过好几种材料，还是这种更柔软一点。
[name="奥斯塔"]那几天为了挑材料真是费了不少事。
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]那你是在宿舍里做这衣服的吗，需要的材料会很多吧？我前阵子沉迷积木的时候也是，不知不觉占用了太多公共空间，已经被骂咯。
[name="医疗干员"]你的舍友会对这个有意见吗？要是因为我你们之间有了矛盾，我会有点过意不去的。
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=1)]
[name="奥斯塔"]那倒没有，他们都知道我这个爱好的。
[Character(name="avg_346_aosta_1#1$1",name2="char_016_medic",focus=2)]
[name="医疗干员"]不过，柏喙干员申请了一个纺织室，你也可以去和后勤部申请一下，这样材料就不用堆在宿舍里了。
[name="医疗干员"]或者你可以在舰上开个摊的！
[name="医疗干员"]柏喙小姐基本上只主动去找人做衣服，梓兰小姐基本上是提供一些穿搭经验，你要是开个小摊，就是独一份呀！
[Dialog]
[Character(name="avg_346_aosta_1#2$1")]
[name="奥斯塔"]......
[Character(name="avg_346_aosta_1#2$1",name2="avg_npc_088",focus=2)]
[name="术师干员"]不过看你的表情，你是不是还没和她们说过话？
[Character(name="avg_346_aosta_1#3$1",name2="avg_npc_088",focus=1)]
[name="奥斯塔"]嗯......是的。说实在的，你们都是听了贾维的话才来找我的，但我其实还没想过要给其他干员做衣服挂件这些事情。
[name="奥斯塔"]我也还不认识你说的这两位干员。
[Character(name="avg_346_aosta_1#3$1",name2="avg_npc_088",focus=2)]
[name="术师干员"]我就这么一提啦~不过柏喙和梓兰小姐她们都是很好相处的人，你要是想和她们聊聊，肯定不会有问题的。
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[Character(name="char_252_bibeak_1#1",fadetime=0.5)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0,block=true)]
[characteraction(name="middle", type="move", xpos=400, fadetime=3,block=false)]
[Delay(time=2)]
[Character(fadetime=0.5)]
[Delay(time=1)]
[Character(name="avg_346_aosta_1#1$1",name2="avg_npc_088")]
[Blocker(a=0, fadetime=0.5, block=true)]
[Characteraction(name="right", type="jump", power=30, times=1, fadetime=0.5,block=true)]
[Character(name="avg_346_aosta_1#1$1",name2="avg_npc_088",focus=2)]
[name="术师干员"]那位就是柏喙小姐！
[Character(name="char_252_bibeak_1#1")]
[name="柏喙"]欸？
[name="柏喙"]叫我吗？
[Dialog]
[PlaySound(key="$d_gen_walk_n", volume=0.7)]
[Character(name="avg_346_aosta_1#1$1",name2="char_252_bibeak_1#1")]
[characteraction(name="left", type="move", xpos=-200, fadetime=0,block=true)]
[characteraction(name="left", type="move", xpos=200, fadetime=1.5,block=true)]
[Delay(time=2)]
[Character(name="avg_346_aosta_1#1$1",name2="char_252_bibeak_1#1",focus=1)]
[name="奥斯塔"]啊、啊，不好意思！
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[character(fadetime=0)]
[Background(image="bg_warehouse",screenadapt="coverall")] 
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_252_bibeak_1#1")]
[name="柏喙"]这里就是我的仓库了。
[name="柏喙"]今天我还邀请了梓兰姐，她会来给其他干员们教教设计，你要是有什么知道的缝纫知识，也可以教给大家。
[Character(name="avg_346_aosta_1#1$1")]
[name="奥斯塔"]打扰了，只是我原本是打算来问点问题，可能没什么能教的。
[Character(name="char_252_bibeak_1#1")]
[name="柏喙"]没事没事，我其实也没什么能教给大家的东西，只是互相交流一下自己关于缝纫的想法，你能来，我很感谢！
[Dialog]
[Character]
[playsound(key="$dooropenquite")]
[Character(name="char_278_orchid_1#6",fadetime=1)]
[Delay(time=1)]
[name="梓兰"]柏喙？我来啦。
[Character(name="char_252_bibeak_1#1")]
[name="柏喙"]梓兰姐！
[Character(name="char_278_orchid_1#3")]
[name="梓兰"]这位是？
[Character(name="avg_346_aosta_1#1$1")]
[name="奥斯塔"]您好，我是奥斯塔，今天也一起来上课。
[Character(name="char_278_orchid_1#6")]
[name="梓兰"]“您”？不用这么礼貌啦。你比我组里的人看起来顺眼多了，和他们待久了，有点不敢相信罗德岛上还有这样的好孩子......啊。
[Character(name="avg_npc_090")]
[name="认真的干员"]真好，我还以为只有我一个男干员呢！
[Character(name="char_278_orchid_1#6")]
[name="梓兰"]抱歉，我是最后一个来的吗？给大家带了一点小吃，空闲时间可以尝一点。
[Character(name="char_252_bibeak_1#1")]
[name="柏喙"]谢谢梓兰姐，那我们开始吧~
[Dialog]
[Character]
[playsound(key="$d_avg_crwddiscuss_inside",volume=0.3,loop=true, channel="a")]
[Delay(time=1)]
整个

... (全文22770字符)
```

### story_aprl_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_barracks")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_365_aprl_1#1$1",fadetime=1)]
[delay(time=1.5)]
[playsound(key="$d_gen_transmissionget")]
[delay(time=0.7)]
[name="爱尔莉"]喂，是我，爱尔莉。
[name="爱尔莉"]刚刚营地的广播你听到了吗？......对喔，我现在还在任务中，离钢铁萝卜城大概也就走个一天一夜的距离吧。
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]是啊！本来我以为这两天就可以回家了，结果今天接到新的通知，我们这支勘察队在中转站补给之后，还要去更远的矿区。
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]唉，公司的队伍说走就走，安排我当护卫，我也没有什么办法呢。
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]所以，这周的聚会我去不了啦，不好意思哦。
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]......当然会觉得有点可惜啦，毕竟大家准备了这么久嘛。好不容易找到那间废弃的矿石仓库可以做场地，又花了那么大力气把它布置好。
[Character(name="avg_365_aprl_1#7$1")]
[name="爱尔莉"]啊，这样一看，还好我负责的工作前期就完成了呢，现在突然到不了场也不会误什么事。
[Character(name="avg_365_aprl_1#6$1")]
[name="爱尔莉"]（难过）嗯，是哦，反正以后还有很多机会......
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]......下一次聚会的时候，天气应该就很暖和了呢，之前我们一起逛街的时候买的那条连衣裙总算可以穿了。
[Character(name="avg_365_aprl_1#7$1")]
[name="爱尔莉"]......对吧，你也很期待吧？我还买了能搭配的耳饰呢。
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]啊，对了，你们之前说排练了一首我喜欢的歌要在聚会上表演，但是要给我个惊喜，所以先不告诉我是哪首......现在总可以说了吧？
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]......我猜不到啦，我喜欢的乐队两只手都数不过来，每支乐队还有那么多好专辑，要我从中挑一首歌也太难了吧。
[name="爱尔莉"]也不要再等下一次聚会啦，万一下次我又被公司安排长期任务了呢？
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]......喔，那首啊，确实很应景呢！
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]你们可要成为超级明星组合喔，那样我就可以实现在家门口看演唱会的心愿了。
[Character(name="avg_365_aprl_1#6$1")]
[name="爱尔莉"]......
[Dialog]
[character]
不着痕迹地，卡特斯女孩突然用手捂住了通讯器的收音位置。
[name="猎人的声音"]......哇，那个花枝招展的小卡特斯？不会吧，她怎么在这儿，最近还有人敢委托任务给她？
[name="工作人员的声音"]但她依然是注册猎人，原则上她是可以在营地停留的，虽然是独来独往......
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]......啊，队伍要出发了呢，本来我还想跟你抱怨一下这次任务有多麻烦，看来只能下次再说啦。
[name="爱尔莉"]嗯，我回到城里再联系你们咯。
[dialog]
[playsound(key="$transmission", volume=0.4)]
[delay(time=2)]
[character]
[name="猎人的声音"]如果我是她的话，我就会识相地低下头赶快走掉。不过看她穿得那么惹眼，大概还是和以前一样不知好歹吧，哈哈哈......
[Character(name="avg_365_aprl_1#6$1")]
[name="爱尔莉"]......啊，赶路的时候就把耳机戴上吧。
[Dialog]
[playsound(key="$d_avg_clothmovement")]
[stopmusic(fadetime=1)]
[delay(time=2)]
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]嗯，清净多啦！为了不犯困，路上就听点动感的音乐吧！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_forest",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]	
[playsound(key="$d_gen_walk_n")]
[character(name="avg_365_aprl_1#6$1",fadetime=1.5)]
[delay(time=2)]
[name="爱尔莉"]咦，最近的价目表被我放在哪里了......啊，对，这里写了裂兽的价格最高。
[name="爱尔莉"]不过我也不会处理那种庞然大物呀......还是算了。
[name="爱尔莉"]以前只要把野兽赶走就好了，现在却要主动去树林里找它们的麻烦呢。
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]还好只差一点点就攒够目标金额了，就算再捕几只羽兽，应该也够了吧。
[Character(name="avg_365_aprl_1#3$1")]
[name="爱尔莉"]按照公司福利政策，攒下来的钱差不多能买一台公司淘汰的旧投影仪了呢，那样就可以躺在床上看买来的影碟了。
[Character(name="avg_365_aprl_1#2$1")]
[name="爱尔莉"]不不，有钱的话，首先还是改善一下住宿条件吧。如果换间隔音好一点的出租屋，半夜出完任务回家或者搬动家具就不会吵到邻居了。
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]啊，我还是不太擅长做长线计划呢......
[dialog]
[character]
[stopmusic(fadetime=1)]
[playsound(key="$leaveshake", volume=0.4)]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=20, randomness=70, fadeout=true, block=true)]
[Delay=(time=1.5)]
[Character(name="avg_365_aprl_1#6$1")]
[name="爱尔莉"]......有动静了。
[name="爱尔莉"]不知道今天的运气怎么样呢......受伤的野兽总是会跑掉，从书上学来的陷阱也不知道好不好用。
[Dialog]
[character]
[delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_008",blackstart=0.4,blackend=0.6,fadetime=1.5)]
[delay(time=2.8)]
[Character(name="avg_365_aprl_1#2$1")]
[name="爱尔莉"]是人啊！好险好险——
[Dialog]
[Delay(time=1)]
[playsound(key="$d_avg_arrowshot")]
[characteraction(name="middle", type="move", xpos=200, fadetime=0.3, block=false)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[name="爱尔莉"]喂，你好——别认错啦，我不是猎物，我是猎人呀！我都穿得这么鲜艳了，应该不像野兽吧？
[dialog]
[character]
[PlayMusic(intro="$chasing_intro", key="$chasing_loop", volume=0.4)]
[character(name="avg_npc_008",fadetime=1,block=true)]
[Delay(time=1.5)]
[name="强盗头目"]我们可没认错，你就是我们的猎物。
[name="强盗头目"]值钱的东西都交出来，不然别怪我们不客气。
[dialog]
[character]
[playsound(key="$d_gen_walk_n")]
[character(name="avg_npc_007",name2="avg_npc_007",fadetime=1,block=true)]
[delay(time=2.5)]
[Character(name="avg_365_aprl_1#2$1")]
[name="爱尔莉"]欸，好像真的有其他人靠过来了......
[name="爱尔莉"]躲在那边树上的，我背后石头旁边的......
[Dialog]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=false)]
[playsound(key="$d_avg_arrowshot")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Delay(time=1)]
[character]
[character(name="avg_npc_007")]
[name="强盗头目"]我倒数三次，乖乖把钱拿来。否则，就不是一支箭这么简单的事情了。
[name="强盗头目"]三。
[Character(name="avg_365_aprl_1#5$1")]
[name="爱尔莉"]......不行哦。
[character(name="avg_npc_007")]
[name="强盗头目"]二。
[Character(name="avg_365_aprl_1#5$1")]
[name="爱尔莉"]这些钱可是我好不容易攒下来的。
[character(name="avg_npc_007")]
[name="强盗头目"]一。
[Character(name="avg_365_aprl_1#5$1")]
[name="爱尔莉"]要不你们还是试试看能不能追上我吧！
[stopmusic(fadetime=1)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.2)]
[Delay(time=2)]
[Background(image="bg_barracks",screenadapt="showall")]
[CameraEffect(effect="Grayscale", amount=0.8, keep=true)]
[Character(name="avg_365_aprl_1#1$1")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="avg_365_aprl_1#1$1",focus=-1)]
[name="杂货市场老板"]哦，爱尔莉，你又过来啦。
[Character(name="avg_365_aprl_1#1$1")]
[name="爱尔莉"]是呀，今天总算把家里收拾完啦。没想到我的房间不大，杂七杂八的东西还挺多的呢。
[Character(name="avg_365_aprl_1#1$1",fo

... (全文18790字符)
```

### story_aprot2_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)] 
天空的颜色很古怪。
太阳暗淡无光，云朵染着灰色，天幕从远处开始破碎，裂痕向着中心蔓延。
但这一切在此时都不再重要。
你还记得这一天。
你总是忘不掉这一天。
这一天好似一个注定会来的预言，早已被所有人知晓。
这一天又像一个无法摆脱的噩梦，从无一刻停止纠缠。
你已经分不清这是否是一场戏。
你的生活，或许从来只是他人眼中的一场戏。
沉渊。
你问你自己。
台上的演员只有剧本，可是你呢？
你要怎么选择？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="bg_indoor_u",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4025_aprot2_1#6$1",duration=1.5)]
[Delay(time=2)]
[playsound(key="$d_avg_daggerexsheath")]
[Delay(time=2)]
[charslot(slot="m",name="avg_4025_aprot2_1#6$1")]
[name="沉渊"]......
[charslot(slot="m",name="avg_4025_aprot2_1#5$1")]
[name="沉渊"]我还是做不到。
[Dialog]
[charslot]
[playsound(key="$d_avg_clothmovement")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_701_1#1$1",focus="m")]
[name="悲伤的男性"]沉渊，你不该心软。
[name="悲伤的男性"]如果不是我搞砸了我们的计划，其他人也不会死。
[name="悲伤的男性"]现在你还有将功抵过的机会，带我的脑袋回去——
[charslot(slot="m",name="avg_4025_aprot2_1#3$1",focus="m")]
[name="沉渊"]闭嘴！别让我后悔！
[charslot(slot="m",name="avg_npc_701_1#1$1",focus="m")]
[name="悲伤的男性"]......
[charslot(slot="m",name="avg_4025_aprot2_1#4$1",focus="m")]
[name="沉渊"]我不该心软......
[name="沉渊"]......那我该如何？
[name="沉渊"]我应该现在就杀了你，割下你的头，带回领主面前。
[charslot(slot="m",name="avg_4025_aprot2_1#5$1",focus="m")]
[name="沉渊"]然后忍辱负重，等待复仇时机......
[name="沉渊"]不，这不对。
[name="沉渊"]......拿着这个。
[Dialog]
[playsound(key="$d_avg_clothmovement")]
[Delay(time=1.5)]
[charslot(slot="m",name="avg_npc_701_1#1$1",focus="m")]
[name="悲伤的男性"]这是，你的匕首......
[charslot(slot="m",name="avg_4025_aprot2_1#2$1",focus="m")]
[name="沉渊"]给你，你走吧。
[charslot(slot="m",name="avg_npc_701_1#1$1",focus="m")]
[name="悲伤的男性"]可是，沉渊！
[name="悲伤的男性"]放走了我，你要怎么办？
[charslot(slot="m",name="avg_4025_aprot2_1#4$1",focus="m")]
[name="沉渊"]我......
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="bg_black",screenadapt="showall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
你又一次做出了选择。
你已经很清楚自己要怎么做了，不是吗？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Delay(time=2)]
[Background(image="bg_county_1",screenadapt="showall")]
[playMusic(intro="$distressed_intro", key="$distressed_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_npc_005",duration=1.5)]
[Delay(time=2)]
[name="和善的村人"]小伙子，多谢你这几天帮着照看孩子们。
[name="和善的村人"]几个小崽子都说你讲故事讲得好听咧！
[charslot(slot="m",name="avg_4025_aprot2_1#1$1")]
[name="沉渊"]不用谢，老伯。
[name="沉渊"]孩子们都很听话，反而是我们借住在这里，给各位添麻烦了。
[charslot(slot="m",name="avg_npc_005")]
[name="和善的村人"]不麻烦不麻烦。
[name="和善的村人"]哎，那我就不耽搁你们干活了。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(duration=1.5)]
[Delay(time=2.5)]
[charslot(slot="l",name="avg_npc_012",focus="l")]
[charslot(slot="r",name="avg_4025_aprot2_1#1$1",focus="l")]
[name="罗德岛干员"]给小孩讲故事？
[name="罗德岛干员"]看来你和村里人相处得挺不错。
[charslot(slot="r",name="avg_4025_aprot2_1#10$1",focus="r")]
[name="沉渊"]动动嘴而已，也不费什么功夫。
[charslot(slot="l",name="avg_npc_012",focus="l")]
[name="罗德岛干员"]那也是你有这个耐心，我就不太行。
[name="罗德岛干员"]这几天过得太平静了，任务也没出什么意外，我都不太习惯了。
[charslot(slot="r",name="avg_4025_aprot2_1#9$1",focus="r")]
[name="沉渊"]平静一点也很好。
[charslot(slot="r",name="avg_4025_aprot2_1#1$1",focus="r")]
[name="沉渊"]我倒是希望不要出任何意外......
[charslot(slot="l",name="avg_npc_012",focus="l")]
[name="罗德岛干员"]你的理想是隐居嘛。我知道。
[name="罗德岛干员"]对了，沉渊。
[name="罗德岛干员"]我这有件礼物要给你。
[stopmusic(fadetime=1.5)]
[charslot(slot="r",name="avg_4025_aprot2_1#4$1",focus="r")]
[name="沉渊"]礼物？是什么......
[Dialog]
[charslot]
[playsound(key="$bodyfalldown1")]
[Delay(time=2)]
[playMusic(intro="$plot_intro", key="$plot_loop", volume=0.6)]
球形的重物被丢在你的面前。
微微腐烂的东西落在地上，发出沉闷的声响。
“礼物”在地上滚动，最终停在你的脚边。
那双浑浊无光的眼珠与你对视。
[charslot(slot="l",name="avg_npc_012",focus="r")]
[charslot(slot="r",name="avg_4025_aprot2_1#4$1",focus="r")]
[name="沉渊"]——
[charslot(slot="l",name="avg_npc_012",focus="l")]
[name="罗德岛干员"]我把这家伙的武器也一起带回来了。
[name="罗德岛干员"]这原本是你的，对吧？
[charslot(slot="r",name="avg_4025_aprot2_1#4$1",focus="r")]
[name="沉渊"]为......什么......
[charslot(slot="l",name="avg_npc_012",focus="l")]
[name="罗德岛干员"]被你一时心软放走的人。
[name="罗德岛干员"]在你以为自己已经逃离过去的时候，忽然以这种形式出现......
[name="罗德岛干员"]沉渊，你当时不杀掉他是正确的选择。
[charslot(slot="r",name="avg_4025_aprot2_1#5$1",focus="r")]
[name="沉渊"]正确的，选择？
[charslot(slot="l",name="avg_npc_012",focus="l")]
[name="罗德岛干员"]这让这出戏更精彩。
[name="罗德岛干员"]怎么，沉渊，这不正是你为剧团完成的剧本吗？
[charslot(slot="r",name="avg_4025_aprot2_1#5$1",focus="r")]
[name="沉渊"]剧本......？
[charslot(slot="r",name="avg_4025_aprot2_1#3$1",focus="r")]
[name="沉渊"]不，不是的！
[name="沉渊"]我已经和剧团没关系了，我早就逃出来了！
[name="沉渊"]这不是剧本！这怎么会是剧本？！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.8, r=1, g=0, b=0, fadetime=1.5, block=false)]
[CameraShake(duration=2, xstrength=5, ystrength=15, vibrato=20, randomness=50, fadeout=true, block=false)]
[charslot(slot="r",afrom=1,ato=0,duration=1.5)]
[charslot(slot="l",afrom=1,ato=0,duration=1.5)]
[Background(image="bg_indoor_u",screenadapt="showall",fadetime=1.5)]
[charslot(slot="m",name="avg_4025_aprot2_1#5$1",duration=1.5)]
[Delay(time=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
[name="沉渊"]不......
[charslot(slot="m",name="avg_4025_aprot2_1#6$1")]
[name="沉渊"]这是我自己的选择......
[charslot(slot="m",name="avg_npc_701_1#1$1")]
[name="悲伤的男性"]什么选择？
[name="悲伤的男性"]沉渊，你在说什么？
[charslot(slot="m",name="avg_4025_aprot2_1#6$1")]
[name="沉渊"]......这是......我自己的...

... (全文14304字符)
```

### story_archet_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[playMusic(intro="$calm_loop",key="$calm_loop", volume=0.4)]
[Background(image="26_g6_laterano_chapelin",screenadapt="coverall")]
[Delay(time=3)]
我们今天聚集在这里，为了纪念过去，也为了迎接新的开始。
站在我身边的，都是我的兄弟姐妹。我需感谢缘分，我们彼此间的每一段联系，都是修道院给予的无比珍贵的礼物。
我们不会忘记这里的面包与啤酒，钟声与麦田。我们不会忘记学习过的律法，兄弟姐妹的情谊。
我们今天在这里相聚，来见证兰登修道院的落幕。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[delay(time=1)]
[character(name="char_332_archet#2",fadetime=1)]
[delay(time=2)]
[character(name="char_332_archet#4")]
[name="席德佳"]还是，没有办法了吗......
[character(name="avg_npc_369_1#1$1")]
[name="虔诚的修士"]很遗憾，教会已经决定于今年年底正式停止兰登修道院的运营。
[name="虔诚的修士"]修道院已经彻底无力支撑自身的运营，教会决定不再为修道院拨更多的款项。
[name="虔诚的修士"]我们最后能做的事，就是带着敬意在这里见证它的结局。
[character(name="char_332_archet#3")]
[name="席德佳"]能不能再宽限一点时间，修道院的修士们都已经在积极为修道院寻找出路了。
[name="席德佳"]只要再多给我们一些时间，也许还有办法可以扭转修道院财政赤字的局面......
[character(name="avg_npc_369_1#1$1")]
[name="虔诚的修士"]很抱歉我的姐妹，教会已经给了修道院足够长的时间。
[character(name="char_332_archet#3")]
[name="席德佳"]可就算这样，为什么一定要拆除修道院呢？ 
[character(name="char_332_archet#4")]
[name="席德佳"]哪怕是只留下这栋建筑，当作一个纪念也好......
[character(name="avg_npc_369_1#1$1")]
[name="虔诚的修士"]由于常年的运营亏损，兰登修道院不得不出让土地来填补债务。
[name="虔诚的修士"]我们会永远怀念这里的麦田与阳光，但同时也不应该去妨碍这里的土地实现更大的价值。
[character(name="char_332_archet#4")]
[name="席德佳"]如果我可以再努力一些，是不是就能保住这里了......
[character(name="avg_npc_369_1#1$1")]
[name="虔诚的修士"]我的姐妹，对于这样的结局，我和你一样遗憾。但是典籍中的教义也指导我们，对于那些不可改变的结果，我们要学会坦然接受。
[name="虔诚的修士"]就让那些美好的往日时光留存在我们的记忆里，为其他兄弟姐妹的将来送上祝福——
[StopMusic(fadetime=1)]
[Dialog]
[Character(fadetime=0.3)]
[Delay(time=0.5)]
[character(name="avg_103_angel_1#6$1")]
[name="能天使"]那爆破工作就交给我吧！
[playMusic(intro="$relax_intro",key="$relax_loop", volume=0.4)]
[character(name="char_332_archet#3")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="席德佳"]能天使？！为什么？！
[character(name="avg_103_angel_1#6$1")]
[name="能天使"]对于已经失去用处的建筑，当然应该干净利落地处理掉。
[character(name="avg_103_angel_1#10$1")]
[name="能天使"]既然修道院已经不能再正常行使它的职能，那么它最后的价值就只剩下了——完成一场华丽的爆破！
[character(name="char_332_archet#3")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="席德佳"]什么？！
[character(name="char_332_archet#6")]
[name="席德佳"]等一下！就算要拆除修道院，也应该要对它怀有最基本的敬意！怎么可以这么胡闹——
[character(name="avg_103_angel_1#1$1")]
[name="能天使"]都让一让，让一让！
[name="能天使"]废话少说，就让我们用最热烈的派对，为这座有数百年历史的老古董送行吧！
[name="能天使"]三——二——
[character(name="char_332_archet#6")]
[multiline(name="席德佳")] 等——
[CameraShake(duration=1, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[multiline(name="席德佳")] 等一下！
[StopMusic(fadetime=3)]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=3, block=true)]
[character(fadetime=0)]
[Background(image="bg_lungmen_b",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[playMusic(intro="$path_intro",key="$path_loop", volume=0.4)]
[Delay(time=1)]
[character(name="char_332_archet#6",fadetime=0.3)]
[CameraShake(duration=0.3, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="空弦"]等一下！
[Dialog]
[character(name="char_332_archet#3")]
[Delay(time=1)]
[name="空弦"]原来是个梦......还好是个梦啊......
[character(name="char_332_archet#1")]
[name="空弦"]我......这是在......
[character(name="char_332_archet#3")]
[name="空弦"]啊，对了！今天是要举办偶像握手会的......我在偶像握手会上睡着了？！
[Dialog]
[Character]
[character(name="avg_npc_022",fadetime=0.5)]
[Delay(time=1)]
[name="经纪人"]倒也不用担心，在你睡着的半小时里，还没有一个人光临过哦。
[character(name="char_332_archet#1")]
[name="空弦"]这样啊，还好......
[character(name="char_332_archet#1",name2="avg_npc_022",focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="经纪人"]一点也不好！
[name="经纪人"]今天的专辑签售会从早上开始到现在，我们连一张专辑都没有卖出去过！
[name="经纪人"]明明别家偶像的展位前都是人满为患，就算考虑到你出道以来一直没什么人气，今天这样的情况也过于惨淡了点。
[character(name="char_332_archet#2",name2="avg_npc_022",focus=1)]
[name="空弦"]十分抱歉，我不该懈怠的......
[character(name="char_332_archet#2",name2="avg_npc_022",focus=2)]
[name="经纪人"]唉，倒也不是指责你的意思，毕竟这段时间空弦小姐的努力我也是看在眼里的。
[name="经纪人"]可是想要成为一名人气偶像，需要的是话题讨论度和第一时间抓住观众的人设，而在这些事上只有努力是远远不够的！
[name="经纪人"]虽说在一开始同意你用修道院修士人设出道的我也有责任就是了，下次打造偶像人设的时候还是应该多考虑一下本土化的问题啊......
[character(name="char_332_archet#1",name2="avg_npc_022",focus=1)]
[name="空弦"]我只是保持自己原本的样子，这也算是一种人设吗......
[name="空弦"]（而且如果不能用这种形象宣传修道院的话，当偶像也毫无意义了呀......）
[character(name="char_332_archet#1",name2="avg_npc_022",focus=2)]
[name="经纪人"]总而言之，从公司运营的角度来讲，空弦小姐，你的偶像生涯已经是岌岌可危的状态了。
[name="经纪人"]今天的偶像握手会暨专辑签售会就是我们最后的机会了，如果再不能把这些积压的专辑处理掉，我们俩就一起做好被公司解约的准备吧。
[character(name="char_332_archet#4",name2="avg_npc_022",focus=1)]
[name="空弦"]虽然不知道还能有什么办法......我会努力加油的！
[Dialog]
[character(name="char_332_archet#4",name2="avg_npc_022",focus=2)]
[Delay(time=1)]
[name="经纪人"]哎，看那边，好像有一个人向这边走来了！
[name="经纪人"]快做好准备，说不定这就是今天的第一个客户！
[character(name="char_332_archet#2")]
[name="空弦"]咳咳......
[character(name="char_332_archet#5")]
[name="空弦"]（熟练而流畅地背诵）
[name="空弦"]“钟声奏鸣爱的旋律，让我们因美好的缘分在这里相遇！”
[name="空弦"]欢迎参加见面会，虔诚的修士今天也与您一同聆听爱与希望的声音！
[name="空弦"]现在购入《爱的钟声奏鸣曲》专辑，还会获赠兰登修道院瘤奶面包大礼盒一份哦！
[Dialog]
[characteraction(name="middle", type="move", ypos=-30, fadetime=0.5, block=false)]
[Delay(time=0.8)]
[characteraction(name="middle", type="move", ypos=30, fadetime=0.3, block=false)]
[name="空弦"]（摆出活力而不失端庄的造型）
[character(name="avg_npc_033")]
[name="激动的粉丝"]您......您就是那位大名鼎鼎的——！
[name="激动的粉丝"]我真是太幸运了！没想到能在这里见到您！
[character(name="char_332_archet#2")]
[name="空弦"]谢谢您的支持，可是“大名鼎鼎”也谈不上了啦......
[character(name="avg_npc_033")]
[name="激动的粉丝"]我经常在广播里听到您的歌，也买了许多您的专辑。
[name="激动的粉丝"]虽然是第一次见到您，但是您闪闪发光的样子真是和我想象中的一模一样！
[character(name="char_332_archet#4")]
[name="空弦"]（这就是偶像受人追捧的感觉吗......冷静，冷静一下，注意偶像的姿态！）
[character(name="char_332_archet#5")]
[name="空弦"]（开朗而不失优雅的笑容）
[name="空弦"]谢谢您的喜爱，今后我会用更美好的歌声来回应大家的喜爱。
[name="空弦"]“懂得欣赏他人的人，自己也一定是智慧且善良的人”，愿好运眷顾着您。
[character(name="avg_npc_033")]
[name="激动的粉丝"]您说话真好听！和唱片里的歌声一样好听！
[name="激动的粉丝"]今天能见到您，我实在是太幸

... (全文21807字符)
```

### story_ardign_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_iceforest_1",screenadapt="coverall",fadetime=0.6)]
[playMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="char_209_ardign")]
[PlaySound(key="$runsand", volume=1)]
[name="梅莉"]哈、哈......
[name="梅莉"]快一点，必须再快一点......
[name="梅莉"]哇啊——
[PlaySound(key="$bodyfalldown1", volume=1)]
[characteraction(name="middle", type="move", ypos=-300, fadetime=0.5,block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[dialog]
[character(fadetime=0.5)]
[delay(time=2)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[Character(name="char_209_ardign",enter="down",fadetime=2)]
[PlaySound(key="$bodyfalldown2", volume=1)]
[delay(time=1)]
[name="梅莉"]咳、咳咳......好痛......
[name="梅莉"]糟了！滑雪板......还能用。好，拜托了，再坚持一下，山下有最近的租车行，只要到了那里......
[name="梅莉"]必、必须快一点......来不及了......
[name="梅莉"]安德切尔，史都华德......再等我一会......！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_snowconutry_2",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$drift_intro", key="$drift_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="char_209_ardign")]
[PlaySound(key="$doorknockquite", volume=1)]
[name="梅莉"]不好意思，请问有人在吗！
[name="梅莉"]我需要用车，请问有人在吗——
[dialog]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[Character(name="char_209_ardign",focus=-1)]
[name="载具出租商人"]......*莱塔尼亚俗话*，吵死了，天都还没亮，谁在敲门啊！
[PlaySound(key="$sheildimpact", volume=1)]
[Character(name="char_209_ardign")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="梅莉"]呃、我的额头——
[dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_006", name2="char_209_ardign",fadetime=0.5)]
[delay(time=0.51)]
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]......小姑娘？你没事吧。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]我、我没事，这里是租车行吧？对不起打扰您睡觉了，但我必须要一辆马上能够进入城区的车！
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]你也不看看时间，这才早上五点......你急着赶路？回到城区还要三、四个小时呢。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]咳，我......我遇到了紧急情况必须现在上路，麻烦先生您快点租给我吧！我真非常、非常需要——
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]*莱塔尼亚俗话*，什么事能有我睡觉重要？
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]我......我的朋友有生命危险，我是去城区找医生的。
[name="梅莉"]他们在北边的山区遇险受了伤，只在聚落接受了最简单的治疗......必须寻找更好的救助组织。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]你是说，你一直从北边赶路过来的？
[name="载具出租商人"]......大半夜的，从那个山区跨过来？这暴雪现在都还没停......
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]我没有别的办法、咳咳......他们实在伤得太重了，没法移动，聚落里没有好的医疗设备和药......
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]摔着还是冻着了？这种事熬到救援队来就行，干嘛非要你跨过山区来找人。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]不是的，普通的急救医生不行......还要找到能够治疗的药......
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]*莱塔尼亚俗话*，真麻烦，话也不说清楚，我怎么敢现在就把车借给你。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]拜托您了，先生，我不能失去我的朋友......只要有一线希望，我一定要去城里找到能治好他们的医生！咳咳......咳......
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]......啧，你这一路赶来也够呛。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]我，我不要紧......
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]算了，人命要紧，跟我来吧。但是小姑娘，算我多嘴，提醒你一句......你可别想得太好，真去了城里也未必能请来医生。
[name="载具出租商人"]城里那些拿着高额薪水的医生可不会愿意冒着这暴雪的危险来治疗。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]我在老家当过雪橇巡逻队队员，借到车我就可以拉医生走了！还有，我、我有一些储蓄，都给医生也没关系，只要能救我的朋友——
[name="梅莉"]我相信一定会有好心的医生愿意出诊。我会找到他们，拜托他们回来，必须要治好我的朋友们。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]......哼。你倒是很义气。
[name="载具出租商人"]但愿你能找到医生吧。行了，车给你，一天起租，定金和证件准备好了吗？
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]抱歉先生，我没想到会遇上这种事，随身带着的钱不多，定金......您看这些够吗？
[name="梅莉"]如果不够的话，我还有、还有这条项链，是我最喜欢的生日礼物，应该能值一点钱......！嗯，呃，还有，我找找......
[Character(name="avg_npc_006", name2="char_209_ardign",focus=1)]
[name="载具出租商人"]......罢了，那破项链你就自己留着吧。车借你，等你回来的时候，我需要自己的车完好无损。
[Character(name="avg_npc_006", name2="char_209_ardign",focus=2)]
[name="梅莉"]......！
[name="梅莉"]谢谢您，先生，我一定会及时回来的！我，我的滑雪板也暂时抵押在您这里，等我找到医生，进山前我一定来取！
[Dialog]
[PlaySound(key="$runsand", volume=1)]
[characteraction(name="right", type="move", xpos=300, fadetime=2,block=false)]
[character(name="avg_npc_006",name2="char_empty",fadetime=0.5)]
[delay(time=2)]
[name="载具出租商人"]......唉，不知道说这小姑娘太单纯还是莽撞。
[name="载具出租商人"]这滑雪板都坏成这样了，哪还有什么抵押价值。
[name="载具出租商人"]罢了，看她那样子，确实是赶着要救人命的......就当做点好事。
[name="载具出租商人"]不过......
[Dialog]
[PlaySound(key="$blizzard", volume=1, delay=0.4, loop=true, channel="bgs")]
[delay(time=1)]
[name="载具出租商人"]嘶，这么冷的天，没有丁点光，还是从最危险的山区横穿而来......她是怎么做到的？
[name="载具出租商人"]到底是得的什么病，还专门得从城区找医生来？如果是受伤出血、受冻都应该有更好的解决办法。
[name="载具出租商人"]......总不能是矿石病那种危险程度吧？
[name="载具出租商人"]哈，那不是白费功夫嘛，谁会在这鬼天气里去救已经死定了的家伙？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_snowconutry_2",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[Character(name="char_209_ardign",fadetime=0.5)]
[name="梅莉"]（好，出发了。）
[name="梅莉"]（雪又大了，但这算什么，这点阻碍休想让我停下！）
[name="梅莉"]（我一定要......）
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=

... (全文20355字符)
```

### story_aroma_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_room_2",screenadapt="coverall")]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[charslot(slot = "m", name = "avg_npc_972_1#1$1", duration=0.5, isblock=true)]
[name="人事部干员"]阿罗玛小姐，这是您试用期考核通过的通知。
[name="人事部干员"]考核评估科提供的人事任用申请记录显示，基于您在试用期的优异表现，有其他部门向您发起了邀请。
[name="人事部干员"]不过，要加入哪个部门，选择权还是在您手中。
[charslot(slot = "m", name = "avg_446_aroma_1#3$1")]
[name="阿罗玛"]我......
[name="阿罗玛"]请问，最后的期限是？
[charslot(slot = "m", name = "avg_npc_972_1#1$1")]
[name="人事部干员"]只要在本周结束前告诉我您的决定就行。
[name="人事部干员"]希望您慎重作出选择。
[charslot(slot = "m", name = "avg_446_aroma_1#7$1")]
[name="阿罗玛"]......好。
[name="阿罗玛"]我会好好考虑的，谢谢。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_corridor",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[name="罗德岛干员A"]橡皮，怎么回事啊，洗衣间又要维修？
[charslot(slot = "m", name = "avg_npc_973_1#1$1")]
[name="橡皮"]不好意思！洗衣机出了点故障，很抱歉给大家造成困扰了。
[name="橡皮"]后勤部会联合工程部一起尽快维修，洗衣间再次开放的时间，我们将会另行通知！
[charslot]
[name="罗德岛干员A"]我都排了这么久的队了......
[name="罗德岛干员B"]算了算了，这也是没办法的事，我们就先回去吧。
[charslot(slot = "m", name = "avg_npc_973_1#1$1")]
[name="橡皮"]对不起，我们会尽快......
[dialog]
[charslot(slot = "m", focus="n")]
[PlaySound(key="$d_gen_walk_n", volume=0.3, channel="1")]
[Delay(time=0.3)]
[PlaySound(key="$d_gen_walk_n", volume=0.5, channel="2")]
[Delay(time=2)]
[charslot(slot = "m", name = "avg_npc_973_1#1$1")]
[name="橡皮"]唉......
[name="橡皮"]已经这个时候了，阿罗玛怎么还没来？
[name="橡皮"]没有她来帮忙清洗这些衣服，我可真不知道该怎么办了......
[name="橡皮"]......不过，要是阿罗玛知道有这么多加急的洗衣预约单等着她，一定会头疼吧？
[name="橡皮"]......
[name="橡皮"]不管了，正事要紧，还是先去宿舍找找她吧......
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_rhodesroom",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$pourwater", volume=1)]
[Delay(time=1.5)]
[name="工程干员"]感觉水温怎么样？
[dialog]
[charslot(slot = "m", name = "avg_446_aroma_1#1$1", duration=1, isblock=true)]
[name="阿罗玛"]再热一点也没问题。
[charslot(slot = "m", focus="n")]
[name="工程干员"]力度如何？
[charslot(slot = "m", name = "avg_446_aroma_1#1$1")]
[name="阿罗玛"]嗯......挺好的，很舒服。
[charslot(slot = "m", name = "avg_446_aroma_1#4$1")]
[name="阿罗玛"]可以再往上面一点吗？对，请帮我抓一抓这里。
[dialog]
[charslot(duration=0.5, isblock=true)]
[name="工程干员"]好的，刷头会保持在这个位置。
[name="工程干员"]如果有任何不舒服的地方，可以随时叫我哦。
[charslot(slot = "l", name = "avg_446_aroma_1#4$1")]
[name="阿罗玛"]哦，好......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "r", name = "avg_484_robrta_1#9$1", posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[delay(time=0.5)]
[charslot(slot = "r", name = "avg_484_robrta_1#9$1", focus="r")]
[name="罗比菈塔"]阿罗玛，这台尾巴美容水疗仪不错吧？这可是工程部研发的最新产品哦。
[charslot(slot = "l", name = "avg_446_aroma_1#7$1", focus="l")]
[name="阿罗玛"]我觉得很有帮助。
[name="阿罗玛"]不过，体验这台水疗仪就是今天课程讲座的全部内容吗？
[charslot(slot = "r", name = "avg_484_robrta_1#2$1", focus="r")]
[name="罗比菈塔"]体验很重要啊。既然产品要为人服务，那了解用户体验当然是非常重要的！
[charslot(slot = "l", name = "avg_446_aroma_1#7$1", focus="l")]
[name="阿罗玛"]哦......
[charslot(slot = "r", name = "avg_484_robrta_1#9$1", focus="r")]
[name="罗比菈塔"]当然，这只是课程中的一部分啦。
[name="罗比菈塔"]阿罗玛，你在后勤部每天都那么忙，一定很辛苦吧？
[charslot(slot = "r", name = "avg_484_robrta_1#10$1", focus="r")]
[name="罗比菈塔"]即使在课程结束后，只要你有空，随时可以来放松放松哦！
[charslot(slot = "l", name = "avg_446_aroma_1#1$1", focus="l")]
[name="阿罗玛"]欸？真的可以吗？
[charslot(slot = "l", name = "avg_446_aroma_1#4$1", focus="l")]
[name="阿罗玛"]那我就趁午休多待一会儿吧，下午还有好多事情要做呢。
[charslot(slot = "r", name = "avg_484_robrta_1#9$1", focus="r")]
[name="罗比菈塔"]欢迎，如果能多提一些建议就更好啦。
[name="罗比菈塔"]为了给大家提供更好的美容造型服务，这都是工程部必要的调研工作。
[charslot(slot = "l", name = "avg_446_aroma_1#7$1", focus="l")]
[name="阿罗玛"]......
[charslot(slot = "l", name = "avg_446_aroma_1#1$1", focus="l")]
[name="阿罗玛"]对了，我记得化妆和美容造型，应该都属于后勤部的工作范畴吧。
[name="阿罗玛"]罗比菈塔小姐当初正式入职罗德岛时，为什么会选择加入工程部呢？
[dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_room_2",screenadapt="coverall")]
[Delay(time=1)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[PlaySound(key="$dooropenquite", volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_npc_973_1#1$1" , posfrom="200,0", posto="0,0", duration=1.5, isblock=true)]
[name="橡皮"]阿罗玛——
[name="橡皮"]......也不在宿舍......奇怪，她到底去哪儿了？
[name="橡皮"]嗯？桌上有一本《毛发护理与保养技术》......
[dialog]
[playsound(key="$d_avg_paper1",volume=1)]
[delay(time=0.5)]
[playsound(key="$d_avg_paper2",volume=1)]
[delay(time=1)]
[name="橡皮"]批注笔记做得好详细，原来阿罗玛最近在学习这些知识......
[name="橡皮"]欸，有东西从书里掉出来了......这是工程部的课程讲座通知？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=50, randomness=70, fadeout=true, block=false)]
[name="橡皮"]等等，工程部？！
[name="橡皮"]我记得阿罗玛的试用期就快要结束了......
[name="橡皮"]该不会......阿罗玛她不想留在后勤部了吧？
[dialog]
[charslot]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "m", name = "avg_385_finlpp_1#10$1", duration=1.5, isblock=true)]
[name="清流"]橡皮前辈，请问小阿罗玛在吗？
[charslot(slot = "m", name = "avg_npc_973_1#1$1")]
[name="橡皮"]是清流啊，什么事？
[charslot(slot = "m", name = "avg_385_finlpp_1#10$1")]
[name="清流"]今天大浴场要做例行清洁，我来问问小阿罗玛有没有空！
[charslot(slot = "m", name = "avg_npc_973_1#1$1")]
[name="橡皮"]大浴场？为什么要阿罗玛去？大浴场应该有别的清洁负责人吧？
[charslot(slot = "m", name = "avg_385_finlpp_1#4$1")]
[name="清流"]欸？其、其实就是我......
[dialog]
[Blocker(a=1, r=0, g=0, b=0, style = "slider", inverse = true, fadetime=2, block=true)]
[charslot]
[charslot(slot = "r", name = "avg_np

... (全文24490字符)
```

### story_asbest_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="bg_village",screenadapt="coverall")]
[playMusic(intro="$farce_intro", key="$farce_loop",fadetime=3, volume=0.4,delay=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=3, block=true)]
[Character(name="avg_npc_075",fadetime=0.5)]
[Delay(time=0.6)]
[name="依娜姆"]  就是这里啦，嘉维尔和我说过了，你也是罗德岛上的。
[name="依娜姆"]  我的手下们都是做生意的，我给他们多多少少都教了点萨尔贡语，你要是有什么想要的，跟他们买就好。
[Character(name="avg_378_asbest_1#1$1")]
[name="石棉"]  好。但那人怎么一直盯着我看？
[Character(name="avg_npc_075")]
[name="依娜姆"]  我们这里很少有人来，他们看到外乡人还是挺开心的！
[name="依娜姆"]  起码我挺开心的！
[dialog]
[character]
[Character(name="avg_npc_072",name2="avg_npc_073", fadetime=1)]
[Delay(time=1.5)]
[Character(name="avg_npc_072",name2="avg_npc_073", focus=1)]
[name="害羞的阿达克利斯人"] 瞧她的尾巴！
[Character(name="avg_npc_072",name2="avg_npc_073",focus=2)]
[name="直爽的阿达克利斯人"] 她的尾巴看起来好柔软......肉肉的但又很细长......尾巴尖好灵活......上面还有橘色的花纹？
[Characteraction(name="right", type="jump",  power=20, times=1, fadetime=0.5, block=true)]
[name="直爽的阿达克利斯人"] 看到了吗？她用尾巴提起了那么大一包东西？！还有那个门板，看起来也好重，她一只手就拿起来了？哇——
[name="直爽的阿达克利斯人"] 她摔跤一定很厉害，她看起来一尾巴就能扫断一棵树，她、她......好美啊！
[name="直爽的阿达克利斯人"] 我从来没见过这样的人，我要和她做朋友！
[Dialog]
[Character(name="avg_npc_072",name2="avg_npc_073")]
[Characteraction(name="right", type="move", xpos=200, fadetime=1, block=true)]
[Character(name="avg_npc_072", name2="char_empty")]
[delay(time=0.6)]
[Characteraction(name="left", type="jump", xpos=20, power=30, times=1, fadetime=0.3,block=false)]
[name="害羞的阿达克利斯人"]  等、等一下，就这样上去吗，我、我还有点，不好意思——啊——
[Characteraction(name="left", type="move", xpos=1000,fadetime=1.5,block=false)]
[Dialog]
[Character(fadetime=0.51)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Character(name="avg_npc_070",fadetime=0.5)]
[Delay(time=1)]
[playsound(key="$d_avg_axehitscrape")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[playsound(key="$d_avg_axehitscrape")]
[name="快乐的阿达克利斯人"]  磐蟹护甲，磐蟹护腿！坚硬的外壳可以抵挡一切攻击！
[Character(name="avg_npc_071")]
[playsound(key="$swordtsing1", volume=0.3)]
[playsound(key="$swordtsing2", volume=0.3,delay=0.5)]
[name="认真的阿达克利斯人"] 锯齿鳞牙锤，锯齿鳞骨刀！锋利的齿刃可以破开一切物品！
[Character(name="avg_378_asbest_1#1$1")]
[name="石棉"]  ......
[Character(name="avg_npc_072")]
[name="害羞的阿达克利斯人"]  （过来了过来了......！）
[Dialog]
[character]
[Character(name="avg_378_asbest_1#1$1",fadetime=1)]
[PlaySound(key="$d_gen_walk_n")]
[Delay(time=2)]
[Character(name="avg_npc_073")]
[name="直爽的阿达克利斯人"] 呃呃——你好？
[Character(name="avg_378_asbest_1#1$1")]
[name="石棉"]  怎么了？
[Character(name="avg_npc_073")]
[name="直爽的阿达克利斯人"] 啊！我、我喜欢你的尾巴！
[Character(name="avg_378_asbest_1#7$1")]
[name="石棉"]  ？
[name="石棉"]  我的尾巴？你在说啥？
[Character(name="avg_378_asbest_1#4$1")]
[name="石棉"]  ......姑奶奶忙得很，别挡道！
[Character(name="avg_npc_072")]
[name="害羞的阿达克利斯人"]  （呜！好可怕......）
[Character(name="avg_npc_073")]
[name="直爽的阿达克利斯人"] 啊、等一下！
[name="直爽的阿达克利斯人"] 你好凶啊，我说我喜欢你哎？
[name="直爽的阿达克利斯人"] 你应该对我也表示一下才行呀，你不觉得我的尾巴也很好看吗？很多人都夸我长了一条很帅气的尾巴呢！
[Character(name="avg_378_asbest_1#4$1")]
[name="石棉"]  哈？你在说什么啊？
[name="石棉"]  自己找点事去做，拉着你的朋友玩泥巴吧。
[Character(name="avg_npc_072")]
[name="害羞的阿达克利斯人"]  你会说我们这里的话哎？但怎么都是脏话啊......
[Character(name="avg_npc_073")]
[name="直爽的阿达克利斯人"] 我不玩泥巴！你小看我是不是，我已经不是孩子了！
[character]
[Dialog]
[Character(name="char_empty",name2="avg_378_asbest_1#1$1")]
[Character(name="avg_npc_073",name2="avg_378_asbest_1#1$1")]
[playsound(key="$runsand", loop=true, channel="bgs")]
[characteraction(name="left", type="move", xpos=-200, fadetime=0, block=true)]
[characteraction(name="left", type="move", xpos=150, fadetime=1.3, block=true)]
[delay(time=0.6)]
[StopSound(channel="bgs", fadetime=0)]
[Character(name="avg_npc_073",name2="avg_378_asbest_1#1$1",focus=1)]
[name="直爽的阿达克利斯人"] ......我们打一架！
[Character(name="avg_npc_073",name2="avg_378_asbest_1#7$1",focus=2)]
[name="石棉"]  啧，你这人怎么回事？
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1")]
[characteraction(name="right", type="move", xpos=-30, fadetime=1, block=true)]
[Character(name="avg_npc_073",name2="avg_378_asbest_1#7$1",focus=2)]
[delay(time=0.5)]
[name="石棉"]  把路让开！
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1")]
[Characteraction(name="left", type="jump", xpos=100, power=16, times=2, fadetime=0.8, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$fightgeneral", volume=0.3)]
[Characteraction(name="right", type="jump", xpos=50, power=15, times=2, fadetime=0.5, block=true)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1",focus=2)]
[name="石棉"]  喂，你想死啊！
[name="石棉"]  你很美行了吧？你尾巴好看！特别美！
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1")]
[Characteraction(name="left", type="jump", xpos=80, power=16, times=2, fadetime=0.5, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$fightgeneral", volume=0.3)]
[Characteraction(name="right", type="jump", xpos=50, power=15, times=2, fadetime=1, block=true)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1",focus=2)]
[name="石棉"]  哈？没完没了的！来劲了是吧！
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1")]
[characteraction(name="right", type="jump", xpos=-150, power=17, times=3, fadetime=0.8, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[playsound(key="$fightgeneral", volume=0.3)]
[characteraction(name="left", type="jump", xpos=-200, power=15, times=2, fadetime=1,block=true)]
[dialog]
[Delay(time=0.6)]
[Character(name="avg_npc_073",name2="avg_378_asbest_1#4$1")]
[Characteraction(name="left", type="jump", xpos=80, power=16, times=2, fadetime=0.5, block=true)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, rando

... (全文27409字符)
```

### story_ascln_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="49_g4_kazdelstreet_shabby",screenadapt="coverall")]
[Delay(time=1)]
[playMusic(intro="$ponder_intro",key="$ponder_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
1072年秋
[Dialog]
[Delay(time=0.5)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",duration = 1.5,posfrom = "-200,0", posto = "0,0")]
[Delay(time=2.5)]
[PlaySound(key="$d_avg_wind", volume=1)]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[charslot]
[Background(image="bg_black",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=true)]
[PlaySound(key="$d_avg_bldwhoosh")]
[charslot(slot = "left", name = "avg_npc_1301_1#4$1",posfrom = "50,0", posto = "250,0",duration = 0.3)]
[Delay(time=0.1)]
[charslot(duration=0.3)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.3, block=true)]
[charslot]
[Blocker(a=1, r=1, g=1, b=1, fadetime=0.01, block=true)]
[CameraShake(duration=0.2, xstrength=30, ystrength=30, vibrato=50, randomness=90, fadeout=false, block=false)]
[PlaySound(key="$swordtsing4")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.3, block=false)]
[Background(image="49_g4_kazdelstreet_shabby",screenadapt="coverall")]
[PlaySound(key="$d_avg_swordy")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
刺客从阴影中跃出，一柄断剑几乎是贴着特雷西斯的前胸掠过。他侧身，出手，佩剑已经横在了刺客的脖颈上。
[Dialog]
[charslot(slot = "left", name = "avg_npc_1301_1#1$1",duration = 1)]
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "left", name = "avg_npc_1301_1#1$1",focus="l")]
[name="阿斯卡纶"]......
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]日影刚好在此时完全倾斜过来，将街道遮住。
[name="特雷西斯"]......你一直在等待这一刻。
[name="特雷西斯"]这样确实能最大化发挥你的优势，隐藏身形，接近敌人。但在昼夜交替的特殊时刻，你的敌人对环境变化的感知也会更敏感。
[charslot(slot = "left", name = "avg_npc_1301_1#1$1",focus="l")]
[name="阿斯卡纶"]好，知道了。
[name="阿斯卡纶"]整个下午，我一共出手了七次，但一次都没能得手。
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]换一个对手，你早就成功了。
[charslot(slot = "right", name = "avg_npc_1297_1#3$1",focus="r")]
[name="特雷西斯"]你割断了我胸前的绑带......用这柄曾经被我斩断的长剑。
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]今天就到这里，明天继续。
[charslot(slot = "left", name = "avg_npc_1301_1#3$1",focus="l")]
[name="阿斯卡纶"]......
[charslot(slot = "left", name = "avg_npc_1301_1#1$1",focus="l")]
[name="阿斯卡纶"]昨天，两个喝醉的佣兵闯进了我们的办公地点，他们扔下了一个酒壶，里面是活性化的源石粉尘。
[name="阿斯卡纶"]当时，殿下正在大厅给两个孩子包扎伤口。
[name="阿斯卡纶"]那不是意外。
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]我已经知道，我已经处理。
[charslot(slot = "left", name = "avg_npc_1301_1#4$1",focus="l")]
[name="阿斯卡纶"]类似的事情，越来越多。
[name="阿斯卡纶"]军事委员会......你保护不了殿下和巴别塔？你是真的没有办法，还是在纵容他们？
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]这件事，不需要你来质问我，阿斯卡纶。
[name="特雷西斯"]什么对萨卡兹更好，我比你更清楚。
[charslot(slot = "left", name = "avg_npc_1301_1#4$1",focus="l")]
[name="阿斯卡纶"]可是，老师......
[charslot(slot = "left", name = "avg_npc_1301_1#5$1",focus="l")]
[name="阿斯卡纶"]如果真有人对殿下动手，你会出手吗！
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]会。
[charslot(slot = "left", name = "avg_npc_1301_1#5$1",focus="l")]
[name="阿斯卡纶"]那如果其他人都架着你，逼你对她动手，你会出手吗？
[charslot(slot = "m", focus = "n")]
沉默。
但两人的心中各自都有了答案。
[charslot(slot = "left", name = "avg_npc_1301_1#2$1",focus="l")]
[name="阿斯卡纶"]这是最后一堂课了，老师。
[charslot(slot = "left", name = "avg_npc_1301_1#3$1",focus="l")]
[name="阿斯卡纶"]我没有想通......但从明天起，我会去殿下身边，守护好她。
[charslot(slot = "left", name = "avg_npc_1301_1#1$1",focus="l")]
[name="阿斯卡纶"]连带着你本应有的心意一起。
[Dialog]
[charslot(slot = "m", focus = "n")]
阿斯卡纶不再言语，她弯腰捡起刚刚被特雷西斯打落的断剑，以及散落在一旁，被她视作战利品的断裂绑带。
她头也不回地离开。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[charslot(slot = "l",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[Delay(time=2)]
[charslot(slot = "right", name = "avg_npc_1297_1#1$1",focus="r")]
[name="特雷西斯"]......
[name="特雷西斯"]你选择的只是某个人，而不是那个人脚下的道路。
[name="特雷西斯"]不知道为何而行，那么你要如何承受失去同行人的痛苦，阿斯卡纶？
[stopmusic(fadetime=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="bg_coldforest",screenadapt="coverall")]
[playMusic(intro="$loading_intro",key="$loading_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
1094年秋
卡兹戴尔北部地区
[Dialog]
[charslot(slot="m",name="avg_npc_1308_1#1$1",duration=1)]
[delay(time=1)]
[playsound(key="$d_gen_transmissionget")]
[delay(time=1.5)]
[name="巴别塔成员"]炸药已经填放好。接下来我就守在这里......
[name="巴别塔成员"]土方子、早霜，船上还有好几个跟我一样熟悉航路的人，要是发现异样，他们会在第一时间让罗德岛转向。
[name="巴别塔成员"]只剩下一个小时了，我得守在这里，保证炸药能在罗德岛经过这片区域的时候被触发——
[charslot(slot = "m", focus = "n")]
[name="？？？"]你放在外围的人都已经死了，细盐。
[Dialog]
[charslot(slot="m",name="avg_npc_1308_1#1$1")]
[playsound(key="$transmission")]
[delay(time=1.5)]
[name="细盐"]阿斯卡纶......
[name="细盐"]哈，还是被你找到了。
[Dialog]
[charslot]
[playsound(key="$d_gen_walk_n")]
[charslot(slot="m",name="avg_4132_ascln_1#1$1",duration=1)]
[delay(time=2)]
[name="阿斯卡纶"]......
[charslot(slot="m",name="avg_npc_1308_1#1$1")]
[name="细盐"]也是，我的武艺和潜行的技术都是你教的，指望躲过你，不现实。
[name="细盐"]说起来，以前我就好奇，不管藏得多么好，都能被你找到，你到底是靠什么精准定位到每个人的？
[name="细盐"]味道？声音？
[name="细盐"]......总不能是靠哈出来的气吧，这在你看来也是某种“烟”？
[charslot(slot="m",name="avg_4132_ascln_1#3$1")]
[name="阿斯卡纶"]......
[charslot(slot="m",name="avg_npc_1308_1#1$1")]
[name="细盐"]*萨卡兹粗口*，还真是！
[name="细盐"]那就没办法了，我总不能不呼吸。
[name="细盐"]既然都被你发现了，介意我生堆火吗？入秋了，这荒郊野岭的，冷得很！
[Dialog]
[charslot]
[playsound(key="$d_avg_woodcracle")]
[delay(time=2)]
萨卡兹生起了火，风有点大，他用剑拨了拨火堆，火势才起来，哔剥声变大了，声音远远地传开去。
阿斯卡纶没有动。
[charslot(slot="m",name="avg_4132_ascln_1#1$1")]
[name="阿斯卡纶"]这些烈性源石炸药，制作得很粗糙......
[charslot(slot="m",name="avg_npc_1308_1#1$1")]
[name="细盐"]情报到手得有点迟，做得太仓促了。
[name="细盐"]当年离开卡兹戴尔的时候，我万万没想到，先是需要跟你学潜行和动刀子，后来又得学做炸药，和这些我最讨厌的石头打交道。
[name="细盐"]说真的，这比把野生盐泉旁边的那些粗盐粒提炼成可以吃的细盐可难多了。
[name="细盐"]说起来，当时缺帽檐“细盐”“细盐”地叫我的时候，就应该直接给他一拳让他闭嘴。
[name="细盐"]这个代号

... (全文13906字符)
```

### story_ash_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
“Lord，希望你在乌萨斯过得愉快。”
“我已经到达了哥伦比亚，这里是个很有意思的地方。是的，很有意思，我只能这么形容。”
“不知为何，最近我频频想起一个问题。我们都曾听过，或是思考过一个问题。许多事物的价值和存在意义或许都能追究于此。”
“我们所熟悉的那段历史，究竟是从天扔下的一枚骰子，还是有某种必然性？”
“如果将时间调到亿万年前，让生命重新演化一次，我们所处的世界又会是一副怎样的模样？”
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_cave_2",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[name="莱塔尼亚工人"]他们好像离开了。
[name="乌萨斯村民"]你怎么知道？
[Dialog]
[playsound(key="$d_avg_clothmovement",volume=1)]
[charslot(slot="l",name="avg_npc_068",posfrom="-150,0",posto="-150,0",duration=1.5)]
[charslot(slot="m",name="avg_npc_004",duration=1.5)]
[charslot(slot="r",name="avg_npc_081",posfrom="150,0",posto="150,0",duration=1.5)]
[Delay(time=2)]
[charslot(slot="l",focus="l")]
[name="莱塔尼亚工人"]脚步声。
[name="莱塔尼亚工人"]之前在山洞口至少会有一个人的脚步声，现在那儿一片安静。一定发生了什么。
[name="莱塔尼亚工人"]我们被关在这里几天了？
[charslot(slot="m",focus="m")]
[name="卡西米尔女孩"]我记得，大概是第三天......
[name="卡西米尔女孩"]看那边，有一个水洼。太阳落山的时候，会有一点点阳光透进来。
[charslot(slot="l",focus="l")]
[name="莱塔尼亚工人"]三天了，大部队可能已经离开了。我们还要在这里等到什么时候？
[name="莱塔尼亚工人"]我受够了，我现在就要出去。
[name="莱塔尼亚工人"]我身后的石头可以磨断绳子，我们一起走吧。
[charslot(slot="r",focus="r")]
[name="乌萨斯村民"]冷静点，这伙劫匪至少有十个人，而且都有武器。我们连他们为什么要绑架我们都不知道——
[charslot(slot="l",focus="l")]
[name="莱塔尼亚工人"]至少他们没有立刻杀了我们，这就是我们的机会。
[charslot(slot="m",focus="m")]
[name="卡西米尔女孩"]或许我们应该再等等，万一激怒了他们......
[charslot(slot="l",focus="l")]
[name="莱塔尼亚工人"]如果你们愿意在这里等死的话就留在这吧。
[name="莱塔尼亚工人"]我要走了，哥伦比亚近在眼前，就算死，我也不要死在这里！
[Dialog]
[charslot]
[CameraShake(duration=1.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",channel="1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$a_bat_buildingshaking_2",channel="2")]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=3.5)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="char_456_ash_1#1",duration=1.5)]
[delay(time=2)]
[name="灰烬"]各位，你们看起来需要帮助？
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
“我们来到这个光怪陆离的世界已经有一段时间了。然而时至今日，我仍然不能说自己已经适应了这里的生活。我想你们也是一样。”
“可是当你试着忽视那些违背常识的生物，对于这个世界，你会找到一种超乎想象的熟悉感。”
“这么说或许很奇怪，但没错，我的确是这样觉得的。”
“我们应该试着去理解它。”
[Dialog]
[Background(image="bg_desert_1",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[PlaySound(key="$d_gen_walk_n")]
[charslot(slot="m",name="char_456_ash_1#1",duration=1.5)]
[delay(time=2)]
[name="灰烬"]从篝火痕迹判断，你们说的“大部队”大概在三天前就已经离开了。不巧的是，我的车子也在偶遇你们的前一天抛了锚。
[name="灰烬"]看来我们的运气的确不太好，应该是追不上他们了。
[charslot(slot="m",name="avg_npc_068")]
[name="莱塔尼亚工人"]该死，该死！我就知道，我就知道他们是绝对不会等我们的！
[name="莱塔尼亚工人"]哥伦比亚就近在眼前，遍地都是财富，谁还会停下脚步等我们？
[charslot(slot="m",name="avg_npc_081")]
[name="乌萨斯村民"]可我们明明也给车队付了钱，我们失踪以后，他们甚至都没有找过我们。
[charslot(slot="m",name="avg_npc_004")]
[name="卡西米尔女孩"]对于其他人来说，在荒野上多待一天都是危险的......
[charslot(slot="m",name="avg_npc_068")]
[name="莱塔尼亚工人"]别说了，接受事实吧。这就是一片人人为己的大地，永远不要指望别人，永远不要！
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]我很赞同，但是抱怨别人同样是没有用的。现在我们要自己行动了。
[name="灰烬"]地图上显示，最近的一个村庄在南边一百公里左右，我们至少要走到那里，才可以获得补给。
[charslot(slot="m",name="avg_npc_068")]
[name="莱塔尼亚工人"]南边？可我们要往西走啊！
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]有位古老的东方哲人说过：“如果你想要去千里之外的地方，那么首先要花三个月囤积粮食。” 
[charslot(slot="m",name="avg_npc_081")]
[name="乌萨斯村民"]准备粮食？为什么不是准备钱？
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]算了，不必在意......总之，如果不想倒在路上，我们就得先做好充分的准备。
[name="灰烬"]没时间在这里抱怨了。打起精神，我们需要尽快出发。
[Dialog]
[stopmusic(fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_desert_3",screenadapt="coverall")]
[Delay(time=2.5)]
[playMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1.5)]
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]好，再来一次。
[name="灰烬"]你叫艾尔温，种族是卡普里尼，是莱塔尼亚人。
[name="灰烬"]你们那的执政者是双子女皇，你们那有许多人都很擅长......嗯，源石技艺。
[charslot(slot="m",name="avg_npc_068")]
[name="莱塔尼亚工人"]没错，但别忘了我们引以为傲的音乐。
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]你的名字是尼古拉，你的国籍是乌萨斯，种族也是......乌萨斯。
[charslot(slot="m",name="avg_npc_081")]
[name="乌萨斯村民"]是的，这个名字让其他国家畏惧，很多时候也让它自己的人民畏惧。
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]你叫阿莉恰，来自卡西米尔。那里有举世闻名的骑士竞技。
[charslot(slot="m",name="avg_npc_004")]
[name="卡西米尔女孩"]嗯！
[charslot(slot="m",name="char_456_ash_1#4")]
[name="灰烬"]关于骑士竞技，我还有一些疑问。
[name="灰烬"]按你说的，由企业出资，雇佣战士生死决斗的运动，为卡西米尔创造了巨大的经济利益。
[name="灰烬"]这些参战的“骑士”，有些人可以受到明星甚至是英雄一样的礼遇，而有些人的生命是可交易的商品。是这样吗？
[charslot(slot="m",name="avg_npc_004")]
[name="卡西米尔女孩"]听去过大城市的人说，确实是这样的。
[charslot(slot="m",name="char_456_ash_1#4")]
[name="灰烬"]的确很奇怪，但并不能说，无法理解。
[charslot(slot="m",name="avg_npc_068")]
[name="莱塔尼亚工人"]这位小姐，请恕我直言。您从那伙劫匪手中救下我们，足以证明您是一位强大的战士。
[name="莱塔尼亚工人"]但您对于这片大地的常识，着实有些......匮乏。
[name="莱塔尼亚工人"]我实在有些好奇，您究竟是来自一个什么样的地方？
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]还请见谅。我的确是来自一个......有些遥远的地方。
[charslot(slot="m",name="avg_npc_081")]
[name="乌萨斯村民"]别在意那么多了，这位是救了我们的恩人，我们应该信任她。
[charslot(slot="m",name="char_456_ash_1#1")]
[name="灰烬"]现在也可以算是队友了，我们暂时都有着一个共同的目的地。
[name="灰烬"]按你们所说，你们是跟着许多人一起，准备去哥伦比亚？嗯......哥伦比亚。
[name="灰烬"]好吧，这里有维多利亚，有高卢，那当然也应该有哥伦比亚。
[charslot(slot="m",name="avg_npc_004")]
[name="卡西米尔女孩"]我和尼古拉大叔还有艾尔温大叔，都是在从卡西米尔西边村

... (全文20800字符)
```

### story_ashlok_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_arena_2",screenadapt="coverall", block=true)]
[Delay(time=1)]
[PlayMusic(intro="$kazimierz2_1_intro", key="$kazimierz2_1_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[PlaySound(key="$livecrowd", volume=0.4, loop=false, channel="people")]
[Delay(time=1)]
[PlaySound(key="$e_skill_skulsrsword",volume=0.8)]
[PlaySound(key="$swordtsing4", volume=0.9,delay=0.2)]
[delay(time=1)]
[PlaySound(key="$d_avg_spear",volume=0.8)]
[PlaySound(key="$swordtsing5", volume=0.9,delay=0.2)]
[delay(time=2)]
[name="比赛解说"]一记漂亮的突刺，伯雷斯瓦夫家的小少爷对昔日的同伴真是毫不留情！
[name="比赛解说"]不过保守的打法依旧无法抵御轰鸣的火炮，灰毫骑士再次用重盾挡下攻击，反手将对方逼到场地死角。
[name="比赛解说"]各位观众，欣赏热血沸腾的骑士交锋的同时，别忘了您还可以按下手边的按键，为您支持的选手下注。
[name="比赛解说"]在卡西米尔，一夜暴富不是梦想！
[Dialog]
[PlaySound(key="$e_skill_skulsrsword",volume=0.5)]
[PlaySound(key="$swordtsing5",volume=1,delay=0.4)]
[CameraShake(duration=1, xstrength=50, ystrength=50, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=0.95,g=0.95, b=0.95, fadetime=0, block=true)]
[Blocker(a=1, r=0.95,g=0.95, b=0.95, fadetime=0.1, block=true)]
[Effect(name="$e_spark_01_mid",x =0, y =0,rox =50, roy =100, roz =50, layer = 1)]
[Effect(name="$e_spark_02_mid",x =0, y =0,rox =100, roy =100, roz =50, layer = 2)]
[Effect(name="$e_slash_cross",x =0, roz =50, layer = 3)]
[Blocker(a=0, r=0.95,g=0.95, b=0.95, fadetime=0.7, block=true)]
[delay(time=0.3)]
[PlaySound(key="$grenade_explosion", volume=0.8)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1.5, xstrength=20, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.1, block=true)]
[charslot(slot="l",name="avg_npc_218",duration=0.3)]
[charslot(slot="r",name="avg_npc_123#1",duration=0.3)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1)]
[charslot(slot="l",name="avg_npc_218",focus="l")]
[name="阿贝特"]格蕾纳蒂，现在就是机会。
[charslot(slot="r",name="avg_npc_123#1",focus="r")]
[name="格蕾纳蒂"]......
[Dialog]
[PlaySound(key="$explolarge1", volume=0.6)]
[PlaySound(key="$d_avg_runstop", volume=1,delay=0.2)]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[charslot(slot="l",posfrom="0,0",posto="-200,0",afrom=1,ato=0,duration=0.4,isblock=false)]
[delay(time=1)]
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_218",focus="m")]
[name="阿贝特"]你站在我的对面，说明你已经做出了选择。难道几次交锋之后，你就后悔了？
[name="阿贝特"]就当是满足一位朋友提出的请求——
[name="阿贝特"]杀了我。
[Dialog]
[PlaySound(key="$d_avg_clothmovementsp", volume=1)]
[charslot(duration=0.3)]
[delay(time=0.8)]
[PlaySound(key="$d_avg_bldwhoosh", volume=1)]
[Effect(name="$e_bladeline_01_large",x = -1, y = 8.3,rox =-98.5, roy =20, roz =121, layer = 1)]
[CameraShake(duration=0.6, xstrength=25, ystrength=25, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_sportsbar",screenadapt="coverall", block=true)]
[delay(time=2)]
[PlaySound(key="$d_avg_crwddiscuss_outside", volume=0.4, loop=true, channel="bse")]
[PlayMusic(key="$normal_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=0.5)]
两周前
[Dialog]
[PlaySound(key="$clink")]
[PlaySound(key="$clink", loop=false, channel="1",delay=0.04)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_221",duration=0.7)]
[charslot(slot="r",name="avg_npc_220",duration=0.7)]
[Delay(time=1)]
[charslot(slot="l",name="avg_npc_221",focus="l")]
[name="乔伊"]上啊！砍他肩甲和护肘之间的缝隙......漂亮！
[charslot(slot="r",name="avg_npc_220",focus="r")]
[name="罗伯特"]小点声，乔伊。你把大家的视线都吸引过来了。
[charslot(slot="l",name="avg_npc_221",focus="l")]
[name="乔伊"]在酒吧里看转播还有低调的道理？我就是支持感染者把对面的贵族老爷打趴下！
[name="乔伊"]呃......你们知道我没有指桑骂槐对吧，格蕾纳蒂，阿贝特？
[Dialog]
[charslot]
[charslot(slot="m",name="avg_npc_218",focus="m")]
[name="阿贝特"]罗格最近的胜率一直不错，看来他在采访中提到的“利用源石技艺转变打法”并不是空话。
[name="阿贝特"]反观奥兹家的继承人，他全身上下唯一值得称赞的可能只有那双赞助商提供的新型动力靴了。
[Dialog]
[charslot(slot="m",name="avg_npc_123#7",focus="m")]
[PlaySound(key="$d_avg_chess", volume=1)]
[Delay(time=1)]
[name="格蕾纳蒂"]将军。
[charslot(slot="m",name="avg_npc_221",focus="m")]
[name="乔伊"]可以啊，没想到每天看报真有用处。
[charslot(slot="m",name="avg_npc_218",focus="m")]
[name="阿贝特"]当然。
[name="阿贝特"]唉......我认输，格蕾纳蒂。你看上去可不止“小时候随便下过几局”的水平。
[charslot(slot="m",name="avg_npc_123#7",focus="m")]
[name="格蕾纳蒂"]我有很多无所事事的表亲。
[name="格蕾纳蒂"]要不是太想保下那枚骑士，你或许还有胜算。
[charslot(slot="m",name="avg_npc_221",focus="m")]
[name="乔伊"]我说，咱们能不能做点酒吧里该做的事？
[charslot(slot="m",name="avg_npc_220",focus="m")]
[name="罗伯特"]他俩用下棋训练战术思维也不是一天两天了。倒是你该反思一下，上场淘汰赛到底为什么被对手骗得团团转？
[charslot(slot="m",name="avg_npc_221",focus="m")]
[name="乔伊"]嘿，这不公平，我可不像你们从小接受专业训练。
[name="乔伊"]我只是想在大骑士领租间小店，谁知道会在半道上感染？打比赛来钱快，等凑足资金我就光荣退役。
[charslot(slot="m",name="avg_npc_222",focus="m")]
[name="？？？"]抱歉打断各位聊天，请问您是不是灰毫骑士？
[charslot(slot="m",name="avg_npc_123#1",focus="m")]
[name="格蕾纳蒂"]是我。
[charslot(slot="m",name="avg_npc_222",focus="m")]
[name="记者"]我是《红酒报》的记者，前几天向您的临时住所寄了采访信，但似乎出了一些小问题......
[name="记者"]我个人十分看好您在赛场上的表现，并认为您有足够的实力冲击骑士锦标赛。
[charslot(slot="m",name="avg_npc_123#1",focus="m")]
[name="格蕾纳蒂"]谢谢。
[charslot(slot="m",name="avg_npc_222",focus="m")]
[name="记者"]我想除了竞技表现之外，观众们对于您私下的生活也会很感兴趣。
[name="记者"]包括您常来的这家酒吧，您日常是如何训练的，还有......卡利斯卡家族将您驱逐的始末。
[charslot(slot="m",name="avg_npc_123#4",focus="m")]
[name="格蕾纳蒂"]我的个人生活并没有你想象的那么精彩。
[charslot(slot="m",name="avg_npc_222",focus="m")]
[name="记者"]听闻您对家族心怀怨恨。比起争夺希望渺茫的锦标赛冠军，一篇重要版面的头

... (全文32902字符)
```

### story_astesi_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_room_2",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$path_intro", key="$path_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
罗德岛本舰
星极的房间
[Dialog]
[Character(name="avg_274_Astesia_1#2",fadetime=1,block=true)]
[Delay(time=0.5)]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=2)]
[name="星极"]（揉眼睛）
[Characteraction(name="middle",type="move",xpos=-2,fadetime=0.5,isblock=true)]
[Characteraction(name="middle",type="move",xpos=2,fadetime=0.5,isblock=true)]
[name="星极"]如果我没记错的话......
[Dialog]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=0.5)]
[Character(name="avg_274_Astesia_1#2")]
[name="星极"]根据书上的记载，今晚星象会很稳定，星体也很明显。
[name="星极"]但愿今晚能有所收获......吧......
[name="星极"]（不经意地揉眼睛）
[Characteraction(name="middle",type="move",xpos=-2,fadetime=0.5,isblock=true)]
[Characteraction(name="middle",type="move",xpos=2,fadetime=0.5,isblock=true)]
[name="星极"]近期的星象测算结果和占星研究协会公布的数据相差太多了。
[name="星极"]父亲他......一定对这件事很不满意。
[name="星极"]给父亲的回信还是再缓一段时间比较稳妥。
[name="星极"]......
[name="星极"]矿石病......矿石病......
[name="星极"]（不经意地揉眼角）
[Characteraction(name="middle",type="move",xpos=-2,fadetime=0.5,isblock=true)]
[Characteraction(name="middle",type="move",xpos=2,fadetime=0.5,isblock=true)]
[name="星极"]唉......
[Dialog]
[PlaySound(key="$d_avg_paper2", volume=1)]
[Delay(time=0.5)]
[Character(name="avg_274_Astesia_1#1")]
[name="星极"]今晚多做些记录吧。如果推测还是有问题，就只能先观测一份正确的数据了。
[Character(name="avg_274_Astesia_1#1")]
[name="星极"]（轻轻摁了摁眼角）
[Characteraction(name="middle",type="move",xpos=-2,fadetime=0.5,isblock=true)]
[Characteraction(name="middle",type="move",xpos=2,fadetime=0.5,isblock=true)]
[Character(name="avg_274_Astesia_1#2")]
[name="星极"]呵啊......
[name="星极"]眼睛好痒......
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=1)]
[Character(name="avg_135_halo_1#1$1",fadetime=1)]
[Delay(time=2)]
[name="星源"]姐姐，我来了。
[Character(name="avg_135_halo_1#1$1",name2="avg_274_Astesia_1#1",focus=2)]
[name="星极"]嗯，早上——
[Character(name="avg_135_halo_1#7$1",name2="avg_274_Astesia_1#1",focus=1)]
[name="星源"]姐，你眼睛怎么了？！
[Character(name="avg_135_halo_1#7$1",name2="avg_274_Astesia_1#5",focus=2)]
[name="星极"]眼睛吗？只是有些痒。
[Character(name="avg_135_halo_1#7$1",name2="avg_274_Astesia_1#5",focus=1)]
[name="星源"]眼睛里全是血丝，怎么还有血点？！
[Character(name="avg_135_halo_1#7$1",name2="avg_274_Astesia_1#2",focus=2)]
[name="星极"]很快就会好的......
[Character(name="avg_135_halo_1#3$1",name2="avg_274_Astesia_1#2",focus=1)]
[name="星源"]眼睑里还有肿块......
[name="星源"]人的自愈能力可不包括修复这种损伤。
[Character(name="avg_135_halo_1#9$1",name2="avg_274_Astesia_1#2",focus=1)]
[name="星源"]我现在就带你去医疗部。
[Character(name="avg_135_halo_1#9$1",name2="avg_274_Astesia_1#5",focus=2)]
[name="星极"]可是，今天晚上——
[Character(name="avg_135_halo_1#9$1",name2="avg_274_Astesia_1#5",focus=1)]
[name="星源"]你就别管星星不星星的了。它们就算掉下来也不能治好你的眼睛。
[name="星源"]跟我走。
[Character(name="avg_135_halo_1#9$1",name2="avg_274_Astesia_1#5",focus=2)]
[name="星极"]等，等等......
[Dialog]
[Character(name="avg_135_halo_1#9$1",name2="avg_274_Astesia_1#5")]
[characteraction(name="left",type="move",xpos=150,fadetime=1.2,isblock=true)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left",type="move",xpos=-200,fadetime=1,isblock=false)]
[characteraction(name="right",type="move",xpos=-200,fadetime=1.2,isblock=false)]
[character(fadetime=1)]
[Delay(time=0.5)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_ri_1",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[Character(name="avg_274_Astesia_1#1",name2="char_345_folnic_1#1",focus=2)]
[name="亚叶"]细菌感染，双眼急性化脓性炎症。
[name="亚叶"]不是特别严重，现在安排手术切除后上药，很快就能康复。
[Character(name="avg_274_Astesia_1#1",name2="char_345_folnic_1#1",focus=1)]
[name="星极"]呼......
[Character(name="avg_274_Astesia_1#1",name2="char_345_folnic_1#1",focus=2)]
[name="亚叶"]手术后三十六小时不能视物，保险起见最好在医疗部留观。
[Character(name="avg_274_Astesia_1#5",name2="char_345_folnic_1#1",focus=1)]
[name="星极"]......
[name="星极"]手术，可以延迟吗？
[Character(name="avg_135_halo_1#9$1")]
[name="星源"]医生，这件事我拿主意。
[Character(name="char_345_folnic_1#1")]
[name="亚叶"]家属和患者先得出一个结论吧。
[Character(name="avg_274_Astesia_1#1",name2="avg_135_halo_1#9$1",focus=1)]
[name="星极"]吉妮......
[Character(name="avg_274_Astesia_1#1",name2="avg_135_halo_1#9$1",focus=2)]
[name="星源"]这件事没得商量。
[name="星源"]我了解你的理由，也明白这对你来说很重要。
[Character(name="avg_274_Astesia_1#1",name2="avg_135_halo_1#11$1",focus=2)]
[name="星源"]但我还是要重申一遍。
[name="星源"]这件事没得商量。
[name="星源"]你知道我更关心什么。
[Character(name="avg_274_Astesia_1#2",name2="avg_135_halo_1#11$1",focus=1)]
[name="星极"]......
[Character(name="avg_274_Astesia_1#2",name2="avg_135_halo_1#9$1",focus=2)]
[name="星源"]我姐姐同意了，麻烦安排手术吧。
[Character(name="char_345_folnic_1#1")]
[name="亚叶"]星极干员，我需要你的口头确认。
[Character(name="avg_274_Astesia_1#2")]
[name="星极"]（小声）嗯......
[Character(name="char_345_folnic_1#1")]
[name="亚叶"]家属先在这份告知书上签字。
[Character(name="avg_135_halo_1#11$1")]
[name="星源"]（阅览并签署告知书）
[Dialog]
[PlaySound(key="$d_avg_penrustle", volume=1)]
[Delay(time=2.5)]
[Characteraction(name="middle",type="move",xpos=-7,fadetime=0.5,isblock=true)]
[Characteraction(name="middle",type="move",xpos=7,fadetime=0.5,isblock=true)]
[Character(name="char_345_folnic_1#1")]
[name="亚叶"]（接过告知书，在终端上输入信息）
[Dialog]
[PlaySound(key="$keyboard", volume=1)]
[Delay(time=2.5)]
[name="亚叶"]去前台协调床位，一会结束手术后病患会直接被送到病房，家属在那里等待即可。
[name="亚叶"]星极干员，请跟我来。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_infirmary",screenadapt="showall")]
[Delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]	
[name="星极"]......
[Character(name="char_345_folnic_1#1")]
[name="亚叶"]手术本身没有什么难度，请放轻松。
[name="亚叶"]根据手术前交流，我们会为你准备全身麻醉，没有问题吧。
[Dialog]
[Char

... (全文26399字符)
```

### story_astesi_2_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Background(image="38_g13_trimountlivingroom",screenadapt="coverall")]
[playMusic(intro="$m_dia_street_intro",key="$m_dia_street_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
哥伦比亚，特里蒙
[dialog]
[charslot(slot = "r", name = "avg_274_Astesia_1#7",duration = 1)]
[charslot(slot = "l", name = "avg_135_halo_1#1$1",duration = 1)]
[delay(time=2)]
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]我想应该没有需要继续修改的地方了。
[name="星极"]辛苦了，吉妮。
[charslot(slot = "l", name = "avg_135_halo_1#1$1",focus="l")]
[name="星源"]没事，应该的。
[name="星源"]再说我也没做什么，只是帮你提供基础数据模型，顺带调试一下而已。
[name="星源"]内容和具体框架排布，不还是姐姐你做的。
[charslot(slot = "r", name = "avg_274_Astesia_1#1",focus="r")]
[name="星极"]再过一周，占星研究协会的会堂讨论就要开始了。
[charslot(slot = "l", name = "avg_135_halo_1#12$1",focus="l")]
[name="星源"]特里蒙天上的空洞一定给你带来了很多麻烦吧。
[charslot(slot = "r", name = "avg_274_Astesia_1#1",focus="r")]
[name="星极"]对我们家应该没什么影响，毕竟父亲母亲不是喜欢搭空中楼阁的人。
[charslot(slot = "r", name = "avg_274_Astesia_1#5",focus="r")]
[name="星极"]嗯......父亲母亲已经到特里蒙有一段时间了，我忙着写东西，还没时间去见他们两位。
[name="星极"]你想见见他们吗，吉妮？
[charslot(slot = "l", name = "avg_135_halo_1#4$1",focus="l")]
[name="星源"]别，除了姐姐你，我见到姓乌比卡的就头疼。
[charslot(slot = "l", name = "avg_135_halo_1#1$1",focus="l")]
[name="星源"]说起来，姐姐，你的这篇......就当是研究内容吧，准备怎么用？
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]在宣讲以后无偿提供给学界吧。
[name="星极"]特里蒙空洞外的星空似乎有着完全不同的运行规律，可空洞只有这么一点，没法囊括所有星星。
[name="星极"]但只要有了我们研究的换算模型，所有研究者都可以初步获得两套系统下星座的大致坐标，从而进一步推演运行规律与相对关系。
[name="星极"]想必这能给今后研究星空的人提供一些便利吧。
[charslot(slot = "l", name = "avg_135_halo_1#4$1",focus="l")]
[name="星源"]确实像是姐姐你会做的事呢。
[charslot(slot = "l", name = "avg_135_halo_1#1$1",focus="l")]
[name="星源"]对了，你不是说，空洞后的星空带来了新的占星可能性吗，反正你来特里蒙的初衷已经完成了，要不——帮我看看今天的运势？
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]你什么时候又重新对这个感兴趣了？
[charslot(slot = "l", name = "avg_135_halo_1#2$1",focus="l")]
[name="星源"]好玩嘛，来吧姐姐。
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]好吧......
[charslot(slot = "r", name = "avg_274_Astesia_1#2",focus="r")]
[name="星极"]（沉思）
[name="星极"]（喃喃自语）
[name="星极"]（高举天球仪）
[charslot(slot = "r", name = "avg_274_Astesia_1#5",focus="r")]
[name="星极"]......
[charslot(slot = "l", name = "avg_135_halo_1#1$1",focus="l")]
[name="星源"]怎么样？
[charslot(slot = "r", name = "avg_274_Astesia_1#5",focus="r")]
[name="星极"]好像占星的结果......和以前的形式不太一样......
[name="星极"]“今日是黎博利的灾难。”
[name="星极"]这就是星星们传达到的消息。
[name="星极"]以前明明可以更具体的，奇怪......
[charslot(slot = "l", name = "avg_135_halo_1#12$1",focus="l")]
[name="星源"]听上去就不太吉利......唉，别在意，我也就是随口问问。
[charslot(slot = "l", name = "avg_135_halo_1#5$1",focus="l")]
[name="星源"]以前你也给我占到过大难临头这个那个的，我不也一点事都没有吗，别往心里去。
[charslot(slot = "l", name = "avg_135_halo_1#1$1",focus="l")]
[name="星源"]早饭吃完了吗？我去拿咖啡给你。
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]嗯，谢谢你，吉妮。
[dialog]
[charslot(slot = "l",posfrom = "0,0", posto = "-200,0",duration = 1,afrom=1,ato=0)]
[delay(time=2)]
[PlaySound(key="$doorknockquite", volume=1)]
[delay(time=1)]
[charslot(slot = "r", name = "avg_274_Astesia_1#7")]
[name="星极"]来了。
[dialog]
[charslot(slot = "r", posfrom = "0,0", posto = "-150,0",duration = 1)]
[delay(time=1.3)]
[PlaySound(key="$dooropenquite", volume=1)]
[charslot(slot = "l", name = "avg_npc_523_1#1$1",posfrom = "-100,0", posto = "0,0",duration=1)]
[charslot(slot = "r", posfrom = "-150,0", posto = "-0,0",duration = 1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_npc_523_1#1$1",focus="l")]
[name="快递员"]您好，是阿丝忒希娅·乌比卡小姐吗？我是来取您要快递的文件的。
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]在这里。
[dialog]
[PlaySound(key="$d_avg_paper2", volume=1)]
[delay(time=1)]
[charslot(slot = "l", name = "avg_npc_523_1#1$1",focus="l")]
[name="快递员"]好的，我收到了，再和您确认一下，是送到这个地址的，佛朗索瓦·乌比卡先生手上，对吧。
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]嗯，今天能送到吗？
[charslot(slot = "l", name = "avg_npc_523_1#1$1",focus="l")]
[name="快递员"]这是城内快递，而且您支付了加急费用，没有意外的话，今天就可以送到。
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]好的，谢谢。
[charslot(slot = "l", name = "avg_npc_523_1#1$1",focus="l")]
[name="快递员"]不客气，很高兴为您服务。
[name="快递员"]祝您生活愉快，再见。
[dialog]
[PlaySound(key="$doorclosequite", volume=1)]
[charslot(slot = "l", name = "avg_npc_523_1#1$1",afrom=1,ato=0,duration=0.5)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", name = "avg_135_halo_1#1$1",duration=1)]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_135_halo_1#1$1",focus="l")]
[name="星源"]有客人？是住隔壁的维多利亚老妇人吗？
[charslot(slot = "r", name = "avg_274_Astesia_1#7",focus="r")]
[name="星极"]埃文斯女士？不是，只是快递员罢了。
[name="星极"]他来拿我给父亲的文稿。
[dialog]
[stopmusic(fadetime=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$bottlebroken", volume=1)]
[charslot(slot = "l", name = "avg_135_halo_1#11$1",focus="l")]
[delay(time=1.5)]
[charslot(slot = "l", name = "avg_135_halo_1#11$1",focus="l")]
[name="星源"]姐？
[charslot(slot = "l", name = "avg_135_halo_1#9$1",focus="l")]
[name="星源"]............
[charslot(slot = "l", name = "avg_135_halo_1#6$1",focus="l")]
[name="星源"]你是不是疯了？！
[charslot(slot = "r", name = "avg_274_Astesia_1#4",focus="r")]
[name="星极"]怎么了，吉妮？
[playMusic(intro="$storyendjp_intro",key="$storyendjp_loop", volume=0.6)]
[charslot(slot = "l", name = "avg_135_halo_1#9$1",focus="l")]
[name="星源"]我之前是不是和你说过很多次了，要是把文章给乌比卡先生，他就会把自己的名字添到你的名字前面？！
[charslot(slot = "r", name = "avg_274_Astesia_1#5",focus="r")]
[name="星极"]别把父亲想得那么不堪。
[charslot(slot = "l", name = "avg_135_halo_1#9$1",focus="l")]
[name="星源"]不堪？呵，那你告诉我，你拿得出哪怕一篇你独自署名的文章吗？
[charslot(slot = "r", name = "avg_274_Astesia_1#5",focus="r")]
[name="星极"]......我只是，我只是觉得这么重要的内容需要他这样的专家过目一下。
[charslot(slot = "l", name = "avg_135_halo_1#9$1",focus="l")]
[name="星源"]好，好啊，就算是这样吧。
[charslot(slot = "l", 

... (全文31559字符)
```

### story_aurora_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="30_ex1_snowmount",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$m_dia_street_intro", key="$m_dia_street_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1)]
[PlaySound(key="$d_avg_cloakmovement", volume=0.7)]
[delay(time=1.5)]
[Character(name="avg_248_mgllan_1#1$1",name2="avg_422_aurora_1#1$1",fadetime=0.7,block=true)]
[delay(time=1)]
[Character(name="avg_248_mgllan_1#1$1",name2="avg_422_aurora_1#1$1",focus=1)]
[name="麦哲伦"]极光，你已经开始收拾装备了吗？
[Character(name="avg_248_mgllan_1#1$1",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]对呀，麦麦，我们不是已经把收集的样本和测试的材料都整理好了吗？
[name="极光"]如果明天返程的话，今天提前收拾好做好准备，明天就会快很多。
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#1$1",focus=1)]
[name="麦哲伦"]那——我有一个新的提议哦！计划的日期还有剩余，而且这段日子正好是极光的高发期，所以，要不要多待两天再返程？
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#8$1",focus=2)]
[name="极光"]唔，可以吗？
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#8$1",focus=1)]
[name="麦哲伦"]当然啦！两天后正好是规划中返程的日子，我的“辅助勘察员”，你这回帮了我很多，我当然也希望能满足你的愿望。
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]麦麦，这是我应该做的事情嘛。
[name="极光"]如果这一次科考任务我只是跟随你出来，什么忙都帮不到的话，最开始我是不会答应的。
[Character(name="avg_248_mgllan_1#9$1",name2="avg_422_aurora_1#1$1",focus=1)]
[name="麦哲伦"]那你算是同意了吗？我们多待两天，如果那个时候我们还没能看到极光，就按原计划返回吧！
[Character(name="avg_248_mgllan_1#9$1",name2="avg_422_aurora_1#9$1",focus=2)]
[name="极光"]麦麦，谢谢你。
[Character(name="avg_248_mgllan_1#9$1",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]那我有一件事情想拜托你，可以吗？
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#1$1",focus=1)]
[name="麦哲伦"]当然呀！
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#2$1",focus=2)]
[name="极光"]我想用这两天继续测验一下新研究出的防御工事盾牌，那架承担摄制任务的无人机，能不能在我测验时记录一下施术过程？
[name="极光"]我虽然在自己的盾牌上也安装了摄制模块，但它并不能脱离我独立运行。
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]而且我刚刚把盾牌的源石回路做出来，性能还不太稳定，如果是人为摄制的话，可能会伤到摄影师，让无人机远远地拍是最好的方法啦。
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#1$1",focus=1)]
[name="麦哲伦"]来，我教给你怎么设定它的数值。
[Character(name="avg_248_mgllan_1#8$1",name2="avg_422_aurora_1#1$1",focus=2)]
[name="极光"]嗯，那我去远一点的地方，测试动静会很大，免得干扰到你。
[Character(name="avg_248_mgllan_1#1$1",name2="avg_422_aurora_1#1$1",focus=1)]
[name="麦哲伦"]有什么问题一定要叫我哦！
[Character(name="avg_248_mgllan_1#1$1",name2="avg_422_aurora_1#9$1",focus=2)]
[name="极光"]嗯！
[Dialog]
[Character(name="avg_248_mgllan_1#1$1",name2="avg_422_aurora_1#9$1")]
[delay(time=0.51)]
[PlaySound(key="$d_avg_snowbootwalk", volume=1)]
[Character(name="avg_248_mgllan_1#1$1",name2="char_empty",fadetime=1.5,block=true)]
[delay(time=2.5)]
[Character(name="avg_248_mgllan_1#1$1")]
[name="麦哲伦"]哎呀，真的是太刻苦了。我还想着这两天让她好好休息下的，之前找样本的时候也一直冲在最前面。
[Character(name="avg_248_mgllan_1#5$1")]
[name="麦哲伦"]虽然是乌萨斯，但还是个病人啊。
[name="麦哲伦"]还一直念叨着这面盾牌——
[Dialog]
[stopmusic(fadetime=3)]
[PlaySound(key="$d_avg_snowstormflp", volume=0.6, loop=true, channel="bgs")]
[Blocker(a=0.2, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[Character(name="avg_248_mgllan_1#4$1")]
[name="麦哲伦"]......起风了？
[name="麦哲伦"]云层昏暗而云顶较高，边缘模糊，云体高大......
[name="麦哲伦"]这种特征......
[Character(name="avg_248_mgllan_1#6$1")]
[name="麦哲伦"]极光——
[name="麦哲伦"]极光！
[Character(name="avg_248_mgllan_1#6$1",focus=-1)]
[name="极光"]麦麦，快穿防护服！
[Dialog]
[StopSound(channel="bgs", fadetime=2)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_thundercloud",screenadapt="showall")]
[Delay(time=1)]
[playMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)] 
[Character(name="avg_422_aurora_1#5$1")]
[name="极光"]我见过这种云，可能是源石冰雹，它——
[Dialog]
[musicvolume(volume=0.2, fadetime=1.5)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[cameraEffect(effect="Grayscale", keep=true, amount=1, fadetime=0)]
[Background(image="bg_thundercloud",screenadapt="showall")]
[Delay(time=0.51)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.51)]
[Character(name="avg_422_aurora_1#5$1")]
[name="极光"]快站到我身后来！躲在防御工事后面，把防护服裹紧，已经有同学被冰雹砸伤了！
[name="极光"]这些冰雹上......有源石！！绝对要小心不要被砸到！
[Dialog]
[character]
[Delay(time=0.51)]
[name="惊恐的同学"]洛拉，你、你的胳膊......？
[name="勇敢的同学"]把防御工事给我，洛拉，你退到后面去！
[name="勇敢的同学"]你已经被源石冰雹砸到了！
[Dialog]
[Delay(time=0.51)]
[Character(name="avg_422_aurora_1#5$1")]
[name="极光"]！！
[name="极光"]你——
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0.5, block=true)]
[character]
[cameraEffect(effect="Grayscale", keep=true, amount=0, fadetime=0)]
[Background(image="30_ex1_snowmount_s",screenadapt="showall")]
[Delay(time=0.51)]
[musicvolume(volume=0.4, fadetime=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Delay(time=0.51)]
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#5$1",focus=2)]
[name="极光"]麦麦，你站到我身后来！
[name="极光"]我经历过这种源石冰雹，感染几率极高，你一定要把防护服裹紧！
[Dialog]
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#5$1")]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=100, fadetime=1,block=true)]
[delay(time=1)]
[PlaySound(key="$d_avg_clothmovement", volume=0.7)]
[delay(time=1.5)]
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#2$1",focus=2)]
[name="极光"]你的防护服穿好了吗？麦麦，你先穿好自己的，再来帮我穿——
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#2$1",focus=1)]
[name="麦哲伦"]我已经穿好了！
[name="麦哲伦"]极光，听我说，我遇到过类似的突发灾害，我们往后退，那边有岩体可以提供依靠，在空地上我们挡不过五分钟！
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#8$1",focus=2)]
[name="极光"]可是移动会让我没办法完全护住你！
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#8$1",focus=1)]
[name="麦哲伦"]但在空地上你绝对会受伤！
[Character(name="avg_248_mgllan_1#6$1",name2="avg_422_aurora_1#8$1",focus=2)]
[name="极光"]......
[Character(name="avg_

... (全文20742字符)
```

### story_ayer_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[dialog]
[stopmusic]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[Background(image="bg_laccolith",screenadapt="coverall")]
[playMusic(intro="$darkness01_intro",key="$darkness01_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=1)]
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", duration = 1.5)]
[charslot(slot = "r", name = "avg_npc_418_1#1$1", duration = 1.5, isblock=true)]
[charslot(slot = "r", focus="r")]
[name="陌生女人"]嗯......
[name="陌生女人"]这边......不对，那边？那句话是怎么说的来着......
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", focus="l")]
[name="断崖"]......
[charslot(slot = "r", focus="r")]
[name="陌生女人"]应该还是这边，那边就是污染区了。
[name="陌生女人"]保险起见，我再确认下......
[dialog]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[charslot(slot = "l", posfrom="0,0", posto="300,0", duration=1.5)]
[charslot(slot = "l", afrom = 1, ato = 0, duration=0.5)]
[delay(time=2)]
[charslot(slot = "r", focus="r")]
[name="陌生女人"]喂，等等我。
[dialog]
[charslot(slot = "r", posfrom="0,0", posto="500,0", afrom = 1, ato = 0, duration=2, isblock=true)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "l", name = "avg_294_ayer_1#1$1")]
[delay(time=1)]
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", posfrom="-300,0", posto="0,0", duration=1, isblock=true)]
[charslot(slot = "r", focus="r")]
[name="陌生女人"]哦，你走的方向是对的，运气不错。
[charslot(slot = "l", name = "avg_294_ayer_1#3$1", focus="l")]
[name="断崖"]我说过，前面没有你的事，后面自然有你派上用场的时候。
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", focus="l")]
[name="断崖"]但是现在，我开始怀疑你作为天灾信使的能力了。
[charslot(slot = "r", focus="r")]
[name="天灾信使"]什么？不懂就不要乱说。
[name="天灾信使"]天灾信使的责任很重的，能否准确地判断天灾的动向，将关乎很多人的性命，慎重一点不会错的。
[name="天灾信使"]不然你以为天灾信使为什么这么少，我能出现在你面前已经算你走运了。难道你还见过第二个天灾信使不成？
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", focus="l")]
[name="断崖"]......少废话。
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]断崖先生，承认吧。要深入天灾过后的现场，你一定需要我的帮助。
[charslot(slot = "l", name = "avg_294_ayer_1#3$1", focus="l")]
[name="断崖"]我承认。
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]啊？
[charslot(slot = "l", name = "avg_294_ayer_1#11$1", focus="l")]
[name="断崖"]我们可以继续赶路了吗？
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]......
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", focus="l")]
[name="断崖"]......
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]你要找的那个被科威尔带人掳去灾区深处的家伙，是你的什么人？
[charslot(slot = "l", name = "avg_294_ayer_1#2$1", focus="l")]
[name="断崖"]（吸气）
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]停，先别急着拒绝回答。你知道我要找科威尔是因为和他有笔账要算，要是你要找的人其实是科威尔那边的，那我可麻烦大了。
[name="天灾信使"]你一个人就解决了科威尔矿业的不少打手，坐在电椅上还笑得出来，我对付不了你。
[name="天灾信使"]我有必要知道他的身份，毕竟我们现在一起行动，对吧？
[dialog]
[charslot]
[charslot(slot = "m", name = "avg_294_ayer_1#3$1")]
[delay(time=1)]
[name="断崖"]......他是我的雇主。
[charslot(slot = "m",  name = "avg_npc_418_1#1$1")]
[name="天灾信使"]雇主？你是他的护卫？
[charslot(slot = "m", name = "avg_294_ayer_1#3$1")]
[name="断崖"]是。
[charslot(slot = "m", name = "avg_294_ayer_1#1$1")]
[name="断崖"]我们受雇于科威尔矿业的竞争企业，玉米钻头公司，你应该听过这个名字。
[charslot(slot = "m",  name = "avg_npc_418_1#1$1")]
[name="天灾信使"]嗯，是此次灾后最先派矿队进入灾区勘探的矿业公司吧？
[name="天灾信使"]听说那支矿队从东南进入，速度惊人，很快就帮助玉米钻头公司发现了矿区并取得了所有权。
[charslot(slot = "m", name = "avg_294_ayer_1#11$1")]
[name="断崖"]我们受雇于那支矿队，先前发现的矿脉只是很小的一部分，勘探显示在中心广场原址附近有更多的矿脉暴露了出来。
[charslot(slot = "m", name = "avg_294_ayer_1#3$1")]
[name="断崖"]那之后公司筹划从北部再次进入灾区进行二次勘探，在灾区边缘建立了临时营地。
[charslot(slot = "m", name = "avg_294_ayer_1#1$1")]
[name="断崖"]但就在昨天清晨，我从城镇买毛豆返回后，发现营地已经被暴力破坏了，队员全部失踪。
[charslot(slot = "m", name = "avg_294_ayer_1#3$1")]
[name="断崖"]我根据雇主身上发信器的信号，找到了你所在的那个营地，潜入后发现他已经不在那里了，只留下了发信器。
[charslot(slot = "m", name = "avg_294_ayer_1#1$1")]
[name="断崖"]后面的事你都清楚。
[charslot(slot = "m",  name = "avg_npc_418_1#1$1")]
[name="天灾信使"]你这护卫还挺负责，但我可要提醒你，这次是科威尔亲自带队，以他的性子，这一路上有不少人得掉脑袋，你的雇主大概率活不到最后。
[name="天灾信使"]反正是在雷姆必拓，这种情况你完全不必蹚浑水。
[charslot(slot = "m", name = "avg_294_ayer_1#1$1")]
[name="断崖"]根据合同里的条款，确认雇主死亡后我才能终止护卫工作。
[charslot(slot = "m", name = "avg_294_ayer_1#11$1")]
[name="断崖"]拿钱办事，天经地义。
[charslot(slot = "m",  name = "avg_npc_418_1#1$1")]
[name="天灾信使"]那就随你便咯。
[name="天灾信使"]前面可能还有污染区，我再确认下......啊，你等等我。
[dialog]
[PlaySound(key="$rungeneral", volume=1)]
[charslot(duration=2)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[charslot(slot = "l", name = "avg_294_ayer_1#1$1")]
[delay(time=1)]
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", posfrom="-300,0", posto="0,0", duration=1, isblock=true)]
[delay(time=1)]
[charslot(slot = "r",focus="r")]
[name="天灾信使"]呼，你走得可真够快的。
[charslot(slot = "l", name = "avg_294_ayer_1#2$1", focus="l")]
[name="断崖"]别抱怨，你又这么磨叽，莱——
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]莱什么？
[charslot(slot = "l", name = "avg_294_ayer_1#11$1", focus="l")]
[name="断崖"]......没什么。
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]断崖先生，说实话，我严重怀疑你对我隐瞒了什么。
[charslot(slot = "l", name = "avg_294_ayer_1#3$1", focus="l")]
[name="断崖"]我对你隐瞒的可太多了。
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]......是这样没错，但是现在我要说的是关键的问题。
[name="天灾信使"]你！是和你的雇主失联了，没错吧？
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", focus="l")]
[name="断崖"]是。
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]那你怎么知道往哪里是正确的方向？
[charslot(slot = "l", name = "avg_294_ayer_1#1$1", focus="l")]
[name="断崖"]......
[charslot(slot = "r",  name = "avg_npc_418_1#1$1", focus="r")]
[name="天灾信使"]而且你好几次都没有等我说话就擅自行动，却能和我判断的方位一致。
[name="天灾信使"]你......有什么手段？
[charslot(slot = "l", name = "avg_294_ayer_1#3$1", focus="l")]

... (全文34730字符)
```

### story_baslin_1_1

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[stopmusic]
[Dialog]
[Delay(time=1)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Background(image="44_g8_towersquare",screenadapt="showall")]
[Delay(time=1)]
[PlayMusic(key="$calm_loop", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=0.5)]
12月28日 5:00 P.M.
崔林特尔梅，双子女皇塔前
[dialog]
[PlaySound(key="$d_avg_footstep_stonestep", volume=0.8)]
[charslot(slot = "m", name = "avg_4109_baslin_1#1$2",focus="m",duration=2)]
[delay(time=2.5)]
米夏埃尔抱着对他来说过于沉重的低音号，带着乐队，跟随接待他的侍从走向双子塔。
[dialog]
[charslot]
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="r")]
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]米夏埃尔阁下，您出发的时候，家乡应该已经在筹备新年活动了吧？
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l")]
[name="米夏埃尔"]嗯。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l")]
[name="米夏埃尔"]叫我米夏埃尔就好。
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]啊，好。
[name="负责接待的侍从"]真怀念啊，家乡的晚霞或许没有崔林特尔梅的灿烂，但烤扭结饼的香味，是什么东西都没法替代的......
[name="负责接待的侍从"]没想到您会在这个时间到达崔林特尔梅，我以为......
[name="负责接待的侍从"]您至少会在自己的高塔里度过新年。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l")]
[name="米夏埃尔"]毕竟这可能是我在家乡过的最后一个新年了，对吧？被送到崔林特尔梅“学习”的继承人们，不知道什么时候才能回到家乡。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l")]
[name="米夏埃尔"]是我坚持想要赶上首都的新年庆典的。
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]您想参加新年庆典？......
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l")]
[name="米夏埃尔"]今天觐见时，我就会向两位女皇提出申请。父亲说了，要想其他大区在贸易上平等地对待鲁珀坎，首先，得看陛下们的态度。
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]可是，陛下们......啊，米夏埃尔，再往前我就不被允许过去了。虽然我没进去过，但前往恩典高塔的路应该就是那条。
[charslot(slot = "l", name = "avg_4109_baslin_1#10$2",focus="l")]
[name="米夏埃尔"]你从来没进去过？......那过去几年里，从家乡递给陛下们的官方文书，都是谁在传递？
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]唉......陛下们不想听的时候，鲜有“杂音”能传到她们的耳朵里。这些“特殊礼遇”，周围的贵族也全一清二楚。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l")]
[name="米夏埃尔"]......
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]总之，米夏埃尔，和陛下们说话千万小心啊。我听说过很多不好的传闻。
[name="负责接待的侍从"]尤其是那位赫琳玛特——差点把我们的家乡踏平的那位——听说要是有人说错半个字，她就会用腰间那把剑把那人砍成两半！
[name="负责接待的侍从"]您可不要以为这些都是危言耸听！尽量多和那位和善亲切的伊维格娜德交流，毕竟您的安全才是最重要的......
[charslot(slot = "l", name = "avg_4109_baslin_1#2$2",focus="l")]
[name="米夏埃尔"]为这场觐见准备了一整年，算不算足够小心？
[charslot(slot = "l", name = "avg_4109_baslin_1#2$2",focus="l")]
[name="米夏埃尔"]从自我介绍，到选曲介绍词，到参加新年庆典申请书的每个词，光是写稿子都写烂了好几支笔呢。
[charslot(slot = "l", name = "avg_4109_baslin_1#8$2",focus="l")]
[name="米夏埃尔"]再说，终于有鲁珀坎的狼被允许踏入羊群的高塔，这本来就是个好信号，不是吗？
[charslot(slot = "r", name = "avg_npc_271_1#1$1",focus="r")]
[name="负责接待的侍从"]......祝您一切顺利，米夏埃尔。
[dialog]
[charslot]
米夏埃尔走上了那条陌生且过于宽阔的道路。
[name="米夏埃尔"]（呼——吸——呼——吸——）
[dialog]
[PlaySound(key="$d_avg_footstep_stonestep", volume=0.8)]
[delay(time=2)]
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=2)]
[Background(image="44_g6_towerterrace",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[Dialog]
[Character]
[PlaySound(key="$dooropenquite", volume=1)]
[Delay(time=1)]
[charslot(slot = "m", name = "avg_4109_baslin_1#1$2",focus="m",duration=1)]
[delay(time=1)]
[name="米夏埃尔"]（只有......一位女皇在场？还有一些文武官员。那位令人害怕的赫琳玛特不在？）
[charslot(slot = "m", name = "avg_4109_baslin_1#1$2",focus="m")]
[name="米夏埃尔"]（太好了......许多特意为她准备的说辞用不上了。）
[Dialog]
[Character]
[PlaySound(key="$d_gen_walk_n")]
[delay(time=2)]
他走上前时，能听到自己轰隆作响的心跳。他向伊维格娜德行礼，动作稳重而收敛，如之前预演过无数次那般。
[dialog]
[charslot(slot = "r", name = "avg_npc_487_1#1$1", focus="all",duration=1)]
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="all",duration=1,isCopy=true)]
[Delay(time=2.5)]
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l",isCopy=true)]
[name="米夏埃尔"]陛下，米夏埃尔代表家族前来觐见。
[charslot(slot = "r", name = "avg_npc_487_1#10$1", focus="r")]
[name="伊维格娜德"]米夏埃尔，到了这里还适应吗？
[charslot(slot = "l", name = "avg_4109_baslin_1#8$2",focus="l",isCopy=true)]
[name="米夏埃尔"]一切都很好，感谢您的关心。这里到处是我在家乡未曾见过的景色。
[charslot(slot = "l", name = "avg_4109_baslin_1#8$2",focus="l",isCopy=true)]
[name="米夏埃尔"]目睹了首都的繁荣，我愈发期待在“永恒恩典”与“无情权威”的照耀下，鲁珀坎也能、跟上发展的脚步。
[Dialog]
[Character]
米夏埃尔的心抽紧了一下。因为紧张，在他流利的对答中出现了一个几乎无法察觉的小停顿。
他偷眼观察伊维格娜德的反应，发现她脸上的笑容依旧亲切，仿佛在鼓励他不要害怕。米夏埃尔心里紧绷的弦终于放松了些许。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="r",isCopy=true)]
[charslot(slot = "r", name = "avg_npc_487_1#1$1", focus="r")]
[name="伊维格娜德"]我看你带着乐队，这次带来了怎样的演奏？
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l",isCopy=true)]
[name="米夏埃尔"]是一首来自我家乡的叙事曲——《白牙》。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l",isCopy=true)]
[name="米夏埃尔"]它讲述的，是丛林中茹毛饮血的野兽，有一日走到丛林边缘时，被远处传来的乐声吸引，并为之感动......
[charslot(slot = "r", name = "avg_npc_487_1#1$1", focus="r")]
[name="伊维格娜德"]于是它们收起獠牙，走出丛林，迎接了乐声的感召。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l",isCopy=true)]
[name="米夏埃尔"]（她明白我选曲的用意！而且看起来也很满意......太好了。）
[charslot(slot = "r", name = "avg_npc_487_1#1$1", focus="r")]
[name="伊维格娜德"]听听你对这首曲子的演绎吧。
[charslot(slot = "l", name = "avg_4109_baslin_1#1$2",focus="l",isCopy=true)]
[name="米夏埃尔"]是。请允许我代表鲁珀坎将接下来的演奏献给女皇陛下！
[Dialog]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[charslot]
[delay(time=1)]
[Background(image="44_g6_towerterrace",screenadapt="coverall")]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
来自鲁珀坎的叙事曲响彻高塔。高音活泼明快，低音温润顺从，年轻的狼向女皇收起了獠牙。
选曲无疑投了伊维格娜德所好。但是，为了进一步留下好印象，米夏埃尔在最后的低音号独奏中还留了一手。
一拍、二拍、三拍、四拍——所有乐器收声，米夏埃尔上前一步，开始了他经过刻苦练习、精妙绝伦的独奏。
这段独奏与原版听起来不一样。原版质朴而深情，但那配不上伊维格娜德对高贵华丽的喜好。
所以，米夏埃尔为它加入了触感完美的滑音，给每一个音区赋予更丰富的色彩。
看看这金碧辉煌的恩典高塔、随处飘舞的彩色锦缎，还有抬头就能欣赏的、铺满天际的晚霞——
华丽的音色和绚烂的演奏技巧与高塔主人的喜好正相合，它金光灿烂，它光辉圣洁，它——万幸，被完美地演绎了出来！
这全然不辜负他过去一年的准备！米夏埃尔的心激动得狂跳。他缓缓放下低音号，满心期待地偷看伊维格娜德的脸色。
[charslot(slot = "m", name = "avg_4109_baslin_1#7$2",focus="m")]
[name="米夏埃尔"]（太好了，她看起来仍然很亲切。）
[charslot(slot = "m", name = "avg_4109_baslin_1#1$2",focus="m")]
[name="米夏埃尔"]（...

... (全文13204字符)
```


> 本章节共371个脚本文件，此处展示前30个。

## 统计

- 总字符数：678326
- 对话行数：6070


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
