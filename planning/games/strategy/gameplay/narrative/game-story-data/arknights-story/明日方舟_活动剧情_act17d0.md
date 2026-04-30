# 明日方舟 · 活动剧情 · act17d0（22段脚本）

> 来源：Kengxxiao/ArknightsGameData
> 原始链接：https://github.com/Kengxxiao/ArknightsGameData
> 分类：gameplay
> 标签：明日方舟, 塔防策略RPG, 活动剧情, 剧情脚本, 对话, 演出
> 游戏类型：塔防策略RPG

## 概述
明日方舟活动剧情「act17d0」完整剧情脚本（22个文件，2485行对话）

## 正文
## 章节信息

- 分类：活动剧情
- 目录：activities/act17d0
- 脚本文件数：22

### act17d0_01

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17d0_01关剧情
[PopupDialog(dialogHead="$avatar_shwazr6")] ……这不是普通的感染生物！
[PopupDialog(dialogHead="$avatar_rang")] 普通的感染生物可不会分裂出不同的个体。
[Tutorial(focusX=100, focusY=30, focusWidth=190, focusHeight=90,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",           protectTime=0.5, dialogHead="$avatar_shwazr6", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] ……这些<@tu.imp>变异的感染生物</>被击倒之后会<@tu.imp>分裂</>出其他个体，要小心！
[Tutorial(focusX=-75, focusY=-30, focusWidth=190, focusHeight=50,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="Top",          protectTime=0.5, dialogHead="$avatar_shwazr6", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 这些分裂的个体虽然<@tu.imp>不计入</>敌人进度中...
[Tutorial(focusX=80, focusY=-30, focusWidth=190, focusHeight=50,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black",anchor="Top",           protectTime=0.5, dialogHead="$avatar_shwazr6", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 但是当它们进入目标点时，仍然会<@tu.imp>扣除</>目标生命值，一定要注意！
[PopupDialog(dialogHead="$avatar_franka")] 这里到底发生什么事了……
```

### act17d0_03

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17d0_03关剧情
[PopupDialog(dialogHead="$avatar_rfrost")] 让他们再靠近一点！
[PopupDialog(dialogHead="$avatar_blitz")] 你有什么计划。
[PopupDialog(dialogHead="$avatar_rfrost")] 我在那些安全屋的爆炸物里找到了这个高装药炸弹。
[PopupDialog(dialogHead="$avatar_ash")] 这玩意…感觉能把我们都炸上天。
[Tutorial(focusX=-5, focusY=15, focusWidth=220, focusHeight=220,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="BottomRight",           protectTime=0.5, dialogHead="$avatar_rfrost", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 它的爆破范围相当大，除了能把范围内的<@tu.kw>敌人炸飞</>外，还能够<@tu.kw>损毁土堆</>开辟地形。
[Tutorial(focusX=-5, focusY=15, focusWidth=220, focusHeight=220,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="BottomRight",           protectTime=0.5, dialogHead="$avatar_rfrost", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 但启动它可不那么容易，部署后需要执行一段启动程序。在它启动之前，需要保证它<@tu.kw>不被敌人摧毁</>。
[PopupDialog(dialogHead="$avatar_ash")] 虽然很危险，但是现在没有其他选择。
[PopupDialog(dialogHead="$avatar_rfrost")] 炸弹部署完成后，我们就可以在<@tu.kw>任意时间引爆</>它了。
[PopupDialog(dialogHead="$avatar_ash")] 选择一个好位置把这“大家伙”给安好。
[PopupDialog(dialogHead="$avatar_ash")] 不要给敌人留下任何机会。
[PopupDialog(dialogHead="$avatar_rfrost")] 明白。
```

### act17d0_08

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17d0_08关剧情
[PopupDialog(dialogHead="$avatar_ash")] 这……到底是什么鬼东西。
[PopupDialog(dialogHead="$avatar_shwazr6")] 看起来像是某种感染生物……但是这种感染生物……
[PopupDialog(dialogHead="$avatar_shwazr6")] ……几乎是由源石组成的身体，这真的算是生物么。
[PopupDialog(dialogHead="$avatar_blitz")] 盖革计数器在响……这怪物身上有辐射。
[PopupDialog(dialogHead="$avatar_blitz")] 等等……他还在不断分裂。
[PopupDialog(dialogHead="$avatar_ash")] 这就是列维所谓的“科学的产物”？
[PopupDialog(dialogHead="$avatar_ash")] 不管用什么办法，不能让这个生物离开实验室。
[Tutorial(focusX=-5, focusY=15, focusWidth=220, focusHeight=220,           animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", anchor="BottomRight",           protectTime=0.5, dialogHead="$avatar_blitz", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] 你们坚持住……我去安装炸弹。
```

### level_act17d0_01_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_desert_1")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[delay(time=2)]
[Character(name="avg_npc_166",fadetime=1,block=true)]
[delay(time=1)]
[name="黑"]我回来了。
[Character(name="avg_npc_166",name2="char_503_rang",focus=2)]
[name="巡林者"]没什么问题吧？
[Character(name="avg_npc_166",name2="char_503_rang",focus=1)]
[name="黑"]前方三十公里范围内没有值得注意的目标，这片区域目前暂定是安全的。
[Character(name="char_503_rang")]
[name="巡林者"]很好，让老夫看看地图。
[name="巡林者"]嗯......
[name="巡林者"]方向不会有错，继续向北走，就能看到一个被本地人叫做喇叭山的地标。
[name="巡林者"]我们可以在山脚下休息，然后再向西走两天的路程，就能到达费坤。
[Character(name="avg_npc_166",name2="char_503_rang",focus=1)]
[name="黑"]费坤城是我们的目的地吗？
[Character(name="avg_npc_166",name2="char_503_rang",focus=2)]
[name="巡林者"]当然不是，但它是最合适的中转站。费坤有哥伦比亚人的大篷车商队，我们可以跟着商队一起去双河城，那边有罗德岛的办事处。
[name="巡林者"]只要到了办事处，就能想办法弄到交通工具，剩下的事情就很好办了。
[Dialog]
[Character]
[delay(time=1)]
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]太好了！终于可以结束这次徒步远征了，我的鞋底都要磨平了。
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]多在外面走一走对你的身体有好处，你也不用老惦记着减肥了。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]你！
[Dialog]
[Character]
[delay(time=1)]
[Character(name="avg_npc_166",name2="avg_npc_156_1#1",focus=1)]
[name="黑"]通讯器怎么样了，能联系到信号节点吗？
[Character(name="avg_npc_166",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]还是不行，看这个情况，直到费坤之前都很难和罗德岛本舰取得直接联系。
[name="雷蛇"]除非我们能弄到一个功率更大的发射器......
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]别想了，这附近没有其他移动城市。
[Character(name="char_503_rang")]
[name="巡林者"]是，到达费坤之前我们都很难得到补给，所以老夫之前让你们带上足够多的食物和水。
[name="巡林者"]我印象中这附近有其他小型聚落，但是这么多年了，这些城镇是否还在原来的地方，老夫可说不准。
[Dialog]
[Character]
[delay(time=1)]
[Character(name="avg_npc_156_1#1",name2="char_503_rang",focus=1)]
[name="雷蛇"]巡林者先生对这片区域很熟悉啊。
[Character(name="avg_npc_156_1#1",name2="char_503_rang",focus=2)]
[name="巡林者"]哈哈哈......老夫年轻的时候可能会更熟悉一点。其实这片荒地我已经很久没来过了。
[Character(name="avg_npc_156_1#1",name2="char_503_rang",focus=1)]
[name="雷蛇"]那张地图，是巡林者先生自己画的？
[Character(name="avg_npc_156_1#1",name2="char_503_rang",focus=2)]
[name="巡林者"]是，每个巡林者都会绘制自己的地图，只是我没想到这张地图现在还能用。这里的地貌没被天灾改变太多，算是我们运气好吧。
[Character(name="avg_npc_156_1#1",name2="char_503_rang",focus=1)]
[name="雷蛇"]很抱歉，这次又麻烦您了。
[Character(name="avg_npc_156_1#1",name2="char_503_rang",focus=2)]
[name="巡林者"]放宽心，照顾你们这些年轻人是老夫的职责所在。
[name="巡林者"]这次意外我也有责任。如果提前想好预备方案，就不至于如此狼狈了。
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]一群来历不明的雇佣兵袭击了仓库，又恰好抢走了我们的车？
[name="雷蛇"]这种故事，谁会信啊！？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]我怀疑那个商人是偷偷拆了我们的车拿去卖，然后随便编了个理由来糊弄。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]我难得同意你的观点。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]难得两个字很多余。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]以黑钢佣兵的习惯，放在以前我不会这么轻易饶了他。
[Character(name="char_503_rang")]
[name="巡林者"]但是以罗德岛干员的身份，老夫还是希望你们尽量不要和本地人发生冲突。
[name="巡林者"]药品安全送达，那个商人也没有在报酬上耍花招，我们也不能要求太多。
[Character(name="avg_npc_166")]
[name="黑"]但是提着一袋精炼源石锭徒步走在荒地上，实在是太危险了。
[Character(name="char_503_rang")]
[name="巡林者"]他们的解释充满漏洞，你也不能指望瓦伊凡的本地雇佣兵说实话，下一次老夫就得多长个心眼了。
[name="巡林者"]不过回去之后得向后勤报告一下财物损失。
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]唉......瓦伊凡就是这样的地方。
[Dialog]
[Character]
[delay(time=1)]
[Character(name="char_503_rang")]
[name="巡林者"]不过......
[name="巡林者"]就算没有地图和法术，老夫也能想办法找到方向，但是那样会耗费太多时间。我们人太多，水和食物坚持不了那么久。
[Character(name="avg_npc_166",name2="char_503_rang",focus=1)]
[name="黑"]在萨尔贡荒地中不依靠工具就能判断方向？您要如何做到呢？
[Character(name="avg_npc_166",name2="char_503_rang",focus=2)]
[name="巡林者"]以后有机会我可以教教你，都是经验而已。
[Dialog]
[Character]
[delay(time=1)]
[Character(name="avg_npc_155_1#1")]
[name="芙兰卡"]该怎么说呢......
[name="芙兰卡"]不愧是那位“红色山谷的游侠”。
[Character(name="char_503_rang")]
[name="巡林者"]哈哈哈哈，原来你们年轻人也会讲这些老故事。
[name="巡林者"]那只是个言过其实的称号。
[Character(name="avg_npc_155_1#1")]
[name="芙兰卡"]所以那些故事是真的吗？一天之内把詹金斯七兄弟全数抓捕归案，单枪匹马挡下整支锈锤劫匪纵队......
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]用一支箭击中十个目标，凌空射下拉特兰人的连发铳弹......
[Character(name="char_503_rang")]
[name="巡林者"]有趣，这些故事现在都变成这样了。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]黑钢的萨尔贡同行们偶尔会讲述巡林者的故事，大多都是这种风格的段子。
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]都是很适合写小说的题材。
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]黑小姐也听说过吧。
[Character(name="avg_npc_166")]
[name="黑"]......嗯......
[name="黑"]以前在哥伦比亚，一位走南闯北的佣兵讲过几个故事。
[name="黑"]叫做“血色山谷的弯刀”和“王酋之灾”。
[Character(name="char_503_rang#2")]
[name="巡林者"]......
[Dialog]
[delay(time=1)]
[Character(name="char_503_rang")]
[name="巡林者"]唔......这个就有点夸张了。
[name="巡林者"]巡林者不是你们想象的那种组织。
[name="巡林者"]老夫不知道你们都听到了什么样的传闻，但传播最广的故事多半都不是真的。
[name="巡林者"]巡林者不是专职战斗的组织，要我形容的话，更像是一群联合起来的荒野求生者。
[name="巡林者"]最开始他们只是几个苦陷于动荡年代的普通人，在战乱中挺身而出，保护那些被歹人劫掠的村落。
[name="巡林者"]他们不是训练有素的战士，而是在无法避免的战争与不见宁日的劫掠中诞生的反抗者。
[name="巡林者"]他们满腔怒火，他们拒绝对战乱岁月的残酷命运屈膝。
[name="巡林者"]后来，加入他们的人越来越多，组织也慢慢地从自治民兵演变成区域性团体，在荒地上向各大聚落提供医疗和防卫。
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]这部分我在黑钢的出勤记录里见过。在萨尔贡地区，除了官方队伍之外，巡林者也会追剿荒地中的歹徒与劫掠村落的佣兵。
[Character(name="char_503_rang")]
[name="巡林者"]那样的事情的确有过。
[name="巡林者"]那时候，巡林者的队伍里确实......有过那么几个好汉，也确实抓过几个歹人。你描述的事情发生过，但不是常态。
[name="巡林者"]大部分时间里，巡林者们只是帮镇子上的人修理水井、抵御野兽、搜集药品，就只是这些琐事。
[name="巡林者"]再加上，当年，这片区域还没被并入萨尔贡的领土......
[Character(name="avg_npc_155_1#2")]
[name="芙兰卡"]那么，巡林者老先生当年肯定是那些“好汉”中的一员了？
[Character(name="char_503_rang")]
[name="巡林者"]哈哈哈，老夫可没有那么威风，我只是个普通的斥候而已。
[Character(name="avg_npc_166")]
[name="黑"]......普通......？
[name="黑"]但是巡林者这个组织，最后还是解散了？
[Character(name="char_503_rang")]
[name="巡林者"]这就说来话长了......
[name="巡林者"]再后来，发生了很多事情。战争结束了，王酋们得到了他们想要的土地。
[name="巡林者"]对于萨尔贡王酋们来说，巡林者这类拒绝顺从的组织是不能被容忍的。
[name="巡林者"]当

... (全文9391字符)
```

### level_act17d0_01_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_desert_1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_166")]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="黑"]最后一只！
[Dialog]
[Character]
[delay(time=1)]
[Character(name="char_503_rang")]
[name="巡林者"]其他人呢！有人受伤么?
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]没问题。
[Character(name="avg_npc_155_1#1")]
[name="芙兰卡"]我这里也没问题。
[Character(name="char_503_rang")]
[name="巡林者"]通讯设备呢。
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]安全。
[Dialog]
[Character]
[delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[delay(time=1)]
[Character(name="char_503_rang")]
[name="巡林者"]这是地洞？......奇怪。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]这些怪物，看起来像是沙地兽。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]长成这样的沙地兽？两米多长？
[Character(name="char_503_rang")]
[name="巡林者"]......老夫在荒地里过了大半辈子，可没有见过会挖洞的沙地兽。
[Character(name="avg_npc_166")]
[name="黑"]......这些动物，身上都有源石结晶。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]......嗯......
[name="雷蛇"]会不会是源石污染导致的生物变异？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]这附近没有移动城市，没有工厂，没有矿山，怎么会有源石污染。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]有没有可能是天灾导致的？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]你太小看大自然了。野生动物远比我们熟悉天灾，也比我们更清楚如何回避源石污染。
[name="芙兰卡"]天灾能摧毁一座城市，但野生动物几乎不会受到影响——
[name="芙兰卡"]——这片大地的淘汰是无情的，一个物种如果做不到以自己的方式与源石共生，就不可能延续到现在。
[Character(name="avg_npc_166")]
[name="黑"]原来如此......我能想象。就像最常见的源石虫那样，体表外壳吸收了所有源石成分，内部的软体部分却完全纯净没有污染。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]说回来，PRTS的记录里有过类似案例吗？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]没有，就算是哥伦比亚铸铁城的那次泄漏事故也没有出现这种情况。
[Character(name="char_503_rang")]
[name="巡林者"]沙地兽是很胆小的生物，源石变异也不该如此剧烈地改变这一点。除非被法术影响，否则它们不会展现出攻击性。
[name="巡林者"]保持警戒，不要松懈。
[Character(name="avg_npc_166")]
[name="黑"]......法术？术师？我只希望这趟远路不要再节外生枝。
[Character(name="char_503_rang")]
[name="巡林者"]不用想太多，继续按照原定安排前进。
[Character(name="avg_npc_166")]
[name="黑"]明白。
[Dialog]
[Character]
[delay(time=1)]
[stopmusic(fadetime=1)]
[PlaySound(key="$transmission", volume=1)]
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]这是......罗德岛的紧急求援信号？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]是其他罗德岛的外勤队伍？
[Dialog]
[Character]
[delay(time=1)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1)]
[name="？？？"]......谢天谢......终于有人回应了！
[name="？？？"]......救......救命......请求支援......
[Dialog]
[Character]
[delay(time=1)]
[PlayMusic(intro="$nervous_intro", key="$nervous_loop", volume=0.4)]
[Character(name="avg_npc_156_1#2")]
[name="雷蛇"]这里是罗德岛外勤小队，收到请回复。
[Dialog]
[Character]
[delay(time=1)]
[name="？？？"]这里是......长泉......瞭望塔33......
[name="？？？"]......暴徒......正在......
[name="？？？"]......他们进来了！
[Dialog]
[Character(name="char_503_rang")]
[name="巡林者"]冷静一点！干员，出什么事了！
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]信号很差，断断续续的。
[Dialog]
[Character]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="？？？"]......救命......救......啊......
[Dialog]
[stopmusic]
[PlaySound(key="$transmission", volume=1)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="在一阵剧烈的噪音后，通讯中断了。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]......
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]这可麻烦了。
[Dialog]
[Character]
[delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Character(name="avg_npc_166")]
[name="黑"]瞭望塔33是什么意思？
[Character(name="char_503_rang")]
[name="巡林者"]听起来像是罗德岛的安全屋代号。
[Character(name="avg_npc_155_1#1")]
[name="芙兰卡"]安全屋？任务报告上没说过这附近还有安全屋啊。
[Character(name="char_503_rang")]
[name="巡林者"]......嗯......
[name="巡林者"]罗德岛确实会在一些偏僻的区域安插隐蔽安全屋，用于特殊外勤任务。
[Character(name="avg_npc_166")]
[name="黑"]但是我们不知道瞭望塔33在哪里。
[Character(name="char_503_rang")]
[name="巡林者"]长泉......长泉......
[name="巡林者"]这个名字，老夫有点印象，让我看看地图。
[name="巡林者"]嗯......
[name="巡林者"]应该是这里，沿着喇叭山向东走20公里就能看到另一个峡谷，峡谷附近确实有过一个小镇。
[name="巡林者"]当年小镇里有一口井，是这附近少数可靠的水源。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]所以就叫作长泉？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]所以接下来要怎么办，改变计划？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]也可以连夜赶往费坤，尝试联络办事处，寻求支援。
[Character(name="char_503_rang")]
[name="巡林者"]......恐怕安全屋的那位干员坚持不了这么久。
[name="巡林者"]你们继续前往费坤，想办法寻找支援。
[name="巡林者"]我去长泉看看情况。这片地方老夫很熟悉，一个人行动也比较灵活。
[name="巡林者"]如果情况太糟糕，我会去费坤与你们会合。
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]这......
[Dialog]
[Character]
[Character(name="avg_npc_166", name2="char_503_rang",focus=1)]
[name="黑"]我不赞同。
[Character(name="avg_npc_166", name2="char_503_rang",focus=2)]
[name="巡林者"]哦？
[Character(name="avg_npc_166")]
[name="黑"]沙地里钻出来的变异生物，安全屋的求救，说它们之间有联系可能显得太过多疑，但我们必须在萨尔贡荒地里保持警惕。
[name="黑"]在不清楚长泉镇周围情况的前提下，巡林者老先生您一个人去就更是太冒险了。
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]我也建议整队一起行动，状况不对我们也可以互相照应，掩护彼此撤离。
[Character(name="char_503_rang")]
[name="巡林者"]......嗯......
[name="巡林者"]你们说的有道理。
[name="巡林者"]这次老夫还是听你们的。我这一把年纪，确实也不该像年轻时那样孤身犯险了。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=

