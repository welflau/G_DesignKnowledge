# 明日方舟 · 活动剧情 · act17d1（1段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act17d1」完整剧情脚本（1个文件，112行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act17d1
- 脚本文件数：1

### level_act17d1_entry

```
[HEADER(key="title_test", is_skippable=false, fit_mode="BLACK_MASK")] 
[ConsumeGuideOnStoryEnd(target="STAGE_ACTIVITY",subsignal="act17d1_entry",showAnyway=false)]
[Dialog]
[stopmusic]
[Blocker(a=1, r=0,g=0, b=0, fadetime=0, block=true)]
[Dialog]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4, crossfade=1, delay=0.5)]
[Background(image="bg_rhodescom",screenadapt="coverall",fadetime=1,block=true)]
[delay(time=1, black=true)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[dialog]
[PlaySound(key="$dooropenquite")]
[delay(time=1)]
[PlaySound(key="$rungeneral", volume=0.9)]
[delay(time=1)]
[Character(name="char_383_snsant_1",fadetime=1,blok=true)]
[Delay(time=2)]
[name="雪雉"]  我......我到了。
[Character(name="char_259_Jessica_1")]
[name="杰西卡"]  中午好。
[Character(name="char_383_snsant_1",name2="char_007_closre_1#5",focus=2)]
[name="可露希尔"]  雪雉妹妹你来了！欢迎欢迎！
[Character(name="char_007_closre_1")]
[name="可露希尔"]  那么人到齐了。
[name="可露希尔"]  这次是工程部的特殊委托哦。
[name="可露希尔"]  之前发生在萨尔贡的事情你们都应该听说过了。
[Character(name="char_259_Jessica_1")]
[name="杰西卡"]  是安全屋被袭击那回的事吗？
[Character(name="char_007_closre_1")]
[name="可露希尔"]  是的！
[name="可露希尔"]  这次是不幸中的万幸啦，没有罗德岛干员出事。
[name="可露希尔"]  但是为了避免再出现类似的情况呢，我认为罗德岛的安全屋还是需要更多的防御设备！
[name="可露希尔"]  所以工程部采购了一批全新的非致命防御武器，委托你们进行一次装备测试！
[Character(name="char_383_snsant_1")]
[name="雪雉"]  ......咦。
[name="雪雉"]  装备采购？
[name="雪雉"]  可是我这边没有收到物资检验的物料单？
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]  ......呃，那个......现场验收！
[name="可露希尔"]  总之，我需要登记一下雪雉妹妹你的工作资格证。
[Character(name="char_383_snsant_1")]
[PlaySound(key="$g_card_10cardsrelease")]
[name="雪雉"]  压力容器操作证书、源石设备使用证书、安全岗位认证证书、高空作业资格证书、电力设备使用证书......
[name="雪雉"]  都在这里了。
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]  优秀！雪雉妹妹真是可靠啊！
[name="可露希尔"]  我来登记一下。
[dialog]
[PlaySound(key="$g_card_10cardsrelease")]
[delay(time=1)]
[Character(name="char_383_snsant_1")]
[name="雪雉"]  那个......呃......
[name="雪雉"]  只是工程操作岗位......需要登记这么多证书么？
[Character(name="char_007_closre_1")]
[name="可露希尔"]  需要的，需要的，这会让你的工作能力显得更加可靠！
[Character(name="char_383_snsant_1")]
[name="雪雉"]  ......好吧。
[Character(name="char_007_closre_1")]
[name="可露希尔"]  很好，没问题了，那么明天就麻烦你们两个了。
[Character(name="char_259_Jessica_1")]
[name="杰西卡"]  好的。
[Character(name="char_383_snsant_1")]
[name="雪雉"]  ......感觉有点不放心。
[Dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=2, block=true)]
[Character]
[Character(name="char_007_closre_1#4")]
[Background(image="bg_aircraft",screenadapt="coverall",fadetime=1,block=true)]
[delay(time=1)]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[delay(time=1)]
[name="可露希尔"]  你们来了，好......
[dialog]
[character]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n")]
[Character(name="char_383_snsant_1",fadetime=2)]
[delay(time=2)]
[name="雪雉"]  这就是罗德岛的飞行器啊......我有点晕。
[dialog]
[character]
[delay(time=1)]
[Character(name="avg_npc_096",fadetime=2.2,block=false)]
[PlaySound(key="$sheildimpact",volume=0.2)]
[CameraShake(duration=0.3, xstrength=0, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[PlaySound(key="$sheildimpact",volume=0.2)]
[CameraShake(duration=0.3, xstrength=0, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[PlaySound(key="$sheildimpact",volume=0.2)]
[CameraShake(duration=0.3, xstrength=0, ystrength=20, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[name="杰西卡"]  为什么装备测试要来这么远的地方。
[Character(name="char_007_closre_1#4")]
[name="可露希尔"]  只有这种地方才能放开手做实验嘛！
[name="可露希尔"]  还有，你这是什么打扮啊。
[Character(name="avg_npc_096")]
[name="杰西卡"]  安全第一......
[dialog]
[character]
[delay(time=1)]
[Character(name="char_383_snsant_1")]
[name="雪雉"]  这是......废弃的移动城市地块？
[Character(name="char_007_closre_1")]
[name="可露希尔"]  是的，这是矿业平台的小型地块，不过上面除了废墟已经什么都没有了。
[name="可露希尔"]  这间废弃的双层建筑刚好适合拿来做测试，我准备好久了。
[Character(name="char_383_snsant_1")]
[name="雪雉"]  所以、所以......其他人呢？
[Character(name="char_007_closre_1")]
[name="可露希尔"]  什么其他人？
[Character(name="avg_npc_096")]
[name="杰西卡"]  还有其他人？
[Character(name="char_383_snsant_1")]
[name="雪雉"]  ......
[name="雪雉"]  杰西卡小姐，是测试人员对吧。
[Character(name="avg_npc_096")]
[name="杰西卡"]  是的。
[Character(name="char_383_snsant_1")]
[name="雪雉"]  那场地监督员，源石设备操作员呢。
[name="雪雉"]  还有安全评审员，工程负责人......
[name="雪雉"]  还有......
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]  有的，有的，都有，你放心吧。
[Character(name="char_383_snsant_1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="雪雉"]  我不放心啊！
[name="雪雉"]  可露希尔小姐！请把这次装备测试的申请书给我看一下！
[Character(name="char_007_closre_1#5")]
[name="可露希尔"]  ......哈哈哈......有这个必要么。
[Character(name="char_383_snsant_1")]
[name="雪雉"]  请 给 我 过 目。
[delay(time=1)]
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]  好吧......
[Character(name="char_383_snsant_1")]
[PlaySound(key="$g_card_10cardsrelease")]
[name="雪雉"]  ......
[name="雪雉"]  这上面......
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="雪雉"]  这上面怎么都是我的名字啊！
[name="雪雉"]  这违反规定了！可露希尔小姐！
[name="雪雉"]  而且这根本不是装备测试的申请书，这上面写的是地质勘探申请啊！
[Character(name="avg_npc_096")]
[name="杰西卡"]  ......凯尔希医生会生气的。
[Character(name="char_007_closre_1#2")]
[name="可露希尔"]  冷静点，你听我说。
[name="可露希尔"]  你看，雪雉妹妹，这里都写着你的名字，就说明......
[name="可露希尔"]  你可以拿五份工资哦！
[name="可露希尔"]  五份！
[Character(name="char_383_snsant_1")]
[name="雪雉"]  ......五......五份......
[Character(name="avg_npc_096")]
[name="杰西卡"]  这些设备真的可靠么......怎么看起来都摇摇欲坠的？
[Character(name="char_007_closre_1")]
[name="可露希尔"]  没问题，你看这些商标，都是雷神工业的产品，没有问题的。
[name="可露希尔"]  总之，你们先安放器材，我去楼下看看。
[dialog]
[PlaySound(key="$rungeneral")]
[delay(time=1)]
[character(fadetime=1)]
[delay(time=2)]
[MusicVolume(volume=0.2, fadetime=1)]
[Character(name="avg_npc_096")]
[name="杰西卡"]  ......
[name="杰西卡"]  这个雷神工业的商标，怎么歪歪扭扭的？
[name="杰西卡"]  这是什么？胶水？
[dialog]
[Character]
[delay(time=0.6)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_npc_096")]
[name="杰西卡"]  掉，掉下来了......
[name="

... (全文11100字符)
```


## 统计

- 总字符数：11100
- 对话行数：112


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
