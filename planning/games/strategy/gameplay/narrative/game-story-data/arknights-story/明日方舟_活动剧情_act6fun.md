# 明日方舟 · 活动剧情 · act6fun（1段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act6fun」完整剧情脚本（1个文件，100行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act6fun
- 脚本文件数：1

### level_act6fun_entry

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")] 
[stopmusic]
[Dialog]
[Background(image="bg_black",screenadapt="coverall",fadetime=2)]
[Delay(time=1)]
[PlayMusic(key="$babel_loop", volume=0.8, delay=0.2)]
[Delay(time=2)]
[name=""]   哦，是你。
[Dialog]
[name=""]   离我们上一次见面，已经过去了很久。
[name=""]   这段时间里......你一直徘徊在悬崖的边缘。
[Dialog]
[Delay(time=1.3)]
[name=""]   你可能已经忘记了你的身份，但你还记得那个名字，这就够了。
[Dialog]
[name=""]   ——好了，别在这里逗留太久。
[name=""]   毕竟，你既不是我的客人，也不应该出现在这里。
[name=""]   有许多人需要你。
[Dialog]
[Delay(time=1)]
[name=""]   4月1日。
[name=""]   你可能记不清这一天对你来说，究竟意味着什么。
[name=""]   这会让你陷入十分危险的处境。
[name=""]   ......
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Image]
[name=""]   不。
[name=""]   你必须想起来。
[Dialog]
[stopmusic(fadetime=2)]
[delay(time=2)]
[PlayMusic(intro="$ekg_loop", key="$ekg_loop", volume=0.5, delay=0)]
[Blocker(a=1, r=255, g=255, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[CameraEffect(effect="Grayscale", fadetime=0, keep=true, initamount=0, amount=1)]
[Image(image="bg_0_am", tiled=true, fadetime=0, block=false)]
[Blocker(a=0, fadetime=0.3, block=true)]
[CameraEffect(effect="Grayscale", fadetime=18, amount=0, block=false)]
[Delay(time=3)]
[name="模糊的声音"]   ......找到了......大箱子......打不开。
[name="电子音"]   请输入语音口令。
[name="模糊的声音"]   ......
[name="模糊的声音"]   “为了罗德岛”？
[name="电子音"]   口令错误。
[name="电子音"]   声纹认证失败。检测到非认证个体正在输入口令。
[name="电子音"]   疑似非法入侵。请立刻输入正确口令，否则自卫协议将启动，对入侵者进行驱逐。
[CameraEffect(effect="Grayscale", fadetime=8, amount=1, block=false)]
[name="模糊的声音"]   对了......出发前领袖......卡——
[name="模糊的声音"]   我有认证卡！
[name="电子音"]   口令错误，自卫协议即将启动。
[name="模糊的声音"]   怎么办......对了......把卡放上去！
[dialog]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[delay(time=2)]
[PlaySound(key="$d_avg_scan", volume=1)]
[Delay(time=1.5)]
[Dialog]
[CameraEffect(effect="Grayscale", fadetime=8, amount=0, block=false)]
[Delay(time=1)]
[name="电子音"]   认证通过，欢迎您。
[name="电子音"]   装置即将开启。
[Dialog]
[Delay(time=1)]
[name="模糊的声音"]   呼......好险......
[dialog]
[playsound(key="$d_avg_labamb", loop=false, channel="aa",volume=0.8)]
[stopSound(channel="aa", fadetime=3)]
[Delay(time=3)]
[name="模糊的声音"]   真的......人！
[Dialog]
[Delay(time=0.5)]
[StopMusic(fadetime=1)]
[PlaySound(key="$flashback", volume=0.3)]
[PlaySound(key="$e_atk_arrow_h", volume=0.2, Delay=0.4)]
[PlaySound(key="$flashback", volume=0.1, Delay=0.3)]
[PlaySound(key="$flashback", volume=0.2, Delay=0.7)]
[Blocker(a=1, r=255, g=255, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=1, r=159, g=254, b=255, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.1, block=true)]
[Blocker(a=0.8, r=255, g=96, b=15, afrom=1, rfrom=14, gfrom=0, bfrom=15, fadetime=0.2, block=true)]
[Blocker(a=0.8, r=0, g=0, b=0, afrom=0.8, rfrom=255, gfrom=96, bfrom=15, fadetime=0.3, block=true)]
[delay=0.5]
[Blocker(a=1, r=0, g=0, b=0, afrom=0, rfrom=0, gfrom=0, bfrom=0, fadetime=0.3, block=true)]
[delay=1]
[Blocker(a=1, r=225, g=225, b=225, afrom=1, rfrom=0, gfrom=0, bfrom=0, fadetime=2, block=true)]
[Image(fadetime=0)]
[Image(image="60_ifd01",x=150, y=250,xScale=1.4, yScale=1.4, fadetime=0)]
[name="？？？"]   ......
[Dialog]
[Blocker(a=0, r=1, g=1, b=1,  fadetime=10, block=false)]
[name="？？？"]   ......手！
[name="？？？"]   抓......紧！
[name="？？？"]   抓紧我的手！！
[Dialog]
[Delay(time=1)]
[Image(image="60_ifd01",x=-100, y=-50,xScale=1, yScale=1, fadetime=2)]
[delay(time=3)]
[CameraShake(duration=2, xstrength=10, ystrength=12, vibrato=15, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[stopmusic(fadetime=1)]
[ImageTween(xFrom=-100, yFrom=-50, xTo=0, yTo=0, xScaleFrom=1, yScaleFrom=1, xScaleTo=1, yScaleTo=1, duration=35, block=false)]
[Image(image="60_ifd02",x=-100, y=-50,xScale=1, yScale=1, fadetime=2)]
[delay(time=2)]
[name="？？？"]   ......
[Dialog]
[Blocker(a=1, r=1, g=1, b=1, fadetime=3, block=true)]
[Blocker(a=1, r=0, g=0, b=0,  fadetime=2, block=true)]
[Image(fadetime=2)]
[Delay(time=2)]
[name="？？？"]   喂，说句话，你还活着吗？
[dialog]
[charslot]
[Decision(options="......",values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "char_1002_nsabr_2")]
[name="？？？"]   好像死了。
[charslot(slot = "m", name = "char_1002_nsabr_1")]
[name="？？？"]   领袖不是教过我们紧急的心肺复苏方法吗？
[charslot(slot = "m", name = "char_1002_nsabr_2")]
[name="？？？"]   别吵，我正在回忆呢。
[name="？？？"]   先把人平放到地上。
[name="？？？"]   然后两只手一起按压他的胸口——
[dialog]
[PlaySound(key="$d_avg_punch",volume=0.9)] 
[PlaySound(key="$d_avg_bone_rub", volume=0.5)]
[CameraShake(duration=10, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[dialog]
[charslot]
[Decision(options="......（吃痛地呼吸）",values="1")]
[Predicate(references="1")]
[name="？？？"]   哦？好像有效果，再来！
[dialog]
[PlaySound(key="$d_avg_punch",volume=0.9)] 
[PlaySound(key="$d_avg_bone_rub", volume=0.5)]
[CameraShake(duration=10, xstrength=20, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=2)]
[dialog]
[charslot]
[Decision(options="......（试图抓住对方的手）",values="1")]
[Predicate(references="1")]
[name="？？？"]   再来！
[dialog]
[charslot]
[Decision(options="（猛烈地呼吸）",values="1")]
[Predicate(references="1")]
[Background(image="bg_indoor_1",fadetime=0, block=true)]
[delay(time=1)]
[image]
[PlaySound(key="$d_avg_clothmovement", volume=0.6)]
[Blocker(a=0, r=0, g=0, b=0,  fadetime=0.7, block=true)]
[charslot(slot = "l", name = "char_1002_nsabr_1",duration=1)]
[charslot(slot = "r", name = "char_1002_nsabr_2",duration=1)]
[delay(time=2)]
[PlayMusic(intro="$darkness01_intro", key="$darkness01_loop", volume=0.6, crossfade=1, delay=0.5)]
[charslot(slot = "r", name = "char_1002_nsabr_2",focus="r")]
[name="？？？"]   太好了，你醒了！
[dialog]
[charslot]
[Decision(options="你差点要了我的命！;（愤怒地咳嗽）;如果你再努力一点，我就真的死了。",values="1;2;3")]
[Predicate(references="1;2;3")]
[charslot(slot = "m", name = "char_1002_nsabr_2")]
[name="？？？"]   呃，抱歉，我以前没干过这事，对不起啊。
[dialog]
[charslot]
[Decision(options="你们是谁？",values="1")]
[Predicate(references="1")]
[charslot(slot = "m", name = "char_1002_nsabr_2")]
[name="？？？"]   我们？我们是整合运动。我是整合运动的成员，凯文。
[charslo

... (全文13740字符)
```


## 统计

- 总字符数：13740
- 对话行数：100


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