... (全文11182字符)
```

### level_act17d0_02_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[character(name="char_456_ash_1#5")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="灰烬"]任务记录第184天。
[name="灰烬"]截至目前为止，我们还是坚守在这个破屋子里。
[name="灰烬"]任务的第184天，到达前述破屋子的第27天。
[name="灰烬"]谁能相信我们已经在这个地方生活了184天。
[name="灰烬"]我们对这个世界依然毫无头绪。
[name="灰烬"]两周前，按照本地人的指引，我们从破烂屋子前往了另一个城镇。
[name="灰烬"]出发之前，镇子上的人说那是个“更发达的地方”，我不确定我们对发达一词的定义是否相同。
[name="灰烬"]结果呢？其实就是个土匪窝。
[name="灰烬"]没有电池，没有任何有价值的情报，甚至没有找到一个能正常沟通的人。
[name="灰烬"]当然，我们还是有点收获，蒂娜“弄”来了一辆车。
[name="灰烬"]过程充满坎坷，还消耗了我们本来就不多的弹药补给。
[name="灰烬"]在冲突中，车子也受损严重，开回破屋之后，这辆车就抛锚了。
[name="灰烬"]亚历山大试过修车，但这车连个加油口都没有，连带着也没发现油箱，发动机的构造完全弄不明白。
[name="灰烬"]他甚至到最后也不确定那个东西是不是发动机。
[name="灰烬"]唯一的好消息是，这辆车是左舵的。
[name="灰烬"]来到这个世界已经半年了，如今我们非常确信这里不是地球。
[name="灰烬"]我们抢车，枪战，就像是一群活在后启示录电影里的亡命徒。
[name="灰烬"]枪战这个词不够精确，那些长着蜥蜴尾巴的土匪甚至不用枪。
[name="灰烬"]他们能把十公斤重的投矛丢出去十几米远，能凭空丢出巨大的火球，用法介于手雷和火箭弹之间。
[name="灰烬"]这个世界实在是太异常了，异常到我已经不会再感到惊讶了。
[name="灰烬"]人的适应力往往超出了自己的预期，我们还得继续在这里挣扎求生。
[name="灰烬"]今天是我最后一次录音，我不打算再记录了。
[name="灰烬"]录音笔的内存快满了，电池也坚持不了多久。
[name="灰烬"]我们在这个世界上唯一能用的电源就是蒂娜的太阳能充电板，感谢这个世界上还有太阳。
[name="灰烬"]如果这块充电板损坏了该怎么办，如果我们的弹药补给都用完了该怎么办？
[name="灰烬"]说实话，我不知道。
[name="灰烬"]我依然对自己的当前生活缺乏实感，一切都发生得太过反常......又太过自然。
[name="灰烬"]回家的路在什么方向？
[stopmusic(fadetime=1)]
[Dialog]
[character]
[delay(time=2)]
[Background(image="bg_indoor4",fadetime=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[delay(time=2)]
[character(name="char_459_tachak_1")]
[name="战车"]来吧，乌曼，看看这个。
[name="战车"]嘿，你是不是不吃蔬菜。
[name="战车"]我翻翻这里还剩些什么......
[Dialog]
[character]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[character(name="char_456_ash_1#7",fadetime=1)]
[delay(time=2)]
[name="灰烬"]你在干什么？
[character(name="char_459_tachak_1")]
[name="战车"]哈！来见见乌曼，我的小家伙。
[character(name="char_456_ash_1#5")]
[name="灰烬"]你养了一只......这什么东西来着？
[character(name="char_459_tachak_1")]
[name="战车"]源石虫，本地人管这个东西叫源石虫。
[character(name="char_456_ash_1#7")]
[name="灰烬"]......
[name="灰烬"]你居然还有心思养这个？
[character(name="char_459_tachak_1")]
[name="战车"]不然呢，我每天干坐在屋顶上，总得找点事情做，总不能和机枪聊天吧。
[character(name="char_456_ash_1#6")]
[name="灰烬"]你的工作是警戒周围的安全，不是逗变种蜗牛玩儿。
[character(name="char_459_tachak_1")]
[name="战车"]你说的很有道理，但是警戒什么？是那些颤颤巍巍的病人，还是住在一公里开外，从来不靠近这边的镇民？
[name="战车"]这段时间里唯一靠近这栋破屋子的生物是一只会飞的蜥蜴，还算是给大家加餐了。
[character(name="char_456_ash_1#5")]
[name="灰烬"]......蒂娜和库兹呢？
[character(name="char_459_tachak_1")]
[name="战车"]他们去找那些病人交换物资了。
[name="战车"]蒂娜昨天又猎到了一些东西，她越来越熟练了。
[character(name="char_456_ash_1#5")]
[name="灰烬"]蒂娜又一个人出去打猎了？
[character(name="char_459_tachak_1")]
[name="战车"]当然，她可乐在其中，她最近在尝试抓一只“野生驮兽”。
[name="战车"]顺带，库兹去镇上了。
[name="战车"]还记得我从车上拆下来的那个玩意儿吗？库兹说他认识镇上的一个机械师，他想去问问。
[character(name="char_456_ash_1#5")]
[name="灰烬"]......好吧。
[character(name="char_459_tachak_1")]
[name="战车"]你太焦虑了，科恩。
[name="战车"]放松心态，反正我们短时间内都回不去了。
[name="战车"]学学库兹，去和那些人聊聊，这里的人还算友善。
[name="战车"]我还没学会本地人的语言，库兹这家伙，还真有两下子。
[stopmusic(fadetime=1)]
[character(name="char_456_ash_1#5")]
[name="灰烬"]这就是我担心的地方。
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[character(name="char_459_tachak_1")]
[name="战车"]担心什么？
[character(name="char_456_ash_1#5")]
[name="灰烬"]库兹和他们走得太近了，这不是好事，本地的氛围很不正常。
[name="灰烬"]这个镇子里矛盾重重，我们到这儿已经快一个月了，别告诉我你看不出来。
[name="灰烬"]一个躲在大宅里足不出户的当地政府负责人......哦，确切说法是“领主”，以及他那全副武装的私人卫兵们。
[name="灰烬"]还有这个“病人社区”。
[name="灰烬"]这整片区域都被同一个领主管辖，但病人不能居住在镇子里，其他镇民甚至不愿意靠近这边。
[name="灰烬"]他们是被赶到这边来的。
[character(name="char_459_tachak_1")]
[name="战车"]那是因为这些朋友们“得了怪病”。
[name="战车"]瘟疫肆虐的时候把病人关在一起，历史上又不是没发生过这种事，至少本地领主没有把这些病人都关在大牢里。
[character(name="char_456_ash_1#5")]
[name="灰烬"]源石病......还是矿石病？我不记得确切说法了。
[name="灰烬"]我们对这种病的了解仅限于：它和源石有关，它有传染性，它是不治之症。
[name="灰烬"]但它究竟是怎么在人和人之间传播的？不治之症具体又是怎么个病法？
[name="灰烬"]没人回答过我们相关的问题，所有人都觉得我们理应掌握基本状况。
[name="灰烬"]这种疾病要么是这座城镇的常识，要么就是这个世界的常识。
[name="灰烬"]如果只是与源石矿石的直接接触会导致问题，那我是不觉得这怪病有值得进行这种隔离的必要性。
[name="灰烬"]再说，医生也觉得我们与病人的接触频度和距离没有被感染的风险。
[name="灰烬"]这个病人社区就是没有围墙的监牢，病人和镇民互相憎恨彼此，你不用看都能感觉到。
[name="灰烬"]我的用词是“仇恨”，而不仅仅是排斥和歧视。仇恨刻在所有人的一举一动和一言一行里，是他们文化的一部分。
[name="灰烬"]仇恨。你明白我的意思吗？这不仅仅是未知疾病的问题了，我们不该卷进本地人的这种冲突里。
[name="灰烬"]假设一个场景吧，如果镇民们举着火把和草叉，冲到这些病人的家里，你打算怎么办，对他们开枪么。
[character(name="char_459_tachak_1")]
[name="战车"]那可不好说。
[name="战车"]这几个月来，我们的食物、饮水、药物可全都要感谢他们。
[name="战车"]在更早之前，我们颠沛流离，艰难跋涉，在荒野中被任何会动的东西攻击，文明的痕迹遍寻不得......直到得到他们的帮助。
[name="战车"]你觉得我们能够“置身事外”吗，科恩？
[name="战车"]如果他们拿着武器冲到米亚罗医生的诊所里，你难道要站在一边干看着？
[character(name="char_456_ash_1#6")]
[name="灰烬"]......
[character(name="char_459_tachak_1")]
[name="战车"]至于你刚才说的问题，我觉得传播性是不容忽视的。
[name="战车"]这世界里的所有人都像是接受过最专业的化学战训练，不论男女老少都随时懂得遮住自己的口鼻，他们对呼吸道保护有着极强的敏感性。
[name="战车"]我之前也反复提过这点，所以我们才一定要准备类似的防护......
[name="战车"]医生也认可我们保持距离的做法。所幸病人们对此没有任何意见，对他们来说，这应该也是常态。
[character(name="char_459_tachak_1",name2="char_456_ash_1#5",focus=2)]
[name="灰烬"]医生是怎么说的？
[character(name="char_459_tachak_1",name2="char_456_ash_1#5",focus=1)]
[name="战车"]我没问过他，大家都没问过他。
[name="战车"]每次和他聊到这个话题，他都很明显地表现出不想详谈的意愿，只要他觉得我们的防护措施没有问题，我也就不去追问了。
[Dialog]
[character(name="char_459_tachak_1",name2="char_456_ash_1#5")]
[delay(time=1)]
[stopmusic(fadetime=1)]
[PlaySound(key="$doorknockquite",volume=1)]
[delay(time=1)]
[character(name="char_459_tachak_1",name2="char_456_ash_1#10",focus=2)]
[name="灰烬"]嘘！
[character(name="char_459_tachak_1",name2="char_456_ash_1#6",focus=2)]
[name="灰烬"]......
[name="灰烬"]“我没有订披萨”。
[Dialog]
[character]
[name="？？？"]不用对口令了，科恩小姐。
[name="？？？"]是我，米亚罗。
[Dialog]
[character(name="char_459_tachak_1",name2="char_456_ash_1#5",focus=1)]
[name="战车"]说医生医生到。
[character(name="char_459_tachak_1",name2="char_456_ash_1#5",focus=2)]
[name="灰烬"]稍等，我给你开门。
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Dialog]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[characteraction(name="right", type="exit", direction="right",fadetime=2)]
[delay(time=2)]
[character]
[delay(time=1)]
[character(name="char_456_ash_1#5",name2="char_empty")]
[PlaySound(key="$dooropenquite",volume=1)]
[delay(time=2)]
[PlaySound(key="$d_gen_walk_n",volume=1)]
[cha

... (全文23314字符)
```

### level_act17d0_02_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_deserttownD")]
[character(name="char_456_ash_1#2")]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="char_456_ash_1#2")]
[name="灰烬"]停火！小心平民！
[character(name="char_459_tachak_1")]
[name="战车"]他们跑了，科恩！
[character(name="char_456_ash_1#2")]
[name="灰烬"]别管了，保护其他人！
[dialog]
[character]
[delay(time=1)]
[character(name="char_458_rfrost_1#2")]
[name="霜华"]来人帮帮忙，这边有人受伤。
[character(name="char_457_blitz_1#1")]
[name="闪击"]先把他们抬进去。
[character(name="char_456_ash_1#3")]
[name="灰烬"]医生！你还好吗！
[character(name="avg_npc_160_1#1")]
[name="米亚罗"]我在这儿！我没事！
[dialog]
[character]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="感染者镇民"]我的腿！我的腿断了！我的腿！
[dialog]
[PlaySound(key="$rungeneral")]
[Character(name="char_empty",name2="avg_npc_160_1#2",enter2="left",fadetime=2)]
[delay(time=2)]
[name="米亚罗"]冷静，你的腿还在，只是脱臼了，咬紧牙关。
[dialog]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[name="感染者少女"]妈妈......妈妈......
[dialog]
[PlaySound(key="$rungeneral")]
[characteraction(name="right", type="move", xpos=-400, fadetime=1,block=true)]
[delay(time=2)]
[name="米亚罗"]谁看到阿尔加的妈妈了！
[dialog]
[name="重伤的镇民"]救命......救......
[dialog]
[PlaySound(key="$rungeneral")]
[characteraction(name="right", type="move", xpos=400, fadetime=1,block=true)]
[delay(time=2)]
[name="米亚罗"]绷带要不够了......
[dialog]
[character]
[delay(time=1)]
[character(name="char_456_ash_1#2")]
[name="灰烬"]混账东西，*粗口*！
[character(name="char_457_blitz_1#1")]
[name="闪击"]那边是不是着火了？
[character(name="char_456_ash_1#2")]
[name="灰烬"]那个方向，是镇中心？
[character(name="char_459_tachak_1")]
[name="战车"]看来不只是这里遭到袭击。
[character(name="avg_npc_160_1#2")]
[name="米亚罗"]为什么，领主卫队去哪儿了？
[character(name="char_459_tachak_1")]
[name="战车"]别管什么领主卫队了。
[name="战车"]到处都是打斗声，事情变麻烦了，我们不能在这里逗留，这里太空旷了。
[name="战车"]先把那几个伤员抬到建筑后面！
[Character(name="avg_npc_163",name2="avg_npc_165",focus=2)] 
[name="感染者镇民"]怪物！怪物又来了！
[Character(name="avg_npc_163",name2="avg_npc_165",focus=1)] 
[name="感染者女性"]救命啊！ 
[character(name="char_456_ash_1#2")]
[name="灰烬"]没完没了！
[name="灰烬"]亚历山大！你去屋顶掩护我们！
[character(name="char_459_tachak_1")]
[name="战车"]明白。
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1",focus=1)]
[name="灰烬"]来不及了医生，我们必须离开这里。
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1",focus=2)]
[name="米亚罗"]可是我们能去哪儿？
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1",focus=1)]
[name="灰烬"]先去你的诊所。
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1",focus=2)]
[name="米亚罗"]那些感染者......
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1",focus=1)]
[name="灰烬"]别管那么多，先让所有人都去你的诊所。
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1",focus=2)]
[name="米亚罗"]......好。
[dialog]
[character(name="char_456_ash_1#2",name2="avg_npc_160_1#1")]
[delay(time=0.6)]
[PlaySound(key="$rungeneral")]
[characteraction(name="right", type="exit", direction="right",fadetime=1.5)]
[delay(time=2)]
[character(name="char_empty",name2="avg_npc_164")]
[delay(time=1.5)]
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[characteraction(name="right", type="move", ypos=-80, fadetime=1, block=true)]
[delay(time=1)]
[PlaySound(key="$rungeneral")]
[delay(time=1)]
[character(name="avg_npc_160_1#3",name2="avg_npc_164",enter="left",fadetime=1)]
[delay(time=1)]
[name="米亚罗"]来人搭把手！他走不动了！
[dialog]
[characteraction(name="left", type="move", xpos=220, fadetime=0.51, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", ypos=-50, fadetime=0.51, block=true)]
[delay(time=1)]
[characteraction(name="left", type="move", ypos=50, fadetime=0.8, block=true)]
[characteraction(name="right", type="jump",power=30,times=1, ypos=80, fadetime=1, block=true)]
[delay(time=2)]
[character]
[character(name="char_457_blitz_1#1",name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]库兹，你看看还有没有其他人躲在屋子里，再把这个社区的人都带到诊所去。
[name="灰烬"]注意安全！
[character(name="char_457_blitz_1#1",name2="char_456_ash_1#2",focus=1)]
[name="闪击"]明白。
[character(name="char_456_ash_1#2")]
[name="灰烬"]......
[dialog]
[delay(time=1)]
[name="灰烬"]......真是一场灾难。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[PlaySound(key="$rungeneral")]
[Character]
[Background(image="bg_indoor4")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="char_456_ash_1#2")]
[name="灰烬"]四十多个人......所有人都在这里了？
[character(name="avg_npc_160_1#3")]
[name="米亚罗"]是......
[name="米亚罗"]我们救下的人......都在这里了。
[character(name="char_456_ash_1#1")]
[name="灰烬"]少了多少人？
[character(name="avg_npc_160_1#3")]
[name="米亚罗"]不少人跑丢了，可能是去了镇子那边。
[character(name="avg_npc_160_1#1")]
[name="米亚罗"]但是有一些老人......他们来不及......
[character(name="char_457_blitz_1#3",name2="avg_npc_160_1#1",focus=1)]
[name="闪击"]别想了，不是你的错。
[name="闪击"]这些怪物，它们是从哪儿来的？它们是训练过的战兽吗？
[character(name="char_457_blitz_1#3",name2="avg_npc_160_1#1",focus=2)]
[name="米亚罗"]不知道......我以前没见过这种东西。
[character(name="char_456_ash_1#1")]
[name="灰烬"]那些暴徒掏出武器的时候，这些怪物就从地里钻出来了。
[Dialog]
[character]
[delay(time=1)]
[CameraShake(duration=1,ystrength=10, vibrato=10, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_atk_smg_h",volume=1)]
[delay(time=1)]
[CameraShake(duration=0.3,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$dooropenquite")]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_459_tachak_1",fadetime=0.7)]
[delay(time=2)]
[name="战车"]别管它们是从哪儿

... (全文17373字符)
```

### level_act17d0_03_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_cave_2")]
[character(name="avg_npc_158_1#1")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="德鲁奇"]铳？雇佣兵？
[name="德鲁奇"]你在说什么瞎话。
[character(name="avg_npc_007")]
[name="雇佣兵"]我说的全是真的，老大！他们拿着大型铳，贾曼被他们干掉了！
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]拿着大型铳的雇佣兵？萨科塔人？
[name="德鲁奇"]你是想告诉我，你们任务失败，是因为四个萨科塔人？
[character(name="avg_npc_007")]
[name="雇佣兵"]......呃......
[name="雇佣兵"]他们应该不是萨科塔人......大概？
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]不是萨科塔人但是拿着大型铳的佣兵？
[name="德鲁奇"]如果你要撒谎，你可以把故事杜撰得真实一点。
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]他说的是真的。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]什么意思？
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]他说的是真的，那几个武装人员确实不是萨科塔人。
[name="萨卡兹雇佣兵"]贾曼被打烂了脑袋，但是我没看到箭矢与弩弹，萨卡兹人可没有那么脆弱。
[name="萨卡兹雇佣兵"]这些人不在你的计划范围内。
[name="萨卡兹雇佣兵"]之前合同里可没提到我们还得对付一群全副武装拿着铳器的佣兵，老板，得加钱。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]那些佣兵现在在哪？
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]他们不在感染者社区了，我们的人在排查，没见到太大动静，应该还没离开镇子周边。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]......
[name="德鲁奇"]老混蛋那边的状况怎么样？
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]你父亲的手下都很厉害，尤其是你的妹妹。
[name="萨卡兹雇佣兵"]我们干掉了几个卫兵，但没能突破宅邸的防线。
[name="萨卡兹雇佣兵"]你那科学家的怪物干得不错，但是你找来的术师们就是废物，很多怪物折损得毫无意义。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]他们已经是我能雇到的术师里最靠谱的了。
[name="德鲁奇"]除非你们的老板愿意指派术师过来，不然抱怨也没用。
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]那就让你的科学家多造点怪物。
[name="萨卡兹雇佣兵"]或者换个战术，强行攻打大宅行不通。你家的大宅就是个要塞，你妹妹也不是省油的灯。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]老混蛋呢？他还是躲在屋子里？
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]我根本就没看到你的父亲，自始至终他都没有露面。
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]哈哈哈......我就知道。
[name="德鲁奇"]我就知道他出事了！
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]继续盯着大宅，有情况立刻告诉我。
[character(name="avg_npc_054")]
[name="萨卡兹雇佣兵"]关于我刚才提到的“换个战术”的部分，你的动作得快一点。
[name="萨卡兹雇佣兵"]这是萨卡兹佣兵的直觉。事情拖得越久，破绽就越多。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]我确实有备用计划，不过我需要时间来安排。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2")]
[Background(image="bg_lab")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#3",focus=2)]
[name="列维"]虽然我对自己的实验成果非常自信，但是从表情来看，你似乎没有类似的体验。
[name="列维"]来吧，说说看，又是哪个环节出岔子了。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#3",focus=1)]
[name="德鲁奇"]你需要加快一点进度。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]除了毫无意义的催促，你还能讲点更有建设性的意见吗？
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]我带给你的尸体够多了，我还需要至少二十只这种怪物。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]畸变体。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]什么？
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]“这种怪物”叫源石畸变体，它是有名字的。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]突变体、畸变体，我才不在乎这东西叫什么。
[name="德鲁奇"]我需要更多的怪物。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]我之前已经给你不少了，这么快就死光了？
[name="列维"]我很好奇......你的手下是怎么操纵畸变体的？依靠你们的“源石技艺”？
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#3",focus=2)]
[name="列维"]这算是什么？超能力？神秘学？法术？原理是什么？
[name="列维"]来吧，满足我的好奇心，我想和你手下的那些“术师”聊一聊。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#3",focus=1)]
[name="德鲁奇"]干好你的本职工作，学者。
[name="德鲁奇"]源石技艺不是你现在需要操心的事情。
[name="德鲁奇"]等事成之后，你有的是时间做你的研究。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]（俄语）我对你的事业还真没什么信心。
[name="列维"]不过说到时间，我有没有提醒过你？其实你的时间也不多。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]你什么意思？
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]这些源石畸变体的寿命不会超过一周，无论你想要做什么，动作都得快一点。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]你又在搞什么鬼！
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]这是代价，是你毫无耐心的代价。
[name="列维"]你想要高速制造这些畸变体，又想要它们孔武有力，你还希望它们没有任何缺点？
[name="列维"]你当真觉得天底下有这样的好事情？
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]......
[name="德鲁奇"]我说过，不要和我耍花招，学者。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=2)]
[name="列维"]我很忙，没时间和你开玩笑。
[name="列维"]既然你这么不满意，我建议你自己来，动用你的聪明才智，搞定我这个专业人士短时间无法解决的基因工程问题。
[name="列维"]当然，你也可以给我带来更多的材料，给我更多的时间，来为你无趣的“家庭伦理剧”添砖加瓦。
[name="列维"]科学是公平的，你总是有得选。
[Character(name="avg_npc_158_1#1",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]不要和我油嘴滑舌。
[Character(name="avg_npc_158_1#2",name2="avg_npc_157_1#2",focus=1)]
[name="德鲁奇"]继续你的工作，学者。如果你失败了，我不会饶了你。
[name="德鲁奇"]失败的代价就是惨死，很惨。我说到做到。
[Character(name="avg_npc_158_1#2",name2="avg_npc_157_1#3",focus=2)]
[name="列维"]哈哈哈，你把话说成这样，那我还能怎么接呢？
[name="列维"]祝你好运，我的朋友。
[Character(name="avg_npc_158_1#2",name2="avg_npc_157_1#3")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_desert_1")]
[Delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]浓烟四起，满地狼藉，不用靠近就能掌握大致状况了。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]没想到是这种规模的本地骚乱......
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]贸然介入一定会出问题。
[dialog]
[character]
[delay(time=1)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetim

... (全文20528字符)
```

### level_act17d0_03_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_safehouseoutdoorD")]
[Character(name="avg_npc_156_1#1",name2="avg_npc_007")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="avg_npc_156_1#2",name2="avg_npc_007",focus=1)]
[name="雷蛇"]雷鸣！
[dialog]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$lightning_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=0.7)]
[Character(name="avg_npc_156_1#2",name2="avg_npc_007",focus=2)]
[name="雇佣兵"]啊啊啊啊......我的眼睛！
[dialog]
[character]
[delay(time=0.6)]
[Character(name="char_empty",name2="avg_npc_054")]
[name="萨卡兹雇佣兵"]术师呢！干掉那个瓦伊凡！
[dialog]
[Character(name="avg_npc_155_1#1",name2="avg_npc_054",enter="left",fadetime=0.6)]
[delay(time=1)]
[name="芙兰卡"]想都别想。
[dialog]
[characteraction(name="left", type="jump", xpos=250, power=10, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=10, vibrato=30, randomness=20, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$p_imp_sword_n", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[characteraction(name="left", type="move", xpos=-100, fadetime=1,block=true)]
[characteraction(name="left", type="jump", xpos=100, power=10, times=1, fadetime=0.1,block=true)]
[CameraShake(duration=0.5, xstrength=40, ystrength=10, vibrato=30, randomness=20, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$p_imp_sword_n", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.1, block=true)]
[characteraction(name="left", type="move", xpos=-250, fadetime=1,block=true)]
[Delay(time=1)]
[CameraShake(duration=1, xstrength=3, ystrength=3, vibrato=10, randomness=90, fadeout=true, block=false)]
[Character(name="avg_npc_155_1#1",name2="char_empty",focus=1, fadetime=0.7)]
[PlaySound(key="$bodyfalldown1", volume=1)]
[dialog]
[Delay(time=1)]
[Character(name="avg_npc_054",name2="avg_npc_053",focus=2)]
[name="萨卡兹雇佣兵"]什么情况，又多了一批人？
[Character(name="avg_npc_054",name2="avg_npc_053",focus=1)]
[name="萨卡兹雇佣兵"]怎么搞的！
[Character(name="avg_npc_054",name2="avg_npc_053",focus=2)]
[name="萨卡兹雇佣兵"]情况不妙，这些人的火力太凶猛了。
[Character(name="avg_npc_054",name2="avg_npc_053",focus=1)]
[name="萨卡兹雇佣兵"]不要在这里节外生枝，先撤退。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_166",fadetime=0.7, focus=-1)]
[name="黑"]......我看见你了......
[dialog]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=1)]
[Character(name="avg_npc_054",name2="avg_npc_053",focus=2)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.04, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="right", type="move", ypos=-80, fadetime=0.7,block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[name="萨卡兹雇佣兵"]呃啊！
[delay(time=0.7)]
[Character(name="avg_npc_054",name2="avg_npc_053",focus=1)]
[name="萨卡兹雇佣兵"]小心狙击手！！
[dialog]
[characteraction(name="right", type="move", ypos=80, fadetime=0.7,block=false)]
[Character(name="avg_npc_054",name2="avg_npc_053",focus=2)]
[name="萨卡兹雇佣兵"]妈的，在哪？！！
[Character(name="avg_npc_054",name2="avg_npc_053",focus=1)]
[name="萨卡兹雇佣兵"]别找了，撤了！
[character(name="avg_npc_166",focus=-1)]
[name="黑"]......你跑不掉的。
[dialog]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=1)]
[Character(name="avg_npc_053")]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.04, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[characteraction(name="right", type="move", ypos=-80, fadetime=0.7,block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[name="萨卡兹雇佣兵"]呃......
[dialog]
[characteraction(name="middle", type="move", ypos=-80, fadetime=1,block=false)]
[PlaySound(key="$bodyfalldown3")]
[character(fadetime=0.5)]
[delay(time=2)]
[Character(name="avg_npc_007")]
[name="雇佣兵"]撤！快撤！别管了！
[dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[character(name="char_458_rfrost_1#4")]
[name="霜华"]他们跑了！
[character(name="char_456_ash_1#2")]
[name="灰烬"]报告情况！
[dialog]
[character]
[stopmusic(fadetime=1)]
[delay(time=1)]
[character(name="char_empty",name2="char_459_tachak_1")]
[delay(time=1)]
[character(name="char_457_blitz_1#1",name2="char_459_tachak_1",enter="left",fadetime=1)]
[delay(time=1)]
[character(name="char_457_blitz_1#1",name2="char_459_tachak_1",focus=1)]
[name="闪击"]亚历山大，你没事吧？
[character(name="char_457_blitz_1#1",name2="char_459_tachak_1",focus=2)]
[name="战车"]没事，皮外伤。
[name="战车"]这些家伙学聪明了。
[character(name="char_456_ash_1#2")]
[name="灰烬"]不要放松警惕！
[name="灰烬"]还有其他人在这。
[dialog]
[character]
[Dialog]
[Character(name="char_empty", name2="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[PlaySound(key="$d_gen_walk_n", volume=1,delay=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime

... (全文17035字符)
```

### level_act17d0_05_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_safehouseindoor")]
[character(name="char_456_ash_1#10")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="灰烬"]加油！Lord！
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[character(name="char_459_tachak_1")]
[name="战车"]嗯......嗯！！呃！
[delay(time=1)]
[character(name="char_456_ash_1#10")]
[name="灰烬"]差一点！还差一点！
[CameraShake(duration=1, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[character(name="char_459_tachak_1")]
[name="战车"]嗯......哈！
[delay(time=1)]
[name="战车"]拉上了！
[character(name="char_456_ash_1#5")]
[name="灰烬"]好样的！
[character(name="char_459_tachak_1",name2="char_503_rang",focus=2)]
[name="巡林者"]嗯......能徒手拉开这张弩，确实是一把好手。
[character(name="char_459_tachak_1",name2="char_503_rang",focus=1)]
[name="战车"]呼......
[name="战车"]这弩的设计也太夸张了，表面上根本看不出来有这么高的拉力。
[character(name="char_459_tachak_1",name2="char_503_rang",focus=2)]
[name="巡林者"]这种重弩是很常见的类型，大部分萨卡兹人都能徒手拉开。
[character(name="char_459_tachak_1",name2="char_503_rang",focus=1)]
[name="战车"]这种力道的重弩......100米以内威力不会比枪械小，就是用起来太费事了。
[name="战车"]......有关体能差异这件事，我之前已经领教过了。
[name="战车"]闹不好那个放电的姑娘力气都不比我小。
[character(name="char_459_tachak_1",name2="char_503_rang",focus=2)]
[name="巡林者"]你是说雷蛇吗？她毕竟是瓦伊凡，瓦伊凡确实是体格强壮的种族。
[character(name="char_459_tachak_1",name2="char_503_rang",focus=1)]
[name="战车"]嗯......
[dialog]
[character]
[delay(time=1)]
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]为什么突然对这些武器感兴趣了？
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]既然可预见的高频度战斗在前，现在确实得思考一下弹药用完后该怎么办了。
[name="战车"]没有子弹，枪械都是烧火棍。
[name="战车"]到时候总不能和他们肉搏吧，光从刚才的经历来看，我觉得就没什么胜算。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]还剩下多少？
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]我这边不多了，不到400发。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]给你看个东西。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]这是什么......子弹？
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]这是那位叫雷蛇的罗德岛干员使用的子弹，学名叫“蚀刻子弹”，据说是非常昂贵的产品。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]你已经拆开了？
[name="战车"]这子弹是什么结构啊，发射药呢？
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]就是这块结晶了。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]看着像是能量源，它是算发射药还是战斗部？
[character(name="char_503_rang")]
[name="巡林者"]老夫从前听拉特兰工匠讲过，每一发蚀刻子弹内都装着一块微型施术单元，这些施术单元都与拉特兰铳的结构相互对应。
[name="巡林者"]也就是说，不仅是铳器本身，就连它们发射的每一发蚀刻子弹都等同于术师的法杖，所以蚀刻子弹才会造价高昂。
[name="巡林者"]与之对应的源石技艺也复杂深奥，只有萨科塔人才会大量使用铳器，其他人则会选择更易于使用的远程武器。
[character(name="char_459_tachak_1")]
[name="战车"]拉特兰是国名，萨科塔是种族名，拉特兰人并不都是萨科塔......我明白了。
[name="战车"]但关于子弹的部分可真是个坏消息。
[name="战车"]这个世界上就没有什么普通枪械吗？不需要“源石技艺”的那种。
[character(name="char_503_rang")]
[name="巡林者"]......不需要源石技艺的铳械，老夫可从来没听说过。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]唉......
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]走一步看一步吧，至少那些爆炸物大家都能用。
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=2)]
[name="战车"]库兹他们在哪？
[character(name="char_456_ash_1#5",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]他们在地下室，还在尝试修复长得像无线电台的通讯器。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1")]
[Background(image="bg_safehouseindoor")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]通讯施术单元还是无法供能。
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]是能源的问题吗？
[Character(name="avg_npc_155_1#1",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]有可能......我得试试看。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac17_4",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="芙兰卡"]好了，你们躲开一点，优等生要开始表演了。
[name="雷蛇"]......充能准备......
[PlaySound(key="$lightning_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Image(image="avg_ac17_5",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1)]
[name="闪击"]喔！喔！喔！
[name="闪击"]这就是源石技艺？这效果也太酷炫了。
[name="灰烬"]真是......让人印象深刻。
[dialog]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image]
[Blocker(a=0, r=0,g=0, b=0, fadetime=2, block=true)]
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]好了吗？
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]启动了！
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=1)]
[name="芙兰卡"]干得漂亮，不愧是我的移动能源小姐。
[Character(name="avg_npc_155_1#2",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]你除了烦我，就没有别的事情做了吗！
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]......嗯......
[name="雷蛇"]不行，还是无法接通。
[name="雷蛇"]可能是晶体电子单元损坏太严重了，也可能是其他地方的电路有肉眼不易察觉的损坏。
[name="雷蛇"]这里也没有维修源石电路的专业设备，没法系统性地排查问题。
[Character(name="avg_npc_155_1#3")]
[name="芙兰卡"]唉，看起来是没戏了。
[dialog]
[character]
[delay(time=1)]
[character(name="char_459_tachak_1")]
[name="战车"]这种源石技艺什么的，普通人能学会吗？
[character(name="char_503_rang",name2="avg_npc_155_1#2",focus=2)]
[name="芙兰卡"]理论上说......绝大多数人经过培训之后都可以学会一定程度的源石技艺。
[name="芙兰卡"]只是源石技艺的学习需要付出心血与时间，而且也与天赋密切相关。
[name="芙兰卡"]很多人即便是付出了远超他人的

... (全文9906字符)
```

### level_act17d0_05_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_indoor4")]
[character(name="char_456_ash_1#2")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=0.51)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[delay(time=1)]
[character(name="char_458_rfrost_1#3")]
[name="霜华"]有发现吗？
[character(name="char_456_ash_1#9")]
[name="灰烬"]找到了！虽然量不多，但是有收获。
[character(name="char_503_rang")]
[name="巡林者"]很好，这些粮食加上安全屋的应急储备，应该能够省省勉强再过一个星期。
[character(name="char_456_ash_1#1")]
[name="灰烬"]时候不早了，先回去吧。
[dialog]
[character]
[delay(time=1)]
[stopmusic(fadetime=1)]
[CameraShake(duration=1.5, xstrength=10, ystrength=10, vibrato=20, randomness=70, fadeout=true, block=false)]
[PlaySound(key="$rungeneral")]
[delay(time=2.5)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[character(name="avg_npc_166")]
[name="黑"]......有人来了。
[character(name="char_503_rang")]
[name="巡林者"]有多少？
[character(name="avg_npc_166")]
[name="黑"]......十几个人，可能是雇佣兵。
[character(name="char_503_rang")]
[name="巡林者"]不要和他们缠斗。快！往安全屋方向！
[PlaySound(key="$rungeneral")]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_safehouseoutdoorN")]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_503_rang",fadetime=0.7)]
[delay(time=2)]
[name="巡林者"]他们还跟着？
[character(name="avg_npc_166")]
[name="黑"]......是的。
[character(name="char_503_rang")]
[name="巡林者"]不太对劲。
[character(name="char_456_ash_1#2")]
[name="灰烬"]我就知道这群人肯定不会善罢甘休。
[character(name="char_503_rang")]
[name="巡林者"]在这里战斗容易被包围，继续撤退。
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_safehouseindoor")]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[PlaySound(key="$dooropenquite")]
[delay(time=1)]
[Character(name="char_empty", name2="char_459_tachak_1")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_456_ash_1#2", name2="char_459_tachak_1",fadetime=0.7)]
[delay(time=1.5)]
[character(name="char_456_ash_1#2",name2="char_459_tachak_1",focus=2)]
[name="战车"]怎么了？
[character(name="char_456_ash_1#2",name2="char_459_tachak_1",focus=1)]
[name="灰烬"]追兵。准备战斗。
[character(name="avg_npc_166")]
[name="黑"]......不对。
[name="黑"]......不要开枪......
[character(name="char_459_tachak_1")]
[name="战车"]怎么了？
[character(name="avg_npc_166")]
[name="黑"]......他们不是那些雇佣兵。
[name="黑"]......是瑞柏巴军人......
[character(name="char_503_rang")]
[name="巡林者"]是本地卫兵？
[name="巡林者"]不要动手！
[dialog]
[character]
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac17_6",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="皮加尔"]卫兵，包围这个建筑！不要让任何人跑了。
[dialog]
[PlaySound(key="$rungeneral")]
[delay(time=1)]
[name="闪击"]等等，我们是不是被包围了。
[name="巡林者"]......情况不太妙。
[name="雷蛇"]领主卫队为什么要包围我们？
[name="巡林者"]你们先别说话。
[dialog]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_safehouseoutdoorN")]
[Image]
[character(name="avg_npc_159_1#2")]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[name="皮加尔"]躲在里面的人，听好了！
[name="皮加尔"]我是长泉镇卫兵队长，长泉镇领主之女皮加尔·图拉。
[name="皮加尔"]现在所有人都给我放下武器，乖乖地滚出来。
[name="皮加尔"]不要尝试挑战我的耐心，你们会后悔的。
[dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[CameraShake(duration=1, xstrength=10, ystrength=10, vibrato=30, randomness=90, fadeout=true, block=false)]
[Subtitle(text="魁梧的瑞柏巴战士用长戟柄端用力击打地面。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一瞬间，大地都在震动。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[name="皮加尔"]雇佣兵，又是雇佣兵。
[name="皮加尔"]你们这群无德无耻无信无义的恶徒！我那个恶贯满盈的兄弟到底给了你们多少金子？
[name="皮加尔"]你们逃不掉的，我要碾碎你们，我要击溃你们。
[name="皮加尔"]我要让你们为恶行付出代价。
[name="皮加尔"]等你们死在我刀下后，你们才会知道，再多脏钱也买不来第二条性命！
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_safehouseindoor")]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[character(name="char_457_blitz_1#1")]
[name="闪击"]喔！喔！你确定他们是来“帮忙”的？
[name="闪击"]这是要把我们挂在城门口吧。
[character(name="char_456_ash_1#2")]
[name="灰烬"]这就是我最担心的情况。
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[Character]
[Background(image="bg_safehouseoutdoorN")]
[Delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=1.5)]
[playSound(key="$d_gen_walk_n")]
[character(name="char_503_rang",fadetime=1)]
[delay(time=2)]
[name="巡林者"]这中间肯定是有什么误会。
[name="巡林者"]皮加尔大人。
[name="巡林者"]老夫是罗德岛外勤

... (全文19914字符)
```

### level_act17d0_06_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_nobleN")]
[character(name="avg_npc_158_1#2")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="德鲁奇"]我们有多久没见面了，我亲爱的妹妹？
[name="德鲁奇"]半年，一年，还是更久？
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]德鲁奇，你袭击领主卫队，攻占领主府邸，这是在谋反！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]谋反，哼，呵呵。
[name="德鲁奇"]你应该知道，皮加尔。
[name="德鲁奇"]如果不是老头子那腐朽的脑袋里还想着保护他那些感染的......啊，劣质资产。
[name="德鲁奇"]这位子根本轮不到你坐。
[name="德鲁奇"]冷静点，妹妹。
[name="德鲁奇"]看看这个，这些玩具来自一位哥伦比亚的热心赞助商。
[dialog]
[delay(time=0.6)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="狡猾的瑞柏巴敲了敲自己身后的设备。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]TSW-2号超声波冲击装置，高精尖工业产品，尚未投入实战的实验武器，唯一的缺点是尺寸太大。
[name="德鲁奇"]我把它藏在镇子里，可是花了不少时间。
[name="德鲁奇"]把你从大宅里骗出来，也花了我不少时间。
[name="德鲁奇"]所以我亲爱的妹妹，你那强大的武技起到什么作用了？你坚强的意志又起到什么作用了？
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]......
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]你再看看这些朋友，这些萨卡兹朋友。
[name="德鲁奇"]他们可不是那些死脑筋的魔族佬，他们同样来自哥伦比亚，他们为钱办事。
[name="德鲁奇"]你知道这代表着什么吗？
[name="德鲁奇"]他们代表着更先进的东西，是你和老头子永远都不会明白的东西。
[name="德鲁奇"]只要利润够高，金钱能汇聚的力量远超你的想象。
[name="德鲁奇"]老头子坚持的那些狗屁不通的道理，现在又到哪儿去了？
[character(name="avg_npc_007")]
[name="雇佣兵"]老大，我们在一间大房子里找到了这个。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]给我。
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]哦，巴耶勒王酋的领主委任书。
[name="德鲁奇"]细纹草纸，绣边签名，砖块一样的巴耶勒文，还有这黝黑盖章。
[name="德鲁奇"]哼。
[dialog]
[delay(time=1)]
[name="德鲁奇"]老头子呢？
[character(name="avg_npc_007")]
[name="雇佣兵"]没有，我们找遍了所有房间，大宅里只有一大群镇民，没看到你说的老头子。
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]父亲已经过世了，现在我就是长泉镇的领主。
[name="皮加尔"]你违抗领主，就是违抗王酋，你已经死罪难逃了！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]这就是你和那个老东西想出来的计谋？
[name="德鲁奇"]哈哈哈......
[name="德鲁奇"]哈哈哈哈哈......
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=0.3,xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$fightgeneral", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.03, block=true)]
[delay(time=1)]
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]唔呃！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]老东西真的是越来越蠢了。你们居然觉得依靠王酋就能将我一军，你真的是天真得可笑。
[name="德鲁奇"]死罪？
[name="德鲁奇"]老头子引以为豪的瑞柏巴卫队现在就躺在巷子里身首异处。
[name="德鲁奇"]最棘手的领主卫队已经没了，你觉得这里还有谁能管我？
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]你这个丧心病狂的废物！他们从小看着你长大！你竟然......
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]他们不该挡我的道。
[name="德鲁奇"]你也不该。
[name="德鲁奇"]看在我们血脉相连的份上，我就讲得再直白一点，便于你理解吧，妹妹。
[name="德鲁奇"]是，你现在是萨尔贡的领主，没错。
[name="德鲁奇"]而我呢？我只是一个被家族放逐的流浪汉。
[name="德鲁奇"]但过个几年，等到你不幸亡故，再由我亲自去一趟巴耶勒王廷。
[name="德鲁奇"]我既有血统，又带着矿产和大笔财富向王酋表忠心，你觉得他会不会把长泉镇重新分封给我？
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]你！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]我再好心地做一个假设，如果你上任没多久就在一场血战中丧生。
[name="德鲁奇"]我把你的遗体献给王酋，假若你有幸成为长生军的一员，我会不会因此获得更多好处？
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]德鲁奇，你这个卑鄙无耻的败类！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]别这么激动，妹妹。
[dialog]
[character]
[delay(time=1)]
[Character(name="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_166",blackstart=0.14,blackend=0.4,fadetime=0.7,focus=-1)]
[delay(time=1)]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]当然，前述内容都只是我的假设，假设不会成真，这只是兄妹谈心。
[name="德鲁奇"]因为我早就想好了更适合你的去处。
[name="德鲁奇"]看到这些身上带石块的东西吗？
[name="德鲁奇"]既然你那么愿意保护感染者，不妨就加入他们吧。
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]德鲁奇！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]等你因此而亡的时候，我会找个山洞把你填进去。
[name="德鲁奇"]这样，你和老头就能看着我是怎么把矿洞底下深藏的源石挖出来，让长泉镇变成整个巴耶勒的矿产中心。
[name="德鲁奇"]怎么，不说话了？
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]......你在出卖你的家族，出卖这片土地！我诅咒你，德鲁奇，你不得好死！
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]随你开心，我亲爱的妹妹，你想咒多久就咒多久，趁你还有本事说话。
[name="德鲁奇"]那就这样吧。
[dialog]
[character]
[delay(time=1)]
[character(name="char_empty",name2="avg_npc_158_1#1")]
[name="德鲁奇"]（哥伦比亚语）你，过来。
[dialog]
[Dialog]
[Character(name="char_empty", name2="avg_npc_158_1#1")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",focus=1)]
[name="萨卡兹雇佣兵"]（哥伦比亚语）老板，你说。
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",focus=2)]
[name="德鲁奇"]（哥伦比亚语）把那些感染者带到学者那边去。
[character(name="avg_npc_160_1#1")]
[name="米亚罗"]咳咳......咳......
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",focus=1)]
[name="萨卡兹雇佣兵"]（哥伦比亚语）好的，我把他们带给科学家。
[name="萨卡兹雇佣兵"]（哥伦比亚语）这个年轻人呢？看起来快不行了。
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",focus=2)]
[name="德鲁奇"]（哥伦比亚语）是死是活都带过去。
[name="德鲁奇"]（哥伦比亚语）至于我妹妹。
[name="德鲁奇"]（哥伦比亚语）把她变成感染者，你们萨卡兹人肯定知道怎么弄。
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",focus=1)]
[name="萨卡兹雇佣兵"]（哥伦比亚语）明白。
[name="萨卡兹雇佣兵"]（哥伦比亚语）不过这可不是合同规定的工作内容，得加钱。
[Character(name="avg_npc_053", name2="avg_npc_158_1#1",focus=2)]
[name="德鲁奇"]（哥伦比亚语）别那么多废话。往长远看，等我们的事成了，矿山运作起来，有的是钱可分。
[character(name="avg_npc_159_1#2",name2="avg_npc_053",focus=2)]
[name="萨卡兹雇佣兵"]你可真是有个好哥哥。
[character(name="avg_npc_159_1#2",name2="avg_npc_053",focus=1)]
[name="皮加尔"]（闭上了眼睛）
[character(name="a

... (全文24799字符)
```

### level_act17d0_06_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_nobleN")]
[Delay(time=1)]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="char_457_blitz_1#4")]
[name="闪击"]已净空！
[character(name="char_456_ash_1#2")]
[name="灰烬"]好的，警戒交给你了！
[name="灰烬"]亚历山大，看看躺在地上的雇佣兵还有没有人活着！
[character(name="char_459_tachak_1")]
[name="战车"]马上就办。
[character(name="char_456_ash_1#2")]
[name="灰烬"]蒂娜，把绷带拿来。我们清点人数，给伤员包扎一下。
[character(name="char_458_rfrost_1#3")]
[name="霜华"]好！
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="战车"]别装死！！
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=1)]
[name="雇佣兵"]等等，把......把铳口移开！我什么都说！
[dialog]
[delay(time=1)]
[character(name="char_459_tachak_1",name2="char_457_blitz_1#6",focus=1)]
[name="战车"]库兹，把他绑起来。
[character(name="char_459_tachak_1",name2="char_457_blitz_1#6",focus=2)]
[name="闪击"]好的。
[character(name="char_456_ash_1#2")]
[name="灰烬"]医生呢？米亚罗医生！
[character(name="avg_npc_166")]
[name="黑"]在这里！
[dialog]
[stopmusic(fadetime=1)]
[character]
[delay(time=1)]
[character(name="avg_npc_160_1#1")]
[name="米亚罗"]......咳......
[dialog]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="感染者少年躺在地上，随着他的每一次咳嗽，鲜血都顺着他浑身的大量伤口渗出。他全身裸露在外的皮肤都覆满了细密的源石结晶，这是近距离面对源石爆炸的直接结果。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="没有强烈的冲击波，没有击垮身体的暴风。但源石的诅咒从这次刺激中变得更为强烈，已经渗透了他的年轻身体。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="char_456_ash_1#2")]
[name="灰烬"]蒂娜！绷带！快！
[dialog]
[character]
[delay(time=1)]
[Dialog]
[Character(name="char_empty", name2="avg_npc_160_1#1")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_459_tachak_1", name2="avg_npc_160_1#1",fadetime=0.7)]
[delay(time=1.5)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[character(name="char_459_tachak_1",name2="avg_npc_160_1#1",focus=1)]
[name="战车"]保持清醒！小伙子，不要闭上眼睛！
[character(name="char_456_ash_1#3",name2="avg_npc_156_1#1",focus=1)]
[name="灰烬"]为什么......发生什么事了？
[character(name="char_456_ash_1#3",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]强行使用源石技艺......源石感染扩散了......
[character(name="char_456_ash_1#2",name2="avg_npc_156_1#1",focus=1)]
[name="灰烬"]罗德岛没有办法吗？你们不是最擅长这个吗？
[character(name="char_456_ash_1#2",name2="avg_npc_156_1#1",focus=2)]
[name="雷蛇"]失血、灼伤、矿石病剧烈发作，就算是在罗德岛本舰......
[dialog]
[character]
[delay(time=1)]
[character(name="char_459_tachak_1",name2="avg_npc_160_1#1",focus=2)]
[name="米亚罗"]......咳......
[character(name="char_459_tachak_1",name2="avg_npc_160_1#1",focus=1)]
[name="战车"]撑住，小伙子。
[character(name="char_459_tachak_1",name2="avg_npc_160_1#1",focus=2)]
[name="米亚罗"]......
[character(name="char_459_tachak_1",name2="avg_npc_160_1#1",focus=1)]
[name="战车"]......坚持住，你不是还想远游他乡吗？想想你梦中的哥伦比亚。
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="战车"]......坚持住！
[character(name="char_459_tachak_1",name2="avg_npc_160_1#1",focus=2)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="米亚罗"]咳咳......咳......
[name="米亚罗"]......咳......
[dialog]
[delay(time=1)]
[character(name="char_459_tachak_1",name2="char_empty",fadetime=1.5)]
[delay(time=2)]
[name="战车"]......
[delay(time=1)]
[character(name="char_456_ash_1#4")]
[name="灰烬"]......医生......
[character(name="char_458_rfrost_1#3")]
[name="霜华"]......他走了。
[character(name="avg_npc_166")]
[name="黑"]......抱歉，我没能......
[character(name="char_456_ash_1#4")]
[name="灰烬"]不......不是你的错。
[stopmusic(fadetime=1)]
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=2)]
[name="战车"]......
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=1)]
[name="雇佣兵"]......不......这和我没关系，我不是负责的！
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="战车"]*俄语粗口*，今天你别想活着出去。
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=1)]
[name="雇佣兵"]......我只是......别......
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=2)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="战车"]你完了，*俄语粗口*，你死定了。
[character(name="avg_npc_007", name2="char_459_tachak_1",focus=1)]
[CameraShake(duration=0.5, xstrength=15, vibrato=20, fadeout=true, block=false)]
[name="雇佣兵"]别！别打我！不是我干的！别！
[dialog]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$fightgeneral", volume=1)]
[delay(time=1)]
[character(name="char_457_blitz_1#4")]
[name="闪击"]亚历山大！别这样！冷静点！
[character(name="avg_npc_156_1#1")]
[name="雷蛇"]那个卫兵队长去哪儿了？就那位领主之女？
[character(name="avg_npc_166")]
[name="黑"]她追着逃走的人跑出去了，巡林者跟着她一起过去了，别担心。
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[character(name="avg_npc_156_1#2")]
[name="雷蛇"]等等......医生身上的结晶......在发光？
[character(name="avg_npc_155_1#1")]
[name="芙兰卡"]这？！
[name="芙兰卡"]这么快？为什么？
[character(name="avg_npc_166")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="黑"]！！
[character(name="avg_npc_156_1#2")]
[name="雷蛇"]别管这个了！找个房间！
[character(name="char_456_ash_1#3")]
[name="灰烬"]你们要做什么？
[character(name="avg_npc_155_1#1")]
[CameraShak

... (全文9185字符)
```

### level_act17d0_07_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_cave_2")]
[character(name="avg_npc_158_1#1",name2="avg_npc_007")]
[Delay(time=1)]
[PlayMusic(intro="$mist_intro", key="$mist_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_158_1#1",name2="avg_npc_007",focus=1)]
[name="德鲁奇"]混账东西。
[character(name="avg_npc_158_1#1",name2="avg_npc_007",focus=2)]
[name="雇佣兵"]头儿，接下来怎么办？
[name="雇佣兵"]头儿，我觉得还是先撤吧。
[character(name="avg_npc_158_1#1",name2="avg_npc_007",focus=1)]
[name="德鲁奇"]撤？我可还没输呢。
[name="德鲁奇"]领主卫队已经死光了，我只需要等待下一波反攻的时机。
[name="德鲁奇"]几个罗德岛的佣兵，不是我的对手。
[dialog]
[delay(time=1)]
[name="德鲁奇"]那个科学家呢?
[name="德鲁奇"]怎么一个人都没有。
[character(name="avg_npc_158_1#1",name2="avg_npc_007",focus=2)]
[name="雇佣兵"]这是什么味道。
[name="雇佣兵"]看着他的人去哪儿了？
[dialog]
[character]
[delay(time=1)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[character(name="avg_npc_157_1#3",fadetime=1.5)]
[delay(time=2)]
[name="列维"]看起来情况不是很顺利啊，朋友。
[name="列维"]让我猜猜看，就算是带着我强而有力的造物，你还是没有成功。
[name="列维"]说实话我真的一点都不感到意外。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]我没有那么多时间听你阴阳怪气。
[character(name="avg_npc_157_1#3")]
[name="列维"]那么依据你以往的风格，你又要更新的玩具，难怪你的父亲不喜欢你。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]少废话，我现在需要......
[character(name="avg_npc_157_1#3")]
[name="列维"]你在和我说话么，先生？
[name="列维"]那你至少要加上“请”这个字。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]什么？
[character(name="avg_npc_157_1#3")]
[name="列维"]你在求我帮你，你这是求人的态度？
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]你在耍我吗？
[character(name="avg_npc_157_1#2")]
[name="列维"]我看起来像是在开玩笑吗？
[character(name="avg_npc_007")]
[name="雇佣兵"]妈的，这个老东西，你找打。
[dialog]
[dialog]
[stopmusic(fadetime=0)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="雇佣兵"]啊啊啊啊啊啊！
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="雇佣兵"]这是什么！这是什么！
[name="雇佣兵"]我的头！我的头要炸了......我的......
[dialog]
[CameraShake(duration=0.5, xstrength=40, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[character]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[Dialog]
[delay(time=2)]
[character(name="avg_npc_158_1#1")]
[PlayMusic(intro="$tense_intro", key="$tense_loop", volume=0.4)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="德鲁奇"]你！你做了什么！
[character(name="avg_npc_157_1#2")]
[name="列维"]你们这类打手啊，除了一身蛮力，真的是什么素质都不具备。
[name="列维"]而你，先生，你真的以为，就靠这么几个智力低下的蠢货，就能把科学困在这里？
[name="列维"]去，让我们的赞助商大老爷冷静点。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_015",blackstart=0.14,blackend=0.4,name2="char_empty",fadetime=1)]
[delay(time=1)]
[name="畸变体感染者"]嘎......
[dialog]
[character(name="avg_npc_015",blackstart=0.14,blackend=0.4,name2="avg_npc_015",blackstart2=0.14,blackend2=0.4,fadetime=1)]
[delay(time=1)]
[name="畸变体感染者"]嗝......
[dialog]
[delay(time=1)]
[character]
[delay(time=1)]
[character(name="avg_npc_158_1#1")]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="德鲁奇"]这是什么东西！
[character(name="avg_npc_157_1#3")]
[name="列维"]认不得了？这是你的手下。
[name="列维"]当然，现在它们更厉害了，也更听话了。
[name="列维"]马上你也会加入它们。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]为什么你可以操纵这些怪物，你明明不会源石技艺！
[character(name="avg_npc_157_1#3")]
[name="列维"]只有源石技艺才可以操纵它们？你们这些人思维如此狭隘。
[name="列维"]你有没有思考过为什么所谓的“源石技艺”可以控制“感染生物”。
[name="列维"]当然，以你的智商无法得出这个问题的答案。
[dialog]
[delay(time=0.7)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="癫狂的科学家捋起了大衣的袖子。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="一块肿胀的源石瘤在他的胳膊上抽搐着。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="仿佛是一个独立的活物。", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_157_1#2")]
[name="列维"]只要成为它们的一部分，你自然就能和这些生物沟通，我们相处得很融洽。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]......你真是个无药可救的疯子。
[name="德鲁奇"]我可是图拉家族的人，我继承了图拉家族的神民血脉。
[name="德鲁奇"]你敢在巴耶勒王酋的领土上谋杀贵族，你找死。
[character(name="avg_npc_157_1#1")]
[name="列维"]王酋？贵族？血脉？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[name="列维"]哈哈......
[delay(time=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="列维"]哈哈哈哈哈哈哈哈。
[delay(time=1)]
[name="列维"]很有幽默感，德鲁奇先生。
[name="列维"]但是这个笑话有点过时。
[name="列维"]“我不曾鄙夷猪猡，唯独憎恶高挂枝头的金冠。”
[name="列维"]在我的祖国，人们烧死了主教，吊死了国王，砍了皇帝的脑袋，将旧日的一切权贵砸得稀烂，不会有人再惧怕所谓的王侯贵族。
[name="列维"]什么王酋，什么血脉。
[name="列维"]你在我眼里屁都不是。
[name="列维"]你这身臭皮囊，还不如那些矿石病患者有用。
[name="列维"]你把那些矿石病患者叫作什么来着？
[name="列维"]哦对，感染者。
[name="列维"]感染者能为我的实验做出贡献，而你呢？
[name="列维"]你的身份毫无意义，你的短视让我瞠目结舌。
[name="列维"]无能的废物。
[name="列维"]就你这种卑劣愚蠢的坏东西，居然还自称“贵族”。
[name="列维"]你有什么“高贵过人”的地方。
[name="列维"]但也不用担心，我和你的腐朽观念很不一样......我是一位科学家，我追求的是客观存在的真理。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]你想干什么？
[character(name="avg_npc_157_1#3")]
[name="列维"]科学对所有人都很公平，不会因为你的出身而改变。
[name="列维"]贵族、平民，当你躺在手术台上，当柳叶刀划开皮肤，所有人的价值和贡献都是一样的。
[name="列维"]在你的个人案例里，当你献身科学时，你可能会比现在要略微更加高贵一点。
[name="列维"]你应该感到荣幸。
[character(name="avg_npc_158_1#1")]
[name="德鲁奇"]你这个可耻的叛徒！
[character(name="avg_npc_157_1#2")]
[name="列维"]叛徒？叛徒？
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[character(name="avg_npc_157_1#1")]
[name="列维"]哈哈哈哈哈哈哈哈......
[name="列维"]你向你

... (全文10879字符)
```

### level_act17d0_07_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_nobleD")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]滚开！
[dialog]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[PlaySound(key="$e_skill_skulsrsword", volume=1)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]真是没完没了。
[dialog]
[character]
[delay(time=1)]
[character(name="char_459_tachak_1#2")]
[CameraShake(duration=1,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_atk_smg_h",volume=1)]
[delay(time=0.51)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[name="战车"]他们到底造了多少这种鬼东西！
[dialog]
[character]
[delay(time=0.6)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
[character(name="char_503_rang")]
[name="巡林者"]雷蛇！小心身后！
[character]
[name="源石畸变体"]噶......
[dialog]
[Character(name="avg_npc_156_1#2",name2="char_empty",focus=1)]
[name="雷蛇"]！！
[dialog]
[Character(name="avg_npc_156_1#2",name2="avg_npc_155_1#1",focus=2,enter2="right",fadetime=0.7)]
[name="芙兰卡"]小心！
[delay(time=0.7)]
[dialog]
[characteraction(name="right", type="jump", xpos=-250, power=0, times=1, fadetime=0.3, block=true)]
[CameraShake(duration=0.5, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[PlaySound(key="$fightgeneral",volume=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.05, block=true)]
[characteraction(name="left", type="exit", direction="left",fadetime=1, block=true)]
[delay(time=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[character(fadetime=0.7)]
[delay(time=1)]
[CameraShake(duration=0.5, xstrength=15, ystrength=15, vibrato=20, randomness=70, fadeout=true, block=false)]
[PlaySound(key="$bodyfalldown3")]
[delay(time=1)]
[Character(name="avg_npc_156_1#2")]
[name="雷蛇"]芙兰卡！
[name="雷蛇"]你在搞什么！
[name="雷蛇"]领主小姐，帮我搭把手！
[character(name="avg_npc_159_1#1")]
[name="皮加尔"]好，好的!
[dialog]
[character]
[delay(time=0.7)]
[Character(name="char_empty",name2="avg_npc_155_1#1")]
[PlaySound(key="$rungeneral")]
[delay(time=0.7)]
[Character(name="avg_npc_156_1#2",name2="avg_npc_155_1#1",enter="left",fadetime=1)]
[delay(time=1)]
[Character(name="avg_npc_156_1#2",name2="avg_npc_155_1#1",focus=2)]
[name="芙兰卡"]你......快跑。
[Character(name="avg_npc_156_1#2",name2="avg_npc_155_1#1",focus=1)]
[name="雷蛇"]你不要说话了！
[Character(name="avg_npc_156_1#2",name2="avg_npc_155_1#1",focus=2)]
[name="芙兰卡"]我的腿......你......你，别管我了。
[Character(name="avg_npc_156_1#2",name2="avg_npc_155_1#1",focus=1)]
[name="雷蛇"]不要说蠢话！
[dialog]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=true)]
[delay(time=1)]
[name="雷蛇"]我背你，快上来。
[character(name="avg_npc_159_1#2")]
[name="皮加尔"]它们又冲上来了！
[dialog]
[character]
[delay(time=0.51)]
[character(name="char_459_tachak_1#2")]
[CameraShake(duration=1,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_atk_smg_h",volume=1)]
[delay(time=0.51)]
[name="战车"]趁现在，快跑！
[character(name="avg_npc_012")]
[name="奥克芬"]到这来！
[Character(name="avg_npc_156_1#2")]
[name="雷蛇"]奥克芬先生！你怎么上来了！
[character(name="avg_npc_012")]
[name="奥克芬"]我实在是做不到待在下面干等着，我可也是罗德岛干员啊！
[Character(name="avg_npc_156_1#1")]
[name="雷蛇"]太好了！帮大忙了！
[character(name="char_503_rang")]
[name="巡林者"]准备引爆爆炸物......
[name="巡林者"]三、二、一......
[dialog]
[character]
[delay(time=1)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=2.5)]
[character(name="char_503_rang",name2="char_empty")]
[PlaySound(key="$rungeneral")]
[delay(time=1)]
[character(name="char_503_rang",name2="char_459_tachak_1#2",enter2="right",fadetime=1)]
[delay(time=1)]
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]怎么样了？
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]只是短暂被击退，用不了多久它们还会再来的。
[character(name="char_458_rfrost_1#3")]
[name="霜华"]它们......好像变少了一点？
[name="霜华"]“迎宾踏垫”已经用完了，我也没有子弹了。
[character(name="char_458_rfrost_1#3",name2="char_459_tachak_1#2",focus=1)]
[name="霜华"]亚历山大，接下来怎么办？
[character(name="char_458_rfrost_1#3",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]去避难所。
[character(name="char_458_rfrost_1#3",name2="char_459_tachak_1#2",focus=1)]
[name="霜华"]什么？
[character(name="char_458_rfrost_1#3",name2="char_459_tachak_1#2",f

... (全文10850字符)
```

### level_act17d0_08_beg

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_labentrance")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_456_ash_1#2",fadetime=0.7)]
[delay(time=2)]
[name="灰烬"]巡林者的地图只画到这里了。
[name="灰烬"]接下来就只能靠我们了。
[character(name="char_457_blitz_1#4")]
[name="闪击"]这个洞穴......没想到这么大。
[name="闪击"]这么来看，整个镇子的地下都是空的？
[character(name="avg_npc_166", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]爆炸物没问题吧？
[character(name="avg_npc_166", name2="char_456_ash_1#2",focus=1)]
[name="黑"]......安全屋里威力最大的那一批都在这里了。
[character(name="avg_npc_166", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]希望Lord的计划有效。
[character(name="avg_npc_166", name2="char_456_ash_1#2",focus=1)]
[name="黑"]恐怕没有那么简单，看那边......
[character(name="avg_npc_166", name2="char_456_ash_1#1",focus=2)]
[name="灰烬"]......希望不是我想的那种......
[dialog]
[character]
[delay(time=1)]
[stopmusic(fadetime=1)]
[character(name="avg_npc_015",blackstart=0.14,blackend=0.4,fadetime=1)]
[delay(time=1)]
[name="畸变体感染者"]嘎......
[dialog]
[character]
[delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[character(name="char_457_blitz_1#4")]
[name="闪击"]这是......人？
[character(name="avg_npc_015",blackstart=0.14,blackend=0.4)]
[name="畸变体感染者"]呃......
[character(name="avg_npc_166")]
[name="黑"]不管它是什么，它会死，就够了。
[character(name="char_457_blitz_1#4")]
[name="闪击"]现在不管出现什么鬼东西我都不会觉得奇怪了......
[character(name="char_456_ash_1#2")]
[name="灰烬"]不要缠斗，尽量突破，我们没有时间浪费在这里！
[character(name="char_457_blitz_1#4")]
[name="闪击"]明白。
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=0.5)]
[PlaySound(key="$lightning_n")]
[CameraShake(duration=0.7, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Background(image="bg_labcorridor")]
[Delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="avg_npc_166",fadetime=0.7)]
[delay(time=2)]
[name="黑"]......为什么长泉的地下会有一个这样的设施？
[dialog]
[character]
[delay(time=1)]
[Character(name="char_empty", name2="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[characteraction(name="right", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[characteraction(name="right", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",fadetime=0.7)]
[delay(time=1.5)]
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=1)]
[name="闪击"]科恩......这里是？
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]我就知道！我*粗口*就知道！
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=1)]
[name="闪击"]原来大部分实验室都被传送到这里了。
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]现在想想，都是我们太大意了。
[name="灰烬"]在这个镇子上生活了这么久，竟然毫无察觉。
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=1)]
[name="闪击"]这件事情的背后，就是那个疯子......
[dialog]
[delay(time=1)]
[character(name="char_457_blitz_1#4")]
[name="闪击"]这是什么味道......
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]还能是什么，死亡的味道。
[character(name="avg_npc_166")]
[name="黑"]......
[character(name="char_456_ash_1#2")]
[name="灰烬"]保持警惕，跟紧点。
[character(name="char_457_blitz_1#4")]
[name="闪击"]这都是什么？
[name="闪击"]笼子？这么多笼子？
[character(name="avg_npc_166")]
[name="黑"]全都是尸体......人和动物混在一起......
[character(name="char_456_ash_1#2")]
[name="灰烬"]这都是列维•克里奇科的杰作，此人的疯狂和残忍超乎常人想象。怪我当初还想过活捉，就应该一枪打穿他的脑门。
[character(name="char_457_blitz_1#4")]
[name="闪击"]一般的疯子还做不到这么恐怖的事情。
[character(name="avg_npc_166")]
[name="黑"]等等。
[name="黑"]......笼子里有个活人。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]呵。
[name="德鲁奇"]看看谁来了？
[dialog]
[character]
[delay(time=0.6)]
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]......
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=1)]
[name="闪击"]是那个德鲁奇。
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]这混账东西就是烧成灰我也认得。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]啊，是你们，是那群雇佣兵。
[name="德鲁奇"]很高兴看到你们。
[name="德鲁奇"]我知道我们之前有过很多矛盾......但是这些矛盾都可以搁置一边。
[name="德鲁奇"]我猜你们要找那个学者......我知道他在哪。
[name="德鲁奇"]我们现在有一个共同的敌人，在这件事上我们应该能够合作。
[dialog]
[character]
[delay(time=0.6)]
[character(name="char_456_ash_1#2")]
[name="灰烬"]这人的脸皮厚得让我感到恶心。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_158_1#2")]
[name="德鲁奇"]那边那个菲林，我知道你。
[name="德鲁奇"]你的身手还是很好认的，哥伦比

... (全文18005字符)
```

### level_act17d0_08_end

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_lab")]
[Delay(time=1)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="巨大的球形生物崩裂分解，变成了散落一地的蠕动块状物，这些奇诡的活物还在扭动翻腾，它们拒绝着死亡。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name="avg_npc_166")]
[name="黑"]这东西还在动！
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=1)]
[name="闪击"]炸弹部署完了，我们得撤了！
[name="闪击"]它......好像在重生？
[name="闪击"] 这东西......到底算什么生物？
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]不管它是什么，这东西都不应该存在于这个世界上。
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#2",focus=1)]
[name="闪击"]我们得撤了，要赶在炸弹爆炸之前跑出去。
[character(name="avg_npc_166")]
[name="黑"]走这边！
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=2)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_nobleD")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[Delay(time=2)]
[character(name="char_459_tachak_1#2")]
[CameraShake(duration=0.8,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_atk_smg_h",volume=1)]
[delay(time=0.51)]
[CameraShake(duration=0.8,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_atk_smg_h",volume=1)]
[delay(time=0.51)]
[CameraShake(duration=0.8,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$p_atk_smg_h",volume=1)]
[delay(time=1)]
[CameraShake(duration=0.2,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=0.51)]
[CameraShake(duration=0.2,ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[character(name="char_459_tachak_1#2")]
[name="战车"]我没子弹了。
[name="战车"]巡林者？
[character(name="char_503_rang#2")]
[name="巡林者"]我还在......
[character]
[dialog]
[delay(time=1)]
[Character(name="char_503_rang#2", name2="char_empty")]
[PlaySound(key="$rungeneral", volume=1)]
[characteraction(name="right", type="move", xpos=200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="right", type="move", xpos=-200, fadetime=1, block=false)]
[Character(name="char_503_rang#2",name2="char_459_tachak_1#2",fadetime=0.7)]
[delay(time=2)]
[character(name="char_503_rang#2",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]你的情况看起来可不太好。
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]老了，老了......呼......
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]你的手怎么了？
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]刚才没躲开，小问题。
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]现在怎么办？要去避难所吗？
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]矿洞那边，还没消息吗？
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]没有。
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]哈哈哈......
[name="巡林者"]老夫也没想到我们能坚持这么久......不过也快到极限了。
[Dialog]
[Character]
[Delay(time=1)]
[character(name="char_459_tachak_1#2")]
[delay(time=1)]
[playsound(key="$p_imp_blunt_h")]
[CameraShake(duration=0.4, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[playsound(key="$sheildimpact",volume=0.6)]
[CameraShake(duration=0.4, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[playsound(key="$p_imp_blunt_h",volume=0.8)]
[CameraShake(duration=0.4, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=true)]
[delay(time=1)]
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]你在干什么？
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]弄一面盾牌，我其实早想这么试试了。
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]哈哈哈......
[character(name="char_503_rang")]
[name="巡林者"]这就像是回到了过去，那些有关荣耀的美好时光。
[name="巡林者"]年轻的巡林者们集结在镇子的入口。
[name="巡林者"]明知道大军压境，明知道在战争之后他们中很多人都会血洒这片荒地之上。
[name="巡林者"]但是他们有说有笑，高呼着战歌，仿佛敌人是不堪一击的虫豸。
[name="巡林者"]战争残忍无情，有人退缩了，更多人决定死守到底。
[name="巡林者"]倒下的人成为了传奇，站着的人负责铭记他们的一切。
[name="巡林者"]最后站着的那个人，也慢慢开始畏惧死亡了。
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]因为他不想忘记那些倒下的人？
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=1)]
[name="巡林者"]哈哈哈......也许是这样。
[name="巡林者"]很荣幸和你并肩作战，亚历山大。
[character(name="char_503_rang",name2="char_459_tachak_1#2",focus=2)]
[name="战车"]我也很荣幸，巡林者。
[name="战车"]不要这么悲观，我还没有放弃战斗。
[name="战车"]我就是用砸的，也要敲死几个。
[dialog]
[character]
[delay(time=0.51)]
[PlaySound(key="$p_imp_arrow_h", volume=1)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[delay(time=1)]
[character(name="char_503_rang")]
[name="巡林者"]等等......那是什么。
[Dialog]
[Character]
[stopmusic(fadetime=1)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=tr

... (全文8024字符)
```

### level_act17d0_st01

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_labcorridor")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[Character(name="char_empty")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="middle", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_456_ash_1#1",fadetime=0.7)]
[delay(time=2)]
[name="灰烬"]我们已进入磁山二号，重复一遍，我们已进入磁山二号。
[name="灰烬"]双月、艾拉，你们那边情况如何？完毕。
[dialog]
[delay(time=1)]
[Character(name="char_456_ash_1#1",focus=-1)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1)]
[name="艾拉"]一切照旧，我们很快就能完成收尾。
[name="艾拉"]完毕。
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",volume=0.6)]
[delay(time=1.5)]
[Character(name="char_456_ash_1#9")]
[name="灰烬"]艾拉？
[dialog]
[delay(time=1)]
[Character(name="char_456_ash_1#9",focus=-1)]
[PlaySound(key="$d_gen_transmissionget", volume=1)]
[delay(time=1)]
[name="艾拉"]双月，准备接敌！
[name="双月"]已就位！
[name="双月"]复制器已开启！
[name="艾拉"]地雷部署！
[name="艾拉"]如果情报无误，这就是最后一批了！
[name="艾拉"]我们处理完毕后就向你们靠拢！
[dialog]
[delay(time=1)]
[CameraShake(duration=0.5, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n",volume=0.6)]
[delay(time=1.5)]
[name="艾拉"]Gówno！
[name="艾拉"]艾拉通讯完毕！
[PlaySound(key="$transmission", volume=1)]
[delay(time=1)]
[Character(name="char_456_ash_1#1")]
[name="灰烬"]情况就是这样。
[dialog]
[character]
[delay(time=1)]
[PlayMusic(intro="$suspenseful_intro", key="$suspenseful_loop", volume=0.4)]
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#1",focus=1)]
[name="闪击"]放心交给波兰人吧。
[name="闪击"]我已经听到雷电地雷触发的声音了，她们会没事的。
[character(name="char_457_blitz_1#4", name2="char_456_ash_1#1",focus=2)]
[name="灰烬"]而你，闪击，把注意力放回警戒上。
[character(name="char_457_blitz_1#6", name2="char_456_ash_1#1",focus=1)]
[name="闪击"]听你的，女士。
[character(name="char_457_blitz_1#6", name2="char_456_ash_1#1",focus=2)]
[name="灰烬"]注意仪表读数，情报显示这个建筑物里有封存的核废料。
[dialog]
[delay(time=1)]
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=1)]
[name="灰烬"]霜华，我们离目标还有多远？
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=2)]
[name="霜华"]穿过前面的检查站和材料储藏室，就是主实验室。
[name="霜华"]无人机显示雇佣兵在检查站及周边建造了简易工事 。
[name="霜华"]没有掩体，没有死角，入口位置堵死，周边布设了大量铁丝网。
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=1)]
[name="灰烬"]人数。
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=2)]
[name="霜华"]九人，大致位置已标记在了小队的终端上。
[name="霜华"]检查站进入储藏室的长廊入口完全封死了，无人机无法进一步深入。
[name="霜华"]汇报完毕。
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=1)]
[name="灰烬"]还有其他入口吗？
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=2)]
[name="霜华"]没有看到入口。
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=1)]
[name="灰烬"]好，我会解决。
[dialog]
[delay(time=1)]
[character(name="char_459_tachak_1", name2="char_456_ash_1#1",focus=2)]
[name="灰烬"]有什么建议吗，Lord？
[character(name="char_459_tachak_1", name2="char_456_ash_1#1",focus=1)]
[name="战车"]燃烧榴弹还有剩余，你要用几颗？
[character(name="char_459_tachak_1", name2="char_456_ash_1#1",focus=2)]
[name="灰烬"]两发。
[character(name="char_459_tachak_1", name2="char_456_ash_1#1",focus=1)]
[name="战车"]了解。
[dialog]
[character]
[delay(time=1)]
[Character(name="char_456_ash_1#1")]
[name="灰烬"]检查站入口的阻塞太庞杂了，如果爆破，瓦砾会对突入造成很大影响。
[name="灰烬"]我的计划是炸开墙体上方和右侧的墙面，一个人挂绳在上方提供火力压制，剩余人员从右侧缺口突入。
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=1)]
[name="灰烬"]霜华，压制和支援交给你来办。
[character(name="char_456_ash_1#1", name2="char_458_rfrost_1#3",focus=2)]
[name="霜华"]收到。
[Character(name="char_456_ash_1#1")]
[name="灰烬"]贴片炸药爆炸后，战车，你从上方缺口抛射榴弹，其他人按照标识位置投掷闪光弹。
[name="灰烬"]地面突入按照闪击、灰烬、战车的顺序来，行动要紧凑，不留可趁之机。
[name="灰烬"]有问题就现在提出。
[dialog]
[delay(time=1)]
[Character(name="char_456_ash_1#1")]
[name="灰烬"]都确认了？那好，各自就位。
[name="灰烬"]霜华，等你的信号，然后我们开始行动。
[dialog]
[character]
[character(name="char_458_rfrost_1#3")]
[name="霜华"]正在前往预定位置。
[name="霜华"]贴片炸药部署完毕。
[character(name="char_457_blitz_1#4")]
[name="闪击"]炸药部署完毕。
[Character(name="char_456_ash_1#2")]
[name="灰烬"]准备——
[dialog]
[delay(time=0.7)]
[stopmusic(fadetime=0)]
[CameraShake(duration=1, ystrength=40, vibrato=30, randomness=90, fadeout=true, block=false)]
[PlaySound(key="$d_gen_explo_n")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.05, block=true)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1.5)]
[PlayMusic(intro="$warchaos_intro", key="$warchaos_loop", volume=0.4)]
[character(name="char_458_rfrost_1#4")]
[name="霜华"]闪光弹！
[dialog]
[delay(time=0.7)]
[PlaySound(key="$explolarge1")]
[Blocker(a=0, r=255, g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255, g=255, b=255, fadetime=0.03, block=true)]
[delay(time=0.51)]
[Blocker(a=0, r=255, g=255, b=255, fadetime=1, block=true)]
[delay(time=1.5)]
[character(name="char_459_tachak_1", name2="char_456_ash_1#2",focus=1)]
[name="战车"]榴弹已射出！！
[character(name="char_459_tachak_1", name2="char_456_ash_1#2",focus=2)]
[name="灰烬"]突入！突入！突入！！！
[dialog]
[character]
[delay(time=1)]
[character(name="char_458_rfrost_1#3")]
[delay(time=0.6)]
[PlaySound(key="$staplegun_n",volume=1)]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[name="霜华"]敌人倒下！
[Character(name="char_456_ash_1#2")]
[name="灰烬"]闪击，两点钟方向！
[dialog]
[character]
[delay(time=0.6)]
[character(name="char_457_blitz_1#4")]
[playsound(key="$sheildimpact")]
[CameraShake(duration=0.3, xstrength=30, ystrength=30, vibrato=30, randomness=90, fadeout=true, block=false)]
[delay(time=1)]
[PlaySound(key="$staplegun_n",volume=1)]
[CameraSha

... (全文28159字符)
```

### level_act17d0_st02

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_desert_1")]
[Delay(time=1)]
[PlayMusic(intro="$loneliness_intro", key="$loneliness_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=2)]
[name="感染者老人"]（萨尔贡语）......他已归去，抛弃世间琐事。
[name="感染者老人"]（萨尔贡语）我们痛心疾首，只因命运不曾公正。
[name="感染者老人"]（萨尔贡语）但毋需悲伤，只因他脱离了现实的苦难。
[name="感染者老人"]（萨尔贡语）我们应当为他高歌，他最终回归了大地。
[name="感染者老人"]（萨尔贡语）他的亲友，他所爱之人，都不应留下泪水。
[name="感染者老人"]（萨尔贡语）死亡是大地的仁慈，我们本是万物的子嗣。
[name="感染者老人"]（萨尔贡语）......让一切化为尘土。
[name="感染者老人"]（萨尔贡语）......让一切归于荒野。
[name="感染者老人"]（萨尔贡语）......我们也终将归去。
[dialog]
[character]
[delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=0.6, r=0, g=0, b=0, fadetime=0.5, block=true)]
[Subtitle(text="在枯木的阴影下，立着一块粗糙打磨的石碑，石碑不光滑的表面上雕刻着几行字。", x=300, y=370, alignment="left", size=24, delay=0.04, width=700)]
[Subtitle(text="“这里长眠着我们的朋友，米亚罗。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“他是一位感染者。他是一位医生。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[Subtitle(text="“他是个好人。”", x=300, y=370, alignment="center", size=24, delay=0.04, width=700)]
[subtitle]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0.5, block=true)]
[delay(time=1)]
[character(name2="char_456_ash_1#8")]
[name="灰烬"]......
[Dialog]
[Character(name="char_empty", name2="char_456_ash_1#8")]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="left", type="move", xpos=-200, fadetime=0.3, block=true)]
[delay(time=0.51)]
[characteraction(name="left", type="move", xpos=200, fadetime=1, block=false)]
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",fadetime=0.7)]
[delay(time=1.5)]
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=1)]
[name="战车"]你还好吗？
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=2)]
[name="灰烬"]......我很难说。
[Character(name="char_459_tachak_1")]
[name="战车"]我听那位蜥蜴老爷子说，在这个国家，只有身份显赫的人才会举办葬礼。
[name="战车"]大部分普通人死了就死了，他们会被家人简单地埋葬在荒地上，没有墓碑，也没有悼念。
[name="战车"]大多数生活在巨型平台——移动城市上的人会把死者的骨灰埋在城市的必经之路上，因为城市的空间非常宝贵，极少有安置死者的空间。
[name="战车"]那些普通的聚落里也少见墓地这种东西，一场要命的灾害席卷而过，就没人找得到逝去的人埋在哪儿了。
[name="战车"]萨尔贡几乎没有宗教，这里的大部分人不太相信死亡之后的世界，他们认为死者会回归大地，成为这个世界的一部分。
[name="战车"]就这个角度来说，这种文化透着坦诚和朴实，我还挺喜欢的。
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=2)]
[name="灰烬"]米亚罗的墓，以后也会消失不见?
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=1)]
[name="战车"]或许吧，但是我们为他举办了葬礼，这很重要。
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=2)]
[name="灰烬"]我不是很能接受。
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=1)]
[name="战车"]为什么？
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=2)]
[name="灰烬"]在目睹了那样的事情之后，我很难接受他的结局。
[name="灰烬"]我们或许也有责任，亚历山大。
[name="灰烬"]如果没有米亚罗，之前近半年来艰苦跋涉的我们会在这里遭遇更多艰辛。
[name="灰烬"]我一直在想，如果我们当时动作再快一点呢？如果我们强硬一点，坚持要和那些病人们一起行动呢？
[name="灰烬"]如果我们......
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=1)]
[name="战车"]我建议你放弃这种思考方式。
[name="战车"]米亚罗做出了自己的选择，这不是你的错。
[name="战车"]那个大个子姑娘尝试尽职尽责，作为一个生长在这种文化和制度下的贵族，她愿意庇护那些病人，无疑也是高尚的行为。
[name="战车"]按照那几位罗德岛干员的说法，米亚罗病得很重。
[name="战车"]对他来说，每天早上太阳是伴随着死亡一起升起的。
[name="战车"]像他那样的病情能够坚持到现在已经是奇迹了。
[name="战车"]这就是他们的生活，我们能做的事情不多。
[Character(name="char_456_ash_1#8")]
[name="灰烬"]但是我们真的做对了吗？
[delay(time=1)]
[name="灰烬"]我们想当然地对他们伸出了援手，我们想当然地“帮助”了他们。
[name="灰烬"]我不知道我为什么会如此自信，觉得我能够“帮助”他们。
[name="灰烬"]我们和这些病人生活在一起。
[name="灰烬"]但是我们根本不了解感染者，我们想当然地把“矿石病”当做略带感染性的癌症，当做我们熟悉的那些无法治愈的绝症。
[name="灰烬"]但是这根本不是一种疾病......这是灾难。
[name="灰烬"]我们对此一无所知，却尝试拯救他们。
[dialog]
[character]
[delay(time=1)]
[Character(name="char_459_tachak_1")]
[name="战车"]你不该无端指责自己，科恩。
[name="战车"]这样没有意义。
[name="战车"]我理解你现在的心情。
[name="战车"]但是你不能否定我们做的事情。
[name="战车"]还记得我在屋顶上的无所事事吗？我有大把大把的时间。
[name="战车"]我坐在那里，看着米亚罗的诊所，看着居住在这里的人。
[name="战车"]以异世界来客的身份，我见证着这个世界。
[name="战车"]我不是个敏锐的人，但是即便如此我也能看到很多事情，那些不堪的，残忍的事情。
[name="战车"]有一天晚上，一个镇民在夜色的掩护下，从另一个居民的家里抬出来一件包裹。
[name="战车"]那是一个用麻袋扎得严严实实的，一人高的包裹。
[character(name="char_456_ash_1#8")]
[name="灰烬"]......
[Character(name="char_459_tachak_1")]
[name="战车"]我看到他们把麻袋抬上了板车，一路沿着小镇的边缘走向戈壁滩，消失在南边的那块巨石后面。
[name="战车"]我看到了好几次同样的事情。过去三周里大概有过两次。在我没看到的地方，一定还发生过更多。
[character(name="char_456_ash_1#8")]
[name="灰烬"]你之前从来没有说过这件事。
[Character(name="char_459_tachak_1")]
[name="战车"]我不想说，我觉得没有必要。
[name="战车"]你说得没错，我们是外人，不是这个国家的居民。就像我刚才的描述，我们对他们而言甚至是异世界人。
[name="战车"]我不了解他们。他们的历史、他们的文化、他们的生活，他们的喜怒哀乐，我都不了解。
[name="战车"]我没有权利对我不了解的东西指指点点，他们无论做什么都有他们的理由。
[name="战车"]事情本该如此。
[name="战车"]但是后来有一天晚上，也许是我的好奇心击败了我的理智，我沿着那条路，走到了他们埋藏麻袋的巨石后面。
[name="战车"]我看到沙土之下闪烁着光芒，我看到闪耀的粉尘从沙砾中升腾，最终消散在空气中。
[name="战车"]在夜色中，那些粉尘如此耀眼。
[name="战车"]麻袋里装着什么，我当然知道。那些粉尘是什么，我多半也能猜到。
[name="战车"]当然，现在我们都知道那些粉尘是什么了。
[name="战车"]那家抬出麻袋的屋子，门口经常坐着一个老妇人。那天晚上之后，那位老妇人再也没有出现。
[name="战车"]库兹每天都和这些镇民待在一起，他一定也知道。
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=2)]
[name="灰烬"]（叹气）
[name="灰烬"]你之前编了个什么借口......人人都像是受过防化学战训练？懂得保护口鼻？这理由真烂。
[Character(name="char_459_tachak_1", name2="char_456_ash_1#8",focus=1)]
[name="战车"]因为我见过原因。
[dialog]
[delay(time=1)]
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character]
[Image(image="avg_ac17_9",screenadapt="coverall", fadetime=0)]
[Blocker(a=0, fadetime=1, block=true)]
[Delay(time=1)]
[name="战车"]你刚才问我“我们真的做对了吗？”
[name="战车"]答案很简单，我们帮助他们，只是因为我们的道德与良知。
[name="战车"]生老病死是不可阻挡的事情，无论是这个世界还是我们的世界。
[name="战车"]就算是没有这种“矿石病”，这些穷困的人们要面对的痛苦也不会减少。
[name="战车"]就算是没有这种病，战争、苛税、自然灾害依然会带走那些可怜人。
[name="战车"]看看他们的领主，看看这个镇子，他们活在什么样的社会里？
[name="战车"]这种样貌的封建在我们熟悉的地球里已经早就落后于时代，但这是他们的现实。
[name="战车"]按我们的标准，他们不算是活在一个文明的世界里。
[name="战车"]这些年我见识过的混账事情够多了，科恩。你知道我指的是什么。
[name="战车"]这世界烂透了，但是我们并非什么都做不到。
[name="战车"]不要否定善行，道德和良知永远不会错。
[dialog]
[delay(time=1)]
[name="灰烬"]......唉。
[name="灰烬"]你是对的，亚历山大。
[name="灰烬"]忘掉我的蠢话吧，我应该是太累了。
[name="战车"]你确实太久没休息了。
[name="战车"]我们都累了。
[dialog]
[Blocker(a=0, r=0,g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0,g=0, b=0, fadetime=1, block=true)]
[Character(name="char_459_tachak_1")]
[Im

... (全文12812字符)
```

### level_act17d0_st03

```
[HEADER(key="title_test", is_skippable=true, fit_mode="BLACK_MASK")]
[Blocker(a=1, r=0, g=0, b=0, fadetime=0, block=true)]
[stopmusic]
[Dialog]
[Background(image="bg_nobleD")]
[Delay(time=1)]
[PlayMusic(intro="$storyendjp_intro", key="$storyendjp_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=1, block=true)]
[delay(time=1.5)]
半个月后
[delay(time=1)]
[dialog]
[delay(time=1)]
[character(name="avg_npc_159_1#1")]
[name="皮加尔"]感谢你们的付出，科恩、库兹、蒂娜、亚历山大。
[name="皮加尔"]我谨代表......长泉镇的......
[name="皮加尔"]抱歉，我还不太擅长使用这种措辞和人说话。
[name="皮加尔"]多亏了你们，我才能从弟弟手里活下来，我的领民也能重新回到自己的土地上生活。
[name="皮加尔"]谢谢。
[Character(name="char_456_ash_1#5")]
[name="灰烬"]这只是我们应该做的。
[name="灰烬"]我们引发了这场危机，所以我们有义务将其终结。
[character(name="avg_npc_159_1#1")]
[name="皮加尔"]如果不是我那无可救药的弟弟，一切都不会发生。
[name="皮加尔"]我本想为你们准备报酬的。
[name="皮加尔"]但是，如你们所见，整个长泉镇已经毁了。
[name="皮加尔"]剩下的资产，我想全部投入到镇子的复兴上。
[name="皮加尔"]现金酬劳......可能没法支付给你们。
[character(name="avg_npc_159_1#3")]
[name="皮加尔"]但这座房子里，只要有你们想要的东西，尽管拿。
[name="皮加尔"]最好把它全拆了搬走，这样我就能和活下来的人一起建造新的长泉。
[Character(name="char_456_ash_1#5")]
[name="灰烬"]关于这一点。
[name="灰烬"]亚历山大？
[Character(name="char_459_tachak_1")]
[name="战车"]这头盔挺合身的，我能留着么。
[Character(name="char_457_blitz_1#6",name2="char_458_rfrost_1#1",focus=2)]
[name="霜华"]嗯哼。
[Character(name="char_457_blitz_1#5",name2="char_458_rfrost_1#1",focus=1)]
[name="闪击"]的确，甲片亮到能闪瞎眼睛，我想给盾上也安一个，以后就用不着电池了。
[Character(name="char_456_ash_1#5")]
[name="灰烬"]这件事情的结果，我们都很满意，已经足够了。
[character(name="avg_npc_159_1#1")]
[name="皮加尔"]这，不需要更多的吗？
[name="皮加尔"]我的武器、父亲的其他收藏，你们都可以——
[Character(name="char_456_ash_1#5")]
[name="灰烬"]不用这么客气，你或许更需要这些东西。
[character(name="avg_npc_159_1#1")]
[name="皮加尔"]......
[character(name="avg_npc_159_1#3")]
[name="皮加尔"]谢谢你们。
[dialog]
[character]
[delay(time=1)]
[Character(name="char_456_ash_1#5")]
[name="灰烬"]走吧各位，我们该离开了。
[Dialog]
[delay(time=0.7)]
[PlaySound(key="$d_gen_walk_n", volume=1)]
[characteraction(name="middle", type="move", xpos=-300, fadetime=2,block=false)]
[Character(fadetime=0.5)]
[delay(time=1)]
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Background(image="bg_desert_1")]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[Character(name="avg_npc_156_1#1",name2="avg_npc_155_1#2",focus=1)]
[name="雷蛇"]库兹先生，各位。
[Character(name="avg_npc_156_1#1",name2="avg_npc_155_1#2",focus=2)]
[name="芙兰卡"]你们终于出来了。
[character(name="avg_npc_166")]
[name="黑"]......
[character(name="char_503_rang")]
[name="巡林者"]和领主小姐道别完了吧。
[name="巡林者"]那我们也该离开这里了。
[character(name="avg_npc_167",name2="char_503_rang",focus=1)]
[name="stormeye"]我的小队会护送你们回岛。
[character(name="avg_npc_167",name2="char_503_rang",focus=2)]
[name="巡林者"]有劳了。
[dialog]
[character]
[delay(time=1)]
[character(name="avg_npc_167",name2="char_456_ash_1#1",focus=1)]
[name="stormeye"]科恩小姐，您的小队将会与我们同行，对吗？
[character(name="avg_npc_167",name2="char_456_ash_1#1",focus=2)]
[name="灰烬"]是，我和我的队员已经战斗太久了，他们需要一个能够休息和进行补给的地方。
[name="灰烬"]最重要的，我们可能需要身份。
[name="灰烬"]一个行走在这个世界……不，行走在这片“大地”上的身份。
[character(name="avg_npc_167",name2="char_456_ash_1#1",focus=1)]
[name="stormeye"]好。
[character(name="avg_npc_167")]
[name="stormeye"]车已经就位了，我们出发。
[Dialog]
[stopmusic(fadetime=2)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character(name="char_016_medic")]
[Background(image="bg_corridor")]
[Delay(time=1)]
[PlayMusic(intro="$farce_intro", key="$farce_loop", volume=0.4)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="人事干员"]各位的信息已经录入罗德岛终端了，以后可以在大地各处的罗德岛办事处或安全屋进行逗留与补给。
[name="人事干员"]虽然各位并非罗德岛的正式雇员，但任务网络已向各位开放，各位可以通过承接任务来获得报酬。
[name="人事干员"]大致情况就是这样，各位还有什么想要知道的吗？
[Character(name="char_457_blitz_1#5")]
[name="闪击"]稍等，我能问一问，罗德岛上有哪儿能看到科幻小说吗？
[Character(name="char_016_medic")]
[name="人事干员"]什么？？
[Dialog]
[Blocker(a=0, r=0, g=0, b=0, fadetime=0, block=true)]
[Blocker(a=1, r=0, g=0, b=0, fadetime=2, block=true)]
[Character]
[Image(image="avg_ac17_13", fadetime=0)]
[ImageTween(xScaleFrom=1.1, yScaleFrom=1.1, xScaleTo=1, yScaleTo=1, duration=15, block=false)]
[Delay(time=1)]
[Blocker(a=0, r=0, g=0, b=0, fadetime=2, block=true)]
[Delay(time=2)]
[name="战车"]所以，这就是我们的新身份。
[name="闪击"]至少我的盾能用了，还不错。
[name="霜华"]有什么计划吗？
[name="灰烬"]尝试去看看这片大地吧，我们对这个世界还了解得太少。
[name="灰烬"]我也希望能有份详尽的计划书。
[name="灰烬"]但这一次，抱歉。
[name="灰烬"]我们只能依靠自己。
[name="闪击"]所以我们的第一个目的地是哪？
[name="灰烬"]有一个叫汐斯塔的地方，听起来是个很不错的城市。
[name="战车"]那就走吧。
[name="战车"]在回到家之前，我们终究还在路上。
[Dialog]
[playsound(key="$d_gen_walk_n")]
[Blocker(a=0, r=255,g=255, b=255, fadetime=0, block=true)]
[Blocker(a=1, r=255,g=255, b=255, fadetime=1, block=true)]
[stopmusic(fadetime=1)]
[Character]
[Image]
```

### training_act17d0_01_a

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17d0教学关_a

[PopupDialog(dialogHead="$avatar_tachak")] 该死，这片区域根本找不到能落脚的地方
[PopupDialog(dialogHead="$avatar_ash")] 没时间抱怨了，前方又是一阵沙尘暴
[PopupDialog(dialogHead="$avatar_blitz")] 至少从沙尘暴这点上，还是我们熟悉的地球
[PopupDialog(dialogHead="$avatar_blitz")] 除了这里的生物个头也太大了。

[PopupDialog(dialogHead="$avatar_ash")] 大家注意保持距离，不要暴露在沙尘暴下。
[PopupDialog(dialogHead="$avatar_ash")] 暴露在沙尘暴下，只会进一步损坏我们的武器导致<@tu.imp>攻击力降低</>，还会快速<@tu.imp>消耗生命值</>。一旦生命值耗尽，再次部署出击的时间将<@tu.imp>大幅提升</>。
[Tutorial(focusX=-159, focusY=138, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_ash", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
寻找掩体，动作快！那些<@tu.kw>土石结构</>可以<@tu.kw>抵挡沙尘暴</>。
[Tutorial(focusX=163, focusY=136, focusWidth=566, focusHeight=150, \
          animStyle="Highlight", focusStyle="HighlightRect", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_ash", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
土石结构背后的<@tu.kw>一排位置</>应该不会受到沙尘暴的影响。
[Tutorial(focusX=-159, focusY=138, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_rfrost", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
沙尘暴太猛了，这些土石结构看起来坚持不了多久！沙尘暴会<@tu.kw>不断破坏</>土石结构，直到它们被摧毁。
[PopupDialog(dialogHead="$avatar_sys")] 沙尘暴是萨尔贡地区的常见气象灾害，需要想办法规避。
[PopupDialog(dialogHead="$avatar_sys")] 穿越荒地的旅行者可以尝试寻找体积较大的土石结构<@tu.kw>躲避</>沙尘暴。
[Tutorial(focusX=-159, focusY=138, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
但是土石结构并<@tu.kw>不牢固</>，会在沙尘暴的侵蚀下逐渐坍塌。
[Tutorial(focusX=61, focusY=-50, focusWidth=140, focusHeight=140, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_sys", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
使用<@tu.kw>加固装置</>强化附近的土石结构，形成牢固的屏障。



```

### training_act17d0_01_b

```
[HEADER(is_skippable=true, is_autoable=false)] 活动17d0教学关_b

[Tutorial(focusX=-348, focusY=222, focusWidth=125, focusHeight=125, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_blitz", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
又来了，石头螃蟹，还不止一只！

[PopupDialog(dialogHead="$avatar_rfrost")] 闪击！后退！注意避开沙尘暴！
[Tutorial(focusX=-348, focusY=222, focusWidth=125, focusHeight=125, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_blitz", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
等等，这些螃蟹在沙尘暴中似乎也受影响。看起来这些沙尘暴会<@tu.kw>降低敌人的移动速度</>。
[Tutorial(focusX=-46, focusY=209, focusWidth=125, focusHeight=125, \
          animStyle="Highlight", focusStyle="HighlightCircle", black="$f_tut_black", \
          protectTime=0.5, dialogHead="$avatar_ash", dialogX="$f_lower_dialog_pos_x", dialogY="$f_lower_dialog_pos_y")] \
闪击，看到那些<@tu.kw>地穴</>了吗？这些铁螃蟹虽然够硬，但是看起来不是很聪明的样子，把他们吸引到那里。但是注意你自己的脚下！
[PopupDialog(dialogHead="$avatar_blitz")] 行吧，看起来是一种选择。

```


## 统计

- 总字符数：262661
- 对话行数：2485


## 策划参考价值
塔防策略RPG的完整剧情脚本格式。含演出指令(BGM/立绘/特效)和对话文本的混合格式。
